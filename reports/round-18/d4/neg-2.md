# R18-D12 — negative: a gloss smuggled onto the D4 sound channel (run receipts)

- round: 18 (operator loop 2 of 3, build round 2 of 4; `reports/round-18/claims.json`)
  · shard: **D12** (negatives ×3, claim D `culture-d4-gate-verification`) · owner:
  L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "D R18-D11..D13 (negatives x3): a hold laundered as
  clean / a gloss smuggled onto the D4 sound channel / an era tag outside the
  declared set — each must be caught by the generalized gate;
  reports/round-18/d4/neg-{1..3}.md."
- date: 2026-10-18 (stamps UTC). Reference revision HEAD
  `c66ac3c951b346a2a56f9386e3324b4f5fe33902`; baseline
  `3dd3754207032cb81f5fb3e202fe85cf79211339`. Runs stamped 10:36:30Z–10:37:53Z.
- canon: NON-CANON engineering evidence. Nothing here is a culture design, a
  canon record, a handoff, or a real-world claim.
- writes: **this file only** plus gitignored scratch under `.scratch/r18d11/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No
  tool, gate, packet, component, projection, expected file or earlier-round byte
  is edited by this seat. No commit, no push.
- **status: complete — caught.** The restored gloss is caught by `L2-channel`
  with a record-addressed line naming `GAR-01` and the naming gate (§3.1); the
  raw-packet variant is refused upstream by the declared-identity leg (§3.4).

## 1. The hazard, and the catch criterion

The D4 typed routing moves each translated gloss off the sound-and-identity
channel: one `typed_channel` row per costume record `GAR-01..GAR-06` carries
`source_field: garment` → `off_channel_field: garment_gloss`
(`.scratch/r18d11/base-typed-standin.yml:2353-2413`; the same shape the D2 gate
froze at `examples/culture-d2/packet.d2.typed.yml:3324-3424`). The hazard is the
inverse move: the gloss is put **back** on the checked field, so the naming gate
reads an English gloss as a surface form and the "typed" packet silently carries
translated text on the channel the pipeline exists to protect.

Catch criterion (design §6 hazard control 1; generalized gate
`tools/gates/typed-pipeline-gate.py:469-556`, the check at `:550`): the run must
exit non-zero **and**
`L2-channel` must name the off-channel record. The leg fails when the typed run
contains any line naming a moved record (`off-channel lines in the typed run:
[…]`), when the retired lines are not exactly the moved records' artifact lines
(`removed N, routed M`), or when an added/removed line is not a PHON artifact.

## 2. Fixture (scratch, byte-pinned)

Base: `.scratch/r18d11/base-typed-standin.yml` sha256
`028fa016e2fc602374bab61ddcff1ca2909e9d45b528ddbbd822a10a159e6acf`
(71716 bytes); provenance as in `reports/round-18/d4/neg-1.md` §2.

| id | fixture (`.scratch/r18d11/…`) | sha256 | injection |
|---|---|---|---|
| 2 | `neg-2.yml` | `9230db46be532ddea17bb0a7845598dc9d97c6b5d9f79d8703540eba9c487210` | `    garment_gloss: "forge apron (thick hide; spark and slag protection)"` → `    garment: "forge apron (thick hide; spark and slag protection)"` on `GAR-01` (the moved gloss restored onto the checked field) |

One byte-range edit. `.scratch/r18d11/build-report.json` proves the delta with
the gate's own loader: exactly
`$.costumes[0].garment: absent -> 'forge apron (thick hide; spark and slag
protection)'` and `$.costumes[0].garment_gloss: '…' -> absent`. Nothing else
moved.

Tool revisions at every run: `tools/gates/typed-pipeline-gate.py`
`ea95e2a1452ef51d780a701a77c37b2daf38bdae5fe6ac25e404ce2dc65d282d` (stable
10:35:26Z–10:37:53Z); `tools/assemble-d2-typed.py` `c7e5a749…`;
`tools/assemble-culture-d4.py` `943f487b…`. Python 3.14.7.

## 3. Receipts

### 3.1 Caught by `L2-channel`

```sh
python3 tools/gates/typed-pipeline-gate.py .scratch/r18d11/neg-2.yml
```

counts (that command, 2026-10-18 10:36Z): exit **1**, `summary: 13/15 legs
passed` (`.scratch/r18d11/final/neg-2.out:34`). The catch's failing leg, verbatim
(`:24`; the other failing leg, `:33`, is `neg-1.md` §3.0's pre-existing
condition):

```text
FAIL L2-channel — off-channel lines in the typed run: ["naming-collision-gate.py: FINDING PHON-INVENTORY: FAIL — name GAR-01 'forge apron (thick hide; spark and slag protection)': symbol /f/ at position 1 is not in the declared inventory (consonants {p, t, k, b, d, g, m, n, s, r, l, w, j, h}, vowels {a, e, i, o, u})"]
```

The catch names both the gate (`naming-collision-gate.py`) and the record
(`GAR-01`) — record-addressed, not a bare nonzero exit. Corroborating line
(`:23`): `channel: 5 PHON artifact(s) retired, 0 added, retained lines identical`
against 6 moved rows — one retirement was lost, and the lost one is the smuggled
record. Against the untampered base (`14/15`, its only failure the pre-existing
routing condition of `neg-1.md` §3.0), the smuggle adds exactly this leg.

### 3.2 The declared-identity route catches it too

```sh
python3 tools/gates/typed-pipeline-gate.py .scratch/r18d11/neg-2.yml \
    --assembler tools/assemble-culture-d4.py \
    --legacy-packet examples/culture-d4/packet.d4.yml \
    --projection examples/culture-d4/typed-labels.d4.yml \
    --adapter tools/assemble-d2-typed.py \
    --expected examples/culture-d4/expected-holds.json
```

counts (that command, 2026-10-18 10:37Z): exit **1**, `summary: 14/16 legs
passed`; the failing leg is the same `L2-channel` line naming `GAR-01`
(`.scratch/r18d11/final/flag-neg-2.out:25`). The positive base under the same
flags is `15/16` (only the pre-existing routing leg), so the smuggle adds exactly
one leg there as well. `--json` agrees (`exit_code 1`,
`translated_on_sound_channel 1`).

### 3.3 Determinism

The fixture was run twice under each route (10:36Z, 10:37Z); stdout and `--json`
are byte-identical (`cmp` clean,
`.scratch/r18d11/final/{neg-2,neg-2-r2,flag-neg-2,flag-neg-2-r2}.out|.json`).

### 3.4 Boundary — the raw-packet route is refused before the channel leg

A legacy-packet smuggle (the same edit applied to
`examples/culture-d4/packet.d4.yml` in scratch) cannot reach the channel leg:
the declared-identity leg refuses the bytes first — exit **2**, `FAIL
L1-assembler: packet bytes … are not tools/assemble-culture-d4.py's
deterministic assembly (e7ecd2045ef0)` (the receipt is the same identity
refusal recorded in `reports/round-18/d4/neg-1.md` §3.4 and `neg-3.md` §3.3).
Reported, not absorbed: for D4 the end-to-end channel injection point is the
**typed packet**, exactly as in round 17 (`reports/round-17/tests/neg-1.md`
§3.2); a component-level injection belongs to the D4 build's own tests.

## 4. Sweep and the D4 route (to-verify)

Recorded under `.scratch/r18d11/final/`; sweep `cat
.scratch/r18d11/final/runs.log` (2026-10-18). Exits observed: default D2 path 0
(stdout `15cdfbda…`, byte-identical to the round-11 record), selftest 0 (12/12),
positive base 1, **2 → 1** under both routes; no smuggle variant exited 0; no
traceback; gate sha unchanged across the battery.

**Status of the D4 artifacts (to-verify).** `examples/culture-d4/packet.d4.typed.yml`
and `tools/assemble-d4-typed.py` did not exist at any stamp of this file (10:37Z
sweep). The graded base is the stand-in of §2. Re-run recipe when the delivered
typed packet lands:

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/r18d11/build-neg.py examples/culture-d4/packet.d4.typed.yml
python3 tools/gates/typed-pipeline-gate.py .scratch/r18d11/neg-2.yml
```

Caught = exit non-zero **and** a `L2-channel` line naming the routed record. The
injection is read from the routing row (`off_channel_field` → `source_field`
rename), so it re-points itself at whatever the delivered routing declares.

## 5. Sources

- `tools/gates/typed-pipeline-gate.py` `ea95e2a1…` — `L2-channel`
  (off-channel collect `:521`, check `:550`), moved/retained routing split
  (`:463-466`), identity leg
  (`assembler_identity`)
- `.scratch/r18d11/base-typed-standin.yml` `028fa016…` — `typed_channel`
  (`:2353-2448`), `assembly` declaration block (`:2344-2352`)
- `examples/culture-d4/packet.d4.yml` `e7ecd204…`; `typed-labels.d4.yml`
  `a59990bb…`; `tools/assemble-d2-typed.py` `c7e5a749…`
- receipts: `.scratch/r18d11/final/{neg-2,neg-2-r2,flag-neg-2,flag-neg-2-r2,positive-base,flag-base-typed-standin}.out`,
  `.scratch/r18d11/final/runs.log`, `.scratch/r18d11/build-report.json`
- prior art: `reports/round-17/tests/neg-1.md` (the same hazard on the D2
  wiring, including the raw-packet identity refusal)

## 6. Re-run under the next gate revision (2026-10-18 10:42Z)

`tools/gates/typed-pipeline-gate.py`
`286d6e82711427ea03a9a42e5cb10f6c369f0f1b0cd589c74a4092f3b8c12af9` (stable
across the re-run): default D2 path exit **0** (stdout sha `15cdfbda73cd56cb…`,
unchanged); `--selftest` 12/12; base 14/15 and 15/16 (flags); **the smuggle
again exits 1** — 13/15 (declaration route) and 14/16 (flags) with the identical
`L2-channel` line naming `GAR-01`; `channel: 5 PHON artifact(s) retired` against
6 moved rows. Receipts `.scratch/r18d11/final/r2-{base-typed-standin,neg-2,flag-neg-2}.out`.
The catch is revision-stable across `ea95e2a1…` and `286d6e82…`.
