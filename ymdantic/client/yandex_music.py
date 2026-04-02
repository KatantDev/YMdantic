from typing import Sequence, Unpack, Optional

from dataclass_rest import get, post
from dataclass_rest.client_protocol import FactoryProtocol
from pydantic import HttpUrl

from ymdantic import enums
from ymdantic.adapters.pydantic_factory import PydanticFactory
from ymdantic.client.session import AiohttpClient
from ymdantic.exceptions import YMUndefinedUserError
from ymdantic.models import (
    Album,
    ArtistData,
    ChartBlock,
    DownloadInfo,
    DownloadInfoDirect,
    EditorialResponse,
    FileInfo,
    FileInfoParams,
    FileInfoWrapped,
    InStyle,
    InStyleResponse,
    LandingAlbumItem,
    LandingAlbumItemData,
    LandingArtist,
    LandingArtistItem,
    LandingLikedPlaylistItem,
    LandingLikedPlaylistItemData,
    LandingOpenPlaylist,
    LandingPersonalPlaylistItem,
    LandingPersonalPlaylistItemData,
    LandingPlaylistItem,
    LandingPlaylistItemData,
    LandingPromotion,
    LandingPromotionResponse,
    LandingSpecial,
    LandingWaves,
    LandingWavesResponse,
    NewRelease,
    NewReleasesBlock,
    NewReleasesResponse,
    OldChartBlock,
    Playlist,
    Response,
    S3FileUrl,
    SearchInstantMixedResponse,
    SearchParams,
    ShortAlbum,
    SkeletonResponse,
    TrackType,
)
from ymdantic.models.account import AccountSettings, SetAccountSettingsParams
from ymdantic.models.landing.artist import LandingArtistItemData


from aiohttp import ClientSession, TCPConnector
# Для поддержки SOCKS прокси
from aiohttp_socks import ProxyConnector
import ssl

class YMClient(AiohttpClient):
    """Клиент для работы с API Яндекс Музыки."""

    def __init__(
        self,
        token: str,
        user_id: int | None = None,
        base_url: str = "https://api.music.yandex.net/",
        proxy: str | None = None,
        # Формат: scheme://login:password@ip:port
        check_certs: bool = True,  # Проверка SSL сертификатов
    ) -> None:
        self.user_id = user_id
        self.proxy = proxy
        self.check_certs = check_certs
        headers = {
            "Accept": "application/json",
            "Authorization": f"OAuth {token}",
            "X-Yandex-Music-Client": "YandexMusicAndroid/24023621",
        }
        session = self._create_session_with_proxy(headers=headers) if self.proxy else None
        super().__init__(
            base_url=base_url,
            headers=headers,
            session=session
        )

    def _create_session_with_proxy(self, headers: dict[str,str]) -> ClientSession:
        """
        Создает ClientSession с учетом прокси и настроек SSL.
        Поддерживает HTTP, HTTPS и SOCKS прокси (4, 4a, 5).
        """
        # Настройка SSL контекста
        if not self.check_certs:
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
        else:
            ssl_context = None  # Используем стандартную проверку

        # Определяем тип прокси по схеме
        proxy_lower = self.proxy.lower()

        # SOCKS прокси (поддерживаются socks4, socks4a, socks5, socks5h)
        if any(scheme in proxy_lower for scheme in
               ['socks4', 'socks5', 'socks5h', 'socks4a']):

            # Определяем точный тип SOCKS
            if 'socks5h' in proxy_lower:
                proxy_type = 'socks5h'
            elif 'socks5' in proxy_lower:
                proxy_type = 'socks5'
            elif 'socks4a' in proxy_lower:
                proxy_type = 'socks4a'
            elif 'socks4' in proxy_lower:
                proxy_type = 'socks4'
            else:
                proxy_type = 'socks5'

            # Используем ProxyConnector для SOCKS
            connector = ProxyConnector.from_url(
                self.proxy,
                ssl=ssl_context,
            )
            return ClientSession(connector=connector,headers=headers)

        # HTTP/HTTPS прокси
        elif proxy_lower.startswith('http://') or proxy_lower.startswith('https://'):
            connector = TCPConnector(ssl=ssl_context)
            return ClientSession(
                connector=connector,
                proxy=self.proxy,
                proxy_auth=self._get_proxy_auth(),
                headers=headers
            )

        # Если схема не распознана, предполагаем HTTP
        else:
            connector = TCPConnector(ssl=ssl_context)
            return ClientSession(
                connector=connector,
                proxy=f"http://{self.proxy}",
                proxy_auth=self._get_proxy_auth(),
                headers=headers
            )

    def _get_proxy_auth(self) -> Optional[tuple]:
        """
        Извлекает логин и пароль из строки прокси.
        Возвращает кортеж (login, password) или None.
        """
        try:
            # Ищем логин и пароль в формате login:password@
            import re
            match = re.search(r'://([^:]+):([^@]+)@', self.proxy)
            if match:
                return (match.group(1), match.group(2))
        except Exception:
            pass
        return None

    def _init_request_body_factory(self) -> FactoryProtocol:
        return PydanticFactory()

    def _init_request_args_factory(self) -> FactoryProtocol:
        return PydanticFactory()

    async def get_track(self, track_id: int | str) -> TrackType:
        response = await self.get_track_request(track_id=track_id)
        return response.result[0]

    @get("tracks/{track_id}")
    async def get_track_request(
        self,
        track_id: int | str,
    ) -> Response[list[TrackType]]:
        raise NotImplementedError

    async def get_tracks(
        self,
        track_ids: Sequence[int | str],
    ) -> list[TrackType]:
        response = await self.get_tracks_request(track_ids=track_ids)
        return response.result

    @get("tracks")
    async def get_tracks_request(
        self,
        track_ids: Sequence[int | str],
    ) -> Response[list[TrackType]]:
        raise NotImplementedError

    async def get_track_download_info(
        self,
        track_id: int | str,
    ) -> list[DownloadInfo]:
        response = await self.get_track_download_info_request(track_id=track_id)
        return response.result

    async def get_track_download_info_direct(
        self,
        track_id: int | str,
    ) -> list[DownloadInfoDirect]:
        """
        Используется для получения прямых ссылок на скачивание трека.

        :param track_id: ID трека.
        :return: Список информации для скачивания трека + прямые ссылки.
        """
        result = await self.get_track_download_info(track_id=track_id)

        new_response = []
        for download_info in result:
            direct_url_info = await self.__get_direct_url_info_request(
                url=download_info.download_info_url,
            )
            new_response.append(
                DownloadInfoDirect(
                    **download_info.model_dump(),
                    direct_url_info=direct_url_info,
                ),
            )
        return new_response

    @get("tracks/{track_id}/download-info")
    async def get_track_download_info_request(
        self,
        track_id: int | str,
    ) -> Response[list[DownloadInfo]]:
        raise NotImplementedError

    @get("{url}")
    async def __get_direct_url_info_request(
        self,
        url: HttpUrl,
        format: str = "json",
    ) -> S3FileUrl:
        raise NotImplementedError

    async def get_track_file_info(self, track_id: int | str) -> FileInfo:
        """
        Используется для получения lossless файлов, если доступен.

        :param track_id: ID трека.
        :return: Информация о файле.
        """
        response = await self.get_track_file_info_request(
            params=FileInfoParams(track_id=track_id),
        )
        return response.result.download_info

    @get("get-file-info")
    async def get_track_file_info_request(
        self,
        params: FileInfoParams,
    ) -> Response[FileInfoWrapped]:
        raise NotImplementedError

    async def get_old_chart(self, limit: int | None = None) -> OldChartBlock:
        response = await self.get_old_chart_request(limit=limit)
        return response.result

    @get("landing3/chart")
    async def get_old_chart_request(
        self,
        limit: int | None = None,
    ) -> Response[OldChartBlock]:
        raise NotImplementedError

    async def get_new_releases_old(self) -> NewReleasesBlock:
        response = await self.get_new_releases_old_request()
        return response.result

    @get("landing3/new-releases")
    async def get_new_releases_old_request(self) -> Response[NewReleasesBlock]:
        raise NotImplementedError

    async def get_playlist(
        self,
        playlist_id: int | str,
        user_id: int | str | None = None,
    ) -> Playlist:
        user_id = user_id or self.user_id
        if user_id is None:
            raise YMUndefinedUserError
        response = await self.get_playlist_request(
            user_id=user_id,
            playlist_id=playlist_id,
        )
        return response.result

    @get("users/{user_id}/playlists/{playlist_id}")
    async def get_playlist_request(
        self,
        user_id: int | str,
        playlist_id: int | str,
    ) -> Response[Playlist]:
        raise NotImplementedError

    async def get_album(self, album_id: int | str) -> ShortAlbum:
        response = await self.get_album_request(album_id=album_id)
        return response.result

    @get("albums/{album_id}")
    async def get_album_request(
        self,
        album_id: int | str,
    ) -> Response[ShortAlbum]:
        raise NotImplementedError

    async def get_album_with_tracks(self, album_id: int | str) -> Album:
        response = await self.get_album_with_tracks_request(album_id=album_id)
        return response.result

    @get("albums/{album_id}/with-tracks")
    async def get_album_with_tracks_request(
        self,
        album_id: int | str,
    ) -> Response[Album]:
        raise NotImplementedError

    async def get_albums(
        self,
        album_ids: Sequence[int | str],
    ) -> list[ShortAlbum]:
        response = await self.get_albums_request(album_ids=album_ids)
        return response.result

    @get("albums")
    async def get_albums_request(
        self,
        album_ids: Sequence[int | str],
    ) -> Response[list[ShortAlbum]]:
        raise NotImplementedError

    async def get_editorial_new_releases(
        self,
        block_type: enums.EditorialNewReleasesEnum,
    ) -> list[NewRelease]:
        response = await self.get_editorial_new_releases_request(block_type=block_type)
        return response.new_releases

    @get("landing/block/editorial/new-releases/{block_type}")
    async def get_editorial_new_releases_request(
        self,
        block_type: enums.EditorialNewReleasesEnum,
    ) -> NewReleasesResponse:
        raise NotImplementedError

    async def get_recommended_new_releases(self) -> list[NewRelease]:
        response = await self.get_recommended_new_releases_request()
        return response.new_releases

    @get("landing/block/new-releases")
    async def get_recommended_new_releases_request(self) -> NewReleasesResponse:
        raise NotImplementedError

    # Не нужен отдельный метод, так как возвращается прямой результат.
    @get("landing/skeleton/main")
    async def get_skeleton_main(self) -> SkeletonResponse:
        raise NotImplementedError

    async def get_editorial_artists(
        self,
        block_type: enums.EditorialArtistsEnum,
    ) -> list[LandingArtist]:
        response = await self.get_editorial_artists_request(
            block_type=block_type,
        )
        return [item.data.artist for item in response.items]

    @get("landing/block/editorial/artists/{block_type}")
    async def get_editorial_artists_request(
        self,
        block_type: enums.EditorialArtistsEnum,
    ) -> EditorialResponse[LandingArtistItem]:
        raise NotImplementedError

    async def get_editorial_compilation(
        self,
        block_type: enums.EditorialCompilationEnum,
    ) -> list[LandingAlbumItemData] | list[LandingLikedPlaylistItemData]:
        response = await self.get_editorial_compilation_request(
            block_type=block_type,
        )
        return [item.data for item in response.items]

    @get("landing/block/editorial/compilation/{block_type}")
    async def get_editorial_compilation_request(
        self,
        block_type: enums.EditorialCompilationEnum,
    ) -> EditorialResponse[LandingAlbumItem | LandingLikedPlaylistItem]:
        raise NotImplementedError

    async def get_editorial_promotions(
        self,
        block_type: enums.EditorialPromotionEnum,
    ) -> list[LandingPromotion]:
        response = await self.get_editorial_promotions_request(block_type=block_type)
        return response.promotions

    @get("landing/block/editorial-promotion/{block_type}")
    async def get_editorial_promotions_request(
        self,
        block_type: enums.EditorialPromotionEnum,
    ) -> LandingPromotionResponse:
        raise NotImplementedError

    # Не нужен отдельный метод, так как возвращается прямой результат.
    # Может быть smart-open-playlist или open-playlist.
    @get("landing/block/{block_type}")
    async def get_open_playlist(
        self,
        block_type: enums.OpenPlaylistEnum,
    ) -> LandingOpenPlaylist:
        raise NotImplementedError

    # Не нужен отдельный метод, так как возвращается прямой результат.
    @get("landing/block/special/{block_type}")
    async def get_special_blocks(
        self,
        block_type: enums.SpecialEnum,
    ) -> LandingSpecial:
        raise NotImplementedError

    async def get_personal_playlists(self) -> list[LandingPersonalPlaylistItemData]:
        response = await self.get_personal_playlists_request()
        return [item.data for item in response.items]

    @get("landing/block/personal-playlists")
    async def get_personal_playlists_request(
        self,
    ) -> EditorialResponse[LandingPersonalPlaylistItem]:
        raise NotImplementedError

    async def get_new_playlists(self) -> list[LandingLikedPlaylistItemData]:
        response = await self.get_new_playlists_request()
        return [item.data for item in response.items]

    @get("landing/block/new-playlists")
    async def get_new_playlists_request(
        self,
    ) -> EditorialResponse[LandingLikedPlaylistItem]:
        raise NotImplementedError

    async def get_personal_artists(self) -> list[LandingArtist]:
        response = await self.get_personal_artists_request()
        return [item.data.artist for item in response.items]

    @get("landing/block/personal-artists")
    async def get_personal_artists_request(
        self,
    ) -> EditorialResponse[LandingArtistItem]:
        raise NotImplementedError

    async def get_recently_played(
        self,
    ) -> list[LandingPlaylistItemData | LandingArtistItemData | LandingAlbumItemData]:
        response = await self.get_recently_played_request()
        return [item.data for item in response.items]

    @get("landing/block/recently-played")
    async def get_recently_played_request(
        self,
    ) -> EditorialResponse[LandingPlaylistItem | LandingArtistItem | LandingAlbumItem]:
        raise NotImplementedError

    # Не нужен отдельный метод, так как возвращается прямой результат.
    @get("landing/block/chart")
    async def get_chart(
        self,
        limit: int | None = None,
    ) -> ChartBlock:
        raise NotImplementedError

    async def get_in_style(self) -> list[InStyle]:
        response = await self.get_in_style_request()
        return response.in_style_tabs

    @get("landing/block/in-style")
    async def get_in_style_request(
        self,
        limit: int | None = None,
    ) -> InStyleResponse:
        raise NotImplementedError

    async def get_waves(self) -> list[LandingWaves]:
        response = await self.get_waves_request()
        return response.waves

    @get("landing/block/waves")
    async def get_waves_request(
        self,
        limit: int | None = None,
    ) -> LandingWavesResponse:
        raise NotImplementedError

    @get("artists/{artist_id}")
    async def get_artist(
        self,
        artist_id: int | str,
    ) -> Response[ArtistData]:
        raise NotImplementedError

    async def get_account_settings(self) -> AccountSettings:
        response = await self.get_account_settings_request()
        return response.result

    @get("account/settings")
    async def get_account_settings_request(self) -> Response[AccountSettings]:
        raise NotImplementedError

    async def set_account_settings(
        self,
        **params: Unpack[SetAccountSettingsParams],  # type: ignore[misc]
    ) -> AccountSettings:
        response = await self.set_account_settings_request(
            params=SetAccountSettingsParams(**params),
        )
        return response.result

    @post("account/settings")
    async def set_account_settings_request(
        self,
        params: SetAccountSettingsParams,
    ) -> Response[AccountSettings]:
        raise NotImplementedError

    async def search_instant_mixed(
        self,
        **params: Unpack[SearchParams],  # type: ignore[misc]
    ) -> SearchInstantMixedResponse:
        response = await self.search_instant_mixed_request(
            params=SearchParams(**params),
        )
        return response.result

    @get("search/instant/mixed")
    async def search_instant_mixed_request(
        self,
        params: SearchParams,
    ) -> Response[SearchInstantMixedResponse]:
        raise NotImplementedError
