from pydantic import BaseModel


class YandexMusicErrorModel(BaseModel):
    """Pydantic модель, представляющая ошибку в API Яндекс.Музыки."""

    name: str
    # Название ошибки.
    message: str
    # Сообщение об ошибке.
