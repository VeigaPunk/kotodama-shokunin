# R28-D01 — the register law's replay leg: what it resolves, against what, and what it finds

- **Seat:** R28-D01 (D axis, law-replay design 1 of 4), round 28, loop 3 build 4
  of 4 — the last build round. Claim **D** `register-law-replay`
  (`reports/round-28/claims.json`).
- **Date:** 2026-10-18 (measurements 20:0x–20:15Z). Baseline revision
  `69cecbc7dcf575a29f29660ecac470e05260fd86` ("round-28: declare claims D/O/C"),
  lane HEAD `69cecbc`. Declaration commit `69cecbc`; baseline of the round's
  claim text is `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`.
- **Reads first, as the assignment directs:** `reports/round-27/law/design.md`
  (`27d23fa6…` sibling; this round's own reading is digest-pinned below),
  `reports/round-27/law/review.md` (RL-1 §2, RL-3 §4, RL-4 §5),
  `reports/round-27/law/impl-5.md` (the three law controls C-1/C-2/C-2b),
  `reports/round-27/law/rules.md` (the RLAW-01..06 registry), and the delivered
  bytes themselves.
- **Write scope:** `reports/round-28/law/{design,vocab,rl4-delta,review}.md`,
  plus gitignored scratch under `.scratch/r28-law/`.
  `export TMPDIR=$PWD/.scratch` preceded every scratch-writing command. No
  component, packet, tool, gate, fixture, pin file, or filed rounds 8–27 byte
  was written by this seat; no commit, no push.
- **Canon:** NON-CANON engineering design. No real language, institution, script
  or argot is described, cited or approximated. No clearance is claimed.

**Verdict in one line.** The law now has a designed replay leg with **three
resolutions** (speaker, force, consequence) and **six finding classes**; it is
calibrated against the delivered bytes and it **fires 6 findings on the clean
packet** — because the delivered law has real defects, not because the leg is
over-sensitive. Its teeth are proven on four controls that add a finding each,
and two controls are **inert, which is reported rather than hidden**.

## 0. The gap this seat closes, restated in round 27's own words

Round 27 named the law's central honesty as finding **RL-1**:

> "A law row whose `force` is nonsense is **invisible** … Identical.
> `force: "no-such-force"` produces no finding anywhere in the pipeline.
> **The law, as landable today, is a declaration with no teeth.**"
> — `reports/round-27/law/review.md` §2

and its sibling implementation seat measured it three ways:

> "C-1, C-2 and C-2b produce **the same finding count as the clean packet**.
> Three independent mutations of the law — a bogus illocutionary force, a deleted
> row, a deleted clause classifier — are invisible to every delivered gate."
> — `reports/round-27/law/impl-5.md` §3

Round 27 then **declined to build the leg**, and the reason was measured rather
than stylistic: the obvious repair (`property.kind: register` in `rank_rules`)
routes into the family projector's **costume-rank** resolver, whose `verdict_for`
reads `row["material"]`, `row["garment"]`, `row["badge_office"]` — fields a
speech act does not have — and whose membership guard widened turns an honest
hold into a silent `not-applies` (`reports/round-27/law/review.md` §3).

**This design takes the other road.** It does not amend the projector. It
specifies a **standalone checking leg** that reads the packet's own blocks and
resolves the law's three clauses against them. §1 fixes what it resolves; §2
fixes the finding classes; §3 calibrates it against the delivered bytes; §4
prices the alternative (a projector amendment) so the choice is re-makeable on
evidence; §5 declares the limits.

## 1. What the leg resolves, and the ground truth for each resolution

The leg answers the three questions the round-27 design fixed
(`reports/round-27/law/design.md` §1), plus two structural questions the
delivered bytes force. **Each resolution names its own ground truth**, and the
choice of ground truth is where the leg can go wrong — §3.3 measures one such
wrong choice directly.

| # | resolution | field | ground truth | why that ground truth |
|---|---|---|---|---|
| 1 | **who may speak** | `speaker`, `holder` | the ids the packet carries **as records** (every list block's rows' `id`) | the round-27 design already wrote the citation in the `Name (ID)` shape — `mold-keeper (OR-02, component-only)` — so the id is the resolvable token, and the packet's own record set is the only authority |
| 2 | **with what force** | `force` | a declared illocutionary-class vocabulary (§`vocab.md`) | `force` is a closed semantic field (Searle's five classes); a value outside it is a typo or a prose leak, and both are findings |
| 3 | **with what record consequence** | `consequence` | the delivered roll/rank machinery — a **stem** list | the consequence is a claim that *something happens to a record*; the packet supplies the stems (`roll`, `rank`, `rk-`, `tally`, `entry`, `void`, `binds`, …) and nothing else |
| 4 | **in which register** | `register` | the **register names** the `registers` block declares (`plain`, `stamp`) | the law row says `register: "stamp"`, and `stamp` is a *name*, not an id; resolving against `QREG-01..04` is the wrong ground truth and is measured wrong in §3.3 |
| 5 | **on which axis** | `axis` | the spine's declared axis vocabulary (`mark`, `fire`, …) | the packet's own `spine_coupling` names the axes; an axis outside it is outside the culture |

**Resolution 1's granularity is a design choice, and it is the one that
matters.** Two readings are available and they disagree:

- **(a) by office name** — `mold-keeper` must be a `wearer_ranks` value or an
  institution name.
- **(b) by record id** — the parenthetical `(OR-02)` must be a delivered record.

The delivered bytes resolve **differently** under each, and §3.2 measures it.
The leg takes **(b) as its primary** and reports **(a) as a secondary
observation**, because (b) is the shape the design already wrote and (a) has no
declared office registry to resolve against.

**And resolution 1 has a trap that this design names before anyone builds it.**
`RGL-02`'s speaker is an **exclusion**:

```
speaker: "stamp-holder only — no master, no delegate"
```

The tokens `master` and `delegate` name offices that are **forbidden**, and both
are substrings of permitted offices:

```
'master'   in 'furnace-master'  → True
'delegate' in 'league delegate' → True
```

A **substring matcher grants exactly the offices the row forbids**:

| row | exact-token matcher | substring matcher |
|---|---|---|
| `RGL-01` | `['furnace-master', 'stamp-holder']` | `['furnace-master', 'stamp-holder']` |
| `RGL-02` | `['stamp-holder']` | `['furnace-master', 'league delegate', 'stamp-holder']` |
| `RGL-03` | `['broker', 'market-goer']` | `['broker', 'market-goer']` |

**The leg therefore resolves by exact token, never by substring**, and
`RGL-02`'s `only`/`no` polarity is carried as the row's `kind: exclusion` rather
than inferred from the field text. This is `D4L-LAW-SPEAKER`'s calibration
clause and it is recorded as a limit (`LD-6`).

## 2. The `D4L-LAW-*` finding classes

Six classes. Each names its resolution, its ground truth, and — the column that
keeps a class from being a place to park an opinion — **the control that proves
it can fire**.

| class | resolution | fires when | control that fires it |
|---|---|---|---|
| `D4L-LAW-SPEAKER` | 1 | an agent id in `speaker`/`holder` resolves to no delivered record | C-3: `(OR-02)` → `(ZZ-99)` |
| `D4L-LAW-FORCE` | 2 | a `force` value names no declared illocutionary class and is not the literal `none` | C-1: `commissive-binding refused` → `no-such-force` |
| `D4L-LAW-CONSEQUENCE` | 3 | a `consequence` names no delivered roll/rank machinery | **none — see §3.4** |
| `D4L-LAW-REGISTER` | 4 | a `register` names no register the `registers` block declares | C-5: `stamp` → `no-such-register` |
| `D4L-LAW-AXIS` | 5 | an `axis` is outside the spine's vocabulary | (structural; not exercised — `mark`/`fire` are both declared) |
| `D4L-LAW-DANGLING` | structural | a `design_row` names an id the `registers` block does not carry | **none — see §3.4** |
| `D4L-LAW-ROW` | structural | one of the declared law rows `RGL-01..05` is absent | C-2: the `RGL-05` record removed |

**Two classes have no firing control, and this design says so rather than
inventing one.** `D4L-LAW-CONSEQUENCE` and `D4L-LAW-DANGLING` **already fire on
the clean packet** (§3.1), so a further tamper in those classes cannot raise the
count — a control can only add a finding to a class that is not already
saturated. The control battery for those two classes is therefore the **clean
run itself**: the delivered bytes are their positive control, and §3.4 states
the consequence.

**Severity.** Every class is a **hold**, not a fail, and the reason is the same
for all six: the law is a NON-CANON design statement, and a malformed law row is
an open design question, not a contradiction in the delivered packet. This
mirrors the freeze rule the lane already applies (`SKILL.md:151`: "the
**emitted** vocabulary governs the expectation file"). A later round that wants
a fail severity must name the leg that upgrades it.

## 3. Calibration against the delivered bytes

Every number below is measured on `examples/culture-d4/packet.d4.yml`
`543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f`
(98,841 bytes), read at 20:15Z on 2026-10-18.

The reference implementation is `.scratch/r28-law/replay-probe.py` (read-only;
one finding per `(class, row, token)` — the granularity the round-28 runner's own
independent reader uses). Command:

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/r28-law/replay-probe.py
```

### 3.1 The leg on the clean packet — 6 findings, and they are real

```
findings_total 6
by_class {'D4L-LAW-DANGLING': 4, 'D4L-LAW-CONSEQUENCE': 2}
context {'record_ids': 179, 'law_rows': 5, 'registers': ['QREG-01','QREG-02','QREG-03','QREG-04']}
```

| class | row | token | reading |
|---|---|---|---|
| `D4L-LAW-DANGLING` | `RGL-01` | `QREG-05` | the design row the law claims to implement **is not a packet record** |
| `D4L-LAW-DANGLING` | `RGL-01` | `QREG-07` | same |
| `D4L-LAW-DANGLING` | `RGL-02` | `QREG-06` | same |
| `D4L-LAW-DANGLING` | `RGL-03` | `QREG-08` | same |
| `D4L-LAW-CONSEQUENCE` | `RGL-04` | (text) | a sound-channel constraint carries no roll/rank machinery |
| `D4L-LAW-CONSEQUENCE` | `RGL-05` | (text) | a dating constraint carries no roll/rank machinery |

**The four `DANGLING` findings are the important ones, and they are a real defect
in the delivered tree.** `reports/round-27/law/rules.md` §2 specified four new
`registers` rows (`QREG-05..08`) carrying `speech_act`, `speaker`, `force`,
`consequence`, `era_rule`. The landing took **Route A'** instead: the law rows
went into a new `register_law` block as `RGL-01..05`, and the four `QREG-05..08`
act rows were **never landed as records**:

```
registers block ids: ['QREG-01', 'QREG-02', 'QREG-03', 'QREG-04']
RGL-01: design_row=['QREG-05','QREG-07']  DANGLING=['QREG-05','QREG-07']
RGL-02: design_row=['QREG-06']            DANGLING=['QREG-06']
RGL-03: design_row=['QREG-08']            DANGLING=['QREG-08']
```

So every law row points at a design row that does not exist, and the
`design_row` field — whose whole purpose is "so a reader can check the law
against the design rather than reconcile two vocabularies"
(`examples/culture-d4/components/13-register-law.yml`) — **resolves to nothing**.
This is the same class as round 26's `RD-1` (cited where-keys that do not exist
in the delivered tree) and round 27's `RL-4`, one level in.

**The two `CONSEQUENCE` findings are a class-fit question, not a defect.**
`RGL-04` and `RGL-05` are the two rows the round-27 design itself marks as *not
speech acts* — "none — a sound-channel constraint" and "none — a dating
constraint". Their `consequence` text therefore names no roll, because their
consequence is *sound-channel* and *dating*, not record. **The leg is right to
flag them and the flag is a design question**: either those two rows belong in a
different block (they are not speech acts), or the leg's consequence resolution
must be scoped to `kind: admissibility|exclusion|asymmetry`. This design reports
it and does not decide it — deciding it changes the packet, and §4 prices that.

### 3.2 The speaker resolution, both readings, measured

```
RGL-01: speaker='stamp-holder, furnace-master (RK-03), mold-keeper (OR-02, component-only)'
RGL-02: speaker='stamp-holder only — no master, no delegate'
RGL-03: speaker='broker, market-goer (RK-04), at market days'
RGL-04: speaker='any speaker admitted by RGL-01 or RGL-03'
RGL-05: speaker='any speaker admitted by RGL-01 or RGL-03'
```

Under the leg's primary reading (the `(ID)` shape):

| row | agent ids | resolve? |
|---|---|---|
| `RGL-01` | `RK-03`, `OR-02` | both ✓ — and `OR-02` resolves **only because the RL-4 fix landed** (§`rl4-delta.md`) |
| `RGL-02` | none | the row carries no id; its named offices are the forbidden ones |
| `RGL-03` | `RK-04` | ✓ |
| `RGL-04`, `RGL-05` | none | they delegate by row reference (`RGL-01 or RGL-03`), which the leg does not follow |

**The `mold-keeper` finding from round 27 is now closed, and closed by the RL-4
fix, not by a law edit.** Round 27 measured `mold-keeper` as an office absent
from the packet:

```
'reports/round-27/law/design.md' §3: "QREG-07's speaker: mold-keeper names an
office that no packet record carries"
```

Measured now, after the fix:

```
offices (rank_rules.wearer_ranks + costumes.wearer_ranks):
  ['broker','charcoal burner','furnace-master','kiln tender','league delegate','market-goer','smith','stamp-holder']
mold-keeper in offices? False
mold-keeper in literacy_institutions (substring)? True — "the mold-keeper's license"
mold-keeper (OR-02) resolves as a RECORD ID? True
```

So `mold-keeper` is **still not an office** — but `OR-02`, the id the row
carries, **is** a delivered record. The law's citation was correct in shape and
the packet was wrong; the packet has been fixed. That is the whole of the
`RL-4` story, and it is why `rl4-delta.md` exists as a separate file.

### 3.3 A wrong ground truth, measured — and a second reader that takes it

The round-28 lane runner carries its **own** independent law reader
(`reports/round-28/run-validation.py` `law_check`, `53e9b4d1…`). Measured on the
same clean bytes, the two readers disagree completely:

```
$ python3 -c "import runpy; m=runpy.run_path('reports/round-28/run-validation.py');
              print(m['law_check'](m['load_packet']('examples/culture-d4/packet.d4.yml'))[0])"
[]                        # the runner's reader: ZERO findings
findings_total 6          # this seat's leg: SIX findings
```

The disagreement is **two wrong ground truths**, and both are measured:

**(a) the runner resolves `register` against register *ids*, not names.**

```python
register_ids(packet) -> {'QREG-01','QREG-02','QREG-03','QREG-04'}
# then: if register and registers and register not in registers
#       and not any(register in str(other) for other in registers):
```

The law row says `register: "stamp"`; the block's ids are `QREG-01..04`; the
block's *names* are `plain`, `stamp`. The runner's predicate therefore fires on
**every** row (`stamp` is in no id), and its own `not any(register in str(other))`
escape clause then suppresses all of them — so the class exists in the runner's
code and can never fire. Measured directly:

```
runner's law_check on the clean packet: findings=7, of which
  D4L-LAW-REGISTER ×5   (RGL-01..05, value 'stamp')   ← then suppressed
```

**(b) the runner resolves `speaker` only by `(ID)` parenthetical.**

Its `AGENT_ID_RE = \(\s*([A-Z]{2,4}-\d{2,3})\b` finds `RK-03` and `OR-02` in
`RGL-01` and checks both against the record set — and **both resolve**, because
the RL-4 fix landed `OR-02`. So the runner's speaker resolution is green *by
construction on these bytes*, and it never sees the office-name reading at all.
It also never checks `design_row`, so the four dangling rows are invisible to it.

**The consequence is a control-flow fact worth stating plainly.** The runner's
`measure_law_replay` fails the round if its own reader reports any finding
(`if own_findings: failures.append(...)`). **At the start of this seat's window
its reader reported `[]` on these bytes** — the two wrong ground truths above
made it blind. **A sibling seat amended the runner inside the window**
(`run-validation.py` `53e9b4d1…` → `0a215dc4…` → `7ed294c1…`), and after the
amendment the runner's own reader reports **4 findings, all
`D4L-LAW-DANGLING`** — the same four tokens this seat's leg reports:

```
$ python3 -c "import runpy;m=runpy.run_path('reports/round-28/run-validation.py');
              print(m['law_check'](m['load_packet']('examples/culture-d4/packet.d4.yml'))[0])"
[{'class': 'D4L-LAW-DANGLING', 'row': 'RGL-01', 'token': 'QREG-05', ...}, … ×4]
```

So the two readers now **converge on the dangle** and differ only on
`D4L-LAW-CONSEQUENCE` (this seat 2, runner 0): the amendment scoped the
consequence resolution to *binding* acts, so `RGL-04`/`RGL-05` — which declare
`force: none` and are a sound-channel and a dating constraint — are no longer
resolved as record consequences. **That is the class-fit question §3.1 raised,
answered by a sibling in the cheaper direction** (no packet change). Both numbers
are correct; they answer different questions.

**And the producer check has two roots, and the leg has since landed.** The
round's `measure_law_replay` §3 fails the round if no tool names a `D4L-LAW-*`
id, and `law_finding_producers()` walks **both** `tools/` and `reports/round-28/`.
At 20:20Z a sibling seat landed the leg itself:

```
$ ls -la tools/gates/register-law-gate.py
-rw-r--r-- … 26699 bytes  2026-10-18 17:20  sha256 16843de66dc11ef6…
$ python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
FINDING D4L-LAW-DANGLING: HOLD — RGL-01 design_row names QREG-05, which no delivered record carries: …
FINDING D4L-LAW-DANGLING: HOLD — RGL-01 design_row names QREG-07, …
FINDING D4L-LAW-DANGLING: HOLD — RGL-02 design_row names QREG-06, …
FINDING D4L-LAW-DANGLING: HOLD — RGL-03 design_row names QREG-08, …
coverage: … law_rows=5 identity_rows=4 record_ids=179 registers=9 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=4 findings=4
exit=1
```

**The landed gate is this design, byte for byte in behaviour** — the same eight
classes, the same four resolutions, the same clean baseline of 4 (it scopes
`CONSEQUENCE` to binding acts, as this seat's §3.1 predicted a leg would have
to), and its controls fire identically (measured: `+FORCE`, `+SPEAKER`,
`+REGISTER`, `+ROW`; `designrow`/`consequence` inert). Before the landing:

```
$ grep -rl "D4L-LAW" tools/          # 0 — no delivered gate names the class
$ python3 -c "import runpy;m=runpy.run_path('reports/round-28/run-validation.py');
              print(m['law_finding_producers']())"
['reports/round-28/gate-tests/run-gate-tests.py',
 'reports/round-28/scribe/x54-law-negatives-spotcheck.py']   # the runner excludes itself
```

So the class is named by **two round instruments**, neither a delivered gate, and the runner's own failure text says exactly that: *"a tool names the
`D4L-LAW-*` class but no run of it emitted a finding: the leg is declared and
never fires."* That is `RL-1` closed **in design and instrumentation** and still
open **as delivered bytes** — recorded in `review.md` §2 and §5.

### 3.4 The control battery, with the two inert controls named

Controls are single-token textual rewrites of the delivered bytes (never a
re-serialization), run through the reference leg. Restores are verified with
`cmp`.

| # | control | change | findings | Δ | reading |
|---|---|---|---|---|---|
| C-0 | clean | — | 6 | — | the delivered baseline |
| C-1 | `force` | `commissive-binding refused` → `no-such-force` | 7 | **+1** `D4L-LAW-FORCE` | **fires** |
| C-2 | row drop | the `RGL-05` record removed | 6 | **+1** `D4L-LAW-ROW`, −1 `D4L-LAW-CONSEQUENCE` | **fires** |
| C-3 | `speaker` | `(OR-02)` → `(ZZ-99)` | 7 | **+1** `D4L-LAW-SPEAKER` | **fires** |
| C-4 | `design_row` | `QREG-06` → `QREG-99` | 6 | **0** | **inert — class saturated** |
| C-5 | `register` | `stamp` → `no-such-register` | 7 | **+1** `D4L-LAW-REGISTER` | **fires** |
| C-6 | `consequence` | the `RGL-01` consequence text replaced | 6 | **0** | **inert — class saturated** |

**Why C-4 and C-6 are inert, and why that is the honest reading.** Both classes
already fire on the clean packet (§3.1): there are four `DANGLING` findings and
two `CONSEQUENCE` findings before any tamper. A control in a saturated class
cannot raise the count, because the finding it would add is a
`(class, row, token)` triple that is already present — C-4 rewrites `RGL-02`'s
`design_row` from one dangling id to another dangling id, and C-6 replaces one
non-machinery consequence with another. **A leg that reported 0 on the clean
packet would have shown both controls as +1.** The saturation is the defect
showing through the control harness, and it is reported as such rather than
papered over by weakening the clean baseline.

### 3.5 What the leg does *not* see, measured

| not resolved | measured | consequence |
|---|---|---|
| the delegation `RGL-04`/`RGL-05` → `"any speaker admitted by RGL-01 or RGL-03"` | the leg reads no cross-row reference | a broken delegation is invisible (`LD-1`) |
| `kind` (`admissibility`/`exclusion`/`no-segment`/`era`/`asymmetry`) | `grep -c` on the packet finds no vocabulary check anywhere | deleting `kind` changes nothing: C-7 measured **0** (round-27's C-2b reproduced) |
| the `act` text | free prose, no resolution | an act row that describes nothing is invisible (`LD-3`) |
| the `holder` field's `none —` polarity | the leg reads ids only | `RGL-02`'s `holder: "none — the register admits no binding oath"` is not checked as a negation (`LD-6`) |

## 4. The alternative, priced: a projector amendment

Round 27 priced Route B (the forecast's Δ6 shape) at seven items E-1..E-7 and
declined it. This design does not re-open it, but records **why the standalone
leg is the cheaper road**, on the same evidence:

| # | route | site | new holds | new finding ids |
|---|---|---|---|---|
| A | the law in `registers`/`register_law`, **no leg** (delivered today) | — | 0 | 0 — and a tamper is invisible (C-1/C-2/C-3 measured, §3.4) |
| **B** | the standalone checking leg (this design) | a new tool or a new leg in the typed gate | **0** — it reads the packet, it does not add rows | 6 `D4L-LAW-*` |
| C | the forecast's Δ6: `property.kind: register` in `rank_rules` | `tools/d2-typed-labels.py` | **+4** (one per row) | reuses `D2L-RANK` |

Route B costs **zero** new holds and **zero** projector bytes. It is the only
route that gives the law teeth without touching the family projector, and it is
the route this design takes. Route C's price is round 27's `design.md` §5 E-1..E-7
and is not re-measured here.

**The leg's own cost, priced.** A leg that ships as a new tool costs: one new
file under `tools/`, one battery registration row, one fixture pair (positive +
negative control), and — the item round 27's E-6/E-7 named — **no re-pin of
`tools/d2-typed-labels.py`**, because the leg does not touch it. That is the
whole reason the standalone road is cheaper, and it is why `rl4-delta.md`'s
pin cascade (§4 of that file) is the round's only pin-moving change.

## 5. Named limits (declared, not silently skipped)

| id | limit | measured |
|---|---|---|
| **LD-1** | the leg does not follow cross-row delegation (`"admitted by RGL-01 or RGL-03"`) | §3.5 |
| **LD-2** | the leg resolves `speaker` by record id, not by office name: a row naming an office that is not an id is invisible | §3.2 — `mold-keeper` is still not an office |
| **LD-3** | the `act` text is free prose and is not resolved | §3.5 |
| **LD-4** | the `consequence` resolution is a **stem** match, so a consequence that says "roll" while meaning nothing passes | §1 resolution 3 |
| **LD-5** | `D4L-LAW-CONSEQUENCE` and `D4L-LAW-DANGLING` are **saturated on the clean packet**, so their controls are inert | §3.4, C-4/C-6 |
| **LD-6** | the leg resolves by **exact token**, never substring: a substring matcher inverts `RGL-02`'s exclusion | §1, measured |
| **LD-7** | `kind` is unconstrained: a row's clause classifier can be deleted or changed with no finding | §3.5, C-7 = 0 |
| **LD-8** | every class is a **hold**, never a fail: the law is NON-CANON design and a malformed row is an open question | §2 severity |
| **LD-9** | the leg **landed** at 20:20Z as `tools/gates/register-law-gate.py` (`16843de6…` → `cfbff16b…`), reproducing this design's classes, resolutions and controls; it is **not yet registered** in the battery or the typed gate, so it fires only when invoked directly | §3.3 |

## 6. Owners

| artifact | owner | what they owe |
|---|---|---|
| the `D4L-LAW-*` leg as executable bytes | **the D/O seats of a later build round** | a new tool or a typed-gate leg; the reference implementation is `.scratch/r28-law/replay-probe.py` (gitignored) |
| the four `design_row` dangles | **`13-register-law.yml`'s owner** | either land `QREG-05..08` as `registers` records, or drop the `design_row` field and cite the design in `cite` (which already resolves — §3.6) |
| the two `CONSEQUENCE` class-fit findings | **`13-register-law.yml`'s owner** | move `RGL-04`/`RGL-05` out of a speech-act block, or scope the leg's consequence resolution by `kind` |
| the runner's own reader's two wrong ground truths | **`reports/round-28/run-validation.py`'s owner** | resolve `register` against names and `speaker` by both readings, or the runner's green is a green over a blind reader |
| the `cite:` resolution surface | **no owner needed** — measured green | §3.6 |

### 3.6 The `cite:` surface, measured green

Every path cited in a law row's `cite` field resolves on disk (13 of 13):

```
RGL-01: reports/round-26/register/forms.md exists=True
RGL-01: reports/round-27/law/design.md exists=True
RGL-02: reports/round-26/register/forms.md exists=True
RGL-02: reports/round-27/law/design.md exists=True
RGL-02: reports/round-17/d4/design-brief.md exists=True
RGL-03: reports/round-26/register/forms.md exists=True
RGL-03: reports/round-27/law/design.md exists=True
RGL-04: reports/round-26/register/forms.md exists=True
RGL-04: reports/round-26/register/design.md exists=True
RGL-05: reports/round-26/register/forms.md exists=True
RGL-05: examples/culture-d4/components/03-orthography.yml exists=True
```

So the law's **prose** citations are all resolvable while its **structured**
`design_row` citations are all dangling. That asymmetry is the finding: the law
is documented against the design and not linked to it.

## 7. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
sha256sum examples/culture-d4/packet.d4.yml
python3 .scratch/r28-law/replay-probe.py                       # clean: 6 findings
python3 .scratch/r28-law/replay-probe.py .scratch/r28-law/tamper-force.yml       # +1 FORCE
python3 .scratch/r28-law/replay-probe.py .scratch/r28-law/tamper-speaker.yml     # +1 SPEAKER
python3 .scratch/r28-law/replay-probe.py .scratch/r28-law/tamper-register.yml    # +1 REGISTER
python3 .scratch/r28-law/replay-probe.py .scratch/r28-law/drop-rgl05.yml         # +1 ROW
python3 .scratch/r28-law/replay-probe.py .scratch/r28-law/tamper-designrow.yml   # 0 (saturated)
python3 .scratch/r28-law/replay-probe.py .scratch/r28-law/tamper-consequence.yml # 0 (saturated)
python3 -c "import runpy;m=runpy.run_path('reports/round-28/run-validation.py');\
print(len(m['law_check'](m['load_packet']('examples/culture-d4/packet.d4.yml'))[0]))"  # 0 — the runner's reader
grep -rl "D4L-LAW" tools/ | wc -l                              # 0 under tools/
python3 -c "import runpy;m=runpy.run_path('reports/round-28/run-validation.py');print(m['law_finding_producers']())"  # 3 round instruments
```

### Artifact digests at measurement (`sha256sum`, 20:15Z 2026-10-18)

| artifact | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` | `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f` |
| `examples/culture-d4/typed-labels.d4.yml` | `339bfd83bf66832479b5b8ffbbce708c8be15e13b08967fa7049b848661a3cf8` |
| `examples/culture-d4/packet.d4.typed.yml` | `15c81ec11b42efaa7d683dd9320bfc7cd9b5d1e812e042d99dbf8d8726ec5da6` |
| `examples/culture-d4/expected-holds.json` | `857417e949fb5cb9b265918b8982ca86e47a820d136ba7b009414d84aa4ec28f` |
| `examples/culture-d4/components/13-register-law.yml` | `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7` |
| `tools/gates/typed-pipelines.json` | `69f250df363d70a2001840ab37f4f947e28244b4ac053a5a79d4a92860822f7a` |
| `tools/d2-typed-labels.py` | `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` |
| `reports/round-28/run-validation.py` | a **moving byte** inside this window: `53e9b4d1…` → `0a215dc4…` → `7ed294c1…` → `0fa5e0ca…` (sibling amendments; measure the live digest before quoting one) |
| `tools/gates/register-law-gate.py` (the landed leg) | a **moving byte**: `16843de6…` → `cfbff16b…` (20:21Z); behaviour unchanged, clean 4 findings |
| `examples/culture-d4/expected-holds.json` | a **moving byte**: `857417e9…` → `65f5a03e…` (the O sweep's re-pin) |
| `.scratch/r28-law/replay-probe.py` (reference leg, gitignored) | see `.scratch/r28-law/replay-probe.json` |

## 8. The green at this stamp, measured

```
$ python3 tools/check-gate-battery.py
summary: {battery_exit: 0, fail: 0, pass: 7, unevaluable: 0}
$ python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: … records=183 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
$ python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml
findings_total=12
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
ok   L3b-argot
FAIL L1-profile: packet: pins 86079a6708a0, live 543d68a82640 (examples/culture-d4/packet.d4.yml);
                 projection: pins 88a94422b412, live 339bfd83bf66 (examples/culture-d4/typed-labels.d4.yml)
```

**The one red is the pin cascade, and it is the O claim's, not this seat's.**
`tools/gates/typed-pipelines.json` and `examples/culture-d4/expected-holds.json`
still carry the pre-fix `86079a67…`/`88a94422b412…` pins; the live bytes are
`543d68a8…`/`339bfd83…`. Re-pinning is a **new row** in each file and belongs to
the O sweep. Recorded here because a reader of this file will run the gate and
see it.

**And the landed leg is not yet wired in**, measured: `grep -rn
"register-law-gate" tools/check-gate-battery.py tools/gates/typed-pipeline-gate.py
tools/gates/typed-pipelines.json` → **no hits**. So the law now has teeth and
nothing runs them on the standing battery: `python3 tools/gates/register-law-gate.py`
must be invoked by hand. That is the round's remaining wiring debt, and it is one
registration row plus one battery leg — the item this seat's §4 priced.
