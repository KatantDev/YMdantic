from pydantic import TypeAdapter
from typing import Any, Dict

from ymdantic.models.base import YMBaseModel


class PydanticFactory:
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
