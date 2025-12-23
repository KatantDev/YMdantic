"""Модели подкастов."""

from datetime import date
from typing import Literal

from ymdantic.mixins import DeprecatedMixin
from ymdantic.models.tracks.album import TrackAlbum
from ymdantic.models.tracks.track import Track, UnavailableTrack

PodcastEpisodeType = Literal["full", "bonus", "trailer"]


class UnavailablePodcast(UnavailableTrack, DeprecatedMixin):
    """Модель информации о недоступном подкасте."""

    type: Literal["music", "comment", "podcast-episode"]  # type: ignore[assignment]
    # Тип трека. Возможные значения: "music", "comment".
    # (почему-то не "podcast-episode")
    albums: list[TrackAlbum]
    # Список альбомов, в которых присутствует подкаст.
    podcast_episode_type: PodcastEpisodeType | None = None
    # Тип эпизода подкаста (если есть).
    pub_date: date | None = None
    # Дата публикации подкаста (если есть).
    short_description: str | None = None
    # Краткое описание подкаста (если есть).


class Podcast(Track):
    """Модель информации о доступном подкасте."""

    type: Literal["podcast-episode", "comment"]  # type: ignore[assignment]
    # Тип трека. Возможные значения: "podcast-episode", "comment".
    albums: list[TrackAlbum]
    # Список альбомов, в которых присутствует подкаст.
    podcast_episode_type: PodcastEpisodeType | None = None
    # Тип эпизода подкаста (если есть).
    pub_date: date | None = None
    # Дата публикации подкаста (если есть).
    short_description: str | None = None
    # Краткое описание подкаста (если есть).
