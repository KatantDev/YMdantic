import sys

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from strenum import StrEnum


class EditorialArtistsEnum(StrEnum):
    """Перечисление, представляющее типы блоков с артистами на главной странице."""

    ALL_ISRKA = "ALL_isrka"
    RU_ARTISTS = "RU_artists"
    RU_ISKRA = "RU_iskra"
