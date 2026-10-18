# R18-D22 — fragment ledger: round-18 wave (gate generalization, D4 gate, civ map)

- round: 18 (operator loop 2 of 3, build round 2 of 4; 64 declared workers)
  · seat **R18-D22** (fragment ledger) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "D R18-D21..D28 (scribes+docs x8): frozen-manifest
  records; fragment ledger; capability drafts; ASSEMBLY.md/README updates for
  culture-d4 (new files only); docs; run logs; disposition drafts; spot-check
  ledger. reports/round-18/d4/scribe-{1..8}.md."
- date: 2026-10-18. Reference revision
  `c66ac3c951b346a2a56f9386e3324b4f5fe33902`; declared baseline `3dd3754`.
- canon: NON-CANON engineering evidence. This ledger ties fragments for the
  parent's LOG/SCORECARD integration; it admits nothing.
- writes: **this file only** + `.scratch/r18d21/`. No commit, no push.
- **close state: the wave was still in flight.** The ledger records what had
  landed by the last poll (10:25:55Z) with per-file digests; every row is
  attributed to the fragment that carries it, unless marked ⟦IC⟧
  (independently checked by this seat, command + stamp given).

## 0. Method and clock

- cwd = lane root; `export TMPDIR=$PWD/.scratch` before every scratch-writing
  command; timestamps UTC.
- Poll cadence 60 s (assignment rule; max 20 min). Window T0 = 10:19:24Z
  (independent census by seat X01, `corpus/lessons/round-18.md`), this
  seat's poll window 10:23:55Z → last poll 10:25:55Z, close sweep 10:26Z.
- A fragment hash is a read-time pin; a later mismatch means the file moved.
- A row marked *in flight* was declared by its shard's assignment but had not
  landed at the last poll; absence claims carry the poll log (negative claim
  = no path at any poll, receipt `.scratch/r18d21/poll.log`).

## 1. Declared shards (from `reports/round-18/claims.json`, `targets.json`)

| axis | workers | shard families |
|---|---:|---|
| O / operability — gate generalization + re-pin cascade + regressions | 20 | O01…O20 (`reports/round-18/gate/`, `reports/round-18/repin/`) |
| D / depth — generalized gate over D4; findings == 15-hold expected set; frozen replays | 28 | D01…D28 (this shard's family: D21–D28 scribes+docs; D01–D20 gate/tests/freeze) |
| C / coverage — round-18 civ-map revision from the round-17 patch | 10 | C01…C10 (`reports/round-18/civ/`) |
| X — cross-checks, scope, lessons, runner | 6 | X01…X06 |

## 2. Landed fragments (read-time pins, 2026-10-18)

| # | path | shard (attribution) | bytes | sha256 (16) | landed (poll) |
|---|---|---|---:|---|---|
| 1 | `reports/round-18/claims.json` | declare (parent) | 1655 | — (committed at `c66ac3c`) | pre-wave |
| 2 | `reports/round-18/targets.json` | declare (parent) | 359 | — (committed) | pre-wave |
| 3 | `examples/culture-d4/expected-holds.json` | D4-gate family | 2850 | `09490a2756d123eb` | T2 10:24:55Z |
| 4 | `tools/gates/d4-typed-labels-check-gate.py` | O family (pinnable wrapper) | 2487 | `05f99629d870280c` | T3 10:25:55Z |
| 5 | `tools/gates/d4-assembly-check-gate.py` | O family (pinnable wrapper) | 2751 | `df1a364b3970365c` | T3 10:25:55Z |
| 6 | `reports/round-18/scope.md` | X02 | — | `451428d889c8e555` | T3 |
| 7 | `reports/round-18/gate/tests-1.md` | O11 (tests ×4) | — | `8dab351ffb117352` | T3 |
| 8 | `corpus/lessons/round-18.md` | X01 | — | `f8f4e6399f1fe726` | T3 |

Every row above is **NON-CANON engineering evidence**; none of them admits
round 18 or any capability.

## 3. What each landed fragment carries (attributed readings)

- **`expected-holds.json` (row 3)** — schema `kotodama-typed-pipeline-holds-v1`;
  pins `packet_sha256 e7ecd2045ef0e5f9…`, `projection_sha256 a59990bbfe5a8992…`,
  `projector_sha256 0da0015f700345c9…`; counts `{hold: 15, note: 1, fail: 0}`;
  15 hold rows + 1 note row. ⟦IC⟧ this seat re-read the file (10:25:27Z) and
  re-derived the same counts and the same `(id, severity, where, detail)` set
  the projector emits (scribe-7 reconciliation; scribe-8 spot-check SP-4).
- **`d4-typed-labels-check-gate.py` (row 4)** — a thin read-only adapter that
  makes the flag-shaped projection check pinnable by a frozen row: it runs
  `tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check
  <target>` and forwards stdout/stderr/exit unchanged; exit codes are the
  peer's (0/1/2). ⟦IC⟧ default invocation at 10:26Z → exit 0, stdout
  `examples/culture-d4/typed-labels.d4.yml: byte-identical deterministic
  projection`.
- **`d4-assembly-check-gate.py` (row 5)** — same shape for
  `tools/assemble-culture-d4.py --check`. ⟦IC⟧ default invocation 10:26Z →
  exit 0, stdout `packet.d4.yml: byte-identical deterministic assembly`.
- **`reports/round-18/gate/tests-1.md` (row 7)** — O11's default-path
  byte-identity half: pins the pre-round-18 gate bytes
  (`d102fd1d…`, equal to `git show c66ac3c:tools/gates/typed-pipeline-gate.py`,
  ⟦IC⟧ digest match at 10:19:55Z), runs the D2 invocations under a pinned
  revision and a mirror, and quotes the round-18 brief. Its own status line
  says the post-generalization leg lands separately.
- **`reports/round-18/scope.md` (row 6)** — X02's scope watch: fleet root
  clean, filed rounds 8–17 byte-stable across the worker window (766-file
  snapshot digest `c0594947…` identical before/after; 694/694 round-17
  per-file rows recompute), round-17's rejected bytes unchanged.
- **`corpus/lessons/round-18.md` (row 8)** — X01's opening census: HEAD
  `c66ac3c`, baseline `3dd3754` is HEAD's parent, worker allocation 20+28+10+6
  = 64 equal to the declaration, LOG/SCORECARD untouched, 94 civ entries.

## 4. In-flight at close (declared, not yet landed)

| expected artifact | family | state at 10:25:55Z |
|---|---|---|
| generalized `tools/gates/typed-pipeline-gate.py` (declared assembler pin) | O | **not landed** — file still `d102fd1d…` at every poll (T1–T3) |
| `examples/culture-d4/packet.d4.typed.yml` | D | **absent** — `typed_packet=no` at every poll |
| a round-18 frozen generation (D4 typed row + wrappers) | D | **absent** — no new `MANIFEST.tsv` under `reports/round-18/` or `tools/gates/frozen/` at 10:26Z |
| `reports/round-18/run-validation.py` (the claims' counting command) | parent | **absent** at 10:26Z |
| `reports/round-18/civ/**` map revision | C | **absent** at 10:26Z |

Negative claims above rest on the poll log and on
`find reports/round-18 -type f` (4 files at T3) plus `ls examples/culture-d4/`
(6 entries at 10:25:27Z: ASSEMBLY.md, brief.md, components/, expected-holds.json,
packet.d4.yml, README.md, typed-labels.d4.yml).

## 5. Poll log (verbatim rows, receipt `.scratch/r18d21/poll.log`)

```
2026-10-18T10:23:55Z i=1 gate=d102fd1dd1bae3cc adapter=c7e5a7493601d331 projector=0da0015f700345c9 expected_holds=no  typed_packet=no r18_files=2 d4tools=0
2026-10-18T10:24:55Z i=2 gate=d102fd1dd1bae3cc adapter=c7e5a7493601d331 projector=0da0015f700345c9 expected_holds=yes typed_packet=no r18_files=2 d4tools=0
2026-10-18T10:25:55Z i=3 gate=d102fd1dd1bae3cc adapter=c7e5a7493601d331 projector=0da0015f700345c9 expected_holds=yes typed_packet=no r18_files=4 d4tools=0
```

(`d4tools` counts `tools/*d4-typed*`/`*assemble-d4*`; the two new pinnable
gates live under `tools/gates/` and are counted in `r18_files` through the
`reports/round-18/` sweep only when a fragment names them.)

## 6. Integration notes for the parent

1. **Claim O's re-pin cascade** (scribe-1 §3): the single live pin a gate
   change breaks today is `tools/gates/frozen/round-11/MANIFEST.tsv` row 1;
   new pins must be new rows/generations, never in-place edits.
2. **Claim D's equality leg** (scribe-7): the landed `expected-holds.json`
   equals the projector's emitted set exactly — 15 holds / 1 note / 0 fails —
   so the reconciliation delta is *zero* against the emitted set and *nonzero*
   against the two pre-implementation namings (design-brief 18/1, fragment
   17/1) and the landed registry declaration (6/0).
3. **Do not inherit round-17's live-path readings**: its frozen record pins a
   pre-normalization packet copy; live naming verdict moved 8 → 14 findings.
4. This ledger's fragments are per-shard evidence, not acceptance: the parent
   re-reads them against the settled tree before LOG/SCORECARD use.

## 7. Post-state addendum — what landed after §4 (10:26–10:36Z)

The wave resolved part of §4 while this seat's poll ran. Same method; stamps
from `.scratch/r18d21/poll.log` and direct reads.

| # | path | attribution (families as declared) | state |
|---|---|---|---|
| 9 | `examples/culture-d4/expected-holds.json` | D4-gate family | landed (T2 10:24:55Z) — §2 row 3 |
| 10 | `reports/round-18/d4/holds.md` (+ `interop-1..3.md`, `review-1..2.md`) | D01/D02, D-family interop/review | landed 10:26–10:33Z; holds.md carries the extraction + reconciliation (scribe-7 cross-references it) |
| 11 | `reports/round-18/run-validation.py` | parent runner (counting command) | landed 10:28Z; 1230+ lines; not executed by this seat |
| 12 | `reports/round-18/civ-map-r18.json` + `reports/round-18/civ/{README.md,patch-apply.md,delta-vs-round16.json,lessons-entry.md}` | C family | landed 10:29–10:33Z (C is another shard's claim; recorded, not re-derived here) |
| 13 | `tools/gates/frozen/<gate>/r18-post/` × 7 | O re-pin seat | landed ~10:28Z; new baseline ids at revision `c66ac3c9…`; a green battery over the enlarged surface |
| 14 | `tools/gates/frozen/round-18-repin/MANIFEST.tsv` | O re-pin seat | landed by 10:31Z; row 1 pins the gate at `5b4501a9…` and reproduces round-11's verdict bytes — but **replays exit 2** because the live gate moved past that pin (scribe-1 §9.3/§9.6) |
| 15 | `reports/round-18/gate/tests-2.md` | O11 tests | landed 10:33Z |
| 16 | `tools/gates/typed-pipeline-gate.py` (modified) | O generalization | six distinct digests 10:29:55–10:35:55Z, latest observed `ea95e2a1452ef51d…`; still writing at close |
| 17 | `reports/round-18/scope.md`, `gate/tests-1.md`, `corpus/lessons/round-18.md` | X02, O11, X01 | landed 10:25–10:26Z (§2 rows 6–8) |

Still absent at the last poll (i=13, 10:35:55Z): `examples/culture-d4/packet.d4.typed.yml`,
`tools/assemble-d4-typed.py`, any manifest row pinning the D4 typed run —
`typed_packet=no` and `d4tools=0` in every poll row.

Poll rows (verbatim tail; full log in the receipt):

```
2026-10-18T10:31:55Z i=9  gate=d09f7c3b0cb83742 … r18_files=22 d4tools=0
2026-10-18T10:32:55Z i=10 gate=3897833101be9c3a … r18_files=26 d4tools=0
2026-10-18T10:33:55Z i=11 gate=d4785d9afc0306af … r18_files=27 d4tools=0
2026-10-18T10:34:55Z i=12 gate=d4785d9afc0306af … r18_files=31 d4tools=0
2026-10-18T10:35:55Z i=13 gate=ea95e2a1452ef51d … r18_files=36 d4tools=0
```

**Close note:** the wave outlived this seat's window. Everything in this
addendum is a stamp-named reading; the parent must re-read the moving rows
(12–16) against the settled tree before any LOG/SCORECARD use.
