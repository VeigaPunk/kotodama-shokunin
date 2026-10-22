#!/usr/bin/env python3
"""Round-56 QUALITY criterion 11 controls for claim C (adapted from round 55), built before dispatch.

  python3 -B reports/round-56/criterion11-controls.py <lane-repo> <tree-ish> > reports/round-56/telemetry/criterion11-controls.txt

Read-only on the lane: `git archive <tree-ish>` is extracted into a mktemp directory, and every
control copy is built there. Each copy runs the declared argv verbatim from its own root:
  python3 -B reports/round-56/accept-c.py
GREEN  every mechanical clause holds through a stand-in landing that is never landed: a stand-in
       entry at the ENTRY path citing S359-S378, twenty stand-in SOURCES rows (mined, used-by the
       entry) and a README index row with the section header, totals line and footer moved by one.
       Expected exit 0.
One RED per mechanical clause, each the GREEN copy with that clause alone changed by its nearest
near-miss; expected exit 1 with that clause's leg FAIL and every other leg PASS (RED-COUNT is the
one two-leg control: the count 232 is pinned by both SET and SWEEP, so a count-only miss fails both):
  COUNT     a second new .md file with its own README row, and the section header, totals line and
            footer all moved to 233 so the sweep itself exits 0 (count 233): SET and SWEEP fail,
            SWEEP through the 232 pin alone
  SET       a second new file (with its own README row) added and a base file (with its README
            row) removed, so the count stays 232
  SET-EXT   a second new file that is not *.md (`kongo-kingdom.notes.txt`) beside the entry
  SWEEP     the entry's README row names `kongo-kingdo.md` (one letter off)
  SWEEP-EXIT the counts footer left at 231 files / civilizations 94 (rows 232 files 232, missing 0,
            the sweep exits 1)
  FLOOR     the entry's S378 citation becomes S377: 20 citations, 19 distinct ids
  RANGE     the entry cites S358 (one below the block; queued at base, which STATUS never reads for a
            RANGE-bad row) in place of S378 (20 distinct) and S358's used-by names the entry
  RANGE-HIGH the entry cites S419 (one above the reserved block S359-S418) in place of S378, and a
            stand-in S419 row (mined, used-by the entry) is added after S378
  RANGE-NOROW the entry cites S379, which has no row, in place of S378
  RANGE-DUP a second, queued S378 row placed before the mined one
  RANGE-SPAN the entry's (S378) citation written as the range (S377–S378)
  RANGE-DUP2 a second, queued S378 row written `|S378 |` (no space) placed before the mined one
  RANGE-THROUGH the entry's (S378) citation written as (S377 through S378)
  USEDBY-SUBSTR row S378's used-by names `<entry>.bak`
  STATUS    row S378 is `queued`
  USEDBY  row S378's used-by names a neighbouring entry instead
  ACCESS  row S378's anchor records reaching the page through a headless browser
The script prints sha256 of each instrument it ran. Lines carry no `$ ` prefix, so criterion 9's
two-way dry-run check does not read this receipt.
"""
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

ENTRY = "corpus/knowledge/civilizations/kongo-kingdom.md"
TOPIC = "Kingdom of Kongo linguistic-cultural reference base: Kikongo noun classes and the first Bantu grammars, kingship and the mani titles, Kongo Christianity and the Antonian movement, minkisi and contested cosmogram readings, raffia cloth, nzimbu money and regalia, and era staging from the founding traditions to the colonial partition; method and reference only, not fictional canon"
ARGV = ["python3", "-B", "reports/round-56/accept-c.py"]
SIDS = [f"S{n}" for n in range(359, 379)]
INSTRUMENTS = ["reports/round-56/accept-c.py", "reports/round-56/base-knowledge-files.txt",
               "reports/round-28/readme/sweep.py", "tools/check-source-access.py",
               "reports/round-56/criterion11-controls.py"]


def edit(path, fn):
    text = open(path, encoding="utf-8").read()
    new = fn(text)
    assert new != text, path
    open(path, "w", encoding="utf-8").write(new)


def row(sid, used_by=ENTRY, status="mined", anchor="stand-in anchor"):
    return (f"| {sid} | stand-in source {sid} — https://example.invalid/{sid} | paper | A | stand-in scope "
            f"| {anchor} | stand-in teaches | {status} | 2026-10-22 | 2027-10-22 | {used_by} |\n")


def green(root):
    os.makedirs(os.path.dirname(os.path.join(root, ENTRY)), exist_ok=True)
    body = "".join(f"- stand-in sentence ({s}).\n" for s in SIDS)
    open(os.path.join(root, ENTRY), "w", encoding="utf-8").write(
        f"# Kingdom of Kongo (stand-in)\n\n- topic: {TOPIC}\n- couples: stand-in\n\n{body}")
    edit(os.path.join(root, "corpus/SOURCES.md"),
         lambda t: re.sub(r"(^\| S358 .*\n)", lambda m: m.group(1) + "".join(row(s) for s in SIDS), t, count=1, flags=re.M))

    def readme(t):
        t = t.replace("## civilizations/ (94)", "## civilizations/ (95)", 1)
        t = re.sub(r"(^- `korea-joseon\.md` — .*\n)",
                   lambda m: f"- `kongo-kingdom.md` — {TOPIC}\n" + m.group(1), t, count=1, flags=re.M)
        t = t.replace("Total knowledge entries: 231.", "Total knowledge entries: 232.", 1)
        return t.replace("(total 231 files; directory totals 28/27/29/29/24/94).",
                         "(total 232 files; directory totals 28/27/29/29/24/95).", 1)
    edit(os.path.join(root, "corpus/README.md"), readme)


def red_set(root):
    extra = "corpus/knowledge/civilizations/kongo-kingdom-notes.md"
    open(os.path.join(root, extra), "w", encoding="utf-8").write("# notes\n\n- topic: stand-in notes\n- couples: stand-in\n")
    os.remove(os.path.join(root, "corpus/knowledge/civilizations/khmer-angkor.md"))

    def readme(t):
        t = re.sub(r"^- `khmer-angkor\.md` — .*\n", "", t, count=1, flags=re.M)
        return re.sub(r"(^- `kongo-kingdom\.md` — .*\n)",
                      lambda m: m.group(1) + "- `kongo-kingdom-notes.md` — stand-in notes\n", t, count=1, flags=re.M)
    edit(os.path.join(root, "corpus/README.md"), readme)


def red_count(root):
    extra = "corpus/knowledge/civilizations/kongo-kingdom-notes.md"
    open(os.path.join(root, extra), "w", encoding="utf-8").write("# notes\n\n- topic: stand-in notes\n- couples: stand-in\n")
    def readme(t):
        t = re.sub(r"(^- `kongo-kingdom\.md` — .*\n)",
                   lambda m: m.group(1) + "- `kongo-kingdom-notes.md` — stand-in notes\n", t, count=1, flags=re.M)
        t = t.replace("## civilizations/ (95)", "## civilizations/ (96)", 1)
        t = t.replace("Total knowledge entries: 232.", "Total knowledge entries: 233.", 1)
        return t.replace("(total 232 files; directory totals 28/27/29/29/24/95).",
                         "(total 233 files; directory totals 28/27/29/29/24/96).", 1)
    edit(os.path.join(root, "corpus/README.md"), readme)


def red_set_ext(root):
    open(os.path.join(root, "corpus/knowledge/civilizations/kongo-kingdom.notes.txt"), "w",
         encoding="utf-8").write("stand-in notes\n")


def red_sweep(root):
    edit(os.path.join(root, "corpus/README.md"),
         lambda t: t.replace("- `kongo-kingdom.md` — ", "- `kongo-kingdo.md` — ", 1))


def red_sweep_exit(root):
    edit(os.path.join(root, "corpus/README.md"), lambda t: t.replace(
        "(total 232 files; directory totals 28/27/29/29/24/95).",
        "(total 231 files; directory totals 28/27/29/29/24/94).", 1))


def red_floor(root):
    edit(os.path.join(root, ENTRY), lambda t: t.replace("(S378)", "(S377)", 1))


def red_range(root):
    edit(os.path.join(root, ENTRY), lambda t: t.replace("(S378)", "(S358)", 1))

    def s284(t):
        line = re.search(r"^\| S358 .*$", t, re.M).group(0)
        cells = line.split("|")
        cells[11] = cells[11].rstrip() + "; " + ENTRY + " "
        return t.replace(line, "|".join(cells), 1)
    edit(os.path.join(root, "corpus/SOURCES.md"), s284)


def red_range_high(root):
    edit(os.path.join(root, ENTRY), lambda t: t.replace("(S378)", "(S419)", 1))
    edit(os.path.join(root, "corpus/SOURCES.md"), lambda t: t.replace(row("S378"), row("S378") + row("S419"), 1))


def red_range_norow(root):
    edit(os.path.join(root, ENTRY), lambda t: t.replace("(S378)", "(S379)", 1))


def red_range_dup2(root):
    edit(os.path.join(root, "corpus/SOURCES.md"), lambda t: t.replace(row("S378"), row("S378", status="queued", used_by="—").replace("| S378 |", "|S378 |", 1) + row("S378"), 1))


def red_range_through(root):
    edit(os.path.join(root, ENTRY), lambda t: t.replace("(S378)", "(S377 through S378)", 1))


def red_usedby_substr(root):
    edit(os.path.join(root, "corpus/SOURCES.md"), lambda t: t.replace(
        row("S378"), row("S378", used_by=ENTRY + ".bak"), 1))


def red_range_span(root):
    edit(os.path.join(root, ENTRY), lambda t: t.replace("(S378)", "(S377–S378)", 1))


def red_range_dup(root):
    edit(os.path.join(root, "corpus/SOURCES.md"), lambda t: t.replace(row("S378"), row("S378", status="queued", used_by="—") + row("S378"), 1))


def red_status(root):
    edit(os.path.join(root, "corpus/SOURCES.md"), lambda t: t.replace(row("S378"), row("S378", status="queued"), 1))


def red_usedby(root):
    edit(os.path.join(root, "corpus/SOURCES.md"), lambda t: t.replace(
        row("S378"), row("S378", used_by="corpus/knowledge/civilizations/khmer-angkor.md"), 1))


def red_access(root):
    edit(os.path.join(root, "corpus/SOURCES.md"), lambda t: t.replace(
        row("S378"), row("S378", anchor="page reached through a headless browser"), 1))


CONTROLS = [("GREEN", None, 0, []), ("RED-COUNT", red_count, 1, ["SET", "SWEEP"]),
            ("RED-SET", red_set, 1, ["SET"]), ("RED-SET-EXT", red_set_ext, 1, ["SET"]),
            ("RED-SWEEP", red_sweep, 1, ["SWEEP"]), ("RED-SWEEP-EXIT", red_sweep_exit, 1, ["SWEEP"]),
            ("RED-FLOOR", red_floor, 1, ["FLOOR"]),
            ("RED-RANGE", red_range, 1, ["RANGE"]), ("RED-RANGE-HIGH", red_range_high, 1, ["RANGE"]),
            ("RED-RANGE-NOROW", red_range_norow, 1, ["RANGE"]),
            ("RED-RANGE-DUP", red_range_dup, 1, ["RANGE"]),
            ("RED-RANGE-DUP2", red_range_dup2, 1, ["RANGE"]), ("RED-RANGE-THROUGH", red_range_through, 1, ["RANGE"]),
            ("RED-USEDBY-SUBSTR", red_usedby_substr, 1, ["USEDBY"]), ("RED-RANGE-SPAN", red_range_span, 1, ["RANGE"]), ("RED-STATUS", red_status, 1, ["STATUS"]),
            ("RED-USEDBY", red_usedby, 1, ["USEDBY"]), ("RED-ACCESS", red_access, 1, ["ACCESS"])]


def main():
    lane, tree = sys.argv[1], sys.argv[2]
    rev = subprocess.run(["git", "-C", lane, "rev-parse", tree], capture_output=True, text=True, check=True).stdout.strip()
    tmp = tempfile.mkdtemp(prefix="kotodama-r56-c11-")
    try:
        base = os.path.join(tmp, "base")
        os.mkdir(base)
        archive = subprocess.run(["git", "-C", lane, "archive", rev], capture_output=True, check=True).stdout
        subprocess.run(["tar", "-x", "-C", base], input=archive, check=True)
        print(f"measured-revision {rev} (git archive into a mktemp directory)")
        for p in INSTRUMENTS:
            print(f"sha256 {hashlib.sha256(open(os.path.join(base, p), 'rb').read()).hexdigest()}  {p}")
        print("argv (run from each copy's root): python3 -B reports/round-56/accept-c.py")
        failures = 0
        for name, fn, want, expect in CONTROLS:
            copy = os.path.join(tmp, name)
            shutil.copytree(base, copy)
            green(copy)
            if fn:
                fn(copy)
            r = subprocess.run(ARGV, cwd=copy, capture_output=True, text=True)
            legs = re.findall(r"^(\w+) (PASS|FAIL)", r.stdout, re.M)
            failing = [l for l, v in legs if v == "FAIL"]
            ok = r.returncode == want and failing == expect and len(legs) == 7
            failures += not ok
            print(f"\n## {name}: exit {r.returncode} (expected {want}); failing legs {failing}; "
                  f"{'AS EXPECTED' if ok else 'NOT AS EXPECTED'}")
            print((r.stdout + r.stderr).rstrip())
        print(f"\nCONTROLS {len(CONTROLS) - failures}/{len(CONTROLS)} as expected")
        return 1 if failures else 0
    finally:
        shutil.rmtree(tmp)


if __name__ == "__main__":
    sys.exit(main())
