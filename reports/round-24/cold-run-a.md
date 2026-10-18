# Round 24 — cold-run A: SKILL.md 'Checklist (executable)' executed by a fresh-context seat

Seat: executor A, round 24. Contract honored: I had zero lane history; I read
ONLY `SKILL.md`, `AGENTS.md`, `PROVINCE.md`, `corpus/README.md` (plus directory
listings and tool invocations; no reports/round-8..23 content, no `LOG.md`, no
corpus entry bodies — the one pointer-resolution probe at
`source-discipline-calibration.md:67` printed a 3-character prefix only). Every
command ran from the repo root with `TMPDIR=$PWD/.scratch`. No git writes; no
writes outside this file and `.scratch/` (verified: `git status --porcelain`
before and after differs only by files not mine — see §5).

Target: the checklist at `SKILL.md:408-420` ("Checklist (executable where a
tool exists)"), executed end-to-end exactly as written, items 1→4.

## 0. Execution log (commands → exit codes)

| Step | Command | Exit | Result digest |
|---|---|---|---|
| E1 | `python3 tools/gates/provenance-audit.py --selftest` | 0 | `SELFTEST OK: 7 fixture file(s), planted IDs missing-topic, missing-sources, empty-sources, missing-couples, empty-couples, missing-calibration, exit 1 on the defect tree, exit 0 on the clean entry, exit 2 on a missing path` |
| E2 | `python3 tools/gates/provenance-audit.py corpus/knowledge` | 0 | `INFO scan: files=199 marks=733 mark-lines=719 findings=0 blocked=0`; one shape INFO `calibration-prose-only` on `corpus/knowledge/synthesis/glossary-registry-format.md` |
| E3 | `python3 tools/gates/costume-era-consistency-gate.py --selftest` | 0 | `self-test: 10/10 checks passed; fixture exit 1 with 21 planted finding IDs` |
| E4 | `python3 tools/gates/costume-era-consistency-gate.py tools/gates/fixtures/costume-era-consistency-gate.yml` | 1 | 21 planted findings (T-02, R-01..R-06, MAT-05 ×2, …) — defect fixture reproduces |
| E5 | `python3 tools/gates/handoff-packet-check.py --selftest` | 0 | `selftest: OK — fixture findings 11 across 9 ids (…) clean control exit 0; probes cover canon, baseline, dependency, contract_ref and glossary vocabulary` |
| E6 | `python3 tools/gates/handoff-packet-check.py tools/gates/fixtures/handoff-packet-check.md` | 1 | 11 planted findings (HO-MANIFEST-DIGEST, HO-DEP-FLOAT, HO-CANON-MARKER, HO-CANON-CLAIM, HO-GLOSS-ETYM ×2, …) |
| E7 | `python3 tools/check-gate-battery.py` (default) | 0 | `battery_exit 0, pass 7 / fail 0 / unevaluable 0`, `coverage: 9/9`, `preserved: true, modified: 0` |
| E8 | `python3 tools/check-gate-battery.py --baselines-root reports/round-9/baselines` | 2 | `battery_exit 2, pass 7 / fail 0 / unevaluable 0`; 4× `BASELINE-GATE-UNCOVERED` (costume-era-consistency-gate.py, lexicon-coverage-audit.py, phonology-sanity-gate.py, provenance-audit.py — "no committed expected.json under the declared roots") |
| E9 | `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | 0 | schema `kotodama-source-audit-inventory/1`, `read_only: true`, corpus `files=199` (matches `corpus/README.md:401-405` count claim) |

Pointer resolutions attempted before execution (all resolved):
`tools/gates/provenance-audit.py`, `tools/gates/costume-era-consistency-gate.py`,
`tools/gates/handoff-packet-check.py`, `tools/check-gate-battery.py`,
`tools/source-audit-inventory.py` exist; `tools/gates/fixtures/` holds all seven
fixture pairs plus `provenance/` (7 files);
`corpus/knowledge/synthesis/source-discipline-calibration.md` exists (197 lines;
line 67 exists — content unread, out of seat scope);
`reports/round-10/drift/shard-06.md` exists (content unread — lane history).

## 1. Item-by-item execution verdicts

### Item 1 — typological basis (`SKILL.md:410-412`): NOT EXECUTABLE (self-declared; declaration verified accurate)

The item is prose and says so: "No lane executable reads this item — prose
gap, recorded in `reports/round-10/drift/shard-06.md` §06-G." Verified
independently: `grep -rln "typological basis" tools/` → no hits. Execution is
impossible by design, and the seat's four files give no way to even attempt it:
no enumeration of "language systems" (no examples/packets path is named in the
checklist item), no definition of what counts as "cites its typological basis".
F1 (break, documented): confirmed as-is; the item contributes zero executable
coverage. Not a new defect — but a promotion reviewer should read the checklist
header's "(executable where a tool exists)" as covering 1 of 4 items, not 4 of 4.

### Item 2 — mythic/symbolic claims name framework + calibration status (`SKILL.md:413-416`): EXECUTABLE, ran clean, one ambiguity

Only item with a named executable: "`provenance-audit`'s `missing-calibration`
family checks the declared shape only." Executed:
- Selftest E1 exit 0, `missing-calibration` among the planted IDs — the family
  exists and is negative-controlled.
- Corpus run E2 exit 0, `files=199 … findings=0`, with one shape-level INFO
  (`calibration-prose-only`, `glossary-registry-format.md`). The item's own
  parenthetical ("checks the declared shape only") matches observed behavior:
  the gate emits shape findings/INFO only, and its own caveat line prints
  "marker absence is not verification"-class limits.

F2 (ambiguity): the checklist names no invocation scope. The Gates table row
(`SKILL.md:495`) says `provenance-audit.py <corpus-paths>`; I chose
`corpus/knowledge` (the only sensible whole-corpus reading, consistent with the
Corpus map at `SKILL.md:424-443` and the counts command in
`corpus/README.md:403-405`). Another executor may pick a narrower path and also
read exit 0; the item therefore has no defined pass surface — "clean over the
corpus" is a shape verdict, not evidence that every mythic/symbolic claim
semantically names S/C/H/R/U/V. Also minor: the item's path
`synthesis/source-discipline-calibration.md:67` is rooted at
`corpus/knowledge/` only via the Corpus map; resolvable, but only by combining
two sections of SKILL.md.

### Item 3 — costume/era claims couple term+material+who-may-wear (`SKILL.md:417-418`): NOT EXECUTABLE AS WRITTEN (no operand; machinery exists but is unlinked)

The item names no tool and no artifact. Unlike item 1 it does not even declare
its own prose status — a fresh executor cannot tell whether executability was
considered. F3 (break): no operand is named anywhere in the four files, so the
item cannot be run against any real costume/era claim; `grep -rln "who may
wear" tools/` hits only `tools/gates/expected/d4-typed-labels-check-gate/…`
baseline data, no gate logic — no executable reads this item either.
Machinery capability demonstrated (not checklist execution): the Gates table's
`costume-era-consistency-gate` (`SKILL.md:493`) covers exactly this domain
(its fixture findings include term/mechanism T-02, material supply MAT-05, and
rank rule R-01..R-06): selftest E3 exit 0 (10/10), committed fixture E4 exit 1
with the 21 planted findings — but that fixture is a defect specimen, not a
lane artifact, and nothing links the checklist item to the gate.

### Item 4 — handoffs name recipient + open questions (`SKILL.md:419-420`): NOT EXECUTABLE AS WRITTEN (no operand; backing exists)

F4 (break): same linkage gap. The Gates table's `handoff-packet-check`
(`SKILL.md:496`) does enforce the item's requirements —
`tools/gates/handoff-packet-check.py:127` (`recipient`) and `:138`
(`open_questions`) are required fields, and the embedded template shows
`| recipient | lore-shokunin |` and `## open_questions` (`:623`, `:673`); the
item's "canon decisions are never made here" maps to the gate's
HO-CANON-MARKER / HO-CANON-CLAIM FAIL legs (observed in E6). Selftest E5 exit
0. But the four files name no real handoff packet to check: the only packet
path the Gates table pins is the defect fixture
`tools/gates/fixtures/handoff-packet-check.md` (11 planted findings, exit 1).
A cold seat therefore cannot execute "every handoff …" over the lane's actual
handoffs; it can only prove the checker works.

## 2. F5 — stale documentation break, battery row (`SKILL.md:501`) — highest severity

`SKILL.md:501` (Gates table row "isolated legacy selftest battery") states:
"the committed default currently exits 2 with `BASELINE-GATE-UNCOVERED` for
myth and naming, whose pins live under `reports/round-9/baselines/`; add that
root via `--baselines-root` to reach 0." Measured on today's tree, both halves
are inverted:

- Default (E7): exit **0**, `pass 7 / fail 0 / unevaluable 0`, `coverage 9/9`.
- `--baselines-root reports/round-9/baselines` (E8): exit **2** — the
  instructed flag *causes* the failure: 4× `BASELINE-GATE-UNCOVERED`
  (costume-era-consistency-gate.py, lexicon-coverage-audit.py,
  phonology-sanity-gate.py, provenance-audit.py) because those gates'
  `expected.json` baselines now live under the battery's default discovery
  roots, not the round-9 root.

A fresh executor following `SKILL.md:501` verbatim turns a clean battery into a
fail-closed 2 and, per the row's own verdict map, reads "tampered, revised or
uncovered gate". The current behavior is documented elsewhere in the seat's
own allowed reading: `corpus/README.md:18-21` (revision 1.5) already records
the battery at "nine gates … `pass 7 / fail 0 / unevaluable 0`, exit 0".
Condition for operability: fix the `SKILL.md:501` cell (default exits 0,
coverage 9/9; drop or invert the `--baselines-root` instruction, or state it as
historical round-9 context). Not fixed by this seat (verifier, non-author;
write scope = this file only).

## 3. Positive controls (what held)

- Every pointer the checklist and its machinery name resolves on today's tree
  (§0 resolution list) — no missing files, no dead paths.
- Item 2's executable is real, negative-controlled (E1), and shape-scoped
  exactly as the item claims; corpus run is clean (E2, exit 0, 199 files).
- The corpus count quoted to the seat (`corpus/README.md:401`: 199 entries)
  reproduces independently (E2 `files=199`; E9).
- Items 3/4 machinery is green on selftests (E3, E5) and behaves per its
  verdict map on committed defect fixtures (E4, E6 → exit 1 with planted IDs).
- Gate write discipline held: battery reports `preserved: true, modified: 0`
  (E7/E8); inventory is `read_only: true` (E9); `git status` clean of my
  effects (§5).

## 4. Conditions under which the checklist is end-to-end executable (for the O verdict)

The checklist executes end-to-end only under these named conditions:
1. Item 1 is accepted as documented prose (no executable exists or is claimed).
2. Item 2's invocation scope is stated in the item (e.g. "run over
   `corpus/knowledge`"), and "clean" is read as shape-only per the item's own
   parenthetical.
3. Items 3 and 4 gain an operand: either the items name their gates and a
   current artifact set (real costume/era artifacts and real handoff packets —
   none are named in the four seat files), or they declare their prose status
   like item 1 does.
4. `SKILL.md:501`'s battery cell is corrected to the measured behavior
   (default exit 0, coverage 9/9; the round-9 `--baselines-root` instruction is
   stale and now fail-closes the run).

## 5. Seat hygiene

Baseline `git status --porcelain` at seat start: ` M
reports/round-7/validation.json`, `?? reports/round-24/box4-province.md` —
pre-existing, not mine, untouched. At seat end, additionally
`?? reports/round-24/box1-craft.md`, `?? reports/round-24/box2-d4.md` (other
seats' outputs). I wrote exactly one file: this report (plus `.scratch/`
scratch, gitignored). No commits, no pushes, no edits to rounds 8-23 artifacts.
