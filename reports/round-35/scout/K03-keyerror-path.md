- Seat: K03 | scout | O | date 2026-10-19 | baseline 4a7aede

# K03 — R34-N1 scout: the exact KeyError path and the diagnostic conventions to mirror

## 1. Reproduction (isolated copy only)

Provenance: `git archive HEAD | tar -x -C .scratch/k03-iso` at baseline 4a7aede.
Renderer bytes in the copy: sha256 `34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9`
— identical to the in-tree file (`sha256sum` on both paths, same digest). No filed round
runner was executed; the in-tree renderer was never run for this replay.

Command (cwd = the isolated copy):

```
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet \
  --baseline reports/round-30/handoff/declared-in-r6/expected.json
```

Observed: exit 1, stdout empty, traceback on stderr:

```
Traceback (most recent call last):
  File ".../.scratch/k03-iso/tools/exercise-handoff-e2e.py", line 4613, in <module>
    sys.exit(main())
  File ".../.scratch/k03-iso/tools/exercise-handoff-e2e.py", line 4578, in main
    code, err, records = v3_exercise(root=root, baseline_rel=args.baseline or baseline_default)
  File ".../.scratch/k03-iso/tools/exercise-handoff-e2e.py", line 3822, in v3_exercise
    record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
                                                                                 ~~~~~~~~~~~~~~~~^^^^^
KeyError: 'reports/round-20/handoff/claims-map.md'
```

The same command without `--quiet`: exit 1, stdout still empty — the `handoff-v3: exit=…`
summary line is never printed either way.

**Exit-code caveat for the acceptance leg.** The `1` is the CPython uncaught-exception exit
status, not `EXIT_FAIL` (`EXIT_PASS/EXIT_FAIL/EXIT_UNEVALUATED = 0/1/2`,
`tools/exercise-handoff-e2e.py:112-114`). An acceptance leg asserting only `exit == 1`
passes *today*, so it does not discriminate. The leg must assert absence of `Traceback` on
stderr plus the named code in the `handoff-v3: {code}: {detail}` line.

## 2. Resolving code site

- `tools/exercise-handoff-e2e.py:3479-3484` — `V3Assembly.__init__` builds `self.digests`
  over the live `V3_READ_SET` only (`self.digests[rel] = digest`, :3483).
- `:3819` — drift detection: `... if assembly.digests.get(rel) != digest` — tolerant lookup,
  behaves correctly.
- `:3822` — **the defect line**: the *reporting* step indexes directly,
  `assembly.digests[rel]` → `KeyError` for any baseline member absent from the live read set.
- `:3823` — `raise Failed("E2E-DIGEST", ...)`: the designed leg. Reachable for content drift
  (member present, digest differs), unreachable for membership-only drift, because :3822
  throws first.
- Same pattern in v1: `:1436-1438` detection, `:1440` the mirror crash line, `:1441` the
  designed raise. Latent only: the v1 default baseline `reports/round-11/handoff/expected.json`
  (21 members) is a subset of `V1_READ_SET` (baseline-only set = ∅), so it is not currently
  triggerable — but the same one-line fix applies at both sites.
- Catch tails accept only `Failed` / `Unevaluatable`: v1 `:1510-1515`, v3 `:3971-3975`. Any
  new exception must subclass one of these or it escapes as a traceback.

## 3. The condition is membership, not content drift (design input for the diagnostic text)

The superseded member's bytes are unchanged: the r6 baseline pins
`reports/round-20/handoff/claims-map.md` at
`4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8`, and the live file hashes
to the same `4b1b9a35…` (file exists, 24888 bytes, mtime Oct 18 10:11).

Both read sets hold 58 members; the set difference is exactly one member each way:

- baseline-only (unresolvable in the live digests): `reports/round-20/handoff/claims-map.md`
- live-only (absent from the r6 baseline): `reports/round-34/handoff/declared-in-r7/claims-map.md`
  — live sha256 `d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c`, the r34
  successor row named in `reports/round-34/handoff/repin.json:39`.

Consequence: the existing message at `:3823` ("read-set file(s) changed since the baseline was
frozen") and the m12b control label (`:4430`, "naming the changed file") are both *false
statements* for this row — nothing changed; the member left the read set. A patch that only
swaps the index for `.get()` and reuses the E2E-DIGEST text emits a misleading diagnostic. The
truthful wording names the unresolvable member and states that the live read set no longer
carries it (superseded row).

Symmetric blind spot worth one line in the design record: the comprehension at `:3819`
iterates `baseline["inputs"]` only, so a live read-set member the baseline does not name is
never examined by this leg (it is caught later, if at all, by the packet/twin digest legs).

## 4. Diagnostic conventions to mirror

- Exit map, docstring `:89-93` (the tool's own contract text, including the phrase "stable
  messages, no traceback"): 0 clean; 1 mismatch — `E2E-DIGEST`, `E2E-COUNT`, `E2E-GATE`,
  `E2E-SCAN`, `E2E-UNC`, `E2E-LINK`; 2 could-not-evaluate — `E2E-ARTIFACT` (missing/unreadable
  read-set file), `E2E-BASELINE` (absent or edited baseline), `E2E-DATA` (malformed input).
- Exception taxonomy `:244-268`: `Unevaluatable` (code `E2E-DATA`) → `ArtifactError`
  (`E2E-ARTIFACT`) → `MissingArtifact`; `BaselineError` (`E2E-BASELINE`); `Failed(code, message)`
  for ran-and-negative.
- Message style names the path: `:288`
  `raise MissingArtifact(f"read-set file unreadable: {rel} ({exc})")` (same at `:298`).
- User surface: `:4603-4604` prints `handoff-v3: {err}: {records[-1]['detail']}` when `err` and
  not `--quiet` — a code returned via `(code, err)` surfaces automatically; a raised exception
  does not.
- Code census at HEAD (`grep -o 'E2E-[A-Z]*' tools/exercise-handoff-e2e.py | sort | uniq -c`):
  `E2E-COUNT` 44, `E2E-DIGEST` 32, `E2E-UNC` 26, `E2E-DATA` 13, `E2E-SCAN` 11, `E2E-LINK` 10,
  `E2E-BASELINE` 10, `E2E-GATE` 8, `E2E-ARTIFACT` 6. **`E2E-READSET` occurs 0 times** — it is a
  new code, so the docstring list at `:89-93` must be extended in the same patch or the tool's
  own contract text goes stale.

### Exit-class trade (P02/O01 decide; both satisfy claim O)

Evidence for keeping exit 1 (`Failed`-family, new code `E2E-READSET`):

- `reports/round-34/handoff/repin.json:19-21` files the r6 control with `"exit": 1`; repin.json
  is filed bytes (never editable), so exit 1 keeps that recorded reading reproducible.
- The sibling drift leg at `:3823` is exit 1 (`E2E-DIGEST`); both read-set conditions stay in
  one class, no exit-code fork for near-identical conditions.
- Exit 2 is documented for a *missing/unreadable* artifact or an *absent/edited* baseline;
  neither holds here — the file exists and the baseline is integrity-valid, so
  `v3_load_baseline` (`:3772-3812`) passes it.

Evidence for exit 2 (`Unevaluatable`-family): a superseded baseline row is arguably "input
cannot be evaluated". Claim O's `after_required` and thresholds both allow either ("exits
non-zero", "E2E-READSET or the renderer's existing diagnostic convention"), so this is a design
choice, not a claim violation — it must simply be recorded with its reason.

## 5. Regression baselines captured in the isolated copy (for O03/O05/O11)

- r7 default chain, `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0:
  `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27
  statuses=16/7/4 v2_subset=equal alias_leg=landed
  packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` — equals
  repin.json's `R34-D-default-pointer` control (exit 0, same `packet_sha256`).
- selftest, `--profile v3 --selftest` → exit 0, header `selftest: OK — positive run (…) plus 39
  controls:`; 40 control bullets printed.
- **Count discrepancy to settle before O02 states its expected N**: `:4464` prints
  `{len(results) - 1} controls` while `:4466-4467` prints every element of `results`, including
  `results[0]` (the witnesses line appended at `:4169`). Header 39 vs bullets 40 is a label
  off-by-one in the header only; the suite is green. After two controls are added the numbers
  become header 41 / bullets 42 (or the label is corrected) — the acceptance leg should assert
  the bullet count, not the header.
- Controls the patch must not disturb: m12a tamper baseline `:4422` (exit 2 `E2E-BASELINE`),
  m12b tamper read-set `:4430` (exit 1 `E2E-DIGEST` naming the changed file), missing D4
  artifact `:4457` (exit 2 `E2E-ARTIFACT`). Note m12b already covers the "preserved E2E-DIGEST
  digest-mismatch path" for a member that *is* in the live read set; the genuinely new control
  required by claim O is the superseded-row (membership) refusal — O02 should say so rather than
  re-adding m12b's leg.

## Owed: none

## Citations

- `reports/round-34/handoff/repin.json:19-21` (r6 control: command, exit 1, KeyError mechanism)
- `reports/round-34/handoff/repin.json:39` (r34 successor claims-map row, digest `d181de28…`)
- `tools/exercise-handoff-e2e.py:89-93` (exit-code map, "stable messages, no traceback")
- `tools/exercise-handoff-e2e.py:112-114` (`EXIT_PASS/EXIT_FAIL/EXIT_UNEVALUATED`)
- `tools/exercise-handoff-e2e.py:244-268` (`Unevaluatable`/`ArtifactError`/`BaselineError`/`Failed`)
- `tools/exercise-handoff-e2e.py:288`, `:298` (path-naming message style)
- `tools/exercise-handoff-e2e.py:1436-1438`, `:1440`, `:1441` (v1 mirror block)
- `tools/exercise-handoff-e2e.py:1510-1515` (v1 catch tail)
- `tools/exercise-handoff-e2e.py:1933-1935`, `:1935-1971` (`V3_BASELINE_DEFAULT`, `V3_READ_SET`)
- `tools/exercise-handoff-e2e.py:3479-3484` (`V3Assembly` digests built over the live read set)
- `tools/exercise-handoff-e2e.py:3772-3812` (`v3_load_baseline` integrity checks)
- `tools/exercise-handoff-e2e.py:3816`, `:3819`, `:3820-3824` (snapshot, detection, crash, designed raise)
- `tools/exercise-handoff-e2e.py:3971-3975` (v3 catch tail)
- `tools/exercise-handoff-e2e.py:4169`, `:4422`, `:4430`, `:4457` (witnesses, m12a, m12b, missing-artifact controls)
- `tools/exercise-handoff-e2e.py:4464`, `:4466-4467` (selftest header count vs printed bullets)
- `tools/exercise-handoff-e2e.py:4578`, `:4613` (traceback frames: v3 dispatch, `sys.exit(main())`)
- `tools/exercise-handoff-e2e.py:4603-4604` (v3 `handoff-v3: {err}: {detail}` surface)
- `reports/round-30/handoff/declared-in-r6/expected.json` (`inputs` = 58 members, profile `kotodama-handoff-e2e/3`, pins `4b1b9a35…`)
- `reports/round-34/handoff/declared-in-r7/expected.json` (`inputs` = 58 members, pins `d181de28…`)
- `reports/round-11/handoff/expected.json` (v1 baseline, 21 members — latent-only exposure)
- Commands run in the isolated copy `.scratch/k03-iso` (`git archive HEAD | tar -x`), TMPDIR `.scratch`:
  - `sha256sum tools/exercise-handoff-e2e.py` (both copies) → `34c85f57…` (same digest)
  - `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` → exit 1, KeyError traceback above
  - `python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline reports/round-30/handoff/declared-in-r6/expected.json` → exit 1, stdout empty
  - `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0, `packet_sha256=45f57132…`
  - `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` → exit 0, 40 bullets
  - `sha256sum reports/round-20/handoff/claims-map.md` → `4b1b9a35…` (== frozen value in the r6 baseline)
  - `sha256sum reports/round-34/handoff/declared-in-r7/claims-map.md` → `d181de28…`
  - set-difference probe (`importlib` load of the renderer): baseline-only = {r20 claims-map}, live-only = {r34 claims-map}, both sets 58
  - `grep -o 'E2E-[A-Z]*' … | sort | uniq -c` → census above; `E2E-READSET` 0
