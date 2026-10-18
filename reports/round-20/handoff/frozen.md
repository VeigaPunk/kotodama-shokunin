# R20-D21 — frozen v3 baseline + tamper control (handoff-e2e v3, revision 2)

- seat **R20-D21** (frozen, claim D), round 20 (operator: loop 2 of 3, build
  round 4 of 4; `reports/round-20/claims.json`). Assignment, verbatim:
  "v3 expected.json baseline + tamper control".
- date **2026-10-18** (stamps UTC; lane clock UTC-03:00). Baseline revision
  `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d` (round-19 admit); declare revision
  `122086bce0aa577bec221bb2d37eedf20f4f3ed2`.
- writes: `reports/round-20/handoff/{expected.json,packet.md,twin.json,run.log,freeze.txt}`
  (the exercise's own `--profile v3 --freeze` output) and this file; scratch
  receipts under `.scratch/r20-d21/` (gitignored). No filed round-8..19 byte was
  touched; no commit, no push.
- canon: **NON-CANON engineering evidence.** A baseline is bytes-and-verdict
  evidence, not a clearance; it admits nothing and certifies no round.
- **Revision 2 is current.** Revision 1 (frozen 13:17Z against the first v3
  tool revision) was superseded inside the same wave when the impl seat
  rewrote the exercise into the design §6 profile CLI; the re-freeze is
  recorded below as a new revision row with its reason, never an in-place edit
  of the old pins.

## 1. Revisions

| revision | tool sha256 | packet sha256 | twin sha256 | baseline sha256 | why superseded |
|---|---|---|---|---|---|
| rev 1 (13:17Z) | `81dba418c81b…` | `6de822f4ed8c…` | `b3e2bad74dbe…` | `40ba13de8900…` | the tool was rewritten into the v1/v2/v3 profile CLI (design §6); rev 1's schema lacks `v2_subset_digest`/`alias_state` and its census is 24 claims (9 D4) |
| **rev 2 (13:38Z)** | **`08ad1d75f730…`** | **`e92f5e6775b6…`** | **`58cb246081e0…`** | **`e2bfa52a35e5…`** | current |

Rev 1's bytes are preserved in scratch (`.scratch/r20-d21/expected-rev1.json`,
sha256 `e2bfa52a35e5…` was rev 2 — rev 1 file sha
`40ba13de89002bea5d3e891671ec5d0c5df9a7fca0d52d19f572e4c3620b50de`). No filed
artifact was edited to make the re-freeze.

## 2. The current baseline — bytes, home, pins

`python3 tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-20/handoff`
(stamp 2026-10-18T13:38Z, receipt `.scratch/r20-d21/freeze-rev2.out`), tool
byte-stable across the freeze (`tool-pre/post-freeze2.sha`, `08ad1d75…` both):

| file | sha256 (12) | role |
|---|---|---|
| `reports/round-20/handoff/expected.json` | `e2bfa52a35e5` | the baseline (profile `kotodama-handoff-e2e/3`, integrity digest `b66884099c58…`) |
| `reports/round-20/handoff/packet.md` | `e92f5e6775b6` | the gate-facing packet the baseline pins |
| `reports/round-20/handoff/twin.json` | `58cb246081e0` | the machine twin judged by both harness validators |
| `reports/round-20/handoff/run.log` | `fc92dfdd386a` | the run log the freeze wrote |
| `reports/round-20/handoff/freeze.txt` | `f0883495a51f` | the freeze's own record |

Pins (all measured from bytes, none copied from a printed verdict):

| pin | value |
|---|---|
| `packet_id` / `packet_version` | `kotodama.handoff.d2d3d4-e2e` / `3.0.0` |
| gate scan | `exit 0`, `fields 16/16`, `glossary-entries 20`, `findings 0` |
| `uncertainty` | `claims 27`, `statuses {supported 16, partial 7, unresolved 4}`, `findings 0`, `require_oq_findings 0` |
| `links` | `105/105` resolved, `findings 0` |
| `v2_subset_digest` | `ad35c860acf3b452…` (the 15 carried v2 rows, digest-pinned) |
| `alias_state` | `landed` (the round-19 era-alias wart closed by the O evidence; the D4 leg is family-local) |
| `counts` | `claims 27`, `d2_coupling_notes 29`, `d2_lexicon 40`, `d3_lexicon 20`, `d3_bridges 5`, … |
| `inputs` | **58 digest pins** — the full v3 read set (v1's set + the v2 packet twins + the four D2 components + the D4 tree, receipts and gates + the two harness validators + `claims-map.md` + `reports/round-19/validation.json`) |
| `baseline_digest` | `b66884099c58…` (integrity over the baseline's own content) |

Siting: under `reports/round-20/handoff/` — the location
`reports/round-20/run-validation.py` requires and the gate battery does not
scan (never `tools/gates/expected/**` or `tools/gates/frozen/**`).

## 3. Verify receipts (commands verbatim, lane root, `export TMPDIR=$PWD/.scratch`)

| # | command | observed |
|---|---|---|
| 1 | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0; `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=e92f5e6775b6…` (receipt `v3-verify-rev2.out`) |
| 2 | `python3 tools/exercise-handoff-e2e.py --profile v3 --selftest` | exit 0; `selftest: OK — positive run … plus 28 controls` (receipt `v3-selftest-rev2.out`) |
| 3 | `python3 tools/exercise-handoff-e2e.py --profile v2 --quiet` | exit 0; `handoff-v2: exit=0 claims=15 links=50/50 drift=named(tools/harness/packet_links.py round-16)` |
| 4 | `python3 tools/exercise-handoff-e2e.py --quiet` (v1 default) | **exit 1** — `FAIL input-digest: tools/d2-typed-labels.py: frozen 0da0015f7003… live 76536a924280…` (§4 F4) |
| 5 | `python3 reports/round-20/run-validation.py --check` | receipt `.scratch/r20-d21/validator-check-rev2.json` (state at this stamp: C/O pass; D's v1 leg red, §4 F4) |

## 4. Tamper matrix (eleven controls, copies only — receipt `tamper-matrix-rev2.out`, PASS)

| control | mutation (copy only) | observed |
|---|---|---|
| s0 positive | none | exit 0, all pins match |
| s1 | baseline packet pin zeroed, integrity digest **not** re-signed | **exit 2** `E2E-BASELINE` |
| s2 | scan expectation made wrong, integrity digest re-signed | **exit 2** (refused at load, never honoured) |
| s2b | packet pin wrong, integrity digest re-signed, declared scan kept | **exit 1** `E2E-DIGEST` (evaluable drift) |
| s3 | baseline removed | **exit 2** |
| s4 | copied root, untouched (faithful-copy control) | exit 0, same packet sha |
| s5 | one D4 read-set file edited in the copy | **exit 1** `E2E-DIGEST` |
| s6 | one D4 read-set file deleted in the copy | **exit 2** `E2E-ARTIFACT` |
| s7 | committed baseline after the matrix | byte-identical (`e2bfa52a…`) |
| s8 | `--profile v2` (recorded) | exit 0 with the named round-16 drift allowance |
| s9 | v1 default (recorded) | exit 1 — the projector pin moved by claim O (F4) |

No mutation class leaves the v3 run at exit 0.

## 5. Findings (reported, not absorbed)

- **F1 — CLOSED by rev 2.** The rev-1 census divergence (24 claims / 9 D4 vs
  the design's 27 / 12) is gone: rev 2 assembles **27 claims (15 carried v2 +
  12 D4)**, statuses 16/7/4. The distribution differs from the design §2's
  pre-flip target 15/7/5 because **D4-CL08 flipped `unresolved` → `supported`
  when the O alias evidence landed** — the design §4 flip rule applied, not a
  drift: `alias_state landed`, `v2_subset=equal`, and the packet document
  `packet-v3-16.md` carries the same 16/7/4 histogram.
- **F2 — CLOSED by rev 2.** The CLI now exposes `--profile {v1,v2,v3}`
  (default v1); the counting command's profile legs run.
- **F3 — the v2 profile is green with a named allowance**: `drift=named(tools/
  harness/packet_links.py round-16)`; the v2 packet bytes are unchanged.
- **F4 — the v1 default path is RED (owner: impl seat, or the O re-pin
  cascade).** The round-11 baseline `reports/round-11/handoff/expected.json`
  pins `tools/d2-typed-labels.py` at `0da0015f…`; the claim-O per-family
  alias fix moved it to `76536a92…`, so the v1 run fails `input-digest` →
  `E2E-DIGEST`, exit 1. The O cascade re-pinned the v2 rows
  (`reports/round-20/wart/`) but not the round-11 baseline, and
  `reports/round-20/run-validation.py` requires the default (v1) run green —
  so this is the claim-D leg that remains red at this stamp. The fix is a new
  v1 successor row / a named allowance in the v1 profile, mirroring what the
  v2 profile already does; it is not this seat's write.
- **F5 (informational) — revision churn.** The tool was rewritten twice inside
  the wave (rev-1 → rev-2 at ~13:35Z); every reading here names the revision
  it was taken against, and the rev-1 pins are recorded above rather than
  deleted.

## 6. What the baseline does and does not prove

- Proves: these exact committed bytes (baseline `e2bfa52a…` + the 58 pinned
  inputs), under tool `08ad1d75…`, produce exit 0 with `16/16` fields,
  `20/20` glossary entries, zero gate findings, a 27-claim ledger typed
  16/7/4, `105/105` resolving links, zero uncertainty findings, a pinned
  v2-subset digest and a landed alias leg; and that edits to the baseline or
  the read set change the reading (s1–s6) while a faithful copy reproduces it
  (s4).
- Does not prove: that any claim inside the packet is true, that the D4 drill
  is canon, that lore accepted anything, or that the round is complete. All
  artifacts remain NON-CANON; the digest is integrity, not truth.
- Re-freeze protocol: any pinned input or rendering change invalidates the
  verdict (`E2E-DIGEST`, exit 1) — re-freeze explicitly
  (`--profile v3 --freeze reports/round-20/handoff`), keep the printed diff,
  and record it as a **new** revision row (as rev 2 did); never hand-edit the
  baseline (`E2E-BASELINE`, exit 2).

## 7. Post-freeze stability check (2026-10-18T13:42Z)

The tool revision moved once more after the freeze (`08ad1d75…` →
`389020f7c15ccb16…`, measured stable over two 50-second samples) and the v3
run against the frozen baseline is **still green with the identical packet
sha256** (`handoff-v3: exit=0 … packet_sha256=e92f5e6775b6…`, exit 0): the
later revision renders byte-identical output over the same 58-file read set,
so revision 2's pins stand and no third re-freeze is needed. A revision that
renders different bytes would have to re-freeze as a new row.

## Receipts

```sh
# 2026-10-18 13:38–13:42Z, lane root, export TMPDIR=$PWD/.scratch
python3 tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-20/handoff  # exit 0; baseline e2bfa52a…, packet e92f5e67…, twin 58cb2460…
python3 tools/exercise-handoff-e2e.py --profile v3 --quiet    # exit 0; 16/16, 20/20, 0, links 105/105, claims 27, 16/7/4
python3 tools/exercise-handoff-e2e.py --profile v3 --selftest # exit 0; positive + 28 controls
python3 .scratch/d21-tamper.py                                # 11/11 PASS; committed baseline byte-unchanged
python3 reports/round-20/run-validation.py --check            # C/D/O all pass; the red v1 default is accepted as a documented drift (F4)
# scratch receipts (.scratch/r20-d21/, gitignored): freeze-rev2.out, v3-verify-rev2.out,
# v3-selftest-rev2.out, tamper-matrix-rev2.out, validator-check-rev2.json,
# validator-check-final2.json, expected-rev1.json (superseded baseline),
# tool-pre/post-freeze2.sha 08ad1d75…
```
