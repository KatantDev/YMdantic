from typing import Literal, Optional

from ymdantic.models.base import YMBaseModel
from ymdantic.models.landing.skeleton.tab_source import TabSource
from ymdantic.models.landing.view_all_action import ViewAllAction


class TabData(YMBaseModel):
    """Pydantic модель, представляющая информацию о блоке вкладки."""

    show_policy: Literal["SHOW_AND_LOAD", "LOAD_AND_SHOW"]
    # Политика показа.
    title: Optional[str] = None
    # Заголовок вкладки.
    description: Optional[str] = None
    # Описание вкладки.
    playlist_type: Optional[str] = None
    # Тип плейлиста.
    view_all_action: Optional[ViewAllAction] = None
    # Действие на кнопке "Смотреть все".
    source: Optional[TabSource] = None
    # Источник данных.
