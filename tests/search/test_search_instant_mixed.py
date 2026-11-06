import pytest
from ymdantic import YMClient
from ymdantic.models.search import SearchInstantMixedResponse
from ymdantic.models.search.results import (
    AlbumSearchResult,
    ArtistSearchResult,
    ClipSearchResult,
    PlaylistSearchResult,
    PodcastAlbumSearchResult,
    PodcastSearchResult,
    TrackSearchResult,
    UnknownSearchResult,
)

XOLIDAYBOY_ARTIST_ID = 10878798


@pytest.mark.anyio
async def test_search_instant_mixed(client: YMClient) -> None:
    response = await client.search_instant_mixed(text="xolidayboy")
    assert response.text == "xolidayboy"
    assert len(response.results) > 0
    assert response.per_page > 0
    assert isinstance(response.search_request_id, str)
    assert isinstance(response.misspell_corrected, bool)


@pytest.mark.anyio
async def test_search_has_artist_result(client: YMClient) -> None:
    response = await client.search_instant_mixed(text="xolidayboy")
    artist_results = [r for r in response.results if isinstance(r, ArtistSearchResult)]
    assert len(artist_results) > 0, (
        "Expected at least one artist result for 'xolidayboy'"
    )
    artist = artist_results[0].artist
    assert artist.id == XOLIDAYBOY_ARTIST_ID
    assert artist.name.lower() == "xolidayboy"


@pytest.mark.anyio
async def test_search_has_track_results(client: YMClient) -> None:
    response = await client.search_instant_mixed(text="xolidayboy")
    track_results = [r for r in response.results if isinstance(r, TrackSearchResult)]
    assert len(track_results) > 0, "Expected at least one track result for 'xolidayboy'"
    for track_result in track_results:
        track = track_result.track
        assert track.id > 0
        assert track.title


@pytest.mark.anyio
async def test_search_result_types(client: YMClient) -> None:
    response = await client.search_instant_mixed(text="xolidayboy")
    for result in response.results:
        assert not isinstance(result, UnknownSearchResult), (
            f"No model for search result type {result.type!r}"
        )


@pytest.mark.anyio
async def test_search_with_filter_artist(client: YMClient) -> None:
    response = await client.search_instant_mixed(
        text="xolidayboy",
        filter="artist",
    )
    assert len(response.results) > 0
    for result in response.results:
        assert isinstance(result, ArtistSearchResult)
        assert result.type == "artist"


@pytest.mark.anyio
async def test_search_with_filter_track(client: YMClient) -> None:
    response = await client.search_instant_mixed(
        text="xolidayboy",
        filter="track",
    )
    assert len(response.results) > 0
    for result in response.results:
        assert isinstance(result, TrackSearchResult)
        assert result.type == "track"


@pytest.mark.anyio
async def test_search_with_filter_album(client: YMClient) -> None:
    response = await client.search_instant_mixed(
        text="xolidayboy",
        filter="album",
    )
    assert len(response.results) > 0
    for result in response.results:
        assert isinstance(result, AlbumSearchResult)
        assert result.type == "album"


@pytest.mark.anyio
async def test_search_filters_present(client: YMClient) -> None:
    response = await client.search_instant_mixed(text="xolidayboy")
    assert len(response.filters) > 0
    for f in response.filters:
        assert f.id
        assert f.display_name


@pytest.mark.anyio
async def test_search_nocorrect(client: YMClient) -> None:
    response = await client.search_instant_mixed(
        text="xolidayboy",
        nocorrect=True,
    )
    assert response.misspell_corrected is False
    assert response.text == "xolidayboy"


@pytest.mark.anyio
async def test_search_with_page_size(client: YMClient) -> None:
    page_size = 5
    response = await client.search_instant_mixed(
        text="xolidayboy",
        page_size=page_size,
    )
    assert response.per_page == page_size
    assert len(response.results) <= page_size


@pytest.mark.anyio
async def test_search_misspelled_query(client: YMClient) -> None:
    response = await client.search_instant_mixed(text="холидейбой")
    assert len(response.results) > 0
    artist_results = [r for r in response.results if isinstance(r, ArtistSearchResult)]
    if artist_results:
        assert any(a.artist.id == XOLIDAYBOY_ARTIST_ID for a in artist_results)


@pytest.mark.anyio
async def test_search_gibberish_returns_no_results(client: YMClient) -> None:
    response = await client.search_instant_mixed(
        text="zzzqqq999xxx888jjj777",
    )
    assert len(response.results) == 0


@pytest.mark.anyio
async def test_search_with_filter_playlist(client: YMClient) -> None:
    response = await client.search_instant_mixed(
        text="xolidayboy",
        filter="playlist",
    )
    assert len(response.results) > 0
    for result in response.results:
        assert isinstance(result, PlaylistSearchResult)


@pytest.mark.anyio
async def test_search_with_filter_podcast(client: YMClient) -> None:
    response = await client.search_instant_mixed(
        text="подкаст",
        filter="podcast",
    )
    assert len(response.results) > 0
    for result in response.results:
        assert isinstance(result, PodcastAlbumSearchResult)
        assert result.podcast.meta_type == "podcast"


@pytest.mark.anyio
async def test_search_with_filter_book(client: YMClient) -> None:
    response = await client.search_instant_mixed(
        text="гарри поттер",
        filter="book",
    )
    assert len(response.results) > 0
    for result in response.results:
        assert isinstance(result, (PodcastAlbumSearchResult, PodcastSearchResult))


@pytest.mark.anyio
async def test_search_with_filter_clip(client: YMClient) -> None:
    response = await client.search_instant_mixed(
        text="xolidayboy",
        filter="clip",
    )
    assert len(response.results) > 0
    for result in response.results:
        assert isinstance(result, ClipSearchResult)
        assert result.clip.title


def test_unknown_result_type_does_not_break_response() -> None:
    response = SearchInstantMixedResponse.model_validate(
        {
            "searchRequestId": "request",
            "text": "xolidayboy",
            "misspellCorrected": False,
            "responseType": "mixed",
            "perPage": 20,
            "lastPage": True,
            "results": [{"type": "concert", "concert": {"id": "1"}}],
        },
    )
    [result] = response.results
    assert isinstance(result, UnknownSearchResult)
    assert result.type == "concert"
    assert result.model_extra == {"concert": {"id": "1"}}
