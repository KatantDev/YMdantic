from typing import Annotated, Literal, NotRequired, TypedDict

from pydantic import Field

from ymdantic.models.base import YMBaseModel, YMPostBaseModel
from ymdantic.models.search.results import (
    SearchResult,
)


class SearchParams(YMPostBaseModel):
    """Параметры запроса поиска."""

    text: str
    with_likes_count: bool = True
    page: int = 0
    page_size: int = 20
    with_best_results: bool = False
    type: Literal["all"] = "all"
    filter: (
        Literal["track", "artist", "album", "playlist", "podcast", "book", "clip"]
        | None
    ) = None
    nocorrect: bool = False


class SearchParamsDict(TypedDict, total=False):
    """Fields for search function."""

    text: str
    with_likes_count: NotRequired[bool]
    page: NotRequired[int]
    page_size: NotRequired[int]
    with_best_results: NotRequired[bool]
    type: NotRequired[Literal["all"]]
    filter: NotRequired[
        Literal["track", "artist", "album", "playlist", "podcast", "book", "clip"]
    ]
    nocorrect: NotRequired[bool]


class SearchFilter(YMBaseModel):
    """Фильтры для поиска."""

    id: str
    # ID фильтра.
    display_name: str
    # Название фильтра.


class SearchPager(YMBaseModel):
    """Пагинатор для поиска."""

    total: int
    # Общее количество элементов.
    per_page: int
    # Количество элементов на странице.
    last_page: bool
    # Флаг, указывающий, является ли текущая страница последней.


class SearchInstantMixedResponse(SearchPager):
    """Ответ на запрос поиска смешанного типа."""

    search_request_id: str
    # Идентификатор запроса поиска.
    text: str
    # Текст запроса.
    misspell_corrected: bool
    # Флаг, указывающий, была ли исправлена опечатка в запросе.
    response_type: str
    # Тип ответа.
    results: Annotated[list[SearchResult], Field(default_factory=list)]
    # Результаты ответа (может отсутствовать при пустой выдаче).
    filters: Annotated[list[SearchFilter], Field(default_factory=list)]
    # Доступные фильтры для поиска.
