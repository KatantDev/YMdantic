from datetime import datetime
from typing import Literal, Optional

from ymdantic.models.base import YMBaseModel, YMPostBaseModel


class SetAccountSettingsParams(YMPostBaseModel):
    """Pydantic модель для установки настроек аккаунта (POST)."""

    last_fm_scrobbling_enabled: Optional[bool] = None
    # Включено ли скробблирование в Last.fm.
    facebook_scrobbling_enabled: Optional[bool] = None
    # Включено ли скробблирование в Facebook.
    shuffle_enabled: Optional[bool] = None
    # Включено ли перемешивание.
    add_new_track_on_playlist_top: Optional[bool] = None
    # Добавлять ли новые треки в начало плейлиста.
    volume_percents: Optional[int] = None
    # Громкость в процентах.
    user_music_visibility: Optional[Literal["PUBLIC", "PRIVATE"]] = None
    # Видимость музыки пользователя.
    user_social_visibility: Optional[Literal["PUBLIC", "PRIVATE"]] = None
    # Видимость социальной активности пользователя.
    ads_disabled: Optional[bool] = None
    # Отключена ли реклама.
    rbt_disabled: Optional[bool] = None
    # Отключены ли РБТ.
    theme: Optional[Literal["black", "white"]] = None
    # Тема.
    promos_disabled: Optional[bool] = None
    # Отключены ли промо-акции.
    auto_play_radio: Optional[bool] = None
    # Автовоспроизведение радио.
    sync_queue_enabled: Optional[bool] = None
    # Включена ли синхронизация очереди.
    explicit_forbidden: Optional[bool] = None
    # Запрещен ли контент с ненормативной лексикой.
    child_mod_enabled: Optional[bool] = None
    # Включен ли режим для детей.
    wizard_is_passed: Optional[bool] = None
    # Прошел ли пользователь визард.


class AccountSettings(YMBaseModel):
    """Pydantic модель настроек аккаунта."""

    uid: int
    # Уникальный идентификатор пользователя.
    last_fm_scrobbling_enabled: bool
    # Включено ли скробблирование в Last.fm.
    facebook_scrobbling_enabled: bool
    # Включено ли скробблирование в Facebook.
    shuffle_enabled: bool
    # Включено ли перемешивание.
    add_new_track_on_playlist_top: bool
    # Добавлять ли новые треки в начало плейлиста.
    volume_percents: int
    # Громкость в процентах.
    user_music_visibility: Literal["PUBLIC", "PRIVATE"]
    # Видимость музыки пользователя.
    user_social_visibility: Literal["PUBLIC", "PRIVATE"]
    # Видимость социальной активности пользователя.
    ads_disabled: bool
    # Отключена ли реклама.
    modified: datetime
    # Дата последнего изменения настроек.
    rbt_disabled: bool
    # Отключены ли РБТ.
    theme: Literal["black", "white"]
    # Тема.
    promos_disabled: bool
    # Отключены ли промо-акции.
    auto_play_radio: bool
    # Автовоспроизведение радио.
    sync_queue_enabled: bool
    # Включена ли синхронизация очереди.
    explicit_forbidden: bool
    # Запрещен ли контент с ненормативной лексикой.
    child_mod_enabled: bool
    # Включен ли режим для детей.
    wizard_is_passed: bool
    # Прошел ли пользователь визард.
    user_collection_hue: int
    # Цвет коллекции пользователя.
    child_mode_changed_by_user: bool
    # Изменил ли пользователь режим для детей.
