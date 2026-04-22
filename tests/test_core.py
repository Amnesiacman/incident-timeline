from pathlib import Path

from incident_timeline.core import build_timeline, render_markdown


def test_build_timeline_sorts_events(tmp_path: Path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp":"2026-04-22T12:05:00Z","title":"Recovered"}\n'
        '{"timestamp":"2026-04-22T12:00:00Z","title":"Alert fired"}\n',
        encoding="utf-8",
    )
    report = build_timeline(path)
    assert report["total_events"] == 2
    assert report["timeline"][0]["title"] == "Alert fired"


def test_render_markdown_contains_header(tmp_path: Path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp":"2026-04-22T12:00:00Z","title":"Alert fired"}\n', encoding="utf-8"
    )
    report = build_timeline(path)
    text = render_markdown(report)
    assert "# Incident Timeline" in text
