# R27-C50 — reviewer of the gap-naming fragment (`C42.md`)

- round 27, seat **C** (`R27-C50`, entry reviewer 2 of 6). Date 2026-10-18.
  Lane HEAD `b95fca1`; baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`.
- canon: NON-CANON engineering review. Author-side evidence; admits nothing,
  certifies no round, is not independent promotion verification.
- writes: this file only. No corpus, tool, packet or component byte touched.
  Scratch `.scratch/`, `TMPDIR=$PWD/.scratch`.
- reviews: `reports/round-27/entry/C42.md` (gap naming) against the entry it
  grounds, `corpus/knowledge/linguistics/register-strata-attestation.md`
  (sha256 `811c5a032380d875…` at review close).

## 0. Verdict

**The gap is real, unfilled before the entry, and correctly located — PASS. One
defect found in the fragment's own framing, fixed by the author.**

| check | verdict |
|---|---|
| the gap is named in the entry's head block, field form | pass |
| the gap was unfilled before the entry (absence sweep reproduces) | pass |
| the gap is not filler (named by a prior lane artifact; measurable) | pass |
| the gap is located against the right lane vocabulary | **defect D-3** (fixed) |
| the subject does not duplicate a neighbour | pass |

## 1. The sweep reproduces — re-run by this seat

Lane root, `TMPDIR=$PWD/.scratch`, 2026-10-18, excluding the entry itself:

```sh
E=corpus/knowledge/linguistics/register-strata-attestation.md
grep -rl -i "illocutionary"       corpus/knowledge/ | grep -v "$E" | wc -l   # 0
grep -rl -i "perlocutionary"      corpus/knowledge/ | grep -v "$E" | wc -l   # 0
grep -rl -i "constitutive rule"   corpus/knowledge/ | grep -v "$E" | wc -l   # 0
grep -rl -i "deontic"             corpus/knowledge/ | grep -v "$E" | wc -l   # 0
grep -rl -i "attestation register" corpus/knowledge/ | grep -v "$E" | wc -l  # 0
grep -rl -i "register law"        corpus/knowledge/ | grep -v "$E" | wc -l   # 0
grep -rn -i "felicity"            corpus/knowledge/ | grep -v "$E"
# linguistics/semantics-pragmatics.md:88
# myth-symbol/ritual-liminality.md:112
```

Every count matches the fragment's claim, including the two honest `felicity`
hits. A sweep that reported "0 files" for `felicity` would have been the
false-absence shape `x63`'s own history warns about (`X63-H2`), so the two hits
being reported is a **positive** sign, not a defect.

## 2. The gap is not invented by this entry

Independently confirmed: the lane declared it first.

```sh
grep -n "no component that owns a register law\|RL-6\|RD-5c" reports/round-26/register/review.md
# §6.3: "The delivered tree has no component that owns a register law"
```

and the round-27 instrument that measures it is built on **different machinery**
from the lane gate (Ruby YAML loader, no lane code imported), so the reading is
not circular. The fragment's claim that the gap is "measurable on delivered
bytes, not asserted" holds.

## 3. Defect D-3 — the gap was located against a section that does not carry it

`C42.md` §1 says the entry's gap is named against "the `corpus/README.md` 'Known
gaps (frontier)' section and the round-19 `reports/round-19/gaps.md` registry
convention", and its §4 limit says "the entry's gap is named against the
round-19 registry convention and the round-26 finding, not against a `Known
gaps` bullet that names 'register law' verbatim".

Measured by this seat:

```sh
sed -n '274,436p' corpus/README.md | grep -c -i "register law\|attestation\|speech act\|illocution"
# 0
```

**Zero frontier bullets mention this subject.** So the sentence's first clause
("named against the `Known gaps (frontier)` section") is misleading: the entry
is *consistent with* that section's convention (dated bullets, one per landing)
but the frontier section carries **no** bullet for this gap, and none is claimed.
The fragment's §4 limit was already correct; the §1 sentence was not.

**Disposition: fixed by the author** — `C42.md` §1 now states plainly that the
gap is located against the round-19 registry convention and the round-26 finding,
and that no `Known gaps` bullet names it. The distinction matters because a
reader who searches the frontier section for this gap will find nothing and may
conclude the gap is unregistered.

## 4. Non-duplication, checked at the right grain

The fragment's nearest-neighbour test (`grep -ril "speech act"` ∩
`grep -qi "register"` → 15 files) is correct but coarse; this seat checked the
grain that matters — **is any of the 15 the same subject?**

| file | why it is a mention, not the subject |
|---|---|
| `syntax-typology.md`, `semantics-pragmatics.md` | one-line framework asides |
| `politeness-taboo-euphemism.md` | politeness = standing; not binding |
| `ritual-liminality.md:112` | names the felicity code as a thing to write; does not write it |
| `creation-myths-taxonomy.md`, `symbolism-synthesis-method.md`, `trickster.md` | "register" in the *style/medium* sense |
| `craft-artisan-lexicon.md`, `egypt-ancient.md`, `mongol.md`, `swahili-coast.md`, `persia-sasanian.md` | unrelated senses |

No file duplicates the entry's subject. The entry's §1 separation table is
accurate.

## 5. What this review did not do

Did not edit the entry or the fragment; did not certify claim C; did not
re-measure the round-26 artifacts the gap rests on (cited by path).

## 6. Replay

```sh
export TMPDIR=$PWD/.scratch
E=corpus/knowledge/linguistics/register-strata-attestation.md
grep -rl -i "illocutionary" corpus/knowledge/ | grep -v "$E" | wc -l
grep -rn -i "felicity" corpus/knowledge/ | grep -v "$E"
grep -n "no component that owns a register law" reports/round-26/register/review.md
sed -n '274,436p' corpus/README.md | grep -c -i "register law\|attestation\|speech act\|illocution"
```
