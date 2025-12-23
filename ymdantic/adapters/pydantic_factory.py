from typing import Any, Optional, Type, TypeVar

from pydantic import TypeAdapter

from ymdantic.adapters.to_query_params import bools_to_str

TypeT = TypeVar("TypeT")


class PydanticFactory:
    """Фабрика для преобразования данных в pydantic модели."""

    def load(self, data: Any, type_: Type[TypeT]) -> TypeT:
        """
        Преобразование данных в pydantic модель.

        :param data: Данные для преобразования.
        :param type_: Тип модели.
        :return: Преобразованные данные.
        """
        client = data.pop("__client")
        return TypeAdapter(type_).validate_python(
            data,
            context={"client": client},
        )

    def dump(
        self,
        data: TypeT,
        class_: Optional[Type[TypeT]] = None,
    ) -> Any:
        """
        Преобразование данных в pydantic модель.

        :param data: Данные для преобразования.
        :param class_: Тип модели.
        :return: Преобразованные данные.
        """
        if class_ is None:
            return None
        result = TypeAdapter(class_).dump_python(data, by_alias=True, exclude_none=True)
        if isinstance(result, dict) and result.get("params"):
            return bools_to_str(result["params"])
        return result
