from ymdantic.models.playlists.playlist import ShortPlaylist
from ymdantic.models.playlists.track import BasePlaylistTrack
from ymdantic.models.trailer import Trailer


class ChartTrack(BasePlaylistTrack):
    """Pydantic модель, представляющая трек в чарте."""

    play_count: int
    # Количество воспроизведений трека.


class OldChart(ShortPlaylist):
    """Pydantic модель, представляющая чарт."""

    tracks: list[ChartTrack]
    # Список треков в чарте.
    similar_playlists: list["ShortPlaylist"]
    # Список похожих плейлистов.
    trailer: Trailer
    # Флаг, указывающий, является ли чарт трейлером.
