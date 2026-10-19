# Ca07 — README integrity after the duplicate-H1 fix (claim Ca)

- **Seat:** `Ca07` | role: verifier (README integrity), claim **Ca** (calibration) | round 48, loop 2
- **Out path:** `reports/round-48/calib/Ca07-integrity.md` (the only file this seat wrote outside `.scratch/ca07/`)
- **Baseline:** HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (= `reports/round-48/claims.json:7` short form `a01405d`), `git status --porcelain -- corpus tools` empty
- **Verification snapshot:** 2026-10-19T19:40Z
- **Subject:** the live `corpus/README.md` (sha256 `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd`, 575 lines, 143,866 bytes) and the proposed duplicate-H1 removal the integrator applies for Ca.
- **Non-author statement:** I authored no README fix fragment and no landing wire. I staged and measured the edit from the live bytes before W02/Ca03 landed (my staging 16:38–16:40Z; their fragments 16:40–16:41Z), then reconciled my staged digests against `reports/round-48/calib/W02-landing-spec.md` §2 and `reports/round-48/calib/Ca03-readme-verify.md` §4; all three agree on both variants. I edited no corpus byte and no filed round byte. Every number below is a command output, reproduced in §9.

## 0. Verdict

**PASS on Ca-alone integrity, with one ordering condition and four findings.**

The duplicate-H1 removal is surgical: the content diff between HEAD and the fixed file is **exactly one removed H1 occurrence**, the second title at `corpus/README.md:3`. The landing-wire variant B also drops the one blank line that separated the two titles (`3,4d2`); variant A drops only the H1 (`3d2`). Every other line is unchanged — all 223 index rows in the same order, the 12-entry revision history, the totals line and the counts footer, and the trailing newline. The r28 sweep is green before and after with identical legs (only `readme_sha256` changes).

| # | Integrity check (post-fix) | Verdict | Measured |
|---|---|---|---|
| 1 | exactly one H1 remains | **PASS** | `grep -c '^# '` 2 → 1 |
| 2 | no other heading or block edited | **PASS** | diff = one H1 (+ one blank in B); H2 7 → 7, H3 0 → 0 |
| 3 | all 223 index rows intact and in order | **PASS** | ordered row-name sequence identical (223 == 223) |
| 4 | revision history intact | **PASS** | 12 `revision:` lines → 12; first block still rev 2.4 |
| 5 | totals line intact | **PASS** | `Total knowledge entries: 223.` unchanged |
| 6 | counts footer intact | **PASS** | `(total 223 files; directory totals 25/26/25/29/24/94)` unchanged |
| 7 | sweep still green | **PASS** | all legs identical, `ok=True`, 223 == 223 |
| 8 | file encoding / EOF | **PASS** | UTF-8, no CR, ends with newline |
| 9 | no filed byte or `corpus/` write by a seat | **PASS** | `git status --porcelain -- corpus tools` empty |

Condition: apply Ca **before** inserting C's rev-2.5 block, or apply both as one edit (§7). Findings F-Ca07-1..4 are in §6.

## 1. Baseline measured (not asserted)

```
$ sha256sum corpus/README.md
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd  corpus/README.md
$ wc -l corpus/README.md
575 corpus/README.md
$ grep -n '^# ' corpus/README.md
1:# kotodama-shokunin corpus index
3:# kotodama-shokunin corpus index
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
$ grep -n '^## ' corpus/README.md
177:## linguistics/ (25)      205:## myth-symbol/ (26)   234:## culture-material/ (25)
261:## synthesis/ (29)        293:## verification/ (24)  320:## civilizations/ (94)
417:## Known gaps (frontier)
$ grep -c '^revision: ' corpus/README.md
12
$ grep -n '^Total knowledge entries\|^Counts checked' corpus/README.md
544:Total knowledge entries: 223.
546:Counts checked 2026-10-19 from the repo root:
```

Row census from the sweep's own row regex (`reports/round-28/readme/sweep.py:60`): **223 rows, 223 unique**; live files **223**; partition vector `25/26/25/29/24/94` = 223, matching the section headers and the footer. So "all 223 rows" is the live figure at this baseline, and "224" only exists after C lands.

## 2. The exact edit

The head of the file is:

```
1  # kotodama-shokunin corpus index
2
3  # kotodama-shokunin corpus index
4
5  revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
```

Two byte-exact variants were staged under `.scratch/ca07/` (never under `corpus/`):

| Variant | Edit | Result | Lines | Bytes | sha256 |
|---|---|---|---:|---:|---|
| **B (landing-wire variant; certified)** | delete line 3 + the blank at line 4 (`sed '3,4d'`) | one H1, single blank | 573 | 143,832 | `d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079` |
| A (letter-minimal alternative) | delete line 3 only | one H1, then a double blank | 574 | 143,833 | `84e16f566e170ac4be9d7f01d90ca1743640d36c899d9c81808c5dc8c0065633` |

Both are integrity-equivalent. W02 §2 and Ca03 §4 independently staged the same two variants and reached these same digests; the landing wire specifies B, so B is the expected post-apply value certified here. A is the literal "remove only the redundant title" act; its extra blank is already tolerated in the file (three double-blank runs exist pre-fix at lines 203, 232, 318), but it would not match the wire's `wc -l`/digest postconditions.

Exact diff for B (machine accounting `3,4d2`):

```
$ diff -u corpus/README.md .scratch/ca07/README.B.md
@@ -1,7 +1,5 @@
 # kotodama-shokunin corpus index

-# kotodama-shokunin corpus index
-
 revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
```

Machine accounting: B is `3,4d2` (the H1 and one blank, two deletions, zero insertions); A is `3d2` (the H1 only). The blank-line difference is parse-neutral — no sweep leg reads blank lines.

## 3. "Only the second H1 removed" — measured, not eyeballed

```
$ diff corpus/README.md .scratch/ca07/README.A.md
3d2
< # kotodama-shokunin corpus index
$ diff corpus/README.md .scratch/ca07/README.B.md
3,4d2
< # kotodama-shokunin corpus index
<
```

Stronger checks, both PASS on both variants:

- **Line multiset difference** (Python `Counter`): A → `{'# kotodama-shokunin corpus index': 1}`; B → `{'# kotodama-shokunin corpus index': 1, '': 1}` (the same H1 plus one blank). The reverse difference is empty for both, so nothing was added.
- **Ordered row-name sequence equality**: the 223 `^- \`…md\` — ` names extracted from HEAD and from the fixed file are identical in order (`rows identical ordered: True 223 223`, both variants).

So no row, revision paragraph, totals line, footer line, or section header was dropped, reordered, or rewritten.

## 4. Sweep before / after

Run by importing the filed instrument (read-only; no in-tree runner):

```
$ python3 -B reports/round-28/readme/sweep.py --selftest
... 12/12 checks passed

# HEAD text
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25,
       "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd

# fixed text (variant B, the landing-wire variant)
rows 223 files 223
missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer_findings [] footer_ok True
readme_sha256 d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079

# variant A: identical legs, readme_sha256 84e16f56… (staged and swept separately)
```

Every leg is identical except the readme digest. This is expected from the instrument's own parse: it matches only `^## ` section headers (`sweep.py:59`), `^- \`…\` — ` rows (`:60`), `^- topic:` (`:61`), the totals line (`:62`) and the counts footer (`:66-71`); no leg reads an H1.

## 5. The sweep's heading blind spot, proven

The Ca claim says the control is missing, not merely untested. I proved the blindness: starting from the certified fixed text (one H1), I re-planted another H1 immediately above `revision: 2.4` and re-ran the sweep:

```
control: H1 count in planted text 2
control: sweep ok True rows 223 files 223
```

The instrument returns green on a file with a duplicated H1 — exactly the defect being repaired. The durable control the integrator should land with Ca (Ca05's remit; offered here as the measured form):

```
$ test "$(grep -c '^# ' corpus/README.md)" -eq 1 && echo "H1 control PASS"
$ test "$(grep -c '^# kotodama-shokunin corpus index' corpus/README.md)" -eq 1 && echo "duplicate-title control PASS"
```

Expected after the fix: both exit 0, printing PASS; before the fix both exit 1. A sweep extension would add this as a `heading` leg asserting exactly one `^# ` line and no repeated H1 text.

## 6. Findings

**F-Ca07-1 — a second duplicated block exists and is untouched by this fix.** `revision: 2.0 — Round-35 …` appears twice: `corpus/README.md:42` (a header line with no body) and `corpus/README.md:44` (the real block), separated by a blank line. This is the same duplicate-block class as the H1 but is a different defect; the H1 removal leaves it in place (12 `revision:` lines, one of them a bodyless duplicate). I found no queue row for it in the searches in §9 (`grep -rn 'DUPLICATE-HEADING' reports/` returns the H1 row only). **Disposition: `to-verify` / needs its own row** — do not silently fold it into this repair; the Ca claim names only the H1.

**F-Ca07-2 — the defect row's live home is the r40 parent, not the successors.** `R36-README-DUPLICATE-HEADING` is filed at `reports/round-40/op/defect-queue-v2.json:111-120` (id at `:112`) (class `carried-with-owner`, `verification` recorded, `next_touch` "r42 or r44"). Its successors — `reports/round-43/calib/defect-queue-v2-successor-r43.json` (4 rows) and `reports/round-47/calib/queue-successor-r47.json` (4 rows) — do not carry it. Closing the repair therefore requires a successor record that names the r40 row id and the applied README sha; otherwise the parent record remains `carried-with-owner` while the repair is live, i.e. a stale queue state. Recommendation: the Ca landing wire records `{id: R36-README-DUPLICATE-HEADING, class: fixed-with-evidence, evidence: applied sha + grep output + sweep}` in the r48 successor, without editing the pinned parent (`parent_sha256_at_assembly` `dfc9265d…`).

**F-Ca07-3 — the rev-2.4 prose vector is wrong; the repair is C's, not Ca's.** `corpus/README.md:11` states the vector moved `25/23/25/29/24/94 → 25/23/26/25/24/94` (sums **220 → 217**), while the live vector is `25/26/25/29/24/94` (sum **223**) per the section headers and the footer. If Ca lands alone, this defect remains and must not be read as a regression from the H1 removal (the diff proves no other line changed). C's rev-2.5 edit repairs it per `reports/round-48/claims.json:29`. **Disposition:** cross-claim note; verified by C10/C03 in their own remits.

**F-Ca07-4 — line anchors below line 3 shift by one after the fix.** Filed reports cite `corpus/README.md` by line; those citations describe the pre-fix file and remain historical records. New citations must use post-fix numbering:

| Anchor | HEAD | after A | after B |
|---|---:|---:|---:|
| H1 | 1, 3 | 1 | 1 |
| `revision: 2.4` | 5 | 4 | 4 |
| duplicate `revision: 2.0` | 42, 44 | 41, 43 | 41, 43 |
| `## linguistics/` | 177 | 176 | 176 |
| `Total knowledge entries: 223.` | 544 | 543 | 543 |
| `Counts checked …` footer | 546 | 545 | 545 |

The queue's own evidence field (`corpus/README.md:1,3`) is correct only pre-fix; the successor record should cite the applied sha instead of a line pair.

## 7. Ordering condition with claim C

Ca and C both edit the same head. Two safe orders (`W02-landing-spec.md` §2.5 names the first canonical):

1. **Ca first** (`sed '3,4d'`), then C inserts its rev-2.5 block immediately after the surviving H1 and its blank line. The C edit's anchor is unambiguous.
2. **One combined edit**: remove the second H1 (+ its blank) and insert the rev-2.5 block in the same apply.

If C's rev-2.5 patch is context-anchored to HEAD's lines 1-5, applying it after Ca may fail to apply; applying it before Ca still permits the deletion but leaves the rev-2.5 block above a duplicate H1 if the deletion is skipped. **Integrity requirement after the combined apply: exactly one H1, one rev-2.5 block above rev 2.4, 12+1 revision entries, 224 rows, footer 224 / `25/26/26/29/24/94`.**

Anchor hazard: `W02-landing-spec.md:127` says "the H1 removal does not move the `revision:` block". Read as line numbers that is false — the block moves from line 5 to line 4 (F-Ca07-4). What is true is that its position relative to the prologue is unchanged. Apply and cite by content/sha, not by line number.

Mechanical combined check (not a landing prediction): I staged a 224-file tree in `.scratch/ca07/combinedB/` using a throwaway stub entry, applied B plus a rev-2.5 block, one row inserted between `calendar-festival-systems.md` and `costume-semiotics.md`, and the 224/vector updates:

```
rows 224 files 224
missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []
header_drift {}
totals_line 224 totals_ok True
footer {"total": 224, "dir_totals": [25, 26, 26, 29, 24, 94]}
footer_findings [] footer_ok True
OK True
```

The staged fixture's sha (`8f5d2651…`, 580 lines) and its stub topic are **not** deliverables or predictions; only the structural legs are evidence. (The A-based fixture at `.scratch/ca07/combined/` gives the same legs, one line longer.) The real 224-row state must be re-measured with C's actual entry bytes at landing (C11/V01).

## 8. Apply checklist for the integrator (Ca act)

1. Apply exactly one variant to `corpus/README.md` and nothing else: B → `d407260d…` (573 lines, the landing-wire variant), or A → `84e16f56…` (574 lines, the letter-minimal alternative). Do not assert `d407260d…` if C landed first; re-derive the post-edit sha (W02 §2.5).
2. Re-run, in this order, and paste the outputs into the landing receipt:
   - `grep -c '^# kotodama-shokunin corpus index' corpus/README.md` → `1`
   - `grep -c '^# ' corpus/README.md` → `1`
   - `python3 -B reports/round-28/readme/sweep.py` → exit 0, `rows 223 files 223`, footer ok
   - `sha256sum corpus/README.md` → the variant digest above
3. If C lands in the same apply: repeat with `224` / footer `25/26/26/29/24/94`, and confirm H1 count is still `1`.
4. File the close of `R36-README-DUPLICATE-HEADING` in the r48 successor with the applied sha and the grep/sweep outputs (F-Ca07-2). Do not edit the pinned r40 parent.
5. Do not fold F-Ca07-1 (duplicated rev-2.0 header) into this act without a separate row.

## 9. Commands run (reproducibility)

All from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; no network, no git mutation, no in-tree `run-validation.py`.

```
sha256sum corpus/README.md
git rev-parse HEAD                     # a01405dd36367292255c2652ac0a601f4cd6a0af
git status --porcelain -- corpus tools # empty
grep -n '^# ' corpus/README.md
grep -c '^# kotodama-shokunin corpus index' corpus/README.md
grep -n '^## \|^revision: \|^Total knowledge entries\|^Counts checked' corpus/README.md
find corpus/knowledge -name '*.md' | wc -l          # 223
for d in linguistics myth-symbol culture-material synthesis verification civilizations; do
  printf '%s ' "$d"; ls corpus/knowledge/$d/*.md | wc -l; done
python3 -B reports/round-28/readme/sweep.py --selftest
# staged copies (scratch only):
python3 - <<'PY'   # delete line index 2 → .scratch/ca07/README.A.md; delete lines 2-3 → README.B.md
PY
diff -u corpus/README.md .scratch/ca07/README.A.md
python3 - <<'PY'   # import sweep.py; sweep(head), sweep(fixed), sweep(planted 2nd H1); Counter line diff; ordered row equality
PY
sha256sum reports/round-40/op/defect-queue-v2.json  # dfc9265d…
grep -rn 'DUPLICATE-HEADING' reports/round-4[4-7]/ | head
python3 - <<'PY'   # read defect-queue-v2 successor files; enumerate rows
PY
```

## 10. Limits

- My byte staging ran before W02/Ca03 landed. I reconciled afterwards: `W02-landing-spec.md` §2 specifies the same B edit (`sed '3,4d'`, 573 lines, `d407260d…`) and `Ca03-readme-verify.md:145-146` stages the same two digests. Agreement is independent (different scratch directories, same live bytes), but the reconciliation is post-hoc; if Ca01 later proposes a third variant, only A and B are certified here.
- The combined 224 state is proven structurally with a stub entry, not with C's bytes; `8f5d2651…` is a fixture digest, not a prediction.
- No post-apply `validation.json` exists yet; the sweep after the real apply is the delivery certificate, not this report.
- I did not re-review the r47 over-build disposition (Ca02/Ca04/N02 own that half of the claim); no assumption about it is made here.
