from typing import Literal, Optional

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.landing_cover import LandingCover


class LandingAlbum(YMBaseModel):
    """Pydantic модель, представляющая информацию о LandingAlbum."""

    id: int
    # Уникальный идентификатор альбома.
    title: str
    # Название альбома.
    cover: LandingCover
    # Обложка альбома. Содержит информацию о цветах для обложки и URI обложки.
    album_type: Optional[Literal["single"]] = None
    # Тип альбома.
    content_warning: Optional[Literal["explicit"]] = None
    # Предупреждение о содержании.
