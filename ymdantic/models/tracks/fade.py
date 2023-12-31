from ymdantic.models.base import YMBaseModel


class Fade(YMBaseModel):
    """Pydantic модель, представляющая информацию о постепенном переходе в треке."""

    in_start: float
    # Время в секундах, когда начинается постепенное увеличение громкости.
    in_stop: float
    # Время в секундах, когда заканчивается постепенное увеличение громкости.
    out_start: float
    # Время в секундах, когда начинается постепенное уменьшение громкости.
    out_stop: float
    # Время в секундах, когда заканчивается постепенное уменьшение громкости.
