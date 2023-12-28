from typing import Literal

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.playlist import LandingPlaylist


class LandingPersonalPlaylistItemData(YMBaseModel):
    """Pydantic модель, представляющая информацию о личном плейлисте на главной."""

    playlist: LandingPlaylist
    # Информация о плейлисте.
    playlist_type: str
    # Тип плейлиста. Известны: neverHeard, playlistOfTheDay, recentTracks, rewind2023
    # Не Literal так как постоянно меняются типы.
    description: str
    # Описание плейлиста.
    notify: bool
    # Оповещения (неизвестно зачем).
    id_for_from: str
    # Тип откуда взят плейлист. Известны: never_heard, playlist_of_the_day,
    # recent_tracks, rewind2023. Не Literal так как постоянно меняются типы.


class LandingPersonalPlaylistItem(YMBaseModel):
    """
    Pydantic модель, представляющая информацию об элементе на главной.

    В данном случае, о личном плейлисте.
    """

    type: Literal["personal_playlist_item"]
    # Тип элемента.
    data: LandingPersonalPlaylistItemData
    # Информация о блоке плейлиста.
