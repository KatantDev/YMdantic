from pydantic import HttpUrl

from ymdantic.models.base import YMBaseModel


class ArtistVideo(YMBaseModel):
    """Pydantic модель, представляющая видео артиста."""

    title: str
    # Название видео.
    cover: HttpUrl
    # Ссылка на обложку видео.
    embed_url: HttpUrl
    # Ссылка на видео.
    provider: str
    # Провайдер видео.
    provider_video_id: str
    # ID видео на провайдере.

    def get_cover_image_url(self, size: str = "200x200") -> HttpUrl:
        """
        Возвращает URL изображения обложки видео с заданным размером.

        :param size: Размер изображения.
        :return: URL изображения обложки видео с заданным размером.
        """
        return HttpUrl(f"https://{str(self.cover).replace('%%', size)}")
