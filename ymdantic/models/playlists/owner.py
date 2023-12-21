from typing import Literal

from ymdantic.models.base import YMBaseModel


class PlaylistOwner(YMBaseModel):
    """Pydantic модель, представляющая владельца плейлиста."""

    uid: int
    # Уникальный идентификатор пользователя.
    login: str
    # Логин пользователя.
    name: str
    # Имя пользователя.
    sex: Literal["male", "female", "unknown"]
    # Пол пользователя.
    verified: bool
    # Флаг, указывающий, подтвержден ли пользователь.
