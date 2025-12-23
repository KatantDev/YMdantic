from typing import Any

from pydantic import TypeAdapter

from ymdantic.models.base import YMBaseModel


class PydanticFactory:
    """Фабрика для преобразования данных в pydantic модели."""

    @staticmethod
    def load(data: dict[str, Any], type_: Any) -> Any:
        """
        Преобразование данных в pydantic модель.

        :param data: Данные для преобразования.
        :param type_: Тип модели.
        :return: Преобразованные данные.
        """
        client = data.pop("__client")
        model: YMBaseModel = TypeAdapter(type_).validate_python(
            data,
            context={"client": client},
        )
        return model

    @staticmethod
    def dump(data: dict[str, Any], type_: Any) -> Any:
        """
        Преобразование данных в pydantic модель.

        :param data: Данные для преобразования.
        :param type_: Тип модели.
        :return: Преобразованные данные.
        """
        return TypeAdapter(type_).dump_python(data)
