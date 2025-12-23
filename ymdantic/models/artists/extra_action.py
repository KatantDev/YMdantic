from ymdantic.models.base import YMBaseModel


class ExtraAction(YMBaseModel):
    """Pydantic модель, представляющая дополнительные действия с артистом."""

    type: str
    # Тип действия.
    title: str
    # Название действия.
    color: str
    # Цвет действия.
    url: str
    # Ссылка на действие.
