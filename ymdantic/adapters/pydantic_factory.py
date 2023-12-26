from adaptix import Retort, TypeHint
from pydantic import TypeAdapter
from typing import Any, Dict, Optional

from ymdantic.models.base import YMBaseModel


class PydanticFactoryBody:
    @staticmethod
    def load(data: Dict[str, Any], type_: Any) -> Any:
        client = data.pop("__client")
        model: YMBaseModel = TypeAdapter(type_).validate_python(
            data,
            context={"client": client},
        )
        return model

    @staticmethod
    def dump(data: Dict[str, Any], type_: Any) -> Any:
        return TypeAdapter(type_).dump_python(data)


class PydanticFactoryArgs(Retort):
    def dump(self, data: Any, tp: Optional[TypeHint] = None, /) -> Any:
        params: Optional[YMBaseModel] = data.pop("params", None)
        if params is not None:
            return params.model_dump(mode="json", by_alias=True, exclude_none=True)
        return super().dump(data, tp)
