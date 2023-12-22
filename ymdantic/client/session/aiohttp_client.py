import asyncio
import ssl
import urllib.parse
from contextlib import asynccontextmanager
from typing import Optional, Any, Type, Dict, AsyncIterator

import certifi
from aiohttp import ClientSession, FormData, ClientError, ClientTimeout, TCPConnector
from dataclass_rest.base_client import BaseClient
from dataclass_rest.exceptions import ClientLibraryError
from dataclass_rest.http_request import HttpRequest

from ymdantic.client.session.aiohttp_method import YMHttpMethod


class AiohttpClient(BaseClient):
    method_class = YMHttpMethod

    def __init__(
            self,
            base_url: str,
            headers: Optional[Dict[str, Any]] = None,
            timeout: Optional[ClientTimeout] = None,
    ):
        super().__init__()
        self.base_url = base_url
        self.headers = headers or {}
        self.timeout: ClientTimeout = timeout or ClientTimeout(total=0)

        self._session: Optional[ClientSession] = None
        self._connector_type: Type[TCPConnector] = TCPConnector
        self._connector_init: Dict[str, Any] = {
            "ssl": ssl.create_default_context(cafile=certifi.where()),
        }

    @asynccontextmanager
    async def context(self, auto_close: bool = True) -> AsyncIterator["AiohttpClient"]:
        """
        Контекстный менеджер для работы с клиентом

        :param auto_close: Автоматически закрывать сессию после выполнения.
        :yields: клиент
        """
        try:
            yield self
        finally:
            if auto_close:
                await self._session.close()

    async def get_session(self) -> ClientSession:
        if self._session is None or self._session.closed:
            self._session = ClientSession(
                connector=self._connector_type(**self._connector_init),
                headers=self.headers,
            )

        return self._session

    async def close(self) -> None:
        if self._session and not self._session.closed:
            await self._session.close()

            await asyncio.sleep(0.25)

    async def do_request(self, request: HttpRequest) -> Any:
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
                    filename=file.filename, content_type=file.content_type,
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

    def __del__(self):
        if self._session and not self._session.closed:
            if self._session.connector is not None and self._session.connector_owner:
                self._session.connector.close()
            self._session._connector = None
