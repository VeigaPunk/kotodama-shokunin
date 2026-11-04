# Round 89 — re-verifying the recheck queue and an evidentiality entry

author: kotodama lane (including its dispatched seats), 2026-11-04.
Claims: F / freshness — live re-verification of the 16 URL-bearing rows of the
registry's upcoming-recheck queue; C / coverage — a dedicated entry
`corpus/knowledge/linguistics/evidentiality-epistemic-marking.md`.
Base `42816d2533c44f1d19f38a12fc5f5040d01a2fd3`; claims, counter, executed
controls, counter selftest and its red-before land together in freeze
`1cbd0efc56edaa9394e3532fc5d8ef924f122f01`; wave spec/dispatch and the
do-nothing counter runs at the freeze (F 3/5, C 2/8) land at
`9ad00be1a48d33a4f54e1663a1d46e4590cc3438`.
`reports/round-89/claims.json` (sha256 `cd74cfc2…`) and `measure89.py`
(sha256 `6bc14bcd…`) remain unchanged after data.

## Gate

Opened sources, access 2026-11-04 (America/Sao_Paulo, −03:00). Tier scope is
the exact use, not a general certificate. Two kinds of line follow, both in
the shapes `measure89.py` reads (`LOCATED_RE`, `NOTLOC_RE`, `QUOTE_RE`; every
quote ≤25 whitespace words and ≥20 characters after `norm()`):

- **F re-verification lines**, one per population id (S009 S012 S020 S021
  S031 S032 S033 S084 S104 S105 S106 S107 S142 S157 S163 S875). An advanced
  row reads `- Sxxx LOCATED recheck <old>→<new> — <url> accessed 2026-11-04:
  "<quote>" — <what still holds>`, where `<new>` is an ISO date with
  2027-02-02 < new ≤ 2027-11-05 and `<url>` is one of the row's source URLs or
  a `web.archive.org` capture of one. A row whose teaching could not be
  located reads `- Sxxx NOT-LOCATED: <observed status / reason>` and its
  recheck cell is not advanced. Each LOCATED quote occurs in a capture listed
  in `reports/round-89/rechecks/manifest.json` (sha256, 2xx, fetched_at
  2026-11-04). A 403/429/challenge was recorded as such and the Wayback
  capture tried; no challenge or login was passed.
- **C admission lines**, one per new id S936–S941 that the entry cites: id,
  row URL, 2026-11-04, tier/status decision and a double-quoted quote that
  occurs in its capture under `reports/round-89/evidence/manifest.json`.

Rows (from the executor/reviewer and evidence seats; integrated by L1):

<TBD: 16 F disposition lines from ExecRecheckA/ExecRecheckB rows.md, as re-fetched by ReviewerRefetch>

<TBD: C admission lines for S936–S94x from ScribeEvidentiality>

Registry changes: population rows change only their recheck cell; new rows
S936–S94x are additions; no other old cell changes (legs OTHERCELLS,
APPENDONLY). <TBD: final counts from registry re-derivation.>

**Known survivor, stated before data:** a capture fabricated with its quote
pasted in passes F and C (`reports/round-89/controls/controls.txt`
`F-forged-capture`, `C-forged-capture`, both rc0). The counter cannot see a
forged capture; the non-author re-fetch (ReviewerRefetch) and the closure's
re-open are the only defence and are reported separately, not as counter
evidence. <TBD: ReviewerRefetch agree/disagree tally.>

**Independent spot-check:** pending outside closure. Dispatched seats and L1
are the lane, not non-author verifiers. No promotion box becomes `[x]`.
Assimilation: none; no considerthese directory in this lane.

## Understanding and trial

F works the historically lowest non-retired axis directly: the recheck auditor
(`tools/check-sources-recheck.py --as-of 2026-11-04 --window 90`) classed 20
rows as upcoming at base (`reports/round-89/recheck-queue-base.txt`:
`RECHECK-QUEUE: 0 due / 20 upcoming / 16 on-release / 859 rows`); the four
own-work repo-path rows (S859, S860, S929, S934) are not live surfaces and are
outside the population. Re-verification means a row's teaching is still
locatable at its surface today by a quote of the re-verifier's choosing. It
does not re-certify tier, scope, or the citing entry's use, and it does not
touch the open round-11 drift-threshold question. <TBD: advanced n/16,
NOT-LOCATED ids and reasons, any surface that moved (new arXiv version,
DOI resolving to metadata only, Wayback-only).>

C adds the first dedicated entry on evidentiality — grammatical marking of
information source — and keeps it separate from epistemic modality (speaker
commitment). At base the lane held only sub-bullets in
`semantics-pragmatics.md`, `syntax-typology.md` and civilization entries. The
entry is method and design reference, NON-CANON; counted structure and source
binding are not the scholarly truth of each typological statement — the
closure's source re-open is the content check. <TBD: what L1 cut or corrected
from the scribe draft; table shape; which existing bullets now point to the
entry.>

Index: the new file makes the linguistics partition 34 on disk, so the README
heading `## linguistics/ (33)` becomes `(34)` — `tools/check-corpus-index.py`
reports `HEADER_DRIFT` when a declared partition count differs from disk —
and an appended round-89 block carries the row, `Total knowledge entries: 261`
and a footer `34/36/43/29/24/95`. Dry run over a scratch overlay:
`CORPUS-INDEX: OK files=261 rows=261 findings=0` rc0 with the bump, rc1
`HEADER_DRIFT` without it (`.ufo/waves/round-89/w1/stage/ScribeLesson/receipts/index-dryrun.txt`).

## Mistakes

| id | class | evidence | captured-by | fix or retained limit |
|---|---|---|---|---|
| R89-M1 | vacuous (prior round, repaired prospectively) | R88-V2 / R88-M2: `measure88.py --selftest` exit0 while its positive child exits1 on FileNotFoundError (`reports/round-88/counter-selftest-false-green.json`). r89: `measure89.py` selftest accepts the clean positive only on `ACCEPT-<c>-89: PASS legs=N/N` in child stdout with empty stderr (measure89.py:513), each negative only on observed rc1 plus `LEG FAIL <leg>` (:517), and keeps every child's stdout/stderr (`counter-selftest.txt.json`, 21 rows); `counter-selftest.txt` PASS 21/21 | QUALITY35, QUALITY23 | Fixed in the r89 counter at freeze, before dispatch. Red-before `reports/round-89/selftest-redbefore.txt`: BACKED forced true (mutant sha256 `80a8aa56…`) → selftest FAIL 18/21, exit1, bumponly/wrongquote/badurl BAD; ScribeLesson reproduced the same mutant hash and the same 18/21 exit1 (`.ufo/waves/round-89/w1/stage/ScribeLesson/receipts/redbefore-repro.txt`). Limits: the red-before mutates one leg only; the other legs' ability to fail rests on their negative scenarios, not on mutants; the mutant bytes are not committed (reproducible from the one-string substitution). `measure88.py` stays a historical false green. |
| R89-M2 | reference-drift (prior round, located this round) | r88 `controls/extra-id.py:11` and `controls/shotgun-all-labels.py:12`: `ROOT = KOTODAMA_ROOT or Path(__file__).resolve().parents[2]`; for `reports/round-88/controls/<c>.py`, `parents[2]` is `<lane>/reports`, so the fallback names `<lane>/reports/tools/check-attestation-packet.py`, which does not exist. Without the variable both controls score 0/13 (case rc2 `can't open file`) in the lane worktree and in a shared clone at base; with `KOTODAMA_ROOT=<lane>` extra-id scores 4/13 (`.ufo/waves/round-89/w1/stage/ScribeLesson/receipts/r88v3-controls-noenv.txt`) | R88-V3 (non-author closure); cause located by ScribeLesson | R88-V3 called the variable undocumented; it is in fact mandatory, because the fallback can never resolve a tree root. SKILL's r88 note ("otherwise depend on the live working tree or fail their fallback path") is half right: only the failure branch happens. Control bytes stay frozen; documentation notes under R88-V3 below. constant-pass and filename-only read neither the variable nor the fallback. |
| R89-M3 | reference-drift (this round) | `claims.json` `separability`: "reports/round-89/separability89.py builds both overlays from committed revisions"; `git ls-tree -r --name-only 9ad00be1 reports/round-89` (and the freeze) lists no `separability89.py` | QUALITY7, QUALITY9 (declared procedure absent when the wave was dispatched); same class as R88-V5 | Separability is not a frozen leg, so no predicate changes. <TBD: L1 either lands the script as a post-freeze, ungraded receipt generator labelled as authored after dispatch, with its overlay revisions reachable from the repo, or records that it was never built.> |

<TBD: further mistakes mined from seat reports (ReviewerCounter, CriticClaims, MutationCounter, ReviewerRefetch).>

## R88 routed-defect dispositions

| item | disposition / pointer |
|---|---|
| R88-V1 | Both r89 declared counters carry `--work <existing-dir>` (`claims.json` F/C `counter`; SCORECARD round-89 plan "Both declared commands carry `--work` (R88-V1)"). The r88 `claims.json` D `counter` still omits it (verified: `reports/round-88/claims.json` line 34) and stays frozen; the SCORECARD round-88 D row says "same counter with `--claim D`", i.e. inherits the O row's `--work`. Proposed appended SCORECARD note: "R88-V1: the round-88 D counter as declared in `reports/round-88/claims.json` exits 2 without `--work`; the valid command is `python3 -B reports/round-88/measure88.py --root <clone> --base 4956282281dac1306cfbe59523e46dde99749d75 --lands <lands> --claim D --work <existing-dir>`, the frozen declaration is not edited." |
| R88-V2 | Repaired prospectively in the r89 counter: R89-M1. QUALITY35 binds and is met at freeze; `measure88.py` not retrofitted. |
| R88-V3 | Verified and sharpened: R89-M2. Proposed text appended to the SKILL `finding-set-comparator` row's pinned-values cell (column 6; keeps 8 cells, adds no path to the entry-command cell that `tools/check-gate-registry.py` scans): `; control candidates reports/round-88/controls/shotgun-all-labels.py and extra-id.py resolve the honest auditor only through KOTODAMA_ROOT=<lane root or committed clone> — their parents[2] fallback is <lane>/reports, so without the variable they score 0/13 with case rc2, not 4/13; constant-pass.py and filename-only.py need nothing`. Proposed appended SCORECARD note (round-89 axes section, not an edit of the r88 row): "R88-V3: the round-88 counterfeit controls shotgun-all-labels and extra-id require `KOTODAMA_ROOT` set to the lane root or a committed clone when scored by `tools/check-finding-sets.py` or `measure88.py`; their `parents[2]` fallback resolves to `reports/`, so a run without it reports 0/13 (an environment miss), not a discrimination result. Receipt: `.ufo/waves/round-89/w1/stage/ScribeLesson/receipts/r88v3-controls-noenv.txt`." |
| R88-V4 | r89 wave registry (`.ufo/waves/round-89/w1/swarm-registry.json`, 11 seats) names four canonical attack seats — ReviewerRefetch, ReviewerCounter (reviewer), CriticClaims (critic), MutationCounter (mutation-tester) — 4/11; no sentinel. <TBD: delivered attack reports; any death is re-spawned or declared as a bound on the claims it grades, per R88-V4.> |
| R88-V5 | Open in a new form: R89-M3 (declared separability script absent at dispatch). <TBD: separability receipt must cite overlay revisions reachable from the repo, or ship the overlay procedure itself.> |
| R88-V6 | No action: `.ufo/waves/round-79/w1-results.json` is not cited by any r89 claim, control or receipt (no `round-79` reference under `reports/round-89/` or in `spec-v1.json` at `9ad00be1`). |
| R88-V7 | Inherited debts remain open and are not closed by this round: formal L2-planner conflict (L1 holds the planner seat; the validator rejects planner as a swarm role), numeric/lowest-axis mapping (R86-C1), full cited-record red from non-author r84, round-51/round-69 L0 questions. F moves freshness through re-verification without answering the round-11 drift-threshold question. |

## Settlement

One v1 wave (`kotodama-r89-v1`, milestone r89-v1), 11 seats: 3 executor
(ExecRecheckA, ExecRecheckB, ExecSeparability), 2 scribe
(ScribeEvidentiality, ScribeLesson), 1 scout (ScoutOverlap), 1 connector
(ConnectorSiblings), 2 reviewer (ReviewerRefetch, ReviewerCounter), 1 critic
(CriticClaims), 1 mutation-tester (MutationCounter). L1 holds planning.
<TBD: WAVE-DONE text and pointer; delivered/dead seats; replacements.>
Landed hashes and observed integration results are appended below after
measurement, not invented here:

<TBD: lands revision; `measure89.py --claim F` legs n/5 and `--claim C` legs n/8
with receipts; separability; census end; index; registry 859→<TBD>.>
