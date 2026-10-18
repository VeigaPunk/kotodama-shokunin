# R17-D32 — negative: a loan without a layer reference (run receipts)

- round: 17 (loop 2 of 3, build round 1 of 4) · shard: **D32** (negatives ×3,
  claim D `culture-d4-assembly`) · owner: L2 worker, kotodama-shokunin lane
- assignment (verbatim): "D4 R17-D30..D32 (negatives x3): gloss smuggled onto
  sound channel; owed form silently dropped; loan without layer ref — each must
  be caught; reports/round-17/tests/neg-<n>.md."
- date: 2026-10-18. Baseline revision
  `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` (`reports/round-17/claims.json:5`);
  working-tree HEAD `9b49a4a` at write time.
- canon: NON-CANON engineering evidence. Fixtures are synthetic controls derived
  from filed D2 bytes and a filed gate fixture; nothing here is a culture design,
  a canon record, a handoff, or a real-world claim.
- writes: **this file only** plus gitignored scratch under `.scratch/r17-d-neg/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No
  tool, gate, packet, component, projection, fixture or earlier-round byte is
  edited by this seat. No commit, no push.
- **status: complete — caught on both channels.** Typed channel: the projector
  emits a `D2L-BORROW` **fail** naming the loan (§3.1, §3.2, §3.3). Lexicon
  channel: the coverage audit adds `L-layer-unregistered` naming the lexeme
  (§3.4).

## 1. The hazard, and the catch criterion

A borrowed-strata label must name the declared loan layer it entered through:
the projector builds `borrow.layer_ref` from the lexicon entry's `loan_layer`
(or falls back to the `layer` value, `tools/d2-typed-labels.py:540-579`) and
`check_borrow` refuses a `layer_ref` that does not resolve to a declared layer
(`:701-704`). The hazard is a loan that carries no layer reference at all: the
borrow route is then unevaluated while the form still reads as a supplied,
inventory-clean surface form.

Catch criterion: the run must exit non-zero **and** a finding must name the loan
record and the unresolved reference. Two channels are exercised because the
typed pipeline (D4's route) reads the projector, while the legacy/audit route
reads the lexicon entry directly.

## 2. Fixtures (scratch, byte-pinned)

| id | fixture (`.scratch/r17-d-neg/…`) | sha256 | injection |
|---|---|---|---|
| 3a | `packet-loan-nolayer-live.yml` | `c99931390cb22d25a1a83abc62ff7a7e9cbce5aed17531207c02c6ad58bd3fc3` | a `typed_labels` entry `NEG-LOAN-01` (`borrowed-strata`, supplied, donor `gas`, substitutions `g→k`) whose `borrow` block carries **no `layer_ref`**, inserted before `costumes:` in the live packet |
| 3b | `packet-lexicon-loan-nolayer.yml` | `7d1e49497224c0782243b42f7cc7e4012fd703771b0841b9f747eaa3968d72b9` | `    loan_layer: "Salt-road trade layer"\n` removed from lexicon entry `L-26` — the loan's layer reference deleted at the lexicon channel |
| 3c | `audit-loan-nolayer.yml` | `43125da4de993c02950131ca61d22095691f57e8d44b8d590329ddb2b6295e82` | the filed audit fixture with its **first** `    loan_layer: Kulvan trade layer\n` removed (entry `parnu` loses its layer reference) |

Base bytes: `examples/culture-d2/packet.d2.yml` sha256
`e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643`;
`tools/gates/fixtures/lexicon-coverage-audit.yml` (read-only, copied to scratch
before editing). Each fixture is one insertion or one deletion; generation was a
`python3` heredoc from the lane root with `TMPDIR=$PWD/.scratch` (the exact
strings are the table's injection column, byte for byte). A fourth, minimal
packet was attempted and abandoned: `--packet` runs the full reconciliation
projection, which requires the complete packet shape
(`d2-typed-labels error: packet.materials: expected a non-empty record list`) —
the isolation control is §3.3 instead.

Tool revisions at every run below: `tools/d2-typed-labels.py`
`0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`;
`tools/gates/lexicon-coverage-audit.py`
`2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287`;
`tools/assemble-d2-typed.py`
`c7e5a7493601d3312f2eb55185ac4d081139cdaa0e11f67dd69f67250b037071`.
Python 3.14.7.

## 3. Receipts

Live control: `python3 tools/d2-typed-labels.py --packet examples/culture-d2/packet.d2.yml`
→ exit 1 (holds), `stats {fail: 0, hold: 15, labels: 58, note: 1}`
(`.scratch/r17-d-neg/proj-live.json`) — the live packet carries zero fails and
two typed loan records, both with their layer reference
(`examples/culture-d2/packet.d2.yml:844,860`).

### 3.1 Typed label with no `layer_ref` — caught by the projector

```sh
python3 tools/d2-typed-labels.py --packet .scratch/r17-d-neg/packet-loan-nolayer-live.yml --json
```

counts (that command, 2026-10-18): exit **1**, `stats {fail: 1, hold: 15,
labels: 59, note: 1}` (`run-packet-loan-nolayer-live.json`). The fail, verbatim:

```json
{"code": "D2L-BORROW", "detail": "layer_ref None does not resolve to a declared layer",
 "id": "D2L-BORROW", "severity": "fail", "where": "NEG-LOAN-01"}
```

The catch names the record and the unresolved reference, and it is a **fail**
(not a hold): the run's fail count moved 0 → 1 while the hold set stayed at 15.
The live run's `--json` and the fixture run differ in exactly that one finding
plus the label count.

### 3.2 Lexicon channel: `loan_layer` deleted — caught by the projector

```sh
python3 tools/d2-typed-labels.py --packet .scratch/r17-d-neg/packet-lexicon-loan-nolayer.yml --json
```

counts (that command, 2026-10-18): exit **1**, `stats {fail: 1, hold: 15,
labels: 58, note: 1}` (`run-packet-lexicon-loan-nolayer.json`). The fail:

```json
{"code": "D2L-BORROW", "detail": "layer_ref 'loan' does not resolve to a declared layer",
 "id": "D2L-BORROW", "severity": "fail", "where": "L-26"}
```

Here the layer reference was deleted at the lexicon channel; the projector's
fallback (`layer_name = … else layer`, `tools/d2-typed-labels.py:545`) hands the
literal string `loan` to `check_borrow`, which still refuses it. The catch names
the lexeme (`L-26`).

### 3.3 Isolation control — `parse_typed_labels` direct call

```sh
python3 - <<'EOF'   # runpy.run_path("tools/d2-typed-labels.py"); parse_typed_labels(probe)
EOF
```

counts (2026-10-18, `probe-loan-nolayer.json`): `exit_code` **2** (the
function-level code: fails present, `tools/d2-typed-labels.py:812`),
`stats {fail: 2, hold: 0, labels: 1}`; the `D2L-BORROW` finding carries the same
detail and `where: NEG-LOAN-01`. The CLI maps the same defect to process exit 1
per the spec table (a finding is 1; `D2L-DATA`/loader is 2). This control shows
the catch is the projector's own check, not an artifact of the live packet.

### 3.4 Lexicon audit channel — `L-layer-unregistered`

```sh
python3 tools/gates/lexicon-coverage-audit.py .scratch/r17-d-neg/audit-loan-nolayer.yml
```

counts (that command, 2026-10-18): exit **1**; findings 20 (baseline fixture,
`audit-fixture-baseline.txt`) → 21 (`audit-loan-nolayer-run.txt`). The single
added line, verbatim (`diff` of the `FINDING` sets):

```text
FINDING L-layer-unregistered: borrowed lexeme 'parnu' references layer '(none)', which is not declared; its contact, adaptation, and chronology records are unevaluated
```

The audit names the loan and the missing reference at the legacy channel
(`tools/gates/lexicon-coverage-audit.py:907-917`). No other line changed.

### 3.5 Boundary note — packet-byte injection is refused earlier

Handing 3a to the typed adapter
(`python3 tools/assemble-d2-typed.py --packet .scratch/r17-d-neg/packet-loan-nolayer-live.yml`)
exits **2**, `FAIL assembler_identity: packet bytes are not assemble-d2.py's
deterministic assembly (c99931390cb2 vs e0f21509e14a)`
(`adapter-loan-nolayer.txt:1`). Reported, not absorbed: the assembler refuses a
hand-edited packet before any semantic check, so the end-to-end injection point
for the typed chain is the **components** (which the assembler turns into the
packet), not the packet bytes. For D4 this means the loan-without-layer-ref
control must be run after a component-level injection, or at the typed-label
stage as here.

### 3.6 Gate leg — the build-time fail reaches L3 and is caught

The adapter carries the projector's finding set verbatim into the typed packet's
`pipeline_findings` (`tools/assemble-d2-typed.py:1-30`), and the gate's L3 grades
that set against the frozen baseline. Probe fixture
`typed-loan-fail-added.yml` sha256
`a34e5b9ebb171ae6dd53bdc89cca3fd11d2aae908ff770c3e6ab0e5d6ccbe0f2`: the typed
packet with one `D2L-BORROW` fail block for `NEG-LOAN-01` prepended to
`pipeline_findings` (the shape §3.1's projector output takes once assembled).

```sh
python3 tools/gates/typed-pipeline-gate.py .scratch/r17-d-neg/typed-loan-fail-added.yml
```

counts (that command, 2026-10-18): exit **1**, `summary: 9/13 legs passed`
(`run-typed-loan-fail-added.txt:32`). The failing legs, verbatim:

```text
FAIL L3-fails — fail set: [('D2L-BORROW', 'fail', 'NEG-LOAN-01')]                    (:25)
FAIL L3-counts — observed counts differ from {'hold': 15, 'note': 1, 'fail': 0}      (:26)
FAIL L3-details — a detail string differs from the committed baseline                (:28)
FAIL L3-baseline-set — committed set differs from the observed finding set           (:29)
```

The catch names the loan record and the `D2L-BORROW` class. So a loan that
reaches the gate as an added fail is caught by L3; the projector (§3.1-§3.3) is
where it is caught earliest.

## 4. Sweep

Every run of this shard is recorded under `.scratch/r17-d-neg/`; the sweep is
`ls .scratch/r17-d-neg/run-*` plus `probe-loan-nolayer.json` and the audit diff
(2026-10-18). Exits observed: live control 1 (holds only, fail 0), 3a **1**
(fail 1), 3b **1** (fail 1), 3c API **2** (fail 2), 3d **1** (one added
finding), 3e gate **1** (L3-fails names `D2L-BORROW`/`NEG-LOAN-01`), adapter
**2** (identity refusal). No loan-without-layer-ref variant exited 0; no run
produced a traceback.

## 5. D4 re-point (to-verify at write time)

D4's design contracts landed during this shard
(`reports/round-17/d4/typed-support-1.md` §4-5, `typed-support-2.md` §2-3);
state at last poll (2026-10-18 09:32Z): `tools/assemble-culture-d4.py` has
landed, while `examples/culture-d4/` is still absent (components drafting under
`reports/round-17/d4/components/`, 3/12 at that stamp). Re-point recipe when D4
lands:

1. inject the defect at D4's source of borrowed labels — a component-level
   lexicon/loan entry or a typed label whose borrow block lacks its layer
   reference;
2. run D4's typed-label step (or the D4 projector) and the D4 gate;
3. caught = nonzero exit **and** a `D4L-BORROW`-class finding naming the loan
   record and the unresolved reference (`typed-support-1.md` §5.5 names the
   class); the audit-channel equivalent is `L-layer-unregistered` naming the
   lexeme.

Note for the D4 projector seat (report, not absorbed): the D2 projector's
culture-bound legs measured by D18 (`typed-support-1.md` §4, F-D18-1..5) mean a
D4 derivation must bind its own slot prefix, rank leg and assembler identity —
the loan check itself (`check_borrow`) is culture-neutral and must survive the
port.

This is `to-verify` — both catch mechanisms are shared tool code
(`tools/d2-typed-labels.py:701-704`,
`tools/gates/lexicon-coverage-audit.py:907-917`), but neither has been re-run
over D4 bytes by this seat.

Note on the D4 spelling: D4's candidate set uses `D4L-BORROW` for a *different*
trigger — incomplete donor separation (`AL-03`,
`reports/round-17/d4/design-brief.md` §7.1 row 3) — so a D4 loan with no layer
reference must surface as a fail class in the D4 controls (its §8 battery,
C-01..C-10), per the freeze rule that every FAIL class lives in controls, not in
the shipped bytes (§7.2.4). The catch criterion is unchanged: a finding naming
the loan record and the unresolved reference.

## 6. Sources

- `tools/d2-typed-labels.py` `0da0015f…` — `_lexicon_label` (`:540-579`),
  `check_borrow` (`:692-730`), `validate_labels` (`:733-813`)
- `tools/gates/lexicon-coverage-audit.py` `2c4dd397…` — loan-layer coherence
  (`:876-917`)
- `tools/assemble-d2-typed.py` `c7e5a749…` — assembler identity
  (`adapter-loan-nolayer.txt:1`)
- `examples/culture-d2/packet.d2.yml` `e0f21509…` — `L-26` (`:838-844`),
  `L-27` (`:854-860`), layers (`:2539+`)
- `tools/gates/fixtures/lexicon-coverage-audit.yml` (read-only base for 3c)
- receipts: `.scratch/r17-d-neg/run-packet-loan-nolayer-live.json`,
  `run-packet-lexicon-loan-nolayer.json`, `probe-loan-nolayer.json`,
  `audit-fixture-baseline.txt`, `audit-loan-nolayer-run.txt`,
  `run-typed-loan-fail-added.txt`, `adapter-loan-nolayer.txt`, `proj-live.json`
