from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.landing_cover import LandingCover


class LandingArtist(YMBaseModel):
    """Pydantic модель, представляющая информацию о LandingArtist."""

    id: int
    # Уникальный идентификатор артиста.
    name: str
    # Имя артиста.
    cover: LandingCover
    # Обложка артиста. Содержит информацию о цветах обложки и URI обложки.

    def get_cover_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает ссылку на изображение обложки.

        :param size: Размер изображения.
        :return: Ссылка на изображение обложки.
        """
        return self.cover.get_image_url(size)
