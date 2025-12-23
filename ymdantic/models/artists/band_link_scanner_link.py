from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel


class BandLinkScannerLink(YMBaseModel):
    """Pydantic модель, представляющая ссылку на band.link артиста."""

    title: str
    # Название ссылки.
    subtitle: str
    # Подзаголовок ссылки.
    url: HttpUrl
    # Ссылка.
    img_url: str
    # Ссылка на изображение.

    def get_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает URL изображения с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения с заданным размером.
        """
        return HttpUrl(f"https://{self.img_url.replace('%%', size)}")
