# R11-D01 — Design: wiring the typed-label projection into the D2 gate flow

Seat: D01 (design lead), round 11, claim **D (depth)**. Written 2026-10-17, cwd = lane root
`kotodama-shokunin/`. This file names the wiring, fixes the interfaces for shards D03–D26, and
declares the **expected hold set** for `examples/culture-d2` from executed tool output.

Base revision `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7` (`git rev-parse HEAD`, 2026-10-17). Every
pin below is as-read at 2026-10-17T19:0x-03:00 and is conditional on that revision: sibling round-11
seats are editing `tools/` and `examples/` concurrently, so a pin that no longer matches is a
re-read event, never a licence to compare across revisions.

Inputs read (sha256, `sha256sum`, 2026-10-17T19:04-03:00):

| path | sha256 | role |
|---|---|---|
| `examples/culture-d2/packet.d2.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` | gate-facing packet (assembler output) |
| `examples/culture-d2/typed-labels.d2.yml` | `e70ba1477dbeb830061db6fd12516b7d902587bddae173f55a3650015d380b2f` | round-8 typed projection |
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` | projector (round 8) |
| `tools/assemble-d2.py` | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` | D2 assembler |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` | sound/identity channel reader |
| `tools/gates/phonology-sanity-gate.py` | `d5fe087ffb2342e54cd6d6f3ef1e891315a95224bc25cdc5bc425b91dec34230` | inventory reader (= r9-pre pin) |
| `tools/gates/costume-era-consistency-gate.py` | `e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f` | era/material reader |

---

## 1. The live state the wiring must change

### 1.1 The legacy flow pronounces ten English glosses

`python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml` (2026-10-17,
stdout sha256 `ebc8850d08ec1b7e32616cbca9092ba66f3b6f148a61515a033e6bed6fa66f4b`, exit 1) emits
17 finding lines: `PHON-INVENTORY` ×10, `NAME-NEAR` ×6, `CROSS-HOLD` ×1. The ten are the costume
glosses, e.g.

```
FINDING PHON-INVENTORY: FAIL — name GAR-01 'winter valley coat (heavy felted wool; uncombed finish
optional)': symbol /v/ at position 7 is not in the declared inventory …
```

The mechanism is exact: `tools/gates/naming-collision-gate.py` builds its entity inventory from
`("costumes", "garment", "garment")` (`:670`), so the reader-facing English gloss sits on the
name/sound channel. This is the round-4 `PHON-INVENTORY` class already diagnosed as a
representation artifact (`examples/culture-d2/ASSEMBLY.md:94`, `SKILL.md:86`).

### 1.2 The typed projection already knows the right answer

`python3 tools/d2-typed-labels.py --json` (exit 1, stats `{fail: 0, hold: 15, note: 1, labels: 58}`)
types all 58 form-bearing records across three kinds and emits 16 findings — 15 holds and 1 note,
**zero fails**. Coverage: `labels_by_kind = {translated-label: 10, native-form: 46,
borrowed-strata: 2}` with the ten `translated-label` records routed off both the sound and the
identity channel (`reports/round-8/depth/design-spec.md`, T1 table in
`reports/round-8/depth/skill-table-draft.md:105-146`).

The split is exact and total: 10 `translated-label` records (`GAR-01..GAR-10`, source
`11-costumes.yml` field `garment`), 46 `native-form` supplied (38 lexicon `term` L-01..L-40 minus
L-26/L-27, plus 8 names NM-01..08 `name`), 2 `borrowed-strata` supplied (L-26, L-27).

### 1.3 The routing mechanism is measured, not assumed

Two scratch experiments over byte copies of the packet (scratch only; no repository file written):

1. **One record routed.** `GAR-01`'s checked field renamed `garment:` → `garment_gloss:`
   (`.scratch/d01/packet-route-gar01.yml`, stdout `.scratch/d01/route.out` sha256
   `842d606a1cc2d6ffb1c5368a90f75e69ff399f3d662dd47748d1bd2a7124505c`) → naming gate 17 → 16
   findings, `PHON-INVENTORY` 10 → 9, **no other line changed**.
2. **All ten routed.** `.scratch/d01/packet-all-routed.yml` → naming gate exit 1, 7 findings
   (`NAME-NEAR` ×6, `CROSS-HOLD` ×1), `PHON-INVENTORY` ×0 (stdout sha256
   `feb6488127f115f986bf7602c0b074ce911c951751e5e2c63e32e5d23bb52bd9`).

The four remaining gates are byte-unchanged between the legacy and the all-routed run
(phonology 3 findings / `1ce5f0cdabad1bda177245607226cb6bf643f2bfbbe2ddb0918c510749066dd2`;
lexicon, myth and costume each 0 findings / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`).

> **The channel differential is exactly the ten `PHON-INVENTORY` lines.** No cascade, no new finding,
> no lost finding. That is the wiring's measurable signature and the L2 leg of §3.

### 1.4 Two blocking facts the flow must handle

- **The committed projection is stale by one pin line.**
  `python3 tools/d2-typed-labels.py --check` exits 1: the projection records
  `packet_sha256 8da90b07…` while the packet now hashes `e0f21509…` (the packet was re-assembled at
  17:40, after the projection was emitted at 17:33). `diff` over the emitted bytes shows **one**
  differing line — `assembly.packet_sha256` — so the re-pin is mechanical and its predicted result is
  byte-exact (§5.1).
- **The round-3 frozen manifest no longer replays.**
  `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` exits **2** with
  "REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate … gate_digest_mismatch" for all 7 rows: the five
  gate scripts have been revised since round 3, and `replay-frozen.py` verifies `gate_sha256` *before*
  running any row. Consequence: "frozen replay re-pinned and green" **cannot** mean re-pointing the
  round-3 manifest at today's gates. It means a **new** frozen revision for the typed run (§5.2), with
  the old manifests left exactly as filed, and the divergence reported, not repaired.

---

## 2. Where typed labels enter assembly

### 2.1 Three artifacts, one direction

```
components/ (15 files)
   │  tools/assemble-d2.py                      [unchanged]
   ▼
examples/culture-d2/packet.d2.yml  (gate-facing, committed, --check green)
   │  tools/d2-typed-labels.py                  [unchanged; re-pinned to the packet]
   ▼
examples/culture-d2/typed-labels.d2.yml  (typed projection, committed)
   │  tools/assemble-d2-typed.py               [NEW — adapter, D03/D04]
   ▼
packet.d2.typed.yml  (typed packet, BUILD PRODUCT — gates read this)
```

Typed labels enter assembly **at the adapter step**, not inside `assemble-d2.py` and not inside
`d2-typed-labels.py`. Reasons, in order of weight:

1. `python3 tools/assemble-d2.py --check` is part of the claim's counting command and is green today;
   changing the assembler's output would invalidate the committed packet bytes and every pin on them.
2. The projector's own contract is "read-only over components, packet and gates; the packet is never
   rewritten" (projection `assembly.notes[0]`). The adapter honours that by emitting a *derived
   packet*, never touching the original.
3. The derived packet is a build product: it is regenerated on every e2e run and is frozen only as a
   copy inside a baseline directory (§5.2), so it can never rot in `examples/`.

### 2.2 Adapter contract — `tools/assemble-d2-typed.py` (NEW; single writer, D03/D04)

```
python3 tools/assemble-d2-typed.py [--packet P] [--projection J] [--emit PATH] [--check [PATH]] [--selftest]
```

Inputs and fail-closed rules:

| check | rule | on failure |
|---|---|---|
| assembler identity | `--packet` bytes equal `assemble-d2.py`'s deterministic assembly (call the assembler's own build path; do not re-implement) | exit 2 |
| projection freshness | projection's `assembly.packet_sha256` equals sha256 of `--packet` bytes; and `d2-typed-labels.py --check` reproduces the projection byte-for-byte | exit 2 (stale pin is a hard error, never a warning) |
| coverage | every record the projector types as an off-channel kind has exactly one routing row; every routed record exists in the packet; no routing row names a record the projector did not type | exit 2 |
| determinism | two consecutive builds are byte-identical; `--check` compares bytes without writing | exit 1 |

Output: one deterministic YAML-subset document containing the packet's blocks plus

```yaml
typed_channel:            # the routing table, one row per off-channel record
  - record: GAR-01
    kind: translated-label
    label_id: LEX-GAR-01
    owner: 11-costumes
    source_field: garment          # the packet field this record used to be checked on
    off_channel_field: garment_gloss
    channel: off-sound-and-identity
    hold: D2L-FORM-UNRESOLVED
assembly:                 # pins, verbatim from the projection plus the adapter's own digest
  packet_sha256: …
  projection_sha256: …
  adapter_sha256: …       # self-digest, so the freeze row's gate hash transitively pins this file
```

### 2.3 Routing rules (kind → channel)

| projector kind / status | checked field in the typed packet | hold carried | authority |
|---|---|---|---|
| `translated-label` (any status) | checked field moved to `*_gloss`; **not on sound or identity channel** | `D2L-FORM-UNRESOLVED` per owed slot | T1 row 1; `era-language-staging.md:124` |
| `native-form`, `status: supplied` | checked field unchanged — native bytes govern | none from routing (projector may still hold, §4) | T1 row 2 |
| `native-form`/`borrowed-strata`, `status: absent`/`to-verify` | checked field moved off-channel | `D2L-FORM-UNRESOLVED` | T1 row 3 ("silent pass forbidden") |
| `borrowed-strata`, `status: supplied` | checked field unchanged, recipient-adapted; borrow-ledger checks stay | none from routing | T1 row 4 |
| untyped legacy record | checked field unchanged | none | T1 row 6 ("adding typing fields cannot exempt a string") |
| kind not asserted (1 discriminator) | off-channel, kind not written | `to-verify` hold with the discriminator named | T1 row 5 |

For `examples/culture-d2` today the routing table has exactly **ten rows**, all `translated-label /
to-verify`, all `11-costumes.yml` field `garment` → `garment_gloss`, all holding
`D2L-FORM-UNRESOLVED`. Nothing else is routed: the 46 supplied native forms and 2 supplied loans stay
on the checked channel, which is why §1.3's differential is exactly ten lines.

---

## 3. How the gates receive the typed packet

### 3.1 Four evaluation legs

Entry point (new, gate-shaped so `tools/replay-frozen.py` can pin it):
`tools/gates/typed-pipeline-gate.py` — single writer D05.

```
python3 tools/gates/typed-pipeline-gate.py [PACKET]   # default examples/culture-d2/packet.d2.yml
python3 tools/gates/typed-pipeline-gate.py --selftest
python3 tools/gates/typed-pipeline-gate.py --json
```

| leg | what it does | passes when |
|---|---|---|
| **L1 → build** | `assemble-d2.py` build check; projector run over the packet; adapter emits the typed packet into a temp mirror (never into `examples/`) | all three steps exit 0 |
| **L2 → channel** | runs the five culture gates over the **legacy** packet and over the **typed** packet (isolated mirror copies) and diffs the two stdout streams | typed findings = legacy findings **minus exactly the ten `PHON-INVENTORY` lines** naming `typed_channel` records, and **zero** typed-run finding line names an off-channel record |
| **L3 → holds** | extracts the pipeline finding set from the typed run (projector findings carried in the typed packet) | the hold set equals the frozen expected set **exactly**, the note set equals the pinned note set, the fail set is empty (§4) |
| **L4 → pins** | re-verifies `packet_sha256`, `projection_sha256`, `adapter_sha256` embedded in the typed packet | all three match the bytes read |

Source gates are invoked read-only, from their repository paths, by sha recorded in the gate's own
constants block (the pins are covered transitively by `gate_sha256` — see §5.2 on circularity).

### 3.2 Exit semantics — and the anti-laundering rule

```
0  L1–L4 all pass: the pipeline emitted exactly the frozen expected hold set
1  any leg mismatched (channel, hold set, note set, fail set, determinism)
2  could-not-evaluate: stale projection pin, malformed packet, gate traceback, pin mismatch
```

Exit 0 must never be readable as "the culture is clean". The gate therefore prints, before the
finding lines, one banner line naming the semantics:

```
TYPED-PIPELINE: exit 0 = the emitted findings equal the frozen expected hold set; every hold below is
still open design debt.
```

and it **emits the 15 hold lines verbatim** (`FINDING D2L-…: [hold] <where> — <detail>`), so the
artifact a reader sees is red at the design level. A hold laundered into a note, deleted, or renamed
fails L3 (§6.3). Because the ten `PHON-INVENTORY` FAILs are *replaced* by ten named holds, the
aggregate verdict stays red exactly as `reports/round-8/depth/skill-table-draft.md:105-146` requires:
"removing a gloss from the sound channel removes an artifact; it does not clear the name."

### 3.3 Why the five gate scripts are never edited

Measured, not asserted:

- `replay-frozen.py` verifies `gate_sha256` before running a row (`tools/replay-frozen.py` docstring,
  step 2); one edited gate byte turns its rows into `could-not-evaluate` / exit 2.
- Each round-9 baseline pins `gate_sha256` and `stdout_sha256`
  (`tools/gates/expected/phonology-sanity-gate/r9-pre/expected.json`), and
  `tools/check-gate-battery.py` re-verifies those pins. Today the live phonology gate sha equals the
  pin (`d5fe087f…`); the round-9 freeze control already demonstrated that gate edits are invisible to
  stdout and visible only to the digest.
- The wiring needs no gate edit: routing the record off the checked field removes the finding at the
  source (§1.3). The "gate's own reader" limitation recorded at
  `reports/round-8/depth/skill-table-draft.md` §7 is answered by *what the gate is handed*, not by
  changing the gate — a decision the D20 wiring-vs-spec reviewer should attack first.

---

## 4. EXPECTED HOLD SET for `examples/culture-d2` — the contract

### 4.1 Derivation

Command (2026-10-17, cwd = lane root, `TMPDIR=$PWD/.scratch`):

```
python3 tools/d2-typed-labels.py --json > .scratch/typed.json      # exit 1
python3 -c 'import json; d=json.load(open(".scratch/typed.json")); [print(f["id"], f["severity"], f["where"]) for f in d["findings"]]'
```

Projector sha256 `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`, packet sha256
`e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643`, stats
`{fail: 0, hold: 15, note: 1}`.

### 4.2 The 15 holds (each named)

| # | finding id | severity | `where` | class / reason | source |
|---|---|---|---|---|---|
| 1 | `D2L-FORM-UNRESOLVED` | hold | `GAR-01` | `LEX-GAR-01` has no supplied native/borrowed form | 11-costumes gloss, off-channel |
| 2 | `D2L-FORM-UNRESOLVED` | hold | `GAR-02` | as above | 11-costumes gloss, off-channel |
| 3 | `D2L-FORM-UNRESOLVED` | hold | `GAR-03` | as above | 11-costumes gloss, off-channel |
| 4 | `D2L-FORM-UNRESOLVED` | hold | `GAR-04` | as above | 11-costumes gloss, off-channel |
| 5 | `D2L-FORM-UNRESOLVED` | hold | `GAR-05` | as above | 11-costumes gloss, off-channel |
| 6 | `D2L-FORM-UNRESOLVED` | hold | `GAR-06` | as above | 11-costumes gloss, off-channel |
| 7 | `D2L-FORM-UNRESOLVED` | hold | `GAR-07` | as above | 11-costumes gloss, off-channel |
| 8 | `D2L-FORM-UNRESOLVED` | hold | `GAR-08` | as above | 11-costumes gloss, off-channel |
| 9 | `D2L-FORM-UNRESOLVED` | hold | `GAR-09` | as above | 11-costumes gloss, off-channel |
| 10 | `D2L-FORM-UNRESOLVED` | hold | `GAR-10` | as above | 11-costumes gloss, off-channel |
| 11 | `D2L-NATIVE` | hold | `L-15` | supplied `sára` carries `á` outside the segment inventory; acute accent declared by 02-phonology's own minimal pair, so held for the form's owner, not failed | native form on channel |
| 12 | `D2L-NATIVE` | hold | `L-16` | supplied `sará`, same reason | native form on channel |
| 13 | `D2L-RANK` | hold | `TR-04#a\|TR-06#a` | act-collision: genuine-priority-gap | rank adapter |
| 14 | `D2L-RANK` | hold | `WR-02#g\|WR-09#g` | R-05-class: genuine-priority-gap | rank adapter |
| 15 | `D2L-RANK` | hold | `WR-08#g\|WR-09#g` | R-05-class: genuine-priority-gap | rank adapter |

The first ten are **new to this wiring** (they replace the ten `PHON-INVENTORY` FAILs). Items 11–15
already exist in the round-8 projection and are carried through unchanged by the wiring — they are in
the set because L3 compares the *whole* pipeline finding set, and a wiring that silently dropped them
would be indistinguishable from one that fixed them.

### 4.3 The excluded note and the empty fail set

| id | severity | `where` | detail | disposition |
|---|---|---|---|---|
| `D2L-RANK` | **note** | `SR-01#a\|SR-01#b` | act-collision: band-keyed-pair | pinned, **excluded from the hold set** |

Fail set: **∅**. A fail anywhere in the pipeline finding set is an automatic L3 mismatch.

### 4.4 Exactness rules

1. The comparison key is the triple `(id, severity, where)`, as a **set** (order-insensitive), plus the
   counts `hold = 15`, `note = 1`, `fail = 0`.
2. Hold set == table 4.2 exactly: no extra hold, no missing hold, no severity swap. The note in 4.3
   must be present and must **not** be counted as a hold.
3. `detail` strings are pinned too (full finding objects, canonical JSON, sorted by `(id, where)`): a
   prose rewrite re-pins the baseline explicitly. Advisory-drift-only comparison is **rejected** — it
   is the exact laundering channel this round's negative control D19 probes.
4. The set is over the **typed run** only. The legacy run's ten `PHON-INVENTORY` FAILs are not part of
   the set; they are the minus-basis of L2.

### 4.5 Committed baseline

`examples/culture-d2/expected-holds.json` (new; writer D06, reviewer D21) — canonical JSON:

```json
{"schema": "kotodama-typed-pipeline-holds-v1",
 "packet_sha256": "e0f21509…", "projection_sha256": "e70ba147…",
 "projector_sha256": "0da0015f…",
 "counts": {"hold": 15, "note": 1, "fail": 0},
 "holds": [ {"id": "D2L-FORM-UNRESOLVED", "severity": "hold", "where": "GAR-01", "detail": "…"}, … ],
 "notes": [ {"id": "D2L-RANK", "severity": "note", "where": "SR-01#a|SR-01#b", "detail": "…"} ]}
```

The gate's `--selftest` must assert its embedded `EXPECTED_HOLDS` constant equals this file
(both directions), so the constant and the committed record cannot drift apart.

---

## 5. Freeze and re-pin mechanics

### 5.1 Projection re-pin (mandatory, one line)

`python3 tools/d2-typed-labels.py --emit <path>` reproduces the projection; against the committed file
the only difference is `assembly.packet_sha256`. Predicted post-re-pin bytes:
`a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`
(measured on the emitted scratch file `.scratch/proj-emit.yml`, 2026-10-17, 3010 lines, same line count
as the committed projection). Procedure: emit to a scratch path, `cmp` against the committed file,
record both shas, then move the re-pinned bytes into place and re-run `--check` (must exit 0). The old
and new shas go in the round-11 fragment ledger (D24); no file under `reports/round-8/**` is touched.

If the packet changes again during round 11, the prediction moves — re-derive, never force the
predicted hash to hold.

### 5.2 New frozen revision for the typed run

`tools/gates/expected/typed-pipeline/r11/` (writer D08, reviewer D23):

```
packet.d2.typed.yml     frozen copy of the build product, input of the replay row
packet.d2.yml           frozen copy of the base packet (byte copy at freeze time)
expected.json           schema kotodama-frozen-run-v1: command, exit 0, finding-count 15,
                        finding-ID set, stdout_sha256, gate_sha256 of the typed-pipeline gate,
                        inputs{packet.d2.typed.yml, packet.d2.yml}, tool_pins{projector, adapter,
                        reader gates} — the pins live inside the pinned gate as constants
run.log                 verbatim stdout of the graded command
freeze.txt              steps, controls, tamper evidence (r9-pre `freeze.txt` is the template)
```

Replay row (append to a **new** manifest, e.g. `tools/gates/frozen/round-11/MANIFEST.tsv`):
`gate=tools/gates/typed-pipeline-gate.py`, `input=tools/gates/expected/typed-pipeline/r11/packet.d2.typed.yml`,
recorded `exit_code=0`, `finding_count=15`, `output_sha256` of the recorded stdout, `input_snapshot` =
the frozen copy. Green = `python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv`
exits 0. `replay-frozen.py` requires the gate to sit directly under `tools/gates/` — satisfied.

**Circularity guard (D22's target).** The freeze record must never be authored by the same step that
decides the expectation. Concretely: `expected.json`'s hold set is *read off the projector's live
output* (independent tool, sha pinned), and the gate's internal constant is *asserted equal* to the
committed `expected-holds.json`; if a re-pin were used to bless a new hold, both the adapter's coverage
check (§2.2) and L2's channel differential (§3.1) would have to move with it, and the reviewers can see
that in the diff of two frozen revisions. A re-pin that changes the hold set is reported as a finding,
not a pass.

### 5.3 What is NOT re-pinned

- `tools/gates/frozen/round-3/MANIFEST.tsv` and its snapshots: filed. They replay exit 2 today because
  the gates moved on (§1.4). Report the divergence; do not rewrite the pins.
- The five `r9-pre` baselines (`tools/gates/expected/{phonology-sanity-gate,costume-era-consistency-gate}/r9-pre/`,
  `tools/gates/frozen/{handoff-packet-check,lexicon-coverage-audit,provenance-audit}/r9-pre/`): pins
  still verify; the typed run reads the same five gates and must not disturb them.

### 5.4 Pre-wire green baseline for the "remain green" leg

Recorded before any wiring lands (2026-10-17T19:0x-03:00), so a later red is attributable:

| check | pre-wire verdict |
|---|---|
| `python3 tools/assemble-d2.py --check` | exit 0, "byte-identical deterministic assembly" |
| `python3 tools/d2-typed-labels.py --selftest` | exit 0, "39/39 checks passed" |
| `python3 tools/d2-typed-labels.py --check` | **exit 1** — the one stale pin line (§1.4) |
| `python3 tools/assemble-culture-d3.py --check` | exit 0, "byte-identical deterministic assembly" (packet.json + packet.gates.yml) |
| `python3 tools/assemble-culture-d3.py --selftest` | exit 0, "85/85 checks passed" |
| `python3 tools/check-gate-battery.py` | exit 2 / `{pass: 7, fail: 0, unevaluable: 0, findings: []}`, 5 baselines `pinned`, 2 gates uncovered (`myth-consistency-gate.py`, `naming-collision-gate.py`) |

The battery's exit 2 is a **coverage** verdict, not a regression: every baseline that exists is pinned
and clean, and the two uncovered gates' baselines live under `reports/round-9/baselines/`, outside the
battery's default roots. "Battery remains green" therefore means: same five pins verifying, `pass: 7`,
`fail: 0`, `findings: []` — and the exit-2 coverage gap unchanged (a pre-existing condition to report,
not to absorb).

---

## 6. Negative controls (D17–D19) keyed to mechanism

| control | injected fault | must be caught by | how it shows |
|---|---|---|---|
| **D17 — gloss smuggled onto the sound channel** | typed packet where a `typed_channel` record's gloss is left in its checked field (`garment`, `case`-equivalent of §1.3 experiment 1) | L2 | a typed-run finding line names an off-channel record (`PHON-INVENTORY` for `GAR-0N`) → channel violation, exit 1. The legacy run already contains this finding, so the detector has teeth by construction |
| **D18 — owed form dropped silently** | adapter that omits a routing row / a hold for a `translated-label` with no supplied form | adapter coverage check (§2.2) **and** L3 | routed set ≠ typed off-channel set → exit 2 at the adapter; if it got past the adapter, the hold count drops to 14 → L3 mismatch |
| **D19 — hold laundered as clean** | hold downgraded to `note`, renamed, or removed in the finding set | L3 (notes are pinned separately and never counted as holds) | hold count ≠ 15 or an unpinned note appears → exit 1 |

Each control runs in an isolated temp tree under `TMPDIR=$PWD/.scratch` and asserts (a) the exit code,
(b) the specific violating line/set difference, so a control that merely fails for an unrelated reason
cannot be counted as a pass.

---

## 7. Shard interface map (collision avoidance)

| shard | file(s) — single writer | interface consumed |
|---|---|---|
| D03/D04 | `tools/assemble-d2-typed.py` | projection + packet (§2.2) |
| D05 | `tools/gates/typed-pipeline-gate.py` | typed packet + expected constant (§3) |
| D06 | `examples/culture-d2/expected-holds.json` | projector output (§4.5) |
| D07 | (no new file) projection re-pin procedure + receipt | §5.1 |
| D08 | `tools/gates/expected/typed-pipeline/r11/**`, `tools/gates/frozen/round-11/MANIFEST.tsv` | §5.2 |
| D09–D16 | test receipts under `reports/round-11/depth/**` | this design's legs L1–L4 |
| D17–D19 | negative controls under `reports/round-11/depth/neg/**` | §6 |
| D24–D26 | capability row / frozen records / fragment ledger | SCORECARD row `d2-typed-pipeline` |

No shard edits the five gate scripts, `tools/assemble-d2.py`, `tools/d2-typed-labels.py`, or any file
under `reports/round-{8,9,10}/**`.

---

## 8. Open items, to-verify, and out-of-province

1. **Realized-shard confirmation (to-verify).** Sibling D-seats were already executing during this
   design pass (`.scratch/d11/`, `.scratch/d12/build-typed-manifest.py`, `.scratch/d16/`, `.scratch/d24-poll.log`
   — uncommitted scratch). Their step names (`s1-assemble`, `s2-typed-emit`, typed-manifest build) match
   §2.1/§5.2, but no landed file confirms conformance; D20 (wiring vs design spec) is the check.
2. **Naming gate `exit 1` after routing (to-verify).** The all-routed run still exits 1 with zero FAIL
   lines (6 REVIEW + 1 HOLD). Any leg that keys off the *exit code* of the naming gate must therefore
   key off finding classes instead; the design's L2 does exactly that.
3. **`to-verify` hold for declared-sound-kind-without-bytes (carried defect).** Round-10 shard-05 (N2)
   found the projector silent for `native-form, status: to-verify` with no bytes, against design-spec
   R5. The routing table (§2.3) requires that class to be off-channel **and** held; if the projector is
   still silent there, the adapter must inject the hold itself and the deviation must be reported as a
   finding against the projector, not silently patched into the typed packet.
4. **Detail-string pinning may be contested.** §4.4(3) pins prose details, which makes every wording
   edit a re-pin. That is deliberate (it is the D19 defence) but a reviewer may prefer a
   detail-digest-with-advisory rule; the trade-off is named here so it is decided, not drifted.
5. **Out of province (report, never absorb).** Canon status of the ten owed garment forms (lore);
   whether a real project would license an English gloss as an in-world name (lore);
   any real-world-language claim about the glosses (not asserted here).

---

## 9. Sources

Repo-relative paths, sha256 as read 2026-10-17T19:0x-03:00 at revision
`e3ef1719c123ab4fb83ed94e033961dd61a2e8c7` (lane HEAD; `git status --porcelain` showed only sibling
edits, no commit was made by this seat):

- `tools/d2-typed-labels.py` `0da0015f…` — command `python3 tools/d2-typed-labels.py --json`, `--selftest` (39/39), `--check` (exit 1), `--emit` (predicted `a3aa452c…`)
- `examples/culture-d2/packet.d2.yml` `e0f21509…`; `examples/culture-d2/typed-labels.d2.yml` `e70ba147…`
- `tools/assemble-d2.py` `8ea6bdde…`; `tools/assemble-culture-d3.py` (`--check` exit 0, `--selftest` 85/85)
- `tools/gates/naming-collision-gate.py` `d9e4e8f4…` (`:670` costume channel), `tools/gates/phonology-sanity-gate.py` `d5fe087f…`, `tools/gates/costume-era-consistency-gate.py` `e6bffd70…`
- `tools/replay-frozen.py` (pin-before-run semantics), `tools/check-gate-battery.py` (exit codes `:31-43`), `tools/gates/expected/phonology-sanity-gate/r9-pre/{expected.json,freeze.txt}`
- `reports/round-8/depth/design-spec.md`, `reports/round-8/depth/skill-table-draft.md:105-146,276-303` (T1 routing, §7 limits), `reports/round-10/drift/shard-05.md` (N2, id drift)
- `examples/culture-d2/ASSEMBLY.md:94` (the ten `PHON-INVENTORY` FAILs), `SKILL.md:86,88,90`
- Scratch receipts (uncommitted, `TMPDIR=$PWD/.scratch`): `.scratch/d01/route.out` `842d606a…`, `.scratch/d01/allrouted-naming-collision-gate.out` `feb64881…`, `.scratch/d01/naming-collision-gate.out` `ebc8850d…`, `.scratch/d01/phonology-sanity-gate.out` `1ce5f0cd…`, `.scratch/d01/replay-round3.out` `76c00a6b…`, `.scratch/d01/battery.out` `7bfcd18b…`, `.scratch/typed.json`, `.scratch/proj-emit.yml` `a3aa452c…`

No web retrievals were made for this design; every claim is a repo file, a command output, or a scratch
receipt with a hash.
