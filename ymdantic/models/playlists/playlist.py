from datetime import datetime
from typing import Literal, List, Optional, Annotated

from pydantic import HttpUrl, BeforeValidator

from ymdantic.models.action_button import ActionButton
from ymdantic.models.base import YMBaseModel
from ymdantic.models.custom_wave import CustomWave
from ymdantic.models.pager import Pager
from ymdantic.models.playlists.owner import PlaylistOwner
from ymdantic.models.playlists.playlist_cover import PlaylistCover
from ymdantic.models.playlists.playlist_track import PlaylistTrack
from ymdantic.models.playlists.tag import Tag

BackgroundColor = Annotated[
    Optional[str],
    BeforeValidator(lambda color: color if color else None),
]


class BasePlaylist(YMBaseModel):
    """Pydantic модель, представляющая базовую информацию о плейлисте."""

    owner: PlaylistOwner
    # Владелец плейлиста.
    available: bool
    # Доступность плейлиста.
    uid: int
    # Уникальный идентификатор пользователя.
    kind: int
    # Вид плейлиста.
    title: str
    # Название плейлиста.
    revision: int
    # Ревизия плейлиста.
    snapshot: int
    # Снимок плейлиста.
    track_count: int
    # Количество треков в плейлисте.
    visibility: Literal["public"]
    # Видимость плейлиста.
    collective: bool
    # Коллективный плейлист.
    created: datetime
    # Дата создания плейлиста.
    modified: datetime
    # Дата последнего изменения плейлиста.
    is_banner: bool
    # Является ли плейлист баннером.
    is_premiere: bool
    # Является ли плейлист премьерой.
    duration_ms: int
    # Длительность плейлиста в миллисекундах.
    cover: PlaylistCover
    # Обложка плейлиста.
    og_image: str
    # OG-изображение плейлиста. Может быть преобразовано в URL.
    tags: List[Tag]
    # Теги плейлиста.
    playlist_uuid: Optional[str] = None
    # UUID плейлиста.


class ShortPlaylist(BasePlaylist):
    """Pydantic модель, представляющая краткую информацию о плейлисте."""

    id_for_from: Optional[str] = None
    # Идентификатор для источника плейлиста.
    og_title: Optional[str] = None
    # OG-заголовок плейлиста.
    description: Optional[str] = None
    # Описание плейлиста.
    description_formatted: Optional[str] = None
    # Отформатированное описание плейлиста.
    custom_wave: Optional[CustomWave] = None
    # Пользовательская волна плейлиста.
    last_owner_playlists: Optional[List["ShortPlaylist"]] = None
    # Последние плейлисты владельца.
    likes_count: Optional[int] = None
    # Количество лайков плейлиста.
    background_image_url: Optional[str] = None
    # URL фонового изображения плейлиста.
    background_video_url: Optional[HttpUrl] = None
    # URL фонового видео плейлиста.
    image: Optional[Literal[""]] = None
    # Изображение плейлиста.
    text_color: Optional[str] = None
    # Цвет текста плейлиста.
    action_button: Optional[ActionButton] = None
    # Кнопка действия плейлиста.
    background_color: BackgroundColor = None
    # Цвет фона плейлиста.
    child_content: Optional[bool] = None
    # Содержит ли плейлист детский контент.


class Playlist(ShortPlaylist):
    """Pydantic модель, представляющая информацию о плейлисте с треками."""

    tracks: List[PlaylistTrack]
    # Список треков в плейлисте.
    similar_playlists: Optional[List[ShortPlaylist]] = None
    # Список похожих плейлистов.
    pager: Pager
    # Объект пейджера, содержащий информацию о пагинации.
