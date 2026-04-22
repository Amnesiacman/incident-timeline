# incident-timeline

[English version](README.md)

Построение таймлайна инцидента из JSONL-событий.

## Формат входных данных

Каждая строка входного файла — JSON-объект минимум с полями:

- `timestamp`
- `title`

Опциональные поля:

- `source`
- `details`

## Использование

```bash
python3 main.py --input events.jsonl --format markdown
python3 main.py --input events.jsonl --format json
python3 main.py --input events.jsonl --output timeline.md
```
