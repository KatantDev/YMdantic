import asyncio
import urllib.parse
from types import TracebackType
from typing import Any, Optional, Self

from aiohttp import ClientError, ClientSession, ClientTimeout, FormData, TCPConnector
from dataclass_rest.base_client import BaseClient
from dataclass_rest.exceptions import ClientLibraryError
from dataclass_rest.http_request import HttpRequest

from ymdantic.client.session.aiohttp_method import YMHttpMethod


class AiohttpClient(BaseClient):
    """Базовый клиент для работы с API через aiohttp."""

    method_class = YMHttpMethod

    def __init__(
        self,
        base_url: str,
        session: Optional[ClientSession] = None,
        headers: Optional[dict[str, Any]] = None,
        timeout: Optional[ClientTimeout] = None,
        proxy: Optional[str] = None,
    ) -> None:
        super().__init__()
        self.base_url = base_url
        self.headers = headers or {}
        self.proxy = proxy
        self.timeout = timeout

        self._session = session or self._create_session(headers=headers)

    def _create_session(self, headers: dict[str, Any] | None) -> ClientSession:
        """
        Создает ClientSession с учетом прокси.

        Поддерживает HTTP, HTTPS и SOCKS прокси (4, 4a, 5).

        :param headers:
        :return: aiohttp ClientSession.
        """
        if self.proxy is None:
            return ClientSession(
                headers=headers,
                timeout=self.timeout or ClientTimeout(total=0),
            )

        try:
            from aiohttp_socks import ProxyConnector  # noqa: PLC0415
        except ImportError as e:
            raise ImportError(
                "Warning: aiohttp_socks not installed. "
                "SOCKS proxies will not work. "
                "Install with: pip install aiohttp_socks",
            ) from e

        # Определяем тип прокси по схеме
        proxy_lower = self.proxy.lower()

        # SOCKS прокси (поддерживаются socks4, socks4a, socks5, socks5h)
        if any(
            scheme in proxy_lower
            for scheme in ["socks4", "socks5", "socks5h", "socks4a"]
        ):
            # Используем ProxyConnector для SOCKS
            connector = ProxyConnector.from_url(self.proxy)
            return ClientSession(
                connector=connector,
                headers=headers,
                timeout=self.timeout or ClientTimeout(total=0),
            )

        # HTTP/HTTPS прокси
        if proxy_lower.startswith(("http://", "https://")):
            connector = TCPConnector()
            return ClientSession(
                connector=connector,
                proxy=self.proxy,
                headers=headers,
                timeout=self.timeout or ClientTimeout(total=0),
            )

        # Если схема не распознана, предполагаем HTTP
        connector = TCPConnector()
        return ClientSession(
            connector=connector,
            proxy=f"http://{self.proxy}",
            headers=headers,
            timeout=self.timeout or ClientTimeout(total=0),
        )

    async def close(self) -> None:
        """Этот метод используется для закрытия текущей сессии, если она открыта."""
        if self._session and not self._session.closed:
            await self._session.close()
            await asyncio.sleep(0)

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
            async with self._session.request(
                url=urllib.parse.urljoin(self.base_url, request.url),
                method=request.method,
                json=json,
                data=data,
                params=request.query_params,
                headers=request.headers,
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
