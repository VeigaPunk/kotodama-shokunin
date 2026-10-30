# ExecCaCounter — round 79 W1 — Ca census-receipt correction counter (draft, pre-freeze)

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Base `44f76d456c1b326a71ffdb381590af825cbf11be` (HEAD unchanged; nothing committed in the lane). Seat: `ExecCaCounter`. No subagent dispatched. No tool installed or updated (pacman not used).

## Verdict

- The mismatch is real and reproduces exactly as the CLAIMS-DRAFT states: `reports/round-78/telemetry/census-end.txt` names the S884 used-by path `…worldbuilding-setting-practice.amend-2026-10-24-r13.md`; the registry at the measured round-78 revision `4b255745dea45a45d88b17e3c3fea4cdb6700cf7` (and at base) names `…amend-2026-10-23.md`. Derivation: **mismatch = 1**.
- The counter (`accept-ca.py`) reads only committed git objects, takes its constants from the freeze commit, and refuses/grades per criteria 17, 19, 23, 25 and 28. Its selftest passes **12/12**. On the real receipt and registry bytes, in an isolated clone, it goes **mismatch 1 → unresolved 0** with the correction record, and fails 4/7 without it.
- **Claim-target finding (for L1):** no SCORECARD, SHONEN or LOG statement corresponds to the S884 used-by token (details below). Under the CLAIMS-DRAFT rule, Ca should be rejected before freeze. The correction can still land as unclaimed conformance repair, graded by this counter if L1 wants that.

## Re-derivation (read-only, committed bytes)

| item | value |
|---|---|
| receipt `reports/round-78/telemetry/census-end.txt` blob (same at `4b255745` and base) | `62eb55b77f44bf47c283c98c5645dd7141e98495` |
| receipt sha256 | `05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867` |
| `corpus/SOURCES.md` blob at `4b255745` and at base | `c28330a37535223939ea5820af50d8d8595ed059` (no SOURCES change base..`4b255745`) |
| used-by lines in receipt | 4 (S881, S882, S884, S893) |
| mismatches | **1: S884** — receipt `…amend-2026-10-24-r13.md` vs registry `…amend-2026-10-23.md` |
| S881 / S882 / S893 | agree with registry |
| `census-start.txt` S884 | `…amend-2026-10-23.md` (agrees with registry) |
| `…amend-2026-10-24-r13.md` in any commit (`git log --all`) | never existed |
| `…amend-2026-10-23.md` at base | exists |

Re-run commands (read-only): `python3 -B .ufo/waves/round-79/w1/stage/ExecCaCounter/accept-ca.py --derive --root <lane> --at 4b255745dea45a45d88b17e3c3fea4cdb6700cf7 --receipt-path reports/round-78/telemetry/census-end.txt --registry-path corpus/SOURCES.md` (and `--at 44f76d456c1b326a71ffdb381590af825cbf11be`). Both print `DERIVE used-by-lines=4 mismatches=1 errors=0` and `MISMATCH S884 …`.

## Claim-target check (SCORECARD / SHONEN / LOG)

Searched SCORECARD.md, SHONEN.md, LOG.md, `corpus/lessons/round-78.md` and `round-78-verifier-spotcheck.md`. No self-assessment states an S884 used-by token. The S884 mentions are: `round-78.md:15` (names the census receipts, no token), and the round-78 verifier spot-check `:32, :56, :67` (routed defect 2: the end receipt is "a quality defect in the evidence record"). SHONEN.md's "census exit 0 … census-end.txt" (round 75) concerns row counts, not this token. So nothing "genuinely corresponding" exists; the CLAIMS-DRAFT rule rejects Ca before freeze. My recommendation: reject Ca as a claim and land the correction as unclaimed conformance repair. Decision is L1's.

## Artifacts (stage: `.ufo/waves/round-79/w1/stage/ExecCaCounter/`)

- `accept-ca.py` — counter (`--lands`, `--freeze`, `--work` required; `--derive`; `--selftest`). Final sha256 **`adfadbec65e15a763c9db6c6745a5d4f0e3ad5f7c658be3d9256f1da4d181620`**.
- `draft/reports/round-79/corrections/census-r78-S884.txt` — the correction record (exact receipt blob/sha, measured revision `4b255745…`, old token, actual token). Lands **after** freeze (see integration rules).
- `draft/claims-Ca-census_correction.fragment.json` — frozen constants for L1 to merge into `reports/round-79/claims.json` (legs list = counter table).
- `receipts/` — `selftest-ca79.txt`, three real-bytes receipts, derive receipts, `real-fixture-ids.json`, `SHA256SUMS`.

## Counter design

- **Constants**: `git show <freeze>:reports/round-79/claims.json`, claim id `Ca`, object `census_correction` (receipt path/blob/sha, registry path, measured revision, base, expected_mismatches, mismatches list, correction_dir, legs). Malformed or missing constants refuse; LEGCOUNT refuses when the frozen legs differ from the counter table.
- **Reads**: `git show`, `rev-parse`, `rev-list --first-parent`, `diff-tree -z`. No worktree byte is opened; no network; no repository tool is executed. Global and system git config are disabled for reads.
- **Refusals (exit 2, `FAIL legs=0/7 (refused: …)`)**: lands/freeze not 40-hex or not commits; freeze has no readable claims.json; LEGCOUNT; lands equal to base; freeze, measured revision or base not on lands' first-parent chain; `--work` missing (no TMPDIR fallback).
- **Legs (in order)**: `FROZENCFG` (claims.json at lands byte-identical to freeze blob) · `RECEIPT` (receipt blob at measured and lands = frozen id, sha256 = frozen digest) · `DERIVE` (re-derived mismatches == frozen list, count == expected) · `CORRECTION` (every file added under `correction_dir` binds exactly the frozen constants for one frozen row; exactly one per row; no spurious row; no modified/deleted file) · `UNRESOLVED` (re-derived mismatches not covered by a valid correction == 0) · `SEPARABLE` (every path changed freeze..lands is an added file under `correction_dir`; O paths, registry and receipt cannot change) · `NOSTUB` (≥1 correction; no empty, placeholder or `<…>` key).
- Graded runs write `<work>/accept-ca-79-<lands12>.txt` with the stamp headers (`stamped`, `evaluated`, `measured`, `freeze`, `tree`, `counter sha256 (self)`).

## Selftest (run by me; scratch removed afterwards)

Command: `python3 -B …/accept-ca.py --selftest --work /fast/scratch/hyaku/kotodama-r79/ExecCaCounter` → `SELFTEST: 12/12`, exit 0. Fixture: isolated `git init` repo under the explicit scratch, toplevel asserted. Predictions were written before the run and all twelve matched.

| scenario | exit | failing legs | verdict |
|---|---|---|---|
| clean | 0 | none | PASS 7/7 |
| do-nothing (lands = freeze) | 1 | CORRECTION, UNRESOLVED, NOSTUB | FAIL 4/7 |
| no-correction (empty commit) | 1 | CORRECTION, UNRESOLVED, NOSTUB | FAIL 4/7 |
| lying-token (actual-token = r13 path) | 1 | CORRECTION, UNRESOLVED | FAIL 5/7 |
| wrong-revision (measured = base) | 1 | CORRECTION, UNRESOLVED | FAIL 5/7 |
| changed-receipt (receipt edited in place + correction) | 1 | RECEIPT, SEPARABLE | FAIL 5/7 |
| frozen-tamper (freeze constant lies) | 1 | DERIVE, UNRESOLVED | FAIL 5/7 |
| refuse lands = base | 2 | refusal | refused |
| refuse freeze off lands chain | 2 | refusal | refused |
| refuse freeze without claims.json | 2 | refusal | refused |
| refuse non-hex lands | 2 | refusal | refused |
| clean after worktree moved to base | 0 | none | PASS 7/7 (blobs only) |

## Real-bytes run (isolated clone, scratch removed)

A `git clone --shared --no-checkout` of the lane was created in scratch and its toplevel asserted. Only the clone received commits: a freeze on base carrying the real Ca constants, then the real draft correction (lands) or an empty commit (no-correction). Measured revision and base are the real lane commits. Clone-local commit ids: freeze `893d6323…`, lands `975d6963…`, no-correction `9422a8f9…`.

| run | exit | verdict |
|---|---|---|
| derive at measured, before correction | 0 | mismatches=1 (S884) |
| clean (lands = freeze + correction) | 0 | PASS legs=7/7; `UNRESOLVED … unresolved 0` |
| do-nothing (lands = freeze) | 1 | FAIL legs=4/7 |
| no-correction | 1 | FAIL legs=4/7 |

## QUALITY pre-dispatch shape checks run on the final bytes

- Criterion 23 limb 1 (`build_fixture` form): prints nothing. An earlier draft printed `ST_RECEIPT` because the fixture was inline in `selftest()`; I moved it into `build_fixture()` and re-ran everything.
- Criterion 23 limb 2: `head -2 selftest-ca79.txt | grep -q 'clean -> exit=0'` passes.
- Criterion 25 one-liner: exit 0 (`--freeze` present, `"show", "%s:%s"` present, no graded-root `CLAIMS` join).
- Criterion 28 one-liner: prints nothing (the counter executes no repository tool).

## Integration rules for L1

1. **The correction must not be in the freeze commit.** CORRECTION compares additions between freeze and lands; a correction frozen in would show as no addition. Freeze = `reports/round-79/claims.json` (Ca fragment merged), the counter, the selftest receipt, and no correction.
2. Land the correction at `reports/round-79/corrections/census-r78-S884.txt` as its own lands commit after freeze (copy the draft bytes unchanged).
3. Grade with `--root <lane> --lands <lands> --freeze <freeze> --work <explicit dir>`. The grade uses committed bytes only, so a moving worktree cannot affect it.
4. Commit the selftest receipt under telemetry before any falsify wave (criterion 23).

## Gaps and limits (stated, not hidden)

- **Criterion 19 header label:** the counter prints `# measured revision:` (the frozen round-78 measured revision), not `# measured revision (lane main):`. It has no `--main` because it never materializes a clone. I did not run `tools/check-receipt-seq.py`; L1 must reconcile the grammar.
- **Criterion 11 (review-only):** that the correction's `reason` is accurate, and that the registry's `…10-23.md` is the right page for S884, is not checked by any command. The counter checks that the receipt and registry agree with the record, not the content.
- **Re-derivation method:** the derive mode parses the receipt's `used-by=` lines and the registry's used-by cell; it does not re-run `scripts/sources-census.sh` (a fleet-root script, unpinned in this lane). That script was not executed.
- **Selftest fixture** is synthetic (small registry), used to exercise each failure mode; the real bytes were exercised only by the isolated clone run above, and only for clean/do-nothing/no-correction. Lying-token and wrong-revision on real bytes are covered by the selftest only.
- Clone-local commit ids in `real-fixture-ids.json` are not reproducible across machines (they depend on timestamps); the blob ids and the derived mismatch are.
- No lane commit, push or worktree change was made. Scratch `/fast/scratch/hyaku/kotodama-r79/ExecCaCounter/` was removed after copying receipts; peers' scratch under `kotodama-r79/` was not touched.

Report: .ufo/waves/round-79/w1/ExecCaCounter.md
