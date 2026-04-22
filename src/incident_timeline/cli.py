import argparse
import json
from pathlib import Path

from incident_timeline.core import build_timeline, render_markdown


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="incident-timeline",
        description="Build incident timeline from JSONL events",
    )
    parser.add_argument("--input", required=True, help="Path to events JSONL file")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--output", help="Optional output file path")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    report = build_timeline(Path(args.input))
    text = (
        json.dumps(report, ensure_ascii=True, indent=2)
        if args.format == "json"
        else render_markdown(report)
    )
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0

