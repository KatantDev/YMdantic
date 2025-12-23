from ymdantic.models.error import YandexMusicErrorModel


class YMError(Exception):
    """Исключение, выбрасываемое при ошибке в API Яндекс Музыки."""

    def __init__(self, error: YandexMusicErrorModel) -> None:
        self.error = error
        super().__init__(self.error.message)

    def __str__(self) -> str:
        original_message = super().__str__()
        return f"{self.error.name}" + (
            f" - {original_message}" if original_message else ""
        )


class YMUndefinedUserError(Exception):
    """Исключение, выбрасываемое при неопределенном пользователе."""

    def __init__(self) -> None:
        super().__init__("ID пользователя не указан")


class YMTrackNotFoundError(YMError):
    """Исключение, выбрасываемое при не найденном треке."""

    def __init__(self) -> None:
        super().__init__(
            error=YandexMusicErrorModel(
                name="not-found",
                message="Трек не найден",
            ),
        )
