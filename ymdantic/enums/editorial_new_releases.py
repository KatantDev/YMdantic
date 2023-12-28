import sys

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from strenum import StrEnum


class EditorialNewReleasesEnum(StrEnum):
    """Перечисление, представляющее типы блоков с новинками на главной странице."""

    ALL_ALBUMS_OF_THE_MONTH = "ALL_albums_of_the_month"
    RU_ALBUMS = "RU_albums"
