#!/usr/bin/env python3
"""MEP handoff.md conformance checker (schema 1.2).

Validates newest-first ordering, required sections, same-day timestamp
order, and Hello [active] stubs. Stdlib only.

Default baton path is handoff.md at repo root. machines/handoff.md is a
legacy alias used only when the default file is missing.

Usage:
  python3 scripts/check-handoff.py path/to/handoff.md
  python3 scripts/check-handoff.py --self-test
  python3 scripts/check-handoff.py --ci
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

HEADER_RE = re.compile(
    r"^##\s+(\d{4}-\d{2}-\d{2})\s+[—–-]\s+(.+)$"
)
TAG_RE = re.compile(
    r"\*\*Tag-in:\*\*\s*([^\n|]+?)\s*\|\s*\*\*Tag-out:\*\*\s*([^\n]+?)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
TIME_RE = re.compile(
    r"^(\d{1,2}):(\d{2})(?:\s*([A-Za-z]{2,4}))?$"
)

TZ_OFFSET_HOURS = {
    "UTC": 0,
    "GMT": 0,
    "Z": 0,
    "ET": -4,
    "EST": -5,
    "EDT": -4,
    "CT": -5,
    "CST": -6,
    "CDT": -5,
    "MT": -6,
    "MST": -7,
    "MDT": -6,
    "PT": -7,
    "PST": -8,
    "PDT": -7,
}

ACTIVE_SENTINEL = dt.datetime.max.replace(tzinfo=dt.timezone.utc)


class Issue:
    def __init__(self, level: str, message: str) -> None:
        self.level = level
        self.message = message


def parse_clock(raw: str) -> dt.datetime | None:
    text = raw.strip()
    if text.lower() in {"[active]", "active"}:
        return ACTIVE_SENTINEL
    match = TIME_RE.match(text)
    if not match:
        return None
    hour, minute, zone = match.groups()
    offset_hours = TZ_OFFSET_HOURS.get((zone or "UTC").upper())
    if offset_hours is None:
        return None
    tz = dt.timezone(dt.timedelta(hours=offset_hours))
    return dt.datetime(2000, 1, 1, int(hour), int(minute), tzinfo=tz).astimezone(
        dt.timezone.utc
    )


def split_entries(text: str) -> list[tuple[int, str]]:
    lines = text.splitlines()
    starts: list[int] = []
    for index, line in enumerate(lines):
        if HEADER_RE.match(line):
            starts.append(index)
    entries: list[tuple[int, str]] = []
    for i, start in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(lines)
        entries.append((start + 1, "\n".join(lines[start:end]).strip() + "\n"))
    return entries


def check_text(text: str, source: str) -> list[Issue]:
    issues: list[Issue] = []
    if not text.lstrip().startswith("# Handoff Log"):
        issues.append(Issue("error", f"{source}: file must start with '# Handoff Log'"))

    entries = split_entries(text)
    if not entries:
        issues.append(Issue("error", f"{source}: no '## YYYY-MM-DD' entries found"))
        return issues

    parsed: list[tuple[int, dt.date, dt.datetime | None, str]] = []
    for line_no, body in entries:
        first = body.splitlines()[0]
        match = HEADER_RE.match(first)
        if not match:
            issues.append(Issue("error", f"{source}:{line_no}: unparseable header: {first}"))
            continue
        date = dt.date.fromisoformat(match.group(1))
        if "### What happened" not in body:
            issues.append(
                Issue("error", f"{source}:{line_no}: missing '### What happened'")
            )
        if "### What's pending" not in body:
            issues.append(
                Issue("error", f"{source}:{line_no}: missing \"### What's pending\"")
            )
        tag = TAG_RE.search(body)
        stamp = parse_clock(tag.group(2)) if tag else None
        if tag and stamp is None:
            issues.append(
                Issue(
                    "warning",
                    f"{source}:{line_no}: tag-out not parseable ({tag.group(2)!r}); "
                    "same-day order cannot be checked",
                )
            )
        parsed.append((line_no, date, stamp, first))

    for prev, curr in zip(parsed, parsed[1:]):
        _, prev_date, prev_stamp, prev_header = prev
        line_no, curr_date, curr_stamp, curr_header = curr
        if curr_date > prev_date:
            issues.append(
                Issue(
                    "error",
                    f"{source}:{line_no}: newest-first violated: {curr_date} appears below {prev_date}",
                )
            )
            continue
        if curr_date == prev_date and prev_stamp and curr_stamp:
            if curr_stamp > prev_stamp:
                issues.append(
                    Issue(
                        "error",
                        f"{source}:{line_no}: same-day newest-first violated: "
                        f"{curr_header!r} is later than {prev_header!r}",
                    )
                )
        elif curr_date == prev_date and (prev_stamp is None or curr_stamp is None):
            issues.append(
                Issue(
                    "warning",
                    f"{source}:{line_no}: same-day entries without comparable timestamps; "
                    "first-party repos should use v2 tag-in/tag-out with timezones",
                )
            )
    return issues


def resolve_baton(path: Path) -> Path:
    if path.is_dir():
        default = path / "handoff.md"
        legacy = path / "machines" / "handoff.md"
        if default.exists():
            return default
        if legacy.exists():
            return legacy
        return default
    return path


def check_file(path: Path) -> list[Issue]:
    baton = resolve_baton(path)
    if not baton.exists():
        return [Issue("error", f"{baton}: file not found")]
    return check_text(baton.read_text(encoding="utf-8"), str(baton))


def example_handoffs(root: Path) -> list[Path]:
    found: list[Path] = []
    examples = root / "examples"
    if not examples.exists():
        return found
    for candidate in sorted(examples.rglob("handoff.md")):
        found.append(candidate)
    return found


def run_ci() -> int:
    root = Path(__file__).resolve().parents[1]
    failed = self_test()
    for handoff in example_handoffs(root):
        issues = check_file(handoff)
        errors = [i for i in issues if i.level == "error"]
        status = "ok" if not errors else "FAIL"
        print(f"{status:4} {handoff.relative_to(root)}: {len(errors)} error(s)")
        if errors:
            failed = 1
            for issue in errors:
                print(f"       {issue.level}: {issue.message}")
    return failed


def self_test() -> int:
    root = Path(__file__).resolve().parents[1] / "tests" / "handoff"
    cases = [
        ("valid.md", 0, 0),
        ("valid-v2-sameday.md", 0, 0),
        ("valid-active.md", 0, 0),
        ("invalid-order.md", 1, None),
        ("invalid-sameday.md", 1, None),
        ("invalid-missing-section.md", 1, None),
    ]
    failed = 0
    for name, min_errors, max_warnings in cases:
        issues = check_file(root / name)
        errors = [i for i in issues if i.level == "error"]
        warnings = [i for i in issues if i.level == "warning"]
        ok = len(errors) >= min_errors if min_errors else len(errors) == 0
        if max_warnings is not None and len(warnings) != max_warnings:
            ok = False
        if min_errors and not errors:
            ok = False
        status = "ok" if ok else "FAIL"
        if not ok:
            failed += 1
        print(f"{status:4} {name}: {len(errors)} error(s), {len(warnings)} warning(s)")
        if not ok:
            for issue in issues:
                print(f"       {issue.level}: {issue.message}")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", help="handoff.md or a repo directory")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument(
        "--ci",
        action="store_true",
        help="run fixtures plus every examples/**/handoff.md",
    )
    args = parser.parse_args(argv)

    if args.ci:
        return run_ci()
    if args.self_test:
        return self_test()
    if not args.path:
        parser.print_help()
        return 2

    issues = check_file(Path(args.path))
    for issue in issues:
        print(f"{issue.level}: {issue.message}")
    errors = sum(1 for i in issues if i.level == "error")
    if not issues:
        print("ok")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
