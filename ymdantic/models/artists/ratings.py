from ymdantic.models.base import YMBaseModel


class Ratings(YMBaseModel):
    """Pydantic модель, представляющая рейтинги артиста."""

    week: int | None = None
    # Позиция артиста в недельном рейтинге.
    month: int | None = None
    # Позиция артиста в месячном рейтинге.
    day: int | None = None
    # Позиция артиста в дневном рейтинге.
