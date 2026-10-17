# R12-O03..O04 — round-9 conformance defect sweep

Date: 2026-10-17. Scope: round-9 report and artifacts against `reports/round-9/claims.json`, `targets.json`, `corpus/knowledge/verification/gate-frozen-run-standard.md`, and `SHONEN.md`. Read-only review of filed round-8–11 artifacts; no historical files changed.

## Finding O-R9-01 — baseline placement is outside the declared standard

**Status: open; route for round-14 integration.** Claim O requires seven gates to carry an `expected.json` baseline layout “per the gate standard” (`reports/round-9/claims.json:19-23`). The standard specifies `tools/gates/frozen/<gate>/<round>-<phase>/` (`gate-frozen-run-standard.md:50-75`). Two required baselines instead exist only at `reports/round-9/baselines/myth-consistency-gate/expected.json` and `reports/round-9/baselines/naming-collision-gate/expected.json`; their baseline IDs are gate names, not round-phase IDs.

This is not inferred from the historical receipt alone. On 2026-10-17, with `TMPDIR=$PWD/.scratch`, the following real calls were run:

```sh
python3 tools/check-gate-battery.py
```

Observed exit 2: all seven gate selftests passed, but the default baseline roots found and pinned five baselines and left `myth-consistency-gate.py` and `naming-collision-gate.py` uncovered (`BASELINE-GATE-UNCOVERED`). Then:

```sh
python3 tools/check-gate-battery.py \
  --baselines-root tools/gates/frozen \
  --baselines-root tools/gates/expected \
  --baselines-root reports/round-9/baselines
```

Observed exit 0: eight pins validated, all seven gates covered; the handoff baseline is present twice. The same split is in the stored receipt (`validation.json:811-873`) and the registry (`baselines/registry.md:169-175`). The round-9 runner explicitly classifies the default-root gap as “reported … not failed” (`validation.json:1071-1077`), so its overall O pass does not establish standard-layout conformance. The round report draft itself leaves relocation/reconciliation open (`report-draft.md:219-225`), but the admission entries in `SCORECARD.md:144,149-152` and `LOG.md:2966-2969` do not carry that qualification.

**Disposition:** preserve the filed round-9 baselines; do not relocate or rewrite them in this sweep. Round 14 should have the integrator settle the standard-path exception and make the default battery/claim wording agree before claiming standard-complete coverage.

## Report, marker, and hash checks

- The current committed `validation.json` parses as `acceptance_checks_passed: true`, F/O/D all true, and frozen D replay exit 0 with no findings. On 2026-10-17 this was checked with:

  ```sh
  python3 -c 'import json; v=json.load(open("reports/round-9/validation.json")); d=v["claims"]["D"]["measurement"]["frozen_replay"]; print(v["acceptance_checks_passed"], [v["claims"][k]["passed"] for k in ("F","O","D")], d["exit"], d["finding_ids"])'
  ```

  Its runner digest equals `sha256sum reports/round-9/run-validation.py`. A read-only input-pin check on the same date used:

  ```sh
  python3 -c 'import json,hashlib,pathlib; v=json.load(open("reports/round-9/validation.json")); m=v["input_sha256"]; missing=[p for p in m if not pathlib.Path(p).is_file()]; mismatched=[p for p,h in m.items() if pathlib.Path(p).is_file() and hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()!=h]; print(len(m),len(m)-len(missing)-len(mismatched),len(missing),len(mismatched))'
  ```

  Result: 54 input hashes, 54 matched, no missing or mismatched inputs.
- The report draft’s `D=false` / acceptance-false passage is explicitly a timestamped 18:03:39 snapshot (`report-draft.md:157-177`), and the file labels itself a draft. It is superseded by the later integration state: `git show 9dc18ec -- examples/culture-d3/expected.json` shows the three formerly stale manifest values updated; the same commit introduces the current accepted validation receipt, and the round-9 SCORECARD/LOG record the later admission. The mismatch is temporal, not evidence that the current receipt disagrees with its pinned inputs. Do not read the draft’s old red result as the current verdict. No lane-local `reports/round-9/kotodama.md` final report was found; the draft points to an external `.ufo` filing target, which this lane-only sweep did not inspect.
- SHA-256 citations in the draft were checked against their source artifacts, receipt fields, or the pre/post commit blobs. On 2026-10-17, `sha256sum` and `git show <revision>:<path> | sha256sum` reproduced the runner (`8e488130…`), battery before/after (`077f68e4…` / `0a126b70…`), province (`05b34a57…`), assembler-output receipt (`8e8910da…`), and all three old→new D3 pin pairs (`50c4c2f2…` / `5f4c02bf…`, `29a9361c…` / `e6bffd70…`, `8c5afb0a…` / `d9e4e8f4…`). No unresolved hash citation was found.
- SHONEN check passes: the draft includes `## SHONEN skeleton`, all four boxes remain `[~]`, and it says no non-author verifier was named (`report-draft.md:192-209`). This matches `SHONEN.md:5-11`: `[~]` is lane assertion; `[x]` requires a named non-author verifier. The current LOG entry records round-9 admission, consistent with the current validation receipt; the lesson’s “none yet” is explicitly the earlier survey-close state.

## Sweep conclusion

One open operability conformance defect is recorded: standard baseline placement/default-root coverage does not match the round-9 O wording, despite the custom-root battery run and accepted receipt. No round-9 artifact was repaired or back-patched; send the root-layout reconciliation to the round-14 integrator. The current acceptance receipt, SHONEN markers, LOG entry, and cited hashes otherwise reconcile when their timestamps are respected.
