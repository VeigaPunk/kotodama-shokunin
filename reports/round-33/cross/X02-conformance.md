- Seat: X02 | critic | cross | date 2026-10-19 | baseline 139e3b6

# X02 — conformance critique (append-only discipline, filed-bytes preservation, lane identity, report shape, telemetry)

Mission: `reports/round-33/targets.json:75`. Binding rules: `targets.json:6-10`
(shared_rules), `REGIMEN.md:45-50` (per-round record set), `AGENTS.md:5-9`
(append-only LOG, workers never race shared bookkeeping), `AGENTS.md:15-39`
(telemetry, incl. "Close what you open").

## 0. Observation window and method

Seat X02 ran read-only. Observations are timestamped; the tree was live (the
64-seat wave was landing fragments while this seat read).

- Window: `2026-10-19T03:53Z`–`04:05Z` (declaration `claims.json:6`
  `2026-10-19T03:49:01Z`; baseline commit `139e3b6`).
- At `03:54:27Z` the tree was dirty at two filed paths (finding X02-F1).
- At `03:56:38Z` and `04:00:05Z` those paths were clean again and HEAD was
  still `139e3b6`.
- 42 files had landed under `reports/round-33/` at `04:00:05Z`
  (41 seat fragments + the parent's `telemetry/dispatch-declared.json`).

## 1. Check table

| # | Check | Verdict | Evidence |
|---|---|---|---|
| C1 | No seat writes outside `reports/round-33/` | **green** | `git status --porcelain -uall` at `04:00:05Z`: only `reports/round-33/**` untracked + ` M LOG.md`, `?? REGIMEN.md` (both parent acts, declared at `LOG.md` regimen entry) |
| C2 | Filed round bytes `reports/round-1..32/**` preserved | **harmed then reverted** — see X02-F1 | dirty `03:54:15Z`/`03:54:18Z`, byte-exact restore `03:55:27.940Z`; clean at `03:56:38Z` |
| C3 | `corpus/lessons/*.md`, `tools/gates/frozen/**`, `SKILL.md`, `PROVINCE.md`, `AGENTS.md`, `SCORECARD.md` untouched | **green** | `git status --porcelain -uall -- corpus/lessons tools/gates/frozen` → 0 lines; `git diff --stat HEAD` for each of the four files → empty |
| C4 | LOG.md append-only | **green** | `git diff --stat LOG.md` → `18 insertions(+)`, 0 deletions; pure insertion hunk `@@ -3499,0 +3500,18 @@`; mtime `03:42:59Z` (pre-wave, parent) |
| C5 | Lane git identity not used by seats | **green, with exposure** — X02-F5 | HEAD `139e3b6` unchanged; `git reflog -5` HEAD@{0} = `139e3b6`; `git stash list` empty |
| C6 | Report-shape readiness | **not ready — owed** — X02-F4 | `reports/round-33/run-validation.py`, `validation.json`, fleet report, MANIFEST entry, SCORECARD row all absent at `04:00:05Z` |
| C7 | AGENTS.md telemetry rules for round 33 | **partial** — X02-F3 | `reports/round-33/telemetry/dispatch-declared.json` present and durable; observed counters deferred without explicit `null`+owner+reason fields |
| C8 | No credentials / prompt payloads in artifacts | **green** | `grep -rInE 'sk-[A-Za-z0-9]{8,}|Bearer [A-Za-z0-9._-]{10,}|api[_-]?key|authorization:|password|token' reports/round-33/` → only prose hits on the phrase "owner token" (`op/O03-owner-checks.md:27,32,42,46,109`); zero credential-shaped strings |
| C9 | Fragment format | **green, 5 cosmetic deviations** — X02-F6 | all 41 seat fragments carry `## Owed` and `## Citations` and the correct seat id in an assigned out path |

## 2. X02-F1 (severity: high, already reverted) — two filed receipts rewritten in place during the wave

**What happened.** `reports/round-5/validation.json` and
`reports/round-7/validation.json` — filed bytes of the closed regimen — were
rewritten in the working tree during this round, then restored byte-exact.

**Timeline (all 2026-10-19 UTC, from `stat -c %y` and my own dated reads).**

| Time | Event | Evidence |
|---|---|---|
| `03:54:15.802Z` | `reports/round-5/validation.json` rewritten | mtime; content digest `fe926984e8d15728c43c44b2fc4c0f60058f784aa4aa4b7c2e6aecc04a4dfeee` |
| `03:54:18.609Z` | `reports/round-7/validation.json` rewritten | mtime; digest `af0cf4ed32d68c2b96284b49de97cfe75900c512299d4dd7423580e9573912a4` |
| `03:54:27Z` | X02 observes both dirty | `git status --porcelain` → ` M reports/round-5/validation.json`, ` M reports/round-7/validation.json` |
| `03:54:37Z` | isolated copy created | `.scratch/c05-iso/` mtime; it is a full tree copy without `.git` |
| `03:54:39–42Z` | the same three runners re-run **inside the copy** | `.scratch/c05-tmp/r5.log`, `r6.log`, `r7.log`; `.scratch/c05-iso/reports/round-{5,6,7}/validation.json` |
| `03:55:27.940Z` | both repo receipts restored, identical mtime → bulk restore | current digests equal the HEAD blobs: `73a66f7464ead0d99318750422256ceafac3d8c2d283f94604eb258abc1bb794` (r5), `2f4c1e159b60d78250074c51f013d13aac3cf1b140a623d197a0883e5ecac6f3` (r7) |
| `03:56:38Z` / `04:00:05Z` | X02 re-verifies clean | `git status --porcelain -uall` shows no filed path dirty |

**Mechanism (certain).** The three filed runners publish their receipt in
place: `reports/round-5/run-validation.py:194`,
`reports/round-6/run-validation.py` (publishes `HERE / "validation.json"`),
`reports/round-7/run-validation.py:1171` — all `(HERE / "validation.json").write_text(...)`.
They are the **only three** filed runners that do so
(`grep -l 'HERE / "validation.json"' reports/round-*/run-validation.py` → 3
paths), and **none of the three supports a `--check`/no-publish flag**
(no `--check` argument in `reports/round-{5,6,7}/run-validation.py`; contrast
round-32's `run-validation.py` docstring "`--check` never publishes a
receipt"). Re-running any of them from the repo root therefore *must* rewrite
filed bytes.

**Context (why it happened, and why it will recur).** The r5/r6/r7 acceptance
re-runs are explicitly in this round's claim-C scope: item C-07 "cold-run N1 —
no expected-verdict errata for the r5/6/7 acceptance re-runs"
(`reports/round-33/calib/C16-receipt.md:67`). The `.scratch/c05-tmp/r{5,6,7}.log`
artifacts sit in seat C05's scratch, i.e. the re-run is a claim-C work product,
not an accident of curiosity. The correct pattern was demonstrated minutes
later: run the filed runner **inside an isolated copy** (`.scratch/c05-iso/`).

**Attribution.** The mechanism and the purpose are established; the *writer of
the in-repo bytes* is **to-verify** — no artifact names the invoking shell. The
copy's r5 receipt carries the dirty bytes (`fe926984…`, identical to the dirty
repo file), so the copy was taken after the rewrite; that is consistent with a
seat running the runner in-repo first and then switching to the copy pattern,
but it does not prove who ran the in-repo pass. The parent should attribute from
its own dispatch/agent logs, not from this fragment.

**Exposure had it not been reverted.** Both receipts are digest-pinned by filed
rounds: `reports/round-20/validation.json:17150-17151` and `:17372-17373`
(`baseline_sha256` = `current_sha256` = the two HEAD digests), and
`reports/round-23/wording/evidence/tie-break-check-receipt.json:17031-17032`
and `:17253-17254`. `reports/round-6/run-validation.py:283` and
`reports/round-6/check-checkpoint.py:99` also *read* the round-5 receipt. A
persisted rewrite would have broken two filed digest chains and round-6's
parent-check. Round 33's own baseline receipt already records the same two
digests as the correct values (`reports/round-33/op/O07-baseline-receipt.md:171,174`),
so the revert restored agreement rather than creating a new state.

**Remediation (for the integrator).**

1. Rule to state in the round record: *any* re-run of `reports/round-{5,6,7}/run-validation.py`
   must happen in an isolated copy of the tree (the `.scratch/c05-iso/` pattern)
   or not at all — there is no `--check` on those three runners.
2. Preserve the evidence: the dirty bytes and digests above are the proof that
   the round's own discipline was tested and held only by revert. If the round
   wants a durable record, file the two digests + the timeline in the
   round-33 report; do **not** re-create the dirty files anywhere.
3. Close-time detection (independent of `git status`, works even if the
   worktree were later re-dirtied and re-reverted):
   `sha256sum reports/round-5/validation.json reports/round-7/validation.json`
   must print `73a66f74…` and `2f4c1e15…`; plus
   `git status --porcelain -uall -- 'reports/round-[0-9]*' | grep -v '^?? reports/round-33/'`
   must be empty.

## 3. X02-F2 (severity: medium) — `AGENTS.md` tail is corrupted by a leaked mission fragment

`AGENTS.md:40-42` (committed, unmodified since `17e90b9`, mtime
`2026-10-18 20:49:59`, `git diff --stat AGENTS.md` empty) reads:

```
40  ```
41  (blank)
42  ### 2.2 `SKILL.md` — append one item to "## Checklist (executable where a tool exists)" (after :534)
```

The telemetry rules this round must obey end at `AGENTS.md:39`. Lines 40-42 are
a stray closing fence plus a leftover heading from an earlier round's own
mission text — the only surviving artifact of the edit that added the
"Close what you open" rule at `17e90b9`.

**Risk to round 33.** (a) A seat or the integrator reading `AGENTS.md` can
mistake `:42` for a live instruction to append to `SKILL.md` — which is exactly
the kind of shared-file edit the round forbids seats from making
(`targets.json:7`); (b) any close-time validator that checks `AGENTS.md`
preservation (`reports/round-32/run-validation.py:896` lists `AGENTS` among the
preservation-checked files) will treat a seat's "cleanup" as a violation.

**Draft fix (integrator-applied only, only if the round wants it).** Before:
lines 39-42 end `... detectable as a digest mismatch.` / ` ``` ` / blank /
`### 2.2 ...(after :534)`. After: end the file at the line
`  close time, so any later in-place edit is detectable as a digest mismatch.`
— delete `AGENTS.md:40-42`. Verification after applying:
`tail -3 AGENTS.md` shows the rule sentence as the last non-blank line, and
`grep -c '### 2.2' AGENTS.md` → 0. Cascade to check first: if `AGENTS.md` is
in any frozen baseline or digest pin, the edit needs a re-pin; the round-33
preservation check is against baseline `139e3b6`, so an integrator edit is
visible in `git status` and must be named in the LOG entry.

**Seat rule restated:** no seat may touch `AGENTS.md` this round; this finding
is a draft, not a permission.

## 4. X02-F3 — telemetry conformance (`AGENTS.md:15-39`)

**Conforms.** `reports/round-33/telemetry/dispatch-declared.json`
(sha256 `139b964ead124364443d208cb858967b12a108532eab01b22229dfea1c1ad9ac`):
durable location under `reports/round-33/telemetry/` (`AGENTS.md:17-18`);
named owner (`"orchestrator (goal-mode parent)"`, `AGENTS.md:21`); declaration
window (`declared_at_utc 2026-10-19T03:49:01Z`); counting command and date
(`AGENTS.md:22`); durable sources with SHA-256 for `claims.json`
(`ba69090f…`) and `targets.json` (`342c8f80…`) — both digests re-verified by
this seat; requested allocation kept separate from observed (`AGENTS.md:23-24`);
prior-route evidence for the opencode-go key choice; `closing_snapshot` field
already records the `open-at-seat-close` state (`AGENTS.md:32`). No credentials
(`AGENTS.md:30-31`) — C8.

**Gaps (each cheap to close).**

1. *No explicit unknown counters.* `AGENTS.md:25-26` requires unknown counters
   to stay `null` **with an owner and reason**. The record instead defers in
   prose (`"observation": "pre-dispatch declaration; …recorded in a separate
   observed-dispatch record after the batch returns"`). Fix: the observed
   record owed at close (`reports/round-33/telemetry/observed-dispatch.json`,
   absent at `04:00:05Z`) must carry `launches`, `completions`, `failures`,
   `runtime_concurrency`, `actual_route` as integers or explicit
   `null` + owner + reason — never inferred zeroes (`AGENTS.md:25-26`).
2. *Composition taxonomy drift.* The record's `seat_composition` folds the
   verifiers and scribes into "A-executors (10 audit + 4 verify + 2 scribe)" and
   counts 5 scribes; `targets.json`'s own `role` fields give
   scout 4 / planner 2 / connector 1 / executor 34 / verifier 4 / reviewer 8 /
   critic 4 / scribe 7 = 64. Totals agree, labels do not. Fix: have the observed
   record cite the role counts **read from `targets.json`** rather than a prose
   paraphrase.
3. *Closing snapshot mechanics.* `AGENTS.md:32-39`: when `validation.json`
   lands, the closing snapshot must be a **new** file that names the record it
   closes and that record's SHA-256 **at close time**. At my observation the
   record's digest is `139b964e…`; if it is edited in place before close, the
   snapshot's cited digest will mismatch by design. Recommendation: treat
   `dispatch-declared.json` as frozen from `03:49:01Z` and file the observed +
   closing records as new files.

## 5. X02-F4 — report-shape readiness: what is owed at close

Absent at `04:00:05Z` (all verified by `test -e` / `ls`):

| Owed artifact | Required by | Detection command |
|---|---|---|
| `reports/round-33/run-validation.py` | `REGIMEN.md:57-58` ("for every admitted round … exits 0 at close time") | `test -s reports/round-33/run-validation.py` |
| `reports/round-33/validation.json` | `REGIMEN.md:57-58`; `AGENTS.md:33` (triggers the closing snapshot) | `test -s reports/round-33/validation.json` |
| SCORECARD.md round-33 row (verdicts + before→after, no scalar aggregation) | `REGIMEN.md:44` | `grep -n 'round 33' SCORECARD.md` (SCORECARD.md unmodified at `04:00:05Z`, mtime `2026-10-18 22:03:28`) |
| LOG.md round-33 entry, lane identity, append-only | `REGIMEN.md:45-46`, `AGENTS.md:5-7` | `git diff --stat LOG.md` must remain insertions-only after the parent appends |
| Fleet report `/home/vgpnk/Projects/shokunin/.ufo/reports/round-33/kotodama.md` with **Work performed / Landed changes / Before→after / SHONEN** | `REGIMEN.md:46-48` | dir absent at `04:00:05Z`; shape template `…/.ufo/reports/round-32/kotodama.md:1,16,70,88,109` |
| `MANIFEST.json rounds[]` entry | `REGIMEN.md:48` | see below |
| Telemetry observed + digest-pinned closing snapshot | `REGIMEN.md:49-50`, `AGENTS.md:32-39` | `test -s reports/round-33/telemetry/observed-dispatch.json` |

**MANIFEST target must be the durable fleet file.** The durable fleet MANIFEST
is `/home/vgpnk/Projects/shokunin/MANIFEST.json` (247 rounds, kotodama entries
through round 32; round-32 entry shape: `round/date/type:"closure"/
lanes.kotodama:"ok"/lane_rounds.kotodama/promotions:[]/minted:[]/admitted/
verdicts{6 axes}/notes`). The lane-local copy
`kotodama-shokunin/.scratch/MANIFEST.json` is **stale** (its kotodama entries
stop at round 30) and is gitignored (`.gitignore:6` `.scratch/`) — a round-33
entry filed only there would not be durable. This is a fleet-root write, i.e.
outside this repo; it belongs to the parent, and `reports/round-33/adj/A03-scope.md`
scope-watch must name it as the one legitimate external write if it happens.

## 6. X02-F5 — lane identity exposure (no violation found)

`git config user.name` → `kotodama-shokunin`; `user.email` →
`kotodama@shokunin.local` (local config). No violation this round: HEAD is
still `139e3b6`, `git reflog -5` shows no post-baseline entry, `git stash list`
is empty, and the only tracked modification is `LOG.md` (parent, pure append).
The exposure to note for the close record: because the lane identity is
*configured*, a stray seat `git commit` would carry exactly the identity the
integrator's commit is supposed to carry — so the round's "no seat commits"
claim must be evidenced by content (`git log --oneline 139e3b6..HEAD` at close
lists only the integrator's declared round-33 commits) rather than by author
string.

## 7. X02-F6 — fragment-format sweep (42 files at 04:00:05Z)

All 41 seat fragments: seat id matches the `targets.json` assignment for their
path, `## Owed` present, `## Citations` present, `to-verify` used (0–14 marks
per file). No file was written outside its assigned out path (C1).

Five header-line deviations, all cosmetic (seat id + role + date + baseline are
present in every case; the required literal shape
`- Seat: <ID> | <role> | <claim> | date 2026-10-19 | baseline 139e3b6` is not):

- `reports/round-33/adj/A03-scope.md:1` — `- Seat: A03 | executor (scope watch, claim A) | claim A (adjacency) | date 2026-10-19 | baseline 139e3b6`
- `reports/round-33/adj/A10-receipt.md:1` — `- Seat: A10 | executor | A | 2026-10-19 | baseline 139e3b6` (no `claim`/`date` words)
- `reports/round-33/calib/C04-item-04.md:1` — `… | executor (claim C / calibration, open item 4) | box-1 citation conditions 2-4 | date …`
- `reports/round-33/calib/C08-item-08.md:1` — `… | claim C (calibration) | item 8 = OI-08 (lore-owned bilateral same-revision read) | date …`
- `reports/round-33/op/K02-lessons-census.md:1` — `- Seat: K02 | scout (claim O, leg a) | lessons census: … | date …`

Recommendation: the close-time validator should accept
`^- Seat: <assigned-id> \|` plus role token plus `date 2026-10-19` and
`baseline 139e3b6` on line 1, and record the five deviations as cosmetic in the
round report rather than rewriting filed round-33 fragments in place (the
append-only habit should not be relaxed for a cosmetic gain).

`reports/round-33/telemetry/dispatch-declared.json` is the only file under
`reports/round-33/` that is not a seat fragment and not in `targets.json`'s
`out` map — correct, it is the parent's telemetry record (section 4).

## 8. Close-time conformance checklist (paste-ready)

```sh
# 1. filed bytes preserved (git-level)
git status --porcelain -uall -- 'reports/round-[0-9]*' | grep -v '^?? reports/round-33/'   # must be empty
git diff --quiet HEAD -- corpus/lessons tools/gates/frozen SKILL.md PROVINCE.md SCORECARD.md AGENTS.md; echo "exit=$?"  # 0 unless a declared integrator edit
# 2. r5/r7 receipts at their pinned digests (independent of git)
sha256sum reports/round-5/validation.json reports/round-7/validation.json
#   expect 73a66f74… (r5) and 2f4c1e15… (r7)
# 3. LOG append-only
git diff --stat LOG.md                    # insertions only, never deletions
# 4. no seat commits
git log --oneline 139e3b6..HEAD           # only declared integrator commits
# 5. owed artifacts
for p in reports/round-33/run-validation.py reports/round-33/validation.json \
         reports/round-33/telemetry/observed-dispatch.json \
         /home/vgpnk/Projects/shokunin/.ufo/reports/round-33/kotodama.md; do test -s "$p" || echo "MISSING $p"; done
grep -n 'round 33' SCORECARD.md
# 6. telemetry closing snapshot cites the declaration digest 139b964e… (or records could-not-recover)
```

## Owed: none

## Citations

- `reports/round-33/targets.json:6-10,12-83,75`; `reports/round-33/claims.json:6,19-38,66-71`
- `REGIMEN.md:44,45-50,57-58`; `AGENTS.md:5-9,15-39,30-31,32-39,40-42`; `.gitignore:6`
- `git status --porcelain -uall` (2026-10-19T03:54:27Z, 03:56:38Z, 04:00:05Z); `git diff --stat LOG.md`; `git diff --stat AGENTS.md`; `git reflog -5`; `git stash list`; `git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb`; `git config user.name|user.email`
- `stat -c '%y'` on `reports/round-5/validation.json` (03:54:15.802Z dirty, 03:55:27.940Z restored), `reports/round-7/validation.json` (03:54:18.609Z, 03:55:27.940Z), `LOG.md` (03:42:59Z), `SCORECARD.md` (2026-10-18 22:03:28), `AGENTS.md` (2026-10-18 20:49:59)
- `sha256sum` → dirty r5 `fe926984…`, dirty r7 `af0cf4ed…`; restored/HEAD r5 `73a66f7464ead0d99318750422256ceafac3d8c2d283f94604eb258abc1bb794`, r7 `2f4c1e159b60d78250074c51f013d13aac3cf1b140a623d197a0883e5ecac6f3`; `git show HEAD:reports/round-{5,7}/validation.json | sha256sum` (same two values)
- In-place publishers: `reports/round-5/run-validation.py:194`, `reports/round-6/run-validation.py`, `reports/round-7/run-validation.py:1171`; `grep -l 'HERE / "validation.json"' reports/round-*/run-validation.py` → 3 paths; no `--check` in `reports/round-{5,6,7}/run-validation.py` (vs `reports/round-32/run-validation.py:2`)
- Pin/reader exposure: `reports/round-20/validation.json:17150-17151,17372-17373`; `reports/round-23/wording/evidence/tie-break-check-receipt.json:17031-17032,17253-17254`; `reports/round-6/run-validation.py:283`; `reports/round-6/check-checkpoint.py:99`; `reports/round-33/op/O07-baseline-receipt.md:171,174`
- Claim-C context: `reports/round-33/calib/C16-receipt.md:67`; `.scratch/c05-tmp/r5.log|r6.log|r7.log` (03:54:39–42Z); `.scratch/c05-iso/` (03:54:37Z) incl. `reports/round-5/validation.json` = `fe926984…`
- `reports/round-33/telemetry/dispatch-declared.json` (sha256 `139b964ead124364443d208cb858967b12a108532eab01b22229dfea1c1ad9ac`); re-verified `claims.json` `ba69090f…`, `targets.json` `342c8f80…`
- `/home/vgpnk/Projects/shokunin/MANIFEST.json` (247 rounds; kotodama through r32) vs stale gitignored `.scratch/MANIFEST.json` (kotodama last r30)
- `/home/vgpnk/Projects/shokunin/.ufo/reports/round-32/kotodama.md:1,16,70,88,109`; `…/.ufo/reports/round-33/` absent at 04:00:05Z
- Credential scan and language scan outputs as quoted in C8 and §7; header sweep script output over the 42 landed files at 04:00:05Z
