# R20-D19 — v2 regression: the v2 handoff paths under the round-20 wave

- seat: R20-D19 (v2-regression), lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- date: 2026-10-18. Baseline revision `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d`
  (round-19 admit); observed HEAD `122086bce0aa577bec221bb2d37eedf20f4f3ed2`
  ("round-20: declare claims D/O/C"). Readings stamped UTC; lane clock UTC−03:00.
- role limits: this seat executes and measures only; it decides no admission,
  promotes no claim, certifies no canon. Writes: **this file** plus the seat's
  other assigned round-20 fragments (`audit-v3.md`, `interop.md`, the
  adversarial review) and gitignored scratch under `.scratch/r20-d17/`
  (`TMPDIR=$PWD/.scratch` exported for every scratch-writing command; the
  frozen replay uses `TMPDIR=/var/tmp/kotodama-r20-d17` because
  `replay-frozen.py` refuses an in-repo mirror root by design). No commit, no
  push, no filed round-8..19 byte touched.
- what "v2 paths" means here: the D claim's own wording — "v2 paths unchanged
  and green". Measured surfaces: (a) the round-15 v2 packet twins and their
  frozen baselines (`reports/round-15/handoff/packet-v2-05.{md,yml}`,
  `expected.json`); (b) the successor v2 baselines `reports/round-16/handoff/
  expected-v2-07.json` and `reports/round-18/repin/expected-v2-07-r18.json`;
  (c) the two round-15 harness validators; (d) the round-11 v1 exercise
  baseline path; (e) the D2 byte path the v2 packet pins (the O change's own
  control).

## 0. Verdict

**The v2 packet bytes are unchanged; the v2 frozen baselines are RED mid-wave,
and the cause is the claim-O projector change, not a silent break.** At the
pre-wave stamp (13:01:03Z) every v2 reading was green except the documented
build05 supersession. At the mid-wave stamp (13:09:15Z) two readings moved to
red — both are `V2F-DIGEST` on `tools/d2-typed-labels.py`, the file the O
seat's per-family alias fix rewrites. That is exactly the re-pin cascade the
claim O text anticipates ("d2-typed-labels.py is byte-pinned by several
surfaces — any change keeps the D2 path byte-identical and updates pins as NEW
rows"); at this stamp the new rows have not landed. Findings:

| id | reading | cause | owner | control |
|---|---|---|---|---|
| F19-1 | `expected-v2-07.json` → exit 2, `V2F-DIGEST: 1 pinned file(s) changed since the freeze: tools/d2-typed-labels.py` (13:09:15Z) | O-seat projector change moved the pinned tool (`0da0015f…` → `76536a92…`) | O claim's re-pin cascade | re-run after the new pin row lands; the v2 packet twins must stay byte-identical |
| F19-2 | `expected-v2-07-r18.json` → exit 2, same code (13:09:15Z) | same | same | same |
| F19-3 | round-15 `expected.json` → exit 2, `V2F-DIGEST: … packet_links.py` (both stamps) | round-16 harness fix moved `packet_links.py` (`f81bc9f7…` → `66d854cc…`); documented supersession since round 16 | recorded history, no action | successor rows `expected-v2-07*.json` are the live pins |
| F19-4 | `replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` → exit 2, row 2 `gate_digest_mismatch` (`typed-pipeline-gate.py`), 10/11 reproduced | round-18 gate generalization; documented supersession, successor manifest `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` (11/11) | recorded history | round-18 re-pin manifest |
| F19-5 | round-11 v1 exercise path: **re-pointed** — `python3 tools/exercise-handoff-e2e.py --baseline reports/round-11/handoff/expected.json` → exit 2, `E2E-BASELINE: frozen baseline is missing ['expected_uncertainty_findings', 'expected_links_findings', 'expected_links_unresolved', 'twin_sha256', 'claim_ids', 'uncertainty', 'links'] — it was not written by this exercise` (13:14Z); the tool's profile is hard-coded `kotodama-handoff-e2e/3` and no `--profile` flag exists, although `design.md` §6 specified `--profile v1|v2|v3` with the v1 default | v3 impl seat re-pointed the exercise surface | impl seat / integrator (decide: implement the profile surface, or record the re-point as a design deviation) | pre-wave reading (13:01:03Z): exit 0, packet sha `6583b6bd…`; re-run after any profile support lands |

No lane byte was edited by this seat; both live reds are routed, not absorbed.

## 1. The v2 pin set — before/after (sha256, measured)

Command form (both stamps): `sha256sum <paths>` via
`.scratch/r20-d17/regcheck.py` (`--json` receipts `reg-pre.json`, `reg-post.json`).

| file | 13:01:03Z (pre) | 13:14:05Z (post v3 landing) | movement |
|---|---|---|---|
| `reports/round-15/handoff/packet-v2-05.md` | `24f9dd39bdadf05f…` | `24f9dd39bdadf05f…` | none |
| `reports/round-15/handoff/packet-v2-05.yml` | `39cf4d53b02a1a90…` | `39cf4d53b02a1a90…` | none |
| `reports/round-15/handoff/expected.json` | `b927db311370c27a…` | `b927db311370c27a…` | none |
| `reports/round-15/handoff/frozen-verify.py` | `f6e3b4ae25e821dd…` | `f6e3b4ae25e821dd…` | none |
| `reports/round-16/handoff/packet-v2-07.md` | `1295f5b35c35a0c5…` | `1295f5b35c35a0c5…` | none |
| `reports/round-16/handoff/packet-v2-07.yml` | `717e29e5aecf4c1f…` | `717e29e5aecf4c1f…` | none |
| `reports/round-16/handoff/expected-v2-07.json` | `dc75c5d7e347987e…` | `dc75c5d7e347987e…` | none |
| `reports/round-18/repin/expected-v2-07-r18.json` | `d5fda399490d47eb…` | `d5fda399490d47eb…` | none |
| `reports/round-11/handoff/expected.json` | `a94f9ded9d0938ec…` | `a94f9ded9d0938ec…` | none |
| `tools/harness/packet_uncertainty.py` | `cdcc19319269ee90…` | `cdcc19319269ee90…` | none |
| `tools/harness/packet_links.py` | `66d854cc710f0b14…` | `66d854cc710f0b14…` | none |
| `tools/gates/handoff-packet-check.py` | `e2fa3223b2aa5738…` | `e2fa3223b2aa5738…` | none |
| `tools/assemble-d4-typed.py` | `1ddad6a7da1fc27f…` | `92f5460bcc34ffbb…` | **moved (O wart closure in the adapter mirror)** |
| `tools/d2-typed-labels.py` | `0da0015f700345c9…` | `76536a924280ad41…` | **moved (O fix)** |
| `tools/exercise-handoff-e2e.py` | `a21934ade22b2cda…` | `b138723e456466fe…` (moving; `f4f8e79c…` at 13:14:45Z) | **moved (v3 rewrite)** |

Every v2 packet byte is byte-identical across the wave so far. The three moved
tools are the round's own subjects (O fix, its adapter closure, v3 exercise),
not v2 artifacts.

## 2. The v2 reading set (commands and observed exits)

| # | command (`TMPDIR=$PWD/.scratch`, lane root) | 13:01:03Z (pre-wave) | 13:14Z (post v3 landing) | reading |
|---|---|---|---|---|
| 1 | `python3 reports/round-15/handoff/frozen-verify.py` (round-15 build05 baseline) | exit 2 `V2F-DIGEST … packet_links.py` | exit 2, same | documented supersession (F19-3) |
| 2 | `… frozen-verify.py --baseline reports/round-16/handoff/expected-v2-07.json` | exit 0, `fields=16/16 glossary=20/20 findings=0 claims=15/15 links=50/50 packet_sha256=24f9dd39…` | **exit 2 `V2F-DIGEST … d2-typed-labels.py`** | **F19-1** |
| 3 | `… frozen-verify.py --baseline reports/round-18/repin/expected-v2-07-r18.json` | exit 0 (same reading) | **exit 2, same code** | **F19-2** |
| 4 | `python3 tools/harness/packet_uncertainty.py --selftest` | exit 0 | exit 0 | green |
| 5 | `python3 tools/harness/packet_links.py --selftest` | exit 0 | exit 0 | green |
| 6 | `python3 tools/harness/packet_uncertainty.py --packet reports/round-15/handoff/packet-v2-05.yml --require-oq` | exit 0, `claims=15 findings=0` | exit 0, same | green |
| 7 | `python3 tools/harness/packet_links.py --packet reports/round-15/handoff/packet-v2-05.yml` | exit 1 — `links=50 resolved=50`, findings = the two documented digest drifts (`d2-typed-labels.py`, `packet_links.py` self-pin) | exit 1, same | recorded, expected |
| 8 | `python3 tools/gates/handoff-packet-check.py reports/round-15/handoff/packet-v2-05.md` | exit 0, `fields=16/16 glossary-entries=20 findings=0` | exit 0, same | green |
| 9 | `python3 tools/exercise-handoff-e2e.py --quiet` (round-11 v1 baseline) | exit 0, packet sha `6583b6bdbf5e3fe0…`, `fields=16/16 glossary=20/20 findings=0` | **exit 2** — default: `E2E-BASELINE: frozen baseline not found: reports/round-20/handoff/expected.json` (not yet frozen); `--baseline reports/round-11/handoff/expected.json`: `E2E-BASELINE: frozen baseline is missing [twin_sha256, claim_ids, uncertainty, links, …]` | **F19-5** — the v1 path is re-pointed; the v3 baseline is a pending freeze, not a defect |

## 3. The build05 default baseline — supersession, not a defect

The round-15 baseline failed at **both** stamps on `packet_links.py` because
that harness file was fixed in round 16 (round-16 `verify.md` §5(e);
round-18 `repin/v207.md` §1). The successor rows — `expected-v2-07.json`
(round-16) and `expected-v2-07-r18.json` (round-18) — re-pinned the read set
and were green until the O change moved `d2-typed-labels.py` (§0 F19-1/2). The
supersession chain is recorded in `reports/round-18/repin/v207.md`; this seat
re-measured it rather than trusting the record.

## 4. D2 byte-identity under the O change (the claim's own control)

Measured 13:07Z, with the projector already at `76536a92…`:

| control | command | observed | recorded reference |
|---|---|---|---|
| D2 gate default | `python3 tools/gates/typed-pipeline-gate.py` | exit 0, `summary: 16/16 legs passed` | round-11 |
| D2 gate `--json` stdout | `… --json \| sha256sum` | `19765ddf2c36a7db5d71bd262079d6164b24f6222d9df83d0cefdeaeb8f47e62` | byte-identical to round-11's recorded stdout |
| D2 gate frozen row stdout | `… tools/gates/frozen/round-11/typed-pipeline/packet.d2.typed.yml \| sha256sum` | `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606` | byte-identical to `run.log` |
| D2 projection | `python3 tools/d2-typed-labels.py --check` | exit 0, "byte-identical deterministic projection" | round-8..19 |
| D2 projector selftest | `python3 tools/d2-typed-labels.py --selftest` | exit 0, `50/50 checks passed` | was 39/39 pre-fix; growth recorded |

So the D2 **outputs** are byte-identical under the O change — the regression is
in the *pins*, not the behavior. That distinction is what the re-pin cascade
must repair.

## 5. Post-landing readings (13:14Z, v3 tool landed)

- **F19-5 confirmed.** `python3 tools/exercise-handoff-e2e.py --baseline
  reports/round-11/handoff/expected.json` → exit 2, `E2E-BASELINE: frozen
  baseline is missing ['expected_uncertainty_findings',
  'expected_links_findings', 'expected_links_unresolved', 'twin_sha256',
  'claim_ids', 'uncertainty', 'links'] — it was not written by this exercise`.
  The tool's `PROFILE = "kotodama-handoff-e2e/3"` and
  `BASELINE_DEFAULT = reports/round-20/handoff/expected.json`; no `--profile`
  flag exists (`--help` measured), so the design's §6 profile surface
  (`--profile v1|v2|v3`, default v1) is not implemented. The default run is
  exit 2 `E2E-BASELINE` only because the v3 baseline is not frozen yet — a
  pending freeze, not a defect. Control: the pre-wave reading of the same
  command was exit 0 / packet sha `6583b6bd…` (13:01:03Z).
- **F19-1/F19-2 unchanged**: both v2 successor baselines still exit 2
  `V2F-DIGEST … tools/d2-typed-labels.py` at 13:14:05Z (the re-pin rows had not
  landed). Re-run command once they land:

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/r20-d17/regcheck.py --json .scratch/r20-d17/reg-post.json --label post-v3
python3 reports/round-15/handoff/frozen-verify.py --baseline <new v2 pin row, when landed>
```

## 6. Limits

- Integrity readings only: exit codes, stdout digests, pinned bytes. No canon,
  lore, source-freshness or rights verdict is made or implied.
- Mid-wave tree: every reading is stamped; the wave was still writing when the
  mid stamp was taken (§0 F19-1/2 are the wave's own in-flight state).
- The frozen replay in §0 F19-4 used `TMPDIR=/var/tmp/kotodama-r20-d17`; all
  other commands used `TMPDIR=$PWD/.scratch`.
