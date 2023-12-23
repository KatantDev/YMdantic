from typing import Optional

from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel
from ymdantic.models.tracks import DerivedColors


class LandingPlaylistCover(YMBaseModel):
    """Pydantic модель, представляющая информацию об обложке плейлиста на лендинге."""

    uri: str  # TODO: get_url
    # URI обложки плейлиста.
    color: Optional[str] = None
    # Основной цвет обложки плейлиста.
    derived_colors: Optional[DerivedColors] = None
    # Дополнительные цвета обложки плейлиста.

    def get_image_url(self, size: str = "200x200") -> Optional[HttpUrl]:
        """
        Возвращает ссылку на изображение обложки.

        :param size: Размер изображения.
        :return: Ссылка на изображение обложки.
        """
        if self.uri is None:
            return None
        return HttpUrl(f"https://{self.uri.replace('%%', size)}")


class LandingCover(YMBaseModel):
    """Pydantic модель, представляющая информацию об обложке на лендинге."""

    uri: str  # TODO: get_url
    # URI обложки.
    color: str
    # Основной цвет обложки.
    derived_colors: DerivedColors
    # Дополнительные цвета обложки.

    def get_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает ссылку на изображение обложки.

        :param size: Размер изображения.
        :return: Ссылка на изображение обложки.
        """
        return HttpUrl(f"https://{self.uri.replace('%%', size)}")
