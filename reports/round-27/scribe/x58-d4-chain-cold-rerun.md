# Round 27 — SCRIBE X58 — independent cold re-run of the D4 chain post-law

- **Seat:** SCRIBE X58, round 27, loop 3 build 3 of 4. Claim **D / depth**
  (register-law cold re-run leg), supporting evidence for **O / operability**
  (the frozen-row and committed-baseline sweep).
- **Assignment (verbatim):** "SCRIBE X58: independent cold re-run of the D4 chain post-law."
- **Date:** 2026-10-18. Commands run with `python3` 3.14.7. `export TMPDIR=$PWD/.scratch`
  preceded every scratch-writing command; scratch under `.scratch/x58/` (gitignored).
- **Baseline binding:** declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`
  (`reports/round-27/claims.json:5`); lane HEAD at the cold run
  `b95fca1e40f32f7346937ab6426f9ccca60e319f` (round-27 claims declared, no D/O/C
  work landed). Control revisions: `1ad491a1a4b0aef9ebdc1861dfb8237727503825`
  (round-26 declare, pre-register) and `4f09c99` (round-26 close, post-register).
- **Two states measured.** The D-seat **landed the register law mid-run** — a new
  component `13-register-law.yml`, a `register_law:` packet block, regenerated
  build products, and a rewritten `argot-derivation-gate.py` `syllabify`. So this
  fragment carries **§2–§7 at the pre-law state `b95fca1`** (the revision the
  assignment named) and **§11, the post-law re-run**, measured on a clone carrying
  the live overlay. §11 supersedes §4's and §5's conclusions; both are kept so the
  delta the law moved is visible. The two states differ on the syllabify and on
  the law's ownership, and **not** on the frozen-row surface (§11.4).
- **Write scope:** this fragment only, plus `.scratch/x58/`. No tool, packet, pin,
  validator or shared-bookkeeping edit; no Git mutation, commit or push; no filed
  round-8–26 byte written. This seat authored none of the artifacts it re-runs.
- **Method:** every execution happens inside an isolated `git clone --shared` of
  the lane under `.scratch/x58/`, never in the lane worktree, so a re-run cannot
  move the tree it measures. The round-26 X64 harness
  (`.scratch/x64/chain-cold-run.py`, `chain-controls.py`, `chain-delta.py`) is
  re-used, not rewritten; this seat adds the frozen-manifest sweep, the committed
  baseline verdict-replay, and the register-law ownership census.
- **Canon:** NON-CANON engineering evidence. A reproduced red verdict stays red;
  a pin is integrity, never truth and never clearance.

## 0. Headline

The D4 chain is **operationally green and byte-deterministic** at the revision
measured, and it **fails closed on all 12 negative controls** this seat re-ran.

Three results the round must carry:

1. **The register law is landed but has no owning component.** The packet
   declares a 4-row `registers:` block; no gate reads it, and two of its four
   rows (`QREG-02` speech-act admissibility, `QREG-04` era) have **no executable
   owner at all** — measured by a control that does not bite (§4).
2. **The published syllabify disagreement "15 of 62" is an artifact of a bug in
   the round-26 checker.** A faithful implementation of the design's own stated
   algorithm gives **12 of 70**, and the round-26 checker's own cited worked
   example does not reproduce under its own code (§5).
3. **The un-swept pin surface is red.** Four frozen manifests carry D4 rows and
   two of them are red at the revision measured; **all four committed
   `expected/` D4 baselines** record `exit 0` and re-run at `exit 1`. The control
   at three revisions separates the pre-existing red from the red the round-26
   register landing caused (§6).

## 1. The chain as re-run

The D4 chain is the three build products plus their graders:

```
examples/culture-d4/components/*.yml  (12 inputs)
  -> tools/assemble-culture-d4.py      -> packet.d4.yml
  -> tools/d2-typed-labels.py          -> typed-labels.d4.yml      (projection)
  -> tools/assemble-d4-typed.py        -> packet.d4.typed.yml      (adapter)
  -> tools/gates/typed-pipeline-gate.py   (L1..L4 + L3b-argot)
  -> tools/gates/d4-typed-labels-check-gate.py
  -> tools/gates/argot-derivation-gate.py (sibling, invoked by the typed gate)
```

Command: `python3 .scratch/x58/chain-cold-run.py --root .scratch/x58/clone-t0
--out .scratch/x58/t0-chain.json --scratch .scratch/x58/scratch-t0 --jobs 6`
(2026-10-18, revision `b95fca1`).

## 2. Cold run — every step, with exit and legs

| command | exit | legs | tool sha256 (16) | stdout sha256 (16) |
|---|---:|---:|---|---|
| `python3 tools/assemble-culture-d4.py --check` | 0 | — | `943f487ba991d45d` | `293bf19f7e6e9c70` |
| `python3 tools/assemble-culture-d4.py --selftest` | 0 | — | `943f487ba991d45d` | `0182f7178e24616d` |
| `python3 tools/d2-typed-labels.py --selftest` | 0 | 163/163 | `2819f68769dfc0b5` | `12002ae29aa64f32` |
| `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | 0 | — | `2819f68769dfc0b5` | `1c8add321259a9f0` |
| `python3 tools/assemble-d4-typed.py --selftest` | 0 | 12/12 | `92f5460bcc34ffbb` | `4945c941cd243734` |
| `python3 tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml` | 0 | — | `92f5460bcc34ffbb` | `692d476ad07f1ca6` |
| `python3 tools/gates/typed-pipeline-gate.py --selftest` | 0 | 19/19 | `b749ad07cf171027` | `35b344fce7daa4ed` |
| `python3 tools/gates/typed-pipeline-gate.py --selftest-generalized` | 0 | 16/16 | `b749ad07cf171027` | `4bc6817850c6b6be` |
| `python3 tools/gates/typed-pipeline-gate.py` | 0 | 16/16 | `b749ad07cf171027` | `15cdfbda73cd56cb` |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 | **20/20** | `b749ad07cf171027` | `3eb9042e066426fd` |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | 0 | **17/17** | `b749ad07cf171027` | `67056bb9090e437d` |
| `python3 tools/gates/d4-typed-labels-check-gate.py` | 0 | — | `05f99629d870280c` | `1c8add321259a9f0` |
| `python3 tools/gates/d4-typed-labels-check-gate.py --selftest` | 0 | 163/163 | `05f99629d870280c` | `12002ae29aa64f32` |
| `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | 0 | — | `df1a364b3970365c` | `c60820a54742ecaa` |
| `python3 tools/gates/argot-derivation-gate.py --selftest` | 0 | — | `5b5abe7865ed906c` | `c6b83ebcf1d22cd8` |
| `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | 0 | — | `5b5abe7865ed906c` | `4c29a83965f38254` |
| `python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml` | **1** | — | `d9e4e8f4f93a21b3` | `0c613c9d973f3c32` |
| `python3 tools/gates/phonology-sanity-gate.py examples/culture-d4/packet.d4.yml` | **1** | — | `d5fe087ffb2342e5` | `3a28efd5eabe6ca4` |
| `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d4/packet.d4.yml` | 0 | — | `e6bffd7020c0b116` | `e3b0c44298fc1c14` |
| `python3 tools/gates/lexicon-coverage-audit.py examples/culture-d4/packet.d4.yml` | 0 | — | `2c4dd39702a15ea3` | `e3b0c44298fc1c14` |
| `python3 tools/gates/myth-consistency-gate.py examples/culture-d4/packet.d4.yml` | 0 | — | `5368b13542cd4b8a` | `e3b0c44298fc1c14` |
| `python3 tools/gates/provenance-audit.py examples/culture-d4/packet.d4.yml` | **2** | — | `8a96aaf4ccd14ef4` | `7cc4a3d8cf9ab6e1` |

The three non-zero exits are the **standing red verdicts**, identical in kind to
round 26 and unchanged by the register landing: `naming-collision` returns 1 with
14 findings (7 `NAME-NEAR` REVIEW + 6 `PHON-INVENTORY` FAIL on the six garment
glosses + 1 `CROSS-HOLD` HOLD); `phonology-sanity` returns 1 with the `A-CLASS`
REVIEW on `notable_rules[3]`; `provenance-audit` returns 2 because the packet is
not a corpus entry document. **A reproduced red verdict stays red.**

### 2.1 The register-domain census, cold

```
coverage: examples/culture-d4/packet.d4.yml records=170 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
```

### 2.2 Pins measured at this revision (`sha256`, full digests)

| path | sha256 |
|---|---|
| `examples/culture-d4/components/01-brief.yml` | `feca7bda25beb6ec7cecd2569fe8f8d6d802ff492f40c79cb6c58fdf5ac18d7d` |
| `examples/culture-d4/components/04-lexicon.yml` | `d0d4e17cc3c43a11e598259271fe16f18539c8bce3c3a30a40b6d2554b6c7240` |
| `examples/culture-d4/expected-holds.json` | `d6136488e22f989e109c435cb4f7eb02ca680043785e88e78038ed5f47150fd3` |
| `examples/culture-d4/packet.d4.typed.yml` | `618a78c90fc04c0d17e2619d1fed080e99f98b1213ad01fcbb75e7aab48fd18c` |
| `examples/culture-d4/packet.d4.yml` | `dd25077bc01681bc17f4586b40cfdd6959d4f45fc63e4f33f13fdc9b2cc88e67` |
| `examples/culture-d4/typed-labels.d4.yml` | `d03f6391fb8dc2b4d2b2ad05e08547455bc96c580050d830ce0c7c22bb75e580` |
| `tools/assemble-culture-d4.py` | `943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2` |
| `tools/assemble-d4-typed.py` | `92f5460bcc34ffbb43a771504d213d23aafd818b39c7017c823a363e99063fd0` |
| `tools/d2-typed-labels.py` | `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` |
| `tools/gates/argot-derivation-gate.py` | `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211` |
| `tools/gates/d4-typed-labels-check-gate.py` | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` |
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` |
| `tools/gates/typed-pipelines.json` | `35946c8d71d5a023990a0e07cdde821af93f59c0e0686be240b83f0a8f6871d3` |

### 2.3 Determinism and no-write (control for the table above)

Two fresh copies produced byte-identical products: `assemble_identical=True`,
`projection_identical=True`, `typed_identical=True`. Regeneration matched the
committed bytes for all three artefacts:
`{'packet.d4.typed.yml': True, 'packet.d4.yml': True, 'typed-labels.d4.yml': True}`.
The five read-only entries (`--check` ×3, gate ×2) left every artefact
byte-identical: `unchanged=True`, `changed=[]`.

## 3. Negative controls — the chain's teeth

Command: `python3 .scratch/x58/chain-controls.py --root .scratch/x58/clone-t0
--out .scratch/x58/t0-controls.json --scratch .scratch/x58/ctl-t0`.
Each control mutates exactly one input inside its own clone copy.

| # | control | command | exit | expected | bites |
|---|---|---|---:|---|---|
| 1 | `packet-byte-tamper` | `typed-pipeline-gate.py packet.d4.yml` | 2 | [1,2] | **True** |
| 2 | `expected-holds-tamper` | `typed-pipeline-gate.py packet.d4.yml` | 2 | [1,2] | **True** |
| 3 | `projection-stale` | `typed-pipeline-gate.py packet.d4.yml` | 2 | [1,2] | **True** |
| 4 | `pipeline-pin-stale` | `typed-pipeline-gate.py packet.d4.yml` | 2 | [1,2] | **True** |
| 5 | `adapter-drift` | `assemble-d4-typed.py --check packet.d4.typed.yml` | 1 | [1] | **True** |
| 6 | `assembly-drift` | `assemble-culture-d4.py --check` | 1 | [1] | **True** |
| 7 | `argot-violating-form` | `argot-derivation-gate.py packet.d4.yml` | 1 | [1] | **True** |
| 8 | `argot-clean-positive` | `argot-derivation-gate.py packet.d4.yml` | 0 | [0] | **True** |
| 9 | `thirteenth-component-refused` | `assemble-culture-d4.py` | 2 | [2] | **True** |
| 10 | `corrupt-packet-input` | `argot-derivation-gate.py packet.d4.yml` | 2 | [2] | **True** |
| 11 | `register-violation-propagates` | `typed-pipeline-gate.py packet.d4.yml` | 2 | [1,2] | **True** |
| 12 | `register-clean-propagates` | `typed-pipeline-gate.py packet.d4.yml` | 2 | [1,2] | **True** |

**12/12 bite.** A control that does not bite is a finding, not a pass.

### 3.1 The standing battery — two duties, both green

`python3 tools/check-gate-battery.py` → `battery_exit 0, pass 7, fail 0,
unevaluable 0` (command run 2026-10-18 at `b95fca1`).

The tool runs **two** duties over **two** different gate sets, which matters for
claim O's acceptance text:

| duty | gate set | size | result |
|---|---|---:|---|
| 1 — isolated selftest battery | `GATE_NAMES` (`check-gate-battery.py:116`) | 7 | `pass 7 / fail 0` — the maximum |
| 2 — committed-baseline digest check | `REGISTERED_GATE_NAMES` (`:130`) = duty 1 + `D4_GATE_NAMES` | 9 | `coverage 9/9, pinned 19/19, unevaluable 0, baseline_exit 0` |

The two D4 adapters are in `D4_GATE_NAMES` with the source comment: "Registered
for duty-2 coverage only: each is a gate-shaped entry point whose ROOT resolves
from its own file location and whose peer lives outside `tools/gates/`, so the
duty-1 mirror cannot host it and this battery does not launch it."

**Consequence for the claim text.** "battery 9/9" is right for duty 2 and
unachievable for duty 1: `pass 7 / fail 0` **is** the ceiling, and the two D4
adapters are covered by duty 2's digest check and their own committed
`expected/` baselines. Both duties are green at this revision.

**The duty-2 green is weaker than it reads.** The tool states its own boundary in
the report: `"verdict_replay": "not-run: the battery verifies digests and pins;
the verdict comparison belongs to the baseline's own re-run receipt"`. Duty 2
checks that each `expected.json` still declares the digests the gate now has. It
never runs the baseline. §6 runs that comparison, and the D4 baselines fail it.

## 4. The register law — landed, and with no owner

**The law is in the packet.** `examples/culture-d4/packet.d4.yml:1298` carries a
4-row `registers:` block, merged from `04-lexicon.yml:244` by the assembler's
`PACKET_KEYS` allowlist (`tools/assemble-culture-d4.py:81`):

| id | title | what it declares |
|---|---|---|
| `QREG-01` | plain | the unmarked baseline, present from E0; not a member of the stratum |
| `QREG-02` | the stamp register | **the speech-act rule**: a stamp form is admissible only in a stamp-act slot (a charge at the weigh-stone, an oath attested before the stamp-holder, a lot named as it is sealed) |
| `QREG-03` | the operation rule | `axis mark -> reverse; axis fire -> lengthen` |
| `QREG-04` | era | **`era_rule`: a stamp form is available_from E1**; a stamp form claimed at E0 is a defect |

**Ownership census (measured).** Three independent structural facts:

1. **No gate reads the block.** `for f in tools/gates/*.py; do grep -q registers
   "$f" && echo READS: $f; done` → **nothing**. The only consumers of the packet
   key anywhere are the assembler (merge allowlist) and a `d2-typed-labels.py`
   docstring line. The typed gate's 20 legs contain no register-law leg.
2. **`QREG-03` is enforced only indirectly.** The argot gate replays the
   arithmetic through each record's `derived_from`/`derivation` pair — 8 pairs,
   `violations=0`. It re-derives the forms; it does not read `operation_rule`.
3. **`QREG-02` and `QREG-04` have no executable owner.**

**X58-F2 — the era leg has no teeth (control that does not bite).** `QREG-04`
states a rule with a named defect class: a stamp form claimed at E0 is a defect.
This seat built the control and ran it.

```
$ # mutate L-56 (stamp, E1) -> E0 in a scratch copy of the component tree, reassemble
$ python3 tools/assemble-culture-d4.py            # exit 0 — assembles clean
$ python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: ... records=170 register_scoped=14 derived_pairs=8 ... violations=0 rule_holds=0
                                                  # exit 0 — no finding
$ python3 tools/gates/costume-era-consistency-gate.py examples/culture-d4/packet.d4.yml
                                                  # exit 0 — no finding
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
FAIL L1-profile: packet: pins dd25077bc016, live 9ec8950a4dc3
                                                  # the ONLY thing that fires is pin staleness
```

**The control does not bite.** An E0-dated stamp form assembles clean and every
semantic gate passes it; the only refusal is the pin-drift leg, which is a
consequence of the mutation, not a verdict on the era rule. Read against claim
D's `after_required` ("a D4 component declares the stamp register's speech-act
rules … with what record consequences"), the law is **declared as data and
enforced nowhere**: `QREG-02`'s admissibility and `QREG-04`'s era rule are prose
in a block no component consumes.

## 5. The syllabify disagreement — the published number is a checker artifact

`design-language.md:191-196` fixes `head2` as **maximal-onset**: "a consonant is
taken as the onset of the following syllable **whenever that yields a legal
syllable**", and states the algorithm "because the two readings disagree, and a
derivation that is not deterministic cannot be checked."

This seat implemented that sentence faithfully (`CONS`/nucleus split, the
consonant run attached to the following syllable's onset when it yields a legal
syllable, no onset clusters, codas from the eight) and ran it against the
delivered gate's `syllabify` over every delivered form.

### 5.1 The worked-example control

| base | design-language.md §5 | faithful implementation | delivered gate |
|---|---|---|---|
| `saalumi` | `saalu` | `['saa','lu','mi']` → **`saalu`** ✓ | `['saa','lu','mi']` → `saalu` ✓ |

The faithful implementation reproduces the design's cited example. **The round-26
reimplementation does not:** `reports/round-26/register/review.md` §5's
`design_syll` gives `saalumi → saal`, contradicting its own cited authority.

### 5.2 The recount

| comparison | forms | disagreements |
|---|---:|---:|
| delivered gate vs **faithful** design algorithm | 70 | **12** |
| delivered gate vs the **round-26** reimplementation | 70 | 15 |

The round-26 reimplementation shifts the onset only when the consonant run is
**exactly one** consonant, and unconditionally consumes a trailing coda. Its 15
rows include three the faithful algorithm does not produce — `L-12 sau`,
`L-19 dau`, `L-28 hai` — where it splits a word-initial consonant into its own
syllable (`['s','a','u']`) rather than reading `sau` as one syllable. Those three
are **false positives of the checker**, and they are why the published figure
reads 15 rather than 12.

The true 12 are the consonant-run rows, and they are the real divergence:

```
L-45 tikmes  gate ['ti','kme','s']  faithful ['tik','mes']   head2 tikme vs tikmes
L-46 mesar   gate ['me','sa','r']   faithful ['me','sar']    head2 mesa  vs mesar
L-47 kalen   gate ['ka','le','n']   faithful ['ka','len']    head2 kale  vs kalen
L-48 haitun  gate ['ha','i','tu','n'] faithful ['hai','tun'] head2 hai   vs haitun
NM-01 tumhai … NM-08 salwer (the eight names)
```

**Severity, re-measured and unchanged in kind:** `gate head2 illegal: 0` — the
gate's outputs are never illegal D4 words, so the divergence manufactures no
finding on the delivered packet. It becomes load-bearing the moment any round
builds a `head2` stratum.

### 5.3 A stronger identity result

The published figure "59 of 62 forms map to themselves" is a **floor** produced
by the buggy algorithm's extra splits. Under the faithful algorithm the design's
`head2` is the **identity on 70 of 70** delivered forms (62 lexicon + 8 names) —
not one form in the delivered tree derives anything under `head2`. That is a
strictly stronger statement for the design's own decision to keep `head2`
declared-but-unused, and it removes the three apparent exceptions.

## 6. The un-swept pin surface — frozen rows and committed baselines are red

Claim O names "every frozen manifest, battery baseline, expected-holds, and
replay row that pins the D4 surfaces". This seat swept all three surfaces at
three revisions, so the red can be attributed.

Method: `tools/replay-frozen.py <MANIFEST.tsv> --json` for every manifest under
`tools/gates/frozen/`, run inside each revision's clone with
`TMPDIR` **outside** the repo (a `TMPDIR` inside the repo makes every row
`mirror_unsafe` exit 2). Committed baselines re-run from their own recorded
`command` and compared against their own `expected.exit`.

### 6.1 Frozen manifests

| manifest | `1ad491a` (r26 declare, pre-register) | `4f09c99` (r26 close, post-register) | `b95fca1` (r27 declare) |
|---|---|---|---|
| `frozen/round-18` | 1r / **1m** | **0r / 2m** | **0r / 2m** |
| `frozen/round-18/repin-d2` | 10r / 0m / 1c | 10r / 0m / 1c | 10r / 0m / 1c |
| `frozen/round-20/repin-d2` | 10r / 0m / 1c | 10r / 0m / 1c | 10r / 0m / 1c |
| `frozen/round-22/d4-repin` | 2r / 0m / 1c | **0r / 2m** / 1c | **0r / 2m** / 1c |
| `frozen/round-23/repin-d2` | 10r / 0m / 1c | 10r / 0m / 1c | 10r / 0m / 1c |
| `frozen/round-26/gate-input` | — | 4r / **2m** | 4r / **2m** |
| `frozen/round-26/post-register` | — | **6r / 0m / 0c** | **6r / 0m / 0c** |
| `frozen/round-11`, `round-3`, `round-3/attempt-1`, `round-25/gate-input` | unchanged at all three revisions | | |

*(r = reproduced, m = mismatch, c = could-not-evaluate.)*

**The attribution.** `frozen/round-18` line 3 (`d4-assembly-check-gate`) is
**green at `1ad491a` and red from `4f09c99`** — the round-26 register landing
broke it. Line 2 (`d4-typed-labels-check-gate`) is red at all three revisions:
pre-existing. `frozen/round-22/d4-repin` lines 2 and 3 move the same way.

`frozen/round-22/d4-repin` line 4 is `could-not-evaluate gate_digest_mismatch` —
the manifest pins `typed-pipeline-gate.py` at `04ad4bb4`, superseded since.

### 6.2 Committed `expected/` baselines — all four red

| baseline | recorded | `1ad491a` | `4f09c99` | `b95fca1` |
|---|---:|---|---|---|
| `expected/d4-assembly-check-gate/r19-pre` | exit 0 | **MATCH** | **RED** (1) | **RED** (1) |
| `expected/d4-typed-labels-check-gate/r19-pre` | exit 0 | **RED** (1) | **RED** (1) | **RED** (1) |
| `expected/d4-typed-labels-check-gate/r20-post` | exit 0 | **RED** (1) | **RED** (1) | **RED** (1) |
| `expected/d4-typed-labels-check-gate/r22-post` | exit 0 | **MATCH** | **RED** (1) | **RED** (1) |

Every red is `… differs from the deterministic assembly` / `… differs from the
deterministic projection`. Two of the four (`r19-pre` assembly, `r22-post`) were
green pre-register and went red at the register landing; the other two were
already red. **The round-26 landing broke the two that were green and left the
other two red; nothing has re-pinned any of the four.**

Note `expected/d4-typed-labels-check-gate/r19-pre/expected.json` pins
`tools/d2-typed-labels.py` at `0da0015f…` — a digest the projector no longer has
(`2819f687…`). Duty 2 still reads that baseline `pinned` because the pin is
self-consistent with its own recorded bytes; only a re-run reveals the staleness.

### 6.3 The mechanism, isolated

Both D4 gates re-derive from the **live component tree**, not from the input
they are handed. Isolated control — a mirror containing **only** the snapshot,
the gate invoked by absolute path, `cwd` = mirror:

```
mirror contains ONLY: ['examples/culture-d4/packet.d4.yml']
gate __file__ resolves to the REAL repo: .../tools/gates/d4-assembly-check-gate.py
observed exit: 1
stderr: examples/culture-d4/packet.d4.yml differs from the deterministic assembly
snapshot sha256: e7ecd2045ef0e5f9
live     sha256: dd25077bc01681bc
```

`d4-assembly-check-gate.py:33-34` resolves `ROOT = Path(__file__).resolve().parent.parent.parent`
and calls `ROOT / "tools/assemble-culture-d4.py"`; `d4-typed-labels-check-gate.py:33-34,49`
does the same with `--packet ROOT / PACKET`. A frozen row over a snapshot of a
**superseded** packet therefore cannot reproduce once the components move, no
matter how honest the snapshot is. This is a structural property of these two
gates, not a defect introduced by any round.

### 6.4 The gap claim O owns

The successor generation exists and is green — `frozen/round-26/post-register`,
6/6 reproduced — but it **re-pins only `typed-pipeline-gate` rows**. Its
`inputs/` carries `packet.d4.yml` and `packet.d4.typed.yml`; its `MANIFEST.tsv`
has no `d4-assembly-check-gate` and no `d4-typed-labels-check-gate` row. Grep
across every manifest finds exactly four rows naming those two gates:

```
round-18/MANIFEST.tsv:2,3          typed-labels a59990bb…   assembly e7ecd204…
round-22/d4-repin/MANIFEST.tsv:2,3 typed-labels 60b526b0…   assembly e7ecd204…
```

**No generation re-pins those two rows against the current packet `dd25077b…`,
and no `expected/` successor re-pins any of the four baselines.** That is exactly
the un-swept surface claim O describes. The successor rows, when a seat records
them, are **new rows in a new generation** (the `tools/gates/frozen/round-18/README.md`
rule: "a re-freeze is a new recording, never an in-place edit"); this fragment
names the gap and measures it, and records no row.

## 7. X58-F1 — `--emit` returns a failure exit while succeeding

`tools/d2-typed-labels.py --emit PATH` writes byte-correct output and returns
`result["exit"]` (`:3635`), which is **1** on the delivered packet.

```
$ python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --emit /tmp/x58-p2.yml
Wrote /tmp/x58-p2.yml
exit=1
$ diff /tmp/x58-p2.yml examples/culture-d4/typed-labels.d4.yml && echo IDENTICAL
IDENTICAL
```

**Control:** `--check` on the same bytes returns **0** (`:3624`, "`--check`
answers byte-identity; findings are the report's job"). So the two flags
disagree about the same bytes: `--check` says green, `--emit` says 1 while
writing a file that `--check` then passes.

**Pre-existing, not a regression:** the round-26 baselines record `project.exit
= 1` in their determinism leg at both `1ad491a` and `4f09c99`. Any driver that
reads `--emit`'s exit status as a verdict will mis-read a successful emit as a
failure.

## 7b. Cross-check against the sibling claim-O instrument

This seat is not the only one on the pin surface: `reports/round-27/audit/x61-pin-sweep.py`
(seat X61) re-derives every frozen row with its own machinery, deliberately
**not** calling `tools/replay-frozen.py`. An agreement between the two is
evidence, not a shared bug. Run by this seat, `TMPDIR=/tmp`:

| manifest | X58 (via `replay-frozen.py`) | X61 (own re-derivation) |
|---|---|---|
| `frozen/round-18` | 0r / **2m** / 0c | 0r / **2m** / 0c |
| `frozen/round-22/d4-repin` | 0r / **2m** / 1c | 0r / **2m** / 1c |
| `frozen/round-26/gate-input` | 4r / **2m** / 0c | 4r / **2m** / 0c |
| `frozen/round-26/post-register` | **6r** / 0m / 0c | **6r** / 0m / 0c |

**Full agreement on every row.** X61 adds a classification this seat's tool does
not emit: each of the six mismatches is `class: supersession (live input
moved=True)` — the live input moved under the frozen snapshot — which is the
mechanism §6.3 isolates. X61's own summary: `50/81 rows reproduced; 6 mismatch
(6 supersession, 0 drift); 25 could-not-evaluate (25 gate_digest_mismatch);
baselines 19/19 pinned`. Its TMPDIR probe reproduces §6's trap exactly:
`inside-repo: 0 reproduced, 0 mismatch, 6 could-not-evaluate (6 mirror_unsafe)`
vs `outside-repo: 6 reproduced`.

**One boundary of the corroboration.** X61's baseline duty is **digest-only by
construction** — its docstring states "A baseline is never re-executed here;
`pinned` means the digests hold", and its `19/19 pinned` agrees with the battery's
own `pinned 19/19`. So both X61 and `check-gate-battery.py` confirm the pins hold
while neither runs the baselines. §6.2's verdict replay is the leg **neither
sibling covers**: it is what turns `pinned` into the four reds. The two readings
are complementary, not contradictory.

## 8. What this seat did not do

- Did not edit any tool, gate, packet, component, pin, manifest, baseline or
  frozen row; did not commit or push. **Records no new row** — §6.4 is the
  measurement a recording seat needs, written so it does not re-derive it.
- Did not repair the syllabifier, the era leg, the register ownership, or the
  `--emit` exit. Each is another seat's file or another claim's work.
- Did not decide whether the four red baselines and two red manifests are
  acceptable debt or a defect to close. That is claim O's call.
- Did not audit the D2 chain. `frozen/round-3`, `round-3/attempt-1` and
  `round-25/gate-input` report `could-not-evaluate` at all three revisions
  (`gate_digest_mismatch` on `naming-collision-gate.py` and
  `provenance-audit.py`) — pre-existing, outside this assignment, named only so
  the sweep is not read as complete.

## 9. Reproduction

```sh
export TMPDIR=$PWD/.scratch
git clone --quiet --no-hardlinks --shared . .scratch/x58/clone-t0

# the chain (22 steps + determinism + no-write)
python3 .scratch/x58/chain-cold-run.py --root .scratch/x58/clone-t0 \
    --out .scratch/x58/t0-chain.json --scratch .scratch/x58/scratch-t0 --jobs 6

# 12 negative controls
python3 .scratch/x58/chain-controls.py --root .scratch/x58/clone-t0 \
    --out .scratch/x58/t0-controls.json --scratch .scratch/x58/ctl-t0

# delta against the round-26 pre-register baseline
python3 .scratch/x58/chain-delta.py --before .scratch/x64/pre-register-chain.json \
    --after .scratch/x58/t0-chain.json --out .scratch/x58/t0-delta.json

# frozen-manifest sweep (TMPDIR must be OUTSIDE the repo)
.scratch/x58/replay-sweep.sh "$PWD/.scratch/x58/clone-t0" "$PWD/.scratch/x58/replay-t0.jsonl"

# committed-baseline verdict replay, at each control revision
.scratch/x58/baseline-replay2.sh "$PWD/.scratch/x58/clone-pre"   # 1ad491a
.scratch/x58/baseline-replay2.sh "$PWD/.scratch/x58/clone-r26"   # 4f09c99
.scratch/x58/baseline-replay2.sh "$PWD/.scratch/x58/clone-t0"    # b95fca1

# register-law ownership census and the syllabify recount (inside a clone)
cd .scratch/x58/clone-t0 && python3 ../../x58/syl-faithful.py

# the sibling claim-O instrument, for the cross-check in section 7b
TMPDIR=/tmp python3 -B reports/round-27/audit/x61-pin-sweep.py
```

## 10. Findings index

| id | finding | severity today | owner |
|---|---|---|---|
| **X58-F1** | `d2-typed-labels.py --emit` returns exit 1 while writing byte-correct output; `--check` on the same bytes returns 0 | low — pre-existing, mis-reads a success as a failure | the projector's file |
| **X58-F2** | `QREG-04`'s era rule has no executable owner: an E0-dated stamp form assembles clean and every semantic gate passes it | medium — a declared law with no teeth | claim D (register law) |
| **X58-F3** | the published syllabify disagreement "15 of 62" is inflated by a bug in the round-26 checker; faithful recount is **12 of 70**, and the design's `head2` is the identity on **70 of 70** | medium — a published number needs correcting | the round-26 review's number |
| **X58-F4** | `QREG-02`'s speech-act admissibility has no executable owner; no gate reads `packet['registers']` | medium — the law is data no component consumes | claim D (register law) |
| **X58-F5** | 2 frozen manifests red (1 caused by the register landing, 1 pre-existing) and **all 4** committed `expected/` D4 baselines red (2 caused by the landing, 2 pre-existing); no successor row re-pins them | high — the claim-O sweep surface | claim O |
| **X58-F6** | the D4 adapters resolve `ROOT` from their own `__file__` and re-derive from the live component tree, so a frozen row over a superseded packet can never reproduce | structural — the mechanism behind F5 | named, not a defect of any round |

**Corroboration.** X58-F5's frozen-row half is independently confirmed row for
row by `reports/round-27/audit/x61-pin-sweep.py` (§7b), which re-derives every
row without calling `replay-frozen.py`. X58-F3's recount is independently
confirmed by `reports/round-27/scribe/x54-syllabify-spotcheck.md` (X54-F2, same
12-of-70 figure from different machinery). The committed-baseline verdict replay
in §6.2 is the one leg no sibling covers: X61's baseline duty and the battery's
duty 2 are both digest-only by construction, so they report `pinned 19/19` while
the four D4 baselines fail their own recorded verdicts.
| **X58-F6** | the D4 adapters resolve `ROOT` from their own `__file__` and re-derive from the live component tree, so a frozen row over a superseded packet can never reproduce | structural — the mechanism behind F5 | named, not a defect of any round |

## 11. POST-LAW re-run — the D-seat landed during this seat's window

**State measured.** The D-seat landed the register law while this fragment was
being written. `git status` at the lane now shows two modified tracked files and
one new component; the deltas are:

| file | change |
|---|---|
| `examples/culture-d4/components/13-register-law.yml` | **new component** — the law as a declared block, `packet_keys: [register_law]` |
| `examples/culture-d4/packet.d4.yml` | +76 lines: a `register_law:` block, `RGL-01..RGL-05` |
| `examples/culture-d4/packet.d4.typed.yml`, `typed-labels.d4.yml` | regenerated |
| `examples/culture-d4/expected-holds.json` | re-pinned; round-26 pins moved to `supersedes_pins`; hold set still 12/0/0 |
| `tools/gates/argot-derivation-gate.py` | rewritten `syllabify` (+`CODAS`, `ONSET_CLUSTERS`, `is_legal_syllable`) |
| `corpus/README.md` | claim-C work (not this seat's) |

**Method.** A fresh clone plus `rsync` of the live overlay (excluding `.git`,
`.scratch`), so the post-law state is measured in isolation exactly as the
pre-law state was:

```sh
git clone --quiet --no-hardlinks --shared . .scratch/x58/clone-law
rsync -a --exclude='.git' --exclude='.scratch' ./ .scratch/x58/clone-law/
python3 .scratch/x58/chain-cold-run.py --root .scratch/x58/clone-law \
    --out .scratch/x58/law-chain.json --scratch .scratch/x58/scratch-law --jobs 6
```

### 11.1 The chain at the post-law state — green, 12/12 controls bite

All 22 steps return the **same exit codes** as §2: `typed-pipeline-gate` 20/20 on
the source packet and 17/17 on the typed packet, projector 163/163, adapter 12/12,
argot selftest green, and the same three standing reds (`naming-collision` 1,
`phonology-sanity` 1, `provenance-audit` 2). Byte-determinism holds:
`regeneration_matches_committed` is `True` for all three artefacts and the
no-write control is `unchanged=True, changed=[]`.

`python3 .scratch/x58/chain-controls.py --root .scratch/x58/clone-law …` →
**12/12 bite**, the same set as §3. The register law's landing did not weaken the
chain's teeth.

Register-domain census, post-law:
`records=175 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6
violations=0 rule_holds=0` (was `records=170` pre-law; the five `register_law`
rows are the delta).

### 11.2 The law's ownership — moved, and still short of an owner

The law now exists as **structured data with a declared record consequence**,
which is a real advance on §4: `RGL-01..RGL-05` carry `kind`
(`admissibility` / `exclusion` / `asymmetry` / `no-segment` / `era`), `act`,
`holder`, `consequence`, `cite` and `follows` — i.e. *what may be said, by whom,
with what record consequence*, exactly claim D's `after_required` wording.

**But no component consumes it.** Measured at the post-law state:

```
$ for f in tools/gates/*.py tools/*.py; do n=$(grep -c "register_law\|RGL-\|admissib" "$f"); [ "$n" != 0 ] && echo "$f: $n"; done
(no output — not one tool or gate reads the block)
```

The packet carries it because `13-register-law.yml:18` declares
`packet_keys: [register_law]`, which the assembler honours **without** the key
being in `PACKET_KEYS` (`tools/assemble-culture-d4.py:258-264`). So the law is
merged, pinned and replayable — and **graded by nothing**.

**X58-F2 still stands, re-measured post-law.** The era control, re-run against
the new component tree:

```
$ # mutate L-56 (stamp, E1) -> E0, reassemble in an isolated copy
$ python3 tools/assemble-culture-d4.py                       # exit 0
$ python3 tools/gates/argot-derivation-gate.py packet.d4.yml # exit 0, violations=0
$ python3 tools/gates/costume-era-consistency-gate.py …      # exit 0, no finding
$ python3 tools/gates/typed-pipeline-gate.py …               # only FAIL is pin drift
```

`RGL-05` states "an E0 stamp claim is a defect"; `RGL-02` states "an oath spoken
in stamp is void". **Both controls assemble clean and pass every semantic gate.**
The law landed as *declaration*; the enforcement legs `RL-6` asked for are still
absent. The claim's `after_required` says "wired into the packet
deterministically" — that half holds — and "what may be said in-register, by
whom, with what record consequences", which now holds as data.

### 11.3 The syllabify — fixed on the consonant run, still wrong on the diphthong

The rewritten `syllabify` fixes the divergence §5 measured. Cold, on the live
gate:

| base | pre-law gate | **post-law gate** | faithful design algorithm |
|---|---|---|---|
| `saalumi` | `saa.lu.mi` → `saalu` | `saa.lu.mi` → `saalu` ✓ | `saalu` |
| `tikmes` | `ti.kme.s` → `tikme` | **`tik.mes` → `tikmes`** ✓ | `tikmes` |
| `kalker` | `ka.lke.r` → `kalke` | **`kal.ker` → `kalker`** ✓ | `kalker` |
| `ker` | `ke.r` | **`ker`** ✓ | `ker` |

The consonant-run rows are now **correct**, and the gate agrees with the faithful
implementation on 67 of 70 forms — down from 12 disagreements pre-law.

**X58-F7 (new, found cold) — three residual disagreements, all on the `ai`
diphthong.** The design declares its vowel sequences explicitly
(`02-phonology.yml:109,123`; `design-language.md:82,157-158`): "long vowels
(identical VV) **and the falling diphthongs `ai`, `au`**; no other sequences", and
"a syllable is an optional single onset, a nucleus (**short vowel, long vowel, or
`ai`/`au`**), and an optional single coda". The rewritten gate treats a nucleus as
at most two vowels **only when identical**:

```
$ python3 -c "… is_legal_syllable('hai') …"
  hai  legal=False      # should be True: onset h + diphthong ai
  hau  legal=False      # should be True
  saal legal=True       # long vowel — handled
```

So `hai` is read as `ha.i`, and the three delivered forms carrying `ai` disagree
with the design:

| form | post-law gate | faithful design algorithm |
|---|---|---|
| `L-48 haitun` | `['ha','i','tun']` → `hai` | `['hai','tun']` → `haitun` |
| `NM-01 tumhai` | `['tum','ha','i']` → `tumha` | `['tum','hai']` → `tumhai` |
| `NM-05 haitik` | `['ha','i','tik']` → `hai` | `['hai','tik']` → `haitik` |

The `au` case is latent, not measured: no delivered form carries `au`. The fix is
one clause — a falling diphthong is a legal nucleus alongside the identical-VV
long vowel — and the design states it in three places.

**Severity: low today, unchanged in kind from §5** — `gate head2 illegal: 0`, the
divergence manufactures no finding on the delivered packet. It is a correctness
gap against the gate's own cited authority, and it becomes load-bearing the moment
a `head2` stratum is built.

**X58-F3, restated post-law:** the published "15 of 62" remains a checker
artifact (§5) and the faithful figure is **12 of 70** pre-law; the post-law gate
cuts that to **3 of 70**, the three `ai` rows above.

### 11.4 The pin surface is unchanged by the law — and still red

Re-run at the post-law state:

| surface | pre-law `b95fca1` | post-law |
|---|---|---|
| `frozen/round-18` | 0r / **2m** | 0r / **2m** |
| `frozen/round-22/d4-repin` | 0r / **2m** / 1c | 0r / **2m** / 1c |
| `frozen/round-26/gate-input` | 4r / **2m** | 4r / **2m** |
| `frozen/round-26/post-register` | **6r** | **6r** |
| all other manifests | unchanged | unchanged |
| all four committed `expected/` D4 baselines | 4 **RED** | 4 **RED** |

**The law moved no frozen row and no baseline.** X58-F5 is therefore not
something the law landing resolves: the two red manifests and four red baselines
are still un-re-pinned after it, and the new component `13-register-law.yml` is
covered by no frozen row at all. The D-seat's own re-pin of
`expected-holds.json` (round-26 pins moved to `supersedes_pins`) is exactly the
right pattern — a new pin recorded, the old one named, not overwritten — and it is
the pattern the four baselines and two manifests still need.

### 11.5 Post-law pins (measured on the live worktree, 2026-10-18)

| path | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` | `c5441e3d0b237f331cfabe8002ad3bf4db7694e2666c21ba8c723ac66bf21f6a` |
| `examples/culture-d4/packet.d4.typed.yml` | `7dff3ea7b40af0b45f9472dec77e7b396489baa1d1f383feb20a42bf18e9f939` |
| `examples/culture-d4/typed-labels.d4.yml` | `072fa806ed78dc321107e5741dc7e365e4dff613395be1c916d60deaab77fe63` |
| `examples/culture-d4/expected-holds.json` | `b9f98381f382cbff13a1b0d2ac6edaba901ff43aef68d385305edc313997cd96` |
| `examples/culture-d4/components/13-register-law.yml` | `40f774cb7a69abae9d5914abad54d4c8b6bf63b30003b151c48ae3fbfb7dad7a` |
| `tools/gates/argot-derivation-gate.py` | `d7a3ad1a6ad1c4c5993b7d74bf8bc96326916f113a07e6472d90ceecd7faf1aa` |

Note on the pin race. When this seat took its post-law snapshot the D-seat had
**not yet re-pointed `tools/gates/typed-pipelines.json`**, which still pinned the
pre-law packet `dd25077bc016…` and projection `d03f6391fb8d…`; the typed gate
therefore failed `L1-profile` on pin drift in the §11.1 receipt. **The D-seat
re-pointed the pipeline pins during this fragment's writing** (packet
`c5441e3d…`, projection `072fa806…`, expected `b9f98381…`, with the round-26 pins
recorded under `superseded` and `repin_history` rather than overwritten), and the
live typed gate is now **20/20 legs** on the source packet and **17/17** on the
typed packet. Measured after the re-pin:

```
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
summary: 20/20 legs passed
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml
summary: 17/17 legs passed
```

So the mid-landing pin drift §11.1 records is **closed**, and the `L1-profile`
FAIL in that receipt is a snapshot of an intermediate state, not a standing
defect. **The four committed `expected/` D4 baselines and the two red frozen
manifests are not affected by this re-pin** and remain red (§11.4).

### 11.6 Post-law finding index

| id | status |
|---|---|
| **X58-F2** | **open** — `RGL-02`/`RGL-05` landed as data; still no gate enforces them (§11.2) |
| **X58-F3** | **confirmed, refined** — the faithful count is 12/70 pre-law, **3/70** post-law (§11.3) |
| **X58-F5** | **open, unchanged** — the law moved no frozen row and no baseline (§11.4) |
| **X58-F7** | **new** — the rewritten syllabifier mishandles the `ai` diphthong, disagreeing with the design on 3 of 70 forms (§11.3) |
| X58-F1, F4, F6 | unchanged; F4's ownership census is now the §11.2 measurement |
