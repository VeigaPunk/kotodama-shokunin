# Round 87 — non-author closure spot-check

author: hyaku closure (non-author integrator, @m_zfl)

Reviewed round: kotodama r87, 2026-11-04. Base
`83846a22ee1e9da7aa52ac505ccebf4455169247`; delivered lane tip
`2e86e988ba9a649260e557d0e4f465bba2e10bac`. This verifier did not author the
round. Three fresh read-only seats (claim re-derivation, Gate source
spot-check, adversarial no-harm/conformance) inspected committed bytes; none
executed a lane gate, selftest, counter or production tool, and none wrote or
ran `jj`. This integrator re-ran every census, hash and ancestry command below
itself.

Dispatch/completion digest (copied from `.ufo/watchdog.log`, mutable):

```text
2026-11-04T15:23:57-03:00 launch kotodama round=87 pgid=409133 driver=hyaku-inline attempt=1
2026-11-04T15:45:11-03:00 complete kotodama round=87; hyaku-inline attempt=1
```

## Conformance

- Real report, not a marker: `.ufo/reports/round-87/kotodama.md` (274 lines)
  names one checkable claim, landed commits, measurements, Sources &
  frontier, trend verdicts and an author-asserted SHONEN assessment
  (`## SHONEN` at line 264). `git log --format='%an %H' -- .ufo/reports/round-87/kotodama.md`
  returned `kotodama-shokunin 6ecff55a3afcd8cc96c67bfeceaaabe509e7ce23`;
  the committed blob equals the working file (both sha256
  `44d15a4124a861048c94c7c3684d0c0d5c0aa28798562390220abfea94362e33`).
- Cited lane commits exist and are ancestors of the branch:
  `git -C <lane> merge-base --is-ancestor <h> refs/heads/main` returned 0 for
  `732c45394c73fcffd9fc623b939d446c7b11a9db`, `2a3b5643899c3520867ae930593cafef6ef19cad`,
  `12903255b6d3c940d18e6b81dce4d7cf49d519c2`, `2e86e988ba9a649260e557d0e4f465bba2e10bac`
  and base `83846a22ee1e9da7aa52ac505ccebf4455169247`. Committer times
  (`732c4539` 15:27:23, `2a3b5643` 15:27:48, `12903255` 15:40:42, `2e86e988`
  15:42:55) are ordered after the 15:23:57 launch. `732c4539`'s *author*
  stamp 15:22:28 predates the launch because jj stamps the working-copy
  change when it is created — the base is the previous integrator's
  `83846a22` commit at 15:22:28 — so this is not backdating.
- Lane state: `scripts/hyaku/jj-lane.sh state <lane>` returned
  `branch=main local=2e86e988ba9a649260e557d0e4f465bba2e10bac remote=2e86e988ba9a649260e557d0e4f465bba2e10bac ahead=0 behind=0 head=detached tracked=0 untracked=1`;
  `git ls-remote origin refs/heads/main` printed the same hash.
  `git status --porcelain` returned one entry,
  `?? .ufo/waves/round-79/w1-results.json` — not round-87 work: the fleet
  inline dispatcher adopted a stale round-79 `w1.ready` (32 seats) at
  15:31:39 and wrote that file at 15:31:50
  (`.ufo/state/inline-dispatcher.log:113070,113074`). No modified tracked
  file and no uncommitted round-87 work.
- Prompt: `.ufo/prompts/kotodama-round-87.md` (793 lines) is committed at
  `07e734c6f779503a837ed97442baa70f7f36f9ed` under `kotodama-shokunin`
  ("dispatch evidence", inline attempt 1). Substituting `LANE`/`ROUND`/`FLEET_ROOT`/`AXES`
  into `templates/round-prompt.md` and diffing its 140 lines against prompt
  sections 1–5 returned exactly one differing line — the template's
  `{{FLEET_ROOT}}/<{{LANE}}-repo>` working-dir line, rendered by the driver
  as the real `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. All five
  child-lane items are present verbatim (report path/filename, SHONEN
  heading, commit-hash citation rule, commit-before-report with pre-report
  `ls-remote` gate, push/write scope) plus mission/axes, L2 floor and the L0
  side channel; the hyaku addendum follows as §6.
- Report landed and pushed in the fleet repo: `git branch -r --contains 6ecff55a`
  lists `origin/main`; fleet remote head was `8a4920ed143534b332c850bdaf6a096858a9260e`.
- Wave evidence: `.ufo/waves/round-87/w1.ready.dispatched` records 10 names;
  `w1-dispatch.json` counts `spawn=10, total=10` in one dispatch;
  `swarm-registry.json` holds exactly 3 executor / 2 scribe / 1 scout /
  1 connector / 1 reviewer / 1 critic / 1 mutation-tester; all ten seat
  reports, `w1-results.json` (all ten `output: null`), `wave-done.json` and
  `wave-summary.json` are committed. The kernel-restart statement matches
  committed bytes.

## Claim re-checks: re-measured versus evidence-verified

`tools/check-attestation-packet.py` and `reports/round-87/measure87.py` are
registered lane **gates** (`SKILL.md` `## Gates and probes`), so under the
Gate standard I verified their committed evidence and re-derived only plain
counts, hashes and existence. No gate, selftest or counter was executed.

### O / operability capability acquisition — improved, verifies (evidence-verified run; counts re-measured)

- Predicate (unchanged since the freeze): the committed tool scores exactly
  12/12 on `measure87.py` through its public `--packet PATH --json` CLI.
- Before: `git cat-file -e 83846a22:tools/check-attestation-packet.py` →
  `fatal: path 'tools/check-attestation-packet.py' exists on disk, but not in
  '83846a22…'` (rc 128; "on disk" is the worktree, the revision has no entry).
  `reports/round-87/no-work.json`: `rc=1`, stdout
  `{"label":"MEASURE87","revision":"83846a22…","passed":0,"total":12,"finding":"TOOL_ABSENT"}`.
- After: `reports/round-87/lands-o.json` carries `rc=0`,
  `revision=12903255…`, 12 cases, `passed=12/total=12`, every per-case
  `passed:true`, and `candidate_sha256=4abcbbd0…`,
  `counter_sha256=131b29e8…`, `baseline_packet_sha256=4f631b60…`.
  `tool-selftest.json` `rc=0`, 37/37 checks, none failed.
  `tool-original-packet.json` `rc=0`, stdout `{"findings": [], "records": 6}`.
  `final-checks.json` lists all seven after-checks at `rc=0`.
- Hash re-measurement (this integrator): `sha256sum` of
  `git show 12903255:tools/check-attestation-packet.py` and of the tip copy
  both give `4abcbbd058c33b95cc7c8acc4840493ccaeda0bdf01cb3947d074c3352c497aa`;
  `git diff 12903255 2e86e988 -- tools/check-attestation-packet.py` is empty,
  so the tool is byte-unchanged after the measured revision.
  `measure87.py` at the tip hashes `131b29e84d39c2cbd22993aaadd469b5a96602651927730c980503cc74738e62`,
  identical at `732c4539`, `2a3b5643`, `12903255` and `2e86e988` (seat check) —
  the counter was not revised after the data. The base packet at
  `83846a22` hashes `4f631b60…`, matching the receipt.
- Static re-derivation: `measure87.py` builds exactly 12 cases (3 requiring
  rc0 with `records=6, findings=[]`, 8 requiring rc1 and one named finding
  id, 1 requiring rc2 `ATTESTATION_ERROR`); each expected id exists in the
  tool's vocabulary (`RECORD_ID`, `CLOCK_MISSING`, `CLOCK_REASON`,
  `CLOCK_DATE`, `RECORD_FIELD`, `SOLUTION_CONFLICT`, `EDITORIAL_CONFLICT`,
  `TRANSLATION_CLOCK`, `ATTESTATION_ERROR`); the tool reads packet content
  and emits per-record findings, so a constant pass cannot satisfy the eight
  dirty cases (the committed `constant-pass` control records 3/12).
- Limits of the instrument, recorded and not repaired here (see Routed
  defects): the battery accepts expected-id **membership**, not equality, so
  a shotgun-id auditor would also reach 12/12; `total=12` in the
  `TOOL_ABSENT` branch is a literal; `CLOCK_SCOPE` is emitted but unexercised
  by the battery. The report already discloses the filename/label survivors
  and the null-findings crash; the shotgun case is an additional limitation.

### Sources & frontier — re-measured

- Independent awk census over `git show <rev>:corpus/SOURCES.md`
  (`^[ ]{0,3}\|[ ]*S\d{3,}[ ]*\|`, fields 5 and 9):

```text
rev=83846a22… rows=852 tier[A]=504 tier[B]=326 tier[C]=22 status[mined]=752 status[queued]=58 status[rejected]=42
rev=2e86e988… rows=854 tier[A]=505 tier[B]=326 tier[C]=23 status[mined]=753 status[queued]=58 status[rejected]=43
```

- `comm` over the ID-keyed row lines: `0` base rows changed; exactly `S929`
  and `S930` added. `git diff --numstat 83846a22 2e86e988 -- corpus/SOURCES.md`
  → `5 0` (rows, one Paths bullet, one search-log paragraph; no old cell changed).
- `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`
  returned exit 0 with 36 lines, final
  `kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`.
  Pre-existing W01 tier-C/mined and W04 duplicate-URL warnings persist and
  are not called repaired.
- No-harm: `git diff --name-only 83846a22 2e86e988 -- corpus/knowledge PROVINCE.md`
  is empty; `git diff --numstat -- SCORECARD.md` → `40 0` (one capability
  row added, one axis section appended, no score decreased).

## Per-axis verdicts

| Axis | Verdict | Evidence |
|---|---|---|
| operability | **improved** | capability row added; absent-at-base path now a 240-line CLI with 12/12 frozen battery, 37/37 CLI selftests and a clean original packet, all hash-bound |
| calibration | **unchanged** | R87-M1/M3 self-corrections and preserved unfavorable probes are recorded, but the SHONEN seed/pointer edits were silent (R87-C7) and SCORECARD records no new calibration score |
| depth | **unchanged** | no knowledge entry added or deepened; no dossier change |
| coverage | **unchanged** | PROVINCE.md untouched; no frontier topic promoted |
| freshness | **unchanged** | no external source re-verified; the round-11 L0 pause and R86-C1 numeric/lowest-axis debt are retained, not waived |
| adjacency | **unchanged** | no cross-domain absorption; ConnectorScope reports lore/chousa authority boundaries |

## Discernment spot-check

Both Gate candidates were sampled (all admitted rows plus the reject);
sources were re-opened at the cited revisions.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S929 | admit A / mined, scoped to the fictional interface only | `git show 83846a22:.ufo/waves/round-86/w1/stage/ExecCraftLedger/craft.json` line 5 (`boundary`); sha256 `4f631b60…` | **agree** (one low presentation defect) | the boundary field stipulates fictional authorship and the packet is `status: NON-CANON`; tier A own-work and `mined` via the lesson both fit. The committed quote is a verbatim 13-word **prefix** of a 20-word sentence and drops ", not quotations, source evidence or lore proposals" without an ellipsis (R87-C3); decision unaffected |
| S930 | reject C, scoped to suitability as a packet-reader implementation | `git show 732c4539:reports/round-87/controls/constant-pass.py` line 2 (module docstring); sha256 `78b66e10…`; byte-identical to the stage copy | **agree** | the file reads no input and prints a fixed `{'records': 6, 'findings': []}`; rejection with a stated, falsifiable flip is honest and preserves it as a negative control |

New-row quote check (`corpus/SOURCES.md:885-886`): S929 quote 13 words, S930
quote 8 words, both ≤25 and both locatable verbatim at the named line; row
tier/status/used-by cells match the lesson. No `could not re-open`.

## Trend verdicts

- **expansion: improved** — a capability is admitted to `SCORECARD.md`
  (LEARNING's explicit expansion observable) and its demonstration verifies;
  no knowledge entry or frontier promotion is claimed, and the report says so.
- **quality: unchanged** — no knowledge entry re-verified, deepened or
  superseded and none found false and left unmarked; new criterion 34 binds
  round 88 and is grounded in R87-M2, so it does not retrofit this round.
- **discernment: improved** — this outside spot-check agrees with the Gate on
  both the admit and the reject, and the round turned prior non-author
  findings (R86-C2/C3) into named lessons plus prospective criterion 34.

## Routed defects for the lane (status-neutral; fix next round)

1. **R87-C1 (counter).** `measure87.py:55` accepts expected-id membership, so
   a tool that emits every finding id on any dirty input still scores 12/12.
   Add exact id-set equality plus a no-extra-id negative case in a *new*
   freeze; do not retrofit the current frozen predicate.
2. **R87-C2 (counter).** `total=12` in the `TOOL_ABSENT` branch is a literal
   (`measure87.py:99`), not `len(cases())`; a future case would misreport the
   denominator.
3. **R87-C3 (quotation).** S929's 13-word prefix omits the clause that most
   supports its scope. Add an ellipsis or use the full 20-word sentence in
   both the lesson and the row; sweep every mention per CORPUS rule.
4. **R87-C4 (LOG binding).** The report's `732c4539` row claims the "counter
   transport selftest", but `LOG.md` contains `measure87` and
   `counter-selftest` zero times and item 1 describes the tool that landed
   only at `12903255`. Add the missing binding in the next appended entry.
5. **R87-C5 (receipt pinning).** `census-start.json`/`census-end.json` carry a
   hand-written `revision`; `scripts/sources-census.sh` takes no revision and
   reads the live tree. Keep revision claims in revision-addressed receipts
   (`registry-counts.json` already does this) and label the census as a
   worktree run.
6. **R87-C6 (underived number).** "attack3/10" rests only on
   `wave-summary.json`; the committed dispatch prompts one seat with "Attack".
   Record the counting rule or the three seat names.
7. **R87-C7 (SHONEN transparency).** `SHONEN.md` box 2's pointer was swapped
   from the r86 Iron positional run (`reports/round-86/lands-o.txt`) to r87
   synthetic-packet audits, and the "Marks:" legend was deleted, with no
   disclosure in report or LOG. The legend removal is defensible (the
   mechanical seed is the indented block; 21/21 fleet lanes lack it; the old
   legend pointed at a heading no SHONEN.md carries) but a normative-text
   change must be named. Marks correctly stayed `[~]`; no `[x]` was written.
8. **R87-C8 (report precision).** "Both lane commits" while four are cited;
   "all852 old lines" conflates registry rows with physical lines; the
   addendum is cited as "lines4790 onward" though it begins at `LOG.md:4828`.
   Report SHONEN bullets each span two physical lines where the contract says
   one line per box.
9. **R87-C9 (inherited tree state).** The untracked
   `.ufo/waves/round-79/w1-results.json` is orchestrator scratch from a stale
   round-79 `w1.ready`, not lane work; the lane should attribute-and-commit or
   remove it and name the decision next round. This integrator did not touch it.
10. **Inherited debt re-flagged.** R86-C1 numeric/lowest-axis mapping,
    R86-C4 L2 planner conflict, R86-C5 full cited-record red on non-author r84
    and R86-C2 empty-decision-cell/duplicate-ID counter debts remain open; the
    lane's registry kind strings (`gate (capability)`, `gate (round counter)`)
    are not recognised as gates by its own `check-gate-registry.py` 8-cell check.

## Admission

Every declared claim verifies from committed bytes and no axis is harmed:
**admitted**. Promotion is operator-owned — the four SHONEN boxes carry
resolvable pointers and look mechanically checkable by a non-author, but box 2
rests on a bounded structural audit (domain trial 5/6), and no box was
upgraded here. Tools installed or upgraded: none.
