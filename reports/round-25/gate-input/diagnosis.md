# Round 25 — O R25-O01..O03 — gate-input false-red diagnosis

- **Seat:** R25-O-gate-input, round 25. Claim O / operability, sub-claim
  "gate-input honesty" (`reports/round-25/claims.json`, before-clause (a)).
- **Date:** 2026-10-18 (all commands run 14:2x–14:3x local, `python3` 3.14.7).
- **Scope of this file:** reproduce the typed-packet-input false red *precisely*
  and locate every surface it travels through. The minimal-fix design is in the
  sibling `design.md`; the code repair is **not** applied by this seat. **Note:**
  a sibling round-25 seat (O08..O10) landed a stronger fix **and** the repin
  cascade while this file was being written (final gate sha `879d40bf…`);
  `design.md` §8 verifies that revision against this seat's whole control set.
  All reproduction commands below were run against the pre-fix bytes
  (`sha256` = `04ad4bb4…`, the `d4-repin` MANIFEST pin) and were re-confirmed
  against the settled revision.
- **Artifacts read, not written:** `tools/gates/typed-pipeline-gate.py`,
  `examples/culture-d4/packet.d4.{yml,typed.yml}`, `tools/assemble-d2.py`,
  `tools/d2-typed-labels.py`, `tools/gates/naming-collision-gate.py`,
  `tools/gates/typed-pipelines.json`. Scratch under `.scratch/r25-o1/`
  (`TMPDIR=$PWD/.scratch`), gitignored. No filed artifact of rounds 8–24 was
  modified; no git mutation.

## 1. Reproduction (exact, with the gate bytes pinned)

Gate bytes were unchanged since the round-22 freeze when these runs were made:
`sha256 tools/gates/typed-pipeline-gate.py` =
`04ad4bb479562c419b48d750a8f9303c4a5a717ca7f2fe3b3658cc1bb9578a48`, which is
the `d4-repin` MANIFEST pin (`tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv`
row 4). So this was a live defect on the pinned tool, not a drifted working copy.
(At 14:31–14:33 a sibling round-25 seat fixed the tool in the working tree — sha
now `879d40bf…`; the R2 red no longer reproduces there. `design.md` §8 verifies that
revision and records the manifest pins it left refused under the declared
cascade convention.)

| # | Command (2026-10-18) | Exit | Legs | Key legs |
|---|---|---|---|---|
| R1 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | **0** | 19/19 | all ok |
| R2 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | **1** | 14/16 | `FAIL L2-channel`, `FAIL L3-routing-consistency` |
| R3 | `python3 tools/gates/typed-pipeline-gate.py` (flagless, D2 default) | **0** | 16/16 | all ok |
| R4 | `python3 tools/gates/typed-pipeline-gate.py --selftest` | **0** | — | `12/12 checks passed` |

The claim's two named symptoms reproduce verbatim.

**L3 (R2, line 30 of the run):**

```
FAIL L3-routing-consistency — holds ['GAR-01' … 'LEX-GAR-06'] vs routed ['GAR-01' … 'LEX-GAR-06'];
owed slots ['LEX-GAR-01' … 'LEX-GAR-06'] vs routing ['LEX-GAR-01' … 'LEX-GAR-06', 'null', 'null', 'null', 'null', 'null', 'null']
```

The `holds`/`routed` halves **agree** (12 = 12). Only the `owed slots` half
fails: the observed side has 12 entries, the routing side 18 — six phantom
`'null'` strings.

**L2 (R2, line 22):** eight lines, all of the form

```
naming-collision-gate.py: non-artifact removal: FINDING DERIV-REPLAY: FAIL —
name NM-0x '<name>': rule 'CX-01' does not apply to stem '<a>+<b>'; the stated inputs and rules do not yield the candidate
```

for NM-01…NM-08. These are *manufactured by the gate's own internal comparison*,
not read from either packet.

## 2. Root cause A — `routed_slots` reads the reader's `'null'` string as a slot

`tools/gates/typed-pipeline-gate.py:748-749` (the area the assignment names):

```python
routed_slots = sorted(row.get("owed_slot") for row in routing
                      if moved_field(row) and row.get("owed_slot"))
```

`moved_field()` (`:186-194`) already carries exactly the null-ish guard this
line needs, and its docstring names the trap:

> A missing key or a null-ish value (`null`, `none`, `~`, empty — the lane's
> reader keeps an unquoted `null` as the string) means the row stays on channel

`routed_slots` does **not** apply it. It tests bare truthiness, and the lane's
reader (`tools/d2-typed-labels.py:356 load_packet_strict`) keeps an unquoted YAML
`null` as the four-character string `'null'` — which is truthy. Proof (14:2x):

```
$ python3 -c "…load_packet_strict('examples/culture-d4/packet.d4.typed.yml')…"
GAR-01 | off= 'garment_gloss' | owed= 'null' | hold= 'D2L-FORM-UNRESOLVED'      ← string 'null'
GAR-02 | off= 'garment_gloss' | owed= 'null' | hold= 'D2L-FORM-UNRESOLVED'
… GAR-03..GAR-06 identical …
LEX-GAR-01 | off= 'garment_gloss' | owed= 'LEX-GAR-01' | hold= 'D2L-FORM-UNRESOLVED'
… LEX-GAR-02..06 identical …
```

The committed typed packet carries **12** routing rows
(`examples/culture-d4/packet.d4.typed.yml:2681+`): six costume rows
`record: "GAR-0x"` with `owed_slot: null` (unquoted, lines 2691/2701/…), and six
slot rows `record: "LEX-GAR-0x"` with a real `owed_slot`. All twelve carry
`off_channel_field: "garment_gloss"`, so `moved_field()` is truthy for all
twelve. The six `'null'` strings therefore enter `routed_slots`, giving 12
observed slots against 6 held slots.

**This leg is a false red twice over:**

- The intended comparison is `hold_slots == routed_slots`, i.e. the six
  *labelled* slots. Both sides of the meaningful comparison are in fact
  consistent (6 = 6); the guard's missing filter manufactures the mismatch.
- `L3-routing-consistency` has **no `L2-retention`-style negative control** in
  the tool's own `--selftest` (12/12 covers the smuggle, dropped-row, laundered
  hold, adapter drift, malformed and missing cases — none of which is a
  `null`-valued `owed_slot`). So the null reading was never exercised.

## 3. Root cause B — the L2 legacy arm is a *rebuild of the product*, not the source

### 3.1 The design hole: the declared, digest-verified source packet is never read

The gate resolves and **digest-verifies** the pipeline's declared legacy packet
(`config["packet"]` = `examples/culture-d4/packet.d4.yml`,
sha `e7ecd2045ef0e5f9…`, matching both the `d4` profile pin in
`tools/gates/typed-pipelines.json` and `assembly.packet_sha256` inside the typed
packet). But in the typed-input direction that verification feeds only the
identity legs. `tools/gates/typed-pipeline-gate.py:588-608`:

```python
if typed_arg is not None:
    # reconstruct the legacy packet by moving the off-channel fields back
    rebuilt = copy.deepcopy(typed_doc)
    …
    legacy_bytes = ("\n".join(load_peer(SERIALIZER)["yaml_lines"](rebuilt)) + "\n").encode("utf-8")
else:
    legacy_bytes = Path(packet_path).read_bytes()      # ← packet_path IS the typed file here
```

In this direction `packet_path` *is* the typed file (`main():1338-1347` sets
`typed_arg = candidate`), so the `else` arm — the only one that reads a real
source packet — is unreachable. The L2 legacy arm is therefore a **lossy
re-serialization of the typed document through the D2 serializer**
(`tools/assemble-d2.py:72 yaml_lines`), the exact round-trip class the D4
adapter's own docstring warns about (`assemble-d4-typed.py:297-303`: "the
round-trip serializer corrupts regex backslashes, booleans and nulls"). Every
byte-level defect of that rebuild lands on the L2 comparison and is then
reported as a *finding about the packet*.

### 3.2 The rebuild's three defect classes (measured)

Reproduced by hand at 14:24 (`.scratch/r25-o1/rebuilt-legacy.yml`, sha
`182f07b9229a44a83ad837df347341be0cd6fcc631e374227fe1376dff1c165e`):

```
$ python3 …  # deepcopy typed_doc; apply the gate's own 588-598 loop; pop the 7 typed keys; yaml_lines
field moves: 6   rebuilt lines: 2343   committed lines: 2676
diff hunks: 14   differing lines: 359   positional differing lines: 103
key sequences equal: False (1874 vs 1785 keys; first divergence at "form_slot")
```

**(a) One over-escaped regex manufactures all eight `DERIV-REPLAY` lines.**
The single behavioural divergence between the rebuild and the committed source
is `morphology.derivation_rules` (source packet line 205), whose CX-01 pattern
is re-escaped on round-trip:

| file | line 209 | in-memory value |
|---|---|---|
| `examples/culture-d4/packet.d4.yml` | `pattern: "^(?P<a>.+)\\\\+(?P<b>.+)$"` | `^(?P<a>.+)\+(?P<b>.+)$` |
| `.scratch/r25-o1/rebuilt-legacy.yml` | `pattern: "^(?P<a>.+)\\\\\\\\+(?P<b>.+)$"` | `^(?P<a>.+)\\+…` ← one backslash too many |

The gate runs `naming-collision-gate.py` over that rebuilt file, whose gate C
(`naming-collision-gate.py:1483`) emits `DERIV-REPLAY` when the stated rule does
not apply to the stated stem. With the doubled escape the `\+` becomes a literal
backslash-plus class, `re.fullmatch` fails on `tum+hai`, and eight findings
appear — one per `CX-01` name.

Isolation (14:2x) — restore **only** that one line in the rebuilt file and the
class disappears entirely:

```
$ python3 tools/gates/naming-collision-gate.py .scratch/r25-o1/rebuilt-legacy.yml            → 8 × DERIV-REPLAY
$ python3 tools/gates/naming-collision-gate.py .scratch/r25-o1/rebuilt-pattern-fixed.yml    → 0 × DERIV-REPLAY
$ python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml            → 0 × DERIV-REPLAY
$ python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.typed.yml      → 0 × DERIV-REPLAY
```

So **neither committed packet** produces `DERIV-REPLAY`; only the gate's internal
rebuild does. The eight lines are an artifact of the comparison machinery being
graded as if it were evidence about the packet.

**(b) Structural loss: the rebuild drops a whole top-level block.**
Top-level key census: committed **34**, typed **39**, rebuild **33**.
`in committed, not rebuilt: ['assembly']` — the entire 336-line `assembly:`
block (pins, `unresolved`, `skipped_keys`, `normalizations`) is absent, because
the gate pops `assembly` (`:598`) along with the six typed-only keys. The
committed file is 2676 lines, the rebuild 2343; the final diff hunk
(`@@ -2341,336 +2341,3 @@`) is that block disappearing. The rebuild also
reorders keys within records (each costume's `garment:` moves from first to
after `notes:` — the first key divergence at index 1237).

**(c) Coercions: booleans and nulls become strings.**
`onset_clusters: false` → `"false"` (line 189); `rite: null` → `"null"` ×3
(lines 1289/1300/1311); `"the cold fire (reserved)": [null, null]` →
`["null", "null"]` (line 1910). These are the serializer's own round-trip
defects and are the same class as (a), just currently benign for the five gates'
verdicts.

### 3.3 Why the L2 leg did not *also* fire on the structural loss

`L2-channel`'s guard (`:646-651`) only rejects a `removed` line that is neither
`FINDING PHON-*` nor names a moved record:

```python
for line in removed:
    if not line.startswith("FINDING PHON-") or not any(record in line for record in moved_records):
        delta_ok = False
        delta_detail.append("%s: non-artifact removal: %s" % (gate, line))
```

It compares *gate verdict lines*, never bytes. The eight `DERIV-REPLAY` lines are
the only diff the five gates notice, and they are exactly the lines this guard
was written to reject. That is the round-24 reading ("an unfaithful `yaml_lines`
rebuild manufacturing DERIV-REPLAY findings") — confirmed here at the byte level
and narrowed to a single root line.

### 3.4 The routing-row / costume-record conflation (latent, same leg)

The same 588-598 loop shows a second, currently-masked defect:

```python
for row in routing:                     # 12 rows
    for entry in rebuilt.get("costumes") or []:
        if str(entry.get("id")) == row["record"]:   # only GAR-0x rows own a garment
            field = row.get("source_field") or "garment"
            moved = moved_field(row) or "%s_gloss" % field
            if moved in entry: entry[field] = entry.pop(moved)   # 6 actual moves
```

`moved_records` (`:572`) is built from **all** routing rows (`12`), while only
the **6** costume rows actually move a field. The gate patches around this with
the `generalized` branch at `:658-664` (`field_moved` intersected with
`costume_ids`), so `L2-channel`'s `removed_total == len(field_moved)` check
survives — but only because the *rebuild* is lossy enough to mask it, and only
on the D4 path. `routed_slots` and `routing_hold_ids` use the same 12-row set.

## 4. Controls — the honest red survives the fix (negative controls)

Every leg the fix touches must still fail closed on a real defect. All of these
were run against a **patched scratch copy** of the gate
(`.scratch/r25-o1/gate-patched.py`, sha
`0e3152c750113edeb4e63ce3979f486c968f13132469e6af2a3317c450fc5fae`; patch is
+41/−3 lines, 3 hunks — see `design.md` §3/§4) so that the real tool stays
untouched. Each input below is derived from the committed typed packet in
`.scratch/r25-o1/neg/`.

| # | Negative control | Unpatched | Patched | Reading |
|---|---|---|---|---|
| N1 | one routing row dropped (`GAR-06`) | exit 1 | **exit 1** — `FAIL L2-channel` (PHON-INVENTORY for the un-moved field) **and** `FAIL L3-routing-consistency` (holds 12 vs routed 11) | still fails closed; now with an accurate detail |
| N2 | `owed_slot: "LEX-GAR-99"` smuggled onto the `GAR-01` row | exit 1 | **exit 1** — `FAIL L3-routing-consistency`, `routed` gains `LEX-GAR-99` | a *real* slot on a row that holds nothing is still caught |
| N3 | `GAR-01` field never moved (`garment:` restored, routing still claims the move) | exit 1 | **exit 1** — `FAIL L2-channel`: "off-channel lines in the typed run: … GAR-01 …" | the field-move check still fires |
| N4 | `--legacy-packet examples/culture-d4/packet.d4.typed.yml` (self-referential arm) | exit 2 | **exit 2** — `FAIL L1-assembler`: bytes `ffece0fe…` ≠ the assembler's deterministic `e7ecd204…` | a wrong declared source is refused, not silently graded |

N1/N2/N3 each reproduce under the patched gate, and N2 shows the new `nullish()`
filter is not a blanket amnesty: `'null'`/`''`/`'none'`/`'~'` are dropped, any
other string is kept and still compared.

### 4.1 Controls that do *not* yet fail (named, not fixed — honesty about the guard's reach)

- **N5** — `hold: null` (unquoted) on a moved `LEX-GAR-0x` row: patched gate
  **exit 0, 16/16**. `routing_hold_ids` (`:741`) tests `row.get("hold")`
  truthiness, so the reader's `'null'` string is kept as a hold id; the resulting
  mismatch with the finding set is then invisible because the same string is
  used to select findings. Unpatched gate also reads 14/16 (its L2 failure is the
  DERIV-REPLAY noise, not this).
- **N6** — the `hold` key absent entirely on a moved `LEX-GAR-0x` row: patched
  gate **exit 0, 16/16**. The record's hold drops out of `routing_hold_ids`, so
  it also drops out of `hold_records`, and the equality with `moved_records`
  still holds.

Both are pre-existing gaps on the *source* path as well (the source-packet run
is 19/19 with the same code), i.e. they are not introduced by this diagnosis and
are not part of the R25-O fix. They are recorded here because the round's
"fails closed and honestly" clause should not be read as "the L3 leg is now
sound" — see `design.md` §5 (N1/N2 residual).

## 5. Verdict

- **Both symptoms are one-directional and reproducible on pinned bytes.**
- **Symptom 1 (`L3-routing-consistency`)**: `routed_slots` (`:748-749`) omits the
  null-ish filter `moved_field()` (`:186-194`) already has; the lane reader keeps
  `owed_slot: null` as `'null'`; six phantom slots. **False red — the leg's own
  comparison is consistent (6 = 6).**
- **Symptom 2 (`L2-channel`)**: in the typed-input direction the gate rebuilds
  its legacy arm from the typed document through the D2 serializer instead of
  reading the declared, digest-verified source packet. The rebuild drops the
  `assembly:` block, reorders keys, coerces booleans/nulls to strings, and
  double-escapes `CX-01`'s `pattern`, which alone produces all eight
  `DERIV-REPLAY` lines. **Manufactured finding — neither committed packet emits
  `DERIV-REPLAY`.**
- The round-24 mechanism reading is **confirmed and narrowed**: the "unfaithful
  `yaml_lines` rebuild" is one missing source read (`:608` vs `:588`) plus one
  over-escaped regex, not a diffuse corruption.

The minimal-fix design, its patch, the byte-identity regression evidence and the
pin cascade are in `reports/round-25/gate-input/design.md`.
