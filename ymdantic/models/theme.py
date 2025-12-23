from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel


class Theme(YMBaseModel):
    """Pydantic модель, представляющая тему оформления."""

    button_color: str
    # Цвет кнопок в формате HEX.
    text_color: str
    # Цвет текста в формате HEX.
    bg_image_url: HttpUrl
    # Ссылка на изображение фона.

    def get_bg_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает URL изображения фона с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения фона с заданным размером.
        """
        return HttpUrl(str(self.bg_image_url).replace("%%", size))
