# CriticClauseListC — round 55, claim C, QUALITY criterion 11 pre-dispatch seat

Seat: non-author (authored none of the files below). Declaration `662239d2`, claim base `d44309a1`.
Read: `reports/round-55/claims.json` (C), `accept-c.py`, `criterion11-controls.py`,
`telemetry/criterion11-controls.txt`, `telemetry/declaration-dry-run.txt`, `corpus/QUALITY.md:39`,
`reports/round-28/readme/sweep.py`, `tools/check-source-access.py`, round-54 counterparts.
Scratch: `/fast/scratch/hyaku/kotodama-r55/CriticClauseListC/lane` (clone at `662239d2`). No lane writes other than this file.
Tools installed or updated: none.

## Verdict: DEFECTS (one blocking, one cosmetic)

The clause list covers every clause-bearing phrase of the statement, the before value is correct, and `accept-c.py` reads every exit status. But two of the SWEEP leg's three sub-predicates have no control that isolates them. Each can be deleted from `accept-c.py` and the declared builder still prints `CONTROLS 13/13 as expected`. The listed reason for RED-COUNT's SWEEP failure is also false.

## Findings

### 1. SWEEP's "exits 0" and "rows 231 files 231" are never shown able to fail on their own (blocking under criterion 11)

**Counterexample.** Two mutants of `accept-c.py`, each committed in the scratch clone and run through the declared builder (`python3 -B reports/round-55/criterion11-controls.py . HEAD`):

| mutant | edit to `accept-c.py:71-73` | builder result |
|---|---|---|
| M1 | drop `sweep.returncode == 0 and` | `CONTROLS 13/13 as expected` |
| M2 | drop `int(rows.group(1)) == TOTAL and int(rows.group(2)) == TOTAL` | `CONTROLS 13/13 as expected` |
| M5 (sanity check that the method can fail) | drop `and not spans` | `RED-RANGE-SPAN: exit 0 … NOT AS EXPECTED`, `12/13` |

Two other mutants are equivalent, so they are not defects. Dropping the SET leg's `len(live) == TOTAL` is harmless because the count is implied by `added == [ENTRY]` and `removed == []` over a 230-path base. Dropping SWEEP's `missing_from_index == 0` is harmless because sweep.py's `ok` already requires no missing rows (`sweep.py:191-194`). M1 and M2 are not equivalent; the probes below show live states where each conjunct is the only thing that fails.

**Why RED-COUNT doesn't test the 231 pin.** `claims.json:28` says "SET and SWEEP fail together, because both pin 231". In the RED-COUNT copy the controls script adds only the README row (`criterion11-controls.py:91-96`). The header, totals line and footer are left in their 231 state, so sweep.py exits 1 for drift reasons. Probe output for that copy:

```
sweep exit 1; rows 232 files 232; missing_from_index 0
header_drift {'myth-symbol': {'declared': 27, 'files': 28}}; totals_line 231 totals_ok False
footer_findings FOOTER_TOTAL 231 vs 232, FOOTER_DIR_TOTALS …27… vs …28…
```

So SWEEP fails through `returncode`, not the pin. That is why M2 survives. RED-SWEEP (`criterion11-controls.py:104-106`) changes exit status and `missing_from_index` together (exit 1, missing 1), so M1 survives too.

**The near-misses exist and fail one leg as required** (scratch probe, `accept-c.py` unmodified):

- PROBE-COUNT-CONSISTENT: a second `.md` file plus a README that is fully consistent with 232 files (`## myth-symbol/ (28)`, `Total knowledge entries: 232.`, footer `(total 232 files; directory totals 28/28/29/29/24/94).`). Sweep.py exits 0 with `rows 232 files 232`, and accept-c fails SET and SWEEP. Here SWEEP fails only through the 231 pin.
- PROBE-FOOTER-STALE: the green copy with the footer left at `(total 230 files; directory totals 28/26/29/29/24/94).` This is the round-28 defect class that sweep.py exists to catch. Sweep.py exits 1 with `rows 231 files 231` and `missing_from_index 0`, and accept-c fails SWEEP alone.
- PROBE-TOPIC-DRIFT: the entry's README row topic is one word off. Sweep.py exits 1 with `topic_mismatch 1` and rows 231, and accept-c fails SWEEP alone.

**Impacted axes.** Coverage: claim C's SWEEP leg and clauses C-count and C-index. Under criterion 11, "a clause with no control is unverified, not passing." This is inherited, not an adaptation regression: `reports/round-54/criterion11-controls.py` has the same `red_count` and `red_sweep`.

**Smallest safe correction** (edit the instruments, then regenerate the receipt at a new instrument commit):

1. In `criterion11-controls.py`, make `red_count` also move the README to a consistent 232-file state: header `(27)`→`(28)`, `Total knowledge entries: 231.`→`232.`, footer `(total 231 files; directory totals 28/27/29/29/24/94).`→`(total 232 files; directory totals 28/28/29/29/24/94).`. Expected result: SET and SWEEP fail, and in the SWEEP detail sweep.py shows `exit=0`.
2. Add a `red_sweep_exit` control that leaves the footer stale, as in PROBE-FOOTER-STALE. Add `("RED-SWEEP-EXIT", red_sweep_exit, 1, ["SWEEP"])` to `CONTROLS` and a matching line in the docstring.
3. In `claims.json`, change C-count's `red_control` to: "RED-COUNT (a second new .md file with its README row, section header, totals line and footer all moved to 232, so the sweep exits 0): SET and SWEEP fail together, because both pin 231". Change C-index's `red_control` to: "RED-SWEEP (index row names monsters-hybrid-being.md) and RED-SWEEP-EXIT (counts footer left at 230/26: rows 231 files 231, missing_from_index 0, sweep exits 1)".
4. Regenerate `telemetry/criterion11-controls.txt` (expect `14/14`). Then re-run `dry-run.py`, since the instrument commit changes.

### 2. A round-54 constant is left in a function name (cosmetic; no effect on behaviour)

`criterion11-controls.py:116` reads `def s238(t):`. The body correctly edits row S284 (line 117), so this has no functional effect. Rename it to `s284` if the builder is edited for finding 1. A grep of `accept-c.py` and `criterion11-controls.py` found no other leftover 229, S238, S239, S257–S259, masks or culture-material constants.

## Checks that hold (with evidence)

1. **Clause coverage.** Every clause-bearing phrase in `claims.json:16` maps to a listed clause:
   - "230 to 231" → C-count
   - "one file added … no file is removed", including the SET leg's "of any extension" and "all 231 are present" → C-one-new-file
   - SWEEP parenthetical → C-index
   - FLOOR → C-floor
   - RANGE, including "no S-id range" → C-range
   - STATUS → C-status
   - USEDBY → C-usedby
   - ACCESS → C-access

   "exits 0, with its seven legs passing" is enforced by the builder's `len(legs) == 7` check (`criterion11-controls.py:181`). The topic, sentence support, ordinary opening, one-way pointers, handoff and substantive gap are listed as review-only (`claims.json:94-101`). No `- topic:` stand-in or similar predicate is used: `accept-c.py` reads no topic text, and the topic equality sweep.py checks is index consistency.
2. **Red controls.** The other eleven reds each change one clause with a near-miss, and the receipt shows exactly that leg failing with every other leg passing. The receipt reproduces byte for byte: re-running the builder at `d44309a1` gave exit 0, and `diff` against `telemetry/criterion11-controls.txt` was empty. The five instrument sha256 values in the receipt match the files at the base, at HEAD and in the working tree.
3. **Exit statuses.** `accept-c.py:41-46` uses `subprocess.run` with no shell or pipe. Both tools' `returncode` values are read (`:71`, `:102`). A tool that fails to launch or times out returns exit 2 (`:67-68`, `:100-101`).
4. **Before value.** `claims.json:110` and `:112` match the dry-run receipt (`declaration-dry-run.txt:2-10`): SET FAIL count=230 added=[] removed=[]; SWEEP FAIL exit=0 rows 230 files 230; FLOOR FAIL cited=0; RANGE, STATUS and USEDBY PASS vacuously; ACCESS PASS; exit 1. A replay at `662239d2` is identical. No base row is S285 or above (count 0), so no hand-applied predicate over base rows is needed.
5. **Inputs.** `base-knowledge-files.txt` (230 lines) is identical to `git ls-tree -r --name-only d44309a1 corpus/knowledge`. The gap evidence reproduces: 0 filename owners, 10 files mentioning `monster`, 7 mentioning `bestiar`. All 284 base SOURCES rows match both the `accept-c.py` row regex and the `check-source-access.py` row regex, so the duplicate count has no row-shape escape at base. The used-by convention for rows S239–S284 is the full `corpus/knowledge/...` path, which matches the USEDBY substring test.

## Statement text no leg checks strictly (residual, not defects)

- RANGE's span regex (`accept-c.py:82`) catches en dash, em dash, hyphen and `to` between ids. It misses `S303 through S304` and an abbreviated second id such as `S303–04`. A corpus grep shows the lane writes ranges only as `S044–S046`, which the regex catches.
- FLOOR and RANGE count every `\bS\d{3}\b` token in the entry, whether it is a citation or a passing mention. That is consistent with "cites" as RANGE enforces it. Four-digit ids are invisible to the regex, but none can occur this round.
- RANGE also fails a cited row with fewer than 11 cells (`len(table[s]) < 13`). That is stricter than the statement's wording and harmless.

## Outside the clause list (noted only)

`claims.json:5` gives `declared_at` as 19:58Z, but the declaration commit is dated 19:56:50Z and the dry-run header 19:56:43Z.

## Not run

- Claim O and its controls (`accept-o.py`, `criterion11-controls-o.py`).
- `sweep.py --selftest` and `check-source-access.py --selftest`.
- `dry-run.py` check mode (criterion 9).
- Any review-only substance: topic, sentence support, ordinary opening, whether the gap is uncovered in substance.
