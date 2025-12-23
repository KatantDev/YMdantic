import sys

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from strenum import StrEnum


class YandexLanguage(StrEnum):
    """Перечисление, представляющее языки в Yandex Music."""

    RUSSIAN = "ru"
    ENGLISH = "en"
