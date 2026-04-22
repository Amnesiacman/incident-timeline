import json
from pathlib import Path


def load_events(path: Path) -> list[dict]:
    events = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        item = json.loads(line)
        if "timestamp" not in item or "title" not in item:
            continue
        item.setdefault("source", "unknown")
        item.setdefault("details", "")
        events.append(item)
    events.sort(key=lambda x: x["timestamp"])
    return events


def build_timeline(path: Path) -> dict:
    events = load_events(path)
    return {
        "input": str(path),
        "total_events": len(events),
        "timeline": events,
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Incident Timeline",
        "",
        f"Source: `{report['input']}`",
        f"Total events: {report['total_events']}",
        "",
    ]
    for item in report["timeline"]:
        lines.append(f"- **{item['timestamp']}** [{item['source']}] {item['title']}")
        if item["details"]:
            lines.append(f"  - {item['details']}")
    return "\n".join(lines)

