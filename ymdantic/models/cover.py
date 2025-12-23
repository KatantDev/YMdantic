from typing import Literal

from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel


class Cover(YMBaseModel):
    """Pydantic модель, представляющая обложку альбома или артиста."""

    type: Literal["from-artist-photos", "from-album-cover"]
    # Тип обложки. Определяет источник обложки.
    uri: str
    # URI обложки. Это уникальный идентификатор, который можно использовать
    # для получения изображения обложки.
    prefix: str
    # Префикс URI. Используется для формирования полного пути к изображению
    # обложки.
    copyright_name: str | None = None
    # Название правообладателя обложки. Используется очень редко.
    copyright_cline: str | None = None
    # Копирайт обложки. Используется очень редко.

    def get_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает URL изображения обложки с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения обложки с заданным размером.
        """
        return HttpUrl(f"https://{self.uri.replace('%%', size)}")
