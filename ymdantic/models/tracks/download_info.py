from typing import Literal

from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel

CodecType = Literal["mp3", "aac"]


class DownloadInfo(YMBaseModel):
    """Pydantic модель, представляющая информацию о скачивании трека."""

    codec: CodecType
    # Кодек трека. Возможные значения: "mp3", "aac".
    gain: bool
    # Флаг для нормализации громкости трека (видимо).
    preview: bool
    # Доступно ли предварительное прослушивание трека.
    download_info_url: HttpUrl
    # Ссылка на S3-хранилище с данными для формирования ссылки на скачивание трека.
    direct: bool
    # Является ли ссылка на S3-хранилище прямой ссылкой на скачивание трека.
    bitrate_in_kbps: int
    # Битрейт трека в кбит/с.
