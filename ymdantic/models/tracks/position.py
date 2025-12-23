"""Модель позиции трека в альбоме."""

from ymdantic.models.base import YMBaseModel


class TrackPosition(YMBaseModel):
    """Модель позиции трека в альбоме."""

    volume: int
    # Номер диска, на котором находится трек.
    index: int
    # Порядковый номер трека на диске.
