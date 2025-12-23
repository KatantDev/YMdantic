from datetime import datetime
from typing import Annotated, Any, Optional

from pydantic import Field

from ymdantic.models.base import YMBaseModel
from ymdantic.models.chart_position import ChartPosition
from ymdantic.models.tracks import TrackType


class BasePlaylistTrack(YMBaseModel):
    """Pydantic модель, представляющая базовую информацию о треке в плейлисте."""

    id: int
    # Уникальный идентификатор трека в плейлисте.
    track: TrackType
    # Объект трека.
    timestamp: datetime
    # Временная метка добавления трека в плейлист.
    recent: bool
    # Флаг, указывающий, является ли трек недавно добавленным в плейлист.
    chart: Optional[ChartPosition] = None
    # Позиция трека в чарте, если он в нём находится.
    content_restrictions: Annotated[dict[str, Any], Field(default_factory=dict)]


class PlaylistTrack(BasePlaylistTrack):
    """Pydantic модель, представляющая детальную информацию о треке в плейлисте."""

    original_index: int
    # Исходный индекс трека в плейлисте.
    original_shuffle_index: int
    # Исходный индекс перемешивания трека в плейлисте.
