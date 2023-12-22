from typing import Dict, Any, TYPE_CHECKING

from pydantic import model_validator, ValidationInfo

if TYPE_CHECKING:
    from ymdantic import YMClient


class ClientMixin:
    """Миксин, добавляющий в Pydantic модель клиент для отправки запросов."""

    __client: "YMClient"

    @model_validator(mode="before")
    def inject_ym_client(
        cls,
        obj: Dict[str, Any],
        info: ValidationInfo,
    ) -> Dict[str, Any]:
        """
        Валидатор, добавляющий в модель клиент для отправки запросов.

        :param obj: Словарь с данными модели.
        :param info: Информация о валидации.
        :return: Словарь с данными модели.
        """
        if info.context is not None:
            cls.__client = info.context.get("client")
        return obj


class DeprecatedMixin:
    """Миксин, удаляющий устаревшие поля из модели."""

    @model_validator(mode="before")
    def remove_deprecated(cls, obj: Dict[str, Any]) -> Dict[str, Any]:
        """
        Удаляет устаревшие поля из модели.

        :param obj: Словарь с данными модели.
        :return: Словарь с данными модели без устаревших полей.
        """
        obj.pop("substituted", None)
        obj.pop("deprecation", None)
        obj.pop("decomposed", None)
        if obj.get("version") is not None:
            obj["title"] += f" ({obj.get('version')})"
            obj.pop("version")
        return obj
