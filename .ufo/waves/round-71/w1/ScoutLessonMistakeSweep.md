# R71 Scout: lesson mistake sweep (round 70 → 71 material)

Seat: `ScoutLessonMistakeSweep` (leaf; no delegation). Scope: re-read
`corpus/lessons/round-70-verifier-spotcheck.md` and `round-70.md`; swept round-71
material (`reports/round-71/claims.json`, `.ufo/waves/round-71/`). According 3 mistake
candidates for the round-71 lesson `## Mistakes` table (class · evidence pointer ·
captured-by · fix). Every evidence pointer below was resolved against committed bytes at
base `b94a543c` (materialized clone `/tmp/r71-base` at that exact revision) and/or the
current worktree.

Tooling: no tools installed (none needed; pacman untouched).

---

## Candidate 1 — stale-premise (claim C gap sweep is false at base)

- **class**: stale-premise
- **evidence pointer**: `reports/round-71/claims.json` — claim `C`, fields `surface`
  ("0 word-bounded filename owners and 0 topic-line owners … sweep command below prints
  no dedicated filename and no topic-line owner") and `before` ("`grep -rniE '^-
  topic:.*(danc|choreograph|movement culture)' corpus/knowledge/culture-material/*.md`
  prints nothing"). Resolves against `corpus/knowledge/culture-material/funerary-material-culture.md:4`
  (the `- topic:` line).
- **verified**: ran the claim's verbatim grep at `b94a543c` (clone), command as quoted
  in claims.json:
  ```
  $ grep -rniE '^- topic:.*(danc|choreograph|movement culture)' corpus/knowledge/culture-material/*.md
  corpus/knowledge/culture-material/funerary-material-culture.md:4:- topic: how a culture disposes of its dead, … dance terms … dance registry: … dance and euphemism …
  $ echo $? → 0
  ```
  Result: **1 match in 1 file** (`funerary-material-culture.md:4`, containing
  "dance …" substrings), exit 0 — the premise "prints nothing" does not hold at base.
  The filename half is true (`find corpus/knowledge/culture-material -maxdepth 1 -type f
  -name '*danc*'` → 0). Because the round-71 lesson will be written after the claim's
  sweep, the false premise would otherwise enter the lesson uncorrected.
- **captured-by**: round-71 w1 `ScoutLessonMistakeSweep` (this seat; base-clone
  measurement at `b94a543c`).
- **fix**: re-run the gap sweep with word-bounded patterns (`\bdanc`, `\bchoreograph`,
  `movement culture` as a phrase) so the funerary false positive is excluded; report the
  actual 0-owner ground in the lesson/report; the claim's `before`/`surface` sentence is
  false as frozen, so record a correction (D-style) in the round-71 lesson — never edit
  the frozen claims.json. If the funerary topic line is judged a genuine dance/movement
  owner instead of a false positive, the claim's gap is doubly stale and must be
  re-scoped.

## Candidate 2 — landing (filed round-49 receipt mutated in the worktree)

- **class**: landing (filed-round bytes rewritten during round 71; no declared claim
  surface includes this file)
- **evidence pointer**: `git status --porcelain` → ` M reports/round-49/validation.json`
  (worktree differs from HEAD `b694afd`); `git diff --stat reports/round-49/validation.json`
  → `1 file changed, 2349 insertions(+), 58 deletions(-)` (index `bd762a8..25d3755`).
  File mtime `2026-10-25 08:21:56 -0300`, i.e. ~3 min after declaration
  (`reports/round-71/claims.json` mtime 08:18:50).
- **verified**: diff hunks flip the committed round-49 verdict `passed: true` → `false`,
  `verdict: improved` → `unchanged-blocked`, `total: 225` → `242`, `culture_material: 27`
  → `35`, `sweep_green: true` → `false`; `baseline_revision` stays `c42d675` (round 49's
  baseline). These rewritten values equal the round-71 C claim's current-tree baseline
  numbers (`corpus 242`, `culture-material 35`), i.e. the receipt was re-derived against
  the present tree and written over the filed bytes. The freeze rule in claims.json
  ("no frozen byte of any filed round is rewritten") is violated in the worktree, and
  nothing in the declared claims/plan names `reports/round-49/validation.json` as a
  fix surface.
- **captured-by**: round-71 w1 `ScoutLessonMistakeSweep` (this seat; worktree scan).
- **fix**: restore the committed bytes before any round-71 commit (`git checkout --`
  equivalent), keep the round-49 receipt immutable, and re-derive any baseline/control
  numbers only by running the declared instruments at base in a materialized clone
  (`/tmp`), never by letting a tool write into the lane worktree. If a re-measurement
  was needed, file it as a new artifact.

## Candidate 3 — attribution (mutated receipt pairs old baseline with present-tree numbers)

- **class**: attribution (number-drift as the secondary facet)
- **evidence pointer**: same object as candidate 2 — `reports/round-49/validation.json`
  (worktree version), fields `baseline_revision: "c42d675"` vs `measurement.total: 242`
  and `culture_material: 35`; compare the committed version: same `baseline_revision:
  "c42d675"` with `total: 225`, `culture_material: 27`.
- **verified**: the committed round-49 receipt measured 225 entries / 27 culture-material
  at `c42d675`; the worktree rewrite keeps `baseline_revision = c42d675` while asserting
  242 / 35 — numbers that belong to the 2026-10-25 tree, not to round 49's baseline. Any
  downstream reader of the round-49 receipt will now misattribute the present corpus size
  to round 49's baseline revision. (Parsed from `git diff reports/round-49/validation.json`;
  the pre-mutation values are the committed ones at HEAD.)
- **captured-by**: round-71 w1 `ScoutLessonMistakeSweep` (this seat).
- **fix**: restore committed bytes (as in candidate 2); when reporting baseline numbers,
  always pair them with the revision they were measured at, and never let a tool's output
  overwrite a filed receipt. If the round needs current-tree numbers, they belong in the
  round-71 receipts, not inside a round-49 file.

---

## Additional observation (not a candidate)

Frozen claims `wave.wave1_seats: 34` vs committed wave-1 evidence
(`.ufo/waves/round-71/w1/{plan.json,wave1-dispatch.json,swarm-registry.json}` counts:
spawn 37 / members 37; commit `b694afd` message "wave-1 spec/plan/dispatch evidence
(37 seats)"). The claim used "~34", so this is a mild number drift, not a hard
contradiction; the round-71 report should state the executed 37-seat count.

## Verdict

Three candidates proposed, one per class, all evidence pointers resolved against
committed bytes at base `b94a543c` and the current worktree. No round-71 lesson was
written (report-only per assignment).
