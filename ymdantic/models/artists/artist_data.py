from typing import TYPE_CHECKING, List, Optional

from ymdantic.models.artists.artist import Artist, SimilarArtist
from ymdantic.models.artists.artist_track_chart_position import TrackChartPosition
from ymdantic.models.artists.band_link_scanner_link import BandLinkScannerLink
from ymdantic.models.artists.concert import ArtistConcert
from ymdantic.models.artists.extra_action import ExtraAction
from ymdantic.models.artists.video import ArtistVideo
from ymdantic.models.base import YMBaseModel
from ymdantic.models.clips.clip import Clip
from ymdantic.models.cover import Cover
from ymdantic.models.custom_wave import CustomWave

if TYPE_CHECKING:
    from ymdantic.models.albums.album import ShortAlbum
    from ymdantic.models.tracks import TrackType


class ArtistData(YMBaseModel):
    """Модель информации об артисте."""

    artist: Artist
    # Информация об артисте.
    albums: List["ShortAlbum"]
    # Список альбомов артиста.
    also_albums: List["ShortAlbum"]
    # Список альбомов, в которых участвует артист.
    last_release_ids: List[int]
    # Список последних релизов артиста.
    popular_tracks: List["TrackType"]
    # Список популярных треков артиста.
    bandlink_scanner_link: BandLinkScannerLink
    # Ссылка на band.link артиста.
    similar_artists: List[SimilarArtist]
    # Список похожих артистов.
    all_covers: List[Cover]
    # Список обложек артиста.
    concerts: List[ArtistConcert]
    # Список концертов артиста.
    videos: List[ArtistVideo]
    # Список видео артиста.
    clips: List[Clip]
    # Список клипов артиста.
    vinyls: List[str]
    # Список винилов артиста.
    has_promotions: bool
    # Флаг, указывающий, есть ли у артиста акции.
    tracks_in_chart: Optional[List[TrackChartPosition]] = None
    # Список треков артиста в чарте.
    last_releases: List["ShortAlbum"]
    # Список последних релизов артиста.
    extra_actions: List[ExtraAction]
    # Список дополнительных действий с артистом.
    custom_wave: CustomWave
    # Информация о кастомной волне артиста.
