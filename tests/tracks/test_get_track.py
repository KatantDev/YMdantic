import asyncio
import secrets

import pytest
from ymdantic import YMClient
from ymdantic.exceptions import YMTrackNotFoundError
from ymdantic.models import Podcast, Track, UnavailablePodcast, UnavailableTrack


@pytest.mark.anyio
async def test_get_available_track(client: YMClient) -> None:
    result = await client.get_track(track_id=83313323)
    assert result.type == "music"
    assert result.available is True
    assert isinstance(result, Track)


@pytest.mark.anyio
async def test_get_unavailable_track(client: YMClient) -> None:
    result = await client.get_track(track_id=83313324)
    assert result.type == "music"
    assert result.available is False
    assert isinstance(result, UnavailableTrack)


@pytest.mark.anyio
async def test_get_available_podcast(client: YMClient) -> None:
    result = await client.get_track(track_id=133991955)
    assert result.type == "podcast-episode"
    assert result.available is True
    assert isinstance(result, Podcast)


@pytest.mark.anyio
async def test_get_unavailable_podcast(client: YMClient) -> None:
    result = await client.get_track(track_id=133991956)
    assert result.type == "music"
    assert result.available is False
    assert isinstance(result, UnavailablePodcast)


@pytest.mark.anyio
async def test_get_not_found_track(client: YMClient) -> None:
    with pytest.raises(YMTrackNotFoundError):
        await client.get_track(track_id=2000000000)


@pytest.mark.anyio
async def test_get_random_tracks(client: YMClient) -> None:
    track_ids = [secrets.randbelow(140_000_000) for _ in range(50)]
    results = await asyncio.gather(
        *[client.get_track(track_id=track_id) for track_id in track_ids],
        return_exceptions=True,
    )
    error_results = [
        result
        for result in results
        if isinstance(result, BaseException)
        and not isinstance(result, YMTrackNotFoundError)
    ]
    assert len(error_results) == 0
