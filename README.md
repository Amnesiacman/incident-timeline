# incident-timeline

[Русская версия](README.ru.md)

Build incident timelines from JSONL events.

## Input format

Each line in input file must be a JSON object with at least:

- `timestamp`
- `title`

Optional fields:

- `source`
- `details`

## Usage

```bash
python3 main.py --input events.jsonl --format markdown
python3 main.py --input events.jsonl --format json
python3 main.py --input events.jsonl --output timeline.md
```
