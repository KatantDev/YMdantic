from typing import Literal

from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel


class SocialLink(YMBaseModel):
    """Pydantic модель, представляющая ссылку на социальную сеть."""

    title: str
    # Имя артиста в социальной сети.
    href: HttpUrl
    # Ссылка на артиста в социальной сети.
    type: Literal["social"]
    # Тип ссылки. Возможные значения: "social".
    social_network: str
