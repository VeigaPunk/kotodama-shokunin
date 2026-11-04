# MutationCounter — round 89 w1 — mutation probe of the frozen counter

Target: `reports/round-89/measure89.py` sha256 `6bc14bcd541239e7d969d74291af46193fca7ac2e46850c40dc420d777cdf040` (verified at start and end of the run; lane bytes were not touched).
Detectors: (a) the mutant's own `--selftest --work <scratch>`; (b) an unmodified copy of `controls89.py` (sha256 `9ccd4eae…af6e`), run as `--lane <scratch --shared clone of the lane at 9ad00be1, worktree holding the mutant at reports/round-89/measure89.py>`.
Kill rule: selftest rc≠0, or controls rc≠0 / any `MISMATCH` line.
Isolation: each of the 45 mutants got its own `git clone --shared` under `/fast/scratch/hyaku/kotodama-r89/MutationCounter/m/<id>/lane`, with the toplevel asserted. The work ran 8 at a time. Scratch is now deleted.

## Baseline / restoration evidence
| bytes | selftest | controls |
|---|---|---|
| pristine (6bc14bcd…) | rc=0, `SELFTEST: PASS 21/21` | rc=0, 9/9 MATCH |
| restored (copy of M01's clone, rewritten to pristine bytes) | rc=0, `SELFTEST: PASS 21/21` | rc=0, 9/9 MATCH |

All 45 clones were rewritten to pristine bytes after mutation. `sha256sum` printed `6bc14bcd…` 45 times. `controls-pristine.txt` and `controls-restored.txt` are byte-identical (a7d5cad1…), and so are `selftest-pristine.txt` and `selftest-restored.txt` (38ec0b44…). Each mutant's sha256 is in `mutants.patch` and `results.json`.

## Result table
Exposure is the input that shows the mutant. "Exposed" means I ran it in `expose.py`: the pristine counter FAILs the leg, or refuses, and the mutant PASSes it on the same fixture lands. For each probe the fixture is the selftest fixture (`fx_clean`) with one change.

| mutant | leg | killed-by | survived | exposure input (pristine → mutant) |
|---|---|---|---|---|
| M01 FROZENCFG compares claims.json only, not the counter | FROZENCFG | — | **yes** | lands edits `reports/round-89/measure89.py` (comment appended): rc1 FROZENCFG FAIL → rc0 PASS 5/5 |
| M02 FROZENCFG always passes | FROZENCFG | selftest (cfgdrift F,C) | no | — |
| M03 ADVANCED `>=` → `>` | ADVANCED | selftest (clean F) | no | — |
| M04 lower date bound (as_of+90d) dropped | ADVANCED | — | **yes** | S001 recheck 90d→2026-11-10, lesson line matches: rc1 → rc0 |
| M05 upper date bound (as_of+366d) dropped | ADVANCED | — | **yes** | S001 recheck →2030-01-01: rc1 → rc0 |
| M06 LOCATED/not-NOT-LOCATED filter dropped | BACKED lesson line | — | **yes** | S001 line says `NOT-LOCATED recheck 90d→2027-05-03 …`: rc1 → rc0 (a NOT-LOCATED row gets advanced) |
| M07 `recheck old→new` relaxed to `→new` | BACKED recheck | — | **yes** | line `recheck 60d→2027-05-03` (wrong old value): rc1 → rc0 |
| M08 access date not required on lesson line | BACKED access date | — | **yes** | S001 line without `2026-11-04`: rc1 → rc0 |
| M09 max-25-words bound dropped | BACKED quote bounds | — | **yes** | 30-word quote, present in capture with sha updated: rc1 → rc0 |
| M10 min-20-chars bound dropped | BACKED quote bounds | — | **yes** | quote `"evidential"` (10 chars): rc1 → rc0 |
| M11 uncommitted capture read as `b''` | BACKED capture presence | — | yes (**equivalent**) | probe: capture removed, manifest sha256 = sha256(b''). Both versions give rc1 BACKED FAIL, because `contains(b'', q)` is false for every quote that passes `quote_ok`. Only the reason string changes |
| M12 sha256 check dropped | BACKED sha | — | **yes** | capture edited after hashing, quote still present: rc1 → rc0 |
| M13 http_status check dropped | BACKED http_status | — | **yes** | manifest `http_status: 404`: rc1 → rc0 |
| M14 fetched_at check dropped | BACKED fetched_at | — | **yes** | `fetched_at: 2026-10-01T…`: rc1 → rc0 |
| M15 manifest url check dropped | BACKED url_ok | selftest (badurl) | no | — |
| M16 wayback prefix not required (`endswith` only) | BACKED url_ok | — | **yes** | manifest url `https://evil.example/https://example.org/a`: rc1 → rc0 |
| M17 word-boundary padding dropped in `contains` | BACKED contains | — | **yes** | quote `"idential suffixes mark how the speaker knows"` against capture text "evidential suffixes…": rc1 → rc0 |
| M18 quote-in-capture check dropped | BACKED contains | selftest (wrongquote) + controls (F-wrongcapture MISMATCH) | no | — |
| M19 DISPOSED always passes | DISPOSED | selftest (undisposed) | no | — |
| M20 any line naming the id counts as disposed | DISPOSED | — | **yes** | `- S002 pending review` instead of NOT-LOCATED: rc1 → rc0 |
| M21 non-population recheck drift not checked | OTHERCELLS | — | **yes** | non-population S003 recheck 90d→2027-05-03: rc1 → rc0 |
| M22 deleted base row skipped (length/None check dropped) | OTHERCELLS | — | **yes** | S003 row deleted from SOURCES.md: rc1 → rc0 |
| M23 min_bytes dropped | ENTRY bytes | — | **yes** | complete entry under 200 bytes (headings, keys, 5-row table, S004): rc1 → rc0 |
| M24 min_headings −1 | ENTRY headings | — | **yes** | entry with 4 `## ` headings: rc1 → rc0 |
| M25 header keys not required | ENTRY keys | — | **yes** | `- recheck:` header removed: rc1 → rc0 |
| M26 absent-at-base not required | ENTRY absent-at-base | — | **yes** | fixture base already holds the entry: rc1 → rc0 |
| M27 table row minimum dropped | TABLE | — | **yes** | table with 3 data rows: rc1 → rc0 |
| M28 tier C admitted | NEWIDS tier | — | **yes** | S004 tier C: rc1 → rc0 |
| M29 status mined not required | NEWIDS status | — | **yes** | S004 status `pending`: rc1 → rc0 |
| M30 opened==as_of not required | NEWIDS opened | — | **yes** | S004 opened 2026-10-19: rc1 → rc0 |
| M31 used-by not required | NEWIDS used-by | — | **yes** | S004 used-by `—`: rc1 → rc0 |
| M32 unregistered cited ids tolerated | NEWIDS fabricated | selftest (fakeid) | no | — |
| M33 new_ids_min dropped | NEWIDS min | — | **yes** (leg-level only) | entry cites only base ids (S004→S001): NEWIDS FAIL → PASS. The claim still FAILs (rc1 both) because GATE/CAPTURE need `bool(qual)`, so the verdict is masked and only the leg line changes |
| M34 gate line needs no row URL | GATE | — | **yes** | S004 gate line without URL: rc1 → rc0 |
| M35 gate line needs no as_of | GATE | — | **yes** | gate line says `accessed today`: rc1 → rc0 |
| M36 CAPTURE ignores cap_bad | CAPTURE | selftest (nocapture) + controls (C-gate-no-capture MISMATCH) | no | — |
| M37 index tool read from lands, not freeze | INDEX freeze-pin | selftest (stubtool) | no | — |
| M38 README row not required in INDEX verdict | INDEX row | — | yes (**equivalent**) | the tool only runs `if tool is not None and row_ok`, so `rc == 0` implies `row_ok`. Probe (README says "See also \`fx.md\`." and has no row): both versions FAIL INDEX |
| M39 tier cell dropped from APPENDONLY set | APPENDONLY | selftest (oldrow) | no | — |
| M40 source cell dropped from APPENDONLY set | APPENDONLY | — | **yes** | base S003 source URL rewritten: rc1 → rc0 |
| M41 `lands == base` refusal removed | refusal | — | yes (**equivalent**) | when lands==base, the freeze must lie on base's chain, yet the freeze's claims.json names base. That is a hash cycle, so the first-parent refusal always fires instead. Probe: rc2 both (the reason text differs) |
| M42 freeze-on-chain refusal removed | refusal | — | **yes** | lands built on a sibling commit that holds identical claims/counter bytes but is not the freeze: rc2 refused → rc0 PASS 5/5 |
| M43 LEGCOUNT refusal removed | refusal | selftest (refuse-legcount) | no | — |
| M44 HEX40 syntax gate removed | refusal | — | yes (**equivalent in this SHA-1 lane**) | `rev-parse` output must equal the argument byte-for-byte, so non-lowercase-40-hex is still refused. Probe with an uppercase sha: rc2 both. It would only differ in a SHA-256 object-format repo |
| M45 `--first-parent` dropped | refusal | — | **yes** | lands = merge whose first parent is side work off base, with the freeze reachable only as second parent: rc2 → rc0 PASS |

## Totals
- 45 semantic mutants covering every requested leg and sub-check.
- **Killed: 10** (M02 M03 M15 M18 M19 M32 M36 M37 M39 M43). The selftest killed all 10; the controls killed only 2 (M18, M36).
- **Survived: 35.** Of these, 4 are equivalent (M11, M38, M41, M44) and 31 are not. Every one of the 31 was exposed by a concrete fixture input (expose.json). That is 30 with a full false PASS (29 rc1→rc0, plus M42/M45 rc2→rc0) and M33 at leg level only.
- Mutation score over non-equivalent mutants: 10/41 = 24%. Controls alone: 2/41.

## Findings (coverage only, not contract changes; the frozen predicate, counter and controls are unchanged)
1. Each leg's detector pins only one sub-check. The selftest has one negative scenario per leg, so whichever sub-check does not trip that scenario can be deleted without notice. This covers most BACKED sub-checks (lesson-line filter, old→new, access date, both quote bounds, sha, http_status, fetched_at, wayback prefix, word boundary), every NEWIDS row check except "fabricated", ENTRY bytes/keys/absent-at-base, the TABLE row floor, GATE url/date, and OTHERCELLS non-population/deleted rows.
2. **M01:** FROZENCFG's check of the counter's own bytes is untested. A lands that rewrites `measure89.py` is caught only by that check, and no scenario edits the counter.
3. **M42/M45:** the chain refusal is untested. `refuse-base` is refused before it reaches the chain check, and the fixture has no off-chain or merge lands, so either refusal mutant turns rc2 into a false PASS.
4. controls89.py is a regression check for claim-level outcomes, not a per-check detector. It killed only the mutants that remove the final quote/capture comparison.
5. In the pristine counter, the M33 behaviour also masks NEWIDS-min failures at the verdict level: GATE/CAPTURE fail whenever `qual` is empty. That is not a defect in the predicate, only an observation.

## Paths written
- `.ufo/waves/round-89/w1/MutationCounter.md` (this file)
- `.ufo/waves/round-89/w1/stage/MutationCounter/`:
  - `drive.py`: mutant table and driver
  - `expose.py`: survivor probes
  - `results.json`: per-mutant detector outputs, hashes and restore evidence
  - `expose.json`
  - `mutants.patch`: unified diff per mutant with mutant sha256
  - `controls-pristine.txt`, `controls-restored.txt`
  - `selftest-pristine.txt`, `selftest-restored.txt`

## Observed commands (rc)
- `sha256sum reports/round-89/measure89.py controls89.py`: rc0 (6bc14bcd…, 9ccd4eae…), both at start and at end
- pristine `measure89.py --selftest --work …/base/st`: rc0, 21/21
- pristine `controls89.py --lane …/base/lane --work …/base/cw --out …/base/out`: rc0, 9/9 MATCH
- `J=8 python3 -B drive.py` (45 mutants × {selftest, controls}): rc0; driver results as tabled above
- `python3 -B expose.py`: rc0; sanity clean F rc0 PASS 5/5 and clean C rc0 PASS 8/8; probe outcomes as tabled
- restored-bytes `--selftest`: rc0, 21/21; restored-bytes `controls89.py`: rc0, 9/9 MATCH
- `rm -rf /fast/scratch/hyaku/kotodama-r89/MutationCounter`: see summary

Tools installed: none. No lane production files, git refs or commits were touched.

## Unresolved defects
- 31 non-equivalent survivors (listed above). These are coverage gaps in the selftest/controls and need L1's decision. I did not amend the counter, predicate or controls.
- The known-survivor forged-capture controls (F, C) still PASS under the pristine counter, as declared in claims.json `bounds`.
