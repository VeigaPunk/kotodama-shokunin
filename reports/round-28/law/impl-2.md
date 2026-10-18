# R28-D06 — the replay leg, resolution by resolution

- **Seat:** R28-D06 (D axis, law-replay implementation 2 of 8). Round 28, loop 3
  build 4 of 4, claim **D** `register-law-replay`. Integrator: `impl-1.md`
  (R28-D05).
- **Date:** 2026-10-18. Baseline `6c0ac448…`; lane HEAD `69cecbc`.
- **Artifact:** `tools/gates/register-law-gate.py`
  (sha256 `bbad35784bfb463d41912908748ebb711f72109d811d0dc8f0110657e3b4c026`).
- **Write scope:** this file only; scratch under `.scratch/r28-d/`.
- **Canon:** NON-CANON engineering evidence.

## 1. What the leg reads

The packet's `register_law` block (the five speech-act rows) and, as its ground
truth, the packet's **other** blocks: every list block whose rows are mappings
carrying an `id` (179 ids on the delivered packet), the `registers` block's
declared names, and the contract's `record_fields`.

It resolves **eight** things. `reports/round-28/law/design.md` §2 names six
classes and `vocab.md` fixes the vocabularies; this implementation carries those
plus the two structural resolutions (`ROW`, `KIND`) the design's own reader and
the round runner both perform, so a single invocation covers every reading.

| # | resolution | ground truth | class | severity |
|---|---|---|---|---|
| 1 | `speaker` / `holder` agent ids | every id a packet record carries | `D4L-LAW-SPEAKER` | FAIL |
| 2 | `force` | the declared class set + modifier set, or the literal `none` | `D4L-LAW-FORCE` | FAIL |
| 3 | `consequence` of a **binding** act | delivered roll/rank machinery stems | `D4L-LAW-CONSEQUENCE` | FAIL |
| 4 | `register` | the `registers` block's ids, `register` values and titles | `D4L-LAW-REGISTER` | FAIL |
| 5 | `axis` | the spine's axis vocabulary | `D4L-LAW-AXIS` | FAIL |
| 6 | `kind` | the declared rule-kind set | `D4L-LAW-KIND` | HOLD |
| 7 | `design_row` tokens | every id a packet record carries | `D4L-LAW-DANGLING` | HOLD |
| 8 | declared row presence (`RGL-01..05`) | the block's own row ids | `D4L-LAW-ROW` | HOLD |

## 2. The three clauses the claim names

The claim's `after_required` reads: "speaker classes resolve against delivered
records, forces against a declared vocabulary, consequences against the roll/rank
machinery". Those are resolutions 1, 2 and 3, and each is measured firing:

```
$ export TMPDIR=$PWD/.scratch
$ python3 - <<'PY'   # each tamper lands on a LAW row, not a lexicon row
… register     added_classes=['D4L-LAW-REGISTER'] lines=1
… axis         added_classes=['D4L-LAW-AXIS']     lines=1
… kind         added_classes=['D4L-LAW-KIND']     lines=1
… design_row   added_classes=[]                   lines=1   (same class, new line)
PY
```

**Resolution 1 — speaker.** `RGL-01`'s `speaker` carries
`mold-keeper (OR-02, component-only)`. Round 27 measured `OR-02` as **absent from
the packet** (RL-4), so this resolution could not have been written honestly then:
it would have reported a defect the packet's own blindness caused. The RL-4 fix
(§`impl-4.md`) makes `OR-02` a packet record, so the resolution now reads true —
`speaker_tokens=3`, `speaker_failures=0` on the clean packet — and fires on
`(ZZ-99)`. **That coupling is the reason the two halves of this claim land
together rather than separately.**

**Resolution 2 — force.** The packet declares no `force` vocabulary (round-28
audit X59-F5 measured `force_vocabulary=0`), so a leg resolving `force` against
the packet alone could not fire. The vocabulary is therefore the gate's own
declared **closed** set, quoted from `design.md` §3 and `rules.md` RU-L2, and
printed in the finding text so a reader can disagree with it:

```
FINDING D4L-LAW-FORCE: FAIL — RGL-01 force 'no-such-force' names no declared
illocutionary class or modifier; the declared set is assertive/directive/commissive/
expressive/declarative plus binding/refused/not-rollable/none/attested/witnessed/
naming/constraint (reports/round-27/law/design.md section 3; rules.md RU-L2)
```

**Resolution 3 — consequence.** A **binding** act's consequence must name
delivered roll/rank machinery. A row declaring `force: none` is by its own terms
not a speech act (`RGL-04`'s sound-channel constraint, `RGL-05`'s dating
constraint), so its `consequence` is a constraint statement and is **not**
resolved — otherwise the leg would report two findings that are not defects. That
scoping is the design's (`design.md` §1 resolution 3) and it is what makes the
clean packet's consequence count 0 rather than 2.

## 3. The `none` resolution, and a hole the selftest found

The literal `none` is a declared non-force. The first implementation tested it by
token membership — `"none" in tokens and not classes` — and its own selftest
caught that this admits a value which smuggles `none` alongside garbage:

```
'none but wibble'   -> []        # WRONG: read as the declared non-force
```

The rule was tightened to require a **separator** after the head word, matching
the landed rows' actual shape (`none — a sound-channel constraint, not a speech
act`):

```
NON_FORCE_RE = ^\s*none\s*(?:[—–\-:,]|$)
```

Re-measured:

```
'none but wibble'                                      -> ['D4L-LAW-FORCE']   # fires
'none'                                                 -> []
'none — a sound-channel constraint, not a speech act'  -> []
'none — a dating constraint, not a speech act'         -> []
```

**This is recorded because it is a real hole that a control found**, not because
it is tidy: without the separator requirement a tamper could append an unknown
force to `none` and walk through the leg unremarked.

## 4. Exact-token resolution, never substring

The design measured that a substring matcher **inverts** `RGL-02`'s exclusion:

```
'master'   in 'furnace-master'  -> True     # the office RGL-02 forbids
'delegate' in 'league delegate' -> True
```

A substring reading of `RGL-02`'s `speaker: "stamp-holder only — no master, no
delegate"` would grant exactly the offices the row forbids. This implementation
resolves agent ids by the `Name (ID)` token shape only, never by substring, and
reads `RGL-02`'s polarity from its `kind: exclusion` rather than inferring it from
the prose. That is `design.md`'s `LD-6`, honoured.

## 5. What the leg does not resolve (declared)

| id | not resolved | consequence |
|---|---|---|
| LD-1 | cross-row delegation (`"any speaker admitted by RGL-01 or RGL-03"`) | a broken delegation is invisible |
| LD-3 | the `act` text (free prose) | an act row describing nothing is invisible |
| LD-4 | `consequence` is a **stem** match | a consequence saying "roll" while meaning nothing passes |
| LD-5 | `CONSEQUENCE`/`DANGLING` are **saturated** on the clean packet | their further tampers add a *line*, not a *class* — which is why the runner grades lines |
| LD-6 | `holder`'s `none —` polarity is not checked as a negation | ids only |

## 6. Exit codes and output shape

Matches the family's convention exactly (the argot gate's):

```
0  clean — no findings printed
1  one or more findings printed
2  could-not-evaluate — unreadable, not UTF-8, or outside the declared YAML subset;
   a single `FINDING D4L-LAW-DATA` line is printed
```

Output: one `FINDING <id>: <LEVEL> — <message>` per line, then one `coverage:`
line (with the counts a reader needs to check the domain) and one `dependency:`
line naming the reader's live digest.

## 7. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 tools/gates/register-law-gate.py --selftest
python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
python3 -c "import runpy;m=runpy.run_path('tools/gates/register-law-gate.py');print(sorted(m['DECLARED_FORCE_CLASSES']), sorted(m['DECLARED_FORCE_MODIFIERS']))"
python3 -c "import runpy;m=runpy.run_path('tools/gates/register-law-gate.py');n=m['load_naming']();print([i['id'] for i in m['evaluate_text'](m['_packet'](force='none but wibble'),n)[1]])"
sha256sum tools/gates/register-law-gate.py
```
