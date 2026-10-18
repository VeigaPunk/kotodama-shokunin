# Round 25 — O R25-O08..O10 — gate-input verify + re-pin

- **Seat:** R25-O-gate-input (verify + re-pin), claim O, round 25.
- **Date:** 2026-10-18. Times are **UTC−03:00**.
- **Scope:** verify that feeding the derived packet back can no longer manufacture
  findings, that the documented source-packet entry still passes, that the gate
  still refuses bad input, and land the **new frozen rows** for both input
  classes. The v3-supersession half of claim O is a sibling seat's write
  (`reports/round-25/v3-supersession/`) and is not measured here.
- **Non-author statement:** this seat wrote `tools/gates/typed-pipeline-gate.py`
  (the input-class fix, see the collision note in §6),
  `tools/gates/frozen/round-25/gate-input/` and this file. No other file was
  written; no round-8–24 filed artifact was edited; no commit or push.
- **Scratch discipline:** `export TMPDIR=$PWD/.scratch` before every
  scratch-writing command; replays were run with `TMPDIR=/tmp` because
  `tools/replay-frozen.py` refuses an in-repo mirror root as `mirror_unsafe`
  (documented in the round-23 freeze notes). All measured outputs are quoted
  inline below.

## 1. What was wrong (both mechanisms reproduced, not inferred)

Measured 2026-10-18, gate at its round-25 predecessor digest `04ad4bb4…`:

| Command | Exit | Result |
|---|---|---|
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 | 19/19 legs — the documented canonical green |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | 1 | **14/16 legs** — `L2-channel` with 8 `DERIV-REPLAY` FAILs (`NM-01`…`NM-08`) and `L3-routing-consistency` showing six `null` routing scalars |

Two independent causes, each reproduced in isolation:

- **L2 — the rebuild is not byte-faithful.** The gate reconstructed the legacy
  packet from the typed one through `tools/assemble-d2.py`'s `yaml_lines`. That
  serializer's `scalar` runs every string through `json.dumps`, which
  **double-escapes backslashes** and re-quotes the string `"null"`/`"false"`.
  The rebuild of `packet.d4.typed.yml` is **65,128 bytes against the source's
  82,859**, and differs on `morphology.derivation_rules[0].pattern`
  (`^(?P<a>.+)\+(?P<b>.+)$` → `\\+`), `onset_clusters`, `rite`, and the position
  of each `garment` key. Handing that rebuilt file to
  `tools/gates/naming-collision-gate.py` produces **8 `DERIV-REPLAY` FAILs** —
  the rule's `\+` no longer matches the stem, because the rebuild escaped it a
  second time. The red is **manufactured by the gate's own reconstruction** and
  exists in no file on disk. (Round-24 cold-run C2 recorded the symptom; this
  seat measured the cause.)
- **L3 — a null-ish scalar read as present.** `routed_slots` collected
  `row.get("owed_slot")` behind a plain truthiness test, and the lane's reader
  keeps an unquoted `null` as the **string** `"null"` — truthy. Six D4 routing
  rows carry `owed_slot: null` (the register class), so the comparison saw six
  **phantom** owed slots and failed. `moved_field` already applied the null-ish
  rule to `off_channel_field`; the two halves of a routing row disagreed.

## 2. The fix as landed

`tools/gates/typed-pipeline-gate.py`, digest **`879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126`**
(predecessor `04ad4bb479562c419b48d750a8f9303c4a5a717ca7f2fe3b3658cc1bb9578a48`):

- **L3:** one null-ish predicate (`nullish`) now backs both `moved_field` and the
  new `owed_slot_of`; `routed_slots` reads slots through `owed_slot_of`, so a
  `null`/`~`/empty/absent slot can never enter the comparison. The same helper
  name is used by the sibling seat's control (see §6).
- **L2, input class — the graded legacy side is the source the typed packet
  declares**, under `typed_assembly.packet`, digest-checked against the typed
  packet's own `assembly.packet_sha256`. Precedence is explicit:
  1. source **named**, readable, digest matches → grade the source
     (`input_class = typed-declared-source`);
  2. source **named** but unreadable → **exit 2**, `L2-channel` detail
     *"typed-packet input without its source: … is not a gate input"*
     (`typed-unresolvable`);
  3. source **named** but the pin no longer matches its bytes → **exit 2**,
     *"stale against its own source"* (`typed-stale-source`);
  4. source **unnamed** → the rebuild stands in as before, plus a round-trip
     fidelity check; if the rebuild is unfaithful **and** L2 would fail, the run
     is **exit 2** naming the rebuild as the cause (`typed-unfaithful-rebuild`)
     rather than reporting a manufactured red.
- The chosen class is reported in `--json` as `input_class`, and `--json` carries
  the same value a reader needs to tell which direction was graded.

Rule 4 is what keeps the historical frozen generations green: the round-11 D2
typed snapshot (pinned by round-18/round-20) **names no source**, so the rebuild
path — and therefore its recorded verdict — is unchanged (§5).

## 3. Matrix (command + date, all 2026-10-18)

| Input class | Command | Exit | Legs |
|---|---|---|---|
| source (documented entry) | `… typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | **0** | **19/19** |
| typed, declared source | `… examples/culture-d4/packet.d4.typed.yml` | **0** | **16/16** |
| source | `… examples/culture-d2/packet.d2.yml` | **0** | 16/16 |
| typed, declared source | `… examples/culture-d2/packet.d2.typed.yml` | **0** | 13/13 |

- `DERIV-REPLAY` lines in the typed-D4 run: **0** (was 8).
- The typed-D2 run's stdout is **byte-identical** to the round-23 frozen row
  (`tools/gates/frozen/round-23/repin-d2/typed-pipeline.out`), i.e. the fix moved
  no legitimate verdict.
- Gate selftests: `--selftest` **19/19**, `--selftest-generalized` **14/14**.
- `python3 tools/check-gate-battery.py` → exit 0, duty 1 **7/7**, duty 2 19/19
  baselines, `originals.preserved: true` (32 files hashed before and after, 0
  modified).

## 4. Teeth (the gate did not lose its teeth)

Measured through `reports/round-25/run-validation.py --check` (isolated clone):

| Control | Exit | Note |
|---|---|---|
| truncated D4 packet (`gate-broken`) | **2** | refuses, no traceback |
| tampered `expected-holds.json` (`gate-tamper`) | **1** | the verdict moves |
| typed packet, declared source absent | **2** | named input-class diagnostic |
| typed packet, stale `packet_sha256` | **2** | named input-class diagnostic |

The first two are the round-25 validator's own controls; the last two are the new
frozen control rows (§5). Two additional controls run inside `--selftest`
(the null-ish truth table, and that a null-ish `owed_slot` never reaches the
routing comparison).

## 5. New frozen rows (append-only; no historical manifest touched)

`tools/gates/frozen/round-25/gate-input/` — **6 new rows**, every file new:

- four **input-class rows**: `packet.d4.yml` (exit 0, 12 findings),
  `packet.d4.typed.yml` (exit 0, 12), `packet.d2.yml` (exit 0, 15),
  `packet.d2.typed.yml` (exit 0, 15);
- two **fail-closed control rows** under `controls/`: a typed packet whose
  declared source is absent (exit **2**) and one whose `assembly.packet_sha256`
  no longer matches its declared source (exit **2**).

Replay (2026-10-18, `TMPDIR=/tmp`):
`python3 tools/replay-frozen.py tools/gates/frozen/round-25/gate-input/MANIFEST.tsv --json`
→ exit 0, **6/6 reproduced**, 0 mismatch, 0 could-not-evaluate.

**Cascade — new rows, not edits.** Moving the gate digest makes every earlier
generation that pinned the predecessor refuse its typed-pipeline row with
`gate_digest_mismatch`. Measured 2026-10-18 on the live tree:

| Manifest | Exit | Reproduced | Refused row |
|---|---|---|---|
| `round-18/repin-d2` | 2 | 10/11 | line 2, `…/round-11/typed-pipeline/packet.d2.typed.yml` |
| `round-20/repin-d2` | 2 | 10/11 | line 2, same snapshot |
| `round-22/d4-repin` | 2 | 2/3 | line 4, `examples/culture-d4/packet.d4.yml` |
| `round-23/repin-d2` | 2 | 10/11 | line 2, `examples/culture-d2/packet.d2.typed.yml` |

Exactly one refused row each; every other row still reproduces. **Restore recipe
proved in an isolated clone:** `git show f74fc94:tools/gates/typed-pipeline-gate.py`
reproduces the predecessor digest `04ad4bb4…` exactly, and with it restored
`round-22/d4-repin` returns to **3/3** and `round-23/repin-d2` to **11/11**; the
round-18/round-20 row 2 then refuses on `output_missing`
(`tools/gates/frozen/round-11/typed-pipeline/run.log` absent from the clone's
tracked tree) — the same pre-existing condition the round-23 regression notes as
historical. No historical manifest was edited; the successor generations are the
new round-25 rows.

## 6. Collision note (disclosure, not a claim)

A **sibling round-25 seat** (`reports/round-25/gate-input/design.md`,
`diagnosis.md`) wrote the same file concurrently. Their design states they did
**not** edit the real gate and kept their patch on a scratch copy; their landed
contribution was a selftest control block (an `owed_slot` truth table, a
phantom-slot control, and a declared-source-leg control) that calls the helper as
`owed_slot_of` while this seat had named it `owed_slot`, which crashed
`--selftest` with `KeyError: 'owed_slot_of'`. This seat **reconciled by adopting
their documented name** (`owed_slot_of`) and left their control block, design and
diagnosis files untouched — the merged gate is green at **19/19** selftest
controls. Their `design.md` §8 independently verifies the interim `ec65d655…`
revision against their own control set. The digest this seat froze
(`879d40bf…`) is the reconciled revision, so the pinned artifact is green.

## 7. Round-25 validator read (isolated clone, 2026-10-18)

`python3 reports/round-25/run-validation.py --check` in an isolated clone →
claim O **not yet PASS**, and the only claim-O failure is the sibling half:

- `gate_input_honesty` — **all checks pass**: source `exit 0, 19/19`,
  derived `exit 0, 16/16`, `deriv_replay_lines: 0`,
  `nullish_routing: false`, corrupted-packet control `exit 2`,
  tampered-expectation control `exit 1`.
- `v3_supersession` — fails on *"no superseding v3 row landed under
  reports/round-25"*: the successor row this validator looks for
  (`expected.json` + `packet.md` + `twin.json`) is the sibling seat's write, and
  at measurement time `reports/round-25/v3-supersession/` held
  `build-revision.py`, `v3-supersession-check.py`, `evidence.md` and
  `declared-in-r4/` but no `twin.json`. Claim D and claim C were also still open
  at that measurement.

## 8. Limits

- This file measures the **gate-input** half of claim O only. The v3-supersession
  half, claims D and C, and the parent's acceptance run are outside this seat's
  write and are not adjudicated here.
- The gate digest is pinned **as of this measurement**; if a sibling edits the
  file again the frozen rows refuse with `gate_digest_mismatch` until the rows are
  re-frozen — that refusal is the intended behavior, not a regression.
- The round-25 validator does not read the new frozen generation, so §5's replay
  result is this seat's own measurement, reproducible with the command quoted.
