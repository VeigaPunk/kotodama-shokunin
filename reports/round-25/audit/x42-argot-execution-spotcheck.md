# R25-X42 — spot-check audit: the argot-execution leg, independently re-run

- Seat **R25-X42** (SCRIBE X42: spot-check auditor — argot execution re-runs). Round 25
  (operator: loop 3 of 3, build 1 of 4; 64 workers on `devin/deepseek-v4-1-flash-high` —
  `reports/round-25/targets.json`: O-gate-input 10, O-v3-supersession 10, D-argot 24,
  C-lessons 12, X 8).
- Date: **2026-10-18**. Every count below carries its command and date; raw receipts live in
  this seat's scratch (`.scratch/r25-x42/`, gitignored) and only this fragment is filed.
- Declared baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc` (`reports/round-25/claims.json`);
  lane HEAD `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- **Write scope: this fragment only.** No filed round-8–24 byte is edited; no tool, gate,
  packet, component, fixture or sibling fragment is changed; no Git mutation. The round-25
  runner was executed only inside an isolated clone under `.scratch/`, as its own guard
  requires. NON-CANON engineering evidence; canon standing is lore-shokunin's.
- **Independence.** Every command below was executed by this seat, in this seat's own shell.
  Sibling fragments are cited as *attribution* (what they claim), never as this seat's
  measurement. Where a sibling's number and this seat's differ, both are printed.

## 0. This audit ran across a live landing — the finding that matters most

When this seat started, the D leg did not exist as a tool: `grep -rl "ARGOT" tools/ examples/`
returned nothing, and the four `reports/round-25/argot/execution-*.md` fragments described a
**scratch** harness. During the audit the implementation landed — `tools/gates/argot-derivation-gate.py`
plus its two fixture files — and `tools/gates/typed-pipeline-gate.py` was revised for the O
fix. The round-25 runner itself moved **three times** inside this window
(`aaeab0cb31a5` → `141b77d7e215` → `d6e27b91edb7` → `4cd6f066f823`), and the **first** revision
this seat ran scored claim D red on two failures that the current revision does not have.

The consequence is a hard limit on every receipt in this fragment: **a receipt binds the bytes
it was taken against.** The final measurements below were taken after the runner, the argot
gate and the typed gate all stopped moving (three consecutive 30 s polls, 14:38:39–14:39:39,
identical digests). Anything measured earlier in the window is reported as *observed
in-flight*, not as a verdict.

## 1. The audited surfaces, and their final digests

All digests measured by this seat 2026-10-18, after stability:

| surface | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` |
| `examples/culture-d4/packet.d4.typed.yml` | `ffece0feb52c5b0b8ae6b0f8c1848d6220ad2dc2b36b1faac6385d62f4bfd84e` |
| `tools/gates/argot-derivation-gate.py` (new this round) | `07db6e9b4e01539e1dbb8af9e51eada6fe37784145915a0387f48f2ecd99f8fe` |
| `tools/gates/fixtures/argot-derivation-gate.yml` | `c4c35294d581b204482427b3776776c57d1e7f83065a0b5f8f3906c38d8c2ccd` |
| `tools/gates/fixtures/argot-derivation-gate.expected` | `38a283ff3b7cef4336418237f345f3602c4faeee197baca4d1ebc1bb0f78a018` |
| `tools/gates/typed-pipeline-gate.py` (O fix) | `879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126` |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` |
| `reports/round-25/run-validation.py` | `4cd6f066f823c7e0eb3eb3f07d661d171a344c1fb78086c67ebb3ae5c9678779` |
| `.scratch/r25-d11/argot-replay.py` (the D11 scratch harness) | `4934f17d0cfed1b5248d45aca18dab6b129d42ce709981b76ed70f5f7853673d` |

The naming gate's digest is unchanged from the round-24 audits, so the replay semantics this
seat exercised are the frozen ones. The two culture packets are byte-unchanged all round.

## 2. Verdict summary

| # | audited claim (source) | this seat's measurement | verdict |
|---|---|---|---|
| X42-1 | execution 1: 12 stated-derivation rows replay, 0 violations | 12 rows, 0 violations, exit 0 | **REPRODUCED** |
| X42-2 | the design's 11 worked argot derivations re-derive | 11/11 agree | **REPRODUCED** |
| X42-3 | execution 2: two tamper controls each yield exactly 1 violation | 1 violation each, naming record+rule+values | **REPRODUCED** |
| X42-4 | execution 2: the false red is manufactured by the L2 rebuild | isolated to one escape; 0→8 `DERIV-REPLAY` | **REPRODUCED, root-caused** |
| X42-5 | execution 3: the forecast-vs-delivered delta names every element | 13/13 elements re-measure absent | **REPRODUCED** |
| X42-6 | execution 4: the register-form leg has no input on the delivered tree | 0 slots, 0 `derived_from`, 0 operations | **REPRODUCED** |
| X42-7 | the delta's root cause: round-17 shipped the furnace-league, not the weigh-court | confirmed at `design-brief.md:596-670`, `01-brief.yml:79,85` | **CONFIRMED** |
| X42-8 | the landed argot gate discriminates (correct passes, violating fails) | `reverse` and `head2` pairs both discriminate | **CONFIRMED** |
| X42-9 | claim D as scored by the round-25 runner | `passed=true`, 0 failures at runner `4cd6f066` | **PASSES** |
| X42-10 | the O fix: derived-packet input is honest | typed packet now exit 0, no `DERIV-REPLAY` | **CONFIRMED** |
| X42-11 | D02 `current-state.md` §4 census: `reverse`/`slot_ref` in `tools/` = 0 | `reverse` = 6, `slot_ref` = 7 | **VALUE DRIFT** (§5) |

## 3. The scratch-harness claims, re-run (X42-1..X42-6)

All commands below: `export TMPDIR=$PWD/.scratch`, cwd = lane root, 2026-10-18.

```
python3 -B .scratch/r25-d11/argot-replay.py examples/culture-d4/packet.d4.yml
```

→ exit **0**; `"rules": ["CX-01","CX-02","CX-03"], "rows": 12, "violations": 0`; twelve `ok`
lines (`L-45 tikmes` / `L-46 mesar` / `L-47 kalen` / `L-48 haitun` + `NM-01..NM-08`). This seat's
own run of the sibling's harness reproduces execution 1 exactly (**X42-1**).

```
python3 -B .scratch/r25-d11/argot-replay.py .scratch/r25-d11/mirror/packet.d4-tamper-lex.yml
python3 -B .scratch/r25-d11/argot-replay.py .scratch/r25-d11/mirror/packet.d4-tamper-name.yml
```

→ `"violations": 1` each; `VIOL L-46 | mesor | derived | CX-02 | mesar | replay disagrees` and
`VIOL NM-05 | haitka | name | CX-01 | haitik | replay='haitik' name='haitka' expected='haitik'`.
Both fire; the name-side message separates the three values (**X42-3**).

This seat's own controls, written independently of that harness
(`.scratch/r25-x42/argot-replay-audit.py`, legs A/B):

- **leg A** — the two operations re-implemented from `design-language.md` §5's stated algorithms,
  re-derived against the design's own 11 worked rows → **11/11 agree**; `saalumi` → `saa.lu.mi` →
  `saalu` (maximal onset). The onset/coda disagreement the design names is reproduced (**X42-2**).
  (First pass of this seat's own code returned `saa` for `saalumi`; the correct reading treats the
  length mark as **one long-vowel token**, not two short vowels. Recorded because it is exactly
  the reading the design says is load-bearing.)
- **leg B** — negative control: a pair list with one tampered quote form → exactly **one**
  `D4L-ARGOT-DERIV` FAIL; the all-correct list → **0** findings. The relation discriminates.

This seat's own replay of the *delivered* formation surface (independent code) → **8/8**
(`tum+hai→tumhai`, `kal+ker→kalker`, `sam+ren→samren`, `mes+tum→mestum`, `hai+tik→haitik`,
`mes+lun→meslun`, `kal+nes→kalnes`, `sal+wer→salwer`).

### 3.1 X42-4 — the false red, isolated to a single variable

Execution 2 attributes the false red to the L2 rebuild doubling the packet-authored regex
backslash. This seat reproduced the stored values and then isolated the cause:

| file | stored CX-01 `pattern` | `re.match(pat, 'tum+hai')` |
|---|---|---|
| `examples/culture-d4/packet.d4.yml` | `^(?P<a>.+)\+(?P<b>.+)$` | **True** |
| `examples/culture-d4/packet.d4.typed.yml` | `^(?P<a>.+)\+(?P<b>.+)$` | **True** |
| `.scratch/r25-o1/rebuilt-legacy.yml` (the L2 mirror) | `^(?P<a>.+)\\\+(?P<b>.+)$` | **False** |

The decisive control is a **single-variable mutation of the source packet** — change *only* the
escape on line 209 (`\\+` → `\\\\+`), touch nothing else:

| input | exit | findings | `DERIV-REPLAY` |
|---|---|---|---|
| `examples/culture-d4/packet.d4.yml` (baseline) | 1 | 14 | **0** |
| same packet, line 209 escape doubled | 1 | **22** | **8** |

An 8-row delta from one character-class change, naming `NM-01`..`NM-08`, is the manufactured
class. This seat also reproduced the sibling's three receipts by re-running the gate itself:

| run | input | exit | `grep -c DERIV` |
|---|---|---|---|
| A | source packet | 1 | 0 |
| B | typed packet, read **directly** | 1 | 0 |
| C | `.scratch/r25-o1/rebuilt-legacy.yml` | 1 | **8** |

The red exists only in the gate's in-memory rebuild, not in either delivered artifact — which is
the O claim's hazard (a), correctly scoped as **not** a D4 defect.

### 3.2 X42-5 / X42-6 — the delta and the empty register domain

This seat's own token census (2026-10-18):

| token | `packet.d4.yml` | `packet.d4.typed.yml` | components | `tools/` |
|---|---|---|---|---|
| `ARGOT` / `argot` | 0 | 0 | 0 | 0 |
| `head2` | 0 | 0 | 0 | 0 |
| `derived_from` | 0 | 0 | 0 | 0 |
| `derived_forms` / `derived_ok` | 0 | 0 | 0 | 0 |
| `doublet_of` | 0 | 0 | 0 | 0 |

`grep -rl "D4-X" examples/ tools/` → **0** files; `grep -c 'term: "' packet.d4.yml` → **54**
lexicon records; top-level packet keys → **34**. The delivered derivation surface is the
CX-01/02/03 table only, and all 8 delivered names are CX-01 compounds — so the register-form leg
of execution 4 has, as claimed, **zero input** (**X42-6**). The 13 forecast elements (F-1..F-8,
Δ1-class2, Δ2, AL-01..06, name-side argot, the 11 derivations) each re-measure absent (**X42-5**).

## 4. X42-7 — the delta's root cause is documented, not inferred

The delta file (execution 3 §1) states the forecast was written against a **weigh-court** culture
and the delivered D4 is the **furnace-league**. This seat confirmed the divergence is recorded in
the round-17 design docs:

- `reports/round-17/d4/design-brief.md:596-612` — a status table listing **five mutually
  divergent** round-17 D4 positions (weigh-court COUNT × QUOTE; furnace-league FIRE × MARK;
  TIDE + LEDGER; a salt-flat caravan confederation; a tide-work wardrobe), with the explicit note
  that they "do **not** agree on the D4 culture, the component registry, or the hold set".
- `reports/round-17/d4/design-brief.md:653-663` — the three reconciliation paths **A/B/C**, marked
  "parent's decision; this seat implements none".
- `examples/culture-d4/components/01-brief.yml:79,85` — the shipped `SEED-01`/`SEED-07`:
  "Furnace-league culture…" / "Non-negotiable spine: FIRE … + MARK", i.e. **path A** shipped.

So the argot's non-delivery is a consequence of the shipped culture choice, not an oversight in
the argot leg. This seat records the root cause as **documented at the cited lines**; it does
**not** adjudicate which path was correct — that is the parent's, per the brief's own note.

## 5. X42-8 — the landed argot gate discriminates (this seat's own fixtures)

The claim requires the leg be "implemented and executed on D4". By the end of the window it is a
real gate: `tools/gates/argot-derivation-gate.py`, 701 lines, stdlib-only, with an embedded
`head2`/`reverse` operation table (maximal-onset syllabification cited to `design-language.md` §5),
three rule sources (built-in ops → packet `morphology.derivation_rules` → layer substitutions),
and four ids (`D4L-ARGOT-DATA` exit 2, `D4L-ARGOT-DERIV` FAIL, `D4L-ARGOT-RULE`/`-COVERAGE` HOLD).

This seat wrote its **own** minimal fixtures (`.scratch/r25-x42/ctl/`) rather than reusing the
sibling's, and probed both directions:

| fixture | declared | form | gate exit | finding |
|---|---|---|---|---|
| `ok` | `reverse`, base `min` | `nim` (correct) | **0** | none — clean |
| `bad` | `reverse`, base `min` | `min2` (wrong) | **1** | `D4L-ARGOT-DERIV` FAIL, names `reverse`/`min`/`nim` |
| `identity` | `reverse`, base `min` | `min` (not a derivation) | **1** | `D4L-ARGOT-DERIV` FAIL |
| `head2-ok` | `head2`, base `saalumi` | `saalu` (maximal onset) | **0** | none — clean |
| `head2-coda-wrong` | `head2`, base `saalumi` | `saalum` (maximal coda) | **1** | `D4L-ARGOT-DERIV` FAIL, yields `saalu` |

The gate is discriminating in both operations, and it implements the **maximal-onset** reading the
design says is load-bearing (accepts `saalu`, rejects `saalum`). The gate's own `--selftest` →
**18/18, exit 0**; its canonical D4 run → exit 0,
`coverage: records=156 register_scoped=6 derived_pairs=0 borrow_pairs=6 violations=0 rule_holds=0`.
Note `derived_pairs=0`: the delivered packet declares no argot pair, so the gate's D4 run is a
**clean run over an empty domain**, not evidence that D4's argot forms replay — the distinction
execution 3's delta makes. (An earlier revision of the gate crashed its selftest with
`NameError: record_id`; the shipped revision does not. Recorded as observed in-flight.)

## 6. X42-9 / X42-10 — the round-25 runner, and the O fix

The runner refuses to run in-tree (`could-not-evaluate: run round validators only in an isolated
Git clone under the lane's .scratch`, exit 2), so this seat built a `git clone` of the lane under
`.scratch/`, verified the declared baseline `e06581b7` is reachable, overlaid the live round-25 /
tools / corpus trees, and ran `python3 -B reports/round-25/run-validation.py --check`.

**Runner revisions observed in this window:** `aaeab0cb31a5` → `141b77d7e215` → `d6e27b91edb7` →
`4cd6f066f823`. Against `aaeab0cb` (the first revision this seat ran) claim D was **red** on two
failures ("the D4 typed gate's selftest names no argot/derivation-replay control"; "the control …
emits neither `D4L-ARGOT-DERIV` nor a named derivation diagnostic") — a superseded receipt, since
that revision's own control leg called the typed gate where the current one calls the argot gate.

Against the stable revision `4cd6f066f823` (this seat's own clone run, exit 0):

| claim | passed | failures |
|---|---|---|
| O | **true** | none |
| D | **true** | none |
| C | **true** | none |

`acceptance_checks_passed: true`, `missing_dependencies: []`. The D measurement records
`argot_gate.selftest_summary: "selftest: 18/18 checks passed"`, `d4_run_exit: 0`,
`control_violating_derivation.argot_id_emitted: true` (exit 1) with `positive_control_exit: 0`,
and `runner_independent_rederivation: 11/11, mismatches: []` — i.e. the runner re-derives the
eleven design pairs with **its own** implementation, never reading them back from the design doc.
The runner also records `typed_gate_carries_the_leg: false`, and the delta's addendum
(`reports/round-25/argot/delta.md` §8, "a sibling seat landed an argot gate mid-window") names that
substitution — which is the runner's stated requirement for a substituted leg.

**X42-10 — the O fix.** `tools/gates/typed-pipeline-gate.py` gained `owed_slot_of()`
(null-normalization for the lane's reader, which keeps an unquoted YAML `null` as the string) and
an `L2-legacy-source` leg that uses the **declared assembler's own `assemble()`** instead of the
D2 `yaml_lines` round-trip. Measured by this seat after the fix:

| input | before (round-24 cold run) | after |
|---|---|---|
| `packet.d4.typed.yml` | exit 1, 14/16 legs, 8 false `DERIV-REPLAY`, `L3-routing-consistency` FAIL | **exit 0, 16/16 legs**, no `DERIV-REPLAY` |
| `packet.d4.yml` (documented entry) | exit 0, 19/19 | **exit 0, 19/19** (unchanged) |
| `--selftest` / `--selftest-generalized` | 12/12 / — | **12/12 / 14/14**, both exit 0 |

Feeding the typed packet back can no longer manufacture findings. (The leg count moved 17/17 → 16/16
across two mid-window revisions; both are exit 0 and both have zero `DERIV-REPLAY`. The count is
reported as observed, not as a pinned value.)

## 7. X42-11 — a value drift in the audited census (conclusion unaffected)

`current-state.md` §4's token table reports `reverse` and `slot_ref` as **0** in `tools/`.
Re-running the file's own command shape, this seat gets non-zero values:

| token | D02's filed table (`tools/`) | this seat's measurement | what the hits actually are |
|---|---|---|---|
| `reverse` | 0 | **6** (4 files) | all `sorted(..., reverse=True)` / `reversed()` — a Python sort keyword, not the argot operation |
| `slot_ref` | 0 | **7** (1 file) | the D2 rank-property field `slot_ref` in `tools/d2-typed-labels.py` (`:432,902,904,1036,1041`), not a register slot |

Command: `grep -rho -- "$t" tools/*.py tools/gates/*.py | wc -l` for `t` in `reverse`, `slot_ref`
(2026-10-18). The filed `0` values are **wrong as counts**; they are **right as conclusions**,
because `grep -rn -- reverse tools/*.py tools/gates/*.py | grep -i "argot\|derivation\|head2"` → **0**:
none of the hits is an argot operation. Flagged so the integrator can correct or footnote the table
before it is cited as a receipt; the delta it supports does not change. (At final measurement
`reverse` in `tools/` reads 30 across the tree including the new argot gate, whose `reverse` is now
a real operation — the drift is in the pre-landing table's snapshot, which is why a re-read is owed.)

## 8. Corroboration of the sibling audits, and where this seat differs

- `reports/round-25/audit/x47-argot-negatives-audit.py` — re-run by this seat: `--selftest`
  **9/9**, exit 0; full run exit 0; its `R25-X47-1` 11/11, `R25-X47-2` (0 pairs / 0 argot rows),
  `R25-X47-3` (backslash doubled) and `R25-X47-4` (leg discriminating) all agree with this seat's
  independent measurements. Its claims hold.
- `reports/round-25/scribe/capability-row.md` §3's four stdout digests — re-run by this seat,
  **3/3 match exactly** (`naming` `0c613c9d…`, `typed-pipeline` `b064da28…`, `d4-assembly`
  `c60820a5…`) at this tree. Its §4(a) control (mutate CX-01's `output` to `{a}-{b}`) —
  reproduced here: **14 findings / 0 `DERIV-REPLAY`** unmutated vs **22 / 8** mutated, as filed.
- Where this seat differs: §7's two census values, and §6's runner-revision observation — the
  sibling capability row's gating note ("the leg is not on disk") was true at its stamp and is
  **no longer true** after the landing.

## 9. Limits and `to-verify`

1. **The window moved under the audit.** Three runner revisions and two gate landings occurred
   inside it. Every number above is bound to §1's digests; a number measured before 14:38Z is
   labelled in-flight. A receipt against superseded runner bytes is a superseded receipt.
2. **Scratch harnesses are not lane artifacts.** The D11 harness and the four fixtures live under
   `.scratch/` (gitignored); the four `reports/round-25/argot/execution-*.md` fragments are the
   filed record, and they say so.
3. **The gate's D4 run is clean over an empty domain.** `derived_pairs=0` means the delivered
   packet declares no argot pair; the discriminating evidence is this seat's own fixtures (§5),
   not the D4 run.
4. **The false-red mechanism is named, not repaired here.** Repairing the L2 rebuild is the O
   claim's scope; this seat isolated it and confirmed the landed fix.
5. **Not admission.** Nothing here admits a claim, verifies a promotion, or clears canon. The
   runner's `--check` output in this seat's clone is evidence of a run, not a round verdict.

## 10. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
# the landed gate, both directions
python3 -B tools/gates/argot-derivation-gate.py --selftest                     # 18/18, exit 0
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml  # exit 0, derived_pairs=0
python3 -B tools/gates/argot-derivation-gate.py .scratch/r25-x42/ctl/bad.yml   # exit 1, D4L-ARGOT-DERIV
python3 -B tools/gates/argot-derivation-gate.py .scratch/r25-x42/ctl/ok.yml    # exit 0
# the O fix
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml  # exit 0, 16/16, 0 DERIV-REPLAY
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml        # exit 0, 19/19
# the scratch harness the D fragments cite
python3 -B .scratch/r25-d11/argot-replay.py examples/culture-d4/packet.d4.yml  # 12 rows, 0 violations
# the round validator (isolated clone only)
cd .scratch/r25-x42/clone/repo && python3 -B reports/round-25/run-validation.py --check   # exit 0, O/D/C all passed
```
