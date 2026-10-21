# ScoutLessonsIndex — round-50 falsify: lessons index vs `corpus/lessons/round-50.md`

Seat: `KotodamaR50-2.ScoutLessonsIndex-21` (leaf; no delegation, no lane writes).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Landed commit under attack:
`1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All runs in a private clone (`/tmp/scout-li-clone`, `GIT_CEILING_DIRECTORIES=/tmp`, deleted after);
no lane file, index, jj state or git index touched.

## Verdict

**BROKEN.** The lessons-index reconciliation the round evidences **did not land**, and the landed
"ready-to-apply" diff is both **stale** (its `round-50.md` pin is a 15-line placeholder) and
**not directly appliable** (absolute diff headers). At the landed bytes the audit is red:
`findings: 3`, exit 1 — the same count as base, with one *extra* unindexed file.

This is a bookkeeping/operability defect, not a false claim inside `reports/round-50/`:
`validation.json` (untracked in the lane, see F4) never mentions the lessons index, and no round-50
claim declares it. The false statement lives in the landed revision-5 diff text itself.

## Evidence

### 1. README is byte-identical base → landed

```
$ git -C /tmp/scout-li-clone rev-parse 4ad2683:corpus/lessons/README.md 1c779e4a:corpus/lessons/README.md
187b273362d6699ca8e4b1337078b9c74f47df77
187b273362d6699ca8e4b1337078b9c74f47df77
```

Only `corpus/lessons/round-50.md` (77 insertions) landed under `corpus/lessons/`:
`git diff --stat 4ad2683 1c779e4a -- corpus/lessons/` → `round-50.md | 77 +`.

### 2. Audit at the landed commit — exit 1, 3 findings

```
$ cd /tmp/scout-li-clone && python3 -B reports/round-25/audit/c31-lessons-index-audit.py
index present: True
lesson files:  36
index rows:    34
queue rows:    78
formats:       {'gate-keeper': 23, 'fragment-index': 5, 'plain': 8}
  FAIL C31_index_rows_eq_files
  PASS C32_owners_resolve
  PASS C33_formats_documented
  FAIL C34_pins_rederived
  PASS C34c_shape_cells_rederived
  FAIL C34b_prose_arithmetic
findings:      3
  C31-1 unindexed-file: ['round-49-verifier-spotcheck.md', 'round-50.md']
  C34-1 pin-drift: [('round-49.md', 'bytes', '35993', 39223), ('round-49.md', 'lines', '293', 317), ('round-49.md', 'sha8', '272eab2e', '51ab6a5c')]
  C34-2 prose-arithmetic-drift: {'table_rows_vs_files': {'stated': [34, 34], 'measured': [34, 36]}}
EXIT=1
```

Base (`4ad2683`) for comparison — also 3 findings, but `C31-1` names only
`round-49-verifier-spotcheck.md` and `C34-2` measures `[34, 35]`. The round therefore converted a
2-file/2-row gap into a 2-file/2-row gap **plus** one more unindexed file
(`round-50.md`), while leaving both by-hand prose passages stale.

Lesson bytes measured at landed (authoritative pins):
`round-50.md` = **bytes=11814 lines=77 sha8=d67969bf**;
`round-49-verifier-spotcheck.md` = **1880 / 17 / b1169c50**;
`round-49.md` = **39223 / 317 / 51ab6a5c** (matches the audit's `live` census).
`ls corpus/lessons/*.md | wc -l` = 36, `find ... -name '*.md' | wc -l` = 36.

### 3. The landed revision-5 diff, applied verbatim, still exits 1

The diff is tracked in the landed commit:
`1c779e4a:.ufo/waves/round-50/build/ReviewLessonsIndex-revision5.diff`, 76 lines,
sha256 `c4c3e6f0ea81b992…` (working copy byte-identical).

- **Not appliable as stored**: `patch -p0 --dry-run` on the landed README prints
  `can't find file to patch at input line 3 … 5 out of 5 hunks ignored`, exit 1 — the headers are
  absolute (`--- /home/vgpnk/…/corpus/lessons/README.md`, `+++ /tmp/rli-r50.NYRfPn-sim/…`), and the
  `+++` target is a 930 MB simulation tree the build seat's own report calls deletable
  (`.ufo/waves/round-50/build/ReviewLessonsIndex.md` §5). "Ready-to-apply" is not true from the repo root.
- **After header rewrite** (`---`/`+++` → `corpus/lessons/README.md`): applies cleanly, then

```
index rows: 36   lesson files: 36   queue rows: 78   formats: 23/5/8
  PASS C31  PASS C32  PASS C33  PASS C34b  PASS C34c
  FAIL C34_pins_rederived
findings: 1
  C34-1 pin-drift: [('round-50.md','bytes','499',11814), ('round-50.md','lines','15',77), ('round-50.md','sha8','420b1b0b','d67969bf')]
EXIT=1
```

The diff's own sentence — "On these revision-5 bytes it exits 0 with findings 0" (diff line 72-73) —
is **false**. The build seat knew: `ReviewLessonsIndex.md` §3 says "Its round-50 row holds fixture
pins (`bytes=499 lines=15 sha8=420b1b0b`) and must be replaced with the final measured values."
The placeholder was never replaced, and the README edit was never made.

- **With the pin corrected to the landed bytes** (and nothing else changed): `findings: 0`,
  `EXIT=0`, all six checks PASS; `--selftest` is `28/28`, exit 0 on both the landed and patched bytes.

### 4. Exact requirement at landed bytes

A single README patch, seven hunks' worth, is necessary and sufficient (validated: exit 0):

| # | landed line | change |
|---|---|---|
| 1 | `corpus/lessons/README.md:40-41` | `# 33 (2026-10-19)` → `# 36 (2026-10-21)` in **both** annotation lines (`ls` and `find`) |
| 2 | `:104` | re-pin round-49 row in place: `bytes=35993 lines=293 sha8=272eab2e` → `bytes=39223 lines=317 sha8=51ab6a5c` |
| 3 | after `:104` | **add** `\| `corpus/lessons/round-49-verifier-spotcheck.md` \| plain \| 0/4 \| none (the adjudication names no open item id) \| `corpus/lessons/round-49.md` (the adjudicated lesson; outside-review record) \| bytes=1880 lines=17 sha8=b1169c50 \|` |
| 4 | after that | **add** `\| `corpus/lessons/round-50.md` \| gate-keeper \| 4/4 \| none (fixture) \| `reports/round-50/claims.json` \| bytes=11814 lines=77 sha8=d67969bf \|` |
| 5 | `:106` | `**Rows: 34. Files: 34.**` → `**Rows: 36. Files: 36.**` |
| 6 | `:255-258` | `Of the 33 index rows` → `Of the 36 index rows`; `the three that carry none` → `the six …` listing round-1-gates, round-25, round-49, round-49-verifier-spotcheck, round-50 and the README self-row (verified: 36 rows, **30** carry Q ids, **6** carry none) |
| 7 | `:354` + EOF | roll-call `revisions 4 and 5 appended below (rounds 49 and 50)`; append the revision-5 block **with the corrected pin** |

`round-50.md` classifies `gate-keeper` (exact `## Gate` heading) with contract **4/4** — the shape
cells `gate-keeper | 4/4` in the diff are correct; only the pins are wrong. An in-place re-pin
(never a second row) is required for round-49: a duplicate row trips `C31-3` and `C34-2`.

### Secondary findings

- **F1 (operability, medium).** `--json` exits **0** while reporting the 3 findings; the default
  run exits 1. Any receipt-based gate that reads the `--json` exit sees green on a red index.
  Confirmed serially on clean landed bytes: `JSON_EXIT=0, findings 3 / DEFAULT_EXIT=1`.
- **F2 (calibration, low).** `ReviewLessonsIndex.md` F2 — "No `*.py` file in the lane references
  `c31-lessons-index-audit`" — is false: `reports/round-33/run-validation.py:49` defines `C31` and
  `:1185-1193` runs it as O1/O2 with exit-code gating. True narrower statement: round 49 and round 50
  runners do not invoke it (`grep -n 'c31\|lessons' reports/round-50/run-validation.py` → no hits),
  so this round's red index is off its acceptance surface.
- **F3 (accuracy, low).** The revision-5 diff leaves §3's histogram (`README:126-157`, "Total 33")
  and revision 4's tail line (`README:460-462`, "plain 7 (total 34)") untouched, and records no new
  live histogram. Live after the fix: `23/5/8 (36)`. The audit does not check these (build report F4);
  the smallest complete fix adds one line to the revision block, which I validated in the
  corrected patch (`**Live histogram after this revision:** gate-keeper 23, fragment-index 5, plain 8 (total 36).`).
- **F4 (coverage, medium, adjacent).** `reports/round-50/validation.json` does **not** exist at
  `1c779e4a` (`git cat-file -e 1c779e4a:reports/round-50/validation.json` → fatal); it exists only as
  an untracked working-tree file (30 003 B, mtime 13:32). Yet `corpus/lessons/round-50.md:3` names it
  as the "acceptance receipt". The proposed index row correctly points at `claims.json`, so the row
  pin is unaffected — but the lesson's `source:` line forward-references a file the commit does not carry.
- **F5 (wording, info).** Revision block: "This revision writes this file and adds the round-50
  lesson file" — a README revision cannot add a file; the lesson landed separately in the same commit.

## Smallest fix

Apply hunks 1–7 above (equivalently: the landed diff with two edits — round-50 pin
`499/15/420b1b0b` → `11814/77/d67969bf`, optional live-histogram line), then run
`python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → `findings: 0`, exit 0, and
`--selftest` → 28/28. Do not gate on `--json`'s exit; gate on `findings` or the default exit.

## Confidence and gaps

High confidence in every measured number above (re-run in-clone at the landed SHA; base re-measured
for the "3 findings" claim). Not evaluated: whether the round-50 builder intended the diff to be
applied at all (the seat report calls its pins fixtures, which supports "not applied by design"), and
whether any later round-close step owns the index. The round-50 receipt is untracked, so its
`acceptance_passed` flag could not be treated as a landed claim.
