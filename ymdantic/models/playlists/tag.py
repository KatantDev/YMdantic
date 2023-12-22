from ymdantic.models.base import YMBaseModel


class Tag(YMBaseModel):
    """Pydantic модель, представляющая тег трека."""

    id: str
    # Уникальный идентификатор тега.
    value: str  # TODO: Изменить на Literal, выяснить, какие значения могут быть.
    # Значение тега.
