from pydantic import HttpUrl

from ymdantic.models.agent import Agent
from ymdantic.models.base import YMBaseModel


class WaveColor(YMBaseModel):
    """Pydantic модель, представляющая цвет волны на главной."""

    average: str
    # Средний цвет волны.
    wave_text: str
    # Цвет текста волны.


class LandingCustomWave(YMBaseModel):
    """Pydantic модель, представляющая волну на главной."""

    title: str
    # Заголовок волны.
    header: str
    # Заголовок волны.
    animation_url: HttpUrl
    # Ссылка на анимацию волны.
    station_id: str
    # Уникальный идентификатор станции.
    seeds: list[str]
    # Список идентификатор станций, на основе которых сформирована волна.
    colors: WaveColor
    # Цвета волны.
    background_image_url: str | None = None
    # URL фонового изображения альбома.
    compact_image_url: str | None = None
    # URL фонового изображения альбома.
    agent: Agent
    # Информация об агенте волны.

    def get_background_image_url(self, size: str = "200x200") -> HttpUrl | None:
        """
        Возвращает URL изображения фона с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения фона с заданным размером.
        """
        if self.background_image_url is None:
            return None
        return HttpUrl(f"https://{self.background_image_url.replace('%%', size)}")

    def get_compact_image_url(self, size: str = "200x200") -> HttpUrl | None:
        """
        Возвращает URL изображения волны с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения волны с заданным размером.
        """
        if self.compact_image_url is None:
            return None
        return HttpUrl(f"https://{self.compact_image_url.replace('%%', size)}")


class LandingWaves(YMBaseModel):
    """Pydantic модель, представляющая подборки волн на главной."""

    id: str
    # Уникальный идентификатор волны.
    title: str
    # Заголовок волны.
    items: list[LandingCustomWave]
    # Подборка волн на основе заголовка.


class LandingWavesResponse(YMBaseModel):
    """Pydantic модель, представляющая ответ на запрос волны на главной."""

    waves: list[LandingWaves]
    # Список подборок волн на главной.
