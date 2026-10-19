# K02 — README defect scout (claim Ca)

- Seat: `K02` | role: scout | claim: **Ca** (calibration) | round 48, loop 2, position 2
- Out path: `reports/round-48/scout/K02-readme-defect.md` (this file)
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7`
- Date of measurement: 2026-10-19T19:39Z
- Mission: confirm the duplicate H1 at `corpus/README.md:1,3`, the rev-2.4 prose-vector defect, and the sweep's missing heading-count control; specify the exact edits.

**Result in one line.** All three Ca premises are true at HEAD. The duplicate H1 is a two-line deletion whose post-state I built and sweep-tested green; the rev-2.4 vector is wrong by six entries and my one-line replacement re-sums to 223; the sweep has 12 selftests and none reads headings. I also found a **fourth, unqueued defect** (a truncated duplicate `revision: 2.0` header at `:42`/`:44`) that the Ca edit must *not* absorb.

---

## 1. Baseline measured

All commands from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-48/
$ wc -l corpus/README.md
575 corpus/README.md
$ sha256sum corpus/README.md
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd  corpus/README.md
$ find corpus/knowledge -name '*.md' | wc -l
223
$ for p in civilizations culture-material linguistics myth-symbol synthesis verification; do
    printf '%-16s %s\n' "$p" "$(ls corpus/knowledge/$p/*.md | wc -l)"; done
civilizations    94
culture-material 25
linguistics      25
myth-symbol      26
synthesis        29
verification     24
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", ..., "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0
```

The sweep is green **with** the duplicate H1 present. That is the defect: the instrument's 12 selftests (`python3 -B reports/round-28/readme/sweep.py --selftest` → `selftest: 12/12 checks passed`, exit 0) cover rows, topics, headers, totals and the footer — no heading leg. The lineage is already filed: `reports/round-40/op/defect-queue-v2.json:112-119` carries `R36-README-DUPLICATE-HEADING` as `carried-with-owner`, its `reason` says "sweep-blind (the r28 sweep checks sections/rows/totals/footer, not headings — r39 X00-7)", and its `next_touch` prescribes exactly this claim: "remove the redundant title as a separate recorded act, then re-run the sweep plus a heading-count control the sweep lacks". Round 48's Ca claim is that next touch.

---

## 2. Defect D1 — duplicate H1 (`R36-README-DUPLICATE-HEADING`)

### 2.1 Evidence

```
$ grep -n '^# ' corpus/README.md
1:# kotodama-shokunin corpus index
3:# kotodama-shokunin corpus index
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
$ diff <(sed -n '1p' corpus/README.md) <(sed -n '3p' corpus/README.md) && echo IDENTICAL
IDENTICAL
$ grep -c '^#' corpus/README.md
9        # 2 H1 + 7 H2
```

Live bytes (`awk`, line numbers mine):

```
1	# kotodama-shokunin corpus index
2	(blank)
3	# kotodama-shokunin corpus index
4	(blank)
5	revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
```

Lines 1 and 3 are byte-equal. Therefore "keep `:1`" and "keep `:3`" produce **the same file**: whichever pair of lines (1–2 or 3–4) is deleted, the surviving bytes are `H1\n\nrevision: 2.4 …`. The deliverable is one title plus one blank removed so the file opens with a single H1 and the revision block begins at line 3.

### 2.2 Exact edit (fenced, integrator-applied)

Target: `corpus/README.md`. Delete lines 3 and 4. Before/after bytes:

```diff
--- a/corpus/README.md
+++ b/corpus/README.md
@@ -1,5 +1,3 @@
 # kotodama-shokunin corpus index
 
-# kotodama-shokunin corpus index
-
 revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
```

Byte-equivalent command forms (either yields the same sha256):

```
sed -i '3,4d' corpus/README.md
# or: sed -i '1,2d' corpus/README.md   -> identical bytes, because :1 == :3 and both blanks are empty
```

### 2.3 Post-edit state — measured on a staged copy, not asserted

I staged the edit under `.scratch/k02/readme-dupfix.md` and ran the live sweep against it with the sweep's own `--readme` flag (`reports/round-28/readme/sweep.py:415`), which compares the supplied README against the live knowledge tree; no corpus byte was touched.

```
$ awk 'NR==3||NR==4{next}{print}' corpus/README.md > .scratch/k02/readme-dupfix.md
$ wc -l .scratch/k02/readme-dupfix.md
573
$ grep -c '^# kotodama-shokunin corpus index' .scratch/k02/readme-dupfix.md
1
$ grep -n '^#' .scratch/k02/readme-dupfix.md
1:# kotodama-shokunin corpus index
175:## linguistics/ (25)
203:## myth-symbol/ (26)
232:## culture-material/ (25)
259:## synthesis/ (29)
291:## verification/ (24)
318:## civilizations/ (94)
415:## Known gaps (frontier)
$ python3 -B reports/round-28/readme/sweep.py --readme .scratch/k02/readme-dupfix.md
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer_findings [] footer_ok True
readme_sha256 d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079
exit=0
```

`sha256` of the post-D1 file is `d407260d…b3190079`; 573 lines; one H1; all 7 H2 sections and all 223 rows intact.

### 2.4 Line-number shift — a trap for the C-claim drafter

Deleting two lines above the revision block shifts every later `corpus/README.md` line by −2. Any pre-fix `path:line` citation into the README becomes stale the moment Ca lands. Measured mapping:

| Anchor | Pre-Ca | Post-Ca |
|---|---:|---:|
| `revision: 2.4` block | 5 | 3 |
| rev-2.4 vector line | 11 | 9 |
| `## linguistics/ (25)` | 177 | 175 |
| `## myth-symbol/ (26)` | 205 | 203 |
| `## culture-material/ (25)` | 234 | 232 |
| calendar row | 240 | 238 |
| costume row | 241 | 239 |
| `## synthesis/ (29)` | 261 | 259 |
| `## verification/ (24)` | 293 | 291 |
| `## civilizations/ (94)` | 320 | 318 |
| `## Known gaps (frontier)` | 417 | 415 |
| `Total knowledge entries: 223.` | 544 | 542 |
| `Counts checked 2026-10-19 …` | 546 | 544 |
| `(total 223 files; directory totals 25/26/25/29/24/94).` | 548 | 546 |

Concrete collision: the cartography seed cites `reports/round-44/scout/K02-gap-scout.md:307-311` as `corpus/README.md:234`, `:240-241`, `:544`, `:548`, `:5`. Those are correct **pre-Ca**; post-Ca they are `:232`, `:238-239`, `:542`, `:546`, `:3`. The C10 README draft must use post-Ca numbers, or the assembled index will carry correctly-worded edits at addresses that have moved. The filed r44 report cannot be edited; the correction is C10's to make.

### 2.5 Ordering constraint against C's rev 2.5

Both Ca and C edit the README top. Apply **Ca first**, then C:

1. Ca deletes lines 3–4 → 573 lines, `revision: 2.4` at line 3.
2. C inserts its new `revision: 2.5` block above rev 2.4, i.e. starting at line 3, pushing rev 2.4 down by the block's line count.
3. C's rev 2.5 block must state the corrected vector `25/26/26/29/24/94` (sums 224) — see §3.

If C's rev 2.5 is inserted *before* Ca's deletion, the block lands between two H1s, and the duplicate-heading control still fails after the round. The round's final state must be: exactly one H1, one `revision: 2.5` block, one `revision: 2.4` block.

---

## 3. Defect D2 — rev-2.4 prose vector sums 217, not 223

### 3.1 Evidence

Line 11 pre-fix (`awk`, exact bytes):

```
10	`## myth-symbol/` moved 23 → **26**; the totals and footer moved 220 → **223** and
11	the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**. Re-measured with
```

Arithmetic, recomputed:

```
before vector 25+23+25+29+24+94 = 220   # matches the "220 → 223" phrase
after  vector 25+23+26+25+24+94 = 217   # does NOT match 223
correct      25+26+25+29+24+94 = 223   # live sweep footer: [25, 26, 25, 29, 24, 94]
```

The error is a **slot swap**, not a missing term: the +3 belongs to `myth-symbol` (slot 2), but the prose puts it in `culture-material` (slot 3) while dropping `synthesis` 29 → 25. The same block's own sentence "`## myth-symbol/` moved 23 → **26**" contradicts the vector it prints. The live footer (`corpus/README.md:548`) and the sweep's `footer_live` both read `25/26/25/29/24/94`.

### 3.2 Exact edit (fenced)

Target: `corpus/README.md:11` (post-Ca: line 9). One token changes:

```diff
--- a/corpus/README.md
+++ b/corpus/README.md
@@ -11 +11 @@
-the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**. Re-measured with
+the vector 25/23/25/29/24/94 → **25/26/25/29/24/94**. Re-measured with
```

Measured post-state (D1 + D2, `.scratch/k02/readme-dupfix-vector.md`): 573 lines, `sha256 e80b90e1fc4d47770fb33277060fb9884f18fd5b95805e20aa9ddbcc9e570bef`, sweep `rows 223 files 223`, `footer_findings []`, exit 0.

### 3.3 One decision the integrator should make explicitly

Rewriting a revision-history block is editing a dated record. The README's own convention, at `corpus/README.md:549-556`, is to **preserve** a superseded reading and label it ("Superseded reading, preserved as the dated record it was…"). The Ca claim's `after_required` (`reports/round-48/claims.json:45`) says "the rev-2.4 prose-vector defect repaired in the same edit", so the literal repair in §3.2 is the primary action and what I have measured.

An equally defensible alternative, following the file's own precedent, is to leave `:11` untouched and add one dated line under the rev-2.4 block: "Correction (r48): this revision's vector printed `25/23/26/25/24/94` (sums 217); the live vector was and is `25/26/25/29/24/94` (sums 223)." That preserves the record and fixes the reader's arithmetic, but it does not meet the claim's literal "repaired". I recommend the literal repair, with this note in LOG.md so the edit is a recorded act rather than a silent history rewrite. Flagging it because Ca03/R04 will read the diff and should judge it as a deliberate correction, not an unaudited mutation.

---

## 4. Defect D3 — the sweep has no heading-count control

### 4.1 Evidence

- The sweep's documented legs are index / footer / block (`reports/round-28/readme/sweep.py:20-30`); no heading leg.
- `grep -n 'heading\|H1' reports/round-28/readme/sweep.py` → no match.
- 12 selftests, all green, none about headings (`--selftest` → `12/12 checks passed`).
- The filed queue row already names the blind spot: `reports/round-40/op/defect-queue-v2.json:116` — "sweep-blind … not headings — r39 X00-7"; `:117` requires "a heading-count control the sweep lacks".

### 4.2 Where the control can land

`reports/round-28/readme/sweep.py` is filed round bytes under the shared rule (`reports/round-1..47/**` immutable), so the control **cannot** be added there. It must be a new live tool. `tools/` holds the lane's standalone checkers (`tools/check-evidence-coupling.py`, `tools/check-craft-exercise.py`, `tools/check-gate-battery.py`); `tools/harness/` holds lane instruments. I specify `tools/check-readme-headings.py` — new file, stdlib, read-only, unregistered in any frozen gate manifest (no `declared-in-r7` re-freeze, no packet-surface change).

### 4.3 Specification — written, run, and green

I wrote the tool to `.scratch/k02/check-readme-headings.py` and executed it. It is red on the live file, green on both staged fixes, and 6/6 on its own controls:

```
$ python3 -B .scratch/k02/check-readme-headings.py --selftest
PASS single H1 passes {"ok": true, "findings": []}
PASS duplicate H1 flagged {"ok": false, "findings": ["H1_COUNT", "DUPLICATE_HEADING"]}
PASS no H1 flagged {"ok": false, "findings": ["H1_COUNT"]}
PASS duplicate H2 flagged {"ok": false, "findings": ["DUPLICATE_HEADING"]}
PASS heading inside a fence ignored {"ok": true, "findings": []}
PASS #not-a-heading (no space) ignored {"ok": true, "findings": []}
selftest: 6/6 checks passed
exit=0

$ python3 -B .scratch/k02/check-readme-headings.py --readme corpus/README.md
h1_count 2 ['kotodama-shokunin corpus index', 'kotodama-shokunin corpus index']
duplicate_headings ['kotodama-shokunin corpus index']
findings [{'class': 'H1_COUNT', 'count': 2, 'expected': 1, ...}, {'class': 'DUPLICATE_HEADING', ...}] ok False
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=1

$ python3 -B .scratch/k02/check-readme-headings.py --readme .scratch/k02/readme-dupfix.md
h1_count 1 ['kotodama-shokunin corpus index']
duplicate_headings []  findings [] ok True
readme_sha256 d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079
exit=0
```

The integrator-applied body (fenced; identical to the tested file):

```python
#!/usr/bin/env python3
"""check-readme-headings.py — the corpus/README.md heading control (read-only).

The r28 index sweep (reports/round-28/readme/sweep.py) checks sections, rows,
topics, totals and the counts footer. It never reads headings, so a duplicated
title (R36-README-DUPLICATE-HEADING, live at corpus/README.md:1,3) passes it
green. This control closes that blind spot: exactly one H1, and no heading
text repeated at any level.

Stdlib only. Read-only. Exit 0 = one H1 and no duplicates; 1 = finding;
2 = could-not-evaluate.

Usage:
  python3 tools/check-readme-headings.py [--readme PATH] [--json] [--selftest]
"""
import argparse
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, ".."))
README = os.path.join(LANE, "corpus", "README.md")

FENCE_RE = re.compile(r"^\s*```")
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)\s*$")


def check(text):
    """Return {h1_count, h1, duplicate_headings, findings, ok, readme_sha256}."""
    h1, seen, dups = [], {}, []
    in_fence = False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if not m:
            continue
        level, title = len(m.group(1)), m.group(2)
        if level == 1:
            h1.append(title)
        seen[title] = seen.get(title, 0) + 1
        if seen[title] == 2:
            dups.append(title)
    findings = []
    if len(h1) != 1:
        findings.append({"class": "H1_COUNT", "count": len(h1), "expected": 1, "h1": h1})
    for title in dups:
        findings.append({"class": "DUPLICATE_HEADING", "text": title, "count": seen[title]})
    return {
        "readme_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "h1_count": len(h1),
        "h1": h1,
        "duplicate_headings": dups,
        "findings": findings,
        "ok": not findings,
    }


def selftest():
    ok = True

    def ctl(name, text, want_ok, want_classes):
        nonlocal ok
        r = check(text)
        got = [f["class"] for f in r["findings"]]
        good = r["ok"] is want_ok and got == want_classes
        ok = ok and good
        print(("PASS " if good else "FAIL ") + name + " " + json.dumps({"ok": r["ok"], "findings": got}))

    ctl("single H1 passes", "# T\n\n## a\n## b\n", True, [])
    ctl("duplicate H1 flagged", "# T\n\n# T\n\n## a\n", False, ["H1_COUNT", "DUPLICATE_HEADING"])
    ctl("no H1 flagged", "## a\n", False, ["H1_COUNT"])
    ctl("duplicate H2 flagged", "# T\n\n## a\n## a\n", False, ["DUPLICATE_HEADING"])
    ctl("heading inside a fence ignored",
        "# T\n\n```\n# not a heading\n```\n", True, [])
    ctl("#not-a-heading (no space) ignored", "# T\n\n#anchor\n", True, [])
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--readme", default=README)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        passed = selftest()
        print("selftest: %s" % ("6/6 checks passed" if passed else "FAILED"))
        return 0 if passed else 1
    try:
        with open(args.readme, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        print(json.dumps({"exit": 2, "error": str(exc)}))
        return 2
    r = check(text)
    if args.json:
        print(json.dumps(r, indent=1, sort_keys=True))
    else:
        print("h1_count %d %s" % (r["h1_count"], r["h1"]))
        print("duplicate_headings %s" % r["duplicate_headings"])
        print("findings %s ok %s" % (r["findings"], r["ok"]))
        print("readme_sha256 %s" % r["readme_sha256"])
    return 0 if r["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
```

Acceptance for the round: pre-fix live exit 1 with `H1_COUNT` + `DUPLICATE_HEADING`; post-Ca live exit 0 with `h1_count 1`. The control does **not** detect D4 (§5), because D4 is not a Markdown heading.

---

## 5. Additional finding (D4, **not** in the Ca claim) — duplicate `revision: 2.0` header

The Ca edit must remove only the title. While verifying "no other heading is touched" I found a separate live duplicate in the same file:

```
41	(blank)
42	revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
43	(blank)
44	revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
45	round-35 entries landed — culture-material six (`agrarian-field-system-lexicon.md`, …
```

```
$ grep -c '^revision: 2\.0' corpus/README.md
2
```

Line 42 is a truncated dangling copy of line 44's header sentence ("…: the ten"), separated by a blank line. It is not a Markdown heading, so neither the sweep nor the §4.3 control sees it; `grep` over `reports/round-37/op/defect-queue.json`, `reports/round-40/op/defect-queue-v2.json` and `reports/round-47/calib/queue-successor-r47.json` finds no row for it. It is an **unqueued** README defect.

Recommendation: do **not** fold it into this edit. Ca07's acceptance ("only the second H1 line removed") and the claim's single-defect scope would both be violated, and mixing a second title-class deletion into the Ca diff makes the sweep-green receipt ambiguous. File it as its own `routed-with-owner` row in the r48 queue successor (owner: integrator / next corpus-index touch; next_touch: r49+; evidence: `corpus/README.md:42,44`, `grep -c` = 2), or record it as a `to-verify` item for the next README touch. This is a handoff to Ca02/Ca06, not a change to my edit.

---

## 6. Apply sequence for the integrator (W02 interface)

1. `sha256sum corpus/README.md` → must equal `7c788a1d…f31cdcd` (baseline pin).
2. Apply D1: delete lines 3–4. Expect 573 lines, sha `d407260d…b3190079`, `grep -c '^# kotodama-shokunin corpus index'` → 1.
3. Apply D2: replace the after-vector at (new) line 9. Expect 573 lines, sha `e80b90e1…e570bef`.
4. Run `python3 -B reports/round-28/readme/sweep.py` → `rows 223 files 223`, `footer_findings []`, `readme_sha256 e80b90e1…`, exit 0.
5. Add `tools/check-readme-headings.py` (fenced body §4.3) and run it: `--selftest` 6/6 exit 0; live exit 0, `h1_count 1`.
6. Only then apply C's rev 2.5 block at line 3 with vector `25/26/26/29/24/94`; re-run the sweep (expect 224) and the heading control (expect 1).
7. File the Ca closing record: `grep` count 2 → 1, sweep green before and after, D4 routed separately.

The two Ca edits touch exactly one file (`corpus/README.md`) plus one new `tools/` file; they touch no corpus entry, no round-1..47 byte, no frozen gate, and no packet surface.

---

## 7. Verification transcript (commands and outputs)

```
$ git rev-parse HEAD                         -> a01405dd36367292255c2652ac0a601f4cd6a0af
$ sha256sum corpus/README.md                 -> 7c788a1d...f31cdcd
$ wc -l corpus/README.md                     -> 575
$ grep -n '^# ' corpus/README.md             -> 1:…; 3:…
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md -> 2
$ grep -c '^#' corpus/README.md              -> 9  (2 H1 + 7 H2)
$ diff <(sed -n 1p) <(sed -n 3p) corpus/README.md -> identical
$ python3 -c "print(25+23+26+25+24+94, 25+26+25+29+24+94, 25+26+26+29+24+94)"
217 223 224
$ python3 -B reports/round-28/readme/sweep.py            -> 223==223, exit 0
$ python3 -B reports/round-28/readme/sweep.py --selftest -> 12/12, exit 0
$ python3 -B reports/round-28/readme/sweep.py --readme .scratch/k02/readme-dupfix.md
  -> 223==223, footer ok, readme_sha256 d407260d..., exit 0
$ python3 -B reports/round-28/readme/sweep.py --readme .scratch/k02/readme-dupfix-vector.md
  -> 223==223, footer ok, readme_sha256 e80b90e1..., exit 0
$ python3 -B .scratch/k02/check-readme-headings.py --selftest -> 6/6, exit 0
$ python3 -B .scratch/k02/check-readme-headings.py --readme corpus/README.md -> exit 1
$ python3 -B .scratch/k02/check-readme-headings.py --readme .scratch/k02/readme-dupfix.md -> exit 0
$ grep -c '^revision: 2\.0' corpus/README.md -> 2
$ sha256sum reports/round-40/op/defect-queue-v2.json
  -> dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907  (unchanged)
```

## 8. What I did not verify

- **D2's historical intent.** I verified the arithmetic and the live footer, not what rev-2.4's author meant to print. The correct vector follows from the block's own "myth-symbol moved 23 → 26" sentence and the live tree; the alternative "preserve + correct" option in §3.3 needs an integrator ruling.
- **Whether the 217 was ever detected.** I did not audit prior rounds for a finding on the rev-2.4 vector; the r44 K02 seed flagged it at `reports/round-44/scout/K02-gap-scout.md:314`, but that is a report, not a queue row.
- **The post-C round state.** The 224 sweep and rev-2.5 bytes belong to C10/C11; I measured only Ca's 223-tree states.
- **D4's origin commit.** `git log` shows README last touched at `7ceff59`; I did not bisect which apply introduced the line-42 leftover.
- **External tooling.** No network, no installs. Everything above is stdlib Python and grep over the live tree.

## 9. Write surface

This file only: `reports/round-48/scout/K02-readme-defect.md`. Test artifacts were written under `.scratch/k02/` (git-ignored scratch, `TMPDIR`), never under `corpus/`, `tools/`, or `reports/round-1..47/**`. No corpus file was staged or edited; no git commit/push; no install; no network; no `reports/round-*/run-validation.py` executed; no frozen gate or packet surface touched. All numbers above are command output at HEAD `a01405d` on 2026-10-19.
