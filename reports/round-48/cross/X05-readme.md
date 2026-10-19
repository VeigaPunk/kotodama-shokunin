# X05 — README duplicate-heading fix: critic review (non-author)

- Seat: `X05` | role: critic | claim: **Ca** (calibration) | round 48, loop 2, position 2
- Baseline: `a01405d` (`git rev-parse --short HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7`
- Out path: `reports/round-48/cross/X05-readme.md` (this file only)
- Non-author statement: I drafted no Ca fragment and edited no repo file. `git status --porcelain` at close shows only the pre-existing untracked `reports/round-46/review/` and `reports/round-48/`; no tracked path changed. Every number below is a command output in §8.

**One-line verdict.** The removal is **safe and byte-unambiguous**: deleting the second H1 and its blank line (lines 3–4) leaves 223 rows, six section headers, 12 revision blocks and the counts footer byte-identical, and the r28 sweep stays green (`rows 223 files 223`, `footer_ok True`, exit 0). But **"sweep still green" is not evidence that the defect is fixed or controlled** — I proved the sweep blind to headings (§2.3), found the same duplicate-block class surviving at `corpus/README.md:42/:44`, and found the authorizing queue row still open (§4). The edit is landable; the claim's acceptance evidence needs the independent control in §5 and the queue closure in §4.2.

---

## 1. Baseline measurement (HEAD `a01405d`, clean tree)

```
$ git rev-parse --short HEAD
a01405d
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-48/
$ sha256sum corpus/README.md
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd  corpus/README.md
$ grep -n '^# ' corpus/README.md
1:# kotodama-shokunin corpus index
3:# kotodama-shokunin corpus index
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
$ grep -c '^revision: ' corpus/README.md
12
$ grep -c '^- `.*\.md` — ' corpus/README.md
223
$ python3 -B reports/round-28/readme/sweep.py    # exit 0
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", ..., "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
```

`reports/round-28/readme/sweep.py --selftest` = 12/12 PASS, exit 0 — the instrument is trustworthy for the legs it owns.

The defect is not new. `reports/round-40/op/defect-queue-v2.json:112` records the same finding (`R36-README-DUPLICATE-HEADING`, origin r33–36 census) with `verification` "grep count 2 at dfb0719". It has now survived r41–r47.

## 2. Simulated post-fix state (staged in `.scratch/x05/`, repo untouched)

### 2.1 The edit is exactly two lines

```
# original bytes, lines 1-5
'# kotodama-shokunin corpus index\n'
'\n'
'# kotodama-shokunin corpus index\n'
'\n'
'revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three\n'

# unified diff against the fixed text (context 2)
@@ -1,4 +1,2 @@
-# kotodama-shokunin corpus index
-
 # kotodama-shokunin corpus index
 
removed lines: ['# kotodama-shokunin corpus index\n', '\n']
```

Because the two H1 lines are byte-identical, "remove `:3`" and "remove `:1`" produce the same file bytes; the act is well-defined at the byte level even though line numbers are not. Fixed sha256: `d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079` (573 lines).

Two variants were tested: **A** = drop 1-based lines 3–4 (single blank between title and revision, recommended); **B** = drop line 3 only (leaves two consecutive blank lines). Both sweep green; only A is typographically clean. No other byte differs in either variant.

### 2.2 Post-fix sweep and controls

```
$ python3 -B reports/round-28/readme/sweep.py   # on the fixed text via sweep()
ok True rows 223 files 223 totals 223 footer_ok True
missing [] ghosts [] mismatch 0 drift {}
readme_sha256 d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079

$ grep -c '^# kotodama-shokunin corpus index' fixed   -> 1
$ grep -c '^# ' fixed                                 -> 1
$ grep -c '^revision: ' fixed                          -> 12
$ grep -c '^- `.*\.md` — ' fixed                       -> 223
```

### 2.3 The sweep is blind to the defect (proof, not assertion)

I built a fixture with **three** H1 copies and ran the real sweep over it:

```
ok True   rows 223 files 223   '^# ' count 3
```

So the sweep returns exit 0 for the very defect Ca removes. This is exactly what the queue row already says ("sweep-blind … the r28 sweep checks sections/rows/totals/footer, not headings", `reports/round-40/op/defect-queue-v2.json:116`). **Consequence for the claim:** "sweep still green" is a *no-collateral-damage* certificate, not a *defect-fixed* certificate. Ca's `after_required` needs the independent count in §5, or acceptance rests on an instrument that cannot see the change.

## 3. Integrity checklist after the edit

| Element | Pre-fix | Post-fix | Verdict |
|---|---:|---:|---|
| H1 (`^# `) count | 2 (`:1`,`:3`) | 1 (`:1`) | fixed |
| Index rows (sweep's `.md`-anchored regex) | 223 | 223 | identical text + order (`o_rows == f_rows` True) |
| Section headers `## part/ (N)` | 6 | 6 | identical, same declared counts |
| `^revision: ` blocks | 12 | 12 | all retained |
| `Total knowledge entries: 223.` | `:544` | `:542` | retained, value unchanged |
| Counts footer block | `:546` | `:544` | parses, `footer_ok True` |
| `## Known gaps (frontier)` | `:417` | `:415` | retained with body |
| Any programmatic consumer of the H1 | — | — | none: `grep -rn "README\.md" tools/ --include=*.py` finds only `tools/exercise-handoff-e2e.py:1197` (an `examples/` path) |

Line map for downstream authors (every line ≥ 5 shifts by −2):

```
revision 2.4   5 -> 3
first row      178 -> 176
## culture-material/ (25)  234 -> 232
last row       415 -> 413
## Known gaps  417 -> 415
Total knowledge entries  544 -> 542
Counts checked 546 -> 544
```

Filed reports that cite `corpus/README.md:5` (e.g. `reports/round-40/plan/P01-plan.md:59`, `reports/round-40/cross/X01-trades.md:160`) are pre-fix citations and **must not be rewritten** (filed bytes). Round-48 fragments citing README line numbers must be authored against the post-fix map.

## 4. Findings

### 4.1 F1 (high) — the same duplicate-block class survives at `:42/:44`

`reports/round-40/op/defect-queue-v2.json` calls the defect "title repeated at lines 1 and 3", but the README carries a second duplicated block of the same generation:

```
$ sed -n '42p' corpus/README.md | sha256sum
5db4ca8350fdfe325378e10a98e804c15b5e727d707210c6d60bee402366edf5  -
$ sed -n '44p' corpus/README.md | sha256sum
5db4ca8350fdfe325378e10a98e804c15b5e727d707210c6d60bee402366edf5  -
```

Both lines read `<revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten>`; `:42`–`:43` is a truncated duplicate, and the full paragraph begins at `:44`. My control reports it post-fix as `duplicate_revision_first_lines [(40, 42)]` — still present after the H1 removal. The H1 count is a subset of a broader class (duplicated generated blocks), so a control that only counts H1s will certify an index that still duplicates a revision block.

Disposition (recommended, integrator's call): either (a) extend the recorded act to delete the `:42`–`:43` stray pair — same file, same class, same 2-line shape, verified safe because the byte-identical paragraph follows at `:44`, or (b) file it as a named successor row with owner and next_touch. Do **not** silently leave it while the round records "duplicate-heading defect fixed" — that is the r47 failure mode (claim narrower than the measured defect).

### 4.2 F2 (high) — the authorizing queue row is still open, and Ca's claim does not close it

```
$ grep -c README reports/round-43/calib/defect-queue-v2-successor-r43.json
0
```

The r43 successor delta never touches the row; `R36-README-DUPLICATE-HEADING` therefore remains authoritative in the parent as `"class": "carried-with-owner"`, `"next_touch": "r42 or r44"` (`reports/round-40/op/defect-queue-v2.json:112-120`) — already overdue. Ca's `after_required` names only the r47 over-build successor, not this row. If the fix lands without a successor row flipping it to `fixed-with-evidence` (with the post-fix grep, the control output, and the fixed sha as evidence), the durable queue still says the defect is carried, and the round's fix is recorded only in round-48 prose. The r40 file is pinned by the r43 successor (`parent_sha256_at_assembly` = `dfc9265d…`, which I recomputed and it matches), so the only correct move is a **new** successor delta, never an in-place edit.

### 4.3 F3 (medium) — the sweep cannot certify the counts prose; Ca alone leaves it wrong

`reports/round-28/readme/sweep.py:66-72` matches only the `Counts checked <date>` block. The rev-2.4 paragraph is unmeasured, and it is wrong:

```
25/23/26/25/24/94 = 217        (rev 2.4 prose)
25/26/25/29/24/94 = 223        (live tree, section order)
```

So after Ca the index is structurally green but its newest revision prose still undercounts by 6 and misplaces myth-symbol/culture-material/synthesis. `claims.json` assigns that repair to C10 (C landing). Two consequences: (i) Ca must not be scored as "index count prose correct"; (ii) C's README edit must land the vector `25/26/26/29/24/94 = 224` — 25+26+26+29+24+94 = 224 checks out — and the acceptance evidence must re-read the prose, since the sweep will never flag it.

### 4.4 F4 (medium) — the control cannot be "added to the sweep" in place

`reports/round-28/readme/sweep.py` is filed bytes (`reports/round-1..47/**`, shared rules). Editing it would violate the round's own rule and re-open a closed round. Ca's wording ("added to the sweep or a durable note filed") is satisfiable only as a **new** file (a `tools/` gate or a round-48 wrapper that imports the r28 sweep read-only). Any fragment that proposes a diff to `reports/round-28/readme/sweep.py` should be rejected by the integrator.

### 4.5 F5 (low) — a naive row-count control false-positives

```
$ grep -c '^- `' corpus/README.md
224
$ grep -c '^- `.*\.md` — ' corpus/README.md
223
```

The 224th match is a command line inside `## Known gaps` (`corpus/README.md:443`, `- \`python3 tools/replay-frozen.py ...\``). Any new control must reuse the sweep's `.md`-anchored row regex (`reports/round-28/readme/sweep.py:60`), not a bare backtick prefix.

### 4.6 F6 (low) — ordering with C

Ca's two-line delete commutes with C's rev-2.5 insertion (both are content-anchored, and the two H1s are byte-identical), but the integrator should apply **Ca first**, then C, so that C10's row-anchored edits and D01's predicted sha are computed against the post-fix map in §3. Applying C first does not corrupt Ca, but it makes every pinned line number in C's fragments stale in a less obvious way.

## 5. Control draft (tested; integrator applies as a new `tools/` file)

`tools/corpus-readme-heading-gate.py` — read-only, no repo writes, exits 1 on violation:

```python
#!/usr/bin/env python3
"""Read-only corpus/README.md heading + revision-block control.

The r28 sweep (reports/round-28/readme/sweep.py) owns rows/sections/totals/
footer and is blind to headings (r39 X00-7; r40 queue R36-README-DUPLICATE-
HEADING). This gate closes that blind spot without editing filed bytes.
"""
import argparse, hashlib, re, sys


def scan(text):
    h1, fence = [], False
    for i, ln in enumerate(text.splitlines(), 1):
        if ln.startswith("```"):
            fence = not fence
            continue
        if not fence and re.match(r"^# ", ln):
            h1.append((i, ln))
    revs = [(i, ln) for i, ln in enumerate(text.splitlines(), 1)
            if ln.startswith("revision: ")]
    seen, dup = {}, []
    for i, ln in revs:
        if ln in seen:
            dup.append((seen[ln], i, ln))
        else:
            seen[ln] = i
    return h1, revs, dup


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default="corpus/README.md")
    ap.add_argument("--strict-revisions", action="store_true")
    a = ap.parse_args()
    text = open(a.path, encoding="utf-8").read()
    h1, revs, dup = scan(text)
    ok = len(h1) == 1
    print(f"sha256 {hashlib.sha256(text.encode()).hexdigest()}")
    print(f"h1_count {len(h1)} {[i for i, _ in h1]}")
    print(f"revision_blocks {len(revs)}")
    print(f"duplicate_revision_first_lines {[(x, y) for x, y, _ in dup]}")
    if not ok:
        print("FAIL h1_count != 1")
    if dup:
        print("WARN duplicate revision blocks (same first line)")
    if a.strict_revisions and dup:
        print("FAIL strict-revisions")
        ok = False
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
```

Tested matrix (this seat, `.scratch/x05/`):

| Fixture | `h1_count` | `duplicate_revision_first_lines` | exit |
|---|---:|---|---:|
| `corpus/README.md` at `a01405d` | 2 (`[1, 3]`) | `[(42, 44)]` | 1 (FAIL) |
| fixed (lines 3–4 removed) | 1 (`[1]`) | `[(40, 42)]` | 0 (PASS + WARN) |
| fixed + two extra H1 copies | 3 (`[1, 3, 5]`) | `[(44, 46)]` | 1 (FAIL) |

Note the middle row: after Ca, the gate passes on H1 but still warns on the rev-2.0 duplicate (F1). If the integrator wants the gate to be all-green after the correction, the rev-2.0 stray must be removed in the same act (F1a); if it is routed instead, `--strict-revisions` must stay off until that successor lands, and the WARN must be cited in the round record (not hidden).

## 6. Exact apply packet for Ca's README half

- Target: `corpus/README.md`, live file (not filed round bytes).
- Delete: the second block of `# kotodama-shokunin corpus index\n` followed by `\n` (current 1-based lines 3–4). Keep one blank line between the title and `revision: 2.4`.
- Expected post-apply: 573 lines, sha256 `d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079` **if no other edit lands first**; if C's rev-2.5 edit lands in the same batch, the sha differs and only the post-apply sweep + the gate output are certificates.
- Post-apply evidence to file: `grep -c '^# ' corpus/README.md` = 1; `python3 -B reports/round-28/readme/sweep.py` exit 0 with `rows 223 files 223`; gate exit 0 with the WARN (or the rev-2.0 stray removed too).
- Queue: new successor delta closing `R36-README-DUPLICATE-HEADING` as `fixed-with-evidence` (F2), parent = `reports/round-43/calib/defect-queue-v2-successor-r43.json` (or the integrator's designated current head), pinned by sha. Never edit `reports/round-40/op/defect-queue-v2.json` in place.

## 7. Limits

- Everything above was measured on a staged copy; the live README was not modified. I did not run `reports/round-48/run-validation.py` (no such file exists yet at my seat's close).
- Whether the integrator extends Ca to the rev-2.0 stray (F1a) or routes it is a scope decision I cannot make; both are defensible, but the WARN must be recorded either way.
- The over-build disposition half of Ca (Ca02's successor row for the r47 `B1`–`B9` class) is outside this seat's mission and is not judged here; one cross-check only: the heading gate in §5 does **not** cover entry build quality, so the over-build row must not cite it as its control.

## 8. Reproduction commands

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git rev-parse --short HEAD
sha256sum corpus/README.md
grep -n '^# ' corpus/README.md
grep -c '^revision: ' corpus/README.md
grep -c '^- `.*\.md` — ' corpus/README.md
python3 -B reports/round-28/readme/sweep.py; echo exit=$?
python3 -B reports/round-28/readme/sweep.py --selftest; echo exit=$?
python3 -B .scratch/x05/heading-gate.py corpus/README.md
python3 -B .scratch/x05/heading-gate.py .scratch/x05/readme-fixed-A.md
python3 -B .scratch/x05/heading-gate.py .scratch/x05/readme-triple-h1.md
```
