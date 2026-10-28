# MutCrows — wave-2 falsifier, claim C ROWS (round 77, hyaku run 10)

Seat: `MutCrows` (leaf, attack-only). Target: the ROWS leg of `ACCEPT-C-77`
(the wave-1 counter staged at `.ufo/waves/round-77/w1/stage/ExecAdaptC/accept-c.py`,
sha256 `5ac63e0d6630e8711aca7cceb159ee2b13c94b5a1bec4997afbdb3806826dca4`,
3303 lines — verified byte-identical to the lane stage copy before and after).
Named W1 artifacts attacked: ExecAdaptC's required change 2 ("ROWS counts only
`| S### |` additions inside the frozen row_set; required Paths/Search-log lines
… are checked by INDEX") and its selftest matrix rows `row-extra`,
`pre-row-edit`, `pre-row-rule2-cell`, `index-required-section`.

Method: the counter's own fixture machinery (`_st_build`/`_st_run`/`_st_commit`,
imported from my scratch copy) drives every probe — pristine build → mutated
build (mut dict or surgical edit + explicit commit) → restored build, with
sha256 of the lands `corpus/SOURCES.md` recorded at each step. The same
detector (the counter subprocess over a 40-hex lands) ran on all three states.
No lane file was read-write anywhere except this Report.

## Baseline (pristine) — conclusive before mutation

```
$ HYAKU_SCRATCH=/fast/scratch/hyaku/kotodama-r77/MutCrows \
  python3 -B accept-c.py --selftest
SELFTEST: 37/37            (exit 0)
```
All 37 CASE lines byte-identical to W1's committed
`…/stage/ExecAdaptC/selftest-receipt.txt` (`diff` of `^CASE` prefixes: no
output, CASE_LINES_IDENTICAL) — the borrowed harness did not drift.

Pristine fixture run (mut=None): `exit 0`, `ACCEPT-C-77: PASS legs=13/13`,
registry sha256 `555d0557ceffb555…` (full: `555d0557ceffb555` prefix of
`results.json`). The do-nothing `lands == freeze` control inside the selftest
stays FAIL 3/13 (data legs red, CENSUS/SCRATCHMIRROR/FROZENCFG green), and
`lands == base` is refused exit 2 — the detector is not vacuously green.

## Probes (expected per claim C ROWS vs actual)

| probe | mutant | expected | actual (raw verdict) | verdict |
|---|---|---|---|---|
| P0 | none (pristine) | PASS 13/13 | exit 0 `PASS legs=13/13` | baseline green |
| M1 | plant S-row outside row_set (`row_extra`: adds `| S006 |` line) | ROWS red only | exit 1 `FAIL legs=12/13`, fails exactly `{ROWS}` | **KILLED** |
| M2 | remove one wanted row (delete lands `| S005 |` line) | ROWS red | exit 1 `FAIL legs=9/13`, fails `{COLLCHECK, ENTRIES, REPOINTED, ROWS}` | **KILLED** (ROWS red; 3 co-reds are other legs' own contracts) |
| M3a | alter existing row outside rule-2 cells (`pre_row_edit`: S002 source cell) | ROWS red only | exit 1 `FAIL legs=12/13`, fails exactly `{ROWS}` | **KILLED** |
| M3b | control: rule-2 cell edit only (used-by extended) | PASS | exit 0 `PASS legs=13/13` | exemption holds |
| M4a | add non-row Paths/Search-log prose (extra `## Search log` bold line) | ROWS green | exit 0 `PASS legs=13/13` | r76 defect fixed |
| M4b | required section dropped (`drop_required_section`) | INDEX red, ROWS green | exit 1 `FAIL legs=12/13`, fails exactly `{INDEX}` | separation proven |

### Raw ROWS/INDEX failure lines

M1 (`LEG FAIL ROWS`): `row ids added ['S004', 'S005', 'S006'] (want the frozen
row_set ['S004', 'S005']); lands registry holds 6 row(s); 3+k with k=2 is 5`.
The planted out-of-set row is named in the detail; no other leg reacted.

M2 (`LEG FAIL ROWS`): `row ids added ['S004'] (want the frozen row_set
['S004', 'S005']); lands registry holds 4 row(s); 3+k with k=2 is 5; S005
missing at lands`. Co-reds, each from its own contract, not row-diff leakage:
ENTRIES `cites S005, which no landed row carries`; REPOINTED `source line for
S005 names a document its row does not carry`; COLLCHECK `S005 row missing at
lands (no source cell to compare)`.

M3a (`LEG FAIL ROWS`): `pre-existing row S002 changes cell(s) [1] outside the
rule-2 set`. M3b (same edit confined to `used-by`): PASS 13/13.

M4b (`LEG FAIL INDEX`): `required section 'Paths entry naming S897 and S898'
missing from corpus/SOURCES.md (0 < 1); required section 'Search-log entry for
round 77' missing from corpus/SOURCES.md (0 < 1)`. ROWS stayed green on the
same landing.

## Restoration evidence

Surgical probes (the only ones that mutate a built fixture):

- M2: pristine `555d0557ceffb555…` → mutated `f8527608250d2f8f…` → restored
  `555d0557ceffb555…`, `sha_match=True`; restored run `PASS legs=13/13`.
- M4a: pristine `555d0557ceffb555…` → mutated `332bd586ac969543…` → restored
  `555d0557ceffb555…`, `sha_match=True`; restored run `PASS legs=13/13`.

Non-surgical probes are rebuilt from the pristine builder with a mut dict;
pristine (P0) PASS brackets them. The fixture worktrees were verified clean
(`git status --porcelain` empty) before every hash, with
`git rev-parse --show-toplevel` asserted to the fixture dir before every
commit (builder asserts the same at init). Full hashes in
`/fast/scratch/hyaku/kotodama-r77/MutCrows/results.json` and raw stdout/stderr
per probe under `…/probe-outputs/` until scratch deletion, recorded below.

## Coverage finding

None. Every S-row-defect mutant was killed with ROWS in the failing set
(exactly `{ROWS}` for out-of-set addition and out-of-rule-2 alteration); the
non-row addition is invisible to ROWS and graded green; the required-section
defect reddens INDEX with ROWS green. The claim's ROWS/INDEX separation and
the r76 "ROWS predicate out-of-set non-row section additions" routed defect
both hold under these mutants. Observation, not a contract change: M2's
co-reds mean "ROWS red only" is true for the two single-cause S-row defects,
while row removal is intentionally over-determined (three sibling legs also
fire) — consistent with the counter's design, worth keeping in mind when
reading a lands-only failing set.

## Scope / hygiene

- Mutated only my scratch fixture copies; the lane stage counter and W1
  receipts were only read (sha256 unchanged, verified post-run).
- Installs: none. pacman: not run.
- Scratch `/fast/scratch/hyaku/kotodama-r77/MutCrows` (driver.py, accept-c.py,
  results.json, probe-outputs/, fx-*/ run-scratch/) deleted after this report;
  figures above are transcribed from the recorded outputs.
- No fleet-repo, sibling-lane, LOG/SCORECARD/SKILL/SHONEN/corpus/reports
  production file was written; the only lane write is this Report.

---
report: .ufo/waves/round-77/w2/MutCrows.md
