# R10-O11 — verifier: O04 (idx 2, 10) and O05 (idx 3, 11)

- seat: **R10-O11** (findings verifier), round 10 (loop 1 of 3, build round 3 of 4), 2026-10-17
- assignment (verbatim): "FINDINGS R10-O11 (verifier): O04+O05. reports/round-10/findings-verify-2.md."
- write scope: **this file only**. No tracker row, fixer fragment, tool, pin, packet, corpus or SCORECARD byte was written by this seat. Scratch: in-lane `.scratch/r10o11/` (`export TMPDIR=$PWD/.scratch` before every scratch-writing command; `/tmp` never used). No commit made.
- worktree at verification: HEAD `e3a1ec9435787328ac9f828f96cb6390e4916b8f` + untracked `.scratch/`; declared round-10 baseline `9dc18ec1339bffd6f81e74f1a5742464ef578749`. All commands below ran from the lane root on 2026-10-17, verification window 21:33Z–21:40Z.
- method: read both fixer fragments, then **re-ran every control they cite** on the live tree and re-measured every digest/token independently (no fragment value was accepted by quotation). Where a fixer's number and mine disagreed I report the disagreement rather than smoothing it.
- canon: NON-CANON engineering evidence. Nothing here adjudicates canon, real-world rights, or game mechanics.

## 0. Rows verified, and how the seat→row mapping was established

| fixer | fragment | tracker rows verified |
|---|---|---|
| R10-O04 | `reports/round-10/fix-04.md` | **idx 2** = R9-D09 S1 (re-pin record) · **idx 10** = R8-D16 S12 (strict-loader fragment) |
| R10-O05 | `reports/round-10/fix-05.md` | **idx 3** = R9-D10 F2 (D3 frozen pin red) · **idx 11** = R8-D16 S13 (pins/locators invalidated) |

The mapping was not assumed: the tracker was compiled after the wave launched, so the fixers
used the fallback rule ("the i-th and i+8-th findings", `reports/round-10/targets.json`), and
three fixer-authored control scripts state their row explicitly, which fixes the formula
`O(2+j) → idx j, j+8` (0-based):

- `.scratch/o02/control-f-d17-2.py:2` — "R10-O02 control for finding idx 8 (R8-D17 F-D17-2)" (j=0 → idx 8)
- `.scratch/fix07/check_s10.py:1` — "R10-O07 control for tracker idx 5 (R8-D16 S10)" (j=5 → idx 5)
- `.scratch/fix07/probe_s5.py:1` — "R10-O07 probe for tracker idx 13 (R9-D09 S5)" (j=5 → idx 13)
- `.scratch/r10o09-superset-census.py:2` — "R10-O09 control for tracker idx 7 (R9-D09 S3)" (j=7 → idx 7)

Hence O04 (j=2) → idx 2 and 10; O05 (j=3) → idx 3 and 11. Both fragments state the same rows
(fix-04.md:9-13; fix-05.md:5), and the tracker's own `ordering` note
(`reports/round-10/findings-tracker.json:52`) is consistent. Tracker read at verification:
sha256 `3bfd40181ca98c830ef1042b23c3e446328b915ced9773dbc12b431d6b22d353`.

## 1. O04 — `reports/round-10/fix-04.md`

### 1.1 idx 2 (R9-D09 S1) — disposition claimed `fixed-with-control`: **VERIFIED, 7/7 record items**

Every item of the S1 minimum record was re-measured by this seat:

| # | S1 item | my independent re-run (2026-10-17) | verdict |
|---|---|---|---|
| 1 | pre-refresh freeze token | `git show a7bb205:examples/culture-d3/expected.json \| sha256sum` → `74496aa8aa7db2d7…d5080` | match |
| 2 | three keys old→new + causing commit | my own `json` load of `9dc18ec^` vs `9dc18ec`: **exactly 3** manifest values changed (`50c4c2f2→5f4c02bf`, `29a9361c→e6bffd70`, `8c5afb0a→d9e4e8f4`); `git log --oneline -1 -- <each path>` → `e1694ba` for all three | match |
| 3 | verdict-preservation differential | round-7 gate bytes extracted (`git show 57c3ce6:…` → sha `8c5afb0a…`/`29a9361c…`, equal to the old pins); old vs current gates on `examples/culture-d3/packet.gates.yml`: **stdout byte-identical** (`cmp`), exits 1/1; naming `506d163231051f294b221d1bb46f78605a689a834ece776b65847a4dc5e3f386`, costume `40d4048c326e10373b8466cb668d51e92a5733668c9e5789533aae8143b63c64` — both hashes equal O04's | match |
| 4 | byte-level no-change traversal | `python3 tools/assemble-culture-d3.py --check` exit 0 ("byte-identical deterministic assembly"); `git status --short -- examples/culture-d3` empty; independent `hashlib` sweep of the freeze's own manifest (no guard code): **24 entries, 0 mismatches** | match |
| 5 | `expected_exit`/`finding_ids` unedited | both `0` / `[]` pre and post; 24 manifest entries both sides, none added/removed; `profile`, `declared_expectation`, `coverage`, `limits` identical | match |
| 6 | stamped revision + date | `LOG.md:2972-2978` (round-9 entry, "D3 pins refreshed"); post-refresh token `562b76cb…` at `reports/round-9/validation.json:24` and `:991`; claims.D `passed: true`, `frozen_replay.exit 0`, `finding_ids []`, `drift_paths []` | match |
| 7 | independent re-run by a different shard | this verification run + O04's own re-run (both non-re-piner seats) | match |

Frozen-run receipt re-measured: exit 0, raw stdout sha256
`e282a0688498034144fb376ab43884c8607133bd6deaab763150d789b113669d` — identical to the value
claimed by both fix-04.md:34 and fix-05.md:31.

### 1.2 idx 10 (R8-D16 S12) — disposition claimed `fixed-with-control`: **VERIFIED, controls A/B/C**

| control | O04's claim | my re-run | verdict |
|---|---|---|---|
| A | `grep -c '^ *-$' examples/culture-d2/packet.d2.yml` → 312 | 312 | match |
| B | filed §4.1 fragment (extracted, 302 lines) refuses: exact case → `P-UNTERMINATED-FLOW` line 2; real packet → `packet: None`, first refusal line 82 | I re-extracted the fenced block myself (`.scratch/r10o11/loader_frag.py`) and ran it: exact case → identical finding; real packet → `None`, refusal line 82 (`"content '-' is not a mapping line"`) | match |
| C | shipped loader (tool sha `0da0015f…`) parses both cases | `sha256sum tools/d2-typed-labels.py` = `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` = `git show e1694ba:tools/d2-typed-labels.py`; importing the tool and calling `load_packet_strict`: exact case → `{'packet': {'costumes': [{'id': 'GAR-01'}]}, 'findings': []}`; real packet → `packet` not None, **0 findings**, 19 top-level keys, 10 costumes, 40 lexicon | match |
| delta | fragment lines 190/194 accept only `startswith("- ")`; shipped `_parse_block` accepts a bare item (`:287 first[1] == "-"`, `:291 body == "-"`) | line-level read confirms both branches verbatim | match |

Supporting: `--selftest` **39/39 exit 0** (my run), including `loader: P-UNTERMINATED-FLOW
refused`; the live run exits 1 with 16 findings total (15 hold + 1 note) and no `P-*` code —
O04's "16 findings" figure reproduces under the run's own total.

**Disposition judgment.** "fixed-with-control for the shipped artifact, filed fragment
documented as residual" is the correct shape: the finding's own remedy was "do not land §4.1
as-is", the shipped loader never carried the defect, and the filed fragment bytes stay frozen
per the lane's correction-as-new-entry rule. No live artifact carries the defect (independently
reproduced).

### 1.3 Open item for the integrator (not a defect in the fragment)

fix-04.md explicitly proposes its two tracker rows but does **not** write them ("for the
integrator; I did not edit the tracker", fix-04.md:128). At my verification close (21:36Z) the
tracker still read **`pending` for idx 2 and idx 10**, while O05's rows (3, 11) were applied.
The harness's zero-pending check (`reports/round-10/run-validation.py:790-793`) will fail until
the integrator applies O04's two proposed rows. The dispositions themselves are verified above;
only the write is outstanding.

## 2. O05 — `reports/round-10/fix-05.md`

### 2.1 idx 3 (R9-D10 F2) — disposition claimed `fixed-with-control`: **VERIFIED**

- Frozen re-run exit 0, stdout sha256 `e282a068…` (match, §1.1) — the pin that F2 filed red is green.
- Independent manifest sweep, no guard code: 24 entries, 0 mismatches (match).
- Pre-refresh anchors re-read: `reports/round-9/d3/evidence-coupling.md:16` and
  `reports/round-9/baselines/handoff-packet-check/packet.md:65` both carry `74496aa8…` (match).
- Three-key table with causing commit re-read at `reports/round-9/d3/check-diagnosis.md:74-75` (match).
- Verdict-preservation differential re-run independently by me: byte-identical, hashes and
  exits as §1.1 item 3 (match).
- `expected_exit`/`finding_ids` unchanged pre/post (match); stamped revision `9dc18ec` +
  `LOG.md` + `validation.json` post-refresh token (match).
- **Fail-closed control of my own** (not in the fragment): flipping one declared digest in a
  scratch copy of the freeze → `--frozen` exit 2, `D3-SNAPSHOT` "manifest digest mismatch …
  declared 000…0, actual d9e4e8f4…". The guard still fails closed after the re-pin.
- §1.4 residual independently confirmed: the re-pin **is not** a three-line edit — indentation
  2→1 space per level and the trailing newline was dropped. One precision note: "34 → 33 lines"
  (fix-05.md:74) is the `wc -l` reading (`wc -l`: 34 → 33); by `splitlines()` the count is
  **34 → 34** (the post-pin last line is simply unterminated). The substance — re-serialization
  beyond the three values, semantically identical — is correct and correctly flagged as a
  caveat no acceptance ledger may omit.

### 2.2 idx 11 (R8-D16 S13) — disposition claimed `fixed-with-control`: **VERIFIED**

| claim | my re-run | verdict |
|---|---|---|
| pins resolve at `291c714` | `git show 291c714:…era-language-staging.md \| sha256sum` → `226e1104…52da` (the pin, exact); `…loanword-material-dating.md` → `bb08d458…6fd8` (the pin, exact) | match |
| current bytes | HEAD and worktree both `621b7a33…1da8` / `5b1d75ab…4d58` | match |
| locators at `291c714` | `:44` = "Separate **ultimate etymon** from **immediate donor** and **carrier**…"; `:54` = the donor-innovation row — matching S13b's correction | match |
| +3 shift is the metadata sweep | `git diff --stat 291c714 e1694ba -- …loanword-material-dating.md` → `3 insertions(+)` | match |
| (c) churn record not-a-defect | `sha256sum examples/culture-d2/components/11-costumes.yml` → `b6e2c5c2…3f22` (the "bytes were" side) | match |
| no live consumer | `grep -c 'secondary_entries_sha256_before' tools/check-craft-exercise.py` → **0**; `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` → exit 0 | match |

Scope nuance on the sweep: my wider sweep (`grep -rn "226e1104\|bb08d458"` over `*.json/*.py/*.md`)
found the one live-input file O05 names plus four **report-file** hits
(`reports/supplement-opencode-1/32-craft-exercise.md:27`,
`reports/supplement-opencode-1/inventory-after.json:2438,2486`,
`reports/round-8/depth/skill-table-draft.md:316`) — all filed records, none a live pin or a
checker input. O05's "exactly one live-input file" holds as scoped; the wording is precise, the
sweep is reproducible.

Tracker rows 3 and 11 re-read: `fixed-with-control` with `control`, `control_command`, `note`,
`verified_at`, `verified_by` — labels inside the harness vocabulary
(`run-validation.py:104-108`), evidence fields satisfying the `:764-779` text rule.

### 2.3 Adjacent measurement for idx 4 (S6) — **independently reproduced**

O05's §3 byproduct (not its disposition) is correct on every point I re-measured:
`sha256sum .scratch/o05/packet-native-inject.d2.yml` → `2a79a893d7c0be3e…`; my own full JSON
walk of `--json` base vs mirror finds **exactly 1** difference (`/packet` path echo; base
`880d0e45…`, mirror `8cfa555b…`); `grep -rn 'native_form' examples/culture-d2/` → **0**. My
independent GAR-01 injection test (§4) agrees: the supplied `native_form` channel does not exist
in the corpus and the key is not read by tool revision `0da0015f…`. This is evidence *for* idx 4
(another seat's row), not a disposition.

## 3. Corrections and new observations (mine; none of these changes a verified disposition)

1. **Self-correction (my own earlier reading).** An initial pass read `replay-frozen.py
   tools/gates/frozen/round-3/MANIFEST.tsv` as exit 0 because `$?` was captured after a pipe
   (`| tail`). Re-measured without a pipe: **exit 2**, `REPLAY COULD-NOT-EVALUATE: 7
   could-not-evaluate` (`gate_digest_mismatch`, `provenance-audit.py`), matching drift shard-09's
   row. Recorded because a verifier's own false reading is evidence too.
2. **Runner hash convention (explains a non-discrepancy).** `reports/round-9/validation.json`
   records `frozen_replay.stdout_sha256 = c8d1a7b9…`, not the raw-pipe `e282a068…`. Cause found:
   the runner hashes `sanitize(stdout)` (`run-validation.py:234-242`, whitespace collapsed). Same
   verdict (exit 0, `findings: []`); no conflict with either fixer's receipt.
3. **Stale freeze token in documentation (new observation, no tracker row).**
   `examples/culture-d3/README.md:34` and `:91` and `corpus/lessons/round-9.md:169` still cite
   `74496aa8…` as the freeze token; the live token is `562b76cb…`. The README is deliberately
   outside the freeze manifest ("handoff/README deliberately excluded"), so this is
   documentation-only staleness — flagged for the round-10 scribe/orchestrator, not absorbed here.
4. **The re-pin's residual is real but bounded.** Independently confirmed (§2.1). Any future
   record of a re-pin must carry the re-serialization caveat; the S1 record test passes
   semantically (3 values, expectation untouched), not textually.

## 4. My own independent measurements behind the S6 cross-check (kept for idx 4's owner)

Injected `native_form: "vintervalley"` (contains `/v/`, not in the declared inventory) into
GAR-01 of a scratch copy of `examples/culture-d2/packet.d2.yml`; the tool's findings list,
stats (`fail 0, hold 15, labels 58, note 1`) and exit (1) are **byte-identical** to the baseline
run — the supplied form is not read (agrees with fix-04.md Appendix A, fix-05.md §3, and R8-D16
S6 as filed). Scratch: `.scratch/r10o11/packet-s6.yml`, `base.json`, `inj.json`.

## 5. Limits

- I verified only O04's and O05's rows (idx 2, 3, 10, 11) and the byproduct they offered for
  idx 4. No other tracker row, and no other seat's fragment, was assessed here.
- Verdicts are pinned to the revisions and hashes named above; a later edit to any cited file
  invalidates the corresponding row of this verification and requires a re-run.
- The re-pin act itself (round 9) and the round-8 repairs remain the orchestrator's and
  round-8's own audit's to certify; this file verifies the *records and controls*, not history.
- Out of province and not assessed: any canon decision, real-world rights, or game mechanics.

## 6. Reproduction

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
# idx 2 / idx 3 — the re-pin record and the green frozen leg
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json \
        --frozen examples/culture-d3/expected.json          # exit 0, stdout sha256 e282a068…
git show a7bb205:examples/culture-d3/expected.json | sha256sum            # 74496aa8…
git show 291c714:corpus/knowledge/synthesis/era-language-staging.md | sha256sum   # 226e1104… (S13 pin)
git show 291c714:corpus/knowledge/synthesis/loanword-material-dating.md | sed -n '44p;54p'
git diff --stat 291c714 e1694ba -- corpus/knowledge/synthesis/loanword-material-dating.md
git show 57c3ce6:tools/gates/naming-collision-gate.py > .scratch/n-r7.py
python3 .scratch/n-r7.py examples/culture-d3/packet.gates.yml | sha256sum  # 506d1632…, exit 1
python3 tools/gates/naming-collision-gate.py examples/culture-d3/packet.gates.yml | sha256sum  # same
# idx 10 — loader fragment vs shipped loader
grep -c '^ *-$' examples/culture-d2/packet.d2.yml          # 312
sha256sum tools/d2-typed-labels.py                          # 0da0015f… = git show e1694ba:…
python3 tools/d2-typed-labels.py --selftest                  # 39/39, exit 0
# verification scratch (this seat)
ls .scratch/r10o11/                                         # loader_frag.py, control_drive.py, v2-*.out/json
python3 .scratch/r10o11/control_drive.py                    # 19 controls re-driven, exits all match
```

FILES: reports/round-10/findings-verify-2.md | SUMMARY: Verifier R10-O11 re-ran every control in fix-04.md (O04: idx 2 R9-D09 S1 re-pin record 7/7 items and idx 10 R8-D16 S12 loader fragment-vs-shipped) and fix-05.md (O05: idx 3 R9-D10 F2 frozen pin now green and fail-closed, idx 11 R8-S13 pins resolving exactly at 291c714) — all four dispositions **verified**, every digest/token/exit independently reproduced (frozen stdout e282a068…, 3-value semantic diff, byte-identical old-vs-new gate differential, 24/24 manifest sweep, shipped loader 0da0015f parses both cases, 39/39 selftest), with two flagged residuals: O04's tracker rows 2/10 still `pending` (proposed, not written — integrator must apply) and the re-pin's re-serialization caveat (wc -l 34→33 vs splitlines 34→34), plus one self-correction (pipe-swallowed exit code) and one documentation-only stale freeze token (examples/culture-d3/README.md:34,91).
