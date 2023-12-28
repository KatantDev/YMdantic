# mypy: disable-error-code="empty-body"
from typing import List, Union, Optional

from dataclass_rest import get
from dataclass_rest.client_protocol import FactoryProtocol
from pydantic import HttpUrl

from ymdantic import enums
from ymdantic.adapters.pydantic_factory import PydanticFactory
from ymdantic.client.session import AiohttpClient
from ymdantic.exceptions import UndefinedUser
from ymdantic.models import (
    Response,
    ShortAlbum,
    Album,
    OldChartBlock,
    Playlist,
    TrackType,
    DownloadInfo,
    NewReleasesResponse,
    NewRelease,
    NewReleasesBlock,
    S3FileUrl,
    DownloadInfoDirect,
    SkeletonResponse,
    EditorialResponse,
    LandingArtist,
    LandingArtistItem,
    LandingAlbumItemData,
    LandingAlbumItem,
    LandingLikedPlaylistItem,
    LandingLikedPlaylistItemData,
    LandingPromotion,
    LandingPromotionResponse,
    LandingOpenPlaylist,
    LandingSpecial,
    LandingPersonalPlaylistItemData,
    LandingPersonalPlaylistItem,
    LandingPlaylistItem,
    LandingPlaylistItemData,
    ChartBlock,
    InStyle,
    InStyleResponse,
    LandingWaves,
    LandingWavesResponse,
)
from ymdantic.models.landing.artist import LandingArtistItemData


class YMClient(AiohttpClient):
    def __init__(
        self,
        token: str,
        user_id: Optional[int] = None,
        base_url: str = "https://api.music.yandex.net/",
    ):
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

    async def get_track(self, track_id: Union[int, str]) -> TrackType:
        response = await self.get_track_request(track_id=track_id)
        return response.result[0]

    @get("tracks/{track_id}")
    async def get_track_request(
        self,
        track_id: Union[int, str],
    ) -> Response[List[TrackType]]:
        ...

    async def get_tracks(
        self,
        track_ids: List[Union[int, str]],
    ) -> List[TrackType]:
        response = await self.get_tracks_request(track_ids=track_ids)
        return response.result

    @get("tracks")
    async def get_tracks_request(
        self,
        track_ids: List[Union[int, str]],
    ) -> Response[List[TrackType]]:
        ...

    async def get_track_download_info(
        self,
        track_id: Union[int, str],
    ) -> List[DownloadInfo]:
        response = await self.get_track_download_info_request(track_id=track_id)
        return response.result

    async def get_track_download_info_direct(
        self,
        track_id: Union[int, str],
    ) -> List[DownloadInfoDirect]:
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
        track_id: Union[int, str],
    ) -> Response[List[DownloadInfo]]:
        ...

    @get("{url}")
    async def __get_direct_url_info_request(
        self,
        url: HttpUrl,
        format: str = "json",  # noqa
    ) -> S3FileUrl:
        ...

    async def get_old_chart(self, limit: Optional[int] = None) -> OldChartBlock:
        response = await self.get_old_chart_request(limit=limit)
        return response.result

    @get("landing3/chart")
    async def get_old_chart_request(
        self,
        limit: Optional[int] = None,
    ) -> Response[OldChartBlock]:
        ...

    async def get_new_releases_old(self) -> NewReleasesBlock:
        response = await self.get_new_releases_old_request()
        return response.result

    @get("landing3/new-releases")
    async def get_new_releases_old_request(self) -> Response[NewReleasesBlock]:
        ...

    async def get_playlist(
        self,
        playlist_id: Union[int, str],
        user_id: Optional[Union[int, str]] = None,
    ) -> Playlist:
        user_id = user_id or self.user_id
        if user_id is None:
            raise UndefinedUser()
        response = await self.get_playlist_request(
            user_id=user_id,
            playlist_id=playlist_id,
        )
        return response.result

    @get("users/{user_id}/playlists/{playlist_id}")
    async def get_playlist_request(
        self,
        user_id: Union[int, str],
        playlist_id: Union[int, str],
    ) -> Response[Playlist]:
        ...

    async def get_album(self, album_id: Union[int, str]) -> ShortAlbum:
        response = await self.get_album_request(album_id=album_id)
        return response.result

    @get("albums/{album_id}")
    async def get_album_request(
        self,
        album_id: Union[int, str],
    ) -> Response[ShortAlbum]:
        ...

    async def get_album_with_tracks(self, album_id: Union[int, str]) -> Album:
        response = await self.get_album_with_tracks_request(album_id=album_id)
        return response.result

    @get("albums/{album_id}/with-tracks")
    async def get_album_with_tracks_request(
        self,
        album_id: Union[int, str],
    ) -> Response[Album]:
        ...

    async def get_albums(
        self,
        album_ids: List[Union[int, str]],
    ) -> List[ShortAlbum]:
        response = await self.get_albums_request(album_ids=album_ids)
        return response.result

    @get("albums")
    async def get_albums_request(
        self,
        album_ids: List[Union[int, str]],
    ) -> Response[List[ShortAlbum]]:
        ...

    async def get_editorial_new_releases(
        self,
        block_type: enums.EditorialNewReleasesEnum,
    ) -> List[NewRelease]:
        response = await self.get_editorial_new_releases_request(block_type=block_type)
        return response.new_releases

    @get("landing/block/editorial/new-releases/{block_type}")
    async def get_editorial_new_releases_request(
        self,
        block_type: enums.EditorialNewReleasesEnum,
    ) -> NewReleasesResponse:
        ...

    async def get_recommended_new_releases(self) -> List[NewRelease]:
        response = await self.get_recommended_new_releases_request()
        return response.new_releases

    @get("landing/block/new-releases")
    async def get_recommended_new_releases_request(self) -> NewReleasesResponse:
        ...

    # Не нужен отдельный метод, так как возвращается прямой результат.
    @get("landing/skeleton/main")
    async def get_skeleton_main(self) -> SkeletonResponse:
        ...

    async def get_editorial_artists(
        self,
        block_type: enums.EditorialArtistsEnum,
    ) -> List[LandingArtist]:
        response = await self.get_editorial_artists_request(
            block_type=block_type,
        )
        return [item.data.artist for item in response.items]

    @get("landing/block/editorial/artists/{block_type}")
    async def get_editorial_artists_request(
        self,
        block_type: enums.EditorialArtistsEnum,
    ) -> EditorialResponse[LandingArtistItem]:
        ...

    async def get_editorial_compilation(
        self,
        block_type: enums.EditorialCompilationEnum,
    ) -> Union[List[LandingAlbumItemData], List[LandingLikedPlaylistItemData]]:
        response = await self.get_editorial_compilation_request(
            block_type=block_type,
        )
        return [item.data for item in response.items]

    @get("landing/block/editorial/compilation/{block_type}")
    async def get_editorial_compilation_request(
        self,
        block_type: enums.EditorialCompilationEnum,
    ) -> EditorialResponse[Union[LandingAlbumItem, LandingLikedPlaylistItem]]:
        ...

    async def get_editorial_promotions(
        self,
        block_type: enums.EditorialPromotionEnum,
    ) -> List[LandingPromotion]:
        response = await self.get_editorial_promotions_request(block_type=block_type)
        return response.promotions

    @get("landing/block/editorial-promotion/{block_type}")
    async def get_editorial_promotions_request(
        self,
        block_type: enums.EditorialPromotionEnum,
    ) -> LandingPromotionResponse:
        ...

    # Не нужен отдельный метод, так как возвращается прямой результат.
    # Может быть smart-open-playlist или open-playlist.
    @get("landing/block/{block_type}")
    async def get_open_playlist(
        self,
        block_type: enums.OpenPlaylistEnum,
    ) -> LandingOpenPlaylist:
        ...

    # Не нужен отдельный метод, так как возвращается прямой результат.
    @get("landing/block/special/{block_type}")
    async def get_special_blocks(
        self,
        block_type: enums.SpecialEnum,
    ) -> LandingSpecial:
        ...

    async def get_personal_playlists(self) -> List[LandingPersonalPlaylistItemData]:
        response = await self.get_personal_playlists_request()
        return [item.data for item in response.items]

    @get("landing/block/personal-playlists")
    async def get_personal_playlists_request(
        self,
    ) -> EditorialResponse[LandingPersonalPlaylistItem]:
        ...

    async def get_new_playlists(self) -> List[LandingLikedPlaylistItemData]:
        response = await self.get_new_playlists_request()
        return [item.data for item in response.items]

    @get("landing/block/new-playlists")
    async def get_new_playlists_request(
        self,
    ) -> EditorialResponse[LandingLikedPlaylistItem]:
        ...

    async def get_personal_artists(self) -> List[LandingArtist]:
        response = await self.get_personal_artists_request()
        return [item.data.artist for item in response.items]

    @get("landing/block/personal-artists")
    async def get_personal_artists_request(
        self,
    ) -> EditorialResponse[LandingArtistItem]:
        ...

    async def get_recently_played(
        self,
    ) -> List[
        Union[LandingPlaylistItemData, LandingArtistItemData, LandingAlbumItemData]
    ]:
        response = await self.get_recently_played_request()
        return [item.data for item in response.items]

    @get("landing/block/recently-played")
    async def get_recently_played_request(
        self,
    ) -> EditorialResponse[
        Union[LandingPlaylistItem, LandingArtistItem, LandingAlbumItem]
    ]:
        ...

    # Не нужен отдельный метод, так как возвращается прямой результат.
    @get("landing/block/chart")
    async def get_chart(
        self,
        limit: Optional[int] = None,
    ) -> ChartBlock:
        ...

    async def get_in_style(self) -> List[InStyle]:
        response = await self.get_in_style_request()
        return response.in_style_tabs

    @get("landing/block/in-style")
    async def get_in_style_request(
        self,
        limit: Optional[int] = None,
    ) -> InStyleResponse:
        ...

    async def get_waves(self) -> List[LandingWaves]:
        response = await self.get_waves_request()
        return response.waves

    @get("landing/block/waves")
    async def get_waves_request(
        self,
        limit: Optional[int] = None,
    ) -> LandingWavesResponse:
        ...
