# RevD4Bound — attack on the R65-D4 disposition (bounded separability receipt)

Seat: attack, round 66 (hyaku run 5), lane `kotodama-shokunin` @ base `94209e8f80969dbac48d56c5d0e2e623635b8616`.
Scope: does `reports/round-66/telemetry/separability-real.txt` have to show a *complete, correctly
sized* verdict, and can it pass while repair attempts were skipped, absent, or fabricated?

## Verdict

**The D4 leg is a shape check, not a bound check.** `accept-ca.py:156-161` accepts *any*
`SEPARABILITY: <n> findings` line with *any* `acceptance_runs=<n>` and without the substring
`PARTIAL`. It never reads `units=`, `ordered_pairs=`, `skipped=`, the exit code, or the two
findings that `claims.json` itself declares as expected. I built four manifests and ran the
real tool with the declared flags: **runs = 0, 2 and 4 all satisfy the D4 predicate** against a
manifest shaped exactly like round 66's (units=4, ordered_pairs=12). Only the honest one is 6.

Skips are caught honestly ("could it pass while the run skipped repair attempts?" → no for a
*skip*); the failure mode is a complete verdict in which no repair was ever *required or
attempted* because the acceptance was removed, or in which every "evaluation" was a timeout.

**Dependency: the receipt does not exist yet**, nor does the manifest it must describe
(`reports/round-66/telemetry/separability-real.txt`, `reports/round-66/separability-manifest.json`
both absent at review time). Everything below is derived from the frozen instrument, `claims.json`
`separability.manifest_units`, and fixture runs of the real tool.

## Re-derived needed run count (round 66)

`_acceptance_findings` (`tools/check-claim-separability.py:711-744`) meters: 1 run per
acceptance-bearing unit, plus `len(units)-1` repair runs *only if* that unit's own run fails.

Manifest per `claims.json` `separability.manifest_units`: units = **4** (C, O, Ca, REC;
acceptance-bearing = **3**, REC is `role: record` with no acceptance), ordered pairs = **12**.

| unit | own run | fails at base+own lands? | repairs | runs |
|---|---|---|---|---|
| C   | 1 | expected no  | 0 (only if it fails) | 1 |
| O   | 1 | expected no  | 0 (only if it fails) | 1 |
| Ca  | 1 | **yes, by declaration** (D2 reads `final-measures-{c,o,ca}.txt`, REC lands) | 3 (C, O, REC) | 4 |

**Needed = 6**, `skipped=0`, `acceptance_runs=6`, exit **1**, findings == the 2 declared in
`claims.json` (`Ca->REC` static land path + `Ca->REC` via acceptance). Worst case with all three
failing is 12 (= ordered pairs). A receipt whose `acceptance_runs` is not 6 (or 9/12 if C or O
also fail) is not a verdict about this claim.

Fixture proof of the formula (same shape, real tool, `--jobs 4 --timeout 120 --budget 300`):
`SEPARABILITY_NOTE units=4 ordered_pairs=12 acceptance_runs=6 skipped=0`, exit 1,
`SEPARABILITY_DEPENDENCY Ca->REC via acceptance ...`.

## Findings

### HIGH-1 — D4 passes at `acceptance_runs=0` and at `=2`: an acceptance-free manifest is a "complete verdict"
`accept-ca.py:157-161`:
```python
d4_ok = (re.search(r"^SEPARABILITY: \d+ findings$", d4, re.MULTILINE)
         and re.search(r"acceptance_runs=\d+", d4)
         and "PARTIAL" not in d4)
```
Observed against the real tool, manifests of identical unit/pair shape:
- all acceptances removed → `SEPARABILITY: 0 findings`, `units=4 ordered_pairs=12 acceptance_runs=0 skipped=0`, exit 0 → **D4 PASS**.
- only Ca's acceptance removed (the one unit the round must exercise) → `acceptance_runs=2`, `0 findings`, exit 0 → **D4 PASS**.

So the cheapest shortcut for the R65-D4 disposition is to ship a manifest in which Ca carries
`lands` but no `acceptance`. The receipt then reads "COMPLETE, no partial", the dynamic leg never
touches `accept-ca.py`, and the declared `Ca->REC` acceptance finding silently disappears. Nothing
in `accept-ca.py` or in `claims.json`'s predicate notices.

### HIGH-2 — `PARTIAL`-only check cannot distinguish a fabricated `<base>` from a real one, and timeouts fabricate it
The tool's own docstring (`tools/check-claim-separability.py:39-41`) declares a timed-out run
"counts as a failed run". `_run_acceptance` returns `(False, "timeout after Ns")`, which flows into
`SEPARABILITY_DEPENDENCY X-><base> ... and no declared unit's lands repairs it`. Observed: an
acceptance that sleeps past `--timeout 0.5` in base+lands and in every repair yields
`SEPARABILITY: 1 findings`, `acceptance_runs=4 skipped=0`, exit 1 — **COMPLETE, `skipped=0`, `<base>`
asserted with zero evaluation**, and **D4 PASS**. `claims.json` O promises "never fabricated
`<base>`"; that holds for skipped runs only, not for timeouts or non-1 exit codes (`--selftest`
enshrines `sys.exit(3)` → `C-><base>` at `:1089-1094`). A 120 s per-run cap on an acceptance that
needs 130 s is therefore a legitimate-looking, complete, false dependence on `<base>`.

### HIGH-3 — the receipt is not bound to the round-66 manifest, the flags, or the declared findings
D4 embeds no `units=`/`ordered_pairs=`/`skipped=` assertion, no exit-code assertion, and no
assertion of `claims.json`'s two `expected_findings`. Consequences, each of which passes D4 today:
- a 3-unit manifest (REC dropped) → `units=3 ordered_pairs=6`, `Ca-><base>` instead of `Ca->REC`;
- the tool's own selftest fixture lanes (claim O's `BOUND`/`FIXTURES` legs already emit
  `PARTIAL`/non-`PARTIAL` notes) — a fixture stdout pasted into the receipt is undetectable;
- a run with `--static-only`-style degradation is caught (`PARTIAL`), but a run whose *repairs* all
  failed is indistinguishable from a run whose repair succeeded;
- the verdict (`SEPARABILITY:`) is stdout and `acceptance_runs=` is stderr — a receipt concatenating
  the two streams from *different* runs passes the regex pair.

### MED-4 — circularity: `separability-real.txt` is a `Ca` land, so the receipt records a state that no longer exists
`claims.json` `manifest_units.Ca.lands` includes `reports/round-66/telemetry/separability-real.txt`,
and D4's leg reads it. The run that produces the receipt therefore reads an earlier receipt, and the
committed bytes are never the bytes any single run saw. This is a fixed-point requirement, not a
one-shot artifact: the honest procedure is run → write → re-run → require byte-identical
`acceptance_runs`/findings on the second run, and say so in the receipt. Neither `claims.json` nor
`accept-ca.py` requires it. Note also that the `separability.note` class declaration mis-assigns
D4's receipt to the REC unit ("D2/D3/D4 legs read committed receipt/evidence files that are lands of
the REC record unit") — `separability-real.txt` is a **Ca** land, so the declared static finding for
it will not fire; only the acceptance-level `Ca->REC` is declared. Calibration defect in the
instrument's own declaration.

### MED-5 — `Ca->REC` acceptance repair is not reachable until the receipts are committed on `main`
D2 (`accept-ca.py:108-142`) requires `git log -1 main -- <receipt>` to name a carrier **and** that
carrier's parent to equal the stamped revision. Inside `_git_counterfactual` the clone's `main` is
the lane's real ref, so before the L1's integration commits land, `no_carrier` keeps D2 failing even
at base+Ca+REC → the honest run prints `Ca-><base>`, not the declared `Ca->REC`, while
`acceptance_runs` stays 6. Run count cannot detect this; only the finding line can. The D4 leg must
therefore assert the finding text, and the real run must happen **after** the receipts are committed
and **before** the final `final-measures` stamping.

### LOW-6 — `--budget` bounds run *starts*, not wall time
`_Budget.take()` checks the deadline before incrementing; a run started at t=299 s may run a full
`--timeout 120` → worst-case wall ≈ 420 s for a 300 s budget. Claim O's "returns a verdict inside a
round's budget" is off by one `timeout`. Declared knobs are otherwise sound; the `--max-runs 2` case
was verified to produce exit 2 + `SEPARABILITY_PARTIAL 2 run(s) skipped` +
`SEPARABILITY_UNRESOLVED Ca->{O,REC}` and **fails** the D4 predicate — the skip path is honest.

## Required D4 leg (recommended, minimal)

```
d4_ok = (re.search(r"^SEPARABILITY: 2 findings$", d4, re.M)
         and re.search(r"acceptance_runs=6 skipped=0", d4)
         and "SEPARABILITY_NOTE units=4 ordered_pairs=12" in d4
         and "PARTIAL" not in d4
         and "SEPARABILITY_DEPENDENCY Ca->REC via land path" in d4
         and "SEPARABILITY_DEPENDENCY Ca->REC via acceptance" in d4
         and "-><base>" not in d4
         and "timeout after" not in d4)
```
plus the run's exit code recorded in the receipt (`exit 1`), and a second identical run whose
`acceptance_runs`/findings lines are byte-identical (MED-4).

## Verification gaps / residual risk

- The receipt and the manifest are absent at review time, so no live receipt was judged; all
  shortcut results come from fixture manifests of identical shape run through the committed tool
  with the declared flags.
- I did not run `accept-c.py`/`accept-o.py`/`accept-ca.py` counterfactuals against the real corpus
  (would require writing lands); the "Ca fails at base+Ca.lands" premise is taken from the declared
  D2 dependency and the D2 code path, not observed.
- If C or O also fail their own counterfactual, the honest count is 9 or 12, not 6 — the receipt's
  finding lines, not the count, must be the acceptance criterion.

No tool installs or upgrades were performed for this seat.
