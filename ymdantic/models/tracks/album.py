from datetime import date
from typing import Optional

from ymdantic.models.albums import BaseAlbum
from ymdantic.models.tracks.position import TrackPosition


class TrackAlbum(BaseAlbum):
    """Pydantic модель, представляющая информацию об альбоме с  текущим треком."""

    start_date: Optional[date] = None
    # Дата начала альбома.
    track_position: Optional[TrackPosition] = None
    # Позиция трека в альбоме (если есть).
