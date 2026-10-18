# R28-D22 — frozen rows for the round-28 RL-4 landing and the final pin cascade (new rows only)

- round: 28 (operator: loop 3 of 3, **build round 4 of 4 — the last build round**;
  64 declared workers, `devin/deepseek-v4-1-flash-high`). Seat **R28-D22**
  (D-scribe 2 of 4).
- claim under draft: `reports/round-28/claims.json` claim **D** (`register-law-replay`)
  for §2–§3, with claim **O**'s pin surface named in §4–§6 because the rows that
  close it are the same generation.
- date: 2026-10-18. Declared baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`.
  Lane HEAD `69cecbc7dcf575a29f29660ecac470e05260fd86`.
- **final stamp 2026-10-18T20:15:52Z; post-stamp landings to 20:29Z recorded in
  §4, §4a and §6.** The D4 packet moved **once** inside this seat's window: the
  RL-4 `packet_keys` fix landed ~20:13Z, taking `packet.d4.yml` `86079a67…` →
  **`543d68a8…`** and `typed-labels.d4.yml` `88a94422…` → **`339bfd83…`**. **Every
  pin this file proposed as "named, not landed" then landed** — the two pin files
  were re-pinned, the `r28-post` generation was extended to four rows, and the v3
  baseline was frozen. Those sections keep the proposal and the delivered result
  side by side rather than rewriting the proposal away.
- **writes: this file only** plus gitignored scratch under `.scratch/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch write; the frozen
  replays themselves need `TMPDIR` **outside** the repo — §5a).
- **no filed frozen row was edited.** No `MANIFEST.tsv`, no `expected.json`, no
  `freeze.txt`, no `freeze-receipt.json` under `tools/gates/frozen/`,
  `tools/gates/expected/` or `reports/round-27/` was touched by this seat. No
  commit, no push.
- canon: **NON-CANON engineering evidence.** A freeze pins bytes and verdicts,
  never design quality, scholarship or lore standing; a reproduced red verdict
  stays red.

## 1. The movement, and the one landing that matters

All stamps UTC, 2026-10-18. The frozen surface has **two** relevant states in this
round, and a reader who used the first would pin bytes that no longer exist.

| stamp | `packet.d4.yml` | `typed-labels.d4.yml` | what happened |
|---|---|---|---|
| ~20:10:20 | `86079a67…` | `88a94422…` | the round-28 declaration lands (`claims.json`, `targets.json`) on the **round-27** packet; every round-27 pin still names these bytes |
| **~20:13:00** | **`543d68a8…`** | **`339bfd83…`** | **the RL-4 fix merges**: `03-orthography.yml` declares `packet_keys: [orthography, records, literacy_institutions]` and `09-costumes.yml` adds `enforcement`. Three list blocks (`records`, `literacy_institutions`, `enforcement`) enter the packet; the argot census moves `records=175` → **`183`**. Every pre-fix pin is stale from this instant |
| 20:15:52 (**final**) | `543d68a8…` | `339bfd83…` | stable across four re-reads (§5) |

**The load-bearing consequence, measured.** The round-27 frozen generation
`reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv` pinned
`86079a67…`/`88a94422…` — the **pre-RL-4** bytes — so it is stale against the
live tree:

```
$ TMPDIR=/var/tmp/r28-d22 python3 tools/replay-frozen.py reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv
ROW 3 mismatch reason=replay_mismatch gate=tools/gates/d4-typed-labels-check-gate.py input=examples/culture-d4/typed-labels.d4.yml exit=1/0 count=0/0 bytes=differ launched=yes
REPLAY MISMATCH: 2 mismatch, 0 reproduced of 2 row(s)
```

That is the **designed** behaviour and it is the round-25 lesson restated: a
generation goes red because the artifact it graded **moved**, not because it was
wrong. The successor is a **new generation** (§3), never an in-place edit — and it
landed: §4a measures `reports/round-28/pinsweep/frozen/r28-post/` at **4/4 rows
reproduced**.

## 2. The rows the RL-4 landing needs (measured today, new rows)

All digests measured 2026-10-18T20:14–20:16Z (`sha256sum`, cwd = lane root).
Column schema is the `MANIFEST.tsv` schema:
`gate  gate_sha256  input  input_sha256  exit_code  finding_count  output  output_sha256  input_snapshot  command`.

### 2.1 The rows that are replayable today — proposed successors

| # | gate | gate_sha256 | input | input_sha256 | exit | count | output_sha256 |
|---|---|---|---:|---:|---:|---:|---|
| **R28-1** | `tools/gates/d4-assembly-check-gate.py` | `df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a` | `examples/culture-d4/packet.d4.yml` | `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f` | **0** | 0 | `c60820a54742ecaa1edef972c6c94cce3f88313fbace8ef19eaeddd9a42572a7` |
| **R28-2** | `tools/gates/d4-typed-labels-check-gate.py` | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` | `examples/culture-d4/typed-labels.d4.yml` | `339bfd83bf66832479b5b8ffbbce708c8be15e13b08967fa7049b848661a3cf8` | **0** | 0 | `1c8add321259a9f026d6e37b0dbd95b0f548f31fe0a10c56098911c21532a6fe` |
| **R28-3** | `tools/gates/argot-derivation-gate.py` | `b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb` | `examples/culture-d4/packet.d4.yml` | `543d68a8…` | **0** | 0 | `1c422ab6a90abb029c0fe0066ac40e50f5e047bf4e5e7e9403a20e6f0e592a8d` |
| R28-3b | `tools/gates/argot-derivation-gate.py` | `b5406bcd…` | `examples/culture-d4/packet.d4.typed.yml` | `15c81ec11b42efaa7d683dd9320bfc7cd9b5d1e812e042d99dbf8d8726ec5da6` | **0** | 0 | `abf0c7c8bd9b…` *(re-hash at integration)* |
| **R28-4** | `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` | `examples/culture-d4/packet.d4.yml` | `543d68a8…` | **1** | **14** | `0c613c9d973f3c32bb20f4db7a43a02da7a5edcaa1bc3382531acce21e2a89f7` |
| R28-4b | `tools/gates/argot-derivation-gate.py` | `b5406bcd…` | `tools/gates/fixtures/argot-derivation-gate.yml` | `c4c35294d581b204482427b3776776c57d1e7f83065a0b5f8f3906c38d8c2ccd` | **1** | **5** | `556d31d6f66715cbcb0c8dc7d5820e0be60b62fae39e304a79537dad06c205a6` |

**R28-1 and R28-2 are the two rows the O seats froze last round**, and this seat's
independent measurements **agree exactly with their successors**: the gates'
verdicts did not change, only the bytes graded. Both stdout shas are
**byte-identical to every earlier row** — `c60820a5…` for the assembly gate (the
round-19, -22, -26 and -27 rows all carry it) and `1c8add32…` for the labels gate.
**A landing that moves the packet but not a gate's verdict text is exactly the
shape a re-pin is for.**

Measured verdicts (this seat, 20:14–20:16Z, `TMPDIR=$PWD/.scratch`):

| row | command | exit | findings | notes |
|---|---|---|---:|---|
| **R28-1** | `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | **0** | 0 | green; **not selftest-capable** (`--selftest` is read as an input path → exit 2). The row must carry no selftest claim |
| **R28-2** | `python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` | **0** | 0 | green; stdout byte-identical to the round-18/22/27 rows |
| **R28-3** | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | **0** | 0 | coverage: `records=183 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0`. **`records` moved `175 → 183`** — the eight RL-4 records entering the packet is a *census* change, and the register domain (`register_scoped=14 derived_pairs=8`) is **unmoved**, which is the honest reading: the new blocks add records, not register-scoped derivations |
| R28-3b | `… examples/culture-d4/packet.d4.typed.yml` | 0 | 0 | `records=207 register_scoped=14 derived_pairs=8 … violations=0 rule_holds=0` |
| **R28-4** | `python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml` | **1** | **14** | 7 `NAME-NEAR` REVIEW + 6 `PHON-INVENTORY` FAIL on the six garment glosses + 1 `CROSS-HOLD` HOLD. **Byte-identical output sha `0c613c9d…` across the round-26 row, the register landing, the law landing and the RL-4 landing** — the new records add no naming finding. **A reproduced red stays red** |
| R28-4b | `python3 tools/gates/argot-derivation-gate.py tools/gates/fixtures/argot-derivation-gate.yml` | **1** | **5** | 4 `D4L-ARGOT-DERIV` + 1 `D4L-ARGOT-RULE`, exactly the committed `.expected`; output sha `556d31d6…` **unchanged across every round** |

### 2.2 The row that is red and must stay red

| row | command | exit | findings | reading |
|---|---|---:|---:|---|
| **R28-5** | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | **2** | 1 | `FAIL L1-profile: packet: pins 86079a6708a0, live 543d68a82640; projection: pins 88a94422b412, live 339bfd83bf66`. **`ok L3b-argot` is still green** — the law leg inside the typed gate passes; only the **pin** leg fails. This row **may not be re-pinned by this seat**: the pins live in `examples/culture-d4/expected-holds.json` and `tools/gates/typed-pipelines.json`, both of which are O-seat files (§4) |

**This is the round's most easily misread red.** The typed gate exits 2 on the
**clean** packet, so it cannot be used as evidence about any tamper (§2.3 of the
sibling capability row says the same). It is a **stale-pin** reading, not a
finding about the delivered design.

## 3. The successor generation — named, not landed

A successor freeze is a **new directory** with its own `freeze.txt` +
`freeze-receipt.json` + `MANIFEST.tsv`, never an in-place edit of
`reports/round-27/pinsweep/frozen/r27-post/`.

```
reports/round-28/pinsweep/frozen/r28-post/
  MANIFEST.tsv          rows R28-1 .. R28-3 (the two D4 adapter gates + the argot leg)
  freeze-receipt.json   supersedes: reports/round-27/pinsweep/frozen/r27-post (input pins 86079a67/88a94422)
  freeze.txt            the rule in prose
  inputs/examples/culture-d4/packet.d4.yml          # copy at 543d68a8…
  inputs/examples/culture-d4/typed-labels.d4.yml    # copy at 339bfd83…
  d4-assembly.out  d4-typed-labels.out
```

Its `supersedes` list must name, at minimum:

| superseded | why |
|---|---|
| `reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv` rows 1-2 | pins `86079a67…`/`88a94422…`; replay reads **2 mismatch / 0 reproduced** today |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/` | 3 rows drift (the round-28 sweep's `J-DIGEST-DRIFT`) |
| `reports/round-27/pinsweep/baselines/d4-typed-labels-check-gate/r27-post/` | 2 rows drift |
| `reports/round-27/pinsweep/v3-baseline-r27/expected.json` | **5 of 58 inputs stale** — it pinned the pre-RL-4 packet |
| `tools/gates/frozen/round-26/post-register/MANIFEST.tsv` rows 2-3 | replay **2 mismatch / 4 reproduced** |
| `tools/gates/frozen/round-26/gate-input/MANIFEST.tsv` rows 2-3 | same class |

**The round-26 generations' red is now three landings old.** At round 27 they
went red on the register-law landing; the RL-4 landing moved their pinned packet
further. They remain **supersession**, never drift.

## 4. The pin files that needed the same treatment — and were re-pinned

**Both landed after this seat's stamp**, and the readings below are kept as the
named-not-landed rows this seat proposed, with the delivered result beside them.

### 4.1 `examples/culture-d4/expected-holds.json` — **RE-PINNED** (`65f5a03e…`)

| field | this seat's reading (`857417e9…`) | delivered (`65f5a03e…`) |
|---|---|---|
| `packet_sha256` | `86079a67…` (**stale**) | **`543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f`** |
| `projection_sha256` | `88a94422…` (**stale**) | **`339bfd83bf66832479b5b8ffbbce708c8be15e13b08967fa7049b848661a3cf8`** |
| `projector_sha256` | `2819f687…` | `2819f687…` (unchanged, as predicted) |
| `counts` | `{"hold": 12, "note": 0, "fail": 0}` | **`{"hold": 12, "note": 0, "fail": 0}`** |
| `revision_note` | round-27 register-law build, revision 2 | names the round-28 landing |

**The counts did not move, exactly as this file predicted, and that is the correct
reading.** The three new blocks add **records, not forms**: no `OR`, `LI` or `EN`
row obliges a surface form, so the twelve garment-form obligations still route to
their twelve record/slot rows. A count that moved here would have been a defect —
which is why §7 rule 9 makes "a count that does not move is not a missing update"
binding on a recording seat.

### 4.2 `tools/gates/typed-pipelines.json` — **RE-PINNED**

All three of its `d4` pins now verify against the live tree:

```
packet      543d68a82640  543d68a82640  OK
projection  339bfd83bf66  339bfd83bf66  OK
expected    65f5a03e092f  65f5a03e092f  OK
```

Its `note` states the rule the re-pin honoured: *"editing this file cannot
silently re-point a run — a stale pin refuses (exit 2, L1-profile) until it is
re-pinned with a command and a date."* The `typed-pipeline-gate` consequently
went from **exit 2 / `FAIL L1-profile`** to **`summary: 20/20 legs passed`,
exit 0** — the round's last red D4 reading.

## 4a. The successor generation — **LANDED, and extended past this file's proposal**

`reports/round-28/pinsweep/frozen/r28-post/` landed at 20:17:09Z with **2** rows;
it was extended to **4** rows and replays **4/4**:

```
$ TMPDIR=/var/tmp/r28-d22 python3 tools/replay-frozen.py \
    reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv | tail -1
REPLAY OK: 4/4 rows reproduced the recorded verdicts
```

| row | gate | input | exit | findings |
|---|---|---|---:|---:|
| 1 | `tools/gates/d4-assembly-check-gate.py` | `examples/culture-d4/packet.d4.yml` | 0 | 0 |
| 2 | `tools/gates/d4-typed-labels-check-gate.py` | `examples/culture-d4/typed-labels.d4.yml` | 0 | 0 |
| 3 | `tools/gates/typed-pipeline-gate.py` | `examples/culture-d4/packet.d4.yml` | 0 | 12 |
| 4 | `tools/gates/typed-pipeline-gate.py` | `examples/culture-d4/packet.d4.typed.yml` | 0 | 12 |

**Rows 1–2 are exactly the two rows §2.1 of this file proposed**, with the same
gate digests, input digests, exits and output shas. **Rows 3–4 close the
`X61R28-A2` gap** — the typed-pipeline gate's two D4 rows, which the round-27
generation and the sweep's first pass both left without a successor. The receipt
names its supersessions explicitly, including
`tools/gates/frozen/round-{22,25,26}/*/MANIFEST.tsv typed-pipeline-gate.py D4 rows
(no successor existed before this generation; round-28 audit X61 finding
X61R28-A2)`.

**Its `supersedes` list is the chain §3 asked for**, and the O seats closed the
gap this seat named rather than leaving it for a later round.

**An independent timing witness that the freeze was taken on settled bytes.** This
seat ran a 20-sample poll at 60 s intervals across 19 minutes
(20:15:40Z–20:34:40Z) recording the packet digest and the tree's file count. **The
packet read `543d68a82640` in all 20 samples**, so the `r28-post` generation
(frozen 20:17:09Z) was taken on bytes that had **already settled** — the opposite
of the round-27 case, where the generation was frozen 2 minutes before a landing
and went red. Rule 7 of §7 ("a freeze taken while the tree is still moving is
already stale") is the discipline this round **honoured**, not merely cited.

The same poll also records the law leg's arrival: `lawleg=` is **empty for all
five samples from 20:15:40Z to 20:19:40Z** and non-empty from **20:20:40Z**
onward, independently dating the gate's landing to the 20:19:40–20:20:40Z window
and confirming that the leg was absent for the first four minutes of the poll.

## 5. The cascade, measured at the final stamp

Replayed with `TMPDIR` **outside** the repo (`/var/tmp/r28-d22`).

| generation | rows | at 20:16Z | reason | notes |
|---|---:|---|---|---|
| `tools/gates/frozen/round-3/MANIFEST.tsv` | 7 | **could-not-evaluate 7/7** | `gate_digest_mismatch` | pins the gates at `291c714` |
| `tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` | 7 | **could-not-evaluate 7/7** | `gate_digest_mismatch` | same class |
| `tools/gates/frozen/round-11/MANIFEST.tsv` | 11 | **could-not-evaluate 1, reproduced 10/11** | `gate_digest_mismatch` | one row pinned `provenance-audit.py` at a superseded revision |
| `tools/gates/frozen/round-18/MANIFEST.tsv` | 2 | **mismatch 2, reproduced 0/2** | `replay_mismatch` | both D4 rows; **superseded in substance** by the round-27/28 D4 generation |
| `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` | 11 | **could-not-evaluate 1, reproduced 10/11** | `gate_digest_mismatch` | row 2 pins `typed-pipeline-gate.py`; the gate moved at round 25 |
| `tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv` | 11 | **could-not-evaluate 1, reproduced 10/11** | `gate_digest_mismatch` | same row class |
| `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` | 3 | **could-not-evaluate 1, mismatch 2, reproduced 0/3** | mixed | rows 2–3 `replay_mismatch` on the moved D4 artifacts; row 4 `gate_digest_mismatch`. **Superseded in substance** |
| `tools/gates/frozen/round-23/repin-d2/MANIFEST.tsv` | 11 | **could-not-evaluate 1, reproduced 10/11** | `gate_digest_mismatch` | same row class |
| `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv` | 6 | **could-not-evaluate 6/6** | `gate_digest_mismatch` | every row pins `typed-pipeline-gate.py` at `879d40bf…` |
| `tools/gates/frozen/round-26/gate-input/MANIFEST.tsv` | 6 | **mismatch 2, reproduced 4/6** | `replay_mismatch` | its two D4 rows pin the pre-register packet |
| `tools/gates/frozen/round-26/post-register/MANIFEST.tsv` | 6 | **mismatch 2, reproduced 4/6** | `replay_mismatch` | **was 6/6 OK at round 27's 19:16Z, red from 19:21Z, still red** — three landings on, and every red is the artifact moving |
| `reports/round-17/tests/frozen/MANIFEST.tsv` | 5 | **reproduced 5/5** | — | green; no D4 row |
| **`reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv`** | 2 | **mismatch 2, reproduced 0/2** | `replay_mismatch` | **was 2/2 OK at round 27's close.** Red because the RL-4 landing moved its pinned packet `86079a67…` → `543d68a8…` |

**Independent confirmation of the class.** `reports/round-28/audit/x61-pin-sweep.py`
re-derives every frozen row itself and classifies each mismatch as
**supersession** (the live input no longer hashes to the pin) or **drift** (a
pinned byte was tampered with). At this stamp:

```
summary: 53/86 rows reproduced; 8 mismatch (8 supersession, 0 drift); 25 could-not-evaluate (25 gate_digest_mismatch); baselines 19/19 pinned
successors: 0/8 superseded rows carry a later row at the live digest (8 do not)
```

**`0 drift` is the single most important sentence in this file for the O claim's
disposition**, and it reproduces the round-27 reading. Every red D4 row is red
because the artifact it graded **moved**.

**The `successors: 0/8` line was the round's real bookkeeping gap, and it has
since closed.** At the sweep's stamp eight superseded rows existed and **none**
carried a later row at the live digest — the round-27 `frozen/r27-post` generation
had itself been superseded by the RL-4 landing. **§4a measures the closure**: the
round-28 `frozen/r28-post` generation now carries **four** rows at the live
digests (two D4 adapters **and** the typed gate's two D4 rows), replays **4/4**,
and its receipt names the superseded generations explicitly, including the
`X61R28-A2` typed-gate gap. **A reader who quotes `0/8` is quoting a superseded
reading**; the successor exists.

## 6. The battery, the v3 chain, and the remaining pin surfaces

### 6.0 The v3 chain — **LANDED**, the round's last red

At this seat's stamp `tools/exercise-handoff-e2e.py:1933` already named
`reports/round-28/pinsweep/v3-baseline-r28/expected.json` and that path did **not
exist**, so `--profile v3` read **exit 2**. The O seats then landed it:

```
$ python3 tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27
            statuses=16/7/4 v2_subset=equal alias_leg=landed
            packet_sha256=a20ae059aa7cac9e28345d1a80a4dae3fa302117e26b5b1405f05b38d12f0001
```

**`exit 0`, every leg green.** This is the reading that flipped `claim O` from FAIL
to PASS in the round's acceptance runner.

### 6.1 The battery

```sh
python3 tools/check-gate-battery.py
# battery_exit 0, pass 7, fail 0, unevaluable 0; coverage "9/9", pinned 19
```

**`pinned 19` does not mean the live tree agrees with the baselines**, and this
file must not let a reader conclude it does. Six baselines are discovered under
`tools/gates/expected/`; all six read **`pinned`** (their `gate_sha256` equals the
live gate and every declared input digest equals the snapshot copy inside the
baseline directory). The baseline's own `freeze.txt` states the rule: *"the
battery's digest step … compares the copy to the pin, never the copy to the live
file"*. The battery is a **snapshot-integrity** check; the live-vs-pin
recomputation is a **different** duty, and it is the one that reads stale (§4).

### 6.2 The v3 handoff chain — the predecessor rows, and the landed successor

| surface | state at this seat's stamp |
|---|---|
| `reports/round-26/handoff/declared-in-r5/expected.json` | **7 of 58 inputs stale** — `01-brief.yml` (`feca7bda…`→`649aa111…`), `03-orthography.yml` (`de1820b0…`→`0f2ff454…`), `09-costumes.yml` (`82fb92ad…`→`f61cc684…`), `expected-holds.json`, `packet.d4.typed.yml`, `packet.d4.yml` (`dd25077b…`→`543d68a8…`, **two landings behind**), `typed-labels.d4.yml` (`d03f6391…`→`339bfd83…`) |
| `reports/round-27/pinsweep/v3-baseline-r27/expected.json` | **5 of 58 inputs stale** — `03-orthography.yml`, `09-costumes.yml`, `packet.d4.typed.yml`, `packet.d4.yml` (`86079a67…`→`543d68a8…`), `typed-labels.d4.yml` (`88a94422…`→`339bfd83…`) |
| `reports/round-28/pinsweep/v3-baseline-r28/expected.json` | **LANDED after this stamp** — `--profile v3` reads **exit 0**, all legs green (§6.0) |
| `tools/exercise-handoff-e2e.py` `V3_BASELINE_DEFAULT` (`:1933`) | points at the round-28 baseline; the constant was re-pointed **before** the baseline landed, which is why the intermediate reading was exit 2 |
| `--profile v2` | **green**: `handoff-v2: exit=0 claims=15 links=50/50 drift=named(tools/harness/packet_links.py round-16)` |

**The v3 chain was the O claim's live surface, and the sequence is the lesson.**
The constant was re-pointed ahead of the artifact, so the tool refused (exit 2)
rather than reading a stale baseline — the designed fail-closed behaviour. The
successor row had to be frozen **and** the run re-measured, not merely re-pinned,
and that is what happened.

### 6.3 The other pinned surfaces

| surface | state |
|---|---|
| `reports/round-26/remainders/r4-twin/`, `v3-baseline-r26/`, `register/v3-baseline-r26/` | `twin.json` `H-DIGEST-DRIFT` (7–8 rows each) on the moved D4 artifacts |
| `reports/round-22/handoff/declared-in/`, `declared-in-r2/` | `twin.json` `H-DIGEST-DRIFT` (8 rows each) — historical, unaffected in substance |
| `reports/round-9/baselines/` (legacy battery root) | discovered by the battery; no D4 row, unaffected |
| `reports/round-27/pinsweep/baselines/*/r27-post/` | `J-DIGEST-DRIFT` (3 and 2 rows) — the round-27 successor baselines are themselves now stale |
| `reports/round-27/pinsweep/frozen/r27-post/freeze-receipt.json` | `J-DIGEST-DRIFT` (2 rows) — its `input_pins` name the pre-RL-4 packet |

## 7. Freeze rules a recording seat must honour (binding)

1. **New generation, new rows.** A round-28 generation is a new directory; no
   earlier `MANIFEST.tsv`, `expected.json`, `freeze.txt` or receipt is edited.
2. **A freeze receipt that is not a battery baseline is not named
   `expected.json` under a battery root.** Use `freeze.txt` + `freeze-receipt.json`
   (the round-22/25/26/27 shape).
3. **`TMPDIR` outside the repo, always.** §5a.
4. **A row the gate cannot prove does not enter the file.**
   `d4-assembly-check-gate.py` has no `--selftest` (§2.1 R28-1).
5. **A red verdict reproduces as red.** R28-4 is exit 1 / 14 findings, R28-4b is
   exit 1 / 5, and R28-5 is exit 2 / 1 — none may be "cleaned", and R28-5's red is
   a **stale pin**, not a design finding.
6. **A `supersedes` pointer is part of the row's content.** §3 names the six
   superseded generations the round-28 successor must carry, and §5 measures
   `successors: 0/8` — the gap this generation closes.
7. **A freeze taken while the tree is still moving is already stale.** §1 is the
   worked instance: the round-27 generation was frozen at 19:21:44Z and was
   superseded at 20:13Z the next round. **Freeze after the landing settles, and
   name the revision you froze against.**
8. **A `run.log` under a battery baseline is gitignored** by `.gitignore:3`
   (`*.log`) and must be force-added by the parent.
9. **A count that does not move is not a missing update.** §4.1: the hold counts
   stay 12/0/0 across the RL-4 landing because the new blocks add records, not
   forms. **Re-pin the digests; do not manufacture a count movement.**

### 7.1 The `TMPDIR` control

```sh
export TMPDIR=$PWD/.scratch        # inside the repo
python3 tools/replay-frozen.py tools/gates/frozen/round-26/post-register/MANIFEST.tsv
# every row reads mirror_unsafe, exit 2:
#   detail: mirror: temporary root is inside the repo: …/.scratch/replay-frozen-XXXX
```

Re-measured this round by the round-28 `x61` instrument's own probe:
`inside-repo: 0 reproduced, 0 mismatch, 6 could-not-evaluate (6 mirror_unsafe)` /
`outside-repo: 4 reproduced, 2 mismatch, 0 could-not-evaluate (0 mirror_unsafe)`.
A recording seat that runs the replay from the lane's usual scratch shape sees a
**refusal rather than a verdict** — the designed behaviour
(`tools/replay-frozen.py:177`). §5's commands use `/var/tmp/r28-d22`.

## 8. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
mkdir -p /var/tmp/r28-d22
sha256sum tools/gates/*.py examples/culture-d4/*.yml examples/culture-d4/*.json \
  tools/gates/typed-pipelines.json
find tools/gates/frozen -name MANIFEST.tsv | sort
for m in $(find tools/gates/frozen -name MANIFEST.tsv | sort); do
  printf "%-56s " "$m"
  TMPDIR=/var/tmp/r28-d22 python3 tools/replay-frozen.py "$m" | tail -1
done
TMPDIR=/var/tmp/r28-d22 python3 tools/replay-frozen.py \
  reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv | tail -1   # 2 mismatch / 0 reproduced
python3 tools/check-gate-battery.py                                  # 7 pass / 0 fail; coverage 9/9
python3 reports/round-28/audit/x61-pin-sweep.py | tail -3            # 8 mismatch (8 supersession, 0 drift)
python3 reports/round-28/sweep/sweep.py | tail -20
python3 tools/exercise-handoff-e2e.py --profile v2 --quiet           # exit 0
python3 tools/exercise-handoff-e2e.py --profile v3 --quiet           # exit 2 (baseline not landed)
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -3
python3 -c "import json,hashlib,pathlib; d=json.load(open('examples/culture-d4/expected-holds.json')); \
  print(d['packet_sha256'][:12], hashlib.sha256(pathlib.Path('examples/culture-d4/packet.d4.yml').read_bytes()).hexdigest()[:12])"
```

## 9. Limits

- The rows in §2.1 and §6 are **measured today** on the live tree; they are the
  rows a round-28 generation records. They are not filed — this seat writes no
  `MANIFEST.tsv` and no `expected.json`.
- The successor generation in §3 and the successor pins in §4 are **named, not
  landed**.
- **Every reading binds to the digest and stamp beside it, and the tree moved once
  in this seat's window.** A successor must re-hash before quoting any digest
  here. In particular **every round-27 artifact's D4 digest is one landing out of
  date**, and the round-26 artifacts' are three.
- **This file makes no claim that the round-28 O claim is met.** It measures the
  cascade, names the six superseded generations, and names the gap
  (`successors: 0/8`) the round-28 generation must close.
- A freeze pins bytes and verdicts, never design quality, scholarship, lore
  standing or promotion. This file admits nothing.
