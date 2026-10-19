- Seat: X00 | connector | cross | date 2026-10-19 | baseline 139e3b6

Cross-claim consistency for round 33: dependency/sequencing map for O/C/A, the
collision matrix on the shared files, pin-cascade exposure, and the
integration-order recommendation. Read-only seat: this fragment is the only
path I wrote; the round-33 claim directories were empty at my first read
(`ls reports/round-33/{cross,op,calib,adj,review,scribe}/` → six empty
listings, 2026-10-19), so everything below is derived from
`reports/round-33/claims.json`, `reports/round-33/targets.json` and the live
tree at `139e3b6`, not from other seats' drafts.

## 1. Dependency and sequencing map

Seat census from `reports/round-33/targets.json` (computed, not quoted):
declared `seat_count: 64`, actual seats 64; by claim `{O: 15, C: 22, A: 20,
cross: 7}`; by role `{scout 4, planner 2, connector 1, executor 34,
verifier 4, scribe 7, reviewer 8, critic 4}`; **zero duplicate `out` paths,
zero duplicate ids, all 64 `out` values inside the six claim directories**
(`op 11, calib 18, adj 17, cross 5, review 8, scribe 5`). No write collision
exists at the path level in this wave.

Five dependency tiers, by each seat's own `mission` text:

| tier | seats | consumes | notes |
|---|---|---|---|
| 0 scouts | K01, K02, K03, K04 | the live tree only | every other seat in its claim is downstream of its scout |
| 1 planners | P01 (O), P02 (C+A) | K01/K02; K03/K04 | `P02` is the only seat spanning two claims |
| 2 executors | O01–O08, C01–C16, A01–A16 | the tier-1 plan + its scout | `A11–A14` are verifiers over `A01–A10`, not executors |
| 3 reviewers | R01–R03 (op), R04–R06 (calib), R07–R08 (adj) | the whole claim directory | `R01–R06` and `R07–R08` cite "re-run every cited command" |
| 4 scribes | S01–S03 (per claim), S04, S05 (cross) | tier 3 findings | S04 carries the validation-leg spec the integrator implements |

Cross-claim edges that actually bind (the rest are intra-claim):

- **X00 → A09 → R08.** `A09`'s mission says "re-pin needs listed per X00's
  matrix" (`reports/round-33/targets.json:56`), so §3 below is a required
  input, and `R08`'s second-pass focus is "would the proposed shared-file
  edits actually break a pin?" (`targets.json:72`). Both must consume §3, not
  re-derive it.
- **C14 → A09/R08.** The C claim names "the three box-1 citation pointer
  fixes" as C14 drafts (`claims.json:46`) — those are `SKILL.md` edits, so the
  pin exposure A09 must assess is not only the lessons README.
- **O05 ↔ C ledger (the one double-disposition hazard).** Claim O owns "the
  falsifier audit's filename mismatch (substance 5/5)"
  (`claims.json:23-26`) and lands its disposition at
  `op/O05-falsifier-disposition.md`. Claim C's K03 seat is instructed to
  "Canonicalize THE twelve standing open items" (mission wording,
  `targets.json:15`) from `reports/round-32/dossier-d13-operator-decisions.md`
  Decision 4 plus `reports/round-32/dossier-d11-shonen-boxes.md`
  (`claims.json:44`) — the falsifier item is a round-32
  **lesson** open route (`corpus/lessons/round-32.md:55`, Q-32-1), not a
  dossier item. Rule: **C13's consistency check must see the falsifier item as
  O-owned and referenced, never dispositioned a second time**; if K03's
  item set turns out to include it, the two claims will file contradictory
  classes for one artifact and `run-validation.py` will be asked to certify
  both.
- **O07 → everything.** O07's baseline receipt must run **before** any
  integrator edit (`targets.json:28`); it is the only pre-state control in the
  wave, and my §4 step 1 reproduces its numbers now.
- **A02 handoff leg is independent.** The handoff gate reads a packet pair,
  not the shared files (§3), so it is not on the critical path.

## 2. Collision matrix on the shared files

| shared file | seats whose drafts touch it | current state (measured) | binding rule |
|---|---|---|---|
| `corpus/lessons/README.md` | O01 (rows), O02 (prose + queue), O03 (owner cells), O04 (format cells) — all drafts; integrator applies | blob `a3187055…`, sha256 `ec7469dadf87df3e…`, 29059 B / 346 lines; last touched `fc13cd2` (round 25) per `corpus/lessons/round-31.md:53` | `targets.json:7` carves the README out of the no-edit list ("the lessons README and SKILL.md changes are drafted by seats and applied by the integrator"); the file's own rule is "Superseding edits land as a new revision block here, never as an in-place rewrite of the per-round rows' provenance claims" (`corpus/lessons/README.md:303-306`). Precedent = the Revision 2 block (`README.md:307-345`), which did refresh one pin and one pointer under a named revision with a stated control — so row-cell repair is admissible **only** inside a new named revision block with its own control line |
| `SKILL.md` | C14 (box-1 citation pointer drafts), R06 (verifies them) | blob `79460eb6…`, sha256 `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d`, 715 lines | same `targets.json:7` carve-out. **No frozen pin exists** (§3), so the risk is anchoring, not pinning: every C14 draft must name its target line, and any SKILL.md line ≥ 535 cited anywhere in the wave must be re-derived after a structural edit |
| `AGENTS.md` | **no seat** — `targets.json` has no AGENTS.md mission | 42 lines; `AGENTS.md:40-42` is the round-31 patch scaffold (` ``` `, blank, `### 2.2 \`SKILL.md\` — append one item … (after :534)`), named as residue at `corpus/lessons/round-32.md:31` (F-X16-1) and still open as Q-32-2 (`corpus/lessons/round-32.md:56`) | the residue rides the instruction channel: it is the trailing line of the AGENTS.md block quoted into this seat's own dispatch prompt, matching `AGENTS.md:42` verbatim. No seat may act on it — read as an instruction it says "append one item to SKILL.md's `## Checklist`", which would collide with C14 and with the already-landed item at `SKILL.md:713-715` (`corpus/lessons/round-32.md:33`) |
| `LOG.md` | integrator only | **dirty**: `git diff --stat LOG.md` → 18 insertions; the regimen-2 entry is `LOG.md:3500-3517`; committed blob `223256b…`, worktree blob `c866970…` | append-only; seats write no LOG bytes (`targets.json:8`) |
| `SCORECARD.md` | integrator only | 647 lines; round-32 section at `SCORECARD.md:427-447` | round-33 rows are appended at round close |
| `reports/round-33/run-validation.py` | integrator (S04 drafts the spec) | **absent** | all three claims' counting commands point at it (`claims.json:48,61`), so claim C and claim A are unmeasurable until the integrator lands it; claim O's counting commands (`claims.json:32-35`) are the only ones runnable today |

Two format-level collisions inside the README itself, both measured:

- **R6 — queue-row pipe escaping.** The queue parser counts rows by
  `line.startswith("| Q-")` but reads the owner with an escaped-pipe-aware
  split and returns `""` for any row that still yields ≠ 4 cells
  (`reports/round-25/audit/c31-lessons-index-audit.py:138-149`; the counting
  parser is `parse_index` at `:119-134`). The live
  example is `Q-20-3`, whose `v2\|v3` makes a naive split yield 5 cells
  (`README.md`, §4; measured: 5 cells naive, 4 escaped). **Any new queue row
  for r26–r32 that contains a literal `|` must escape it `\|` or C32 fails on
  a row the author believes is fine.**
- **R7 — C34b's blind spot (the false-green hazard).** C34b re-derives exactly
  two prose statements: `**Rows: N. Files: M.**` and `Rows: **N**`
  (`reports/round-25/audit/c31-lessons-index-audit.py:293-316`; the shape-cell
  leg C34c is `:268-291`). It reads
  `README.md:97` (`**Rows: 26. Files: 26.**`) and `README.md:207`
  (`- Rows: **49**. …`). Every other count in the file is **unchecked**:
  `:6-7` ("26 at the final stamp"), `:35` ("# 26/26"), `:39-40` ("# 26"),
  `:118`/`:124`/`:127` (§3 histogram 14/5/7), `:140` ("Total 26 = the runner's
  file set"), `:204` (the re-measure stamp), `:257` ("beside the 26 `*.md`
  lesson files"), `:285` ("the tool's `--selftest` is 26/26 in-memory checks"
  — **already false**: the live selftest is 28/28), `:294` ("the 24 filed
  lessons"). A reconciliation that fixes only `:97` and adds rows **goes green
  on C31/C34b while leaving ten stale statements**, including one that was
  already stale before round 33. O02 must enumerate them and O06's prose-lie
  control must state that C34b cannot see them.

Live per-row cells the new rows must carry (measured now via
`python3 -B reports/round-25/audit/c31-lessons-index-audit.py --json`, key
`live`; C34/C34c re-derive these cells, so a wrong cell fails):

| file | format | contract | bytes | lines | sha8 |
|---|---|---|---|---|---|
| `round-26.md` | gate-keeper | 4/4 | 60054 | 222 | cae06660 |
| `round-27.md` | gate-keeper | 4/4 | 54972 | 203 | f15e285b |
| `round-28.md` | gate-keeper | 4/4 | 50419 | 145 | dd832ff7 |
| `round-29.md` | gate-keeper | 3/4 | 17847 | 118 | b6765d33 |
| `round-30.md` | gate-keeper | 3/4 | 30665 | 181 | 56e77835 |
| `round-31.md` | gate-keeper | 4/4 | 16637 | 73 | 8870bbdd |
| `round-32.md` | gate-keeper | 4/4 | 12879 | 66 | 8aacfc2b |

The r26–r31 pins agree with the pins already recorded at
`corpus/lessons/round-32.md:45`; the r32 pin is measured here for the first
time. All seven are `gate-keeper`, so the §3 histogram arithmetic becomes
gate-keeper 21 / fragment-index 5 / plain 7 = 33 (the tool's own
`format_histogram` reads `{'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}`
at 33 files). Contract coverage: five files 4/4, r29 and r30 3/4 — **not** a
uniform value, so O01 must not copy one contract cell down the column.

A second collision of naming: `reports/round-26/zzz-lessons-index-revision-3.md:1`
is already filed as "index — revision 3", declaring "Rows: 27. Files: 27."
(`:18`). An in-file README block also called "Revision 3" would give the lane
two different artifacts under one name. The README block should carry the
round number in its heading (the existing block's own style,
`README.md:307`).

## 3. Pin-cascade exposure

**Frozen baselines: zero exposure.** No frozen row references either shared
file. Evidence: `grep -rn "lessons/README\|corpus/lessons\|SKILL.md"
tools/gates/frozen/` returns only (a) prose inside copied knowledge bytes
(`tools/gates/frozen/round-3/inputs/corpus/knowledge/verification/gate-frozen-run-standard.md:5,15,28`,
and the same file under `round-3/attempt-1/` and both `provenance-audit/`
generations) and (b) digest rows for `corpus/lessons/round-6-sources/*.json` —
evidence files in the lessons partition, not the README
(`tools/gates/frozen/handoff-packet-check/r9-pre/packet.md:69-72` and the
`r18-post` twin). All 13 `MANIFEST.tsv` files under `tools/gates/frozen/**`
plus the r27-post/r28-post generations carry no `lessons`/`SKILL` row
(checked file-by-file; the largest are `round-11/`, `round-18/repin-d2/`,
`round-20/repin-d2/` and `round-23/repin-d2/` at 12 rows each).
`grep -n "SKILL\|lessons" tools/replay-frozen.py` → no output. **So editing
`corpus/lessons/README.md` or `SKILL.md` breaks no frozen generation and
requires no re-freeze.**

**Filed digest pins that name these bytes are historical measurements, not
live pins**: `reports/round-25/validation.json:1020` (README
`ec7469dadf87df3e…` — still the live digest, see §2), `reports/round-25/rerun.json:260`
(README `ee2a15df…` at checkpoint-d), `reports/round-30/rerun.json:326` and
`reports/round-31/rerun.json:120` (SKILL `2d85bfea…`, `83b0a78a…`),
`reports/round-31/validation.json:1026` (SKILL `79fe91d3…` = live). Filed
rounds are never re-run for acceptance (`REGIMEN.md:66-68` non-goals), so a
new README digest does not falsify any filed receipt.

**Live instruments are the real cascade** — five readers, **none of them in the
round-32 acceptance matrix** (`grep -c` over the 51 command lines of
`reports/round-32/sweep/commands.txt` → 0 for each of `c31-lessons`,
`round-25/run-validation`, `box1-survey`):

1. `reports/round-25/audit/c31-lessons-index-audit.py` — reads the README
   live. Reproduced now: `lesson files: 33`, `index rows: 26`, `queue rows: 49`,
   `FAIL C31_index_rows_eq_files`, `FAIL C34b_prose_arithmetic`, findings 2
   (`C31-1` seven unindexed files, `C34-2` stated `[26,26]` vs measured
   `[26,33]`), exit 1; `--selftest` → `SELFTEST OK: 28/28`, exit 0. **This is
   claim O's counting command** (`claims.json:32-33`) and it is partition-size
   independent, so it survives the reconciliation (verified: it passes its own
   selftest at 33 files).
2. `reports/round-25/run-validation.py:88` (`LESSONS_README`) — a **second**
   live reader of the same file. It refuses to run in place:
   `python3 reports/round-25/run-validation.py` → `could-not-evaluate: run
   round validators only in an isolated Git clone under the lane's .scratch`,
   exit 0. It is **not** in the round-32 sweep manifest
   (`reports/round-32/sweep/commands.txt` — 51 commands, no `reports/round-*`
   runner) and not in the battery, so no round-33 acceptance cascade; but any
   later round that re-runs it in a clone will read the edited README, and
   today it would measure 26 rows against 33 files.
3. `reports/round-30/craft/box1-survey.py` — reads **SKILL.md** live.
   Reproduced now: `{"named": 28, "resolvable": 28, "unnamed_in_skill": [],
   "skill_sha256": "79fe91d3…"}`, exit 0. This is the instrument behind the
   round-32 dossier's "inventory condition CLOSED — 28/28 named executables
   resolve, re-verified this round" (`reports/round-32/final-dossier.md:46`,
   re-run command at `:131`). **If C14's drafts change which executable paths
   SKILL.md names, this count moves and that filed sentence stops reproducing;
   re-run the survey after any SKILL.md edit and record the new count.**
4. `reports/round-26/audit/x63-lessons-audit.py:357` hard-codes
   `check("live partition is 26 md files", len(files) == 26, len(files))`.
   **That auditor's selftest is red by construction at the live 33-file
   partition**, and its filed receipt quotes the 26-file stamp
   (`reports/round-26/zzz-lessons-index-revision-3.md:47`: "queue rows: 49,
   six checks PASS, findings: 0, exit 0"). It is not in the sweep or the
   battery. **Trap for round 33: do not cite x63 as a green lessons control.**
   `reports/round-27/audit/x57-lessons-audit.py` and
   `reports/round-28/audit/x57-lessons-audit.py` are the peer auditors that
   moved 8 → 9 findings when one lesson landed
   (`corpus/lessons/round-28.md:139`); they will move again on a README edit
   and are likewise not acceptance instruments.
5. `reports/round-25/audit/x45-lessons-pointer-audit.py` +
   `x45-lessons-pointer-receipt.json:57-62` — a pointer-only reader whose
   receipt pins the README's old digest and row count (`index_rows: 26`,
   `index_sha256 ee2a15df…`). Same class as 4: historical, not acceptance.

**Net re-pin obligation for round 33: none for frozen baselines; one live
instrument to re-run (box1-survey) if SKILL.md changes; one counting command
to re-run (c31) for claim O regardless.**

## 4. Integration-order recommendation

The three shared-file edits are mutually independent (three different files),
so the only hard constraints are intra-file anchoring and instrument re-runs
after each landing. Recommended order:

1. **Freeze the pre-edit baseline** (O07's receipt): `python3 -B
   reports/round-25/audit/c31-lessons-index-audit.py` (expect the 2 findings
   above, exit 1), `python3 -B reports/round-30/craft/box1-survey.py` (28/28),
   `python3 -B tools/check-gate-battery.py` (exit 0, `pass 7 / fail 0 /
   unevaluable 0`), `python3 -B tools/check-gate-battery.py --selftest`
   (`SELFTEST OK 44/44`). All four reproduced by me at this seat.
2. **Apply the README reconciliation as ONE edit** — new rows, the ten stale
   prose statements of R7, the §3 histogram, the §4 queue rows, and a named
   revision block — because c31 grades the file atomically: a partial
   application can leave C31 green while C34b stays red (or the reverse).
3. **Re-run c31** → expect exit 0, `findings: 0`, `33 rows == 33 files`,
   `--selftest` 28/28. This is claim O's counting command and must be recorded
   with its output.
4. **Apply the SKILL.md drafts** (C14's box-1 pointer fixes; the
   `SKILL.md:713-715` checklist-position item only if the integrator takes
   Q-32-3) as one hunk set. Anchoring arithmetic, checked: the four box-1
   citation conditions named at `reports/round-32/final-dossier.md:46` sit at
   `SKILL.md:486`, `:488`, `:501`, `:128` — all **< 522**, so moving the
   `:713-715` block into `## Checklist` (`:522-534`) does not shift them;
   conversely that move shifts `:535-:712` by −3, so any round-33 draft citing
   a SKILL.md line in that range must be re-derived after it. No round-33
   target names such a line except C14 and R06.
5. **Re-run `reports/round-30/craft/box1-survey.py`** and record the new
   count/digest (step 3 of §3).
6. **Apply the `AGENTS.md:40-42` excision** if the integrator takes Q-32-2
   (independent of steps 2–5; verify the file ends at 39 lines and that no rule
   text was cut). If not taken, record it carried with the owner already named
   at `corpus/lessons/round-32.md:56`.
7. **Re-run the regression set** (`tools/check-gate-battery.py` ± `--selftest`,
   `tools/check-craft-exercise.py --selftest`,
   `tools/assemble-culture-d4.py --selftest`) and the A-claim's handoff gate.
8. **Only then** assemble `reports/round-33/run-validation.py` (S04's spec),
   the SCORECARD rows, the single LOG.md entry, the fleet report and the
   telemetry records.

Rationale, from the lane's own record: the round-28 lesson documents eight
surfaces moving under one seat's reads and four receipts read from one path
(`corpus/lessons/round-28.md:5,106`); re-running each instrument immediately
after the landing that moves its input is the only way the round-33 record
can bind its own bytes.

## 5. Handoffs this fragment owes other seats

- **A09 / R08**: §3 is the requested matrix. The short answer is "no frozen
  pin, one live instrument (box1-survey), one counting command (c31)"; the
  worked evidence is above so neither seat needs to re-derive it.
- **O05 / K01**: the artifact is located — `corpus/lessons/round-32.md:41`
  (F-X16-3) with the open route at `:55`. I re-ran the audit verbatim: it
  prints the five `reports/round-{19,25,26,27,28}/availability.json` paths
  while every one of them is closed by a differently-named snapshot
  (`reports/round-*/telemetry/availability-close-*.json`, 5 present), so
  "substance 5/5, instrument false-fires" reproduces at HEAD. The mismatch is
  a **filename convention** mismatch inside `SKILL.md:713-715`'s inline audit
  string, not a data defect.
- **C13**: §1's double-disposition rule for the falsifier item.
- **O02 / R02**: R6 (pipe escaping) and R7 (the ten unchecked counts) are the
  two ways the README delta can be wrong while c31 is green.
- **X02**: `AGENTS.md:40-42` residue still rides the dispatch prompt's
  AGENTS.md block; no seat owns it in `targets.json`.

## Owed

- `calib/C14-fix-drafts.md` and `op/O02-readme-delta.md` were **absent** at
  this seat's read (`ls reports/round-33/{calib,op}/` → empty, 2026-10-19), so
  R2 (SKILL.md anchoring) and R7 (the prose list) are derived from
  `claims.json`/`targets.json` plus the live tree, not from the drafts. The
  integrator must re-check both rules against the actual drafts — specifically
  that every C14 target line is real and unchanged after any structural
  SKILL.md edit, and that O02's prose list covers the ten statements of R7 —
  before applying them. If the drafts contradict a rule here, this fragment's
  rule is the one to re-derive, not the drafts to bend.
- `reports/round-33/run-validation.py` is absent; claim C's and claim A's
  counting commands (`claims.json:48,61`) cannot run until the integrator
  implements S04's spec.

## Citations

- `reports/round-33/claims.json:19-65` (claims O/C/A, counting commands, thresholds), `:66-71` (non-goals)
- `reports/round-33/targets.json:5-11` (shared_rules), `:13-83` (64 seat missions/outs)
- `REGIMEN.md:25-50` (per-round contract), `:60-69` (scope/non-goals)
- `corpus/lessons/README.md:6-7,35,39-40,97,118,124,127,140,204,207,257,285,294,303-306,307-345`
- `corpus/lessons/round-32.md:31,33,41,45,55-60`
- `corpus/lessons/round-31.md:53,59`, `corpus/lessons/round-28.md:5,106,139`, `corpus/lessons/round-30.md:101-105`
- `reports/round-32/final-dossier.md:46,131`; `reports/round-32/sweep/commands.txt` (51-command manifest)
- `reports/round-32/dossier-d13-operator-decisions.md`, `reports/round-32/dossier-d11-shonen-boxes.md` (named by `claims.json:44`; contents not read by this seat — to-verify for the 12-item enumeration)
- `reports/round-25/audit/c31-lessons-index-audit.py:119-134` (parse_index), `:138-149` (owner_cell/escaping), `:268-291` (C34c), `:293-316` (C34b), `:35-36` (LESSONS/INDEX constants)
- `reports/round-25/run-validation.py:88`; `reports/round-25/validation.json:1020`; `reports/round-25/rerun.json:260`; `reports/round-25/audit/x45-lessons-pointer-receipt.json:57-62`
- `reports/round-26/audit/x63-lessons-audit.py:357`; `reports/round-26/zzz-lessons-index-revision-3.md:1,18,47`
- `reports/round-30/craft/box1-survey.py` (run); `reports/round-30/craft/box1-landed-survey.json`; `reports/round-30/rerun.json:326`
- `reports/round-31/rerun.json:120`; `reports/round-31/validation.json:1026`
- `AGENTS.md:32-39` (closing-snapshot rule), `AGENTS.md:40-42` (round-31 residue; file = 42 lines)
- `SKILL.md:713-715` (the inline availability audit; file = 715 lines)
- `tools/gates/frozen/**/MANIFEST.tsv` (13 files checked); `tools/gates/frozen/handoff-packet-check/r9-pre/packet.md:69-72`; `tools/gates/frozen/round-3/inputs/corpus/knowledge/verification/gate-frozen-run-standard.md:5,15,28`; `tools/replay-frozen.py` (no SKILL/lessons references)
- Commands run at this seat (all from the repo root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  - `ls reports/round-33/{cross,op,calib,adj,review,scribe}/` → six empty listings
  - `python3 -c "import json,collections; d=json.load(open('reports/round-33/targets.json')); …"` → 64 seats, O15/C22/A20/cross7, no duplicate outs
  - `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → 33 files / 26 rows / 49 queue rows, FAIL C31 + FAIL C34b, findings 2, exit 1
  - `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` → `SELFTEST OK: 28/28`, exit 0
  - `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --json` → `format_histogram {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}`; per-file cells in §2
  - `python3 reports/round-25/run-validation.py` → `could-not-evaluate: run round validators only in an isolated Git clone under the lane's .scratch`, exit 0
  - `python3 -B reports/round-30/craft/box1-survey.py` → `named 28, resolvable 28, unnamed_in_skill [], skill_sha256 79fe91d3…`, exit 0
  - `python3 -c "import json,glob,os; [print(f) for f in sorted(glob.glob('reports/round-*/availability*.json')) if json.load(open(f)).get('state')=='open-at-seat-close' and os.path.exists(os.path.join('reports',f.split('/')[1],'validation.json')) and not os.path.exists(os.path.join('reports',f.split('/')[1],'telemetry','closing-snapshot.json'))]"` → 5 paths (rounds 19/25/26/27/28), matching `corpus/lessons/round-32.md:41`
  - `python3 -B tools/check-gate-battery.py` → exit 0, `pass 7 / fail 0 / unevaluable 0`; `--selftest` → `SELFTEST OK 44/44`
  - `git hash-object` / `sha256sum` / `wc -c -l` on `corpus/lessons/README.md` → `a3187055…` / `ec7469dadf87df3e…` / 29059 / 346
  - `git hash-object` / `sha256sum` / `wc -l` on `SKILL.md` → `79460eb6…` / `79fe91d3…` / 715
  - `git diff --stat LOG.md` → 18 insertions; `git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb`
  - `grep -rn "lessons/README\|corpus/lessons\|SKILL.md" tools/gates/frozen/`; `grep -n "SKILL\|lessons" tools/replay-frozen.py` (no output)
