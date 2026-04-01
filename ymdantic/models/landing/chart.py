from ymdantic.models.landing3.chart import ChartTrack
from ymdantic.models.playlists import ShortPlaylist


class Chart(ShortPlaylist):
    """Pydantic модель, представляющая чарт."""

    tracks: list[ChartTrack]
    # Список треков в чарте.
