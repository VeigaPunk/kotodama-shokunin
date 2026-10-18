# R28-D02 — the law's vocabulary: what each clause may say, and where the words come from

- **Seat:** R28-D02 (D axis, law-replay design 2 of 4), round 28, loop 3 build 4
  of 4. Claim **D** `register-law-replay` (`reports/round-28/claims.json`).
- **Date:** 2026-10-18 (measurements 20:0x–20:15Z). Baseline revision
  `69cecbc7dcf575a29f29660ecac470e05260fd86`; lane HEAD `69cecbc`.
- **Design authority:** `reports/round-28/law/design.md` (this round, seat
  R28-D01) — this file supplies the vocabularies its §1 resolves against.
- **Write scope:** this file only; scratch under `.scratch/r28-law/`.
  `export TMPDIR=$PWD/.scratch` preceded every scratch-writing command. No
  component, packet, tool, gate, fixture, pin file, or filed 8–27 byte written;
  no commit, no push.
- **Canon:** NON-CANON engineering rules. No real language, institution or
  script is described, cited or approximated.

**Verdict in one line.** Three of the law's four fields have a **declared**
vocabulary the packet itself supplies — `speaker` resolves against **8 offices**
and **3 institutions**, `register` against **2 register names**, `axis` against
**3 axis values** — but `force` has **none**: it is free prose in all five rows,
and the delivered `force` values mix an illocutionary class, a modifier and a
prose explanation in one string. §4 fixes the vocabulary and §5 measures what
that costs.

## 1. The five fields, and which have a vocabulary at all

| field | vocabulary? | supplied by | rows that exercise it |
|---|---|---|---|
| `speaker`, `holder` | **yes** — offices + institutions + record ids | `rank_rules`, `costumes`, `literacy_institutions` | 5 of 5 |
| `register` | **yes** — 2 names | `registers` (`register` field) | 5 of 5 |
| `axis` | **yes** — 3 values in use | the packet's own spine | 5 of 5 |
| `kind` | **yes** — 5 values, declared in the contract, checked by nothing | `contract.record_fields.register_law` | 5 of 5 |
| **`force`** | **no — free prose** | nothing | 5 of 5 |

The table's last row is the round's vocabulary finding, and §4 is about it.

## 2. `speaker` / `holder` — the office and institution vocabulary

Measured from the delivered packet (`sha256 543d68a8…`, 20:15Z 2026-10-18):

**The eight offices**, with the rows that supply each:

```
broker               <- RK-04, GAR-06
charcoal burner      <- GAR-05
furnace-master       <- RK-01, RK-02, RK-03, RK-04, GAR-01..04
kiln tender          <- GAR-05
league delegate      <- RK-02, GAR-03
market-goer          <- RK-04, GAR-06
smith                <- RK-01, GAR-01, GAR-02
stamp-holder         <- RK-03, GAR-04
```

**The three institutions** (the `literacy_institutions` block, which the RL-4
fix landed):

```
LI-01  'the stamp-house'
LI-02  "the mold-keeper's license"
LI-03  'the furnace roll'
```

**The rite holders**, which are a fourth, looser surface:

```
RIT-01 holder='the furnace-master'    participants='the town'
RIT-02 holder='the smith at the quench' participants='the forge crew'
RIT-03 holder='the stamp-house'       participants='the town and the council'
RIT-04 holder='the shade-keeper'      participants='the lineage'
```

**Three surfaces, three shapes, and the law's `speaker` field matches none of
them exactly.** The law says `"stamp-holder, furnace-master (RK-03), mold-keeper
(OR-02, component-only)"` — a comma-separated list where each item is an office
name, optionally followed by a parenthetical id, optionally followed by a prose
qualifier. `RIT-02`'s `'the smith at the quench'` shows the packet's own prose
convention is a **definite article plus a qualifying phrase**; the law's is a
**bare hyphenated office**. The two conventions do not meet.

**And `mold-keeper` is in none of the three surfaces as an office**, measured
after the RL-4 fix:

```
mold-keeper in offices? False
mold-keeper in literacy_institutions (substring)? True — "the mold-keeper's license"
mold-keeper (OR-02) resolves as a RECORD ID? True
```

It survives as a substring of an institution's *name* and as the record id
`OR-02`. Both are weak resolutions and the leg takes the id (§`design.md` §3.2,
`LD-2`).

### 2.1 The forbidden-office trap, restated as a vocabulary rule

`RGL-02`'s speaker names offices in order to **forbid** them:

```
speaker: "stamp-holder only — no master, no delegate"
```

`master` and `delegate` are substrings of two permitted offices:

```
'master'   in 'furnace-master'  → True
'delegate' in 'league delegate' → True
```

So the vocabulary rule is: **resolution is by exact token against the eight
offices and the three institution names; a substring match is not a resolution
and inverts an exclusion.** Measured consequence (`design.md` §1):

| row | exact-token | substring |
|---|---|---|
| `RGL-01` | `furnace-master`, `stamp-holder` | `furnace-master`, `stamp-holder` |
| `RGL-02` | `stamp-holder` | **`furnace-master`, `league delegate`**, `stamp-holder` |
| `RGL-03` | `broker`, `market-goer` | `broker`, `market-goer` |

**The polarity is carried by `kind`, not by the text.** `RGL-02`'s
`kind: "exclusion"` is what tells a reader the named offices are forbidden; the
words `only` and `no` are the human-readable restatement of it. A leg that
inferred polarity from `only`/`no` would be parsing English, and this design does
not.

## 3. `register`, `axis`, `kind` — the three short vocabularies

### 3.1 `register` — 2 names, and the name/id confusion is a measured defect

```
registers block:
  id=QREG-01  register='plain'  class='unmarked'
  id=QREG-02  register='stamp'  class='marked'
  id=QREG-03  register='stamp'  class='marked'
  id=QREG-04  register='stamp'  class='marked'
```

**The vocabulary is the *name* set `{plain, stamp}` — not the id set
`{QREG-01..04}`.** The law row says `register: "stamp"`, which is a name. The
round-28 lane runner resolves against the **id** set and therefore fires on all
five rows and then suppresses all five through its own escape clause
(`design.md` §3.3(a)). This is a vocabulary defect in a reader, not in the law,
and it is recorded here because it is the second independent reader to get a
vocabulary wrong.

### 3.2 `axis` — 3 values in use, 1 declared-and-unused

Every `axis:` value in the packet, counted:

```
fire     89
mark     75
both      6
neutral   1
```

The law's five rows carry `mark` (×4) and `fire` (×1 — `RGL-04`, the
no-segment constraint). Both are in the packet's own set. **The vocabulary has a
gap the packet does not close**: `both` and `neutral` are used by 7 records but
declared nowhere as values, and no `contract` block names the axis set. The leg
therefore takes the **observed** set as its vocabulary, which means a new axis
value would pass silently (`LD-7`'s sibling limit).

### 3.3 `kind` — 5 values, declared in the contract, checked by nothing

```
contract.record_fields.register_law:
  [id, register, axis, kind, act, speaker, holder, force, consequence,
   design_row, evidence, follows]

the packet's own `kind` values, counted:
  admissibility 1   exclusion 1   asymmetry 1   no-segment 1   era 1
  (+ local 4, suffix 2, material 2, badge 2, compound 1, vowel-length 1,
     import 1 — these are other blocks' kinds, not the law's)
```

The five law `kind` values are exactly the five rows' `kind` values — one each.
**No reader checks the set**, so a sixth value, or a deleted `kind`, produces no
finding: round 27's control `C-2b` (`kind` stripped → no finding) is reproduced
at this stamp (§`design.md` §3.5, C-7 = 0).

## 4. `force` — the field with no vocabulary, and the one this seat fixes

### 4.1 What the delivered rows actually carry

```
RGL-01: "directive-binding for the charge; declarative-naming for the lot's name"
RGL-02: 'commissive-binding refused'
RGL-03: 'directive-binding, not-rollable'
RGL-04: 'none — a sound-channel constraint, not a speech act'
RGL-05: 'none — a dating constraint, not a speech act'
```

**Five rows, five shapes, one field.** The values mix three things:

| component | example | kind of thing |
|---|---|---|
| an illocutionary class | `directive`, `commissive`, `declarative` | the Searle class the act belongs to |
| a **modifier** | `binding`, `refused`, `not-rollable` | how the class is qualified in this register |
| a **prose explanation** | `for the charge`, `— a sound-channel constraint, not a speech act` | a gloss for a human reader |

`RGL-01` carries **two** class/modifier pairs separated by a semicolon, because
one row covers two acts (the round-27 design's `QREG-05` charge and `QREG-07`
lot-naming). `RGL-04` and `RGL-05` carry the literal `none` followed by a prose
clause that itself contains the words "not a speech act" — so a naive
class-matcher looking for `declarative` finds nothing, and a naive matcher
looking for the token `none` finds it in a sentence, not as a value.

### 4.2 The declared vocabulary

**Illocutionary classes** (Searle's five, the standard closed set for a speech-act
system):

```
assertive | directive | commissive | expressive | declarative
```

**Modifiers** — the qualifiers the delivered rows use, fixed as a declared set
rather than left as free text:

```
binding | refused | not-rollable | none | attested | witnessed | naming | constraint
```

**The grammar of a `force` value**, stated so a writer and a reader agree:

```
force := NONE
       | CLASS-MODIFIER [; CLASS-MODIFIER]*
NONE  := "none"
```

where `CLASS` is one of the five and `MODIFIER` is one of the eight, joined by a
hyphen. The delivered rows conform to this grammar except in one respect:
**every row appends a prose gloss**, which the grammar has no slot for.

### 4.3 The fix, and what it costs

| option | what changes | cost |
|---|---|---|
| **F-1** — keep `force` as prose, and have the leg check only the **class** substring | no packet change | the leg cannot detect a bogus **modifier**; `commissive-binding` and `commissive-refused` both pass |
| **F-2** — split the field: `force_class` + `force_modifier` + keep the prose in `law` | 5 rows × 2 new fields; `contract.record_fields.register_law` gains 2 names | a packet change; new pins (§`rl4-delta.md` §4's cascade) |
| **F-3** — keep one `force` field, declare the grammar, and **move the prose gloss out** into the existing `act`/`consequence` text | 5 rows lose their trailing gloss; no new field | a packet change, but the smaller one: no schema change, no new field name |
| **F-4** — declare the vocabulary, change nothing, and let the leg flag any row outside the grammar | no packet change | `RGL-04`/`RGL-05` and the `RGL-01` gloss are flagged **today** — the leg's clean baseline stays at the 6 findings `design.md` §3.1 measures |

**This design takes F-4**, and the reason is the round's own discipline: the
vocabulary is the deliverable, and the packet change it would take to *conform*
the rows is priced in `rl4-delta.md` §4 alongside the RL-4 cascade. F-4 gives
the leg a checkable predicate **today** and reports the three non-conforming rows
as findings rather than laundering them. F-1 is rejected because it cannot
detect a modifier typo, which is exactly the class `RL-1`'s control exercises.

### 4.4 The measured effect of F-4 on the clean packet

Under F-4, `D4L-LAW-FORCE` fires on the clean packet. Measured with the
reference leg's stricter reading:

```
RGL-01: force="directive-binding for the charge; declarative-naming for the lot's name"
RGL-02: force="commissive-binding refused"
RGL-03: force="directive-binding, not-rollable"
RGL-04: force="none — a sound-channel constraint, not a speech act"
RGL-05: force="none — a dating constraint, not a speech act"
```

Under the **class-substring** reading (which the reference leg implements, and
which is F-4's weaker form), all five pass, because every row contains a class or
the token `none`:

```
classes found: RGL-01 directive,declarative; RGL-02 commissive;
               RGL-03 directive; RGL-04 none; RGL-05 none
```

Under the **grammar** reading (F-4's stricter form, `force := NONE | CLASS-MODIFIER`),
three rows fail — `RGL-01` (two pairs plus a gloss), `RGL-04`, `RGL-05` (prose
after `none`). **The reference leg implements the class-substring reading**, so
its clean baseline carries no `D4L-LAW-FORCE` finding and control C-1 adds
exactly one (`design.md` §3.4). A leg implementing the strict grammar would carry
three findings on clean and C-1 would add a fourth. Both readings are declared;
the reference leg's is the one the round's numbers are quoted against.

## 5. `consequence` — a stem vocabulary, and its two weak members

The leg resolves `consequence` against a **stem** list, because a consequence is
a claim that something happens to a record and the packet supplies the machinery
by name:

```
roll | rk- | rank | tally | rite | rit- | entry | written | record | void |
binds | binding | no entry
```

Measured against the five delivered rows:

| row | stems found | reading |
|---|---|---|
| `RGL-01` | `roll`, `tally`, `written`, `binds` | ✓ names machinery |
| `RGL-02` | `roll`, `rk-`, `entry`, `void`, `binding`, `no entry` | ✓ names machinery |
| `RGL-03` | `roll`, `rite`, `record`, `binds` | ✓ names machinery |
| `RGL-04` | **none** | ✗ a sound-channel constraint names no record |
| `RGL-05` | **none** | ✗ a dating constraint names no record |

**Two of the eleven stems are load-bearing and two are weak, and the difference
matters.**

- **Load-bearing and resolvable**: `roll` — the packet carries `LI-03 'the
  furnace roll'` and `ER-03`'s seam text "the furnace roll opened and the council
  of furnace-masters seated". A consequence naming the roll names a delivered
  institution.
- **Load-bearing and *un*resolvable**: `tally` — the packet mentions `tally` 4
  times and **carries no tally record**; `stamp-roll` likewise, 3 mentions and no
  record. So `RGL-01`'s "the lot's name is written on the ingot's tally face"
  names machinery that exists only in prose.
- **Weak**: `written`, `binds`, `binding`, `record`, `entry`, `void` are verbs
  and adjectives. A consequence containing the word "written" passes whether or
  not anything is written anywhere.

Measured, the roll chain resolves unevenly:

```
'furnace roll'  prose_hits=6   named_record=LI-03   present_as_record=True
'council'       prose_hits=11  named_record=ER-03   present_as_record=True
'stamp-roll'    prose_hits=3   named_record=None    present_as_record=False
'tally'         prose_hits=4   named_record=None    present_as_record=False
```

**The consequence vocabulary is therefore two-tiered**: the *institution* tier
(`roll`, `council`) resolves to a record, and the *record-shape* tier (`tally`,
`stamp-roll`) does not, because no record for either exists. This design keeps
both tiers in the stem list (a consequence naming a tally is not wrong; the
packet simply has no tally record to point at) and records the gap as `LD-4`.

## 6. The full vocabulary, in one place

```
speaker, holder  := ( OFFICE | INSTITUTION | RECORD-ID )  [ , ... ]
                    OFFICE      := one of the 8 the packet supplies
                    INSTITUTION := one of the 3 literacy_institutions names
                    RECORD-ID   := the parenthetical (XX-99) shape
                    resolution is by EXACT TOKEN, never substring

register         := plain | stamp                    (the registers block's NAMES)

axis             := mark | fire | both | neutral     (the packet's OBSERVED set —
                                                      `both`/`neutral` are used and
                                                      declared nowhere)

kind             := admissibility | exclusion | asymmetry | no-segment | era
                    (declared in contract.record_fields.register_law;
                     checked by NO reader)

force            := none
                  | (assertive|directive|commissive|expressive|declarative)
                    -(binding|refused|not-rollable|none|attested|witnessed|naming|constraint)
                    [ ; ... ]
                    (the CLASS/MODIFIER vocabulary is DECLARED BY THIS FILE,
                     not by the packet; the delivered rows conform to it only
                     after their prose gloss is removed — §4.4)

consequence      := text containing at least one stem from
                    {roll, rk-, rank, tally, rite, rit-, entry, written,
                     record, void, binds, binding, no entry}
                    (two-tiered: `roll`/`council` resolve to a record,
                     `tally`/`stamp-roll` resolve to nothing — §5)
```

## 7. Named limits

| id | limit | measured |
|---|---|---|
| **LV-1** | `force` has **no packet-declared vocabulary**: the class/modifier set is this file's, not the packet's | §4 |
| **LV-2** | the delivered `force` values append a prose gloss the declared grammar has no slot for; three of five rows are non-conforming under the strict reading | §4.4 |
| **LV-3** | `axis`'s vocabulary is **observed**, not declared: `both` and `neutral` are used by 7 records and named nowhere | §3.2 |
| **LV-4** | `kind`'s five values are declared in the contract and checked by no reader | §3.3 |
| **LV-5** | the `consequence` stems `written`, `binds`, `binding`, `record`, `entry`, `void` are **verbs**, not machinery: they pass trivially | §5 |
| **LV-6** | `tally` and `stamp-roll` are named in the law and carry **no record** anywhere in the packet | §5 |
| **LV-7** | `speaker`'s three surfaces (offices, institutions, rite holders) have **three different textual conventions**; the law's matches none exactly | §2 |
| **LV-8** | the vocabulary is **this file's**, so a reader who takes another set gets another green: two independent readers already disagree (`design.md` §3.3) | §3.1, §4 |

## 8. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
P=examples/culture-d4/packet.d4.yml
python3 - <<'PY'   # the office/institution vocabulary
import runpy
m=runpy.run_path('tools/gates/naming-collision-gate.py'); p=m['load_yaml'](open('examples/culture-d4/packet.d4.yml').read())
off=set()
for r in p.get('rank_rules',[]): off.update(r.get('wearer_ranks') or [])
for c in p.get('costumes',[]): off.update(c.get('wearer_ranks') or [])
print(sorted(off)); print([r.get('name') for r in p.get('literacy_institutions',[])])
PY
grep -n "^    force:" $P                     # the 5 delivered force values
grep -c "^      - \"stamp\"" $P 2>/dev/null || true
python3 -c "
import re;t=open('examples/culture-d4/packet.d4.yml').read()
import collections;print(collections.Counter(re.findall(r'^\s*axis:\s*\"?([a-z]+)\"?\s*\$',t,re.M)))"
grep -o '"\?register: \"[a-z]*"' $P | sort | uniq -c
```

### Digests at measurement

| artifact | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` | `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f` |
| `examples/culture-d4/components/13-register-law.yml` | `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7` |
| `examples/culture-d4/components/03-orthography.yml` | `0f2ff45439fd7db3e9014bd1012bd917e42d042f457b8cef2bed2c9a791d4e1b` |
| `examples/culture-d4/components/09-costumes.yml` | `f61cc6845518d44f50e5179339a1a2fda2c5290efb52d6badb28cbec87768c23` |
| `.scratch/r28-law/replay-probe.py` | see `.scratch/r28-law/replay-probe.json` |

All measurements read at 20:15Z on 2026-10-18 against the packet digest above.
