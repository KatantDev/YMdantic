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