# R28-D17 — adversarial review 1 of 4: a law row bypassing the replay leg

- **Seat:** R28-D17 (reviewer 1 of 4), round 28, loop 3 build 4 of 4 (the last
  build round), claim **D** `register-law-replay` (`reports/round-28/claims.json`).
- **Date:** 2026-10-18. Declared baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`
  (round-27 admit); lane HEAD at every measurement `69cecbc7dcf575a29f29660ecac470e05260fd86`
  (`git log --oneline -1`). Measurement window **2026-10-18T20:11Z–20:16Z**
  (`date -u +%FT%TZ`).
- **Review target:** the round-28 register-law **replay leg** — whatever the
  delivered tree carries that emits a `D4L-LAW-*` finding — measured against the
  law the round-27 component declares (`examples/culture-d4/components/13-register-law.yml`,
  `RGL-01..RGL-05`) and against the round-28 runner's own law reader
  (`reports/round-28/run-validation.py`, `law_check`).
- **Write scope:** this file only, plus gitignored scratch under
  `.scratch/r28-d17/`. `export TMPDIR=$PWD/.scratch` preceded every
  scratch-writing command. **No component, packet, tool, gate, fixture, pin,
  runner or filed rounds 8–27 byte was written; no commit, no push.**
- **Canon:** NON-CANON engineering evidence. Findings are review evidence, never
  canon rulings.

**Assignment.** Reviewer 1 of 4, adversarial: *a law row bypassing the replay
leg?* Round 27's `RL-1` named the defect — a tampered law row is invisible to
every delivered gate. Round 28's claim D promises "the law gains a
replay/checking leg … a tampered row is a named finding (`D4L-LAW-*` class)".
This file asks the only question that matters about a negative claim: **can a row
violating the law still pass?**

**Verdict in one line.** **The artifact landed, and the teeth are partial.**
At the start of this review the tree named no `D4L-LAW-*` id under `tools/` and
the only law reader was the round-28 runner's own; by the end,
**`tools/gates/register-law-gate.py` had landed** (`cfbff16b…`, selftest 33/33,
in the claim's named place — `D17-F8` **closed**). It resolves speaker, force,
consequence, register, axis, kind, `design_row` and row-presence, and it catches
the structural mutations. But **five law violations still pass it silently**,
re-measured against the delivered gate in §4.4: a force **inverted to its
opposite** (`commissive-binding granted` for `commissive-binding refused`), a
force **negated** (`not-directive-binding`), a **blanked** consequence, a **bare
bogus office name**, and a consequence asserting the **absence** of the record
it must name. Each changes the law's meaning while keeping its field syntax, and
each leaves the gate's finding count at its own clean reading. The gate is a
field-shape check with real coverage; it is not yet a law check.

## 0. What is actually delivered, measured — three readings

The claim's `after_required` names a class (`D4L-LAW-*`) and a place (the
delivered tree). Both are measurable:

```
$ date -u +%FT%TZ
2026-10-18T20:16:07Z
$ grep -rl "D4L-LAW" tools/ ; echo "exit=$?"
exit=1
```

**No tool under `tools/` named the class at 20:16:07Z.** The four places the
string occurred in the tree were all round-28 reporting artifacts, not gates:

```
$ grep -rl "D4L-LAW" tools/ reports/round-28/        # at 20:16:07Z
reports/round-28/claims.json
reports/round-28/scribe/x54-law-negatives-spotcheck.py
reports/round-28/audit/x59-register-law-negatives.py
reports/round-28/run-validation.py
```

The runner's own guard was explicit that this is a failure, not a nuance:

```
$ sed -n '714,717p' reports/round-28/run-validation.py      # at 20:16:07Z
    if not producer_files:
        failures.append("no tool under tools/ names a `D4L-LAW-*` finding id: the law has no "
                        "replay leg (round-27 RL-1)")
```

### 0.0 The delivered gate landed at 20:20:40Z — D17-F8 is closed

**`tools/gates/register-law-gate.py` landed while this review was being
written**, four minutes after the §0 reading above. It is the claim's named
artifact, in the claim's named place, and it closes `D17-F8`:

```
$ date -u +%FT%TZ
2026-10-18T20:20:40Z
$ sha256sum tools/gates/register-law-gate.py
cfbff16bbb67d94d39b8d19f7f3fa14d985d18d1f306c8b8e39f79d20ad00e5e  tools/gates/register-law-gate.py
$ python3 tools/gates/register-law-gate.py --selftest | tail -1
selftest: 33/33 checks passed
$ python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml; echo "exit=$?"
FINDING D4L-LAW-DANGLING: HOLD — RGL-01 design_row names QREG-05, which no delivered record carries…
FINDING D4L-LAW-DANGLING: HOLD — RGL-01 design_row names QREG-07, which no delivered record carries…
FINDING D4L-LAW-DANGLING: HOLD — RGL-02 design_row names QREG-06, which no delivered record carries…
FINDING D4L-LAW-DANGLING: HOLD — RGL-03 design_row names QREG-08, which no delivered record carries…
coverage: … law_rows=5 identity_rows=4 record_ids=179 registers=9 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=4 findings=4
exit=1
```

**The gate is real, it is in the right place, its selftest is 33/33, and it
emits the claim's named class.** That is a material improvement over the state
at §0 and it is credited in §4.4, where the bypasses are re-measured against
*this* gate rather than the runner. Its own docstring declares its limits
honestly — the closed vocabulary, the stem-resolved consequence, the
`Name (ID)`-only speaker shape, and the four `DANGLING` holds on the clean
packet. It does **not** declare the force over-match, which §4.4 measures and
which reproduces here as it did in the runner.

### 0.1 The runner is a moving target inside the measurement window

The runner was edited **six** times while this review ran. Six digests, minutes
apart, all with the same declared baseline:

| stamp (`date -u`) | `reports/round-28/run-validation.py` sha256 (first 16) | `law_check` on the clean packet |
|---|---|---|
| 20:15:09Z | `b71721aa6edd7d6e` | **7 findings** (two false-red classes) |
| 20:15:56Z | `53e9b4d1537ed48d` | 0 findings |
| 20:16:07Z | `a130f36877494060` | 0 findings |
| 20:18:17Z | `6f8db1d21c2a496f` | **4 findings** (`D4L-LAW-DANGLING`) |
| 20:18:19Z | `c398bdc485eeee74` | 4 findings (`D4L-LAW-DANGLING`) |
| 20:18:35Z | `7ed294c19939c59e` | 4 findings (`D4L-LAW-DANGLING`) |

Two things changed materially across those revisions, and both matter for
grading the claim:

1. **The clean-packet findings stopped being a verdict.** From `c398bdc4…` the
   runner states: *"A finding here is a measurement, not a verdict: the
   delivered law is a NON-CANON design statement, and the D seat's own design
   measures honest findings on the clean bytes (dangling `design_row` ids,
   non-act consequences). The runner records its reading and the delivered leg's,
   and grades on the tamper **delta**."* The four `D4L-LAW-DANGLING` findings are
   the `design_row` ids `QREG-05..08`, which were **never landed as records** —
   the law landed as the separate `register_law` block `RGL-01..05` while
   `registers` still carries only `QREG-01..04` — so the dangling reference is a
   real property of the delivered bytes and the runner now measures it rather
   than failing on it.
2. **The declared-row leg was added.** From `7ed294c1…` a dropped row is caught
   (`LAW_DECLARED_ROWS = ("RGL-01", …, "RGL-05")`), closing one of the bypasses
   this seat measured at 20:16Z (§4.2 B3).

**Consequence for this file's findings.** Two of the seven bypasses I measured
at `a130f368…` are **closed** on `7ed294c1…`: row deletion (B3) now emits
`D4L-LAW-ROW`, and the `design_row` field is graded at all. The remaining five
(B1, B2, B4, B5, B6/B7) reproduce unchanged on the current revision — measured
in §4.3, which is the revision-pinned table. **The churn itself is the finding
`D17-F9`**: six revisions of the artifact that grades claim D, inside the
window, with no changelog and no filed reading. A claim whose instrument moves
six times while it is being reviewed cannot be replayed by a third party, which
is the standard `RL-1` set.

## 1. The law as landed — the surface the leg must check

Five rows, six fields each (`13-register-law.yml`, sha256
`c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7`), delivered
into the packet's `register_law:` block (`examples/culture-d4/packet.d4.yml`,
sha256 `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f`):

| row | kind | force (verbatim) | speaker (verbatim) | consequence (verbatim, head) |
|---|---|---|---|---|
| `RGL-01` | admissibility | `directive-binding for the charge; declarative-naming for the lot's name` | `stamp-holder, furnace-master (RK-03), mold-keeper (OR-02, component-only)` | `the spoken form binds and the stamp-holder enters the act on the stamp-roll…` |
| `RGL-02` | exclusion | `commissive-binding refused` | `stamp-holder only — no master, no delegate` | `an oath spoken in stamp is void; the binding oath is plain speech…` |
| `RGL-03` | asymmetry | `directive-binding, not-rollable` | `broker, market-goer (RK-04), at market days` | `the act binds the goods at the gate and is entered on the stamp-roll…` |
| `RGL-04` | no-segment | `none — a sound-channel constraint, not a speech act` | `any speaker admitted by RGL-01 or RGL-03` | `the register owns no segment…` |
| `RGL-05` | era | `none — a dating constraint, not a speech act` | `any speaker admitted by RGL-01 or RGL-03` | `every stamp form is available_from E1…` |

**Every field is free prose.** That is the whole adversarial problem: a leg that
checks these fields must decide what a *value* is, and the delivered values do
not have a machine shape. The three that matter:

1. `force` is prose in five different shapes — one compound (two forces joined by
   `;`), one negated, one qualified, two a bare `none` with a dash-clause.
2. `speaker` is prose that **embeds citations inside the value**:
   `furnace-master (RK-03)`, `mold-keeper (OR-02, component-only)`,
   `broker, market-goer (RK-04), at market days`.
3. `consequence` is prose whose *polarity* varies: `RGL-02`'s consequence
   asserts a **void** (`an oath spoken in stamp is void`), while `RGL-05`'s
   asserts a **date**. Both are correct law; neither is machine-shaped.

A leg that reads these as strings will pass things it should fail and fail
things it should pass. §4 measures both directions.

## 2. The control: the clean packet must be silent

A checker that fires on everything would pass every tamper route, so the first
measurement is the negative control:

```
$ export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
$ python3 - <<'PY'
import runpy
ns = runpy.run_path('reports/round-28/run-validation.py')
p  = ns['load_packet']('examples/culture-d4/packet.d4.yml')
f, ctx = ns['law_check'](p)
print("findings =", len(f), "context =", ctx)
PY
findings = 0 context = {'record_ids': 179, 'registers': ['QREG-01', 'QREG-02', 'QREG-03', 'QREG-04'], 'law_rows': 5, 'identity_rows': 4}
```

**The clean control was silent on `a130f368…` and `53e9b4d1…`.** That is a real
and necessary result, and it is the half of the claim that holds at those
revisions. Two other revisions in the window did **not** have a silent clean
control — the earliest reds with seven false-positive findings (§3) and the
current one returns four correct `D4L-LAW-DANGLING` findings (§0.1). **A control
that reads 0, then 7, then 4 across three revisions of the same artifact is not
a control**; the honest statement is that the clean-packet reading is
revision-dependent and the runner now grades on the tamper delta instead
(§4.2).

## 3. D17-F1 — the clean packet was red, and the reading is not reproducible

At 20:15:09Z, against `b71721aa…`, the same reader on the same packet returned
**seven** findings:

```
D4L-LAW-REGISTER    RGL-01  'stamp'  register names no declared register id
D4L-LAW-REGISTER    RGL-02  'stamp'  register names no declared register id
D4L-LAW-REGISTER    RGL-03  'stamp'  register names no declared register id
D4L-LAW-CONSEQUENCE RGL-04           consequence names no delivered roll/rank machinery
D4L-LAW-REGISTER    RGL-04  'stamp'  register names no declared register id
D4L-LAW-CONSEQUENCE RGL-05           consequence names no delivered roll/rank machinery
D4L-LAW-REGISTER    RGL-05  'stamp'  register names no declared register id
```

Two distinct false-positive classes, both structural:

**F1a — a name compared against an id set.** `register_ids()` returns the
`registers` rows' **ids**; the law rows carry the register's **name**:

```
$ python3 - <<'PY'
import runpy
ns = runpy.run_path('reports/round-28/run-validation.py')
p  = ns['load_packet']('examples/culture-d4/packet.d4.yml')
print("register_ids()      ->", sorted(ns['register_ids'](p)))
print("law rows' register  ->", sorted({r.get('register') for r in p['register_law']}))
print("registers' own names->", sorted({r.get('register') for r in p['registers']}))
PY
register_ids()      -> ['QREG-01', 'QREG-02', 'QREG-03', 'QREG-04']
law rows' register  -> ['stamp']
registers' own names-> ['plain', 'stamp']
```

`'stamp'` is never in `{QREG-01..04}`, so every law row reds on the clean
packet. The set that resolves is the `registers` rows' own `register` **values**,
not their ids. This is a two-line fix but it is exactly the class the claim is
about — a check that cannot distinguish "the register is undeclared" from "I
compared the wrong two columns".

**F1b — a consequence judged by a stem list that excludes the law's own
constraint rows.** `RGL-04`'s consequence is *"the register owns no segment …"*
and `RGL-05`'s is *"every stamp form is available_from E1 …"*. Neither names a
roll, a rank, a tally or a rite, so `LAW_CONSEQUENCE_STEMS` reds both. But
`RGL-04`/`RGL-05` are **constraint** rows whose `force` is explicitly
`none — … not a speech act`; a constraint row's consequence is a *sound-channel*
or *dating* fact, not a record consequence, and the reader knows this in the
`force` branch but not in the `consequence` branch.

Both F1a and F1b are gone on `a130f368…`. **Neither closure is filed.** No
round-28 artifact records the 7-finding reading, its two classes, or the fix;
`reports/round-28/law/` is empty and the runner carries no changelog. A reader
who takes the current runner's 0-finding control at face value cannot tell
whether the reader was ever wrong. That is **D17-F5** and it is the same class
round 27 filed as `RL-1`'s companion: *a defect that leaves no trace cannot be
replayed.*

## 4. The bypasses — measured at `a130f368…`, re-measured at `7ed294c1…`

Seven law violations passed `law_check` (`a130f36877494060`) with **zero**
findings against a clean control of zero. Two of the seven are **closed** on the
current revision; five reproduce. Both readings are given, because the
difference between them is the round's real progress and it should not be
smoothed away.

### 4.1 The seven, as first measured (`a130f368…`, clean control 0)

```
$ export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
$ python3 - <<'PY'      # runner sha256 a130f36877494060…
import runpy, copy
ns = runpy.run_path('reports/round-28/run-validation.py')
base = ns['load_packet']('examples/culture-d4/packet.d4.yml')
def probe(label, mutate):
    p = copy.deepcopy(base); mutate(p)
    f, _ = ns['law_check'](p)
    print(f"{label:54} findings={len(f)} {sorted({x['class'] for x in f})}")
probe("CLEAN control", lambda p: None)
probe("B1 RGL-02 force inverted -> 'commissive-binding granted'", lambda p: p['register_law'][1].__setitem__('force','commissive-binding granted'))
probe("B2 RGL-02 kind -> 'no-such-kind'", lambda p: p['register_law'][1].__setitem__('kind','no-such-kind'))
probe("B3 RGL-02 row deleted", lambda p: p['register_law'].pop(1))
probe("B4 RGL-02 consequence blanked", lambda p: p['register_law'][1].__setitem__('consequence',''))
probe("B5 RGL-02 speaker -> bare 'no-such-office'", lambda p: p['register_law'][1].__setitem__('speaker','no-such-office'))
probe("B6 RGL-02 consequence -> 'no record at all'", lambda p: p['register_law'][1].__setitem__('consequence','no record at all'))
probe("B7 RGL-02 consequence -> 'never written down'", lambda p: p['register_law'][1].__setitem__('consequence','never written down'))
PY
CLEAN control                                          findings=0 []
B1 RGL-02 force inverted -> 'commissive-binding granted' findings=0 []
B2 RGL-02 kind -> 'no-such-kind'                       findings=0 []
B3 RGL-02 row deleted                                  findings=0 []
B4 RGL-02 consequence blanked                          findings=0 []
B5 RGL-02 speaker -> bare 'no-such-office'             findings=0 []
B6 RGL-02 consequence -> 'no record at all'            findings=0 []
B7 RGL-02 consequence -> 'never written down'          findings=0 []
```

### 4.2 Re-measured on the current revision (`7ed294c1…`, clean control 4)

```
$ python3 - <<'PY'      # runner sha256 7ed294c19939c59e8a00925f3453cafd6363b5849fc263959585b4fc1ff6a853
import runpy, copy, hashlib, pathlib
ns = runpy.run_path('reports/round-28/run-validation.py')
print("runner:", hashlib.sha256(pathlib.Path('reports/round-28/run-validation.py').read_bytes()).hexdigest())
base = ns['load_packet']('examples/culture-d4/packet.d4.yml')
def probe(label, mutate):
    p = copy.deepcopy(base); mutate(p)
    f, _ = ns['law_check'](p)
    print(f"{label:56} findings={len(f):2} {sorted({x['class'] for x in f})}")
probe("CLEAN control", lambda p: None)
… (the same eight probes) …
PY
runner: 7ed294c19939c59e8a00925f3453cafd6363b5849fc263959585b4fc1ff6a853
CLEAN control                                            findings= 4 ['D4L-LAW-DANGLING']
force inverted -> 'commissive-binding granted'           findings= 4 ['D4L-LAW-DANGLING']
force -> 'not-directive-binding'                         findings= 4 ['D4L-LAW-DANGLING']
force -> 'assertive-binding'                             findings= 4 ['D4L-LAW-DANGLING']
force -> 'none directive naming'                         findings= 4 ['D4L-LAW-DANGLING']
kind -> 'no-such-kind'                                   findings= 4 ['D4L-LAW-DANGLING']
row RGL-02 deleted                                       findings= 4 ['D4L-LAW-DANGLING', 'D4L-LAW-ROW']   <-- CLOSED
consequence blanked                                      findings= 4 ['D4L-LAW-DANGLING']
speaker -> bare 'no-such-office'                         findings= 4 ['D4L-LAW-DANGLING']
consequence -> 'no record at all'                        findings= 4 ['D4L-LAW-DANGLING']
consequence -> 'never written down'                      findings= 4 ['D4L-LAW-DANGLING']
design_row -> ['QREG-99']                                findings= 4 ['D4L-LAW-DANGLING']               <-- graded, but…
```

**Read the counts, not the totals.** The clean control is 4, so a tamper that
leaves the count at 4 changed nothing the reader can see. Two closures:

- **B3 (row deletion) is closed**: the deleted-row probe rises to 5 and emits
  `D4L-LAW-ROW`, the class added by `LAW_DECLARED_ROWS`.
- **`design_row` is graded at all** (it was not at `a130f368…`), though the
  `['QREG-99']` mutation stays at 4 because the clean packet's four
  `DANGLING` findings are `QREG-05..08` — mutating `RGL-02`'s single token
  `QREG-06` to `QREG-99` swaps one dangling token for another. **The control is
  the count, not the class**: this probe cannot distinguish "graded" from
  "ungraded" and is recorded as a probe-design limit, not a closure.

**The remaining five reproduce unchanged on the current revision:** B1
(force inverted), B2 (`kind` vocabulary unread), B4 (blanked consequence), B5
(bare bogus office), B6/B7 (consequence polarity). Each is a mutation that
changes the law's meaning while keeping its field syntax, and each leaves the
finding count at the clean control's 4.

Against the mutations the reader **does** catch, on the same revision — so the
predicate is not a constant:

```
$ python3 - <<'PY'
probe("force -> 'no directive whatsoever'", lambda p: p['register_law'][1].__setitem__('force','no directive whatsoever'))
probe("axis -> 'bogus'",                    lambda p: p['register_law'][1].__setitem__('axis','bogus'))
probe("register -> 'bogus'",                lambda p: p['register_law'][1].__setitem__('register','bogus'))
PY
force -> 'no directive whatsoever'                       findings= 5 ['D4L-LAW-DANGLING', 'D4L-LAW-FORCE']
axis -> 'bogus'                                          findings= 5 ['D4L-LAW-AXIS', 'D4L-LAW-DANGLING']
register -> 'bogus'                                      findings= 5 ['D4L-LAW-DANGLING', 'D4L-LAW-REGISTER']
```

### 4.3 Why each surviving bypass works — the mechanism, named

**B1 — the force grammar is two independent substring tests.** The reader is:

```
classes   = [name for name in LAW_FORCE_CLASSES if name in force]
modifier_ok = any(m in force for m in LAW_FORCE_MODIFIERS)
... if not ((classes and modifier_ok) or none_only or declared_ok):
```

with

```
LAW_FORCE_CLASSES   = ('assertive', 'directive', 'commissive', 'expressive', 'declarative')
LAW_FORCE_MODIFIERS = ('binding', 'refused', 'not-rollable', 'none', 'attested',
                       'witnessed', 'naming', 'constraint')
```

The predicate is `(any class substring) AND (any modifier substring)`, evaluated
over the *whole value*. So any value containing one class word and one modifier
word passes, **regardless of the relation between them**:

```
$ python3 - <<'PY'
import runpy, re
ns = runpy.run_path('reports/round-28/run-validation.py')
for v in ["commissive-binding granted","assertive-binding","expressive-not-rollable",
          "none directive naming","not-directive-binding"]:
    classes = [n for n in ns['LAW_FORCE_CLASSES'] if n in v]
    mods    = any(m in v for m in ns['LAW_FORCE_MODIFIERS'])
    print(f"  {v!r:32} classes={classes} modifier_ok={mods} -> PASS={bool(classes and mods)}")
PY
  'commissive-binding granted'     classes=['commissive'] modifier_ok=True -> PASS=True
  'assertive-binding'              classes=['assertive'] modifier_ok=True -> PASS=True
  'expressive-not-rollable'        classes=['expressive'] modifier_ok=True -> PASS=True
  'none directive naming'          classes=['directive'] modifier_ok=True -> PASS=True
  'not-directive-binding'          classes=['directive'] modifier_ok=True -> PASS=True
```

`not-directive-binding` **passes**: the negation is invisible because the test is
membership of a substring, not a parse. And `commissive-binding granted` — the
literal inversion of `RGL-02`'s `commissive-binding refused`, a row whose entire
legal content *is* the refusal — passes. The reader cannot see the difference
between "the act is refused" and "the act is granted", which is the one
distinction `RGL-02` exists to make.

**B2 — a `kind` vocabulary is declared but never enforced.** `LAW_KIND_DEFAULT`
lists seven kinds (`admissibility`, `exclusion`, `asymmetry`, `no-segment`,
`era`, `enforcement`, `procedure`) and `law_check` never reads `row['kind']`.
A row whose kind is `no-such-kind` is accepted. The declared vocabulary is
documentation.

**B3 — row count is never asserted.** Deleting `RGL-02` outright — removing the
exclusion row, the only row that forbids anything — produces zero findings. The
leg has no notion of the law's *extent*: it grades rows it finds and never asks
whether a row that should be there is.

**B4 — an empty value is skipped, not flagged.** The consequence branch opens
`if consequence and not any(...)`. An empty string is falsy, so the branch is
skipped. Blanking a law's consequence is therefore **invisible** — while the
runner's own tamper control (`tamper_law_text('consequence')`) writes
`"the act evaporates silently"`, a *non-empty* string, and so never tests the
empty case. The control is real but it does not cover the field's absence.

**B5 — the agent resolver only sees the parenthesised form.** The reader is
`AGENT_ID_RE = re.compile(r"\(\s*([A-Z]{2,4}-\d{2,3})\b")`, applied to `speaker`
and `holder`. It extracts **only** ids inside parentheses. A speaker field that
names an office the packet does not carry, with no parenthesised id, is
invisible:

```
B5 RGL-02 speaker -> bare 'no-such-office'   findings=0
```

This is precisely the `RL-4` class the round claims to fix — an office named but
absent from the packet — and the reader catches it only when the defect is
spelled in the one syntax the regex knows. `mold-keeper (OR-02)` now resolves
(§5), but `mold-keeper` alone would not have been caught even before the fix.

**B6/B7 — the consequence stem list matches stems, not assertions.**
`LAW_CONSEQUENCE_STEMS` contains `record`, `written`, `entry`, `binds`,
`binding`, `void`, `no entry`. A consequence asserting the **absence** of the
record it is supposed to name passes:

```
B6 'no record at all'      findings=0     # contains 'record'
B7 'never written down'    findings=0     # contains 'written'
```

Both sentences say the act leaves no trace — the exact failure `RGL-02` and
`RGL-03` exist to describe — and both are accepted. The polarity of the sentence
is never read.

### 4.4 Re-measured against the DELIVERED gate (`register-law-gate.py`)

The gate landed at 20:20:40Z. Every bypass above was re-run against it, as
line-level text transforms of the delivered bytes in a family-named directory
(`.scratch/r28-d17/culture-d4/`), compared against its own clean reading:

```
$ export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
$ python3 - <<'PY'      # tools/gates/register-law-gate.py cfbff16bbb67d94d39b8d19f7f3fa14d985d18d1f306c8b8e39f79d20ad00e5e
import subprocess, pathlib
src = pathlib.Path('examples/culture-d4/packet.d4.yml').read_text()
D = '.scratch/r28-d17/culture-d4'; GATE = 'tools/gates/register-law-gate.py'
def run(txt, name):
    p = f'{D}/packet.{name}.yml'; pathlib.Path(p).write_text(txt)
    r = subprocess.run(['python3', GATE, p], capture_output=True, text=True)
    lines = [l for l in (r.stdout + r.stderr).splitlines() if 'FINDING' in l]
    return r.returncode, len(lines), sorted({l.split()[1].rstrip(':') for l in lines})
… (routes as in §4.2) …
PY
route                      exit findings  classes
clean                         1        4  ['D4L-LAW-DANGLING']
B1-force-inverted             1        4  ['D4L-LAW-DANGLING']
B1b-force-not                 1        4  ['D4L-LAW-DANGLING']
B2-kind-unknown               1        5  ['D4L-LAW-DANGLING', 'D4L-LAW-KIND']    <-- CAUGHT
B4-consequence-blank          1        4  ['D4L-LAW-DANGLING']
B5-speaker-bare               1        4  ['D4L-LAW-DANGLING']
B6-consequence-polarity       1        4  ['D4L-LAW-DANGLING']
C1-force-unknown              1        5  ['D4L-LAW-DANGLING', 'D4L-LAW-FORCE']   <-- CAUGHT (control)
```

**Read against the clean reading of 4.** A route that leaves the count at 4
changed nothing the gate can see. The results:

| bypass | on the runner (`7ed294c1…`) | on the delivered gate (`cfbff16b…`) |
|---|---|---|
| B1 force inverted to `commissive-binding granted` | bypass | **bypass** |
| B1b force negated `not-directive-binding` | bypass | **bypass** |
| B2 `kind: no-such-kind` | bypass | **caught** (`D4L-LAW-KIND`) |
| B4 consequence blanked | bypass | **bypass** |
| B5 bare bogus office name | bypass | **bypass** |
| B6/B7 consequence polarity | bypass | **bypass** |
| control: `force: no-such-force` | caught | **caught** |

**The delivered gate closes B2** — it grades `kind` against `DECLARED_KINDS`,
which the runner's reader did not. **Five bypasses reproduce on the delivered
gate**, and they are the five that matter: the force over-match (B1/B1b), the
blanked consequence (B4), the bare office name (B5), and the consequence
polarity (B6/B7).

**The gate's force predicate is the runner's, verbatim** — same two substring
tests, same vocabulary, same `none` handling:

```
$ sed -n '262,266p' tools/gates/register-law-gate.py
            classes = [name for name in DECLARED_FORCE_CLASSES if name in force]
            modifier_ok = any(m in force for m in DECLARED_FORCE_MODIFIERS)
            none_only = bool(NON_FORCE_RE.match(force)) and not classes
            binding_act = not none_only
            if not ((classes and modifier_ok) or none_only):
```

so `commissive-binding granted` passes the delivered gate exactly as it passed
the runner — the defect is in the **delivered** artifact now, not only in the
review instrument. One improvement over the runner's version: `NON_FORCE_RE =
r"^\s*none\s*(?:[—–\-:,]|$)"` requires a separator, so `none but wibble` is
correctly **rejected** (`none directive naming` still passes, because the class
word defeats `none_only` and the `AND` branch accepts it).

### 4.5 What the bypasses do and do not establish

They do **not** establish that the leg is worthless: it catches structural
mutations on both revisions, its `speaker` leg resolves the `(ID)` form against
real records, and the delivered gate adds the `kind` leg and the `DANGLING`
class. They **do** establish that the leg is a *field-presence and field-shape*
check, not a *law* check: it can tell that a field is missing or malformed, and
cannot tell that a field has been made to say the opposite of what the law says.
A tamper route that inverts a force, blanks a consequence, or asserts the
absence of a record is outside its reach — and those are the routes an adversary
would actually use, because they change the law's meaning without changing its
syntax.

## 5. What the round did fix — the RL-4 half, verified

The claim's RL-4 half is real and I verified it independently of the runner.
`03-orthography.yml` and `09-costumes.yml` now declare `packet_keys`:

```
$ grep -n "^packet_keys" examples/culture-d4/components/03-orthography.yml examples/culture-d4/components/09-costumes.yml
03-orthography.yml: packet_keys: [orthography, records, literacy_institutions]
09-costumes.yml:    packet_keys: [costumes, materials, cloth_sources, rank_rules, form_slots, enforcement]
```

and the records reach the packet:

```
$ python3 - <<'PY'
import subprocess, json
d = json.loads(subprocess.run(["ruby","-ryaml","-rjson","-e",
    "puts JSON.generate(YAML.load_file(ARGV[0]))",
    'examples/culture-d4/packet.d4.yml'], capture_output=True, text=True).stdout)
for k in ('records','literacy_institutions','enforcement'):
    print(k, "->", [r['id'] for r in d.get(k) or []] or "ABSENT")
PY
records              -> ['OR-01', 'OR-02', 'OR-03']
literacy_institutions-> ['LI-01', 'LI-02', 'LI-03']
enforcement          -> ['EN-01', 'EN-02']
```

Cross-checked by the runner's own ground truth over the round-27 and round-28
bytes (`git show 6c0ac44:examples/culture-d4/packet.d4.yml`):

```
round-27 (6c0ac44): record_ids=171  OR-02 present=False  LI-02=False  EN-01=False
round-28 (live)   : record_ids=179  OR-02 present=True   LI-02=True   EN-01=True
runner law_check findings: round-27=1 (D4L-LAW-SPEAKER)  round-28=0
```

**RL-4 is closed and the reader's own speaker leg is what closes it.** The one
finding the round-27 bytes produce (`mold-keeper (OR-02)` unresolvable) is gone
on the round-28 bytes. This is a genuine depth improvement and it is the part of
claim D that a reviewer can confirm without qualification.

## 6. Named findings

| id | finding | severity | evidence | disposition |
|---|---|---|---|---|
| **D17-F1** | the clean packet was red on `b71721aa…`: 7 findings, two classes (`REGISTER` name-vs-id; `CONSEQUENCE` on the constraint rows) | **high** — a false red on the delivered bytes | §3 | fixed on `a130f368…`, **unfiled** |
| **D17-F2** | the force predicate is `(any class substring) AND (any modifier substring)`; `commissive-binding granted` and `not-directive-binding` pass | **high** — inverts a row's legal content | §4.3 B1 | reported; owner = the delivered leg's seat |
| **D17-F3** | `kind` has a declared vocabulary (`LAW_KIND_DEFAULT`) that is never read; a row with `kind: no-such-kind` passes | medium | §4.3 B2 | reported |
| **D17-F4** | row deletion was invisible at `a130f368…`; **closed** at `7ed294c1…` by `LAW_DECLARED_ROWS` → `D4L-LAW-ROW` | closed | §4.2 B3 | closed by the D seat inside the window |
| **D17-F5** | an empty `consequence` is skipped by `if consequence and …`, so blanking a consequence is invisible; the runner's own consequence tamper never tests the empty case | medium | §4.3 B4 | reported |
| **D17-F6** | the agent resolver reads only the parenthesised `Name (ID)` form; a bare office name absent from the packet passes | medium | §4.3 B5 | reported |
| **D17-F7** | the consequence stems match stems, not polarity: `no record at all` and `never written down` pass | medium | §4.3 B6/B7 | reported |
| **D17-F8** | **closed** — `tools/gates/register-law-gate.py` landed at 20:20:40Z (`cfbff16b…`, selftest 33/33) in the claim's named place, emitting the claim's named class | closed | §0.0 | closed by the D seat inside the review window |
| **D17-F9** | the runner changed **six** times inside the review window (`b71721aa`→`7ed294c1`), with no filed correction, no changelog and no reading of the superseded revisions | medium — replayability | §0.1 | reported |
| **D17-F10** | the four `D4L-LAW-DANGLING` findings on the clean packet are real (`design_row` cites `QREG-05..08`, which were never landed as records) but the runner reclassifies clean-packet findings as "measurements, not verdicts" — so the class fires on the delivered bytes and cannot be used as a tamper signal | medium — control ambiguity | §4.2 | reported |

**Not findings.** Four things this seat checked and found sound: the `register`
and `axis` legs catch their structural mutations on every revision (§4.2); the
`DANGLING` findings are a *correct* reading of a real dangling reference, not a
false red (§0.1); the row-deletion leg was added inside the window and works
(§4.2); and the RL-4 fix is real and verified against the packet's own block
contents (§5).

## 7. What a replay leg with teeth would have to do (priced, not asserted)

Round 27 priced the *projector* amendment (its `E-1..E-7`). This is the cheaper,
narrower price for the leg the claim names — all of it inside the checker, none
of it a projector change:

| # | change | closes |
|---|---|---|
| V-1 | parse `force` into `(class, modifiers, polarity)` instead of substring-matching; a negation token flips the sense, and a class with no licensed modifier is a finding | `D17-F2` |
| V-2 | read `row['kind']` against the declared vocabulary | `D17-F3` |
| V-3 | assert the law's **extent** — a declared row-count or a required-kind set — so a deletion is a finding (**done at `7ed294c1…`**: `LAW_DECLARED_ROWS` → `D4L-LAW-ROW`) | `D17-F4` closed |
| V-4 | treat an empty/missing `consequence` as a finding, and add an empty-consequence route to the tamper control | `D17-F5` |
| V-5 | resolve **every** office token in `speaker`/`holder`, parenthesised or bare, against the packet's record ids and its rank-rule `wearer_ranks` | `D17-F6` |
| V-6 | read the consequence's polarity, not just its stems (a consequence asserting the absence of the record it must name is a finding) | `D17-F7` |
| V-7 | **done** — the checker now lives in `tools/gates/register-law-gate.py` | `D17-F8` closed |
| V-8 | file the reading: every superseded revision, its classes, and each closure, as a round-28 artifact | `D17-F9` |
| V-9 | resolve or land `design_row`'s `QREG-05..08` — either add the four rows to `registers` or repoint `design_row` at `RGL-*` — so the clean packet's `DANGLING` class does not fire on delivered bytes | `D17-F10` |

`V-1` is now the load-bearing item alone: `V-7` was delivered inside the
window, so the leg is a real delivered gate — and it inherits the force
over-match verbatim (`sed -n '262,266p' tools/gates/register-law-gate.py`), so
the delivered gate cannot yet see the inversion `RGL-02` exists to make. `V-3`
and `V-7` are the two items the round can claim; `V-1` is the one that decides
whether the law has teeth.

## 8. Independence and controls

- **The mutation set is authored here**, from the law's own field list
  (`force`, `speaker`, `consequence`, `kind`, `register`, `axis`) and from the
  law's *semantics* — B1 inverts the refusal `RGL-02` states, B3 removes the
  only exclusion row, B4/B6/B7 attack the consequence's polarity. None is copied
  from the runner's three tamper routes; the runner's routes are a subset
  (force/speaker/consequence) and two of the three are non-empty string
  substitutions that cannot reach B4.
- **The mutations are in-memory** (`copy.deepcopy` of the parsed packet), so no
  probe file is written and no tracked byte is touched. The clean control is the
  delivered packet itself, read at the digest in the header.
- **The positive control is the five-mutation catch set** (§4 C1–C5): a checker
  that caught nothing would make the bypasses meaningless, so every bypass is
  reported alongside evidence that the same checker fires on adjacent mutations.
- **The runner is read by `runpy`, read-only**, never re-implemented here: the
  findings quoted in §3 and §4 are the runner's own `law_check` output.
- **The digest churn is disclosed** (§0.1) rather than smoothed over: every
  reading names the revision it was taken against, because three revisions of
  the artifact moved inside the window.

**Write scope honoured:** this file, plus `.scratch/r28-d17/`. No component,
packet, tool, gate, fixture, pin, runner or filed round-8–27 byte was written.
No commit, no push.
