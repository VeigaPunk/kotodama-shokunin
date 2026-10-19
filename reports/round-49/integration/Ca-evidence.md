# R49 claim Ca evidence — README revision-stub removal + sibling control

Agent: R49Revisions. Worktree: kaika/kotodama-shokunin, base c42d675be96b6b3957e6e5c00ab192080cb70083.
All commands run with `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, `python3 -B`.

## Edit made

Deleted `corpus/README.md` lines 55–56 (pre-fix numbering): the truncated duplicate
stub `revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten`
plus its following blank line. The full rev-2.0 changelog record (entry list, totals
vector, sweep receipt) was the block beginning at line 57 and is retained — it now
starts at line 55. No other byte changes.

Note on `reports/round-49/targets.json:137`: its "delete the second block" wording is
inverted relative to the file — the second block is the substantive record, the first
is the dangling half-sentence stub. Deleted the stub, not the record (confirmed with
R49Critic; flagged for scribe).

## BEFORE (base c42d675, README sha256 756647a085d9665a928ad886a2b9abcab56b2dff5b3aed82fa8df0018015f411)

`grep -c '^revision: 2\.0' corpus/README.md` → `2`

`grep -n '^revision:' corpus/README.md` →
```
3:revision: 2.5 — Round-48 culture-material landing + index hygiene (2026-10-19):
15:revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
27:revision: 2.3 — Round-40 linguistics-partition expansion (2026-10-19): four
37:revision: 2.2 — Round-39 verification-partition expansion (2026-10-19): four
46:revision: 2.1 — Round-36 timekeeping-instruments landing (2026-10-19): the routed
55:revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten   <- stub, blank line follows
57:revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten   <- real block
84:revision: 1.8 — Round-28 counts-footer reconciliation (2026-10-18): the
104:revision: 1.7 — Round-27 register-strata landing (2026-10-18): the round-27 C
116:revision: 1.6 — Round-27 re-measurement (2026-10-18): the index was swept again
136:revision: 1.5 — Round-20 reconciliation (2026-10-18): every row re-measured
162:revision: 1.4 — Round-19 index refresh: the thin partitions gained ten new
172:revision: 1.3 — Round-10 index refresh: the thin partitions gained ten new
```

`python3 -B reports/round-28/readme/sweep.py` → exit 0:
rows 224 files 224; missing_from_index 0; topic_mismatch 0; orphan_rows 0;
header_drift {}; totals_line 224 totals_ok True; footer_ok True;
readme_sha256 756647a0…

`python3 -B tools/check-readme-heading.py` → exit 0:
h1_lines [1]; headings {"1": 1, "2": 7}; findings 0

## AFTER (fixed, README sha256 097c2910e91d72d98cd98c167dc2c3e2ef50b11e9a0b7c8271441c261f44c5d7)

`grep -c '^revision: 2\.0' corpus/README.md` → `1` (2 → 1)

`grep -n '^revision:'` → same 13 label lines minus duplicate: now 12 lines,
2.0 only at line 55; labels strictly non-increasing
[2.5, 2.4, 2.3, 2.2, 2.1, 2.0, 1.8, 1.7, 1.6, 1.5, 1.4, 1.3].

`git diff --stat corpus/README.md` → `1 file changed, 2 deletions(-)` (0 insertions).
Diff hunk: removed `revision: 2.0 … the ten` + blank line; nothing else.

`python3 -B reports/round-28/readme/sweep.py` → exit 0 (identical verdicts;
readme_sha256 now 097c2910…).

`python3 -B tools/check-readme-heading.py` → exit 0, findings 0. File untouched.

## New control: tools/check-readme-revisions.py

Sibling of check-readme-heading.py (same argparse/--readme/--json/--selftest shape,
receipt style, exit map 0 clean / 1 findings / 2 could-not-evaluate). Check legs:
REVISION-DUP (label uniqueness, all lines reported), REVISION-STUB (revision line
immediately followed by blank line or EOF), REVISION-ORDER (labels non-increasing
top-to-bottom — enabled because the current README is strictly decreasing).
Advisory warning legs (reported, never counted in `ok` — pre-existing debt must
not turn this round's required green verdict red): REVISION-ORPHAN (a whole
paragraph inside the revisions span not headed by `revision:`) and REVISION-GAP
(skipped minor within one major). Fence-aware like the heading control.

Run on fixed README → **exit 0**:
```
readme …/corpus/README.md
sha256 097c2910e91d72d98cd98c167dc2c3e2ef50b11e9a0b7c8271441c261f44c5d7
revision_lines [3, 15, 27, 37, 46, 55, 82, 102, 114, 134, 160, 170]
labels ["2.5", "2.4", "2.3", "2.2", "2.1", "2.0", "1.8", "1.7", "1.6", "1.5", "1.4", "1.3"]
findings 0
warnings 1
  REVISION-ORPHAN lines=[69, 80] unheaded paragraph inside revisions span
    (starts 'round-28 C entry landed (`linguistics/register-lexicon-ceili…')
```

Run on pre-fix bytes (`git show HEAD:corpus/README.md > .scratch/r49/README-base.md`,
sha256 756647a0…) → **exit 1**:
```
findings 2
  REVISION-DUP lines=[55, 57] revision label '2.0' repeated
  REVISION-STUB lines=[55] revision '2.0' at line 55 has no changelog body
warnings 1
  REVISION-ORPHAN lines=[71, 82] (same detached rev-1.9 body, base numbering)
```

Missing file (`--readme .scratch/r49/does-not-exist.md`) → **exit 2**, JSON
`{"ok": null, "error": "FileNotFoundError(2, …)"}`.

`--selftest` → **exit 0**, 11/11 PASS, 0 skips:
1. clean revision list passes; 2. duplicate label flagged at [1, 4];
3. truncated stub flagged (DUP + STUB); 4. EOF stub flagged;
5. increasing order flagged (REVISION-ORDER); 6. fenced `revision:` ignored;
7. absent revision lines passes; 8. missing file exits 2;
9. base c42d675 README flagged — the real r49 defect produces REVISION-DUP
   lines=[55,57] and REVISION-STUB line 55 (fixture read via
   `git show c42d675…:corpus/README.md`; SKIP not FAIL if object unreachable);
10. orphan paragraph warns at [4, 5] while verdict stays clean;
11. skipped minor warns (REVISION-GAP).

## Routed defect (out of Ca scope — NOT fixed this round)

R49Scout's git archaeology: revision 1.9's HEADER LINE was lost in round-35
ce103bf (which replaced it with the 2.0 block): `ce103bf^:corpus/README.md:3` =
"revision: 1.9 — Round-28 register-lexicon-ceiling landing (2026-10-18): the";
at ce103bf the header is gone and its body survives as the orphan paragraph
now at fixed-README lines 69–80 ("round-28 C entry landed (…"). The footer
still cites "Revision 1.9 moved"; `grep -c '^revision: 1\.9'` = 0 (ART dossier
D5, kotodama-art.md:382-385 noted the same). The 2.0 stub itself was born in
round-36 57c8409. Fix needs a new revision-header line — outside this claim's
2-deletion diff budget; surfaced durably as REVISION-ORPHAN by the new control
and routed to the planner for a later round.

## Mid-wave sweep note (not a Ca regression)

After R49Entry landed claim C (`culture-material/hunting-foraging-subsistence.md`,
untracked, not yet indexed), a late re-run of the sweep goes red with exactly the
expected pending-integration deltas: `rows 224 files 225`,
`missing_from_index 1 ['culture-material/hunting-foraging-subsistence.md']`,
header_drift culture-material declared 26 / files 27, footer totals 224 vs live
225 — all resolved when the integrator adds the README row + revision 2.6.
The Ca-verified post-fix sweep (exit 0, above) was measured before that landing;
README bytes are unchanged since (`readme_sha256` still 097c2910…).
