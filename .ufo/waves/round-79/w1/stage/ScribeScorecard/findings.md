# ScribeScorecard — self-assessment map and Ca correspondence (round 79, W1)

Base `44f76d456c1b326a71ffdb381590af825cbf11be` (lane HEAD = base at probe time). All observations
are committed bytes read with `git show` / `git grep` / `git log`; no worktree read, no mutation.
Raw output: `probe-raw.txt` (P0–P5) and `probe2-raw.txt` (Q1–Q5); commands in `probe.sh` / `probe2.sh`.
The probe prints `exit=0` at the end of each file; fleet-level PROTOCOL/AXES reads are read-only `git -C <fleet>`.

## 1. Registry figures: what the capability table says vs what is committed

| figure | SCORECARD capability row `sources registry` (HEAD line 54) | committed HEAD `corpus/SOURCES.md` (= `4b255745`) | source |
|---|---|---|---|
| rows | 43 | 820 | probe P1 `rows(HEAD)=820` |
| tier A / B / C | 34 / 3 / 6 | 493 / 311 / 16 | probe P1 tier histogram |
| mined / queued / rejected | 20 / 19 / 4 | 725 / 58 / 37 | probe P1 status histogram |

The row's own text names `measured at 8c78e6b` (the round-49 S leg) but the cell carries no as-of date and is
in present tense inside a table whose header says "demonstrated behavior". Introduced by `3596e2bb` (round 49,
`git log -S'43 rows'`), never refreshed; later rounds recorded the registry in per-round axis sections
(e.g. `LOG.md` round-77/78 census lines: 820 rows / A493 / B311 / C16 / mined725 / queued58 / rejected37).
Stale-row gap at HEAD: 820 − 43 = 777 rows.

## 2. SHONEN.md self-assessment

| item | statement | observed at HEAD | verdict |
|---|---|---|---|
| box 1 pointers | `SKILL.md:20` Decision table, `:505` Error patterns, `:564` Checklist | `grep -n` of `## Decision table` `:20`, `## Error patterns` `:505`, `## Checklist (executable…)` `:564` | match |
| round-75 registry counts | 808 / 713 / 58 / 37 at Ca landing; close 817 / 722 / 58 / 37 | `012e8d3c` = 808/713/58/37; `4f5e3b25` = 817/722/58/37 (probe P1) | match (dated to round 75; not claimed current) |
| box marks | four `[~]` | four `[~]`, zero `[ ]`, zero `[x]` (probe Q4) | match |
| "no non-author verifier on record" | box text, per round-51–78 closures | consistent with PROTOCOL rule (§4 below) | match |
| "per **Promotion gates**" (line 15) | names a gate with no path | no heading in the lane; the definition is fleet `PROTOCOL.md:59` (outside lane) (probe Q1, Q2) | pointer defect (minor); fix belongs to a SHONEN regeneration, not W1 |
| "operator-owned" marks wording | cited by round-24 dossier as `SHONEN.md:10-11` | not present in current SHONEN.md (probe P4) | drift; historical only |

## 3. SCORECARD round-24 calibration row (line 300)

Text: "SHONEN boxes never non-author-verified -> promotion-review dossier: boxes 1-4 each verified-with-conditions by
10+ named non-author reviewers (swarm seats that authored none of the lane's artifacts)".

- Dossier `reports/round-24/promotion-review.md` lines 3–5: "16 workers on zai-coding-plan/glm-5.3-flash-low";
  the reviewer seats are the round-24 swarm; line 32: "every seat self-declares non-author status in its artifact".
- The ten reviewer seats in the box table (r24-box1a/1b, box2a/2b, coldrun-a/b/3/4, box4-bleed/province) were
  dispatched by the lane's own regimen. See §4: the protocol says a dispatched subagent is still the lane.
- Verdict: **overclaim against the protocol** (non-author status asserted by the seats themselves). This is a
  genuine calibration mismatch between a SCORECARD entry and the governing rule, but it is review-only
  (QUALITY criterion 11): the dispatch fact is read from prose, not a counter. Correction must be appended, never
  an in-place edit of line 300 (QUALITY 7/original files append-only; SCORECARD is a historical record).

## 4. Governing rule (fleet, read-only)

- `PROTOCOL.md:59–68` (fleet HEAD): "Every `SHONEN.md` box checked by a reviewer who did not author the round's
  changes — a fresh lane or integrator review, never self-attestation; a subagent the lane dispatched is still the
  lane." Rule text first committed at `4c860318` (2026-09-28, `git log -S` on PROTOCOL.md).
- `AXES.md` (fleet HEAD): "an exploratory claim verifies only as `unprovable-but-better` with a named non-author
  reviewer on record (…; a dispatched subagent does not count)." First committed at `84bade03` (2026-10-16).
- Both predate round 24 (2026-10-18). The round-64 seat `ReviewerSHONEN.md` (lane-committed) quotes this same rule.

## 5. Ca correspondence adjudication (CLAIMS-DRAFT §Pre-freeze scope disposition)

The draft asks whether W1 finds a *genuinely corresponding self-assessment mismatch* for Ca. Findings:

- **S884 receipt mismatch (the Ca draft's named target)** — real and reproducible:
  `reports/round-78/telemetry/census-end.txt:33` records `used-by=…worldbuilding-setting-practice.amend-2026-10-24-r13.md`;
  committed registry at `4b255745` and HEAD records `…amend-2026-10-23.md` (probe P3); `census-start.txt:33` matches the
  registry; the `amend-2026-10-24-r13` path is absent at both revisions (probe P3).
  - **Does not correspond to any SCORECARD/SHONEN statement.** `git grep` for the token
    `worldbuilding-setting-practice.amend-2026-10-24` in `SCORECARD.md`, `SHONEN.md`, `LOG.md` at HEAD returns no
    line (probe Q5). The only hits are `corpus/lessons/round-78-verifier-spotcheck.md:67` and
    `reports/round-78/telemetry/census-end.txt:33`. Ca as drafted fixes a receipt, which the draft itself says is
    "evidence-record repair, not that target".
  - **Disposition: Ca-as-drafted is rejected before freeze**, consistent with the draft's own rule. Its correction
    lands as unclaimed conformance repair (ScribeCorrection), append-only, with a note that the receipt and the
    registry are the two evidence records and that no capability/axis verdict moves.
- **Candidate that does correspond: SCORECARD `sources registry` row (§1).** It is a self-assessment figure that
  disagrees with the committed registry, which is the calibration axis's own definition (`AXES.md` calibration:
  "SHONEN.md/SCORECARD entries match observed repo state"). A replacement Ca would have to be declared again
  pre-data with its own old token (`43 rows: A 34 / B 3 / C 6; mined 20 / queued 19 / rejected 4`), new token
  (820 / A493 / B311 / C16 / mined725 / queued58 / rejected37 at the frozen revision) and its counting command
  (probe.sh P1), and it must not be silently substituted for the S884 claim (QUALITY 25 — constants from the freeze).
- Also a candidate, review-only: round-24 line 300 (§3). Correcting it is a second, separate calibration move.

Recommendation to L1: do not freeze Ca on the S884 receipt. If a calibration claim is wanted this round, declare
the sources-row correction (§1) as its own pre-data claim with the probe commands as its counting command, and keep
the S884 receipt repair as an unclaimed ScribeCorrection row.

## 6. Other observed defects routed (not W1-owned)

- `corpus/lessons/round-78-verifier-spotcheck.md:11` states "4 lines `[ ]` matching untouched SHONEN.md boxes". At
  HEAD and at `4b255745` SHONEN.md has four `[~]` lines and zero `[ ]` (probe Q4). The closure record misdescribes
  the boxes. Route to ScribeCorrection/L1; the closure file itself is historical and is not edited here.
- Round-78 verifier routed defect 2 (S884 `used-by`) and defect 3 (R78-M1 red-before) remain open per that closure.
- The untracked file `reports/round-79/telemetry/baseline-census-mismatch.json` (lane working tree, `??`) carries the
  same S884 finding with `mismatches: 1`. It is not in W1's write scope; read only, not cited as committed evidence.

## 7. Dining/tableware candidate (CLAIMS-DRAFT line 5)

Spot-check only: `corpus/knowledge/culture-material/cuisine-food-lexicon.md` at HEAD has `## 6. Etiquette: the table as
grammar` (git show HEAD, lines 88–93 read); `furniture-interior-lexicon.md` at HEAD contains the word "dining"
(`git grep -i dining HEAD`, first hit at line 3). The rejection stands on the committed bytes; not re-derived further.
