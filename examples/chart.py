import asyncio
import os

from ymdantic import YMClient

TOKEN = os.environ["TOKEN"]


async def get_chart() -> None:
    """Получаем чарт и выводим треки в консоль."""
    client = YMClient(token=TOKEN)

    chart_block = await client.get_chart()
    print(chart_block.title)
    for index, playlist_track in enumerate(chart_block.chart.tracks, start=1):
        track = playlist_track.track
        if track.available:
            download_info = await track.get_download_info_direct()
            direct_url = download_info[-1].direct_url
        else:
            direct_url = "Недоступен для скачивания"
        print(
            f"{index}. "
            f"{playlist_track.track.artists_names} - {playlist_track.track.title}\n"
            f"({direct_url})\n",
        )

    await client.close()


if __name__ == "__main__":
    asyncio.run(get_chart())
