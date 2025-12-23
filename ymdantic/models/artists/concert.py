from ymdantic.models.artists.artist import Artist
from ymdantic.models.concerts.concert import BaseConcert


class ArtistConcert(BaseConcert):
    """Pydantic модель, представляющая концерт артиста."""

    artist: Artist
    # Артист, который выступает на концерте.
