from typing import List

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.skeleton.tab_data import TabData


class TabBlock(YMBaseModel):
    """Pydantic модель, представляющая информацию о блоке вкладки."""

    id: str
    # Идентификатор блока.
    type: str
    # Тип блока.
    data: TabData
    # Информация о блоке.


class Tab(YMBaseModel):
    """Pydantic модель, представляющая информацию о вкладке."""

    id: str
    # Идентификатор вкладки.
    title: str
    # Заголовок вкладки.
    blocks: List[TabBlock]
    # Список блоков вкладки.
