from ymdantic.models.base import YMBaseModel


class Tag(YMBaseModel):
    """Pydantic модель, представляющая тег трека."""

    id: str
    # Уникальный идентификатор тега.
    value: str  # TODO: Change to Literal
    # Значение тега.
