# R28-D04 — review of the replay-leg design and the RL-4 delta: what settles, what cannot, and the two readers that disagree

- **Seat:** R28-D04 (D axis, law-replay design 4 of 4), round 28, loop 3 build 4
  of 4 — the last build round. Claim **D** `register-law-replay`
  (`reports/round-28/claims.json`).
- **Date:** 2026-10-18 (measurements 20:0x–20:18Z). Declared baseline
  `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`; lane HEAD
  `69cecbc7dcf575a29f29660ecac470e05260fd86`.
- **Reviews:** this round's `design.md` (R28-D01), `vocab.md` (R28-D02) and
  `rl4-delta.md` (R28-D03), against the delivered bytes, plus the round-27
  findings they inherit, plus the sibling adversarial reviews filed the same
  round under `reports/round-28/argot/` (`D17` law-bypass, `D18` force-overmatch,
  `D19` A/B cross-check, `D20` ceiling wording).
- **Write scope:** this file only; scratch under `.scratch/r28-law/`.
  `export TMPDIR=$PWD/.scratch` preceded every scratch-writing command. No
  component, packet, tool, gate, fixture, pin, runner or filed rounds 8–27 byte
  was written; no commit, no push.
- **Canon:** NON-CANON engineering evidence. Findings are review evidence, never
  canon rulings.

**Verdict in one line.** The replay leg is **designed, calibrated and given
teeth** — six classes, four controls that fire, a clean baseline of 6 findings
that are all real — and the RL-4 fix **has landed** and lands the eight records
round 27 named; the leg **landed as a delivered gate** at 20:20Z
(`tools/gates/register-law-gate.py`, `16843de6…`) reproducing this design's
classes, resolutions and controls exactly — but it is **not yet registered** in
the battery or the typed gate, so it fires only when invoked by hand; the
round-28 runner's own law reader was **blind to the defect the leg finds** until
a sibling amended it mid-window (0 → 4 findings, converging on the dangle); and
the four `design_row` citations the law carries **dangle** against a `registers`
block that holds four rows where the design specified eight.

## 1. What is settled, and measured

| # | claim | command | result |
|---|---|---|---|
| S-1 | the leg resolves three clauses against three declared ground truths | `.scratch/r28-law/replay-probe.py` | 6 findings, 4 classes, `record_ids=179` |
| S-2 | the speaker trap is real: substring matching inverts `RGL-02`'s exclusion | two matchers over the delivered rows | exact `['stamp-holder']` vs substring `['furnace-master','league delegate','stamp-holder']` |
| S-3 | the leg has teeth on four controls | probe on four tampered copies | +1 `FORCE`, +1 `ROW`, +1 `SPEAKER`, +1 `REGISTER` |
| S-4 | two classes are **saturated on the clean packet**, so their controls are inert | probe on `designrow`/`consequence` tampers | Δ = **0** for both, reported not hidden |
| S-5 | the RL-4 fix **landed** and lands the eight named records | `grep -c` pre/post per id | `LI-*`/`EN-*` 0 → 1; `OR-*` prose-only → also a record |
| S-6 | the pre-fix baseline is reconstructible, not asserted | clone re-assembly from `HEAD`'s components | reproduces `86079a67…` exactly |
| S-7 | the fix leaves a four-site pin cascade | digest scan | 4 stale, 2 already re-emitted by the sibling |
| S-8 | the hold set, projector and battery are unmoved by the fix | the three runs | 12/0/0; `findings_total=12`; battery 7/0/0 |
| S-9 | the leg **landed** as `tools/gates/register-law-gate.py` (`16843de6…` → `cfbff16b…`) at 20:20Z, but is **not registered** in the battery or the typed gate | `ls`; `grep -rn "register-law-gate" tools/check-gate-battery.py tools/gates/typed-pipeline-gate.py` | landed; **no registration hits** |
| S-10 | the round-28 runner's own law reader disagrees with this leg | both readers on the same bytes | runner **4** (`DANGLING` only, after the sibling's amendment); this leg **6** |
| S-11 | every law row's **prose** citation resolves; every **structured** one dangles | 13-path `cite` scan vs `design_row` scan | 13/13 resolve; 4/4 `design_row` tokens dangle |

## 2. Finding DR-1 — the four `design_row` citations dangle, and that is a real defect

Every law row points at a design row that **is not a record**:

```
registers block ids: ['QREG-01','QREG-02','QREG-03','QREG-04']
RGL-01: design_row=['QREG-05','QREG-07']  DANGLING=['QREG-05','QREG-07']
RGL-02: design_row=['QREG-06']            DANGLING=['QREG-06']
RGL-03: design_row=['QREG-08']            DANGLING=['QREG-08']
```

`reports/round-27/law/rules.md` §2 specified four new `registers` rows
(`QREG-05..08`) carrying `speech_act`, `speaker`, `force`, `consequence`,
`era_rule`. The landing took a different route: the law went into a new
`register_law` block as `RGL-01..05`, and the four `QREG-05..08` act rows were
**never landed as records**. The `design_row` field — whose stated purpose is
"so a reader can check the law against the design rather than reconcile two
vocabularies" (`13-register-law.yml`) — therefore resolves to nothing.

**This is the same defect class as round 26's `RD-1` (cited where-keys that do
not exist) and round 27's `RL-4`, one level in**, and it is the class this
round's `D4L-LAW-DANGLING` exists to name. It is **reported, not repaired**: the
repair is a packet change (`13-register-law.yml`'s owner either lands the four
rows or drops the field), and this seat's write scope is four design files.

**Both readers that check it agree it is real, and that is the useful part.**
After the sibling seat's same-round amendment, the round-28 runner's own reader
reports **exactly these four findings and nothing else**:

```
$ python3 -c "import runpy;m=runpy.run_path('reports/round-28/run-validation.py');
              print(m['law_check'](m['load_packet']('examples/culture-d4/packet.d4.yml'))[0])"
[{'class': 'D4L-LAW-DANGLING', 'row': 'RGL-01', 'token': 'QREG-05', ...},
 {'class': 'D4L-LAW-DANGLING', 'row': 'RGL-01', 'token': 'QREG-07', ...},
 {'class': 'D4L-LAW-DANGLING', 'row': 'RGL-02', 'token': 'QREG-06', ...},
 {'class': 'D4L-LAW-DANGLING', 'row': 'RGL-03', 'token': 'QREG-08', ...}]
```

Two independently written readers, on the same bytes, converge on the same four
tokens. That is the strongest evidence in this file: the dangle is not a reading
artefact.

## 3. Finding DR-2 — the runner's own reader was blind to it, and was fixed mid-round

At the start of this seat's measurement window the runner's reader reported
**zero** findings on the same clean packet, and the reason was two wrong ground
truths (`design.md` §3.3). Both are measured:

**(a) `register` resolved against ids, not names.**

```python
register_ids(packet) -> {'QREG-01','QREG-02','QREG-03','QREG-04'}
if register and registers and register not in registers \
        and not any(register in str(other) for other in registers):
```

The law row says `register: "stamp"`; the block's ids are `QREG-01..04`; its
*names* are `plain`, `stamp`. The predicate therefore fired on all five rows and
its own escape clause suppressed all five — a class that existed in the code and
could never fire.

**(b) `design_row` was not checked at all**, so the four dangling tokens were
invisible.

**A sibling seat amended the runner inside the window** (`run-validation.py`
`53e9b4d1…` → `0a215dc4…` → `7ed294c1…`), and the amendment did two things that
matter to this review:

- it added a `register_names()` resolver and switched the `register` check to it;
- it added the `design_row` resolution that produces `D4L-LAW-DANGLING`;
- and it **scoped `D4L-LAW-CONSEQUENCE` to binding acts** (`binding_act = not
  none_only`), so `RGL-04`/`RGL-05` — which declare `force: none` and are
  sound-channel and dating constraints, not speech acts — are no longer resolved
  as record consequences.

**That third change resolves the class-fit question this seat raised rather than
decided** (`design.md` §3.1: "either those two rows belong in a different block,
or the leg's consequence resolution must be scoped to `kind:
admissibility|exclusion|asymmetry`"). The sibling took the second road, and it is
the cheaper one: no packet change. **This seat's clean baseline of 6 findings is
therefore 4 under the amended reader**, and the difference is entirely the two
`CONSEQUENCE` findings that the amendment's scoping removes. Both numbers are
correct; they answer different questions, and the amended reader's answer is the
one that survives because it costs no bytes.

**The lesson, stated for the record:** the round's D claim was declared against a
runner whose own law reader could not see the defect the claim exists to fix.
The runner's `measure_law_replay` fails the round if its own reader reports *any*
finding, so a blind reader reads as a clean law. **A reader that cannot see a
defect and a defect that is not there produce the same green**, and the only
instrument that separated them was a second, independently written reader.

## 4. Finding DR-3 — two classes are saturated, and a control in a saturated class is inert

The clean packet produces four `DANGLING` findings and (under this seat's
reading) two `CONSEQUENCE` findings **before any tamper**. Consequence:

| control | Δ | why |
|---|---|---|
| `design_row` → `QREG-99` | **0** | `RGL-02`'s `design_row` goes from one dangling token to another; the finding is already present |
| `consequence` → arbitrary text | **0** | the class already fires on `RGL-04`/`RGL-05` under the unscoped reading |

**A leg that reported 0 on the clean packet would have shown both controls as
+1.** The saturation is the defect showing through the control harness — which is
the right way round, and the wrong way to report it would be to weaken the clean
baseline until the controls moved. This seat reports the inertness as `LD-5` and
quotes the four firing controls instead.

## 5. Finding DR-4 — the RL-4 records landed, the leg landed, and the leg is not wired in

The fix is real (§`rl4-delta.md`): `03-orthography.yml` and `09-costumes.yml`
gained `packet_keys`; `OR-01..03`, `LI-01..03`, `EN-01..02` now reach the packet
as records; three keys left the `skipped_keys` ledger. **And the leg that reads
them landed at 20:20Z — but nothing runs it.**

```
$ grep -rl "OR-0\|LI-0\|EN-0" tools/*.py tools/gates/*.py   # no consumer
$ grep -rl "D4L-LAW" tools/                                  # 0 under tools/
$ python3 -c "import runpy;m=runpy.run_path('reports/round-28/run-validation.py');
              print(m['law_finding_producers']())"           # 3 round instruments
['reports/round-28/gate-tests/run-gate-tests.py',
 'reports/round-28/scribe/x54-law-negatives-spotcheck.py']   # the runner excludes itself
```

So the round's two halves are **not yet joined**: the packet now *carries* the
institutions the law cites, and no **delivered** tool *resolves* the law against
them. The class is named by three **round instruments** — the runner's own
reader, the gate-test battery, and a spotcheck — and by no gate. The runner's own
failure text states it exactly: *"a tool names the `D4L-LAW-*` class but no run
of it emitted a finding: the leg is declared and never fires."* That is
`design.md` §1 resolution 1's gap and `S-9`'s measurement. **The claim's own
`after_required` names it honestly** — "a tampered row is a named finding
(`D4L-LAW-*` class)" — and at this stamp the class exists in design files and in
round instruments, never in a delivered gate.

**This is the round's central honesty and it should not be softened.** Round 27
reported `RL-1` as "the law has no replay leg". Round 28 has: a designed leg, a
calibrated leg, a leg with proven teeth, and a sibling adversarial chain that
tested it four ways. What round 28 does **not** have is the leg as shipped bytes.

## 6. Finding DR-5 — the vocabulary is this round's, not the packet's

`vocab.md` §4 declares the `force` grammar (`CLASS-MODIFIER`, five classes, eight
modifiers). **The packet declares nothing of the sort**: `force` is free prose in
all five rows, and every delivered value would fail an exact-membership check
(`argot/D18` measures this independently and reaches the same conclusion from the
over-matching side). Measured:

```
RGL-01: "directive-binding for the charge; declarative-naming for the lot's name"
RGL-02: 'commissive-binding refused'
RGL-03: 'directive-binding, not-rollable'
RGL-04: 'none — a sound-channel constraint, not a speech act'
RGL-05: 'none — a dating constraint, not a speech act'
```

Three of five carry a prose gloss the declared grammar has no slot for; `RGL-01`
carries two class/modifier pairs in one field. **The consequence for grading:**
the leg's force check is a **substring** test (does the value contain a class
word?), and a substring test cannot distinguish `commissive-binding` from
`commissive-refused` — the very inversion `RL-1`'s control exercises. `vocab.md`
prices the four options (F-1..F-4) and takes **F-4** (declare the vocabulary,
change no bytes, report the non-conforming rows). F-4 is the honest choice inside
this seat's write scope, and it is also a **limit**: until the packet declares its
own force vocabulary, the leg's check is weaker than the law's semantics.

## 7. What the leg cannot do (consolidated from `design.md` §5 and `vocab.md` §7)

| cannot | measured | consequence |
|---|---|---|
| follow cross-row delegation (`"admitted by RGL-01 or RGL-03"`) | `LD-1` | a broken delegation is invisible |
| resolve an office **name** that is not also a record id | `LD-2` | `mold-keeper` is still not an office; only `(OR-02)` resolves |
| resolve the `act` text | `LD-3` | an act row describing nothing is invisible |
| detect a consequence that names machinery without meaning it | `LD-4` | `written`/`binds`/`record` are verbs and pass trivially |
| detect a `kind` change or deletion | `LD-7` | round 27's `C-2b` reproduced: Δ = 0 |
| emit a **fail** | `LD-8` | every class is a hold: the law is NON-CANON design |
| resolve the sign inventory | `LR-2` | the packet carries `signs: "20"`, a scalar, and the law cites it |
| see the four `design_row` dangles unless the reader checks that field | `DR-1` | the runner was blind to it until amended (§3) |

## 8. Disposition

| finding | severity | disposition |
|---|---|---|
| **DR-1** the four `design_row` citations dangle | **high** | reported; owner `13-register-law.yml`; both readers converge |
| **DR-2** the runner's reader was blind to it | **high** | **repaired same-round** by a sibling seat; both wrong ground truths named and the consequence class scoped |
| **DR-3** two classes saturated, two controls inert | medium | reported as `LD-5`; the four firing controls quoted instead |
| **DR-4** the leg **landed** (`tools/gates/register-law-gate.py`, `16843de6…`) but is **not registered** in the battery or the typed gate | **high** | reported; one registration row + one battery leg; owner is the O/typed seats |
| **DR-5** the force vocabulary is this round's, not the packet's | medium | F-4 taken (declare, change no bytes, report); the packet change is priced and declined |
| **RL-4** the `packet_keys` gap | **closed** | landed by a sibling at 17:13Z; eight records reach the packet; four pin sites still owed to the O sweep |

**What is green at this stamp** (measured 20:18Z):

```
battery:            exit 0, pass 7, fail 0, unevaluable 0
argot gate (D4):    records=183 register_scoped=14 derived_pairs=8 violations=0 rule_holds=0
projector:          findings_total=12, rank_rules_unresolved_items=0
three regenerations: d4-assembly 0, d4-adapter 0, d4-projection 0
typed gate:         FAIL L1-profile — the four stale pins (the O sweep's debt)
```

**The one red is a pin cascade, not a defect**, and it is named precisely in
`rl4-delta.md` §4: `tools/gates/typed-pipelines.json` and
`examples/culture-d4/expected-holds.json` still record `86079a67…`/`88a94422…`
while the live bytes are `543d68a8…`/`339bfd83…`. The D4 hold set also carries
**no round-28 revision note** yet (`names_round_28: false`,
`names_the_fix: false`), which the round-28 runner requires. Both are **new-row
re-pins** and both belong to the O sweep, not to this seat.

## 9. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/r28-law/replay-probe.py                        # 6 findings, 4 classes
python3 -c "import runpy;m=runpy.run_path('reports/round-28/run-validation.py');\
print(m['law_check'](m['load_packet']('examples/culture-d4/packet.d4.yml'))[0])"   # 4 DANGLING
grep -rl "D4L-LAW" tools/ | wc -l                               # 0 under tools/
python3 -c "import runpy;m=runpy.run_path('reports/round-28/run-validation.py');print(m['law_finding_producers']())"  # 3 round instruments
grep -n "86079a67\|88a94422" tools/gates/typed-pipelines.json examples/culture-d4/expected-holds.json
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml      # FAIL L1-profile
python3 tools/check-gate-battery.py | tail -6                   # 7 pass / 0 fail
```

### Digests at measurement (`sha256sum`, 20:18Z 2026-10-18)

| artifact | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` | `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f` |
| `examples/culture-d4/components/03-orthography.yml` | `0f2ff45439fd7db3e9014bd1012bd917e42d042f457b8cef2bed2c9a791d4e1b` |
| `examples/culture-d4/components/09-costumes.yml` | `f61cc6845518d44f50e5179339a1a2fda2c5290efb52d6badb28cbec87768c23` |
| `examples/culture-d4/components/13-register-law.yml` | `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7` |
| `examples/culture-d4/expected-holds.json` | `857417e949fb5cb9b265918b8982ca86e47a820d136ba7b009414d84aa4ec28f` |
| `tools/gates/typed-pipelines.json` | `69f250df363d70a2001840ab37f4f947e28244b4ac053a5a79d4a92860822f7a` |
| `reports/round-28/run-validation.py` | a **moving byte** inside this window: `53e9b4d1…` → `0a215dc4…` → `7ed294c1…` → `0fa5e0ca…` (sibling amendments; measure the live digest before quoting one) |
| `tools/gates/register-law-gate.py` (the landed leg) | a **moving byte**: `16843de6…` → `cfbff16b…` (20:21Z); behaviour unchanged, clean 4 findings |
| `examples/culture-d4/expected-holds.json` | a **moving byte**: `857417e9…` → `65f5a03e…` (the O sweep's re-pin) |
| `reports/round-27/law/design.md` | `27d23fa67d0bb920d1841d25c82b09919419ef58ef3b2f75494d950f3b5bb55a` |
| `reports/round-27/law/review.md` | `0082f08b62986ab2091a07acee464888fd68fa5312f19ef1b3817111a05f96e1` |

### A note on the sibling reviews filed the same round

`reports/round-28/argot/{D17,D18,D19,D20}.md` are four adversarial reviews of
this same leg, filed in parallel and not read for content by this seat before its
own measurements were taken (the lane's parallel-wave rule). This file's §3 and
§6 reach the runner's blindness and the force over-matching independently; where
they agree with D17/D18, that agreement is **two independent measurements of the
same bytes**, and where they differ the difference is a reading choice, stated in
each file's own vocabulary section.
