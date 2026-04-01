from ymdantic.models.base import YMBaseModel


class Trailer(YMBaseModel):
    """Pydantic модель, представляющая трейлер альбома."""

    available: bool
    # Доступность трейлера.
