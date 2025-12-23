from typing import List, Literal, Union

from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel


class PlaylistCoverMosaic(YMBaseModel):
    """Pydantic модель, представляющая обложку плейлиста в виде мозаики."""

    type: Literal["mosaic"]
    # Тип обложки, в данном случае "mosaic".
    items_uri: List[str]
    # Список URI элементов мозаики.
    custom: bool
    # Флаг, указывающий, является ли обложка пользовательской.

    def get_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает URL изображения обложки плейлиста с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения обложки плейлиста с заданным размером.
        """
        return HttpUrl(f"https://{self.items_uri[0].replace('%%', size)}")


class PlaylistCoverPic(YMBaseModel):
    """Pydantic модель, представляющая обложку плейлиста в виде одного изображения."""

    type: Literal["pic"]
    # Тип обложки, в данном случае "pic".
    dir: str
    # Директория, в которой хранится изображение обложки.
    version: str
    # Версия изображения обложки.
    uri: str
    # URI изображения обложки.
    custom: bool
    # Флаг, указывающий, является ли обложка пользовательской.

    def get_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает URL изображения обложки плейлиста с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения обложки плейлиста с заданным размером.
        """
        return HttpUrl(f"https://{self.uri.replace('%%', size)}")


PlaylistCover = Union[PlaylistCoverMosaic, PlaylistCoverPic]
# Объединение двух типов обложек плейлиста: мозаики и изображения.
