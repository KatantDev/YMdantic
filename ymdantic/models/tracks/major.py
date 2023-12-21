from ymdantic.models.base import YMBaseModel


class Major(YMBaseModel):
    """Pydantic модель, представляющая основную информацию о лейбле трека."""

    id: int
    # Уникальный идентификатор лейбла.
    name: str
    # Название лейбла.


class PodcastMajor(YMBaseModel):
    """Pydantic модель, представляющая основную информацию о лейбле трека."""

    id: int
    # Уникальный идентификатор лейбла.
    name: str
    # Название лейбла.
