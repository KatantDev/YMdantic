from typing import List

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.album import LandingAlbumItemData
from ymdantic.models.landing.cover import LandingCover


class InStyle(YMBaseModel):
    """Pydantic модель, представляющая информацию о блоке InStyle."""

    title: str
    # Заголовок блока (имя исполнителя).
    cover: LandingCover
    # Обложка блока (исполнителя).
    items: List[LandingAlbumItemData]


class InStyleResponse(YMBaseModel):
    """Pydantic модель, представляющая ответ на запрос информации о блоке InStyle."""

    in_style_tabs: List[InStyle]
