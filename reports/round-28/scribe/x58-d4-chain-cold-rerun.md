# Round 28 — SCRIBE X58 — independent cold re-run of the D4 chain post-law-replay

- **Seat:** SCRIBE X58, round 28, loop 3 build 4 of 4 (the last build round).
  Claim **D / depth** (the law replay leg + the RL-4 fix, cold re-run leg);
  supporting evidence for **O / operability** (the final pin sweep) and
  **C / coverage** (the ceiling as craft knowledge).
- **Assignment (verbatim):** "SCRIBE X58: independent cold re-run of the D4 chain
  post-law-replay."
- **Date:** 2026-10-18. Commands run with `python3` 3.14.7. `export
  TMPDIR=$PWD/.scratch` preceded every scratch-writing command; scratch under
  `.scratch/r28-x58/` (gitignored). All measurements at lane HEAD
  `69cecbc7dcf575a29f29660ecac470e05260fd86` (round-28 declare; the D/O/C seats
  landed into the working tree, uncommitted, during this seat's window).
- **Baseline binding:** declared baseline
  `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede` (`reports/round-28/claims.json:5`).
  Control revisions: `b95fca1` (round-27 declare), `6c0ac44` (round-27 admit).
- **Write scope:** this fragment only, plus `.scratch/r28-x58/`. No tool, packet,
  pin, gate, component, validator or shared-bookkeeping edit; no Git mutation,
  commit or push; no filed round-8–27 byte written. This seat authored none of the
  artifacts it re-runs. **Records no new row** — the successor rows named in §7
  are the O seat's; this fragment measures them.
- **Method:** every execution happens inside an isolated `git clone --shared` of
  the lane under `.scratch/r28-x58/`, never in the lane worktree, so a re-run
  cannot move the tree it measures. **One exception, found late and measured
  (§8.1, X58-R28-F6):** the round's own counting command
  `reports/round-28/run-validation.py` is **not** clone-isolated — it walks up to
  the real lane and syncs the live tree into itself, so its reading is of the live
  lane, not of the clone. Every other instrument used here — including
  `tools/replay-frozen.py`, `tools/check-gate-battery.py` and this seat's own
  probes — carries no sync code and is genuinely clone-isolated. The round-27 X58
  harness
  (`.scratch/x58/chain-cold-run.py`, `chain-controls.py`, `syl-faithful.py`,
  `replay-sweep.sh`, `baseline-replay2.sh`) is **re-used, not rewritten**; this
  seat adds one instrument — `.scratch/r28-x58/law-replay-probe.py`, an
  independent law-replay probe whose tamper routes are authored here and whose
  leg is **discovered**, not named.
- **Canon:** NON-CANON engineering evidence. A reproduced red verdict stays red;
  a pin is integrity, never truth and never clearance. This is a re-run record,
  not round acceptance; the round's own counting command is
  `python3 reports/round-28/run-validation.py` and its verdict is
  `reports/round-28/validation.json`.

## 0. Headline

The round landed **three** changes, and all three are measured here — the chain,
control, law-tamper, frozen-sweep and baseline readings from instruments with no
sync code (genuinely clone-isolated), and the counting-command reading from the
one instrument that syncs the live lane (§8.1):

1. **The law replay leg (RL-1) landed** — `tools/gates/register-law-gate.py` is
   new and emits ten `D4L-LAW-*` classes. **All five of this seat's independently
   authored tamper routes are caught with a distinct new named class** (§4). The
   leg also fires on the **clean** packet — four `D4L-LAW-DANGLING` HOLDs — and
   that is a real defect, not an over-sensitive checker (§4.3).
2. **The RL-4 `packet_keys` fix landed** — the eight record ids now reach the
   packet as *records*; `assembly.skipped_keys` no longer routes them away (§3).
3. **The pin cascade closed** — `typed-pipelines.json` re-pointed; the typed gate
   is back to **20/20** on the source packet and **17/17** on the typed one (§2).

The chain is **operationally green and byte-deterministic** and it **fails closed
on all 12 negative controls**. The round's counting command reads
`acceptance_checks_passed: true`, all three claims green, 0 failures,
`missing_dependencies: []` (§8) — measured by this seat, not read back from the O
seat's receipt. **One correction to the isolation, found late: the counting
command itself is not clone-isolated — it self-syncs the live lane (§8.1,
X58-R28-F6). Every other instrument in this fragment has no sync code and *is*
clone-isolated; §8 measures the live lane at the moment the runner executed, which
is the stronger claim but a different one.**

**Two measurement passes, because the tree moved under this seat (§1b).** The
primary receipt is `clone-final` (the state measured through 20:25Z). A watcher
then caught `tools/gates/register-law-gate.py` moving again (`cfbff16b…` →
`bbad3578…`) and `run-validation.py` moving with it (`b8f08546…` → `20e09ea8…`);
this seat re-ran the **entire** driver plus the law probe on a fresh clone
(`clone-final2`) at 20:28Z and **every reading is unchanged except the two
digests**: chain exits and legs identical, 12/12 controls bite, determinism and
no-write hold, the law leg still emits 4 `D4L-LAW-DANGLING` on the clean packet
and still catches **5/5** of this seat's tampers, the four committed baselines are
still red, and the counting command still reads `acceptance_checks_passed: true`
with all three claims green. Where a digest below names `cfbff16b…` or
`b8f08546…`, the current bytes are `bbad3578…` and `20e09ea8…`; every behavioural
reading in this fragment was re-confirmed on the newer bytes.

**Six findings this round must carry**, four of them gaps or method traps rather
than defects:

- **X58-R28-F1** — `round-27/post-register` (the frozen manifest) reads **4r/2m**
  where round 27's own X58 recorded **6r/0m**. Attributed: the manifest bytes are
  unchanged (`e2e838f3`) and it is 6r/0m at `b95fca1`, 4r/2m from `6c0ac44`. So
  **round 27's own landing broke it and round 27's sweep did not catch it** — not
  a round-28 regression (§5.2).
- **X58-R28-F2** — the O seat's successor rows (`r28-post` manifest 4/4, two
  successor baselines both MATCH) live under **`reports/round-28/pinsweep/`**, not
  under `tools/gates/frozen/` / `tools/gates/expected/` where the four red
  baselines and two red manifests actually are. The recording is drafted and
  green; the installed surface is unchanged (§7.2).
- **X58-R28-F3** — the new gate `register-law-gate.py` is registered in **neither**
  battery duty: `GATE_NAMES` (7) and `D4_GATE_NAMES` (2) both omit it, so
  `coverage 9/9` is unchanged and the round's new leg has no battery coverage
  (§7.3).
- **X58-R28-F4** — the new gate's clean-packet output is 4 `D4L-LAW-DANGLING`
  HOLDs, because `RGL-01..03` cite `design_row` ids `QREG-05..08` that were never
  landed as `registers` records. The claim's own `after_required` says a *tampered*
  row must be a named finding; it does not say the clean packet is silent, and the
  runner grades on the line-level delta — but the dangling citations are a real
  defect the round should not read as clean (§4.3).
- **X58-R28-F5** — this seat's own method note: an unanchored law-field regex
  matched `register:`/`axis:` lines **above** the law block, which read as two gate
  gaps until the routes were anchored inside the block (§4.4).
- **X58-R28-F6** — the round's counting command is **not clone-isolated**: it
  walks up to the real lane and copies the live `tools`/`examples`/`corpus`/
  `reports/round-28` over whatever tree it runs in. Proven with a poison control
  (§8.1). The battery, `replay-frozen.py` and this seat's own instruments do **not**
  sync.

## 1. The chain as re-run

```
examples/culture-d4/components/*.yml  (13 inputs)
  -> tools/assemble-culture-d4.py      -> packet.d4.yml
  -> tools/d2-typed-labels.py          -> typed-labels.d4.yml      (projection)
  -> tools/assemble-d4-typed.py        -> packet.d4.typed.yml      (adapter)
  -> tools/gates/typed-pipeline-gate.py   (L1..L4 + L3b-argot)
  -> tools/gates/d4-typed-labels-check-gate.py
  -> tools/gates/argot-derivation-gate.py  (sibling, invoked by the typed gate)
  -> tools/gates/register-law-gate.py      (NEW this round: the law replay leg)
```

Command (2026-10-18, revision `69cecbc`, `clone-final` = the lane's working tree
cloned + `rsync`'d so the uncommitted landing is measured in isolation):

```sh
export TMPDIR=$PWD/.scratch
git clone --quiet --no-hardlinks --shared . .scratch/r28-x58/clone-final
rsync -a --exclude='.git' --exclude='.scratch' ./ .scratch/r28-x58/clone-final/
bash .scratch/r28-x58/r28-cold-run.sh "$PWD/.scratch/r28-x58/clone-final" "$PWD/.scratch/r28-x58/final"
```

## 1b. The two-pass measurement note

The wave is uncommitted and moved while this seat measured it. Two passes were
taken, and both are receipts on disk:

| pass | clone | stamp | chain | controls | law tampers | counting command |
|---|---|---|---|---|---|---|
| 1 (primary) | `clone-final` | ~20:25Z | green, 22 steps | 12/12 | 5/5 | green, 3/3 claims |
| 2 (refresh) | `clone-final2` | ~20:28Z | green, 22 steps | 12/12 | 5/5 | green, 3/3 claims |

The delta between them is **two file digests and nothing else**:
`register-law-gate.py` `cfbff16b…` → `bbad3578…` and `run-validation.py`
`b8f08546…` → `20e09ea8…`. Both gate behaviours are identical across the two
passes (4 `D4L-LAW-DANGLING` on the clean packet; 33/33 selftest; the same five
tamper classes). **One qualification, found late and measured in §8.1:** the
*counting command's* pass is not independent of the live lane — the runner syncs
the live tree into itself — so the two counting-command readings are one lane at
two instants, while every other reading in this fragment comes from an instrument
with no sync code and is genuinely clone-isolated. This is the honest shape of a
cold re-run over a live wave: a
number without its receipt is not a measurement, and a receipt without its
revision is not one either — so both passes are filed rather than one silently
overwriting the other.

## 2. Cold run — every step, with exit and legs (the landed tree)

| command | exit | legs | tool sha256 (16) |
|---|---:|---:|---|
| `python3 tools/assemble-culture-d4.py --check` | 0 | — | `943f487ba991d45d` |
| `python3 tools/assemble-culture-d4.py --selftest` | 0 | — | `943f487ba991d45d` |
| `python3 tools/d2-typed-labels.py --selftest` | 0 | 163/163 | `2819f68769dfc0b5` |
| `python3 tools/d2-typed-labels.py --packet … --check …` | 0 | — | `2819f68769dfc0b5` |
| `python3 tools/assemble-d4-typed.py --selftest` | 0 | 12/12 | `92f5460bcc34ffbb` |
| `python3 tools/assemble-d4-typed.py --check …` | 0 | — | `92f5460bcc34ffbb` |
| `python3 tools/gates/typed-pipeline-gate.py --selftest` | 0 | 19/19 | `b749ad07cf171027` |
| `python3 tools/gates/typed-pipeline-gate.py --selftest-generalized` | 0 | 16/16 | `b749ad07cf171027` |
| `python3 tools/gates/typed-pipeline-gate.py` | 0 | 16/16 | `b749ad07cf171027` |
| `python3 tools/gates/typed-pipeline-gate.py packet.d4.yml` | 0 | **20/20** | `b749ad07cf171027` |
| `python3 tools/gates/typed-pipeline-gate.py packet.d4.typed.yml` | 0 | **17/17** | `b749ad07cf171027` |
| `python3 tools/gates/d4-typed-labels-check-gate.py` | 0 | — | `05f99629d870280c` |
| `python3 tools/gates/d4-typed-labels-check-gate.py --selftest` | 0 | 163/163 | `05f99629d870280c` |
| `python3 tools/gates/d4-assembly-check-gate.py packet.d4.yml` | 0 | — | `df1a364b3970365c` |
| `python3 tools/gates/argot-derivation-gate.py --selftest` | 0 | — | `b5406bcdaf41c595` |
| `python3 tools/gates/argot-derivation-gate.py packet.d4.yml` | 0 | — | `b5406bcdaf41c595` |
| `python3 tools/gates/naming-collision-gate.py packet.d4.yml` | **1** | — | `d9e4e8f4f93a21b3` |
| `python3 tools/gates/phonology-sanity-gate.py packet.d4.yml` | **1** | — | `d5fe087ffb2342e5` |
| `python3 tools/gates/costume-era-consistency-gate.py packet.d4.yml` | 0 | — | `e6bffd7020c0b116` |
| `python3 tools/gates/lexicon-coverage-audit.py packet.d4.yml` | 0 | — | `2c4dd39702a15ea3` |
| `python3 tools/gates/myth-consistency-gate.py packet.d4.yml` | 0 | — | `5368b13542cd4b8a` |
| `python3 tools/gates/provenance-audit.py packet.d4.yml` | **2** | — | `8a96aaf4ccd14ef4` |

The three non-zero exits are the **standing red verdicts**, identical in kind to
rounds 26 and 27 and unchanged by either landing: `naming-collision` 1 (14
findings), `phonology-sanity` 1 (the `A-CLASS` REVIEW), `provenance-audit` 2 (the
packet is not a corpus entry document). **A reproduced red verdict stays red.**

### 2.1 The mid-landing state, kept because the delta matters

An earlier cold run (`clone-live`, packet `543d68a8`, before the pin re-point)
caught the round mid-landing and is kept so the O claim's cascade is visible:

| step | `clone-live` (pre-re-point) | `clone-final` (settled) |
|---|---|---|
| `typed-gate-d4-source` | exit 2, **1/2 legs** — `FAIL L1-profile` | exit 0, **20/20** |
| `typed-gate-d4-derived` | exit 2, **1/2 legs** — `FAIL L1-profile` | exit 0, **17/17** |
| every other step | same as §2 | same as §2 |

The pre-re-point receipt named the drift exactly: `packet: pins 86079a6708a0, live
543d68a82640; projection: pins 88a94422b412, live 339bfd83bf66`. **Those two legs
were the only chain steps the RL-4 landing moved**, and the O seat's re-point
closed them (§7.1). This is the honest reading of a live wave: a cold run samples
a state, and the state moved under it.

### 2.2 Determinism and no-write (control for the table above)

Two fresh copies produced byte-identical products:
`assemble_identical=True, projection_identical=True, typed_identical=True`.
Regeneration matched the committed bytes for all three artefacts:
`{'packet.d4.typed.yml': True, 'packet.d4.yml': True, 'typed-labels.d4.yml': True}`.
The five read-only entries (`--check` ×3, gate ×2) left every artefact
byte-identical: `unchanged=True, changed=[]`.

## 3. RL-4 — the packet_keys fix, measured cold

Claim D's `after_required` names the fix: "the components declare packet_keys; the
records reach the packet; the named-holds set updated honestly." All three halves
are measured, and all three hold.

**Half one — the declarations.** `03-orthography.yml` now declares
`packet_keys: [orthography, records, literacy_institutions]` (it declared **none**
before, so the assembler fell back to its `PACKET_KEYS` allowlist and skipped the
blocks) and `09-costumes.yml` adds `enforcement` to its list. Measured at
`clone-final`:

```
03-orthography.yml:24  packet_keys: [orthography, records, literacy_institutions]
09-costumes.yml:22     packet_keys: [costumes, materials, cloth_sources, rank_rules, form_slots, enforcement]
```

**Half two — the records reach the packet as records.** Read with the projector's
own strict loader, the packet's top-level keys now include `records`,
`literacy_institutions` and `enforcement`, and the eight ids are rows carrying an
`id`:

| id | block | row head |
|---|---|---|
| `OR-01` | `records` | count-stamp tally, stage E0 |
| `OR-02` | `records` | the extended stamp hand, stage E1 |
| `OR-03` | `records` | the league hand, stage E2 |
| `LI-01` | `literacy_institutions` | the stamp-house |
| `LI-02` | `literacy_institutions` | the mold-keeper's license |
| `LI-03` | `literacy_institutions` | the furnace roll |
| `EN-01` | `enforcement` | the council's fine |
| `EN-02` | `enforcement` | the stamp-holder's refusal |

`assembly.skipped_keys` no longer names any of the eight (the round-27 review
measured `LI-01: 0`, `EN-01: 0` occurrences in the packet; the count is now ≥1 for
all eight). The runner's own `rl4.record_locations` agrees block for block.

**Half three — the holds revised honestly.** `expected-holds.json` (now
`65f5a03e092fb4bb…`) carries `counts {fail: 0, hold: 12, note: 0}`, unchanged, and
a `revision_note` that names **both** the round-28 landing and the RL-4 fix; the
runner reads `names_round_28: true`, `names_the_fix: true`. The old pins moved to
`supersedes_pins` rather than being overwritten — the correct append-only pattern.

**The measurement the round-27 design predicted and this seat confirms:** the
`mold-keeper (OR-02)` citation in `RGL-01` was correct in shape and the packet was
wrong; `OR-02` now resolves. Round 27's `mold-keeper` finding is closed **by the
packet fix, not by a law edit**.

## 4. The law replay leg — discovered, and measured with this seat's own tampers

This is the heart of claim D, and it is measured **by behaviour, not by shape**:
the leg is *discovered* (whichever delivered file emits the class), and the tamper
routes are **authored here** from the claim's own field list, not copied from the
D seat's probe.

### 4.1 The discovery

```
$ grep -rl "D4L-LAW" tools/ ; echo "exit=$?"
tools/gates/register-law-gate.py
exit=0
```

Exactly one delivered file names the class, and it is new this round
(`tools/gates/register-law-gate.py`, 27,090 B at the refresh pass, sha256
`bbad35784bfb463d…`; `cfbff16bbb67d94d…` at the primary pass — see §1b). Its
docstring declares ten classes: `DATA`, `ROW`, `SPEAKER`, `FORCE`, `CONSEQUENCE`,
`REGISTER`, `AXIS`, `KIND`, `DANGLING`, `COVERAGE`. Its own selftest reads
**33/33** (exit 0). **Before this landing the same grep returned exit 1 with no
output** — that was the RL-1 reading, and this seat measured it at the declare
revision (§9).

### 4.2 The tampers — five routes, all caught

Command: `python3 -B .scratch/r28-x58/law-replay-probe.py --root <clone-final>
--out .scratch/r28-x58/final-law.json --scratch …`. Each route is a **line-level
text edit of the delivered bytes**, anchored **inside the `register_law:` block**
so it edits a law field and never a same-named field elsewhere in the packet (see
the method note in §4.4).

| # | route | field rewritten | new named class over clean | caught |
|---|---|---|---|---|
| 1 | `force` | `force:` → `"no-such-force"` | `D4L-LAW-FORCE` | **yes** |
| 2 | `speaker` | `speaker:` → `"nobody-nowhere (ZZ-99)"` | `D4L-LAW-SPEAKER` | **yes** |
| 3 | `consequence` | `consequence:` → `"the act evaporates silently"` | `D4L-LAW-CONSEQUENCE` | **yes** |
| 4 | `register` | `register:` → `"no-such-register"` | `D4L-LAW-REGISTER` | **yes** |
| 5 | `axis` | `axis:` → `"no-such-axis"` | `D4L-LAW-AXIS` | **yes** |

**5/5 caught**, each with a *distinct* class the clean packet does not emit. Route
1 is round 27's own RL-1 control — the exact tamper that produced **the same 12
findings** as a clean packet before this landing. **The teeth the claim promises
are real and this seat measured them with its own hands.**

### 4.3 The clean packet is not silent — and that is a finding

The leg emits **four `D4L-LAW-DANGLING` HOLDs on the delivered bytes**:

```
FINDING D4L-LAW-DANGLING: HOLD — RGL-01 design_row names QREG-05, which no delivered record carries
FINDING D4L-LAW-DANGLING: HOLD — RGL-01 design_row names QREG-07, which no delivered record carries
FINDING D4L-LAW-DANGLING: HOLD — RGL-02 design_row names QREG-06, which no delivered record carries
FINDING D4L-LAW-DANGLING: HOLD — RGL-03 design_row names QREG-08, which no delivered record carries
coverage: … law_rows=5 identity_rows=4 record_ids=179 registers=9 speaker_tokens=3
          force_failures=0 consequence_failures=0 dangling=4 findings=4
```

The mechanism is a real defect: `RGL-01..03` carry `design_row: [QREG-05…08]` —
the act rows round 27's design specified — and the `registers` block still carries
only `QREG-01..04`. So **every law row's `design_row` citation resolves to
nothing**, and the field whose stated purpose is "so a reader can check the law
against the design rather than reconcile two vocabularies" checks against nothing.
It is the same class as round 26's `RD-1` (cited keys that do not exist) and round
27's `RL-4`, one level in.

**Why this is not a claim-D failure, and not silently waived either.** The claim's
`after_required` says a *tampered* row is a named finding; it does not require the
clean packet to be finding-free. The runner grades the **line-level delta** over
the clean packet (`law_replay_probe`, `reports/round-28/run-validation.py:677`),
so a saturated class does not mask a caught tamper — the right construction, since
a leg that fired on nothing would be the defect, not the fix. This seat agrees
with the grading and still records the four HOLDs as an **open defect the round
should carry**, not read as clean.

### 4.4 A method note, recorded because it is the round-26 lesson repeating

This seat's **first** probe pass showed `register` and `axis` **uncalled**, which
would have read as two gate gaps. It was a **probe artifact**: the unanchored
regexes matched the first `register:` / `axis:` lines in the packet — lines 1001
and 281, far **above** the `register_law:` block at line 2710, inside the
`registers` and `lexicon` blocks. Anchoring the routes inside the law block fixed
it and all five routes were then caught. This is the same failure shape as round
26's checker bug (§10 of the round-27 X58 record): **a tamper that edits the wrong
region of the file measures the wrong thing.** Recorded rather than quietly
corrected, because the next seat to author a law tamper will hit it.

### 4.5 Corroboration and its limit

The round-28 runner's own law reader and this seat's probe agree on the substance
— a tamper must add a `D4L-LAW-*` line over the clean packet, and the clean
packet's own findings are reported, never required to be zero. They are **not
identical instruments**: the runner resolves the leg by trying argv shapes and
grades lines; this probe discovers by grep and grades class deltas. An agreement
between them is evidence, not a shared bug. **One boundary:** the D seat's
adversarial review `reports/round-28/argot/D18-force-overmatch.md` measures the
runner's *own* `law_check` force predicate as over-matching (two `AND`-ed
substring tests, so `assertive-binding` or a fabricated class word passes). That
is a finding about the **runner's reader**, not about the delivered leg, and this
seat did not re-measure it — it is named here so the round does not read the
runner's green as covering the force predicate's precision.

## 5. The frozen surface and the committed baselines — swept, and still red

Method: `tools/replay-frozen.py <MANIFEST.tsv> --json` for every manifest under
`tools/gates/frozen/`, run inside the clone with `TMPDIR` **outside** the repo (a
`TMPDIR` inside the repo makes every row `mirror_unsafe` exit 2); committed
baselines re-run from their own recorded `command` and compared against their own
`expected.exit`.

### 5.1 Frozen manifests

| manifest | `b95fca1` (r27 declare) | `6c0ac44` (r27 admit) | `69cecbc` declare | **landed tree** |
|---|---|---|---|---|
| `frozen/round-11` | 10r / 0m / 1c | 10r / 0m / 1c | 10r / 0m / 1c | 10r / 0m / 1c |
| `frozen/round-18` | 1r / **1m** | **0r / 2m** | **0r / 2m** | **0r / 2m** |
| `frozen/round-18/repin-d2` | 10r / 0m / 1c | 10r / 0m / 1c | 10r / 0m / 1c | 10r / 0m / 1c |
| `frozen/round-20/repin-d2` | 10r / 0m / 1c | 10r / 0m / 1c | 10r / 0m / 1c | 10r / 0m / 1c |
| `frozen/round-22/d4-repin` | 2r / 0m / 1c | **0r / 2m** / 1c | **0r / 2m** / 1c | **0r / 2m** / 1c |
| `frozen/round-23/repin-d2` | 10r / 0m / 1c | 10r / 0m / 1c | 10r / 0m / 1c | 10r / 0m / 1c |
| `frozen/round-25/gate-input` | 0r / 0m / 6c | 0r / 0m / 6c | 0r / 0m / 6c | 0r / 0m / 6c |
| `frozen/round-26/gate-input` | 4r / 2m | 4r / 2m | 4r / 2m | 4r / 2m |
| `frozen/round-26/post-register` | **6r / 0m** | **4r / 2m** | **4r / 2m** | **4r / 2m** |
| `frozen/round-3`, `round-3/attempt-1` | 0r / 0m / 7c | same | same | same |

*(r = reproduced, m = mismatch, c = could-not-evaluate.)*

**The landed tree moved no frozen row.** The RL-4 landing and the law leg are both
invisible to this surface, because every red row here re-derives from the *live
component tree* and the row's own snapshot.

### 5.2 X58-R28-F1 — `round-26/post-register` regressed, and round 27 did not catch it

Round 27's own X58 recorded `frozen/round-26/post-register` at **6r / 0m** (its
§11.4). It reads **4r / 2m** now, and the movement is **not** round-28's. Three
control clones fix the attribution:

| revision | `post-register` | manifest sha256 | live packet in that clone |
|---|---|---|---|
| `b95fca1` (r27 declare) | **6r / 0m** | `e2e838f3…` | `dd25077b…` |
| `6c0ac44` (r27 admit) | **4r / 2m** | `e2e838f3…` | `86079a67…` |
| `69cecbc` declare | **4r / 2m** | `e2e838f3…` | `86079a67…` |
| landed tree | **4r / 2m** | `e2e838f3…` | `543d68a8…` |

**The manifest bytes never changed** (`e2e838f3` at all four revisions), so the
movement is entirely in the live tree the frozen gate re-derives against. It is
green at the round-27 declare and red from the round-27 admit onward: **round 27's
own register landing broke it, and round 27's sweep recorded it green** — most
likely because the sweep sampled before the round-27 re-point, exactly as this
round's `clone-live` sampled before the round-28 re-point (§2.1). The two mismatch
rows are lines 2 and 3 (`packet.d4.yml`, `packet.d4.typed.yml`), both
`exit code 2 != recorded 0; finding count 0 != recorded 12`.

This is **not** a round-28 regression and this seat does not repair it. It is a
round-27 sweep gap that round 28 inherited, and the O seat's own census
(`reports/round-28/sweep/_prelanding-census.md`) independently lists the same two
rows as `MANIFEST-INPUT-MOVED` — an agreement from different machinery.

### 5.3 Committed `expected/` baselines — all four red, unchanged

| baseline | recorded | declare | landed tree |
|---|---:|---|---|
| `expected/d4-assembly-check-gate/r19-pre` | exit 0 | **RED** (1) | **RED** (1) |
| `expected/d4-typed-labels-check-gate/r19-pre` | exit 0 | **RED** (1) | **RED** (1) |
| `expected/d4-typed-labels-check-gate/r20-post` | exit 0 | **RED** (1) | **RED** (1) |
| `expected/d4-typed-labels-check-gate/r22-post` | exit 0 | **RED** (1) | **RED** (1) |

Every red is `… differs from the deterministic assembly` / `… differs from the
deterministic projection`. The O seat's own sweep census lists all four as
`B/C-DIGEST-DRIFT`, and its `d4-pins.json` records the same four `controls` with
the same exit 1 and the same stderr tails. **Agreement, not shared bug.**

**Mechanism, re-confirmed by this seat (round-27 X58 §6.3, unchanged):**
`d4-assembly-check-gate.py:33-34` resolves `ROOT = Path(__file__).resolve().parent.parent.parent`
and re-derives from the live component tree; a frozen row over a **superseded**
snapshot therefore cannot reproduce once the components move, no matter how honest
the snapshot is. This is a structural property of those two gates, not a defect
introduced by any round.

## 6. The RL-3 ceiling — the round's C claim, re-measured

Claim C records the register-lexicon ceiling as craft knowledge. Both halves
landed, and this seat re-ran the instruments rather than reading the C seat's
receipt.

**The amendment.** `corpus/knowledge/linguistics/register-strata-attestation.md`
gained **§13** (`## 13. Amendment (round 28): the register-lexicon ceiling,
re-measured, with its mechanism`) — 123 lines added, **every earlier section
header still present**, no baseline byte rewritten. It is a true append.

**The re-measurement, reproduced by this seat.** Running
`reports/round-28/ceiling/measure-ceiling.py` cold:

```
population: mark-axis plain words = 27
delivered gate (b5406bcd)  legal=19 illegal=8
  illegal: L-08, L-15, L-17, L-24, L-26, L-30, L-44, L-51
  cross-tab: {"abstract/illegal": 4, "abstract/legal": 1,
              "material/other/illegal": 4, "material/other/legal": 18}
filed round 27:      legal=18 illegal=9  (pre-fix reader)
mechanism: reverse is legal <=> the base-initial consonant is a licensed coda -> True (27/27)
  onsets=14 codas=8 never-coda=b,g,h,j,p,w
```

**The filed round-27 count does not reproduce, and the amendment says so.** The
18/9 is the **pre-fix reader's** reading (the syllabification that never splits a
consonant run, `5b5abe78` → `b5406bcd`); the delivered reading is **19/8**, and the
single row that moves is `L-45 tikmes`. The amendment keeps the old number as the
round-27 reading at its stamp and tabulates the correction — the right disposition,
and it **sharpens** rather than weakens the ceiling: four of the five
legal/institutional abstractions still refuse `reverse`, including `L-30 gis` (the
oath itself).

**The mechanism is the round's real advance**: `reverse` is legal **iff** the
base-initial consonant is one of the eight licensed codas — verified **27/27** with
no counterexample. The six consonants that are onsets but never codas (`b g h j p
w`) are precisely the refusals. The ceiling is arithmetic over the syllable
template `(C)V(V)(C)`, not a lexical accident more coinage would fix.

**The new entry.** `corpus/knowledge/linguistics/register-lexicon-ceilings.md` is
new (287 lines, `bb579d51cea0a900…`), frontmatter-complete, gap-named (with an
absence sweep whose zero counts I spot-checked), carrying a decision record
`RLC-1..RLC-6`, grounded in round-26/27/28 artifacts and dated external sources
(Dixon 1972/1980, Halliday 1976/1978, Gotowski 2019, Aronoff 1976, Bauer
1983/2001, Labov 1972, Irvine & Gal 2000), and making no canon claim.

**The README.** `corpus/README.md` carries a new revision 1.8 and indexes the new
entry. This seat re-ran `reports/round-28/readme/sweep.py` cold:

```
parts {"civilizations": 94, "culture-material": 18, "linguistics": 21,
       "myth-symbol": 19, "synthesis": 29, "verification": 20}
rows 201 files 201   missing_from_index 0   topic_mismatch 0   orphan_rows 0
header_drift {}   totals_line 201 totals_ok True   footer_findings [] footer_ok True
```

**Clean.** Note the intermediate state this seat caught: at 20:20Z the entry had
landed but the README footer still read 200/`20/19/18/29/20/94` against 201 files
— the C seat's own sweep read **red** on it (`FOOTER_TOTAL declared 200 live 201`),
and it was reconciled later in the same window. Recorded because a cold run that
sampled 20:20Z would have called claim C red.

## 7. The pin surface — what closed, and what is drafted rather than installed

### 7.1 What closed: the typed-pipeline profile

`tools/gates/typed-pipelines.json` (now `7f5a9c722a5ccca5…`) re-pointed the `d4`
profile. Measured against the live bytes:

| surface | pin | live | match |
|---|---|---|---|
| `packet.d4.yml` | `543d68a82640e1b0` | `543d68a82640e1b0` | **yes** |
| `typed-labels.d4.yml` | `339bfd83bf668324` | `339bfd83bf668324` | **yes** |
| `expected-holds.json` | `65f5a03e092fb4bb` | `65f5a03e092fb4bb` | **yes** |

This is the two-leg cascade §2.1 caught mid-landing, closed. The battery reads
`pass 7 / fail 0 / unevaluable 0` and `coverage 9/9, pinned 19/19, baseline_exit 0`
— re-run by this seat.

### 7.2 X58-R28-F2 — the successor rows are drafted, not installed

The O seat built successor recordings under **`reports/round-28/pinsweep/`**, and
this seat re-ran them cold (they are green):

| successor | replay |
|---|---|
| `reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv` | **4/4 reproduced**, exit 0 |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/expected.json` | **MATCH** (exp 0, obs 0) |
| `reports/round-28/pinsweep/baselines/d4-typed-labels-check-gate/r28-post/expected.json` | **MATCH** (exp 0, obs 0) |
| `reports/round-28/pinsweep/v3-baseline-r28/expected.json` | v3 replay exit 0, no drift lines |

**But the red surfaces they answer are unchanged.** `tools/gates/frozen/` still
carries **no** `r28-post` generation, and `tools/gates/expected/` still carries
**only** `r19-pre` / `r20-post` / `r22-post` — the four red baselines of §5.3 and
the two red manifests of §5.1 are exactly as red after the round as before it. The
successor rows live where the runner's `round_repin_rows()` looks (a structured
round-28 file naming a drifted surface with its live digest — which is why the
runner reads `unrepinned_surfaces: []`), and the runner's own limits state that a
drift "must be re-pinned by a NEW round-28 row", not that the installed surface
moves.

**This is a naming/placement finding, not a green-washing accusation.** The
recording is honest, green, and correctly a *new* generation. The question the
round must answer is whether a successor that lives under `reports/round-28/`
discharges claim O's "every drifted row re-pinned as a new row" or whether the
red installed surface is meant to move. **This seat does not decide it**; it
measures that the installed surface did not move and names the consequence.

### 7.3 X58-R28-F3 — the new gate is in no battery duty

`tools/check-gate-battery.py` registers its gates in two tuples
(`:116-134`):

```
GATE_NAMES       = 7 gates  (duty 1: isolated selftest battery)
D4_GATE_NAMES    = d4-typed-labels-check-gate.py, d4-assembly-check-gate.py  (duty 2)
REGISTERED_GATE_NAMES = GATE_NAMES + D4_GATE_NAMES   (9)
```

`register-law-gate.py` appears in **neither** tuple, so `coverage 9/9` is unchanged
by the round's new leg and the gate has **no battery coverage** in either duty. It
does have its own `--selftest` (33/33, measured) and it is exercised by the runner
and by `reports/round-28/gate-tests/`. **The claim does not require battery
registration** and this seat does not treat it as a failure; it is recorded because
"the battery is green" must not be read as "the new leg is covered". It is the same
shape as round 27's note that duty 1's ceiling is `pass 7 / fail 0`.

## 8. The round's own counting command, run cold

Run by this seat with the runner's argv launched inside the clone
(`reports/round-28/run-validation.py`, `runner_sha256 b8f08546f8741946…` at the
primary pass, `20e09ea8db7bcb30…` at the refresh pass — both read the same verdict,
§1b). **Note §8.1: the runner syncs the live lane into itself, so this is a
reading of the live lane at run time, not of the clone.**

```
$ python3 -B reports/round-28/run-validation.py --check
acceptance: True
 claim C passed=True failures=0
 claim D passed=True failures=0
 claim O passed=True failures=0
missing: []
```

### 8.1 X58-R28-F6 — the counting command is not clone-isolated: it self-syncs the live lane

**This is a correction to this seat's own method, found late and measured three
ways.** The runner's own docstring says "Run only in the lane root **or an
isolated clone under its .scratch**", and this seat took that at face value. It is
not what the code does: `live_lane()` (`reports/round-28/run-validation.py:339`)
walks **up from `ROOT`** to the nearest ancestor outside `.scratch` that carries a
`.git` and a `claims.json`, and `sync_round_surface()` (`:1669`, called at
`:1934`) then **copies the live lane's `corpus`, `examples`, `tools`,
`reports/round-28`, `SKILL.md`, `LOG.md`, `SCORECARD.md`, `PROVINCE.md`,
`SHONEN.md` into the running tree**. Its own receipt discloses the copy as
`"synced_from_live": {… "tools": "tree" …}` — but that is a *digest listing*, not a
warning, and a reader who sees `"tools": "tree"` has no reason to read it as "your
clone was overwritten".

**Measured by this seat, with a poison control:**

```
$ # in a fresh clone under .scratch, with the live lane one level up
$ echo "# POISON" > tools/gates/register-law-gate.py
$ echo "# POISON" >> examples/culture-d4/packet.d4.yml
$ python3 -B reports/round-28/run-validation.py --check
$ # after the run, both files are back to the LIVE bytes:
$ sha256sum tools/gates/register-law-gate.py   # bbad35784bfb463d…  (live's digest)
$ sha256sum examples/culture-d4/packet.d4.yml  # 543d68a82640e1b0…  (live's digest)
```

A **second control** confirms the sync is unique to this tool: the same poison in
the same clone is left untouched by `tools/check-gate-battery.py` (exit 0, poisoned
digest still on disk), and `tools/replay-frozen.py`, `.scratch/x58/chain-cold-run.py`,
`.scratch/x58/chain-controls.py` and this seat's `law-replay-probe.py` contain **no**
sync code at all (`grep -c "sync_round_surface\|copy_into_clone\|live_lane"` → 0 in
each).

**What this means, stated plainly.**

- **The runner's verdict is a verdict on the LIVE lane**, not on the clone it was
  launched from. That is arguably the intent — the round's acceptance is about the
  lane — and it is why the receipt's `synced_from_live` block exists. It is **not**
  a defect in the verdict.
- **It is a trap for the reading this fragment makes.** Every other measurement in
  §2–§7 was taken by instruments with **no** sync code, so those readings *are*
  clone-isolated. §8's is not, and the sentence "measured by this seat, in a
  clone" in §0 was **wrong about §8** — corrected here. What §8 actually measures
  is the **live lane at the moment the runner executed**, which is the stronger
  claim, but it is a different one.
- **It also explains the runner-digest movement in §1b.** `clone-final2`'s
  `run-validation.py` read `7310a945…` on disk but self-reported `20e09ea8…`: the
  runner had copied the live lane's own `run-validation.py` over itself. The two
  "passes" are therefore one lane at two instants, not two independent trees.
- **A consumer running the command in a clone to test the command will not test
  the clone.** Anyone reproducing round acceptance from a checkout must know the
  tool reads the live lane above it, or they will attribute the live lane's result
  to their tree.

**Severity:** low for the round's verdict (the live lane is the right target), high
for method transparency. **Owner:** the runner's file. This seat does not edit it.

The receipt (`reports/round-28/validation.json`, `measured_at_utc
2026-10-18T20:25:25+00:00`) carries, in its own words:

| leg | reading |
|---|---|
| `protected_filed_artifacts` | **passed true**, 1587 protected paths, **0 differences** |
| `law_finding_producers` | `['tools/gates/register-law-gate.py', …]` — the leg exists |
| `law_replay.leg` | `tools/gates/register-law-gate.py` |
| `law_replay` tampers | each adds a `D4L-LAW-*` **line** over clean (`added_over_clean` non-empty) |
| `rl4.record_locations` | all eight ids located in their blocks |
| `holds` | `hold 12 / fail 0 / note 0`, `names_round_28 true`, `names_the_fix true` |
| `sweep` | 307 rows, 157 green, 150 drift, 8 drifted surfaces, **`unrepinned_surfaces: []`** |
| `battery` | `pass 7 / fail 0 / unevaluable 0`, `coverage 9/9`, `pinned 19/19` |
| `replays` | `handoff-v2 0, handoff-v3 0, handoff-v3-selftest 0, replay-selftest 0` |
| `v3_replay` | exit 0, `drift_lines: []` |

**This is a green receipt on the settled tree, and it is the round's verdict, not
this seat's.** This seat's independent cold run agrees with it on every leg it
re-measured (§2, §3, §4, §6, §7), and disagrees with nothing.

## 9. What moved, in one table

| surface | declare `69cecbc` | landed tree |
|---|---|---|
| `tools/gates/register-law-gate.py` | absent (RL-1 open) | **present**, `bbad3578…` (refresh pass; `cfbff16b…` at the primary pass), 33/33 selftest |
| `tools/` files naming `D4L-LAW` | **0** | **1** |
| this seat's 5 law tampers caught by name | **0/5** | **5/5** |
| law findings on the clean packet | n/a (no leg) | 4 `D4L-LAW-DANGLING` HOLDs |
| `03-orthography.yml` / `09-costumes.yml` packet_keys | none / no `enforcement` | both declare their blocks |
| the eight RL-4 ids as packet records | OR prose-only, LI/EN absent | **all eight records** |
| `typed-gate-d4-source` | 20/20 (pre-landing) | **20/20** (after re-point) |
| `typed-pipelines.json` `d4` pins | `86079a67` / `88a94422` | `543d68a8` / `339bfd83` |
| `expected-holds.json` | `857417e9…` | `65f5a03e…` (revision note names r28 + RL-4) |
| `register-strata-attestation.md` | 12 sections | **13 sections** (append) |
| `register-lexicon-ceilings.md` | absent | **present**, 287 lines |
| `corpus/README.md` | revision 1.7, footer 199/19 | revision 1.8, footer 201/21 |
| frozen manifests red | 4 | **4** (unchanged) |
| committed `expected/` baselines red | 4 | **4** (unchanged) |
| round-28 counting command | claim D red (RL-1, RL-4) | **all three claims green** |

## 10. Findings index

| id | finding | severity today | owner |
|---|---|---|---|
| **X58-R28-F1** | `frozen/round-26/post-register` reads 4r/2m where round 27 recorded 6r/0m; manifest bytes unchanged, green at `b95fca1` and red from `6c0ac44` — **round 27's landing broke it and round 27's sweep missed it** | medium — an inherited sweep gap, not a round-28 regression | round 27's sweep / the O seat's successor |
| **X58-R28-F2** | the successor rows (`r28-post` manifest 4/4, two baselines MATCH, v3 successor green) live under `reports/round-28/pinsweep/`, so the four red baselines and two red manifests **installed** under `tools/gates/` did not move | medium — a placement question claim O must answer | claim O |
| **X58-R28-F3** | `register-law-gate.py` is registered in **no** battery duty (`GATE_NAMES`, `D4_GATE_NAMES` both omit it); `coverage 9/9` is unchanged | low — no claim requires registration; recorded so "battery green" is not read as "new leg covered" | the battery's file |
| **X58-R28-F4** | the new leg emits 4 `D4L-LAW-DANGLING` HOLDs on the clean packet: `RGL-01..03` cite `design_row` ids `QREG-05..08` that were never landed as `registers` records | medium — a real defect the round should carry, not read as clean | claim D / the register-law component |
| **X58-R28-F5** | this seat's own method note: an unanchored law-field regex matched `register:`/`axis:` lines **above** the law block, which read as two gate gaps until the routes were anchored | method — recorded so the next law-tamper author does not repeat it | this seat (self-reported) |
| **X58-R28-F6** | the round-28 counting command is **not clone-isolated**: `live_lane()` walks up to the real lane and `sync_round_surface()` copies its `tools`/`examples`/`corpus`/`reports/round-28` over the running tree. Proven with a poison control (poisoned clone gate + packet restored to live bytes by the run); the battery and `replay-frozen.py` do **not** sync | low for the verdict (the live lane is the right target), high for method transparency — a reader running it in a clone will attribute the live lane's result to their tree | the runner's file |

**Corroboration.** X58-R28-F1's two rows are independently listed by the O seat's
census (`reports/round-28/sweep/_prelanding-census.md`, `MANIFEST-INPUT-MOVED`) —
different machinery, same rows. §5.3's four red baselines are independently listed
by that census as `B/C-DIGEST-DRIFT` and by `reports/round-28/pinsweep/d4-pins.json`
as four controls with the same exits. §4's leg discovery is independently reported
by `reports/round-28/argot/D17-law-bypass.md`, which reached the same verdict from
its own reading. **The committed-baseline verdict replay in §5.3 remains the leg no
sibling covers**: the battery's duty 2 and the O seat's `d4-pins.json` baseline
duty are both digest-only by construction, so they report `pinned 19/19` while the
four D4 baselines fail their own recorded verdicts.

## 11. What this seat did not do

- Did not edit any tool, gate, packet, component, pin, manifest, baseline, runner
  or frozen row; did not commit or push. **Records no new row** — §7.2 is the
  measurement a recording seat needs, written so it does not re-derive it.
- Did not repair the four red baselines, the two red manifests, the four dangling
  `design_row` citations, or the battery registration. Each is another seat's file
  or another claim's work.
- Did not decide whether the successor rows' placement discharges claim O. That is
  claim O's call (§7.2).
- Did not audit the D2 chain. `frozen/round-3`, `round-3/attempt-1` and
  `round-25/gate-input` report `could-not-evaluate` (`gate_digest_mismatch` on
  `naming-collision-gate.py`, `provenance-audit.py`, `typed-pipeline-gate.py`) —
  pre-existing, outside this assignment, named only so the sweep is not read as
  complete.
- Did not re-measure the D seat's adversarial findings `D18` (force over-match) or
  `D19` (the round-27 A/B does not reproduce). Both are named in §4.5 and §6 where
  they bear on a reading this fragment makes; neither is adjudicated here.
- Did not verify the round's `LOG.md` entry. Per `AGENTS.md`, the parent integrates
  the wave's evidence fragments into shared bookkeeping after the batch; this
  fragment is evidence for that integration, not the integration.

## 12. Reproduction

```sh
export TMPDIR=$PWD/.scratch

# the landed tree, measured in isolation (the wave is uncommitted)
git clone --quiet --no-hardlinks --shared . .scratch/r28-x58/clone-final
rsync -a --exclude='.git' --exclude='.scratch' ./ .scratch/r28-x58/clone-final/

# chain (22 steps + determinism + no-write) + 12 controls + law probe
#   + frozen sweep + baseline verdict replay + battery + counting command
bash .scratch/r28-x58/r28-cold-run.sh "$PWD/.scratch/r28-x58/clone-final" \
     "$PWD/.scratch/r28-x58/final"

# the refresh pass (§1b), run the same way after the tree moved again
git clone --quiet --no-hardlinks --shared . .scratch/r28-x58/clone-final2
rsync -a --exclude='.git' --exclude='.scratch' ./ .scratch/r28-x58/clone-final2/
bash .scratch/r28-x58/r28-cold-run.sh "$PWD/.scratch/r28-x58/clone-final2" \
     "$PWD/.scratch/r28-x58/final2"

# the law probe on its own (own tamper routes, discovered leg)
python3 -B .scratch/r28-x58/law-replay-probe.py \
    --root "$PWD/.scratch/r28-x58/clone-final" \
    --out .scratch/r28-x58/final-law.json --scratch .scratch/r28-x58/final-law-scratch

# the round-27 attribution control (F1): 6r/0m at the declare, 4r/2m from the admit
git clone --quiet --no-hardlinks --shared . .scratch/r28-x58/clone-r27decl
git -C .scratch/r28-x58/clone-r27decl checkout --quiet b95fca1
bash .scratch/x58/replay-sweep.sh "$PWD/.scratch/r28-x58/clone-r27decl" \
     "$PWD/.scratch/r28-x58/replay-r27decl.jsonl"
git clone --quiet --no-hardlinks --shared . .scratch/r28-x58/clone-r27close
git -C .scratch/r28-x58/clone-r27close checkout --quiet 6c0ac44
bash .scratch/x58/replay-sweep.sh "$PWD/.scratch/r28-x58/clone-r27close" \
     "$PWD/.scratch/r28-x58/replay-r27close.jsonl"

# the C leg, re-run cold
python3 -B reports/round-28/ceiling/measure-ceiling.py
python3 -B reports/round-28/readme/sweep.py

# the O seat's successor rows, replayed cold
TMPDIR=/tmp/x58f python3 tools/replay-frozen.py \
    reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv --json
```

---

*Receipts: primary pass `.scratch/r28-x58/{final-chain.json,final-controls.json,
final-law.json,final-replay.jsonl,final-baselines.txt}`; refresh pass
`{final2-chain.json,final2-controls.json,final2-law.json,final2-replay.jsonl,
final2-baselines.txt}` (§1b); control revisions `{declare-chain.json,
replay-declare.jsonl,replay-r27decl.jsonl,replay-r27close.jsonl,law-pre.json}`.
Fragment written 2026-10-18.*
