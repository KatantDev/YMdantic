from enum import Enum


class EditorialNewReleasesEnum(str, Enum):
    """Перечисление, представляющее типы блоков с новинками на главной странице."""

    ALL_ALBUMS_OF_THE_MONTH = "ALL_albums_of_the_month"
    RU_ALBUMS = "RU_albums"
