import pytest
from ymdantic import YMClient
from ymdantic.models.tracks.file_info import FileInfo


@pytest.mark.anyio
async def test_get_available_track_file_info_nq(client: YMClient) -> None:
    track_id = 83313323

    result = await client.get_track_file_info(track_id=track_id)
    assert isinstance(result, FileInfo)
    assert result.quality == "nq"


@pytest.mark.anyio
async def test_get_available_track_file_info_lossless(client: YMClient) -> None:
    track_id = 117708948

    result = await client.get_track_file_info(track_id=track_id)
    assert isinstance(result, FileInfo)
    assert result.quality == "lossless"
