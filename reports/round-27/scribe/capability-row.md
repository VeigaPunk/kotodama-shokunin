# R27-D21 — capability-row draft: the register law

- round: 27 (operator: loop 3 of 3, build round 3 of 4; 64 declared workers,
  `devin/deepseek-v4-1-flash-high`). Seat **R27-D21** (D-scribe 1 of 4).
- claim under draft: `reports/round-27/claims.json` claim **D**, axis `depth`,
  capability `register-law`.
- date: 2026-10-18. Declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`
  (the round-26 admit). Lane HEAD `b95fca1e40f32f7346937ab6426f9ccca60e319f`.
- **final stamp 2026-10-18T19:23:26Z.** The tree moved **five times** inside this
  seat's window (§0b). Every reading below binds to the final stamp; earlier
  stamps are named where a number changed.
- **status: DRAFT ONLY — the orchestrator admits.** This seat edits no
  `SCORECARD.md`, no `SKILL.md`, no `LOG.md`, no tool, gate, example, component
  or packet. Everything below is proposed text plus read-only receipts.
- writes: this file only, plus gitignored scratch under `.scratch/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command; the
  frozen replays themselves need `TMPDIR` **outside** the repo — §5a). No
  commit, no push. No filed artifact of rounds 8–26 was modified.
- canon: **NON-CANON engineering evidence.** A capability row records a
  demonstrated run; it is not canon, not lore acceptance, not a clearance and
  not a real-world register claim.

## 0. Verdict at this seat's final stamp

**Both round-26 gaps are closed on disk, and the row in §3.1 is landing-ready.**
The claim's `after_required` is a conjunction of six legs; **five are met, one is
met in a narrower form than the claim words, and the claim's own
`counting_command` currently returns a FAILING verdict** (§6).

| # | `after_required` leg (`claims.json:15`) | measured | evidence |
|---|---|---|---|
| 1 | a D4 component **declares the stamp register's speech-act rules** (what may be said in-register, by whom, with what record consequences) | **MET** | **NEW this round**: `examples/culture-d4/components/13-register-law.yml` (`40f774cb…`, mtime 19:21Z) carries `register_law:` with **RGL-01..05**, each row stating `act` / `holder` / `consequence` / `kind`. The five kinds are `admissibility`, `exclusion`, `asymmetry`, `no-segment`, `era`. The round-26 `registers:` block (`QREG-01..04`) is the *identity* law and is unchanged in `04-lexicon.yml` |
| 2 | **wired into the packet deterministically** | **MET** | the packet now carries a **`register_law`** key (5 rows) beside `registers` (4 rows): `python3 tools/assemble-culture-d4.py --check` → exit 0, byte-identical; `--selftest` **81/81**. The wiring path is the per-file `packet_keys: [register_law]` declaration (`13-register-law.yml:18`), which the assembler honors per file (`tools/assemble-culture-d4.py:74-79`) — **`register_law` is not in `PACKET_KEYS` and not in `RECORD_FIELDS`**, and §2.1 is the honest reading of that |
| 3 | the **syllabify disagreement fixed (one algorithm, forms re-verified)** | **MET for the legality clause; 3 `head2` rows remain** | **NEW this round**: `tools/gates/argot-derivation-gate.py` moved `5b5abe78…` → **`d7a3ad1a…`** and `syllabify` now implements the legality clause (`tikmes` → `tik.mes`, `head2` `tikmes`, not `ti.kme.s`); `--selftest` 21/21 → **27/27**. The remaining divergence is **diphthong handling**: the gate treats `ai`/`au` as two nuclei. §2 |
| 4 | the **argot gate + typed gate + assemblers all green** with the amended packet | **MET** | argot exit 0; typed gate **20/20** source + **17/17** typed with `ok L3b-argot`; both assemblers `--check` exit 0. §5 |
| 5 | **named holds updated** | **MET in the honest form: updated by re-pin, not by count** | `examples/culture-d4/expected-holds.json` moved `d6136488…` → **`b9f98381…`**; the counts are still **12 / 0 / 0**, because a register field owes no form slot. §4 |
| 6 | the claim's `counting_command` receipt | **RUNS, and reports FAILURE** | `reports/round-27/run-validation.py` (`7c8c725c…`) exists and `reports/round-27/validation.json` exists with **`acceptance_checks_passed: false`** and named D and O failures. §6 |

## 0a. The pin surface at the final stamp

All `sha256sum`, cwd = lane root, measured **2026-10-18T19:23:26Z**.

| artifact | final sha256 | moved this round? |
|---|---|---|
| `examples/culture-d4/components/13-register-law.yml` | `40f774cb7a69abae9d5914abad54d4c8b6bf63b30003b151c48ae3fbfb7dad7a` | **NEW file** |
| `examples/culture-d4/components/04-lexicon.yml` | `d0d4e17cc3c43a11e598259271fe16f18539c8bce3c3a30a40b6d2554b6c7240` | no (round-26 bytes) |
| `examples/culture-d4/components/01-brief.yml` | `feca7bda25beb6ec7cecd2569fe8f8d6d802ff492f40c79cb6c58fdf5ac18d7d` | no |
| `examples/culture-d4/packet.d4.yml` | `c5441e3d0b237f331cfabe8002ad3bf4db7694e2666c21ba8c723ac66bf21f6a` | **yes** (round-26: `e7ecd204…`) |
| `examples/culture-d4/packet.d4.typed.yml` | `7dff3ea7b40af0b45f9472dec77e7b396489baa1d1f383feb20a42bf18e9f939` | **yes** |
| `examples/culture-d4/typed-labels.d4.yml` | `072fa806ed78dc321107e5741dc7e365e4dff613395be1c916d60deaab77fe63` | **yes** |
| `examples/culture-d4/expected-holds.json` | `b9f98381f382cbff13a1b0d2ac6edaba901ff43aef68d385305edc313997cd96` | **yes** |
| `tools/gates/argot-derivation-gate.py` | `d7a3ad1a6ad1c4c5993b7d74bf8bc96326916f113a07e6472d90ceecd7faf1aa` | **yes** (was `5b5abe78…`) |
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` | no |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` | no |
| `tools/gates/d4-typed-labels-check-gate.py` | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` | no |
| `tools/gates/d4-assembly-check-gate.py` | `df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a` | no |
| `tools/gates/typed-pipelines.json` | `be3069088c3ff0f5807084e626e48df2d45da4ba7482e8b1cb9454f3494db507` | **yes** (re-pinned to the final packet/projection) |
| `tools/assemble-culture-d4.py` | `943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2` | no |
| `tools/assemble-d4-typed.py` | `92f5460bcc34ffbb43a771504d213d23aafd818b39c7017c823a363e99063fd0` | no |
| `SKILL.md` | `2d85bfea6e6a7503b4267b84fda5f393ed14e1a3f5eae108940e7fad8adb6048` | no — the round-25 rule **still** never landed |
| `reports/round-27/run-validation.py` | `7c8c725c68183b110aa78101ed0235db5bc18367aea00c872d487cfeb191b725` | **NEW file** |
| `reports/round-27/audit/x59-register-law-negatives.py` | `e86f630319c646e3aec0588d8683d78844c4d34e9b25ded34c36e98e1bf9d8ba` | **NEW file** |
| `reports/round-27/scribe/x54-syllabify-spotcheck.py` | `ee370f782c02b36b2333aaf79224a0047393d5ce3c2008b285a3eeab985165e2` | **NEW file** |

**Re-pin obligation.** Any edit to the argot gate, the typed-pipeline gate, the
projector, the adapter, the components or the packet after this stamp moves
these pins. Re-run §7 at integration and re-pin before citing any digest here.

## 0b. The tree moved five times inside this seat's window — the stamps

Recorded because a reading that hides its own drift is not a reading. All
stamps UTC, 2026-10-18.

| stamp | `packet.d4.yml` | argot gate | `typed-pipelines.json` | what moved |
|---|---|---|---|---|
| 19:14:55 (opening read) | `dd25077b…` | `5b5abe78…` | `35946c8d…` | the round-26-admit state: `registers:` present, `register_law:` absent, syllabify **not** fixed |
| 19:21:20 | `dd25077b…` | **`d7a3ad1a…`** | `35946c8d…` | **the syllabify fix lands** (a D seat's write); `13-register-law.yml` appears on disk but is **not yet merged** |
| 19:21:29 | **`c5441e3d…`** | `d7a3ad1a…` | `35946c8d…` | **the register law merges** — `register_law:` key in the packet; typed gate goes **exit 2 / `L1-profile`** (its profile still pins the old packet) |
| 19:22:54 | `c5441e3d…` | `d7a3ad1a…` | **`be3069088c3f…`** | the profile re-pin lands; typed gate green again |
| 19:23:26 (**final**) | `c5441e3d…` | `d7a3ad1a…` | `be3069088c3f…` | stable across three re-reads |

**Consequence for this file.** Every measurement quoted below was re-taken at the
final stamp. Where a number changed between stamps it is named (e.g. the argot
coverage line read `records=170` before the law merged and reads `records=175`
after). **A consumer must re-measure rather than inherit.**

## 1. What the row would assert — and what it must not

The row records a **capability**: a D4 component declares a register stratum's
speech-act law — the register's identity, what may be said in-register, by whom,
with what record consequence — in the packet's own machine-readable schema, and
the assembler merges that block into the delivered packet deterministically with
a self-check. It is **not** a claim that the register's social design is sound,
that the law is **enforced** by any gate, or that the stratum is complete.

**Admission gate.** The claim requires the law "landed … wired into the packet
deterministically". At 19:23:26Z that is **measured true** (§0 legs 1–2), and the
row is landing-ready. What the row **must not** say:

- It must **not** say the law is *enforced*. Measured at the final stamp:
  `grep -n "register_law" tools/assemble-culture-d4.py` → **no hits**. The block
  reaches the packet only through the per-file `packet_keys` declaration, and
  **no gate reads it**. The round-27 X59 audit instrument measures the toothless
  state directly (§3) and is an **audit instrument, not a lane gate**.
- It must **not** claim the law's own checker is a gate. X59's surviving finding
  is exactly that a tampered law value changes no delivered gate's findings.
- It must **not** say the syllabify question is *closed*. The legality clause is
  fixed; three `head2` rows remain because the gate treats `ai`/`au` as two
  nuclei. §2 is the measurement.
- It must **not** inherit round 26's "register law needs a future component"
  cell (`SCORECARD.md:329`). That component is on disk at
  `examples/culture-d4/components/13-register-law.yml`.

## 2. The syllabify leg: fixed for legality, open for diphthongs

**The gate moved this round.** `tools/gates/argot-derivation-gate.py`
`5b5abe78…` → `d7a3ad1a…`; `--selftest` 21/21 → **27/27**. The new `syllabify`
implements the legality clause its own docstring cites: a single intervocalic
consonant is the following syllable's onset, a run of two or more keeps all but
its last consonant as the preceding coda, and a word-final run is a coda. So
`tikmes` → `tik.mes` (was `ti.kme.s`), `kalker` → `kal.ker` (was `ka.lke.r`),
`ker` → `ker` (was `ke.r`).

**What remains.** The gate's `VOWELS = frozenset("aeiou")` has no diphthong
concept, so `haitun` → `ha.i.tun` (three syllables, `head2` `hai`) where the
design and the packet's own author-declared `syllables:` field both read
`hai.tun`. Measured three ways at the final stamp:

| witness | what it is | `head2` disagreements of 70 forms |
|---|---|---:|
| **W1** the delivered gate | executed, never re-implemented | 3 |
| **W2** the design's stated algorithm | re-implemented from `design-language.md:191-196` + the packet's own legality | 3 |
| **W3** the packet's own `syllables:` field | the 8 `names` records, authored in an earlier round | gate agrees **6/8**; design agrees **8/8** |

The three rows, identical under W1-vs-W2 and under W3:

| id | form | gate | design / W3 |
|---|---|---|---|
| `L-48` | `haitun` | `ha.i.tun` → `hai` | `hai.tun` → `haitun` |
| `NM-01` | `tumhai` | `tum.ha.i` → `tumha` | `tum.hai` → `tumhai` |
| `NM-05` | `haitik` | `ha.i.tik` → `hai` | `hai.tik` → `haitik` |

**W3 is the load-bearing witness and it is new this round.** The packet's own
`names` records carry an author-declared `syllables:` field written in an earlier
round for a different purpose. It agrees with the design's reading **8/8** and
with the gate **6/8** — an independent third party inside the artifact itself,
which neither the gate nor the design-side probe authored. That is what makes
"the gate is the odd one out" a measured claim rather than a preference.

**The round-26 figure of "15 of 62" does not survive re-derivation, and the row
must carry the reason.** Round 26 filed "15 of 62" in two files
(`register/review.md` §5, `register/design.md` RL-3); its own probe
(`.scratch/r26-d-reg/syl.py`) prints `15 of 70`, and X54 re-runs it and
reproduces `15 of 62`/`15 of 70` depending on the form set. That probe's
design-side splitter emits **nucleus-less syllables** (`mestum` →
`['m','es','t','um']`), which the design's legality clause forbids, so its count
is an instrument artifact. Under a legality-respecting reading the same form set
yields **3** (`head2`) / **6** (raw syllable lists). **The defensible number for
the row is 3 `head2` rows**, because `head2` is what the leg computes
(`op_head2`); a raw syllable-list count is instrument-dependent.

**Consequence, measured, and it is narrow.** The divergence manufactures **no**
finding on the delivered packet: every gate `head2` output is a legal D4 word
(`gate head2 illegal: 0` reproduces), and the delivered stratum uses `lengthen`
for the `fire` axis and `reverse` for `mark` — `head2` is declared-but-unused
(`packet.d4.yml:250`). So the leg is green and the defect is latent. It becomes
load-bearing the moment a round builds a `head2` stratum — which is `RL-3`.

## 3. LANDING-READY text

### 3.1 SCORECARD "Capabilities" row — the register law (**landing-ready today**)

Intended surface: `SCORECARD.md` §Capabilities, columns
`name | demonstrated behavior | command / evidence | first working`.

```markdown
| register law (D4) | A D4 component declares a register stratum's speech-act law in the packet's own schema, in two blocks: the register **identity** rows (`registers`: register, class, and the `law` naming the admissible slots and the holder) and the **speech-act** rows (`register_law`: `act`, `holder`, `consequence`, `kind` — admissibility / exclusion / asymmetry / no-segment / era). The assembler honors the component's per-file `packet_keys` declaration and merges both blocks deterministically, validating `registers[].id`; the law's own text records that the operation rule is total over the declared axis values but not total in effect (13 of 54 records yield an unusable form), and the component's `law_binding.enforcement` states in its own words that no gate executes the rows | `python3 tools/assemble-culture-d4.py --check` (exit 0, byte-identical deterministic assembly); `--selftest` 81/81; `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` (exit 0, `records=175 register_scoped=14 derived_pairs=8 violations=0 rule_holds=0`); `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` (exit 0, 20/20 legs incl. `ok L3b-argot`); `python3 reports/round-27/run-validation.py` | round 26 for the identity block (`4f09c99`); round 27 for the speech-act block (`examples/culture-d4/components/13-register-law.yml`); declared as a forecast in round 17 and named as an unowned gap in `reports/round-26/register/design.md` §6.3 |
```

Five obligations for whoever lands it:

- The row **must not** claim enforcement. Measured: `grep -n "register_law"
  tools/assemble-culture-d4.py` → no hits, and no gate reads either block. The
  independent checker is `reports/round-27/audit/x59-register-law-negatives.py`
  (`--controls` 7/7 caught) and it is **audit evidence, not a gate**.
- The row **must** name **two** first-working rounds, because the law landed in
  two pieces. Collapsing them to one round would misstate when the capability
  first worked.
- The row **must** carry the operation rule's non-totality in its own words, as
  the `QREG-03` text does.
- The row **must not** claim the speech-act block is registered in the component
  registry. Measured: `examples/culture-d4/components/01-brief.yml` has **12**
  `C-nn` registry rows and **none** for stem 13; the block reaches the packet by
  the per-file `packet_keys` path instead. That is a real bookkeeping gap the
  parent should disposition (§3.3).
- The claim's `counting_command` currently **fails** (§6). The row cites it and
  the parent must disposition that.

### 3.2 SCORECARD limits row — the syllabify residue (**NOT landing-ready as a capability**)

Do not land this as a capability. It is the honest negative that belongs beside
§3.1; the parent may land it as a limits row or fold it into §3.1's text.

```markdown
| (limits) register operation `head2` | `head2` is declared in the packet (`morphology.derivation_ops`) but **unused**: over the delivered tree it is an identity, not a derivation, so the leg never exercises it. The leg's `syllabify` also disagrees with its own cited design authority on **diphthongs**: the design and the packet's own author-declared `syllables:` field treat `ai`/`au` as one nucleus, while `tools/gates/argot-derivation-gate.py` has no diphthong concept and splits them. Measured on the 8 `names` records: the packet's own `syllables:` field agrees with the design **8/8** and with the gate **6/8**; 3 of 70 forms take a different `head2` (`L-48 haitun`, `NM-01 tumhai`, `NM-05 haitik`). No finding is manufactured today (every gate `head2` output is a legal word) because the delivered stratum uses `lengthen`/`reverse` only | `python3 reports/round-27/scribe/x54-syllabify-spotcheck.py` (three-witness receipt) | open — carried from round 26 as `RL-3`; the legality clause was fixed in round 27 (`5b5abe78…` → `d7a3ad1a…`, selftest 21/21 → 27/27) |
```

### 3.3 The bookkeeping gap this row surfaces

`examples/culture-d4/components/01-brief.yml`'s `registry` block lists 12
components (`C-01`..`C-12`). **Component 13 has no registry row**, and
`register_law` is absent from both `PACKET_KEYS` and `RECORD_FIELDS` in
`tools/assemble-culture-d4.py`. The block reaches the packet because the
assembler honors a component's own top-level `packet_keys:` list per file
(`tools/assemble-culture-d4.py:74-79`). That is a **supported** path, not a
defect — but a reader who checked only `PACKET_KEYS` would conclude the law
never merged, and the packet's `assembly.skipped_keys` records `packet_keys`
itself as skipped while `register_law` is **not** in it, which is the positive
evidence that the merge happened. The parent should decide whether to register
`C-13` and add the key to `PACKET_KEYS`/`RECORD_FIELDS`; this seat writes neither.

## 4. The named holds, measured

`examples/culture-d4/expected-holds.json` (`b9f98381f382cbff13a1b0d2ac6edaba901ff43aef68d385305edc313997cd96`)
carries `schema: kotodama-typed-pipeline-holds-v1`, `counts {hold: 12, note: 0,
fail: 0}`, a `revision_note`, and a `supersedes_pins` block. **The hold count did
not change** across the register landing, and the file's own note says why: the
register stratum owes no form slot because a register field never moves a form
off the sound-and-identity channel. So the claim's leg 5 is met in the **honest**
form: the hold **set** is unchanged by design, and what moved is the pin. The
typed pipeline's `L3-holds`/`L3-counts`/`L3-baseline-set` legs all pass (20/20).

**The `D4L-REGISTER-UNRESOLVED` hold the round-26 SKILL draft named does not
exist and must not be asserted.** `SKILL.md:151` already forbids it.

## 5. Measured controls (final stamp)

Scratch only, `TMPDIR=$PWD/.scratch`, the delivered tree untouched by this seat.

**(a) The full gate set over the amended packet.**

```sh
export TMPDIR=$PWD/.scratch
python3 tools/assemble-culture-d4.py --check                     # exit 0, byte-identical
python3 tools/assemble-culture-d4.py --selftest                  # 81/81
python3 tools/assemble-d4-typed.py --check                       # exit 0, byte-identical typed packet
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml    # exit 0
python3 tools/gates/argot-derivation-gate.py --selftest          # 27/27
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml     # exit 0, 20/20
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml  # exit 0, 17/17
python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml  # exit 0
python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml  # exit 0
python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml   # exit 1, 14 findings
python3 tools/check-gate-battery.py                              # 7 pass / 0 fail / 0 unevaluable
```

| gate | exit | verdict |
|---|---:|---|
| `assemble-culture-d4.py --check` / `--selftest` | 0 / 0 | byte-identical; 81/81 |
| `assemble-d4-typed.py --check` | 0 | byte-identical typed packet |
| `argot-derivation-gate.py` (D4) | **0** | `records=175 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` |
| `typed-pipeline-gate.py` (D4 source) | 0 | **20/20 legs**, `ok L3b-argot` |
| `typed-pipeline-gate.py` (D4 typed) | 0 | **17/17 legs**, `ok L3b-argot` |
| `d4-assembly-check-gate.py` / `d4-typed-labels-check-gate.py` | 0 / 0 | byte-identical assembly / projection |
| `naming-collision-gate.py` | **1** | **14 findings** — unchanged output sha `0c613c9d…` across both the register landing and the law landing. **A reproduced red stays red** |
| `check-gate-battery.py` | 0 | 7 pass, 0 fail, 0 unevaluable; `coverage 9/9`, `pinned 19` |

The argot coverage line's `derived_pairs=8` is the round-26 capability row's
landing gate, and it is **met** (round 26 read `derived_pairs=0`). `records`
moved `156 → 170 → 175` across the two landings as the law rows entered the
packet.

**(b) The register law's own negative control (another seat's instrument).**
`reports/round-27/audit/x59-register-law-negatives.py --controls` → **7/7
caught**. On the delivered packet it now reports the law **present** and its
residue **honest**:

```
counters: admissibility_checked=8 era_checked=8 law_rows=5 oath_checked=8
          plain_records=0 records=62 refs_checked=8 register_law_block=5
          register_rows=4 rule_checked=8 speech_act_rows=5 stamp_records=8
FINDING L6b-HOLD: a tampered law value is not a finding in any delivered gate …
                  the law is a declaration with no teeth — the enforcement leg is unowned
```

The earlier stamp read `law_rows=0 register_rows=4` with `FINDING L6-HOLD`
("declares the register IDENTITY … but no speech-act law rows"). **That finding
is now closed by the bytes**; the surviving `L6b-HOLD` is the enforcement gap,
which is true and must not be smoothed. It parses with `ruby -ryaml` rather than
the lane's loader and re-implements `reverse`/`lengthen` from the design prose,
so it is a genuine independent cross-check.

**(c) The syllabify three-witness control (§2).**
`reports/round-27/scribe/x54-syllabify-spotcheck.py` (`ee370f78…`) executes W1,
re-implements W2 from the prose, and reads W3 from the packet. This seat
independently re-derived W2 (`.scratch/r27d-syl6.py`, diphthong-aware) and got
the same 3 rows and the same 8/8 W3 agreement. An earlier seat-local probe
without diphthong handling read 9 — **that reading was wrong and is recorded
here so it is not inherited.**

**(d) `TMPDIR` trap.** The lane's usual `export TMPDIR=$PWD/.scratch` makes every
`replay-frozen` row `mirror_unsafe` exit 2 — re-measured this round by three
independent seats. §7's frozen commands use `TMPDIR=/var/tmp/kotodama-r27`.

## 6. The counting command runs — and reports failure

```sh
python3 reports/round-27/run-validation.py
# reports/round-27/validation.json → acceptance_checks_passed: false
```

`reports/round-27/run-validation.py` (`7c8c725c68183b110aa78101ed0235db5bc18367aea00c872d487cfeb191b725`,
1778 lines, mtime 19:20:30Z) and `reports/round-27/validation.json`
(`measured_at 2026-10-18T19:23:10+00:00`, `runner_sha256 7c8c725c…`) both exist.
The receipt's named failures:

| claim | failures |
|---|---|
| **C** | *(none)* |
| **D** | `the gate does not reproduce this runner's legality-forced splits: tikmes expected tik observed tikmes; kalker expected kal observed kalker; tumhai expected tum observed tumha`; `d4-gate is not green (exit 2)`; `the round-27 D artifact never records names_rd4` |
| **O** | `the battery reports pass=None fail=None unevaluable=None (expected 7/0/0)`; `the battery's registered-gate coverage is None, not 9/9`; `replay handoff-v3 is not green (exit 1)`; `Regression failed: … typed-pipeline-gate.py examples/culture-d4/packet.d4.yml (exit 2, 2026-10-18)`; `Regression failed: … exercise-handoff-e2e.py --profile v3 --quiet (exit 1, 2026-10-18)` |

`missing_dependencies: ["reports/round-27/handoff/declared-in-r5/expected.json"]`.

**Two of these are mid-write artifacts and this seat measured the green state at
the final stamp.** The `d4-gate exit 2` and `typed-pipeline exit 2` failures
match the window in §0b when `typed-pipelines.json` still pinned the pre-law
packet (`c5441e3d…` was live, `dd25077b…` was pinned): at the final stamp the
same command exits **0 at 20/20**. The battery failures (`pass=None`,
`coverage None`) are likewise the runner reading the battery while it was
mid-run.

**Three failures are NOT artifacts and must not be smoothed:**

1. **The syllabify expectation mismatch.** The runner expects `head2(tikmes) =
   tik`, while both the fixed gate and the design-side reading give `tikmes`.
   **The runner's own legality-forced splitter disagrees with the fixed gate on
   all three of §2's rows** — this is a third reading again, and it is the
   runner's, not this seat's to adjudicate. The parent must disposition it: the
   runner's expectation and the gate must be reconciled to one algorithm, which
   is exactly what the claim's leg 3 asks for and what is **not yet done**.
2. **`the round-27 D artifact never records names_rd4`** — the runner expects a
   named artifact that no D seat filed. A measured gap.
3. **`handoff-v3 exit 1`** — the v3 handoff read-set pins D4 artifacts the two
   landings moved. The O claim's surface, named in §6 of `frozen-rows.md`.

## 7. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
mkdir -p /var/tmp/kotodama-r27
sha256sum tools/gates/*.py examples/culture-d4/*.yml examples/culture-d4/*.json \
  examples/culture-d4/components/13-register-law.yml tools/gates/typed-pipelines.json
grep -c "^registers:"     examples/culture-d4/packet.d4.yml    # 1
grep -c "^register_law:"  examples/culture-d4/packet.d4.yml    # 1
grep -rn "register_law" tools/assemble-culture-d4.py           # 0 — merged via the per-file packet_keys path
grep -c "{id: C-" examples/culture-d4/components/01-brief.yml  # 12 — no row for stem 13
python3 tools/assemble-culture-d4.py --check                                     # exit 0
python3 tools/assemble-culture-d4.py --selftest 2>&1 | tail -1                   # 81/81
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml    # exit 0, derived_pairs=8
python3 tools/gates/argot-derivation-gate.py --selftest 2>&1 | tail -1           # 27/27
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1  # 20/20
python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml | tail -1 # exit 1, 14 findings
python3 tools/check-gate-battery.py                                              # 7 pass / 0 fail; coverage 9/9
python3 reports/round-27/scribe/x54-syllabify-spotcheck.py                       # 3 head2 rows; W3 8/8 design, 6/8 gate
python3 reports/round-27/audit/x59-register-law-negatives.py --controls          # 7/7 caught
python3 reports/round-27/run-validation.py                                       # validation.json: acceptance false
```

## 8. Limits

- The register law's **social** content is a design choice, not attested data;
  nothing here is a claim about any real register, institution or speech act.
- The law is **declared and merged**, not **enforced**: no lane gate reads
  `registers:` or `register_law:`. §3.1's row must say so, and §3.2/§3.3 exist
  so neither the syllabify residue nor the registry gap is absorbed into a green
  row.
- The syllabify count is **instrument-dependent**: 3 `head2` rows under the
  design's legality-and-diphthong reading (confirmed three ways), 15 under the
  round-26 probe's legality-violating reading. The load-bearing rows are
  `L-48`/`NM-01`/`NM-05` in every reading.
- Every reading binds to the digest and stamp beside it. **The tree moved five
  times in this seat's window**; a successor must re-hash before quoting.
- This file makes no claim that the round-27 D claim is met: the claim's own
  counting command returns `acceptance_checks_passed: false` with three
  non-artifact failures (§6).
