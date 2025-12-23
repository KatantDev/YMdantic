from pydantic import BaseModel, ConfigDict

from ymdantic.adapters.to_camel import to_camel
from ymdantic.mixins import ClientMixin


class YMBaseModel(BaseModel, ClientMixin):
    """Базовая Pydantic модель для всех будущих моделей."""

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra="allow",
    )
