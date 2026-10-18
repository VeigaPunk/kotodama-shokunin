# R18-O14 — selftest additions: baseline intact, generalized control set 14/14

- round: 18 (operator loop 2 of 3, build round 2 of 4; 64 workers) · shard:
  **O14** (tests ×4, claim O `gate-generalization`) · owner: L2 worker,
  kotodama-shokunin lane.
- assignment (verbatim): "O R18-O11..O14 (tests x4): … selftest additions;
  reports/round-18/gate/tests-{1..4}.md."
- date: 2026-10-18, evidence window 10:23–10:42Z. The gate file was written by
  the O seats throughout the window; every number below carries the revision it
  was measured at.
- canon: NON-CANON engineering evidence.
- writes: **this file only** plus gitignored scratch under `.scratch/r18-o11/`
  (`export TMPDIR=$PWD/.scratch` before every scratch-writing command). No gate,
  tool, packet, expected file or earlier-round byte is edited by this seat. No
  commit, no push.
- **status: COMPLETE — both selftest sets green at the last revision measured.**
  `--selftest`: 12/12 at every revision sampled. `--selftest-generalized`:
  11/14 → 13/14 → **14/14** as the O seats landed their fixes, and the battery
  stays 7/7. §4 records the intermediate red state and its cause, because a
  control set that was red 20 minutes before the stamp is part of the evidence.

## 1. What is measured

Claim O's "selftest additions" leg: the generalized gate must carry its own
controls for the declared-identity mechanism, and the pre-existing control set
must stay green. Three runs:

1. `python3 tools/gates/typed-pipeline-gate.py --selftest` — the pre-round-18
   control set (12 checks), which must not regress;
2. `python3 tools/gates/typed-pipeline-gate.py --selftest-generalized` — the
   round-18 additions (fixture assembler, declared-identity resolution,
   tamper, assembler drift, self-pin, missing expected file, stale declared
   pin);
3. `python3 tools/check-gate-battery.py` — the standing baseline battery, which
   must not be disturbed by the additions.

## 2. Method

All commands cwd = lane root, `TMPDIR=$PWD/.scratch`,
`PYTHONDONTWRITEBYTECODE=1`. Raw outputs:
`.scratch/r18-o11/selftest-final.out`, `selftest-generalized-final.out`,
`sg-286d.out`, `battery-final.json`. The failing intermediate check was
*diagnosed*, not merely reported: `.scratch/r18-o11/diag_generalized.py` replays
the selftest's own fixture (it loads the gate module read-only and calls its
`FIXTURE_ASSEMBLER`, `_fixture_typed_packet`, `sha256_file`, `SCHEMA`, builds the
same mirror, and runs the gate `--json` over the fixture typed packet), so the
legs failing inside that run can be named. The gate sha is re-hashed before and
after every run.

## 3. Receipts

| # | command | revision (sha256, 16 hex) | exit | observed |
|---|---|---:|---:|---|
| 1 | `--selftest` | `d102fd1d…` (pre-change, 10:23Z) | 0 | `selftest: 12/12 checks passed` |
| 2 | `--selftest` | `d4785d9a…` (10:34Z) | 0 | `12/12` |
| 3 | `--selftest` | `84dc177e…` (10:39Z) | 0 | `12/12` |
| 4 | `--selftest` | `286d6e82…` (10:41Z) | 0 | `12/12` — the pre-round-18 control set is intact at every revision sampled |
| 5 | `--selftest-generalized` | `ea95e2a1…` (10:36Z) | **1** | `11/14 checks passed` — failures: the typed fixture grades green; L1-assembler passed and the pin re-verified; stale declared pin |
| 6 | `--selftest-generalized` | `84dc177e…` (10:38Z) | **1** | `13/14 checks passed` — failure: `declared identity: the typed fixture grades green (exit 0)` |
| 7 | `--selftest-generalized` | `286d6e82…` (10:41Z) | **0** | `selftest-generalized: 14/14 checks passed — default resolution on the D2 constants, a declared family graded green, determinism, and the tamper/drift/self-pin/missing-expected/stale-pin controls, each identity verdict agreed with the assembler's own --check` |
| 8 | `python3 tools/check-gate-battery.py` | `84dc177e…` (10:39Z) | 0 | `{"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}` — the additions do not disturb the battery's standing reading |

The 14 generalized checks at revision 7, in order: default resolution lands on
the D2 constants (×2: packet and typed packet), a declaration resolves the family
paths, fixture assembler built its packet, the typed fixture grades green,
L1-assembler passed and the pin re-verified, the resolved block is reported, two
gate runs byte-identical, the gate's identity leg agrees with the assembler's
`--check`, assembler drift breaks the identity leg, a stale assembler pin is
refused, the identity leg agrees with `--check` on the restored tree, a missing
expected file exits 2 and names the leg, and a stale declared pin exits 2 with
`L4-pins` firing.

## 4. The intermediate red state, and what fixed it

Recorded because it is the honest trajectory: at revision `ea95e2a1…` the
additions were **11/14** and at `84dc177e…` **13/14**. The surviving failure was
`declared identity: the typed fixture grades green (exit 0)`. My independent
replay of that fixture (`.scratch/r18-o11/diag-generalized/typed-fixture-run.json`,
10:38Z) showed the inner run exiting 1 with two failed legs:

```
FAIL L2-channel: off-channel lines in the typed run:
  ["costume-era-consistency-gate.py: FINDING MAT-02: [hold] RF-01: material 'felt'
    has no entry in the packet's material declarations …"]
FAIL L3-routing-consistency: holds ['LEX-RF-01'] vs routed ['RF-01'];
  owed slots [] vs routing ['LEX-RF-01']
```

Both were *fixture-versus-semantics* collisions on the D4-shaped case (a routing
row kept on channel, `off_channel_field: null`, and a hold naming a label rather
than the record). The O seats resolved them between 10:39Z and 10:41Z:

- `L2-channel` now counts an off-channel line only when it names a **moved**
  record (`any(record in line for record in moved_records)`,
  `tools/gates/typed-pipeline-gate.py:517-521`), so kept-on-channel rows no
  longer trip it;
- `L3-routing-consistency` is now read off the routing rows themselves — it
  filters to moved rows and takes the hold id from `row["hold"]`
  (`:616-629`, comment: "a D4-family packet checks its own class
  (`D4L-FORM-UNRESOLVED`)"), so a label-keyed hold no longer collides with the
  record key;
- the fixture typed packet now carries the minimal non-typed blocks the five
  culture gates accept (phonology mapping, one costume, one lexicon entry, era
  tag list — `_fixture_typed_packet`, `:954-959`), which is what removed the
  earlier `L2-channel: phonology-sanity-gate.py: exit 2` could-not-evaluate.

At `286d6e82…` my replay of the fixture returns `gate ok: True, exit_code: 0`
with no failed checks, matching the selftest's own verdict.

## 5. What covers the same ground, on delivered artifacts

The mechanism the additions control is independently exercised on *delivered*
artifacts by the other shards of this seat, so the additions are corroborated
rather than trusted:

- `tests-1.md` §3/§6 — the default D2 path is byte-identical across the pinned
  pre-change gate and the generalized gate (6/6 comparisons, nine runs, three
  revisions now), and the round-11 frozen manifest replays 11/11 with only the
  gate digest re-pointed;
- `tests-3.md` §3/§5 — forged assembler bytes, a forged self-pin and a stale
  packet are each rejected with exit 2 on the delivered D4 tree, in isolated
  mirrors.

## 6. What this does not say

- Selftest green is a control-set statement, not a clearance: the 15 D2 holds
  and the 1 note stay visible, and `--selftest-generalized` grades fixtures
  (family `d9`), not the delivered D4 pipeline — which remains blocked at
  `L1-build: adapter missing` (`tests-2.md` §4).
- The counts are stamped to revisions. The O seats edited the file repeatedly
  during the window (16 hex digests observed in ~15 minutes); a later edit
  invalidates these rows until re-run:

```sh
export TMPDIR=$PWD/.scratch
python3 tools/gates/typed-pipeline-gate.py --selftest                # expect 12/12
python3 tools/gates/typed-pipeline-gate.py --selftest-generalized    # expect 14/14
python3 tools/check-gate-battery.py                                  # expect pass 7, fail 0
```
