# ScribeReceipts — round 90 measurement and sources receipts

Seat: ScribeReceipts (w2, leaf, no dispatch). Lane: kotodama. Milestone r90-v2. Judged on calibration, coverage.
Revisions: BASE 6b0b86e45ae902331aca75863db380f2991458c4 · LANDS 7f3a7aa6615624afadc2cc2d2d4f7ad225f44761 · FREEZE d0b6f2a7f9cc36272682749a9b047b739406f0c8.
Full table, command list and paste-ready blocks: `.ufo/waves/round-90/w2/stage/ScribeReceipts/receipts.md` (repro script beside it: `receipts.sh`).

## Behavior

Read-only. Every number is from `git show`, `git archive` into scratch, or the counter run with `--work` in scratch. No production edit, no git write, no tool installed (none needed; `awk`, `gawk`, `sha256sum`, `python3`, `join`, `comm` already present).

## Findings (measured)

| measure | BASE | LANDS |
|---|---|---|
| registry rows | 865 | 873 (+8: S942–S949) |
| tier A / B / C | 511 / 329 / 25 | 517 / 330 / 26 |
| status mined / queued / rejected | 762 / 58 / 45 | 769 / 58 / 46 |
| pre-existing rows missing or cell-changed | — | 0 of 865 |
| knowledge files total / linguistics | 261 / 34 | 262 / 35 |
| new entry | — | 19,930 B, 128 lines, 3,134 words, 8 H2, one 4-column table of 5 data rows |
| census validate rc (archived revision, fleet-shaped tree) | 0 | 0 |
| census warning lines naming S942–S949 | 0 (start) | 0 (end); delta 0 |

Claim verdicts observed at LANDS with the freeze-pinned counter (revision 6, sha256 `6e1ea6a5…`): `MEASURE90-C: PASS legs=4/4`, `MEASURE90-O: PASS legs=6/6`. Tool sha256 `121888f0…` equals the claims pin. `SELFTEST PASS 67/67`, `MUTATION-SCORE: 43/43 killed, 0 survived, 0 broken-pattern`, 13 refusals `all ok`.

Checks that passed: 8/8 capture sha256 equal `manifest.json`; cell-compare negative control (one flipped status cell) detected; `claims.json` sha256 identical at FREEZE and LANDS; index tool unchanged BASE→LANDS and `CORPUS-INDEX: OK files=262 rows=262 findings=0`; census `census` mode counts agree with the awk histograms at both revisions.

## Discrepancies for L1 (not edited here)

1. `corpus/lessons/round-90.md` "Registry changes" says "six `mined`" for S942–S948; the registry has seven `mined` rows. Use 7.
2. `reports/round-90/census-end.txt` at LANDS has no `rc=` line and no header (36 lines); census-start has `rc=0` (39 lines). Warning bodies are identical. The rc in this report is from a re-run.
3. `measure90.py` is called frozen in `claims.json`, but LANDS bytes are revision 6 (sha256 `6e1ea6a5…`); freeze was revision 1 (`4091cda9…`). Revisions 2–6 are in `counter-revisions.md`, each marked "before any data", but the fleet report should name revision 6 and its hash.
4. Lesson seed-rot section names three tier-C Wikipedia seeds; only S949 has a registry row.

## Touched surfaces

- Written: `.ufo/waves/round-90/w2/stage/ScribeReceipts/receipts.md`, `.ufo/waves/round-90/w2/stage/ScribeReceipts/receipts.sh`, this report.
- Scratch only, removed on exit after copying outputs: `/fast/scratch/hyaku/kotodama-r90/ScribeReceipts/` (BASE and LANDS archives, fleet-shaped census trees, counter work dirs `work-C` and `work-O`). Kept outputs: `.ufo/waves/round-90/w2/stage/ScribeReceipts/outputs/`.
- Read only: `corpus/SOURCES.md`, `corpus/knowledge/linguistics/petitionary-and-votive-formulae.md`, `corpus/lessons/round-90.md`, `corpus/README.md`, `reports/round-90/*`, `tools/check-advance-evidence.py`, `tools/check-corpus-index.py`, `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`, `/home/vgpnk/Projects/shokunin/shokunin.conf`.

## Out of scope

- No freshness claim, no re-verification, re-dating or repair of any old registry row (freshness paused).
- No edit to the lesson, README, SOURCES, counter, or manifest. Discrepancies 1–4 go to L1 and the lesson author.
- Assimilation: none.
- Scholarly content of the entry was not re-checked; this report counts structure and registry binding only.

## Tool installs

None. Recorded per RULES: no `pacman`, `uv tool`, `npx` or binary install performed.

## Artifact paths

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-90/w2/stage/ScribeReceipts/receipts.md`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-90/w2/stage/ScribeReceipts/receipts.sh`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-90/w2/stage/ScribeReceipts/outputs/counter-O-lands.txt`, `counter-C-lands.txt`, `census-validate-B.txt`, `census-validate-L.txt`, `census-end.L.txt` (committed LANDS census-end bytes)
