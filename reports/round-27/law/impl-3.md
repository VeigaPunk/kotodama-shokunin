# R27-D07 — the syllabify fix: one algorithm, and the 62 forms re-verified

- **Seat:** R27-D07 (D axis, syllabify implementation 3 of 8). Round 27, loop 3
  build 3 of 4, claim **D** `register-law`. Integrator: `impl-1.md` (R27-D05).
- **Date:** 2026-10-18. Baseline `4f09c990…`; declaration commit `b95fca1`.
- **Write scope:** this file only; scratch under `.scratch/r27-d/`.
- **Canon:** NON-CANON engineering evidence.

## 1. The algorithm the design states, and the one that was delivered

`design-language.md:191-196` fixes `head2` as maximal onset: "a consonant is
taken as the onset of the following syllable **whenever that yields a legal
syllable**". The delivered gate implemented the first clause and dropped the
second: it moved every consonant run forward and never tested the result.

```
$ python3 .scratch/r27-d/sylref.py          # the pre-fix gate vs a corrected reader
L-01 ker     gate=['ke','r']            design=['ker']
L-45 tikmes  gate=['ti','kme','s']      design=['tik','mes']
NM-02 kalker gate=['ka','lke','r']      design=['kal','ker']
```

`kme`, `lke` and `ke.r` are not syllables. `onset_clusters: false` and the
eight-coda set (`02-phonology.yml:82,92`) refuse the first two; `ke.r` invents a
syllable with no nucleus. The gate therefore did not implement the algorithm its
own docstring cited — round 26's `RD-4` / `RL-3`.

## 2. The fix: three clauses and a public predicate

`tools/gates/argot-derivation-gate.py` (`b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb`):

1. a **single** intervocalic consonant is the following syllable's onset —
   `saalumi` → `saa.lu.mi`, `head2` `saalu` (the design's own worked row);
2. a run of **two or more** keeps all but its last consonant as the preceding
   syllable's coda — `tikmes` → `tik.mes`, `kalker` → `kal.ker`;
3. a **word-final** run is the last syllable's coda — `ker` is one syllable.

The legality clause is now executable and named:
`CODAS = frozenset("nmsklrtd")`, `ONSET_CLUSTERS = False` (both quoted from
`02-phonology.yml`), and the new public predicate

```python
def is_legal_syllable(syllable):
    """Is one syllable of the template `(C)V(V)(C)` with a licensed coda?"""
```

## 3. The disagreement, before and after — and a correction to the count

The claim's `before` carries round 26's figure: **15 of 62**. Re-measured, that
number is a property of the *reader*, and round 26's reader was itself wrong.

| reading | before (vs the pre-fix gate) | after (vs the fixed gate) |
|---|---|---|
| naive maximal onset (any consonant string is an onset) | 0 of 70 | — |
| legality-constrained maximal onset, **round-26's reader** | 15 of 62 | — |
| legality-constrained maximal onset, **corrected** (§2) | **59 of 62** | **0 of 70** |

**The correction matters and is the honest part of this fragment.** Round 26's
reader (`.scratch/r26-d-reg/syl.py`, still on disk) produced
`saalumi → saal` — contradicting the design's own worked row `saalu`, which
round 26 *itself* reported as agreeing in the same output. It mis-split the
vowel sequence `au`/`ai` into separate nuclei. Its 15-row list is therefore not
reproducible from the delivered bytes, and its count **understated** the
divergence by a factor of four: with the reader corrected, 59 of the 62
pre-round-26 forms disagreed, not 15.

Round 26's own number is reported here rather than quietly replaced, because the
claim's `before` cites it and a reader is entitled to see which figure moved and
why.

## 4. The 62 forms, re-verified

```
$ python3 .scratch/r27-d/sylref.py             # before
TRUE disagreements over 62 pre-round-26 forms: 59

$ python3 - <<'PY'                             # after
  forms_checked: 70   disagreements: 0
  design 11 worked rows re-derived: True
  head2(saalumi) = saalu
  forms with any illegal syllable (new gate): 0
```

All **62** forms of the round-26 set are re-verified, and all **70** now
delivered forms with them (`L-01..L-62` + `NM-01..NM-08`). The design's eleven
worked rows re-derive under the fixed gate, including the one `head2` row.

The lane runner re-measures this with **its own** legality-constrained
syllabifier, never reading the gate back as the source of truth
(`run-validation.py:944-960`), and reports `disagreements: 0 forms_checked: 70`.

## 5. The discriminating control, and the design's own trap

The design names the exact row where the two readings disagree, and the fix is
tested on it. A probe register form is added with a declared `head2`:

| control | declared form | result |
|---|---|---|
| C-3 | `saalum` — the maximal-**coda** reading the design explicitly rejects | `FINDING D4L-ARGOT-DERIV`, exit 1, gate replays `saalu` |
| C-3b | `saalu` — the maximal-onset reading | exit 0, no finding |

C-3b is the necessary second half: a control that fires on both would be
measuring nothing. The pair shows the leg discriminates on exactly the row the
design says is why the algorithm is stated at all.

The gate's own selftest grew from 21 to **27 checks**, adding six that pin the
fix and its refusals:

```
syllabify-cluster-splits-coda-onset    ok      # tikmes -> tik.mes
syllabify-naive-scan-differs           ok      # != ti.kme.s
syllabify-word-final-run-is-coda       ok      # ker -> ker; kalker -> kal.ker
syllabify-vowel-sequence-splits        ok      # haitun -> ha.i.tun
head2-cluster-base                     ok      # tumkalker -> tumkal, != tumka
legality-tests-the-template            ok      # tik/tuu legal; kme/s not
selftest: 27/27 checks passed
```

## 6. Blast radius, bounded

The change is confined to `head2`. **No delivered `derived_from`/`derivation`
record in any family names `head2`** — the D4 register stratum uses `reverse`
and `lengthen` — so no replayed verdict over any delivered packet moves:

```
$ python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: … derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0   # exit 0
$ python3 tools/gates/argot-derivation-gate.py tools/gates/fixtures/argot-derivation-gate.yml
FINDING D4L-ARGOT-DERIV ×4, D4L-ARGOT-RULE ×1                                          # exit 1, unchanged
```

The committed fixture's verdict set is byte-identical to the pre-fix run, and
the D4 coverage line is unchanged. The sibling review independently recorded
that the fixed gate's reading is the better one and that a word-final run
belongs to the last syllable's coda (`reports/round-27/law/review.md` §6.1).

## 7. The remaining action is a documentation one

The sibling review's disposition (`review.md` §6): "the remaining action is a
documentation one — lift the new gate's legality predicate into
`design-language.md` so the design's prose and the gate's implementation state
one algorithm." `reports/round-17/d4/design-language.md` is a **filed round-17
byte** and is not this seat's to write; the predicate is stated in the gate's
docstring and in `impl-7.md`, and the lift is named here for the seat that owns
that file.

## 8. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/r27-d/sylref.py
python3 -c "import runpy;g=runpy.run_path('tools/gates/argot-derivation-gate.py');print(g['syllabify']('tikmes'), g['syllabify']('ker'), g['op_head2']('saalumi'))"
python3 tools/gates/argot-derivation-gate.py --selftest | tail -1
sha256sum tools/gates/argot-derivation-gate.py
```
