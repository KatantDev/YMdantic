from ymdantic.models.base import YMBaseModel


class DerivedColors(YMBaseModel):
    """Pydantic модель, представляющая производные цвета обложки альбома."""

    average: str
    # Средний цвет обложки в формате HEX.
    wave_text: str
    # Цвет текста волновой формы в формате HEX.
    mini_player: str
    # Цвет мини-плеера в формате HEX.
    accent: str
    # Акцентный цвет в формате HEX.
