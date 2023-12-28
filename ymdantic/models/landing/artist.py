from typing import Literal

from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.cover import LandingCover


class LandingArtist(YMBaseModel):
    """Pydantic модель, представляющая информацию об артисте на главной."""

    id: int
    # Уникальный идентификатор артиста.
    name: str
    # Имя артиста.
    cover: LandingCover
    # Обложка артиста. Содержит информацию о цветах обложки и URI обложки.

    def get_cover_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает ссылку на изображение обложки.

        :param size: Размер изображения.
        :return: Ссылка на изображение обложки.
        """
        return self.cover.get_image_url(size)


class LandingArtistItemData(YMBaseModel):
    """Pydantic модель, представляющая информацию об артисте на главной."""

    artist: LandingArtist
    # Информация об артисте.


class LandingArtistItem(YMBaseModel):
    """
    Pydantic модель, представляющая информацию об элементе на главной.

    В данном случае, об артисте.
    """

    type: Literal["artist_item"]
    # Тип элемента.
    data: LandingArtistItemData
    # Информация о блоке артиста.
