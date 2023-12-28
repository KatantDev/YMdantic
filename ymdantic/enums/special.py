from enum import Enum


class SpecialEnum(str, Enum):
    """Перечисление, представляющее типы специальных блоков на главной странице."""

    NY_2023_FORU = "NY_2023_foru"
    KARTOCHKI_MOBILE = "KARTOCHKI_mobile"
