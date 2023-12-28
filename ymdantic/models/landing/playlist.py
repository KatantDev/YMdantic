from typing import Literal

from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.cover import LandingPlaylistCover


class LandingPlaylist(YMBaseModel):
    """Pydantic модель, представляющая информацию о плейлисте на главной."""

    uid: int
    # Уникальный идентификатор плейлиста.
    playlist_uuid: str
    # Уникальный идентификатор плейлиста.
    kind: int
    # Тип плейлиста.
    title: str
    # Название плейлиста.
    cover: LandingPlaylistCover
    # Обложка плейлиста. Содержит информацию о цветах обложки и URI обложки.

    def get_cover_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает ссылку на изображение обложки.

        :param size: Размер изображения.
        :return: Ссылка на изображение обложки.
        """
        return self.cover.get_image_url(size)


class LandingPlaylistItemData(YMBaseModel):
    """Pydantic модель, представляющая информацию о плейлисте на главной."""

    playlist: LandingPlaylist
    # Информация о плейлисте.


class LandingPlaylistItem(YMBaseModel):
    """
    Pydantic модель, представляющая информацию об элементе на главной.

    В данном случае, о плейлисте.
    """

    type: Literal["playlist_item"]
    # Тип элемента.
    data: LandingPlaylistItemData
    # Информация о блоке плейлиста.
