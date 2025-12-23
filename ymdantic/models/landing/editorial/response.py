from typing import Generic, List, TypeVar

from ymdantic.models.base import YMBaseModel

ResponseVar = TypeVar("ResponseVar")


class EditorialResponse(YMBaseModel, Generic[ResponseVar]):
    """Pydantic модель ответа на запрос редакционных подборок."""

    items: List[ResponseVar]
