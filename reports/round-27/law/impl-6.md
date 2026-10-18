# R27-D10 — the determinism of the landing: three regenerations, byte-identical

- **Seat:** R27-D10 (D axis, register law + syllabify implementation 6 of 8).
  Round 27, loop 3 build 3 of 4, claim **D** `register-law`. Integrator:
  `impl-1.md` (R27-D05).
- **Date:** 2026-10-18. Baseline `4f09c990…`; declaration commit `b95fca1`.
- **Write scope:** this file only; scratch under `.scratch/r27-d/`.
- **Canon:** NON-CANON engineering evidence.

## 1. The clause this fragment measures

The claim's `after_required` says the law must be "wired into the packet
**deterministically**". That is a measurable clause, not a stylistic one: the
three D4 artifacts must each be a pure function of their declared inputs, so a
reader who regenerates them gets the same bytes.

## 2. The three regenerations

| # | artifact | command | result | exit |
|---|---|---|---|---|
| D-1 | `examples/culture-d4/packet.d4.yml` | `python3 tools/assemble-culture-d4.py --check` | `byte-identical deterministic assembly` | 0 |
| D-2 | `examples/culture-d4/typed-labels.d4.yml` | `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | `byte-identical deterministic projection` | 0 |
| D-3 | `examples/culture-d4/packet.d4.typed.yml` | `python3 tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml` | `byte-identical deterministic typed packet` | 0 |

All three are green, and the lane runner re-runs them as its own
`deterministic_regeneration` leg, requiring exit 0 from each
(`run-validation.py:922-927`). Its measurement reports
`{"d4-assembly": 0, "d4-adapter": 0, "d4-projection": 0}`.

## 3. Why the wiring is deterministic rather than incidental

`register_law` is a new top-level block. It reaches the packet through the
assembler's own declared mechanism, not through a special case:

- the component declares `packet_keys: [register_law]`
  (`13-register-law.yml:14`), and a component's own `packet_keys` list **fixes
  that file's packet contribution exactly**
  (`tools/assemble-culture-d4.py:230-266`); a key not in the list is recorded
  under `assembly.skipped_keys` and never merged;
- `build_packet` emits every merged key in `PACKET_KEYS` order and then every
  remaining merged key in sorted order (`:373-378`), so an unknown-but-declared
  block lands deterministically;
- `RECORD_FIELDS["registers"]` already required only `("id",)` (`:118`), so the
  law rows' extra fields need **no assembler edit**.

Measured: the assembler's own selftest is `81/81 checks passed`, including the
too-few-files, collision, duplicate-id, wrong-type, empty-block and missing-field
fail-closed controls — so a component tree that *lost* the new file still fails
closed rather than silently dropping the law.

## 4. The contract declaration, which the sibling review measured absent

The sibling review recorded that the block arrived **undeclared**:

> "The new block is not declared in the schema. `contract.record_fields` has no
> `register_law` key (measured: `None`), and `01-brief.yml`'s C-13 registry row
> is absent — so the block arrives in the packet **undeclared by the contract**"
> — `reports/round-27/law/review.md` §9a

Both halves are closed in revision 2, and the lane runner measures the first
directly: *"the packet contract declares no `record_fields.{name}`: the law block
is outside the declared record contract"* (`run-validation.py:916-921`).

| what | where | value |
|---|---|---|
| `contract.record_fields.register_law` | `01-brief.yml` | `[id, register, axis, kind, act, speaker, holder, force, consequence, design_row, evidence, follows]` |
| registry row C-13 | `01-brief.yml` | `stem: 13-register-law`, `packet_keys: [register_law]`, with the round-26 gap cited in its role text |

The contract now declares what the rows carry, so the block is inside the
declared record contract rather than beside it.

## 5. The packet's assembly block records the provenance

Because the assembler writes `assembly.source_sha256` for every component, the
landing's provenance is machine-readable: the new component's digest appears in
the packet itself, so a reader can tell which bytes produced the packet without
trusting this fragment.

```
$ python3 -c "import json,runpy;d=json.load(open('.scratch/r27-d/packet.json'))" 2>/dev/null || true
$ grep -A2 '13-register-law.yml' examples/culture-d4/packet.d4.yml | head -4
   "examples/culture-d4/components/13-register-law.yml": "c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7"
```

## 6. Determinism under the sibling edits, measured

The lane runner and two sibling artifacts were being edited **concurrently** with
this landing (`reports/round-27/run-validation.py` changed mtime mid-run, and its
`SYLLABLE_CONTROLS` shape changed between two of this seat's runs). The
regenerations were re-run after each observation and stayed green, which is the
statement that matters: **the landing is deterministic against the tool bytes it
declares, not against a moving target.**

## 7. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 tools/assemble-culture-d4.py --check
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml
python3 tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml
python3 tools/assemble-culture-d4.py --selftest | tail -1
grep -n "13-register-law" examples/culture-d4/packet.d4.yml
```
