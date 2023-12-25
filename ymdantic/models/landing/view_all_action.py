from typing import Optional

from ymdantic.models.base import YMBaseModel


class ViewAllAction(YMBaseModel):
    """Pydantic модель, представляющая информацию о при нажатии на кнопку."""

    deeplink: str
    # Deeplink действия.
    weblink: Optional[str] = None
    # Weblink действия (для сайта).
