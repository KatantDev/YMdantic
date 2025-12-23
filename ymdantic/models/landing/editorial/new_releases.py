from datetime import datetime

from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.album import LandingAlbum
from ymdantic.models.landing.artist import LandingArtist
from ymdantic.models.landing.cover import LandingPlaylistCover


class NewRelease(YMBaseModel):
    """Pydantic модель, представляющая информацию о новых релизах."""

    cover: LandingPlaylistCover
    # Обложка плейлиста. Содержит информацию о цветах обложки и URI обложки.
    artists: list[LandingArtist]
    # Список артистов, участвующих в новых релизах.
    album: LandingAlbum
    # Информация об альбоме в новых релизах.
    release_date: datetime
    # Дата релиза нового альбома.

    def get_cover_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает ссылку на изображение обложки.

        :param size: Размер изображения.
        :return: Ссылка на изображение обложки.
        """
        return self.cover.get_image_url(size)


class NewReleasesResponse(YMBaseModel):
    """Pydantic модель, представляющая ответ на запрос о новых релизах."""

    new_releases: list[NewRelease]
    # Список новых релизов.
