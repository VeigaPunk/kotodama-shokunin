- Seat: X01 | critic | cross | date 2026-10-19 | baseline 57c8409

# X01 — trade hunter

This is an evidence register for integration, not an axis verdict or round acceptance. The declared axes are calibration, operability and adjacency; freshness is paused (`reports/round-37/claims.json:9,32-34`). Findings below separate established trade-offs from unresolved overlaps.

## Trade register

### T1 — Recount coverage vs safe reproduction (confirmed hazard; route is constrained)

- **Gain:** Ca requires a row for every filed acceptance counting command across rounds 33–36, including rejected rounds, plus independent samples (`reports/round-37/claims.json:13-18`). This improves calibration coverage.
- **Cost:** the no-in-tree-runner rule protects filed receipts, but a plain archive/clone is not sufficient isolation for runners that hardcode the live repository path. Round 36 documented that r34/r35 runners `chdir` to that absolute path; an archive execution rewrote the live r35 receipt. Its recount used a self-contained clone bind-mounted over the lane path in a private mount namespace (`reports/round-36/cross/X01-trades.md:251-277`; `reports/round-36/calib/Ca03-ledger-draft.md:27-34`).
- **Disposition discipline:** count coverage and successful reproduction separately. A `could-not-reproduce` row with owner and reason is permitted by Ca's threshold; it is not a `match` and cannot be converted into one to meet 100% coverage (`claims.json:16-18`). Do not run a known absolute-root runner from a merely extracted copy.
- **Route:** K01 inventory + Ca executors; the assigned runner isolation must be demonstrated before execution. If a safe carrier is unavailable, preserve the row with the documented could-not-reproduce disposition and owner.

### T2 — Source-set completeness vs r7 freeze stability (real asymmetry; adjudication pending)

- **Gain:** A requires re-render comparison and disposition of the `13-register-law.yml` packet-manifest/read-set asymmetry (`claims.json:25-30`; `targets.json:49`).
- **Cost:** the live `D4_COMPONENTS` tuple lists components 01–12 (`tools/exercise-handoff-e2e.py:157-170`), and `V3_READ_SET` expands that tuple (`:1939-1958`). Meanwhile the assembler enumerates every eligible component file (`tools/assemble-culture-d4.py:214-224`); the prior review records component 13 entering the packet's assembly-source digest while not being a direct read-set member, and adding it to the read set would change 58 members to 59 (`reports/round-34/review/R01-d-review.md:97-110`). More direct source coverage is the gain; it changes the pinned input set and so risks breaking r7 comparison/operability.
- **Boundary:** r37 explicitly forbids re-freezing `declared-in-r7` (`claims.json:32-34`). A01 must adjudicate from a read-only re-render and the existing packet/source pins; if a membership change is proposed, it is a successor-freeze decision for the integrator, not a silent rewrite of r7. This seat does not decide whether the asymmetry is defect or documented skip.

### T3 — Recount schema simplicity vs revision-specific truth (risk carried forward)

- **Gain:** Ca06's assigned schema is compact: `{round, claim, command, filed, observed, disposition, owner}` (`targets.json:24`).
- **Cost:** it has no observation-revision field. Round 36 already identified a concrete temporal collision: corpus-count commands read 211 before a landing and 212 after it, both valid at their respective revisions; its trade report recommended recording an observed revision or explicit ordering (`reports/round-36/cross/X01-trades.md:172-183`). Round 37's recount spans several rounds, so omitting the observation boundary could turn a revision change into an apparent mismatch or obscure which bytes were tested.
- **Route:** Ca06/integrator should retain the requested fields and add `observed_at_revision` (or a ledger-wide revision plus explicit ordering) rather than smoothing a difference. No row-level mismatch is asserted here; K01/Ca06 inputs were unavailable to Ca09 at its inspection (`reports/round-37/calib/Ca09-coverage.md:3-7`).

### T4 — Ca/O overlap is not yet decidable

Ca re-runs filed counting commands; O02 independently re-runs controls for items called fixed (`targets.json:19-24,36-40`). Reusing one observation could reduce work, but can conflate an old acceptance reading with a present-day fix check unless command, target revision, owner and purpose are identical. X00 is assigned to resolve recount/queue ownership, including the r36 rejection (`targets.json:17,68`). No overlap is claimed or assigned here: K01/Ca06 inputs were absent at Ca09's inspection, and the defect census/queue evidence needed to compare rows is not cited as available (`reports/round-37/calib/Ca09-coverage.md:3-7`). Keep separate rows until X00's owner map establishes a valid cross-reference.

### Rejected-r36 evidence boundary (not a trade to optimize)

Ca's recount includes r36, but X04 is specifically tasked to prevent a rejected r36 D-leg from being repaired by this round (`targets.json:68-74`). Any current re-run may characterize current behavior; it must not replace or upgrade r36's filed evidence. The no-rewrite and no-closure constraints remain binding (`claims.json:32-34`).

## Owed

- Reconcile T1 against K01's command inventory and Ca01–Ca06's landed rows; confirm the isolation procedure for each runner before any execution. Assignments: `reports/round-37/targets.json:11,19-27`.
- Reconcile T2 against A01's actual re-render comparison and A06 review; do not decide from the manifest asymmetry alone. Assignments: `targets.json:49,54`.
- Reconcile T3/T4 against K02's census, O01/O02 queue and fix-verification outputs, and X00's overlap matrix. Assignments: `targets.json:12,17,36-40`.
- No current claim of final trade disposition: these are constraints and risks for the integrator, not round acceptance evidence.

## Citations

- `reports/round-37/claims.json:9,13-18,19-30,32-34` — axes, Ca/O/A requirements and non-goals.
- `reports/round-37/targets.json:5-8,11-27,36-40,49,54,68-74` — shared fences and assigned owners/missions.
- `reports/round-37/calib/Ca09-coverage.md:3-7` — K01/Ca06 absence at Ca09's inspection and resulting unknown coverage.
- `reports/round-36/cross/X01-trades.md:251-277,172-183` — absolute-root isolation hazard and revision-boundary precedent.
- `reports/round-36/calib/Ca03-ledger-draft.md:20-34` — isolated replay methods for r33 versus r34/r35.
- `tools/exercise-handoff-e2e.py:157-170,1937-1958` — declared component tuple and read-set composition.
- `tools/assemble-culture-d4.py:214-224` — component enumeration.
- `reports/round-34/review/R01-d-review.md:97-110` — component-13 asymmetry and 58-to-59 option.
