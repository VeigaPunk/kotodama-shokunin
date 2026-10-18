# Round 20 — Scope watch (auditor R20-A13)

- **Seat:** R20-A13 (auditor, SCOPE — first of the two scope seats, R20-A13..A14).
  **Lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. **Date:** 2026-10-18,
  local clock UTC-03:00. Observation window **09:54:00–10:07:00 -03:00**
  (12:54–13:07Z), with the closing re-check recorded in §6.
- **Role limits:** this seat executes and measures; it decides no admission,
  promotes no claim, and certifies no canon or source content. Its only writes
  are this file and its sibling `scope-a14.md`; scratch under `.scratch/r20-a13/`
  with `TMPDIR=$PWD/.scratch` exported. No git mutation, no commit, no push, no
  write outside the lane repo, no filed-round byte of rounds 8–19 touched, no
  historical validator executed.
- **Regimen / state:** operator loop 2 of 3, build round 4 of 4 — one 64-worker
  batch on `opencode-go/deepseek-v4.1-flash`, per `reports/round-20/claims.json`
  (`state: declared-before-dispatch`).
- **Revision binding:** lane `HEAD = 122086bce0aa577bec221bb2d37eedf20f4f3ed2`
  ("round-20: declare claims D/O/C", 2026-10-18T09:53:37-03:00);
  `HEAD^ = caf1beac19b55f3bbce47e4a9e7e8710cc1c581d` = the declared
  `baseline_revision` (round-19 admit, 09:52:31-03:00). `git show --stat 122086b`
  → exactly `reports/round-20/claims.json` (+32) and
  `reports/round-20/targets.json` (+12); the declare commit is the baseline's
  direct child.
- **Question this file answers (assignment, verbatim):** "AUDIT R20-A13..A14
  (scope x2): filed rounds 8-19 untouched; fleet root clean; PROVINCE accurate."

## 0. Verdict

**IN SCOPE AND CLEAN, with one routed transient (F-A13-1).** Fleet root clean
at every reading; the committed filed surface of rounds 8–19 is byte-stable
(all 892 tracked files git-object-identical to the baseline revision; the
declaration commit touched exactly two `reports/round-20/` paths); `PROVINCE.md`
is byte-identical to the baseline and accurate against the live surface. **One
transient deviation was observed and closed during the window:** a live wave
process re-ran the historical round-5/round-7/round-9 harnesses, which rewrote
those receipts **in place** in the working tree (12:57:19–13:01:01Z; round-9 is
inside the audited 8–19 bind); all three were restored to HEAD bytes by
13:03:17Z, and the closing re-derivation is 892/892 clean (§2b, §5 F-A13-1). No
repair was made by this seat; the disposition is the parent's.

## 1. Fleet root clean

`git -C /home/vgpnk/Projects/shokunin status --porcelain=v1` → **empty** (0
lines) at four observation points: 09:55:51, 09:57:13, 09:58:16, and the
closing reading 10:06:16 -03:00; `-uall` likewise 0. Fleet root HEAD
`e637dad7826a345c9dbcff99eefb2422d3f64211` "close kotodama round-19: admitted
(hyper provider; D/C/O)", committed 2026-10-18T09:53:01-03:00;
`git log --since="2026-10-18T09:53:37-03:00"` → 0 commits (no fleet commit
postdates this round's declaration).

- `git check-ignore -v kotodama-shokunin` → `.gitignore:1:*-shokunin/` — the
  lane is an independent repository, correctly invisible to fleet git.
- Fleet `.scratch/` → 0 entries; fleet `reports/` → 0 entries (an empty
  directory carries no git entry, so it is not dirt).

## 2. Filed rounds 8–19 untouched

**Scope of the check:** every tracked file under `reports/round-8` …
`reports/round-19`; `git ls-files` → **892 paths**. Rounds 5–7 sit outside this
bind; the round-5/round-7 receipts' transient rewrite is still reported in
§2b/§5 because it is the same event as the in-range round-9 one.

### 2a. Committed history — PASS

| # | check | command | observed |
|---|---|---|---|
| 1 | untracked in filed surface | `git status --porcelain=v1 -uall -- reports/round-{8..19}` | `0` at 09:55:51 and again at closing 10:06:15 |
| 2 | commit hygiene | `git diff --name-only caf1bea HEAD -- reports/round-{8..19}` | `0` (empty) |
| 3 | declare-commit contents | `git show --stat 122086b` | exactly `reports/round-20/claims.json` (+32), `reports/round-20/targets.json` (+12) |
| 4 | **git-object identity** (primary path) | per path: `git rev-parse caf1bea:<p>` vs `git hash-object <p>` | **892 match, 0 mismatch, 0 not-in-baseline**, at 09:55:5x and re-run at closing 10:06:15 |
| 5 | whole-surface digest | `find reports/round-{8..19} -type f -not -path '*__pycache__*' \| sort \| xargs sha256sum \| sha256sum` | `1085567561e375b95a60fbc1f3d2ccfe3ffc8491e3b4d99b09e76ebb03209399` (897 files; re-derived identical at closing) |
| 6 | sub-surface digest | same over rounds 8–18 | `17cfb543bcd32c2133b7905aa55a01c2dfb859a4402562927b52b52a072bdd80` — identical to the value round-19 recorded for the same surface |
| 7 | hardlink contamination | `find reports/round-{8..19} -type f -links +1` | `0` |
| 8 | tree identity | `git diff --stat caf1bea 122086b` | 2 files, both `reports/round-20/*`; `caf1bea^{tree}`=`8cdf9ca843b179a5f1c8f68aceeb388d4c8c7d12`, `122086b^{tree}`=`8003229ed9de09555bc08ca1288fab25017dc046` |

**Composition note (honest reading).** The non-`__pycache__` on-disk count
under rounds 8–19 is 897, of which 892 are tracked; the 5-file delta is
git-ignored run logs (`.gitignore` line 3, `*.log`):
`reports/round-9/baselines/{naming-collision-gate,myth-consistency-gate,handoff-packet-check}/run.log`
and `reports/round-11/handoff/{run.log,tamper-control.log}` — the same five as
round-19. Ignored files carry no git baseline and are reported as
observed-only. 10 ignored `__pycache__/*.pyc` files are likewise excluded.

### 2b. Live worktree — transient in-place receipt rewrites, restored (routed)

The primary identity reading (§2a row 4) was taken at 09:55:5x while the
worktree was clean. Between 09:57:19 and 10:01:01 -03:00, three **filed
receipts were rewritten in place** in the working tree:

| file | rewrites (mtime, local) | observed change |
|---|---|---|
| `reports/round-5/validation.json` | 09:57:19, 10:00:55 | 2 insertions/2 deletions: `O` error becomes the `tools/replay-frozen.py` re-run's failure; `tested_file_sha256["tools/check-gate-battery.py"]` `0a126b70…`→`cd8c0ec2…`; size 17366→3221 bytes |
| `reports/round-7/validation.json` | 10:00:58 | modified in worktree (not diffed by this seat before the restore) |
| `reports/round-9/validation.json` | 09:59:16, 10:01:01 | 594 insertions/64 deletions: `acceptance_checks_passed` `true`→`false`; `O` failures list gains `tools/gates/typed-pipeline-gate.py: no expected.json baseline found…`; new `r18-post` baseline rows |

All three were **restored to HEAD bytes at 10:03:17** (identical nanosecond
mtimes on all three = one restore operation; `git diff --quiet -- reports/round-{5,7,9}`
→ clean). The closing re-derivation (10:06:15) is 892/892 clean and both
aggregate digests are byte-identical to §2a. The only residue is an mtime:
`find reports/round-{8..19} -type f -newermt "2026-10-18 09:52:31"` → exactly 1
file, `reports/round-9/validation.json` (mtime 10:03:17, content byte-identical
to HEAD — `git diff --quiet` clean, identity row 4 matches). So "no filed byte
written after the baseline commit" holds **in content**; one file carries a new
mtime from the restore. Attribution (candidate, not proven) and controls are in
§5 F-A13-1.

## 3. PROVINCE accurate

`PROVINCE.md` sha256
`05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`, git blob
`313b182f251564b7997b06996b4f063370778f11`; byte-identical at baseline and HEAD
(`git diff caf1bea 122086b -- PROVINCE.md` → empty; `git diff HEAD -- PROVINCE.md`
→ empty); last content change `c53782a` (2026-10-17T13:09:14-03:00), before
this round. Assertions checked against the live surface (2026-10-18,
09:55–10:06):

| PROVINCE assertion | check | observed |
|---|---|---|
| owns `corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}` | `ls corpus/knowledge/` | exactly those six partitions; `.md` counts at 09:55: linguistics 19, myth-symbol 19, culture-material 18, synthesis 29, verification 20, civilizations 94 (in flux — the wave is landing new entries) |
| "this lane's own gates" | `ls tools/gates/*.py` | 10 gate scripts present |
| "non-canon examples" | `grep -rin 'is canon\|canonical truth\|declared canon' corpus examples` | 13 hits, each a refusal or handoff ("no claim here is canon"; "which is canon → lore-shokunin"), never a canon claim |
| adjacent contract path | `ls corpus/knowledge/synthesis/worldbible-integration-contract.md` | present (28421 bytes) |
| refuses: canon (lore), rights, game mechanics (game-dev-2d/3d), source method (chousa), web publishing (kake), prompt/skill craft (kotoba) | `[ -d ../<lane> ]` for each | all six sibling lanes exist |
| "Only writes this standalone lane repository" | `git ls-files` (1636 tracked) filtered for non-lane paths | no out-of-lane tracked paths; the only non-partition entries are lane-root metadata (`AGENTS.md`, `LOG.md`, `MINT.md`, `PROVINCE.md`, `README.md`, `SCORECARD.md`, `SHONEN.md`, `SKILL.md`, `.gitignore`) |
| world bible is lore's, not ours | `ls -d world-bible corpus/world-bible` | neither exists in this lane |

The one assertion this seat cannot falsify from inside the lane is the negative
"siblings … remain read-only" — a lane-local audit cannot prove no out-of-lane
write ever occurred (§5 N2).

## 4. Commands (all run 2026-10-18, ~09:54–10:07 -03:00, `TMPDIR=$PWD/.scratch`)

- `git status --porcelain=v1` and `-uall` — lane (over rounds 8–19: 0; full-tree
  readings in §5 N1) and fleet root (0 at four points).
- `git rev-parse HEAD` / `HEAD^`; `git log -1 --format='%H %cI %s'`;
  `git show --stat 122086b`; `git log --since=…` on the fleet root.
- per-path `git rev-parse caf1bea:<p>` vs `git hash-object <p>` over the 892
  tracked filed paths → 892/0/0 (twice).
- `find reports/round-{8..19} … | sha256sum` → `1085567561…` (twice); same over
  rounds 8–18 → `17cfb543…`.
- `git diff --name-only caf1bea HEAD` (and `-- reports/round-{8..19}`);
  `git diff --stat caf1bea 122086b`.
- `stat -c '%y %s'` on the three receipts; `git diff -- reports/round-{5,9}/validation.json`;
  `git diff --quiet` after the restore.
- `sha256sum PROVINCE.md`; `git rev-parse HEAD:PROVINCE.md`.
- `ls corpus/knowledge/`; per-partition counts; `ls tools/gates/*.py`;
  `ls -l corpus/knowledge/synthesis/worldbible-integration-contract.md`;
  `git ls-files | wc -l`; `grep -rin 'is canon\|canonical truth\|declared canon'`.
- `for d in /home/vgpnk/Projects/shokunin/*-shokunin/; do git -C "$d" status --porcelain=v1 | wc -l; done`
  — sibling sweep, 20 lanes.

## 5. Findings

- **F-A13-1 (routed, in-lane, transient — closed):** three filed receipts
  rewritten in place during the wave (§2b table), round-9 inside the audited
  8–19 bind, then restored to HEAD bytes at 10:03:17. The rewrite commands are
  exactly the round-10 drift-ledger rows re-run: `python3 reports/round-5/run-validation.py`
  (rows 102, 120, 170), `python3 reports/round-7/run-validation.py` (rows 130,
  172), `python3 reports/round-9/run-validation.py` (rows 114, 132) — recorded in
  `.scratch/ledger-snapshot/out/row-*.json` (R20-A15..A16 ledger-snapshot seat;
  its `rerun.py` executes drift-ledger rows 1:1 and assigns write-capable rows
  to the `.scratch/ledger-snapshot/iso-full` mirror). The seat's recorded batch
  begins 13:01:10Z (all its receipts ≥ that time; the mirror was built
  13:01:47Z), so the in-place rewrites at 12:57:19–13:01:01Z fall **before** its
  recorded batch — consistent with an earlier phase of that sweep (before the
  mirror existed) or another process executing the same rows; reported as
  candidate, not proven. Controls: (a) the round's sanctioned re-pin mechanism
  is NEW-files-only — `.scratch/o11/build-repin-r20.py` docstring: "R20-O11..O14
  re-pin builder — NEW files only… Never opens a filed round 8-19 artifact for
  writing", and `tools/gates/expected/d4-typed-labels-check-gate/r20-post/*`
  landed as NEW files during the window; (b) the round-5/7/9 harnesses carry no
  `receipt_guard` (0 mentions in their `run-validation.py`; the guard files
  appear from round-14), so a re-run writes their `validation.json`
  unconditionally. Cross-references: the R20-O15/O16 regression seat filed its
  own findings on round-5/round-9 (`.scratch/r20-regression/finding-filed-rounds.txt`,
  `finding-filed-round5.txt`); the X19 scribe seat kept filed-surface snapshots
  including `.scratch/x19/filed-r9.diff`. The restore actor was not identified
  from scratch records (no scratch script contains a restore command; the three
  identical mtimes indicate a single operation). This seat made no repair.
- **F-A13-2 (out-of-lane, informational):** `lore-shokunin` working tree is
  dirty (`dirty=2` at the 09:56 sweep) — the recurring r16/r17/r18/r19 class.
  Cause and disposition are lore's own scope; left untouched. All other 19
  siblings and the lane report `dirty=0`.
- **N1 (in-flight wave):** the worktree at the closing listing (10:06:47) shows
  the wave mid-landing: 4 modified files — `corpus/README.md` (claim C),
  `tools/d2-typed-labels.py` (claim O), `examples/culture-d4/typed-labels.d4.yml`
  and `tools/gates/typed-pipelines.json` (claim D/O craft) — plus 17 untracked
  `reports/round-20/` artifacts (audit, handoff, readme, integration, wart,
  `run-validation.py`, `report-draft.md`, `rerun.json`), `corpus/lessons/round-20.md`,
  and NEW `tools/gates/expected/d4-typed-labels-check-gate/r20-post/*` baselines.
  None touches rounds 8–19. The §2 verdict binds the filed surface and the
  declaration commit `122086b` only.
- **N2 (limit, negative assertion):** a lane-local scope watch cannot prove the
  negative "no out-of-lane write ever happened" — the fleet root is a different
  repository and ignores `*-shokunin/`; sibling repos are independent. This
  audit establishes the lane's own history, its filed surface, and the fleet
  root's cleanliness, not an attribution proof of all fleet activity.

## 6. Closing re-check and compliance self-attestation

Closing readings (10:06:15–10:06:47 -03:00): lane `HEAD = 122086b`; rounds 8–19
status 0; identity 892/892; digests `1085567561…` / `17cfb543…`; fleet root 0
lines. The round-9 receipt is content-clean with a 10:03:17 mtime (§2b).

This seat wrote only `reports/round-20/scope.md` and its sibling
`reports/round-20/scope-a14.md`, plus scratch under `.scratch/r20-a13/`
(`TMPDIR=$PWD/.scratch` exported before every scratch-writing command). No git
mutation, no commit, no push, no write outside the lane repo, no filed-round
bytes of rounds 8–19 touched (all scratch files are new), no historical
validator executed. Out-of-province observations are routed in §5, never
absorbed.
