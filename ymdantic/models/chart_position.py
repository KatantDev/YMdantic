from typing import Literal, Optional

from ymdantic.models.base import YMBaseModel


class ChartPosition(YMBaseModel):
    """Pydantic модель, представляющая позицию трека в чарте."""

    position: int
    # Позиция трека в чарте.
    progress: Literal["same", "up", "down", "new"]
    # Информация о том, как изменилась позиция трека за последнее время.
    listeners: int
    # Количество слушателей трека на прошлой неделе.
    shift: int
    # Количество позиций, на которое изменилась позиция трека за последнее время.
    bg_color: Optional[str] = None
    # Цвет фона позиции трека.
