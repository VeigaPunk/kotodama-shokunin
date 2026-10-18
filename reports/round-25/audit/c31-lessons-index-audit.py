#!/usr/bin/env python3
"""C31..C34 — lessons-index audit (round 25), read-only.

Answers one question per run: does `corpus/lessons/README.md` reconcile the
lesson partition it claims to index?

  R25-C31  index rows == files: every `corpus/lessons/*.md` file has exactly
           one README row, and every README row names a file on disk.
  R25-C32  every open-question queue row in the README carries an owner that
           resolves to a live lane surface (a path on disk, or the literal
           token `operator`, or a `round-N` pointer that resolves).
  R25-C33  the three census formats the README documents are the three the
           partition actually carries (gate-keeper / fragment-index / plain).
  R25-C34  independent re-derivation: the per-row `bytes`/`lines`/`sha8`
           columns are re-measured from the live bytes, never inherited.

Stdlib only. Opens no file for writing: the receipt is the caller's stdout
redirect. `--selftest` runs in-memory controls and writes nothing.

    export TMPDIR=$PWD/.scratch
    python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest
    python3 -B reports/round-25/audit/c31-lessons-index-audit.py
    python3 -B reports/round-25/audit/c31-lessons-index-audit.py --json
"""

import argparse
import glob
import hashlib
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
LESSONS = os.path.join(ROOT, "corpus", "lessons")
INDEX = os.path.join(LESSONS, "README.md")

# A row is `| `corpus/lessons/name.md` | ... |`. The first column names the
# file repo-relative, matching the round-25 runner's own row regex
# (`reports/round-25/run-validation.py:121`), so the two agree on what an
# index row is. Columns follow.
ROW_RE = re.compile(r"(?m)^\|\s*`?corpus/lessons/([A-Za-z0-9_.-]+\.md)`?\s*\|(.*)\|\s*$")
# `bytes=1234`, `lines=56`, `sha8=abcdef12` cells inside a row. The self-row
# for the README carries `sha8=self-referential`, which is not a digest.
CELL_RE = re.compile(r"(bytes|lines|sha8)=([0-9a-f]+|self-referential)")

FORMAT_MARKERS = (
    # (documented format name, predicate over file text). The Gate heading is
    # matched exactly: `## Gate candidates` (round 7) and `## Gates are real`
    # (round 1) are prose headings, not gate sections.
    ("gate-keeper", lambda t: bool(re.search(r"^## Gate\s*$", t, re.M))),
    ("fragment-index", lambda t: bool(re.search(r"^## Fragment index\s*$", t, re.M))),
    ("plain", lambda t: True),  # fallback class; assigned only when neither above
)

CONTRACT_LINES = ("source:", "verified-at:", "recheck:", "scope:")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def read_text(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def classify(text):
    """Return the census-format class of a lesson file's own bytes."""
    if FORMAT_MARKERS[1][1](text):
        return "fragment-index"
    if FORMAT_MARKERS[0][1](text):
        return "gate-keeper"
    return "plain"


def contract_lines(text):
    """The four lesson contract lines, matched as whole-file `^key:` anchors.

    The convention is the round-23 X09 tool's (`reports/round-23/audit/
    x09-lessons-audit.py:102`): a line-start anchor anywhere in the file. A
    fixed leading window was tried first and under-counted `scope:` on the
    lessons that place it after their opening census block.
    """
    return [k for k in CONTRACT_LINES if re.search(rf"^{k}", text, re.M)]


def census():
    """Live, re-measured census of the lesson partition.

    The partition is `corpus/lessons/*.md` exactly as the round-25 runner
    globs it (`reports/round-25/run-validation.py:761`), which includes this
    README. The README is indexed as its own row rather than skipped, so the
    index's row set and the runner's file set are the same set.
    """
    rows = []
    for path in sorted(glob.glob(os.path.join(LESSONS, "*.md"))):
        name = os.path.basename(path)
        text = read_text(path)
        lines = text.splitlines()
        rows.append(
            {
                "file": name,
                "bytes": os.path.getsize(path),
                "lines": len(lines),
                "sha256": sha256_file(path),
                "sha8": sha256_file(path)[:8],
                "format": classify(text),
                "contract_lines": contract_lines(text),
            }
        )
    return rows


def parse_index(path):
    """Return (declared_file_rows, queue_rows, prose) from the README."""
    if not os.path.exists(path):
        return None
    text = read_text(path)
    file_rows = []
    for line in text.splitlines():
        m = ROW_RE.match(line)
        if m:
            cells = dict(CELL_RE.findall(line))
            file_rows.append({"file": m.group(1), "cells": cells, "raw": line})
    queue_rows = []
    for line in text.splitlines():
        if line.startswith("| Q-") and not line.startswith("| Q-id"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            queue_rows.append({"id": cells[0], "cells": cells, "raw": line})
    return {"file_rows": file_rows, "queue_rows": queue_rows, "text": text}


def owner_cell(line):
    """Extract the owner cell from a queue row, or "" if the row is malformed.

    The row is `| Q-id | question | owner | status |`. A question may itself
    contain a literal pipe; Markdown requires it escaped as `\\|` (`--profile
    v2\\|v3`), so the split ignores escaped pipes. A row that still yields
    more than four cells is malformed — an unescaped pipe in a cell — and is
    reported as "" rather than silently misread as a different column.
    """
    parts = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
    return parts[2] if len(parts) == 4 else ""


def resolves(owner_token):
    """An owner resolves if it names a live path, `operator`, or a round token."""
    tok = owner_token.replace("`", "").strip()
    # Drop a trailing parenthetical annotation: the owner is what precedes it.
    tok = re.sub(r"\s*\([^()]*\)\s*$", "", tok).strip()
    if not tok:
        return False, "empty"
    if tok in ("operator", "parent", "lore-shokunin", "integrator"):
        return True, "role-token"
    if re.fullmatch(r"round-\d+", tok):
        # A round pointer resolves iff that round's directory exists.
        return os.path.isdir(os.path.join(ROOT, "reports", tok)), "round-pointer"
    # Otherwise: treat as a repo-relative path.
    cand = os.path.join(ROOT, tok)
    if os.path.exists(cand):
        return True, "path"
    return False, "unresolved"


def run_checks():
    live = census()
    live_by_name = {r["file"]: r for r in live}
    idx = parse_index(INDEX)
    findings = []
    checks = {}

    if idx is None:
        return {
            "index_present": False,
            "lesson_files": len(live),
            "findings": [
                {
                    "id": "C31-0",
                    "class": "missing-index",
                    "detail": "corpus/lessons/README.md does not exist",
                }
            ],
            "checks": {},
            "live": live,
        }

    indexed = [r["file"] for r in idx["file_rows"]]
    # C31 — set equality, plus no duplicates.
    missing_from_index = sorted(set(live_by_name) - set(indexed))
    ghosts = sorted(set(indexed) - set(live_by_name))
    dupes = sorted({n for n in indexed if indexed.count(n) > 1})
    checks["C31_index_rows_eq_files"] = (
        not missing_from_index and not ghosts and not dupes
    )
    if missing_from_index:
        findings.append(
            {"id": "C31-1", "class": "unindexed-file", "detail": missing_from_index}
        )
    if ghosts:
        findings.append(
            {"id": "C31-2", "class": "ghost-row", "detail": ghosts}
        )
    if dupes:
        findings.append(
            {"id": "C31-3", "class": "duplicate-row", "detail": dupes}
        )

    # C32 — every queue row owner resolves.
    bad_owners = []
    for row in idx["queue_rows"]:
        cell = owner_cell(row["raw"])
        if not cell:
            bad_owners.append((row["id"], "<no owner cell>"))
            continue
        ok, why = resolves(cell)
        if not ok:
            bad_owners.append((row["id"], cell, why))
    checks["C32_owners_resolve"] = not bad_owners
    if bad_owners:
        findings.append(
            {"id": "C32-1", "class": "unresolvable-owner", "detail": bad_owners}
        )

    # C33 — documented formats == live formats.
    declared_formats = set()
    for name in ("gate-keeper", "fragment-index", "plain"):
        if name in idx["text"]:
            declared_formats.add(name)
    live_formats = {r["format"] for r in live}
    checks["C33_formats_documented"] = live_formats.issubset(declared_formats)
    if not live_formats.issubset(declared_formats):
        findings.append(
            {
                "id": "C33-1",
                "class": "undocumented-format",
                "detail": sorted(live_formats - declared_formats),
            }
        )

    # C34 — per-row byte/line/sha8 cells re-derived from live bytes. The
    # README's own self-row is exempt by construction: a file cannot carry its
    # own digest, so its `sha8=self-referential` is documented, not measured.
    SELF_ROW = "README.md"
    drift = []
    for row in idx["file_rows"]:
        name = row["file"]
        if name not in live_by_name:
            continue
        if name == SELF_ROW:
            continue
        if not row["cells"]:
            drift.append((name, "no bytes/lines/sha8 cells"))
            continue
        live_row = live_by_name[name]
        for key, want in row["cells"].items():
            got = live_row["sha8"] if key == "sha8" else live_row[key]
            if str(got) != str(want):
                drift.append((name, key, want, got))
    checks["C34_pins_rederived"] = not drift
    if drift:
        findings.append({"id": "C34-1", "class": "pin-drift", "detail": drift})

    # C34c — the per-row `format` and `contract` cells must match the
    # measurement too. A table whose pin cells are live but whose shape cells
    # are stale is half-reconciled. The self-row's `—` cells are exempt.
    shape_drift = []
    for line in idx["text"].splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        name = m.group(1)
        if name not in live_by_name or name == SELF_ROW:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        want_format, want_contract = cells[1], cells[2]
        got_format = live_by_name[name]["format"]
        got_contract = f"{len(live_by_name[name]['contract_lines'])}/4"
        if want_format != got_format:
            shape_drift.append((name, "format", want_format, got_format))
        if want_contract != got_contract:
            shape_drift.append((name, "contract", want_contract, got_contract))
    checks["C34c_shape_cells_rederived"] = not shape_drift
    if shape_drift:
        findings.append({"id": "C34-3", "class": "shape-cell-drift", "detail": shape_drift})

    # C34b — the index's own prose arithmetic must match the measurement. A
    # self-referential index that states a row count it does not have is the
    # defect this whole claim exists to prevent.
    stated = {}
    for m in re.finditer(r"Rows:\s*\*\*(\d+)\*\*", idx["text"]):
        stated.setdefault("queue", []).append(int(m.group(1)))
    for m in re.finditer(r"\*\*Rows:\s*(\d+)\.\s*Files:\s*(\d+)\.\*\*", idx["text"]):
        stated["table"] = [int(m.group(1)), int(m.group(2))]
    arithmetic_ok = True
    detail = {}
    if stated.get("queue") and stated["queue"][0] != len(idx["queue_rows"]):
        arithmetic_ok = False
        detail["queue_rows"] = {"stated": stated["queue"][0], "measured": len(idx["queue_rows"])}
    if stated.get("table") and (
        stated["table"][0] != len(idx["file_rows"])
        or stated["table"][1] != len(live)
    ):
        arithmetic_ok = False
        detail["table_rows_vs_files"] = {
            "stated": stated["table"],
            "measured": [len(idx["file_rows"]), len(live)],
        }
    checks["C34b_prose_arithmetic"] = arithmetic_ok
    if not arithmetic_ok:
        findings.append({"id": "C34-2", "class": "prose-arithmetic-drift", "detail": detail})

    return {
        "index_present": True,
        "lesson_files": len(live),
        "index_rows": len(idx["file_rows"]),
        "queue_rows": len(idx["queue_rows"]),
        "format_histogram": {f: sum(1 for r in live if r["format"] == f) for f in ("gate-keeper", "fragment-index", "plain")},
        "checks": checks,
        "findings": findings,
        "live": live,
        "index_sha256": sha256_file(INDEX),
    }


# --------------------------------------------------------------------------
# Selftest — in-memory controls, no file written.
# --------------------------------------------------------------------------


def selftest():
    ok = 0
    total = 0

    def check(label, cond):
        nonlocal ok, total
        total += 1
        if cond:
            ok += 1
            print(f"  PASS {label}")
        else:
            print(f"  FAIL {label}")

    # control 1: row regex captures a well-formed index row and its cells.
    # The first column is repo-relative, matching the runner's row contract.
    line = "| `corpus/lessons/round-5.md` | gate-keeper | 2 | bytes=8684 lines=117 sha8=deadbeef |"
    m = ROW_RE.match(line)
    check("row regex captures name", bool(m) and m.group(1) == "round-5.md")
    check("cell regex captures bytes/lines/sha8", dict(CELL_RE.findall(line)) == {"bytes": "8684", "lines": "117", "sha8": "deadbeef"})
    check("row regex matches the runner's row contract",
          {x.group(1) for x in ROW_RE.finditer(
              "| round-10.md | gate-keeper | 2 |\n"
              "| `corpus/lessons/round-5.md` | plain | 0 |\n")} == {"round-5.md"})
    check("self-row sha8 token parses",
          dict(CELL_RE.findall(
              "| `corpus/lessons/README.md` | index | — | bytes=0 lines=0 sha8=self-referential |"
          )) == {"bytes": "0", "lines": "0", "sha8": "self-referential"})

    # control 2: negative — a non-row line must not match
    check("non-row rejected", ROW_RE.match("Some prose line, no pipes.") is None)
    check("header row rejected", ROW_RE.match("| file | format | open-questions |") is None)

    # control 3: format classifier, all three classes plus precedence
    check("fragment-index wins over gate-keeper",
          classify("# X\n## Fragment index\n## Gate\n") == "fragment-index")
    check("gate-keeper class", classify("# X\n## Gate\n") == "gate-keeper")
    check("plain class", classify("# X\n## What moved\n") == "plain")
    check("prose Gate heading is not a gate section",
          classify("# X\n## Gate candidates\n") == "plain")

    # control 3b: the contract scan is whole-file and line-anchored — a
    # `scope:` line far down the file counts, a mid-line `xscope:` does not
    probe = "# H\nsource: a\nverified-at: b\nrecheck: c\n" + "\n" * 40 + "scope: d\nxscope: e\n"
    check("contract scan is whole-file", contract_lines(probe) == ["source:", "verified-at:", "recheck:", "scope:"])
    check("contract scan is line-anchored", contract_lines("source: a\nnote: b\n") == ["source:"])

    # control 4: owner resolution — positive path, positive token, negative
    okp, why = resolves("corpus/lessons/round-2-adjacency.md")
    check("owner path resolves", okp and why == "path")
    check("operator token resolves", resolves("operator")[0])
    check("round pointer resolves", resolves("round-24")[0])
    check("empty owner does not resolve", not resolves("")[0])
    check("missing path does not resolve",
          not resolves("corpus/lessons/__no_such_file__.md")[0])
    check("owner with parenthetical annotation resolves",
          resolves("`corpus/lessons/README.md` (claim C)")[0])

    # control 4b: the owner cell is read from a 4-cell row, and a row that
    # gains cells (an unescaped pipe in a cell) is refused, not misread.
    check("owner cell immune to a properly escaped inner pipe",
          owner_cell("| Q-x | a `v2\\|v3` route | `operator` | open |") == "`operator`")
    check("owner cell on a well-formed row",
          owner_cell("| Q-x | q | `operator` | open |") == "`operator`")
    check("owner cell absent on a short row", owner_cell("| Q-x | q |") == "")
    check("malformed row (unescaped inner pipe) refused",
          owner_cell("| Q-x | a `v2|v3` route | `operator` | open |") == "")

    # control 5: live census is non-empty and sha8 is 8 hex chars. The README
    # is part of the partition (the runner's glob includes it), so it IS in the
    # census; the index must carry a row for it.
    live = census()
    check("census non-empty", len(live) > 0)
    check("sha8 well-formed", all(re.fullmatch(r"[0-9a-f]{8}", r["sha8"]) for r in live))
    check("README is in the census (partition = the runner's glob)",
          any(r["file"] == "README.md" for r in live))

    # control 6: re-derivation is real — recompute one file's bytes independently
    probe = live[0]
    again = os.path.getsize(os.path.join(LESSONS, probe["file"]))
    check("bytes re-derivation stable", again == probe["bytes"])

    # control 7: the prose-arithmetic regexes both fire, and the drift path is
    # reachable — a stated count that disagrees with the measurement must be
    # detectable, else C34b could never go red.
    fake = "Rows: **999**.\n\n**Rows: 999. Files: 1.**\n"
    stated = {}
    for m in re.finditer(r"Rows:\s*\*\*(\d+)\*\*", fake):
        stated.setdefault("queue", []).append(int(m.group(1)))
    for m in re.finditer(r"\*\*Rows:\s*(\d+)\.\s*Files:\s*(\d+)\.\*\*", fake):
        stated["table"] = [int(m.group(1)), int(m.group(2))]
    check("arithmetic regexes fire", stated.get("queue") == [999] and stated.get("table") == [999, 1])
    check("arithmetic drift detectable",
          stated["queue"][0] != len(live) and stated["table"][1] != len(live))

    print(f"SELFTEST {'OK' if ok == total else 'FAILED'}: {ok}/{total} checks passed")
    return 0 if ok == total else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    res = run_checks()
    if args.json:
        print(json.dumps(res, indent=1, sort_keys=True))
        return 0

    print(f"index present: {res['index_present']}")
    print(f"lesson files:  {res['lesson_files']}")
    if res["index_present"]:
        print(f"index rows:    {res['index_rows']}")
        print(f"queue rows:    {res['queue_rows']}")
        print(f"formats:       {res['format_histogram']}")
        for k, v in res["checks"].items():
            print(f"  {'PASS' if v else 'FAIL'} {k}")
    print(f"findings:      {len(res['findings'])}")
    for f in res["findings"]:
        print(f"  {f['id']} {f['class']}: {f['detail']}")
    return 0 if not res["findings"] else 1


if __name__ == "__main__":
    sys.exit(main())
