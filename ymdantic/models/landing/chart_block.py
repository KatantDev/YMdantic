from typing import Literal

from ymdantic.models.landing.chart import Chart
from ymdantic.models.landing3.block import BaseBlock
from ymdantic.models.landing3.menu import Menu


class ChartBlock(BaseBlock):
    """Pydantic модель, представляющая информацию о блоке с чартами."""

    menu: Menu
    # Меню блока
    type: Literal["chart"]
    # Тип блока, в данном случае "chart".
    type_for_from: Literal["chart"]
    # Тип для источника блока. В данном случае "chart".
    chart_description: str
    # Описание списка чартов.
    chart: Chart
    # Объект чарта, содержащий информацию о нём (является плейлистом).
