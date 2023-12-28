from typing import List
from pydantic import HttpUrl

from ymdantic.models.playlists.cover import PlaylistCover
from ymdantic.models.playlists.tag import Tag
from ymdantic.models.playlists.track import BasePlaylistTrack
from ymdantic.models.playlists.playlist import BasePlaylist
from ymdantic.models.playlists.playlist import ShortPlaylist


class ChartTrack(BasePlaylistTrack):
    """Pydantic модель, представляющая трек в чарте."""

    play_count: int
    # Количество воспроизведений трека.


class OldChart(BasePlaylist):
    """Pydantic модель, представляющая чарт."""

    cover: PlaylistCover
    # Обложка плейлиста.
    tags: List[Tag]
    # Теги плейлиста.
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

    def get_background_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает URL изображения фона чарта с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения фона чарта с заданным размером.
        """
        return HttpUrl(f"https://{self.background_image_url.replace('%%', size)}")

    def get_cover_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает URL изображения обложки плейлиста с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения обложки плейлиста с заданным размером.
        """
        return self.cover.get_image_url(size)
