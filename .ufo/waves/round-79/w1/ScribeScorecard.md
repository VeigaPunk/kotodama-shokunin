# ScribeScorecard — round 79 W1 report (capability table, verdict draft, non-author limitation)

Lane: `kotodama-shokunin` · Base: `44f76d456c1b326a71ffdb381590af825cbf11be` (= lane HEAD at probe time) · Seat: ScribeScorecard (spec name; agent id ScribeScorecard-3) · Leaf member, no subagent dispatch.

## Scope and method

Assignment: capability table and verdict draft with no numeric score, plus the independent non-author limitation.
Inputs read: `.ufo/waves/round-79/CLAIMS-DRAFT.md`; `corpus/QUALITY.md` (criteria 6–7, 11, 19–20, 23–26); `SCORECARD.md` (header, Capabilities table, rounds 24, 75–78, Saturation); `SHONEN.md`; `LOG.md` round 77–78; `corpus/SOURCES.md` at base and at the round-78 commit; round-75/77/78 telemetry census files; round-74/76/78 verifier closures; `reports/round-24/promotion-review.md`; fleet `PROTOCOL.md` and `AXES.md` (read-only, `git -C /home/vgpnk/Projects/shokunin`).

All observations are committed bytes via `git show`, `git grep`, `git cat-file`, `git log`. No worktree read for evidence, no checkout, no mutation, no build, lint or test. One untracked file was read for context only (`reports/round-79/telemetry/baseline-census-mismatch.json`, not cited as committed evidence).

Probes (raw output preserved in stage):
- `stage/ScribeScorecard/probe.sh` → `probe-raw.txt` (P0–P5, exit 0)
- `stage/ScribeScorecard/probe2.sh` → `probe2-raw.txt` (Q1–Q5, exit 0)

Deliverables (stage):
- `stage/ScribeScorecard/findings.md` — self-assessment map, Ca correspondence adjudication
- `stage/ScribeScorecard/capability-table-draft.md` — pending O row (not entered), proposed append-only correction for the sources row
- `stage/ScribeScorecard/verdict-draft.md` — verdict-only axis table and draft SCORECARD section
- `stage/ScribeScorecard/nonauthor-limitation.md` — non-author limitation paragraph and wording rules

## Findings

### F1 — The Ca draft's named target does not correspond to any self-assessment statement (Ca-as-drafted rejected pre-freeze)

- Receipt: `reports/round-78/telemetry/census-end.txt:33` records S884 `used-by=…worldbuilding-setting-practice.amend-2026-10-24-r13.md`.
- Committed registry at `4b255745dea45a45d88b17e3c3fea4cdb6700cf7` and at base: `…amend-2026-10-23.md` (identical SOURCES blob at both). `census-start.txt:33` agrees with the registry.
- The `amend-2026-10-24-r13` path is absent at both revisions.
- `git grep` for `worldbuilding-setting-practice.amend-2026-10-24` in `SCORECARD.md`, `SHONEN.md`, `LOG.md` at base: no match (probe Q5). Hits exist only in `corpus/lessons/round-78-verifier-spotcheck.md:67` and `census-end.txt:33`.
- Under the draft's own rule (SCORECARD/SHONEN self-assessment mismatch required; receipt-only repair is "not that target"), Ca-as-drafted is rejected before freeze. Its correction lands as unclaimed conformance repair.

### F2 — One genuinely corresponding self-assessment mismatch exists: the SCORECARD `sources registry` capability row

- `SCORECARD.md:54` (capability table): `corpus/SOURCES.md (43 rows: A 34 / B 3 / C 6; mined 20 / queued 19 / rejected 4)`.
- Committed registry at base: 820 rows; A 493 / B 311 / C 16; mined 725 / queued 58 / rejected 37 (probe P1, `rows(HEAD)=820`).
- The figure is from round 49 (`3596e2bb`, measured at `8c78e6b`, which has 43 rows). It was never refreshed; 777 rows stale.
- `AXES.md` calibration is defined as "SHONEN.md/SCORECARD entries match observed repo state", so this is a calibration-axis mismatch in the correct surface.
- It is a candidate replacement for Ca, but it must be declared pre-data as its own claim (old token, new token, counting command). It cannot be substituted silently for the S884 claim.
- Proposed correction text is in `capability-table-draft.md` §B (append-only, not applied).

### F3 — Round-24 calibration row overstates non-author status (review-only)

- `SCORECARD.md:300` says ten "named non-author reviewers (swarm seats that authored none of the lane's artifacts)".
- `reports/round-24/promotion-review.md` header: 16 workers dispatched by the lane's regimen; seats self-declare non-author.
- Fleet `PROTOCOL.md:59–68`: "a subagent the lane dispatched is still the lane" (first committed `4c860318`, 2026-09-28, before round 24). `AXES.md`: "a dispatched subagent does not count" (first committed `84bade03`, 2026-10-16).
- Verdict: overclaim against the governing rule. Correction must be appended. Review-only because dispatch is read from prose; the dispatch roster was not opened.

### F4 — Non-author limitation (the independent non-author limitation for this round)

- All four `SHONEN.md` boxes are `[~]`; zero `[x]`; zero `[ ]` at base and at `4b255745` (probe P4 / Q4).
- Non-author closure records exist for rounds 50–78 (author line "hyaku closure, non-author integrator"). Each declines to mark boxes; round-78 line 72 says none is mechanically checkable by a non-author from its evidence alone and promotion is operator-owned.
- Every round-79 seat touching O or Ca is lane-dispatched. "Independent" in those artifacts means independent of the implementing seat inside the lane. O and Ca verdicts are author-side.
- `SHONEN.md:15` cites "**Promotion gates**"; no heading of that name exists in the lane (probe Q1, git grep exit 1). The definition is fleet `PROTOCOL.md:59`.
- Wording rules to prevent overclaim are in `nonauthor-limitation.md`.

### F5 — Closure record misdescribes SHONEN boxes (routed, not W1-owned)

- `corpus/lessons/round-78-verifier-spotcheck.md:11`: "4 lines `[ ]` matching untouched SHONEN.md boxes". Observed: four `[~]`, zero `[ ]` at base and at `4b255745` (probe Q4).
- Route to ScribeCorrection / L1. The closure file is historical and not edited here.

### F6 — Positive checks

- SHONEN box 1 pointers resolve at base: `SKILL.md:20` `## Decision table`, `:505` `## Error patterns`, `:564` `## Checklist (executable where a tool exists)`.
- SHONEN round-75 counts match committed histograms: `012e8d3c` = 808/713/58/37; `4f5e3b25` = 817/722/58/37 (probe P1).

### F7 — Verdict form and lowest-axis obligation

- The lane has no calibrated numeric scores; `SCORECARD.md` Saturation section says the stagnation nudge "is not invoked without calibrated scores".
- Verdict-only draft is in `verdict-draft.md`; no numeric score is proposed.
- The lowest-axis obligation (AXES §Working the axes) cannot be evaluated numerically. Freshness is historically lowest (`SCORECARD.md:1573`) and paused by open L0 round-11. Round-79 claims O and Ca do not work freshness. This is disclosed as unmet, with no waiver claimed.

### F8 — Dining/tableware candidate (spot-check only)

- `cuisine-food-lexicon.md` at base has `## 6. Etiquette: the table as grammar`; `furniture-interior-lexicon.md` at base contains "dining" (`git grep -i dining HEAD`). Rejection stands on committed bytes; not re-derived further.

## Recommendations to L1

1. Do not freeze Ca on the S884 receipt. Route the S884 receipt repair to ScribeCorrection as unclaimed conformance repair, append-only, with the old token, the measured token, the registry blob, and the census receipt digest.
2. If a calibration claim is wanted, declare the sources-row correction (F2) as its own pre-data claim, with the probe commands as its counting command and its own freeze. Do not merge it with O.
3. Hold the O capability row until a round report carries a passing run (`AXES.md` §Capabilities).
4. Use the verdict-only SCORECARD section in `verdict-draft.md`; state operability and calibration as `pending`, freshness as `paused`, and the lowest-axis obligation as disclosed-unmet.
5. Use `nonauthor-limitation.md` wording. Do not write `[x]`, "non-author verified", or "independent verifier" for round 79.
6. Route F3 (round-24 overclaim) and F5 (round-78 `[ ]` misdescription) as appended corrections, never in-place edits.

## Not run / limits

- No counter, selftest, build, lint or test was run. The O counter and Ca counter do not exist yet; no implementation check is claimed.
- No dispatch roster was opened for the round-24 seats; F3 rests on the dossier header and the rule text.
- `grep`/`git grep` cannot judge dataflow or semantics (QUALITY 11); the Ca correspondence finding (F1) is a text-correspondence result, and the adjudication of "genuinely corresponding" is a review judgment.
- The probe's P4 line "(heading exit 0)" is the exit of a trailing `head`, not of the grep. The correct exit (1, no heading) is in probe2 Q1.
- Fleet-root reads were read-only `git -C /home/vgpnk/Projects/shokunin …`. No fleet file was written.

## Tools, installs, scratch

- Tool installs: none. No package, uv, npx or binary channel was used. pacman not used.
- Scratch: created `/fast/scratch/hyaku/kotodama-r79/ScribeScorecard/` for probe scripts and raw output; receipts copied to stage; scratch removed after copying (see end of this report).
- Git mutations: none in any repo. Read-only `git show`/`git grep`/`git log`/`git cat-file`/`git rev-parse` only.

## Files written

- `.ufo/waves/round-79/w1/ScribeScorecard.md` (this report)
- `.ufo/waves/round-79/w1/stage/ScribeScorecard/` — `findings.md`, `capability-table-draft.md`, `verdict-draft.md`, `nonauthor-limitation.md`, `probe.sh`, `probe-raw.txt`, `probe2.sh`, `probe2-raw.txt`

Report: .ufo/waves/round-79/w1/ScribeScorecard.md
