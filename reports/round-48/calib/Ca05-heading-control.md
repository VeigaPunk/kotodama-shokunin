# Ca05 — heading-count control for `corpus/README.md` (claim Ca)

- Seat: `Ca05` | role: executor | claim: **Ca** (calibration) | round 48, loop 2, position 2
- Baseline: HEAD `a01405d` — `git rev-parse HEAD` → `a01405dd36367292255c2652ac0a601f4cd6a0af`, equal to `reports/round-48/claims.json:7`
- Seat contract: `reports/round-48/targets.json:37`
- Out path: `reports/round-48/calib/Ca05-heading-control.md` (this file)
- Mission: draft the durable control that counts `^# ` headings in `corpus/README.md` and asserts exactly 1 — as a tools/ diff or documented gate the integrator adds.

**One-line result.** The round-28 sweep cannot see the live defect: it exits 0 on the README that carries two H1s at `corpus/README.md:1` and `:3`. I drafted a sibling control, `tools/check-readme-heading.py` (244 lines, stdlib only, read-only), measured it 8/8 on its own selftest, red (`exit 1`, `H1-COUNT lines=[1,3]`) on the live README, and green (`exit 0`, `h1_lines [1]`) on a staged copy with exactly lines 3–4 removed. The sweep stays green on that staged copy (`exit 0`). The tool is fenced in §3 for the integrator to create; no byte under `corpus/` or `reports/round-28/` was edited.

---

## 1. Measured baseline (not asserted)

Commands run from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-48/

$ grep -c '^# ' corpus/README.md
2
$ grep -n '^# ' corpus/README.md
1:# kotodama-shokunin corpus index
3:# kotodama-shokunin corpus index

$ wc -l corpus/README.md
575 corpus/README.md
$ sha256sum corpus/README.md
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd  corpus/README.md
```

The complete heading census at the baseline (`grep -n '^#' corpus/README.md`): two H1s at lines 1 and 3; seven H2s at lines 177, 205, 234, 261, 293, 320 and 417. Heading total before the fix: 9 (2 H1 + 7 H2).

### 1.1 The sweep is green on the defective file

```
$ python3 -B reports/round-28/readme/sweep.py | tail -4
totals_line 223 totals_ok True
footer {... "total": 223 ...} footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
$ echo $?
0
```

The receipt names the same sha256 as the defective file above. This is the gap in one line: the instrument's green verdict covers rows, sections, totals and footer — not headings.

### 1.2 Why the leg cannot be added to the sweep in place

- `reports/round-28/readme/sweep.py:18-27` enumerates the legs (`index`, `footer`, `block`); none reads headings.
- `reports/round-28/readme/sweep.py:191-194` computes `ok` from `missing`, `ghosts`, `mismatches`, `drift`, `footer_findings` and `totals_line` only — no heading term exists to flip.
- `reports/round-28/**` is filed-round bytes (shared rule: never edit `reports/round-1..47/**`). A new leg must therefore be a sibling instrument, or a successor copy made by the integrator — not an in-place edit.

The control below is the sibling. It deliberately does **not** re-check rows, topics, section counts, totals or the footer; the sweep owns those and stays the primary receipt. One defect class, one control.

---

## 2. What the control asserts

| Diagnostic id | Rule | Why it is in scope |
|---|---|---|
| `H1-ABSENT` | file has no level-1 heading | an index with no title is malformed |
| `H1-COUNT` | exactly one level-1 heading; report every line | the live defect (`:1` and `:3`) |
| `H1-NOT-FIRST` | the H1 is the first non-blank line | an H1 after a preamble still breaks the file's title contract |
| `HEADING-DUP` | no two headings of the same level share text (levels 2–6) | catches a duplicated `## section/ (N)` row heading; H1 duplicates are already reported by `H1-COUNT` and are not double-reported |

Scanning rules that keep it from false-positiving: ATX headings require a space after the `#` run (so `#nospace` is content, per CommonMark), and headings inside fenced code blocks (``` or `~~~`, up to three leading spaces) are ignored.

Exit codes follow the lane's existing tool convention (`tools/check-craft-exercise.py:7`): `0` clean, `1` finding, `2` could-not-evaluate (missing/unreadable input or usage error). Stdout is either a text receipt or `--json`; the receipt carries the input path and its sha256 so a later run can prove which bytes were judged.

---

## 3. Drafted tool — `tools/check-readme-heading.py`

Integrator action: create this file with exactly these bytes. The outer fence is four backticks because the selftest fixture contains a literal triple-backtick string (line 184 of the tool).

````python
#!/usr/bin/env python3
"""Heading-count control for corpus/README.md (round 48, claim Ca).

The round-28 index sweep (`reports/round-28/readme/sweep.py`) checks rows,
section counts, the totals line and the counts footer. It has no heading leg:
a duplicated H1 passes every existing check, which is why the live README
carried `# kotodama-shokunin corpus index` at both lines 1 and 3 while the
sweep stayed green.

The sweep is filed round-28 bytes and is not editable; this control is its
sibling. It reads one Markdown file, counts ATX headings outside fenced code
blocks, and asserts:

  * exactly one level-1 heading (`^# `); duplicates are reported with lines
  * that H1 is the first non-blank line of the file
  * no two headings of the same level share the same text

Stdlib only. Read-only: no network, no writes, no eval/exec.

Usage:
  python3 tools/check-readme-heading.py
  python3 tools/check-readme-heading.py --readme <path> [--json]
  python3 tools/check-readme-heading.py --selftest

Exit codes: 0 = clean, 1 = finding present, 2 = could-not-evaluate (missing or
unreadable input, usage error). Unexpected internal failures print a JSON
object with `ok: null` and exit 2; no traceback is printed.
"""
import argparse
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, ".."))
DEFAULT_README = os.path.join(LANE, "corpus", "README.md")

HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.*?)[ \t]*$")
FENCE_RE = re.compile(r"^[ ]{0,3}(`{3,}|~{3,})")

# Stable diagnostic ids.
H1_ABSENT = "H1-ABSENT"
H1_COUNT = "H1-COUNT"
H1_NOT_FIRST = "H1-NOT-FIRST"
HEADING_DUP = "HEADING-DUP"


def headings(text):
    """ATX headings outside fenced code blocks: [(line_no, level, text)]."""
    out = []
    fence = None
    for i, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip("\r")
        m = FENCE_RE.match(line)
        if m:
            marker = m.group(1)[0]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            continue
        if fence is not None:
            continue
        h = HEADING_RE.match(line)
        if h:
            out.append((i, len(h.group(1)), h.group(2).strip()))
    return out


def evaluate_text(text):
    """Measure one README string. Pure: no IO."""
    hs = headings(text)
    h1 = [(n, t) for n, lvl, t in hs if lvl == 1]
    findings = []

    if not h1:
        findings.append({"class": H1_ABSENT, "detail": "no level-1 heading", "lines": []})
    elif len(h1) > 1:
        findings.append(
            {
                "class": H1_COUNT,
                "detail": "expected exactly 1 level-1 heading, found %d" % len(h1),
                "lines": [n for n, _ in h1],
                "texts": [t for _, t in h1],
            }
        )

    lines = text.splitlines()
    first = next((i for i, ln in enumerate(lines, 1) if ln.strip()), None)
    if h1 and first != h1[0][0]:
        findings.append(
            {
                "class": H1_NOT_FIRST,
                "detail": "first non-blank line is %s, first H1 is line %d"
                % (first, h1[0][0]),
                "lines": [first, h1[0][0]] if first is not None else [h1[0][0]],
            }
        )

    by_level = {}
    for n, lvl, t in hs:
        by_level.setdefault(lvl, {}).setdefault(t, []).append(n)
    for lvl, texts in sorted(by_level.items()):
        if lvl == 1:
            continue  # H1-COUNT already reports the whole level
        for t, ns in texts.items():
            if len(ns) > 1:
                findings.append(
                    {
                        "class": HEADING_DUP,
                        "detail": "level-%d heading %r repeated" % (lvl, t),
                        "lines": ns,
                    }
                )

    return {
        "ok": not findings,
        "findings": findings,
        "h1": h1,
        "h1_lines": [n for n, _ in h1],
        "heading_count": len(hs),
        "headings_by_level": {
            str(lvl): sum(1 for _, l, _ in hs if l == lvl) for lvl in sorted(by_level)
        },
    }


def receipt(path, text, result):
    result = dict(result)
    result["readme"] = path
    result["sha256"] = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return result


def selftest():
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        if not cond:
            ok = False
        print(("PASS " if cond else "FAIL ") + name + (" " + detail if detail else ""))

    # 1. one H1 first -> clean
    r = evaluate_text("# title\n\nbody\n")
    check("control: single leading H1 passes", r["ok"] is True, json.dumps(r["findings"]))

    # 2. the live defect shape -> flagged with both lines
    r = evaluate_text("# title\n\n# title\n\nrevision: 2.4\n")
    f = [x for x in r["findings"] if x["class"] == H1_COUNT]
    check(
        "control: duplicate H1 flagged at [1, 3]",
        len(f) == 1 and f[0]["lines"] == [1, 3],
        json.dumps(r["findings"]),
    )

    # 3. no H1 -> flagged
    r = evaluate_text("## section\n\nbody\n")
    check(
        "control: absent H1 flagged",
        [x["class"] for x in r["findings"]] == [H1_ABSENT],
        json.dumps(r["findings"]),
    )

    # 4. H1 after content -> flagged
    r = evaluate_text("preamble\n\n# title\n")
    check(
        "control: H1 after content flagged",
        any(x["class"] == H1_NOT_FIRST for x in r["findings"]),
        json.dumps(r["findings"]),
    )

    # 5. '#nospace' is not an ATX heading
    r = evaluate_text("# title\n\n#nospace\n")
    check(
        "control: '#nospace' not counted",
        r["ok"] is True and r["heading_count"] == 1,
        json.dumps(r),
    )

    # 6. a heading inside a fenced block is not counted
    r = evaluate_text("# title\n\n```\n# not a heading\n```\n")
    check(
        "control: fenced '# ' ignored",
        r["ok"] is True and r["heading_count"] == 1,
        json.dumps(r),
    )

    # 7. duplicate H2 -> flagged
    r = evaluate_text("# title\n\n## a\n\n## a\n")
    check(
        "control: duplicate H2 flagged",
        any(x["class"] == HEADING_DUP for x in r["findings"]),
        json.dumps(r["findings"]),
    )

    # 8. level counts are reported
    r = evaluate_text("# title\n\n## a\n\n### b\n")
    check(
        "control: level counts reported",
        r["headings_by_level"] == {"1": 1, "2": 1, "3": 1},
        json.dumps(r["headings_by_level"]),
    )

    return ok


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--readme", default=DEFAULT_README)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        passed = selftest()
        print("selftest: %s" % ("8/8 checks passed" if passed else "FAILED"))
        return 0 if passed else 1

    try:
        with open(args.readme, encoding="utf-8") as fh:
            text = fh.read()
        result = receipt(args.readme, text, evaluate_text(text))
    except (OSError, UnicodeDecodeError) as exc:
        print(json.dumps({"ok": None, "error": repr(exc), "readme": args.readme}))
        return 2

    if args.json:
        print(json.dumps(result, indent=1, sort_keys=True))
    else:
        print("readme %s" % result["readme"])
        print("sha256 %s" % result["sha256"])
        print("h1_lines %s" % result["h1_lines"])
        print("headings %s" % json.dumps(result["headings_by_level"], sort_keys=True))
        print("findings %d" % len(result["findings"]))
        for f in result["findings"]:
            print("  %s lines=%s %s" % (f["class"], f["lines"], f["detail"]))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
````

Line count of the fenced body: 244. No third-party imports; `hashlib`, `json`, `os`, `re`, `sys`, `argparse` are stdlib.

---

## 4. Measured behavior of the drafted control

The tool was prototyped at `.scratch/ca05/check-readme-heading.py`; all runs below are from the lane root with `python3 -B`.

### 4.1 Selftest — 8/8, exit 0

```
$ python3 -B .scratch/ca05/check-readme-heading.py --selftest
PASS control: single leading H1 passes []
PASS control: duplicate H1 flagged at [1, 3] [...]
PASS control: absent H1 flagged [...]
PASS control: H1 after content flagged [...]
PASS control: '#nospace' not counted {...}
PASS control: fenced '# ' ignored {...}
PASS control: duplicate H2 flagged [...]
PASS control: level counts reported {"1": 1, "2": 1, "3": 1}
selftest: 8/8 checks passed
$ echo $?
0
```

The first run was 7/8: control 5 originally placed `#nospace` *before* the H1, so `H1-NOT-FIRST` fired correctly and the fixture — not the tool — was wrong. The fixture now places `#nospace` after the H1, where it tests only the ATX-space rule.

### 4.2 Live README — red, exit 1 (the defect is caught)

```
$ python3 -B .scratch/ca05/check-readme-heading.py --readme corpus/README.md
readme corpus/README.md
sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
h1_lines [1, 3]
headings {"1": 2, "2": 7}
findings 1
  H1-COUNT lines=[1, 3] expected exactly 1 level-1 heading, found 2
$ echo $?
1
```

### 4.3 Staged fixed copy — green, exit 0

The staged fix removes exactly lines 3–4 (the second H1 and one of the two blank lines that separated it from `revision: 2.4`), preserving one blank line after the remaining H1:

```
$ diff -u corpus/README.md .scratch/ca05/README.fixed.md
--- corpus/README.md
+++ .scratch/ca05/README.fixed.md
@@ -1,7 +1,5 @@
 # kotodama-shokunin corpus index
 
-# kotodama-shokunin corpus index
-
 revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
 myth-symbol entries landed (`mineral-stone-symbolism.md`,
 `purity-pollution-boundary-systems.md`, `sacred-topography-pilgrimage.md`),

$ sha256sum .scratch/ca05/README.fixed.md
d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079  ...
$ wc -l .scratch/ca05/README.fixed.md
573
$ python3 -B .scratch/ca05/check-readme-heading.py --readme .scratch/ca05/README.fixed.md
readme .scratch/ca05/README.fixed.md
sha256 d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079
h1_lines [1]
headings {"1": 1, "2": 7}
findings 0
$ echo $?
0
```

575 lines minus 2 = 573; H1 count 2 → 1; heading total 9 → 8; H2 count unchanged at 7. No other heading moved (the diff touches only the header block).

### 4.4 The sweep stays green on the staged fix

```
$ python3 -B reports/round-28/readme/sweep.py --readme .scratch/ca05/README.fixed.md | head -8
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
$ echo $?
0
```

This is the two-instrument receipt the claim needs: the sweep is green before and after (it never saw the defect), and the new control is red before / green after.

### 4.5 `tools/`-shaped mirror — default path resolution proven

The tool computes `LANE` from its own location (`HERE/..`). To prove that resolves correctly once installed at `tools/check-readme-heading.py`, I copied it into `.scratch/ca05/mirror/tools/` with a mirror `corpus/README.md`:

```
$ python3 -B .scratch/ca05/mirror/tools/check-readme-heading.py --selftest | tail -1
selftest: 8/8 checks passed          # exit 0
$ python3 -B .scratch/ca05/mirror/tools/check-readme-heading.py --json   # live bytes
... "readme": ".../.scratch/ca05/mirror/corpus/README.md", "ok": false, "sha256": "7c788a1d..."
                                     # exit 1
$ cp .scratch/ca05/README.fixed.md .scratch/ca05/mirror/corpus/README.md
$ python3 -B .scratch/ca05/mirror/tools/check-readme-heading.py
findings 0                           # exit 0
```

### 4.6 Could-not-evaluate — exit 2

```
$ python3 -B .scratch/ca05/check-readme-heading.py --readme .scratch/ca05/absent.md --json
{"ok": null, "error": "FileNotFoundError(2, 'No such file or directory')", "readme": ".scratch/ca05/absent.md"}
$ echo $?
2
```

---

## 5. Integrator apply order (exact)

1. Create `tools/check-readme-heading.py` from the §3 fence (244 lines). `chmod +x tools/check-readme-heading.py`.
2. Run `python3 tools/check-readme-heading.py --selftest` → expect `8/8 checks passed`, exit 0.
3. **Before** applying Ca01's fix, run `python3 tools/check-readme-heading.py` → expect exit 1 with `H1-COUNT lines=[1, 3]`. Capture this output in the round receipt: it is the red leg that proves the control detects the real defect rather than a fixture.
4. Apply Ca01's edit: delete `corpus/README.md:3-4` (the second identical H1 plus the blank line after it). Do not touch line 1.
5. Run `python3 tools/check-readme-heading.py` → expect exit 0, `h1_lines [1]`, `headings {"1": 1, "2": 7}`, and sha256 equal to the delivered file.
6. Run `python3 reports/round-28/readme/sweep.py` → expect exit 0, `223 rows / 223 files`, footer `223`, unchanged.
7. File both receipts (the step-3 red and step-5 green) in the round's Ca evidence chain. The step-5 sha256 is the delivery certificate for the heading leg; the sweep's own `readme_sha256` is the certificate for the row/footer legs.

Order matters: installing the control before the fix means the red state and the green state are measured by the same instrument on the same path, rather than the fix being asserted and the control run only afterwards.

---

## 6. Durability — where the control must be named

A tool that is never invoked is not a control. Three placements, in increasing durability:

1. **This round:** add a leg to `reports/round-48/run-validation.py` (absent at filing time — `ls reports/round-48/run-validation.py` → `No such file or directory`; the integrator authors it). The leg is exactly `python3 tools/check-readme-heading.py --json`, and its verdict rides the existing `run-validation.py` aggregation.
2. **Landing wire:** W02's apply spec should name step 5 above as a required post-edit check, beside the sweep.
3. **Future README revisions:** the README's own convention already requires the sweep after each revision (see the rev 2.1–2.4 blocks, e.g. `corpus/README.md:12`). C10's rev 2.5 note can add one clause that the heading control was run alongside it — that is C10's edit, not mine; this seat only supplies the command.

No gate baseline or freeze is needed: this is a structural control over one live file, not a frozen-input gate. It does not belong in `tools/gates/frozen/` and does not touch `declared-in-r7`.

---

## 7. Boundaries and limits

- **Edited nothing.** Only `reports/round-48/calib/Ca05-heading-control.md` is written. The prototype and staged README live under `.scratch/ca05/` and are disposable. `corpus/README.md` and `reports/round-28/**` are byte-unchanged (sha256 above).
- **Not a replacement for the sweep.** It does not check rows, topics, section counts, totals or footer, and it must not be cited as evidence for any of those.
- **Not yet wired.** Until the integrator adds step 1 of §6, the tool is a tool, not a gate. Calling the claim's "heading-count control" satisfied while the tool is unfiled/uninvoked would be false; the honest post-apply state is "control exists and has a red/green receipt in round 48, invocation leg pending".
- **Scope of the invariant.** Duplicate H2 detection is a bonus, not a requirement; if any future README legitimately repeats an H2 text (e.g. per-part "Notes"), the integrator should narrow that rule rather than suppress the control. At the baseline all 7 H2 texts are unique (verified by the heading census in §1), so the rule is clean today.
- **`to-verify` (owner: integrator):** that `reports/round-48/run-validation.py` incorporates the leg; that W02 names it. Neither file exists at filing time.

---

## 8. Verified numbers and citations

| Number / citation | Measured by | Result |
|---|---|---|
| HEAD | `git rev-parse HEAD` | `a01405dd36367292255c2652ac0a601f4cd6a0af`, prefix `a01405d` = `reports/round-48/claims.json:7` |
| README H1 count | `grep -c '^# ' corpus/README.md` | `2` at lines 1 and 3 |
| README H1 lines | `grep -n '^# ' corpus/README.md` | `1:`, `3:` |
| README length | `wc -l corpus/README.md` | `575` |
| README sha256 | `sha256sum corpus/README.md` | `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` |
| Sweep on defective file | `python3 -B reports/round-28/readme/sweep.py` | exit `0`; `readme_sha256 7c788a1d…` |
| Sweep legs | `reports/round-28/readme/sweep.py:18-27` | `index`, `footer`, `block`; no heading leg |
| Sweep `ok` terms | `reports/round-28/readme/sweep.py:191-194` | missing/ghosts/mismatches/drift/footer_findings + totals; no heading term |
| Staged fix length | `wc -l .scratch/ca05/README.fixed.md` | `573` = 575 − 2 |
| Staged fix sha256 | `sha256sum .scratch/ca05/README.fixed.md` | `d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079` |
| Control selftest | `... --selftest` | `8/8 checks passed`, exit `0` |
| Control on live | `... --readme corpus/README.md` | exit `1`; `H1-COUNT lines=[1, 3]` |
| Control on staged fix | `... --readme .scratch/ca05/README.fixed.md` | exit `0`; `h1_lines [1]` |
| Control on missing file | `... --readme .scratch/ca05/absent.md` | exit `2`, `ok: null` |
| Sweep on staged fix | `python3 -B reports/round-28/readme/sweep.py --readme …` | exit `0`, 223/223 |
| Drafted tool length | `wc -l .scratch/ca05/check-readme-heading.py` | `244` |

### 8.1 Adjacent arithmetic check (outside this seat — for C10/C03)

Not part of the Ca edit, but verified while measuring the header, because r47 failed on unverified arithmetic:

- `corpus/README.md:11` states the rev-2.4 vector moved `25/23/25/29/24/94 → **25/23/26/25/24/94**`.
- The written target sums `217` (`25+23+26+25+24+94`), not `223`.
- The live directory counts are linguistics 25 / myth-symbol 26 / culture-material 25 / synthesis 29 / verification 24 / civilizations 94 = `223`. The corrected rev-2.4 target is therefore `25/26/25/29/24/94` (sum `223`): myth-symbol's second slot goes 23→26; culture-material stays 25; synthesis stays 29.
- Post-landing rev 2.5 adds one culture-material entry: `25/26/26/29/24/94` = `224`.
- `reports/round-48/claims.json` describes the repair as "synthesis 25→29, myth-symbol 23→26, culture-material 26→25 = 224"; the three deltas are right but the `= 224` conflates the rev-2.4 repair (223) with the rev-2.5 post-landing total (224). C10 should state the two vectors separately.
