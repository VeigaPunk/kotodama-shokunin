# R10-O14 — findings scribe: final tracker state, zero-undispositioned check, regression battery

- seat: **R10-O14** (findings scribe, claim O), round 10 (loop 1 of 3, build round 3 of 4), 2026-10-17
- assignment (verbatim): "FINDINGS R10-O14 (scribe): final tracker state; assert zero undispositioned findings; confirm no previously green check regressed (re-run battery selftest); reports/round-10/findings-scribe.md."
- writes: this file, plus the final tracker state in `reports/round-10/findings-tracker.json` (fixer payloads merged; §1.3). No commit, no push, no other repository byte written.
- worktree at work: HEAD `e3a1ec9` with the round-10 wave in flight (peer writes: `SKILL.md`, `corpus/README.md`, `reports/round-8/run-validation.py`, `reports/round-9/validation.json` modified; new corpus entries; all `reports/round-10/*` untracked). All scratch in-lane under `.scratch/` (`export TMPDIR=$PWD/.scratch` before every scratch-writing command); `/tmp` unused (inode-exhausted, re-confirmed by drift shards).
- canon: NON-CANON engineering evidence; nothing here admits a round, a capability or a canon fact.

## 0. Method and clock

Measurement window 21:26Z–21:46Z (UTC), local UTC-03. The tracker was compiled by R10-O01 at 21:27Z; eight fixer fragments (`fix-02.md`–`fix-09.md`) and four verifier verdicts (`findings-verify-1.md`–`findings-verify-4.md`) landed during the window, as did the drift ledger (`drift/ledger.json`, 191 rows), the drift audit (`drift/audit.md`), 14 drift shard fragments and eight drift-fix fragments (`drift/fix-16.md`–`fix-23.md`). I read every fixer fragment's proposed row payload, re-verified a sample of their controls on the live tree myself, merged the payloads into the tracker, and re-ran the previously green checks. The counting command `reports/round-10/run-validation.py` was pre-read (not re-run by me; it rewrites `validation.json`, which is the parent's acceptance artifact).

## 1. Final tracker state

### 1.1 Counts after integration

- rows: **24** — all four source files covered: `reports/round-8/depth/findings.md` 13, `reports/round-8/depth/findings-17.md` 3, `reports/round-9/d3/findings.md` 6, `reports/round-9/d3/findings-10.md` 2.
- dispositions: **18 fixed-with-control**, **4 wont-fix**, **1 wont-fix (superseded by round-8 acceptance decision; fix recipe demonstrated)**, **1 wrong**.
- **undispositioned: 0** — zero undispositioned rows; **all 24 findings dispositioned**, each with either a demonstrated control or a stated reason (≥12 characters). No row is left pending, open, todo, tbd or unset.
- verify chain: 4/4 verifier verdict files present (counting command requires ≥4).
- `final_state` block added to the tracker (counts, `undispositioned_rows: []`, verify files, merge provenance).

### 1.2 Per-row audit (disposition · owner · my independent check)

| idx | source finding | disposition | owner | independent check I ran (2026-10-17) |
|---|---|---|---|---|
| 0 | R8-D16 S2 no D2 frozen manifest | wont-fix (superseded; recipe demonstrated) | O02 | `find` → still no committed D2 manifest; fix-02's scratch manifest replays 5/5; pristine-HEAD replay 0/7 (matches my finding, §3.2) |
| 1 | R8-D16 S3 regeneration + round-3 replay red | fixed-with-control | O03 | `assemble-d2.py --check` → exit 0 byte-identical (my run); live round-3 replay exit 2/7 by design (my run); scratch D2 manifest 5/5 |
| 2 | R9-D09 S1 re-pin = blessing operation | fixed-with-control | O04 | my semantic diff `a7bb205→9dc18ec`: **exactly 3** manifest digests changed; `expected_exit`/`finding_ids` unchanged; byte diff is a whole-file re-indent (33/33) |
| 3 | R9-D10 F2 D3 frozen pin red | fixed-with-control | O05 | my run: `--frozen examples/culture-d3/expected.json` → **exit 0, findings []** |
| 4 | R8-D16 S6 supplied `native_form` unread | **wrong** | O06 | fix-06 Controls A–D; the injected record-level key is undeclared (spec §1.5 unchanged); the declared typed-label channel is read (O04 Appendix A + fix-06) |
| 5 | R8-D16 S10 rank ratio in SCORECARD | fixed-with-control (patch verified, landing deferred) | O07 | SCORECARD's capability row (line 128) carries no rank claim today; fix-07's anchored patch FAILs on filed SCORECARD / PASSes on the patch |
| 6 | R9-D09 S2 green-by-construction surfaces | wont-fix | O08 | guard selftest still builds fixtures from live bytes (code :1863-1876); the frozen leg's evidence is the `--frozen` run itself (exit 0, my run) |
| 7 | R9-D09 S3 superset control matcher | wont-fix (subset semantics recorded) | O09 | census by fix-09; guard is not in a fixer's write scope; acceptance legs do not rely on exact verdicts |
| 8 | R8-D17 F-D17-1 donor_form/substitutions absent | fixed-with-control | O02 | artifact: `donor_form "gas"`, `substitutions {…g:k…}`, derivation `gas→kas`; tool selftest B3 positive/negative controls present (:2757-2768) |
| 9 | R8-D16 S11 SCORECARD regex false positive | fixed-with-control (residual named) | O03 | filed harness bytes untouched (no-rewrite rule); anchored replacement function demonstrated fail-before/pass-after |
| 10 | R8-D16 S12 loader fragment rejects real packet | fixed-with-control | O04 | my test: shipped `load_packet_strict("costumes:\n  -\n    id: GAR-01\n")` → **PARSED**; tool reads the real 156 KB packet |
| 11 | R8-D16 S13 pins/locators invalidated | fixed-with-control | O05 | pins resolve exactly at revision `291c714` (226e1104…/bb08d458…); worktree=HEAD bytes 621b7a33…/5b1d75ab…; sub-items (b)/(c) are the reviewer's own corrections, not defects |
| 12 | R9-D09 S4 freeze unpinned by construction | fixed-with-control | O06 | pre-refresh `74496aa8…` (round-9 d3/scribe.md) and post-refresh `562b76cb…` (validation.json:24,991) both recorded; live bytes = recorded value |
| 13 | R9-D09 S5 `--selftest` outside exit-2 envelope | fixed-with-control (landing deferred, reason stated) | O07 | code still pre-`try` at :915-917 (my read); fix-07's patch fail-before (traceback) / pass-after (rc=2) verified; landing would turn the D3 frozen leg red without a re-pin |
| 14 | R8-D17 F-D17-2 vocabulary divergence | fixed-with-control | O08 | artifact: `supplied` ×60, `to-verify` ×23, `D2L-` ×37; `TL-01`/`TL-02` gone |
| 15 | R8-D17 F-D17-3 layer reference shape | fixed-with-control | O09 | artifact carries `layer_ref`; tool resolves it against declared layers (:701-704, `D2L-BORROW` fail path) |
| 16 | R9-D09 S6 informational conventions | wont-fix | O09 | reproduced live (hash convention, stubbed-matrix limit, `/tmp` 100%) |
| 17 | R9-D10 F1 two rule sentences differ | wont-fix (recorded intentional) | O09 | my read: sentences still differ (packet.json:16 vs packet.gates.yml:438); fix-09 sweep: no consumer reads either string; unify is acceptance-affecting |
| 18 | R8-D16 S1 (resolved) selftest broken | fixed-with-control | O09 | my run: `--selftest` **39/39 exit 0**, 0 tracebacks |
| 19 | R8-D16 S4 (resolved) D2L ids absent | fixed-with-control | O09 | tool `D2L-` ×69 / artifact ×37; live codes D2L-FORM-UNRESOLVED ×10, D2L-NATIVE ×2, R-RANK-CONFLICT ×4 |
| 20 | R8-D16 S5 (resolved) five kinds | fixed-with-control | O09 | `KINDS = ("translated-label","native-form","borrowed-strata")` (:414) — exactly three |
| 21 | R8-D16 S7 (resolved) exit map | fixed-with-control | O09 | my run: exit 1, 16 findings = 15 holds + 1 note (no exit-0-with-holds) |
| 22 | R8-D16 S8 (resolved) CLI / `--emit` | fixed-with-control | O09 | my two emits → byte-identical `a3aa452c…`; five CLI flags present |
| 23 | R8-D16 S9 (resolved) contract §5 fields | fixed-with-control | O09 | my counts: script 65 / representation 58 / scheme 78 / evidence 58; `pronunciation` = 0 residual (honest, no datum in components) |

### 1.3 Integration notes

- Ten rows were updated in place by their fixers (idx 0, 1, 3, 6, 8, 9, 11, 14 — fix-02/03/05/08 wrote the tracker directly).
- I merged the remaining rows from the fragments' own "Proposed tracker rows" JSON payloads: idx 2/10 (fix-04), 4/12 (fix-06), 5/13 (fix-07), 7/15/16-23 (fix-09). Payload fields were applied verbatim (`disposition`, `control`, `reason`, `landing`, `disposition_evidence`). Two minimal additions to satisfy the counting command's evidence contract: a `reason` on idx 4 (payload had only `disposition_evidence`), and command+exit `control` strings for idx 12/15/18-23 quoting the fixers' own receipts (their original control values were bare fragment locators without command/exit text). No fixer's conclusion was altered.
- Rows 16-23 (informational + resolved-at-source) were dispositioned by R10-O09 (fix-09 §4-§6), not by this seat.
- Concurrent writers: several seats wrote the tracker during the window; my final write was at 21:42Z and a re-read at 21:45Z showed no later write. Tracker sha256 at final read: `5a0ca3de9a058de2b8e772f5f2af0bd5302a04957764e3639938f00ba496effc`.

## 2. Verifier chain (O10–O13) — 4/4 present

| file | verifies |
|---|---|
| `findings-verify-1.md` | O02 (idx 0, 8) + O03 (idx 1, 9) |
| `findings-verify-2.md` | O04 (idx 2, 10) + O05 (idx 3, 11) |
| `findings-verify-3.md` | O06 (idx 4, 12) + O07 (idx 5, 13) |
| `findings-verify-4.md` | O08 (idx 6, 14) + O09 (idx 7, 15) |

Verify-2 and verify-4 state they re-ran every cited control independently ("no fragment value was accepted by quotation"); verify-2 additionally re-established the seat→row mapping from control-script headers rather than assuming it.

## 3. No previously green check regressed

### 3.1 The battery selftest (assigned check) — green, re-run last

```sh
export TMPDIR=$PWD/.scratch
python3 tools/check-gate-battery.py --selftest    # exit 0; "SELFTEST OK 28/28 controls behaved as expected"
```

Also re-run by me on the current worktree: `tools/check-craft-exercise.py --selftest` → 10/10 tamper + 18/18 CLI, exit 0; `tools/replay-frozen.py --selftest` → 79/79, exit 0; `tools/source-audit-inventory.py --selftest` → PASS, exit 0; `tools/d2-typed-labels.py --selftest` → 39/39, exit 0; `tools/assemble-d2.py --check` → byte-identical, exit 0; `tools/assemble-culture-d3.py --check` → byte-identical, exit 0; `tools/check-evidence-coupling.py --selftest` → `selftest_passed: true`, exit 0, and `--frozen examples/culture-d3/expected.json` → exit 0, `findings: []`; the battery's plain run → gate selftests **7/7 pass**, 5 baselines pinned, exit 2 from the two gates without a default-root baseline (myth/naming) — the same exit-2 state recorded in round-9's own validation receipt, so not a regression.

### 3.2 One recorded mechanism was stale; round 10 repaired it

The round-8 acceptance recorded `replay_frozen.accepted: "isolated-pinned-revisions"` with `7/7` reproduced. That receipt is **not reproducible at the revision that carries it**: `replay_isolated()` restored the pinned gates from `HEAD`, which matched the round-3 pins only until the round-8 admit commit `e1694ba` revised all six gate files (596 insertions). My run of the pre-repair function: exit 2, **7 could-not-evaluate, 0 reproduced** (gates restored from HEAD: 7). Round-10's drift fixer repaired the mechanism in place (resolve each manifest `gate_sha256` against git history); my re-run of the repaired function:

```text
exit 0; rows 7, reproduced 7, mismatch 0, could_not_evaluate 0;
gates restored from history: 7 (revision 291c714 for all six; 6/7 matched by pin)
```

The drift ledger carries the live-tree command as `stale-documented` with the remediation control `current` (shard-09 rows R10-F09-01..03), and fix-02 independently re-confirmed the pristine-HEAD 0/7 reading. So no deliverable regressed; one recorded *mechanism* did, and round 10 fixed it in place with a demonstrated 7/7 control.

## 4. Adjacent observations (reported, not absorbed)

- **A1 — stale freeze tokens in the D3 docs.** `examples/culture-d3/README.md:34,91` and `handoff.md:65,242,278` still print the pre-re-pin digest `74496aa8…` while the live freeze is `562b76cb…` (fix-06 A1; I confirmed the tokens remain). The round-9 scribe listed re-dating them at re-pin time; it was not done, and no tracker row covers it. Both files are freeze-excluded, so no guard sees it.
- **A2 — `python3 tools/d2-typed-labels.py --check` exits 1 at HEAD.** The committed artifact's `packet_sha256` (`8da90b07…`) ≠ the committed packet (`e0f21509…`); `diff` is one changed line (4-line unified diff). The pair was already inconsistent in `e1694ba` (packet re-pinned, artifact not re-emitted). Verified by me (exit 1). No round-8/9 acceptance check covered this command (round-8's runner checks only `--selftest`); flagged for the drift sweep by fix-06/fix-07.
- **Round-9 `validation.json` re-run in place.** The worktree copy is modified vs HEAD (battery stdout hashes and `git_status` changed after the baseline dirs were committed); its verdicts are unchanged (`claims D/F/O: true`, acceptance true). Observed as a peer write, not mine — worth an integration note because filed-report bytes changed.
- **Hygiene:** `reports/round-10/__pycache__/run-validation.cpython-314.pyc` exists (a seat imported the runner); it should be covered by `.gitignore`/cleaned at integration.
- **Ledger growth under concurrency:** `drift/ledger.json` grew 122 → 191 rows while the wave ran (152 current / 29 stale-documented / 10 stale-fixed at final read); the F-scribe's ledger and F19 audit own its consistency, not this seat.

## 5. Limits

- I re-verified a sample of fixer controls myself (D3 re-pin semantic diff, loader, emit determinism, exit map, artifact fields, repaired replay) but did not re-run every fixer control; the four verifier files carry that (4/4 present, two of them explicitly re-running all cited controls).
- Rows 5 and 13 carry verified patches whose landing is deferred to the integration step (SCORECARD row; assembler envelope); the rows state this in `landing`. The scribe does not land shared artifacts.
- Row 7's inventory text paraphrases "5 of 16" where the census shows 1 distinct extra id + 4 multiplicity-only differences; fix-09 §8.1 notes the precise form; the inventory text is preserved as compiled.
- I did not adjudicate the honesty of the round-8 repairs themselves, any canon decision, real-world rights, or game mechanics.
- The counting command `reports/round-10/run-validation.py` was run at 21:46Z after integration: **claim O: PASS** (0 failures). It rewrites `reports/round-10/validation.json`, which the parent owns and will regenerate at admission; the pre-run in-process `measure_o()` check and the run agree.

## 6. Round state at scribe close (observed, for the parent)

`python3 reports/round-10/run-validation.py` at 21:46Z: **claim O: PASS (0 failures)**; **claim C: FAIL (4 failures)** — two authored entries still carry no named gap (filler risk) and one no retrievable locator, plus 2 audit fragments vs 4 required (C seats were still landing while this file was written); **claim F: FAIL (22 failures)** — ledger rows still missing `output_sha256` and stale-fixed rows without demonstrated fix evidence, 35/36 cited commands covered (F seats still landing). `acceptance_checks_passed: false` at that moment, driven by C and F only. The O claim's own criteria (tracker dispositions, verifier files, this scribe file) are fully satisfied.

## Receipts

```sh
# tracker final read + counts
python3 -c "import json;d=json.load(open('reports/round-10/findings-tracker.json'));print(len(d['findings']), d['final_state']['disposition_counts'])"
sha256sum reports/round-10/findings-tracker.json
# battery selftest (assigned regression check)
export TMPDIR=$PWD/.scratch && python3 tools/check-gate-battery.py --selftest   # exit 0, 28/28
python3 tools/check-craft-exercise.py --selftest   # exit 0, 10/10 + 18/18
python3 tools/replay-frozen.py --selftest          # exit 0, 79/79
python3 tools/d2-typed-labels.py --selftest        # exit 0, 39/39
python3 tools/assemble-d2.py --check               # exit 0 byte-identical
python3 tools/assemble-culture-d3.py --check       # exit 0 byte-identical
python3 tools/check-evidence-coupling.py --frozen examples/culture-d3/expected.json  # exit 0, findings []
python3 tools/d2-typed-labels.py --json            # exit 1: 16 findings = 15 holds + 1 note
python3 tools/d2-typed-labels.py --check           # exit 1 (A2; stale artifact packet pin)
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv  # exit 2, 7 could-not-evaluate (by design)
python3 reports/round-10/run-validation.py   # claim O: PASS (0 failures); C 4 / F 22 failures at 21:46Z
# repaired isolated replay (in-process): exit 0, 7/7, gates from history 291c714
# semantic re-pin diff: git show 9dc18ec^:examples/culture-d3/expected.json vs live -> exactly 3 digests
```

FILES: reports/round-10/findings-scribe.md, reports/round-10/findings-tracker.json | SUMMARY: Final tracker state: 24/24 rows dispositioned (18 fixed-with-control, 4 wont-fix, 1 wont-fix-superseded, 1 wrong) with zero undispositioned rows, all four verifier verdicts present; merged fix-02..fix-09 payloads into the tracker and strengthened eight control fields with the fixers' own command/exit receipts; regression battery re-run green (selftest 28/28, craft 10/10+18/18, replay 79/79, d2 39/39, both assemblers byte-identical, coupling frozen exit 0), with the one stale recorded mechanism (round-8 isolated replay at HEAD, 0/7) shown repaired in-round (7/7 via history-matched gates); adjacent observations filed (stale D3 doc freeze tokens, d2-typed-labels --check red since e1694ba, round-9 validation.json in-place re-run, __pycache__ hygiene).
