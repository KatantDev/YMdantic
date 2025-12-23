import sys

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from strenum import StrEnum


class EditorialPromotionEnum(StrEnum):
    """Перечисление типов промо-блоков на главной странице."""

    NEUROMUSIC = "NEUROMUSIC"
    KOSTYL_VREMYA_KLIPOV = "kostyl_vremya_klipov"
    NY_PROMO = "NY_promo"
    PLUS_ITOGI = "plus_itogi"
