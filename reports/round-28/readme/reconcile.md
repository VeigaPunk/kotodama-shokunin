# R28-C47 — `corpus/README.md` reconciliation (round 28)

- **seat:** R28-C47 (C-readme). **lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  **assignment (verbatim):** "C R28-C47..C48 (README + audit): README reconciled;
  entry audits."
- **date:** 2026-10-18. **declared baseline:** `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`
  (`reports/round-28/claims.json`); **HEAD at measurement:** `69cecbc7dcf575a29f29660ecac470e05260fd86`.
  **measurement stamps:** 20:13:39Z (the footer correction, revision 1.8, 200
  files) and **20:20:50Z (final, after the C-ceiling entry landed and revision
  1.9 was integrated, 201 files)**. Both readings are carried below; the final
  one is binding.
- **canon:** NON-CANON engineering evidence. This seat admits no entry, judges no
  entry's quality or sources, touches no gate, ledger, or canon.
- **instrument:** `python3 reports/round-28/readme/sweep.py`
  (sha256 `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`
  at the final stamp; re-check the digest before quoting any reading below).
- **writes:** `corpus/README.md`, this file, `reports/round-28/readme/sweep.py`,
  and disposable scratch under `.scratch/`. No commit, no push.
- **counting command for this round:** `python3 reports/round-28/run-validation.py`.
  At the 20:13Z stamp its claim C reported exactly two failures, both the peer
  ceiling seats' in-flight deliverables (§3); **at the 20:20Z stamp claim C
  reports `failures: []`** — the entry landed, the amendment section is present,
  and the README indexes it with partition headers reproducing the tree.

## 0. Verdict at a glance

Final reading (20:20:50Z, revision 1.9, 201 files):

| # | requirement | measured | status |
|---|---|---|---|
| C47-a | counts command-carried against actual contents | `21/19/18/29/20/94` = **201 files**, two independent methods (§1) | done |
| C47-b | index rows == files | **201 rows vs 201 files**; 0 missing, 0 ghosts, 0 duplicates, 0 header drift, totals line 201 (§2) | done |
| C47-c | every row is its entry's own `- topic:` text | **0 topic mismatches**, the new ceiling row included (§2) | done |
| C47-d | the **counts footer** agrees with the tree | **defect found and repaired** at 20:13Z (it read 199/19 while the tree measured 200/20); final reading 201 / `21/19/18/29/20/94` (§3) | done |
| C47-e | receipts | this file + `verify.md` (independent re-measure) + `sweep.py` (fresh committed instrument, 12/12 controls, incl. 4 new footer controls) | done |

Pre-landing reading (20:13:39Z, revision 1.8, 200 files): 200 rows / 200 files,
0 mismatches, footer `200` / `20/19/18/29/20/94`. Both readings are
measurements; the final one is binding.

## 1. Counts, command-carried

Method 1 — the lane's own read-only inventory:

```sh
python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge
# totals.files = 201 (final); per-dir civilizations 94, culture-material 18,
# linguistics 21, myth-symbol 19, synthesis 29, verification 20
# at the pre-landing pin (20:13:39Z) the same command read totals.files = 200,
# linguistics 20
```

Method 2 — an independent plain-filesystem count:

```sh
for d in linguistics myth-symbol culture-material synthesis verification civilizations; do
  find corpus/knowledge/$d -maxdepth 1 -name '*.md' -type f | wc -l; done
# 21 19 18 29 20 94
find corpus/knowledge -maxdepth 2 -name '*.md' -type f | wc -l   # 201
```

Both agree at both pins. The vector moved 20 → 21 in `linguistics` when the
round-28 ceiling entry landed (17:20Z); the other five partitions are unchanged
from round 27's final reading.

## 2. The sweep — index rows vs the files they name

```sh
export TMPDIR=$PWD/.scratch
python3 -B reports/round-28/readme/sweep.py --selftest   # 12/12, exit 0
python3 -B reports/round-28/readme/sweep.py              # exit 0
# parts {"civilizations": 94, "culture-material": 18, "linguistics": 21,
#        "myth-symbol": 19, "synthesis": 29, "verification": 20}
# rows 201 files 201
# missing_from_index 0 []     topic_mismatch 0 []     orphan_rows 0 []
# header_drift {}             totals_line 201 totals_ok True
# footer {"date": "2026-10-18", "command": "python3 tools/source-audit-inventory.py ...",
#         "total": 201, "dir_totals": [21, 19, 18, 29, 20, 94]}
# footer_live {"total": 201, "dir_totals": [21, 19, 18, 29, 20, 94], ...}
# footer_findings [] footer_ok True
# readme_sha256 053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c
```

All legs clean. The `topic_mismatch 0` result is the one the round-10/19/20
convention turns on: each row's text is byte-equal to its entry's own `- topic:`
head text with continuation lines space-joined, never a condensed paraphrase.
The new `register-lexicon-ceilings.md` row was added in filename order by the
peer C seat (revision 1.9) and its text is byte-equal to the entry's own head.

## 3. The defect this round found — and why round 27's sweep went green over it

Round 27's sweep (`reports/round-27/readme/sweep.py`) checks the index rows,
section headers, row topics, ghosts, missing rows and the `Total knowledge
entries:` line. It does **not** read the counts footer at the end of the file.
That is where a live stale claim sat:

```sh
git show HEAD:corpus/README.md | sed -n '/^Counts checked/,+3p'
# Counts checked 2026-10-18 from the repo root:
# `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
# (total 199 files; directory totals 19/19/18/29/20/94).
```

Revision 1.7 (round 27) moved `## linguistics/` 19 → 20 and the totals line
199 → 200 **in the same file**, but left this present-tense footer reading
199/19. The footer carries the command that produces it, so the claim was
falsifiable and false: the command now returns `totals.files 200` and directory
totals 20/19/18/29/20/94.

**The fix (revision 1.8).** Two edits, 27 diff lines, nothing else touched:

| region | before | after |
|---|---|---|
| the revision block (new `1.8` prepended) | — | records the defect, the fix, and that round 27's sweep could not have caught it |
| the footer's `(total …; directory totals …)` | `199` / `19/19/18/29/20/94` | **`200`** / **`20/19/18/29/20/94`** |
| below the footer | — | the superseded 199/19 reading kept verbatim as the dated record it was |

**The instrument (round 28's sweep).** A new committed instrument was written
because the old one's blind spot is exactly the defect class found: it adds a
`footer` leg that parses the `Counts checked <date> …` block and compares both
its file total and its six-directory vector against the live tree, in the
README's own section order. Four new controls (on top of round 27's eight
inherited ones) prove the leg is neither always-red nor always-green:

| control | planted | expected |
|---|---|---|
| stale footer total | `199` against a 1-file tree | `FOOTER_TOTAL` fires, exit 1 |
| stale dir vector, matching total | total 1, vector `19/19/…` | `FOOTER_DIR_TOTALS` fires, `FOOTER_TOTAL` does not |
| absent footer | no `Counts checked` block | `FOOTER_ABSENT` fires (a missing footer is not a silent pass) |
| correct footer | total and vector both live | clean, exit 0 |

The control that matters most is the last: it shows the leg is not a hard-coded
red. Before the fix the live leg failed 11/12 with only the live reading red;
after the fix the selftest is **12/12** and the live run exits 0.

**The before/after control, on the same bytes.** The repair's own claim — that
the footer was stale and that round 27's instrument could not have caught it —
was tested by replaying both instruments over the committed `HEAD` bytes, which
still carry the defect:

```sh
export TMPDIR=$PWD/.scratch
git show HEAD:corpus/README.md > .scratch/r28-readme-before.md
python3 -B reports/round-28/readme/sweep.py --readme .scratch/r28-readme-before.md
# footer_findings [FOOTER_TOTAL 199 vs 200, FOOTER_DIR_TOTALS [19,19,18,29,20,94] vs [20,19,18,29,20,94]]
# exit 1
python3 -B reports/round-27/readme/sweep.py --readme .scratch/r28-readme-before.md
# rows 200 files 200; 0 missing; 0 topic mismatches; totals_ok True
# exit 0   <-- green over the defect: this is the blind spot, measured
python3 -B reports/round-28/readme/sweep.py --readme corpus/README.md   # exit 0 (fixed)
```

Round 27's sweep exits **0** on the exact bytes that carry the defect, while
round 28's exits **1**; after the fix both exit 0 on the working tree. That is
the instrument-difference claim demonstrated rather than asserted, and it is why
this round's sweep is a new committed file rather than a re-run.

**The landing, integrated.** The round-28 **C-ceiling entry**
(`corpus/knowledge/linguistics/register-lexicon-ceilings.md`) landed at 17:20Z,
after this seat's 20:13Z footer correction. It was indexed by the peer C seat
in revision 1.9: a new row in filename order (between
`politeness-taboo-euphemism.md` and `register-strata-attestation.md`) whose text
is byte-equal to the entry's own `- topic:` head, `## linguistics/` moved
20 → 21, the totals line 200 → 201, and the counts footer 200/`20/…` →
201/`21/…`. The final reading above is that state. The round-28 runner's claim C
measures the same dependency and now reports `failures: []`.

The sequencing is worth naming: this seat's 1.8 correction and the peer's 1.9
landing touched the **same two regions** (the revision stack and the counts
footer). The 1.8 block was preserved as a dated revision and the footer was
advanced rather than reverted — which is what this file's revision convention
requires, and what the sweep's `footer` leg verifies against the live tree at
the final stamp.

## 4. What did not change

The index rows, section headers and totals line were reconciled by round 27 and
reproduce exactly at both pins; the only row added is the round-28 ceiling
entry's own. This round's README work is the footer leg and its repair plus the
final 201-state reconciliation, not a re-landing of the index.

## 5. Limits of this receipt

- **Same-seat measurement.** `sweep.py` and this receipt are the same seat's
  work; the controls are planted, not an independent reader. Independent
  corroboration is the round-28 runner's own `corpus_readme` measurement, which
  reads `mismatches {}`, `names_the_entry true` and `total_files 201` from the
  delivered bytes.
- **Point-in-time.** The final reading is at 20:20:50Z, revision 1.9. The tree
  moves under the round; re-run the command before quoting any count.
- **Non-canon.** A reconciled index and a green structural sweep do not certify
  historical truth, and this seat admits nothing into the corpus.
