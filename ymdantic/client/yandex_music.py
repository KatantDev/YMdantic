from typing import Sequence

from dataclass_rest import get
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
    ShortAlbum,
    SkeletonResponse,
    TrackType,
)
from ymdantic.models.landing.artist import LandingArtistItemData


class YMClient(AiohttpClient):
    """Клиент для работы с API Яндекс Музыки."""

    def __init__(
        self,
        token: str,
        user_id: int | None = None,
        base_url: str = "https://api.music.yandex.net/",
    ) -> None:
        self.user_id = user_id
        super().__init__(
            base_url=base_url,
            headers={
                "Accept": "application/json",
                "Authorization": f"OAuth {token}",
                "X-Yandex-Music-Client": "YandexMusic/649",
            },
        )

    def _init_request_body_factory(self) -> FactoryProtocol:
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
