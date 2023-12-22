import asyncio
from ymdantic import YMClient


async def get_chart(client: YMClient) -> None:
    chart_block = await client.get_chart()
    print(chart_block.title, end="\n\n")
    print("Треки в чарте:")
    for playlist_track in chart_block.chart.tracks:
        print(f"{playlist_track.track.artists_names} - {playlist_track.track.title}")


if __name__ == "__main__":
    asyncio.run(get_chart(client=YMClient(token="y0_123")))
