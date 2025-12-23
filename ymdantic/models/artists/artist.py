from pydantic import HttpUrl

from ymdantic.mixins import DeprecatedMixin
from ymdantic.models.artists.counts import Counts
from ymdantic.models.artists.extra_action import ExtraAction
from ymdantic.models.artists.ratings import Ratings
from ymdantic.models.artists.social_link import SocialLink
from ymdantic.models.base import YMBaseModel
from ymdantic.models.cover import Cover


class ShortArtist(YMBaseModel, DeprecatedMixin):
    """Pydantic модель, представляющая краткую информацию об артисте."""

    id: int
    # Уникальный идентификатор артиста.
    name: str
    # Имя артиста.
    various: bool
    # Флаг, указывающий, является ли артист группой.
    composer: bool
    # Флаг, указывающий, является ли артист композитором.
    genres: list[str]
    # Жанры треков артиста.
    disclaimers: list[str]  # TODO: Проверить, что тут может быть.
    # Список отказов от ответственности артиста.
    cover: Cover | None = None
    # Обложка артиста.

    def get_cover_image_url(self, size: str = "200x200") -> HttpUrl | None:
        """
        Возвращает URL изображения обложки артиста с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения обложки артиста с заданным размером.
        """
        if self.cover is None:
            return None
        return self.cover.get_image_url(size)


class SimilarArtist(ShortArtist):
    """Pydantic модель, представляющая похожего артиста."""

    available: bool
    # Флаг, указывающий, доступен ли артист для прослушивания.
    counts: Counts
    # Счетчики артиста (количество треков, альбомов).
    tickets_available: bool
    # Флаг, указывающий, доступны ли билеты на концерты артиста.


class Artist(SimilarArtist):
    """Pydantic модель, представляющая подробную информацию об артисте."""

    og_image: str
    # OG изображение артиста.
    ratings: Ratings | None = None  # TODO: Проверить может ли быть None у доступных
    # Рейтинги артиста.
    links: list[SocialLink]
    # Список ссылок на социальные сети артиста.
    likes_count: int
    # Количество лайков артиста.
    db_aliases: list[str]
    # Список псевдонимов артиста в базе данных (для поиска).
    extra_actions: list[ExtraAction]

    def get_og_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает URL OG-изображения артиста с заданным размером.

        :param size: Размер изображения.
        :return: URL OG-изображения артиста с заданным размером.
        """
        return HttpUrl(f"https://{self.og_image.replace('%%', size)}")
