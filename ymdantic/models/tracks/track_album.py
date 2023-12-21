from typing import Optional

from ymdantic.models.albums import YMBaseAlbum
from ymdantic.models.tracks.track_position import TrackPosition


class TrackAlbum(YMBaseAlbum):
    """Pydantic модель, представляющая информацию об альбоме с  текущим треком."""

    track_position: Optional[TrackPosition] = None
    # Позиция трека в альбоме (если есть).
