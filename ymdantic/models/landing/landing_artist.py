from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.landing_cover import LandingCover


class LandingArtist(YMBaseModel):
    """Pydantic модель, представляющая информацию о LandingArtist."""

    id: int
    # Уникальный идентификатор артиста.
    name: str
    # Имя артиста.
    cover: LandingCover
    # Обложка артиста. Содержит информацию о цветах обложки и URI обложки.
