# Round 12 O19–O20 regression verification

Tested the current checkout at `69d0c2191628c1396a85aea2fd7408f2d1bba08e` (`git rev-parse HEAD`, 2026-10-17T19:38:22-03:00). `git status --short` was empty before this evidence file was created. Before each scratch-capable command, exported `TMPDIR="$PWD/.scratch"` and created that directory. Dates below are the `date -Iseconds` output immediately preceding each command; all runs were on 2026-10-17 in the local `-03:00` timezone.

## Selftests

- `python3 tools/check-gate-battery.py --selftest` — 2026-10-17T19:37:23-03:00; exit 0, `SELFTEST OK 28/28 controls behaved as expected`.
- `python3 tools/check-craft-exercise.py --selftest` — 2026-10-17T19:37:24-03:00; exit 0, `SELFTEST OK 10/10 tamper cases detected` and `CLI-SELFTEST OK 18/18 cases passed`.
- `python3 tools/d2-typed-labels.py --selftest` — 2026-10-17T19:37:24-03:00; exit 0, `selftest: 39/39 checks passed`; output states no file outside its temporary directory was touched.
- `python3 tools/assemble-d2.py --selftest` — 2026-10-17T19:37:25-03:00; exit 0, `selftest: 42/42 checks passed`; output states no file outside its temporary directory was touched.
- `python3 tools/assemble-culture-d3.py --selftest` — 2026-10-17T19:37:25-03:00; exit 0, `selftest: 85/85 checks passed`; real naming and costume gates ran read-only, and output states no file outside its temporary directory was touched.

## Actual runner and committed-output checks

- `python3 tools/check-gate-battery.py --baselines-root "$PWD/tools/gates/expected" --baselines-root "$PWD/tools/gates/frozen" --baselines-root "$PWD/reports/round-9/baselines"` — 2026-10-17T19:38:06-03:00; exit 0, battery summary `pass: 7`, `fail: 0`, `unevaluable: 0`; baseline summary `baselines_found: 8`, `pinned: 8`, `gates_uncovered: []`. The runner reports `added: 0`, `deleted: 0`, `modified: 0`, and `files_hashed_before: 28` / `files_hashed_after: 28`. Its output explicitly says verdict replay was not run: this battery checks gate selftest exits and baseline digests/pins, not baseline verdict replay.
- `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` — 2026-10-17T19:38:06-03:00; exit 0, `OK all checks passed (audits=7, mech_cases=11, derivations=9, approx_checks_runner=37)`.
- `python3 tools/d2-typed-labels.py --check` — 2026-10-17T19:38:06-03:00; exit 0, typed-label projection byte-identical.
- `python3 tools/assemble-d2.py --check` — 2026-10-17T19:38:06-03:00; exit 0, D2 packet byte-identical to deterministic assembly.
- `python3 tools/assemble-culture-d3.py --check` — 2026-10-17T19:38:06-03:00; exit 0, both D3 `packet.json` and `packet.gates.yml` byte-identical to deterministic assembly.

**Result:** all requested selftests passed on the recorded checkout; the actual isolated battery and craft positive call also passed, and all checked generated projections were byte-identical. No implementation or filed round-8–11 artifact was changed by this runner; this worker wrote only this assigned evidence file.
