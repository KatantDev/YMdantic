from typing import Literal, Optional

from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel


class CustomWave(YMBaseModel):
    """Pydantic модель, представляющая пользовательскую волну."""

    title: str
    # Заголовок пользовательской волны.
    animation_url: HttpUrl
    # URL анимации пользовательской волны.
    header: str
    # Заголовок пользовательской волны.
    position: Optional[Literal["default"]] = None
    # Позиция пользовательской волны.
