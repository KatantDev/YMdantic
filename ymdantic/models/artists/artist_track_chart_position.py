from pydantic import BaseModel

from ymdantic.models.chart_position import ChartPosition


class TrackId(BaseModel):
    """Модель ID трека."""

    id: str
    # Идентификатор трека.


class TrackChartPosition(ChartPosition):
    """Модель позиции трека в чарте."""

    track_id: TrackId
    # Идентификатор трека.
