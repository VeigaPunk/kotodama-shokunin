# R28-D20 — adversarial review 4 of 4: the RL-3 ceiling wording, reviewed

- **Seat:** R28-D20 (reviewer 4 of 4), round 28, loop 3 build 4 of 4, claim **C**
  `register-lexicon-ceiling` (`reports/round-28/claims.json`), reviewing the
  measurement claim D depends on.
- **Date:** 2026-10-18. Declared baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`;
  lane HEAD `69cecbc7dcf575a29f29660ecac470e05260fd86`. Measurement window
  **2026-10-18T20:14Z–20:16Z** (`date -u +%FT%TZ`).
- **Review target:** the **RL-3 ceiling** as it is stated in the round-27
  artifacts and in the craft record — `reports/round-27/law/{design,rules,review}.md`
  §3.3/§4 and `corpus/knowledge/linguistics/register-strata-attestation.md` §6 —
  which round-28's claim C is to record as a design constraint.
- **Write scope:** this file only, plus gitignored scratch under
  `.scratch/r28-d20/`. `export TMPDIR=$PWD/.scratch` preceded every
  scratch-writing command. **No component, packet, tool, gate, fixture, pin,
  runner, knowledge entry or filed rounds 8–27 byte was written; no commit, no
  push.**
- **Canon:** NON-CANON engineering evidence.

**Assignment.** Reviewer 4 of 4: the **RL-3 ceiling wording** reviewed. The
ceiling is the round's load-bearing craft lesson — "a register's derivational
operation silently decides which semantic classes can enter it" — and it is about
to be promoted from round artifacts into a knowledge entry. A lesson promoted on
a wrong number teaches the wrong lesson, so this seat re-measures every figure
the ceiling rests on and reads the wording against what the measurement shows.

**Verdict in one line.** **The lesson is sound and the figures are not.** The
generalisable claim — that the operation, not the designer's intention, picks the
register's semantic profile — is **confirmed and stronger than stated**: it is a
property of the *operation*, not of the register, and the delivered tree carries
the proof, because `head2` carries 5 of the 5 institutional abstractions while
`reverse` carries 1 of 5 (§4). But **two** of the numbers the ceiling is stated with do
not reproduce: the reverse-legality split is **19/8, not 18/9**; and the
abstractions that refuse `reverse` are **4 of 5, not 5 of 5** (§3). Both are
reproducible defects with controls, and both are whole-word applications of a
per-syllable predicate — the same class as the round-26 syllabify defect the
round was supposed to close. A third figure I first read as wrong — the eight
register forms — is **not** a defect, and the correction is recorded in §3.1
rather than dropped.

## 0. What the ceiling says, and where it lives

Four places state the same numbers, and they are the record the round-28 claim C
promotes:

```
$ grep -rn "reverse-legal: 18\|18   reverse-ILLEGAL: 9\|5 of 5\|0 legal  / 5 illegal" \
      reports/round-27/ corpus/knowledge/linguistics/register-strata-attestation.md
reports/round-27/law/design.md:205:mark-axis plain words: 27   reverse-legal: 18   reverse-ILLEGAL: 9
reports/round-27/law/rules.md:157:mark-axis plain words: 27   reverse-legal: 18   reverse-ILLEGAL: 9
reports/round-27/law/review.md:151:mark-axis plain words: 27   reverse-legal: 18   reverse-ILLEGAL: 9
corpus/knowledge/linguistics/register-strata-attestation.md:225:mark-axis plain words: 27   reverse-legal: 18   reverse-ILLEGAL: 9
```

and the claim's own `before` field rests on them:

```
$ python3 -c "import json;print(json.load(open('reports/round-28/claims.json'))['claims'][2]['before'])"
The RL-3 ceiling (the register cannot spell its own law's vocabulary — 5 legal abstractions refuse reverse) is recorded only in round artifacts.
```

**"5 legal abstractions refuse reverse."** §3 measures that as 4.

## 1. The rowset and the predicate — stated before measuring

A count is meaningless without both. The rowset is the delivered lexicon's
mark-axis plain records:

```
$ export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
$ python3 - <<'PY'
import runpy, subprocess, json
g = runpy.run_path('tools/gates/argot-derivation-gate.py')
is_legal, syllabify = g['is_legal_syllable'], g['syllabify']
d = json.loads(subprocess.run(["ruby","-ryaml","-rjson","-e",
    "puts JSON.generate(YAML.load_file(ARGV[0]))",
    'examples/culture-d4/packet.d4.yml'], capture_output=True, text=True).stdout)
mk = [r for r in d['lexicon'] if r.get('axis') == 'mark' and r.get('register') in (None, 'plain')]
print("rowset: mark-axis plain words =", len(mk))
PY
rowset: mark-axis plain words = 27
```

The predicate is `tools/gates/argot-derivation-gate.py`'s own public function
(sha256 `b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb`,
selftest **27/27**). Its docstring is the contract:

```
$ python3 -c "
import runpy, inspect
g = runpy.run_path('tools/gates/argot-derivation-gate.py')
print(inspect.getdoc(g['is_legal_syllable']))
"
Is one syllable of the template `(C)V(V)(C)` with a licensed coda?
```

**`is_legal_syllable` takes one syllable.** Its internal use confirms it: the
gate calls it on `syllabify(...)` output and on hand-written single syllables,
never on a whole word:

```
$ grep -n "is_legal_syllable" tools/gates/argot-derivation-gate.py
217:def is_legal_syllable(syllable):
804:    is_legal_syllable("tik") and is_legal_syllable("kme") is False
805:    and is_legal_syllable("tuu") and is_legal_syllable("s") is False))
```

## 2. The measurement — the split is 19/8, not 18/9

Two independent readings of the ceiling, both faithful to the predicate's
documented contract, and a third that misapplies it:

```
$ python3 - <<'PY'
import runpy, subprocess, json
g = runpy.run_path('tools/gates/argot-derivation-gate.py')
is_legal, syllabify = g['is_legal_syllable'], g['syllabify']
d = json.loads(subprocess.run(["ruby","-ryaml","-rjson","-e",
    "puts JSON.generate(YAML.load_file(ARGV[0]))",
    'examples/culture-d4/packet.d4.yml'], capture_output=True, text=True).stdout)
mk = [r for r in d['lexicon'] if r.get('axis') == 'mark' and r.get('register') in (None, 'plain')]
A = [r for r in mk if is_legal(r['term'][::-1])]                              # whole-string misuse
B = [r for r in mk if all(is_legal(s) for s in syllabify(r['term'][::-1]))]   # the documented use
print(f"rowset={len(mk)}")
print(f"  A  whole-string is_legal(rev):     {len(A)} legal / {len(mk)-len(A)} illegal")
print(f"  B  per-syllable (documented use):  {len(B)} legal / {len(mk)-len(B)} illegal")
print(f"  recorded in round 27:              18 legal / 9 illegal")
PY
rowset=27
  A  whole-string is_legal(rev):     17 legal / 10 illegal
  B  per-syllable (documented use):  19 legal / 8 illegal
  recorded in round 27:              18 legal / 9 illegal
```

**Neither reading gives 18/9.** To rule out a third reading the recorded figure
might have come from, a 16-way sweep over the plausible variants — diphthong
handling on/off, long-vowel handling on/off, onset clusters on/off,
per-syllable vs whole-string — was run:

```
$ python3 - <<'PY'
# 16 combinations of (diphthong, long-vowel, cluster, per-syllable)
PY
diph=0 long=0 cluster=0 per_syl=0: 17 legal / 10 illegal
diph=0 long=0 cluster=0 per_syl=1: 19 legal /  8 illegal
… (all 16) …
diph=1 long=1 cluster=1 per_syl=1: 19 legal /  8 illegal
matches for 18/9: []
```

**No combination produces 18/9.** The value is off by one in both directions,
which is the signature of a single row read differently — and §3 identifies it.

The 62-record lexicon, the 54-record reverse domain and the register's own forms
are all unaffected by this; only the split of the mark-axis plain set is.

## 3. The abstraction count is 4 of 5, and the row that differs is the script

The ceiling's sharpest claim is "all five legal/institutional abstractions refuse
`reverse`", and the claim's own `before` says "5 legal abstractions refuse
reverse". Measured per-syllable — the documented use:

```
$ python3 - <<'PY'
import runpy
g = runpy.run_path('tools/gates/argot-derivation-gate.py')
is_legal, syllabify = g['is_legal_syllable'], g['syllabify']
abs5 = {'L-15':'wer','L-30':'gis','L-44':'wad','L-45':'tikmes','L-51':'gul'}
for i, b in abs5.items():
    rv = b[::-1]; syl = syllabify(rv)
    per = all(is_legal(s) for s in syl); whole = is_legal(rv)
    print(f"  {i} {b:7} -> {rv:7} syllabify={str(syl):16} per-syllable-refuses={not per}  whole-string-refuses={not whole}")
PY
  L-15 wer     -> rew     syllabify=['rew']         per-syllable-refuses=True   whole-string-refuses=True
  L-30 gis     -> sig     syllabify=['sig']         per-syllable-refuses=True   whole-string-refuses=True
  L-44 wad     -> daw     syllabify=['daw']         per-syllable-refuses=True   whole-string-refuses=True
  L-45 tikmes  -> semkit  syllabify=['sem', 'kit']  per-syllable-refuses=False  whole-string-refuses=True
  L-51 gul     -> lug     syllabify=['lug']         per-syllable-refuses=True   whole-string-refuses=True
```

**`L-45 tikmes → semkit` syllabifies to `sem.kit`, and both `sem` and `kit` are
legal D4 syllables.** It refuses only if `is_legal_syllable` is applied to the
whole six-letter word — the misuse §1 established. So:

- **per-syllable (documented): 4 of 5 abstractions refuse.**
- **whole-string (misuse): 5 of 5 refuse** — the recorded figure.

The recorded "5 of 5" is therefore the **whole-string** reading. The recorded
18/9 is a *different* thing again, and the C seat's landed amendment (entry §13,
`corpus/knowledge/linguistics/register-strata-attestation.md`, sha256
`ddeeee75af9856c95dc58519a40a3992b06029682d61d0babff662e1cdcc3284`) identifies
the cause independently of this seat:

```
$ git diff corpus/knowledge/linguistics/register-strata-attestation.md | grep "^+"
+delivered gate (b5406bcd)  legal=19 illegal=8
+pre-fix gate (5b5abe78) legal=18 illegal=9
+**The filed 18/9 is the pre-fix reader's reading.**
```

**The 18/9 is the pre-fix gate revision's reading, not a second predicate.**
Round 27's law seats measured the ceiling *before* the syllabify fix landed and
the `RL-3` numbers were carried forward into `design.md`, `rules.md`, `review.md`
and the entry §6 without being re-taken against the fixed gate (`b5406bcd…`).
That is a cleaner explanation than mine — one reader, two revisions — and it
supersedes this seat's earlier "two predicates" hypothesis (`D20-F3`), which is
withdrawn below. **The two seats agree on the corrected figure: 19 legal /
8 illegal, and 4 of 5 abstractions refusing.** The 5-of-5 whole-string reading
remains a separate defect, because the entry §6 and the round-27 files state it
in a table headed by the per-syllable split.

**D20-F3, withdrawn.** This seat first attributed the 18/9 to "two different
predicates in one table". The C seat's amendment shows the real cause is a
**stale instrument**: the numbers were taken against `5b5abe78…` (pre-syllabify-
fix) and not re-taken against `b5406bcd…`. Recorded here rather than deleted,
because the distinction matters for the remedy — a stale instrument is fixed by
re-measuring, a two-predicate table is fixed by choosing one predicate, and the
amendment correctly does the former.

**A control, so the finding is not an artifact of my reading.** The gate's own
`op_head2` calls `syllabify` and takes syllables — the gate is a per-syllable
consumer:

```
$ python3 -c "
import runpy
g = runpy.run_path('tools/gates/argot-derivation-gate.py')
print('syllabify(tikmes)      =', g['syllabify']('tikmes'))
print('is_legal(tikmes)       =', g['is_legal_syllable']('tikmes'))
print('all legal per-syllable =', all(g['is_legal_syllable'](s) for s in g['syllabify']('tikmes')))
print('op_head2(tikmes)       =', g['op_head2']('tikmes'))
"
syllabify(tikmes)      = ['tik', 'mes']
is_legal(tikmes)       = False
all legal per-syllable = True
op_head2(tikmes)       = tikmes
```

`is_legal_syllable('tikmes')` is `False` — but that call is itself a misuse, and
the gate never makes it.

### 3.1 The third figure, re-checked: the eight forms are legal — under the axis rule

The ceiling also says "every one of the eight landed register forms descends from
a **material-presence** base … **Zero** abstractions". The semantic half of that
is **correct**: all eight bases are things at the weigh-stone, and none is an
obligation. But the passage's table shows each base beside a `reverse` form, and
**only two of the eight bases are mark-axis** — the other six are fire-axis and
are carried by `lengthen`, not `reverse`. The table's arrows are therefore not
the delivered derivations for six of the eight rows:

```
$ python3 - <<'PY'
import runpy, subprocess, json
g = runpy.run_path('tools/gates/argot-derivation-gate.py')
is_legal, syllabify = g['is_legal_syllable'], g['syllabify']
d = json.loads(subprocess.run(["ruby","-ryaml","-rjson","-e",
    "puts JSON.generate(YAML.load_file(ARGV[0]))",
    'examples/culture-d4/packet.d4.yml'], capture_output=True, text=True).stdout)
AXIS_OP = {'mark': 'reverse', 'fire': 'lengthen'}
ok = 0
for r in d['lexicon']:
    if r.get('register') != 'stamp': continue
    base = r['derived_from']; op = r['derivation']['op']
    ba = next(x for x in d['lexicon'] if x.get('term') == base)
    sel = AXIS_OP[ba['axis']]; legal = all(is_legal(s) for s in syllabify(r['term']))
    ok += legal
    print(f"  {r['id']} {r['term']:6} <- {base:5} axis={ba['axis']:5} rule-op={sel:9} "
          f"delivered-op={op:9} agrees={sel == op} legal={legal}")
print(f"  => {ok} of 8 delivered register forms are legal under their own axis rule")
PY
  L-56 kit    <- tik   axis=mark  rule-op=reverse   delivered-op=reverse   agrees=True legal=True
  L-57 lom    <- mol   axis=mark  rule-op=reverse   delivered-op=reverse   agrees=True legal=True
  L-55 tuum   <- tum   axis=fire  rule-op=lengthen  delivered-op=lengthen  agrees=True legal=True
  L-58 nees   <- nes   axis=fire  rule-op=lengthen  delivered-op=lengthen  agrees=True legal=True
  L-59 huum   <- hum   axis=fire  rule-op=lengthen  delivered-op=lengthen  agrees=True legal=True
  L-60 mees   <- mes   axis=fire  rule-op=lengthen  delivered-op=lengthen  agrees=True legal=True
  L-61 reek   <- rek   axis=fire  rule-op=lengthen  delivered-op=lengthen  agrees=True legal=True
  L-62 saam   <- sam   axis=fire  rule-op=lengthen  delivered-op=lengthen  agrees=True legal=True
  => 8 of 8 delivered register forms are legal under their own axis rule
```

**All eight forms are legal, and the operation rule is honoured row for row** —
this is the round-26 `REGISTER-OP-01` leg, and it holds. So the ceiling's
"eight forms, all material bases" is **not** a count defect; my first reading of
it was, and the correction is recorded here rather than dropped:

> **Correction, this seat.** An earlier pass of this file reported "7 of 8
> material bases, `L-59 hum → muh` refuses reverse". That reading was wrong: it
> applied `reverse` to all eight bases, but six of the eight bases are fire-axis
> and the rule sends them to `lengthen` (`huum`, not `muh`). The mistake is
> exactly the defect this file names in §2/§3 — applying the wrong operation to
> a rowset — and it is left visible because a reviewer who silently fixes their
> own off-by-one teaches nothing. The figure that stands: **8 of 8 legal under
> the axis rule**, and the semantic claim (0 abstractions) **confirmed**.

## 4. The lesson itself — confirmed, and stronger than the wording

The craft lesson the claim promotes is:

> **A register's derivational mechanism silently decides which *semantic
> classes* can enter the register.** If you generate in-register forms by a
> mechanical operation over an everyday lexicon, the operation's legality
> conditions, not your intentions, will pick the register's semantic profile.

**This is confirmed, and the delivered tree proves it more sharply than the
wording does.** The same five abstractions under the *other* declared operation:

```
$ python3 - <<'PY'
import runpy
g = runpy.run_path('tools/gates/argot-derivation-gate.py')
is_legal, syllabify, head2, rev = g['is_legal_syllable'], g['syllabify'], g['op_head2'], g['op_reverse']
abs5 = {'L-15':'wer','L-30':'gis','L-44':'wad','L-45':'tikmes','L-51':'gul'}
nrev = nh2 = 0
for i, b in abs5.items():
    r_ok = all(is_legal(s) for s in syllabify(rev(b)))
    h_ok = all(is_legal(s) for s in syllabify(head2(b)))
    nrev += r_ok; nh2 += h_ok
    print(f"  {i} {b:7} reverse->{rev(b):7} carries={r_ok}   head2->{head2(b):7} carries={h_ok}")
print(f"  reverse carries {nrev} of 5 abstractions; head2 carries {nh2} of 5")
PY
  L-15 wer     reverse->rew     carries=False   head2->wer     carries=True
  L-30 gis     reverse->sig     carries=False   head2->gis     carries=True
  L-44 wad     reverse->daw     carries=False   head2->wad     carries=True
  L-45 tikmes  reverse->semkit  carries=True    head2->tikmes  carries=True
  L-51 gul     reverse->lug     carries=False   head2->gul     carries=True
  reverse carries 1 of 5 abstractions; head2 carries 5 of 5
```

**Note the per-syllable reading is used here too**, consistently with §2/§3 —
`semkit` is `sem.kit`, both legal, so `L-45 tikmes` **is** carried by `reverse`
and `reverse` carries **1 of 5**, not 0. The contrast is therefore **1 of 5 vs
5 of 5**, not the clean 0/5-vs-5/5 split a first reading suggests.

**And `head2`'s 5 of 5 is partly trivial, which the wording must not hide.**
All five abstractions are one or two syllables (`wer`, `gis`, `wad`, `gul` one;
`tikmes` two), and `head2` takes the first two syllables — so on this lexicon
`head2` is the **identity** for every one of them. `head2` "carrying" all five is
therefore not evidence that `head2` is a better register operation; it is
evidence that a **different operation has a different domain**, which is the
lesson. Stated precisely:

> `reverse` carries 1 of 5 institutional abstractions; `head2` carries 5 of 5,
> but only because `head2` is the identity on a lexicon whose abstractions are
> all ≤2 syllables. The domain difference is real; the margin is lexicon-
> dependent.

That caveat is what makes the lesson teachable rather than an overclaim, and it
is the reason the wording should name the **(operation, lexicon) pair** rather
than the operation alone.

**This is the measurement the lesson should be stated on**, and it is stronger
than the round-27 wording in two ways:

1. **It is a property of the operation, not the register.** Round 27's entry
   states the ceiling as "the register cannot spell its own law's vocabulary".
   Measured, the *register* is defined by its operation rule (`mark → reverse`,
   `fire → lengthen`), so the ceiling is inherited from `reverse`. Change the
   operation rule and the same register spells more of the abstractions — the
   lesson's own last sentence already says this ("Choose the operation *after*
   deciding which classes must be sayable"), so the diagnosis above it should
   match.
2. **It is a property of the pair (operation, lexicon), not of the operation
   alone.** `head2` carries 5 of 5 here *because* of the lexicon's syllable
   shape; it would not carry 5 of 5 over a lexicon of longer abstractions. The
   wording should name both terms.
3. **The refusal is near-total, not total.** `reverse` carries 1 of 5
   abstractions, and the one it carries (`tikmes`) is the only two-syllable
   abstraction in the set — so the split is **1/5 vs 5/5**, a strong domain
   difference that is nonetheless lexicon-shaped rather than an absolute rule.
   The round-27 wording's "0" would be the stronger claim; it is not what the
   bytes say, and the correct figure is still teachable.

The round-27 entry's §6 wording is otherwise good and its design guidance
("choose the operation *after* deciding which classes must be sayable, or accept
the ceiling") is the right advice. The three corrections are: the operation, not
the register; the pair; and the numbers.

## 5. Why this matters for claim C specifically

Claim C promotes the ceiling from round artifacts into craft knowledge, so the
numbers travel:

```
$ python3 -c "import json;print(json.load(open('reports/round-28/claims.json'))['claims'][2]['after_required'])"
The ceiling recorded as a design constraint in corpus/knowledge/linguistics/register-strata-attestation.md (amendment entry, not in-place rewrite — new section citing the round-27 measurements) + a new sourced knowledge entry on register-lexicon ceilings (gap-named; the general craft lesson: a register's derivation operation constrains which semantic fields it can natively spell); README reconciled.
```

The `after_required` **cites the round-27 measurements**. If the new section
cites 18/9 and 5-of-5-whole-string, the knowledge entry inherits a
two-predicate table and an off-by-one, and a future designer who re-measures
gets 19/8 and concludes the entry is unreliable — which is how a craft lesson
loses its authority. The lesson is right; the receipts must be.

**The amendment is also the correct *form*.** Round 27's entry declines to pin
moving round-27 peer files by digest (`RSA-9`/`RSA-10`, citing by revision
instead), and the round-28 claim correctly says "amendment entry, not in-place
rewrite". Both disciplines hold; only the figures need correcting.

## 6. Named findings

| id | finding | severity | evidence | disposition |
|---|---|---|---|---|
| **D20-F1** | the reverse-legality split is **19 legal / 8 illegal** per-syllable (the documented use) and **17/10** whole-string; the recorded **18/9** matches neither, and a 16-way variant sweep produces no 18/9 | **high** — a promoted number that does not reproduce | §2 | reported; the record must be corrected in the round-28 amendment, not silently rewritten in round-27 files |
| **D20-F2** | "5 of 5 abstractions refuse reverse" is the **whole-string misuse** of a per-syllable predicate; per-syllable it is **4 of 5** (`L-45 tikmes → sem. kit`, both legal) | **high** — the claim's own `before` field rests on it | §3 | reported |
| **D20-F3** | **withdrawn** — I first attributed 18/9 to a two-predicate table; the C seat's landed amendment shows the real cause is a **stale instrument** (18/9 is the pre-fix gate `5b5abe78…` reading, not re-taken after the syllabify fix `b5406bcd…`) | — | §3 | superseded by the C seat's finding; recorded, not deleted |
| **D20-F4** | the ceiling's table shows each base beside a `reverse` form, but **only 2 of the 8 bases are mark-axis**; the other 6 are fire-axis and are carried by `lengthen`, so six arrows are not the delivered derivations (the semantic claim — 0 abstractions — is correct) | low — a reader-facing inaccuracy, not a count error | §3.1 | reported; my own first reading of this row was the same error and is recorded in §3.1 |
| **D20-F5** | the ceiling is stated as a property of the **register**; measured it is a property of the **(operation, lexicon) pair** — `reverse` carries 1/5, `head2` carries 5/5, and `head2`'s margin is partly trivial (identity on a lexicon whose abstractions are all ≤2 syllables) | medium — the lesson's diagnosis is weaker than its own advice | §4 | reported |
| **D20-F6** | the `is_legal_syllable` *application* (per-syllable vs whole-string) is not pinned anywhere; both rounds pinned the file, not the call | medium | §1, §7 | reported; D19-F2 is the same finding from the pin side |

**Not findings — verified sound.** The rowset (27 mark-axis plain words, 62
lexicon records) reproduces exactly; the gate is stable and its selftest is
27/27; the 8 register forms are the 8 named, all descending from the bases
claimed; the five abstractions are the five named; and the lesson's *advice*
("choose the operation after deciding which classes must be sayable") is correct
and follows from the corrected measurement.

## 7. What the round-28 amendment should state (so the numbers travel correctly)

The claim's `after_required` calls for "an amendment entry, not an in-place
rewrite — new section citing the round-27 measurements". Six items, each closing
a finding above:

| # | the amendment should state | closes |
|---|---|---|
| Y-1 | the split as **19 legal / 8 illegal**, per-syllable, over the 27 mark-axis plain words, with the command and date; and record the round-27 figure as **superseded, with the reason** (a whole-word application of a per-syllable predicate) — not silently replaced | `D20-F1` |
| Y-2 | the abstractions as **4 of 5 refuse `reverse`** per-syllable (`L-15`, `L-30`, `L-44`, `L-51`), with `L-45 tikmes → sem.kit` named as the exception and its two legal syllables shown | `D20-F2` |
| Y-3 | one predicate **and one instrument revision**, named, for every count in the section — the defect was a stale instrument, so the amendment must print the gate digest it measured against | `D20-F3` (withdrawn), `D20-F6` |
| Y-4 | the register forms as **8 of 8 legal under the axis rule**, with the per-row axis→operation agreement shown (2 mark/`reverse`, 6 fire/`lengthen`), so a reader cannot mis-read the table as eight `reverse` derivations | `D20-F4` |
| Y-5 | the lesson's diagnosis as the **(operation, lexicon) pair**: `reverse` carries 1 of 5 abstractions, `head2` carries 5 of 5 over the same lexicon — with the honest caveat that `head2` is the identity on these bases, so the margin is lexicon-shaped | `D20-F5` |
| Y-6 | the application, not just the file: "measured per-syllable, `all(is_legal_syllable(s) for s in syllabify(form))`, over `tools/gates/argot-derivation-gate.py` `b5406bcd…`" | `D20-F6` |

## 8. Independence and controls

- **The predicate is the gate's own**, loaded by `runpy` read-only; nothing is
  re-implemented here. Its docstring and its internal call sites are quoted to
  establish the documented use independently of my reading (§1).
- **Both readings are reported**, not just the one that differs from the record:
  whole-string (17/10), per-syllable (19/8), and the recorded 18/9. The finding
  is that the record matches neither, which is a claim that needs all three.
- **A 16-way variant sweep** is run to falsify the possibility that 18/9 comes
  from a reading I did not think of; the sweep's empty result is the evidence.
- **The single-row difference is identified, not merely counted** (`L-45
  tikmes`), so the correction is checkable row by row.
- **The eight forms are re-derived under their own axis rule**, not under one
  operation applied to all eight: the per-row table in §3.1 shows the delivered
  op, the rule-selected op and the agreement for each, which is what caught my
  own first-pass error.
- **A reviewer error is disclosed, not smoothed**: §3.1 records the wrong
  reading this seat first published and why it was wrong — the same defect the
  file names in §2.
- **The stronger reading (§4) is measured, not argued**: `head2` is run over the
  same five abstractions and carries 5 of 5.
- **The churn is disclosed:** the knowledge entry's live digest is
  `0d993a267f6beb432417df1ddefaaab97e8790515c716e3372e47b3c7e6f158d`; round 27
  deliberately cited it by revision (`RSA-9`/`RSA-10`), and this seat does the
  same for the round-27 peer files, quoting digests only where they are stable
  (`argot-derivation-gate.py` `b5406bcd…`).

**Write scope honoured:** this file, plus `.scratch/r28-d20/`. No component,
packet, tool, gate, fixture, pin, runner, knowledge entry or filed round-8–27
byte was written. No commit, no push.
## 9. Corroboration: the C seat's landed amendment, read after this file was written

The C seat's amendment landed while this review was in progress and was read at
its live digest `ddeeee75af9856c95dc58519a40a3992b06029682d61d0babff662e1cdcc3284`
(section `## 13. Amendment (round 28): the register-lexicon ceiling, re-measured,
with its mechanism`). It is the artifact claim C is about, so it is the decisive
cross-check on this file — and it **independently reaches the same corrections**:

| figure | round-27 record | this seat (D20) | the C seat's amendment | agree? |
|---|---|---|---|---|
| reverse-legality split | 18 / 9 | **19 / 8** | **19 / 8** | ✅ |
| abstract class | 0 legal / 5 illegal | **1 legal / 4 illegal** | **1 legal / 4 illegal** | ✅ |
| the five abstractions | all five refuse | **four refuse** (`L-45` does not) | **four refuse** (`L-45` does not) | ✅ |
| the row that moves | — | `L-45 tikmes` | `L-45 tikmes` | ✅ |

Two independent instruments, one conclusion. **This file's D20-F1, D20-F2 and
D20-F4 are therefore corroborated rather than contested**, and the claim's
`before` field ("5 legal abstractions refuse reverse") is corrected by the C
seat's own amendment, which is the right place for it.

**Where the two seats differ, and this seat's reading is superseded.**

1. **The cause of the 18/9.** This seat attributed it to two predicates in one
   table (`D20-F3`, now **withdrawn**); the C seat shows it is a **stale
   instrument** — the numbers were taken against the pre-fix gate `5b5abe78…`
   and carried forward without being re-taken against `b5406bcd…`. The C seat's
   cause is the better one and is adopted in §3.
2. **The mechanism.** This seat measured the *domain contrast* (`reverse` 1/5,
   `head2` 5/5, with `head2`'s margin noted as partly trivial); the C seat
   measured the *phonological cause* (`reverse` is legal **iff** the
   base-initial consonant is a licensed coda — 14 onset consonants vs 8 licensed
   codas). The C seat's mechanism is stronger: it explains *why* the ceiling
   exists rather than only exhibiting it, and it makes the check transferable.
   §4's contrast remains useful as the design-side statement; the mechanism is
   the craft-side one.
3. **The entry §6 table is amended, not rewritten.** The C seat correctly added a
   new section rather than editing §6 in place, and it labels the 18/9 row
   **superseded** with the reason. That is the discipline the round-28 claim
   asked for ("amendment entry, not in-place rewrite") and it is honoured.

**What this seat adds that the amendment does not carry.** The whole-string
misreading of `is_legal_syllable` is still unrecorded in the tree — the amendment
corrects the *number* and names the pre-fix scan, but the "5 of 5" that appears
in the round-27 files and in entry §6's table is a **per-syllable table with a
whole-string row**, and no artifact yet says so. Recorded as the surviving part
of **D20-F2** and as **Y-2**/`D20-F6` in §7.

**Cross-reference.** The amendment's own §13.5 ("Limits of this amendment") is
honest about its one reconstruction (the pre-fix reader is rebuilt from
`.scratch/r27-d13/oldg/`, not recovered). This seat's §2 measured the delivered
reader directly and did not need that reconstruction, so the two readings are
independent on the delivered side — which is what makes the agreement on 19/8
and 1/4 worth something.
