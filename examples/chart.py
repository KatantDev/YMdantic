import asyncio

from ymdantic import YMClient

TOKEN = "y0_123"


async def main(client: YMClient) -> None:
    chart_block = await client.get_chart()
    print(chart_block.title, end="\n\n")
    print("Треки в чарте:")
    for playlist_track in chart_block.chart.tracks:
        artists_name = ", ".join(artist.name for artist in playlist_track.track.artists)
        print(f"{artists_name} - {playlist_track.track.title}")


if __name__ == "__main__":
    asyncio.run(main(client=YMClient(token=TOKEN)))
