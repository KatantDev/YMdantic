"""Модели информации о наличии текста песни."""

from ymdantic.models.base import YMBaseModel


class LyricsInfo(YMBaseModel):
    """
    Модель информации о наличии текста песни.

    Наличие текста и синхронизированных текстов песни.
    """

    has_available_sync_lyrics: bool
    # Флаг, указывающий на наличие синхронизированных текстов песни.
    has_available_text_lyrics: bool
    # Флаг, указывающий на наличие текста песни.
