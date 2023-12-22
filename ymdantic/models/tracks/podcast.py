from datetime import date
from typing import List, Optional, Literal

from ymdantic.models.base import RemoveDeprecated
from ymdantic.models.tracks.track import UnavailableTrack, Track
from ymdantic.models.tracks.track_album import TrackAlbum

PodcastEpisodeType = Literal["full", "bonus", "trailer"]


class UnavailablePodcast(UnavailableTrack, RemoveDeprecated):
    """Pydantic модель, представляющая информацию о недоступном подкасте."""

    type: Literal["music", "comment"]  # type: ignore[assignment]
    # Тип трека. Возможные значения: "music", "comment".
    # (почему-то не "podcast-episode")
    albums: List[TrackAlbum]
    # Список альбомов, в которых присутствует подкаст.
    podcast_episode_type: Optional[PodcastEpisodeType] = None
    # Тип эпизода подкаста (если есть).
    pub_date: Optional[date] = None
    # Дата публикации подкаста (если есть).
    short_description: Optional[str] = None
    # Краткое описание подкаста (если есть).


class Podcast(Track):
    """Pydantic модель, представляющая информацию о подкасте."""

    type: Literal["podcast-episode", "comment"]  # type: ignore[assignment]
    # Тип трека. Возможные значения: "podcast-episode", "comment".
    albums: List[TrackAlbum]
    # Список альбомов, в которых присутствует подкаст.
    podcast_episode_type: Optional[PodcastEpisodeType] = None
    # Тип эпизода подкаста (если есть).
    pub_date: Optional[date] = None
    # Дата публикации подкаста (если есть).
    short_description: Optional[str] = None
    # Краткое описание подкаста (если есть).
