from .landing3 import ChartBlock, NewReleasesBlock
from .landing import (
    NewReleasesResponse,
    NewRelease,
    SkeletonResponse,
    LandingArtist,
    LandingArtistItem,
    LandingAlbumItemData,
    LandingAlbumItem,
    EditorialResponse,
    LandingPlaylistItemData,
    LandingPlaylistItem,
    LandingPromotion,
    LandingPromotionResponse,
    LandingOpenPlaylist,
    LandingSpecial,
)
from .playlists import Playlist
from .response import Response
from .albums import Album, ShortAlbum
from .tracks import (
    TrackType,
    DownloadInfo,
    DownloadInfoDirect,
    Track,
    UnavailableTrack,
    Podcast,
    UnavailablePodcast,
)
from .artists import Artist
from .s3 import S3FileUrl

# Ребилд моделей с учётом новых изменений. (TrackType)
ShortAlbum.model_rebuild()
Album.model_rebuild()

__all__ = (
    "Response",
    "Album",
    "ShortAlbum",
    "Artist",
    "TrackType",
    "DownloadInfo",
    "DownloadInfoDirect",
    "ChartBlock",
    "NewReleasesBlock",
    "Playlist",
    "Track",
    "UnavailableTrack",
    "Podcast",
    "UnavailablePodcast",
    "NewReleasesResponse",
    "NewRelease",
    "SkeletonResponse",
    "LandingArtist",
    "LandingArtistItem",
    "LandingAlbumItemData",
    "LandingAlbumItem",
    "LandingPlaylistItemData",
    "LandingPlaylistItem",
    "LandingPromotion",
    "LandingPromotionResponse",
    "LandingOpenPlaylist",
    "LandingSpecial",
    "EditorialResponse",
    "S3FileUrl",
)
