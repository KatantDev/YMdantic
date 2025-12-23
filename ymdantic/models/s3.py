from hashlib import md5

from pydantic import BaseModel, HttpUrl

PRIVATE_KEY = "uz0zSpaYCLmgk6C7YLdo5F"


class S3FileUrl(BaseModel):
    """Pydantic модель, представляющая данные о URL файла на S3."""

    s: str
    # Используется для формирования подписи.
    ts: str
    # Временная метка для URL файла S3.
    path: str
    # Путь к файлу на S3.
    host: str
    # Хост S3.

    @property
    def sign(self) -> str:
        """
        Генерирует подпись для URL файла S3.

        Этот метод конкатенирует приватный ключ, путь (исключая первый слеш), и атрибут
        's' экземпляра. Полученная строка затем преобразуется в байты и хешируется с
        использованием алгоритма MD5. Возвращается шестнадцатеричное представление этого
        хеша в качестве подписи.

        :return: Хеш MD5 конкатенированной строки в виде шестнадцатеричной строки.
        """
        data = (PRIVATE_KEY + self.path[1::] + self.s).encode("utf-8")
        return md5(data, usedforsecurity=False).hexdigest()

    @property
    def url(self) -> HttpUrl:
        """
        Генерирует URL на S3 для файла.

        Этот метод формирует URL, используя хост, подпись, временную метку и путь файла.
        URL возвращается в формате HttpUrl.

        :return: Сформированный URL для файла S3.
        """
        return HttpUrl(f"https://{self.host}/get-mp3/{self.sign}/{self.ts}{self.path}")
