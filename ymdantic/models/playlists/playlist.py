from datetime import datetime
from typing import Literal, List, Optional

from pydantic import HttpUrl, field_validator

from ymdantic.models.action_button import ActionButton
from ymdantic.models.base import YMBaseModel
from ymdantic.models.custom_wave import CustomWave
from ymdantic.models.pager import Pager
from ymdantic.models.playlists.owner import PlaylistOwner
from ymdantic.models.playlists.cover import PlaylistCover
from ymdantic.models.playlists.track import PlaylistTrack
from ymdantic.models.playlists.tag import Tag


class BasePlaylist(YMBaseModel):
    """Pydantic модель, представляющая базовую информацию о плейлисте."""

    owner: PlaylistOwner
    # Владелец плейлиста.
    available: bool
    # Доступность плейлиста.
    uid: int
    # Уникальный идентификатор пользователя.
    kind: int  # TODO: Проверить, что тут может быть.
    # Вид плейлиста. Известно, что при значении 3 - понравившиеся треки.
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
    og_image: str
    # OG-изображение плейлиста. Может быть преобразовано в URL.
    playlist_uuid: Optional[str] = None
    # UUID плейлиста.

    def get_og_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает URL OG-изображения плейлиста.

        :return: URL OG-изображения плейлиста.
        """
        return HttpUrl(f"https://{self.og_image.replace('%%', size)}")


class ShortPlaylist(BasePlaylist):
    """Pydantic модель, представляющая краткую информацию о плейлисте."""

    cover: PlaylistCover
    # Обложка плейлиста.
    tags: List[Tag]
    # Теги плейлиста.
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
    background_color: Optional[str] = None
    # Цвет фона плейлиста.
    child_content: Optional[bool] = None
    # Содержит ли плейлист детский контент.

    def get_cover_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает URL изображения обложки плейлиста с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения обложки плейлиста с заданным размером.
        """
        return self.cover.get_image_url(size)

    @field_validator("background_color", mode="before")
    @classmethod
    def validate_background_color(cls, v: Optional[str] = None) -> Optional[str]:
        if not v:
            return None
        return v

    def get_background_image_url(self, size: str = "200x200") -> Optional[HttpUrl]:
        """
        Возвращает URL изображения фона плейлиста с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения фона плейлиста с заданным размером.
        """
        if self.background_image_url is None:
            return None
        return HttpUrl(f"https://{self.background_image_url.replace('%%', size)}")


class Playlist(ShortPlaylist):
    """Pydantic модель, представляющая информацию о плейлисте с треками."""

    tracks: List[PlaylistTrack]
    # Список треков в плейлисте.
    similar_playlists: Optional[List[ShortPlaylist]] = None
    # Список похожих плейлистов.
    pager: Pager
    # Объект пейджера, содержащий информацию о пагинации.
