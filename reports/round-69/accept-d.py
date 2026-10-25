#!/usr/bin/env python3
r"""Round-69 depth acceptance counter — claim D2 (NEW counter).

Depth is verifiable technical detail a reader can act on from SKILL.md alone:
a decision table with real thresholds, named error signatures and cited
sources. Claim D2's surface is SKILL.md's new `### Registry correction chains`
decision table: the five supersession-chain states, each with its row shape,
the writer's next action, a named error signature and an evidence pointer,
with the five signatures also listed under `## Error patterns` and the table
citing a mined S-row.

This counter is a NEW file. The round-68 counters are not edited.

Usage:
  --root DIR   evaluate claim D2 against the lane tree at DIR (default ".")
  --selftest   run the GREEN control (a fixture SKILL.md that carries the
               table) and the DO-NOTHING control (the same tree with the table
               removed, which must be caught).

Exit codes: 0 pass · 1 fail · 2 usage/env.
Reads only. No network. No mutation of the lane tree.
"""

import argparse
import hashlib
import os
import re
import sys
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(HERE))
SELF = os.path.basename(__file__)

HEADING = "### Registry correction chains"
STATES = ("pending", "settled-active", "settled-retired", "settled-closed",
          "settled-split")
PATH_RE = re.compile(r"[A-Za-z0-9_./-]+\.(?:py|md|tsv|txt|json|ya?ml)")
SID_RE = re.compile(r"S\d{3,}")
ROW_RE = re.compile(r"^\|\s*(S\d{3,})\s*\|")

FIXTURE_TABLE = """### Registry correction chains

| State | Row shape | Writer's next action | Error signature | Evidence |
|---|---|---|---|---|
| pending | successor mined, target mined | decide the ruling | chain-left-pending | S859 — tools/check-supersession-settlement.py:112 |
| settled-active | successor mined, target queued | repoint the entry | entry-not-repointed | S859 — tools/check-supersession-settlement.py:127 |
| settled-retired | successor rejected | keep the target | retired-row-mined | S859 — tools/check-supersession-settlement.py:129 |
| settled-closed | target rejected | keep the successor | closed-chain-kept | S859 — tools/check-supersession-settlement.py:123 |
| settled-split | both mined, scoped teaches | narrow the scope | scope-limiter-missing | S859 — tools/check-supersession-settlement.py:130 |
"""

FIXTURE_SIGNATURES = """| Observation | Reading |
|---|---|
| chain-left-pending | the correction never landed; rule the chain |
| entry-not-repointed | the successor is mined but no entry cites it |
| retired-row-mined | a retired correction still reads as mined |
| closed-chain-kept | the closed chain's successor was dropped |
| scope-limiter-missing | both rows are mined without a scope limiter |
"""


def sha256_file(path):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(65536), b""):
                h.update(chunk)
    except OSError:
        return None
    return h.hexdigest()


def read_text(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return None


def section_span(lines, heading):
    """(start, end) line indexes of the section whose heading is *heading*."""
    for i, line in enumerate(lines):
        if line.strip() == heading:
            start = i
            for j in range(i + 1, len(lines)):
                if lines[j].startswith("## "):
                    return start, j
            return start, len(lines)
    return None, None


def parse_table(lines, start):
    """(header_cells, data_rows) of the first markdown table after *start*."""
    i = start
    while i < len(lines) and not lines[i].strip().startswith("|"):
        i += 1
    if i >= len(lines):
        return None, []
    header = [c.strip() for c in lines[i].strip().split("|")[1:-1]]
    rows = []
    j = i + 1
    while j < len(lines) and lines[j].strip().startswith("|"):
        cells = [c.strip() for c in lines[j].strip().split("|")[1:-1]]
        if not all(set(c) <= set("-: ") for c in cells):
            rows.append(cells)
        j += 1
    return header, rows


class Result(object):
    def __init__(self, quiet=False):
        self.legs = []
        self.quiet = quiet

    def add(self, name, ok, detail=""):
        self.legs.append((name, bool(ok), detail))
        if not self.quiet:
            print("LEG %s %s %s" % ("PASS" if ok else "FAIL", name, detail))

    @property
    def ok(self):
        return all(ok for _, ok, _ in self.legs)


def evaluate(root, res):
    root = os.path.abspath(root)
    skill = read_text(os.path.join(root, "SKILL.md"))
    lines = skill.splitlines() if skill else []

    mine = sha256_file(os.path.join(HERE, SELF))
    committed = sha256_file(os.path.join(root, "reports", "round-69", SELF))
    res.add("STAMP", bool(mine) and mine == committed,
            "self=%s committed=%s" % ((mine or "none")[:12],
                                      (committed or "none")[:12]))

    start, end = section_span(lines, HEADING)
    res.add("SECTION", start is not None, "heading=%s" % HEADING)
    if start is None:
        for name in ("TABLE", "STATES", "FIELDS", "SIGNATURES", "EVIDENCE",
                     "SOURCE"):
            res.add(name, False, "no decision table")
        return res

    header, rows = parse_table(lines, start)
    res.add("TABLE", header is not None and len(header) == 5
            and len(rows) == 5,
            "header=%s rows=%d" % (len(header) if header else 0, len(rows)))

    got = [r[0].lower() for r in rows if r]
    res.add("STATES", got == list(STATES), "states=%s" % got)

    empty = [(i + 1, j) for i, r in enumerate(rows) for j, c in enumerate(r)
             if not c.strip()]
    short = [i + 1 for i, r in enumerate(rows) if len(r) != 5]
    res.add("FIELDS", not empty and not short,
            "empty=%s short=%s" % (empty or "none", short or "none"))

    ep_start, ep_end = section_span(lines, "## Error patterns")
    ep_text = "\n".join(lines[ep_start:ep_end]) if ep_start is not None else ""
    missing_sig = [r[3] for r in rows if len(r) >= 4 and r[3]
                   and r[3] not in ep_text]
    res.add("SIGNATURES", not missing_sig,
            "missing=%s" % (missing_sig or "none"))

    missing_ev = []
    for r in rows:
        if len(r) < 5:
            missing_ev.append("row-short")
            continue
        toks = PATH_RE.findall(r[4])
        if not any(os.path.exists(os.path.join(root, t)) for t in toks):
            missing_ev.append(r[4][:40])
    res.add("EVIDENCE", not missing_ev, "unresolved=%s" % (missing_ev or "none"))

    table_text = "\n".join("|".join(r) for r in rows)
    sources = read_text(os.path.join(root, "corpus", "SOURCES.md")) or ""
    good = []
    for sid in SID_RE.findall(table_text):
        for line in sources.splitlines():
            m = ROW_RE.match(line.strip())
            if not m or m.group(1) != sid:
                continue
            cells = [c.strip() for c in line.strip().split("|")[1:-1]]
            if len(cells) == 11 and cells[7] == "mined" \
                    and "SKILL.md" in cells[10]:
                good.append(sid)
    res.add("SOURCE", bool(good), "mined_used_by_SKILL=%s" % (good or "none"))
    return res


def build_fixture_root(fx, *, with_table):
    os.makedirs(os.path.join(fx, "corpus", "knowledge"), exist_ok=True)
    skill = os.path.join(fx, "SKILL.md")
    base = read_text(os.path.join(LANE, "SKILL.md")) or "# fixture\n"
    if not with_table:
        # R69-M11: seed the do-nothing fixture from the committed pre-table
        # base (793f797:SKILL.md) so the tree genuinely lacks the table; the
        # live SKILL.md now carries it after the registry-correction-chains
        # repair. Fall back to the live file only if git is unavailable.
        try:
            out = subprocess.check_output(
                ["git", "-C", LANE, "show", "793f797:SKILL.md"],
                stderr=subprocess.DEVNULL, text=True)
            if out:
                base = out
        except Exception:
            pass
    if with_table:
        base = base.replace("## Error patterns",
                            FIXTURE_TABLE + "\n## Error patterns", 1)
        base = base.replace("## Error patterns",
                            "## Error patterns\n" + FIXTURE_SIGNATURES, 1)
        if FIXTURE_TABLE not in base:
            base = base + "\n" + FIXTURE_TABLE + "\n" + FIXTURE_SIGNATURES
    with open(skill, "w", encoding="utf-8") as fh:
        fh.write(base)
    src = os.path.join(LANE, "corpus", "SOURCES.md")
    dst = os.path.join(fx, "corpus", "SOURCES.md")
    if os.path.exists(src):
        with open(src, encoding="utf-8") as fh:
            text = fh.read()
    else:
        text = ""
    if "S859" not in text:
        text += ("\n| S859 | fixture source — https://example.invalid/x | "
                 "own-work | A | fixture | §1 | the fixture teaches | mined | "
                 "2026-10-24 | 90d | SKILL.md |\n")
    with open(dst, "w", encoding="utf-8") as fh:
        fh.write(text)
    kb = os.path.join(fx, "corpus", "knowledge", "a.md")
    with open(kb, "w", encoding="utf-8") as fh:
        fh.write("fixture\n")
    tools = os.path.join(fx, "tools")
    os.makedirs(tools, exist_ok=True)
    for rel in ("tools/check-supersession-settlement.py",):
        src = os.path.join(LANE, rel)
        if os.path.exists(src):
            with open(src, "rb") as fh:
                data = fh.read()
            with open(os.path.join(fx, rel), "wb") as fh:
                fh.write(data)
    src = os.path.join(LANE, "reports", "round-69", "accept-d.py")
    dst = os.path.join(fx, "reports", "round-69", "accept-d.py")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(src, "rb") as fh:
        data = fh.read()
    with open(dst, "wb") as fh:
        fh.write(data)


def selftest():
    with tempfile.TemporaryDirectory(prefix="d69-selftest-") as td:
        green = os.path.join(td, "green")
        build_fixture_root(green, with_table=True)
        r1 = Result(quiet=True)
        evaluate(green, r1)
        green_ok = r1.ok
        print("GREEN FIXTURE: %s (legs %d/%d)" % (
            "PASS" if green_ok else "FAIL",
            sum(1 for _, ok, _ in r1.legs if ok), len(r1.legs)))

        nothing = os.path.join(td, "donothing")
        build_fixture_root(nothing, with_table=False)
        r2 = Result(quiet=True)
        evaluate(nothing, r2)
        nothing_fails = not r2.ok
        print("DO-NOTHING FIXTURE: %s (legs %d/%d)" % (
            "FAIL (as required)" if nothing_fails else "PASS (unexpected)",
            sum(1 for _, ok, _ in r2.legs if ok), len(r2.legs)))
        print("SELFTEST: %d/2" % (sum([green_ok, nothing_fails])))
        return 0 if (green_ok and nothing_fails) else 1


def main():
    ap = argparse.ArgumentParser(description="round-69 depth counter")
    ap.add_argument("--root", default=".")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    res = Result()
    evaluate(args.root, res)
    passed = sum(1 for _, ok, _ in res.legs if ok)
    print("ACCEPT-D-69: %s legs=%d/%d" % (
        "PASS" if res.ok else "FAIL", passed, len(res.legs)))
    return 0 if res.ok else 1


if __name__ == "__main__":
    sys.exit(main())
