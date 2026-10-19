- Seat: X03 | critic | cross | date 2026-10-19 | baseline 4a7aede

# X03 — protocol critique (round 35)

Scope: the four protocol legs my mission names — distinct axes, lowest-axis
rule (coverage), one-batch shape, thresholds checkable. All measurements
re-run at HEAD `4a7aede` on 2026-10-19 from the repo root with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. No axis-move claim of
my own; this fragment feeds the integrator's validator-leg spec (S04/O08) and
the round record. Findings are severity-ranked with owners.

## Leg 1 — distinct axes: PASS

- Declared claim axes: C = coverage (claims.json:22), O = operability
  (claims.json:39), A = adjacency (claims.json:56) — three claims, three
  distinct axes, all members of the SCORECARD axis set
  (depth, coverage, operability, freshness, calibration, adjacency —
  SCORECARD.md:3).
- `axes_in_play` equals the claim-axis vector exactly:
  `["coverage","operability","adjacency"]` (claims.json:17).
- Claim count 3, inside REGIMEN's 1–3 (REGIMEN.md:27).
- Freshness pause respected: zero freshness claims in the declaration
  (command 1: regimen-2 axis census); the non-goal restates the pause
  (claims.json:68) and the pause flag is declared (claims.json:19).

## Leg 2 — lowest-axis rule (coverage): PASS under the standing "lowest non-paused" reading; residual named

- Rule text: "At least one claim works the lane's lowest non-retired axis
  unless the stagnation nudge is invoked and recorded" (REGIMEN.md:30–31).
- claims.json's reasoning: "Coverage has zero regimen-2 claims and is the
  least-worked non-paused axis; claim C works it" (claims.json:18).
- Checkable and true at declaration. Regimen-2 axis-move census *before* r35:
  operability 2 (r33 O, r34 O), calibration 2 (r33 C, r34 C), depth 1 (r34 D),
  adjacency 1 (r33 A), coverage 0, freshness 0 (paused) — coverage was the
  unique zero on a non-paused axis (command 1; per-round axes from
  reports/round-33/claims.json and reports/round-34/claims.json).
- Continuity is on record: r34 declared "depth and coverage have zero
  regimen-2 claims; … coverage is intentionally deferred to a later round"
  (reports/round-34/claims.json `lowest_axis_reasoning`); r35 is that
  deferred round, so the "least-worked" claim is a carried commitment, not a
  fresh post-hoc choice.
- Precedent consistent across the regimen: r33 worked "the least-worked
  [non-paused]" = adjacency; r34 worked depth (tied lowest); r35 works
  coverage. No stagnation nudge invoked in any of the three (checked: the
  string "stagnation" appears nowhere in r33/r34/r35 claims.json — command 2).
- Residual (owner: operator; not a round defect): freshness is non-retired
  (SCORECARD.md:698–701, "No retirement") and historically the lowest axis
  (SCORECARD.md:14–15), but its axis-move claims are paused by operator
  ruling since r11 (claims.json:19; REGIMEN.md:31–33). The literal rule is
  therefore satisfied only under the lane's standing "lowest non-paused"
  substitution.
  Three rounds of precedent make the reading stable, but it has never been
  formally restated by the operator; recommend the round record (or the
  loop-1 retrospective) cite the substitution explicitly rather than leaving
  it in claims.json prose. Note also the ordering among non-paused axes is a
  proxy (regimen-2 claim count), not a calibrated scalar — SCORECARD itself
  records that "defining a calibrated numeric rubric remains an explicit
  protocol-conformance gap" (SCORECARD.md:13–14). The proxy is decisive here
  (0 vs 1), so the leg passes; the rubric gap stands unchanged.

## Leg 3 — one-batch shape: PASS; two observations filed

- Declared size 64, one batch: `requested_workers` 64, `batched_calls` 1
  (claims.json:13–14); `seat_count` 64 with exactly 64 seat objects and 64
  unique ids (targets.json:3; command 3); dispatch-declared.json declares
  `requested_workers` 64 and `batched_agentswarm_calls` 1
  (reports/round-35/telemetry/dispatch-declared.json:11–12).
- Digest binding verified: claims.json sha256 `ccfaafc363981d…` and
  targets.json sha256 `56ad03927c70…` equal the pins in
  dispatch-declared.json:23–24 (command 4). The authoring note records the
  60→64 correction before dispatch (dispatch-declared.json:28), and the four
  added seats C17/O11/A11/R09 are present (targets.json).
- The three 402 probes do not break "one batch": each launched zero workers
  (availability-attempt-1.json `launched_workers: 0`, `failed_workers: 64`;
  availability-attempt-2.json same; availability-attempt-3.json:8 same), so
  the round's work is carried by exactly one effective batch — the r10
  precedent (SCORECARD round-10 record: attempt 4 after keys -3/-4/-5
  returned 402).
- Observation (i): the effective lane is key 1, while claims.json:11 declares
  `provider_lane` "opencode-go-3". The deviation is declared in
  availability-attempt-3.json:14 ("re-dispatches on opencode-go key 1 … a
  named deviation recorded here, in the observed-dispatch record, and in the
  round's LOG/SCORECARD") and is consistent with REGIMEN's permitted
  deviation list ("skipping 402'd opencode-go keys with the failure
  recorded", REGIMEN.md:66–68). Declared vs observed separation is correct
  per AGENTS.md; the observed-dispatch record and the LOG/SCORECARD mention
  are not yet filed — owed below.
- Observation (ii), structural limit not a defect: "every L2 prompt leads
  with /skill:godspeed + the verbatim directive bytes" (REGIMEN.md:34–36) is
  not durably checkable by rule, because AGENTS.md forbids persisting
  "private prompt payloads" in telemetry. Closest durable proxy: the
  directive file's sha256 `db88963cbdf5a0db22b460b284bf6f1d1f4abac9eaadb28bdb5e9bffe27be3bb`
  (command 5); this seat's own prompt carried the directive block verbatim.
- Not yet checkable: observed launches/completions/failures/runtime for the
  effective batch — the observed record is owed (below).

## Leg 4 — thresholds checkable: MIXED (findings X03-F1…F7)

X03-F1 (claim O, medium) — `selftest N/N` (claims.json:51) is an unfilled
placeholder, not a threshold; unfalsifiable as written. Measured today:
`--selftest` prints "positive run (exit 0, fields=16/16, glossary-entries=20,
findings=0) plus 17 controls" and exits 0 (command 6; format at
tools/exercise-handoff-e2e.py:4461–4464), i.e. 1 positive + 17 controls. The
claim adds two controls (claims.json:45), so the pinned value must be 19
controls (or "positive + 19"). Owner: O02/O08 + integrator validator leg.

X03-F2 (claim O, medium) — the threshold's regression leg "the r7 default
chain still exits 0" (claims.json:51) has no declared counting command; claim
O's counting_commands (claims.json:46–50) list only the selftest, the r6-row
replay, and the runner. r34's claim D declared that exact command
(`python3 tools/exercise-handoff-e2e.py --profile v3 --quiet`,
reports/round-34/claims.json claim D). Measured before-state (in-tree,
non-freeze mode — permitted; no in-tree writes: `git status --porcelain`
clean apart from the untracked reports/round-35/): exit 0 with
`packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`,
equal to the r7 freeze pin (commands 7–8). Owner: O04/O08 + validator.

X03-F3 (claim O, medium) — "named diagnostic" is a disjunction: "E2E-READSET
or the renderer's existing diagnostic convention" (claims.json:45, 51). The
tool's existing codes are E2E-{COUNT, DIGEST, UNC, DATA, SCAN, LINK,
BASELINE, GATE, ARTIFACT} (command 9); E2E-READSET does not exist yet, and
the closest existing "names the path" convention is E2E-ARTIFACT (selftest
control: "missing artifact: exit 2 E2E-ARTIFACT naming the unreadable path").
The acceptance leg must pin the code (or a regex such as
`E2E-(READSET|ARTIFACT)`) plus the path string in the message, or the
threshold stays unfalsifiable. Corroboration that the r6-row failure is a
resolution-keying failure, not file absence: the r6 baseline's `inputs` dict
(58 members) contains `reports/round-20/handoff/claims-map.md`, that file
still exists on disk (24,888 bytes), and the live constant `CLAIMS_MAP` now
names `reports/round-34/handoff/declared-in-r7/claims-map.md`
(tools/exercise-handoff-e2e.py:184) — consistent with R34-N1's "after the
CLAIMS_MAP move" wording. Execution evidence is K03's isolated-copy
traceback; I did not execute the replay in-tree.

X03-F4 (claim C, low) — the arithmetic chain is exact and the counting
commands run. Census 21/19/18/29/20/94 = 201 (claim command 1, run: command
1); inventory `read_only: true`, `totals.files 201` (command 10);
18+6=24, 19+4=23, 201+10=211 (claims.json:22–28) all check. The README leg is
executable end-to-end with a ready read-only instrument:
`reports/round-28/readme/sweep.py` is green today — rows 201 / files 201,
totals_line 201, `footer_ok True`, dir_totals [21,19,18,29,20,94],
readme_sha256 `053966a2147e…` (command 11) — so the post-application expected
values are pinned: rows/files 211, totals_line 211, dir_totals
[21,23,24,29,20,94] (the footer vector order is
linguistics/myth-symbol/culture-material/synthesis/verification/civilizations,
corpus/README.md:473; the order is the sweep's `footer_live.order`). Gap:
"10/10 new entries audited clean"
(claims.json:34) does not define the defect-severity cut-off; C12's runbook
supplies the check list, so the validator should pin "zero unfixed defects
across the C12 classes, per entry" (r19 precedent: "integrator-audited zero
defects", SCORECARD.md:202). Owner: C12/S04 + validator.

X03-F5 (claim A, low) — thresholds "every touched surface verdict-filed; zero
unfiled bleed; PROVINCE accuracy re-verified at HEAD" (claims.json:65) are
qualitative but artifact-anchored; the counting-command list names only the
runner (claims.json:62–64). The validator must pin the artifacts and the
method: the assembled audit path (A08/A09/S03), R06's independent diff-based
census over the r33→r35 commit range as the "zero unfiled bleed" measure, and
A06/A11 as the PROVINCE re-verification. Owner: S04 + validator.

X03-F6 (telemetry, low; append-only correction required) —
dispatch-declared.json:13 prose says "verifiers 11 incl.
C13/C14/C17/O05/O08/O11/A07/A11": the enumerated list has 8 names and the
seat file has 8 verifier-role seats (A07, A11, C13, C14, C17, O05, O08, O11;
command 3); "11" matches neither. The rest of the composition prose sums
correctly (4+2+1+17+11+11+9+4+5 = 64, where the 17/11/11 count C-/O-/A-
numbered seats and the 5 scribes are S01–S05 while C15/C16 sit inside the
17). Correction must be a new append-only snapshot, never an in-place edit
(AGENTS.md: "Corrections and final-wave updates are new snapshots or rows
with their own provenance"); the owed closing snapshot can carry the
corrected census. Owner: orchestrator/telemetry author + integrator closing
snapshot.

X03-F7 (standing convention, informational) — all three claims list
`python3 reports/round-35/run-validation.py` as a counting command
(claims.json:32, 49, 63), while the round's own non-goals and shared rules
forbid executing any filed round runner in-tree (claims.json:72;
targets.json:10; F-C13-1 prevention). Same shape in r33/r34 claims
(precedent, not a new defect). The runner is the close-time acceptance
instrument and must be executed in an isolated copy (r23 SCORECARD
precedent, SCORECARD.md:271–273; the r34 runner itself checks "O4: routing
lacks the isolated-copy protocol",
reports/round-34/run-validation.py:227). Recommendation: the validation
receipt record the isolated copy path. Owner: integrator.

## Recommended validator legs (for S04/O08, one line each)

- C: census 21/23/24/29/20/94 = 211; inventory `files == 211`; r28 sweep
  green with rows/files 211, totals_line 211, dir_totals [21,23,24,29,20,94];
  per-entry C12-class open defects == 0 across the 10 new files.
- O: r6-row replay exit != 0 with the pinned code+path regex on stderr;
  `--selftest` exit 0 with 19 controls; r7 default chain exit 0 with
  packet_sha256 `45f57132…`; r7 pin files unchanged (packet/twin digests ==
  freeze.txt).
- A: assembled audit exists with a verdict per K04 surface; R06 census zero
  unfiled; A06/A11 PROVINCE checks re-runnable.
- Cross: claims.json/targets.json digests == the pinned values; seat count 64
  == 64 unique ids; telemetry observed record + closing snapshot present.

## Owed

- `reports/round-35/telemetry/observed-dispatch.json` — the effective
  batch's observed launches/completions/failures/runtime/concurrency/actual
  route (owner: orchestrator; key set per reports/round-34/telemetry/observed-dispatch.json).
- `reports/round-35/telemetry/availability-close-35.json` — closing snapshot
  for dispatch-declared.json, which self-declares open-at-seat-close
  (dispatch-declared.json:30), digest-pinned to that record's sha256 at close
  (AGENTS.md "Close what you open"); r33/r34 precedent:
  availability-close-{33,34}.json.
- The round's LOG/SCORECARD mention of the key-1 lane reuse, promised in
  availability-attempt-3.json:14 (owner: integrator).
- The F1–F5 pins inside `reports/round-35/run-validation.py` (owner: S04/O08
  + integrator).
- The dispatch-declared.json:13 "verifiers 11" correction as a new snapshot
  (owner: orchestrator; F6).

## Citations

Commands (run 2026-10-19 from the repo root, `TMPDIR=$PWD/.scratch`,
`PYTHONDONTWRITEBYTECODE=1`):

1. `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do printf "%s " "$p"; ls corpus/knowledge/$p/*.md | wc -l; done` → 21/19/18/29/20/94; `ls corpus/knowledge/*/*.md | wc -l` → 201; plus the per-round axis census over r33/r34/r35 claims.json → before r35: operability 2, calibration 2, depth 1, adjacency 1, coverage 0.
2. `python3 -c` scan of r33/r34/r35 claims.json for the string "stagnation" → absent in all three; `lowest_axis_reasoning` texts quoted.
3. `python3 -c` seat census of targets.json → seat_count 64, 64 objects, 64 unique ids; roles {scout 4, planner 2, connector 1, executor 26, verifier 8, scribe 10, reviewer 9, critic 4}; claim census {C 24, O 16, A 15, cross 9}; verifier-role ids A07, A11, C13, C14, C17, O05, O08, O11.
4. `sha256sum reports/round-35/claims.json reports/round-35/targets.json` → `ccfaafc363981d16729c351fa11135e8082b1b0695dc399884d5c91bcc9e26e4`, `56ad03927c7063a3616af2ed0e78ab7b1ca1f3ea43fdf67f2ecf60a7f1b63215` == dispatch-declared.json:23–24 pins.
5. `sha256sum /home/vgpnk/.agents/skills/godspeed/directive.md` → `db88963cbdf5a0db22b460b284bf6f1d1f4abac9eaadb28bdb5e9bffe27be3bb`.
6. `python3 -B tools/exercise-handoff-e2e.py --selftest` → exit 0; "positive run … plus 17 controls"; control list incl. "tamper baseline: exit 2 E2E-BASELINE", "tamper read-set: exit 1 E2E-DIGEST naming the changed file", "missing artifact: exit 2 E2E-ARTIFACT naming the unreadable path".
7. `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0, `packet_sha256=45f57132…`; `git status --porcelain` afterwards → only `?? reports/round-35/`.
8. `sha256sum reports/round-34/handoff/declared-in-r7/{packet.md,twin.json}` → `45f57132…`, `0e22913850cd…` == freeze.txt:2–3 pins.
9. `grep -oE "E2E-[A-Z-]+" tools/exercise-handoff-e2e.py | sort | uniq -c` → COUNT, DIGEST, UNC, DATA, SCAN, LINK, BASELINE, GATE, ARTIFACT (no E2E-READSET).
10. `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → `read_only: true`, `totals.files 201`; `git status --porcelain` unchanged.
11. `python3 -B reports/round-28/readme/sweep.py` → exit 0; parts {civilizations 94, culture-material 18, linguistics 21, myth-symbol 19, synthesis 29, verification 20}; rows 201 files 201; totals_line 201 totals_ok True; footer_ok True; dir_totals [21,19,18,29,20,94]; readme_sha256 `053966a2147e…`.

Files read (path:line as cited above): REGIMEN.md:27–36, 66–68;
SCORECARD.md:3, 13–15, 202, 271–273, 698–701; reports/round-35/claims.json:5,
10–19, 20–35, 37–52, 54–66, 68, 72; reports/round-35/targets.json:3, 5–13,
394–398; reports/round-35/telemetry/dispatch-declared.json:8, 11–13, 23–28,
30; reports/round-35/telemetry/availability-attempt-{1,2,3}.json (launched 0 /
failed 64 each; attempt-3:8, 13–14); reports/round-33/claims.json,
reports/round-34/claims.json (`lowest_axis_reasoning`, claim D command);
reports/round-34/handoff/declared-in-r7/freeze.txt:2–3; reports/round-34/telemetry/availability-close-34.json (convention); reports/round-30/handoff/declared-in-r6/expected.json (`inputs`, 58 members, incl. reports/round-20/handoff/claims-map.md); corpus/README.md:1–12, 123–245 headers, 470–477; tools/exercise-handoff-e2e.py:184, 1933–1934, 4461–4464; reports/round-34/run-validation.py:4, 227; reports/round-28/readme/sweep.py (header).
