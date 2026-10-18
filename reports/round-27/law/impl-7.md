# R27-D11 — the algorithm, stated once: the legality predicate and where it lives

- **Seat:** R27-D11 (D axis, register law + syllabify implementation 7 of 8).
  Round 27, loop 3 build 3 of 4, claim **D** `register-law`. Integrator:
  `impl-1.md` (R27-D05).
- **Date:** 2026-10-18. Baseline `4f09c990…`; declaration commit `b95fca1`.
- **Write scope:** this file only; scratch under `.scratch/r27-d/`.
- **Canon:** NON-CANON engineering evidence.

## 1. The problem this fragment addresses

Round 26 filed the syllabify gap as "the gate disagrees with the design's
stated algorithm on 15 of 62 forms". The sibling round-27 review re-measured it
and reached the sharper conclusion:

> "the disagreement **cannot be fixed by choosing an algorithm while the design's
> own prose is ambiguous about what 'legal syllable' means.** The fix is a
> definition, not an implementation: state the legality predicate, then either
> the gate's algorithm or the design's is provably wrong." —
> `reports/round-27/law/review.md` §6

This fragment is that definition, stated once, so the prose and the code stop
being two things a reader has to reconcile.

## 2. The definition

**A legal D4 syllable is a string matching `(C)V(V)(C)` in which:**

1. the onset is **at most one consonant** — `onset_clusters: false`
   (`examples/culture-d4/components/02-phonology.yml:92`);
2. the nucleus is **one vowel, or one doubled (long) vowel** — vowel length is
   one nucleus (`02-phonology.yml:109`);
3. the coda is **empty or one consonant drawn from** `n m s k l r t d`
   (`02-phonology.yml:82-91`);
4. there is **no bare consonant** — every syllable has a nucleus.

Two consequences follow immediately, and they are what the delivered gate got
wrong: `kme` is illegal (two-consonant onset), and `r` is illegal (no nucleus).

## 3. The algorithm, stated once

**Maximal-onset syllabification, legality-constrained:**

> Scan the word as a sequence of nuclei and consonant runs. For each consonant
> run that is **followed by a nucleus**, assign as much of the run to the
> following onset as legality permits — under clause 1 that is exactly its
> **last** consonant — and give the remainder to the preceding syllable as its
> coda. A run **at the end of the word** is the last syllable's coda. A run with
> no syllable before it takes its own onset position.

Worked, on the delivered forms:

| word | syllables | why |
|---|---|---|
| `saalumi` | `saa.lu.mi` | single consonants are onsets; `aa` is one nucleus → `head2` `saalu` |
| `tikmes` | `tik.mes` | the `km` run splits coda\|onset; `kme` would be an illegal onset |
| `kalker` | `kal.ker` | same split; `lke` illegal |
| `ker` | `ker` | the final `r` is a coda, not a syllable — `ke.r` invents a nucleus |
| `haitun` | `ha.i.tun` | `ai` is a vowel sequence, not one long vowel, so it is two nuclei |
| `tumhai` | `tum.ha.i` | `mh` splits; `ha.i` from the `ai` sequence |

## 4. Where the definition now lives

| site | form | status |
|---|---|---|
| `tools/gates/argot-derivation-gate.py` | `is_legal_syllable()` + `CODAS` + `ONSET_CLUSTERS`, and the `syllabify` docstring | **landed this round** |
| `reports/round-27/law/impl-3.md`, this file | the prose statement | landed this round |
| `reports/round-17/d4/design-language.md:191-196` | the design's original prose, which states clause 1 only implicitly ("whenever that yields a legal syllable") without defining *legal* | **NOT written** — a filed round-17 byte, and the sibling review names the lift as the remaining action |

The gate is the executable site; the design's prose is the filed site. This seat
wrote the former and names the latter. `design-language.md` is a round-17
artifact and is not this seat's to rewrite under the lane's supersede-by-new-file
rule.

## 5. The predicate is testable, and tested

```python
is_legal_syllable("tik")   # True   — (C)V(C), coda k licensed
is_legal_syllable("tuu")   # True   — long nucleus, empty coda
is_legal_syllable("kme")   # False  — two-consonant onset
is_legal_syllable("s")     # False  — no nucleus
```

The gate's selftest pins all four (`legality-tests-the-template`), and the
`head2` consumer is exercised on the design's own row:

```
syllabify("tikmes") == ["tik", "mes"]      and  != ["ti", "kme", "s"]
syllabify("ker")    == ["ker"]             and  syllabify("kalker") == ["kal", "ker"]
op_head2("saalumi") == "saalu"
selftest: 27/27 checks passed
```

## 6. Why this is a definition and not a preference

Under the definition above, the pre-fix gate is **provably wrong** on 59 of the
62 round-26 forms, and the corrected reader agrees with the fixed gate on all 70
delivered forms. That is the test the sibling review asked for: state the
predicate, and one of the two implementations becomes demonstrably wrong. It did.

The remaining ambiguity is **not** in the predicate but in the round-26
*measurement*: that seat's reader mis-split vowel sequences and produced
`saalumi → saal`, contradicting its own reported agreement on the design's
worked row. The corrected count is in `impl-3.md` §3.

## 7. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 -c "import runpy;g=runpy.run_path('tools/gates/argot-derivation-gate.py');print([g['is_legal_syllable'](s) for s in ('tik','tuu','kme','s')])"
python3 -c "import runpy;g=runpy.run_path('tools/gates/argot-derivation-gate.py');print(g['syllabify']('tikmes'), g['syllabify']('kalker'), g['syllabify']('haitun'))"
python3 tools/gates/argot-derivation-gate.py --selftest | tail -1
grep -n "is_legal_syllable\|^CODAS\|^ONSET_CLUSTERS" tools/gates/argot-derivation-gate.py
```
