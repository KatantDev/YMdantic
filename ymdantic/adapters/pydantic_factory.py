from pydantic import TypeAdapter
from typing import Any, Dict


class PydanticFactory:
    @staticmethod
    def load(data: Dict[str, Any], type_: Any) -> Any:
        return TypeAdapter(type_).validate_python(data)

    @staticmethod
    def dump(data: Dict[str, Any], type_: Any) -> Any:
        return TypeAdapter(type_).dump_python(data)
