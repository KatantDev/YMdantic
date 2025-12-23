from typing import Union

from ymdantic.models.tracks.album import TrackAlbum
from ymdantic.models.tracks.derived_colors import DerivedColors
from ymdantic.models.tracks.download_info import DownloadInfo, DownloadInfoDirect
from ymdantic.models.tracks.fade import Fade
from ymdantic.models.tracks.lyrics_info import LyricsInfo
from ymdantic.models.tracks.major import Major
from ymdantic.models.tracks.podcast import Podcast, UnavailablePodcast
from ymdantic.models.tracks.r128 import R128
from ymdantic.models.tracks.track import Track, UnavailableTrack

TrackType = Union[UnavailablePodcast, Podcast, Track, UnavailableTrack]

__all__ = (
    "R128",
    "DerivedColors",
    "DownloadInfo",
    "DownloadInfoDirect",
    "Fade",
    "LyricsInfo",
    "Major",
    "Podcast",
    "Track",
    "TrackAlbum",
    "TrackType",
    "UnavailablePodcast",
    "UnavailableTrack",
)
