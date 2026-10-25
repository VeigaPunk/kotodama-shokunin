# ScribeWaveSummary — round 71, wave 1 (scoped findings)

Seat: `L1Kotodama71.ScribeWaveSummary` (leaf scribe, UFO-FSD). Date: 2026-10-25.
Role note: this seat runs concurrently with the wave; it did not review 10 finished sibling
reports (per the assignment's own amendment) — instead it produced the wave-summary template and
the round-71 lesson skeleton, grounded in the 23 seat reports already on disk at its stamp, the
frozen claims (`reports/round-71/claims.json`), the control receipts, and the census baseline.

## Deliverables

1. Template + lesson skeleton: **`/tmp/kotodama-round71-lesson-skeleton.md`** (Part A: wave-summary
   template; Part B: `corpus/lessons/round-71.md` skeleton with the exact `## Gate` / `## Mistakes`
   / `## Corrections` / `## Quarantine` shapes, the census/SOURCES before-after block per
   `/home/vgpnk/Projects/shokunin/CORPUS.md` §SOURCES.md, the explicit reject-sweep line
   `rejected this round: <sweep>`, and a reason+flip candidate table; Part C: L1 filling checklist).
2. This report (scoped findings + wave evidence files to commit).

## Behavior performed

- Read: `reports/round-71/claims.json` (frozen), `/home/vgpnk/Projects/shokunin/CORPUS.md`,
  `corpus/lessons/round-70.md`, `round-69.md`, `round-67.md` (shape precedent), wave
  `spec.json`/`assignments.json`, telemetry `controls-{c,ca,d}.txt`, `census-start.txt`, and 19 of
  the 23 landed seat reports; `git status --porcelain` (read-only) for the untracked evidence set.
- Wrote: `/tmp/kotodama-round71-lesson-skeleton.md` and `.ufo/waves/round-71/w1/ScribeWaveSummary.md`.
- No lane bytes mutated besides this report; no tools installed; no pacman transaction.

## Wave evidence status at stamp

- Dispatch: spec items = assignments entries = **37** seats (validated by script).
- Landed: **23** seat reports on disk; pending: `ScoutOpenSourcesC`, `ConnectorSiblings`,
  `ReviewerTrendClaimCrosscheck`, `ScribeWaveSummary` (self). Dead: 0 observed.

## Findings digest (verified from landed reports)

| # | finding | source seat |
|---|---|---|
| F1 | Census BEFORE: 784 rows, malformed 0, tiers A=474/B=298/C=12, status mined=689/queued=58/rejected=37, no dup ids, no enum/inflation, validate exit 0 with W04=28 | ScoutCensusBaseline, CritRegistrySweep |
| F2 | Claim-C gap holds: 0 filename owners, 0 topic-line owners (single raw grep hit is `danc`⊂"avoidance" false positive); nearest partial owners masks-masquerade / dress-through-eras / gesture-co-speech-pointing | ScoutDanceOwners |
| F3 | V70-1..V70-5 ground truths all CONFIRMED absent/wrong: no 17/19 headers on six round-70 receipts; S860 verify-at wrong blob/revision pair (blob 6a314e9c first exists at acc2d614, not 6cb51a4); round-70 Gate quote = 27 words; fleet report grades expansion/discernment improved; round-70 lesson has no reject-sweep statement | RevCaDefectGroundTruth, RevRound70Gate |
| F4 | D counter draft behaves to target: in-repo SELFTEST 2/2 exit 0; no-git archive SELFTEST COULD-NOT-EVALUATE exit 2; frozen data predicate 8/8 exit 0; **freeze caveat**: counting command archives 453676a2 where the counter file is absent — archive revision must be the freeze commit | ExecDCounterStub |
| F5 | No-git guard false-positive class: any `git rev-parse --git-dir` failure (e.g. `GIT_DIR=/definitely/missing`) is classified "no git" → exit 2; fix: probe object store 793f797:SKILL.md or distinguish absence from git failure | CritNoGitHypothesis |
| F6 | Ca receipt grep leg is necessary-not-sufficient: grep counts 6 on a header whose original bytes were deleted; RECEIPTS leg must pair the 6-line grep with marker + sub-marker nonempty bytes (L1–L4) | MutReceiptHeader |
| F7 | Counter-vacuity: C has no substance leg (entry could cite 12 rows with zero coverage); Ca command greps round-71 telemetry paths, not the six round-70 receipts V70-1 names — must name exact round-70 paths; D in-repo case cannot vacuously exit 2 | CritVacuousCounters |
| F8 | Gate battery green: battery 7/7 exit 0, baselines 20/20, coverage 10/10; check-cited-lines 26/26; gate-quotes 52/52; row-fragments 10/10 | ReviewerGateBattery |
| F9 | Gate-quotes: all 5 mutants killed (incl. cap-27, V70-3 class); settlement-checker: M1/M2/M4 killed, **M3 survived** (dropping a test case shifts 10/10→9/9 exit 0) — count-drift hole | MutGateQuotes, MutSettlementChecker |
| F10 | No credential/private-host material in round-71 evidence | SentinelCredentialScan |
| F11 | Write-scope gaps: ScoutQuarantineFetch1/2/3, RevQuarantineCrossCheck, ScoutPackageIdMap read /home/vgpnk/Projects/shokuknow; ConnectorSiblings scans sibling lanes; ScoutCensusBaseline runs fleet-root scripts — all read-only but outside the allowlist | SentinelWriteScope |
| F12 | Staged-id map: 132 staged rows S859–S990; collisions S859/S860; document-keyed lane map at `.ufo/waves/round-71/assimilation/id-renumber-map.json` (scratch twin `/tmp/kotodama-package-id-map.json`) | ScoutPackageIdMap |
| F13 | Claims.json parses; 3 claims, distinct axes; counting commands bash -n clean; no fidelity defects | ExecClaimsJsonFidelity |

## Wave evidence files that must be committed

Seat reports in `.ufo/waves/round-71/w1/` (37 total: 23 on disk + 4 pending incl. this report):
CritNoGitHypothesis, CritQuarantineDesign, CritRegistrySweep, CritVacuousCounters, ExecCaCounterStub,
ExecClaimsJsonFidelity, ExecDCounterStub, ExecDraftEntryShell, MutGateQuotes, MutReceiptHeader,
MutSettlementChecker, RevCaDefectGroundTruth, RevDanceEntryShape, ReviewerGateBattery, RevRound70Gate,
RevSOURCESRowShape, ScoutCensusBaseline, ScoutDanceOwners, ScoutPackageIdMap, ScoutQuarantineFetch1,
ScoutReadmeFrontier, SentinelCredentialScan, SentinelWriteScope, ScoutOpenSourcesC, ConnectorSiblings,
ReviewerTrendClaimCrosscheck, ScribeWaveSummary (all `*.md`).

Other wave-1 artifacts (untracked, commit after L1 freeze):
- `reports/round-71/accept-d.py`, `reports/round-71/accept-ca.py` (counter drafts — freeze first;
  include the L1–L4 receipt leg in accept-ca.py).
- `.ufo/waves/round-71/assimilation/id-renumber-map.json`.
- `reports/round-71/telemetry/quarantine-verdicts.md` (21 rows, nonempty verdict labels) and
  `reports/round-71/telemetry/census-end.txt` and `corpus/lessons/round-71.md` are land-stage
  outputs the claims require — produced by the L1, not wave evidence.
- Already committed (do not re-add): `claims.json`, `telemetry/controls-{c,ca,d}.txt`,
  `telemetry/census-start.txt` (825b78a); wave spec/plan/dispatch/registry (b694afd6).

## Out-of-scope (checked, untouched)

Frozen `reports/round-69/accept-d.py` (sha256 c41ffbc8… = 453676a2); `/home/vgpnk/Projects/shokuknow`;
fleet scripts/templates; `.ufo/state`; `.ufo/watchdog.log`; `MANIFEST.json`; `.scratch`; sibling
lanes; lane jj/git state. No pacman transactions; no tool installs.

## Known limits

- Findings F1–F13 are sourced from sibling reports and my own reads; I did not re-run the
  experiments (scribe role).
- The lesson skeleton's `<S###>` rows and `<sweep>` name are placeholders until ScoutOpenSourcesC
  lands; the reject-sweep line is authored lowercase at column 0 so claim Ca's `grep -cE
  '^(reject|rejected)'` leg matches.

Report file: /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-71/w1/ScribeWaveSummary.md
