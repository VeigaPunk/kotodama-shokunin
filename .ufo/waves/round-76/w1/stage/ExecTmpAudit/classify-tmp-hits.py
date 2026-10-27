#!/usr/bin/env python3
"""Classify every `/tmp` grep hit at the round-76 base revision (read-only).

Input: the stdout of

  git -C <lane> grep -n -E '("/tmp["/]|dir=.?/tmp|mkdtemp\\(\\)|/tmp/)' <base> \\
      -- '*.py' '*.sh'

(<sha>:<path>:<line>:<text>), plus a tree exported from that revision.

Output: one TSV row per hit —
  path, line, scope, kind, scanner, disposition

  scope      active | frozen     (active = tools/ and reports/round-7[3-5] and the
                                  round-75 counter copy; everything else is frozen
                                  evidence of a closed round)
  kind       code | string | comment | shell-code | shell-comment | receipt | unparsed
  scanner    HIT | FALLBACK | UNROUTED | clean   (from check-scratch-root.py)
  disposition a one-line reading of what the hit is

Stdlib only; writes only its own stdout.
"""
from __future__ import annotations

import importlib.util
import io
import os
import re
import sys
import tokenize

HIT_RE = re.compile(r"^(?P<sha>[0-9a-f]{40}):(?P<path>[^:]+):(?P<line>\d+):(?P<text>.*)$")
ACTIVE_RE = re.compile(
    r"^(?:tools/|reports/round-7[3-5]/|\.ufo/waves/round-75/(?:counters|w2/stage/reports)/)")


def load_scanner(path):
    spec = importlib.util.spec_from_file_location("scratch_root_scanner", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def line_offsets(raw):
    offsets, cursor = {}, 0
    for number, text in enumerate(raw.splitlines(keepends=True), 1):
        offsets[number] = cursor
        cursor += len(text)
    return offsets


def python_kind(path, line, needles):
    """code | string | comment for a python line, by token coverage."""
    try:
        with open(path, "rb") as handle:
            raw = handle.read()
        text = raw.decode("utf-8", "replace")
    except OSError:
        return "unread"
    offsets = line_offsets(text)
    spans = []
    try:
        for token in tokenize.generate_tokens(io.StringIO(text).readline):
            if token.type in (tokenize.STRING, tokenize.COMMENT):
                spans.append((token.start[0], token.end[0], token.type))
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return "unparsed"
    start = offsets.get(line, 0)
    want = start + needles
    kinds = set()
    for begin, end, kind in spans:
        if begin <= line <= end:
            kinds.add(kind)
    if tokenize.COMMENT in kinds and tokenize.STRING not in kinds:
        return "comment"
    if tokenize.STRING in kinds and tokenize.COMMENT not in kinds:
        return "string"
    if kinds:
        return "string-or-comment"
    return "code"


def shell_kind(stripped_present):
    return "shell-code" if stripped_present else "shell-comment"


def disposition(scope, kind, scanner_class):
    if scanner_class == "HIT":
        return ("literal /tmp scratch root (write target)" if scope == "active"
                else "frozen: literal /tmp scratch root, round closed, never edited")
    if scanner_class == "FALLBACK":
        return "env fallback: TMPDIR falls back to literal /tmp when unset"
    if scanner_class == "UNROUTED":
        return "tempdir created with no dir= (honours TMPDIR, bypasses --work/$HYAKU_SCRATCH)"
    if kind == "receipt":
        return "frozen run receipt (captured stdout of a past run, not code)"
    if kind in ("string", "string-or-comment", "comment", "shell-comment"):
        return "doc string / prompt text / comment — no write path"
    if kind in ("code", "shell-code"):
        return "code position, read-only or guard use — no /tmp write target"
    return "unclassified"


def main(argv):
    hits_path, tree, scanner_path = argv[1], argv[2], argv[3]
    scanner = load_scanner(scanner_path)
    rows = []
    cache = {}
    with open(hits_path, "r", encoding="utf-8", errors="replace") as handle:
        for raw in handle:
            match = HIT_RE.match(raw.rstrip("\n"))
            if not match:
                continue
            path = match.group("path")
            line = int(match.group("line"))
            text = match.group("text")
            scope = "active" if ACTIVE_RE.match(path) else "frozen"
            absolute = os.path.join(tree, path)
            if path.endswith((".txt", ".md", ".out")):
                kind = "receipt"
            elif path.endswith((".sh", ".bash")):
                stripped = scanner.strip_shell_comment(text)
                kind = shell_kind("/tmp" in stripped)
            else:
                needles = [m.start() for m in re.finditer(r"/tmp", text)] or [0]
                kind = python_kind(absolute, line, needles[0])
            key = (path, os.path.dirname(absolute) or tree)
            if key not in cache:
                found, rel = scanner.scan_file(absolute, tree)
                cache[key] = {(ln, cls) for ln, cls, _ in found}
            classes = [cls for (ln, cls) in cache[key] if ln == line]
            scanner_class = classes[0] if classes else "clean"
            rows.append((path, line, scope, kind, scanner_class,
                         disposition(scope, kind, scanner_class)))
    print("path\tline\tscope\tkind\tscanner\tdisposition")
    for row in rows:
        print("\t".join(str(cell) for cell in row))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
