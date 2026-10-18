# Round 26 — SCRIBE X58 report draft

**Scope:** independent settled-tree rerun plus this draft; only `report-draft.md` and `rerun.json` are assigned to X58. **Measurement date:** 2026-10-18. **Declared baseline:** `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b` (round-25 admit); declaration HEAD `1ad491a1a4b0aef9ebdc1861dfb8237727503825`. All executions ran in isolated clones under `.scratch/r58/` after `export TMPDIR=$PWD/.scratch`. Counts below carry their commands and dates; full evidence and per-command streams are in [`rerun.json`](rerun.json). This is a rerun record and an integration draft, **not** a round-26 acceptance: the parent owns admission, shared LOG/SCORECARD integration, and the final post-integration rerun.

## Summary

The tree is **operationally green on the filed surface**, the **regression battery is 35/35 exit 0**, and the **register stratum landed during this seat's window**. The round-26 counting command reads **D pass, C pass, O fail**.

- **Preservation clean at every sample.** `python3 .scratch/r58/capture.py protect` compared all **1,328** tracked filed paths (reports rounds 8–25 plus frozen generations 8–25) to the declared baseline at **18:01:26Z**, **18:07:27Z**, **18:24:37Z** and **18:28:36Z**: **0 mismatches** each time, identical manifest `c1fe724d274ba811…`, protected status empty. No round-26 seat wrote a filed round-8–25 path.
- **Regression battery 35/35 exit 0** in the checkpoint-a overlay clone (HEAD `1ad491a` + live surfaces, 748 files, manifest `e4fa13a7…`, `copy_stable` true). Key legs: battery selftest 35/35; craft all passing; assembly selftests 42/42, 85/85, 81/81; adapters 11/11, 12/12; replay 79/79; projector **163/163**; typed gate selftest **19/19**; D2 gate 16/16 and **D4 gate 20/20**; argot gate selftest **21/21** and its D4 run exit 0; handoff v2 50/50 links, v3 105/105 links with fields 16/16, glossary 20/20, findings 0, `alias_leg=landed`. Per-command streams under `.scratch/r58/checkpoint-a-runs/`.
- **Round-26 runner executed by this seat in three overlay clones** (checkpoint-c 869 files manifest `6fe38d5b…`; checkpoint-d 870 files manifest `51bb72d4…`; checkpoint-e 871 files manifest `fab2190a…`), `--check` mode, no receipt written by this seat. The c and d reads: `acceptance_checks_passed: false`, `claim_passed {C: true, D: true, O: false}`, reproducing the filed `reports/round-26/validation.json` (sha256 `202d44bf…`) independently.
- **A historical regression was found and dated.** Two validators round-25's X40 seat filed green now read red — see the finding section below.

## Claim-by-claim state at measurement close

### D — depth (the register stratum): **LANDED, claim passes**

The register stratum arrived mid-window and is measurable end-to-end. Measured at **18:24Z–18:28Z**:

| `after_required` leg | state | evidence |
|---|---|---|
| components declare register-scoped forms with machine-readable derivation rules | **met** | `examples/culture-d4/components/04-lexicon.yml` carries 9 register/derivation tokens (was 0); `packet.d4.yml:1298` opens a `registers:` block (`QREG-01` plain …) |
| the packet regenerates deterministically | **met** | `assemble-culture-d4.py --check` → "byte-identical deterministic assembly"; `d4-assembly` exit 0 |
| the argot leg REPLAYS the register derivations and finds them clean | **met — non-empty domain** | `argot-derivation-gate.py examples/culture-d4/packet.d4.yml` → `records=170 register_scoped=14 derived_pairs=8 … violations=0 rule_holds=0`, exit 0 (was `6/0`) |
| the D4 typed gate passes with the hold set updated and named | **met** | `d4-gate` **20/20 legs** exit 0; `expected-holds.json` carries a round-26 revision note; counts `{hold: 12, note: 0, fail: 0}` agree with the projection's coverage block |
| typed labels classify the register forms | **met** | `labels_by_kind {native-form 64, translated-label 12, borrowed-strata 6}`, 82 labels, `gloss_register_labels: 0` |
| the round-17 forecast marked delivered with the delta closed | **met as the runner measures it** | `reports/round-26/register/` (design, forms, rules, impl, 4 executions, review) names the delivery and the delta |

The runner's own independent replay (never read back from the gate) re-derives **8/8** delivered pairs with every base resolving in the same packet and no self-derivation: `L-55..L-62` in the `stamp` register, operations `reverse` ×2 and `lengthen` ×6. The gate's teeth are exercised by a runner-authored violating pair (emits the argot id, exit 1) with a clean counterpart (exit 0).

**One thing the parent should weigh.** The forecast named `head2`/`reverse`; the delivered set is `reverse` + `lengthen`, and `head2` appears in `morphology_derivation_ops` but on no delivered pair. The runner accepts "the designed equivalents" as the claim allows. That is a reading of the claim, not a defect — but it is the reading, and the parent may want to confirm it.

### O — operability (the three round-25 remainders): **claim FAILS**

The disposition **shape** is right — new rows, filed bytes untouched, controls in both directions — but `after_required`'s last two clauses are not met.

- **r4 twin gap — dispositioned by a new row.** `reports/round-26/remainders/r4-twin/` lands `packet.md`-projected `twin.json` (103,975 B) + `expected.json` + `freeze.txt` + `build-twin.py` + `verify-twin.py`. The filed `reports/round-25/v3-supersession/declared-in-r4/` directory is unchanged (`has_twin: false` in the runner's own `revision_rows` census), so the gap closes by append, per convention. The twin passes `packet_uncertainty.py` (exit 0, 27 claims, 0 findings) and `packet_links.py --no-digests` **106/106 links, 0 findings**; with digests it reports 6 `M-DIGEST-MISMATCH` rows, which is the pin cascade below, not a structural defect. *Note on an in-flight reading:* this seat's checkpoint-c caught the twin directory mid-write (files stamped 15:13–15:21) and recorded a spurious `packet_links` red; the checkpoint-d read clears it. The failure was transient, not real.
- **The two pin tails — re-pointed as new rows, and the checker is still red.** `reports/round-26/remainders/{v2-successor-r26,v3-baseline-r26}/` land as new rows with the filed round-20 rows byte-identical; `filed-rounds-8-25-unchanged` passes. But the bound checkers are **not green**: `pin-repoint-check.py --check` reads **16/17 controls, `passed: false`**, and the round-25 r4 checker reads **51/52, exit 1**, its red naming the stale round-20 rows *plus* `D4 gate legs summary: 20/20 legs passed != 19/19`.
- **Regressions — one red.** `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` exits **1** with `E2E-DIGEST: 6 read-set file(s) changed since the baseline was frozen` (`01-brief.yml`, `04-lexicon.yml`, `expected-holds.json`, `packet.d4.yml`, `packet.d4.typed.yml`, `typed-labels.d4.yml`). This is the **fresh** cascade the D landing created, not a round-25 remainder — the v3 baseline was frozen against pre-register D4 bytes.
- **A second, unfiled O problem: a dual-landing.** The v3 baseline row exists at **both** `reports/round-26/register/v3-baseline-r26/` and `reports/round-26/remainders/v3-baseline-r26/`, both carrying `expected.json` + `twin.json` + `packet.md`. The runner's `revision_rows` census lists both. Whether that is a deliberate D-side re-pin plus an O-side remainder row or an accidental duplicate is the parent's to settle.

**The D/O interaction is the substance here.** The round-26 D seat's write to `examples/culture-d4/` invalidated the O seat's re-pointed v3 row within minutes, and the r4 checker's red is produced by the D seat's new `L3b-argot` gate leg (20/20) — not by the tails the checker names. An O seat cannot make that checker green. `reports/round-26/audit/o39-o40-remainder-fixes-adversarial.md` reaches the same conclusion independently ("the r4 checker's red is caused by a different seat's D-claim delivery … reported, not absorbed").

### C — coverage (the open-question queue): **claim passes**

**49/49 queue rows dispositioned, 100%, zero undispositioned.** The runner measures `queue_rows: 49`, `dispositioned: 49`, `undispositioned: 0`, drawn from 11 disposition sources (`dispositions.json`, `C41.md`–`C46.md`, `audit.json/md`, `verify.json`, `dispositions.md`). Every `carried` row carries an owner, a reason and a `next_touch_round` (27 on 60 rows, 26 on 18). The wider ledger in `dispositions.json` reads 78 rows across both surfaces (the README queue plus the round-25 lessons census, 8 ids overlapping).

The lessons README revision requirement is met: the filed `corpus/lessons/README.md` is byte-unchanged from the baseline (`29,059 B`, sha256 `ec7469da…`, mtime 14:47 — pre-dispatch), and the new revision lands at `reports/round-26/lessons/C51-C52.md` + `C53.md`.

**Contested, reported not absorbed.** The independent index audit `reports/round-26/audit/x63-lessons-audit.md` finds the round-25 index prose stale on six readings that were true at its stamp (`X63-G1`: the round-12 and round-21 pointers, Q-04-1's status, Q-23-1..3's status), a cross-tool disagreement (`X63-D2`), and **no row for round 24**. The dispositions mark exactly those rows `fixed-with-evidence`. Both artifacts are filed; reconciling them is the parent's.

## Historical regression found: r22 and r23 now read red

**This seat's r19–r24 rerun does not reproduce round-25's X40 picture.** Two validators X40 filed exit 0 / acceptance true now read exit 1:

| round | X40 (r25) | X58 (r26) | runner sha8 |
|---|---|---|---|
| r19 | exit 0, `acceptance: False ['C entries']` | exit 0, same | `5b27a80d` (identical) |
| r20 | exit 1, O/C pass, D fail (3 failures) | exit 1, same 3 + a 4th (`20/20 != 19/19`) | `2b7a252b` (identical) |
| r21 | exit 1, O pass, C/A fail | exit 1, same | `938cddee` (identical) |
| r22 | **exit 0, acceptance true** | **exit 1**, C pass, D/O fail | `3af74c2b` (identical) |
| r23 | **exit 0, acceptance true** | **exit 1**, D pass, O fail | `ae897cb8` (identical) |
| r24 | exit 0, acceptance true | exit 0, acceptance true | `ba3b18a7` (identical) |

**Root cause, dated by revision control.** `fc13cd2` (the round-25 admit) grew `tools/gates/typed-pipeline-gate.py` by 295 lines and the D4 profile's leg count from 19 to 20. `reports/round-22/run-validation.py:703` requires the D4 summary to reproduce `(19, 19)`; at `fc13cd2` the gate emits 20/20, so r22's D claim goes red. Controls in isolated clones, runner bytes identical in both arms:

- `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → **19/19** at `f74fc94`, **20/20** at `fc13cd2` (selftest 12/12 → 19/19).
- `reports/round-22/run-validation.py` → **exit 0, acceptance true** at `f74fc94`; **exit 1, acceptance false** at `fc13cd2`.
- r20 gains the same `20/20 != 19/19` line as a fourth failure.

**The r23 arm is not cleanly attributable by this seat and is reported as such.** r23's runner calls `live_lane()` and syncs the live round-23 surface into its clone, so the pre-admit control also reads red on an unrelated D4 profile pin (`L1-profile: packet/projection/expected pins … live`), and my clone rerun is not fully isolated. The r22 divergence is clean; the r23 one is *consistent with* the same cause but not proven by my control.

Disposition is **parent-owned**: whether the historical 19/19 pins move as new rows or the reds stand as filed history is a decision this seat does not make.

## Limits and handoff

- **No round admission asserted.** The round-26 runner existed only from ~18:22Z; this seat ran it `--check` in isolated clones only, wrote no receipt, and refreshed no filed receipt. The filed `reports/round-26/validation.json` (sha256 `202d44bf…`) was produced by another seat; this seat's two independent reads reproduce its verdict.
- **The tree moved throughout.** `reports/round-26/` went 2 → 32 → 92 → 94 files between 18:00Z and 18:28Z; the register stratum landed ~18:18Z and the O-side v3 row went stale within ~3 minutes of landing. Every number binds to its stated snapshot; the regression battery binds to checkpoint-a bytes only.
- **One transient reading is disclosed rather than hidden:** checkpoint-c recorded `packet_links` red over `r4-twin/twin.json` while that directory was being written; checkpoint-d clears it.
- **O fails as the runner measures it**, with two distinct causes: the fresh v3 pin cascade from the D landing (a regression), and two checker controls that do not pass. The twin leg itself is met.
- **D passes as the runner measures it**, with one reading to confirm (`head2` vs `lengthen`).
- **C passes as the runner measures it**, with an independent audit contesting the index prose on six rows.
- **Fleet root is not clean.** The round-26 scope watch (`reports/round-26/scope.md`, SCRIBE X57) discloses the same two debris families round 25 named, byte- and mtime-identical and predating round-26 dispatch. The "fleet root clean" clause **fails as observed**; this seat concurs and asserts no disposition.
- **Protected-surface limit.** Tracked bytes and file modes only; a clean observation does not exclude a transient write-and-restore between samples, and ignored logs have no committed baseline identity.
- All artifacts are **NON-CANON** engineering evidence. No source-freshness certification, rights clearance, lore acceptance or promotion is claimed. No commit, no push, no shared bookkeeping, no filed-round write by this seat. Scratch: `.scratch/r58/{capture.py,clone.py,historical.py,assemble.py,protect2.py,protected-*.json,checkpoint-{a,b,c,d,e}*,r26-checkpoint-{c,d}.json,r25-checkpoint-b.json,historical-validators.json,controls.json,r19..r24,ctl*}` and `.scratch/r58-commands.json`.
