# R01 — independent non-author review, round-46 git-hygiene audit

Reviewer: R01 (independent, non-author). Read-only re-verification: every
command below was re-run by this seat; no seat-file output was trusted.
Audit window: lane `main` commits `139e3b6..1dfb87f` (the 14 loop-1 commits,
rounds 33-44). Fleet repo: `/home/vgpnk/Projects/shokunin`; lane repo:
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` (separate git toplevel,
verified via `git rev-parse --show-toplevel` in both).

Observation note: during this review HEAD advanced `1dfb87f` → `acd37c2`
(round-46 landing) → `6e9a30d` (retrospective). All census evidence was taken
against the immutable window `139e3b6..1dfb87f`; the new commits are outside
rounds 33-44 and do not touch the audited round dirs.

## CLAIM A — commit-chain census — verdict: **unchanged** (re-verified true)

- **Authors.** `git log --format='%h|%an|%ae|%cn|%ce|%s' 139e3b6..main` piped
  through an awk filter flagging any non-`kotodama-shokunin
  <kotodama@shokunin.local>` author/committer → zero hits across all 14
  commits (checked 14). Commits: `da68a6d 4a7aede ce103bf 57c8409 fa90c77
  9bccc9b dfb0719 fd55e1f 13a1657 456674d ac47c78 7ceff59 c9f4eaa 1dfb87f`.
- **Fleet-path isolation.** `git log --all --name-only -- MANIFEST.json .ufo`
  in the lane repo → only pre-window commits `cdd66d7`/`139e3b6` touched
  `.ufo/reports/round-32/kotodama.md` (an in-lane `.ufo/` path, since
  relocated to fleet root); `MANIFEST.json` has *never* been touched in lane
  history. Zero in-window lane commits touched either path.
- **Fleet→lane isolation.** In the fleet repo: `git ls-files | grep -c
  '^kotodama-shokunin/'` → `0`; `git log -- kotodama-shokunin` → empty;
  `.gitignore:1` is `*-shokunin/` — the lane dir is fleet-ignored, so no fleet
  commit can write lane `corpus/`/`tools/`/`reports/`. Structurally zero.
- **Pushes/merges.** `git log --merges 139e3b6..main` → empty. `git reflog
  show origin/main` → newest entry `139e3b6 update by push`; local `main` is
  `ahead 14` (now 16 after the r46 landing) — every loop-1 commit is
  unpushed. The last push delivered the pre-window tip; pushes are
  operator-owned and were not performed in the window.
- **Designed two-commit pattern (context, not a violation).** The lane
  identity authored one fleet-repo ledger/report commit per round 33-44
  (`564e120`…`e85ad13`), each touching only fleet `MANIFEST.json` +
  `.ufo/reports/round-<N>/kotodama.md`. Under the claim's repo-boundary
  reading ("lane commit" = commit in the lane repo) this is the intended
  filing pattern and claim A holds. Under a stricter author-identity
  reading, those fleet-side writes exist — flagged here as an
  interpretation boundary, not a discrepancy.

## CLAIM O — append-only reports/ — verdict: **unchanged** (re-verified true)

- `git log --diff-filter=MD --format='%h' -- reports/round-<N>` for
  N=33..43 → **empty** for every round except r40. Landing commits only add
  files (type A), so an empty M/D list means zero post-landing
  modification/deletion commits.
- **r40 exceptions: exactly the two recorded supersessions.**
  - `456674d` — `git show` under `reports/round-40/` shows `M
    run-validation.py`, `M validation.json` only: the authorized
    `REFRESH_RECEIPTS=1` closing-snapshot refresh. Its "supersedes
    8b7b4508" refers to the prior receipt's sha256 prefix (`git cat-file -t
    8b7b4508` → not a valid object; `reports/round-40/telemetry/
    availability-close-40.json:23` names it as the receipt digest), not a
    commit.
  - `ac47c78` (r41's commit) — `M reports/round-40/op/defect-queue-v2.json`
    in place: reclassifies `N7-receipt-fidelity` +
    `r39-runner-root-regression` to `fixed-with-evidence` and appends a
    `r41_update` block — the documented amendment, cross-recorded in
    `reports/round-42/op/O08-queue-update.md:211` and
    `reports/round-43/calib/Ca03-queue-update.md:25,272` which pin parent
    sha `dfc9265d…` against further drift.
- **Receipts.** `reports/round-<N>/validation.json` for N=33..44: all 12
  present, all parse (`json.load` OK), all committed — last touched by the
  landing commit for each round except r40 (touched by the recorded
  `456674d` refresh, consistent with the refresh semantics).
- Working tree: `git status --short` → only `?? reports/round-47/` (new
  cycle); zero modified tracked files.

**Seat-file nuance (does not affect the claim):** the O01 audit file
attributes three r40 files to `456674d` including `op/defect-queue-v2.json`;
my re-run shows `456674d` touched only `run-validation.py` +
`validation.json` — the queue file was modified solely by `ac47c78`. The
audited claim itself remains accurate.

## CLAIM Ca — MANIFEST ↔ lane receipts — verdict: **unchanged** (re-verified true)

- Lane `validation.json` verdicts (`acceptance_checks_passed` /
  `round_status` / `verdict`):
  r33-35 True, r36 False (`round_status='REJECTED on D …'`), r37-41 True,
  r42 False (no verdict field — plain rejection, matching the "NOT ADMITTED
  on C" commit), r43+r44 `verdict='rejected-honest-stop'`.
  → **8 admitted / 2 rejected (r36, r42) / 2 rejected-honest-stop (r43, r44).**
- Fleet `MANIFEST.json` `rounds[]`, every entry containing `kotodama` for
  rounds 33-44 (container `closure` schema for 33-42 carries
  `lanes.kotodama`/`lane_rounds.kotodama`/`admitted`; flat per-lane schema
  for 43-44 carries `lane`/`verdict`/`admitted`):
  CONT r33-35,37-41 `admitted=True`; CONT r36,r42 `admitted=False`;
  FLAT r43,r44 `verdict='rejected-honest-stop', admitted=False`.
  → identical 8/2/2 distribution, row-for-row, across both ledger schemas.
- No duplicate or missing kotodama rows for rounds 33-44 in either schema.

## Discrepancies / observations

1. O01 seat file over-attributes `defect-queue-v2.json` to `456674d`
   (correct commit: `ac47c78`). Claim-level verdict unaffected.
2. `456674d`'s "supersedes 8b7b4508" names a receipt content digest, not a
   git object — clarified for the record.
3. Claim A's "no lane commit wrote fleet-root MANIFEST.json/.ufo/" is
   verified under the repo-boundary reading; the lane identity's designed
   fleet-side filing commits exist by protocol and are enumerated above.
4. MANIFEST already carries a flat r46 row (`verdict='admitted'`) — outside
   this audit's 33-44 scope; noted for awareness.
5. `reports/round-47/` appeared untracked during this review — next cycle
   beginning; no bearing on the closed window.

Signed: **R01** — independent, non-author. All three claims re-verified by
direct command re-execution; verdicts **unchanged**.
