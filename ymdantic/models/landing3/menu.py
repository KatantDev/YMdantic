from typing import List, Literal, Optional

from ymdantic.models.base import YMBaseModel


class MenuItem(YMBaseModel):
    """Pydantic модель, представляющая элемент меню."""

    title: str
    # Заголовок элемента меню.
    url: Literal["russia", "world"]
    # URL элемента меню.
    selected: Optional[bool] = None
    # Флаг, указывающий, выбран ли элемент меню.


class Menu(YMBaseModel):
    """Pydantic модель, представляющая меню."""

    items: List[MenuItem]
    # Список элементов меню.
