# R18-D23 — capability drafts: generalized typed gate, D4 gate verification, D4 pinnable checks

- round: 18 (operator loop 2 of 3, build round 2 of 4; 64 declared workers)
  · seat **R18-D23** (capability drafts) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "D R18-D21..D28 (scribes+docs x8): frozen-manifest
  records; fragment ledger; capability drafts; ASSEMBLY.md/README updates for
  culture-d4 (new files only); docs; run logs; disposition drafts; spot-check
  ledger. reports/round-18/d4/scribe-{1..8}.md."
- date: 2026-10-18. Reference revision `c66ac3c951b346a2a56f9386e3324b4f5fe33902`.
- canon: NON-CANON. **This is a draft.** It lands no SCORECARD row and admits
  no capability, no round and no canon fact. The parent decides placement and
  admission.
- writes: **this file only** + `.scratch/r18d21/`. No commit, no push.

## 1. Landing format

`SCORECARD.md` capability tables use the columns
`name | demonstrated behavior | command / evidence | first working`
(`SCORECARD.md:161` is the round-17 depth row this round answers). Rounds 8
and 9 landed new rows as a "Capabilities addendum (round N)" table under the
round's axes section; the parent decides placement. Every proposed
`first working` cell below says **proposed** so a reader cannot mistake a
draft for an admitted capability.

## 2. Draft rows (conditional — parent integrates after admission)

Proposed heading: "Capabilities addendum (round 18):"

| name | demonstrated behavior | command / evidence | first working |
|---|---|---|---|
| typed-pipeline-gate-declared-assembler | The typed-pipeline gate consumes a D4 packet through a **declared assembler pin** (packet-declared or flag) instead of the hardcoded D2 serializer; the default D2 path stays byte-identical in behavior (same stdout bytes, same exit, same 15-hold verdict); the D2-bound refusal is gone on the D4 path | `python3 reports/round-18/run-validation.py`; default-path byte-identity receipt `reports/round-18/gate/tests-1.md`; D4 equality receipt `reports/round-18/` (D family) | round 18 — proposed; only after parent admission |
| culture-d4-gate-verification | The generalized gate runs over `examples/culture-d4/packet.d4.yml` and its emitted finding set equals the D4 expected set exactly — 15 holds + 1 note + 0 fails — with `examples/culture-d4/expected-holds.json` (`09490a27…`) pinned to packet `e7ecd204…` / projection `a59990bb…` / projector `0da0015f…`; two gate runs byte-identical (determinism); round-18 frozen manifest replays green | `python3 reports/round-18/run-validation.py`; `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json`; `reports/round-18/d4/scribe-7.md` reconciliation | round 18 — proposed; only after parent admission |
| d4-pinnable-check-gates | Two thin read-only gates make flag-shaped D4 checks replayable by `tools/replay-frozen.py`: `d4-typed-labels-check-gate.py` (`05f99629…`) forwards the projector's `--check` verdict, `d4-assembly-check-gate.py` (`df1a364b…`) forwards the assembler's `--check` verdict; both exit 0 on the delivered tree and add no semantics of their own | `python3 tools/gates/d4-typed-labels-check-gate.py; echo $?` → 0; `python3 tools/gates/d4-assembly-check-gate.py; echo $?` → 0 (measured 10:26Z) | round 18 — proposed; only after parent admission |

Separability: row 1 is the O claim's evidence, rows 2–3 are D-family
evidence. Land only the rows whose claims verified; never merge two claims
into one row.

## 3. Admission conditions (parent-owned, binding)

Do not paste any row as demonstrated until each condition holds with a dated
command and its observed output:

1. `python3 reports/round-18/run-validation.py` (the claims'
   `counting_command`) exits 0 on the delivered tree.
2. **Default D2 path unchanged**: the gate's stdout bytes and exit code for
   the three D2 invocations equal the pre-round-18 revision's, and round-11
   frozen row 1 replays green with only its `gate_sha256` cell re-pointed
   (the O11 method: re-pin = digest change, not verdict change).
   Pre-leg observed by this seat at 10:20Z on the **pre**-generalization
   revision: `python3 tools/gates/typed-pipeline-gate.py` → exit 0, 16/16
   legs, 15 FINDING + 1 NOTE. The after-leg is owed.
3. **D4 equality**: the gate over the D4 packet emits exactly the 15 holds +
   the declared note (set equality on `(id, severity, where)`, counts and
   details pinned), and `examples/culture-d4/expected-holds.json` matches in
   both directions — this seat measured the expected side and the projector
   side as identical (scribe-7 §2, scribe-8 SP-4); the gate side is the D
   family's receipt.
4. **Determinism**: two gate runs over D4 are byte-identical (findings), and
   `d4-typed-labels-check-gate.py` / `d4-assembly-check-gate.py` each exit 0.
5. **Replay**: a round-18 frozen manifest (D4 typed row + wrapper rows)
   replays green under `tools/replay-frozen.py` with `TMPDIR` outside the
   repo; existing generations (round-11 11/11, round-17 5/5) stay green.
6. **Regressions**: battery `battery_exit 0, pass 7, fail 0`,
   `tools/check-craft-exercise.py <exercise.json> --counts` exit 0 and its
   `--selftest` `10/10 + 18/18`, `assemble-d2.py --check`,
   `assemble-culture-d3.py --check`, `assemble-culture-d4.py --check` all
   exit 0, and the D2 typed-pipeline gate exits 0 (all measured green by this
   seat before the generalization landed; re-run on the settled tree).
7. No filed round-8..17 byte is edited (new pins are new rows/files); pins are
   recorded before/after (scribe-1 §3).

## 4. What is deliberately **not** claimed

- No clearance: the D4 hold lines are open design debt; an exit-0 gate run
  asserts set equality, never a clean design or a canon fact.
- No real-language, attribution, or cultural permission claim; the naming
  gate's `CROSS-HOLD` line stays visible.
- No claim that the D2 15-hold set is "fixed": the D4 set reuses the D2
  identifier vocabulary (`D2L-*`) over D4 addresses (`GAR-*`, `LEX-GAR-*`,
  rank pairs) — scribe-7 dispositions that vocabulary choice explicitly.
- No rank/promotion claim; this seat ran read-only commands only.

## 5. Pre-leg receipts used by the conditions (all 2026-10-18)

| command | exit | observed | stamp |
|---|---:|---|---|
| `python3 tools/gates/typed-pipeline-gate.py` (pre-generalization) | 0 | 16/16 legs, 15 FINDING + 1 NOTE | 10:20Z |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 2 | `FAIL L1-assembler_identity: packet bytes are not assemble-d2.py's deterministic assembly (e7ecd2045ef0 vs e0f21509e14a)` | 10:20Z |
| `python3 tools/assemble-d2-typed.py --packet examples/culture-d4/packet.d4.yml --projection examples/culture-d4/typed-labels.d4.yml --emit …` | 2 | `FAIL assembler_identity: … (e7ecd2045ef0 vs e0f21509e14a)` | 10:21Z |
| `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json` | 1 | 74 labels / 15 holds / 1 note / 0 fails | 10:20Z |
| `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | 0 | byte-identical deterministic projection | 10:20Z |
| `python3 tools/gates/d4-typed-labels-check-gate.py` | 0 | projection byte-identical | 10:26Z |
| `python3 tools/gates/d4-assembly-check-gate.py` | 0 | assembly byte-identical | 10:26Z |

The two exit-2 readings are the round-17 rejection reproduced at the round-18
baseline: they are the *before* state the drafted rows may cite as the closed
gap, not as a failure of this round.

## 6. Limits

- Draft only; conditions 1, 3 (gate side) and 5 (round-18 generation) were
  not satisfiable at this seat's last stamp (wave in flight, scribe-2 §4).
- Any row landed before the parent's retrospective and routed dispositions
  would misstate the round; the parent owns that sequencing.

## 7. Post-state addendum (10:34–10:37Z) — condition status after the generalization landed

| condition (§3) | status at 10:37Z | evidence |
|---|---|---|
| 1. `python3 reports/round-18/run-validation.py` exits 0 | **not measurable by this seat** — the runner exists (10:28Z) but this seat does not run a runner that writes a receipt | — |
| 2. default D2 path unchanged | **half-proven** — live default run exit 0, 16/16 legs, stdout `15cdfbda73cd56cb6107…` equal to the pre-change run; the mirror-vs-live comparison is the O11 runner's leg | scribe-6 rows 34–36 |
| 3. D4 equality | **not yet runnable** — the generalized gate accepts the D4 packet to `ok L1-assembler` / `ok L1-expected-holds`, then `FAIL L1-build: adapter missing: tools/assemble-d4-typed.py`; expected side and projector side are equal (scribe-7 §1) | scribe-6 row 37 |
| 4. determinism | gate default run deterministic at its revision (16/16 twice across the window); D4 leg blocked with 3 | scribe-6 rows 3, 35 |
| 5. replay | **red at 10:36Z** — `tools/gates/frozen/round-18-repin/MANIFEST.tsv` replays exit 2 (`1 could-not-evaluate` for the typed-pipeline row: pin `5b4501a9…` vs live `d4785d9a…`); rows 3–12 green | scribe-1 §9.3, scribe-6 row 38 |
| 6. regressions | green: battery 0 (pass 7), craft 0 + 10/10 + 18/18, d2/d3/d4 `--check` 0, gate selftest rows as logged | scribe-6 §1 |
| 7. no filed byte edited | green: rounds 8–17 zero status entries; round-9 baseline bytes empty-diff; `r18-post` ids are new dirs | scribe-6 rows 31, 41 |

Consequence for the drafted capability rows: **none may be pasted at this
stamp.** The O row is closest — its default-path half reproduces and its
re-pin generation exists, but the generation's own pin is stale relative to the
live gate (condition 5 red). The D rows await the D4 adapter and typed packet.
The parent should re-measure §3 in full, rebuild the round-18 generation at the
final gate revision, and only then decide admission.
