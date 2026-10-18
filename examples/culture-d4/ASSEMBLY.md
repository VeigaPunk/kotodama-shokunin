# D4 round-17 assembly and measured pipeline verdicts (NON-CANON)

Non-canon design drill. This directory is a **gate/pipeline artifact set, not an
accepted culture, not a world-bible entry, and not a lore handoff**. Everything
here is NON-CANON; canon standing is lore-shokunin's alone. No real-language
clearance, cultural permission, community consultation, rights/attribution
ruling, or ancient authenticity is claimed anywhere. Era tags E0–E3 are
fixture-relative, not BCE/CE.

## 1. Integration record

The 12 component fragments were authored by the round-17 component seats
(R17-D05…D16) under `reports/round-17/d4/components/` (registry: `01-brief.yml`
`registry:`) and copied into `components/` by the round-17 integrator (seat
R17-D20) on 2026-10-18, byte-for-byte (`cmp` per file, all 12 `same`). The
generated artifacts are build products:

```
components/*.yml  (12 inputs, landed from reports/round-17/d4/components/)
   │  tools/assemble-culture-d4.py            → packet.d4.yml
   │  tools/d4-typed-labels.py                → typed-labels.d4.yml     (not landed)
   │  tools/assemble-d4-typed.py              → packet.d4.typed.yml     (not landed)
   ▼
expected-holds.json  (the named hold set)                                 (not landed)
```

Never hand-edit a generated file; after any component edit, rebuild and re-run
`--check` plus the gates.

## 2. Reproduce

From the repository root:

```sh
python3 tools/assemble-culture-d4.py            # writes exactly packet.d4.yml
python3 tools/assemble-culture-d4.py --check    # read-only drift check
python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml
python3 tools/gates/phonology-sanity-gate.py examples/culture-d4/packet.d4.yml
python3 tools/gates/costume-era-consistency-gate.py examples/culture-d4/packet.d4.yml
python3 tools/gates/lexicon-coverage-audit.py examples/culture-d4/packet.d4.yml
python3 tools/gates/myth-consistency-gate.py examples/culture-d4/packet.d4.yml
```

## 3. Measured runs (2026-10-18, lane root, `TMPDIR=$PWD/.scratch`)

| command | exit | observed |
|---|---:|---|
| `python3 tools/assemble-culture-d4.py` | 0 | `Wrote examples/culture-d4/packet.d4.yml (82635 bytes)` |
| `python3 tools/assemble-culture-d4.py --check` | 0 | `packet.d4.yml: byte-identical deterministic assembly` |
| `python3 tools/assemble-culture-d4.py --selftest` | 0 | `selftest: 81/81 checks passed` (positive, tamper, malformed, missing, collision, duplicate-id, wrong-type, too-few-files controls) |
| `naming-collision-gate.py packet.d4.yml` | 1 | 8 findings: `PHON-INVENTORY` FAIL ×6 (the six `GAR-0n` glosses — the class the typed routing removes), `NAME-NEAR` REVIEW ×1, `CROSS-HOLD` HOLD ×1 (no real-language sweep performed; no clearance claimed) |
| `phonology-sanity-gate.py packet.d4.yml` | 1 | 1 finding: `A-CLASS` REVIEW (a natural-class allophony rule needs finite expansion) |
| `costume-era-consistency-gate.py packet.d4.yml` | 0 | 0 findings |
| `lexicon-coverage-audit.py packet.d4.yml` | 0 | 0 findings |
| `myth-consistency-gate.py packet.d4.yml` | 0 | 0 findings |

All five gates exit in {0,1}: no exit 2, no traceback.

## 4. The named hold set

`components/01-brief.yml` `contract.hold_set_declaration` names the finding set
the typed run is expected to emit, before the packet existed: **6 holds,
0 notes, 0 fails** — `D4L-FORM-UNRESOLVED` at `GAR-01`…`GAR-06`, one per
`LEX-GAR-0n` form slot left owed (the six garment glosses are translated
labels, routed off the sound-and-identity channel). The legacy run above shows
exactly those six glosses as the six `PHON-INVENTORY` lines the typed routing
replaces; the holds are open design debt, never a clearance.

**Pending:** `typed-labels.d4.yml`, `packet.d4.typed.yml`, and
`expected-holds.json` require the D4 typed tools (`tools/d4-typed-labels.py`,
`tools/assemble-d4-typed.py`), which had not landed when this record was
written. `tools/d2-typed-labels.py` is not a substitute: run over this packet
it exits 2 with `packet.eras: expected a non-empty list of era tags` (D4's
`eras` is a record list; D2's is a tag list) — the same culture-boundness the
round-17 typed-support fragments measured.

Measured against the round-17 counting runner's own D leg (read-only harness
over `reports/round-17/run-validation.py`; no receipt written), the tree passes
every leg that does not need those artifacts — discovery (packet + brief +
12 components), assembler determinism, gate interop, d2/d3 preservation,
NON-CANON, and the pre-declared-hold scan — and leaves exactly four gaps:
`packet.d4.typed.yml`, `typed-labels.d4.yml`, `expected-holds.json`, and a
round-17 frozen manifest for the replay leg. The first two need the D4 typed
tools (outside this tree); the third follows from them; the fourth is a
frozen-record artifact for the test seats.

## 5. Pins (sha256, measured from the delivered bytes)

| path | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` | `2776d85cb2b3f03bf084df3974b3ff59c44b81b0004997c4e4bd830b05335d72` |
| `tools/assemble-culture-d4.py` | `03a0754eec5565aad76598be53de4ba26e0199c81a30814ec88e87e31951f466` |
| `components/01-brief.yml` | `a2bc3111b8e936d2aa78feca86b871996455cc98d7d639f3825a88df8a1c056f` |
| `components/02-phonology.yml` | `7aa9cac5c030dfb39fbe5a90d04ea5d94f130f7a7e28b5bbb17ff2773ab0a42a` |
| `components/03-orthography.yml` | `de1820b0c115271f7f86fbad8f7e6d637a6155cb61ad9a92cd53e32fdc08783e` |
| `components/04-lexicon.yml` | `74c2561b7c875c7c98708c589002b85b7989fc64bafa6abf794210401c69a9a5` |
| `components/05-naming.yml` | `b154d80700c47719dcf8395f6017f68c00c21a5eea79965d205df4bdbb688e0c` |
| `components/06-myth.yml` | `2ca4935d8dc33899a98ebfe2212f73ca5efadee56e7720b59a592416fd3a6b9d` |
| `components/07-symbolism.yml` | `5da857dc832c69b71fe1ac51f80232b63527e8e953abe6d93e26836c28c1c80c` |
| `components/08-eras.yml` | `1c9202e3730530a5e82dc57b3e1622b13f94cfd27c4581d90a0b95d8c11f50a0` |
| `components/09-costumes.yml` | `82fb92ad17848fff8fe40421e6f15858ca79b9e6c90ba9e60e262b4cb48b8c8f` |
| `components/10-ritual-calendar.yml` | `5a8d41b4bc58997a8181c8f5ae8f2c279b48c92b76f6728deec23713a1ab85a2` |
| `components/11-contact-history.yml` | `7b6932aff32871c587834ad7d42a237836b01e4188eee118b7203c6ddfddaa9c` |
| `components/12-provenance.yml` | `540f7d2258f3a4000f1aa670742b88b440d2ce107ace49d4246f00c7726d8d69` |

The packet's own `assembly.source_sha256` block pins the same twelve component
digests; a mismatch is drift, never a silent edit.

## 6. Constraints and reported divergences

- NON-CANON everywhere; no clearance, permission, or acceptance claim may be
  written into any file here. The naming gate's `CROSS-HOLD` line stays
  visible: no real-language sweep was performed and none is claimed.
- The typed packet's `pipeline_findings` must be carried verbatim from the
  projector; a hold is never laundered into a note, renamed, or deleted.
- Round 17 carried **mutually divergent D4 design documents** beside the
  landed component registry: `reports/round-17/d4/design-brief.md` (weigh-court
  quote register, COUNT × QUOTE, an 18-hold set), `design-costume.md` (tide-work
  wardrobe, its own hold set), `design-myth-era.md` (salt-pan wells), and
  `design-language.md`. This tree contains the **landed components** — the
  furnace-league registry `01-brief.yml` (FIRE × MARK) and its six-hold
  declaration. The divergence is reported, not repaired here.
- `expected-holds.json`, when landed, omits `projector_sha256`: the round-17
  counting runner pins that key to `tools/d2-typed-labels.py`, so a D4
  projector pin would fail the runner's own pin leg.
