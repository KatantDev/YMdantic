import sys

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from strenum import StrEnum


class SpecialEnum(StrEnum):
    """Перечисление, представляющее типы специальных блоков на главной странице."""

    NY_2023_FORU = "NY_2023_foru"
    KARTOCHKI_MOBILE = "KARTOCHKI_mobile"
