from enum import Enum


class EditorialCompilationEnum(str, Enum):
    """Перечисление, представляющее типы блоков с подборками на главной странице."""

    ALL_NEWYEAR = "ALL_newyear"
    # Плейлисты.
    ALL_WINTER = "ALL_winter"
    # Плейлисты.
    RUSSIA_HITS = "RUSSIA_hits"
    # Плейлисты.
    RUSSIA_NEWCOMERS = "RUSSIA_newcomers"
    # Плейлисты.
    RUSSIA_EDITORIAL_COMPILATION = "RUSSIA_editorial_compilation"
    # Альбомы.
    ALL_ALBUMS_WITH_VIDEOSHOTS = "ALL_albums_with_videoshots"
    # Альбомы.
    ALL_ALBUMS_WITH_COMMENTARY = "ALL_albums_with_commentary"
    # Альбомы.
    RU_GENRES = "RU_genres"
    # Плейлисты.
    RU_TRANDS = "RU_trands"
    # Плейлисты.
    RU_EDITORS = "RU_editors"
    # Альбомы.
