from enum import Enum


class EditorialArtistsEnum(str, Enum):
    """Перечисление, представляющее типы блоков с артистами на главной странице."""

    ALL_ISRKA = "ALL_isrka"
    RU_ARTISTS = "RU_artists"
    RU_ISKRA = "RU_iskra"
