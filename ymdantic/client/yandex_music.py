# mypy: disable-error-code="empty-body"
from typing import List, Union, Optional

from dataclass_rest import get
from dataclass_rest.client_protocol import FactoryProtocol

from ymdantic.adapters.pydantic_factory import PydanticFactory
from ymdantic.client.session import AiohttpClient
from ymdantic.exceptions import UndefinedUser
from ymdantic.models import (
    Response,
    ShortAlbum,
    Album,
    ChartBlock,
    Playlist,
    TrackType,
    DownloadInfo,
)


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
                "Authorization": f"OAuth {token}",
                "X-Yandex-Music-Client": "YandexMusic/648",
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
        response = await self.get_track_download_info_request(
            track_id=track_id,
        )
        return response.result

    @get("tracks/{track_id}/download-info")
    async def get_track_download_info_request(
        self,
        track_id: Union[int, str],
    ) -> Response[List[DownloadInfo]]:
        ...

    async def get_chart(self, limit: Optional[int] = None) -> ChartBlock:
        response = await self.get_chart_request(limit=limit)
        return response.result

    @get("landing3/chart")
    async def get_chart_request(
        self,
        limit: Optional[int] = None,
    ) -> Response[ChartBlock]:
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
