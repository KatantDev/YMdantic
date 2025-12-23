from typing import List

from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.playlist import LandingPlaylist
from ymdantic.models.tracks import TrackType


class LandingOpenPlaylistCover(YMBaseModel):
    """Модель информации об обложке плейлиста на лендинге."""

    uri: str
    # Ссылка на изображение обложки.

    def get_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает ссылку на изображение обложки.

        Может вернуть в неправильном размере, если исходная ссылка оригинальная.

        :param size: Размер изображения.
        :return: Ссылка на изображение обложки.
        """
        if "https://" in self.uri:
            return HttpUrl(self.uri.replace("orig", size))
        return HttpUrl(self.uri.replace("%%", size))


class LandingOpenPlaylist(YMBaseModel):
    """Модель информации о плейлисте на лендинге."""

    playlist: LandingPlaylist
    # Информация о плейлисте.
    cover: LandingOpenPlaylistCover
    # Обложка плейлиста.
    tracks: List[TrackType]
    # Список треков плейлиста.

    def get_cover_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает ссылку на изображение обложки.

        Может вернуть в неправильном размере, если исходная ссылка оригинальная.

        :param size: Размер изображения.
        :return: Ссылка на изображение обложки.
        """
        return self.cover.get_image_url(size)
