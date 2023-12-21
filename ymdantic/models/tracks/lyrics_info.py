from ymdantic.models.base import YMBaseModel


class LyricsInfo(YMBaseModel):
    """
    Pydantic модель, представляющая информацию о наличии текста песни.

    Наличие текста и синхронизированных текстов песни.
    """

    has_available_sync_lyrics: bool
    # Флаг, указывающий на наличие синхронизированных текстов песни.
    has_available_text_lyrics: bool
    # Флаг, указывающий на наличие текста песни.
