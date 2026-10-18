# R17-D17 — the typed-label run over the integrated D4 tree

- round: 17 (operator loop 2 of 3, build round 1 of 4; 64 declared workers,
  `reports/round-17/claims.json`) · shard: **D17** (typed-label lead; sole writer
  of `examples/culture-d4/typed-labels.d4.yml`), claim **D
  `culture-d4-assembly`**.
- assignment (verbatim): "D4 R17-D17 (typed-label lead, ONLY writer of
  examples/culture-d4/typed-labels.d4.yml): run tools/d2-typed-labels.py over
  the integrated D4 tree (poll for components, max 20 min); hold set named;
  reports/round-17/d4/typed-run.md."
- date: 2026-10-18. Stamps UTC. Reference revision
  `9b49a4a0fca6ceeab917d401945358fdedeb7e11` (round-17 declare); baseline
  `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` (round-16 admit).
- canon: NON-CANON engineering evidence. Nothing here is a canon record, a lore
  handoff, a clearance, or a rights/attribution ruling.
- writes: **this file only** plus gitignored scratch under `.scratch/r17d17/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No
  tool, packet, component, projection, baseline or earlier-round byte is edited
  by this seat. No commit, no push.

## 0. Verdict

**The run was performed over the delivered D4 packet and the projector refused
it with a stable exit-2 diagnostic; no projection was emitted and
`examples/culture-d4/typed-labels.d4.yml` was not written.**

```
$ python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json
d2-typed-labels error: packet.eras: expected a non-empty list of era tags
exit=2
```

Packet `examples/culture-d4/packet.d4.yml` sha256
`2776d85cb2b3f03bf084df3974b3ff59c44b81b0004997c4e4bd830b05335d72` (82635
bytes; 09:42Z build read 09:45:08Z at `39c2d56a…c565038`, revised 09:49Z, stable
through 09:54:48Z; `python3 tools/assemble-culture-d4.py --check` → exit 0
"byte-identical deterministic assembly" on both revisions, so the delivered
packet is the assembler's own build). Projector `tools/d2-typed-labels.py`
sha256 `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`.

The refusal survives the 09:49Z packet revision: the blocker is a **packet-shape
deviation**, measured in §4 — D4's `eras` block carries records
(`{id, name, tag, label, span, …}`) where the projector requires the D2 shape, a
list of era tags. The first revision did fix the second deviation this seat had
measured (costume material references by id → by name, §5): the
scratch-normalized diagnostic's reconciliation leg is now clean. The label leg
runs clean over the delivered bytes (74 labels, 12 holds, 0 fails).

## 1. Dependency record

Poll 1 (60 s × 20, 09:16:01Z → 09:35:02Z): `examples/culture-d4` never existed
(20/20 polls `d4-dir=no`, `components=0`, `packet=no`). What landed inside the
window: the seven round-17 D4 docs (`design-brief`, `design-costume`,
`design-language`, `design-myth-era`, `typed-support-1/2`,
`expected-holds.fragment.json`), `tools/assemble-culture-d4.py` (09:33Z), and the
first components staged under `reports/round-17/d4/components/`.

Poll 2 (60 s cadence, 09:33:55Z → 09:43:55Z) watched the tree materialize: 4
staged components (09:33:55Z) → 5 (09:35:55Z) → 6 (09:39:55Z) → 9 (09:40:55Z) →
11 (09:41:55Z) → **12 (09:42:55Z)**, and at the next poll (09:43:55Z)
`examples/culture-d4/` existed with `brief.md`, `components/` (12 files) and
`packet.d4.yml`; `README.md` followed at 09:44Z. The run below was executed
immediately (09:43:48Z–09:45:08Z).

## 2. Inputs and digests

| path | sha256 | note |
|---|---|---|
| `examples/culture-d4/packet.d4.yml` | `2776d85c…335d72` | 82635 bytes (09:49Z revision), 12 components merged; assembler `--check` exit 0; first revision `39c2d56a…c565038` (80509 bytes, 09:42Z) also checked |
| `tools/d2-typed-labels.py` | `0da0015f…fb89c802` | the pinned projector (unchanged since the round-11 freeze) |
| `examples/culture-d4/components/08-eras.yml` | (staged bytes) | declares `eras:` as records, `packet_keys: [eras, named_eras, era_dates, source_era_dates, era_records]` |
| `examples/culture-d4/components/09-costumes.yml` | (staged bytes) | at the 09:42Z revision costumes referenced `material: CMAT-0x` (ids); the 09:49Z revision carries `material: "local hide"` (names, matching the `CMAT-0x` records' `material` field) |
| `examples/culture-d2/components/09-eras-calendar.yml:88` | — | the D2 analogue: `eras: ["E0", "E1", "E2", "E3"]` (tags), records under `named_eras` |

## 3. The run (commands and observed exits)

```sh
export TMPDIR=$PWD/.scratch
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml \
    --emit examples/culture-d4/typed-labels.d4.yml      # exit 2, nothing written
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json  # exit 2
python3 tools/d2-typed-labels.py --check examples/culture-d4/typed-labels.d4.yml    # exit 1 (no such file)
python3 tools/assemble-culture-d4.py --check            # exit 0, byte-identical assembly
```

The exit-2 message is the projector's own stable contract for could-not-evaluate
(`--json` prints nothing; the diagnostic goes to stderr, no traceback). The
`--emit` leg therefore has no projection to write, and the determinism leg
(twice byte-identical) has no bytes to compare: **the typed-labels step of claim
D is blocked at this packet revision.**

Controls re-run this round (2026-10-18), for the projector's health independent
of D4: `--selftest` → 39/39; `--check examples/culture-d2/typed-labels.d2.yml`
→ exit 0 byte-identical; `tools/gates/typed-pipeline-gate.py --selftest` → 12/12.

## 4. Blocker 1 — the `eras` block shape (the refusal)

- Delivered packet (`packet.d4.yml:1715-1718`): `eras:` is a list of mappings —
  `- {id: "E0", name: "E0", tag: "E0", label: "the stamp era", span: "before T1
  to T18", …}`. Element types measured: `{'dict'}`.
- D2's packet, the projector's contract (`examples/culture-d2/packet.d2.yml`):
  `eras` element types `{'str'}` (`["E0", "E1", "E2", "E3"]`), records under
  `named_eras`.
- Projector: `era_scope_from_packet` (`tools/d2-typed-labels.py:1581-1586`)
  requires "a non-empty list of era tags" → the stable refusal above.
- The component that supplies the block is `08-eras.yml` (`eras:` at its line
  27, records in flow mapping), whose `packet_keys` list is otherwise D2-shaped.

Two ways to clear it, both owned by other seats: the packet emits `eras` as tags
(the component/assembler change), or the D4 projector named in
`design-brief.md` §9.1 (`tools/d4-typed-labels.py`) is written to accept the
record shape. This seat does not absorb either.

## 5. The diagnostic (scratch only)

With the `eras` block normalized **in memory** to tags (scratch diagnostics
`.scratch/r17d17/diagnostic.txt` for the 09:42Z revision,
`.scratch/r17d17/diagnostic2.txt` for the 09:49Z one; no file written, no
delivered byte touched), the projector's two packet-driven legs were run over
the delivered packet:

**Label leg — `parse_typed_labels` over the delivered bytes (no normalization
needed, both revisions): 74 labels, `{fail: 0, hold: 12}`, kinds
`{native-form: 56, translated-label: 12, borrowed-strata: 6}`.**

| hold | where | detail |
|---|---|---|
| `D2L-FORM-UNRESOLVED` ×6 | `GAR-01..GAR-06` | `label_id LEX-GAR-0x has no supplied native/borrowed form` |
| `D2L-FORM-UNRESOLVED` ×6 | `LEX-GAR-01..LEX-GAR-06` | same, from the packet's own `form_slots` block — a top-level block D2's packet does not carry |

**Reconciliation leg (eras normalized): 6 holds at the 09:42Z revision, all
`R-MAT-UNRESOLVED-REF` @ `GAR-01..GAR-06`** — `material_ref 'CMAT-0x' resolves in
no declared scope`: the costumes referenced materials by **id** while
`claims_from_packet` reads the field as a name and matches it against the
inventory's `material` names (`"local hide"`, …). **The 09:49Z revision fixed
this** (costume `material:` now carries the name): the reconciliation leg over
the revised packet reports 0 non-ok findings.

**Rank leg (D2 constants, informational):** the engine emits D2's four rows
(`WR-02#g|WR-09#g`, `WR-08#g|WR-09#g`, `TR-04#a|TR-06#a` holds; `SR-01#a|SR-01#b`
note) for any packet — the mis-binding measured in §6.

So even with blocker 1 cleared, the revised delivered packet yields a finding
set of `12 label holds + 4 D2 rank rows` with `D2L-*` ids, whereas the frozen
pre-implementation naming (`reports/round-17/d4/expected-holds.fragment.json`,
17 holds + 1 note + 0 fails, amendment A-19-1) names `GD-01..06`,
`AL-01#plain..AL-06#plain`, `AL-03`, `RG-02`, `RG-05/06/07/08/09`, `SM-03`.
**None of the frozen `where` ids appears in the delivered packet's projection**,
and the frozen `D4L-REGISTER-UNRESOLVED` class has no engine path at all (§6).

## 6. Frozen rows vs the pinned projector: the capability gap

| frozen row(s) | can `tools/d2-typed-labels.py` emit it? | needed |
|---|---|---|
| 6× `D4L-FORM-UNRESOLVED` @ `GD-01..06` | only as `translated-label` records whose `label_id` matches `LEX-GAR-[0-9]{2}`; the delivered packet's owed slots are `LEX-GAR-0x` (measured: 12 holds, §5) | a projection whose `where` ids are the frozen ones, or a re-named frozen set |
| 6× `D4L-REGISTER-UNRESOLVED` @ `AL-01#plain..06#plain` | **no** — `grep -c REGISTER tools/d2-typed-labels.py` → 0 | the register class (quote supply + plain doublet owed) |
| 1× `D4L-BORROW` @ `AL-03` | **no** — the borrow hold branch fires on an unset **immediate** donor; a null `ultimate` emits no hold (probe, 2026-10-18) | D4's borrow hold branch |
| 1× `D4L-ERA` @ `RG-02` | not as named (no register-emergence concept) | register-emergence clock, prose-span → `partial` |
| 2× `D4L-RANK` + note @ `RG-0x` | **no** — the rank leg is D2's constant block (`build_payload()` `:1235`), measured above | D4 rank adapter over register-law rules |
| 1× `D4L-MATERIAL` @ `SM-03` | reconciliation emits `R-MAT-UNRESOLVED-REF` for costume claims (measured, §5), not `D4L-MATERIAL` @ `SM-03` | the sealed-measure claim path and the class mapping |

Additional projector bindings measured this round on scratch probes: a costume
whose `form_slot` carries a non-`LEX-GAR` prefix crashes with a raw
`AttributeError` (`:449`, `:498`) instead of a stable exit-2 code; the era-alias
leg reads D2's components (`:2319`, `:2369`).

The fragment's `pins_note` records that the round validator compares
`projector_sha256` against `tools/d2-typed-labels.py` (`typed-support-1.md`
F-D18-7) — the counting contract treats this projector as the D4 projector, and
this run measures what that decision costs: a stable exit-2 refusal on the
delivered packet plus a frozen naming the engine cannot reproduce.

## 7. What the parent must route

1. **Blocker 1 (blocking):** `eras` as tags in the packet (component 08 /
   assembler change) **or** the D4 projector (`design-brief.md` §9.1) accepting
   the record shape. Until then the typed-labels step cannot produce a
   projection and claim D's "typed labels → assembled packet → gate" chain stops
   here.
2. **Blocker 2 — cleared by the 09:49Z packet revision:** costume material
   references by id vs the projector's name-matching (the 6
   `R-MAT-UNRESOLVED-REF` holds of the 09:42Z revision are gone; §5).
3. **Naming divergence:** the frozen 17-hold naming (`GD-*/AL-*/RG-*/SM-03`,
   `D4L-REGISTER-UNRESOLVED`) vs the delivered components (GAR/LEX-GAR ids,
   `CMAT` materials, `E0-E3` records) — the frozen set and the delivered packet
   describe different record sets; the integrator decides which is authoritative
   before the equality leg can mean anything.
4. **Design-doc divergence** (already reported by the sibling seats): the four
   D4 design docs name four different cultures and three different hold-set
   slices; the staged components follow a fifth (furnace/craft).

The staged run for the re-run once a blocker is cleared is in §8; it needs no
new code.

## 8. The staged run (one minute after a packet fix)

```sh
export TMPDIR=$PWD/.scratch
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml \
    --emit examples/culture-d4/typed-labels.d4.yml
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml \
    --emit .scratch/r17d17/emit2.yml && cmp examples/culture-d4/typed-labels.d4.yml .scratch/r17d17/emit2.yml
python3 tools/d2-typed-labels.py --check examples/culture-d4/typed-labels.d4.yml
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json > .scratch/r17d17/run.json
python3 .scratch/r17d17/compare-holds.py .scratch/r17d17/run.json .scratch/r17d17/named-hold-set.fragment.json
```

Harness built by this seat (gitignored scratch): `run-d4-typed.sh`,
`lint-packet.py`, `compare-holds.py`, `named-hold-set.fragment.json` (the freeze
record's set), `diagnostic.txt` (§5).

## 9. Limits

- This file reports a **refused** run, not a projection: no
  `examples/culture-d4/typed-labels.d4.yml` exists; nothing here claims the
  projection exists, matches the frozen set, or is deterministic.
- The snapshot is the packet at sha256 `2776d85c…335d72` (09:49Z revision, read
  through 09:58:30Z; the 09:42Z revision `39c2d56a…c565038` was the first read);
  a later packet revision supersedes this run and needs a re-run (§8).
- The §5 diagnostic is scratch, in-memory, and non-deliverable: it normalizes
  one field to isolate one blocker and must not be read as the D4 typed run.
- NON-CANON throughout; canon status, lore acceptance and any real-world claim
  are out of province (`PROVINCE.md`).
