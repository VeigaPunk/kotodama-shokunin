# R18-D16 — interop 3/3: battery, frozen replay, and the generalization-window boundary

- round 18 (operator: loop 2 of 3, build round 2 of 4; `reports/round-18/claims.json`,
  claim **D**, shard **D16**). Lane: `kotodama-shokunin`.
- assignment (verbatim): "D R18-D14..D16 (interop x3): D2 path (typed gate on D2
  packet) verdict identical to round-11's recorded verdict; d2/d3 assemblers
  --check green; battery green; reports/round-18/d4/interop-{1..3}.md."
- date: 2026-10-18. Evidence window 10:21:00Z–10:29:00Z UTC (+ the 60 s poll
  through 10:41Z). Reference revision HEAD
  `c66ac3c951b346a2a56f9386e3324b4f5fe33902`. Baseline `3dd37542…` (round-17).
- canon: NON-CANON engineering evidence.
- writes: **this file only** plus gitignored scratch under `.scratch/r18interop*`;
  one documented TMPDIR exception for the replay (§2). No earlier-round byte
  edited; no commit, no push.

## 0. Verdict

**GREEN — the battery exits 0 with all seven gate selftests passing, 8/8
committed baselines pinned and 0 uncovered; the round-11 frozen generation
replays 11/11 rows.** The generalization named by claim O had **not landed** in
this window (gate sha unchanged at `d102fd1d…` through 10:29Z); the boundary and
the exact re-run recipe are §3/§4.

## 1. Gate battery — `python3 tools/check-gate-battery.py`

Run 2026-10-18 10:21:00Z, repo root, `TMPDIR=$PWD/.scratch/r18interop-batt`,
exit **0**; JSON report (`.scratch/r18interop/battery.json`) fields:

| field | observed | r11/r14/r15 reference |
|---|---|---|
| `summary` | `{battery_exit 0, pass 7, fail 0, unevaluable 0}` | r11 `validation.json` D battery run: `baseline_exit 0`; r14 `default_battery`: `gate_selftests_passed 7, failed 0` |
| `gates` (7 entries) | costume-era, handoff-packet-check, lexicon-coverage-audit, myth-consistency, naming-collision, phonology-sanity, provenance-audit — all `outcome pass`, `observed_exit 0`, no findings | same seven |
| `originals` | `{preserved true, files_hashed_before 28, files_hashed_after 28, modified 0, added 0, deleted 0}` | r14 `originals_preserved true` |
| `baselines.summary` | `{baselines_found 8, pinned 8, readings {pinned 8}, unevaluable 0, gates_uncovered [], baseline_exit 0}`; roots `tools/gates/expected` (2 files), `tools/gates/frozen` (3), `reports/round-9/baselines` (3) | r11 D battery `baseline_summary`: `found 8, pinned 8, uncovered [], unevaluable 0`; r14/r15 same |
| `findings` | `[]` | r14/r15 same |
| `mirror` | `{removed: true}` | — |

The battery's stdout is **not byte-stable run-to-run** (the JSON embeds the
disposable mirror path): this run `0d2d1450…`, an earlier run in the same window
`bddd432e…`, r14 `7b1485cb…`, r15 `12f7947b…` — consistent with
`reports/round-15/rerun.json` `battery_stdout_stability_probe`. The stable
contract is exit + JSON summary, both green. The battery's own selftest
(`--selftest`) exits 0 with stdout sha `2812a327…`, byte-equal to r14/r15.

Risk to watch (not a finding of this round): the battery discovers every
`expected.json` under its three roots and fails closed on a gate outside its
seven-name constant (`BASELINE-GATE-UNKNOWN`, r11 `review-20.md`). Round-18
workers are adding new gate scripts under `tools/gates/` (`d4-assembly-check-gate.py`,
`d4-typed-labels-check-gate.py`, seen untracked at 10:26Z). If any `expected.json`
naming those lands under the battery roots, the standing battery will move to
exit 2 by design. Re-run this command after the wave settles.

## 2. Round-11 frozen generation replay

```sh
mkdir -p /var/tmp/kotodama-r18-interop
TMPDIR=/var/tmp/kotodama-r18-interop python3 tools/replay-frozen.py \
    tools/gates/frozen/round-11/MANIFEST.tsv
# exit 0 — REPLAY OK: 11/11 rows reproduced the recorded verdicts
# (reproduction only: a reproduced red verdict stays red)
```

stdout sha256 `9e656e9e06bbcdb9e05eb81748f177ab015fbb3479cc8939196e78478e641cb8`
(2026-10-18 10:21Z). Rows 2 and 7 reproduce their red verdicts (`exit 1`,
naming 7 / phonology 3 / naming 17) exactly as recorded — reproduction, not
clearance, per the tool's own rule. Row 1 (`typed-pipeline-gate.py` over the
frozen typed packet) reproduced byte-identically; the direct comparison is in
`interop-1.md` §0.

**TMPDIR deviation, recorded deliberately:** the lane rule "export
TMPDIR=$PWD/.scratch before scratch-writing commands" cannot be honoured here —
`tools/replay-frozen.py` refuses a temp root inside the repo
(`mirror_unsafe`, `tools/replay-frozen.py:177`) and
`tools/gates/frozen/round-11/README.md` documents exactly this
(`mkdir -p /var/tmp/kotodama-r11`). The tool's guard wins; the mirror is
self-cleaning and outside the repo. Every other scratch write in this set went
through `.scratch/`.

## 3. Window boundary — the generalization had not landed

The claim-O target file `tools/gates/typed-pipeline-gate.py` was polled every
60 s from 10:22:16Z with sha + mtime + the appearance of claim-D artifacts
(`.scratch/r18interop/watch.log`):

```
10:22:16Z gate=d102fd1d…68e27d mtime=1792276009 d4-exp=none r18-manifest=none head=c66ac3c
10:23:16Z … (identical)
10:24:16Z … (identical)
10:25:16Z … d4-exp=09490a2756d123ebbc2023be89fc01c95ec2f8cc7e6df42ecc5b8cd438058e98
10:26:16Z … d4-exp=09490a27… head=c66ac3c
```

`d102fd1d…68e27d` is the round-11 freeze value
(`tools/gates/frozen/round-11/typed-pipeline/run-receipt.json` `gate_sha256`);
it is unchanged at every poll — so every check in this set (and in
`interop-1.md`/`interop-2.md`) was taken **before** the generalization, on the
D2-bound gate. What appeared during the window from other seats:
`examples/culture-d4/expected-holds.json` (10:24Z, untracked),
`reports/round-18/gate/tests-1.md`, `reports/round-18/scope.md`,
`reports/round-18/civ-map-r18.json`, `tools/gates/d4-*-check-gate.py`. Those
files are not this seat's writes and were not touched.

Kept as the pre-generalization baseline for the O seats: the D4 packet
(`examples/culture-d4/packet.d4.yml`, sha `e7ecd2045ef0…`) under this gate exits
**2** with
`FAIL L1-assembler_identity: packet bytes are not assemble-d2.py's deterministic
assembly (e7ecd2045ef0 vs e0f21509e14a)` — the round-17 rejection, now
byte-captured (`interop-1.md` §3 control C). The generalized gate is expected
to clear this by a declared assembler pin; the D2 path must simultaneously still
show the §0 table of `interop-1.md` unchanged.

## 4. Re-run recipe (post-generalization re-verification, for the parent / O seats)

```sh
# 1. D2 default path — must stay: exit 0, 15 FINDING + 1 NOTE, 16/16 legs
python3 tools/gates/typed-pipeline-gate.py
# 2. byte pin — must stay: stdout sha256 19765ddf2c36a7db5d71bd262079d6164b24f6222d9df83d0cefdeaeb8f47e62
python3 tools/gates/typed-pipeline-gate.py --json
# 3. frozen row 1 — must stay byte-identical to tools/gates/frozen/round-11/typed-pipeline/run.log
python3 tools/gates/typed-pipeline-gate.py tools/gates/frozen/round-11/typed-pipeline/packet.d2.typed.yml
# 4. assemblers
python3 tools/assemble-d2.py --check && python3 tools/assemble-culture-d3.py --check
# 5. battery + replay
python3 tools/check-gate-battery.py
TMPDIR=/var/tmp/kotodama-r18-interop python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv
```

A dated appended section below records the post-change re-run if the
generalization lands inside this round-18 window.

---

## 5. Post-change window — appended 2026-10-18 (10:29:16Z–10:42:09Z)

Claim O's generalization landed while this seat was still polling. Gate sha
trajectory (60 s poll `.scratch/r18interop/watch.log` + a 30 s settle watch):

```
10:22:16–10:28:16  d102fd1d…  (round-11 freeze, unchanged)
10:29:16  2a08fb2d…   10:30:16  a2948ebb…   10:31:16  edfec5f3…
10:31:50  d09f7c3b…   10:32:16  38978331…   10:33:16  5b4501a9…
10:33:50–10:34:50  d4785d9a…  (stable ≥90 s)
10:35:00  ea95e2a1…   (stable ≥120 s; all re-runs below taken here)
10:39:16  84dc177e…   10:40:16  a201afee…   10:41:16  286d6e82…   (10:42:09 re-checked)
```

Observed in the same window:

1. **D2 path byte-identical at every revision tested** — plain `15cdfbda…`,
   `--json` `19765ddf…`, frozen row 1 `9a69985a…`, `--selftest` 12/12
   (`interop-1.md` §6).
2. **Battery** exit 0; baselines moved 8 → **15 found / 15 pinned / 0
   uncovered** (seven `tools/gates/frozen/*/r18-post/expected.json`, plus
   `expected/*` and `reports/round-9/baselines/*`), `findings []` — the re-pin
   cascade is adding baselines without moving the standing reading.
3. **Round-11 frozen replay: exit 2 — 10 reproduced + 1 could-not-evaluate**
   (`ROW 2 … reason=gate_digest_mismatch… typed-pipeline-gate.py`, bytes
   skipped). This is the append-only rule working as designed: the generation
   pins the round-11 gate revision, the live gate moved on, so the row can only
   be re-pinned by a new generation. Not a regression; the pre-change reading
   was 11/11 (§2).
4. `tools/gates/frozen/round-18-repin/MANIFEST.tsv` (landed 10:33Z, pinning gate
   `5b4501a9…`) replays **exit 2 — 10 + 1 cne**, same reason: by replay time
   (10:37Z) the live gate was already `ea95e2a1…`. Its `typed-pipeline/run.log`
   is byte-identical to round-11's (`9a69985a…`) — the D2 verdict carried
   unchanged into that generation. The pin must be re-taken after the gate
   settles.
5. `tools/gates/frozen/round-18/MANIFEST.tsv` (new, D4 check gates) replays
   **exit 0, 2/2 rows** (`d4-typed-labels-check-gate` 0 findings,
   `d4-assembly-check-gate` 0 findings).
6. **D4 packet** under the generalized gate: exit 2 —
   `ok L1-assembler` + `ok L1-expected-holds` + `FAIL L1-build: adapter missing:
   tools/assemble-d4-typed.py` (file absent at 10:42Z). The D4 arm of claim D
   still needs that adapter to be gradeable.

## 6. Routing notes (for the parent)

- **O seat:** once the gate stops changing, re-take the typed-pipeline row pin in
  the round-18 generation (new generation/row, per the append-only rule) and
  re-run both replays. Expected post-settle: round-11 generation 10 reproduced +
  1 cne (its pin is historical), round-18 generation 11/11.
- **D4 arm:** `tools/assemble-d4-typed.py` must exist and be the adapter the
  generalized gate's `L1-build` declared for the D4 packet; until then a D4 gate
  run reads exit 2 (could-not-evaluate), which is not a hold set and cannot carry
  claim D's "findings == expected hold set".
- **Post-settle gate check (re-run all of these after the wave):** interop-1 §6
  three commands must keep `15cdfbda…` / `19765ddf…` / `9a69985a…`; the §2
  assemblers must keep `2fa0c8c1…` / `e20620fa…`; battery exit 0; round-18
  generation replays 11/11.
