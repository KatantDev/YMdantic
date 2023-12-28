from typing import Literal, List

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.skeleton.tabs_block import TabsBlock


class SkeletonResponse(YMBaseModel):
    """Pydantic модель ответа на запрос редакционных подборок."""

    id: Literal["main"]
    # Идентификатор редакционных подборок.
    title: str
    # Заголовок редакционных подборок.
    blocks: List[TabsBlock]
    # Список блоков редакционных подборок.
