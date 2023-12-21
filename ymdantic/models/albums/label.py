from ymdantic.models.base import YMBaseModel


class Label(YMBaseModel):
    """Pydantic модель, представляющая информацию о лейбле альбома."""

    id: int
    # Уникальный идентификатор лейбла.
    name: str
    # Название лейбла.
