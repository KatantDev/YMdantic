from typing import List, Literal, Optional

from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.artist import LandingArtist
from ymdantic.models.landing.cover import LandingCover


class LandingAlbum(YMBaseModel):
    """Pydantic модель, представляющая информацию об альбоме не главной."""

    id: int
    # Уникальный идентификатор альбома.
    title: str
    # Название альбома.
    cover: LandingCover
    # Обложка альбома. Содержит информацию о цветах для обложки и URI обложки.
    album_type: Optional[Literal["single", "compilation"]] = None
    # Тип альбома.
    content_warning: Optional[Literal["explicit", "clean"]] = None
    # Предупреждение о содержании.

    def get_cover_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает ссылку на изображение обложки.

        :param size: Размер изображения.
        :return: Ссылка на изображение обложки.
        """
        return self.cover.get_image_url(size)


class LandingAlbumItemData(YMBaseModel):
    """Pydantic модель, представляющая информацию об альбоме на главной."""

    album: LandingAlbum
    artists: List[LandingArtist]


class LandingAlbumItem(YMBaseModel):
    """
    Pydantic модель, представляющая информацию об элементе на главной.

    В данном случае, об альбоме.
    """

    type: Literal["album_item"]
    data: LandingAlbumItemData
