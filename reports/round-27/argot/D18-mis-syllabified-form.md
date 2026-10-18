# R27-D18 — adversarial review 2 of 4: a form mis-syllabified, and the verdict inverted

- **Seat:** R27-D18 (reviewer 2 of 4), round 27, loop 3 build 3 of 4, claim **D**
  `register-law` (`reports/round-27/claims.json`).
- **Date:** 2026-10-18. Declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`;
  lane HEAD `b95fca1e40f32f7346937ab6426f9ccca60e319f`. Measurement stamp
  **2026-10-18T19:33:47Z** (`date -u +%FT%TZ`).
- **Review target:** the round-27 **syllabify fix** in
  `tools/gates/argot-derivation-gate.py` — sha256
  `b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb`, 928 lines,
  `--selftest` **27/27** — against the algorithm the design **states**
  (`reports/round-17/d4/design-language.md:191-196`) and the packet's own
  inventory (`02-phonology.yml` `PHON-01`).
- **Write scope:** this file only, plus gitignored scratch under
  `.scratch/r27-d18/`. `export TMPDIR=$PWD/.scratch` preceded every
  scratch-writing command. **No gate, packet, component, fixture, pin or filed
  rounds 8–26 byte was written; no commit, no push.**
- **Canon:** NON-CANON engineering evidence.

**Assignment.** Reviewer 2 of 4, adversarial: *a form mis-syllabified?* The
round-26 review named this as `RD-4`/`RL-3` and the round-27 claim's
`after_required` reads "the syllabify disagreement fixed (**one algorithm**,
forms re-verified)". This file measures whether the landed fix produces one
algorithm, and whether a disagreement can still **invert a verdict**.

**Verdict in one line.** The fix is **real and substantial** — the
cluster-bearing non-syllables are gone, the gate now carries an
`is_legal_syllable` it had no equivalent of, and the design's named trap
(`saalum`) is rejected under every reading — but it is **not one algorithm**:
the **falling diphthongs `ai`/`au` are still split into two nuclei**, so on
`tumhai`, `haitun` and `haitik` the gate disagrees with the design, **with the
packet's own `syllables:` field**, and with the round-27 runner's own lawful
syllabifier. On that residue a **design-correct form is graded red and the wrong
form green** — the same verdict inversion round 26 measured, narrowed from the
cluster class to the diphthong class, not closed.

## 0. What the fix changed — three independent readings agree

The gate moved inside this round's window. Both revisions are measured here so
the change is dated by bytes, not asserted:

| revision | sha256 | lines | `--selftest` | legality predicate |
|---|---|---:|---:|---|
| pre-fix (round-25/26 revision) | `5b5abe7865ed906c…` | 840 | 21/21 | **absent** |
| **landed (round-27)** | **`b5406bcdaf41c595…`** | **928** | **27/27** | `is_legal_syllable` at `:217` |

The pre-fix gate's reading of a cluster was a "syllable" that no legality table
licenses. Measured on the same forms, before → after:

| form | pre-fix gate | **landed gate** | design / packet |
|---|---|---|---|
| `tikmes` | `['ti','kme','s']` | **`['tik','mes']`** | `['tik','mes']` |
| `ker` | `['ke','r']` | **`['ker']`** | `['ker']` |
| `kalker` | `['ka','lke','r']` | **`['kal','ker']`** | `['kal','ker']` (packet) |
| `saalumi` | `['saa','lu','mi']` | `['saa','lu','mi']` | `['saa','lu','mi']` |

The design's own named trap is now rejected under every reading, and the gate's
selftest grew by six checks (21 → 27), which is the class of evidence the claim
asks for.

## 1. The residue: the diphthong is still two nuclei

`design-language.md:191-196` states the algorithm and **why it is stated**: "a
consonant is taken as the onset of the following syllable **whenever that yields
a legal syllable**". The landed gate implements the legality clause — its own
docstring at `:153-171` quotes it and reasons about `tikmes` → `tik.mes` — but
the **nucleus** is still computed as one vowel (or a doubled vowel), never as a
diphthong:

```
$ sed -n '172,185p' tools/gates/argot-derivation-gate.py
    while index < len(word):
        char = word[index]
        if char in VOWELS:
            if index + 1 < len(word) and word[index + 1] == char:
                tokens.append(("V", char * 2))      # a doubled vowel
                index += 2
            else:
                tokens.append(("V", char))          # <- `ai` becomes V then V
```

The packet states the diphthong twice — once in prose, once in data:

- `02-phonology.yml` `accent`: *"the falling diphthongs **ai** and **au** are the
  only other vowel sequences."*
- the packet's own `syllables:` field on the 8 `names` records:
  `NM-05 haitik -> ['hai','tik']` — **two** syllables, so `hai` is **one**
  nucleus.

### 1.1 The census — gate vs the design and vs the packet

Measured by `.scratch/r27-d18/final-census.py` (this seat's own instrument; the
design reading re-implemented from the prose plus the packet's inventory, never
copied from the gate):

```
forms: 70            (54 lexicon terms + 8 register forms + 8 names)
head2 disagreements (gate vs design):  3 of 70
   L-48  haitun   gate=hai     design=haitun
   NM-01 tumhai   gate=tumha   design=tumhai
   NM-05 haitik   gate=hai     design=haitik
full-split disagreements:              6 of 70
   L-12 sau    gate=['sa','u']            design=['sau']
   L-19 dau    gate=['da','u']            design=['dau']
   L-28 hai    gate=['ha','i']            design=['hai']
   L-48 haitun gate=['ha','i','tun']      design=['hai','tun']
   NM-01 tumhai gate=['tum','ha','i']     design=['tum','hai']
   NM-05 haitik gate=['ha','i','tik']     design=['hai','tik']
```

And against the **packet's own author-declared witness** — a third reading no
round-26 probe consulted, which the packet carries for its own purposes:

```
gate vs the packet's `syllables:` field:  6 of 8 agree, 2 disagree
   NM-01 tumhai  packet=['tum','hai']  gate=['tum','ha','i']  agree=False
   NM-05 haitik  packet=['hai','tik']  gate=['ha','i','tik']  agree=False
```

**All six residual rows are the same class**: `ai`/`au` treated as two nuclei.
The cluster class that round 26 named is closed; the diphthong class is not.

### 1.2 The round-27 runner shares the residue — so the fix passed its own check

This is the part a reader should weigh, because it explains why the landed fix
reads green while disagreeing with the packet. The round-27 acceptance runner
carries **its own** lawful syllabifier (`run-validation.py:512`,
`lawful_syllables`) and its own control rows (`:133-135`):

```
SYLLABLE_CONTROLS = (("tikmes", ["tik","mes"]), ("kalker", ["kal","ker"]),
                     ("tumhai", ["tum","ha","i"]), ("haitun", ["ha","i","tun"]),
                     ("saalumi", ["saa","lu","mi"]))
```

`tumhai` and `haitun` are pinned there as **`['tum','ha','i']`** and
**`['ha','i','tun']`** — i.e. the runner's own reference **also** splits the
diphthong. Measured:

```
runner lawful_syllables("tumhai") = ['tum','ha','i']   gate = ['tum','ha','i']   AGREE
runner lawful_syllables("haitun") = ['ha','i','tun']   gate = ['ha','i','tun']   AGREE
runner lawful_syllables("hai")    = ['ha','i']         gate = ['ha','i']         AGREE
packet        syllables("tumhai") = ['tum','hai']      gate = ['tum','ha','i']   DISAGREE
```

So the runner's syllabify leg reads `disagreements: 0 of 70` — **not because the
gate matches the design, but because the runner's reference makes the same
reading error.** Two instruments sharing a defect agree with each other and
disagree with the artifact both are supposed to check. The runner's `SYLLABLE_
CONTROLS` are its own, labelled as such ("these are this runner's own controls,
not design quotes"), which is honest — but it means the claim's "forms
re-verified" is verified against an instrument that shares the residue.

## 2. The verdict inversion — a design-correct form graded red

This is the adversarial core. Two probe pairs, each built by adding **one**
lexicon record to the delivered packet (`ng._dump_yaml` of a deep copy), so the
only difference between the arms is the declared form.

**Pair A — the cluster class (round 26's finding): now FIXED.**

| arm | declared | expected by the design | measured |
|---|---|---|---|
| `probe-head2-design-correct.yml` | `head2(salwer) = salwer` | clean | **exit 0, `violations=0`** |
| `probe-head2-gate-reading.yml` | `head2(salwer) = salwe` | red | **exit 1, `violations=1`** |

Before the fix the two arms read the **opposite** way (this seat measured it at
gate `5b5abe78…`: the design-correct form read `violations=1`). The fix
**corrected the inversion** on the cluster class.

**Pair B — the diphthong class: the inversion is still there.**

| arm | declared | expected by the design | measured (landed gate) |
|---|---|---|---|
| `diph-design-correct.yml` | `head2(tumhai) = tumhai` | **clean** | **exit 1, `violations=1`** |
| `diph-gate-reading.yml` | `head2(tumhai) = tumha` | **red** | **exit 0, `violations=0`** |

```
$ python3 -B tools/gates/argot-derivation-gate.py .scratch/r27-d18/diph-design-correct.yml
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form PH-2 'tumhai' (register 'stamp'):
  declared chain 'head2' applied to 'tumhai' yields 'tumha'; the stated inputs and
  rules do not yield the candidate
coverage: … violations=1        exit 1

$ python3 -B tools/gates/argot-derivation-gate.py .scratch/r27-d18/diph-gate-reading.yml
coverage: … violations=0        exit 0
```

`tumhai` is **two** syllables by the packet's own field (`['tum','hai']`), so
`head2` — the first **two** syllables, by the design's own definition — is
`tumhai`, the whole word. The gate grades that **red** and grades `tumha` (the
first syllable plus a fragment of the second) **green**. A family building a
`head2` stratum on a diphthong-bearing base is graded against an algorithm its
design does not declare, and the correct form is the one that fails.

**Severity today: low, and the reason is the same as round 26's.** No delivered
rule is `head2`-scoped (`derivation_ops: [head2, reverse, lengthen]` with
`head2` declared-but-unused, `04-lexicon.yml:263`), so no delivered record is
failed by the residue. It becomes load-bearing the moment any round builds a
`head2` stratum — which is exactly what round 26's `RD-3`/`RL-2` warns.

## 3. What this seat did not do, and the limits

| id | limit | statement |
|---|---|---|
| **D18-L1** | the design's reading is **this seat's transcription of prose** | the design states the algorithm in words, not code; this seat implemented it from `design-language.md:191-196` plus the packet's own inventory and diphthong declaration. A different faithful transcription is possible; **the packet's `syllables:` field is the tie-breaker**, and it agrees with this seat on `tumhai`/`haitik` 2 of 2. |
| **D18-L2** | the gate was **not edited** | the gate is not this reviewer's file. The residue is reported, not repaired. |
| **D18-L3** | the fix is **not called a failure** | the cluster class — the class round 26 named and measured at 15/62 — **is closed**. This file's finding is narrower: the claim says *one algorithm*, and two readings remain. |
| **D18-L4** | scratch only | every probe lives under `.scratch/r27-d18/`; none was promoted to the packet or a fixture set. |

## 4. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
sha256sum tools/gates/argot-derivation-gate.py            # b5406bcdaf41c595…
python3 -B tools/gates/argot-derivation-gate.py --selftest | tail -1   # 27/27
python3 -B .scratch/r27-d18/final-census.py               # 3 of 70 head2, 6 of 70 full
python3 -B tools/gates/argot-derivation-gate.py .scratch/r27-d18/probe-head2-design-correct.yml  # exit 0
python3 -B tools/gates/argot-derivation-gate.py .scratch/r27-d18/probe-head2-gate-reading.yml    # exit 1
python3 -B tools/gates/argot-derivation-gate.py .scratch/r27-d18/diph-design-correct.yml         # exit 1 (design-correct!)
python3 -B tools/gates/argot-derivation-gate.py .scratch/r27-d18/diph-gate-reading.yml           # exit 0
grep -n "SYLLABLE_CONTROLS" -A 2 reports/round-27/run-validation.py
python3 -c "import runpy; ns=runpy.run_path('reports/round-27/run-validation.py'); \
  print(ns['lawful_syllables']('tumhai', *ns['inventory'](ns['load_yaml_text'](open('examples/culture-d4/packet.d4.yml').read()))))"
```
