from typing import List, Optional, Dict, Any

from pydantic import model_validator

from ymdantic.models.base import YMBaseModel, RemoveDeprecated
from ymdantic.models.cover import Cover


class Artist(YMBaseModel, RemoveDeprecated):
    """Pydantic модель, представляющая информацию об артисте."""

    id: int
    # Уникальный идентификатор артиста.
    name: str
    # Имя артиста.
    various: bool
    # Флаг, указывающий, является ли артист группой.
    composer: bool
    # Флаг, указывающий, является ли артист композитором.
    genres: List[str]
    # Жанры треков артиста.
    disclaimers: List[str]
    # Список отказов от ответственности артиста.
    cover: Optional[Cover] = None

    # Обложка артиста.

    @model_validator(mode="before")
    def validate_genres(cls, artist: Dict[str, Any]) -> Dict[str, Any]:
        """
        Этот метод класса конвертирует жанры в данных об артисте в новый вид.

        Он проверяет, присутствует ли ключ 'genre' в словаре альбома. Если
        он присутствует, он присваивает список, содержащий жанр,
        ключу 'genres' словаря альбома. Если ключ 'genre' отсутствует,
        он присваивает пустой список ключу 'genres'.

        :param artist: Словарь, содержащий информацию об артисте.
        :return: Словарь, содержащий информацию об артисте с конвертированными
            жанрами.
        """
        genre = artist.get("genre")
        artist.pop("genre", None)
        artist["genres"] = [genre] if genre else []
        return artist
