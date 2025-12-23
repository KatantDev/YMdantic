import base64
import hashlib
import hmac
from datetime import datetime

from pydantic import Field, HttpUrl, computed_field

from ymdantic.models.base import YMBaseModel, YMPostBaseModel
from ymdantic.models.s3 import PRIVATE_KEY


class FileInfoParams(YMPostBaseModel):
    """Параметры запроса информации о файле."""

    track_id: int | str
    # ID трека.
    ts: int = Field(default_factory=lambda: int(datetime.now().timestamp()))
    # Подпись для запроса информации о файле.
    codecs: str = "he-aac,aac,mp3,flac-mp4,aac-mp4,he-aac-mp4"
    # Кодеки для запроса информации о файле.
    quality: str = "lossless"
    # Качество для запроса информации о файле.
    transports: str = "raw"
    # Транспорты для запроса информации о файле.

    @computed_field
    def sign(self) -> str:
        """
        Генерирует подпись для запроса информации о файле.

        :return: Подпись для запроса информации о файле.
        """
        params = {
            "ts": self.ts,
            "trackId": self.track_id,
            "quality": self.quality,
            "codecs": self.codecs,
            "transports": self.transports,
        }
        res = "".join(str(e) for e in params.values()).replace(",", "")
        hmac_sign = hmac.new(
            PRIVATE_KEY.encode(),
            res.encode(),
            hashlib.sha256,
        )
        return base64.b64encode(hmac_sign.digest()).decode()[:-1]


class FileInfo(YMBaseModel):
    """Модель информации о файле."""

    track_id: int
    # ID трека.
    quality: str
    # Качество файла.
    codec: str
    # Кодек файла.
    bitrate: int
    # Битрейт файла.
    transport: str
    # Транспорт файла.
    key: str | None = None
    # Ключ файла. При использовании шифрования.
    size: int
    # Размер файла.
    gain: bool
    # Флаг для нормализации громкости трека (видимо).
    urls: list[HttpUrl]
    # Список URL файлов.
    url: HttpUrl
    # URL файла.
    real_id: int
    # Реальный ID трека.


class FileInfoWrapped(YMBaseModel):
    """Модель информации о файле с оберткой."""

    download_info: FileInfo
    # Информация о скачивании файла.
