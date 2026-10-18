# R26-D04 — review of the register design: what holds, what does not, and the named gaps

- **Seat:** R26-D04 (D axis, register design 4 of 4), round 26, loop 3 build 2 of 4,
  claim **D** `register-stratum`.
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`;
  worktree HEAD `1ad491a`.
- **Reviews:** the design (`design.md`), its forms (`forms.md`) and its rules
  (`rules.md`) from seats D01–D03, against the delivered bytes.
- **Write scope:** this file only, plus gitignored scratch under
  `.scratch/r26-d-reg/`. No tool, gate, packet, component, or filed 8–25 byte
  written; no commit, no push.
- **Canon:** NON-CANON engineering evidence. Findings are review evidence, never
  canon rulings.

**Verdict in one line.** The design is **coherent and its arithmetic leg is
delivered and discriminating** — 8 of 8 forms clean, the required control
`D4L-ARGOT-DERIV` fires, and with the one new rule declared the leg exits 0 —
but it carries **three measured defects in its own claims**, **two legs of the
stratum are unimplemented**, and the **register law has no owner in the
delivered tree**.

## 1. What is delivered and measured green

| # | claim | command | result |
|---|---|---|---|
| G-1 | the argot leg exists and is green on the delivered packet | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `register_scoped=6 derived_pairs=0 violations=0`, exit 0 |
| G-2 | the leg's selftest passes | `… --selftest` | `21/21 checks passed` |
| G-3 | the typed gate passes over the delivered packet | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed`, exit 0 |
| G-4 | the standing battery is green | `python3 tools/check-gate-battery.py` | `battery_exit 0, pass 7, fail 0, unevaluable 0` |
| G-5 | the register's 8 forms replay clean once the rule is declared | `… probe-rule2.yml` | `derived_pairs=8 violations=0 rule_holds=0`, exit 0 |
| G-6 | the forecast's control C-02 fires | `… probe-bad.yml` | `D4L-ARGOT-DERIV` on `RF-02 'kat'` |

Artifact digests at measurement (`sha256sum`):

| artifact | sha256 |
|---|---|
| `tools/gates/argot-derivation-gate.py` | `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211` |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` |
| `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` |
| `examples/culture-d4/components/04-lexicon.yml` | `74c2561b7c875c7c98708c589002b85b7989fc64bafa6abf794210401c69a9a5` |
| `examples/culture-d4/expected-holds.json` | `3826ba68d705b3c379b2a12737c14075d9095a1ba2aa2eb525de1851a9ecd2f7` |
| `reports/round-17/d4/design-language.md` | `cfc2d698559ed552c85b527c3a34e32e4fe308cfd093137483f9d3c782b462cc` |
| `reports/round-17/d4/design-brief.md` | `a5fdc84dfe3f98e92068e2737f6447c9adec82ff669914b3e22963ee8447e78f` |

## 2. Finding RD-1 — the forecast's where-keys do not exist in the delivered tree

The forecast's argot design names `AL-01..AL-06`, `GD-01..GD-06`, `QN-01`, and
the `D4-Xnn` measure/numeral series. Measured:

```
$ grep -rl "AL-0" examples/ | wc -l          # 1 — inside "CAL-01", unrelated
$ grep -rl "D4-X" examples/ tools/ | wc -l   # 0
$ grep -c "registers\|doublets" examples/culture-d4/packet.d4.yml   # 0
```

**Consequence.** The register stratum cannot be reconciled by re-lettering. It
had to be re-hosted on the furnace-league's own record set (design.md §1). The
route taken (round-25 delta §4 Δ-step 7 route (i)) is the one the brief seat
named and the only one that does not supersede a shipped component. **Not a
defect of this design; a defect of the forecast's addressability**, recorded so
no reader thinks the `AL-`/`GD-` rows were dropped.

## 3. Finding RD-2 — the axis→operation rule is not total (13 of 54 unusable)

The rule (`rules.md` §2) is total over the axis space and **not total in
effect**. Measured over all 54 delivered lexicon records:

```
$ python3 .scratch/r26-d-reg/axisrule.py
usable stamp forms: 41 of 54
unusable: [('L-01','ker','rek','collides-delivered'),
           ('L-05','mam','mam','collides-delivered'),
           ('L-06','tat','tat','collides-delivered'),
           ('L-07','nun','nun','collides-delivered'),
           ('L-08','wak','kaw','illegal'), ('L-15','wer','rew','illegal'),
           ('L-17','bek','keb','illegal'), ('L-24','wat','taw','illegal'),
           ('L-26','gim','mig','illegal'), ('L-30','gis','sig','illegal'),
           ('L-44','wad','daw','illegal'), ('L-49','sal','las','collides-D2'),
           ('L-51','gul','lug','illegal')]
```

Two failure modes, both structural:

1. **Illegal** (7 records): `reverse` puts an unlicensed coda or a bad cluster in
   the onset — `wak → kaw`, `gim → mig`, `gul → lug`. This is the forecast's own
   spellability law biting (`design-language.md:216-219`: "a derivation the
   language cannot spell is not a derivation, it is a defect").
2. **Colliding** (5 records): the derived form equals a delivered form
   (`mam → mam`, `tat → tat`, `nun → nun` are palindromes; `ker → rek` and
   `sal → las` name other delivered lexemes). A collision would be a `D4L-DATA`
   class defect.

**Disposition.** Named, not repaired. The 8 forms in `forms.md` §1 were chosen to
avoid both classes, and the rule's cost is declared as `RL-1`. A later round
that wants a larger stratum must either accept the rule's partiality (and
publish the unusable list) or add an escape hatch, which would be a rule change
requiring a recorded amendment.

## 4. Finding RD-3 — `head2` has an empty proper domain over the delivered tree

The forecast's first operation is `head2` (first two syllables). Measured over
every delivered form:

```
$ python3 .scratch/r26-d-reg/final.py
forms with >=3 syllables (maximal-onset): [('L-48','haitun',['ha','i','tun']),
                                           ('NM-01','tumhai',['tum','ha','i']),
                                           ('NM-05','haitik',['ha','i','tik'])]
count: 3 of 62
head2(form)==form (identity, not a derivation): 59 of 62
```

And over the **whole** space of legal 3-syllable compounds built from delivered
roots:

```
distinct head2 values over the >=3-syllable compound space: 3
  head2=dau from dauker (dau+ker)
  head2=hai from haiker (hai+ker)
  head2=sau from sauker (sau+ker)
every head2 value is itself a delivered form: True
```

**Consequence.** A stratum built on `head2` would be a stratum of unchanged
words: 59 of 62 forms map to themselves, and the entire 3-syllable space
collapses to 3 values (`dau`, `hai`, `sau`) that are already delivered lexemes.
That is why this design uses `lengthen` for the `fire` axis and keeps `head2`
only as a declared-but-unused operation (`rules.md` §3.2). The forecast's own
worked row survives — `head2(saalumi) = saalu` reproduces under both the gate's
syllabifier and the design's — but `saalumi` is a weigh-court form that is not
in the delivered tree.

## 5. Finding RD-4 — the gate's syllabifier disagrees with the design's stated algorithm

`design-language.md:191-196` fixes `head2` as maximal-onset: "a consonant is
taken as the onset of the following syllable **whenever that yields a legal
syllable**". The gate's `syllabify` implements a simpler maximal-onset that
never checks legality. Measured:

```
$ python3 .scratch/r26-d-reg/syl.py
disagreements: 15 of 62
L-45 tikmes  gate_syl=['ti','kme','s']   gate_head2=tikme  design_head2=tik
NM-02 kalker gate_syl=['ka','lke','r']   gate_head2=kalke  design_head2=kal
…
```

The gate's outputs are never *illegal* (`kme` is a cluster-bearing "syllable"
only because the gate does not validate), so the divergence does not manufacture
a finding on the delivered packet — `gate head2 illegal: 0`. But it does mean
**the gate does not implement the algorithm its own docstring cites**
(`argot-derivation-gate.py:55-56, 125, 136-140`), and a family that relies on `head2` would
be graded against a different algorithm than its design declares.

**Disposition.** Reported, not repaired (the gate is not this design's file).
Severity: low today, because the design does not use `head2`; it becomes load
bearing the moment any round builds a `head2` stratum. Named as `RL-3`.

## 6. Finding RD-5 — two legs of the stratum are unimplemented, and the register law has no owner

### 6.1 The typing leg (independently confirmed)

The reviewer seat D22 (`reports/round-26/argot/D22-label-typing-crosscheck.md`)
measured that the leg treats every register value as an argot register and
grades glosses. **This design re-measured the same control independently:**

```
$ python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/ctrl-gloss.yml
coverage: … records=165 register_scoped=15 derived_pairs=8 … violations=0 rule_holds=6
findings naming RF-90: NONE
$ python3 tools/d2-typed-labels.py --packet .scratch/r26-d-reg/ctrl-gloss.yml
FINDING D2L-NATIVE: [fail] RF-90 — supplied form 'wool coat' carries symbols outside
  the declared inventory: ['c']
```

Same bytes, two gates: the projector **fails** the gloss, the argot leg
**passes** it and counts it as a register-scoped form. The label-typing table
(`SKILL.md:31-84`) is the governing rule; the argot leg does not implement it.
**Consequence for this design:** every form in `forms.md` §1 is inventory-legal
and syllable-legal, so the stratum as designed does not depend on the missing
typing leg — but a *later* stratum record that is not would pass silently.

### 6.2 The era leg

`rules.md` §5's REGISTER-ERA-01 is specified and has no executable owner:
`ctrl-early-era.yml` (every `stage: E1` → `E0`) produces **no era finding**.
Measured in §3 of `rules.md`. Named as `RL-8`.

### 6.3 The register law

The delivered tree has **no component that owns a register law**. The forecast's
`06-register-contract.yml` was re-planned away (round-25 delta A-8); the landed
12 components are the D2/D3 family stems. The five law rows in `forms.md` §5
(RGL-01..RGL-05) are design statements with no home. `packet_keys` admits
`registers` and `doublets` (`tools/assemble-culture-d4.py:81,118`), so the
landing is additive — but **someone must own it**, and this design names the
owner without writing the component (`design.md` §6).

## 7. Finding RD-6 — the `D4L-ARGOT-DERIV` / `D4L-ARGOT-DERV` spelling split

The assignment's claim text names the violation id `D4L-ARGOT-DERV`; the
round-17 design (`design-brief.md:308`) and the delivered gate both use
`D4L-ARGOT-DERIV`. Census:

```
$ for id in D4L-ARGOT-DERIV D4L-ARGOT-DERV; do …
D4L-ARGOT-DERIV      examples=0 tools=5 r17=2 r25=32 r26=20
D4L-ARGOT-DERV       examples=0 tools=0 r17=0 r25=2  r26=6
```

The delivered id is `D4L-ARGOT-DERIV` and **no code path emits `D4L-ARGOT-DERV`**.
The short spelling appears only in the round-25/26 assignment prose. Recorded so
a reader searching the claim text for the id finds the right one: **the live id
is `D4L-ARGOT-DERIV`**; `D4L-ARGOT-DERV` is an assignment-text variant with zero
producers. A consumer matching the claim text literally would find nothing.

## 8. Summary table

| id | finding | severity | disposition |
|---|---|---|---|
| RD-1 | the forecast's where-keys are absent from the delivered tree | structural | re-hosted on the furnace-league; recorded |
| RD-2 | the axis→operation rule is not total (13 of 54 unusable) | design cost | declared `RL-1`; 8 clean forms chosen |
| RD-3 | `head2` has an empty proper domain (59/62 identity) | forecast defect | `lengthen` used instead; `head2` declared-but-unused |
| RD-4 | the gate's syllabifier disagrees with the design's stated algorithm (15/62) | low today | reported; not this design's file |
| RD-5a | the typing leg is absent (glosses pass) | medium | re-measured; stratum designed to not depend on it |
| RD-5b | the era leg is absent | medium | `RL-8`; specified, unimplemented |
| RD-5c | the register law has no owner component | structural | owner named in `design.md` §6 |
| RD-6 | `D4L-ARGOT-DERV` has zero producers; the live id is `D4L-ARGOT-DERIV` | cosmetic | recorded |

## 9. What this seat did not do

- Did not write any component, packet, tool, gate, fixture, or pin file; the
  probe packets live under `.scratch/r26-d-reg/` and were not promoted.
- Did not repair the gate's typing, era, or syllabifier legs, and did not edit
  another seat's file.
- Did not resolve the culture question (RD-1): the re-hosting choice follows the
  brief seat's own named route and the round-25 delta's recommendation, and the
  final call remains the integrator's.
- Did not claim any form as attested, and did not perform a real-language
  resemblance screening (`forms.md` CAL-4).

## 10. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml   # G-1
python3 tools/gates/argot-derivation-gate.py --selftest | tail -1               # G-2
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1   # G-3
python3 tools/check-gate-battery.py | tail -6                                   # G-4
python3 .scratch/r26-d-reg/probe2.py ; python3 .scratch/r26-d-reg/axisrule.py
python3 .scratch/r26-d-reg/syl.py ; python3 .scratch/r26-d-reg/final.py
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/ctrl-gloss.yml
python3 tools/d2-typed-labels.py --packet .scratch/r26-d-reg/ctrl-gloss.yml
```
