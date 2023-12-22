from typing import Literal, TypeVar

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing3.chart import Chart
from ymdantic.models.landing3.menu import Menu

BlockType = Literal["chart"]
BlockVar = TypeVar("BlockVar")


class BaseBlock(YMBaseModel):
    """Pydantic модель, представляющая базовую информацию о любом блоке в лендинге."""

    id: str
    # Уникальный идентификатор блока.
    type: BlockType
    # Тип блока.
    type_for_from: BlockType
    # Тип для источника блока.
    title: str
    # Заголовок блока.


class ChartBlock(BaseBlock):
    """Pydantic модель, представляющая информацию о блоке с чартами."""

    menu: Menu
    # Меню блока
    type: Literal["chart"]
    # Тип блока, в данном случае "chart".
    chart_description: str
    # Описание списка чартов.
    chart: Chart
    # Объект чарта, содержащий информацию о нём (является плейлистом).
