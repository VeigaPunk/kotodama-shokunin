- Seat: K01 | scout | claim A | date 2026-10-19 | baseline fd55e1f

# Touched-surface census, rounds 37–40

Mission (targets.json K01): every artifact created or edited in rounds 37–40 —
verify ledgers, protocol, policy, successor ledger, 15 corpus entries, the
argot/renderer patches, the r38/r39 records — each with path + risk class.
This census is the input A01 audits per-surface; verdicts are A01's, not filed
here except where a check ran during census-taking (named as such).

## Method (all read-only; zero filed bytes touched)

- Per-round tracked diffs between round baselines:
  `git diff --name-status 57c8409..9bccc9b` (r37), `9bccc9b..dfb0719` (r38),
  `dfb0719..fd55e1f` (r39). Baselines from each round's claims.json
  (`baseline_commit` fields).
- Corpus entry birth-commit attribution:
  `git log --diff-filter=A --name-only --format='@%h %s' -- corpus/knowledge`.
- Working-tree/untracked state: `git status --short` at census time.
- Fleet .ufo existence check (read-only listing, outside the lane repo).
- Commit-level attribution of shared-surface edits:
  `git log --format='%h %s' --name-only fa90c77^..fd55e1f -- LOG.md SCORECARD.md corpus/README.md tools/`.

## Risk classes used

- **R0 record-only** — additive seat fragments / round-record bytes under
  `reports/round-<N>/**` with no runtime coupling; failure mode is audit or
  provenance confusion only.
- **R1 durable instrument** — cross-round-cited instruments (queues, ledgers,
  protocol, policy, claims/targets/validation/telemetry, round runners,
  LOG.md, SCORECARD.md); later rounds compute or rule against them (e.g. r40
  claim Ca computes against the r37 queue; the r39 protocol governs any
  replay of every filed runner).
- **R2 shared corpus surface** — corpus entries and `corpus/README.md`;
  coupled to the sweep contract (`reports/round-28/readme/sweep.py`):
  partition counts, totals line, counts-footer vector. An error here
  propagates into every later count (the r37 `__E3_PLACEHOLDER__` incident is
  the precedent, LOG.md:3715–3717).
- **R3 runtime tooling** — `tools/*.py` executed by gates and validations
  beyond the owning round; a defect here breaks pipelines round-over-round.

## Round 37 — commits fa90c77 (admit) + 9bccc9b (SCORECARD axes table); baseline 57c8409 → 9bccc9b: +75 A / 3 M

Modified (3):

| path | risk | what changed |
|---|---|---|
| `LOG.md` | R1 | r37 admit entry (now at LOG.md:3703–3723); commit fa90c77 |
| `corpus/README.md` | R2 | integrator repair: removed the two `__E3_PLACEHOLDER__` lines the r35 README apply had left (LOG.md:3715–3717); commit fa90c77. Census re-check: `grep -c E3_PLACEHOLDER corpus/README.md` → **0** |
| `SCORECARD.md` | R1 | axes table + r37 rows; commit 9bccc9b |

Added (75, all under `reports/round-37/`):

- **R1 instruments (11):** `op/defect-queue.json` (the 24-row consolidated
  queue — r40 claim Ca's `before` object),
  `calib/recount-ledger.json` (34-row r33–36 verify recount: 25 match / 5
  mismatch / 4 could-not-reproduce; the 4 c-n-r rows re-dispositioned in r39),
  `claims.json`, `targets.json`, `run-validation.py` (ABSOLUTE: no in-tree
  execution; the r39 isolation-replay protocol governs any replay),
  `validation.json` (receipt `616c1c14…`), and telemetry 5 files
  (`telemetry/dispatch-declared.json`, `observed-dispatch.json`,
  `availability-close-37.json`, `inputs/claims.json`, `inputs/targets.json`).
- **R0 seat fragments (64):** `adj/` A01–A12 (12, incl. the freeze-drift
  adjudication A01 + entries-bleed A02), `calib/` Ca01–Ca16 (16),
  `cross/` X00–X04 (5), `op/` O01–O12 (12), `plan/` P01–P02 (2),
  `review/` R01–R08 (8), `scout/` K01–K04 (4), `scribe/` S01–S05 (5).

## Round 38 — commit dfb0719; baseline 9bccc9b → dfb0719: +42 A / 4 M

Modified (4):

| path | risk | what changed |
|---|---|---|
| `LOG.md` | R1 | r38 admit entry (LOG.md:3725–3743), incl. the grok→devin named deviation |
| `SCORECARD.md` | R1 | r38 rows |
| `tools/gates/argot-derivation-gate.py` | **R3** | +186/−2: the F-6 `derived_forms`/`derived_ok` counters + the RL-8 era leg adapted as `D4L-ARGOT-ERA`; selftest 39/39, live counters 8/8, zero pins moved (LOG.md:3732–3735) |
| `tools/exercise-handoff-e2e.py` | **R3** | +60: the v3 manifest-vs-read-set roster guard with selftest controls m15a/m15b; r7 chain exit 0, packet sha `45f57132…` byte-identical (LOG.md:3736–3738) |

Added (42, all under `reports/round-38/`):

- **R1 instruments (10):** `claims.json`, `targets.json`,
  `run-validation.py`, `validation.json` (receipt `88db61bf…`), telemetry 6
  (`dispatch-declared.json`, `observed-dispatch.json`,
  `availability-attempt-1.json` — the grok 403 out-of-credits record,
  `availability-close-38.json`, `inputs/` claims+targets).
- **R0 seat fragments (32):** `adj/` A01–A03 (3), `cross/` X00–X02 (3),
  `depth/` D01–D10b (10), `op/` O01–O08 (8), `plan/` P01 (1),
  `review/` R01–R03 (3), `scout/` K01–K02 (2), `scribe/` S01–S02 (2).

## Round 39 — commit fd55e1f; baseline dfb0719 → fd55e1f: +32 A / 3 M

Modified (3):

| path | risk | what changed |
|---|---|---|
| `LOG.md` | R1 | r39 admit entry (LOG.md:3745–3761) |
| `SCORECARD.md` | R1 | r39 rows |
| `corpus/README.md` | R2 | revision 2.2: verification rows 20→24, totals 212→216, footer vector → 21/23/25/29/24/94 (corpus/README.md:5–10) |

Added (32):

- **R2 corpus entries (4)** — the r39 expansion of the verification partition,
  birth commit fd55e1f:
  - `corpus/knowledge/verification/append-only-record-verification.md`
  - `corpus/knowledge/verification/contact-strata-verification-gate.md`
  - `corpus/knowledge/verification/index-sweep-verification.md`
  - `corpus/knowledge/verification/worked-example-verification.md`
- **R1 instruments (12, `reports/round-39/`):**
  `calib/isolation-replay-protocol.md` (the safe-replay protocol, O12),
  `calib/basename-couples-policy.md` (the basename-couples fallback policy),
  `calib/recount-ledger-successor.json` (re-dispositions the 4 r37 c-n-r rows
  reproduced-under-protocol), `claims.json`, `targets.json`,
  `run-validation.py`, `validation.json` (receipt `0fefcd56…`), telemetry 5
  (`dispatch-declared.json`, `observed-dispatch.json`,
  `availability-close-39.json`, `inputs/` claims+targets).
- **R0 seat fragments (16):** `calib/` Ca01–Ca04 (4), `cov/` C01–C06 (6),
  `cross/` X00 (1), `plan/` P01 (1), `review/` R01 (1), `scout/` K01–K02 (2),
  `scribe/` S01 (1).

## Round 40 — in flight at census time (uncommitted/untracked)

| path | risk | state |
|---|---|---|
| `LOG.md` (working tree) | R1 | uncommitted append: operator amendment 7, devin authorized for deepseek-v4.1-flash waves (LOG.md:3763–3771); parent-owned |
| `reports/round-40/claims.json`, `targets.json` | R1 | declared instruments (this round's contract) |
| `reports/round-40/telemetry/dispatch-declared.json` | R1 | declared dispatch record; observed + close snapshots owed |
| `reports/round-40/plan/P01-plan.md`, `cross/X01-trades.md`, `scribe/S02-telemetry-draft.md`, `calib/Ca03-receipt.md`, `adj/A01-audit.md` | R0 | in-flight seat fragments present at snapshot; other seats' outputs expected before integration |
| `reports/round-40/scout/K01-touched-census.md` | R0 | this file |
| `/home/vgpnk/Projects/shokunin/.ufo/reports/round-{37,38,39}/kotodama.md` | R0 (fleet-owned, read-only to lane seats) | confirmed present via `ls` (fleet root `.ufo/`, per commit 139e3b6 the fleet report lives there, not in the lane repo) |

## Untouched-but-in-scope surfaces (negative census)

- `PROVINCE.md` — not in any r37–39 diff; byte-stable across the audited
  window. Its re-verification at HEAD is A02's assignment.
- `examples/culture-d4/**` — zero bytes moved in r38 despite claim D's
  "tool/example artifacts" allowance: the counters emit from the argot gate
  host (the documented-equivalent route). The two-artifact boundary held.
- Corpus partitions other than the 15 expansions: birth-commit attribution
  shows no r37–40 creation in civilizations / linguistics / myth-symbol /
  synthesis / culture-material. The claim-A phrase "the 15 new corpus
  entries" reconciles exactly: 10 @ ce103bf (r35: 6 culture-material +
  4 myth-symbol) + 1 @ 57c8409 (r36: timekeeping-instruments) + 4 @ fd55e1f
  (r39, listed above). No entry was *edited* post-landing (only-additive
  held for r37–40).
- `corpus/lessons/*.md`, `tools/gates/frozen/**` — absent from all r37–39
  diffs (frozen/lessons boundaries held).

## Census totals

- Rounds 37–39 (committed): **149 files added + 10 shared-surface edits**
  (LOG.md ×3, SCORECARD.md ×3, corpus/README.md ×2, tools/*.py ×2) across 4
  commits (fa90c77, 9bccc9b, dfb0719, fd55e1f).
- Round 40 to date: 3 declared instruments + ≥6 in-flight fragments, all
  untracked; 1 uncommitted LOG.md append.
- Corpus state at HEAD (census re-count): civilizations 94, culture-material
  25, linguistics 21, myth-symbol 23, synthesis 29, verification 24 =
  **216 total**; README revision 2.2 — the exact `before` state r40 claims
  C/Ca/A compute from.

## Owed

- None from this seat. Downstream: A01 turns this census into per-surface
  verdicts; A02 owns the PROVINCE byte-accuracy re-verification; K02's queue
  scout overlaps only at `op/defect-queue.json` (my row: R1, cited as r40 Ca's
  before-object).

## Citations

- `git diff --name-status 57c8409..9bccc9b` → 75 A / 3 M; `9bccc9b..dfb0719`
  → 42 A / 4 M; `dfb0719..fd55e1f` → 32 A / 3 M (run 2026-10-19).
- `git log --format='%h %s' --name-only fa90c77^..fd55e1f -- LOG.md
  SCORECARD.md corpus/README.md tools/` → per-commit attribution above.
- `git log --diff-filter=A --name-only -- corpus/knowledge` → entry birth
  commits ce103bf (10), 57c8409 (1), fd55e1f (4).
- `git status --short` → ` M LOG.md`, `?? reports/round-40/` only.
- LOG.md:3703–3761 (r37/r38/r39 admit entries); LOG.md:3715–3717 (placeholder
  repair); LOG.md:3732–3738 (r38 tool changes + sha pins); LOG.md:3763–3771
  (amendment 7, uncommitted).
- corpus/README.md:5–10 (revision 2.2 note: 212→216, footer vector).
- `grep -c E3_PLACEHOLDER corpus/README.md` → 0.
- Partition counts at HEAD: `ls corpus/knowledge/*/*.md` per directory →
  94/25/21/23/29/24 (total 216).
- `ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-{37,38,39}` →
  `kotodama.md` present in each.
- targets.json:13–17 (this seat's mission), claims.json:25–30 (claim A).
