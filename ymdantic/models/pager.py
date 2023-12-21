from ymdantic.models.base import YMBaseModel


class Pager(YMBaseModel):
    """Pydantic модель, представляющая пагинацию."""

    total: int
    # Общее количество элементов.
    page: int
    # Номер страницы.
    per_page: int
    # Количество элементов на странице.
