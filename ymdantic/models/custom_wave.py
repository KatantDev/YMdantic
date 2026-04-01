from typing import Literal

from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel


class CustomWave(YMBaseModel):
    """Pydantic модель, представляющая пользовательскую волну."""

    title: str
    # Заголовок пользовательской волны.
    animation_url: HttpUrl
    # URL анимации пользовательской волны.
    header: str
    # Заголовок пользовательской волны.
    position: Literal["default"] | None = None
    # Позиция пользовательской волны.
    background_image_url: str | None = None
    # URL фонового изображения плейлиста.

    def get_background_image_url(self, size: str = "200x200") -> HttpUrl | None:
        """
        Возвращает URL изображения фона плейлиста с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения фона плейлиста с заданным размером.
        """
        if self.background_image_url is None:
            return None
        return HttpUrl(f"https://{self.background_image_url.replace('%%', size)}")
