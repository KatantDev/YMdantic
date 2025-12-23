"""Модели лейбла трека."""

from ymdantic.models.base import YMBaseModel


class Major(YMBaseModel):
    """Модель основной информации о лейбле трека."""

    id: int
    # Уникальный идентификатор лейбла.
    name: str
    # Название лейбла.


class PodcastMajor(YMBaseModel):
    """Модель основной информации о лейбле трека."""

    id: int
    # Уникальный идентификатор лейбла.
    name: str
    # Название лейбла.
