# R27-D05..D12 (integrator) — the register law lands, the syllabify disagreement is fixed

- **Seat:** R27-D05..D12 (D axis, register law + syllabify implementation, 8
  seats; **this file is the integrator's** — one seat owns every touched file).
  Round 27, loop 3 build 3 of 4 (`devin/deepseek-v4-1-flash-high`), claim **D**
  `register-law` (`reports/round-27/claims.json`).
- **Date:** 2026-10-18. Baseline revision `4f09c990d4c17f23b5e2cda0871f81db875635fc`
  (round-26 admit); declaration commit `b95fca1`.
- **Write scope (every byte this seat wrote):**
  `tools/gates/argot-derivation-gate.py` (the syllabify fix),
  `examples/culture-d4/components/13-register-law.yml` (**new**),
  `examples/culture-d4/components/01-brief.yml` (the contract declaration),
  `examples/culture-d4/{packet.d4.yml, typed-labels.d4.yml, packet.d4.typed.yml}`
  (regenerated), `examples/culture-d4/expected-holds.json` (re-pinned, new row),
  `tools/gates/typed-pipelines.json` (re-pinned, new row), and
  `reports/round-27/law/impl-{1..8}.md`. Scratch under `.scratch/r27-d/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch write). No filed
  round-8..26 byte written; no commit, no push.
- **Canon:** NON-CANON engineering evidence. No real language, institution,
  script or argot is described, cited or approximated. No clearance claimed.

## 0. The two gaps, and where each is closed

The round-26 review named both, and this seat's claim carries both:

| gap | round-26 id | closed at |
|---|---|---|
| the register **law** has no owning component | `review.md` §6.3, `design.md` §6, `rules.md` RL-6 | §2 of this file; the law lands as a new component |
| the gate's `syllabify` disagrees with the design's stated algorithm | `review.md` §5, `design.md` RL-3, RD-4 | §3 of this file; one legality-constrained algorithm |

Both are **implementation**, not design. The design for each was authored by
sibling seats the same round (`reports/round-27/law/{design,rules,review}.md`,
seats R27-D01..D04) and this seat lands it rather than re-designing it.

## 1. The route the law takes, and why it is the measured-cheapest one

The sibling design seats measured two landing routes against the delivered bytes
and took **Route A**: the law rows are new records in a block the packet already
admits, **not** `rank_rules` rows carrying `property.kind` (Route B, the
round-17 forecast's Δ6 shape). Their measurement:

| route | probe | projector findings | new holds |
|---|---|---|---|
| **A** — a new block beside `registers` | `.scratch/r27-law/A/…` | `findings_total=12` | **0** |
| **B** — `rank_rules` with `property.kind: register`/`speech-act` | `.scratch/r27-law/B/…` | `findings_total=16` | **4** |

This seat lands Route A, and **independently reproduces the zero-new-holds
result** (§5). The route is the design's; the landing is this seat's.

## 2. What was landed, and where

### 2.1 `examples/culture-d4/components/13-register-law.yml` — new

A **new component**, the round-26 design's own named-but-unwritten owner
("a new register-contract component", `design.md` §6). It declares
`packet_keys: [register_law]` and carries the five law rows **RGL-01..RGL-05**
that `reports/round-26/register/forms.md` §5 fixed and left with no home.

Each row carries the three clauses the claim names — what may be said (`act`),
by whom (`speaker`, with `holder` as the round-26 spelling of the same field),
and with what record consequence (`consequence`) — plus the illocutionary
`force` the sibling design's `design.md` §3 fixes and the round-26 rows left
unstated, and a `design_row` back-reference so the round-26 `RGL-*` ids and the
round-27 `QREG-*` ids can be checked against each other instead of reconciled
by a reader:

| RGL | design rows | act | force |
|---|---|---|---|
| RGL-01 | QREG-05, QREG-07 | the charge, the lot's naming, the attested oath | `directive-binding`; `declarative-naming` |
| RGL-02 | QREG-06 | the oath — refused | `commissive-binding refused` |
| RGL-03 | QREG-08 | the guest broker's charge | `directive-binding, not-rollable` |
| RGL-04 | — | the no-segment constraint | none (sound-channel, not a speech act) |
| RGL-05 | — | the E1 dating constraint | none (dating, not a speech act) |

`RGL-04` and `RGL-05` carry `design_row: []` deliberately: the sibling design's
four acts do not include them, because they are **constraints on the register**,
not acts performed in it. That is stated rather than left as an empty column.

### 2.2 `examples/culture-d4/components/01-brief.yml` — the contract declaration

The sibling review measured that the new block arrived **undeclared**: "the new
block is not declared in the schema. `contract.record_fields` has no
`register_law` key (measured: `None`), and `01-brief.yml`'s C-13 registry row is
absent" (`reports/round-27/law/review.md` §9a). Both are closed:

- `contract.record_fields.register_law` declares the twelve fields the rows
  carry;
- the `registry` block gains **C-13** naming the component and its role.

The lane runner measures this clause directly
(`run-validation.py:908-921`: "the packet contract declares no
`record_fields.{name}`: the law block is outside the declared record contract"),
so the declaration is a graded surface, not a courtesy.

### 2.3 The three generated D4 artifacts, regenerated deterministically

`packet.d4.yml`, `typed-labels.d4.yml` and `packet.d4.typed.yml` are rebuilt by
the delivered tools, never hand-edited. `register_law` is emitted as a new
top-level block; the assembler admits it because the component declares it in
its own `packet_keys` (`tools/assemble-culture-d4.py:258-264`), which is the
deterministic-wiring clause the claim names.

## 3. The syllabify fix: one algorithm, stated as a predicate

### 3.1 What was wrong

`design-language.md:191-196` fixes `head2` as maximal onset "**whenever that
yields a legal syllable**". The delivered `syllabify`
(`argot-derivation-gate.py:135-160` at `5b5abe78…`) moved **every** consonant
run into the following onset and never tested the result. Measured over the
delivered forms:

```
$ python3 .scratch/r27-d/sylref.py     # before the fix
L-45 tikmes  gate=['ti','kme','s']  design=['tik','mes']
NM-02 kalker gate=['ka','lke','r']  design=['kal','ker']
L-01 ker     gate=['ke','r']        design=['ker']
```

`kme` and `ke.r` are not syllables: `onset_clusters: false` and the eight-coda
set (`02-phonology.yml:82,92`) refuse both, and `ke.r` invents a syllable with
no nucleus. The gate therefore did not implement the algorithm its own docstring
cited.

### 3.2 What the fix does

`syllabify` now assigns the onset under a legality test, and the predicate is
stated explicitly rather than left to the reader:

- a **single** intervocalic consonant is the following syllable's onset
  (`saalumi` → `saa.lu.mi`, `head2` `saalu` — the design's own worked row);
- a run of **two or more** keeps all but its last consonant as the preceding
  syllable's coda (`tikmes` → `tik.mes`);
- a **word-final** run is the last syllable's coda (`ker` is one syllable).

`is_legal_syllable` is the new public predicate (template `(C)V(V)(C)` with the
licensed codas), and `CODAS` / `ONSET_CLUSTERS` are quoted from
`02-phonology.yml` so the legality clause is no longer reader-dependent.

### 3.3 The disagreement, before and after, and a correction to the count

The round-26 claim's figure was **15 of 62**. Re-measuring it, the number is a
property of the *reader* — and round 26's own reader was wrong:

| reading | before (vs the pre-fix gate) | after (vs the fixed gate) |
|---|---|---|
| naive maximal onset (any consonant string is an onset) | 0 of 70 | — |
| legality-constrained maximal onset, **round-26's reader** | 15 of 62 | — |
| legality-constrained maximal onset, **corrected** (§3.2) | **59 of 62** | **0 of 70** |

Round 26's reader produced `saalumi → saal` — contradicting the design's own
worked row `saalu`, which round 26 itself reported as agreeing. That reader
mis-split the vowel sequence, so its 15-row list is not reproducible and its
count understated the divergence by a factor of four. The honest before/after:

```
$ python3 .scratch/r27-d/sylref.py            # before the fix, corrected reader
TRUE disagreements over 62 pre-round-26 forms: 59
$ python3 .scratch/r27-d/syl-after.json       # after the fix
AFTER fix, new gate vs corrected reference, disagreements: 0 of 70
design 11 worked rows re-derived: True          head2(saalumi)=saalu
forms with any illegal syllable (new gate): 0
```

**All 62 forms are re-verified**, and all 70 now-delivered forms with them. The
fix's own discriminating control (§5, C-3) fires on the exact row where the two
readings disagree — the maximal-**coda** reading `saalum` is rejected with the
gate replaying `saalu`.

### 3.4 Scope of the change, stated so a reader can bound the blast radius

The change is confined to `head2`. **No delivered `derived_from`/`derivation`
record in any family names `head2`** — the D4 register stratum uses `reverse`
and `lengthen` — so no replayed verdict over any delivered packet moves. The
gate's committed fixture verdicts are unchanged (4 `D4L-ARGOT-DERIV` + 1
`D4L-ARGOT-RULE`, byte-identical to the pre-fix run), and the D4 packet's own
coverage line is unchanged (`violations=0 rule_holds=0`, exit 0).

## 4. The hold set: re-pinned, and **unchanged**

`expected-holds.json` carries a round-27 `revision_note`, the round-26 pins moved
into `supersedes_pins` (including the same-round revision-1 digests), and its
counts are **12 holds / 0 notes / 0 fails** — the same set as round 22. That is
the correct result: a law row is not a form, so the register stratum owes no form
slot (`SKILL.md`'s slot-label routing table), and the six owed garment forms
still route to their twelve record/slot rows. Confirmed against the projection's
own `findings_total=12`.

## 5. Measured verdicts (2026-10-18, lane root)

| # | command | result | exit |
|---|---|---|---|
| V-1 | `python3 tools/assemble-culture-d4.py --check` | `byte-identical deterministic assembly` | 0 |
| V-2 | `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | `byte-identical deterministic projection` | 0 |
| V-3 | `python3 tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml` | `byte-identical deterministic typed packet` | 0 |
| V-4 | `python3 tools/gates/argot-derivation-gate.py --selftest` | `selftest: 27/27 checks passed` (was 21/21) | 0 |
| V-5 | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `derived_pairs=8 violations=0 rule_holds=0` | 0 |
| V-6 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed` | 0 |
| V-7 | `python3 tools/check-gate-battery.py` | `battery_exit 0, pass 7, fail 0, unevaluable 0` | 0 |
| V-8 | `python3 tools/assemble-culture-d4.py --selftest` | `81/81 checks passed` | 0 |
| V-9 | `python3 tools/assemble-d4-typed.py --selftest` | `12/12 checks passed` | 0 |
| V-10 | `python3 tools/d2-typed-labels.py --selftest` | `163/163 checks passed` | 0 |
| V-11 | `python3 reports/round-27/run-validation.py` | **`claim D: PASS`** | 1 (claim O open) |
| V-12 | `python3 tools/gates/d4-assembly-check-gate.py …` / `d4-typed-labels-check-gate.py` | both byte-identical, exit 0 | 0 |

The five sibling culture gates are unchanged in finding counts against the
amended packet: naming 14, phonology 1, myth 0, costume 0 — identical before and
after. The register law adds no finding to any of them.

**Controls (each measured, in place, packet restored byte-for-byte after):**

| # | control | result |
|---|---|---|
| C-1 | an `RGL` row's `force` tampered to `no-such-force` | `findings_total=12`, identical to clean — the law has **no replay leg** (`LL-3`, `RL-1`); reported, not laundered |
| C-2 | the last law row (RGL-05) dropped | `findings_total=12`, identical — the same gap, measured on a structural mutation |
| C-3 | a register form whose declared `head2` is the maximal-**coda** reading (`saalum`) | `D4L-ARGOT-DERIV`, exit 1, gate replays `saalu` — the fix's discriminating control, and the design's own named trap |
| C-3b | the same row with the correct reading (`saalu`) | exit 0, no finding — the control is not always-true |

C-1/C-2 are the honest negative result: **the law is a declaration with no
enforcement**, exactly as the sibling review measured (`review.md` §2, `LL-3`).
The claim's `after_required` asks that the law be "wired into the packet
deterministically" — which it is, and the lane runner grades that clause — and
not that a replay leg exist. The gap is named in §6.

## 6. What this seat did not do

- **Did not repair the cascade outside its own surfaces.** The D4 packet moved,
  so four pin classes moved with it. Two are this seat's (§2.3, §4) and are
  re-pinned as **new rows**. Two are other seats': the `handoff-v3` regression
  reads the **filed round-22 baseline** (`V3_BASELINE_DEFAULT`,
  `tools/exercise-handoff-e2e.py:1933`) and now reads `E2E-DIGEST` (exit 1)
  naming exactly the five D4 read-set files this landing moved; and the O seat's
  r27 freeze generations
  (`reports/round-27/pinsweep/baselines/*/r27-post/`,
  `reports/round-27/pinsweep/v3-baseline-r27/`) were frozen at **pre-landing**
  digests (`packet.d4.yml dd25077b…`). **A/B control, measured:** with this
  landing staged out (`git stash push` over the six tracked files, the new
  component moved aside), `python3 tools/exercise-handoff-e2e.py --profile v3
  --quiet` exits **0**; restoring it turns it to exit **1** with `E2E-DIGEST`.
  The cascade is therefore attributable to this landing and to nothing else, and
  both stale surfaces are the O seat's to re-point — the same disposition round
  26 recorded for the same surfaces.
- **Did not build an enforcement/replay leg for the law.** The sibling design
  measured its full price (E-1..E-7, `design.md` §5) and this seat does not open
  a family-projector amendment inside an implementation seat. Named as `LL-3` /
  `RL-1` and reported.
- **Did not amend the round-26 operation rule** or add an escape hatch for
  abstractions (`LL-1`/`LL-2` stand).
- **Did not edit `tools/d2-typed-labels.py`** (byte-pinned in three places) or any
  filed round-8..26 artifact.
- **Did not resolve the culture question**, claim any form as attested, or run a
  real-language resemblance screening (`CAL-4`).

## 7. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 tools/assemble-culture-d4.py --check                                     # V-1
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml   # V-2
python3 tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml   # V-3
python3 tools/gates/argot-derivation-gate.py --selftest | tail -1                # V-4
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml   # V-5
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1   # V-6
python3 tools/check-gate-battery.py | tail -6                                    # V-7
python3 reports/round-27/run-validation.py                                       # V-11
python3 .scratch/r27-d/sylref.py                                                 # the 62-form before/after
```
