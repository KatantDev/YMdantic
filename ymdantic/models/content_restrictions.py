from typing import Annotated

from pydantic import Field

from ymdantic.models.base import YMBaseModel


class ContentRestrictions(YMBaseModel):
    """Pydantic модель, представляющая ограничения контента."""

    available: bool = False
    # Флаг, указывающий, доступен ли контент.
    disclaimers: Annotated[list[str], Field(default_factory=list)]
