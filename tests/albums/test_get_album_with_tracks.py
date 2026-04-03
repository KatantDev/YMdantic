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
