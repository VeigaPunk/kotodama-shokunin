# ExecBattery: round-88 claim O comparator (operability) — scoped findings

Seat: ExecBattery (leaf executor). Axes judged: operability, depth. Claim O only; claim D is not touched.
Milestone: r88-v1. Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin.

## Deliverables (stage only)

| path | sha256 |
|---|---|
| `.ufo/waves/round-88/w1/stage/ExecBattery/check-finding-sets.py` | `4326f1477dc2bb65f1e0a89da505749d23904f122f2adb8f6a73f85fbc00f211` |
| `.ufo/waves/round-88/w1/stage/ExecBattery/usage-fragment.md` | `3887052230b1f13956e2af1033f09c277c0f278ce29129dc535a0cff26319e35` |
| `.ufo/waves/round-88/w1/stage/ExecBattery/receipts/` (COMMANDS.txt, SHA256S.txt, selftest/score/counter/probe outputs) | see `receipts/SHA256S.txt` |

The tool is not committed to `tools/` in the lane. L1 integrates it at lands. No production file, `reports/`, or sibling was written. No commit, push or mutating git was run in the lane. The scratch clone used for the counter probe is scratch-only and is deleted at exit.

## CLI (frozen invocation honoured)

```
check-finding-sets.py --cases PATH --packet PATH --candidate PATH --json --work EXISTING_DIR
check-finding-sets.py --selftest --work EXISTING_DIR
```

- `--json` prints `{"passed","total","cases":[{name,passed,expected_rc,rc,reason}]}`.
- Exit 0 when all cases pass, 1 when some case fails, 2 on input or usage error. Input errors also print JSON with `passed` and `total` at 0.
- Candidates run as `CANDIDATE --packet FILE --json` under `sys.executable -B`, with a 20 s timeout. Scratch is a `TemporaryDirectory` created inside `--work`.
- Opaque filenames are `secrets.token_hex(12).json` per run. No case name appears in any path the candidate sees (probe: 0 matches).
- Exact-set matching: the id set and the `(id, record)` pair set must equal the expected sets. Clean cases require no findings and `records == records_count`. An rc 2 case requires the text `ATTESTATION_ERROR` on stdout or stderr, as the frozen counter does.
- Malformed candidate output (non-JSON, `findings` not a list, finding not an object, non-string id/record, body not an object, crash) fails that case with a reason. It never aborts the run.
- A timeout fails that case and marks the remaining cases "not run", so a hanging candidate costs one timeout (~20 s), not one per case.
- The selftest runs this CLI as a subprocess. It covers the honest auditor, extra-id, shotgun, wrong-record, filename-only, five malformed-output variants, a candidate crash, a hang, a bad cases file, an unknown op, and a missing `--work`.

## Observed results (commands and rc)

Full commands and rc values are in `receipts/COMMANDS.txt`.

- `--selftest --work <scratch>/work` → rc 0, **16/16**.
- Frozen 13-case battery (cases `@4b76524c`, base packet `@4956282`, controls `@0c8c733` read via `git show`):

| candidate | rc | observed | frozen expectation |
|---|---|---|---|
| honest `tools/check-attestation-packet.py` (`@4b76524c`) | 0 | 13/13 | 13 |
| constant-pass | 1 | 3/13 | 3 |
| extra-id | 1 | 4/13 | 4 |
| shotgun-all-labels | 1 | 4/13 | 4 |
| filename-only | 1 | 0/13 | 0 |

- Frozen counter `measure88.py --claim O` on a scratch fixture (clone of 4b76524c plus the stage tool committed in the scratch clone only), `KOTODAMA_ROOT` exported → rc 0, **9/9**. Every leg matches its frozen expectation.
- Counter with `KOTODAMA_ROOT` unset → rc 1, **8/9**; `battery-agrees` observes `[13, 0]` against `[13, 4]`.
- Counter with `KOTODAMA_ROOT` unset, run from the fleet-root cwd → rc 1, **7/9**; `battery-selftest:exit` observes 1 and `battery-agrees` observes `[13, 0]`.

Edge probes (all rc recorded in `receipts/COMMANDS.txt`):
- Missing `--candidate`, absent candidate file, absent `--work`: rc 2 with JSON error.
- Duplicate findings (each finding repeated five times) score **13/13**. Multiplicity is not compared (see defect 2).
- SIGTERM during a hang: the scratch directory is cleaned up. The handler converts SIGTERM to `SystemExit`, so the `TemporaryDirectory` context exits normally.

## Defects and unresolved items

1. **Frozen counter O is environment-dependent (not amended; L1 decision).** `measure88.py` runs the battery subprocesses for `battery-selftest` and `battery-agrees` with the inherited environment. It sets `KOTODAMA_ROOT` only for its own `evaluate` calls. The materialized battery and control wrappers resolve the honest auditor via `KOTODAMA_ROOT` or, failing that, their own parent directories. Materialized into the counter's scratch `work/`, they cannot find `tools/check-attestation-packet.py`. Without the variable, `battery-agrees` observes `[13, 0]` and the O kill rule trips (8/9 and 7/9 above). O reproduces only when `KOTODAMA_ROOT=<lands root>` is exported. Recommend the lands run export it, or that the counter pass it explicitly for every battery invocation. Nothing was changed in the frozen counter.

2. **Control honest-tool resolution reads the worktree, not the committed lands blob.** `measure88.py`'s `evaluate` sets `KOTODAMA_ROOT=ROOT`, the `--root` working tree, so the four control wrappers load `ROOT/tools/check-attestation-packet.py` from the working tree at evaluate time. Claim O's own text says it grades committed bytes at a named revision. For the honest leg the tool is materialized from the lands blob, but the wrappers do not use it. A dirty tracked `tools/check-attestation-packet.py` in the worktree would silently change control scores. The checkout I measured was clean for that path (`git show` at 4b76524c and the worktree sha256 match, `4abcbbd0…`).

3. **Set semantics, not multiplicity (spec-bound limit on "exact").** A candidate that repeats the correct findings five times scores 13/13. The frozen claim and this tool both compare sets. A count check would be a stricter claim; I did not add one because it is outside the frozen predicate. L1 should record this as the bound on O's "exact" wording.

4. **rc 2 uses a text check only (frozen spec).** A candidate that exits 2 and prints `ATTESTATION_ERROR` passes the invalid-json case regardless of its JSON output. The spec names this a text check, so I kept it.

5. **Deliberate divergences from `measure88.py` semantics.** None is exercised by the frozen battery. Honest and all four counterfeits give identical counts under both.
   - `value_from_record` resolves the full dotted path in the source record. The counter uses only the last path component.
   - A clean case requires a `findings` list. A candidate that omits the key fails, where the counter treats it as `[]`.
   - A malformed cases file or unknown mutation op is refused with rc 2. The counter would raise `KeyError`.
   - Names are random per run. The counter derives them from salt plus case name.
   - Timeouts short-circuit the remaining cases.

6. **Lands integration.** The lane has no `tools/check-finding-sets.py`. L1 must copy the stage file to `tools/`, commit it at lands, and then run the counter with `KOTODAMA_ROOT` set. The fixture commit I used (scratch-only) is not a lands revision and is not referenced by any lane ref.

7. **Planner-policy conflict retained.** L1 holds the planner seat. I did not resolve the conflict and did not write any planner artefact.

## Tools and installs

Read `/home/vgpnk/.omp/agent/RULES.md`. No tool was installed or updated. The interpreter was the existing `python3` 3.14.8. No pacman transaction was run, and none is paused by me. Fixture git operations ran only in the scratch clone, after asserting `git rev-parse --show-toplevel` equals the fixture path.

## Scope and host guard

- Writes: stage/ExecBattery/ (tool, usage fragment, receipts) and this report only. Scratch lived under `/fast/scratch/hyaku/kotodama-r88/ExecBattery/` and is removed at exit after receipts were copied.
- No S931–S933 citation. No canon or historical certification. No agent://all, no task calls, no subagent dispatch.
- Read-only lane git: `rev-parse`, `show`, `ls-tree`, `cat-file` only.
- Build/lint/test of siblings' outputs: none.

## Verification to run at integration (main agent)

```
KOTODAMA_ROOT=<lands root> python3 -B tools/check-finding-sets.py --selftest --work <existing dir>   # expect 16/16, rc 0
KOTODAMA_ROOT=<lands root> python3 -B reports/round-88/measure88.py --root . --base 4956282281dac1306cfbe59523e46dde99749d75 --lands <lands> --claim O --work <existing dir>   # expect 9/9
```
