import pytest
from ymdantic import YMClient
from ymdantic.exceptions.custom_exceptions import YMError
from ymdantic.models import DownloadInfoDirect, Track
from ymdantic.models.tracks.download_info import DownloadInfo


@pytest.mark.anyio
async def test_get_available_track_download_info(client: YMClient) -> None:
    track_id = 83313323

    result = await client.get_track_download_info(track_id=track_id)
    assert result is not None
    assert len(result) > 0
    assert all(isinstance(item, DownloadInfo) for item in result)
    assert all(item.download_info_url is not None for item in result)


@pytest.mark.anyio
async def test_get_unavailable_track_download_info(client: YMClient) -> None:
    track_id = 83313324

    with pytest.raises(YMError) as error:
        await client.get_track_download_info(track_id=track_id)
        assert error.value.error.message == "no-rights"


@pytest.mark.anyio
async def test_get_track_download_info_direct(client: YMClient) -> None:
    track_id = 83313323

    result = await client.get_track_download_info_direct(track_id=track_id)
    assert result is not None
    assert len(result) > 0
    assert all(isinstance(item, DownloadInfoDirect) for item in result)
    assert all(item.direct_url is not None for item in result)


@pytest.mark.anyio
async def test_get_download_info_from_track(client: YMClient) -> None:
    track_id = 83313323

    track = await client.get_track(track_id=track_id)
    if not isinstance(track, Track):
        raise AssertionError("Track is not available")

    result = await track.get_download_info_direct()
    assert result is not None
    assert len(result) > 0
    assert all(isinstance(item, DownloadInfoDirect) for item in result)
    assert all(item.direct_url is not None for item in result)
