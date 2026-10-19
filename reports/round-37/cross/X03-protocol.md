- Seat: X03 | critic | cross | date 2026-10-19 | baseline 57c8409

# Protocol audit

**Finding:** The declaration has the expected verify-round shape and three distinct claim axes, but some acceptance denominators and the lowest-axis rule need explicit integration-time treatment. This is a protocol review, not a claim verdict or admission decision.

## Shape and axis set

Round 37 is declared as loop 1, position 5, the luna-max verify round. Its three claims map one-to-one to calibration (Ca), operability (O), and adjacency (A); freshness is expressly excluded, consistent with the regimen's pause. The distinct-axis shape matches the prior verify-round declarations at rounds 21 and 29. Round 36's rejected D claim is not among the r37 claims and must remain a separate historical verdict. ( `REGIMEN.md:13-16,27-33,37-43`; `reports/round-37/claims.json:5-10,12-34`; `reports/round-21/claims.json:9-30`; `reports/round-29/claims.json:9-30`; `SCORECARD.md:651-666`.)

The lowest-axis rationale is not fully settled by the governing text. SCORECARD says its old numeric estimates have no reproducible mapping and describes freshness as historically lowest (`SCORECARD.md:11-16`); the regimen both requires a claim on the lowest non-retired axis and keeps freshness axis-moves paused (`REGIMEN.md:27-33`). The r37 rationale instead says non-paused axes have 2–3 regimen-2 claims (`claims.json:9-10`). Across rounds 33–36, calibration and adjacency each appear in two round claim sets while operability appears in three (`SCORECARD.md:578-666`), so r37 claims both tied minima under that count-based interpretation. The documents do not define that count as the axis-ranking rule or explain how the freshness pause alters “lowest non-retired”; record the interpretation rather than presenting the ranking as independently measured.

## Checkability findings

1. **Calibration denominator differs across assignments.** Ca's claim counts acceptance commands filed in rounds 33–36 validation receipts (`claims.json:13-18`), and K01's inventory / Ca09 coverage check are scoped to those receipt commands (`targets.json:11,27`). Ca05 additionally owns recurring cross-cutting commands “not tied to one round's receipt,” while Ca06 assembles Ca01–Ca05 and Ca09 only requires every K01-inventoried command exactly once (`targets.json:23-27`). Unless the cross-cutting set is either explicitly outside the acceptance denominator or added to the inventory and exact-once comparison, the expected row count and coverage result are ambiguous. Preserve both sets distinctly if the latter is not resolved.

2. **Verifier sample rule needs a reproducible denominator and record.** The claim says two independent verifiers sample at least 25%; the assignments say each verifier runs at least 25%, and Ca08 uses a “different” sample (`claims.json:18`; `targets.json:25-27`). For checkability, report inventory size N, each verifier's command IDs actually rerun, and the minimum integer count `ceil(N/4)`. State whether “different” means non-identical or disjoint samples; the current text does not choose. Keep the two seat identities and their samples separate so the verifier independence can be audited.

3. **Coverage is not the same as successful reproduction.** The Ca threshold requires 100% command-row coverage and permits `could-not-reproduce` rows with an owner (`claims.json:15-18`). It does not set a maximum for such rows. Therefore the acceptance result must report match, named mismatch, and could-not-reproduce counts separately; a documented inability must not be represented as a match or as an actually rerun command. If the intended gate requires a minimum execution/reproduction rate, that threshold is not declared here.

4. **Operability needs stable row identity for exact set equality.** The O claim's census-to-ledger 100% threshold and zero-unowned condition are testable against K02's census; O01/O05 provide the ledger and equality check, O02 checks non-author evidence for fixed items, and O03 checks carried routing (`claims.json:19-24`; `targets.json:12,36-41`). Make the queue's canonical defect key and duplicate/cross-reference rule explicit, so repeated mentions in SCORECARD, LOG, receipts, and fragments neither inflate the expected set nor disappear from the census. Keep the census-completeness review distinct from the O05 set-equality result.

5. **Adjacency requires a finite surface inventory.** A01–A04 divide the work into the freeze comparison, eleven-entry scan, r33–37 scope census, and contested-scope check (`targets.json:49-54`); the claim also requires every surface to receive a verdict and zero unfiled bleed (`claims.json:25-30`). The acceptance record should identify the full surface set (using the scope census and named entry/freeze inputs), map each surface to a verdict and evidence pointer, and separately show the contested items remain routed. Without that inventory-to-verdict mapping, “every surface” and “zero unfiled” are not countable.

At this inspection, `Glob reports/round-37/run-validation.py` returned “No matches found.” Accordingly the runner-level encoding of these gates is not yet inspectable, and no acceptance thresholds have been executed or verified here. The shared rules prohibit an in-tree runner execution; later validation must use the required isolated archive procedure, never the in-tree path. (`reports/round-37/targets.json:3-8,17-18`; command/tool output cited below.)

## Owed

- Integrator: resolve and record the Ca05 denominator boundary; preserve per-verifier sample IDs/counts and non-reproduction dispositions; ensure the acceptance runner checks these as separate outcomes.
- Integrator: require stable O queue keys and an explicit A surface-to-verdict inventory; distinguish census completeness from ledger equality.
- Integrator/operator: record the applicable lowest-axis interpretation while freshness remains paused; do not invent a new numeric score or claim a freshness move.
- Integrator: inspect and exercise the delivered validation runner only in the allowed isolated archive; until then these are declaration-level findings, not verified outcomes.

## Citations

- `REGIMEN.md:13-16,27-43` — scheduled verify round, distinct-axis / lowest-axis / pause / admission requirements.
- `SCORECARD.md:11-16,578-666` — uncalibrated historical score mapping, freshness-lowest note, and rounds 33–36 claim axes/results.
- `reports/round-37/claims.json:5-10,12-34` — round identity, axes rationale, claim scopes, thresholds, and non-goals.
- `reports/round-37/targets.json:3-8,11-12,19-27,36-41,49-60` — shared execution boundary and seat-level inventory, verification, and audit responsibilities.
- `reports/round-21/claims.json:9-30`; `reports/round-29/claims.json:9-30` — prior verify-round claim shape.
- `reports/round-37/run-validation.py` lookup: `Glob` returned “No matches found” at this inspection; no runner was executed.
