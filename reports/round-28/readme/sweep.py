#!/usr/bin/env python3
"""R28-C47 — corpus/README.md index + counts-footer sweep (read-only).

Round 27's sweep (`reports/round-27/readme/sweep.py`, 9/9 controls) checked the
index rows against the files they name: section headers, row topics, ghosts,
missing rows and the totals line. It did **not** check the counts footer, and
that is where round 28 found a live defect:

    Counts checked 2026-10-18 from the repo root:
    `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
    (total 199 files; directory totals 19/19/18/29/20/94).

Revision 1.7 (round 27) moved `linguistics` 19 -> 20 and the totals line
199 -> 200 in the same file, but left this present-tense footer reading 199/19.
Round 27's sweep went green because it never read the footer. This instrument
adds that leg.

Legs (all measured, none asserted):

  index    rows / files / ghosts / missing / duplicate rows / topic equality /
           section-header drift / totals line        (inherited from r27)
  footer   the `Counts checked <date> ...` block's `(total N files; directory
           totals a/b/c/d/e/f)` vs the live tree, and its six directory totals
           vs the six live directory counts, in the README's own section order
  block    the `Total knowledge entries: N.` line vs the live file total
           (inherited; reported separately so a totals-only drift is visible)

The tool is read-only over the repo: it opens `corpus/README.md` and
`corpus/knowledge/**` for reading and has no code path that writes inside the
lane.

Usage:
    python3 reports/round-28/readme/sweep.py            # text summary, exit 0/1
    python3 reports/round-28/readme/sweep.py --json     # receipt on stdout
    python3 reports/round-28/readme/sweep.py --selftest # in-memory controls
"""
import argparse
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
README = os.path.join(LANE, "corpus", "README.md")
KNOWLEDGE = os.path.join(LANE, "corpus", "knowledge")

# The README's section order is the canonical partition order the index uses.
PARTS = [
    "linguistics",
    "myth-symbol",
    "culture-material",
    "synthesis",
    "verification",
    "civilizations",
]

SECTION_RE = re.compile(r"^## ([a-z-]+)/ \((\d+)\)\s*$", re.M)
ROW_RE = re.compile(r"^- `([^`]+\.md)` — (.*)$", re.M)
TOPIC_RE = re.compile(r"^- topic:(.*?)(?=\n- \w)", re.M | re.S)
TOTALS_RE = re.compile(r"^Total knowledge entries: (\d+)\.\s*$", re.M)

# The counts footer: a dated present-tense claim carrying the command that
# produces it, a file total, and the six directory totals in section order.
FOOTER_RE = re.compile(
    r"^Counts checked (\d{4}-\d{2}-\d{2}) from the repo root:\n"
    r"`([^`]+)`\n"
    r"\(total (\d+) files; directory totals ([\d/]+)\)\.",
    re.M,
)


def topic_of(path):
    """The entry's own `- topic:` head-block text, continuations space-joined."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    m = TOPIC_RE.search(text)
    if not m:
        return None
    parts = [ln.strip() for ln in m.group(1).strip("\n").splitlines()]
    return " ".join(p for p in parts if p)


def parse_readme(text):
    """Sections in file order: {part: {'declared': N, 'rows': [(file, topic)]}}."""
    marks = [(m.start(), m.group(1), int(m.group(2))) for m in SECTION_RE.finditer(text)]
    out = {}
    for i, (pos, part, declared) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        body = text[pos:end]
        rows = [(m.group(1), m.group(2)) for m in ROW_RE.finditer(body)]
        out[part] = {"declared": declared, "rows": rows}
    return out


def disk_files(root, part):
    d = os.path.join(root, part)
    if not os.path.isdir(d):
        return []
    return sorted(
        f for f in os.listdir(d) if f.endswith(".md") and os.path.isfile(os.path.join(d, f))
    )


def footer_reading(text):
    """The counts-footer block, parsed. None when the block is absent."""
    m = FOOTER_RE.search(text)
    if not m:
        return None
    return {
        "date": m.group(1),
        "command": m.group(2),
        "total": int(m.group(3)),
        "dir_totals": [int(x) for x in m.group(4).split("/")],
    }


def sweep(readme_text, root_override=None):
    """The measurement. `root_override` swaps the knowledge tree (selftest)."""
    root = root_override if root_override is not None else KNOWLEDGE
    sections = parse_readme(readme_text)
    parts = {}
    missing, ghosts, mismatches, drift = [], [], [], {}
    for part in sorted(sections):
        sec = sections[part]
        files = disk_files(root, part)
        fileset = set(files)
        rowfiles = [f for f, _ in sec["rows"]]
        seen = set(rowfiles)
        dup = sorted(f for f in seen if rowfiles.count(f) > 1)
        for f in sorted(fileset - seen):
            missing.append(f"{part}/{f}")
        for f in sorted(seen - fileset):
            ghosts.append(f"{part}/{f}")
        for f, topic in sec["rows"]:
            if f not in fileset:
                continue
            real = topic_of(os.path.join(root, part, f))
            if real is None or topic != real:
                mismatches.append(
                    {
                        "row": f"{part}/{f}",
                        "class": "NO_TOPIC_FIELD" if real is None else "REWRITE",
                        "row_chars": len(topic),
                        "topic_chars": None if real is None else len(real),
                    }
                )
        if sec["declared"] != len(files):
            drift[part] = {"declared": sec["declared"], "files": len(files)}
        parts[part] = {
            "declared": sec["declared"],
            "rows": len(rowfiles),
            "files": len(files),
            "duplicate_rows": dup,
        }

    total_files = sum(p["files"] for p in parts.values())
    total_rows = sum(p["rows"] for p in parts.values())
    tm = TOTALS_RE.search(readme_text)
    totals_line = int(tm.group(1)) if tm else None

    # the footer leg — measured, not asserted
    footer = footer_reading(readme_text)
    live_order = [p for p in PARTS if p in parts]
    footer_findings = []
    if footer is None:
        footer_findings.append({"class": "FOOTER_ABSENT", "detail": "no `Counts checked` block"})
    else:
        if footer["total"] != total_files:
            footer_findings.append(
                {
                    "class": "FOOTER_TOTAL",
                    "declared": footer["total"],
                    "live": total_files,
                    "date": footer["date"],
                }
            )
        declared_dirs = footer["dir_totals"]
        live_dirs = [parts[p]["files"] for p in live_order]
        if declared_dirs != live_dirs:
            footer_findings.append(
                {
                    "class": "FOOTER_DIR_TOTALS",
                    "declared": declared_dirs,
                    "live": live_dirs,
                    "order": live_order,
                }
            )

    ok = (
        not (missing or ghosts or mismatches or drift or footer_findings)
        and totals_line == total_files
    )
    return {
        "readme_sha256": hashlib.sha256(readme_text.encode("utf-8")).hexdigest(),
        "parts": parts,
        "total_rows": total_rows,
        "total_files": total_files,
        "missing_from_index": missing,
        "orphan_rows": ghosts,
        "topic_mismatch": mismatches,
        "header_drift": drift,
        "totals_line": totals_line,
        "totals_ok": totals_line == total_files,
        "footer": footer,
        "footer_live": {"total": total_files, "dir_totals": [parts[p]["files"] for p in live_order],
                        "order": live_order},
        "footer_findings": footer_findings,
        "footer_ok": not footer_findings,
        "ok": ok,
    }


def render(inv):
    lines = [
        "parts "
        + json.dumps(
            {k: v["files"] for k, v in sorted(inv["parts"].items())},
            separators=(", ", ": "),
        ),
        f"rows {inv['total_rows']} files {inv['total_files']}",
        f"missing_from_index {len(inv['missing_from_index'])} {inv['missing_from_index']}",
        f"topic_mismatch {len(inv['topic_mismatch'])} "
        f"{[m['row'] for m in inv['topic_mismatch']]}",
        f"orphan_rows {len(inv['orphan_rows'])} {inv['orphan_rows']}",
        f"header_drift {inv['header_drift']}",
        f"totals_line {inv['totals_line']} totals_ok {inv['totals_ok']}",
        f"footer {json.dumps(inv['footer'])}",
        f"footer_live {json.dumps(inv['footer_live'])}",
        f"footer_findings {json.dumps(inv['footer_findings'])} footer_ok {inv['footer_ok']}",
        f"readme_sha256 {inv['readme_sha256']}",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------- selftest

def selftest():
    import shutil
    import tempfile

    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        if not cond:
            ok = False
        print(("PASS " if cond else "FAIL ") + name + (" " + detail if detail else ""))

    def make_tree(spec):
        """spec: {part: {name: topic_text}}"""
        d = tempfile.mkdtemp()
        for part, files in spec.items():
            os.makedirs(os.path.join(d, part), exist_ok=True)
            for name, topic in files.items():
                with open(os.path.join(d, part, name), "w", encoding="utf-8") as fh:
                    fh.write(f"# x\n\n- topic: {topic}\n- sources:\n  - A (2001)\n")
        return d

    def make_readme(parts, totals=None, footer=None):
        chunks = []
        for part, (declared, rows) in parts.items():
            chunks.append(f"## {part}/ ({declared})\n\n")
            for f, t in rows:
                chunks.append(f"- `{f}` — {t}\n")
            chunks.append("\n")
        if totals is not None:
            chunks.append(f"\nTotal knowledge entries: {totals}.\n")
        if footer is not None:
            date, cmd, total, dirs = footer
            chunks.append(
                f"\nCounts checked {date} from the repo root:\n"
                f"`{cmd}`\n"
                f"(total {total} files; directory totals {dirs}).\n"
                f"The inventory counts markers, not verified facts.\n"
            )
        return "".join(chunks)

    INVENTORY = "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge"

    try:
        # 1. live leg: the real README against the real tree
        with open(README, encoding="utf-8") as fh:
            inv = sweep(fh.read())
        check(
            "live: rows == files / 0 missing / 0 topic mismatches / 0 ghosts / 0 drift / footer ok",
            inv["total_rows"] == inv["total_files"] and inv["ok"],
            json.dumps(
                {
                    "rows": inv["total_rows"],
                    "files": inv["total_files"],
                    "missing": inv["missing_from_index"],
                    "mismatch": len(inv["topic_mismatch"]),
                    "ghosts": inv["orphan_rows"],
                    "drift": inv["header_drift"],
                    "footer": inv["footer_findings"],
                }
            ),
        )

        # 2. control: a paraphrased row is flagged (inherited leg still fires)
        tree = make_tree({"linguistics": {"a.md": "the real topic text"}})
        rm = make_readme(
            {"linguistics": (1, [("a.md", "a condensed paraphrase")])}, totals=1
        )
        r = sweep(rm, root_override=tree)
        check(
            "control: planted paraphrase flagged (1 mismatch)",
            len(r["topic_mismatch"]) == 1 and r["topic_mismatch"][0]["class"] == "REWRITE",
            json.dumps(r["topic_mismatch"]),
        )

        # 3. control: ghost row flagged
        rm = make_readme(
            {"linguistics": (1, [("a.md", "the real topic text"), ("zz.md", "x")])},
            totals=1,
        )
        r = sweep(rm, root_override=tree)
        check("control: planted ghost row flagged", r["orphan_rows"] == ["linguistics/zz.md"])

        # 4. control: deleted row surfaces a missing file
        rm = make_readme({"linguistics": (1, [])}, totals=1)
        r = sweep(rm, root_override=tree)
        check("control: deleted row surfaces a missing file", r["missing_from_index"] == ["linguistics/a.md"])

        # 5. control: wrong header count flagged
        rm = make_readme({"linguistics": (7, [("a.md", "the real topic text")])}, totals=1)
        r = sweep(rm, root_override=tree)
        check("control: wrong header count flagged", r["header_drift"] == {"linguistics": {"declared": 7, "files": 1}})

        # 6. control: wrong totals line flagged
        rm = make_readme({"linguistics": (1, [("a.md", "the real topic text")])}, totals=9)
        r = sweep(rm, root_override=tree)
        check("control: wrong totals line flagged", r["totals_ok"] is False and r["ok"] is False)

        # 7. control: duplicate rows reported
        rm = make_readme(
            {"linguistics": (1, [("a.md", "the real topic text"), ("a.md", "the real topic text")])},
            totals=1,
        )
        r = sweep(rm, root_override=tree)
        check("control: duplicate row reported", r["parts"]["linguistics"]["duplicate_rows"] == ["a.md"])

        # 8. control (NEW, the round-28 leg): a stale footer TOTAL is flagged
        rm = make_readme(
            {"linguistics": (1, [("a.md", "the real topic text")])},
            totals=1,
            footer=("2026-10-18", INVENTORY, 199, "19/19/18/29/20/94"),
        )
        r = sweep(rm, root_override=tree)
        classes = [f["class"] for f in r["footer_findings"]]
        check(
            "control: stale footer total flagged",
            "FOOTER_TOTAL" in classes and r["ok"] is False,
            json.dumps(r["footer_findings"]),
        )

        # 9. control (NEW): a stale footer DIRECTORY vector is flagged even when the total matches
        rm = make_readme(
            {"linguistics": (1, [("a.md", "the real topic text")])},
            totals=1,
            footer=("2026-10-18", INVENTORY, 1, "19/19/18/29/20/94"),
        )
        r = sweep(rm, root_override=tree)
        classes = [f["class"] for f in r["footer_findings"]]
        check(
            "control: stale footer dir vector flagged with matching total",
            "FOOTER_DIR_TOTALS" in classes and "FOOTER_TOTAL" not in classes,
            json.dumps(r["footer_findings"]),
        )

        # 10. control (NEW): an ABSENT footer is flagged, not silently passed
        rm = make_readme({"linguistics": (1, [("a.md", "the real topic text")])}, totals=1)
        r = sweep(rm, root_override=tree)
        check(
            "control: absent footer flagged",
            [f["class"] for f in r["footer_findings"]] == ["FOOTER_ABSENT"],
            json.dumps(r["footer_findings"]),
        )

        # 11. control (NEW): a CORRECT footer passes (the leg is not always-red).
        # The declared vector is compared over the sections the README actually
        # carries, so a one-section fixture declares one directory total.
        rm = make_readme(
            {"linguistics": (1, [("a.md", "the real topic text")])},
            totals=1,
            footer=("2026-10-18", INVENTORY, 1, "1"),
        )
        r = sweep(rm, root_override=tree)
        check("control: correct footer passes", r["footer_ok"] is True and r["ok"] is True,
              json.dumps(r["footer_findings"]))

        # 12. control: continuation lines are space-joined, not newline-joined
        tree2 = tempfile.mkdtemp()
        os.makedirs(os.path.join(tree2, "linguistics"))
        with open(os.path.join(tree2, "linguistics", "b.md"), "w", encoding="utf-8") as fh:
            fh.write("# x\n\n- topic: alpha beta\n  gamma delta\n- sources:\n  - A (2001)\n")
        rm = make_readme({"linguistics": (1, [("b.md", "alpha beta gamma delta")])}, totals=1)
        r = sweep(rm, root_override=tree2)
        check("control: continuation lines space-joined", r["topic_mismatch"] == [])
        shutil.rmtree(tree2, ignore_errors=True)

        shutil.rmtree(tree, ignore_errors=True)
    except Exception as exc:  # a broken instrument must fail loudly
        print("FAIL selftest raised: " + repr(exc))
        ok = False
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--readme", default=README)
    args = ap.parse_args(argv)
    if args.selftest:
        passed = selftest()
        print("selftest: %s" % ("12/12 checks passed" if passed else "FAILED"))
        return 0 if passed else 1
    with open(args.readme, encoding="utf-8") as fh:
        inv = sweep(fh.read())
    if args.json:
        print(json.dumps(inv, indent=1, sort_keys=True))
    else:
        print(render(inv))
    return 0 if inv["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
