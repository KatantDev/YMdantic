from ymdantic.models.base import YMBaseModel


class TrackPosition(YMBaseModel):
    """Pydantic модель, представляющая позицию трека в альбоме."""

    volume: int
    # Номер диска, на котором находится трек.
    index: int
    # Порядковый номер трека на диске.
