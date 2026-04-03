from typing import Union

from ymdantic.models.tracks.album import TrackAlbum
from ymdantic.models.tracks.download_info import DownloadInfo, DownloadInfoDirect
from ymdantic.models.tracks.fade import Fade
from ymdantic.models.tracks.file_info import FileInfo, FileInfoParams, FileInfoWrapped
from ymdantic.models.tracks.lyrics_info import LyricsInfo
from ymdantic.models.tracks.major import Major
from ymdantic.models.tracks.podcast import Podcast, UnavailablePodcast
from ymdantic.models.tracks.r128 import R128
from ymdantic.models.tracks.track import Track, UnavailableTrack

TrackType = Union[Track, UnavailableTrack, Podcast, UnavailablePodcast]

__all__ = (
    "R128",
    "DownloadInfo",
    "DownloadInfoDirect",
    "Fade",
    "FileInfo",
    "FileInfoParams",
    "FileInfoWrapped",
    "LyricsInfo",
    "Major",
    "Podcast",
    "Track",
    "TrackAlbum",
    "TrackType",
    "UnavailablePodcast",
    "UnavailableTrack",
)
