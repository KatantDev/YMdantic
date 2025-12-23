from ymdantic.models.base import YMBaseModel


class Counts(YMBaseModel):
    """Pydantic модель, представляющая количество треков и альбомов у артиста."""

    tracks: int
    # Количество личных треков у артиста.
    direct_albums: int
    # Количество личных альбомов у артиста.
    also_albums: int
    # Количество альбомов, в которых участвует артист.
    also_tracks: int
    # Количество треков, в которых участвует артист.
