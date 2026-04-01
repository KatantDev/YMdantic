from ymdantic.models.base import YMBaseModel
from ymdantic.models.cover import ShortCover


class Agent(YMBaseModel):
    """Pydantic модель, представляющая информацию об агенте."""

    animation_uri: str
    # URI анимации агента.
    cover: ShortCover
    # Обложка агента.
