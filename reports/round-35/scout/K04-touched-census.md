- Seat: K04 | scout | claim A | date 2026-10-19 | baseline 4a7aede

# K04 — touched-surface census: everything rounds 33–34 created or edited

Deliverable for claim A ("Bleed-scope audit of the rounds-33/34 touched
surfaces"). This file is a **census**, not an audit: it names every touched
path, its owning `PROVINCE.md` line, and the cross-domain risk class the
claim-A audit seats must scan it for. No verdict is issued here.

## 0. Method (how the population was derived)

- Population = the byte-delta of the two filed rounds against their declared
  baselines, not a prose reading: r33 baseline `139e3b662900557afe54f632b468619593dc9fcb`
  (`SCORECARD.md:580`), r34 baseline `da68a6d` (`SCORECARD.md:606`).
  Command: `git diff --name-status 139e3b6 4a7aede`.
- Result: **171 paths = 160 added + 11 modified**, of which
  **13 are live/shared surfaces** (outside `reports/round-33|34/`) and
  **158 are new fragment files** (79 per round).
- Split by author: r33 authored **11** live surfaces, r34 authored **4**;
  `LOG.md` and `SCORECARD.md` are shared by both → 11 + 4 − 2 = 13.
  Commands: `git diff --numstat 139e3b6 da68a6d | grep -v reports/round-33/`,
  `git diff --numstat da68a6d 4a7aede | grep -v reports/round-34/`.
- Record cross-check: every repo path named as evidence in the r33/r34 record
  blocks (`LOG.md:3519-3646`, `SCORECARD.md:578-626`) resolves inside this
  delta; the only record-named paths outside it are the two fleet reports in
  §4 (outside the repo by design, see §5).
- All digests/sizes are HEAD readings taken 2026-10-19 with `sha256sum` /
  `wc -l`. Nothing was executed except read-only git/grep/python readers; no
  filed `run-validation.py` was run, and the guard tool's selftest was **not**
  re-run (its green claim is cited from `LOG.md:3605`, not re-verified).

## 1. Live/shared surfaces (13) — the bleed-risk set

Risk classes are defined in §6. "PROVINCE anchor" is the line the surface
claims or the line it strains against.

| # | path | by | Δ lines | PROVINCE.md anchor | risk class | HEAD evidence |
|---|---|---|---|---|---|---|
| 1 | `SKILL.md` | r33 | 35/18 | `:11` owns "this lane's own gates … reports"; strains `:20` refuses "prompt/skill craft (kotoba)" | R1, R2 | sha256 `f9bd07c2…`, 732 lines; six hunks: `:128`, `:479-491`, `:501`, `:581-584`, `:693-723`, `:730-732` (the F-X16-3 re-key) |
| 2 | `AGENTS.md` | r33 | 0/2 | not enumerated; fleet operating rules | R4 | 40 lines, `grep -c '^```'` = 0 (round-31 drafting residue excised) |
| 3 | `REGIMEN.md` | r33 | +77 (new) | not enumerated; operator-approved lane governance | R4 | 77 lines; schedule table `:11-23`, per-round contract `:27-33` |
| 4 | `SCORECARD.md` | r33+r34 | +54 (r33), 28/3 (r34) | `:27-29` (lane repo, own round reports) | R5 | r33 block `:578-602`, r34 block `:604-626`; **K04-F1 lives at `:616`** |
| 5 | `LOG.md` | r33+r34 | +93 (r33), +54 (r34) | `:27-29` | R5 | r33 admitted `:3519`, F-C13-1 `:3548`, supersessions `:3569`, operator directive `:3585`, r34 errata `:3594`, r34 admitted `:3616`; **K04-F1 at `:3635`** |
| 6 | `corpus/lessons/README.md` | r33 | 130/28 | `:9-11` owns "its records in this repo" — `corpus/lessons` is **not enumerated** | R1, R2, R5 | sha256 `f752e1d7…`; "Revision 3 — round-33 reconciliation" at `:398`; index 33 files / 33 rows |
| 7 | `corpus/knowledge/linguistics/register-lexicon-ceilings.md` | r33 | +28 | `:10` owns the linguistics partition | R1 | 317 lines; append-only "§12. Errata (round 33)" at `:291`, correcting the head block's five absence sweeps at `:4` |
| 8 | `examples/culture-d3/README.md` | r33 | 1/1 | `:11` owns "non-canon examples"; `:22-25` adjacency contract | R3 | old `50c4c2f2…` → `5f4c02bf…` |
| 9 | `examples/culture-d3/handoff.md` | r33 | 2/2 | same as #8 | R3 | two repoints (contract_ref, A-CONTRACT row) → `5f4c02bf…` |
| 10 | `examples/handoff-packet.sample.md` | r33 | 1/1 | same as #8 | R3 | repoint → `5f4c02bf…` |
| 11 | `examples/handoff-packet.sample.yml` | r33 | 2/2 | same as #8 | R3 | repoints → `5f4c02bf…` |
| 12 | `tools/exercise-handoff-e2e.py` | r34 | 11/10 | `:11` owns "this lane's own gates" | R3 | sha256 `34c85f57…`, 4613 lines; six edit sites: `CLAIMS_MAP` `:184`, v3 defaults `:1933-1934`, docstring `:2290`, manifest row `:2566`, packet prose `:2779`, `OQ-V3-05` literal `:3524-3533` |
| 13 | `tools/harness/receipt_guard_adoption.py` | r34 | +1309 (new) | `:11` | R4, R5 | sha256 `5858abcd…`, 1309 lines; selftest green per `LOG.md:3605` (not re-run here) |

Digest closure verified for the repoint set: the new example pins
`5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` equal the
live `corpus/knowledge/synthesis/worldbible-integration-contract.md` sha256, and
the same digest is the one recorded in `reports/round-33/adj/contract-read-record.md:5`.

Boundary checks that came back clean (evidence for the R3 legs):

- `git diff --name-only 139e3b6 4a7aede -- tools/gates/` → **no output**
  (frozen gate bytes untouched by both rounds).
- Under `corpus/`, only two files moved: `corpus/knowledge/linguistics/register-lexicon-ceilings.md`
  and `corpus/lessons/README.md` (no `corpus/lessons/*.md` lesson file changed).
- The renderer's before→after digest in `handoff/repin.json` row
  `R34-D-default-pointer` (`a5e4a8c5…` → `34c85f57…`) matches the live
  `sha256sum tools/exercise-handoff-e2e.py` reading.

## 2. Durable in-round artifacts (named by the records as evidence)

These are the created artifacts that outlive their round — the ones a
cross-round consumer (or a future round's pin) will read. Risk classes per §6.

| path | round | record anchor | risk class | digest / shape |
|---|---|---|---|---|
| `reports/round-34/handoff/declared-in-r7/packet.md` | r34 | `LOG.md:3609`, `SCORECARD.md:615` | R2, R3 | `45f57132…` == `freeze.txt` |
| `…/declared-in-r7/twin.json` | r34 | same | R2, R3 | `0e229138…` |
| `…/declared-in-r7/expected.json` | r34 | same | R3 | `bbe15887…` |
| `…/declared-in-r7/claims-map.md` | r34 | `LOG.md:3627` | R3 | `d181de28…` (re-frozen from `01215594…`) |
| `…/declared-in-r7/freeze.txt` | r34 | `SCORECARD.md:615` | R3 | 10 lines; records both freezes |
| `…/declared-in-r7/run.log` | r34 | `repin.json` surface row | **R3 — K04-F2** | on disk 1603 bytes; **untracked** (`.gitignore:3`) |
| `reports/round-34/handoff/repin.json` | r34 | `LOG.md:3611,3631` | R3 | `1022b603…`; 3 rows, all with controls |
| `reports/round-34/op/adoption-inventory.json` | r34 | `LOG.md:3605`, `SCORECARD.md:616` | R5 — **K04-F1** | `ceeb8d04…`; `runner_count` 28, `{17 guarded-refresh, 11 unguarded-in-place}` |
| `reports/round-34/craft/box1-resurvey-durable.json` | r34 | `SCORECARD.md:617` | R3 | `92581b2c…` (28/28 at `f9bd07c2…`) |
| `reports/round-34/craft/anchor-reissue.md` | r34 | `SCORECARD.md:617` | R3 | `cbc1c493…` |
| `reports/round-33/calib/open-items-ledger.json` | r33 | `LOG.md:3535`, `SCORECARD.md:589` | R2 | `ae35330f…`; 12 rows, 4 `fixed-with-evidence` / 8 `carried-with-owner+reason+next-touch` |
| `reports/round-33/adj/audit-assembled.md` | r33 | `LOG.md:3540`, `SCORECARD.md:590` | R2 | `9ff5d84c…`; bound HEAD `139e3b6` — see K04-F4 |
| `reports/round-33/adj/contract-read-record.md` | r33 | `audit-assembled.md` §"Lore-owned questions" | R2 | 9 lines; kotodama-side §1 read only, `scope:` line excludes lore standing |
| `reports/round-33/op/lessons-reconciliation-receipt.json` | r33 | `LOG.md:3529` | R3 | `6a42699d…`; 14 applied deltas D0–D10 |
| `reports/round-33/calib/r18-d4-adapter-successor.md` | r33 | ledger successor draft | R2 | `08040eb5…`, 16 lines |
| `reports/round-{33,34}/telemetry/*` (11 tracked files) | both | `AGENTS.md` telemetry rules | R4 | incl. `inputs/{claims,targets}.json`, `observed-dispatch.json`, `availability-close-{33,34}.json` |

## 3. Report-fragment classes (bulk, round-scoped)

Counts from `git diff --name-only <baseline> <head> | grep -c reports/round-3N/`
and a per-subdirectory breakdown of the same list:

- **r33: 79 files** — `adj/` 19, `calib/` 20, `cross/` 5, `op/` 12, `review/` 8,
  `scribe/` 5, `telemetry/` 6, root 4 (`claims.json`, `targets.json`,
  `run-validation.py`, `validation.json`).
- **r34: 79 tracked files** — `calib/` 9, `craft/` 2, `cross/` 4, `depth/` 19,
  `handoff/` 6, `op/` 11, `plan/` 2, `review/` 8, `scout/` 4, `scribe/` 5,
  `telemetry/` 5, root 4; plus **1 untracked** (`handoff/declared-in-r7/run.log`)
  → 80 on disk.

Risk class for the class as a whole: **R1/R2 at fragment level** (the r33 A08
whole-wave language scan already covered r33's fragments — 73 files, 64/64 seat
out-paths, per `audit-assembled.md` §"Full-wave language scan" — but **no
equivalent whole-wave scan covers r34's fragments**; that gap is the claim-A
audit's to close — `grep -rln "language scan\|bleed\|MENTION-EXEMPT\|UNSUPPORTED-CLAIM\|cross-domain"`
over `reports/round-34/` returns only `scribe/S04-integration-draft.md:126` (a
standing box-4 note) and `review/R03-d-review.md:354` (an advisory pointer to a
historical r22 artifact), i.e. no r34 whole-wave scan exists). File-level token
counts measured for scan sizing only
(`grep -ril`, files containing the token, r33/r34):
`canon` 56/34, `promotion` 51/12, `clearance` 34/14, `lore-shokunin` 16/3,
`game-dev` 7/0, `kotoba` 6/0, `chousa` 5/0, `kake` 5/0. These are **not**
verdicts: negation/mention/routed-reference framing is exactly what the scanner
must adjudicate (the r33 lexical-ceiling caveat, `A08-language.md:49-56`).

No affirmative promotion/clearance assertion was found by the literal probe
`grep -rl "promoted to canon\|cleared for\|clearance granted\|promotion granted"`
over both round trees → 0 files.

## 4. Out-of-repo fleet surfaces (created by the rounds, outside the lane repo)

| path | digest | lines | note |
|---|---|---|---|
| `../.ufo/reports/round-33/kotodama.md` | `25409207…` | 135 | fleet report; `PROVINCE.md:28` "its own fleet round reports"; read-only for this seat |
| `../.ufo/reports/round-34/kotodama.md` | `9b6ed0ff…` | 104 | same |

Token counts (case-insensitive) for scan sizing: `promotion` 2/2, `clearance`
1/1, `canon` 3/1, `lore-shokunin` 0/0.

## 5. Pre-baseline boundary note

`139e3b6` — round 33's own baseline commit — is itself a bookkeeping commit that
**deletes** `.ufo/reports/round-32/kotodama.md` (123 lines) from the lane repo
("fleet report belongs at the fleet root", `git show --stat 139e3b6`). So the
r33/r34 delta contains no fleet-file edit inside the repo, and the two fleet
reports above live outside it. Anything auditing "the rounds-33/34 touched
surfaces" against the repo tree should not expect them in `git diff`.

## 6. Risk classes to scan for (key for the claim-A audit seats)

- **R1 — cross-domain bleed.** Language, concepts, or authority belonging to
  another province: lore/canon (`PROVINCE.md:16-17`), general source-research
  method (`chousa`, `:20`), web publishing (`kake`, `:20`), prompt/skill craft
  (`kotoba`, `:20`), game mechanics (`game-dev-2d/3d`, `:19`).
- **R2 — ownership drift.** Promotion / canon / clearance / closure assertions
  (`REGIMEN.md:27-33` non-goals; claim A `after_required`), contested scope
  absorbed rather than routed (`PROVINCE.md:25`, `:31`).
- **R3 — pin / digest cascade and filed-byte integrity.** Superseded digests
  still cited, pins pointing at moved bytes, protected-path edits
  (`tools/gates/frozen/**`, `reports/round-1..34/**`, `corpus/lessons/*.md`),
  and artifacts named in a pin that are not actually durable (K04-F2).
- **R4 — fleet-protocol scope.** Telemetry shape, dispatch/seat counts, provider
  facts, `MANIFEST.json`/`.ufo` conventions (`AGENTS.md` telemetry rules;
  `REGIMEN.md:44-50`).
- **R5 — record ↔ artifact reproducibility.** Figures asserted in `LOG.md` /
  `SCORECARD.md` / claims that are not reproducible from the cited durable
  artifact (K04-F1).

### Census-visible candidates (evidence only — the audit seats decide)

- **K04-F1 (R5) — runner denominator 29 vs 28.** `SCORECARD.md:616` and
  `LOG.md:3635` state "29 filed runners — 18 guarded-refresh / 11
  unguarded-in-place" while citing `op/adoption-inventory.json`, which carries
  `runner_count: 28` / `{17, 11}` (`class_counts` read from the JSON) at census
  baseline `da68a6d` (`op/O02-tool-source.md:36`). At HEAD the count really is
  29 (`ls reports/round-*/run-validation.py | wc -l` → `29`) because r34's own
  runner landed and is guard-adopted (`reports/round-34/run-validation.py:514-533`).
  `LOG.md` carries both readings (`:3605-3606` 28/17; `:3635` 29/18).
- **K04-F2 (R3) — untracked frozen-set member.** `handoff/repin.json` row
  `R34-D-new-row` names `run.log` inside the frozen surface set
  `{packet.md, twin.json, expected.json, freeze.txt, run.log, claims-map.md}`;
  the file exists on disk (1603 bytes) but `git check-ignore -v` →
  `.gitignore:3:*.log`, and it is absent from `git ls-files`. repin.json's own
  `digests` map does not pin it (5 entries, no `run.log`).
- **K04-F3 (R1/R2) — PROVINCE enumeration.** Two r33-touched surfaces are not
  named in `PROVINCE.md`'s owns/refuses lists: `corpus/lessons/README.md`
  (the owns sentence enumerates `corpus/knowledge/{…}`, gates, source-check
  records, non-canon examples, reports) and `SKILL.md` (adjacent to the
  `:20` refusal of prompt/skill craft). Both edits read as in-lane by the
  records (the lessons dir is "the lane's append-only lesson record",
  `corpus/lessons/README.md:4`), but no PROVINCE line names either surface —
  scan target for the PROVINCE-accuracy leg.
- **K04-F4 (coverage gap, confirms claim A's "before").** The r33 audit's
  snapshot is bound to `HEAD 139e3b6` (`audit-assembled.md` §"Fresh scope and
  digest checks"), so all four r34 live edits (§1 #4, #5, #12, #13) and every
  §2 r34 artifact postdate it. Conversely the r33 audit already *named* two of
  them as owed (A09 SKILL receipt/anchor reissue; box-1 durable receipt) — r34
  then landed both, so those two r33 findings should now be checkable as
  closed rather than live.

## 7. What this census does not claim

- No green/named-finding verdict on any surface; that is the claim-A audit
  seats' output.
- Not a whole-wave language scan of r34 fragments (§3) — only a sized target.
- No filed runner executed; the guard tool's selftest not re-run; no bytes
  written outside this file.

## Owed: none

No dependency fragment was missing for this census. The claim-A audit seats
consume this file; nothing here is owed forward to the integrator.

## Citations

Commands (all read-only, run at HEAD `4a7aede` in the lane root):

- `git diff --name-status 139e3b6 4a7aede` (171 paths: 160 A / 11 M)
- `git diff --numstat 139e3b6 da68a6d | grep -v reports/round-33/` (r33 live set)
- `git diff --numstat da68a6d 4a7aede | grep -v reports/round-34/` (r34 live set)
- `git diff --name-only 139e3b6 4a7aede -- tools/gates/` (no output)
- `git diff --name-only 139e3b6 4a7aede -- tools/gates/ corpus/knowledge/ corpus/lessons/`
- `git diff --name-only <base> <head> | grep -c 'reports/round-3N/'` → 79 / 79
- `git ls-files reports/round-34/handoff/declared-in-r7/` (5 tracked, no `run.log`)
- `git check-ignore -v reports/round-34/handoff/declared-in-r7/run.log` → `.gitignore:3:*.log`
- `git show --stat --format="%H %s" 139e3b6` (deletes `.ufo/reports/round-32/kotodama.md`)
- `sha256sum` / `wc -l` on every path in §1–§2 (values inline)
- `ls reports/round-*/run-validation.py | wc -l` → 29
- `grep -ril` token counts over `reports/round-33/`, `reports/round-34/`, `../.ufo/reports/round-{33,34}/kotodama.md`
- `grep -rl "promoted to canon\|cleared for\|clearance granted\|promotion granted" reports/round-33/ reports/round-34/` → 0 files
- python readers over `reports/round-34/op/adoption-inventory.json`, `reports/round-34/handoff/repin.json`, `reports/round-33/calib/open-items-ledger.json`

Files read: `REGIMEN.md:1-77`; `PROVINCE.md:9-31`; `SCORECARD.md:578-626`;
`LOG.md:3519-3646`; `reports/round-35/claims.json:54-65`;
`reports/round-35/targets.json` (seat K04); `reports/round-33/adj/audit-assembled.md`;
`reports/round-33/adj/contract-read-record.md`; `reports/round-34/handoff/repin.json`;
`reports/round-34/op/adoption-inventory.json`; `reports/round-34/cross/X02-conformance.md:67-95`;
`reports/round-34/op/O02-tool-source.md:36`; `reports/round-34/run-validation.py:514-533`;
`reports/round-33/op/lessons-reconciliation-receipt.json`; `.gitignore:1-6`;
`reports/round-34/handoff/declared-in-r7/freeze.txt`; `.../run.log:1-12`.

No source outside this repo was used; nothing here is `to-verify` except the
guard tool's selftest green claim, which is cited from `LOG.md:3605` and marked
as not re-verified in §0.
