from typing import Literal

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
