import json
from pathlib import Path

from incident_timeline.cli import main


def test_cli_json_output(tmp_path: Path, capsys):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp":"2026-04-22T12:00:00Z","title":"Alert fired"}\n', encoding="utf-8"
    )
    code = main(["--input", str(path), "--format", "json"])
    payload = json.loads(capsys.readouterr().out)
    assert code == 0
    assert payload["total_events"] == 1


def test_cli_output_file(tmp_path: Path):
    path = tmp_path / "events.jsonl"
    out = tmp_path / "timeline.md"
    path.write_text(
        '{"timestamp":"2026-04-22T12:00:00Z","title":"Alert fired"}\n', encoding="utf-8"
    )
    code = main(["--input", str(path), "--output", str(out)])
    assert code == 0
    assert out.exists()
