# R28-D18 — adversarial review 2 of 4: the force check over-matching

- **Seat:** R28-D18 (reviewer 2 of 4), round 28, loop 3 build 4 of 4, claim **D**
  `register-law-replay` (`reports/round-28/claims.json`).
- **Date:** 2026-10-18. Declared baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`;
  lane HEAD `69cecbc7dcf575a29f29660ecac470e05260fd86`. Measurement window
  **2026-10-18T20:14Z–20:16Z** (`date -u +%FT%TZ`).
- **Review target:** the **force** leg of the round-28 law reader —
  `LAW_FORCE_CLASSES` / `LAW_FORCE_MODIFIERS` and the predicate in
  `law_check` (`reports/round-28/run-validation.py`) — together with the
  **delivered** gate `tools/gates/register-law-gate.py`
  (`cfbff16bbb67d94d39b8d19f7f3fa14d985d18d1f306c8b8e39f79d20ad00e5e`, landed
  20:20:40Z, selftest 33/33) which carries the same predicate, and the
  vocabulary the packet's own `force` values declare
  (`examples/culture-d4/components/13-register-law.yml`, `RGL-01..RGL-05`).
- **Write scope:** this file only, plus gitignored scratch under
  `.scratch/r28-d18/`. `export TMPDIR=$PWD/.scratch` preceded every
  scratch-writing command. **No component, packet, tool, gate, fixture, pin,
  runner or filed rounds 8–27 byte was written; no commit, no push.**
- **Canon:** NON-CANON engineering evidence.

**Assignment.** Reviewer 2 of 4, adversarial: *an over-matching force check?*
D17 measures the force leg's **under**-matching — law violations it misses.
This seat measures the other direction: **does it accept forces that are not
forces**, and does it reject a force the law legitimately declares? An
over-matching vocabulary check is worse than no check, because it launders an
arbitrary string as a validated illocutionary value.

**Verdict in one line.** **Yes, it over-matches — in the strong sense.** The
force predicate is two independent substring tests composed with `AND`, so
membership of the *value* in the vocabulary is never tested: `assertive-binding`,
`expressive-not-rollable` and `none directive naming` all pass, and a fabricated
class word is enough to license any modifier. The five delivered values are not
spelled the way the reader's own vocabulary would spell them — every one of them
would fail an exact-membership check — so the reader's grammar is not derived
from the data it grades, and it cannot distinguish "a declared force" from "a
string containing two of my keywords".

## 0. The surface: what a force *is* in the delivered tree

Five values, all free prose, none in a machine shape (`13-register-law.yml`,
sha256 `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7`):

| row | `force` verbatim | what it asserts |
|---|---|---|
| `RGL-01` | `directive-binding for the charge; declarative-naming for the lot's name` | **two** forces, one per act |
| `RGL-02` | `commissive-binding refused` | a force **refused** |
| `RGL-03` | `directive-binding, not-rollable` | a force with a **rollability** qualifier |
| `RGL-04` | `none — a sound-channel constraint, not a speech act` | **no** force |
| `RGL-05` | `none — a dating constraint, not a speech act` | **no** force |

**There is no declared force vocabulary anywhere in the tree.** Measured:

```
$ grep -rn "directive-binding\|commissive-binding\|declarative-naming\|not-rollable" \
      examples/culture-d4/components/ examples/culture-d4/contract* 2>/dev/null
examples/culture-d4/components/13-register-law.yml:45:  - {id: RGL-01, … force: "directive-binding for the charge; declarative-naming for the lot's name", …}
examples/culture-d4/components/13-register-law.yml:46:  - {id: RGL-02, … force: "commissive-binding refused", …}
examples/culture-d4/components/13-register-law.yml:47:  - {id: RGL-03, … force: "directive-binding, not-rollable", …}
```

The only other place the vocabulary appears is the round-28 runner itself
(`LAW_FORCE_CLASSES`/`LAW_FORCE_MODIFIERS`) and the round-27 design prose
(`reports/round-27/law/design.md` §3, which names `directive-binding`,
`commissive-binding`, `declarative-naming` in a table). **The checker's
vocabulary is therefore a checker-local constant, not a declared contract** —
which is the structural fact every finding below follows from.

## 1. The grammar, stated exactly

```
$ sed -n '144,146p' reports/round-28/run-validation.py
LAW_FORCE_CLASSES = ("assertive", "directive", "commissive", "expressive", "declarative")
LAW_FORCE_MODIFIERS = ("binding", "refused", "not-rollable", "none", "attested",
                       "witnessed", "naming", "constraint")
```

```
$ sed -n '550,561p' reports/round-28/run-validation.py
        classes = [name for name in LAW_FORCE_CLASSES if name in force]
        tokens = {token for token in re.split(r"[^a-z-]+", force) if token}
        modifier_ok = any(m in force for m in LAW_FORCE_MODIFIERS)
        none_only = "none" in tokens and not classes
        declared_ok = bool(declared_forces & tokens)
        if not ((classes and modifier_ok) or none_only or declared_ok):
            findings.append({"class": "D4L-LAW-FORCE", …})
```

The accepted grammar is:

> **accept** if `(∃ class c: c is a substring of force) AND (∃ modifier m: m is a
> substring of force)` — or if `none` appears as a token and no class does — or
> if any token of the value is in a caller-supplied vocabulary (which the caller
> passes as `None`, so this branch is inert in the delivered path).

Three properties follow, and each is a defect:

1. **`class in force` is substring membership of the whole value**, not token
   membership. `directive` is a substring of `not-directive-binding`, and
   `naming` is a substring of `declarative-naming`.
2. **The class test and the modifier test are independent.** They may match
   different words in the value, in any order, with any relation between them.
3. **`modifier_ok` is `any(m in force)`**, so a modifier anywhere licenses a
   class anywhere.

## 2. The over-match: fabricated forces accepted

```
$ export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
$ python3 - <<'PY'
import runpy, re
ns = runpy.run_path('reports/round-28/run-validation.py')
for v in ["commissive-binding granted","assertive-binding","expressive-not-rollable",
          "none directive naming","not-directive-binding","declarative-naming",
          "directive-binding, not-rollable","commissive-binding refused"]:
    classes = [n for n in ns['LAW_FORCE_CLASSES'] if n in v]
    mods    = any(m in v for m in ns['LAW_FORCE_MODIFIERS'])
    print(f"  {v!r:36} classes={str(classes):24} modifier_ok={mods} -> PASS={bool(classes and mods)}")
PY
  'commissive-binding granted'     classes=['commissive'] modifier_ok=True -> PASS=True
  'assertive-binding'              classes=['assertive']  modifier_ok=True -> PASS=True
  'expressive-not-rollable'        classes=['expressive'] modifier_ok=True -> PASS=True
  'none directive naming'          classes=['directive']  modifier_ok=True -> PASS=True
  'not-directive-binding'          classes=['directive']  modifier_ok=True -> PASS=True
  'declarative-naming'             classes=['declarative'] modifier_ok=True -> PASS=True
  'directive-binding, not-rollable' classes=['directive'] modifier_ok=True -> PASS=True
  'commissive-binding refused'     classes=['commissive'] modifier_ok=True -> PASS=True
```

Read the last four rows together. **`not-directive-binding`,
`declarative-naming`, `directive-binding, not-rollable` and
`commissive-binding refused` are indistinguishable to this predicate** — all
four pass with the identical mechanism. The vocabulary cannot tell a negation
(`not-directive-binding`) from an assertion (`directive-binding`), or a refusal
from a grant.

Confirmed end-to-end through the real reader on the delivered packet (in-memory
mutation, no file written):

```
$ python3 - <<'PY'
import runpy, copy
ns = runpy.run_path('reports/round-28/run-validation.py')
base = ns['load_packet']('examples/culture-d4/packet.d4.yml')
def probe(label, v):
    p = copy.deepcopy(base); p['register_law'][1]['force'] = v
    f, _ = ns['law_check'](p)
    print(f"  RGL-02 force={v!r:34} findings={len(f)}")
probe("CLEAN (control, unchanged)", base['register_law'][1]['force'])
for v in ["commissive-binding granted","assertive-binding","expressive-not-rollable",
          "none directive naming","not-directive-binding","no directive whatsoever"]:
    probe("tampered", v)
PY
  RGL-02 force='commissive-binding refused'  findings=0      # clean control
  RGL-02 force='commissive-binding granted'  findings=0
  RGL-02 force='assertive-binding'           findings=0
  RGL-02 force='expressive-not-rollable'     findings=0
  RGL-02 force='none directive naming'       findings=0
  RGL-02 force='not-directive-binding'       findings=0
  RGL-02 force='no directive whatsoever'     findings=1      # the only one caught
```

**The only mutation caught is the one that omits both keyword sets entirely.**
Every mutation that keeps one class word and one modifier word passes, whatever
it says.

## 3. The `none_only` branch: a second over-match

```
none_only = "none" in tokens and not classes
```

`none_only` accepts a value whose token set contains `none` and whose class list
is empty. The delivered constraint rows rely on it:

```
RGL-04  force = 'none — a sound-channel constraint, not a speech act'  -> none_only=True,  PASS
RGL-05  force = 'none — a dating constraint, not a speech act'         -> none_only=True,  PASS
```

But `not classes` is evaluated against the **substring** class test, so a value
carrying a class word anywhere loses `none_only` and falls back to the `AND`
branch — where it passes anyway (§2, `none directive naming`). The two branches
are therefore not independent: whichever way a value goes, a class word plus a
modifier word passes.

Worse, the `none` token is checked for presence, never for **sense**. A value
that says the opposite of "no force" passes:

```
$ python3 - <<'PY'
import runpy, re
ns = runpy.run_path('reports/round-28/run-validation.py')
for v in ["none", "none whatsoever, but binding", "not none at all",
          "none — a sound-channel constraint, not a speech act"]:
    classes = [n for n in ns['LAW_FORCE_CLASSES'] if n in v]
    tokens  = {t for t in re.split(r"[^a-z-]+", v) if t}
    print(f"  {v!r:46} classes={classes} none_only={'none' in tokens and not classes}")
PY
  'none'                                        classes=[] none_only=True
  'none whatsoever, but binding'                classes=[] none_only=True
  'not none at all'                             classes=[] none_only=True
  'none — a sound-channel constraint, not a speech act' classes=[] none_only=True
```

`not none at all` is accepted as "no force". The reader's `none` test is a token
presence test, and the law's own constraint rows show why that is fragile: the
delivered `none` values are `none — …` clauses whose *meaning* is carried by the
clause, which the reader never reads.

## 4. The reverse direction: does it reject a legitimate force?

An over-matching checker can also be an under-inclusive one, if its vocabulary
is wrong. It is: **every one of the five delivered values fails an
exact-membership reading of the reader's own vocabulary.**

```
$ python3 - <<'PY'
import runpy
ns = runpy.run_path('reports/round-28/run-validation.py')
VOCAB = set(ns['LAW_FORCE_CLASSES']) | set(ns['LAW_FORCE_MODIFIERS'])
delivered = [
 "directive-binding for the charge; declarative-naming for the lot's name",
 "commissive-binding refused",
 "directive-binding, not-rollable",
 "none — a sound-channel constraint, not a speech act",
 "none — a dating constraint, not a speech act",
]
for v in delivered:
    print(f"  exact-membership: {v[:52]!r:56} in vocabulary = {v in VOCAB}")
PY
  exact-membership: 'directive-binding for the charge; declarative-naming'  in vocabulary = False
  exact-membership: 'commissive-binding refused'                             in vocabulary = False
  exact-membership: 'directive-binding, not-rollable'                        in vocabulary = False
  exact-membership: 'none — a sound-channel constraint, not a speech act'    in vocabulary = False
  exact-membership: 'none — a dating constraint, not a speech act'           in vocabulary = False
```

**0 of 5.** The vocabulary is a set of *fragments* that the data never equals.
That is why the predicate has to be a substring test, and why the substring test
has to over-match: the vocabulary was written as keywords for a grammar the data
does not follow. The honest description of the current leg is not "a force
vocabulary check" but **"a check that the force field contains at least one of
five class words and at least one of eight modifier words, in any arrangement,
in any relation, with any negation"**.

The one value that is *not* prose-with-keywords — `RGL-01`'s compound, two
forces joined by `;` — shows the missing piece directly. A force grammar for
this data would have to:

- split a compound on `;` or `,` and grade each part;
- treat `refused` as a **polarity** marker that inverts the class's assertion,
  not as a modifier that licenses it;
- treat `none — <clause>` as a *constraint* row whose force is absent by design,
  and grade its clause against the constraint vocabulary instead;
- treat `not-rollable` as a rollability qualifier, not a force class.

None of those four is done. §6 prices them.

## 5. The `declared_ok` branch: inert, and a trap if wired

```
declared_ok = bool(declared_forces & tokens)
```

`declared_forces` comes from `law_check(packet, force_vocabulary=None)`, and the
delivered call sites pass no vocabulary:

```
$ grep -n "law_check(" reports/round-28/run-validation.py
    own_findings, own_context = law_check(packet)
    f, ctx = ns['law_check'](p)          # (this seat's probes)
```

So `declared_ok` is always `False` in the delivered path — a declared-vocabulary
route that exists, is documented in the docstring ("every `force` value must name
a declared illocutionary class"), and is never exercised. **If it were wired**
with a vocabulary derived from the packet's own values (the natural move — "the
force must name a force the packet already uses"), it would *widen* the
acceptance set, because `declared_forces & tokens` is a token-intersection test
that accepts any value sharing one token with a delivered value. That is the
round-27 `RL-3` failure mode repeating in the checker: a self-referential
vocabulary cannot detect a violation of the thing it was derived from.

## 6. Named findings

| id | finding | severity | evidence | disposition |
|---|---|---|---|---|
| **D18-F1** | the force predicate is `(any class substring) AND (any modifier substring)` over the whole value; the class and modifier need no relation — **carried verbatim into the delivered gate** `register-law-gate.py` | **high** — over-match | §1, §2, §9 | reported; owner = the delivered gate |
| **D18-F2** | `commissive-binding granted` passes on `RGL-02`, the row whose entire content is the refusal — confirmed end-to-end on the delivered gate | **high** — inverts the law | §2, §9 | reported |
| **D18-F3** | negation is invisible: `not-directive-binding` and `directive-binding` are indistinguishable | **high** | §2 | reported |
| **D18-F4** | `none_only` tests token presence, not sense; `not none at all` is accepted as "no force". **Narrowed on the delivered gate**, whose `NON_FORCE_RE` requires a separator after `none` (`none but wibble` rejected), though `none directive naming` still passes via the `AND` branch | medium (narrowed) | §3, §9 | reported |
| **D18-F5** | 0 of 5 delivered `force` values equal any member of the reader's own vocabulary: the vocabulary is fragments, not values, so the grammar cannot be tightened without first shaping the data | **high** — the root cause of F1–F4 | §4 | reported |
| **D18-F6** | no declared force vocabulary exists in the component/contract; the vocabulary is a checker-local constant — now in the **delivered gate** (`DECLARED_FORCE_CLASSES`/`MODIFIERS`), quoted from the design prose but not from a declared contract row | medium | §0, §9 | reported |
| **D18-F7** | `declared_ok` is inert (`force_vocabulary=None` everywhere); if wired from the packet's own values it would widen acceptance — the RL-3 self-reference failure repeated | medium | §5 | reported |
| **D18-F8** | `RGL-01`'s compound force (two forces joined by `;`) is graded as one value; a row asserting two forces is checked against one | low–medium | §4 | reported |

**Not findings.** The reader does catch a force value that names neither a class
nor a modifier (`no directive whatsoever`), and its `register`/`axis`/`speaker`
legs are separate surfaces (graded in D17). The clean-packet reading is not
silent on the current tree (four `D4L-LAW-DANGLING` holds — D17 §0.0), so every
finding above is stated against the clean reading rather than against zero.

**On the delivered gate.** `D18-F1`, `D18-F2` and `D18-F3` were re-confirmed
against `tools/gates/register-law-gate.py` after it landed (§9): the delivered
gate carries the same predicate verbatim and accepts `commissive-binding granted`
on `RGL-02`. `D18-F4` is *narrowed* there — the gate's `NON_FORCE_RE` requires a
separator after `none`, so `none but wibble` is rejected, though
`none directive naming` still passes via the `AND` branch.

## 7. What a force leg that does not over-match would need (priced)

| # | change | closes |
|---|---|---|
| W-1 | declare the force vocabulary in the **component or contract**, not in the checker — a `force_vocabulary` row beside `record_fields`, so the vocabulary is replayable from the tree | `D18-F6` |
| W-2 | make the field machine-shaped: `force` as a list of `{class, polarity, qualifiers}` (or `class` + `modifier` + `polarity` columns), so a compound is two rows and a negation is a field | `D18-F5`, `D18-F8` |
| W-3 | grade by token equality against the declared vocabulary, not substring membership | `D18-F1` |
| W-4 | treat polarity explicitly: `refused` inverts the class's assertion; a `refused` row's force is the **negation** of the named class | `D18-F2`, `D18-F3` |
| W-5 | grade a `none` value's clause against the constraint vocabulary (`sound-channel`, `dating`, …) rather than testing the token `none` | `D18-F4` |
| W-6 | drop or wire `declared_ok` honestly: a self-derived vocabulary may not be used to validate itself | `D18-F7` |

`W-2` is the load-bearing item: without a machine shape for `force`, every other
change is a stricter substring test on the same prose, which moves the false
negatives around rather than removing them.

## 8. Independence and controls

- **The probe set is authored here** from the reader's own declared vocabulary
  and from the law's own semantics (the `RGL-02` refusal, the `RGL-01` compound,
  the `RGL-04`/`RGL-05` constraint clauses). The mutations are in-memory
  (`copy.deepcopy`); no probe file is written and no tracked byte is touched.
- **Both directions are measured**: over-match (§2, §3) and under-inclusiveness
  (§4). A reviewer who measured only the over-match would miss that the
  vocabulary cannot express the data at all.
- **The positive control is included**: `no directive whatsoever` is caught, so
  the predicate is shown to be a predicate and not a constant `True`.
- **The runner is read by `runpy`, read-only.** All output quoted is the
  runner's own `law_check` or its own constants.
- **Digest and churn:** the runner moved **six** times inside the window
  (D17 §0.1). The readings in §2 were taken at `a130f36877494060…` (20:16:07Z)
  and **re-verified at `d4f0545850524af5…` (20:19:19Z)** — the last revision
  measured here. The force constants and the predicate are byte-identical across
  every revision measured, so the findings are not churn artifacts. The
  re-verification, with the clean control now at 4 findings (`D4L-LAW-DANGLING`,
  D17 §0.1), compares each mutation against the control rather than against zero:

```
$ python3 - <<'PY'      # runner d4f0545850524af5e1c76ff9f6a2a82cf9322d203eed0cfda8085ee2978c6f0b
import runpy, copy, hashlib, pathlib
ns = runpy.run_path('reports/round-28/run-validation.py')
print("runner:", hashlib.sha256(pathlib.Path('reports/round-28/run-validation.py').read_bytes()).hexdigest())
print("LAW_FORCE_CLASSES  =", ns['LAW_FORCE_CLASSES'])
print("LAW_FORCE_MODIFIERS=", ns['LAW_FORCE_MODIFIERS'])
base = ns['load_packet']('examples/culture-d4/packet.d4.yml')
def n(v):
    p = copy.deepcopy(base); p['register_law'][1]['force'] = v
    return len(ns['law_check'](p)[0])
clean = n(base['register_law'][1]['force'])
print("clean control =", clean)
for v in ["commissive-binding granted","commissive-binding","not-directive-binding",
          "none directive naming","assertive-binding","expressive-not-rollable",
          "no directive whatsoever"]:
    print(f"  {v!r:34} findings={n(v)} {'<-- SAME AS CLEAN (bypass)' if n(v)==clean else '<-- caught'}")
PY
runner: d4f0545850524af5e1c76ff9f6a2a82cf9322d203eed0cfda8085ee2978c6f0b
LAW_FORCE_CLASSES  = ('assertive', 'directive', 'commissive', 'expressive', 'declarative')
LAW_FORCE_MODIFIERS= ('binding', 'refused', 'not-rollable', 'none', 'attested', 'witnessed', 'naming', 'constraint')
clean control = 4
  'commissive-binding granted'       findings=4 <-- SAME AS CLEAN (bypass)
  'commissive-binding'               findings=4 <-- SAME AS CLEAN (bypass)
  'not-directive-binding'            findings=4 <-- SAME AS CLEAN (bypass)
  'none directive naming'            findings=4 <-- SAME AS CLEAN (bypass)
  'assertive-binding'                findings=4 <-- SAME AS CLEAN (bypass)
  'expressive-not-rollable'          findings=4 <-- SAME AS CLEAN (bypass)
  'no directive whatsoever'          findings=5 <-- caught
```

**Every §2 finding reproduces on the live revision, measured against the live
control.** Note `'commissive-binding'` also passes: deleting the modifier
`refused` leaves the class `commissive` present and the value still contains
`binding` as a substring of `commissive-binding` itself — so the modifier test is
satisfied by the class word's own spelling. That is a cleaner statement of
`D18-F1` than the fabricated-value probes and is added to it.

## 9. Confirmed on the DELIVERED gate, not only the runner

`tools/gates/register-law-gate.py` landed at 20:20:40Z with the **same force
predicate, verbatim** — same vocabulary, same two substring tests, same `none`
handling. The predicate is no longer a review-instrument property; it is the
delivered artifact's:

```
$ sed -n '262,266p' tools/gates/register-law-gate.py
            classes = [name for name in DECLARED_FORCE_CLASSES if name in force]
            modifier_ok = any(m in force for m in DECLARED_FORCE_MODIFIERS)
            none_only = bool(NON_FORCE_RE.match(force)) and not classes
            binding_act = not none_only
            if not ((classes and modifier_ok) or none_only):
```

Replicating that predicate verbatim over the probe set:

```
$ python3 - <<'PY'
import runpy
g = runpy.run_path('tools/gates/register-law-gate.py')
C, M, NF = g['DECLARED_FORCE_CLASSES'], g['DECLARED_FORCE_MODIFIERS'], g['NON_FORCE_RE']
for v in ["commissive-binding refused","commissive-binding granted","commissive-binding",
          "not-directive-binding","assertive-binding","expressive-not-rollable",
          "none directive naming","none but wibble",
          "none — a sound-channel constraint, not a speech act"]:
    f = v.lower()
    classes = [n for n in C if n in f]
    mod = any(m in f for m in M)
    none_only = bool(NF.match(f)) and not classes
    print(f"  {v!r:56} classes={str(classes):14} PASS={(classes and mod) or none_only}")
PY
  'commissive-binding refused'                             classes=['commissive'] PASS=True
  'commissive-binding granted'                             classes=['commissive'] PASS=True
  'commissive-binding'                                     classes=['commissive'] PASS=True
  'not-directive-binding'                                  classes=['directive']  PASS=True
  'assertive-binding'                                      classes=['assertive']  PASS=True
  'expressive-not-rollable'                                classes=['expressive'] PASS=True
  'none directive naming'                                  classes=['directive']  PASS=True
  'none but wibble'                                        classes=[]             PASS=False
  'none — a sound-channel constraint, not a speech act'    classes=[]             PASS=True
```

**The delivered gate accepts `commissive-binding granted` on `RGL-02`** — the row
whose entire legal content is the refusal — exactly as the runner did. And it
**does** improve one thing the runner did not: `NON_FORCE_RE =
r"^\s*none\s*(?:[—–\-:,]|$)"` requires a separator after `none`, so
`none but wibble` is correctly rejected. `none directive naming` still passes,
because the class word defeats `none_only` and the `AND` branch accepts it.

End-to-end on the delivered gate, as line-level transforms of the delivered
bytes (D17 §4.4 has the full table): the force-inversion route leaves the gate's
finding count at its clean reading of 4, while the control `force: no-such-force`
raises it to 5. **`D18-F1`, `D18-F2` and `D18-F3` are therefore findings about
the delivered artifact, not about a review instrument.**

**Write scope honoured:** this file, plus `.scratch/r28-d18/`. No component,
packet, tool, gate, fixture, pin, runner or filed round-8–27 byte was written.
No commit, no push.
