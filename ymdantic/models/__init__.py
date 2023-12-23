from .landing3 import ChartBlock, NewReleasesBlock
from .landing import NewReleasesResponse, NewReleases
from .playlists import Playlist
from .response import Response
from .albums import Album, ShortAlbum
from .tracks import (
    TrackType,
    DownloadInfo,
    Track,
    UnavailableTrack,
    Podcast,
    UnavailablePodcast,
)
from .artists import Artist

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
    "ChartBlock",
    "NewReleasesBlock",
    "Playlist",
    "Track",
    "UnavailableTrack",
    "Podcast",
    "UnavailablePodcast",
    "NewReleasesResponse",
    "NewReleases",
)
