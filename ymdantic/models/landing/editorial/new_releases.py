from datetime import datetime
from typing import List

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.landing_album import LandingAlbum
from ymdantic.models.landing.landing_artist import LandingArtist
from ymdantic.models.landing.landing_cover import LandingPlaylistCover


class NewReleases(YMBaseModel):
    """Pydantic модель, представляющая информацию о новых релизах."""

    cover: LandingPlaylistCover
    # Обложка плейлиста. Содержит информацию о цветах обложки и URI обложки.
    artists: List[LandingArtist]
    # Список артистов, участвующих в новых релизах.
    album: LandingAlbum
    # Информация об альбоме в новых релизах.
    release_date: datetime
    # Дата релиза нового альбома.


class NewReleasesResponse(YMBaseModel):
    """Pydantic модель, представляющая ответ на запрос о новых релизах."""

    new_releases: List[NewReleases]
    # Список новых релизов.
