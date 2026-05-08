#!/usr/bin/env python3

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Set, Tuple


DEFAULT_KEEP_REGEX = r"(?i)(error|exception|traceback|failed|fail|warning|fatal|panic|segfault|stack trace|assert)"


@dataclass
class CompressionStats:
    source: str
    original_lines: int
    kept_lines: int
    omitted_lines: int


def _read_text(path: Optional[str]) -> Tuple[str, str]:
    if path:
        p = Path(path).expanduser()
        return p.read_text(errors="ignore"), str(p)
    return sys.stdin.read(), "<stdin>"


def _find_keep_indices(
    lines: List[str],
    head: int,
    tail: int,
    keep_re: re.Pattern,
    context: int,
) -> Set[int]:
    n = len(lines)
    keep: Set[int] = set()

    for i in range(min(head, n)):
        keep.add(i)

    for i in range(max(0, n - tail), n):
        keep.add(i)

    for i, line in enumerate(lines):
        if keep_re.search(line):
            for j in range(max(0, i - context), min(n, i + context + 1)):
                keep.add(j)

    return keep


def _render_with_gaps(lines: List[str], indices: List[int]) -> List[str]:
    if not indices:
        return []

    rendered: List[str] = []
    last = indices[0]
    rendered.append(lines[last])

    for idx in indices[1:]:
        gap = idx - last
        if gap > 1:
            rendered.append(f"... ({gap - 1} lines omitted) ...")
        rendered.append(lines[idx])
        last = idx

    return rendered


def _collapse_consecutive_duplicates(lines: List[str], max_repeat: int) -> List[str]:
    if max_repeat < 1:
        return lines

    out: List[str] = []
    last: Optional[str] = None
    run = 0
    omitted_in_run = 0

    def flush_omitted() -> None:
        nonlocal omitted_in_run
        if omitted_in_run > 0:
            out.append(f"... ({omitted_in_run} duplicate lines omitted) ...")
            omitted_in_run = 0

    for line in lines:
        if last is None or line != last:
            flush_omitted()
            out.append(line)
            last = line
            run = 1
            continue

        run += 1
        if run <= max_repeat:
            out.append(line)
        else:
            omitted_in_run += 1

    flush_omitted()
    return out


def compress_text(
    text: str,
    *,
    head: int,
    tail: int,
    keep_regex: str,
    context: int,
    max_lines: int,
    max_repeat: int,
) -> Tuple[List[str], CompressionStats]:
    raw_lines = text.splitlines()
    keep_re = re.compile(keep_regex)

    keep_indices = _find_keep_indices(raw_lines, head=head, tail=tail, keep_re=keep_re, context=context)
    ordered = sorted(keep_indices)

    rendered = _render_with_gaps(raw_lines, ordered)
    rendered = _collapse_consecutive_duplicates(rendered, max_repeat=max_repeat)

    if max_lines > 0 and len(rendered) > max_lines:
        # Keep head and tail of the rendered excerpt, preserving the final error context.
        half_head = max(1, max_lines // 2)
        half_tail = max(1, max_lines - half_head)
        rendered = rendered[:half_head] + [f"... ({len(rendered) - (half_head + half_tail)} lines omitted for max-lines) ..."] + rendered[-half_tail:]

    stats = CompressionStats(
        source="",
        original_lines=len(raw_lines),
        kept_lines=len(rendered),
        omitted_lines=max(0, len(raw_lines) - len(ordered)),
    )
    return rendered, stats


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Compress long logs/text into high-signal excerpts.")
    parser.add_argument("path", nargs="?", help="Input file path. If omitted, reads from stdin.")
    parser.add_argument("--head", type=int, default=60, help="Keep first N lines (default: 60)")
    parser.add_argument("--tail", type=int, default=120, help="Keep last N lines (default: 120)")
    parser.add_argument("--keep-regex", default=DEFAULT_KEEP_REGEX, help="Regex for evidence lines to always keep")
    parser.add_argument("--context", type=int, default=1, help="Keep +/- N lines around evidence matches")
    parser.add_argument("--max-lines", type=int, default=400, help="Maximum output lines (default: 400; 0 = unlimited)")
    parser.add_argument("--max-repeat", type=int, default=3, help="Max consecutive duplicate lines to keep")

    args = parser.parse_args(argv)

    try:
        text, source = _read_text(args.path)
    except Exception as e:
        print(f"ERROR: could not read input: {e}", file=sys.stderr)
        return 1

    rendered, stats = compress_text(
        text,
        head=max(0, args.head),
        tail=max(0, args.tail),
        keep_regex=args.keep_regex,
        context=max(0, args.context),
        max_lines=args.max_lines,
        max_repeat=max(1, args.max_repeat),
    )

    print("# Compressed Context")
    print(f"Source: {source}")
    print(f"Original: {stats.original_lines} lines")
    print(f"Output:   {len(rendered)} lines")
    print()

    for line in rendered:
        print(line)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
