# Round 20 — Scope watch, second seat (auditor R20-A14)

- **Seat:** R20-A14 (auditor, SCOPE — second of the two scope seats,
  R20-A13..A14). **Lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  **Date:** 2026-10-18, local clock UTC-03:00. Observation window
  **09:55:30–10:07:00 -03:00** (12:55–13:07Z).
- **Role limits:** this seat executes and measures; it decides no admission,
  promotes no claim, and certifies no canon or source content. Its only write is
  this file; scratch under `.scratch/r20-a14/` with `TMPDIR=$PWD/.scratch`
  exported. No git mutation, no commit, no push, no write outside the lane repo,
  no filed-round byte of rounds 8–19 touched, no historical validator executed.
- **Independence from R20-A13:** this seat re-derives the same three
  conclusions with *different* measurement paths — per-round `ls-tree` digests
  at the baseline revision (A13's primary path was per-path
  `rev-parse`/`hash-object`), a cross-round reference to round-19's own recorded
  digests, and PROVINCE via `git cat-file blob` identity — rather than
  restating A13's readings.
- **Revision binding:** lane `HEAD = 122086bce0aa577bec221bb2d37eedf20f4f3ed2`
  (round-20 declare, 09:53:37 -03:00); `HEAD^ = caf1beac19b55f3bbce47e4a9e7e8710cc1c581d`
  = declared `baseline_revision` (round-19 admit, 09:52:31 -03:00). Fleet root
  HEAD `e637dad7826a345c9dbcff99eefb2422d3f64211`.
- **Question this file answers (assignment, verbatim):** "AUDIT R20-A13..A14
  (scope x2): filed rounds 8-19 untouched; fleet root clean; PROVINCE accurate."

## 0. Verdict

**IN SCOPE AND CLEAN.** Fleet root clean; the filed surface of rounds 8–19 is
untouched — all 892 tracked filed paths git-object-identical to the baseline
revision, re-derived per round; `PROVINCE.md` is byte-identical to the baseline
and accurate. One transient in-worktree receipt rewrite (round-5/round-7/round-9,
12:57:19–13:01:01Z) was observed and closed by 13:03:17Z; this seat's
re-derivation after the close is clean (§2b, §5 F-A14-1). No repair by this
seat; disposition is the parent's.

## 1. Fleet root clean (independent re-check)

`git -C /home/vgpnk/Projects/shokunin status --porcelain=v1 -uall` → **0 lines**
at 09:55, 09:58:16, and the fresh post-A13 reading 10:06:16 -03:00. Fleet HEAD
`e637dad` (committed 09:53:01 -03:00, the round-19 close) predates this round's
declaration; `git log --since="2026-10-18T09:53:37-03:00"` → 0 commits.
`git check-ignore -v kotodama-shokunin` → `.gitignore:1:*-shokunin/`.

## 2. Filed rounds 8–19 untouched (per-round re-derivation)

**Tracked filed surface:** `git ls-files reports/round-{8..19}` → **892 paths**.
Per-round tracked counts and `git ls-tree -r caf1bea -- reports/round-N | sha256sum`
at the baseline revision vs HEAD (all 2026-10-18):

| round | tracked files | baseline `ls-tree` digest (16 hex) | == HEAD |
|---|---|---|---|
| 8 | 153 | `045b06cc6825f668` | yes |
| 9 | 87 | `653bb8c4d13b1703` | yes |
| 10 | 73 | `c4fe57c798258e13` | yes |
| 11 | 252 | `bee64f7d51aa9397` | yes |
| 12 | 44 | `a3f3659620d7291d` | yes |
| 13 | 2 | `bab7d795ecbc9c62` | yes |
| 14 | 40 | `ee44819da25f67c4` | yes |
| 15 | 20 | `60ab6cb343ac2a05` | yes |
| 16 | 23 | `276a81d7fb54ef50` | yes |
| 17 | 67 | `99f4cf3ccf3863dd` | yes |
| 18 | 60 | `14920b529336f720` | yes |
| 19 | 71 | `347121d472402755` | yes |

**Cross-round reference (round-19's own filed audit).** `reports/round-19/scope-a20.md`
§2 records per-round `ls-tree` digests for rounds 8–18; re-derived
programmatically against the live git objects at `caf1bea`, **11/11 match,
counts match**. The same file records the rounds 8–18 whole-surface digest
`17cfb543bcd32c2133b7905aa55a01c2dfb859a4402562927b52b52a072bdd80`; re-run now
with the same method → identical. The rounds 8–19 surface digest is
`1085567561e375b95a60fbc1f3d2ccfe3ffc8491e3b4d99b09e76ebb03209399` (897
non-`__pycache__` files; 892 tracked + 5 git-ignored run logs — `*.log`,
`.gitignore` line 3; 10 ignored `.pyc` excluded; 0 hardlinks).

**Declare commit and mtimes.** `git diff --name-only caf1bea HEAD` → exactly
`reports/round-20/claims.json` and `reports/round-20/targets.json`;
`git diff --name-only caf1bea HEAD -- reports/round-{8..19}` → empty;
`git diff HEAD -- reports/round-{8..19}` → empty at closing.

### 2b. Transient rewrites, independent reading

This seat's independent reading of the same event A13 reports:
`git status -uall` at 09:57:13 showed 2 untracked round-20 files and **no**
modified filed receipt; at 09:58:16 `reports/round-5/validation.json` was
modified; at 10:01:24 also round-7 and round-9 (mtimes 10:00:55 / 10:00:58 /
10:01:01). At 10:03:17 all three were restored to HEAD bytes (identical
nanosecond mtimes on all three; `git diff --quiet -- reports/round-{5,7,9}` →
clean). Closing re-derivation 10:06:15: identity 892/892; aggregate digests
unchanged; rounds 8–19 status 0. One mtime residue:
`reports/round-9/validation.json` (10:03:17; content byte-identical to HEAD —
`git diff --quiet` clean). Detail, attribution candidates, and controls in §5
F-A14-1; no repair by this seat.

## 3. PROVINCE accurate (independent re-check)

Byte identity re-derived through git objects rather than the working copy
alone: `git cat-file blob caf1bea:PROVINCE.md | sha256sum` →
`05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` =
`sha256sum PROVINCE.md`; HEAD blob
`313b182f251564b7997b06996b4f063370778f11`; `git diff caf1bea 122086b -- PROVINCE.md`
and `git diff HEAD -- PROVINCE.md` both empty; last content change `c53782a`
(2026-10-17). Surface checks (2026-10-18, 10:06): six owned partitions exist
(`ls corpus/knowledge/`); 10 gate scripts (`ls tools/gates/*.py`); adjacent
contract present (28421 bytes); canon grep 13 hits, all refusals/handoffs;
1636 tracked files, only lane-root metadata outside the partitions; the six
refused-domain siblings exist; no `world-bible/` in the lane. **Limit:** the
negative "siblings remain read-only" is not falsifiable from inside the lane
(§5 N2).

## 4. Commands (all run 2026-10-18, ~09:55–10:07 -03:00, `TMPDIR=$PWD/.scratch`)

- `git -C /home/vgpnk/Projects/shokunin status --porcelain=v1 -uall` → 0 (three
  readings); fleet `git log -1`; `git log --since=…` on the fleet root.
- `git ls-files reports/round-{8..19} | wc -l` → 892; per round,
  `git ls-tree -r caf1bea -- reports/round-N | sha256sum` vs HEAD.
- `python3 -` re-derivation of `reports/round-19/scope-a20.md`'s recorded
  per-round digests and the rounds 8–18 aggregate digest vs live objects →
  11/11 + digest match.
- `git diff --name-only caf1bea HEAD`; `git diff HEAD -- reports/round-{8..19}`.
- `find reports/round-{8..19} … | sha256sum`; `-links +1`; `-newermt "2026-10-18 09:52:31"`
  → 1 file (`reports/round-9/validation.json`, restore mtime).
- `git cat-file blob caf1bea:PROVINCE.md | sha256sum`; `sha256sum PROVINCE.md`;
  `git rev-parse HEAD:PROVINCE.md`.
- `git status -uall` readings at 09:57:13, 09:58:16, 10:01:24, 10:03:17
  (restore), 10:06:15 / 10:06:47 (closing).

## 5. Findings

- **F-A14-1 (routed, in-lane, transient — closed):** the round-5/round-7/round-9
  receipts were rewritten in place in the worktree between 12:57:19 and
  13:01:01Z and restored to HEAD bytes at 13:03:17Z (round-9 is inside the
  audited 8–19 bind; §2b). Candidate attribution (not proven): the R20-A15..A16
  ledger-snapshot sweep re-executes the round-10 drift-ledger rows whose
  commands are exactly `python3 reports/round-{5,7,9}/run-validation.py`
  (`.scratch/ledger-snapshot/out/row-*.json`: rows 102/120/170 → r5; 130/172 →
  r7; 114/132 → r9); its recorded batch begins 13:01:10Z, so the rewrites fall
  before it. Controls: the round's sanctioned re-pin mechanism is
  NEW-files-only (`.scratch/o11/build-repin-r20.py`: "NEW files only… Never
  opens a filed round 8-19 artifact for writing"); the pre-round-14 harnesses
  carry no `receipt_guard` (0 mentions in their `run-validation.py`), so a
  re-run writes their receipt unconditionally. Cross-references:
  `.scratch/r20-regression/finding-filed-rounds.txt` (R20-O15/O16 regression
  seat) and `.scratch/x19/filed-r9.diff` (X19 scribe). No repair by this seat;
  disposition is the parent's.
- **F-A14-2 (out-of-lane, informational):** `lore-shokunin` dirty=2 (recurring
  class); the other 19 siblings and the lane clean.
- **N1 (in-flight wave):** 17 untracked `reports/round-20/` artifacts and NEW
  `tools/gates/expected/d4-typed-labels-check-gate/r20-post/*` baselines were
  landing during the window; the four modified files (`corpus/README.md`,
  `tools/d2-typed-labels.py`, `examples/culture-d4/typed-labels.d4.yml`,
  `tools/gates/typed-pipelines.json`) are claim D/O/C craft, none in rounds
  8–19.
- **N2 (limit):** as A13 §5 N2 — the negative "no out-of-lane write" is not
  provable from inside the lane.

## 6. Compliance self-attestation

This seat wrote only `reports/round-20/scope-a14.md`, plus scratch under
`.scratch/r20-a14/` (`TMPDIR=$PWD/.scratch`). No git mutation, no commit, no
push, no write outside the lane repo, no filed-round bytes of rounds 8–19
touched, no historical validator executed. Out-of-province observations routed
in §5, never absorbed.
