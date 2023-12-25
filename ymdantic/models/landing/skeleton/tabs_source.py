from ymdantic.models.base import YMBaseModel


class TabsSource(YMBaseModel):
    """Pydantic модель, представляющая информацию об источнике данных."""

    uri: str
    # URI источника данных.
