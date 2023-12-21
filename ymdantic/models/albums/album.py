from datetime import date, datetime
from typing import List, Optional, Any, Dict, Literal, TYPE_CHECKING

from pydantic import model_validator, HttpUrl

from ymdantic.models.action_button import ActionButton
from ymdantic.models.albums.label import Label
from ymdantic.models.base import YMBaseModel, RemoveDeprecated
from ymdantic.models.artists import Artist
from ymdantic.models.custom_wave import CustomWave
from ymdantic.models.pager import Pager

if TYPE_CHECKING:
    from ymdantic.models.tracks import TrackType

AvailableForOptions = List[Literal["bookmate"]]
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


class YMBaseAlbum(YMBaseModel, RemoveDeprecated):
    """Pydantic модель, представляющая информацию, присущую всем альбомам."""

    id: int
    # Уникальный идентификатор альбома.
    title: str
    # Название альбома.
    meta_type: Literal["music", "podcast"]
    # Мета-тип альбома.
    og_image: str
    # OG-изображение альбома.
    genres: List[str]
    # Жанры альбома.
    track_count: int
    # Количество треков в альбоме.
    recent: bool
    # Флаг, указывающий, является ли альбом недавним.
    very_important: bool
    # Флаг, указывающий, является ли альбом очень важным.
    artists: List[Artist]
    # Список артистов альбома.
    labels: List[Label]
    # Список лейблов альбома.
    available: bool
    # Флаг, указывающий, доступен ли альбом.
    available_for_premium_users: bool
    # Флаг, указывающий, доступен ли альбом для премиум-пользователей.
    available_for_options: AvailableForOptions
    # Список опций, для которых доступен альбом.
    available_for_mobile: bool
    # Флаг, указывающий, доступен ли альбом для мобильных устройств.
    available_partially: bool
    # Флаг, указывающий, доступен ли альбом частично.
    bests: List[int]
    # Список лучших треков альбома.
    disclaimers: List[str]
    # Список отказов от ответственности альбома.
    short_description: Optional[str] = None
    # Краткое описание альбома.
    description: Optional[str] = None
    # Описание альбома.
    content_warning: Optional[str] = None
    # Предупреждение о содержании альбома.
    year: Optional[int] = None
    # Год выпуска альбома.
    release_date: Optional[datetime] = None
    # Дата выпуска альбома.
    cover_uri: Optional[str] = None
    # URI обложки альбома.
    # Может быть использовано для получения обложки альбома.
    likes_count: Optional[int] = None
    # Количество лайков альбома.
    child_content: Optional[bool] = None
    # Флаг, указывающий, является ли альбом детским.
    type: Optional[AlbumType] = None
    # Тип альбома.
    background_image_url: Optional[str] = None
    # URL фонового изображения альбома.
    background_video_url: Optional[HttpUrl] = None
    # URL фонового видео альбома.
    action_button: Optional[ActionButton] = None
    # Кнопка действия альбома.

    @model_validator(mode="before")
    def validate_genres(cls, album: Dict[str, Any]) -> Dict[str, Any]:
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


class ShortAlbum(YMBaseAlbum):
    """Pydantic модель, представляющая краткую информацию об альбоме."""

    is_banner: Optional[bool] = None
    # Флаг, указывающий, является ли альбом баннером.
    is_premiere: Optional[bool] = None
    # Флаг, указывающий, является ли альбом премьерой.
    meta_tag_id: Optional[str] = None
    # Идентификатор мета-тега альбома.
    start_date: Optional[date] = None
    # Дата начала альбома.


class Album(ShortAlbum):
    """Pydantic модель, представляющая информацию об альбоме с треками."""

    volumes: List[List["TrackType"]]
    # Список пластинок альбома. Каждый том - это список треков.
    sort_order: SortOrder
    # Порядок сортировки альбома.
    pager: Pager
    # Объект пейджера, содержащий информацию о пагинации.
    custom_wave: Optional[CustomWave] = None
    # Пользовательская волна альбома.
    duration_sec: Optional[int] = None
    # Длительность альбома в секундах.
    duplicates: Optional[List["ShortAlbum"]] = None
    # Список дубликатов альбома.
