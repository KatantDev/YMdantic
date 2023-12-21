from pydantic import BaseModel, ConfigDict, model_validator
from typing import Dict, Any

from ymdantic.adapters import to_camel


class YMBaseModel(BaseModel):
    """Базовая Pydantic модель для всех будущих моделей."""

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra="forbid",
    )


class RemoveDeprecated:
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
