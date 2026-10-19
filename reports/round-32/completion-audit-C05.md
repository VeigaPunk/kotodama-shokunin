# Round-32 completion audit — C05 (independent re-verification)

- artifact: reports/round-32/completion-audit-C05.md
- claim: R32-C (calibration) completion criterion — auditor slot C05
- auditor: kotodama-shokunin round-32 C-completion worker slots C04+C05 (operator regimen loop 3 GLM-2, THE REGIMEN'S FINAL ROUND; 16w zai-coding-plan/glm-5.3-flash-low zai MAX)
- date: 2026-10-18; lane HEAD: 4d500501a286d96f2eea8a6188c649255581301a (`git rev-parse`, re-read 2026-10-18); baseline_revision per claims.json: 17e90b9047b289d7a63180a1dc1bebb074137e29
- target: independent re-derivation + field-by-field diff of >=6 lane rounds against reports/round-31/closure-ledger.json (the filed record under audit), from raw sources; slot C04 samples a disjoint primary set and verifies raw-only (no ledger). Sample: rounds {9, 13, 17, 22, 24, 30, 31} — includes two rejections (r17, r22), the operator-skip (r13, overlap with C04), and round 31 (overlap with C04; in-flight at the r31 audit, now closed).
- method (distinct from C04's): extractor at .scratch/r32-c0405-verify.py (`python3 .scratch/r32-c0405-verify.py C05`, 2026-10-18, raw output .scratch/r32-c05-evidence.txt) re-derives per round: report existence/bytes, `^#` section headings, hex tokens ([0-9a-f]{7,40}, non-hex-delimited) classified via `git cat-file -t` + `git merge-base --is-ancestor <h> HEAD` in the lane repo, fleet MANIFEST rounds[] row, work-commit prefix match. A second pass diffs each re-derived field (report_exists, sections_ok, cited-commit set, manifest work commit, verdict) against the row stored in reports/round-31/closure-ledger.json; any disagreement is recorded as a mismatch or as a resolution event with its own evidence.

## Per-row results (ledger diff: 6/7 rows AGREE on every compared field; 1 resolution event, below)

| round | report exists | sections (4 required) | cited commits verified | non-commit tokens | MANIFEST closure entry | work-commit match | ledger diff |
|---|---|---|---|---|---|---|---|
| 9 | true (3893 B) | 4/4 + additive "Conformance defects" heading | 2/2 commits exist + ancestor of 4d50050 | 1 (see below) | present (2026-10-17, admitted) | 9dc18ec: True | agree |
| 13 | false — adjudicated | n/a (no report owed) | n/a | n/a | present (2026-10-17, Operator-skipped, verbatim adjudication) | none named | agree (skipped-operator) |
| 17 | true (2566 B) | 4/4 + `## Round status: REJECTED on D` (line 38) | 3/3 commits exist + ancestor | 1 (see below) | present (2026-10-18, REJECTED on D) | 3dd3754207…: True | agree (closed-rejected) |
| 22 | true (2695 B) | 4/4 | 3/3 commits exist + ancestor | none | present (2026-10-18, REJECTED on D) | 0e81d9d995…: True | agree (closed-rejected) |
| 24 | true (2622 B) | 4/4 | 3/3 commits exist + ancestor | none | present (2026-10-18, admitted) | e06581b7…: True | agree |
| 30 | true (2485 B) | 4/4 | 3/3 commits exist + ancestor | none | present (2026-10-18, admitted) | 71cd9d37…: True | agree |
| 31 | true (2674 B) — landed since the ledger snapshot | 4/4 + additive amendments heading | 3/3 commits exist + ancestor | none | present (2026-10-18, close-out) | 17e90b9047…: True | resolution event (below) |

### Non-commit hex tokens classified

- `010166127` (round-9 report, line context "cl010166127, CDLI P220619 = AO 5477 Rimush bilingual"): CDLI catalog identifier — domain artifact id, not a git citation; `git cat-file -t` → not-an-object (2026-10-18). Matches the r31 audit's classification of the same token (cl010166127). No ancestry requirement applies.
- `e7ecd204` (round-17 report, "deterministic packet e7ecd204…"): packet/projector digest in prose, not a commit citation; `git cat-file -t` → not-an-object (2026-10-18). Matches the r31 audit's digest-not-commit classification.

### Round-31 resolution event (not a mismatch)

- reports/round-31/closure-ledger.json recorded round 31 `verdict: in-flight`, `report_exists: false`, MANIFEST entry absent, with `expected_resolution: "fleet report .ufo/reports/round-31/kotodama.md + MANIFEST closure entry owed at this wave's integration pass"`.
- Re-derived 2026-10-18: the report exists (2674 B, 4/4 sections), the MANIFEST closure row is present ("Regimen loop 3 GLM-1 (close-out): C/O/D verify…"), and the work commit 17e90b9047b289d7a63180a1dc1bebb074137e29 is the round-31 admission commit itself (parent of the round-32 declare 4d50050, `git log --oneline -1 17e90b9`, 2026-10-18).
- Disposition: the ledger snapshot was true at its audit time; the delta is exactly the event its expected_resolution named. Recorded as a resolution, not a ledger error; no filed artifact modified.

## Rejection and skip records (honest-harm requirement of claim C)

- r17: REJECTED on D — report heading `## Round status: REJECTED on D` (line 38) + MANIFEST notes "Regimen loop 2 build 1: REJECTED on claim D — the round-11 typed-pipeline-gate L1 leg is assemble-d2-bound and cannot consume D4 packets (boundary + re-pin recipe routed to r18). C/O verify…". grep commands 2026-10-18.
- r22: REJECTED on D — MANIFEST notes "Regimen loop 2 integrate: REJECTED on claim D — the D4 bleed-fix implementation seats were aborted mid-flight (operator interrupt); analysis/design landed with the round-25 recipe. O/C verify: six routed items resolved with controls…". The report carries 4/4 sections with the substance; LOG.md records the round-22 entry at :3300 plus an append-only correction at :3312; SCORECARD.md rows at :256-:259 carry the r22 before/after rows (O improved / C improved / D "failed as declared" / freshness-adjacency-coverage unchanged).
- r13: operator-skip on record — MANIFEST notes verbatim ("Operator-skipped: expand (Grok) rounds cancelled by operator directive 2026-10-17… no report owed for a skipped round"); report absent (ls 2026-10-18); lane reports/round-13/ holds only claims.json + targets.json.

## Observation recorded, not repaired (r22 acceptance receipt)

- reports/round-22/validation.json is absent lane-side (os.path.isfile, 2026-10-18) — the only sampled round besides r13 without one. r22's validator declares `OUTPUT = f"{ROUND_DIR}/validation.json"` (reports/round-22/run-validation.py:23), so the receipt is re-derivable from the SCORECARD-cited counting command (`python3 reports/round-22/run-validation.py`, SCORECARD.md:256-:257), and the round's O/C evidence lives in the cited artifacts (routed-resolution.json, loop2-retrospective.md, fixes/, bleed/ — ls 2026-10-18). Disposition: recorded as an observation; not run and not repaired, because r22 is a filed round (rounds 8-31 artifacts are never rewritten) and re-running would create a new artifact inside it. Criterion impact: none — the criterion's r22 requirements (content-valid fleet report, SCORECARD before-after rows, LOG entry, MANIFEST closure entry with per-axis adjudication) are all independently present.

## Criterion-edge checks (both owed by claim C's after_required)

- rounds 1-7 retro rows re-confirmed: 7/7 present in fleet MANIFEST rounds[] (rounds 1-6 type=retroactive-closure, 2026-10-17; round 7 type=closure, 2026-10-17, "terminated by operator session wrap… acceptance receipt is failing") — command: MANIFEST.json rounds[] round∈1..7 ∧ 'kotodama' in notes, 2026-10-18.
- round 32 pending-by-construction: `.ufo/reports/round-32/` contains only kumitate.md; fleet MANIFEST round-32 rows = 0 (ls + python count, 2026-10-18). r32's own report + closure entry land at this wave's integration pass — the same path that admitted round 31, documented here as the round-32-by-construction slot.
- LOG/SCORECARD traces: present for all 7 sampled rounds (grep -c "round-N\|rN", LOG min 2 / SCORECARD min 4 per round, 2026-10-18); lane validation.json present for 6/7 (r13 none owed; r22 absence dispositioned above).

## Counts (command + date)

| count | value | command | date |
|---|---|---|---|
| rounds re-verified | 7 | rounds {9, 13, 17, 22, 24, 30, 31} in this audit loop | 2026-10-18 |
| ledger field diffs (vs reports/round-31/closure-ledger.json) | 0 mismatches on 6 rows; 1 resolution event (r31) | re-derive + per-field diff (report_exists, sections, commit set, work commit, verdict) | 2026-10-18 |
| commit citations verified | 17 | [0-9a-f]{7,40} scan + git cat-file -t + git merge-base --is-ancestor vs lane HEAD 4d500501a286d96f2eea8a6188c649255581301a | 2026-10-18 |
| non-commit tokens classified | 2 (010166127 r9, e7ecd204 r17) | git cat-file -t + prose-context read | 2026-10-18 |
| MANIFEST closure entries | 7/7 | MANIFEST.json rounds[] round==N (Regimen/Operator-skipped) | 2026-10-18 |
| rejections on record | 2/2 sampled (r17, r22) | report headings + MANIFEST notes + LOG :3300/:3312 + SCORECARD :256-:259 | 2026-10-18 |
| work-commit prefix matches | 6/6 where MANIFEST names one | MANIFEST-notes token vs report-cited hashes | 2026-10-18 |
| overlap rows with C04 | 2 (r13, r31) — PASS in both slots | cross-auditor agreement | 2026-10-18 |
| rounds 1-7 retro rows | 7/7 | MANIFEST rounds[] round∈1..7 ∧ 'kotodama' in notes | 2026-10-18 |
| round-32 rows | 0 (pending-by-construction) | MANIFEST rounds[] round==32; ls .ufo/reports/round-32/ | 2026-10-18 |

## Verdict

`verify` — all 7 re-derived rows agree with the filed record: 6/7 with zero field mismatches against reports/round-31/closure-ledger.json, and round 31 as the resolution event that ledger's own expected_resolution predicted (closed at admission commit 17e90b9047b289d7a63180a1dc1bebb074137e29). Every cited commit (17 tokens across 6 filed rounds) exists and is an ancestor of lane HEAD 4d50050; both sampled rejections (r17, r22) and the operator-skip (r13) are on record with their harms stated plainly; the single new observation (r22 validation.json absent, receipt re-derivable) is recorded with a disposition, not repaired. No falsifying counter-example found. Falsification: re-run `python3 .scratch/r32-c0405-verify.py C05` plus the per-row git/ls/grep commands and the ledger diff on any sampled round and obtain a different existence/ancestry/adjudication/diff result than recorded above (2026-10-18).
