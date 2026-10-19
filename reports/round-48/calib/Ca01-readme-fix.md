# Ca01 — README duplicate-H1 fix (claim Ca: calibration)

- Seat: `Ca01` | role: executor | claim: **Ca** | round 48, loop 2, position 2
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json` `baseline_commit`.
- Out path: `reports/round-48/calib/Ca01-readme-fix.md` (this file)
- Non-author statement: I drafted no other seat's fragment and edited no filed byte. Every number below is from a command in §8; the fenced patches were validated with `git apply --check`, not asserted.

**One-line judgment.** The defect is live and exactly as claimed: `corpus/README.md` lines 1 and 3 are byte-identical H1s (`grep -c '^# kotodama-shokunin corpus index'` → **2**). Removing the second occurrence plus its trailing blank line yields **575 → 573** lines, sha `7c788a1d…` → `d407260d…`, one H1, and the r28 sweep stays green (**223 rows / 223 files**, 0 missing, 0 ghosts, 0 topic mismatch, 0 header drift, footer ok). Two things the round did not know: the sweep has **no heading leg** at all (§3), and the file carries a **second, same-class duplicate** — a byte-identical orphaned `revision: 2.0` header at lines 42 and 44 (§6). The edit also shifts every `corpus/README.md:NNN` citation by −2; 17 such citations are live, and **all 10 distinct targets are already stale before this edit** (§5).

---

## 1. Measured before-state

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ wc -l corpus/README.md
575 corpus/README.md
$ sha256sum corpus/README.md
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd  corpus/README.md
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
$ grep -n '^# ' corpus/README.md
1:# kotodama-shokunin corpus index
3:# kotodama-shokunin corpus index
$ grep -c '^# ' corpus/README.md
2
```

Bytes 1–5, verbatim (`repr`, so nothing is inferred):

```
1  '# kotodama-shokunin corpus index'
2  ''
3  '# kotodama-shokunin corpus index'
4  ''
5  'revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three'
```

The two H1 lines are byte-identical (32 chars each, no trailing whitespace). Line 2 is the blank separator; line 4 is the blank that separates the title from the revision history. The second title is therefore a duplicated **unit** (blank + H1), not a duplicate line alone — removing only line 3 would leave a double blank (verified as variant B, §4.3).

The live sweep is green over this file, which is the point: nothing in the existing instrument reads `^# ` (§3).

---

## 2. The edit — Hunk 1 (required)

Delete the second H1 and the blank line that follows it. Line 1 is preserved as context; line 3 and line 4 are deleted. Fenced, `git apply`-ready:

```diff
--- a/corpus/README.md
+++ b/corpus/README.md
@@ -1,5 +1,3 @@
 # kotodama-shokunin corpus index
 
-# kotodama-shokunin corpus index
-
 revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
```

Validated against the working tree, not assumed:

```
$ git apply --check --verbose .scratch/ca01/h1-manual.patch
Checking patch corpus/README.md...
rc=0
```

### 2.1 After-bytes (measured by applying the deletion in memory and hashing)

```
wc -l            575 -> 573      (delta -2)
bytes            143866 -> 143832 (delta -34)
sha256           7c788a1d… -> d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079
H1 count        2 -> 1
H1 line         —  -> line 1
head bytes      '# kotodama-shokunin corpus index\n\nrevision: 2.4 — Round-42 …'
```

Arithmetic, stated so it can be checked: the removed slice is the 32-byte H1 plus its two newline characters (`# kotodama-shokunin corpus index\n\n` = 34 bytes). 575 − 2 = 573 lines; 143866 − 34 = 143832 bytes. The 32-character count is `len(lines[0])`, printed in §8, not estimated.

### 2.2 Recorded act

The claim requires the removal "as a recorded act". Recommendation for the integrator: fold one sentence into the **rev 2.5 block that claim C is already writing** (`reports/round-48/targets.json` C10: "new revision 2.5 block above it") — e.g. "This revision also removes the duplicate H1 at old `:3` and (if Hunk 2 is applied) the duplicate `revision: 2.0` header." Do **not** mint a separate rev 2.6 block: two blocks in one landing would invert the file's newest-first order for no gain, and the README's own convention is one block per landing (`corpus/knowledge/verification/index-sweep-verification.md:88`, "Revision blocks are append-only"). The append-only LOG.md entry required by `AGENTS.md` is the durable record either way.

---

## 3. The control the sweep lacks

The r28 sweep cannot catch this defect class. Its docstring declares three legs — `index`, `footer`, `block` (`reports/round-28/readme/sweep.py:18-27`) — and its only heading regex is `^## ` (`:59`). Measured absence of any H1 leg:

```
$ grep -n 'startswith("# ")\|H1\|re.compile(r"\^# ' reports/round-28/readme/sweep.py
(no hits)
```

So a duplicated title, or a duplicated `revision:` header, reads green. `reports/round-28/**` is filed bytes and must not be edited, so the control lands as a **new** tool. Proposed path: `tools/check-readme-structure.py` — the root `tools/check-*.py` convention already carries `--selftest` and JSON-stdout usage blocks (`tools/check-evidence-coupling.py:18-22`, `tools/check-craft-exercise.py:18-21`). Fenced, complete and tested:

```python
#!/usr/bin/env python3
"""readme-structure-control — duplicate-heading control for corpus/README.md.

The r28 index sweep (`reports/round-28/readme/sweep.py`) reads rows, section
headers, the totals line and the counts footer. It never reads the document's
own headings, so a duplicated title, or a duplicated `revision:` header line,
reads green. This control adds exactly that leg.

Legs (stable ids):
  RS-H1       exactly one line matching `^# ` (a markdown H1)
  RS-H1-POS   that single H1 is the first line of the file (no leading blank)
  RS-REV-DUP  no two `^revision: <N>.<N> ` header lines are byte-identical

Usage:
  python3 tools/check-readme-structure.py [--json] [--h1-only] [--selftest]

Exit codes: 0 clean, 1 finding(s), 2 could-not-evaluate (README unreadable).
Read-only: this control opens corpus/README.md and writes nothing.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, ".."))
README = os.path.join(LANE, "corpus", "README.md")
REV_RE = re.compile(r"^revision: (\d+\.\d+) ")


def inspect(text, h1_only=False):
    lines = text.split("\n")
    h1 = [i + 1 for i, ln in enumerate(lines) if ln.startswith("# ")]
    findings = []
    if len(h1) != 1:
        findings.append({"id": "RS-H1", "lines": h1, "count": len(h1)})
    if h1 and h1[0] != 1:
        findings.append({"id": "RS-H1-POS", "line": h1[0]})
    if not h1_only:
        seen = {}
        for i, ln in enumerate(lines):
            if REV_RE.match(ln):
                seen.setdefault(ln, []).append(i + 1)
        for header, where in seen.items():
            if len(where) > 1:
                findings.append(
                    {"id": "RS-REV-DUP", "lines": where, "header": header[:60]}
                )
    return {"findings": findings, "h1_lines": h1, "exit": 1 if findings else 0}


def selftest():
    ok = True

    def chk(name, cond, detail=""):
        nonlocal ok
        ok = ok and cond
        print(("PASS " if cond else "FAIL ") + name + ((" " + detail) if detail else ""))

    good = "# title\n\nrevision: 2.0 — x\n"
    r = inspect(good)
    chk("clean document passes", r["exit"] == 0, json.dumps(r["findings"]))
    r = inspect("# title\n\n# title\n\nrevision: 2.0 — x\n")
    chk("duplicate H1 flagged", [f["id"] for f in r["findings"]] == ["RS-H1"],
        json.dumps(r["findings"]))
    r = inspect("\n# title\n")
    chk("leading blank flags position", [f["id"] for f in r["findings"]] == ["RS-H1-POS"],
        json.dumps(r["findings"]))
    r = inspect("# t\n\nrevision: 2.0 — x\n\nrevision: 2.0 — x\ny\n")
    chk("duplicate revision header flagged",
        [f["id"] for f in r["findings"]] == ["RS-REV-DUP"], json.dumps(r["findings"]))
    r = inspect("# t\n\nrevision: 2.0 — x\n\nrevision: 1.9 — y\n")
    chk("distinct revision headers pass", r["exit"] == 0, json.dumps(r["findings"]))
    r = inspect("# t\n\nrevision: 2.0 — x\n\nrevision: 2.0 — x\ny\n", h1_only=True)
    chk("--h1-only scopes the revision leg", r["exit"] == 0, json.dumps(r["findings"]))
    print("SELFTEST " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--h1-only", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    try:
        with open(README, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        print(json.dumps({"id": "RS-DATA", "detail": str(exc)}))
        return 2
    r = inspect(text, h1_only=a.h1_only)
    if a.json:
        print(json.dumps(r, indent=1))
    else:
        print("h1_lines " + json.dumps(r["h1_lines"]))
        print("findings " + json.dumps(r["findings"]))
        print("exit " + str(r["exit"]))
    return r["exit"]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

### 3.1 Control results (run from a scratch copy; the tool's own `--selftest` is 6/6 PASS)

| Tree state | `h1_lines` | findings | exit |
|---|---|---|---|
| live HEAD `a01405d` | `[1, 3]` | `RS-H1 [1,3]`, `RS-REV-DUP [42,44]` | **1** |
| after Hunk 1 only | `[1]` | `RS-REV-DUP [40,42]` | **1** |
| after Hunk 1 + Hunk 2 | `[1]` | none | **0** |

This is the load-bearing consequence: **the control is red on the live file for a reason the round has not dispositioned** (§6). If the integrator applies only Hunk 1, run the control with `--h1-only` and file the §6 residue as a successor; the recommended path is both hunks, which makes the control green without a scope argument.

---

## 4. Post-edit verification

### 4.1 The r28 sweep stays green (in-memory, on the exact post-edit text)

```
$ python3 - <<'PY'   # importlib-load reports/round-28/readme/sweep.py; sweep(edited_text)
BEFORE  ok=True  rows=223 files=223
AFTER   ok=True  rows=223 files=223  totals_line=223  footer_findings=[]
        missing_from_index=[]  orphan_rows=[]  topic_mismatch=[]  header_drift={}
PY
```

The sweep reads `## section/ (N)`, `- \`file\` — topic`, the totals line and the footer (`reports/round-28/readme/sweep.py:59-72`); none of those touch the title region, which is why the edit is index-safe. The `readme_sha256` the sweep reports moves with the file — that is expected, and the delivery certificate must quote the post-apply sha, not this one (`reports/round-48/targets.json` D01: the post-apply sweep is the only delivery certificate).

### 4.2 The two variants, so the reviewer can see why Hunk 1 is written this way

| Variant | Lines | Head bytes | Verdict |
|---|---:|---|---|
| A: delete lines 3–4 (Hunk 1) | 573 | `# …\n\nrevision: 2.4 …` | **adopt** — one clean blank separator |
| B: delete line 3 only | 574 | `# …\n\n\nrevision: 2.4 …` | reject — leaves a double blank |
| C: `git apply` tolerance | — | — | patch has 3 lines of context; `git apply` resolves offsets, so the hunk is order-independent relative to claim C's row/totals edits |

### 4.3 Nothing else in the file changes

The patch touches only lines 3–4; every other line is byte-identical by construction (a single contiguous deletion, verified by `difflib` producing exactly one hunk). No revision block, row, totals line, or footer byte is edited, so the revision-history invariant (`index-sweep-verification.md:88`) holds.

---

## 5. Blast radius — 17 live line citations, all already stale

Removing two lines shifts every `corpus/README.md:NNN` target at N ≥ 5 to N−2. Measured census before the edit:

```
$ grep -ro "corpus/README\.md:[0-9]\+\(-[0-9]\+\)\?" corpus/knowledge/ | wc -l
16
$ grep -ro "corpus/README\.md:[0-9]\+\(-[0-9]\+\)\?" corpus/lessons/ … | wc -l
1        (corpus/lessons/round-19.md:113 -> :280-291; filed, never editable)
```

16 instances in `corpus/knowledge/` resolve to 10 distinct targets, in two files (`verification/index-sweep-verification.md`, `verification/append-only-record-verification.md`) plus one in `myth-symbol/divination-omen-systems.md`. I read every distinct target:

| Cited target | Claiming `file:line` | What the citation says it holds | What the target holds now | Verdict |
|---|---|---|---|---|
| `:11` | `index-sweep-verification.md:14` | revision 2.1's "212 rows vs 212 files" | rev 2.4's vector line | stale |
| `:14-28` | `index-sweep-verification.md:14` | the revision 2.0 block | revisions 2.3 and 2.2 | stale |
| `:35` | `divination-omen-systems.md:27` | `## myth-symbol/ (16)` row count | a round-35 sparring fragment; the header is `:205` (`(26)`) | stale |
| `:43-55` | `index-sweep-verification.md:10, :53` | revision 1.8's footer-defect record | blank + the revision 2.0 block (1.8 is `:71-89`) | stale |
| `:43-61` | `append-only-record-verification.md:12` | the revision convention precedent | revision 2.0 header/body + round-28 C entry | stale |
| `:52` | `index-sweep-verification.md:88, :99` | "preserved as the dated record it was" | rev 2.0's vector line (the phrase is `:550`) | stale |
| `:95-101` | `index-sweep-verification.md:11, :51, :94` | revision 1.5's repair | inside revision 1.7 (`:91-102`) | stale |
| `:101` | `index-sweep-verification.md:95` | a count-without-reading entry | "…passing structural gates do not certify historical truth." | stale |
| `:505` | `index-sweep-verification.md:14` | the totals line | a Known-gaps bullet (totals is `:544`) | stale |
| `:510` | `index-sweep-verification.md:14, :17, :81, :100` | the counts-footer / inventory note | a D4 receipt line (the note is `:549`) | stale |

So the edit does not create the staleness; it worsens an existing decay by two lines. The mechanism is structural, not carelessness: new revision blocks are inserted at line 5 (newest-first — `:5` is 2.4, `:14` is 2.3, `:24` is 2.2, …), so every landing pushes all fixed-line citations down by the block's length. This is a genuine calibration finding for the round: **README line citations are self-decaying as long as revision history is prepended.** Recommended successor disposition (owner: integrator/Ca queue): cite revision blocks by their text ("revision 1.8 block") or by the section header, not by line; repair the 17 instances in one pass against a post-landing file, never piecemeal. I did **not** draft those repairs — `corpus/knowledge/**` is integrator-applied and outside Ca01's apply scope; the lessons citation is filed and can never be repaired.

### 5.1 Integration ordering with claim C's rev 2.5

Claim C's README edit anchors on `:234` (`## culture-material/ (25)`), `:240-241` (rows), `:544` (totals) and `:546-548` (footer), and inserts a block at `:5`. If Hunk 1 lands first, those become `:232`, `:238-239`, `:542`, `:544-546`. **Do not retype line numbers from one diff into the other.** Two safe orders:

1. Apply both as one combined README patch computed against `a01405d` (both hunks are content-anchored; they touch disjoint regions).
2. Apply Hunk 1 first, then recompute C10's diff against the post-Hunk-1 file before applying.

Either way, the delivery certificate is the post-apply `reports/round-28/readme/sweep.py` reading (223 → 224 rows once C lands).

---

## 6. Adjacent same-class defect — duplicate `revision: 2.0` header (lines 42/44)

Found while verifying the H1 fix, measured, and **outside** the Ca01 mission's literal wording ("removing the redundant second H1 at `corpus/README.md:3`"). Reported, not absorbed — integrator ruling.

```
$ sed -n '42p;44p' corpus/README.md | sha256sum        # both lines hash identically
5db4ca8350fdfe325378e10a98e804c15b5e727d707210c6d60bee402366edf5  -
5db4ca8350fdfe325378e10a98e804c15b5e727d707210c6d60bee402366edf5  -
$ grep -c '^revision: 2\.0 ' corpus/README.md
2
$ sed -n '41,45p' corpus/README.md | nl -ba -v41
41  (blank)
42  revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
43  (blank)
44  revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
45  round-35 entries landed — culture-material six (…
```

Line 42's header is **orphaned**: it has no body of its own; the body at 45–56 belongs to the header at 44. It is the identical defect pattern as the H1 (copy-paste duplicate separated by one blank), and it is invisible to the sweep for the same reason. Optional Hunk 2, applied **after** Hunk 1 (line numbers below are post-Hunk-1):

```diff
--- a/corpus/README.md
+++ b/corpus/README.md
@@ -37,6 +37,4 @@
 Re-measured with `python3 reports/round-28/readme/sweep.py`: 212 rows vs 212 files, exit 0.
 Non-canon examples and passing structural gates do not certify historical truth.
-
-revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
 
 revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
```

Measured effect of Hunk 1 + Hunk 2 together (in memory, hashed):

```
wc -l          575 -> 571
sha256         7c788a1d… -> a80c01696dfa682c1727cae31b7c83055387a6c541670b658e482832cbe6a875
r28 sweep      ok=True rows=223 files=223 totals_line=223 footer_findings=[]
control exit   0 (both legs clean)
```

It removes no revision content: the orphan header carries no body, and the 2.0 block body stays attached to its surviving header. If the integrator declines it, the control must run `--h1-only` and the residue needs a successor row (owner: integrator; next_touch: the same pass that repairs the §5 citations) — otherwise the new gate ships red.

---

## 7. What I did not verify / to-verify

- **The applied file.** I verified the patch with `git apply --check` and hashed the resulting bytes in memory; neither `corpus/README.md` nor any other filed byte was written. The post-apply sha must be re-read at apply time (§4.1).
- **Claim C's rev 2.5 bytes.** I did not read C10's draft; the line-anchor collision in §5.1 is derived from the live line numbers the round's own targets name, not from C10's fragment. If C10 is already content-anchored, the hazard is smaller — `to-verify` at integration.
- **Whether a `tools/check-readme-structure.py` gate must be registered anywhere** (a gate battery, `tools/gates/typed-pipelines.json`, or a round runner). I checked only the invocation convention; registration is `to-verify` with the integrator, and the control is safe as a standalone invocation either way.
- **The 17 citations' original accuracy at authoring time.** I measured their state at `a01405d` only; whether they were correct when written is not recoverable from the live file without reading the historical READMEs, which I did not do.
- **External sources.** None; this claim has no bibliographic surface.

## 8. Commands and write-surface statement

All run from the lane root, 2026-10-19, with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:

```
$ git rev-parse HEAD                       -> a01405dd36367292255c2652ac0a601f4cd6a0af
$ wc -l corpus/README.md                   -> 575
$ sha256sum corpus/README.md               -> 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md -> 2
$ grep -n '^# ' corpus/README.md           -> 1, 3
$ python3 -c 'len(open(...,"rb").read())'  -> 143866 bytes
$ python3 -c 'len(lines[0])'               -> 32 chars
$ python3 (diff + sha + sweep on edited text) -> 573 lines; sha d407260d…; sweep ok=True rows=223 files=223
$ git apply --check --verbose .scratch/ca01/h1-manual.patch -> rc=0
$ python3 .scratch/ca01/check-readme-structure.py --selftest -> 6/6 PASS, SELFTEST PASS
$ python3 (control.inspect on live / H1-only / both) -> exit 1 / 1 / 0
$ grep -ro "corpus/README\.md:[0-9]\+\(-[0-9]\+\)\?" corpus/knowledge/ | wc -l -> 16
$ grep -ro "corpus/README\.md:[0-9]\+\(-[0-9]\+\)\?" corpus/lessons/ … | wc -l -> 1
```

**Write surface:** this file only — `reports/round-48/calib/Ca01-readme-fix.md`. Temporary test artifacts were confined to `.scratch/ca01/` (a patch file and a scratch copy used for `patch --dry-run`); nothing was written under `corpus/**`, `tools/**`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**`. No git commit, push, install, or network. No `reports/round-*/run-validation.py` was executed. No corpus entry was staged; both hunks are fenced for the integrator.
