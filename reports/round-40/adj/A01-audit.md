- Seat: A01 | executor | claim A | date 2026-10-19 | baseline fd55e1f

# A01 — consolidated adjacency audit, rounds 37–40 (self-censused; K01 reconciliation owed)

**Scope.** Claim A requires a consolidated census of every artifact rounds 37–40 created
or edited, per-surface verdicts, PROVINCE re-verified, zero unfiled bleed
(`reports/round-40/claims.json:25-30`). K01's census fragment had not landed at this
seat's scan time, so this audit builds its own census from git evidence; reconciliation
against `scout/K01-touched-census.md` is filed under Owed. Method follows the r37
audit precedent (`reports/round-37/adj/A11-audit-draft.md`, `A02-entries-bleed.md`).

**Snapshot.** `git rev-parse HEAD` → `fd55e1fdfd6cc684f121fd02f32eb5cdd4c88106`, the
declared baseline (`reports/round-40/claims.json:7`). Working tree at audit time:
`git status --porcelain -uall` → ` M LOG.md` (uncommitted operator-amendment append,
`LOG.md:3763-3769`) plus untracked `reports/round-40/` (5 files at scan: claims.json,
targets.json, telemetry/dispatch-declared.json, plan/P01-plan.md, cross/X01-trades.md)
and this fragment. `git status --porcelain PROVINCE.md` → empty; last commit touching
PROVINCE.md is `c53782a` (pre-r33) — byte-clean at HEAD. The r37–r39 window is exactly
`git diff --name-status 57c8409..fd55e1f` (r36-close → r39-close). All commands run
2026-10-19, repo root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

## 1. Per-surface verdicts — round 37 (commits fa90c77, 9bccc9b; baseline 57c8409)

| Surface | Verdict | Evidence |
|---|---|---|
| `reports/round-37/**` wave tree (adj ×12, calib ×17 incl. `recount-ledger.json`, op ×13 incl. `defect-queue.json`, cross ×5, review ×8, scribe ×5, scout ×4, plan ×2, claims/targets/run-validation.py/validation.json, telemetry ×6) | GREEN — in-lane, declared | `git show --stat fa90c77`; `ls reports/round-37/*`; commit lands only `reports/round-37/`, `LOG.md`, `corpus/README.md` |
| `reports/round-37/op/defect-queue.json` | GREEN — 24 rows, matches the filed claim | python json count → `defect-queue rows: 24`; `LOG.md:3710-3712` "24-row defect queue" |
| `reports/round-37/calib/recount-ledger.json` | GREEN — 34 rows, matches filed "34-row verify recount (25 match / 5 mismatch / 4 could-not-reproduce)" | python json count → `recount-ledger rows: 34`; `LOG.md:3706-3709`; the 4 c-n-r rows were re-dispositioned at r39 (see §3) |
| `corpus/README.md` −2 lines (removal of two `__E3_PLACEHOLDER__` lines) | GREEN — integrator repair, recorded in-round | `git show fa90c77 -- corpus/README.md` shows exactly the two placeholder deletions; `LOG.md:3713-3716` records the r35 apply defect and repair; sweep re-verified green by this seat (§5) |
| `LOG.md` +22, `SCORECARD.md` +18 (fa90c77) and `SCORECARD.md` +18 (9bccc9b r37 axes table) | GREEN — lane bookkeeping, append-style | `git show --stat fa90c77`, `9bccc9b`; `SCORECARD.md:668` r37 admitted row |
| `reports/round-37/telemetry/availability-close-37.json` | GREEN — closing snapshot filed after validation.json landed (AGENTS.md duty) | `ls reports/round-37/telemetry/`; `LOG.md:3722` |
| fleet `.ufo/reports/round-37/kotodama.md` | GREEN — exists at fleet root (read-only check; never edited by this lane seat) | `ls ../.ufo/reports/round-37/kotodama.md` |

## 2. Per-surface verdicts — round 38 (commit dfb0719; baseline 9bccc9b)

| Surface | Verdict | Evidence |
|---|---|---|
| `tools/gates/argot-derivation-gate.py` +186/−2 | GREEN — declared artifact; conformance recorded | pre-declared at `reports/round-38/claims.json:17`; `LOG.md:3731-3735` selftest 39/39, live counters 8/8, zero pins moved; in-lane (this lane's own gates, `PROVINCE.md:9-11`) |
| `tools/exercise-handoff-e2e.py` +60 | GREEN — manifest-roster guard; r7 chain unchanged | `LOG.md:3736-3738` r7 chain exit 0, packet sha `45f57132…` byte-identical; guard is render-time, zero freeze bytes moved |
| `examples/**` (all freeze/ packet bytes) | GREEN — untouched across r37–r39 | `git diff --stat 57c8409..fd55e1f -- examples/` → empty output; no re-freeze performed (absolute rule respected) |
| `reports/round-38/**` (46 files incl. telemetry `availability-attempt-1.json` + `availability-close-38.json`) | GREEN; the grok-403 → devin route is a **named deviation, recorded** | `git show --stat dfb0719` ("46 files changed"); `LOG.md:3728-2730` route record; telemetry attempt+close pair present (`ls reports/round-38/telemetry/`) |
| `reports/round-38/op/O07-scribe.md` = 0 bytes | NAMED FINDING (pre-recorded, carried) — still 0 bytes at HEAD | `git show --stat dfb0719` shows `O07-scribe.md \| 0`; `LOG.md:3739-3740` "O07's 0-byte fragment recorded"; not new bleed, stays in queue lineage |
| `LOG.md` +20, `SCORECARD.md` +18, fleet `.ufo/reports/round-38/kotodama.md` | GREEN | `git show --stat dfb0719`; `ls ../.ufo/reports/round-38/kotodama.md`; `SCORECARD.md:746` |

Note: r38's claim text said "the two named tool/example artifacts"
(`reports/round-38/claims.json:16`) but as-landed only `tools/` changed — `examples/`
diff is empty. Recorded as-landed; no undeclared file was touched, so no violation.

## 3. Per-surface verdicts — round 39 (commit fd55e1f; baseline dfb0719)

| Surface | Verdict | Evidence |
|---|---|---|
| `corpus/knowledge/verification/` +4 entries (append-only-record-verification, contact-strata-verification-gate, index-sweep-verification, worked-example-verification) | GREEN — audited pre-landing 4/4 PASS; adjacency re-checked by this seat | `reports/round-39/cov/C05-audit.md:46` "4/4 PASS"; head-block fields present per entry (topic / gap filled / sources — head reads, 2026-10-19); partition count 24 (`ls corpus/knowledge/verification/ \| wc -l`) |
| Language scan of the 4 new entries | GREEN — zero refused-domain hits; canon routed, never claimed | grep over the 4 files for game dev / web publish / prompt engineer / kotoba / kake / ownership-of-canon → 0 hits; each entry states "canon belongs to lore-shokunin" (e.g. `append-only-record-verification.md:3` tail) |
| Couples resolution of the 4 new entries | GREEN — 12/12 distinct file refs resolve, NONE dangling | corrected python check (first run had a base-path bug producing 5 false positives; corrected run: `distinct refs checked: 12 \| dangling: NONE`, output 2026-10-19); the eleven r35/r36 entries' 334/334 resolution stands from r37 (`reports/round-37/adj/A02-entries-bleed.md:7`) |
| `corpus/README.md` rev 2.2 (verification 20→24, totals 212→216, footer `21/23/25/29/24/94`) | GREEN — sweep re-run by this seat: `rows 216 files 216`, `totals_ok True`, `footer_ok True`, `missing_from_index 0`, `orphan_rows 0`, exit 0, `readme_sha256 e73dc971…` | `python3 -B reports/round-28/readme/sweep.py` output 2026-10-19 (this is the r28 instrument, not a round runner); `corpus/README.md:5-11,518,522` |
| In-round bleed event: a seat's stray `corpus/knowledge/verification/C03-draft.md` | RESOLVED, on the record — removed at integration, digest-proven; absent at HEAD | `LOG.md:3748-3752`; partition listing shows 24 files, no C03-draft (`ls corpus/knowledge/verification/`) |
| `reports/round-39/**` (protocol `isolation-replay-protocol.md`, `basename-couples-policy.md`, `recount-ledger-successor.json` = 4 rows re-dispositioning the r37 c-n-r rows, cov/calib/scout/scribe/review fragments, run-validation.py, validation.json, telemetry ×6) | GREEN — in-lane; no in-tree runner execution by this seat | `git show --stat fd55e1f`; python count → `successor rows: 4`; `LOG.md:3753-3758`; this seat ran no `reports/round-*/run-validation.py` and no replay |
| `reports/round-39/telemetry/availability-close-39.json` | GREEN — closing snapshot filed | `ls reports/round-39/telemetry/`; `LOG.md:3760` |
| `LOG.md` +18, `SCORECARD.md` +17, fleet `.ufo/reports/round-39/kotodama.md` | GREEN | `git show --stat fd55e1f`; `SCORECARD.md:764`; `ls ../.ufo/reports/round-39/kotodama.md` |

Carried finding (route, do not absorb): r39's filed instrument row I-C05 cites its
resolver at `.scratch/c05/c05-audit.py` with a filed sha256
(`reports/round-39/cov/C05-audit.md:30`) — the digest is durable but the artifact is
not (`.scratch` is ephemeral). Any future re-verification of that resolver would need
the bytes. Route to defect-queue-v2 with owner+reason+next-touch.

## 4. Per-surface verdicts — round 40 in-flight (working tree at audit time)

| Surface | Verdict | Evidence |
|---|---|---|
| `reports/round-40/{claims.json,targets.json,telemetry/dispatch-declared.json,plan/P01-plan.md,cross/X01-trades.md}` + this fragment | GREEN by construction — declared out-paths only; wave in progress | `find reports/round-40 -type f` output 2026-10-19; `reports/round-40/targets.json` shared_rules |
| `LOG.md` uncommitted append (operator amendment 7, `LOG.md:3763-3769`) | GREEN — in-province, append-only, records an operator directive; **uncommitted at audit time** | `git diff LOG.md` (only hunk); owner: integrating parent commits it with the round |
| Everything else in the tree | GREEN — zero unfiled bleed | `git status --porcelain -uall \| grep -v round-40` → only ` M LOG.md` |

Scout fragments (`scout/K01-touched-census.md`, `K02-queue-scout.md`, `K03-gaps.md`)
and the remaining seats had not landed at this seat's scan; absence at scan time is
recorded, not treated as a defect (same-wave concurrency, r37 A11 precedent).

## 5. Cross-cutting verdicts

- **Ownership:** every r37–r40 path in the census is inside this lane repo under
  PROVINCE-owned categories — `corpus/knowledge/verification/` (owned partition,
  `PROVINCE.md:10`), `corpus/README.md`, lane tools (`tools/gates/`,
  `tools/exercise-handoff-e2e.py`), round report trees, lane LOG/SCORECARD, fleet
  `.ufo` reports (parent-filed, read-only to seats). Zero census paths under
  `corpus/lessons/`, `tools/gates/frozen/`, sibling repos, or the world bible.
- **Language scan (partition-wide):** grep over `corpus/knowledge/verification/` +
  README for game-mechanics / web-publishing / prompt-craft / rights-attribution /
  canon-ownership patterns → all hits are *routing* statements ("goes to chousa",
  "canon belongs to lore-shokunin", "no sibling or canon writes"), i.e. conformant
  with the PROVINCE refuses (`PROVINCE.md:16-20`); zero ownership claims. The r39
  entries themselves: 0 hits.
- **PROVINCE re-verified (this seat's slice):** PROVINCE.md is byte-clean at HEAD
  (empty porcelain status; last touched pre-r33 at `c53782a`); the load-bearing
  handoff-contract file `corpus/knowledge/synthesis/worldbible-integration-contract.md`
  does not appear in the r37–r39 diff census — untouched. Deep semantic
  re-verification is seat A02's assignment.
- **Contested scope:** nothing in r37–r40 absorbed contested scope — the r37
  freeze-drift adjudication and contract-digest question were verdict-filed and
  routed (`reports/round-37/adj/A01-freeze-adjudication.md`, `A04-contested.md`;
  r38 landed the detector, explicitly "naming-not-detection", no re-freeze).
- **Corpus state vs claim C:** the README/counts recorded here (linguistics 21,
  total 216, rev 2.2) are the **before**-state for r40 claim C's 21→25 / 216→220
  move; the sweep receipt in §3 is that before-state's evidence.
- **Process boundaries:** this seat executed no `reports/round-*/run-validation.py`,
  no replay, no re-freeze, no git mutations, no corpus staging; all corpus evidence
  is read-only.

**Consolidated verdict:** every touched surface of rounds 37–40 is verdict-filed
above; zero unfiled bleed at audit time. The two historical bleed events in the
window (r37 `__E3_PLACEHOLDER__` pair; r39 stray `C03-draft.md`) were found, recorded,
and repaired in their own rounds and remain on the record as filed — not smoothed.

## Owed

- `reports/round-40/scout/K01-touched-census.md` — same-wave dependency; reconcile
  K01's path+risk census against §1–4 at integration; route risk-class disagreements
  to X00/integrator.
- r40 claim-Ca / defect-queue-v2: carry the `.scratch/c05/c05-audit.py` durability
  row (digest filed, bytes ephemeral) with owner+reason+next-touch.
- `reports/round-40/adj/A02-province.md` — deep PROVINCE semantic re-verification
  (this audit covers byte-cleanliness and census-level conformance only).
- `reports/round-40/adj/A03-verify-assembly.md` — independent verification of this
  seat's commands and verdicts before the integrator finalizes claim A.
- Integrator: commit the `LOG.md:3763-3769` amendment-7 append with the round; file
  the fleet `.ufo/reports/round-40/kotodama.md`; this fragment is not an admission,
  canon, clearance, promotion, or closure verdict.

## Citations

- `reports/round-40/claims.json:25-30` (claim A scope/threshold), `:7` (baseline
  fd55e1f); `reports/round-40/targets.json:4-9` (shared rules), `:124-130` (A01 seat).
- `PROVINCE.md:9-11` (owns partitions + lane gates), `:16-20` (refuses), `:23-24`
  (handoff contract), `:27-29` (write scope).
- `LOG.md:3705-3722` (r37 admitted entry: 34-row recount, 24-row queue, placeholder
  repair, telemetry close), `:3727-3742` (r38: deviation route, selftest 39/39, r7
  packet unchanged, O07 0-byte), `:3747-3760` (r39: 4/4 PASS, stray C03-draft removal,
  successor ledger, telemetry close), `:3763-3769` (amendment 7, uncommitted).
- `reports/round-37/adj/A11-audit-draft.md:5-27` (method precedent);
  `reports/round-37/adj/A02-entries-bleed.md:7,46` (334/334 couples, 0 language-predicate
  hits for the eleven).
- `reports/round-38/claims.json:16-17` (the two declared artifacts);
  `reports/round-39/cov/C05-audit.md:46` (4/4 PASS), `:30` (I-C05 `.scratch` resolver
  digest — durability finding).
- `corpus/README.md:5-11,518,522` (rev 2.2, 216 total, footer 21/23/25/29/24/94).
- Command outputs (2026-10-19, repo root, `TMPDIR=$PWD/.scratch`
  `PYTHONDONTWRITEBYTECODE=1`): `git rev-parse HEAD` →
  `fd55e1fdfd6cc684f121fd02f32eb5cdd4c88106`; `git status --porcelain -uall` →
  ` M LOG.md` + `?? reports/round-40/` (5 files at scan); `git status --porcelain
  PROVINCE.md` → empty; `git log --oneline -3 -- PROVINCE.md` → c53782a/a527120;
  `git diff --name-status 57c8409..fd55e1f` (full census; only in-lane paths);
  `git diff --stat 57c8409..fd55e1f -- examples/` → empty; `git show --stat fa90c77`,
  `9bccc9b`, `dfb0719`, `fd55e1f`; `git show fa90c77 -- corpus/README.md` (two
  placeholder-line deletions only); python json counts → defect-queue 24 rows,
  recount-ledger 34 rows, successor 4 rows; corrected couples check → 12 refs, NONE
  dangling (first run's 5 dangling were a checker base-path bug, discarded);
  language greps over the 4 r39 entries and the verification partition → 0 ownership
  hits, all canon/chousa mentions routing-language; `python3 -B
  reports/round-28/readme/sweep.py` → `rows 216 files 216`, `totals_ok True`,
  `footer_ok True`, exit 0, `readme_sha256 e73dc971c80207640c90eb671e738a24f2e02561245336f75fb6d5220240181a`;
  `ls reports/round-{37,38,39}/telemetry/` → close snapshots present for all three;
  `ls ../.ufo/reports/round-{37,38,39}/kotodama.md` → all exist;
  `find reports/round-40 -type f` → 5 files at scan. No round runner, no replay, no
  re-freeze, no git mutation, no corpus staging executed.
