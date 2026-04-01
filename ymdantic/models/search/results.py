from typing import Literal

from ymdantic.models import Artist, ShortAlbum
from ymdantic.models.base import YMBaseModel
from ymdantic.models.playlists import BasePlaylist
from ymdantic.models.tracks import Podcast, Track


class TrackSearchResult(YMBaseModel):
    """Результат поиска трека."""

    type: Literal["track"]
    # Тип результата.
    track: Track
    # Трек.


class ArtistSearchResult(YMBaseModel):
    """Результат поиска артиста."""

    type: Literal["artist"]
    # Тип результата.
    artist: Artist
    # Артист.


class AlbumSearchResult(YMBaseModel):
    """Результат поиска альбома."""

    type: Literal["album"]
    # Тип результата.
    album: ShortAlbum
    # Альбом.


class PodcastSearchResult(YMBaseModel):
    """Результат поиска плейлиста."""

    type: Literal["podcast_episode"]
    # Тип результата.
    podcast_episode: Podcast
    # Эпизод подкаста.


class PlaylistSearchResult(YMBaseModel):
    """Результат поиска плейлиста."""

    type: Literal["playlist"]
    # Тип результата.
    playlist: BasePlaylist
    # Плейлист.


SearchResult = (
    TrackSearchResult
    | ArtistSearchResult
    | AlbumSearchResult
    | PodcastSearchResult
    | PlaylistSearchResult
)
