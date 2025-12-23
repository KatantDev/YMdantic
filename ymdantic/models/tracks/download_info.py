"""Модели информации о скачивании трека."""

from typing import Literal

from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel
from ymdantic.models.s3 import S3FileUrl

CodecType = Literal["mp3", "aac"]


class DownloadInfo(YMBaseModel):
    """Модель информации о скачивании трека."""

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


class DownloadInfoDirect(DownloadInfo):
    """Модель информации о скачивании трека + прямой ссылке."""

    direct_url_info: S3FileUrl

    @property
    def direct_url(self) -> HttpUrl:
        """
        Генерирует прямой URL для скачивания трека.

        Этот метод возвращает URL, сформированный на основе информации о прямом URL,
        хранящейся в атрибуте 'direct_url_info' экземпляра.

        :return: Прямой URL для скачивания трека.
        """
        return self.direct_url_info.url
