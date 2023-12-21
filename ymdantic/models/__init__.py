from .landing3 import ChartBlock
from .playlists import Playlist
from .response import Response
from .albums import Album, ShortAlbum
from .tracks import TrackType, DownloadInfo
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
    "Playlist",
)
