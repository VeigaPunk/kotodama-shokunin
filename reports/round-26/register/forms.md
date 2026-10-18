# R26-D02 — the register forms: arithmetic, legality, collisions, era, and the receipt

- **Seat:** R26-D02 (D axis, register design 2 of 4), round 26, loop 3 build 2 of 4,
  claim **D** `register-stratum`.
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`;
  worktree HEAD `1ad491a`.
- **Design authority:** `reports/round-26/register/design.md` (this round, seat
  D01). **Forecast sources:** `reports/round-17/d4/design-language.md`
  (`cfc2d698…`) §5/§6, `reports/round-17/d4/design-brief.md` (`a5fdc84d…`) Δ3/Δ5.
- **Write scope:** this file only, plus gitignored scratch under
  `.scratch/r26-d-reg/`. No tool, gate, packet, component, or filed 8–25 byte
  written; no commit, no push.
- **Canon:** NON-CANON. The forms are design choices, not attested data; no real
  language is cited or approximated.

## 1. The eight register forms (authoritative table)

Operation selection is by the delivered record's own `axis` (design.md §3):
`mark → reverse`, `fire → lengthen`. Every row below was recomputed by
`.scratch/r26-d-reg/probe2.py` and is stored in
`.scratch/r26-d-reg/forms.json`.

| id | base | base gloss | axis | op | form | gloss in the register |
|---|---|---|---|---|---|---|
| RF-01 | L-02 `tum` | breath, life-breath; the bellows breath | fire | lengthen | `tuum` | the breath the smith swears by |
| RF-02 | L-42 `tik` | mark, stamp; to stamp | mark | reverse | `kit` | the mark itself, spoken |
| RF-03 | L-38 `mol` | mold, cast form | mark | reverse | `lom` | the mold, named in the register |
| RF-04 | L-16 `nes` | water, spring; the quench trough's water | fire | lengthen | `nees` | the quench water, named |
| RF-05 | L-09 `hum` | smoke; the furnace's messenger | fire | lengthen | `huum` | the smoke that carries the word |
| RF-06 | L-43 `mes` | metal, ingot | fire | lengthen | `mees` | the ingot as an attested lot |
| RF-07 | L-37 `rek` | ore; bog-ore | fire | lengthen | `reek` | the ore as an attested lot |
| RF-08 | L-39 `sam` | charcoal | fire | lengthen | `saam` | the charcoal as an attested lot |

**8 of 8 clean.** Every form is (a) inventory-legal under 02's PHON-01, (b)
syllable-legal under the template `(C)V(V)(C)` with the eight codas, (c) free of
exact collision with any delivered form, and (d) free of collision with the D2
fixture ledger (`04-lexicon.yml:22` D2B-03 sweep list). The measurement:

```
$ python3 .scratch/r26-d-reg/probe2.py
RF-01 L-02 tum    axis=fire  lengthen  -> tuum   legal=yes deliv_coll=False d2_coll=False syl=['tuum']
RF-02 L-42 tik    axis=mark  reverse   -> kit    legal=yes deliv_coll=False d2_coll=False syl=['kit']
RF-03 L-38 mol    axis=mark  reverse   -> lom    legal=yes deliv_coll=False d2_coll=False syl=['lom']
RF-04 L-16 nes    axis=fire  lengthen  -> nees   legal=yes deliv_coll=False d2_coll=False syl=['nees']
RF-05 L-09 hum    axis=fire  lengthen  -> huum   legal=yes deliv_coll=False d2_coll=False syl=['huum']
RF-06 L-43 mes    axis=fire  lengthen  -> mees   legal=yes deliv_coll=False d2_coll=False syl=['mees']
RF-07 L-37 rek    axis=fire  lengthen  -> reek   legal=yes deliv_coll=False d2_coll=False syl=['reek']
RF-08 L-39 sam    axis=fire  lengthen  -> saam   legal=yes deliv_coll=False d2_coll=False syl=['saam']

clean: 8 of 8; problems: []
```

### 1.1 The two corrections to `design.md`'s first table, and why they matter

`design.md` §4's first draft carried two rows that contradicted its own §3 rule:

1. **RF-01 form.** Drafted `huum`; the correct lengthening of `tum` is `tuum`
   (`huum` is RF-05's, from `hum`). A duplicate would have been a `D4L-DATA`
   class defect (two records, one form).
2. **RF-03 base.** Drafted `L-36 kal` with `reverse → lak`. But `kal` is a
   **`fire`**-axis record (`04-lexicon.yml:168` `axis: fire`), so under §3 it
   takes `lengthen` (`kaal`), not `reverse`. `kal` was therefore replaced by
   `L-38 mol` (`axis: mark`), whose `reverse → lom` is rule-correct.

Both are recorded rather than silently folded. The rule is the design's load
bearing claim; a form set that quietly ignores it is not the design.

## 2. The two operations, stated exactly

The forecast fixed `head2` (first two syllables, maximal-onset) and `reverse`
(character-level string reversal) and proved them on 11 worked rows
(`design-language.md:191-215`). This design **keeps `reverse` unchanged** and
**replaces `head2` with `lengthen`** for the reason measured in §4 of
`review.md`: `head2` has no proper domain over the delivered tree.

| op | algorithm | witness |
|---|---|---|
| `reverse` | character-level reversal of the base: `f = b[::-1]` | `tik → kit`, `mol → lom` (RF-02/03) |
| `lengthen` | double the **first nucleus** of the base: `f = onset + V + V + rest` | `mes → mees`, `rek → reek`, `hum → huum` (RF-05..08) |

`lengthen` is a **design choice**, made to be the `fire` half of the axis rule.
It is coherent with 02's prosody: length is contrastive **only on the stressed
first syllable** (`02-phonology.yml` STR-01: "a stressed vowel may be short or
long; length is contrastive only under stress"), and every delivered root is
stressed on its first syllable, so doubling the first nucleus is the one
length operation the language can spell. The forecast's own §4 recorded the same
fact: "the length mark … is held, not licensed" (`design-language.md:178-184`).

**`lengthen` on a base whose first nucleus is a diphthong or long vowel is
undefined by this rule** and no delivered base in §1 has one — but `sau`, `dau`,
`hai` are vowel-final roots in the delivered lexicon, so the limit is declared
in `rules.md` §4 rather than left to be discovered.

## 3. Era scoping and the control

Every register form is `available_from: E1`, `stage: E1` (design.md §5; the
stamp-house is an E1 institution, `03-orthography.yml:57`). The control the
forecast's Δ5 asked for:

| # | control | fixture | expected |
|---|---|---|---|
| C-E1 | a `stamp` form dated `E0` (before the register exists) | `.scratch/r26-d-reg/ctrl-early-era.yml` | `D4L-ERA` FAIL |
| C-E2 | a `stamp` form dated `E1` | the probe | no era finding |

The era leg is **not implemented** in the delivered argot gate (it has no era
concept; `review.md` §6), so C-E1 currently produces **no finding**. That is a
named gap, not a pass: the mechanism exists in the design (`rules.md` §5) and
has no executable owner yet.

## 4. The probe and its receipt

The probe is the **delivered packet plus the 8 records**, built by a text
transform of the delivered bytes (never a re-serialization):

```
$ python3 .scratch/r26-d-reg/probe2.py     # builds .scratch/r26-d-reg/probe.yml
probe bytes: 85084
```

| # | command | result | exit |
|---|---|---|---|
| R-1 | `python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/probe.yml` | `derived_pairs=8 violations=0 rule_holds=6` — the 6 `lengthen` rows HOLD because `lengthen` is undeclared | 1 |
| R-2 | same over `probe-rule2.yml` (the `LENGTHEN` pattern/output pair declared) | `derived_pairs=8 violations=0 rule_holds=0` | **0** |
| R-3 | same over `probe-bad.yml` (`kit` mutated to `kat`) | `FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form RF-02 'kat' (register 'stamp'): declared chain 'reverse' applied to 'tik' yields 'kit'` | 1 |
| R-4 | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` (baseline) | `register_scoped=6 derived_pairs=0` — the delivered tree carries **no** register form | 0 |

R-2 is the decisive receipt: **with the operation declared, the whole register
stratum replays clean and the leg exits 0.** R-3 is the forecast's required
control C-02 (`design-brief.md:456`) firing.

## 5. Register law rows (the 8 records also need the law that governs them)

The forms are inert without the admissibility rule. Stated here as records the
register-contract owner must realize (design.md §6):

| id | rule | axis |
|---|---|---|
| RGL-01 | a `stamp` form is admissible only in a stamp-act slot (charge at the weigh-stone, attested oath, lot sealed under the mark) | mark |
| RGL-02 | an oath spoken in `stamp` is **void**; the binding oath is plain (`L-30 gis` is a `mark`-axis plain word, `04-lexicon.yml:160`) | mark |
| RGL-03 | a guest broker may speak `stamp` under a stamp-name but may not keep the furnace roll | mark |
| RGL-04 | the register owns no segment: a `stamp` form is inventory-checked exactly as a plain form | fire |
| RGL-05 | every `stamp` form is `available_from: E1`; an E0 claim is a defect | mark |

These are design statements. RGL-02 is the forecast's Δ6 property of kind
`register` (`design-brief.md:342-355`), re-hosted on the furnace-league's
attestation institution.

## 6. Calibration

- **CAL-1 (design-choice).** All 8 forms and both operations are design choices
  calibrated to the delivered spine. No frequency, corpus, or informant
  measurement exists for any of them.
- **CAL-2 (design-choice).** The axis→operation rule is a design choice with a
  measured cost (13 of 54 lexicon forms unusable, `review.md` §3); it was
  preferred over a hand-picked base list because it is total over the delivered
  tree and machine-checkable.
- **CAL-3 (to-verify).** Whether the register should exist at E1 or E2 is a
  judgment on the stamp-house's institutional date; E1 follows
  `03-orthography.yml:57`, and a reader who reads that seam differently moves
  the window with it.
- **CAL-4 (to-verify).** No real-language resemblance screening has been run on
  `tuum`, `kit`, `lom`, `nees`, `huum`, `mees`, `reek`, `saam`; no clearance is
  claimed (`05-naming.yml:CC-03` is the standing unresolved row).

## 7. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/r26-d-reg/probe2.py
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/probe.yml
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/probe-rule2.yml
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/probe-bad.yml
sha256sum .scratch/r26-d-reg/forms.json .scratch/r26-d-reg/probe.yml
```
