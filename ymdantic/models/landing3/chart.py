from typing import List
from pydantic import HttpUrl

from ymdantic.models.playlists.playlist_track import BasePlaylistTrack
from ymdantic.models.playlists.playlist import BasePlaylist
from ymdantic.models.playlists.playlist import ShortPlaylist


class ChartTrack(BasePlaylistTrack):
    """Pydantic модель, представляющая трек в чарте."""

    play_count: int
    # Количество воспроизведений трека.


class Chart(BasePlaylist):
    """Pydantic модель, представляющая чарт."""

    description: str
    # Описание чарта.
    description_formatted: str
    # Отформатированное описание чарта.
    likes_count: int
    # Количество лайков чарта.
    background_image_url: str
    # URL фонового изображения чарта.
    background_video_url: HttpUrl
    # URL фонового видео чарта.
    tracks: List[ChartTrack]
    # Список треков в чарте.
    similar_playlists: List["ShortPlaylist"]
    # Список похожих плейлистов.
