from typing import Generic, TypeVar

from pydantic import BaseModel, Field

from ymdantic.mixins import ClientMixin

ResponseVar = TypeVar("ResponseVar")
# Переменная, которая будет использоваться в качестве типа для поля result в
# модели Response. Это позволит нам в дальнейшем указывать тип возвращаемого
# значения в зависимости от типа запроса. Generic[ResponseVar] - это
# обобщенный тип, который позволяет нам указать, что вместо ResponseVar
# будет подставляться другой тип.


class InvocationInfo(BaseModel):
    """Модель информации о вызове."""

    hostname: str
    # Имя хоста, на котором был выполнен вызов.
    req_id: str = Field(alias="req-id")
    # Уникальный идентификатор запроса.
    exec_duration_millis: int = Field(alias="exec-duration-millis")
    # Продолжительность выполнения запроса в миллисекундах.


class Response(BaseModel, ClientMixin, Generic[ResponseVar]):
    """Модель ответа."""

    invocation_info: InvocationInfo = Field(alias="invocationInfo")
    # Информация о вызове.
    result: ResponseVar
    # Результат вызова.
