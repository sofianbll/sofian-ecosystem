#!/usr/bin/env python3
"""Fail a public-doc build on obvious secrets or direct PII.

Only rule names and file locations are printed. Matched values are never echoed.
Local paths and private-network addresses are warnings because Sofian explicitly
accepted the current public technical corpus on 2026-08-28.
"""

from __future__ import annotations

import argparse
from collections import Counter
import re
from dataclasses import dataclass
from pathlib import Path


TEXT_SUFFIXES = {
    ".css",
    ".html",
    ".js",
    ".mjs",
    ".mts",
    ".json",
    ".md",
    ".ts",
    ".txt",
    ".yaml",
    ".yml",
}
SKIP_PARTS = {".git", "cache", "dist", "node_modules"}


@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]
    blocking: bool = True


RULES = (
    Rule("private_key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    Rule("github_token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),
    Rule("aws_access_key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    Rule(
        "secret_assignment",
        re.compile(
            r"(?i)(?:password|api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret)"
            r"\s*[:=]\s*[\"']?[^\s,\"'}]{12,}"
        ),
    ),
    Rule("email", re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")),
    Rule(
        "phone_fr",
        re.compile(r"(?<!\d)(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}(?!\d)"),
    ),
    Rule("local_user_path", re.compile(r"/Users/[^/\s]+/"), blocking=False),
    Rule(
        "private_network_address",
        re.compile(
            r"(?<!\d)(?:10\.\d{1,3}(?:\.\d{1,3}){2}|192\.168\.\d{1,3}\.\d{1,3}|"
            r"172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}|"
            r"100\.(?:6[4-9]|[7-9]\d|1[01]\d|12[0-7])\.\d{1,3}\.\d{1,3})(?!\d)"
        ),
        blocking=False,
    ),
)


def iter_text_files(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        yield path


def scan(
    root: Path, extra_files: tuple[Path, ...] = ()
) -> tuple[list[tuple[str, Path, int]], list[tuple[str, Path, int]]]:
    blocking: list[tuple[str, Path, int]] = []
    warnings: list[tuple[str, Path, int]] = []
    paths = list(iter_text_files(root))
    paths.extend(path for path in extra_files if path.is_file())
    for path in dict.fromkeys(paths):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for rule in RULES:
                if not rule.pattern.search(line):
                    continue
                try:
                    display_path = path.relative_to(root)
                except ValueError:
                    display_path = Path(path.name)
                finding = (rule.name, display_path, line_number)
                (blocking if rule.blocking else warnings).append(finding)
    return blocking, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("docs"))
    parser.add_argument("--file", type=Path, action="append", default=[])
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"publication scan: ERROR root_not_found {root}")
        return 2

    extra_files = tuple(path.resolve() for path in args.file)
    missing_files = [path for path in extra_files if not path.is_file()]
    if missing_files:
        print(f"publication scan: ERROR file_not_found count={len(missing_files)}")
        return 2

    blocking, warnings = scan(root, extra_files)
    warning_counts = Counter(rule for rule, _, _ in warnings)
    for rule, count in sorted(warning_counts.items()):
        print(f"publication scan: WARN {rule} count={count}")
    for rule, path, line in blocking:
        print(f"publication scan: FAIL {rule} {path}:{line}")

    if blocking:
        print(f"publication scan: BLOCKED findings={len(blocking)} warnings={len(warnings)}")
        return 1
    print(f"publication scan: PASS findings=0 warnings={len(warnings)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
