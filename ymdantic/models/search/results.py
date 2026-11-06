from typing import Annotated, Any, ClassVar, Literal

from pydantic import Discriminator, Tag

from ymdantic.models import Artist, ShortAlbum
from ymdantic.models.base import YMBaseModel
from ymdantic.models.clips.clip import Clip
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
    """Результат поиска эпизода подкаста или главы аудиокниги."""

    type: Literal["podcast_episode"]
    # Тип результата.
    podcast_episode: Podcast
    # Эпизод подкаста.


class PodcastAlbumSearchResult(YMBaseModel):
    """Результат поиска подкаста или аудиокниги целиком."""

    type: Literal["podcast"]
    # Тип результата.
    podcast: ShortAlbum
    # Подкаст: альбом с мета-типом "podcast".


class PlaylistSearchResult(YMBaseModel):
    """Результат поиска плейлиста."""

    type: Literal["playlist"]
    # Тип результата.
    playlist: BasePlaylist
    # Плейлист.


class ClipSearchResult(YMBaseModel):
    """Результат поиска клипа."""

    type: Literal["clip"]
    # Тип результата.
    clip: Clip
    # Клип.


class UnknownSearchResult(YMBaseModel):
    """
    Результат поиска типа, для которого ещё нет модели.

    Яндекс добавляет в выдачу новые типы, и без этой модели один такой
    результат ломал бы разбор всего ответа. Данные результата лежат в
    model_extra.
    """

    KNOWN_TYPES: ClassVar[frozenset[str]] = frozenset(
        {"track", "artist", "album", "podcast_episode", "podcast", "playlist", "clip"},
    )
    # Типы, для которых есть своя модель результата.

    type: str
    # Тип результата.

    @classmethod
    def get_tag(cls, value: Any) -> str:
        """
        Возвращает тег модели, в которую разбирается результат поиска.

        :param value: Сырой результат поиска или уже разобранная модель.
        :return: Тип результата, если для него есть модель, иначе "unknown".
        """
        if isinstance(value, dict):
            result_type = value.get("type")
        else:
            result_type = getattr(value, "type", None)
        if result_type in cls.KNOWN_TYPES:
            return str(result_type)
        return "unknown"


SearchResult = Annotated[
    Annotated[TrackSearchResult, Tag("track")]
    | Annotated[ArtistSearchResult, Tag("artist")]
    | Annotated[AlbumSearchResult, Tag("album")]
    | Annotated[PodcastSearchResult, Tag("podcast_episode")]
    | Annotated[PodcastAlbumSearchResult, Tag("podcast")]
    | Annotated[PlaylistSearchResult, Tag("playlist")]
    | Annotated[ClipSearchResult, Tag("clip")]
    | Annotated[UnknownSearchResult, Tag("unknown")],
    Discriminator(UnknownSearchResult.get_tag),
]
