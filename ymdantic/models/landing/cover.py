from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel
from ymdantic.models.derived_colors import DerivedColors


class LandingCover(YMBaseModel):
    """Pydantic модель, представляющая информацию об обложке на лендинге."""

    uri: str
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
