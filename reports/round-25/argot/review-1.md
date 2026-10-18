# R25-D15 — adversarial review: the argot-derivation leg, attacked

- **Seat:** R25-D15 (reviewer 1 of 3), round 25, loop 3 build 1 of 4, claim **D**
  `argot-derivation-check` (`reports/round-25/claims.json:20-27`).
- **Date:** 2026-10-18. Baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`;
  worktree HEAD at measurement `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- **Write scope:** this file only. Scratch under `.scratch/r25-d15/`
  (`TMPDIR=$PWD/.scratch` preceded every scratch write). No tool, gate, packet,
  component, or rounds 8–24 byte touched; no commit, no push.
- **Canon:** NON-CANON engineering evidence. No real language, institution,
  script, or argot is described, cited, or approximated.

**Assignment.** Reviewer 1 of 3, adversarial: *a replay that should fail passing?
a pattern that over-matches?* The review target is the round-25 D-argot leg —
`reports/round-25/argot/execution-1..4.md`, the harness they run
(`.scratch/r25-d11/argot-replay.py`, sha256
`4934f17d0cfed1b5248d45aca18dab6b129d42ce709981b76ed70f5f7853673d`, scratch,
not promoted), **and the delivered gate that landed during this review**,
`tools/gates/argot-derivation-gate.py` (sha256
`07db6e9b4e01539e1dbb8af9e51eada6fe37784145915a0387f48f2ecd99f8fe`, 748 lines,
`--selftest` 18/18). The delivered engine it is a candidate to extend,
`tools/gates/naming-collision-gate.py` gate C (sha256
`d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d`), is the
third engine and the control throughout.

**Note on target timing.** `argot-derivation-gate.py` did not exist when this
review began; it was written by a sibling seat mid-round. Sections 1–6 review
the scratch harness; **section 6A reviews the delivered gate** and is the more
consequential half — it carries three measured defects with controls.

**Verdict in one line.** The leg's *positive* result is real and reproducible
(12/12 rows, 0 violations — reproduced below, V-0). Its *negative* claim is
weaker than the reports state: the harness answers "should fail" for a
**lexicon** rewrite only by trusting the record's own `bases` (V-1 passes), and
for a **name** rewrite only via a duplicated `expected` column (V-2), and it has
**no exit code**, **no budget**, and **no template guard** where the delivered
gate has all three. Two attacks make a violating packet read green; one makes
the harness crash; one makes it hang. Every one is fixed by the gate discipline
the leg is supposed to inherit, so the findings are *scope and inheritance*
findings, not a refutation of the work. The delivered gate inherits all four
guards correctly — but it launders a violation when a field is deleted, admits a
self-derivation as correct, and never resolves a `derived_from` to a record
(6A.1–6A.3).

## 1. Method, and the two engines under comparison

Attacks run as subprocesses against mutated copies of the delivered packet
written under `.scratch/r25-d15/`. Receipts:

```
export TMPDIR=$PWD/.scratch
python3 .scratch/r25-d15/adv.py                 # 13 attacks, gate C
python3 .scratch/r25-d15/adv-d11.py             # 7 attacks, the D11 harness
python3 .scratch/r25-d15/adv-d11-decisive.py    # 7 decisive attacks
```

| | delivered gate C | D11 harness |
|---|---|---|
| match call | `_match_with_budget` → `re.fullmatch` (`:1230`) | `re.match` (`:31`) |
| wall-clock budget | `MATCH_BUDGET_SECONDS = 0.5` (`:1223`) | none |
| catastrophic-shape screen | `_catastrophic_pattern` (`:1303`) | none |
| template subset guard | `_template_problem` (`:1259`) | none |
| scope | `names[]` only (`:1356`) | `lexicon[]` route derived/compound **and** `names[]` |
| finding ids | `DERIV-AFFIX` / `DERIV-REPLAY` / `DERIV-HOLD` | prints `D4L-ARGOT-DERIV` as a *row field* (never in output, §4) |
| exit code | 0 clean / 1 findings / 2 could-not-evaluate | **always 0** on a well-formed packet |

The harness reads with the gate's own subset reader (`ncg.load_yaml`), which is
the right choice; the divergence is in the replay call and its guards.

## 2. V-0 — the positive result reproduces (control)

```
python3 .scratch/r25-d11/argot-replay.py examples/culture-d4/packet.d4.yml
→ {"rows": 12, "violations": 0}, 12 ok rows, exit 0
python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml
→ exit 1, 14 findings, 0 matching DERIV
```

Both engines agree the delivered packet's stated derivations replay clean. The
`derivation_note`'s pre-registered count ("the three rules replay the four
derived or compound records … and the eight names") is confirmed by
measurement: 4 + 8 = 12. **This is a genuine delivery** and no attack below
touches it.

## 3. A replay that should fail, passing

### V-1 — fabricated bases (measured PASS, should FAIL)

Leg 1 builds the stem from the record's **own** `bases` (`argot-replay.py:50`),
so a record whose term and bases are rewritten together replays clean. `L-48
haitun` (bases `hai`+`tun`) rewritten to `kalmes` with bases `kal`+`mes`:

```
VIOL L-48 | kalmes | derived | CX-01 | haitun | replay disagrees   ← earlier attempt
```

The earlier attempt caught it because the mutation anchored on the wrong lines
(term changed, bases unchanged). With both changed consistently:

```
python3 .scratch/r25-d11/argot-replay.py .scratch/r25-d15/w6c-fabricated.yml
→ violations 0, exit 0
python3 tools/gates/naming-collision-gate.py .scratch/r25-d15/w6c-fabricated.yml
→ exit 1, DERIV ids: []          (the gate does not read lexicon[] at all)
```

**A wrong derivation reads green.** Neither engine resolves a `bases` entry to a
record: the delivered gate never looks at `lexicon[]` (`:1356`), and the harness
trusts the record's own list. This is the assignment's first question answered
affirmatively.

### V-2 — the name side is protected by a redundant field, not by base resolution

**Correction to this review's own first reading.** I first wrote that a stem
rewrite passes; it does not, and the reason matters. `names[]` records carry an
`expected` field — a second, independent copy of the intended form
(`packet.d4.yml`, 8 occurrences) — and the harness compares against it
(`argot-replay.py:70-71`: `got != name or (exp and got != exp)`). So a name-side
rewrite is caught by the **duplicated field**, not by any base resolution:

```
name+stem rewritten consistently (kernam / ker+nam)
→ VIOL NM-01 | kernam | name | CX-01 | kernam | replay='kernam' name='kernam' expected='tumhai'
```

Note what caught it: `replay == name == 'kernam'`, and only `expected` disagreed.
The replay itself was satisfied.

**The lexicon side has no `expected` field, and there the rewrite passes**
(V-1, measured `violations 0`). So the leg's discriminating power on the name
side is a property of one extra column, and a family that omits `expected` —
or an author who rewrites it too — removes the only thing that catches a
consistent fabrication. That is the finding, and it is narrower and more
actionable than the version I first wrote: **the check that catches a fabricated
name derivation is a duplicated field, not a resolved base.**

Decisive receipt — remove `expected` from `NM-01` and rewrite name+stem together:

```
v2d  expected removed, record untouched        → violations 0
v2e  expected removed, name+stem rewritten     → violations 0
     (with `expected` present the same rewrite gave 1 violation naming `expected`)
```

With the field present the catch is `expected='tumhai'`; with it gone there is
nothing left to disagree.

### V-3 — base identity is never resolved (the structural cause)

`tools/check-evidence-coupling.py:871` `check_names` is the D3 precedent and
does what neither D4 engine does: it resolves each base id to the **lexicon
record** and recomputes from the base's own E1 form (`:879-895`,
`computed = "".join(e1_forms)`, then `formation.expected != computed` →
`D3-DERIVATION`). `tools/gates/lexicon-coverage-audit.py` carries the same
discipline for lexicon records (`:802-810`, `D-form-mismatch`) and additionally
enforces `base_eligibility: native-only` (`:963`).

That last check is **dead code on D4**. It compares a base's layer against
`("loan", "borrowed")` (`:966-968`), but D4 stores layer *names*
(`layer: "Salt-road trade layer"`), not those two tokens. Measured:

```
# L-45 tikmes -> karmes (reproduces from the borrowed base kar), construction native-only
lexicon-coverage-audit.py  → exit 0, no finding     ← should be L-integration-mismatch
naming-collision-gate.py   → exit 1, no DERIV id
```

Control: the same mutation with a native base is also exit 0, so the leg is not
merely silent — it cannot fire on this packet's layer vocabulary.

**The delivered argot gate has the same gap in its own vocabulary.** It compares
`apply(op, base_string)` with the form and never resolves `derived_from` to a
record (`argot-derivation-gate.py`), so a fabricated base that happens to yield
the form passes — measured in 6A.2/6A.3 below. The D3 precedent's base
resolution (`any(b not in lex for b in bases)`) is the missing discipline in both
delivered engines.

## 4. A pattern that over-matches

### V-4 — `cname2rid` maps by note prefix (measured mis-grade)

`argot-replay.py:20-24` resolves a construction **name** to a rule **id** by
`str(rule.get("note","")).startswith(str(c.get("name","")))`. A rule whose note
happens to begin with another construction's name is mis-mapped, and the
lexicon record is then graded by the wrong rule. Mutating CX-02's note to begin
`"STACK-COMPOUND …"`:

```
python3 .scratch/r25-d11/argot-replay.py .scratch/r25-d15/w3-note-collision.yml
→ violations 3, exit 0
```

Three rows change verdict because of a **prose** edit in an unrelated rule's
note. The delivered gate has the same class of join but on a typed field
(`formation.rule` is a rule **id**, `:1388`), not on prose. A note is
documentation; making it a join key means a copy-edit can move a grade.

### V-5 — `re.match` where the gate uses `re.fullmatch` (over-match, latent)

`argot-replay.py:31` calls `re.match`; the gate calls `re.fullmatch`. Python's
`$` matches before a trailing newline, so the two disagree on a stem ending in
one:

```
decoded stem: 'tum+hai\n'
gate  fullmatch → None        (rejects)
harness match   → <Match span=(0,7) 'tum+hai'>   (accepts)
```

This is a genuine over-match: the harness's pattern is satisfied by a **prefix**
of the stem. It is **latent, not exploited**, and this review corrects its own
first reading: I expected the gate to catch the corrupt packet and it does not.
The gate normalises the stem with `_s(...).strip()` before matching (`:1384`),
so the trailing newline is removed and both engines read that packet green:

```
gate _gate_c on clean packet        → 0 findings
gate _gate_c on newline-stem packet → 0 findings
```

So V-5 is **not** a demonstrated false pass — it is a demonstrated *divergence*
in match semantics with no packet-representable trigger yet found, because the
gate's strip closes the newline vector and the harness's `stem` for names is
taken from the same `formation.stem` field the gate strips. Recorded as a latent
robustness finding, not a failure: **no false pass was demonstrated here**, and
the claim that one was is withdrawn. The one-word fix (`fullmatch`) still
removes the divergence and the whole prefix-matching class.

### V-6 — no catastrophic-backtracking guard (measured HANG)

The harness has neither the gate's shape screen nor its budget. A
packet-authored catastrophic pattern under the harness's raw `re.match`:

```
pattern ^(?P<a>(a+)+)$, stem 'a'*28 + 'b'
re.match → HUNG (>3 s, killed by the measuring deadline)
gate _catastrophic_pattern(pattern) → True,  budget 0.5 s → DERIV-HOLD, 0.03 s
```

The gate refuses the same pattern in 0.03 s and reports `DERIV-HOLD ×8`. The
harness inherits a packet-authored regex and gives it unbounded wall clock —
the class `SKILL.md:203` and the gate docstring (`:56-62`) name explicitly.

## 5. Attacks that are real but not what the id implies

### V-7 — template escape leaks interpreter internals (measured LEAK)

`out.format(**m.groupdict())` (`:36`) has no subset guard. `{stem.__class__}`
is rendered and echoed into the finding:

```
VIOL L-47 | kalen | derived | CX-03 | <class 'str'> | replay disagrees
VIOL L-45 | tikmes | derived | CX-01 | (<class 'str'>, <class 'object'>)mes | replay disagrees
```

The gate refuses the same output as `DERIV-HOLD` ("placeholder
`{a.__class__.__mro__}` is not a plain named field") in 0.03 s. This is the
round-26 §3 D9 class the gate's `_template_problem` was written for; the
harness reintroduces it.

### V-8 — uncaught `KeyError` (measured CRASH)

A rule whose pattern yields only some of the groups its output names crashes
the harness with a traceback:

```
pattern ^(?P<a>tum)$, output {a}{b}
→ KeyError: 'b', exit 1, traceback on stderr, 0 violations printed
gate → DERIV-REPLAY, exit 1, no traceback
```

The gate wraps the format call (`except (KeyError, IndexError)` → `DERIV-HOLD`,
`:1508-1517`). The harness's exit 1 here is *incidental* (an uncaught
exception), not a verdict: on a well-formed packet its exit is always 0 (§1).

### V-9 — the forecast id is a row field, never printed

Every violation row carries `D4L-ARGOT-DERIV` as `r[6]` (`:48-72`), but the
printer emits `r[0..5]` only (`:77`):

```
python3 .scratch/r25-d11/argot-replay.py .scratch/r25-d15/f5-id.yml
VIOL L-46 | mesor | derived | CX-02 | mesar | replay disagrees
grep D4L-ARGOT-DERIV in stdout → false
```

So the claim "a violating form is `D4L-ARGOT-DERIV`" is **not observable in the
leg's own output**, and at the time of measurement no engine in `tools/` or
`examples/` emitted it (`adv.py` A11: 0 files, 2026-10-18T17:32Z). Also note the
id is stamped on a *concatenation* violation (CX-02), where `forecast.md:41-47`
reserves it for the Δ3 argot relation and says explicitly it is **not** the
naming gate's replay id — the harness collapses two classes onto one id.

**Superseded by 6A (time-stamped).** The A11 sweep is no longer true: the
delivered `tools/gates/argot-derivation-gate.py` emits `D4L-ARGOT-DERIV` in its
findings. V-9 is retained as the harness finding at its measurement time and is
**answered** by the delivered gate, which prints the id, carries real exit codes,
and separates the classes (its `D4L-ARGOT-RULE`/`D4L-ARGOT-COVERAGE` ids keep the
concatenation and relation classes apart).

## 6A. The delivered gate — `tools/gates/argot-derivation-gate.py`

**This is the consequential half of the review.** The gate landed during the
round (sha256 `07db6e9b…`, 748 lines, `--selftest` 18/18, default run over
`examples/culture-d4/packet.d4.yml` → exit 0, `register_scoped=6 violations=0`).
It is well-built: it **inherits all four guards** the harness lacked — it loads
`naming["_match_with_budget"]` and `naming["_catastrophic_pattern"]` and
`naming["_template_problem"]` read-only by path (`:392-419`), it names the
dependency digest on stdout, it has the three real exit codes, and it names the
record, the rule, the inputs and the computed value in every finding. Sections
V-1..V-9 above are largely answered by it. Three defects remain.

### 6A.1 — a violating record launders to green when one field is deleted (measured)

The gate reads a record as in-scope when it declares `derived_from` **and**
`derivation` (or a register). A failing record whose `derivation` field is
removed stops being a derived pair and is no longer replayed:

```
# fixture Q-13 {term: suk, derived_from: sun, derivation: reverse}  → FAIL (reverse(sun) = nus ≠ suk)
python3 tools/gates/argot-derivation-gate.py tools/gates/fixtures/argot-derivation-gate.yml
→ 5 findings, D4L-ARGOT-DERIV ×4 (incl. Q-13), coverage derived_pairs=8 violations=4
# the same record with `derivation` deleted:
→ 4 findings, no line names Q-13,      coverage derived_pairs=7 violations=3
# with both fields deleted:
→ 4 findings, no line names Q-13
```

Control: keeping the pair reproduces the FAIL (`F1_control_keep_pair`). So
**deleting one field clears the finding** — the violation is laundered by
omission, and the coverage counter silently drops 8→7 rather than reporting a
malformed pair. This is the D2 "laundered hold" class (`SKILL.md` T2: "a
`return True` branch for non-default input is a laundering channel") reached by
a different route: not a skip branch, but a **scope predicate** a writer can
leave. The record is still in the packet, still wrong, and now ungraded.

Fix shape: a register-scoped record that declares exactly one of
`derived_from`/`derivation` is `D4L-ARGOT-RULE` (HOLD), not out of scope — the
gate already has that id and uses it for the unlicensed-operation case
(`F4`: `derivation: NOPE` → `D4L-ARGOT-RULE`, measured).

### 6A.2 — a self-derivation is accepted as correct (measured)

A record whose form equals its own base passes whenever the operation is an
identity on that string — a palindrome under `reverse`, or a one-syllable base
under `head2`:

```
{id: Q-02, term: qqq, derived_from: qqq, derivation: reverse}  → no line names Q-02
{id: Q-02, term: kin, derived_from: kin, derivation: head2}    → no line names Q-02
CONTROL {term: qqq, derived_from: min, derivation: reverse}    → D4L-ARGOT-DERIV: FAIL
```

The control proves the leg is discriminating, so this is not "the gate is
asleep": it is that `apply(op, base) == form` is satisfied trivially when
`form == base`. A record that declares itself its own derivation is not a
derivation, and the gate has no check for it.

The D3 precedent has exactly this check
(`tools/check-evidence-coupling.py:904-908`: "name equals its base lexeme" →
`D3-DERIVATION`), so the discipline is already in the lane and was not carried
over. See `review-3.md` §3 for the full cross-check.

### 6A.3 — `derived_from` is a string, never resolved to a record (measured)

The gate compares `apply(op, base_string)` with the form; it never looks up the
base as a record. Consequences measured on the fixture:

```
derived_from: ZZZZ   (no such record)  → FAIL (only because reverse(ZZZZ) ≠ nim)
derived_from: Q-04   (another record's id) → FAIL (same reason)
```

So the *failure* is incidental — the gate is comparing strings, and a
`derived_from` that names nothing fails for the right reason by accident. The
class that does **not** fail is the one where the fabricated base happens to
yield the form (6A.2's palindrome is an instance). The base identity is never
established: the gate cannot distinguish "derived from the lexeme the language
has" from "derived from a string the writer typed".

This is the same gap `review-3.md` §3 reports for the harness, now measured in
the delivered gate; the D3 precedent resolves `bases` against the lexicon index
(`check-evidence-coupling.py:879-882`, `any(b not in lex for b in bases)`).

### 6A.4 — what the gate gets right (recorded so it is not lost)

- All four guards inherited from the naming gate, by path, with the dependency
  digest printed (`dependency: tools/gates/naming-collision-gate.py sha256 …`).
- `D4L-ARGOT-COVERAGE` is real: it fires when operations are declared and no
  record carries a pair, and the selftest asserts the exact id list
  (`:679`, `coverage-hold-fires`). The limit — a packet declaring its ops only
  in prose is not detected — is **stated in the docstring** rather than hidden,
  which is the right treatment.
- Every finding names the record id, the form, the register, the rule, the
  input, the computed value and the delivered value. The fixture's four
  `D4L-ARGOT-DERIV` + one `D4L-ARGOT-RULE` reproduce exactly against the
  committed `.expected` file, and the `head2` maximal-onset trap (`saalum` vs
  `saalu`) is the fixture's own first planted violation — the design's named
  ambiguity, tested.
- It skips a symbol record carrying prose in a `form:` field, with the scope
  control in the fixture itself.

## 6. What the harness gets right, and the honest reading

- The positive replay is real, reproduced, and agrees with the gate (V-0).
- It reads with the gate's own subset reader rather than a second parser.
- `execution-4.md` §2-§3 states the register half has **zero input** and does
  not claim it; `execution-3.md` names F-1..F-8 and the culture-fork root
  cause. That is the SKILL's honest-stop discipline applied correctly, and this
  review does not dispute it.
- `execution-1.md` §4 already declares the replay's bound: "it cannot detect a
  record whose stated rule is *not* the rule the language actually used." V-1
  and V-2 are that bound **measured**, not a contradiction of it. The finding is
  that the bound is wider than the report's framing suggests: on the lexicon
  side the *base identity* is unverified (V-1), on the name side the only catch
  is a duplicated column (V-2), and the leg has no negative exit code (V-9).

**Severity reading.** V-1..V-9 are not defects in delivered bytes — the harness
is scratch and the reports are candid. They are the reason the harness must
**not** be promoted as-is: promoted, it would be a green leg with a false-pass
class (V-1), a prose-keyed join (V-4), a hang vector (V-6), an internals leak
(V-7), and a crash (V-8) — while the id it claims (V-9) is unobservable. The
fix is not new design: it is the gate's own four guards, plus base resolution
(V-3) from the D3 precedent.

**6A severity reading — higher, because the gate is delivered.** 6A.1 is a
laundering channel in shipped bytes: deleting one field clears a FAIL and drops
the coverage counter without a malformed-pair finding. 6A.2 lets a
self-derivation pass. 6A.3 leaves base identity unestablished. None of the three
is a false red — the gate never cries wolf — so the risk is a **false green**
on a packet that omits or fabricates its derivation fields, which is precisely
the direction an author under pressure would move. All three are fixed by
disciplines the lane already holds (`D4L-ARGOT-RULE` for a half-declared pair,
D3's base-resolution and self-derivation checks), so the finding is
**inheritance, not invention**. Recommended before any freeze that pins this
gate: add the half-pair HOLD, the self-derivation check, and base resolution.

## 7. Receipts

All commands `cwd = /home/vgpnk/Projects/shokunin/kotodama-shokunin`,
`TMPDIR=$PWD/.scratch`, 2026-10-18T17:29–17:36Z.

| id | command | observed |
|---|---|---|
| R-1 | `sha256sum .scratch/r25-d11/argot-replay.py tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml` | `4934f17d…` / `d9e4e8f4…` / `e7ecd204…` |
| R-2 | `python3 .scratch/r25-d15/adv.py` | 13 rows; baseline 14 findings 0 DERIV; A1 re-serialized 22 findings 8 `DERIV-REPLAY` |
| R-3 | `python3 .scratch/r25-d15/adv-d11.py` | 7 rows; V1 0 viol; V2 1 viol; V3 10 viol; V4 1 viol; V6 1 viol; gate ids on each: no DERIV |
| R-4 | `python3 .scratch/r25-d15/adv-d11-decisive.py` | W2 harness `KeyError: 'b'` exit 1; W4 leak `(<class 'str'>, <class 'object'>)`; W5 ids `[]`; W7 baseline 0 viol |
| R-5 | `python3 .scratch/r25-d11/argot-replay.py .scratch/r25-d15/w6c-fabricated.yml` | `violations 0`, exit 0 |
| R-6 | `python3 .scratch/r25-d11/argot-replay.py .scratch/r25-d15/w3-note-collision.yml` | `violations 3`, exit 0 |
| R-7 | `python3 -c "import re;print(re.fullmatch(r'^(?P<a>.+)\+(?P<b>.+)$','tum+hai\n'), re.match(r'^(?P<a>.+)\+(?P<b>.+)$','tum+hai\n'))"` | `None <re.Match span=(0, 7)>` |
| R-8 | catastrophic pattern under `re.match` with a 3 s SIGALRM deadline | `HUNG (>3 s)`; gate `_catastrophic_pattern` → `True`, budget `0.5` |
| R-9 | `python3 tools/gates/lexicon-coverage-audit.py .scratch/r25-d15/b2p-reproducing-borrowed-base.yml` | exit 0 (the `native-only` leg does not fire); control with native base also exit 0 |
| R-10 | `python3 -c` sweep for `D4L-ARGOT-DERIV` under `tools/`, `examples/` | at 17:32Z: 0 files (superseded — the delivered argot gate emits it from 14:33) |
| R-11 | `python3 .scratch/r25-d11/argot-replay.py` on `f5-id.yml`; grep stdout for the id | `VIOL L-46 \| mesor \| …`; id absent |
| R-12 | `sha256sum tools/gates/argot-derivation-gate.py` | `07db6e9b4e01539e1dbb8af9e51eada6fe37784145915a0387f48f2ecd99f8fe` |
| R-13 | `python3 tools/gates/argot-derivation-gate.py --selftest` | `selftest: 18/18 checks passed` |
| R-14 | gate on the committed fixture | exit 1, `D4L-ARGOT-DERIV ×4` + `D4L-ARGOT-RULE ×1`, matching the `.expected` file |
| R-15 | gate on `examples/culture-d4/packet.d4.yml` | exit 0, `register_scoped=6 derived_pairs=0 violations=0` |
| R-16 | `python3 .scratch/r25-d15/adv-gate-receipt.json` producer | F1 launder (drop `derivation`): findings 5→4, no line names Q-13, `derived_pairs` 8→7; control keep: 5 findings |
| R-17 | same, F2 | self-derivation `qqq`/`reverse` and `kin`/`head2`: no line names Q-02; control `qqq` from `min`: FAIL |
| R-18 | same, F3/F4 | `derived_from: ZZZZ` and `derived_from: Q-04` → FAIL by string inequality; `derivation: NOPE` → `D4L-ARGOT-RULE ×5` |
| R-19 | harness on `v2a`/`v2b`/`v2c` (name+stem, name-only, stem-only rewrites) | each `viol 1`; the line names `expected='tumhai'` — the duplicated column, not a resolved base, is what caught it |
| R-20 | harness on `v2d`/`v2e` (`expected` removed; untouched / name+stem rewritten) | both `viol 0` — with `expected` gone the consistent fabrication is invisible |
| R-21 | `python3 tools/gates/argot-derivation-gate.py --selftest`; on D4 source | `18/18`; exit 0, `register_scoped=6 violations=0` |
| R-22 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 19/19 legs passed` (no regression from the new gate) |

## 8. What this seat did not do

- Wrote only this file. Every fixture and receipt lives under `.scratch/r25-d15/`.
- Did not edit the D11 harness, any tool, gate, packet, component, or rounds
  8–24 artifact; did not commit or push.
- Did not adjudicate whether the leg should be promoted, nor whether the
  register half should be built — both are the parent's call, and the second
  depends on the culture-fork decision `execution-4.md` §4 names.
- Did not claim the delivered packet is wrong: V-0 confirms it replays clean.
