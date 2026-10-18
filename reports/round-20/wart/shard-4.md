# R20-O08 — shard 4/6: the re-pin cascade, as NEW rows only

- round 20, seat **R20-O05..O10**, claim **O**. Fragment 4 of 6.
- date 2026-10-18, readings stamped `2026-10-18T13:06–13:12Z`. Lane root
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- canon: NON-CANON. A pin is integrity, not truth; reproduction is not clearance.
- writes: the cascade files below and this fragment. **No filed artifact of
  rounds 8–19 is edited** — the round's own preservation duty reads 897 filed
  files against the declared baseline revision with 0 failures, and `r19-pre`,
  the round-18 frozen receipts and the round-16/18 v2-07 baselines are all left
  as filed.

## 1. The cascade at a glance

| # | surface | before | after | movement | where |
|---|---|---|---|---|---|
| 1 | `tools/d2-typed-labels.py` | `0da0015f…` | `76536a92…` | changed (the round-20 impl) | live |
| 2 | `examples/culture-d4/typed-labels.d4.yml` | `a59990bb…` | `cbcf997f…` | changed (the alias leg) | live |
| 3 | `tools/assemble-d4-typed.py` | `1ddad6a7…` | `92f5460b…` | changed: mirror drops the foreign tree; `--emit` writes the three input pins | live |
| 4 | `examples/culture-d4/packet.d4.typed.yml` | `f63ed531…` | `e823db67…` | **+3 lines**: the three pins in the carried `assembly` block | live |
| 5 | `examples/culture-d4/expected-holds.json` | `09490a27…` | `18d0cfce…` | internal projector/projection pins moved; hold set untouched | live |
| 6 | `tools/gates/typed-pipelines.json` (profile `d4`) | projection `a59990bb…`, adapter `null`, expected `09490a27…` | projection `cbcf997f…`, adapter `92f5460b…`, expected `18d0cfce…` | **re-pinned** (the run refused exit 2 / L1-profile until it was) | live pin channel |
| 7 | `tools/gates/expected/d4-typed-labels-check-gate/r20-post/` | — | new baseline dir, **4** inputs (was 6) | new row | new dir |
| 8 | `reports/round-20/wart/expected-v2-07-r20.json` | r18 row `ee9f6277…` digest | new row `44b3c299…`, 28 inputs, **1** moved | new row | new file |
| 9 | `examples/culture-d2/*` (projection, expected-holds) | `a3aa452c…`, `a5dc26d5…` | identical | **none** | live, bytes preserved |

Rows 3–5 are the part of the cascade the round's counting command found and
this seat then closed (it was failing claim O on exactly those three rows before
they landed: `adapter selftest still copies the foreign examples/culture-d2
tree`, `stale pin: examples/culture-d4/expected-holds.json projector_sha256 …`,
and three `stale pin: …packet.d4.typed.yml … None != live` rows).

## 2. Row 7 — the new baseline (`r20-post`), and why it is new rather than edited

The r19-pre baseline declared six inputs, two of them D2 components. The input
edit (shard 1) means a new baseline id, per the standard's §3 quoted inside both
files: "a gate revision, an input edit, or a new phase produces another NEW
baseline id".

| row | r19-pre (filed, untouched) | r20-post (new) |
|---|---|---|
| `inputs` | 6: peer `0da0015f…`, D4 packet `e7ecd204…`, reader `e6bffd70…`, **`examples/culture-d2/components/12-rank-rules.yml` `28696a5a…`**, **`11-costumes.yml` `b6e2c5c2…`**, projection `a59990bb…` | 4: peer `76536a92…`, D4 packet `e7ecd204…`, reader `e6bffd70…`, projection `cbcf997f…` |
| graded run | exit 0, stdout `3aa55393…` | exit 0, stdout `0d92cb4f…` (three reruns identical) |
| copies == live | 6/6 | 4/4 (`cmp` clean, measured) |
| `supersedes` | `none (first baseline)` | `r19-pre (input edit: the peer and the projection moved)` |

Battery reading of both rows, `python3 tools/check-gate-battery.py` at 13:12Z:
`baselines_found 18` (was 17), `pinned 18`, `unevaluable 0`, `coverage 9/9`,
`battery_exit 0`, `originals preserved true`. The r19-pre row still reads
`pinned`: its committed copies are its own snapshot, so the peer's move does not
touch it — it now describes a superseded revision, which is what a filed row is
for.

## 3. Row 8 — the v2-07 re-pin (the "round-18 repin rows, v2-07 pins" of the assignment)

Command (2026-10-18, lane root):

```
python3 reports/round-15/handoff/frozen-verify.py --freeze \
  --baseline reports/round-20/wart/expected-v2-07-r20.json
```

Observed: `froze reports/round-20/wart/expected-v2-07-r20.json`; `packet md
24f9dd39bdad… yml 39cf4d53b02a… gate exit 0 fields=16/16 glossary=20
findings=0`; `inputs: 28 pinned; manifest rows 26; census {'supported': 8,
'unresolved': 2, 'partial': 5}; links 50/50`; exit 0.

Verify against the new row: `python3 reports/round-15/handoff/frozen-verify.py
--baseline reports/round-20/wart/expected-v2-07-r20.json` → exit 0,
`frozen-v2: exit=0 fields=16/16 glossary=20/20 findings=0 claims=15/15 …
links=50/50`.

Diff against the filed r18 row (`reports/round-18/repin/expected-v2-07-r18.json`):
of 28 inputs exactly **one** moved — `tools/d2-typed-labels.py` `0da0015f…` →
`76536a92…`. The other top-level movements are the freeze metadata
(`baseline_digest`, `frozen_by`, `revision_note`, `supersedes`) and
`links.findings` 1 → 2, whose attribution is in shard 6 §2 — it is not a second
input movement.

## 4. Row 4 — why the typed packet now carries pins

The D2 typed packet pins its three inputs in its `assembly` block
(`examples/culture-d2/packet.d2.typed.yml:3319-3322`:
`packet_sha256`/`projection_sha256`/`adapter_sha256`). The D4 adapter built the
same three pins in memory (`doc["assembly"]`, which is what the D4 gate's
`L4-pins` leg reads) but its `--emit` never wrote them, so the filed artifact
pinned nothing. The emit now writes them into the carried `assembly:` block, in
the D2 shape, keeping the source packet's assembler-identity lines
(`generator`, `assembler_sha256`, `reader`, `source_sha256`, `skipped_keys`)
below them.

Controls: `python3 tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml`
→ exit 0; the three written values equal the live bytes
(`packet_sha256 e7ecd204…`, `projection_sha256 cbcf997f…`, `adapter_sha256
92f5460b…`); the adapter selftest's stale-projection control still fires
(`stale projection: exit 2 and the pin is named`).

## 5. Row 5 — the expected-holds re-pin, kept surgical

`git diff examples/culture-d4/expected-holds.json` is exactly: the two pin values,
a `revision_note`, and a `supersedes_pins` block naming the old values. The
`counts`, `holds` and `notes` bytes are unchanged (`fail 0 / hold 15 / note 1`),
which is why the D4 gate's `L3-holds` / `L3-details` / `L3-baseline-set` legs and
the battery's `expected` pin stay green.

## 6. Controls

| control | command (2026-10-18) | observed |
|---|---|---|
| the pin file is valid JSON and carries one profile | `python3 -c "import json;json.load(open('tools/gates/typed-pipelines.json'))"` | valid |
| the D4 legs accept the re-pin | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | exit 0, `19/19 legs passed` |
| the new baseline is pinned, not merely present | `python3 tools/check-gate-battery.py` | `pinned 18`, `unevaluable 0`, exit 0 |
| the D2 projection did not move | `cmp` of a fresh `--emit` against the filed bytes | identical, `a3aa452c…` |
| the typed packet is its own deterministic build | `python3 tools/assemble-d4-typed.py --check …` | exit 0 |
| the whole cascade satisfies the round's counting command | `python3 reports/round-20/run-validation.py` | `claim O: PASS` |
| the machine-readable receipt matches this fragment | `reports/round-20/wart/repin-r20.json` | every before/after value here appears there |

## 7. Limits

- 82 files still name the old projector sha (`grep -rl 0da0015f… . --exclude-dir=.git --exclude-dir=.scratch --exclude-dir=__pycache__ | wc -l` → 82 at 13:07Z). They are documentation and filed receipts (rounds 8–19 fragments, `corpus/lessons/round-17..19.md`, the frozen rows); they are history and are deliberately not edited.
- Rows 3–5 supersede pins that other seats may have cited while measuring (the handoff v3 design cites the r19 projection sha): supersession is signalled by the new rows only; nothing is rewritten in place.
- The adapter and typed-packet edits move two surfaces the D claim may name; re-measure before citing (shard 6 §3).
