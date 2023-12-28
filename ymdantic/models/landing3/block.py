from typing import Literal, TypeVar, List

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing3.chart import OldChart
from ymdantic.models.landing3.menu import Menu

BlockType = Literal["chart", "new-releases"]
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


class OldChartBlock(BaseBlock):
    """Pydantic модель, представляющая информацию о блоке с чартами."""

    menu: Menu
    # Меню блока
    type: Literal["chart"]
    # Тип блока, в данном случае "chart".
    type_for_from: Literal["chart"]
    # Тип для источника блока. В данном случае "chart".
    chart_description: str
    # Описание списка чартов.
    chart: OldChart
    # Объект чарта, содержащий информацию о нём (является плейлистом).


class NewReleasesBlock(BaseBlock):
    """Pydantic модель, представляющая информацию о блоке с новыми релизами."""

    type: Literal["new-releases"]
    # Тип блока, в данном случае "new-releases".
    type_for_from: Literal["new-releases"]
    # Тип для источника блока. В данном случае "new-releases".
    new_releases: List[int]
    # Список ID новых релизов (альбомов).
