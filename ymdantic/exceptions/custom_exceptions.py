from ymdantic.models.error import YandexMusicErrorModel


class YandexMusicError(Exception):
    def __init__(self, error: YandexMusicErrorModel) -> None:
        self.error = error
        super().__init__(self.error.message)

    def __str__(self) -> str:
        original_message = super().__str__()
        return f"{self.error.name}" + (
            f" - {original_message}" if original_message else ""
        )


class UndefinedUser(Exception):
    def __init__(self) -> None:
        super().__init__("ID пользователя не указан")
