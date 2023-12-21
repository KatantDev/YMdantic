from typing import Literal, Union, List

from ymdantic.models.base import YMBaseModel


class PlaylistCoverMosaic(YMBaseModel):
    """Pydantic модель, представляющая обложку плейлиста в виде мозаики."""

    type: Literal["mosaic"]
    # Тип обложки, в данном случае "mosaic".
    items_uri: List[str]
    # Список URI элементов мозаики.
    custom: bool
    # Флаг, указывающий, является ли обложка пользовательской.


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


PlaylistCover = Union[PlaylistCoverMosaic, PlaylistCoverPic]
# Объединение двух типов обложек плейлиста: мозаики и изображения.
