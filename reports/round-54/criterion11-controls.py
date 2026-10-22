#!/usr/bin/env python3
"""Round-54 QUALITY criterion 11 controls for claim C, built before dispatch.

  python3 -B reports/round-54/criterion11-controls.py <lane-repo> <tree-ish> > reports/round-54/telemetry/criterion11-controls.txt

Read-only on the lane: `git archive <tree-ish>` is extracted into a mktemp directory, and every
control copy is built there. Each copy runs the declared argv verbatim from its own root:
  python3 -B reports/round-54/accept-c.py
GREEN  every mechanical clause holds through a stand-in landing that is never landed: a stand-in
       entry at the ENTRY path citing S239-S258, twenty stand-in SOURCES rows (mined, used-by the
       entry) and a README index row with the section header, totals line and footer moved by one.
       Expected exit 0.
One RED per mechanical clause, each the GREEN copy with that clause alone changed by its nearest
near-miss; expected exit 1 with that clause's leg FAIL and every other leg PASS:
  SET     a second new file (with its own README row) added and a base file (with its README
          row) removed, so the count stays 230
  SWEEP   the entry's README row names `masks-masquerades.md` (one letter off)
  FLOOR   the entry cites 19 S-ids (S258 dropped)
  RANGE   the entry cites S238 instead of S258 (still 20 cited)
  STATUS  row S258 is `queued`
  USEDBY  row S258's used-by names a neighbouring entry instead
  ACCESS  row S258's anchor records reaching the page through a headless browser
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

ENTRY = "corpus/knowledge/culture-material/masks-masquerade.md"
TOPIC = ("masks and masquerade as worn object, embodied presence and licensed voice: ritual, funerary, "
         "theatrical and festival masking, masquerade societies and their access rules, as a "
         "worldbuilding method")
ARGV = [sys.executable, "-B", "reports/round-54/accept-c.py"]
SIDS = [f"S{n}" for n in range(239, 259)]
INSTRUMENTS = ["reports/round-54/accept-c.py", "reports/round-54/base-knowledge-files.txt",
               "reports/round-28/readme/sweep.py", "tools/check-source-access.py",
               "reports/round-54/criterion11-controls.py"]


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
        f"# Masks and masquerade (stand-in)\n\n- topic: {TOPIC}\n- couples: stand-in\n\n{body}")
    edit(os.path.join(root, "corpus/SOURCES.md"),
         lambda t: re.sub(r"(^\| S238 .*\n)", lambda m: m.group(1) + "".join(row(s) for s in SIDS), t, count=1, flags=re.M))

    def readme(t):
        t = t.replace("## culture-material/ (28)", "## culture-material/ (29)", 1)
        t = re.sub(r"(^- `material-culture-inference-method\.md` — .*\n)",
                   lambda m: f"- `masks-masquerade.md` — {TOPIC}\n" + m.group(1), t, count=1, flags=re.M)
        t = t.replace("Total knowledge entries: 229.", "Total knowledge entries: 230.", 1)
        return t.replace("(total 229 files; directory totals 28/26/28/29/24/94).",
                         "(total 230 files; directory totals 28/26/29/29/24/94).", 1)
    edit(os.path.join(root, "corpus/README.md"), readme)


def red_set(root):
    extra = "corpus/knowledge/culture-material/masks-masquerade-notes.md"
    open(os.path.join(root, extra), "w", encoding="utf-8").write("# notes\n\n- topic: stand-in notes\n- couples: stand-in\n")
    os.remove(os.path.join(root, "corpus/knowledge/culture-material/ritual-garments.md"))

    def readme(t):
        t = re.sub(r"^- `ritual-garments\.md` — .*\n", "", t, count=1, flags=re.M)
        return re.sub(r"(^- `masks-masquerade\.md` — .*\n)",
                      lambda m: m.group(1) + "- `masks-masquerade-notes.md` — stand-in notes\n", t, count=1, flags=re.M)
    edit(os.path.join(root, "corpus/README.md"), readme)


def red_sweep(root):
    edit(os.path.join(root, "corpus/README.md"),
         lambda t: t.replace("- `masks-masquerade.md` — ", "- `masks-masquerades.md` — ", 1))


def red_floor(root):
    edit(os.path.join(root, ENTRY), lambda t: t.replace("- stand-in sentence (S258).\n", "", 1))


def red_range(root):
    edit(os.path.join(root, ENTRY), lambda t: t.replace("(S258)", "(S238)", 1))


def red_status(root):
    edit(os.path.join(root, "corpus/SOURCES.md"), lambda t: t.replace(row("S258"), row("S258", status="queued"), 1))


def red_usedby(root):
    edit(os.path.join(root, "corpus/SOURCES.md"), lambda t: t.replace(
        row("S258"), row("S258", used_by="corpus/knowledge/culture-material/ritual-garments.md"), 1))


def red_access(root):
    edit(os.path.join(root, "corpus/SOURCES.md"), lambda t: t.replace(
        row("S258"), row("S258", anchor="page reached through a headless browser"), 1))


CONTROLS = [("GREEN", None, 0), ("RED-SET", red_set, 1), ("RED-SWEEP", red_sweep, 1),
            ("RED-FLOOR", red_floor, 1), ("RED-RANGE", red_range, 1), ("RED-STATUS", red_status, 1),
            ("RED-USEDBY", red_usedby, 1), ("RED-ACCESS", red_access, 1)]


def main():
    lane, tree = sys.argv[1], sys.argv[2]
    rev = subprocess.run(["git", "-C", lane, "rev-parse", tree], capture_output=True, text=True, check=True).stdout.strip()
    tmp = tempfile.mkdtemp(prefix="kotodama-r54-c11-")
    try:
        base = os.path.join(tmp, "base")
        os.mkdir(base)
        archive = subprocess.run(["git", "-C", lane, "archive", rev], capture_output=True, check=True).stdout
        subprocess.run(["tar", "-x", "-C", base], input=archive, check=True)
        print(f"tree {rev}")
        for p in INSTRUMENTS:
            print(f"sha256 {hashlib.sha256(open(os.path.join(base, p), 'rb').read()).hexdigest()}  {p}")
        print("argv (run from each copy's root): python3 -B reports/round-54/accept-c.py")
        failures = 0
        for name, fn, want in CONTROLS:
            copy = os.path.join(tmp, name)
            shutil.copytree(base, copy)
            green(copy)
            if fn:
                fn(copy)
            r = subprocess.run(ARGV, cwd=copy, capture_output=True, text=True)
            legs = re.findall(r"^(\w+) (PASS|FAIL)", r.stdout, re.M)
            failing = [l for l, v in legs if v == "FAIL"]
            expect_leg = name.split("-", 1)[1] if fn else None
            ok = r.returncode == want and failing == ([expect_leg] if expect_leg else []) and len(legs) == 7
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
