# R18-D11 — negative: a hold laundered as clean (run receipts)

- round: 18 (operator loop 2 of 3, build round 2 of 4; `reports/round-18/claims.json`)
  · shard: **D11** (negatives ×3, claim D `culture-d4-gate-verification`) · owner:
  L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "D R18-D11..D13 (negatives x3): a hold laundered as
  clean / a gloss smuggled onto the D4 sound channel / an era tag outside the
  declared set — each must be caught by the generalized gate;
  reports/round-18/d4/neg-{1..3}.md."
- date: 2026-10-18 (stamps UTC). Reference revision HEAD
  `c66ac3c951b346a2a56f9386e3324b4f5fe33902`; baseline
  `3dd3754207032cb81f5fb3e202fe85cf79211339` (round-18 declare, `claims.json:6`).
  Runs stamped 10:36:30Z–10:37:53Z.
- canon: NON-CANON engineering evidence. Fixtures are synthetic controls derived
  from delivered D4 bytes; nothing here is a culture design, a canon record, a
  handoff, or a real-world claim.
- writes: **this file only** plus gitignored scratch under `.scratch/r18d11/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No
  tool, gate, packet, component, projection, expected file or earlier-round byte
  is edited by this seat. No commit, no push.
- **status: complete — caught, both directions.** Downgrading the first FORM
  hold (`hold` → `note`) and deleting it outright each exit 1 with legs that
  name the laundered record. The catch survives the pre-existing
  `L3-routing-consistency` condition of the stand-in base (§3.0), because the
  hazard adds legs that name `GAR-01` (§3.1, §3.2).

## 1. The hazard, and the catch criterion

The D4 typed pipeline emits `16` findings — `15` holds and `1` note
(`examples/culture-d4/expected-holds.json` `09490a27…`, `counts {hold 15, note 1,
fail 0}`). Six of the holds are the owed-form debt of the six routed costume
records `GAR-01..GAR-06` (one per moved gloss field, `where` = the record, one
`LEX-GAR-0n` companion row each). "Laundered as clean" is the failure mode where
that debt stops reading as debt while the artifact still assembles: the hold is
downgraded to a note, or removed from `pipeline_findings` altogether.

Catch criterion (design §3.2 anti-laundering, `claims.json:14`; carried into the
generalized gate at `tools/gates/typed-pipeline-gate.py:576-633`): the run must
exit non-zero **and** a named leg must name the missing/extra hold. A shorter
hold set alone is not a catch; the legs are `L3-holds` (`missing … extra …`),
`L3-notes`, `L3-counts`, `L3-baseline-set`, and the routing cross-check
`L3-routing-consistency`.

## 2. Fixtures (scratch, byte-pinned)

Base: `.scratch/r18d11/base-typed-standin.yml` sha256
`028fa016e2fc602374bab61ddcff1ca2909e9d45b528ddbbd822a10a159e6acf`
(71716 bytes) — the D4 typed-packet stand-in built by
`.scratch/r18d11/make-standin.py` through the adapter's own builder path
(`tools/assemble-d2-typed.py` `c7e5a749…`: `build_typed_packet` +
`carry_findings` + `render`) over the delivered `examples/culture-d4/packet.d4.yml`
`e7ecd204…` and `examples/culture-d4/typed-labels.d4.yml` `a59990bb…`; see §4 for
the stand-in's provenance and the re-run recipe once the delivered
`examples/culture-d4/packet.d4.typed.yml` lands.

| id | fixture (`.scratch/r18d11/…`) | sha256 | injection |
|---|---|---|---|
| 1a | `neg-1a.yml` | `3f37ded82979047cccd7261cf488f3d9689de493d59aa50d2f752a4aea244cc2` | `    severity: "hold"` → `    severity: "note"` on the first FORM hold block (`GAR-01` in `pipeline_findings`) |
| 1b | `neg-1b.yml` | `86cb055fd4264c761ba82338f09da4b2dcc8f1db7c3534d92016c253f0540298` | the first FORM hold block (`GAR-01`, 6 lines) deleted from `pipeline_findings` |

Each fixture is one byte-range edit. `.scratch/r18d11/build-report.json` proves
the semantic delta by parsing base and fixture with the gate's own loader and
diffing the documents: 1a is exactly
`$.pipeline_findings[0].severity: 'hold' -> 'note'`; 1b is exactly the first
block removed (`list length 16 -> 15`, every later row shifted by one). No other
field moved.

Tool revisions at every run below: `tools/gates/typed-pipeline-gate.py`
`ea95e2a1452ef51d780a701a77c37b2daf38bdae5fe6ac25e404ce2dc65d282d` (stable from
10:35:26Z through the last run, 10:37:53Z); `tools/assemble-d2-typed.py`
`c7e5a7493601d3312f2eb55185ac4d081139cdaa0e11f67dd69f67250b037071`;
`tools/assemble-culture-d4.py` `943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2`.
Python 3.14.7.

## 3. Receipts

Positive control, same stamp and revision: the untampered stand-in exits **1**
with `summary: 14/15 legs passed` and exactly one failing leg,
`L3-routing-consistency` (§3.0). Default D2 path: exit **0**,
`summary: 16/16 legs passed`, stdout sha `15cdfbda73cd56cb…` — byte-identical to
the round-11 recorded stdout; `--selftest` exit **0**, `12/12 checks passed`
(receipts `.scratch/r18d11/final/{positive-base,default-d2,selftest}.out`).

### 3.0 The pre-existing condition of the stand-in base (stated, not absorbed)

`FAIL L3-routing-consistency — holds ['GAR-01', …, 'LEX-GAR-06'] vs routed
['GAR-01', …, 'GAR-06']; owed slots ['LEX-GAR-01', …, 'LEX-GAR-06'] vs routing
['LEX-GAR-01', …, 'LEX-GAR-06']`
(`.scratch/r18d11/final/positive-base.out:33`). The delivered expected set
carries two FORM holds per routed record (`GAR-0n` and `LEX-GAR-0n`, the latter
with the identical detail), while the stand-in's routing has one moved row per
costume record; the leg requires `holds == moved`. This condition exists in the
untampered base and is therefore **not** part of any catch below; the catches are
read differentially against it. Whether the delivered D4 typed packet satisfies
this leg is a D4-route question for its owners (F-D11-1, §4).

### 3.1 The hold downgraded to a note — caught by four legs

```sh
python3 tools/gates/typed-pipeline-gate.py .scratch/r18d11/neg-1a.yml
```

counts (that command, 2026-10-18 10:36Z): exit **1**, `summary: 10/15 legs
passed` (`.scratch/r18d11/final/neg-1a.out:35`). Failing legs, verbatim
(quoted from `:26`, `:27`, `:29`, `:32`; the fifth failing leg, the pre-existing
`L3-routing-consistency` of §3.0, is `:33`):

```text
FAIL L3-holds — missing [('D2L-FORM-UNRESOLVED', 'hold', 'GAR-01')]; extra []
FAIL L3-notes — missing []; extra [('D2L-FORM-UNRESOLVED', 'note', 'GAR-01')]
FAIL L3-counts — observed counts differ from {'hold': 15, 'note': 1, 'fail': 0}
FAIL L3-baseline-set — committed set differs from the observed finding set
```

The catch names the record (`GAR-01`) and both directions of the swap — the hold
that left the set and the note that entered it. Four legs move against the 14/15
base. `--json` agrees (`exit_code 1`).

### 3.2 The hold deleted — caught by three legs, plus the routing cross-check

```sh
python3 tools/gates/typed-pipeline-gate.py .scratch/r18d11/neg-1b.yml
```

counts (that command, 2026-10-18 10:36Z): exit **1**, `summary: 11/15 legs
passed` (`.scratch/r18d11/final/neg-1b.out:33`). Failing legs, verbatim
(`:25-32`):

```text
FAIL L3-holds — missing [('D2L-FORM-UNRESOLVED', 'hold', 'GAR-01')]; extra []
FAIL L3-counts — observed counts differ from {'hold': 15, 'note': 1, 'fail': 0}
FAIL L3-baseline-set — committed set differs from the observed finding set
FAIL L3-routing-consistency — holds ['GAR-02', …, 'LEX-GAR-06'] vs routed
['GAR-01', …, 'GAR-06']; …
```

Here the routing row for `GAR-01` still exists while the hold that names it is
gone, so the cross-check names the dropped debt too (`GAR-01` present in
`routed`, absent from `holds`). Three legs move against the base.

### 3.3 The declared-identity route catches the same two fixtures

The same fixtures run with the flags the claim names (declared assembler; the
`--expected/--legacy-packet/--projection/--adapter` overrides):

```sh
python3 tools/gates/typed-pipeline-gate.py .scratch/r18d11/neg-1a.yml \
    --assembler tools/assemble-culture-d4.py \
    --legacy-packet examples/culture-d4/packet.d4.yml \
    --projection examples/culture-d4/typed-labels.d4.yml \
    --adapter tools/assemble-d2-typed.py \
    --expected examples/culture-d4/expected-holds.json
```

counts (that command, 2026-10-18 10:37Z): positive base exit 1, `15/16 legs`
(the `L1-assembler` identity leg is green — the delivered packet *is*
`assemble-culture-d4.py`'s build); 1a exit **1**, `11/16` with the same
`L3-holds`/`L3-notes`/`L3-counts` lines naming `GAR-01`
(`.scratch/r18d11/final/flag-neg-1a.out:27-30`); 1b exit **1**, `12/16`
(`flag-neg-1b.out:26-29`). Determinism: 1a/1b each run twice under both routes,
stdout and `--json` byte-identical (`cmp`, `.scratch/r18d11/final/`).

### 3.4 A tampered packet cannot be laundered upstream either

One byte-range tamper of the *legacy* D4 packet (the same era edit as
`reports/round-18/d4/neg-3.md`, `GAR-01` era `E0` → `E4`) exits **2**:
`FAIL L1-assembler: packet bytes 7f7955a2252f are not
tools/assemble-culture-d4.py's deterministic assembly (e7ecd2045ef0)`
(`.scratch/r18d11/final/flag-legacy-era-rogue.out:1`). The declared-identity leg
refuses hand-edited packet bytes before any semantic leg runs, so the
end-to-end injection point for a launder is the **typed packet** (as in §3.1-3.2),
not the packet bytes.

## 4. Sweep and the D4 route (to-verify)

Every run of this shard is recorded under `.scratch/r18d11/final/`; the sweep is
`cat .scratch/r18d11/final/runs.log` plus the flag-route `.out` files
(2026-10-18). Exits observed: default 0, selftest 0, positive 1 (base condition),
1a **1** (both routes), 1b **1** (both routes); no laundered variant exited 0; no
run produced a traceback; the gate sha is identical before and after the battery
(`ea95e2a1…`).

**Status of the D4 artifacts (to-verify).** At every stamp of this file
`examples/culture-d4/packet.d4.typed.yml` and `tools/assemble-d4-typed.py` did
not exist (sweep `ls examples/culture-d4/ tools/ | grep d4`, 10:37Z: packet,
typed-labels, expected-holds, `tools/assemble-culture-d4.py` only). The base
graded here is therefore the stand-in of §2, not the delivered typed packet.
Re-run recipe when the delivered bytes land (drop-in; the fixtures are
regenerated from the delivered base by the same builder):

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/r18d11/build-neg.py examples/culture-d4/packet.d4.typed.yml
# then the §3.1/§3.2 commands over .scratch/r18d11/neg-1{a,b}.yml
```

Caught = exit non-zero **and** a leg naming `GAR-01` in the hold set. If the
delivered typed packet changes the routing shape, the same two injections apply
(the first FORM hold in `pipeline_findings`; the routing row names the record).

**F-D11-1 (reported, not absorbed):** the stand-in cannot pass
`L3-routing-consistency` against the delivered `expected-holds.json` because that
file carries two FORM holds per routed record (`GAR-0n` + `LEX-GAR-0n`) while a
one-row-per-record routing can only carry one. Either the delivered typed packet
routes both record names, or the leg/expected set needs a D4 disposition; this
seat does not absorb the decision. Second observation for the gate owner:
`--selftest-generalized` exits **1** at `ea95e2a1…` on its own check "stale
declared pin: exit 2 and L4-pins fires — exit 2: None"
(`.scratch/r18d11/final/selftest-generalized.out`), reported as an environment
fact, not as this shard's verdict.

## 5. Sources

- `tools/gates/typed-pipeline-gate.py` `ea95e2a1…` — `L3` legs
  (`L3-holds :576`, `L3-notes :578`, `L3-counts :581`, `L3-baseline-set :611`,
  `L3-routing-consistency :630`),
  `L1-assembler` (`assembler_identity`), banner and exit codes
- `examples/culture-d4/expected-holds.json` `09490a27…` — 15 holds / 1 note
- `examples/culture-d4/packet.d4.yml` `e7ecd204…`; `typed-labels.d4.yml`
  `a59990bb…`; `tools/assemble-d2-typed.py` `c7e5a749…`
  (`build_typed_packet`, `carry_findings`); `tools/assemble-culture-d4.py`
  `943f487b…` (`assemble()`)
- receipts: `.scratch/r18d11/final/{positive-base,neg-1a,neg-1a-r2,neg-1b,neg-1b-r2,flag-base-typed-standin,flag-neg-1a,flag-neg-1b,flag-legacy-era-rogue}.out`,
  `.scratch/r18d11/final/{runs.log,selftest.out,selftest-generalized.out,default-d2.out}`,
  `.scratch/r18d11/{build-report.json,make-standin.py,build-neg.py}`
- prior art: `reports/round-17/tests/neg-2.md` (the same hazard on the D2
  wiring); `reports/round-17/tests/neg-1.md` §3.1 (the shipped-and-selftest
  laundering control)

## 6. Re-run under the next gate revision (2026-10-18 10:42Z)

The gate owner landed a further revision inside this shard's window:
`tools/gates/typed-pipeline-gate.py`
`286d6e82711427ea03a9a42e5cb10f6c369f0f1b0cd589c74a4092f3b8c12af9` (stable
across the re-run). Every run of §3 re-runs unchanged (receipts
`.scratch/r18d11/final/r2-*.out`): default D2 path exit **0**, stdout sha still
`15cdfbda73cd56cb…` (byte-identical to round-11); `--selftest` exit **0**, 12/12;
base 14/15 and 15/16 under the flags; **1a → 1** (10/15; 11/16 under the flags)
with the same `L3-holds`/`L3-notes`/`L3-counts`/`L3-baseline-set` lines naming
`GAR-01`; **1b → 1** (11/15; 12/16) naming the dropped hold. The catches are
therefore revision-stable across `ea95e2a1…` and `286d6e82…`; the run-time pin of
§3 remains `ea95e2a1…`.
