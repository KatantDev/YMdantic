from typing import Dict, Any, TYPE_CHECKING
from typing_extensions import Self

from pydantic import model_validator, PrivateAttr, BaseModel

if TYPE_CHECKING:
    from ymdantic import YMClient


class ClientMixin(BaseModel):
    """Миксин, добавляющий в Pydantic модель клиент для отправки запросов."""

    _client: "YMClient" = PrivateAttr()

    def model_post_init(self, __context: Any) -> None:
        """
        После инициализации модели миксин добавляет в данные модели инстанс клиента.

        :param __context: Контекст при валидации модели.
        """
        self._client = __context.get("bot") if __context else None

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
