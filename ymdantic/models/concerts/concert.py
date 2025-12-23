from datetime import datetime
from typing import List

from pydantic import UUID4, Field, HttpUrl

from ymdantic.models.artists.artist import ShortArtist
from ymdantic.models.base import YMBaseModel
from ymdantic.models.concerts.city_case_forms import CityCaseForms


class BaseConcert(YMBaseModel):
    """Pydantic модель, представляющая краткую информацию о концерте артиста."""

    id: UUID4
    # ID концерта.
    concert_title: str
    # Название концерта.
    afisha_url: HttpUrl
    # Ссылка на концерт на сайте афиши.
    city: str
    # Город, в котором проходит концерт.
    place: str
    # Место проведения концерта.
    address: str
    # Адрес места проведения концерта.
    datetime: datetime
    # Дата и время проведения концерта.
    coordinates: List[float] = Field(min_length=2, max_length=2)
    # Координаты места проведения концерта.
    map: HttpUrl
    # Ссылка для получения фотографии карты (Static Maps) места проведения концерта.
    map_url: HttpUrl
    # Ссылка на карту (Yandex Maps) места проведения концерта.
    hash: str
    # Хэш концерта.
    images: List[HttpUrl]
    # Ссылки на изображения концерта.
    content_rating: str
    # Возрастное ограничение концерта. Например: "16+".

    def get_map_url(self, width: int, height: int) -> HttpUrl:
        """
        Возвращает URL карты с заданным размером.

        :param width: Ширина карты.
        :param height: Высота карты.
        :return: URL карты с заданным размером.
        """
        size = f"{width},{height}"
        return HttpUrl(f"{str(self.map).replace('%%', size)}")


class Concert(BaseConcert):
    """Pydantic модель, представляющая концерт артиста."""

    city_case_forms: CityCaseForms
    # Падежи названия города, в котором проходит концерт.
    artists: List[ShortArtist]
    # Список артистов, выступающих на концерте.
    popular_concerts: List["Concert"]
