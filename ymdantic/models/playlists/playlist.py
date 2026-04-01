from datetime import datetime
from typing import Annotated, Literal

from pydantic import Field, HttpUrl, field_validator

from ymdantic.models.action_button import ActionButton
from ymdantic.models.base import YMBaseModel
from ymdantic.models.custom_wave import CustomWave
from ymdantic.models.pager import Pager
from ymdantic.models.playlists.cover import PlaylistCover
from ymdantic.models.playlists.owner import PlaylistOwner
from ymdantic.models.playlists.tag import Tag
from ymdantic.models.playlists.track import PlaylistTrack


class BasePlaylist(YMBaseModel):
    """Pydantic модель, представляющая базовую информацию о плейлисте."""

    uid: int
    # Уникальный идентификатор пользователя.
    kind: int
    # Вид плейлиста. Известно, что при значении 3 - понравившиеся треки.
    title: str
    # Название плейлиста.
    playlist_uuid: str | None = None
    # UUID плейлиста.
    description: str | None = None
    # Описание плейлиста.
    description_formatted: str | None = None
    # Отформатированное описание плейлиста.
    cover: PlaylistCover | None = None
    # Обложка плейлиста.
    track_count: int
    # Количество треков в плейлисте.
    likes_count: int | None = None
    # Количество лайков плейлиста.
    artist_playlist_type: str | None = None
    # Тип плейлиста артиста.

    def get_cover_image_url(self, size: str = "200x200") -> HttpUrl | None:
        """
        Возвращает URL изображения обложки плейлиста с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения обложки плейлиста с заданным размером.
        """
        if self.cover is None:
            return None
        return self.cover.get_image_url(size)


class ShortPlaylist(BasePlaylist):
    """Pydantic модель, представляющая базовую информацию о плейлисте."""

    owner: PlaylistOwner
    # Владелец плейлиста.
    available: bool
    # Доступность плейлиста.
    revision: int
    # Ревизия плейлиста.
    snapshot: int
    # Снимок плейлиста.
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
    tags: Annotated[list[Tag], Field(default_factory=list)]
    # Теги плейлиста.
    id_for_from: str | None = None
    # Идентификатор для источника плейлиста.
    og_title: str | None = None
    # OG-заголовок плейлиста.
    custom_wave: CustomWave | None = None
    # Пользовательская волна плейлиста.
    last_owner_playlists: Annotated[list["ShortPlaylist"], Field(default_factory=list)]
    # Последние плейлисты владельца.
    background_image_url: str | None = None
    # URL фонового изображения плейлиста.
    background_video_url: HttpUrl | None = None
    # URL фонового видео плейлиста.
    image: str | None = None
    # Изображение плейлиста.
    text_color: str | None = None
    # Цвет текста плейлиста.
    action_button: ActionButton | None = None
    # Кнопка действия плейлиста.
    background_color: str | None = None
    # Цвет фона плейлиста.
    child_content: bool | None = None
    # Содержит ли плейлист детский контент.

    @field_validator("background_color", mode="before")
    @classmethod
    def validate_background_color(cls, v: str | None = None) -> str | None:
        """
        Валидатор цвета фона плейлиста.

        :param v: Цвет фона плейлиста.
        :return: Цвет фона плейлиста.
        """
        if not v:
            return None
        return v

    def get_background_image_url(self, size: str = "200x200") -> HttpUrl | None:
        """
        Возвращает URL изображения фона плейлиста с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения фона плейлиста с заданным размером.
        """
        if self.background_image_url is None:
            return None
        return HttpUrl(f"https://{self.background_image_url.replace('%%', size)}")

    def get_og_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает URL OG-изображения плейлиста.

        :return: URL OG-изображения плейлиста.
        """
        return HttpUrl(f"https://{self.og_image.replace('%%', size)}")


class Playlist(ShortPlaylist):
    """Pydantic модель, представляющая информацию о плейлисте с треками."""

    tracks: list[PlaylistTrack]
    # Список треков в плейлисте.
    similar_playlists: Annotated[list[ShortPlaylist], Field(default_factory=list)]
    # Список похожих плейлистов.
    pager: Pager
    # Объект пейджера, содержащий информацию о пагинации.
