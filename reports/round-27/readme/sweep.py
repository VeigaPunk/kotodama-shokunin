#!/usr/bin/env python3
"""R27-C47 — corpus/README.md index sweep (read-only).

Reconciles the README's index rows against the entries they name:

  rows         every `- \\`<name>.md\\` — <topic>` row under a `## <part>/ (N)`
               section header
  files        every `.md` directly under `corpus/knowledge/<part>/`
  topic        each row's `<topic>` must be byte-equal to the entry's own
               `- topic:` head-block text with continuation lines space-joined
  ghosts       rows naming no file
  missing      files with no row
  drift        `## <part>/ (N)` N vs the live file count
  totals       the `Total knowledge entries: N.` line vs the file total

The tool is read-only: it opens `corpus/README.md` and `corpus/knowledge/**`
for reading and has no code path that writes inside the repo.

Conventions are inherited by measurement from rounds 10/19/20
(`reports/round-20/readme/reconcile.md` §2, `reports/round-19/audit/
x27-coverage-readme-vs-files.md` §1). This is a fresh instrument for round 27;
round 20's sweep lived in `.scratch/` and was never committed.

Usage:
    python3 reports/round-27/readme/sweep.py            # text summary, exit 0/1
    python3 reports/round-27/readme/sweep.py --json     # receipt on stdout
    python3 reports/round-27/readme/sweep.py --selftest # in-memory controls
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


def disk_files(part):
    d = os.path.join(KNOWLEDGE, part)
    if not os.path.isdir(d):
        return []
    return sorted(
        f for f in os.listdir(d) if f.endswith(".md") and os.path.isfile(os.path.join(d, f))
    )


def sweep(readme_text, root_override=None):
    """The measurement. `root_override` swaps the knowledge tree (selftest)."""
    global KNOWLEDGE
    saved = KNOWLEDGE
    if root_override is not None:
        KNOWLEDGE = root_override
    try:
        sections = parse_readme(readme_text)
        parts = {}
        missing, ghosts, mismatches, drift = [], [], [], {}
        for part in sorted(sections):
            sec = sections[part]
            files = disk_files(part)
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
                real = topic_of(os.path.join(KNOWLEDGE, part, f))
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
        ok = not (missing or ghosts or mismatches or drift) and totals_line == total_files
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
            "ok": ok,
        }
    finally:
        KNOWLEDGE = saved


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

    def make_readme(parts, totals=None):
        chunks = []
        for part, (declared, rows) in parts.items():
            chunks.append(f"## {part}/ ({declared})\n\n")
            for f, t in rows:
                chunks.append(f"- `{f}` — {t}\n")
            chunks.append("\n")
        if totals is not None:
            chunks.append(f"\nTotal knowledge entries: {totals}.\n")
        return "".join(chunks)

    try:
        # 1. live leg: the real README against the real tree
        with open(README, encoding="utf-8") as fh:
            inv = sweep(fh.read())
        check(
            "live: rows == files / 0 missing / 0 topic mismatches / 0 ghosts / 0 drift",
            inv["total_rows"] == inv["total_files"] and inv["ok"],
            json.dumps(
                {
                    "rows": inv["total_rows"],
                    "files": inv["total_files"],
                    "missing": inv["missing_from_index"],
                    "mismatch": len(inv["topic_mismatch"]),
                    "ghosts": inv["orphan_rows"],
                    "drift": inv["header_drift"],
                }
            ),
        )

        # 2. control: a paraphrased row is flagged
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

        # 3. control: a truncated rewrite (the round-19 defect class) is flagged
        rm = make_readme(
            {"linguistics": (1, [("a.md", "the real topic")])}, totals=1
        )
        r = sweep(rm, root_override=tree)
        check("control: truncated rewrite flagged (1 mismatch)", len(r["topic_mismatch"]) == 1)

        # 4. control: a ghost row is flagged
        rm = make_readme(
            {"linguistics": (1, [("a.md", "the real topic text"), ("zz.md", "x")])},
            totals=1,
        )
        r = sweep(rm, root_override=tree)
        check(
            "control: planted ghost row flagged",
            r["orphan_rows"] == ["linguistics/zz.md"],
            json.dumps(r["orphan_rows"]),
        )

        # 5. control: a deleted row surfaces a missing file
        rm = make_readme({"linguistics": (1, [])}, totals=1)
        r = sweep(rm, root_override=tree)
        check(
            "control: deleted row surfaces a missing file",
            r["missing_from_index"] == ["linguistics/a.md"],
            json.dumps(r["missing_from_index"]),
        )

        # 6. control: a wrong header count is flagged
        rm = make_readme({"linguistics": (7, [("a.md", "the real topic text")])}, totals=1)
        r = sweep(rm, root_override=tree)
        check(
            "control: wrong header count flagged",
            r["header_drift"] == {"linguistics": {"declared": 7, "files": 1}},
            json.dumps(r["header_drift"]),
        )

        # 7. control: a wrong totals line is flagged
        rm = make_readme({"linguistics": (1, [("a.md", "the real topic text")])}, totals=9)
        r = sweep(rm, root_override=tree)
        check("control: wrong totals line flagged", r["totals_ok"] is False and r["ok"] is False)

        # 8. control: continuation lines are space-joined, not newline-joined
        tree2 = tempfile.mkdtemp()
        os.makedirs(os.path.join(tree2, "linguistics"))
        with open(os.path.join(tree2, "linguistics", "b.md"), "w", encoding="utf-8") as fh:
            fh.write("# x\n\n- topic: alpha beta\n  gamma delta\n- sources:\n  - A (2001)\n")
        rm = make_readme({"linguistics": (1, [("b.md", "alpha beta gamma delta")])}, totals=1)
        r = sweep(rm, root_override=tree2)
        check("control: continuation lines space-joined", r["topic_mismatch"] == [], json.dumps(r["topic_mismatch"]))
        shutil.rmtree(tree2, ignore_errors=True)

        # 9. control: duplicate rows are reported
        rm = make_readme(
            {"linguistics": (1, [("a.md", "the real topic text"), ("a.md", "the real topic text")])},
            totals=1,
        )
        r = sweep(rm, root_override=tree)
        check(
            "control: duplicate row reported",
            r["parts"]["linguistics"]["duplicate_rows"] == ["a.md"],
            json.dumps(r["parts"]["linguistics"]["duplicate_rows"]),
        )
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
        print("selftest: %s" % ("9/9 checks passed" if passed else "FAILED"))
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
