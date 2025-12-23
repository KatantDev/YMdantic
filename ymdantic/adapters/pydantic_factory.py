from typing import Any, Optional, Type, TypeVar

from pydantic import TypeAdapter

TypeT = TypeVar("TypeT")


class PydanticFactory:
    """Фабрика для преобразования данных в pydantic модели."""

    @staticmethod
    def load(data: Any, type_: Type[TypeT]) -> TypeT:
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

    @staticmethod
    def dump(
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
        return TypeAdapter(class_).dump_python(data)
