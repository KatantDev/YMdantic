from typing import Optional

from pydantic import AnyUrl

from ymdantic.models.base import YMBaseModel


class ActionButton(YMBaseModel):
    """Pydantic модель, представляющая кнопку действия."""

    text: str
    # Текст кнопки.
    url: AnyUrl
    # Ссылка, которая откроется при нажатии на кнопку.
    color: str
    # Цвет кнопки.
    view_browser: Optional[bool] = None
    # Флаг, указывающий на то, что ссылка должна открываться в браузере.
