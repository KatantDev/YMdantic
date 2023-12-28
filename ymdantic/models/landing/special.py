from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.view_all_action import ViewAllAction
from ymdantic.models.theme import Theme


class LandingSpecial(YMBaseModel):
    """Pydantic модель, представляющая информацию о специальном блоке на главной."""

    id: str
    # Уникальный идентификатор специального блока.
    title: str
    # Заголовок специального блока.
    subtitle: str
    # Подзаголовок специального блока.
    button_title: str
    # Название кнопки специального блока.
    image_url: HttpUrl
    # Ссылка на изображение специального блока.
    align: str
    # Выравнивание специального блока.
    action: ViewAllAction
    # Действие специального блока.
    light_theme: Theme
    # Тема светлого режима.
    dark_theme: Theme
    # Тема темного режима.

    def get_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает ссылку на изображение в указанном размере.

        :param size: Размер изображения.
        :return: Ссылка на изображение в указанном размере.
        """
        return HttpUrl(str(self.image_url).replace("%%", size))
