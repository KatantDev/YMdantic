from typing import List, Optional, Dict, Any, Literal

from pydantic import model_validator, HttpUrl

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
    disclaimers: List[Literal[""]]  # TODO: Проверить, что тут может быть.
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

    def get_cover_image_url(self, size: str = "200x200") -> Optional[HttpUrl]:
        """
        Возвращает URL изображения обложки артиста с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения обложки артиста с заданным размером.
        """
        if self.cover is None:
            return None
        return self.cover.get_image_url(size)
