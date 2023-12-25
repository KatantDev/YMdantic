from typing import TypeVar, Generic, List

from ymdantic.models.base import YMBaseModel

ResponseVar = TypeVar("ResponseVar")


class EditorialResponse(YMBaseModel, Generic[ResponseVar]):
    """Pydantic модель ответа на запрос редакционных подборок."""

    items: List[ResponseVar]
