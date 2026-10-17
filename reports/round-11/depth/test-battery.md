# R11-D16 — test battery: `check-gate-battery --selftest` green post-wiring (claim D, `d2-typed-pipeline`)

- seat: **R11-D16** (test shard, claim D), round 11 (loop 1 of 3, build round 4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D16 (test battery): check-gate-battery --selftest green post-wiring; reports/round-11/depth/test-battery.md."
- writes: this file only (plus in-lane scratch under `.scratch/d16/`). No commit, no push; no earlier-round artifact byte touched (`reports/round-{8,9,10}/**` are filed and read-only here). No tool, gate, packet, baseline or manifest is written or edited by this seat.
- clock: all stamps UTC (`date -u +%FT%TZ`); local = UTC-03:00. Canon: NON-CANON engineering evidence. Nothing here admits a round, a capability or a canon fact.

## 0. Verdict

**PASS — the battery is green post-wiring in the claim's acceptance sense, and unchanged in scope.**

| leg (final stamp 2026-10-17T22:15:21–24Z) | result |
|---|---|
| `python3 tools/check-gate-battery.py --selftest` (×2) | **exit 0; `SELFTEST OK 28/28 controls behaved as expected`**; the two runs are byte-identical (`.scratch/d16/selftest-final-{1,2}.txt`, stdout sha256 `8b1fdd6f2d316ef20ac3ebe23695a81626358084dd8535816116fd71a3fd9e28`) |
| full battery, committed roots (`tools/gates/frozen`, `tools/gates/expected`, `reports/round-9/baselines` — `run-validation.py:BATTERY_ROOT_CANDIDATES`) | **exit 0**; `{pass: 7, fail: 0, unevaluable: 0}`, top-level findings `[]`; 8/8 baselines `pinned`; 7/7 gates covered (`.scratch/d16/battery-final-3root.json`) |
| full battery, default roots (`tools/gates/expected`, `tools/gates/frozen`) | exit 2 — the **filed standing coverage reading**, unchanged: 5/5 baselines `pinned`, `gates_uncovered [myth-consistency-gate.py, naming-collision-gate.py]`; top-level `{pass: 7, fail: 0, unevaluable: 0, findings: []}`; originals preserved, 28 files hashed before/after, 0 modified/added/deleted (`.scratch/d16/battery-final.json`) |

The wiring did not touch anything the battery scans: the seven gate scripts are byte-identical to their pre-wiring hashes, `tools/gates/fixtures/**` is byte-identical, and `tools/check-gate-battery.py` still hashes `0a126b70afa6cbd5c2565b57399c318788540e10c4940d07c906718c8b9e1aa1` (the round-9 record). In-flight interactions were measured and are reported in §5 (the first self-resolved before the final stamp; none blocks the acceptance).

## 1. What this shard checks, and what it does not

- Acceptance form: `reports/round-11/depth/capability-draft.md` §3 c6 and `scribe.md` §1.1 fix "battery remains green" as `python3 tools/check-gate-battery.py --selftest` exit 0; `design.md` §5.4 fixes the full-run reading as "same five pins verifying, `pass: 7`, `fail: 0`" with the exit-2 coverage gap named.
- The battery has two duties and both are measured here: (1) 28 isolated selftest controls on synthetic children (no live path); (2) seven live gate selftests in a disposable mirror plus committed-baseline digest/pin validation — read-only, never re-executing a baseline verdict (`tools/check-gate-battery.py:1-79`).
- It does **not** execute the wired flow (`tools/typed-gate-flow.py` is not one of the battery's seven-name constant `GATE_NAMES`, `tools/check-gate-battery.py:92-100`), and it never re-runs a baseline's gate; the verdict half of a baseline is its own re-run record (the battery prints `verdict_replay: "not-run"`).

## 2. Pre-wiring receipts (before any wiring byte landed)

| leg | command | result |
|---|---|---|
| selftest ×2 | `python3 tools/check-gate-battery.py --selftest` | exit 0; 28/28; runs byte-identical (`.scratch/d16/selftest-pre-{1,2}.txt`) |
| default roots | `python3 tools/check-gate-battery.py` | exit 2; `{battery_exit: 2, pass: 7, fail: 0, unevaluable: 0}`, top-level findings `[]`; 5/5 pinned; uncovered `[myth, naming]` (`.scratch/d16/battery-pre.json`) |
| committed roots | same + 3 × `--baselines-root` (`tools/gates/expected`, `tools/gates/frozen`, `reports/round-9/baselines`) | exit 0; 8/8 pinned; 7/7 covered; findings `[]` (`.scratch/d16/battery-pre-3root.json`) |
| tool hash | `sha256sum tools/check-gate-battery.py` | `0a126b70…` |
| gate pins | all 8 baseline records read `pinned`; every `gate_sha256` matches the live gate byte | recorded in `.scratch/d16/battery-pre-3root.json` |

## 3. Post-wiring receipts

Final stamp **2026-10-17T22:15:21–24Z**; the wired artifacts' stamps are 19:11–19:13 local (22:11–22:13Z), i.e. they were on disk before every reading below.

| leg | command | result |
|---|---|---|
| selftest ×2 | `python3 tools/check-gate-battery.py --selftest` | exit 0; `SELFTEST OK 28/28`; byte-identical runs; stdout sha256 `8b1fdd6f…` — **equal to the full 64-hex `output_sha256` recorded in round-10's ledger rows 100/106/112/122/161** (`reports/round-10/drift/ledger.json`, `"28/28 controls"`), i.e. the battery selftest output is byte-stable across the wiring |
| default roots | `python3 tools/check-gate-battery.py` | exit 2 (standing); top-level findings `[]`; 5/5 pinned; uncovered `[myth, naming]`; originals preserved (28 files, 0 modified/added/deleted). Field-for-field equal to round-10 ledger row 65's note ("duty1 pass 7/fail 0/unevaluable 0, originals preserved; duty2 baseline_exit 2 (5/7 covered)") |
| committed roots | 3 × `--baselines-root` as above | **exit 0**; summary `{battery_exit: 0, pass: 7, fail: 0, unevaluable: 0}`; 8/8 pinned; 7/7 covered; every gate `outcome=pass, observed_exit=0`. Equal to round-10 ledger row 66's note ("7/7 gates covered, pass 7/fail 0/unevaluable 0") |
| all seven gate selftests | inside the battery mirror | `costume-era`, `handoff-packet-check`, `lexicon-coverage`, `myth-consistency`, `naming-collision`, `phonology-sanity`, `provenance-audit` — all `pass`, exit 0 |
| battery tool | `sha256sum tools/check-gate-battery.py` | `0a126b70afa6cbd5c2565b57399c318788540e10c4940d07c906718c8b9e1aa1` — unchanged |
| seven gate scripts | `sha256sum tools/gates/*.py` vs pre | byte-identical, e.g. phonology `d5fe087f…`, naming `d9e4e8f4…`, handoff `e2fa3223…`, provenance `8a96aaf4…` |
| fixtures | `find tools/gates/fixtures -type f \| xargs sha256sum` vs pre | byte-identical (21 files) |

Companion c6 legs (same stamp, `.scratch/d16/typed-*`): `tools/typed-gate-flow.py --selftest` 14/14 exit 0 and `--check` exit 0; `tools/d2-typed-labels.py --selftest` 39/39 exit 0; `tools/assemble-d2.py --selftest` 42/42, `--check` exit 0; `tools/assemble-culture-d3.py --selftest` 85/85, `--check` exit 0 (both artifacts); `tools/replay-frozen.py --selftest` 79/79.

## 4. What changed under the battery's scope — nothing; what the wiring changed, and where it sits

The wiring's landed artifact set, and why the battery is insensitive to it:

| artifact | sha256 (as read 22:15Z) | battery scans it? |
|---|---|---|
| `tools/typed-gate-flow.py` (the wiring's adapter/gate flow, R11-D05) | `ae55e6fa423d6d6a2574933d75402cafcba3f77e25164755eaf159da838a77d2` | no — not in `GATE_NAMES`, not under `gates/fixtures` |
| `examples/culture-d2/typed-gate.expected.json` (expected hold set) | `e962849a2cb13989e41c26677693cefd11d7072c28c0f758f8ab9d24ed6344e8` | no — outside both baseline roots |
| `examples/culture-d2/packet.d2.typed.yml` (derived typed packet) | `e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb` | no |
| `examples/culture-d2/typed-labels.d2.yml` (re-pinned projection) | `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` (= design §5.1's predicted re-pin hash) | no |
| `tools/gates/frozen/round-11/MANIFEST.tsv` (10-row replay generation) + `inputs/` + `*.out` | manifest `4ddb911c…`, 10 rows | no — the battery discovers only `expected.json` / `*.expected.json` under the two default roots (`tools/check-gate-battery.py:388-395`), and this generation carries none |

Consequently the battery's own pre/post diff **is empty**: no gate script, no fixture file, no scanned baseline was added, removed or modified by the wiring. The design's planned `tools/gates/expected/typed-pipeline/r11/expected.json` did not land in that layout; the round-11 generation was committed as the TSV manifest under `tools/gates/frozen/round-11/`, which the battery does not scan (see §5 F2 for the control that shows what would have happened).

Repeat check: an additional run pair at 22:16:30Z reads identically — both full-battery runs are field-for-field equal to the 22:15 runs (summary, per-gate outcomes/findings, originals, baselines summary, baseline findings) once the random mirror path is normalized; the only byte differences are the mirror path strings the child gates echo in their stdout (`.scratch/d16/battery-confirm{,-3root}.json`).

## 5. Interaction findings (for the round; none blocks the D16 acceptance)

**F1 — the O-claim's freeze briefly degraded the battery reading; it moved out of the scanned roots (self-resolved).**
At 22:10–22:11Z `tools/gates/expected/handoff-exercise/r11/expected.json` existed (O-claim freeze, foreign schema: no `gate`, no `expected` block, `inputs` pointing at repo-root paths). The battery discovered it and refused it — 3-root run read **exit 2** with 7 new findings: `BASELINE-GATE-UNKNOWN`, 5 × `BASELINE-EXTERNAL-INPUT`, `BASELINE-EXPECTED-ABSENT` (`.scratch/d16/battery-mid-3root.json`, 22:11Z). By 22:13:31Z the O shard's freeze lived at `reports/round-11/handoff/expected.json` (outside every scanned root) and the 3-root reading returned to exit 0 (22:14:06Z and 22:15:24Z runs). D08's `repin.md` §0 records the same mid-flight observation independently.
Adjacent receipt: `reports/round-11/validation.json` (X03, stamp 22:09:44Z) still carries the degraded reading in its battery leg (`baselines_found 9, pinned 8, no baseline 1`, battery exit 2). At 22:15 the same command set reads 8/8 pinned, exit 0 — the counting command's battery leg should be re-run on the settled tree before admission. Not this seat's file; reported, not absorbed.

**F2 — fail-closed boundary, measured control: any `expected.json` for a gate outside the seven-name constant under a scanned root reads `BASELINE-GATE-UNKNOWN`.**
Synthetic control (scratch only, 22:03Z): a `kotodama-frozen-run-v1` spec with `gate: typed-pipeline-gate` under a scratch `expected/typed-pipeline/r11/` was fed to the battery's own `inspect_baselines` (`runpy` load of the live tool) → `readings {'no baseline': 1}`, `baseline_exit 2`, finding `BASELINE-GATE-UNKNOWN: declared gate 'typed-pipeline-gate' is not one of the seven registered gates`. This is the battery working as designed (it never vouches for a baseline it cannot map to a registered gate); it also means a future freeze that commits a standard-schema `expected.json` for the typed gate under `tools/gates/expected/**` will add this finding to the battery's baseline duty. The landed layout avoids it; the boundary is named so a future re-placement is a decision, not an accident.

**F3 — what the selftest green does and does not prove.**
`--selftest` runs 28 controls on synthetic children in temp trees — it proves the battery's classification/mapping logic (including baseline tamper, revision, unpinned, unknown-gate, path-escape controls) is intact post-wiring; it is by construction insensitive to the wiring. The wiring-sensitivity of this shard comes from (a) the full battery run over the live seven gates and the committed pins, and (b) the c6 companion selftests (§3). Both read green post-wiring.

**F4 — byte-stability boundary (pre-existing, filed).**
The full battery's stdout embeds the random mirror path (`mirror.root … .scratch/gate-battery-<random>`), so raw stdout hashes are path-dependent by construction (round-10 `drift/audit.md` §2 note); stability is read from the summary/outcome fields, as this report does. The `--selftest` stdout has no such path and is byte-stable — `8b1fdd6f…` matches round-10's full recorded hash (§3).

## 6. Limits

1. One tree, one host, one stamp window: every reading names its command and stamp; a later tree (e.g. a re-landed baseline under a scanned root) is a new measurement, not a continuation. The final stamps are 22:15:21–24Z; the wired artifacts were on disk since 22:11–22:13Z.
2. The full battery run verifies digests and pins only; it does not re-execute any recorded baseline verdict (`verdict_replay: "not-run"` in both receipts) — that comparison belongs to each baseline's own re-run record.
3. The battery's originals-preservation check proves byte equality of the 28 files it snapshots (7 scripts + 21 fixture files), not absence of writes (a rewrite with identical bytes would pass — the tool's own docstring, `tools/check-gate-battery.py:11-14`).
4. `check-gate-battery.py` was not edited by this seat or by the wiring (hash unchanged); the round-9 constants (`GATE_NAMES`, the seven-name scope) are deliberately untouched, so any claim that the battery "covers" the typed pipeline gate would be false — the battery covers the seven registered gates and the committed §3 baselines only.
5. Receipts referenced above live under `.scratch/d16/` (gitignored scratch): `selftest-{pre,final}-*.txt`, `battery-{pre,mid,final}*.json`, `gates-post.txt`, `fixtures-{pre,post}.txt`, `typed-*`. Every scratch-writing command ran with `export TMPDIR=$PWD/.scratch`.
