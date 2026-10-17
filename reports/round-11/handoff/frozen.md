# R11-O14 — frozen baseline for the handoff-e2e exercise + tamper control

- seat: **R11-O14** (round 11, claim **O / operability**, targets `R11-O14..O15`).
  Assignment, verbatim: "Frozen expected.json baseline for the exercise + tamper
  control demonstrating could-not-evaluate" — this file, the baseline bytes, and
  the tamper-control script/log are the seat's writes.
- date: **2026-10-17**; measurement window 19:08–19:21 -03 (`date -Is`).
  Lane revision at freeze: `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7`
  (`git rev-parse HEAD`). All scratch under `TMPDIR=$PWD/.scratch`.
- what this is: the committed frozen run of `tools/exercise-handoff-e2e.py`
  (profile `kotodama-handoff-e2e/1`, built to `reports/round-11/handoff/design.md`)
  over its 21-file read set, plus a falsifiability drill proving the baseline
  refuses edits as could-not-evaluate instead of re-blessing them. It is
  lane-local engineering evidence; not canon, not lore acceptance, not round
  completion (`gate-frozen-run-standard.md` §§2, 11).

## 1. The baseline — bytes, home, verdict

`tools/exercise-handoff-e2e.py --freeze reports/round-11/handoff` writes four
files into the design's home (design §8: **not** under `tools/gates/expected/**`
or `tools/gates/frozen/**` — the exercise is not a gate):

| file | sha256 (2026-10-17 19:21 -03) | role |
|---|---|---|
| `reports/round-11/handoff/expected.json` | `a94f9ded9d0938ec1510a1834b83162635c9e94a04b70461d5db0b98a0031d7a` | the baseline (profile `kotodama-handoff-e2e/1`) |
| `reports/round-11/handoff/packet.md` | `6583b6bdbf5e3fe039d1eee1d9f53d63ef09a04e3eeb5c98ae4943ed1771a64f` | the assembled packet the gate graded (= `packet_sha256`) |
| `reports/round-11/handoff/run.log` | `60d2965858c1f25c6d76f44bafdabbb2ea512fb271154274b943d7f6de21047e` | gate stdout verbatim + freeze summary |
| `reports/round-11/handoff/freeze.txt` | `56607f29e7e83eccc6f05d7760f8246066e11a5de4bd8943d37022868627e3d1` | freeze stamp and read-set counts |

Baseline content (measured, not restated): `profile kotodama-handoff-e2e/1`,
`expected_exit 0`, `expected_finding_ids []`, `expected_scan {fields 16/16,
glossary_entries 20, findings 0}`, `packet_sha256 6583b6bd…`, `baseline_digest
19f39f84…` (integrity digest over the baseline's own content), `inputs` = **21
pinned digests**, `frozen_at 2026-10-17`, `frozen_by tools/exercise-handoff-e2e.py`.
The 21 pins cover the whole read set, including the gate under test
(`tools/gates/handoff-packet-check.py` `e2fa3223…`), the four helper tools
(`assemble-d2.py` `8ea6bdde…`, `assemble-culture-d3.py` `ba8d19d5…`,
`d2-typed-labels.py` `0da0015f…`, `check-evidence-coupling.py` `849494b0…`),
the D2 packet (`e0f21509…`), the re-emitted typed projection (`a3aa452c…`),
the D3 packet and its four components, `examples/culture-d3/{packet.gates.yml,
controls.json,expected.json}`, the contract (`5f4c02bf…`), the four closed
round-6 source ledgers and `reports/round-6/parent-reconciliation.json`.
Documentation surfaces (`examples/culture-d3/handoff.md`, `README.md`) stay
outside the freeze by design §7; the exercise script itself is not self-pinned
(no self-digest cycle) — its revision is named by the sha in this report.

Trackedness: every file above is a **new untracked file** at this stamp
(`git status --porcelain reports/round-11/handoff` → `?? reports/round-11/handoff/`);
the orchestrator's round-11 integration commit is what makes them committed evidence.

## 2. Freeze and verify receipts (commands verbatim, lane root)

Tool revision measured throughout: `tools/exercise-handoff-e2e.py` sha256
`a21934ade22b2cda338645ee389c7f848256348446d8a79f38a9c9ff827d2005`.

| # | command | observed |
|---|---|---|
| 1 | `python3 tools/exercise-handoff-e2e.py --freeze reports/round-11/handoff` | exit 0; `re-froze …: packet sha256 6583b6bd…`; `read set: 21 files; component digests 13/13`; `no tracked value changed since the previous freeze` |
| 2 | `python3 tools/exercise-handoff-e2e.py` | exit 0; 8/8 checks OK — `input-digest` 21/21, `preflight`, `cross-references`, `gate-exit` 0 from the isolated copy, `gate-scan fields=16/16 glossary-entries=20 findings=0`, `frozen-packet`, `frozen-glossary` 20 ids, `preservation` (21 files byte-identical before/after) |
| 3 | `python3 tools/exercise-handoff-e2e.py --selftest` | exit 0; positive run + **17 controls** (8 malformed gate cases, dropped-glossary, hazard, isolation from a foreign cwd, preservation, tamper-baseline → exit 2 `E2E-BASELINE`, tamper read-set → exit 1 `E2E-DIGEST`, tamper scan expectation → exit 2 `E2E-BASELINE`, missing artifact → exit 2 `E2E-ARTIFACT`) |
| 4 | `python3 tools/check-gate-battery.py --baselines-root tools/gates/frozen --baselines-root tools/gates/expected --baselines-root reports/round-9/baselines` (the roots `reports/round-11/run-validation.py` uses) | exit 0; baselines `pinned 8/8`, `gates_uncovered []`, `unevaluable 0` — the O baseline is invisible to the battery because it sits outside the baseline roots |
| 5 | `python3 tools/check-gate-battery.py` (default roots) | exit 2 — the standing pre-round state (naming-collision and myth-consistency baselines live under `reports/round-9/baselines/`); `readings {'pinned': 5}`, `unevaluable 0`; the O baseline adds no record |

## 3. Tamper control — could-not-evaluate on the committed bytes

Instrument: `reports/round-11/handoff/tamper-control.sh` (runs each scenario in a
fresh isolated copy of `tools/ examples/ corpus/ reports/` under `$TMPDIR`; the
live tree is read-only). Transcript: `reports/round-11/handoff/tamper-control.log`
(captured 2026-10-17T19:20:58 -03, tool `a21934ad…`, baseline `a94f9ded…`;
`tamper-control: all scenarios matched their expectation`, exit 0).

| scenario | mutation (copy only) | observed | code |
|---|---|---|---|
| T0 positive | none | exit 0, `fields=16/16 glossary=20/20 findings=0`, packet `6583b6bd…` | — |
| T1 absent baseline | `expected.json` removed | **exit 2** | `E2E-BASELINE` |
| T2 malformed baseline | `expected.json` truncated to `{ not json` | **exit 2** | `E2E-BASELINE` |
| T3 baseline body edited | `packet_sha256` rewritten to `000…0` (valid JSON, re-signed) | **exit 2** | `E2E-BASELINE` (integrity digest refuses it) |
| T4 read-set file deleted | `corpus/lessons/round-6-sources/05.json` removed | **exit 2** | `E2E-ARTIFACT` (unreadable path named) |
| T5 read-set value edited | one string in `examples/culture-d2/typed-labels.d2.yml` + `x` (still valid JSON) | exit 1 | `E2E-DIGEST` |
| T6 gate revised | one comment appended to `tools/gates/handoff-packet-check.py` | exit 1 | `E2E-DIGEST` |

- The could-not-evaluate cases (T1–T4) are the ones this control exists to show:
  a missing, malformed, or edited baseline and a missing read-set file all refuse
  to verdict — never a silent pass (`gate-frozen-run-standard.md` §6, fail-closed).
- T5/T6 are **drift**, not could-not-evaluate: a parseable read-set edit reads
  exit 1 with the changed file named (`E2E-DIGEST`), matching design §8's mapping.
- Final pin sweep from the same script: `profile=kotodama-handoff-e2e/1
  expected_exit=0`, `inputs: 21 pinned, 0 drifted`.

## 4. What the baseline does and does not prove

- Proves: these exact committed bytes (`expected.json` + the pinned read set),
  under gate revision `e2fa3223…`, produce exit 0 with 16/16 fields, 20/20
  glossary entries and zero findings; and that an edit to the baseline or the
  read set changes the reading (T1–T6).
- Does not prove: that the packet is good design, that any claim inside it is
  true, that lore accepted anything, or that the round is complete. The digest
  is integrity, not truth (`gate-frozen-run-standard.md` §10).
- Re-freeze protocol: any pinned input or pinned tool revision change makes the
  verdict invalid (read as `E2E-DIGEST`, exit 1) — re-freeze explicitly with the
  same command and record the new stamp; never hand-edit `expected.json`
  (an edit is refused as `E2E-BASELINE`, exit 2).

## 5. Integration notes (reported, not absorbed)

1. **Earlier placement, removed.** Before the O tool was aligned to the design,
   its hard-coded path made the first freeze land at
   `tools/gates/expected/handoff-exercise/r11/` (this seat, 19:08). Measured
   then with the validator's three roots: battery exit **2**, `baselines_found 6`,
   `readings {no baseline: 1, pinned: 5}`, `unevaluable 1`, findings
   `BASELINE-GATE-UNKNOWN` + `BASELINE-EXTERNAL-INPUT ×5` +
   `BASELINE-EXPECTED-ABSENT`; with that directory removed the same command reads
   **exit 0** (`pinned 8/8`, `unevaluable 0`). The tool revision `a21934ad…`
   now defaults to the design's home; the obsolete directory was deleted by this
   seat before the final freeze and the battery leg is green again (receipt row 4
   above).
   `reports/round-11/handoff/design.md` §8 already carries the measured addendum
   naming this mechanism; this note records the resolution.
2. **Tool revision churn during the window.** The exercise changed several times
   while this seat worked (sha prefixes `38d1cba4` → `c896eb14` → `6bf6dfc6` →
   `6d3a34d0` → `eaf2eb65` → `e74e5aea` → `d5b346b8` → **`a21934ad`**). Every
   number in this report was re-measured against `a21934ad`; earlier receipts
   (including an intermediate `--freeze` refusal `E2E-DIGEST contract_ref…`)
   describe superseded revisions and are not cited as current.
3. **Consequence for claim D's battery leg.** `reports/round-11/run-validation.py`
   requires the battery to exit 0 with the three roots (row 4). That held at this
   stamp — conditional on the baseline staying outside `tools/gates/**` and on the
   pinned read set not changing under it. If the orchestrator re-homes the
   baseline or a sibling re-emits a pinned artifact, re-run the freeze before
   reading `run-validation.py`.
4. **Adjacency, out of this seat's claim.** At 19:21 `python3
   tools/d2-typed-labels.py --check` read exit 0 (byte-identical projection); the
   typed-projection drift the round-10 records carried is resolved on the live
   tree. Reported for the D artifact owners, not absorbed here.

## Receipts

```sh
# 2026-10-17 19:08-19:21 -03, lane root, export TMPDIR=$PWD/.scratch
python3 tools/exercise-handoff-e2e.py --freeze reports/round-11/handoff      # exit 0, packet 6583b6bd…
python3 tools/exercise-handoff-e2e.py                                        # exit 0, 8/8 checks, 16/16, 20/20, findings 0
python3 tools/exercise-handoff-e2e.py --selftest                             # exit 0, 17 controls
bash reports/round-11/handoff/tamper-control.sh                              # exit 0, T0-T6 all matched
python3 tools/check-gate-battery.py --baselines-root tools/gates/frozen \
  --baselines-root tools/gates/expected --baselines-root reports/round-9/baselines   # exit 0, pinned 8/8
sha256sum reports/round-11/handoff/{expected.json,packet.md,run.log,freeze.txt}
```
