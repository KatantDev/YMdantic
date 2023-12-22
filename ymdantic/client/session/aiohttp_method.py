from json import JSONDecodeError
from typing import Any

from aiohttp import ClientResponse, ClientError
from dataclass_rest.exceptions import ClientLibraryError, MalformedResponse
from dataclass_rest.http.aiohttp import AiohttpMethod

from ymdantic.exceptions import YandexMusicError
from ymdantic.models.error import YandexMusicErrorModel


class YMHttpMethod(AiohttpMethod):
    async def _on_error_default(self, response: ClientResponse) -> None:
        response_json = await response.json()
        if 400 <= response.status <= 500:
            raise YandexMusicError(
                error=YandexMusicErrorModel.model_validate(
                    response_json.get("error"),
                ),
            )

    async def _response_body(self, response: ClientResponse) -> Any:
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
