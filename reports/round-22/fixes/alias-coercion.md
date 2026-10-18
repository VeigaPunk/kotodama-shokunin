# R22-O07–O09 — malformed packet-era aliases fail closed

- Assignment: alias coercion only; source changes are confined to `validate_alias_pair`, `packet_alias_rows`, and alias helper/CLI controls in `tools/d2-typed-labels.py`.
- Axes: operability (fail closed), compatibility (valid output unchanged), reproducibility (named controls and new pin rows; no historical rewrites).
- Date: 2026-10-18. Declared baseline: `46a03257ee75dd8f685a105e47da3f45a0154172`.
- Source fix, controls and alias-only re-pin capture: **complete and green at the measured snapshot**. Final combined-source integration belongs to the source/D4 re-pin owners; no round-wide admission is claimed.
- Shared-source integration notice: the D04–D06 bleed worker also owns changes in this projector. Keep both sets of non-overlapping edits; this seat does not replace that worker's file. The source SHA below is the alias-only measurement, not a promise that concurrent D edits will preserve it.

## Defect and disposition

The R21 helper probe (`reports/round-21/defects/fix-14.md`) is reproduced before editing: `packet_alias_rows({'era_aliases': {'era-9': [1, 2]}})` returned `{'era-9': '[1, 2]'}` with a confirmed row. The original `str(label): str(tag)` conversion turned malformed data into a declared alias.

The projector now validates before constructing confirmed rows:

- Alias names must be non-empty strings; non-string/blank names are not coerced.
- Tags must be exact members of the existing `CONTRACT_ERAS` (`E0`, `E1`, `E2`, `E3`), not strings containing a plausible tag.
- A present `era_aliases` must be a map. Present `named_eras`/`era_records` must be lists of valid records; missing fields, invalid row shapes and conflicting duplicate names refuse instead of disappearing.
- The named diagnostic is **`P-ERA-ALIAS at <declaration>: ...`**. The existing CLI exception boundary maps it to **exit 2**, without a traceback and before writing a projection. `--json` emits no document on this refusal, matching the existing exception-style malformed-input interface; this fix does not invent a new JSON error contract.
- Empty declarations retain the existing no-alias/fallback semantics. Valid declarations retain the same alias map, row IDs, tags and confirmed status. The legacy D2 component reader is unchanged; this fix closes the packet-local coercion defect, not a new audit of every embedded reconciliation parser.

## Controls and measured commands

All commands run from the lane root with `export TMPDIR=$PWD/.scratch` and `export PYTHONDONTWRITEBYTECODE=1` before any scratch-writing command. No historical round validator was run against this working tree.

On **2026-10-18 at 14:39:56Z**, `python3 tools/d2-typed-labels.py --selftest` passed **50/50** before the fix.

On **2026-10-18 at 14:41:29Z**, the same command passed **132/132**, exit 0: the original 50 controls plus 82 new alias controls.

- Helper controls cover all three declared shapes with list/map/int/float/bool/null tag values and empty, whitespace-padded, lowercase, out-of-contract, multi-digit and suffixed tag strings. Positive controls retain each contract tag and both era-record sources; malformed maps, names, rows and conflicting duplicate names refuse with the named diagnostic. A malformed primary map cannot be hidden by a valid fallback.
- A D4-only temporary mirror (no `examples/culture-d2` tree) exercises four full-packet mutations: list-valued tag, `E9` tag, non-map alias declaration and list-valued `named_eras` tag. Each is tested via `--emit` to an absent output, `--emit` to a pre-existing sentinel, `--json`, and `--check`. Required readings: exit 2, named diagnostic, no created output, no overwritten output, no confirmed JSON row. A valid `era-9: E1` declaration is the paired positive CLI control.

Other measured regressions on **2026-10-18**:

| Command | UTC observation | Result |
|---|---|---|
| `python3 tools/assemble-d4-typed.py --selftest` | 14:41:37Z | exit 0, **12/12** |
| `python3 tools/gates/typed-pipeline-gate.py --selftest` | 14:41:38Z | exit 0, **12/12** |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 14:41:38Z | exit 0, **19/19** legs; open holds remain design debt |
| `python3 tools/d2-typed-labels.py --check` | initial post-fix check | exit 0, D2 byte-identical |
| `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | initial post-fix check | exit 0, D4 byte-identical |

At **14:41:42Z**, command `runpy.run_path('tools/d2-typed-labels.py'); run_pipeline(ROOT / 'examples/culture-{d2,d4}/packet.{d2,d4}.yml'); serialize(result['projection'])` measured:

| Surface | Before SHA-256 | Alias-only after SHA-256 | Reading |
|---|---|---|---|
| `tools/d2-typed-labels.py` | `76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb` | `a10861f039f7e80a2f38a11fe1d72d4ef6fa5f48987f5fff96185b1875924a7b` | source moved |
| D2 projection (84,614 bytes) | `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` | same | unchanged; report exit 1 is the existing hold set |
| D4 projection (92,108 bytes) | `cbcf997f5f38fac89b0fb1b6a6841ec42c9041a2599df44083ddefc5c22cfb4f` | same | unchanged before the separate D4 bleed fix |

## New-row re-pin capture

The alias-only source snapshot is preserved in an isolated Git clone at `.scratch/r22-o07-8iaicnio/repo`. New filed rows, created on **2026-10-18 at 14:44:09Z**:

- `reports/round-22/fixes/alias-coercion-repin.json`: five explicit before/after rows, date/command bindings, control readings, replay and battery summaries, and the blocked first attempt. Every row moves the projector pin `76536a92…` to the measured alias-only source `a10861f0…`; no historical pin is overwritten.
- `reports/round-22/fixes/alias-coercion-v2-07.json`: a new handoff-v2 baseline frozen with the unmodified historical helper **inside the isolated clone**. It pins 28 inputs; only `tools/d2-typed-labels.py` moved relative to the round-20 baseline. Final verification at 14:44:08Z: exit 0, fields **16/16**, glossary **20/20**, findings **0**, claims **15/15**, links **50/50**. Command: `python3 reports/round-15/handoff/frozen-verify.py --baseline reports/round-22/fixes/alias-coercion-v2-07.json` from the alias-source clone.

| New receipt row | Superseded surface | Disposition |
|---|---|---|
| D2 expected-holds `projector_sha256` | live D2 source pin | measured successor row; final live-channel integration required |
| D4 expected-holds `projector_sha256` | live D4 source pin | measured successor row; final D4 source/output writer owns live update |
| D2 typed replay `tool_pins` | `tools/gates/frozen/round-20/repin-d2/run-receipt-repin.json` | new receipt row; standard replay reproduces **11/11** |
| handoff-v2 input source pin | `reports/round-20/repin/expected-v2-07-r20.json` | new baseline file above, verified green |
| D4 projection-check input source pin | `tools/gates/expected/d4-typed-labels-check-gate/r20-post/expected.json` | measured successor source row; D07–D08 owns the final `r22-post` snapshot with the separate bleed-fix projection |

The paired full-CLI source control ran again at **14:44:09Z** in the clone: the filed projector emitted `tag: "[1, 2]", status: "confirmed"` (exit 1); the fixed projector refused the identical malformed D4 packet (exit 2, `P-ERA-ALIAS`) and created no output. The old v2 baseline is intentionally not blessed: `python3 reports/round-15/handoff/frozen-verify.py --baseline reports/round-20/repin/expected-v2-07-r20.json` refused with exit 2, `V2F-DIGEST`, naming only the changed projector. This is the digest-first negative control paired with the new baseline's positive verification.

The following commands ran successfully in the alias-source clone on **2026-10-18 at 14:43Z**, with the lane's `.scratch` as `TMPDIR` (outside the disposable clone):

- `python3 tools/replay-frozen.py tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv --json`: exit 0, **11/11 reproduced**, zero mismatches or could-not-evaluate rows.
- `python3 tools/check-gate-battery.py`: exit 0, **7/7 structural selftests**, **18/18 pinned baselines**, gate coverage **9/9**, zero failures/unevaluable. This checks baseline digests, not a substitute for every verdict replay.

The first replay attempt at **14:43:02Z** refused: Git clone omitted the ignored historical `tools/gates/frozen/round-11/typed-pipeline/run.log`, and the replay's safety check rejected `TMPDIR` inside the clone. The standard route was restored, not bypassed: copy that exact existing log into the disposable clone (SHA-256 `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606`), keep temporary files in the lane's `.scratch` outside the clone, and rerun the unmodified replay tool. Three already existing ignored round-9 baseline logs were likewise copied only into the clone before the battery. No log was regenerated to manufacture a verdict; no original filed workspace artifact was written.

**Integration boundary:** the live expected-hold files and D4 typed-profile channel are not this seat's writes. The D4 source/derived-output owner and D07–D08 re-pin owner must use the final **combined** projector hash, not automatically `a10861f0…`. The handoff owner must rebuild its new v3 manifest/source pins. If those source bytes move, preserve these alias-only rows and file new combined successors; do not edit the alias-only v2 baseline to conceal that movement. No round-8–21 artifact was modified.

This source movement is now observed, not hypothetical: at **2026-10-18 14:45:23Z**, `hashlib.sha256(Path('tools/d2-typed-labels.py').read_bytes()).hexdigest()` was `12642aff37d54cf935b516d2abe7efb343ac26d443bc6c6f8801c81367119830` during the separate D4 implementation. A no-file `runpy.run_path('tools/d2-typed-labels.py')` probe ran `packet_alias_rows` against ten malformed tags across each of the three declared shapes plus the four valid contract tags: **34/34** checks passed, all malformed cases retaining `P-ERA-ALIAS`. Both published JSON files parsed and the v2 baseline's own canonical integrity digest matched. This checks preservation of the alias helper during integration, not the unfinished combined D4 pipeline; the full-suite readings above belong to the named alias-only snapshot. The focused control is reproducible without writing a file:

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
import runpy
n = runpy.run_path('tools/d2-typed-labels.py')
checks = 0
for key in n['PACKET_ALIAS_KEYS']:
    for tag in ([1, 2], {}, 1, True, None, 'E9', 'E10', 'E1 extra', ' E1', ''):
        declared = ({'old era': tag} if key == 'era_aliases' else
                    [{'name': 'old era', 'tag': tag}])
        try:
            n['packet_alias_rows']({key: declared})
        except n['Malformed'] as exc:
            assert str(exc).startswith('P-ERA-ALIAS at ')
        else:
            raise AssertionError((key, tag))
        checks += 1
for tag in n['CONTRACT_ERAS']:
    aliases, rows, key = n['packet_alias_rows']({'era_aliases': {'old era': tag}})
    assert aliases == {'old era': tag} and rows[0]['status'] == 'confirmed'
    checks += 1
print(f'focused alias controls: {checks}/{checks}')
PY
```

## Limits

This is non-canon engineering evidence, not lore acceptance. The alias-only source measurement must not be presented as the final combined-source hash if the D4 worker changes the projector afterward. Round-22 counting-command admission and shared bookkeeping remain the parent integrator's responsibility.
