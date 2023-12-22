from json import JSONDecodeError
from typing import Any

from aiohttp import ClientResponse, ClientError
from dataclass_rest.exceptions import ClientLibraryError, MalformedResponse
from dataclass_rest.http.aiohttp import AiohttpMethod

from ymdantic.exceptions import YandexMusicError
from ymdantic.models.error import YandexMusicErrorModel


class YMHttpMethod(AiohttpMethod):
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
