# R18-D13 — negative: an era tag outside the declared set (run receipts)

- round: 18 (operator loop 2 of 3, build round 2 of 4; `reports/round-18/claims.json`)
  · shard: **D13** (negatives ×3, claim D `culture-d4-gate-verification`) · owner:
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
- **status: complete — caught on a routed record; NOT caught off the routed
  set, and the gap is reported, not absorbed (§3.2-3.4).** The rogue tag on
  `GAR-01` is caught by `L2-channel` quoting the costume-era gate's `G-ERA`
  line naming the record and the tag (§3.1). The same tag on a names-ledger
  record moves no leg and no gate line (§3.2): the generalized gate carries no
  declared-era-set leg of its own.

## 1. The hazard, and the declared set

D4 declares its era tag space in the packet contract:
`contract.era_tags.space: ["E0","E1","E2","E3"]`
(`examples/culture-d4/packet.d4.yml:6-11`, rule at `:12`), mirrored as the flat
tag list at `eras:` (`:1789-1793`) and at `era_tags:` (`:2339-2343`). An era tag
outside that set is the hazard: the record claims a stage the culture never
declared, and every dated check (material/era routes, rank intervals, the
anachronism sweep) reads a tag it cannot place.

Catch criterion (generalized gate `ea95e2a1…`): the run must exit non-zero
**and** a named leg must name the record and the tag. The semantic check is the
costume-era kernel's `G-ERA` (`tools/gates/costume-era-consistency-gate.py:695`,
"era %r is not in `eras`"); the gate surfaces it through `L2-channel`'s
off-channel rule (`typed-pipeline-gate.py:521` collect, `:550` check) when the
record it names is
a routed record.

## 2. Fixtures (scratch, byte-pinned)

Base: `.scratch/r18d11/base-typed-standin.yml` sha256
`028fa016e2fc602374bab61ddcff1ca2909e9d45b528ddbbd822a10a159e6acf`
(71716 bytes); provenance as in `reports/round-18/d4/neg-1.md` §2.

| id | fixture (`.scratch/r18d11/…`) | sha256 | injection |
|---|---|---|---|
| 3 | `neg-3.yml` | `1ac236574f4dc0946ad608949b1c216b1e80bb5207ce63fe9cca5286084f650a` | `    era: "E0"` → `    era: "E4"` on the first costume record (`GAR-01`; the packet's own line is `:1603`) — a tag outside the declared E0–E3 space |
| 3b (boundary) | `neg-3b.yml` | `eccd1fd4b558d2b622b2098b08b2f0809762ecb4aa1524bd6460b5f0ecb31f60` | the same `E0` → `E4` edit on the **first names-ledger record** (`NM-01`; `names:` at packet `:1936` / stand-in `:1936`, the injected `era` line at `:1941` in both) — outside any routed record |
| 3c (legacy) | `legacy-era-rogue.yml` | (regenerated per run; 82759 bytes) | the same `E0` → `E4` edit applied to the legacy packet `examples/culture-d4/packet.d4.yml` (its `costumes: GAR-01` line `:1603`) |

Each is one byte-range edit; `.scratch/r18d11/build-report.json` proves fixture
3 with the gate's own loader — exactly `$.costumes[0].era: 'E0' -> 'E4'`, and
nothing else moved. The rogue tag `E4` is derived, not hard-coded: the builder
reads the declared set from the packet and picks `max+1`.

Tool revisions at every run: `tools/gates/typed-pipeline-gate.py`
`ea95e2a1452ef51d780a701a77c37b2daf38bdae5fe6ac25e404ce2dc65d282d` (stable
10:35:26Z–10:37:53Z); `tools/gates/costume-era-consistency-gate.py`
`e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f`;
`tools/assemble-culture-d4.py` `943f487b…`. Python 3.14.7.

## 3. Receipts

### 3.1 The rogue tag on a routed record — caught by `L2-channel`

```sh
python3 tools/gates/typed-pipeline-gate.py .scratch/r18d11/neg-3.yml
```

counts (that command, 2026-10-18 10:36Z): exit **1**, `summary: 13/15 legs
passed` (`.scratch/r18d11/final/neg-3.out:34`). The failing leg, verbatim
(`:24`):

```text
FAIL L2-channel — off-channel lines in the typed run: ["costume-era-consistency-gate.py: FINDING G-ERA: [hold] GAR-01: era 'E4' is not in `eras` — anachronism sweep cannot date this row"]
```

The catch names the gate (`costume-era-consistency-gate.py`), the record
(`GAR-01`) and the tag (`'E4'`), and it quotes the kernel's own era verdict.
Against the untampered base (`14/15`, its single failure the pre-existing
routing condition of `neg-1.md` §3.0) the rogue tag adds exactly this leg.
Under the declared-identity route (§3.5) the same fixture exits **1**,
`14/16`, with the identical `L2-channel` line
(`.scratch/r18d11/final/flag-neg-3.out:25`). `--json` agrees; two runs per route
are byte-identical (`cmp`).

### 3.2 The boundary — the same tag off the routed set is NOT caught

```sh
python3 tools/gates/typed-pipeline-gate.py .scratch/r18d11/neg-3b.yml
```

counts (that command, 2026-10-18 10:36Z): exit **1**, `summary: 14/15 legs
passed` — the *same* single failure as the untampered base, and no leg names the
rogue tag (`diff .scratch/r18d11/final/{positive-base,neg-3b}.out` → exit 0:
the two stdouts are **byte-identical**; `--json` failing sets are identical,
`translated_on_sound_channel` 0 in both). Measured at
the gate's own inputs: the five culture gates over the tampered packet produce
**zero** line differences against the delivered packet for every one of the five
(`.scratch/r18d11/probe-era-name.yml`; base vs probe outputs `diff` clean,
2026-10-18 10:31Z) — the names ledger's `era` field is read by no kernel.

So the out-of-set era is caught **only when it lands on a routed record**, and
then by the off-channel rule rather than by an era-set rule. **F-D13-1
(reported, not absorbed):** the generalized gate at `ea95e2a1…` carries no
declared-era-set leg; an out-of-set tag on a non-routed record (names,
pantheon/motifs, calendar rows not read by the costume kernel) is invisible to
every leg. If claim O's generalization is meant to police the declared space, a
leg reading `contract.era_tags.space` (and/or the packet's `eras` tag list)
against every `era`/`eras`-bearing record is the missing piece; this seat does
not write it.

### 3.3 The legacy-packet route — a tamper catch, not an era catch

```sh
python3 tools/gates/typed-pipeline-gate.py .scratch/r18d11/legacy-era-rogue.yml \
    --assembler tools/assemble-culture-d4.py \
    --legacy-packet .scratch/r18d11/legacy-era-rogue.yml \
    --projection examples/culture-d4/typed-labels.d4.yml \
    --adapter tools/assemble-d2-typed.py \
    --expected examples/culture-d4/expected-holds.json
```

counts (that command, 2026-10-18 10:37Z): exit **2**, `FAIL L1-assembler:
packet bytes 7f7955a2252f are not tools/assemble-culture-d4.py's deterministic
assembly (e7ecd2045ef0)`
(`.scratch/r18d11/final/flag-legacy-era-rogue.out:1`). The declared-identity leg
refuses a hand-edited packet before any era semantics run, so this is a
tamper/identity catch: it would fire for any byte change, not for the tag.

### 3.4 What the boundary means for the D4 route

The delivered expected set (`examples/culture-d4/expected-holds.json`
`09490a27…`) contains no era-class hold, and the five kernels emit no era line
over the delivered packet (`costume-era-consistency-gate.py` exit 0, 0 findings).
So the era containment that exists today is: (a) the packet assembler's own
`--check` identity (`tools/assemble-culture-d4.py`), (b) the costume kernel's
`G-ERA` for costume/rank rows, and (c) the gate's off-channel rule carrying
(a)/(b) into a typed-run failure when the row is routed. A general declared-set
leg is the gap of F-D13-1.

### 3.5 Determinism

Every fixture was run twice per route (10:36Z, 10:37Z); stdout and `--json`
byte-identical (`cmp` clean,
`.scratch/r18d11/final/{neg-3,neg-3-r2,flag-neg-3,flag-neg-3-r2}.out|.json`).
The gate sha is identical before and after the battery (`ea95e2a1…`).

## 4. Sweep and the D4 route (to-verify)

Recorded under `.scratch/r18d11/final/`; sweep `cat
.scratch/r18d11/final/runs.log` (2026-10-18). Exits observed: default D2 path 0
(stdout `15cdfbda…`, byte-identical to the round-11 record), selftest 0 (12/12),
positive base 1, **3 → 1** on both routes, **3b → 1 with no new leg** (the gap),
3c → 2 (identity). No run produced a traceback.

**Status of the D4 artifacts (to-verify).** `examples/culture-d4/packet.d4.typed.yml`
and `tools/assemble-d4-typed.py` did not exist at any stamp of this file; the
graded base is the stand-in of §2. Re-run recipe when the delivered typed packet
lands:

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/r18d11/build-neg.py examples/culture-d4/packet.d4.typed.yml
python3 tools/gates/typed-pipeline-gate.py .scratch/r18d11/neg-3.yml
```

Caught = exit non-zero **and** a leg naming the record and `E4`. If the
delivered typed packet routes additional record classes, repeat 3b's injection on
a non-routed record to re-check F-D13-1 against the final gate revision.

## 5. Sources

- `examples/culture-d4/packet.d4.yml` `e7ecd204…` — `contract.era_tags.space`
  (`:6-12`), `eras` tags (`:1789-1793`), `era_tags` (`:2339-2343`), costumes
  (`:1596-1704`), names (`:1936-`, the injected `NM-01` era at `:1941`)
- `tools/gates/typed-pipeline-gate.py` `ea95e2a1…` — `L2-channel`
  (off-channel collect `:521`, check `:550`), `L1-assembler`
  (`assembler_identity`)
- `tools/gates/costume-era-consistency-gate.py` `e6bffd70…` — `G-ERA` (`:695`),
  era model (`norm_eras`, `:417-453`)
- `.scratch/r18d11/base-typed-standin.yml` `028fa016…`;
  `.scratch/r18d11/{neg-3,neg-3b,legacy-era-rogue}.yml`; fixtures built by
  `.scratch/r18d11/{make-standin.py,build-neg.py}`; delta proof
  `.scratch/r18d11/build-report.json`
- receipts: `.scratch/r18d11/final/{neg-3,neg-3-r2,neg-3b,flag-neg-3,flag-neg-3-r2,flag-legacy-era-rogue,positive-base,flag-base-typed-standin}.out`,
  `.scratch/r18d11/final/runs.log`, `.scratch/r18d11/probe-era-name.yml` +
  `.scratch/r18d11/{base,probeera}-*-gate.out` (the zero-diff gate sweep)

## 6. Re-run under the next gate revision (2026-10-18 10:42Z)

`tools/gates/typed-pipeline-gate.py`
`286d6e82711427ea03a9a42e5cb10f6c369f0f1b0cd589c74a4092f3b8c12af9` (stable
across the re-run): default D2 path exit **0** (stdout sha `15cdfbda73cd56cb…`,
unchanged); `--selftest` 12/12; base 14/15 and 15/16 (flags). **3 → 1** (13/15
declaration route, 14/16 flags) with the identical `L2-channel` line quoting
`G-ERA … GAR-01: era 'E4'`; **3b still moves no leg** (14/15, 15/16, stdout
byte-identical to the base — `diff -q` clean), so **F-D13-1 reproduces at the
newer revision**. Receipts `.scratch/r18d11/final/r2-{base-typed-standin,neg-3,neg-3b,flag-neg-3,flag-base-typed-standin}.out`.
