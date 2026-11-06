from typing import Annotated

from pydantic import Field, HttpUrl

from ymdantic.mixins import DeprecatedMixin
from ymdantic.models.artists.artist import ShortArtist
from ymdantic.models.base import YMBaseModel


class Clip(YMBaseModel, DeprecatedMixin):
    """Pydantic модель, представляющая клип."""

    clip_id: int
    # Уникальный идентификатор клипа.
    title: str
    # Название клипа.
    version: str | None = None
    # Версия клипа (может отсутствовать).
    player_id: str
    # ID плеера клипа.
    uuid: str
    # UUID клипа.
    thumbnail: HttpUrl
    # Ссылка на обложку клипа.
    preview_url: HttpUrl | None = None
    # Ссылка на превью клипа (видео, может отсутствовать).
    duration: int
    # Длительность клипа.
    artists: list[ShortArtist]
    # Список артистов, участвующих в клипе.
    disclaimers: Annotated[list[str], Field(default_factory=list)]
    # Список отказов от ответственности клипа, например "explicit".
    explicit: bool
    # Флаг, указывающий, содержит ли клип нецензурную лексику.

    def get_thumbnail_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает URL изображения обложки клипа с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения обложки клипа с заданным размером.
        """
        return HttpUrl(f"https://{str(self.thumbnail).replace('%%', size)}")
