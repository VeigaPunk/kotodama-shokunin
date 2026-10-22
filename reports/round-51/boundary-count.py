#!/usr/bin/env python3
"""Round-51 claim D counter: the pastoralism entry's section-2 one-owner boundary table.

Prints `rows=<n> resolved=<m> distinct=<k>` for the data rows of the table under
`## 2. One-owner boundary` in the entry (default path below, relative to --root).

* rows      — table data rows (header and separator excluded).
* resolved  — rows whose first cell carries at least one backticked anchor and whose
              every anchor resolves: `name.md:12,:40-44` names exactly one file under
              corpus/knowledge (by basename or knowledge-relative path) and every line
              number is within that file; `dir/` names an existing knowledge directory.
* distinct  — distinct anchor targets (files or directories) across the first cells.

Exit 0 when rows == resolved == distinct (one resolving neighbour per row), else 1;
exit 2 when the entry or the section cannot be read. Read-only; stdlib only.
"""
import argparse
import os
import re
import sys

ENTRY = "corpus/knowledge/culture-material/pastoralism-animal-husbandry.md"
SECTION = "## 2. One-owner boundary"
TOKEN = re.compile(r"`([^`]+)`")
FILE_ANCHOR = re.compile(r"^([\w./-]+\.md)((?::\d+(?:-\d+)?)?(?:,\s*:\d+(?:-\d+)?)*)$")


def knowledge_index(root):
    base = os.path.join(root, "corpus", "knowledge")
    files, dirs = {}, set()
    for dirpath, dirnames, filenames in os.walk(base):
        rel = os.path.relpath(dirpath, base)
        if rel != ".":
            dirs.add(rel.replace(os.sep, "/") + "/")
        for name in filenames:
            if name.endswith(".md"):
                path = os.path.join(dirpath, name)
                relpath = os.path.relpath(path, base).replace(os.sep, "/")
                files.setdefault(name, []).append(path)
                files.setdefault(relpath, []).append(path)
    return files, dirs


def resolve(token, files, dirs):
    """Return the anchor target for a resolving token, else None."""
    if token.endswith("/"):
        return token if token in dirs else None
    match = FILE_ANCHOR.match(token)
    if not match:
        return None
    hits = files.get(match.group(1), [])
    if len(hits) != 1:
        return None
    with open(hits[0], encoding="utf-8") as handle:
        length = sum(1 for _ in handle)
    for start, end in re.findall(r":(\d+)(?:-(\d+))?", match.group(2)):
        last = int(end or start)
        if not 1 <= int(start) <= last <= length:
            return None
    return hits[0]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=os.path.join(os.path.dirname(__file__), "..", ".."))
    parser.add_argument("--entry", default=ENTRY)
    args = parser.parse_args()
    try:
        with open(os.path.join(args.root, args.entry), encoding="utf-8") as handle:
            lines = handle.read().splitlines()
        start = lines.index(SECTION)
    except (OSError, ValueError) as error:
        print(f"BOUNDARY_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    rows = []
    for line in lines[start + 1:]:
        if line.startswith("## "):
            break
        if line.startswith("|"):
            rows.append(line)
    data = [row for row in rows[2:]] if len(rows) >= 2 else []
    files, dirs = knowledge_index(args.root)
    resolved, targets = 0, set()
    for row in data:
        cell = row.split("|")[1]
        tokens = TOKEN.findall(cell)
        hits = [resolve(token.strip(), files, dirs) for token in tokens]
        if tokens and all(hits):
            resolved += 1
        targets.update(hit for hit in hits if hit)
    print(f"rows={len(data)} resolved={resolved} distinct={len(targets)}")
    return 0 if len(data) == resolved == len(targets) else 1


if __name__ == "__main__":
    sys.exit(main())
