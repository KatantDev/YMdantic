from typing import Literal

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.playlist import LandingPlaylist


class LandingLikedPlaylistItemData(YMBaseModel):
    """Pydantic модель, представляющая информацию о лайкнутом плейлисте на главной."""

    playlist: LandingPlaylist
    # Информация о плейлисте.
    likes_count: int
    # Количество лайков плейлиста.


class LandingLikedPlaylistItem(YMBaseModel):
    """
    Pydantic модель, представляющая информацию об элементе на главной.

    В данном случае, о понравившемся плейлисте.
    """

    type: Literal["liked_playlist_item"]
    # Тип элемента.
    data: LandingLikedPlaylistItemData
    # Информация о блоке плейлиста.
