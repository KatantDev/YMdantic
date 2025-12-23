import asyncio
import secrets
from typing import Type, TypedDict

import pytest
from ymdantic import YMClient
from ymdantic.exceptions.custom_exceptions import YMTrackNotFoundError
from ymdantic.models import Podcast, Track, UnavailablePodcast, UnavailableTrack
from ymdantic.models.tracks.track import BaseTrack


class TrackExpected(TypedDict):
    """Тип, ожидаемый для трека."""

    type: str
    available: bool
    instance_type: Type[BaseTrack]


@pytest.mark.anyio
async def test_get_tracks(client: YMClient) -> None:
    tracks: dict[int, TrackExpected] = {
        83_313_323: {"type": "music", "available": True, "instance_type": Track},
        83_313_324: {
            "type": "music",
            "available": False,
            "instance_type": UnavailableTrack,
        },
        133_991_955: {
            "type": "podcast-episode",
            "available": True,
            "instance_type": Podcast,
        },
        133_991_956: {
            "type": "music",
            "available": False,
            "instance_type": UnavailablePodcast,
        },
    }
    result = await client.get_tracks(track_ids=list(tracks.keys()))
    assert len(result) == len(tracks)
    for track_result, track_expected in zip(result, tracks.values(), strict=True):
        assert track_result.type == track_expected["type"]
        assert track_result.available is track_expected["available"]
        assert isinstance(track_result, track_expected["instance_type"])


@pytest.mark.anyio
async def test_get_not_found_tracks(client: YMClient) -> None:
    with pytest.raises(YMTrackNotFoundError):
        await client.get_tracks(track_ids=[2000000000])


@pytest.mark.anyio
async def test_get_found_and_not_found_tracks(client: YMClient) -> None:
    track_ids = {
        83_313_323: True,
        2_000_000_000: False,
        83_313_324: True,
    }
    available_track_ids = [
        track_id for track_id, available in track_ids.items() if available
    ]

    result = await client.get_tracks(track_ids=list(track_ids.keys()))
    assert len(result) == len(available_track_ids)
    for track_result, track_id in zip(result, available_track_ids, strict=True):
        assert track_result.id == track_id


@pytest.mark.anyio
async def test_get_tracks_with_not_found_track(client: YMClient) -> None:
    track_ids: list[int | str] = [2_000_000_000, 2_000_000_001, 2_000_000_002]
    with pytest.raises(YMTrackNotFoundError):
        await client.get_tracks(track_ids=track_ids)


@pytest.mark.anyio
async def test_get_random_tracks(client: YMClient) -> None:
    track_ids = [[secrets.randbelow(140_000_000) for _ in range(50)] for _ in range(5)]
    results = await asyncio.gather(
        *[client.get_tracks(track_ids=track_ids) for track_ids in track_ids],
        return_exceptions=True,
    )
    error_results = [
        result
        for result in results
        if isinstance(result, BaseException)
        and not isinstance(result, YMTrackNotFoundError)
    ]
    assert len(error_results) == 0
