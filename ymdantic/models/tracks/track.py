"""Модели треков."""

from typing import Annotated, Literal

from pydantic import Field, HttpUrl

from ymdantic.mixins import DeprecatedMixin
from ymdantic.models.artists.artist import ShortArtist
from ymdantic.models.base import YMBaseModel
from ymdantic.models.chart_position import ChartPosition
from ymdantic.models.tracks.album import TrackAlbum
from ymdantic.models.tracks.derived_colors import DerivedColors
from ymdantic.models.tracks.download_info import DownloadInfo, DownloadInfoDirect
from ymdantic.models.tracks.fade import Fade
from ymdantic.models.tracks.lyrics_info import LyricsInfo
from ymdantic.models.tracks.major import Major
from ymdantic.models.tracks.r128 import R128

TrackSource = Literal["OWN", "OWN_REPLACED_TO_UGC"]


class BaseTrack(YMBaseModel, DeprecatedMixin):
    """Модель базовой информации о любом треке."""

    type: str
    # Тип трека.
    id: int
    # Идентификатор трека. Идентификатор трека - это уникальный
    # идентификатор, по которому можно получить трек.
    real_id: str
    # Реальный идентификатор трека. Заглушка для замещенных треков.
    available: bool
    # Доступность трека. В данном случае трек недоступен. Это влияет на то,
    # можно ли скачать и прослушать трек.
    available_for_premium_users: bool
    # Доступность трека для премиум пользователей.
    available_full_without_permission: bool
    # Полная доступность трека без разрешения.
    disclaimers: list[str]
    # Список отказов от ответственности трека.
    artists: list[ShortArtist]
    # Список артистов трека. Может быть пустым.
    albums: list[TrackAlbum]
    # Список альбомов трека. Может быть пустым.
    lyrics_available: bool
    # Доступность текста песни. Если текст песни доступен, то можно получить
    # текст песни по данным из LyricsInfo.
    remember_position: bool
    # Запоминать ли позицию трека. В типе "music" зачастую равен False.
    # В основном используется для подкастов, комментариев и аудиокниг.
    track_source: TrackSource
    # Источник трека
    major: Major | None = None
    # Лейбл трека (если есть)
    r128: R128 | None = None
    # Значение R128 трека (если есть). R128 - это стандарт, который
    # определяет уровень громкости аудио.
    fade: Fade | None = None
    # Значение затухания трека (если есть). Затухание - это изменение
    # громкости аудио на определенном участке.
    cover_uri: str | None = None
    # URI обложки трека (если есть).
    og_image: str | None = None
    # OG изображение трека (если есть). OG изображение - это изображение,
    # которое отображается при публикации ссылки на трек.
    derived_colors: DerivedColors | None = None
    # Производные цвета трека (если есть). Производные цвета - это цвета,
    # которые были получены из обложки трека.
    clip_ids: Annotated[list[int], Field(default_factory=list)]
    # Идентификаторы клипов трека. Клип - это видео, которое относится к треку.
    content_warning: str | None = None
    # Предупреждение о содержании трека (если есть).
    is_suitable_for_children: bool | None = None
    # Подходит ли трек для детей (если есть).
    background_video_uri: HttpUrl | None = None
    # URI фонового видео трека (если есть). Фоновое видео - это видео,
    # которое отображается вместо обложки трека.
    player_id: str | None = None
    # Идентификатор плеера трека (если есть). Плеер требуется для
    # отображения фонового видео.
    best: bool | None = None
    # Является ли трек лучшим (поле доступно при получении альбома с треками
    # `get_album_with_tracks`).

    @property
    def artists_names(self) -> str | None:
        """
        Получает имена артистов трека.

        :return: Имена артистов трека.
        """
        if not self.artists:
            return None
        return ", ".join(artist.name for artist in self.artists)

    def get_cover_image_url(self, size: str = "200x200") -> HttpUrl | None:
        """
        Получает URL изображения обложки.

        :param size: Размер изображения обложки в пикселях.
            По умолчанию 200x200.
        :return: URL изображения обложки.
        """
        if self.cover_uri is None:
            return None
        return HttpUrl(f"https://{self.cover_uri.replace('%%', size)}")

    def get_og_image_url(self, size: str = "200x200") -> HttpUrl | None:
        """
        Получает URL изображения обложки.

        :param size: Размер изображения обложки в пикселях.
            По умолчанию 200x200.
        :return: URL изображения обложки.
        """
        if self.og_image is None:
            return None
        return HttpUrl(f"https://{self.og_image.replace('%%', size)}")


class UnavailableTrack(BaseTrack):
    """
    Модель недоступного трека.

    В случае, если трек недоступен, то его нельзя скачать и прослушать.
    Большинство полей, такие как: `storage_dir`, `available_for_options`,
    `duration_ms`, `preview_duration_ms`, `file_size` и `lyrics_info` по
    сути своей бесполезны для недоступных вида треков и зачастую
    отсутствуют. Но по какой-то причине в некоторых треках они всё же есть.
    """

    type: Literal["music", "asmr", "audiobook", "noise", "fairy-tale"]
    # Тип трека.
    available: Literal[False]
    # Доступность трека. В данном случае трек недоступен.
    error: Literal["no-rights"] | None = None
    # Ошибка, связанная с треком. В данном случае может быть ошибка
    # "no-rights", что означает отсутствие прав на трек.
    title: str | None = None
    # Название трека. В данном случае название может отсутствовать
    # (возникает очень редко).
    track_sharing_flag: str | None = None
    # Флаг, указывающий на возможность делиться треком. В данном случае
    # может отсутствовать (возникает очень редко).
    storage_dir: str | None = None
    # Директория хранения трека. У недоступных треков почти всегда равна
    # пустой строке или отсутствует.
    available_for_options: Annotated[list[str], Field(default_factory=list)]
    # Доступные опции для трека. В данном случае опции могут отсутствовать.
    duration_ms: int | None = None
    # Длительность трека в миллисекундах. В данном случае длительность может
    # отсутствовать.
    preview_duration_ms: int | None = None
    # Длительность предпросмотра трека в миллисекундах. В данном случае
    # длительность предпросмотра может отсутствовать.
    file_size: int | None = None
    # Размер файла трека. В данном случае размер файла может отсутствовать.
    lyrics_info: LyricsInfo | None = None
    # Информация о тексте песни. В данном случае информация о тексте песни
    # может отсутствовать.


class Track(BaseTrack):
    """Модель доступного трека."""

    type: Literal["music", "asmr", "audiobook", "noise", "fairy-tale"]
    # Тип трека.
    available: Literal[True]
    # Доступность трека. В данном случае трек доступен.
    title: str
    # Название трека.
    track_sharing_flag: str
    # Флаг, указывающий на возможность делиться треком.
    storage_dir: str
    # Директория хранения трека.
    lyrics_info: LyricsInfo
    # Информация о тексте песни.
    duration_ms: int
    # Длительность трека в миллисекундах.
    preview_duration_ms: int
    # Длительность предпросмотра трека в миллисекундах.
    file_size: Literal[0]
    # Размер файла трека. Всегда равен 0, видимо старая заглушка.
    available_for_options: Annotated[list[str], Field(default_factory=list)]
    # Доступные опции для трека.
    chart: ChartPosition | None = None
    # Информация о чарте, если трек входит в чарт.

    async def get_download_info(self) -> list[DownloadInfo]:
        """
        Получает информацию для скачивания трека.

        :return: Информация для скачивания трека.
        """
        return await self._client.get_track_download_info(track_id=self.id)

    async def get_download_info_direct(self) -> list[DownloadInfoDirect]:
        """
        Получает информацию для скачивания трека + прямую ссылку.

        :return: Информация для скачивания трека + прямая ссылка.
        """
        return await self._client.get_track_download_info_direct(track_id=self.id)
