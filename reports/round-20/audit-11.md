# R20-A11 — alias-wart negative re-runs and the per-family era-alias leg (NON-CANON)

- seat: R20-A11 (operability auditor, of R20-A09..A12). Lane:
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- assignment (verbatim, my batch): *"AUDIT R20-A09..A12 (entry+handoff auditors x4):
  v3 packet adversarial pass; README-vs-files diff independent re-derivation;
  alias-wart negative re-runs; frozen replay audits."* This file is the third leg.
- date: 2026-10-18 (lane-local UTC−03:00; stamps UTC). Declared baseline
  `caf1beac…`; HEAD `122086b`. The O change to `tools/d2-typed-labels.py` landed
  inside my window (sha 0da0015f… at 12:58Z → fd70df51… → 8eaeba12… → 76536a92…
  at 13:04Z); readings below name which revision they saw.
- role limits: this seat audits and reports. Writes: this file plus gitignored
  scratch (`.scratch/audit/r20-alias-rerun.py`, mirrors and `receipt.json` under
  `.scratch/audit/alias-rerun/`). It edits no tool, no profile, no pin; where a
  claim is unmet at the stamp, it says so and routes it.
- claim O (`reports/round-20/claims.json`): the projector's era-alias leg
  resolves per packet family; the round-19 wart erratum is closed; d2/d3/d4
  projector runs + gate 19/19 + adapter selftest 12/12 green **without the
  mirror copying the foreign examples tree**; D2 byte-identical; repin cascade
  as NEW rows.

## 1. Verdict

| control (stamp, projector revision) | reading | class |
|---|---|---|
| **pre-fix** negative: D4 check in a mirror with no `examples/culture-d2/` (12:5xZ, 0da0015f) | exit 2 — `d2-typed-labels error: missing examples/culture-d2/components/12-rank-rules.yml; A1 cannot be recorded` | wart reproduced (before) |
| **pre-fix** positive control: same mirror + the two D2 components | exit 0 — byte-identical projection | isolates the dependency |
| **post-fix** mirror without the D2 tree (13:07Z, 76536a92) | exit 0 | wart closed |
| **post-fix** mirror with the D2 tree | exit 0 (same output) | no behaviour change |
| **post-fix** mirror with **both D2 components corrupted** (canary) | exit 0 (same output) | the D4 leg does not read the D2 tree at all |
| D2 byte-identity: `--check examples/culture-d2/typed-labels.d2.yml` | exit 0; the projection file is byte-unchanged vs HEAD (`git status` clean; sha256 `a3aa452cd5ae77c3…`) | D2 path intact |
| D4 live: `--check examples/culture-d4/typed-labels.d4.yml` | exit 0 after the O seat regenerated it (cbcf997f5f38…) | projection in sync with the peer |
| ledger skip-in-the-open (emitted D4 projection) | `era_aliases_applied` = the packet's own `named_eras` (E0–E3); `era_aliases_basis` names `examples/culture-d4/packet.d4.yml`; `skipped` = only the costume-era reconciliation leg ("the packet declares no era_reconciliation rows") | no silent aliasing, no foreign read |
| adapter selftest **without the foreign tree** | isolated patched copy (D2 copytree removed, no `examples/culture-d2` in the tree): **12/12, exit 0** | the fix suffices; see §4 residual |

The wart is closed at the projector level, and the D2 path is byte-identical —
both re-derived, not read from the O seat's prose.

## 2. Pre-fix reproduction (the negative re-run's before-half)

Mirror built by hand at 12:5xZ from the then-live revision (projector sha
`0da0015f…`): `tools/d2-typed-labels.py`, the reader gate
`tools/gates/costume-era-consistency-gate.py`, and the two D4 files; run from
the mirror root:

```sh
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml \
    --check examples/culture-d4/typed-labels.d4.yml
# -> d2-typed-labels error: missing examples/culture-d2/components/12-rank-rules.yml; A1 cannot be recorded
# -> exit 2
```

Adding `examples/culture-d2/components/{12-rank-rules,11-costumes}.yml` to the
same mirror flipped it to exit 0 — the failure was attributable to the alias
leg's hard dependency, matching the round-19 routed wart ("projector era-alias
leg requires the D2 alias component even for D4 packets",
`reports/round-19/validation.json` notes).

## 3. Post-fix adversarial re-run

Instrument: `.scratch/audit/r20-alias-rerun.py` (stdlib-only, read-only over
the repo; mirrors under `.scratch/audit/alias-rerun/`), run 13:07Z at projector
sha `76536a924280ad41…`, receipt at `.scratch/audit/alias-rerun/receipt.json`:

```
mirror-none   -> exit 0  "byte-identical deterministic projection"
mirror-good   -> exit 0  (identical stdout)
mirror-canary -> exit 0  (identical stdout; both D2 components replaced by malformed bytes)
d2-check      -> exit 0
d4-live-check -> exit 0
VERDICT: mirrors agree -> [0, 0, 0]
```

The canary is the strongest control: if any code path still opened
`12-rank-rules.yml` or `11-costumes.yml`, the malformed bytes would surface as
a load failure; all three mirrors produce byte-identical verdicts, so the D4
leg resolves only from the packet's own declarations. The emitted D4
projection's era block (read from `--emit` output, no D2 tree present) carries
`"era_aliases_applied": {"the cold fire (reserved)": "E3", "the league": "E2",
"the mark hand": "E1", "the stamp era": "E0"}`, the basis naming
`examples/culture-d4/packet.d4.yml named_eras (A1)`, and a `skipped` row for the
costume-era reconciliation leg only. The design in the tool matches the claim:
`packet_family()` derives d2/d4/… from the `examples/culture-<family>/`
directory (the same convention as `tools/gates/typed-pipeline-gate.py`
`family_of`), the D2 branch keeps the round-8 leg unchanged
(`tools/d2-typed-labels.py` `family_alias_leg`, D2 branch), and every other
family resolves `era_aliases` / `named_eras` / `era_records` from its own packet
or reports a skip row.

## 4. Residuals and repin surfaces (measured at the stamp)

1. **The adapter selftest mirror still copies the foreign tree.**
   `tools/assemble-d4-typed.py:416-419` still does
   `shutil.copytree(ROOT / "examples/culture-d2", mirror / "examples/culture-d2", …)`
   with the round-19 wart comment ("the projector's era-alias leg requires the
   D2 alias component even for D4 packets (documented wart; routed) — the mirror
   must be faithful"). Control: an isolated copy of the tool with that copytree
   removed, in a tree with **no** `examples/culture-d2` at all, still reads
   `selftest: 12/12 checks passed`, exit 0. So the claim's "adapter selftest
   12/12 … without the mirror copying the foreign examples tree" is satisfied in
   substance by the projector fix, but the live adapter still carries the
   redundant copy and a now-stale comment. Routed to the parent: delete the
   copy and the comment, or record why the mirror stays faithful.
2. **Repin cascade, as measured at 13:07Z.**
   - carried as NEW rows: `tools/gates/expected/d4-typed-labels-check-gate/r20-post/`
     (new baseline dir: `expected.json`, `freeze.txt`, `run.log`, example and
     tool snapshots — the r19-pre dir untouched);
     `reports/round-20/wart/expected-v2-07-r20.json` (new successor of the
     round-16/18 v2-handoff baselines; its input table pins the unchanged D2
     projection `a3aa452c…`).
   - edited in place (config, not a filed round artifact):
     `tools/gates/typed-pipelines.json` now pins the new projection
     (`cbcf997f…`), keeps the old digest under a `superseded` key with its
     provenance, pins the adapter, and names a `repin` block pointing at
     `reports/round-20/wart/repin-r20.json`.
   - **owed at the stamp:** that named receipt `repin-r20.json` was not yet
     filed (the wart dir held only `expected-v2-07-r20.json`), and the round-18
     frozen row 2 is red until a successor row pins the regenerated projection
     (see `audit-12.md` §5). Surfaces that still carry the old projector sha
     `0da0015f…` and are *not* allowed to be edited (filed rounds 8–19):
     `tools/gates/frozen/round-11/typed-pipeline/run-receipt.json`,
     `tools/gates/frozen/round-18/repin-d2/run-receipt-repin.json`,
     `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/{expected.json,freeze.txt}`,
     `examples/culture-{d2,d4}/expected-holds.json`, and the round-8..15
     validation/receipt files found by
     `grep -rln 0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`.
     These need successor receipts (as the r20-post and v2-07-r20 files do), not
     edits — the cascade was mid-flight at my last reading.

## 5. Selftest and gate readings (13:06-13:08Z, projector 76536a92…)

| command | reading |
|---|---|
| `python3 tools/assemble-d4-typed.py --selftest` | exit 0, `12/12 checks passed` |
| `python3 tools/gates/typed-pipeline-gate.py --selftest` | exit 0, `12/12 checks passed` |
| `python3 tools/assemble-culture-d4.py --selftest` | exit 0, `81/81 checks passed` |
| `python3 tools/d2-typed-labels.py --selftest` | exit 0, `50/50 checks passed` (was 39/39 pre-round-20; the per-family leg adds controls) |
| `python3 tools/gates/d4-typed-labels-check-gate.py --selftest` | exit 0, forwards to the peer (`50/50`) |
| `python3 tools/gates/d4-assembly-check-gate.py --selftest` | exit 2 — the flagless adapter reads `--selftest` as an input path (documented in README rev 1.5 and round-19 audit-3) |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | **19/19 legs, exit 0** — live tree and, for control, an isolated baseline tree (`git archive caf1bea`) |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | 14/16 legs, exit 1 — **identical at the baseline tree**, i.e. pre-existing; already routed in round 19 as L19-D08-2 (`reports/round-19/integration/log-fragment.md` §3.2: "Exit 1, 14/16 …; the same gate over `packet.d4.yml` is 19/19"). Not a round-20 regression; the O claim's "gate 19/19" is read as the `packet.d4.yml` leg. |

## 6. Limits

- The pre-fix negative is a re-construction from the filed round-19 routing plus
  a live reproduction at the then-live revision; the pre-fix tool revision is
  not filed separately, so the reproduction is the evidence.
- Mirrors are minimal read sets (projector + reader gate + the packet/projection
  + optionally the two D2 components); they prove *which tree the leg reads*,
  not the full pipeline.
- The repin-cascade section is a point-in-time reading of a live wave; §4.2's
  "owed" items may land after my stamp.

## 7. Final addendum (13:34Z) — both §4 residuals closed inside the window

- **§4.1 closed.** `tools/assemble-d4-typed.py` was updated: the selftest mirror
  no longer copies the foreign tree. The comment now reads "the foreign
  examples/culture-d2 tree is NOT copied: the projector's era-alias leg
  resolves per packet family (round 20, O claim), so a D4 mirror is faithful
  without it — the round-19 wart is closed. The controls below are the test: if
  a D4 build ever needs the foreign tree again, --emit fails with 'missing
  examples/culture-d2/…; A1 cannot be recorded' instead of passing"
  (`tools/assemble-d4-typed.py:433-437`). Re-run at this stamp:
  `python3 tools/assemble-d4-typed.py --selftest` → exit 0, 12/12.
- **§4.2 largely closed.** `reports/round-20/wart/repin-r20.json` is now filed
  (the receipt `tools/gates/typed-pipelines.json` names), beside the wart dir's
  design/review/shard files; and a **new frozen generation**
  `tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv` (11 rows, the round-11
  successor shape) replays **11/11 reproduced, exit 0** at 13:34Z. Still owed at
  the stamp: a successor manifest row for the **round-18 D4 typed-labels row**
  (the round-20 generation carries the d2/round-11 rows only; the live D4 pins
  are carried by the new `tools/gates/expected/d4-typed-labels-check-gate/
  r20-post/` baseline, the profile, and the repin receipt — see `audit-12.md`
  §5/§9).
- The three-mirror adversarial run and the D2 byte-identity control were re-run
  unchanged at projector sha `76536a92…` (same verdicts as §3).

