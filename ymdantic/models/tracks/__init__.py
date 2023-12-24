from typing import Union

from .derived_colors import DerivedColors
from .download_info import DownloadInfo, DownloadInfoDirect
from .fade import Fade
from .lyrics_info import LyricsInfo
from .major import Major
from .r128 import R128
from .track import Track, UnavailableTrack
from .podcast import Podcast, UnavailablePodcast
from .track_album import TrackAlbum

TrackType = Union[Track, UnavailableTrack, Podcast, UnavailablePodcast]

__all__ = (
    "TrackType",
    "Track",
    "UnavailableTrack",
    "Podcast",
    "UnavailablePodcast",
    "DownloadInfo",
    "DownloadInfoDirect",
    "TrackAlbum",
    "DerivedColors",
    "R128",
    "Fade",
    "LyricsInfo",
    "Major",
)
