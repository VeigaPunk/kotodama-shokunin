# R28-D12 — the verdicts: every command run, at this tree

- **Seat:** R28-D12 (D axis, law-replay implementation 8 of 8). Round 28, loop 3
  build 4 of 4, claim **D** `register-law-replay`. Integrator: `impl-1.md`.
- **Date:** 2026-10-18 (measurements 20:1x–20:2xZ). Baseline revision
  `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`; lane HEAD
  `69cecbc7dcf575a29f29660ecac470e05260fd86`.
- **Write scope:** this file only; scratch under `.scratch/r28-d/`.
  `export TMPDIR=$PWD/.scratch` preceded every scratch write. No filed round-8..27
  byte written; no commit, no push.
- **Canon:** NON-CANON engineering evidence.

## 1. The acceptance run

```
$ python3 reports/round-28/run-validation.py
claim D: PASS
claim O: PASS
claim C: PASS
acceptance_checks_passed: True
```

`reports/round-28/validation.json` sha256
`6b521d7173ceaaafa9bcc1b8191122fbee805efebd5692878a9a521c14834991`.

## 2. The gate and tool verdicts

| # | command | result | exit |
|---|---|---|---|
| V-1 | `tools/gates/register-law-gate.py --selftest` | `selftest: 33/33 checks passed` | 0 |
| V-2 | `tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | 4 `D4L-LAW-DANGLING` holds (reported, not a defect of this seat) | 1 |
| V-3 | `tools/assemble-culture-d4.py --check` | `byte-identical deterministic assembly` | 0 |
| V-4 | `tools/assemble-culture-d4.py --selftest` | `81/81 checks passed` | 0 |
| V-5 | `tools/d2-typed-labels.py --packet … --check …` | `byte-identical deterministic projection` | 0 |
| V-6 | `tools/d2-typed-labels.py --selftest` | `163/163 checks passed` | 0 |
| V-7 | `tools/assemble-d4-typed.py --check …` | `byte-identical deterministic typed packet` | 0 |
| V-8 | `tools/assemble-d4-typed.py --selftest` | `12/12 checks passed` | 0 |
| V-9 | `tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed` | 0 |
| V-10 | `tools/gates/typed-pipeline-gate.py --selftest` | `19/19 checks passed` | 0 |
| V-11 | `tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `violations=0 rule_holds=0`, `derived_pairs=8` | 0 |
| V-12 | `tools/gates/argot-derivation-gate.py --selftest` | `selftest: 27/27 checks passed` | 0 |
| V-13 | `tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | `byte-identical deterministic assembly` | 0 |
| V-14 | `tools/gates/d4-typed-labels-check-gate.py` | `byte-identical deterministic projection` | 0 |
| V-15 | `tools/check-gate-battery.py` | `pass 7, fail 0, unevaluable 0`, `coverage 9/9` | 0 |

## 3. The D claim's own measurement, read back

From `reports/round-28/validation.json` → `claims.D.measurement`:

| condition | measured |
|---|---|
| `law_blocks.registers` | 4 rows `QREG-01..04`, declared by `04-lexicon.yml` |
| `law_blocks.register_law` | 5 rows `RGL-01..05`, declared by `13-register-law.yml`; kinds `admissibility/asymmetry/era/exclusion/no-segment` |
| `contract_record_fields` | both `registers` and `register_law` declared |
| `runner_law_reader.findings_total` | 4 (all `D4L-LAW-DANGLING`; recorded, never graded) |
| `law_finding_producers` | `tools/gates/register-law-gate.py` (+ two round-28 sibling instruments) |
| `law_replay.clean.lines` | 4 |
| `law_replay.tampers.force` | clean 4 → tampered 5, **+1** `D4L-LAW-FORCE` |
| `law_replay.tampers.speaker` | clean 4 → tampered 5, **+1** `D4L-LAW-SPEAKER` |
| `law_replay.tampers.consequence` | clean 4 → tampered 5, **+1** `D4L-LAW-CONSEQUENCE` |
| `deterministic_regeneration` | `d4-assembly` 0, `d4-adapter` 0, `d4-projection` 0 |
| `gates.typed_gate_legs` | `20/20`, no failed legs |
| `gates.argot_coverage` | `records=183 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` |
| `rl4.records_absent` | `[]` |
| `rl4.still_skipped` | `{}` |
| `holds.names_round_28` | true |
| `holds.names_the_fix` | true |
| `holds.counts` | `{hold: 12, note: 0, fail: 0}` |
| `artifact_tokens` | all five true |

## 4. The protected-file check

No filed round-8..27 byte and no frozen generation was written. Measured:

```
$ python3 reports/round-28/run-validation.py --check | … protected_filed_artifacts
"differences_total": {"value": 0}
"protected_paths":   {"value": 1587}
"protected_status_rows": {"value": 0}
```

`git status --short` over the protected globs (`reports/round-8..27`,
`tools/gates/frozen/round-*`) is **empty**. The two files this seat edited that
live outside its own new artifacts are the two components RL-4 names, both
explicitly this claim's assignment.

## 5. The artifact digests at this tree

| artifact | sha256 |
|---|---|
| `tools/gates/register-law-gate.py` (new) | `bbad35784bfb463d41912908748ebb711f72109d811d0dc8f0110657e3b4c026` |
| `examples/culture-d4/components/03-orthography.yml` | `0f2ff45439fd7db3e9014bd1012bd917e42d042f457b8cef2bed2c9a791d4e1b` |
| `examples/culture-d4/components/09-costumes.yml` | `f61cc6845518d44f50e5179339a1a2fda2c5290efb52d6badb28cbec87768c23` |
| `examples/culture-d4/packet.d4.yml` | `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f` |
| `examples/culture-d4/typed-labels.d4.yml` | `339bfd83bf66832479b5b8ffbbce708c8be15e13b08967fa7049b848661a3cf8` |
| `examples/culture-d4/packet.d4.typed.yml` | `15c81ec11b42efaa7d683dd9320bfc7cd9b5d1e812e042d99dbf8d8726ec5da6` |
| `examples/culture-d4/expected-holds.json` | `65f5a03e092fb4bb1e04f26d73180ca411c1f91bd29d2f1912d275407e15e423` |
| `tools/gates/typed-pipelines.json` | `7f5a9c722a5ccca51f15b704368831381a428f1b977ad75c5b88aa85704a886a` |
| `tools/assemble-culture-d4.py` (unchanged) | `943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2` |
| `tools/d2-typed-labels.py` (unchanged) | `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` |
| `tools/gates/typed-pipeline-gate.py` (unchanged) | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` |
| `examples/culture-d4/components/13-register-law.yml` (unchanged) | `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7` |

## 6. The claim, clause by clause

`reports/round-28/claims.json` claim D `after_required`:

> "The law gains a replay/checking leg: speaker classes resolve against delivered
> records, forces against a declared vocabulary, consequences against the
> roll/rank machinery — a tampered row is a named finding (D4L-LAW-* class);
> RL-4 fixed (the components declare packet_keys; the records reach the packet;
> the named-holds set updated honestly); the D4 typed gate + argot gate +
> assemblers green; the RL-3 ceiling recorded as a design constraint in the
> knowledge entry."

| clause | measured | where |
|---|---|---|
| a replay/checking leg | `tools/gates/register-law-gate.py`, 33/33 selftest | `impl-1.md` §2, `impl-2.md` |
| speaker resolves against delivered records | `speaker_tokens=3`, `speaker_failures=0`; fires on `(ZZ-99)` | `impl-2.md` §2 |
| force against a declared vocabulary | fires on `no-such-force`; the set is printed in the finding | `impl-2.md` §2 |
| consequence against roll/rank machinery | fires on `"the act evaporates silently"` | `impl-2.md` §2 |
| a tampered row is a named `D4L-LAW-*` finding | **+1 line** per tamper, three of three | `impl-3.md` §2 |
| the components declare `packet_keys` | both files, measured | `impl-4.md` §1 |
| the records reach the packet | 8 of 8 ids; `still_skipped` empty | `impl-4.md` §3 |
| the named-holds set updated honestly | revision note names the landing and the fix; counts unchanged at 12/0/0; r27 pins as new keys | `impl-5.md` §2, `impl-6.md` §1 |
| D4 typed gate + argot gate + assemblers green | 20/20 legs; `violations=0 rule_holds=0`; all three `--check` byte-identical | §2 above |
| the RL-3 ceiling in the knowledge entry | **claim C's**, not this seat's | `reports/round-28/ceiling/` |

## 7. What remains open

| item | owner | recorded |
|---|---|---|
| the four `design_row` dangles (`QREG-05..08` never landed as records) | `13-register-law.yml`'s owner | `impl-6.md` §2 |
| the two `CONSEQUENCE` class-fit rows (`RGL-04`/`RGL-05`) | same; this leg scopes by `force: none` and reports 0 | `impl-6.md` §2 |
| the leg is not registered in the battery / not wired into the typed gate | a later round that wants it always-on; owes the baseline pair and the manifest re-pin | `impl-7.md` §2 |
| the pin cascade in the filed frozen/expected/handoff surfaces | the **O claim's sweep** | `impl-5.md` §4 |

## 8. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 reports/round-28/run-validation.py
python3 tools/gates/register-law-gate.py --selftest | tail -1
python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml | tail -2
python3 tools/check-gate-battery.py 2>&1 | grep -o '"coverage": "[^"]*"'
git status --short -- 'reports/round-8*' 'reports/round-1*' 'reports/round-2[0-7]' 'tools/gates/frozen/round-*'
sha256sum tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
```
