from typing import TYPE_CHECKING, Any, Self

from pydantic import model_validator
from pydantic_core.core_schema import ValidationInfo

if TYPE_CHECKING:
    from ymdantic import YMClient


class ClientMixin:
    """Миксин, добавляющий в Pydantic модель клиент для отправки запросов."""

    _client: "YMClient"

    @model_validator(mode="before")
    @classmethod
    def inject_ym_client(
        cls,
        obj: dict[str, Any],
        info: ValidationInfo,
    ) -> dict[str, Any]:
        """
        Валидатор, добавляющий в модель клиент для отправки запросов.

        :param obj: Словарь с данными модели.
        :param info: Информация о валидации.
        :return: Словарь с данными модели.
        """
        if info.context is not None:
            cls._client = info.context.get("client")
        return obj

    def as_(self, client: "YMClient") -> Self:
        """
        Добавляет инстанс бота в уже созданный объект.

        Требуется, если мы не добавили его при валидации модели.

        :param client: Инстанс клиента
        :return: self
        """
        self._client = client
        return self


class DeprecatedMixin:
    """Миксин, удаляющий устаревшие поля из модели."""

    @model_validator(mode="before")
    @classmethod
    def remove_deprecated(cls, obj: dict[str, Any]) -> dict[str, Any]:
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
