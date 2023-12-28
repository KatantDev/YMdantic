from typing import List

from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.view_all_action import ViewAllAction


class LandingPromotion(YMBaseModel):
    """Pydantic модель, представляющая информацию о промо-блоке на главной."""

    feature_id: str
    # Уникальный идентификатор промо-блока.
    title: str
    # Заголовок промо-блока.
    subtitle: str
    # Подзаголовок промо-блока.
    heading: str
    # Heading промо-блока.
    action: ViewAllAction
    # Действие промо-блока.
    image_url: str
    # Ссылка на изображение промо-блока.

    def get_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает URL изображения.

        :param size: Размер изображения.
        :return: URL изображения с указанным размером.
        """
        return HttpUrl(f"https://{self.image_url.replace('%%', size)}")


class LandingPromotionResponse(YMBaseModel):
    """Pydantic модель, представляющая информацию о промо-блоках на главной."""

    promotions: List[LandingPromotion]
    # Список промо-блоков.
