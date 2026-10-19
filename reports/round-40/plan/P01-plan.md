- Seat: P01 | planner | cross | date 2026-10-19 | baseline fd55e1f

# Round-40 plans — all three claims

Planner's note: scouts (K01/K02/K03) run concurrently; their fragments were
not yet landed at plan time (measured: `reports/round-40/` contained only
`claims.json`, `targets.json`, `telemetry/dispatch-declared.json`). Every plan
below consumes scout fragments by CONTRACT (their `out` paths + target
missions), with a stated fallback if a fragment is late. Nothing below asserts
scout fragment contents.

## 0. Anchors measured at plan time (baseline fd55e1f, clean tree except LOG.md + round-40/)

- `ls corpus/knowledge/linguistics/*.md | wc -l` → 21 (claim C's "before").
- Partition census: civilizations 94, culture-material 25, linguistics 21,
  myth-symbol 23, synthesis 29, verification 24 → `find corpus/knowledge -name '*.md' | wc -l` → 216.
- `corpus/README.md` is at revision **2.2** (line 5); totals line 212 → 216 and
  footer vector **21/23/25/29/20/94 → 21/23/25/29/24/94** recorded at lines 9–10.
  Vector order: linguistics/myth-symbol/culture-material/synthesis/verification/civilizations.
- r37 queue: `reports/round-37/op/defect-queue.json` — top-level keys
  `schema, round, date, notes, census_coverage, rows`; **rows = 24**; row fields
  `class, evidence, id, next_touch, origin, owner, reason, verification`.
- r39 gap definitions live in `reports/round-39/scout/K01-verification-gaps.md`:
  G1 contact-strata gate (:84), G2 taboo–euphemism lifecycle (:106),
  G3 dialect/faction register-ecology (:125), G4 cultural-translation protocol
  fidelity (:148), ranked alternates (:169). G1 landed at r39 (README rev 2.2,
  verification 20→24), so round-40's C entry set = G2, G3, G4 + a fourth gap
  named by THIS round's K03 (linguistics-partition, collision-checked).
- `reports/round-28/readme/sweep.py` exists; `PROVINCE.md` exists at repo root.

## 1. Plan — claim C (coverage): linguistics 21→25 + README rev 2.3 (216→220)

Claim contract (claims.json C): four sourced entries (G2/G3/G4 + K03's fourth)
into `corpus/knowledge/linguistics/`, README rev 2.3, thresholds audit 4/4 PASS
+ sweep green; after: linguistics 25, total 220.

Steps (seat → action → gate):

1. **K03 → `scout/K03-gaps.md`**: names the fourth topic with sources + the
   collision check vs the 21 existing linguistics filenames. Gate: each of the
   four topics has ≥1 resolvable source and no filename collision.
2. **C01–C03** author entries 1–3 (G2 taboo–euphemism lifecycle, G3
   dialect/register-consistency, G4 translation-protocol fidelity) as fenced
   blocks (3-or-4 backticks) under the round-35/36/39 entry contract
   (front-matter `- topic:` matching the README index row byte-for-byte;
   sources cited to repo files; NO staged corpus bytes). Gate per entry: draft
   compiles as a block, topic line present, sources resolvable.
3. **C04** authors entry 4 from K03's fourth topic, same contract. FALLBACK if
   K03 is absent at C04 start: draft from r39's ranked alternates
   (`reports/round-39/scout/K01-verification-gaps.md:169`), redo the collision
   check locally; if still unresolved, C04 files `## Owed` with the blocking
   reason — the claim then reports 3/4 honestly rather than forcing a pass
   (rounds 11/17/22 precedent).
4. **C05 → `cov/C05-audit.md`**: audits all four drafts — runbook compliance,
   source resolution (every cited path exists at HEAD), fabrication
   spot-checks (each factual assertion traceable). Gate: 4/4 PASS; any FAIL
   returns to the owning seat for redraft + re-audit before C06.
5. **C06 → `cov/C06-delta-receipt.md`**: README rev 2.3 delta draft — new
   revision block above rev 2.2 (`corpus/README.md:5`), `## linguistics/`
   header 21→25, totals 216→220, footer vector
   `21/23/25/29/24/94 → 25/23/25/29/24/94`, 4 index rows in filename order,
   plus the coverage receipt. Gate: delta's numbers re-derived from the actual
   draft filenames, not asserted.
6. **C07 → `cov/C07-verify.md`**: independent re-verification of C05's
   verdicts AND the delta numbers (counts, filename ordering, row byte-shape
   vs existing linguistics rows).
7. **Integration (parent only)**: apply the 4 fenced entries + README delta;
   measure: linguistics count = 25, knowledge total = 220,
   `python3 reports/round-28/readme/sweep.py` green (220 rows vs 220 files,
   exit 0). Seats never stage corpus.

Non-goals respected: no freshness move, no canon/clearance decisions in the
entries (domain claims cited to sources, canon left to lore-shokunin).

## 2. Plan — claim Ca (calibration): defect-queue-v2 refresh

Claim contract (claims.json Ca): fold r38/r39 findings into the r37 queue;
every row owner/reason/next-touch re-verified current; census_coverage
completed or carried with an owner; thresholds row count ≥28, every row
owner-complete; next-touches aligned with loop-1 positions 41–46 (lane rounds
41/42/43/44/45/46 per REGIMEN.md position table).

Steps:

1. **K02 → `scout/K02-queue-scout.md`**: inventories the 24 r37 rows + every
   finding added in r38/r38-wave/r39 records, each with origin +
   current owner-state. Gate: every finding carries a filed source path.
2. **Ca01 → `calib/Ca01-queue-v2.md`**: assembles `defect-queue-v2.json` as a
   fenced JSON block — schema preserved (`schema/round/date/notes/
   census_coverage/rows`); r38/r39 findings folded as new rows (≥28 total);
   every carried row's `owner`/`reason`/`next_touch` re-verified current;
   `census_coverage` completed or carried with a named owner + reason;
   `next_touch` values aligned to positions 41–46. Owner-complete = all three
   fields non-empty for every row.
3. **Ca02 → `calib/Ca02-verify.md`**: samples ≥30% of v2 rows (≥9 rows) back
   to their origin records; disagreements filed, not silently fixed.
4. **Ca04 → `calib/Ca04-consistency.md`**: strict JSON parse; row count ≥28;
   class vocabulary ⊆ r37 queue's existing classes (any new class recorded
   with reason); zero duplicate `id`s; owner-completeness re-checked
   mechanically.
5. **Ca03 → `calib/Ca03-receipt.md`**: calibration receipt — before (24 rows,
   r37-aged, findings scattered in round records) → after (v2 all-current,
   findings incorporated, next-touches mapped to 41–46), census_coverage
   disposition stated.
6. **Integration (parent only)**: land the fenced JSON as
   `reports/round-40/op/defect-queue-v2.json`. The claim's counting command is
   the round-40 validation leg (spec by S01); per the r39 isolation-replay
   protocol NO seat runs any `run-validation.py` in-tree.

Double gate on completeness: Ca02's sample + R02's dedicated "are the r38/r39
findings REALLY all in?" hunt. An under-count found late is a named finding
with owner, not a forced pass.

## 3. Plan — claim A (adjacency): loop-1 midpoint audit of rounds 37–40 surfaces

Claim contract (claims.json A): consolidated census of every artifact rounds
37–40 created or edited (verify ledgers, protocol/policy, the 15 new corpus
entries, renderer/gate patches, r38/r39 records) with per-surface verdicts;
PROVINCE re-verified; zero unfiled bleed; contested items routed-not-absorbed.

Steps:

1. **K01 → `scout/K01-touched-census.md`**: the touched-surface census — every
   artifact created/edited r37–r40, each with path + risk class. The entry
   count (15) is taken from the census, not asserted by the plan.
2. **A01 → `adj/A01-audit.md`**: walks the census surface-by-surface; per
   surface a verdict (green | named finding + owner) with evidence:
   language-scan (no sibling/world-bible/domain-source bleed), ownership
   (filed vs unfiled), PROVINCE conformance. Contested scope → routed rows
   with the named route, never absorbed.
3. **A02 → `adj/A02-province.md`**: PROVINCE.md accuracy re-verification at
   HEAD `fd55e1f` (scope claims vs actual tree) + contested-scope re-check
   against the r38/r39 contested items.
4. **A03 → `adj/A03-verify-assembly.md`**: independently re-runs a sample of
   A01/A02's commands, then drafts the final consolidated audit assembly.
5. Gate: every touched surface verdict-filed; zero unfiled bleed. Findings do
   not block filing the audit — they are filed with owners; queue-relevant
   ones feed claim Ca's v2 next-touches (cross-link noted for X00).

## 4. Cross-claim integration order (proposed; X00 owns the binding matrix)

1. Scouts: K01, K02, K03.
2. Executors: C01–C03 (unblocked), C04 (gated on K03), Ca01 (gated on K02),
   A01 (gated on K01), A02 (unblocked — PROVINCE + HEAD are stable inputs).
3. Verifiers: C05 → C06 → C07; Ca02 + Ca04 → Ca03; A03.
4. Cross: X00 collision matrix/integration order, R01 adversarial review of
   all three blocks, R02 queue-completeness + fabrication hunt, X01 trades.
5. Scribes: S01 integration dossier + validation-leg spec; S02 telemetry draft.
6. Parent: apply corpus fenced blocks (entries + README delta), land
   `op/defect-queue-v2.json`, file the audit + receipts, run the validation
   leg per the r39 protocol (never in-tree), then SCORECARD/LOG/`MANIFEST`/
   `.ufo` report/telemetry closing snapshot.

Collision control (single-writer): README changes exist only as C06's draft
block; queue-v2 exists only as Ca01's fenced JSON; no seat writes outside its
declared `out` path; corpus is never staged by a seat (r39 precedent recorded).

Top risks: K03 late → C04 fallback/owed path (§1.3); r38/r39 finding
under-count → R02 hunt + Ca02 sample; entry fabrication → C05 spot-checks +
R02; README byte-shape drift → C07 recompute + sweep.py at close.

## Owed

None at plan time. Pending (not owed): scout fragments K01/K02/K03 per their
target contracts; their absence triggers the fallbacks in §1.3/§4.2.

## Citations

- `reports/round-40/claims.json` — claim definitions C/Ca/A, thresholds,
  counting commands, non_goals.
- `reports/round-40/targets.json` — seat P01 mission/role/claim; all seat
  `out` paths and missions cited per seat above.
- `REGIMEN.md:13-23` — position→lane-round schedule (next-touch alignment
  41–46); `REGIMEN.md:42-43` — never force a pass (11/17/22 precedent).
- Measured commands (2026-10-19, baseline fd55e1f): linguistics count 21;
  partition census 94/25/21/23/29/24 = 216; queue 24 rows with fields
  `class,evidence,id,next_touch,origin,owner,reason,verification`;
  `reports/round-40/` contained only claims/targets/telemetry at plan time.
- `corpus/README.md:5,9-10` — rev 2.2, totals 216, footer vector
  21/23/25/29/24/94.
- `reports/round-39/scout/K01-verification-gaps.md:84,106,125,148,169` —
  G1–G4 definitions + alternates; G1 landed at r39 per README rev 2.2.
- `reports/round-37/op/defect-queue.json` — the queue being refreshed.
