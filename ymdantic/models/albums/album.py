from datetime import date, datetime
from typing import TYPE_CHECKING, Annotated, Any, Literal

from pydantic import Field, HttpUrl, model_validator

from ymdantic.mixins import DeprecatedMixin
from ymdantic.models.action_button import ActionButton
from ymdantic.models.albums.label import Label
from ymdantic.models.artists import ShortArtist
from ymdantic.models.base import YMBaseModel
from ymdantic.models.custom_wave import CustomWave
from ymdantic.models.pager import Pager

if TYPE_CHECKING:
    from ymdantic.models.tracks import TrackType

AlbumType = Literal[
    "single",
    "compilation",
    "music",
    "asmr",
    "audiobook",
    "noise",
    "fairy-tale",
    "podcast",
    "comment",
    "video-single",
]
SortOrder = Literal["asc", "desc"]


class BaseAlbum(YMBaseModel, DeprecatedMixin):
    """Модель информации, присущей всем альбомам."""

    id: int
    # Уникальный идентификатор альбома.
    title: str
    # Название альбома.
    meta_type: Literal["music", "podcast"]
    # Мета-тип альбома.
    og_image: str
    # OG-изображение альбома.
    genres: Annotated[list[str], Field(default_factory=list)]
    # Жанры альбома.
    track_count: int
    # Количество треков в альбоме.
    recent: bool
    # Флаг, указывающий, является ли альбом недавним.
    very_important: bool
    # Флаг, указывающий, является ли альбом очень важным.
    artists: list[ShortArtist]
    # Список артистов альбома.
    labels: list[Label]
    # Список лейблов альбома.
    available: bool
    # Флаг, указывающий, доступен ли альбом.
    available_for_premium_users: bool
    # Флаг, указывающий, доступен ли альбом для премиум-пользователей.
    available_for_options: Annotated[list[str], Field(default_factory=list)]
    # Список опций, для которых доступен альбом.
    available_for_mobile: bool
    # Флаг, указывающий, доступен ли альбом для мобильных устройств.
    available_partially: bool
    # Флаг, указывающий, доступен ли альбом частично.
    bests: list[int]
    # Список лучших треков альбома.
    disclaimers: list[str]
    # Список отказов от ответственности альбома.
    short_description: str | None = None
    # Краткое описание альбома.
    description: str | None = None
    # Описание альбома.
    content_warning: str | None = None
    # Предупреждение о содержании альбома.
    year: int | None = None
    # Год выпуска альбома.
    release_date: datetime | None = None
    # Дата выпуска альбома.
    cover_uri: str | None = None
    # URI обложки альбома.
    # Может быть использовано для получения обложки альбома.
    likes_count: int | None = None
    # Количество лайков альбома.
    child_content: bool | None = None
    # Флаг, указывающий, является ли альбом детским.
    type: AlbumType | None = None
    # Тип альбома.
    background_image_url: str | None = None
    # URL фонового изображения альбома.
    background_video_url: HttpUrl | None = None
    # URL фонового видео альбома.
    action_button: ActionButton | None = None
    # Кнопка действия альбома.

    @model_validator(mode="before")
    @classmethod
    def validate_genres(cls, album: dict[str, Any]) -> dict[str, Any]:
        """
        Этот метод класса конвертирует жанры в данных об альбоме в новый вид.

        Он проверяет, присутствует ли ключ 'genre' в словаре альбома. Если
        он присутствует, он присваивает список, содержащий жанр,
        ключу 'genres' словаря альбома. Если ключ 'genre' отсутствует,
        он присваивает пустой список ключу 'genres'.

        :param album: Словарь, содержащий информацию об альбоме.
        :return: Словарь, содержащий информацию об альбоме с конвертированными
            жанрами.
        """
        genre = album.pop("genre", None)
        album["genres"] = [genre] if genre is not None else []
        return album

    def get_og_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает URL OG-изображения альбома с заданным размером.

        :param size: Размер изображения.
        :return: URL OG-изображения альбома с заданным размером.
        """
        return HttpUrl(f"https://{self.og_image.replace('%%', size)}")

    def get_cover_image_url(self, size: str = "200x200") -> HttpUrl | None:
        """
        Возвращает URL изображения обложки альбома с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения обложки альбома с заданным размером.
        """
        if self.cover_uri is None:
            return None
        return HttpUrl(f"https://{self.cover_uri.replace('%%', size)}")

    def get_background_image_url(self, size: str = "200x200") -> HttpUrl | None:
        """
        Возвращает URL изображения фона альбома с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения фона альбома с заданным размером.
        """
        if self.background_image_url is None:
            return None
        return HttpUrl(f"https://{self.background_image_url.replace('%%', size)}")

    @property
    def artists_names(self) -> str | None:
        """
        Получает имена артистов альбома.

        :return: Имена артистов альбома.
        """
        if not self.artists:
            return None
        return ", ".join(artist.name for artist in self.artists)


class ShortAlbum(BaseAlbum):
    """Модель краткой информации об альбоме."""

    is_banner: bool | None = None
    # Флаг, указывающий, является ли альбом баннером.
    is_premiere: bool | None = None
    # Флаг, указывающий, является ли альбом премьерой.
    meta_tag_id: str | None = None
    # Идентификатор мета-тега альбома.
    start_date: date | None = None
    # Дата начала альбома.


class Album(ShortAlbum):
    """Модель информации об альбоме с треками."""

    volumes: list[list["TrackType"]]
    # Список пластинок альбома. Каждый том - это список треков.
    sort_order: SortOrder
    # Порядок сортировки альбома.
    pager: Pager
    # Объект пейджера, содержащий информацию о пагинации.
    custom_wave: CustomWave | None = None
    # Пользовательская волна альбома.
    duration_sec: int | None = None
    # Длительность альбома в секундах.
    duplicates: list["ShortAlbum"] | None = None
    # Список дубликатов альбома.
