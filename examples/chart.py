import asyncio
import os

from ymdantic import YMClient

TOKEN = os.environ["TOKEN"]


async def get_chart() -> None:
    """Получаем чарт и выводим треки в консоль."""
    client = YMClient(token=TOKEN)

    chart_block = await client.get_chart()
    print(chart_block.title, end="\n\n")
    print("Треки в чарте:")
    for playlist_track in chart_block.chart.tracks:
        print(f"{playlist_track.track.artists_names} - {playlist_track.track.title}")

    await client.close()


if __name__ == "__main__":
    asyncio.run(get_chart())
