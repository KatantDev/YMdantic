from typing import List

from pydantic import HttpUrl

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
    seeds: List[str]
    # Список идентификатор станций, на основе которых сформирована волна.
    colors: WaveColor
    # Цвета волны.


class LandingWaves(YMBaseModel):
    """Pydantic модель, представляющая подборки волн на главной."""

    title: str
    # Заголовок волны.
    items: List[LandingCustomWave]
    # Подборка волн на основе заголовка.


class LandingWavesResponse(YMBaseModel):
    """Pydantic модель, представляющая ответ на запрос волны на главной."""

    waves: List[LandingWaves]
    # Список подборок волн на главной.
