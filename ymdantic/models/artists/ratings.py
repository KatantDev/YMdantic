from ymdantic.models.base import YMBaseModel


class Ratings(YMBaseModel):
    """Pydantic модель, представляющая рейтинги артиста."""

    week: int
    # Позиция артиста в недельном рейтинге.
    month: int
    # Позиция артиста в месячном рейтинге.
    day: int
    # Позиция артиста в дневном рейтинге.
