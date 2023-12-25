from typing import Literal, List

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.skeleton.tab_block import Tab
from ymdantic.models.landing.skeleton.tabs_source import TabsSource


class TabsData(YMBaseModel):
    """Pydantic модель, представляющая информацию о всех вкладках в блоке."""

    source: TabsSource
    # Источник данных.
    tabs: List[Tab]
    # Список вкладок.
    selected_tab_index: int
    # Индекс выбранной вкладки.


class TabsBlock(YMBaseModel):
    """Pydantic модель, представляющая информацию о блоке вкладок."""

    id: Literal["TABS_BLOCK"]
    # Идентификатор блока.
    type: Literal["TABS"]
    # Тип блока.
    data: TabsData
    # Информация о блоке.
