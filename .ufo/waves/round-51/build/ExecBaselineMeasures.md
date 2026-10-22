# ExecBaselineMeasures — Round 51 attempt 3 baseline measurements

Seat: `KotodamaR51a3.ExecBaselineMeasures` (leaf executor)
Date: 2026-10-22
Claim base: `bff83ba65bf9559af4d7567e81703059667a0005` (sandbox clone at
`/fast/scratch/hyaku/kotodama-r51a3/ExecBaselineMeasures`, `git rev-parse --short HEAD` =
`bff83ba`). Copy of the lane's `reports/round-51/boundary-count.py`
(3768 bytes, copied from `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-51/boundary-count.py`)
installed at `reports/round-51/boundary-count.py` in the sandbox before the runs.
The one live-lane reader (sources-census.sh) is noted inline.

All measurements ran in the sandbox unless stated. Every command exited 0. No tools were
installed in this session (nothing was needed); versions recorded below.

## Measurements

1. Sources census (live lane, as assigned):
   `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`
   ```
   kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
   ```
   Exit 0. Census validates the live lane's `corpus/SOURCES.md`.
2. `find corpus/knowledge -name '*.md' | wc -l` → `226`, exit 0. Claim C before-state matches (226 -> 227).
3. `ls corpus/knowledge/linguistics/*.md | wc -l` → `25`, exit 0.
   Footer sweep below agrees (linguistics 25 before; 26 required after C).
4. `python3 -B reports/round-28/readme/sweep.py` → exit 0, footer `total 226`,
   `dir_totals [25, 26, 28, 29, 24, 94]`, `missing_from_index 0`, `orphan_rows 0`,
   `header_drift {}`, `totals_ok True`, `footer_ok True`, `footer_findings []`.
   Pre-state for the claim-C acceptance (`footer total 227 and linguistics 26` after).
5. `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit 0,
   `findings: 0`, all six C3x checks PASS.
6. `python3 -B tools/check-readme-revisions.py` → exit 0, `findings 0`, `warnings 1`:
   `REVISION-ORPHAN lines=[101, 112]` — an unheaded paragraph inside the revisions span,
   starting `round-28 C entry landed (linguistics/register-lexicon-ceili` (pre-existing;
   informational for the L1, not a failure of this round's counters).
7. `python3 -B tools/check-readme-heading.py` → exit 0, `findings 0` (h1 x1, h2 x7).
8. `python3 -B tools/check-claim-separability.py --selftest` → `selftest: 56/56 checks passed`,
   exit 0.
9. `python3 -B reports/round-51/boundary-count.py` → `rows=11 resolved=11 distinct=11`, exit 0.
   Claim D before-state matches (11 -> 15 required).
10. `wc -l corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` → `204`, exit 0.
11. `grep -c '^| S[0-9]' corpus/SOURCES.md` → `70`, exit 0. Registry rows S001–S070 (70 rows) at base; C's new rows start at S071 upward.

## Tool versions

- python3: `Python 3.14.8`
- git: `git version 2.56.0`
- jj: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`

No installs or updates performed; no pacman transactions attempted (host-wide pause respected).

## Result

All assigned baseline measurements ran successfully. All exited 0. Both declared
before-states reproduce exactly: D `rows=11 resolved=11 distinct=11`, C 226 knowledge
entries / 25 linguistics / SOURCES rows 70. The only non-clean output is the pre-existing
readme revision orphan warning (item 6), which does not affect any counter in this round.

## Unrun checks

None from the assigned list. No build/lint/test runs were attempted (editing wave in flight;
integration gate belongs to the L1).
