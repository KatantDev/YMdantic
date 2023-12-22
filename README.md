# YMDantic

## Описание
**YMDantic** - это клиентская библиотека на Python для работы с API Yandex Music.
Она позволяет получать информацию о треках, альбомах, плейлистах и других объектах сервиса.

Особенностью библиотеки является использование [Pydantic](https://pydantic-docs.helpmanual.io/) для валидации и сериализации данных.

## Технологии
Проект написан на Python и использует следующие библиотеки:
- aiohttp для асинхронных HTTP-запросов
- dataclass_rest для работы с REST API
- Pydantic для валидации и сериализации данных

## Установка и использование
Для установки библиотеки используйте pip/poetry:

```bash
pip install ymdantic
```
или
```bash
poetry add ymdantic
```

## Пример использования
Получаем список чартов и выводим треки
```python
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
```
