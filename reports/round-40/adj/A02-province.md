- Seat: A02 | executor (claim A, adjacency) | PROVINCE.md re-verified accurate at HEAD fd55e1f; contested scope routed-not-absorbed; 1 stale-prose finding filed (F-A02-1) | date 2026-10-19 | baseline fd55e1f

# A02 — PROVINCE accuracy re-verification at HEAD + contested-scope re-check

**Method.** Read-only: `git rev-parse`/`log`/`status`/`diff`/`show`, `ls`, `sha256sum`, bounded `grep`, one bounded `find` over the lore sibling (read-only). No `run-validation.py` executed anywhere; no corpus staging; no writes outside `reports/round-40/adj/A02-province.md`.

## 1. PROVINCE.md byte state at HEAD

- HEAD = `fd55e1fdfd6cc684f121fd02f32eb5cdd4c88106` — commit `fd55e1f 2026-10-19 10:37:13 -0300 round-39: admit C/Ca — verification partition 24 (216 total), isolation-replay protocol, basename-couples policy`. Matches `reports/round-40/claims.json` `baseline_commit: "fd55e1f"`.
- Working-tree `PROVINCE.md` sha256 `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` == `git show HEAD:PROVINCE.md | sha256sum`; `git diff HEAD -- PROVINCE.md` empty → **byte-accurate at HEAD**.
- Scope at verification time: `git status --porcelain` = 2 rows — ` M LOG.md` (integrator bookkeeping, in-province surface) and `?? reports/round-40/` (this round's outputs). No out-of-lane paths.

## 2. Per-clause accuracy verdicts

| PROVINCE.md | claim | check at HEAD | verdict |
|---|---|---|---|
| :9-11 Owns | six partitions `corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}` | `ls corpus/knowledge/` → exactly those six; counts 94/25/21/23/29/24 = 216, matching r40 claims.json before-state ("linguistics 21 …; total 216") | ACCURATE |
| :9-11 | "own gates, source-check records, non-canon examples and reports" | `tools/gates/`, `corpus/QUALITY.md` + 24-entry verification partition, `examples/`, `reports/` all present | ACCURATE |
| :12-14 | verification/civilizations support coupling; not general method / fleet protocol / history certification | spot-check of all 24 verification filenames (phonology-sanity-gate, naming-collision-gate, myth-consistency-gate, calibration-registry, to-verify-triage-protocol, …) — all lane-coupling surfaces; civilizations filenames are per-culture records (aegean-minoan-mycenaean, ainu, akan, …). Filename-level spot-check, not full-text | ACCURATE (spot-check) |
| :16-20 Refuses | five refuse-target lanes named | all exist as read-only siblings (`ls ../`): lore-shokunin, game-dev-2d-shokunin, game-dev-3d-shokunin, chousa-shokunin, kake-shokunin, kotoba-shokunin | ACCURATE |
| :22-25 adjacent contract | handoff format defined in the synthesis contract | `corpus/knowledge/synthesis/worldbible-integration-contract.md` present (28421 B); sha256 `5f4c02bf…f79069` — identical to the digest r37 A06/A08 verified; last commit `e1694ba 2026-10-17`; `git status` shows corpus/ unmodified → bytes unchanged since r37 | ACCURATE |
| :27-29 write scope | lane-only writes + append-only L0 questions | git scope clean (§1); sibling-write spot check `find ../lore-shokunin -maxdepth 3 -type f -newermt '2026-10-19 10:37'` → **0 hits**; L0 surface `../.ufo/l0-questions.md` exists (51 lines, 40056 B, mtime 09:14 — predates HEAD commit; no r40 append observed) | ACCURATE (spot-check: lore-shokunin only, maxdepth 3) |
| :31 | "Out of province → report, never absorb" | compliance = §3 ledger | ACCURATE |

**7/7 clauses accurate at HEAD; two marked spot-check-limited.**

## 3. Contested-scope re-check at HEAD — routed, not absorbed

| # | item | current evidence at HEAD | owner | status |
|---|---|---|---|---|
| 1 | Bilateral contract ratification / digest (OI-09) | live digest `5f4c02bf…` (re-hashed 2026-10-19, §2); kotodama read record `reports/round-33/adj/contract-read-record.md`; Lore-side record informational-only (`50c4c2f2…`, no acknowledgement: `reports/round-37/adj/A06-verify.md:41`; queue row `reports/round-37/scout/K02-defect-census.md:36`); r38 recorded it untouched (`reports/round-38/adj/A01-scope.md:58-59`); r39 grep `5f4c02bf\|50c4c2f2\|worldbible-integration-contract` → 0 hits | lore/operator/integrator | ROUTED (carried) |
| 2 | Freshness pause / operator ruling | `REGIMEN.md:32-33` (paused since round 11); `reports/round-40/claims.json` `"freshness_pause_in_force": true` + non_goals "no freshness axis-move" | operator | ROUTED (in force at r40 declaration) |
| 3 | r37 K04 corpus-boundary findings (funerary↔afterlife interface; world-end person-scope; bathing/fire; timekeeping/fire; binding-speech/kingship) | routed to integrator (`reports/round-37/adj/A06-verify.md:50`; `reports/round-37/scout/K04-entries-scout.md:50-55`); r38 grep funerary/world-end/afterlife-eschatology → 0 hits; r39 hits are filename lists in the basename-couples policy only (`reports/round-39/calib/Ca03-basename-policy.md:196-202`), no scope disposition | integrator | ROUTED (carried; queue-v2 candidates) |
| 4 | r38 K01-residue §7.1 + D01 §7.1-2 — derived_forms/derived_ok counter domain & relation | consumed at r38 integration: D01's fenced patch landed byte-exact, "corrected derived_failures formula", live counters 8/8 (`LOG.md:3725` round-38 admission, D-verified bullet); sha-move receipt note `reports/round-38/validation.json:18` | resolved-by-integration (recorded) | CONSUMED |
| 5 | r38 K01-residue §7.3 — the r7 re-freeze | still forbidden: `reports/round-40/claims.json` non_goals ("no re-freeze of declared-in-r7"); fix route drafted (`reports/round-38/op/O04-fix-route.md:5-9` — paired read-set-add + baseline-row move, `R36-R7-READSET-13`) | integrator / next re-freeze | ROUTED (owed) |
| 6 | r38 K01-residue §7.4 — era floor owner (`QREG-04.era_rule` vs machine field) | r39 grep `QREG-04\|era_rule` → 0 hits; no disposition found in r39/r40-so-far | D planner / integrator | ROUTED (carried) |
| 7 | r38 K01-residue §7.5 — RU-L5 contract exposure | unchanged; tied to #6 | integrator | ROUTED (carried) |
| 8 | r38 K01-residue §7.6 / D01 §7.6 — `13-register-law.yml:57` enforcement prose | now FINDING F-A02-1 (§4) — filed this round | integrator | FILED (r40, this fragment) |
| 9 | D01 §7.3-5 — consumer permanence, projector route, argot-gate battery registration | battery registration recorded (m15a/m15b controls, `LOG.md:3725` entry, O-verified bullet); projector alternative priced as route B in D01 §7.4; no absorbment observed | integrator / O block | ROUTED (recorded) |

**Rounds 38–40 absorbed nothing.** No canon/clearance/promotion/closure assertion found in the r38/r39 contested sweeps; r39's three "contested" hits are ordinary calibration vocabulary (`reports/round-39/scout/K01-verification-gaps.md:24`; `reports/round-39/cov/C01-entry-1.md:95`; `reports/round-39/calib/Ca03-basename-policy.md:316`), none a scope decision. Round-40-so-far: claims.json non_goals + `freshness_pause_in_force: true` maintain the posture; this seat files, decides nothing.

## 4. Finding F-A02-1 — stale enforcement prose in a delivered component (predates r40; filed here)

- `examples/culture-d4/components/13-register-law.yml:57` (`law_binding.enforcement`) asserts: *"no gate executes these rows. The era leg (RGL-05) is specified and unimplemented — tools/gates/argot-derivation-gate.py has no era concept (reports/round-26/register/rules.md section 5, RL-8)"*.
- At HEAD this is **partly false**:
  - "no gate executes these rows" — still literally true: the argot gate does not parse the component (`grep -n 'RGL\|13-register-law\|register-law' tools/gates/argot-derivation-gate.py` → only message-text and selftest-fixture hits at :689/:1034).
  - "The era leg (RGL-05) is specified and unimplemented" — **false in substance**: the landed argot gate has the "RL-8 era leg (round 38)" (`tools/gates/argot-derivation-gate.py:670-692`) grading every `register: stamp` form against `era_floor = "E1"`, emitting `D4L-ARGOT-ERA` (5 occurrences: :672, :688, :1041, :1049, :1053). Note the leg hardcodes the E1 floor rather than reading RGL-05's row — a host-adapted grader exists; the "unimplemented" claim no longer describes the ecosystem.
  - "…has no era concept" — **false**: the gate carries an in-code provenance comment for the era leg.
- Prediction + ownership on record: `reports/round-38/scout/K01-residue.md:500-503` (§7.6) named exactly this outcome with owner "the D planner — either name the component as a third artifact or leave the prose stale and record it". The staleness was **not recorded at integration**: `reports/round-38/validation.json` and `reports/round-39/validation.json` have zero `13-register-law` mentions (grep, 2026-10-19); `reports/round-38/op/O04-fix-route.md` covers only the read-set roster defect, not the prose.
- Component untouched since r27 (`git log -3 -- examples/culture-d4/components/13-register-law.yml` → `6c0ac44 2026-10-18 round-27: admit D/O/C — register law…`). The component is in the packet manifest but outside the r7 read set (`reports/round-38/op/O04-fix-route.md:15-21`; `reports/round-38/depth/D07-receipt.md:280`), so any prose fix is a packet change → owner **integrator**, natural window = the re-freeze O04 already routes (r40 non_goals forbid it now).
- **Route:** queue row (pointer to `calib/Ca01-queue-v2.md`) + integrator; NOT fixed in r40. This filing preserves claim A's "zero unfiled bleed" — the defect is now named with an owner and route.

## 5. A02 verdict for claim A (this seat's slice)

- PROVINCE.md **accurate at HEAD** (7/7 clauses; 2 spot-check-limited, marked).
- Contested scope: items #1,2,3,6,7 carried routed with owners; #4 consumed-by-integration with citations; #5 routed-owed; #9 recorded; #8 newly filed. **Zero absorbed.**
- Bleed: **zero unfiled** — F-A02-1 filed above; everything else carried with owner + route.

## Owed

- F-A02-1 queue row → `calib/Ca01-queue-v2.md` (owner integrator; fix window = next re-freeze / next declared packet-edit round).
- Sibling-write spot check covered `../lore-shokunin` only (maxdepth 3, since the HEAD commit's 10:37 timestamp); other siblings unaudited — to-verify if the integrator wants a full sweep.
- Items #6/#7 (`QREG-04.era_rule` owner; RU-L5 exposure) have no r39/r40 disposition found — carried; Ca01 should re-verify against the successor ledger before queue-v2 closes.

## Citations

- Commands (2026-10-19, this seat): `git rev-parse HEAD`; `git log -1 --format='%h %ci %s'`; `git status --porcelain | wc -l` → 2; `git diff --stat HEAD -- PROVINCE.md` (empty); `sha256sum PROVINCE.md`; `git show HEAD:PROVINCE.md | sha256sum`; `ls corpus/knowledge/` + per-partition counts (94/25/21/23/29/24); `ls corpus/knowledge/verification/` (24 files); `ls corpus/knowledge/civilizations | head -6`; `ls ../`; `ls -la ../.ufo/l0-questions.md` (51 lines, 40056 B, mtime 2026-10-19 09:14); `find ../lore-shokunin -maxdepth 3 -type f -newermt '2026-10-19 10:37'` → 0 hits; `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` → `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`; `git log -1 -- corpus/knowledge/synthesis/worldbible-integration-contract.md` → `e1694ba 2026-10-17 17:44:17 -0300`; `git log -3 -- examples/culture-d4/components/13-register-law.yml` → `6c0ac44 2026-10-18`; `sha256sum tools/gates/argot-derivation-gate.py` → `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75`; gate greps cited inline in §4.
- Lane documents: `PROVINCE.md:9-31`; `REGIMEN.md:32-33`; `reports/round-40/claims.json` (axes_in_play, freshness_pause_in_force, non_goals); `SCORECARD.md:755` (landed argot-gate sha `10c88433…`); `SCORECARD.md:464` (L0-escalation precedent); `reports/round-24/box4-province.md:22` (L0 surface precedent).
- Round records: `reports/round-33/adj/contract-read-record.md:1-9`; `reports/round-37/adj/A04-contested.md:11`; `reports/round-37/adj/A06-verify.md:41,50`; `reports/round-37/scout/K04-entries-scout.md:50-55`; `reports/round-37/scout/K02-defect-census.md:36` (OI-09); `reports/round-38/adj/A01-scope.md:58-59`; `reports/round-38/scout/K01-residue.md:481-503` (§7); `reports/round-38/depth/D01-f6-design.md:511-536` (§7); `reports/round-38/depth/D05-verify.md:70-107`; `reports/round-38/depth/D07-receipt.md:280`; `reports/round-38/op/O04-fix-route.md:5-9,15-21`; `reports/round-38/validation.json:18` (sha-note; zero `13-register-law` hits in r38/r39 validation.json by grep); `LOG.md:3725` (round-38 ADMITTED, D-verified + O-verified bullets); `LOG.md:3745` (round-39 ADMITTED).
- Round-39 sweeps: `5f4c02bf|50c4c2f2|worldbible-integration-contract` → 0 hits; `QREG-04|era_rule` → 0 hits; `funerary|world-end|afterlife-eschatology` → `reports/round-39/calib/Ca03-basename-policy.md:196-202` only; `contested` → `reports/round-39/scout/K01-verification-gaps.md:24`, `reports/round-39/cov/C01-entry-1.md:95`, `reports/round-39/calib/Ca03-basename-policy.md:316`.
- Component + gate bytes: `examples/culture-d4/components/13-register-law.yml:49,57,65-69`; `tools/gates/argot-derivation-gate.py:670-692,672,688,1041,1049,1053`.
