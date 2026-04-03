"""Модели подкастов."""

from datetime import date
from typing import Any, Literal

from pydantic import model_validator

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

    @model_validator(mode="before")
    @classmethod
    def validate_not_available(cls, data: dict[str, Any]) -> dict[str, Any]:
        """Убеждаемся, что это действительно недоступный трек."""
        # Если трек доступен и это не подкаст-эпизод — не используем эту модель
        if data.get("available") is True and data.get("type") != "podcast-episode":
            raise ValueError(
                f"Available track {data.get('id')} should not be UnavailablePodcast",
            )
        return data


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
