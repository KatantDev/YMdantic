from json import JSONDecodeError
from logging import getLogger
from typing import Any

from aiohttp import ClientResponse, ClientError
from dataclass_rest.exceptions import ClientLibraryError, MalformedResponse
from dataclass_rest.http.aiohttp import AiohttpMethod

from ymdantic.exceptions import YandexMusicError
from ymdantic.models.error import YandexMusicErrorModel

logger = getLogger(__name__)


class YMHttpMethod(AiohttpMethod):
    async def _pre_process_response(self, response: Any) -> Any:
        """
        Этот метод используется для предварительной обработки ответа от сервера.

        Сначала он проверяет, является ли ответ корректным с помощью метода
        `_response_ok`.
        Если ответ не корректен, он вызывает метод `on_error` для
        обработки ошибки.
        Если ответ корректен, он извлекает тело ответа с помощью метода
        `_response_body`.

         Затем он пытается добавить клиента в тело ответа и загрузить тело ответа в
         фабрику тел ответа.

        Если во время этого процесса происходит какая-либо ошибка (ValueError,
        TypeError, AttributeError), он вызывает исключение MalformedResponse.

        :param response: Ответ, полученный от сервера.
        :return: Обработанное тело ответа.
        :raises MalformedResponse: Если во время обработки тела ответа происходит
            ошибка.
        """
        if not await self._response_ok(response):
            return await self.on_error(response)

        body = await self._response_body(response)
        try:
            body["__client"] = self.client
            return self.client.response_body_factory.load(
                body,
                self.method_spec.response_type,
            )
        except (ValueError, TypeError, AttributeError) as e:
            raise MalformedResponse from e

    async def _on_error_default(self, response: ClientResponse) -> None:
        """
        Этот метод вызывается при получении ответа с кодом ошибки от 400 до 500.

        Он пытается извлечь информацию об ошибке из ответа и вызывает исключение
        YandexMusicError с этой информацией.

        :param response: Объект ClientResponse, содержащий ответ от сервера.
        :raises YandexMusicError: Если статус ответа от 400 до 500.
        """
        response_json = await response.json()
        if 400 <= response.status <= 500:
            raise YandexMusicError(
                error=YandexMusicErrorModel.model_validate(
                    response_json.get("error"),
                ),
            )

    async def _response_body(self, response: ClientResponse) -> Any:
        """
        Этот метод используется для обработки тела ответа.

        Он пытается извлечь JSON из ответа и обрабатывает его в зависимости от
        содержимого.
        Если в ответе есть ошибка "not-found", вызывается исключение YandexMusicError.
        Если результатов много, то возвращается список результатов без ошибок.

        :param response: Объект ClientResponse, содержащий ответ от сервера.
        :raises YandexMusicError: Если в ответе есть ошибка "not-found".
        :raises ClientLibraryError: Если происходит ошибка при обработке ответа.
        :raises MalformedResponse: Если ответ не может быть преобразован в JSON.
        :return: Обработанный JSON ответа.
        """
        try:
            response_json = await response.json()
            if response_json.get("result") is None:
                return response_json
            if (
                isinstance(response_json["result"], dict)
                and response_json["result"].get("error") == "not-found"
            ):
                raise YandexMusicError(
                    error=YandexMusicErrorModel(name="not-found", message=""),
                )
            if isinstance(response_json["result"], list):
                response_json["result"] = [
                    result
                    for result in response_json["result"]
                    if result.get("error") != "not-found"
                ]
            if not response_json["result"]:
                raise YandexMusicError(
                    error=YandexMusicErrorModel(name="not-found", message=""),
                )
            return response_json
        except ClientError as e:
            raise ClientLibraryError from e
        except JSONDecodeError as e:
            raise MalformedResponse from e
