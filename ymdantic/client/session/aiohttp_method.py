from json import JSONDecodeError
from logging import getLogger
from typing import Any

from aiohttp import ClientError, ClientResponse
from dataclass_rest.exceptions import ClientLibraryError, MalformedResponse
from dataclass_rest.http.aiohttp import AiohttpMethod
from dataclass_rest.http_request import HttpRequest

from ymdantic.exceptions import YMError
from ymdantic.exceptions.custom_exceptions import YMTrackNotFoundError
from ymdantic.models.error import YandexMusicErrorModel

logger = getLogger(__name__)

ERROR_STATUS_CODES = range(400, 600)


def exclude_none(params: dict[str, Any]) -> dict[str, Any]:
    """
    Удаление элементов из словаря в которых значение равно None.

    :param params: Исходный словарь.
    :return: Словарь без пустых значений.
    """
    return {k: v for k, v in params.items() if v is not None}


class YMHttpMethod(AiohttpMethod):
    """Метод для преобразования запроса и ответа в нужный вид."""

    async def _pre_process_request(self, request: HttpRequest) -> HttpRequest:
        """
        Этот метод используется для предварительной обработки запроса.

        Достаем параметры запроса и очищаем поля в которых значения равны None.

        :param request: Запрос для сервера.
        :return: Обработанное тело запроса.
        """
        request.query_params = exclude_none(request.query_params)
        return request

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
        YMError с этой информацией.

        :param response: Объект ClientResponse, содержащий ответ от сервера.
        :raises YMError: Если статус ответа от 400 до 500.
        """
        response_json = await response.json()
        if response.status in ERROR_STATUS_CODES:
            result = response_json.get("result", {})
            raise YMError(
                error=YandexMusicErrorModel(
                    name=result.get("name", "unknown-error"),
                    message=result.get("message") or str(response_json),
                ),
            )

    async def _response_body(self, response: ClientResponse) -> Any:
        """
        Этот метод используется для обработки тела ответа.

        Он пытается извлечь JSON из ответа и обрабатывает его в зависимости от
        содержимого.
        Если в ответе есть ошибка "not-found", вызывается исключение YMError.
        Если результатов много, то возвращается список результатов без ошибок.

        :param response: Объект ClientResponse, содержащий ответ от сервера.
        :raises YMError: Если в ответе есть ошибка "not-found".
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
                raise YMError(
                    error=YandexMusicErrorModel(name="not-found", message=""),
                )
            if isinstance(response_json["result"], list):
                response_json["result"] = [
                    result
                    for result in response_json["result"]
                    if result.get("error") != "not-found"
                ]
            if not response_json["result"]:
                raise YMTrackNotFoundError
            return response_json
        except ClientError as e:
            raise ClientLibraryError from e
        except JSONDecodeError as e:
            raise MalformedResponse from e
