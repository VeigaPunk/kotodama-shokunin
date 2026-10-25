# RevRerun — residual verification of the three round-69 final measures

Seat: L1Kotodama69.RevRerun (reviewer, round 69 attempt 2, w2-verify)
Date: 2026-10-25
Mode: read-only on the lane and the fleet repo; all execution in a private clone.

## 0. Setup and identity

```
$ git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/RevRerun-r69
$ git -C /tmp/RevRerun-r69 rev-parse HEAD
9e82c7b47651e0aba6ee05cc19770f78bf120cfd
$ git -C /tmp/RevRerun-r69 rev-parse main
9e82c7b47651e0aba6ee05cc19770f78bf120cfd
$ git -C /tmp/RevRerun-r69 status --short
(empty)
```

Tip matches the declared `9e82c7b47651e0aba6ee05cc19770f78bf120cfd`; `HEAD == main`; worktree clean, before and after every run (the counters write nothing).

Counters under test, hashes computed in the clone:

```
08c7ea6149a0212a6ccee7de62a9f5ef2a4efb197235b1586e4b7b91822f7547  reports/round-69/accept-o.py
091074c5c054e1ed214204efee8ac25d12c7697414f2e8ea16aac9ec483b405e  reports/round-69/accept-ca.py
06b0352a0288be7a788bb65f243980c77e107e2e4795743b4c4e1a40cd490c10  reports/round-69/accept-d.py
```

These equal the `# counter sha256 (self):` header of each committed receipt (`final-measures-{o,ca,d}.txt`) byte-for-byte, and equal the `committed=` / `self=` values printed by the STAMP legs of `accept-o.py` and `accept-d.py`. **Step-4 stamp check: MATCH on all three.**

Measurement-revision equivalence: the receipts' header records `measured revision (lane main): e86ed3e99c0ed3abfd7716896315fae4cdca77a2`, `tree: b3064e1f9255a2f4437b3109e81ac3326e06cb97`. Verified:

```
$ git -C /tmp/RevRerun-r69 rev-parse e86ed3e^{tree}
b3064e1f9255a2f4437b3109e81ac3326e06cb97
$ git -C /tmp/RevRerun-r69 diff --stat e86ed3e 9e82c7b
 reports/round-69/telemetry/before-measures.txt   | 25 +++++
 reports/round-69/telemetry/census-end.txt        | 32 +++++++
 reports/round-69/telemetry/final-measures-ca.txt | 17 +++
 reports/round-69/telemetry/final-measures-d.txt  | 17 +++
 reports/round-69/telemetry/final-measures-o.txt  | 16 +++
 5 files changed, 107 insertions(+)
```

The only delta between the data land and the tip is the five telemetry receipts: no counter, SKILL.md, registry, fixture or tools change. Re-running at the tip is therefore equivalent for every artifact these claims measure. The lane has since advanced (content repair `975e8f2`, re-measurement records `3e59d1d`); §8 re-runs all three counters at that tip, compares them to the new `*-attempt2` receipts, and maps the outcome onto these findings.

## 1. O2 — operability, capability acquisition

```
$ cd /tmp/RevRerun-r69 && python3 -B reports/round-69/accept-o.py --root .
LEG PASS STAMP self=08c7ea6149a0 committed=08c7ea6149a0
LEG PASS TOOL tools/check-settlement-fixture.py
LEG PASS FIXTURE rc=0 pending=0 missing_paths=0
LEG PASS NEGCASE rc=0 pending=0 missing_paths=1
LEG PASS LANE rc=0 pending=0 missing_paths=0
LEG PASS NEGPROBE harness_on_counter_fixture rc=1 lane_lines=['LANE: pending=0 missing_paths=1']
LEG PASS R68FROZEN mismatched=none
ACCEPT-O-69: PASS legs=7/7
EXIT=0
```

Diff against `reports/round-69/telemetry/final-measures-o.txt` body (LEG/ACCEPT lines): **IDENTICAL**, all seven leg names and all numbers equal.

Declared control (revision 1), re-run:

```
$ python3 -B reports/round-69/accept-o.py --root . --selftest
GREEN FIXTURE: PASS (legs 7/7) — as required
DO-NOTHING FIXTURE: FAIL (legs 5/7) — as required
SPOOF FIXTURE: FAIL (legs 6/7) — as required
SELFTEST: 3/3
EXIT=0
```

Matches `telemetry/controls-rev1.txt` exactly (5/7 do-nothing, 6/7 spoof, 3/3), and therefore matches the `do_nothing_control` field of `claims.json`. The NEGPROBE leg is the one revision 1 added: the counter builds the negative fixture itself and runs the harness on it (`rc=1`, one missing used-by path), so a harness that only prints the expected strings cannot satisfy it — confirmed by the SPOOF control above.

Frozen round-68 counters, re-derived independently (not trusting the leg):

```
accept-o:  live=f409096c9167 recorded=f409096c9167 MATCH
accept-ca: live=a6d1c1c24e77 recorded=a6d1c1c24e77 MATCH
accept-c:  live=515fa492aac1 recorded=515fa492aac1 MATCH
```

`R68_COUNTERS` is `(accept-o, accept-ca, accept-c)` and the leg fails closed on a missing file or a missing header (`if not live or not rec or live != rec`), so `mismatched=none` is a real result, not an empty loop. The claim's R68-M1 premise checks out: the round-68 operability receipt holds 9 leg lines, 8 PASS, and the failing leg is `EXEC FAIL base_pending_fail=True lands_pass=False`.

**Verdict O2: PASS — `ACCEPT-O-69: PASS 7/7`, exit 0, receipt body identical, both controls reproduce.**

## 2. Ca2 — calibration

```
$ python3 -B reports/round-69/accept-ca.py --root . --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS R68FROZEN live=a6d1c1c24e77 recorded=a6d1c1c24e77
LEG PASS OBSERVED o-legs=(8, 9) ca-verdict=FAIL
LEG PASS EVAL LEGCOUNT|SCORECARD.md live=True covered=True remedy=True hits=['9/10']
LEG PASS EVAL LEGCOUNT|LOG.md live=True covered=True remedy=True hits=['9/10']
LEG PASS EVAL LEGCOUNT|.ufo/reports/round-68/kotodama.md live=True covered=True remedy=True hits=['9/10', '9/10']
LEG PASS EVAL DEADPOINTER|.ufo/reports/round-68/kotodama.md live=False covered=True remedy=True hits=none
LEG PASS EVAL OVERREACH|SCORECARD.md live=True covered=True remedy=True hits=["calibration verdict 'improved' vs receipt FAIL"]
LEG PASS MISMATCHES live_mismatches=4 unannotated_mismatches=0
ACCEPT-CA-69: PASS legs=8/8
EXIT=0
```

Diff against `final-measures-ca.txt` body: **IDENTICAL**. `MISMATCHES` prints `unannotated_mismatches=0` over the 5 declared `(class, surface)` pairs.

Control, re-run: `GREEN FIXTURE: PASS (legs 8/8)`, `DO-NOTHING FIXTURE: FAIL (as required) (legs 2/8)`, `SELFTEST: 2/2`, exit 0 — matches `telemetry/controls.txt`.

Independently re-derived observations:

- `(8, 9)` and `ca-verdict=FAIL`: round-68 `final-measures-o.txt` → `grep -cE '^[A-Z0-9_]+ (PASS|FAIL) '` = 9, same grep restricted to `PASS` = 8; `grep -c 'ACCEPT-CA-68: PASS'` on the round-68 ca receipt = 0, and the receipt carries `NameError: name 'git_bytes' is not defined` (line 17). R68FROZEN also matches independently (a6d1c1c24e77).
- Annotation coverage is honest and non-circular: `correction_pairs()` reads only `reports/round-69/corrections-r68.md` and matches on the literal `(class, surface)` string; that file has exactly the five declared pairs, one row each, with a re-derivation command per row. `mistake_rows_exist()` reads `LOG.md`, `corpus/lessons/round-68.md`, `corpus/lessons/round-69.md` — not the corrections file — so the DEADPOINTER `live=False` (R68-M9 row now exists at `corpus/lessons/round-69.md:26`) is not self-satisfied by the annotator.
- The corrections landed where the rows say: `SCORECARD.md:1339` (`### Round-69 corrections to the filed round-68 self-assessment`), `LOG.md:4229` (round-69 entry), `corpus/lessons/round-69.md` `## Mistakes` (R68-M9) and `## Corrections (round 68, append-only)`.
- `live_mismatches=4` is arithmetically right: five pairs, DEADPOINTER no longer live because its pointer now resolves, the other four still live against frozen filed bytes (append-only; filed bytes are not rewritten).

**Verdict Ca2: PASS — `ACCEPT-CA-69: PASS 8/8`, exit 0, `unannotated_mismatches=0`, receipt body identical, both controls reproduce.**

## 3. D2 — depth

```
$ python3 -B reports/round-69/accept-d.py --root .
LEG PASS STAMP self=06b0352a0288 committed=06b0352a0288
LEG PASS SECTION heading=### Registry correction chains
LEG PASS TABLE header=5 rows=5
LEG PASS STATES states=['pending', 'settled-active', 'settled-retired', 'settled-closed', 'settled-split']
LEG PASS FIELDS empty=none short=none
LEG PASS SIGNATURES missing=none
LEG PASS EVIDENCE unresolved=none
LEG PASS SOURCE mined_used_by_SKILL=['S859', 'S859', 'S859', 'S859', 'S859']
ACCEPT-D-69: PASS legs=8/8
EXIT=0
```

Diff against `final-measures-d.txt` body: **IDENTICAL**.

Content verified by hand against the cited bytes (the depth claim is only as good as its pointers):

- `tools/check-supersession-settlement.py` at the cited lines: `:54` `SPLIT_RE` with the 40-char window; `:123` `if t_st == "rejected"` → settled-closed; `:125` `elif s_st == "rejected"` → settled-retired; `:127` settled-active; `:129` settled-split; `:132` `else` → pending; `:136` `same_url` diagnostic only; `:162-164` used-by existence-only; `:167` `return 1 if pending else 0` (the scan gate); `:21-22` the `STALE-USED-BY` caveat. Every table→code line pointer is correct, and the branch-order caveat ("both rejected reads settled-closed, never settled-retired") matches the code.
- Ledger pointers: 82 data rows in `dedup-ledger.tsv` (= the table's "82 ruling rows", header `:1-6`); `:7` S044>S034 `activate`; `:41` S034>S044 `keep-successor`/`deactivate`; `:19` S186>S157 `retire`/`cell-flip`; `:30` S490>S379 forced retire; `:75` S047>S029 `keep-reject`; `:83` S575>S420 `keep-split`; `:88` S830 keep-reject. `corpus/SOURCES.md:553` is S575; `LOG.md:4214` is the S490>S379 forced-retire note.
- The five signatures also appear under `## Error patterns` (SKILL.md:524-528), matching the SIGNATURES leg.
- S859 is real and re-runnable: 11 cells, status `mined`, used-by `SKILL.md, corpus/lessons/round-69.md`; its blob `1ef2e965204f53f40ffbabf45abea3fae9f029a6` equals both `52b92a6:tools/check-supersession-settlement.py` and `HEAD:…`; `python3 -B tools/check-supersession-settlement.py --selftest` → `SELFTEST: 7/7`, exit 0.

**But the declared do-nothing control no longer reproduces (finding F1).**

```
$ python3 -B reports/round-69/accept-d.py --root . --selftest
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: PASS (unexpected) (legs 8/8)
SELFTEST: 1/2
EXIT=1
```

Committed `telemetry/controls.txt` says `DO-NOTHING FIXTURE: FAIL (as required) (legs 1/8)`, `SELFTEST: 2/2`, `exit=0`. `claims.json` (D2 `do_nothing_control`) declares the FAIL. At the measured revision it does not happen.

**Verdict D2: PASS on the declared predicate (`ACCEPT-D-69: PASS 8/8`, exit 0, receipt body identical, counter still discriminates — see F1), FAIL on the declared do-nothing control at the measured revision (F1), with a depth-substance caveat: the legs never adjudicate the table's content (F4), and the landed `settled-closed` / `settled-active` rows overstate what code enforces (F3).**

## 4. Deviations from the receipts

| receipt | fresh run | deviation |
|---|---|---|
| `final-measures-o.txt` body | identical | none |
| `final-measures-ca.txt` body | identical | none |
| `final-measures-d.txt` body | identical | none |
| `controls-rev1.txt` (accept-o) | identical | none |
| `controls.txt` (accept-ca) | identical | none |
| `controls.txt` (accept-d) | `DO-NOTHING … PASS (unexpected)`, `SELFTEST: 1/2`, exit 1 | **deviation — F1** |
| 7 header lines in each `final-measures-*.txt` (counter sha, stamped/evaluated/measured revision, tree, dirty flag, clone note) | not printed by any of the three counters | **F5** — wrapper metadata, not counter output |

The header block is not emitted by the counters: `grep -rn "counter sha256 (self)\|measured in a materialized clone"` finds those strings only in old round-65/66 mutant copies, never in `reports/round-69/accept-*.py`. Its values are nonetheless consistent with git (self-sha matches, `e86ed3e` tree matches, delta to tip is receipts-only). The `exit=0` trailer is likewise wrapper-appended.

## 5. Findings

### F1 (High — control integrity, D2)
`accept-d.py --selftest`'s do-nothing fixture is not a do-nothing tree; it degrades with the data it is meant to control.

Root cause, `reports/round-69/accept-d.py`, `build_fixture_root()`:
```python
base = read_text(os.path.join(LANE, "SKILL.md")) or "# fixture\n"
if with_table:
    ...  # inserts FIXTURE_TABLE + FIXTURE_SIGNATURES
```
`with_table=False` performs no removal at all — contrary to the counter's own docstring ("the DO-NOTHING control (the same tree with the table removed… )"). It worked pre-data only because the live `SKILL.md` had no table then.

Proof it is a leak, not a different failure:
- Pre-data replay (lane copy, `SKILL.md` = `git show 6a98d7d:SKILL.md`, table count 0): `ACCEPT-D-69: FAIL legs=1/8`, exit 1 — reproduces the committed control exactly.
- Post-data replay with the table genuinely stripped (`/tmp/d-check`): `ACCEPT-D-69: FAIL legs=1/8`, exit 1 — same shape, so the counter itself still discriminates.
- The current selftest's do-nothing fixture therefore passes only because it inherits the landed table.

The GREEN fixture is contaminated the same way: `with_table=True` appends a second `### Registry correction chains` heading before `## Error patterns`, but `section_span()` returns the **first** heading, which in the post-data file is the real landed table. So green is also satisfied by the live file rather than by the fixture's own table.

Consequences: the committed `controls.txt` line (`FAIL (as required) (legs 1/8)`, `SELFTEST: 2/2`, `exit=0`) cannot be re-derived at the measured revision; anyone running the documented command today gets exit 1. This does not falsify the D2 lane predicate (8/8 stands, and discrimination is intact), but the declared control has silently inverted.

Fix shape (not applied; read-only seat): build the do-nothing base from a table-free source (e.g. remove the `HEADING` section, or start from the base-revision SKILL.md and require the section absent), and assert the fixture does not contain `HEADING` before evaluating.

### F2 (Medium — vacuous leg, O2 and D2)
The STAMP legs of `accept-o.py` (`:168-173`) and `accept-d.py` (`:132-136`) compare a path with itself under the declared invocation:

```python
mine = sha256_file(os.path.join(HERE, SELF))
committed = sha256_file(os.path.join(root, "reports", "round-69", SELF))
```

With `HERE = dirname(abspath(__file__))` and the declared `--root .` from the lane root, both resolve to the same file. Empirical probe in the clone (backed up with `cp`, restored byte-identical, `git status` clean):

```
# appended one comment line to each counter
tampered sha: 42a0cd5a9736… (accept-o), cf0ff42a92c2… (accept-d)
LEG PASS STAMP self=42a0cd5a9736 committed=42a0cd5a9736
ACCEPT-O-69: PASS legs=7/7
LEG PASS STAMP self=cf0ff42a92c2 committed=cf0ff42a92c2
ACCEPT-D-69: PASS legs=8/8
```

The leg is a self-hash echo; it cannot detect a modified counter, and the comment above it ("the counter under test is the committed one") is not what it tests. Not falsifying: the receipts' `counter sha256 (self)` header is written by the wrapper and does match the committed bytes, so tamper evidence exists at record level. `accept-ca.py` has no STAMP leg and relies on R68FROZEN, which is a real check.

### F3 (Medium — depth-substance accuracy of the landed table, D2)
The counter's structural green does not mean the table's cells are true. Three cells/claims overstate what the lane's own code enforces; each was reproduced in the clone.

**(a) `settled-closed` writer's next action is under-specified, and read the way its own cited precedent writes it, it fails the lane's gate on 10 of 12 live chains.** The cell reads "keep the successor: rule `keep-reject` from the registry bytes alone; nothing flips", and cites rows `:75` and `:88`. The frozen vocabulary constrains status only for three rulings (`check-supersession-settlement.py:207-212`): `activate` → `mined`; `retire` and `keep-reject` → `rejected`; `keep-successor` and `keep-split` are unconstrained. The registry has 12 live `settled-closed` chains (via `classify()`), and in 10 the successor is `mined` while the target is `rejected` (S185>S145, S570>S135, S571>S141, S572>S147, S573>S151, S574>S159, S648>S602, S649>S616, S650>S623, S651>S643). Three pairings were run against `--ledger`:

```
successor-side keep-reject     → LEDGER: rows=10 findings=10, EXIT=1
                                 (L1:S185 … L10:S651 keep_reject_but_status=mined)
target-side    keep-reject     → LEDGER: rows=10 findings=0,  EXIT=0
successor-side keep-successor  → LEDGER: rows=10 findings=0,  EXIT=0
```

The two green pairings are committed precedents, not inventions: row 75 `S047 | S029 | — | keep-reject` is a both-rejected chain (S047 and S029 each `rejected`), and row 78 `S570 | S135 | — | keep-successor` is the mined-successor shape (S570 `mined`, S135 `rejected`) — the precedent that matches the 10-chain majority. The table's cell mixes row 78's action ("keep the successor") with rows 75/88's ruling (`keep-reject`), and its evidence cell cites `:75` and `:88`, never `:78`. A reader who follows the cited example and writes `keep-reject` against the chain's successor row gets `keep_reject_but_status=mined` on 10 of the 12 live closed chains. The fix is available inside the frozen 5-row shape by naming the id first — "rule the successor row `keep-successor`; rule the rejected target row `keep-reject`" — and either statement alone is green.

A second Evidence-cell problem in the same row: `:88` names ledger row `S830 | S252 | — | keep-reject`, but S830's teaches carries no `supersedes` token (`corpus/SOURCES.md:784`), so `classify()` emits no chain for S830 (nor for S252) and `--scan` never reports either id. "Kept-reject fingerprint S830" is therefore not re-derivable from the checker the same cell cites; it is readable only from the ledger. The `:78` precedent is the one that both generalises and reproduces through the tool.

**(b) `settled-active`'s "used-by naming a real corpus path" is not what `classify()` tests.** Classification only tests truthiness of the used-by cell (`:122, :127`); existence is reported by the scan (`:162-164`), and the `--scan` exit code gates `pending` alone (`:167`). A successor whose used-by names a nonexistent path still classifies `settled-active` and exits 0:

```
SETTLED-ACTIVE S002>S001 s=mined t=queued same_url=False used_by=1
SETTLEMENT: pending=0 chains=1 usedby_paths=1 missing_paths=1
EXIT=0
```

The SKILL.md caveat covers "an existing used-by path is not a reading used-by", but the table's row shape asserts a *real corpus path* as the state's precondition. It is not one. The underlying instrument gap is already filed this round as R69-M5 (`corpus/lessons/round-69.md:31`: existence-only used-by, routed to round 70); what is new here is that the D2 table states the untested property as a state's row shape, telling the reader a check exists that no code path performs.

**(c) Malformed rows are handled inconsistently and silently.** A malformed **target** crashes `classify()`:

```
File "tools/check-supersession-settlement.py", line 121, in classify
    t_st = t_row["status"] if t_row else "missing"
KeyError: 'status'
EXIT=1
```

because `parse_registry()` stores a short row as `{"malformed": True, "id": …}` with no `status` key, and `rows.get(t)` still returns that dict. A malformed **successor** is dropped without a chain and without a diagnostic (`:116`, `if r.get("malformed") or not r["supersedes"]: continue`), so a broken correction row can hide the chain it should open. R69-M4 (`corpus/lessons/round-69.md:30`) already records the swallow and routes it to round 70; the target-side `KeyError` is the refinement — a malformed row then fails loudly with exit 1, which is the exit code `--scan` uses for *pending*, so an instrument error and correction debt are indistinguishable by exit status alone.

(a) is `L1Kotodama69.CritDepth`'s discovery, including the `:88` observation; (b) and (c) corroborate the committed R69-M5 / R69-M4 records and add the malformed-target refinement; every reproduction above is mine.

**(d) The base tool's own docstring overstates ACTIVE and CLOSED.** `tools/check-supersession-settlement.py:8-10` says SETTLED-ACTIVE requires "a `used-by` naming a real corpus path" and a superseded row "no longer `mined` (`queued` or `rejected`)", and `:13-14` calls CLOSED a "keep-successor fingerprint" without naming the statuses involved. The code cannot produce that ACTIVE shape: `:123` tests the target's `rejected` status first and returns `settled-closed`, so `:127`'s `t_st == "queued"` (not "queued or rejected") is the only reachable ACTIVE branch, and the used-by test is truthiness only (`:122`, §F3b). The D2 table's new wording is closer to the code than the docstring is; the docstring is the stale copy, and it is committed, not part of the working-tree drift. (Found by `L1Kotodama69.CritDepth`; re-read here.)

### F4 (Low — content is never adjudicated, D2)
The D2 legs test presence and shape only; a table with no technical content passes 8/8. Probe: replace the section with five filler rows (correct state names, every other cell `filler`, one `TODO` signature duplicated into `## Error patterns`, every evidence cell `S859 — tools/check-supersession-settlement.py:1`):

```
LEG PASS SECTION heading=### Registry correction chains
LEG PASS TABLE header=5 rows=5
LEG PASS STATES …
LEG PASS FIELDS empty=none short=none
LEG PASS SIGNATURES missing=none
LEG PASS EVIDENCE unresolved=none
LEG PASS SOURCE mined_used_by_SKILL=['S859', …]
ACCEPT-D-69: PASS legs=8/8
EXIT=0
```

So what the counter proves is: one heading, five columns × five rows, the five state names in order, each signature string appearing somewhere under `## Error patterns`, each evidence cell containing at least one existing path token, and one S-row that is `mined` with `SKILL.md` in its used-by. Nothing about whether a row shape is true, whether a signature is distinct, or whether a `:NNN` pointer points where it says.

Corroborating probes: (i) bogus line pointers (`:9995`–`:9999`) still yield `EVIDENCE unresolved=none` / 8/8; (ii) the counter's own `FIXTURE_TABLE` replayed on the base revision `793f7974:SKILL.md` passes 8/8 even though it points `pending` at `:112` (real `:132`), `settled-retired` at `:129` (real `:125`) and `settled-split` at `:130` (real `:129`). The landed table's own pointers are all correct (§3), so this is a limit on what green means, not a false positive in the data.

### F5 (Info — deviation)
The seven provenance header lines in each `final-measures-*.txt` are wrapper metadata, not counter output; they are not reproducible with the declared counting command. Values are consistent with git (§0).

### Not findings
- `claims.json`'s "three round-68 counters" is accurate: `accept-o.py`, `accept-c.py`, `accept-ca.py` (there is no round-68 `accept-d.py`).
- Ca2's `ok` for a covered-but-live pair reduces to "a correction row exists", which is the claim's own design (calibration annotates frozen filed bytes; it does not rewrite them).
- O2's revision history is consistent: `controls.txt` records the rev-0 number for the do-nothing control (6/7) while `controls-rev1.txt` records rev 1 (5/7), and the current counter prints 5/7.

## 6. Residual risk

- **D2's declared do-nothing control is inverted at the measured revision** (F1). If a later seat treats `--selftest` as the health check for D2's instrument, it reads red (exit 1) for a green counter — and, symmetrically, a genuinely do-nothing tree can no longer be constructed by the shipped selftest, so the control's original evidence depends on a revision that is no longer reachable by the documented command.
- **D2's depth evidence is structural, not substantive** (F3, F4). Green proves a five-row table with the right state names, signature strings and existing path tokens exists — a filler table scores 8/8. The landed table's pointers and signatures are accurate (verified), but two row-shape cells assert preconditions the code does not enforce, and the `settled-closed` action cell can be applied in a way that fails the lane's own ledger gate on 10 of 12 live chains.
- Ca2 counts only the five declared pairs; a mismatch on an undeclared surface is invisible by design.
- Ca2's DEADPOINTER class clears as soon as the string `R68-M9` appears anywhere in `LOG.md`/`lessons-68`/`lessons-69`; it cannot distinguish "row correct" from "row mentions the id".
- Ca2 reads the live fleet file `/home/vgpnk/Projects/shokunin/.ufo/reports/round-68/kotodama.md`; it is clean in the fleet worktree (last commit `cbc87da3`), but an external edit would move `MISMATCHES` without any lane change.

## 7. Verification gaps (honest accounting)

- I did not execute the counters at `6a98d7d` itself (no checkout — mutating git is prohibited for this seat); pre-data behaviour was established by replaying the fixture against `git show 6a98d7d:SKILL.md` in a copy, which reproduced the committed control number exactly (`FAIL 1/8`).
- The `# worktree dirty (tracked): False` header line cannot be re-verified retroactively; what is verifiable (clean clone, receipts-only delta) is reported above.
- I did not review the wave-1 seat reports beyond a grep for prior notice of F1: no w1 or w2 report records the do-nothing inversion (`w2-verify` held only this file when written; pre-data critique statements about `accept-d` "selftest 2/2" were recorded pre-data and are consistent with F1).
- Cross-check with `L1Kotodama69.CritDepth` (whose file now records the D2 content critique): I re-ran all four of their content claims in my own clone and they reproduce exactly — filler table 8/8 (F4), `FIXTURE_TABLE` on base 8/8 with wrong pointers (F4), `keep-reject` on the successor row 10 findings vs 0 on the target (F3a), fake used-by still `SETTLED-ACTIVE` exit 0 (F3b), malformed target `KeyError: 'status'` at `:121` and malformed successor silently dropped (F3c). The wording in F3 is mine, derived from those runs.
- Not my scope (other seats): mutation battery, records/anchoring critique, item-10 scout.

## 8. Post-repair state (verified at the current tip, not part of the original measurement)

Every number in §0–§7 was measured at the clean commit `9e82c7b`, and the line numbers cited there are `9e82c7b` line numbers. The lane has since advanced: the content repair landed at `975e8f2` and the re-measurement records at `3e59d1d`. §8 was verified against `3e59d1d`; `ef75509` landed afterwards and touches only `.ufo/waves/round-69/w2-verify/CritDepth.md` — no counter, SKILL.md or telemetry change, so every result below still applies at the current tip. This section does not alter the verdicts, which stand for the revision they name.

Re-run at `3e59d1d` in a fresh clone (`/tmp/RevRerun-r69-post`):

```
accept-o.py --root .                              → ACCEPT-O-69: PASS legs=7/7   exit 0
accept-ca.py --root . --fleet-root …/shokunin     → ACCEPT-CA-69: PASS legs=8/8  exit 0
accept-d.py --root .                              → ACCEPT-D-69: PASS legs=8/8   exit 0
```

All three LEG bodies are **identical** to the newly committed `final-measures-{o,ca,d}-attempt2.txt`, so the re-take reproduces line-for-line. The attempt-2 receipts stamp `measured revision 975e8f2`, `tree b154a91907a240e92bb5824f1232704b7ebd69f3`, clean worktree, and the counter sha256 headers are unchanged (`08c7ea61…`, `091074c5…`, `06b0352a…`).

Controls at the current tip match `controls-attempt2.txt` exactly: O green 7/7 / do-nothing FAIL 5/7 / spoof FAIL 6/7 / `3/3`, exit 0; Ca green 8/8 / do-nothing FAIL 2/8 / `2/2`, exit 0; D green 8/8 / do-nothing **PASS (unexpected)** 8/8 / `1/2`, exit 1. The attempt-2 receipt names that D state as R69-M11 rather than claiming it green — which is the honest handling, and it confirms F1 at the new revision.

What the landed repair does to my findings:

- **F3(a) main defect fixed.** The `settled-closed` cell now names both subcases and both ids — "rule `keep-successor` when it is `mined` (S570>S135, ledger `:78`), `keep-reject` when it is itself `rejected` (S047>S029, `:75`) … the ruling attaches to the row the validator checks, and `keep-reject` is refused unless that row reads `rejected` (`:211-212`)" — which is exactly the wording the three ledger probes supported.
- **F3(a) residual survives.** The same evidence cell still ends "kept-reject fingerprint S830 `:88`". S830's teaches has no `supersedes` token (`corpus/SOURCES.md:784`), so `classify()` emits no chain for it and `--scan` can never produce that fingerprint: the pointer is ledger-only, not re-derivable through the checker the cell cites. This is the one repaired-cell residual I can still reproduce at `3e59d1d`.
- **F3(b) addressed in prose**: "a non-`—` `used-by` cell (path existence is reported as `missing_paths`, not gated, `:162-164`)". **F3(c)** is documented in the new malformed-row caution citing R69-M4. **F3(d)** (the tool docstring saying ACTIVE's target may be "queued or rejected") is untouched — committed code, not the table.
- **F1, F2, F3/F4 are now indexed in the record** as R69-M11, R69-M10 and R69-M12 (`corpus/lessons/round-69.md:36-38`); M12's evidence includes the 5-row-filler-scores-8/8 probe. My report and the lesson rows agree; no finding of mine is left unrecorded.
- The earlier bookkeeping concern is settled by the new receipts: the original `final-measures-*.txt` header pinned the pre-repair SKILL.md blob `a66a75fd…` through tree `b3064e1f…`, the repaired blob is `2476a9c05662756ad8c1a79ee63d8972798c0cc7`, and the attempt-2 receipts pin the repaired tree `b154a919…`. Note that the counters' STAMP legs still hash only the counter (F2 / R69-M10), so the receipt's tree hash remains the sole pin of the measured SKILL.md — a landed edit without a re-take would still be uncovered.
