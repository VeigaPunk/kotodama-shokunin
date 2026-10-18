# R27-D16 — negative: a syllabify regression is caught, before and after the fix

- **Seat:** R27-D16 (gate runs 4 of 4), round 27, loop 3 build 3 of 4, claim **D**
  `register-law`. Assignment: *"negatives (… a syllabify regression caught)"*.
- **Date:** 2026-10-18. Declared baseline `4f09c990…`; lane HEAD
  `b95fca1e40f32f7346937ab6426f9ccca60e319f` at every measurement.
- **Write scope:** `reports/round-27/gate-tests/fixtures/s1..s4*.yml` and this
  file, plus gitignored scratch. No gate, packet, component, projector, pin or
  filed rounds 8–26 byte written; no commit, no push.
- **Canon:** NON-CANON fixtures. Every form below is a planted probe or a
  round-17 design row; none is a claim about a language.

## 0. Verdict

**A syllabify regression is caught, the fix landed mid-wave, and this seat's own
reading pair detected the landing by collapsing — which is what it was built to
do.**

Every row below was **executed against both gates** — the committed pre-fix
gate (`git show HEAD:tools/gates/argot-derivation-gate.py`, sha256
`5b5abe78…`) and the live post-fix gate (`d7a3ad1a…`) — not inferred:

| control | pre-fix | post-fix | reading-independent? |
|---|---:|---:|---|
| `s3-head2-maximal-coda.yml` (`saalum` as `head2(saalumi)`) | 1 | **1** | **yes** — rejected under every reading |
| `s1-head2-unconstrained.yml` (`tumka` as `head2(tumkalker)`) | **0** | 1 | no — the pre-fix reading of the cluster row |
| `s2-head2-constrained.yml` (`tumkal` as `head2(tumkalker)`) | 1 | **0** | no — the post-fix reading of the cluster row |
| `s4-head2-prefix-reading.yml` (`tikme` as `head2(tikmes)`) | **0** | **1** | no — the before/after witness |
| the design's 11 worked rows, re-derived | 11/11 | **11/11** | — |

The pair's two rows **swap** across the fix: `s1` was clean and `s2` red
pre-fix; `s2` is clean and `s1` red post-fix. The pair therefore discriminates
on both sides, which is the property it was built for.

`receipt.json`: `summary: 55/55 checks passed`.

## 1. The fix landed, and the gate now implements the design's algorithm

Pinned before and after:

| | pre-fix | post-fix |
|---|---|---|
| `tools/gates/argot-derivation-gate.py` | `5b5abe7865ed906c…` (round-25 revision) | **`d7a3ad1a6ad1c4c5…`** |
| legality check in source (`is_legal_syllable`) | absent | **present** |
| `syllabify('tikmes')` | `['ti', 'kme', 's']` | **`['tik', 'mes']`** |
| `head2('tikmes')` | `tikme` | **`tikmes`** |
| `syllabify('tumkalker')` | `['tu', 'mka', 'lke', 'r']` | **`['tum', 'kal', 'ker']`** |
| the gate's own selftest | 21/21 | **27/27** |
| delivered reading | unconstrained | **legality-constrained** |

`head2(saalumi) == 'saalu'` holds on both sides, so the design's own named row
was never the broken one — the divergence was elsewhere, which §3 shows.

## 2. The reading pair was rebased, and the rebase is itself a finding

The pair was first anchored on `tikmes`: `s1` delivered `tikme` (the
unconstrained reading) and `s2` delivered `tik` (the constrained one). That was
correct **before** the fix and became wrong **after** it, because the legality
clause collapses the two readings of a one-cluster base: `tikmes` is `tik.mes`
under both, so `head2(tikmes) == 'tikmes'` and **neither** fixture derives.

```
the ORIGINAL tikmes pair      pre-fix  post-fix
  o1 = `tikme` (unconstrained)    0        1
  o2 = `tik`   (constrained)      1        1
                              clean    BOTH RED — the pair collapsed
```

**The pair's own check (`exactly one reading derives`) caught this**, which is
exactly what it exists for: a control that goes all-red after a change is not a
passing control, it is a control that has stopped measuring. The pair is now
anchored on `tumkalker`, a **two-cluster** base where the readings genuinely
differ — unconstrained moves each run whole to the onset (`tum.ka.lker` →
`tumka`), constrained splits coda|onset (`tum.kal.ker` → `tumkal`) — and it
discriminates again: `s1` exit 1, `s2` exit 0.

This is worth stating plainly rather than quietly fixing: **a reading pair
anchored on a base the fix makes unambiguous silently stops discriminating.**
The rebase is a new row, and the collapsed reading is preserved above.

## 3. The before/after witness: `s4`

`s4` delivers `tikme` as `head2(tikmes)` — the **pre-fix** reading. It is clean
before the landing and red after it, so it is a witness that the algorithm moved
rather than an assertion that it did:

```
pre-fix :  exit 0   (the gate agreed with the pre-fix reading)
post-fix:  exit 1   FINDING D4L-ARGOT-DERIV — declared chain 'head2' applied to
                    'tikmes' yields 'tikmes'; the stated inputs and rules do not
                    yield the candidate
```

## 4. The residual gap: the falling diphthong, 6/8 → still 2 short

The strongest acceptance surface is **inside the delivered packet**: the 8
`names` records carry an author-declared `syllables:` field, written by an
earlier round for a different purpose and consulted by no gate
(peer seat X54's `X54-H3`, `reports/round-27/scribe/x54-syllabify-spotcheck.md`
§1). It has a fixed answer from delivered bytes:

| id | name | packet declares | the gate yields | |
|---|---|---|---|---|
| NM-01 | `tumhai` | `['tum', 'hai']` | `['tum', 'ha', 'i']` | **DIFF** |
| NM-02 | `kalker` | `['kal', 'ker']` | `['kal', 'ker']` | ok |
| NM-03 | `samren` | `['sam', 'ren']` | `['sam', 'ren']` | ok |
| NM-04 | `mestum` | `['mes', 'tum']` | `['mes', 'tum']` | ok |
| NM-05 | `haitik` | `['hai', 'tik']` | `['ha', 'i', 'tik']` | **DIFF** |
| NM-06 | `meslun` | `['mes', 'lun']` | `['mes', 'lun']` | ok |
| NM-07 | `kalnes` | `['kal', 'nes']` | `['kal', 'nes']` | ok |
| NM-08 | `salwer` | `['sal', 'wer']` | `['sal', 'wer']` | ok |

**Agreement moved 0/8 → 6/8.** The two rows still disagreeing are exactly the
two whose first nucleus is the falling diphthong **`ai`**, which the syllabifier
still splits as two nuclei. The packet states the answer twice — in prose (its
`accent` field: *"the falling diphthongs ai and au are the only other vowel
sequences"*) and in data (`NM-05 haitik → ['hai','tik']` is **two** syllables).

This seat records the residual as a **named gap** with the two row ids and the
reason, rather than as a bare "not 8/8" — a round-27 fix verified against "not
all 8" cannot tell a one-row regression from a two-row one. Note that the gate's
own selftest **encodes** the split the packet's field contradicts:

```
tools/gates/argot-derivation-gate.py:800
    checks.append(("syllabify-diphthong-nucleus",
                   syllabify("haitun") == ["ha", "i", "tun"]))
```

The control is *named* `syllabify-diphthong-nucleus` while asserting the
diphthong is **two** nuclei, and the string `diphthong` appears in the gate's
source nowhere else — there is no diphthong concept in the syllabifier, only
this assertion. So the gate is internally consistent and externally disagreeing
with its own packet: it grades `haitun` as three syllables where the packet's
`NM-05 haitik` field grades `hai` as one. That is the residual in one line, and
it is why the fix took the witness to 6/8 rather than 8/8.

**No delivered finding turns on this.** No delivered packet rule is
`head2`-scoped (round 26's substantive disposition, which this seat agrees
with), so the residual fails nothing today. Its value is that the fix's
acceptance surface is a delivered fact with an answer, and the answer is now
6/8 rather than 0/8.

## 5. What this seat found that round 26 got wrong, and reported rather than edited

Round 26's published figures were measured against `.scratch/r26-d-reg/syl.py`,
a re-implementation labelled "the design's stated algorithm". Re-run, it
**fails the design's own named row**:

```
design-language.md table: head2(saalumi) == 'saalu'
r26 reference  head2(saalumi) = 'saal'      syllables ['s','aal','um','i']
delivered gate head2(saalumi) = 'saalu'
```

It splits a word-initial single consonant off as its own syllable (`sau →
['s','a','u']`), which the design never licenses. So the "15 of 62" figure was
measured against a reference that fails the row it was cited to support.

**This is recorded as a NEW row in this round's file, never as an edit to a
filed round-26 artifact** (the lane's rule: re-pins are new rows; corrections
are new files). Peer seat X54 reached the same conclusion by an independent route
and carries it further (`X54-F2` inflates the count by 3, `X54-F3` finds two
mutually inconsistent "design" implementations). The two seats agree; neither
edited round 26.

## 6. Limits

- **This seat does not repair the gate.** The gate is not this seat's file. The
  fix that landed is another seat's; this seat measures it.
- **The reading pair is discriminating, not adjudicating.** It catches a
  regression without deciding the algorithm.
- **`s3`/`s4` are fixtures, not delivered records.** No delivered packet record
  is `head2`-scoped.
- **Stamp-bound and mid-wave.** The landing is uncommitted at `b95fca1`; the
  digests above are of the working tree. If the residual diphthong is fixed, the
  witness moves to 8/8 and the runner prints that on one command.
