from ymdantic.models.base import YMBaseModel


class TabSource(YMBaseModel):
    """Pydantic модель, представляющая информацию об источнике данных."""

    uri: str
    # URI источника данных.
    count_web: int
    # Количество элементов на сайте.
    count: int
    # Количество элементов.
