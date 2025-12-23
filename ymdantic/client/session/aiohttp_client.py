import asyncio
import ssl
import urllib.parse
from types import TracebackType
from typing import Any, Optional, Self, Type

import certifi
from aiohttp import ClientError, ClientSession, ClientTimeout, FormData, TCPConnector
from dataclass_rest.base_client import BaseClient
from dataclass_rest.exceptions import ClientLibraryError
from dataclass_rest.http_request import HttpRequest

from ymdantic.client.session.aiohttp_method import YMHttpMethod


class AiohttpClient(BaseClient):
    """Базовый клиент для работы с API Яндекс Музыки."""

    method_class = YMHttpMethod

    def __init__(
        self,
        base_url: str,
        headers: Optional[dict[str, Any]] = None,
        timeout: Optional[ClientTimeout] = None,
    ) -> None:
        super().__init__()
        self.base_url = base_url
        self.headers = headers or {}
        self.timeout: ClientTimeout = timeout or ClientTimeout(total=0)

        self._session: Optional[ClientSession] = None
        self._connector_type: Type[TCPConnector] = TCPConnector
        self._connector_init: dict[str, Any] = {
            "ssl": ssl.create_default_context(cafile=certifi.where()),
            "limit": 100,
            "ttl_dns_cache": 3600,
        }

    async def get_session(self) -> ClientSession:
        """
        Этот метод используется для получения текущей сессии.

        Если сессия None или закрыта, он создает новую ClientSession с указанным
        коннектором и заголовками.

        :return: Текущую сессию, если она существует и открыта, в противном случае
            новую сессию.
        """
        if self._session is None or self._session.closed:
            self._session = ClientSession(
                connector=self._connector_type(**self._connector_init),
                headers=self.headers,
            )

        return self._session

    async def close(self) -> None:
        """Этот метод используется для закрытия текущей сессии, если она открыта."""
        if self._session and not self._session.closed:
            await self._session.close()

            await asyncio.sleep(0.25)

    async def do_request(self, request: HttpRequest) -> Any:
        """
        Этот метод используется для выполнения запроса.

        Если запрос является JSON-запросом, данные запроса устанавливаются в json,
        иначе в data.
        Если в запросе есть файлы, они добавляются в FormData.
        Затем выполняется запрос с использованием текущей сессии и возвращается ответ.

        :param request: Объект HttpRequest, содержащий данные запроса.
        :return: Ответ на запрос.
        :raises ClientLibraryError: Если происходит ошибка при выполнении запроса.
        """
        if request.is_json_request:
            json = request.data
            data = None
        else:
            json = None
            data = request.data
        if request.files:
            data = FormData(data or {})
            for name, file in request.files.items():
                data.add_field(
                    name,
                    filename=file.filename,
                    content_type=file.content_type,
                    value=file.contents,
                )
        try:
            session = await self.get_session()
            async with session.request(
                url=urllib.parse.urljoin(self.base_url, request.url),
                method=request.method,
                json=json,
                data=data,
                params=request.query_params,
                timeout=self.timeout,
            ) as response:
                await response.read()
                return response
        except ClientError as e:
            raise ClientLibraryError from e

    async def __aenter__(self) -> Self:
        """Вход в асинхронный контекстный менеджер."""
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Выход из асинхронного контекстного менеджера."""
        await self.close()
