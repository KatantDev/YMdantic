from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel


class ArtistDescription(YMBaseModel):
    """Pydantic модель, представляющая описание артиста."""

    text: str
    # Описание артиста.
    uri: HttpUrl
    # Ссылка на описание артиста.
