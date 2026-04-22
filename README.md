# incident-timeline

`incident-timeline` строит таймлайн инцидента из JSONL-событий.

## Формат входных данных

Каждая строка в файле — JSON-объект:

```json
{"timestamp":"2026-04-22T12:00:00Z","title":"Alert fired","source":"monitoring","details":"5xx > threshold"}
```

Обязательные поля: `timestamp`, `title`.  
Опциональные: `source`, `details`.

## Использование

```bash
python3 -m pip install -e .
incident-timeline --input events.jsonl --format markdown
```

JSON-отчет:

```bash
incident-timeline --input events.jsonl --format json
```

Записать в файл:

```bash
incident-timeline --input events.jsonl --output timeline.md
```
