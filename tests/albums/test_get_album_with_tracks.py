import asyncio
import secrets

import pytest
from ymdantic import YMClient
from ymdantic.exceptions import YMError
from ymdantic.models import Album


@pytest.mark.anyio
async def test_get_available_album_with_tracks(client: YMClient) -> None:
    album_id = 1814060

    result = await client.get_album_with_tracks(album_id=album_id)

    assert result is not None
    assert isinstance(result, Album)
    assert result.meta_type == "music"
    assert result.id == album_id
    assert result.title is not None
    assert result.artists is not None
    assert len(result.artists) > 0
    assert result.track_count > 0
    assert result.volumes is not None
    assert len(result.volumes) > 0
    assert len(result.volumes[0]) > 0


@pytest.mark.anyio
async def test_get_not_found_album_with_tracks(client: YMClient) -> None:
    with pytest.raises(YMError):
        await client.get_album_with_tracks(album_id=181406011111)


async def test_get_available_album_with_podcast(client: YMClient) -> None:
    album_id = 10141723

    result = await client.get_album_with_tracks(album_id=album_id)

    assert result is not None
    assert isinstance(result, Album)
    assert result.meta_type == "podcast"
    assert result.id == album_id
    assert result.title is not None
    assert result.artists is not None
    assert result.track_count > 0
    assert result.volumes is not None
    assert len(result.volumes) > 0
    assert len(result.volumes[0]) > 0


@pytest.mark.anyio
async def test_get_random_album(client: YMClient) -> None:
    album_ids = [secrets.randbelow(140_000_000) for _ in range(50)]
    results = await asyncio.gather(
        *[client.get_album_with_tracks(album_id=album_id) for album_id in album_ids],
        return_exceptions=True,
    )
    error_results = [
        result
        for result in results
        if isinstance(result, BaseException) and not isinstance(result, YMError)
    ]
    assert len(error_results) == 0
