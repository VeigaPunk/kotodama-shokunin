# R18-D26 — run logs: every command this seat ran (round 18, pre-state + landings)

- round: 18 (operator loop 2 of 3, build round 2 of 4) · seat **R18-D26**
  (run logs) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "D R18-D21..D28 (scribes+docs x8): frozen-manifest
  records; fragment ledger; capability drafts; ASSEMBLY.md/README updates for
  culture-d4 (new files only); docs; run logs; disposition drafts; spot-check
  ledger. reports/round-18/d4/scribe-{1..8}.md."
- date: 2026-10-18 · reference revision `c66ac3c951b346a2a56f9386e3324b4f5fe33902`
  · window 10:19:55Z–10:31Z · `export TMPDIR=$PWD/.scratch` before every run.
- canon: NON-CANON. A log, not an acceptance: red stays red, green says only
  "reproduced/expected".
- writes: **this file only** + `.scratch/r18d21/`. No commit, no push.

## 0. Reading guide

Every row is one command, its exit code, its observed output (excerpt), and
its receipt where one was kept. "Pre" = before any round-18 worker artifact
could affect the reading (the generalized gate never landed inside this
window: poll T1–T6 all read `typed-pipeline-gate.py d102fd1dd1bae3cc…`).

## 1. Baseline regressions (all green, pre-generalization)

| # | command | exit | observed | stamp / receipt |
|---|---|---:|---|---|
| 1 | `python3 tools/gates/typed-pipeline-gate.py` | 0 | `summary: 16/16 legs passed`, 15 `FINDING` + 1 `NOTE` lines, 10 `PHON artifact(s) retired` | 10:20Z |
| 2 | `python3 tools/gates/typed-pipeline-gate.py --json` | 0 | JSON keys incl. `checks` (16), `counts`, `routing`, `pins`, `typed_packet` | 10:26Z |
| 3 | `python3 tools/gates/typed-pipeline-gate.py --selftest` | 0 | `selftest: 12/12 checks passed — constant==baseline, the mirrored four legs, determinism/--json, and the smuggled-label, dropped-row, laundered-hold, adapter-drift, malformed and missing controls` | 10:30Z |
| 4 | `python3 tools/d2-typed-labels.py --selftest` | 0 | `selftest: 39/39 checks passed` | 10:30Z |
| 5 | `python3 tools/assemble-d2.py --check` | 0 | `packet.d2.yml: byte-identical deterministic assembly` | 10:29Z |
| 6 | `python3 tools/assemble-culture-d3.py --check` | 0 | `packet.json: …; packet.gates.yml: byte-identical deterministic assembly` | 10:29Z |
| 7 | `python3 tools/assemble-culture-d4.py --check` | 0 | `packet.d4.yml: byte-identical deterministic assembly` | 10:20Z |
| 8 | `python3 tools/assemble-culture-d4.py --selftest` | 0 | `selftest: 81/81 checks passed` | 10:22Z |
| 9 | `python3 tools/check-gate-battery.py` | 0 | `summary: {battery_exit: 0, pass: 7, fail: 0, unevaluable: 0}`; mirror `files_hashed_before 28, modified 0, preserved true` | 10:29Z |
| 10 | `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json --counts` | 0 | counts block (`verdict_supported 5`, `verdict_unresolved 2`, `verdict_contradicted 0`) | 10:29Z |
| 11 | `python3 tools/check-craft-exercise.py --selftest <exercise>` | 0 | `SELFTEST OK 10/10 tamper cases detected` + `CLI-SELFTEST OK 18/18 cases passed` | 10:29Z |
| 12 | `python3 tools/gates/d4-typed-labels-check-gate.py` | 0 | `examples/culture-d4/typed-labels.d4.yml: byte-identical deterministic projection` | 10:26Z |
| 13 | `python3 tools/gates/d4-assembly-check-gate.py` | 0 | `examples/culture-d4/packet.d4.yml: byte-identical deterministic assembly` | 10:26Z |

## 2. The D2-bound boundary (reproduced at the round-18 baseline)

| # | command | exit | observed | stamp |
|---|---|---:|---|---|
| 14 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 2 | `FAIL L1-assembler_identity: packet bytes are not assemble-d2.py's deterministic assembly (e7ecd2045ef0 vs e0f21509e14a)` then `FAIL L1-build: …` — receipt `.scratch/r18d21/gate-d4-reject.out` | 10:20Z |
| 15 | `python3 tools/assemble-d2-typed.py --packet examples/culture-d4/packet.d4.yml --projection examples/culture-d4/typed-labels.d4.yml --emit .scratch/r18d21/packet.d4.typed.yml` | 2 | `FAIL assembler_identity: … (e7ecd2045ef0 vs e0f21509e14a)`; no emit file written — receipt `.scratch/r18d21/adapter-d4.out` | 10:21Z |

Both readings are the round-17 rejection *before*-state, quoted by the O/D
families; the pair also shows the boundary lives on **two** surfaces (gate
leg and adapter), not one.

## 3. D4 projection and expected set

| # | command | exit | observed | stamp |
|---|---|---:|---|---|
| 16 | `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json` | 1 | `stats {"fail": 0, "hold": 15, "labels": 74, "note": 1}`, 16 finding rows — receipt `.scratch/r18d21/proj-d4.json` | 10:20Z |
| 17 | `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | 0 | `byte-identical deterministic projection` | 10:20Z |
| 18 | set-equality of `examples/culture-d4/expected-holds.json` (landed 10:24:55Z) vs the fresh projector rows, keyed `(id, severity, where, detail)` | — | `exp rows 16 / proj rows 16`; `equal: True`; `exp-not-proj: []`, `proj-not-exp: []`; counts `{hold: 15, note: 1, fail: 0}`; pins equal live bytes for packet/projection/projector | 10:29Z |

## 4. Legacy gates over the live D4 packet (interop; exits must be in {0,1})

| # | command | exit | findings | note | stamp |
|---|---|---:|---:|---|---|
| 19 | `python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml` | 1 | 14 | 7 `NAME-NEAR` (NM-05/PAN-01 + six `era#n` grapheme pairs) + 6 `PHON-INVENTORY` (`GAR-01..06` glosses) + 1 `CROSS-HOLD` | 10:22Z |
| 20 | same over `reports/round-17/tests/frozen/packet.d4.yml` (pre-normalization copy) | 1 | **8** | the 6-finding delta is packet-driven (eras normalization), not gate-side | 10:28Z |
| 21 | `python3 tools/gates/phonology-sanity-gate.py examples/culture-d4/packet.d4.yml` | 1 | 1 | `A-CLASS` REVIEW (`s → z / V _ V` natural class needs finite expansion) | 10:22Z |
| 22–24 | costume / lexicon / myth over the same packet | 0 | 0 each | no exit 2, no traceback in any of the five | 10:22Z |

## 5. Frozen replays (TMPDIR outside the repo; `replay-frozen.py` refuses in-repo mirrors)

| # | command | exit | observed | stamp |
|---|---|---:|---|---|
| 25 | `TMPDIR=/var/tmp/kotodama-r18d21 python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` | 0 | `REPLAY OK: 11/11 rows reproduced the recorded verdicts` | 10:22Z |
| 26 | same over `reports/round-17/tests/frozen/MANIFEST.tsv` | 0 | `REPLAY OK: 5/5 rows reproduced` | 10:22Z |
| 27 | same over `tools/gates/frozen/round-3/MANIFEST.tsv` | 2 | `7 could-not-evaluate … on-disk bytes are not the pinned revision` | 10:28Z |
| 28 | same over `tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` | 2 | same class | 10:28Z |
| 29 | same over `tools/gates/frozen/round-4/MANIFEST.tsv` | 2 | `manifest_unreadable` | 10:28Z |

## 6. Cross-round and runner readings

| # | command | exit | observed | stamp |
|---|---|---:|---|---|
| 30 | `git status --porcelain` (whole lane) | 0 | empty at 10:19:55Z and 10:22:33Z; at 10:29Z it lists only the wave's new files (untracked: `examples/culture-d4/expected-holds.json`, `tools/gates/d4-*.py`, `reports/round-18/**`, `corpus/lessons/round-18.md`) | 10:19Z / 10:29Z |
| 31 | `git status --porcelain -- reports/round-8 … reports/round-17` | 0 | 0 lines; `git diff --stat HEAD -- <same>` → 0 lines; `git ls-files <same> \| wc -l` → 761 | 10:30Z |
| 32 | `python3 reports/round-17/run-validation.py --check` (read-only) | 1 | `acceptance_checks_passed: false`, `missing_dependencies: ["examples/culture-d4/typed"]` — the D4 typed packet is the single remaining r17-D gap — receipt `.scratch/r18d21/r17runner-check.json` | 10:29Z |
| 33 | `python3 tools/replay-frozen.py --selftest` | — | not re-run by this seat (round-17 receipt: 79/79, `reports/round-17/tests/replay.md` §2 row 3) | — |

## 7. Pin reads used by the other scribes

`sha256sum` at 10:19:55Z: `typed-pipeline-gate.py d102fd1d…`, `d2-typed-labels.py
0da0015f…`, `assemble-d2-typed.py c7e5a749…`, `assemble-d2.py 8ea6bdde…`,
`examples/culture-d2/expected-holds.json a5dc26d5…`, `packet.d2.typed.yml
1b5010b7…`, D4 `packet.d4.yml e7ecd204…`, `typed-labels.d4.yml a59990bb…`,
`assemble-culture-d4.py 943f487b…`. At 10:26Z: `d4-typed-labels-check-gate.py
05f99629…`, `d4-assembly-check-gate.py df1a364b…`. At 10:25Z:
`expected-holds.json 09490a27…`, `ASSEMBLY.md 37b6a989…`, `README.md
ba69a2b6…`. At 10:26Z: `reports/round-18/scope.md 451428d8…`,
`reports/round-18/gate/tests-1.md 8dab351f…`, `corpus/lessons/round-18.md
f8f4e639…`.

## 8. Negative results and non-readings (explicit)

- No command of this seat ran with `TMPDIR` inside the repo where
  `replay-frozen.py` was the child (it refuses in-repo mirrors by design; the
  five replays in §5 used `/var/tmp/kotodama-r18d21`).
- No D4 typed-packet run was possible: `examples/culture-d4/packet.d4.typed.yml`
  absent at every stamp (negative claim; sweep `ls examples/culture-d4/` +
  poll log `.scratch/r18d21/poll.log`, T1–T6).
- The generalized gate was never observed: every poll read
  `gate=d102fd1dd1bae3cc…`. Any claim about its behavior on the D4 path is
  therefore outside this log; the family's own receipts carry it.
- `python3 reports/round-18/run-validation.py` landed 10:28Z but was **not**
  run by this seat at its last stamp (a runner can itself be a writer; the
  parent owns the receipt).

## 9. Reproduction

```sh
export TMPDIR=$PWD/.scratch
python3 tools/gates/typed-pipeline-gate.py                     # exit 0, 16/16 legs (pre-generalization bytes)
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml   # exit 2 (before-state)
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json | head -20
TMPDIR=/var/tmp/kotodama-r18d21 python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv
```

## 10. Post-state run log — after the generalization landed (10:34–10:37Z)

Appended after §1–§9; same method, same TMPDIR discipline. The gate revision
moved four times between 10:29:55Z and 10:33:55Z and then held at
`d4785d9afc0306afb0a9c78c3c2b014097090413bf9c889ed72fa9558c394ba0` (poll rows
10:33:55Z onward, `.scratch/r18d21/poll.log`).

| # | command | exit | observed | receipt / stamp |
|---|---|---:|---|---|
| 34 | `sha256sum tools/gates/typed-pipeline-gate.py` (sequence) | — | `d102fd1d…` → `bba60bc18ebc1282…` → `edfec5f37a511e09…` → `d09f7c3b0cb83742…` → `3897833101be9c3a…` → **`d4785d9a…`** | poll log; 10:29:55–10:33:55Z |
| 35 | `python3 tools/gates/typed-pipeline-gate.py` | 0 | `summary: 16/16 legs passed`; stdout `15cdfbda73cd56cb6107…` — identical to the pre-change digest | `.scratch/r18d21/gate-default-after.out`, 10:36Z |
| 36 | `python3 tools/gates/typed-pipeline-gate.py --help` | 0 | `[-h] [--json] [--selftest] [packet]` — no `--assembler`/`--projection`/`--expected` flags at this revision | 10:36Z |
| 37 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 2 | `ok L1-assembler`, `ok L1-expected-holds`, `FAIL L1-build: adapter missing: tools/assemble-d4-typed.py`; 0 FINDING/NOTE lines | `.scratch/r18d21/gate-d4-after.out`, 10:37Z |
| 38 | `TMPDIR=/var/tmp/kotodama-r18d21 python3 tools/replay-frozen.py tools/gates/frozen/round-18-repin/MANIFEST.tsv` | **2** | `1 could-not-evaluate, 0 mismatch, 10 reproduced of 11`; row for `tools/gates/typed-pipeline-gate.py` reads `gate_digest_mismatch` (pinned `5b4501a9…` vs live `d4785d9a…`); rows 3–12 (`bytes=match launched=yes`) | 10:36Z |
| 39 | `python3 tools/check-gate-battery.py` (over the enlarged baseline surface) | 0 | `{battery_exit: 0, pass: 7, fail: 0, unevaluable: 0}` | 10:32Z |
| 40 | `git show 3dd3754:<path> \| sha256sum` vs live, four surfaces | — | only the gate changed (`d102fd1d…` → `d4785d9a…`); adapter, projector, serializer unchanged | 10:36Z |
| 41 | `git status --porcelain -- reports/round-9` | 0 | empty — the r18-post cascade left the round-9 baseline bytes alone | 10:31Z |
| 42 | `ls tools/gates/frozen` | — | new: `round-18-repin/`, and `r18-post` ids under 7 gate homes (including new homes for myth and naming) | 10:33Z |

Reading of rows 35–37: the default D2 path is unchanged byte-for-byte at the
stdout level (row 35's digest equals the pre-change run and the D01/D02
fragment's reading), while the D4 path advanced from the assembler-identity
refusal (row 14) to a missing-adapter build failure (row 37) — i.e. the
declared-pin leg works, the D4 adapter has not landed.

Row 38 is the one red post-state reading: the round-18 frozen generation does
not replay green because its gate pin predates the live gate bytes. It is
reported, not repaired (this seat writes only its own files).

Still not runnable at close: any D4 typed-packet run (`packet.d4.typed.yml`
absent), `reports/round-18/run-validation.py` (present at 10:28Z, left to the
parent — a runner can itself be a writer). Poll rows after 10:33:55Z continue
in `.scratch/r18d21/poll.log`.
