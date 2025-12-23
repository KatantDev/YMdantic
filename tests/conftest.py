import os
from typing import Any, AsyncGenerator

import pytest
from ymdantic import YMClient

TOKEN = os.environ["YM_TOKEN"]


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    """
    Backend for anyio pytest plugin.

    :return: backend name.
    """
    return "asyncio"


@pytest.fixture(scope="session")
async def client(
    anyio_backend: Any,
) -> AsyncGenerator[YMClient, None]:
    """
    Fixture that creates client for requesting server.

    :param anyio_backend: the anyio backend.
    :yield: client for the app.
    """
    async with YMClient(token=TOKEN) as ac:
        yield ac
