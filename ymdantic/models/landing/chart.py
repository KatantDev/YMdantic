from pydantic import HttpUrl

from ymdantic.models.landing3.chart import ChartTrack
from ymdantic.models.playlists.playlist import BasePlaylist


class Chart(BasePlaylist):
    """Pydantic модель, представляющая чарт."""

    description: str
    # Описание чарта.
    description_formatted: str
    # Отформатированное описание чарта.
    likes_count: int
    # Количество лайков чарта.
    background_image_url: str
    # URL фонового изображения чарта.
    background_video_url: HttpUrl
    # URL фонового видео чарта.
    tracks: list[ChartTrack]
    # Список треков в чарте.

    def get_background_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает URL изображения фона чарта с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения фона чарта с заданным размером.
        """
        return HttpUrl(f"https://{self.background_image_url.replace('%%', size)}")
