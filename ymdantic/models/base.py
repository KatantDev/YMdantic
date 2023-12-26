from pydantic import BaseModel, ConfigDict

from ymdantic.adapters.to_camel import to_camel
from ymdantic.mixins import ClientMixin


class YMBaseModel(ClientMixin, BaseModel):
    """Базовая Pydantic модель для всех будущих моделей (GET)."""

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra="forbid",
    )


class YMPostBaseModel(ClientMixin, BaseModel):
    """Базовая Pydantic модель для всех будущих моделей (POST)."""

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        json_encoders={
            bool: lambda value: str(value).lower(),
        },
    )
