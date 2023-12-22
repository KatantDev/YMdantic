from typing import List, Optional, Literal

from pydantic import HttpUrl

from ymdantic.models.artists import Artist
from ymdantic.models.base import YMBaseModel, RemoveDeprecated
from ymdantic.models.chart_position import ChartPosition
from ymdantic.models.tracks.r128 import R128
from ymdantic.models.tracks.fade import Fade
from ymdantic.models.tracks.derived_colors import DerivedColors
from ymdantic.models.tracks.track_album import TrackAlbum
from ymdantic.models.tracks.lyrics_info import LyricsInfo
from ymdantic.models.tracks.major import Major


AvailableForOptions = List[Literal["bookmate"]]
TrackSource = Literal["OWN", "OWN_REPLACED_TO_UGC"]


class BaseTrack(YMBaseModel, RemoveDeprecated):
    """Pydantic модель, представляющая базовую информацию о любом треке."""

    type: Literal["music", "asmr", "audiobook", "noise", "fairy-tale"]
    # Тип трека.
    id: str
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
    disclaimers: List[Literal["modal"]]
    # Список отказов от ответственности трека.
    artists: List[Artist]
    # Список артистов трека. Может быть пустым.
    albums: List[TrackAlbum]
    # Список альбомов трека. Может быть пустым.
    lyrics_available: bool
    # Доступность текста песни. Если текст песни доступен, то можно получить
    # текст песни по данным из LyricsInfo.
    remember_position: bool
    # Запоминать ли позицию трека. В типе "music" зачастую равен False.
    # В основном используется для подкастов, комментариев и аудиокниг.
    track_source: TrackSource
    # Источник трека
    major: Optional[Major] = None
    # Лейбл трека (если есть)
    r128: Optional[R128] = None
    # Значение R128 трека (если есть). R128 - это стандарт, который
    # определяет уровень громкости аудио.
    fade: Optional[Fade] = None
    # Значение затухания трека (если есть). Затухание - это изменение
    # громкости аудио на определенном участке.
    cover_uri: Optional[str] = None
    # URI обложки трека (если есть).
    og_image: Optional[str] = None
    # OG изображение трека (если есть). OG изображение - это изображение,
    # которое отображается при публикации ссылки на трек.
    derived_colors: Optional[DerivedColors] = None
    # Производные цвета трека (если есть). Производные цвета - это цвета,
    # которые были получены из обложки трека.
    clip_ids: Optional[List[int]] = None
    # Идентификаторы клипов трека. Клип - это видео, которое относится к треку.
    content_warning: Optional[str] = None
    # Предупреждение о содержании трека (если есть).
    is_suitable_for_children: Optional[bool] = None
    # Подходит ли трек для детей (если есть).
    background_video_uri: Optional[str] = None
    # URI фонового видео трека (если есть). Фоновое видео - это видео,
    # которое отображается вместо обложки трека.
    background_video_url: Optional[HttpUrl] = None
    # URL фонового видео трека (если есть). Фоновое видео - это видео,
    # которое отображается вместо обложки трека.
    player_id: Optional[str] = None
    # Идентификатор плеера трека (если есть). Плеер требуется для
    # отображения фонового видео.
    best: Optional[bool] = None
    # Является ли трек лучшим (поле доступно при получении альбома с треками
    # `get_album_with_tracks`).


class UnavailableTrack(BaseTrack):
    """
    Pydantic модель, представляющая недоступный трек.

    В случае, если трек недоступен, то его нельзя скачать и прослушать.
    Большинство полей, такие как: `storage_dir`, `available_for_options`,
    `duration_ms`, `preview_duration_ms`, `file_size` и `lyrics_info` по
    сути своей бесполезны для недоступных вида треков и зачастую
    отсутствуют. Но по какой-то причине в некоторых треках они всё же есть.
    """

    available: Literal[False]
    # Доступность трека. В данном случае трек недоступен.
    error: Optional[Literal["no-rights"]] = None
    # Ошибка, связанная с треком. В данном случае может быть ошибка
    # "no-rights", что означает отсутствие прав на трек.
    title: Optional[str] = None
    # Название трека. В данном случае название может отсутствовать
    # (возникает очень редко).
    track_sharing_flag: Optional[str] = None
    # Флаг, указывающий на возможность делиться треком. В данном случае
    # может отсутствовать (возникает очень редко).
    storage_dir: Optional[str] = None
    # Директория хранения трека. У недоступных треков почти всегда равна
    # пустой строке или отсутствует.
    available_for_options: Optional[AvailableForOptions] = None
    # Доступные опции для трека. В данном случае опции могут отсутствовать.
    duration_ms: Optional[int] = None
    # Длительность трека в миллисекундах. В данном случае длительность может
    # отсутствовать.
    preview_duration_ms: Optional[int] = None
    # Длительность предпросмотра трека в миллисекундах. В данном случае
    # длительность предпросмотра может отсутствовать.
    file_size: Optional[int] = None
    # Размер файла трека. В данном случае размер файла может отсутствовать.
    lyrics_info: Optional[LyricsInfo] = None
    # Информация о тексте песни. В данном случае информация о тексте песни
    # может отсутствовать.


class Track(BaseTrack):
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
    available_for_options: AvailableForOptions
    # Доступные опции для трека.
    chart: Optional[ChartPosition] = None
    # Информация о чарте, если трек входит в чарт.

    def get_cover_url(self, size: str = "200x200") -> HttpUrl:
        """
        Получает URL изображения обложки.

        :param size: Размер изображения обложки в пикселях.
            По умолчанию 200x200.
        :return: URL изображения обложки.
        """
        return HttpUrl(f"https://{self.cover_uri.replace('%%', size)}")
