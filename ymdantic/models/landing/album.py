from typing import Literal

from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel
from ymdantic.models.content_restrictions import ContentRestrictions
from ymdantic.models.landing.artist import LandingArtist
from ymdantic.models.landing.cover import LandingCover
from ymdantic.models.trailer import Trailer


class LandingAlbum(YMBaseModel):
    """Pydantic модель, представляющая информацию об альбоме не главной."""

    id: int
    # Уникальный идентификатор альбома.
    title: str
    # Название альбома.
    cover: LandingCover
    # Обложка альбома. Содержит информацию о цветах для обложки и URI обложки.
    album_type: Literal["single", "compilation"] | None = None
    # Тип альбома.
    content_warning: Literal["explicit", "clean"] | None = None
    # Предупреждение о содержании.
    content_restrictions: ContentRestrictions | None = None
    # Ограничения по содержанию.

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
    artists: list[LandingArtist]
    trailer: Trailer


class LandingAlbumItem(YMBaseModel):
    """
    Pydantic модель, представляющая информацию об элементе на главной.

    В данном случае, об альбоме.
    """

    type: Literal["album_item"]
    data: LandingAlbumItemData
