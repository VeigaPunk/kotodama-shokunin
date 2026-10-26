# ScribeSkillGates — round 75, wave 1: SKILL.md §Gates and probes rows for the 75 counters

Seat: scribe, leaf (no dispatch). Lane `kotodama-shokunin`, base `f556d1049fe651d3d63975600b13acd9fb686f15`
(= worktree HEAD and every read below; `git status --porcelain` shows only the untracked round-75 wave
and report directories). Nothing was committed, staged, pushed, or written outside the two paths named
at the end. No fetch, no network access, no tool install (so no User-Agent record, no install entry).
No scratch directory was created — the work needed none under
`/fast/scratch/hyaku/kotodama-r75/ScribeSkillGates/`.

## Behaviour — what was produced

`.ufo/waves/round-75/drafts/skill-gates-rows.md` (126 lines, 17,028 B, sha256 `2a6e5d5e8f50aab82699e02f0d61162a140ee06cc32e8779b500deeed0e4484c`)
drafts, verbatim and in the exact eight-column shape of the `accept-c-74` / `accept-ca-74` rows:

| drafted row | content | source of every clause |
|---|---|---|
| `accept-c-75` | entry command with required `--freeze` and optional `--fleet-root`; `PASS legs=13/13` / `FAIL legs=<n>/13` / refusal `FAIL legs=0/13 (refused: …)` exit 2; stale-tree refusal (`--freeze` off the lands first-parent chain); `lands == base` refusal; LEGCOUNT refusal; `lands == freeze` graded, never passed; selftest receipt `reports/round-75/telemetry/selftest-c.txt`; pinned values read with `git show <freeze>:reports/round-75/claims.json`; read-only write scope | claims C (`legs` 13), claims C `do_nothing_control`, QUALITY 25(a)/26(a)(c)(d), round-74 row precedent |
| `accept-ca-75` | same CLI shape plus required `--fleet-root`; `PASS legs=12/12` / `FAIL legs=<n>/12` / `REFUSED` exit 2; stale-tree refusal; `lands == freeze` graded with REPAIR/ANNOTATE/R1EXEMPT red and FROZENCFG/LEDGER green, and a green `lands == freeze` run refused; `--main` consumed by STAMP **and** by RECEIPTS; pinned values incl. the nine-entry observe allowlist, `min-pairs` 10, fleet pin, round-74 lands/freeze and its required `ACCEPT-CA-74: PASS legs=11/11` line, `r1exempt-{green,red}.txt`, `measures-ca-head.txt` | claims Ca (`legs` 12, RECEIPTS, COMBINED, STAMP, APPENDONLY/R1EXEMPT), QUALITY 26 |

"Round introduced 75" is stated in both pinned-values cells. The legs fraction is written as frozen at
freeze time: the denominator is the frozen `legs[]` length read at `--freeze`, a mismatch is a LEGCOUNT
refusal printing `legs=0/<n>`, and nothing renumbers from the graded tree. Stale-tree behaviour is a
refusal in both rows, and the graded (not refused) `lands == freeze` case is spelled out per row.

Also drafted, as a proposal only: seven `## Error patterns` signature rows in the table's existing
style (dash token, then the reading with its pointer), preceded by the measured precedent that the
last five signatures landed in round 69 (`e86ed3e`) and no later round added one — `975e8f2` only
edited those five rows, and every later `SKILL.md` hunk sits in the gate-row region.

## Gates — what was and was not run

| gate/check | run? | result |
|---|---|---|
| `reports/round-75/accept-c.py` (any mode) | no | file absent: `reports/round-75/` holds only `claims.json`, `ledger.json`, `telemetry/` (empty) |
| `reports/round-75/accept-ca.py` (any mode) | no | same |
| `--selftest` for either counter | no | no counter bytes exist; a selftest string would be fabricated |
| read-only anchor probes on `SKILL.md` at base | yes | heading `619`; header row `648` (second bounded table header `761`); last registry row `707` (a `note`); `gate`/`probe` count `45`; `accept-*.py` count `45` |
| claims/ledger field verification | yes | `python3 -c` on both JSON files, twice (see drift note) |
| git mutation of any kind | no | only `git show`, `git ls-tree`, `git log`, `git show <c> -- SKILL.md` |

Consequence stated in the draft, not hidden: every behavioural clause is **contract-only**. Round 74
showed the built counters disagreeing with their own row (`accept-c.py` passed `lands == freeze`,
`accept-ca.py` refused only the green form), so the rows name the claims as authority and say that a
built counter which refuses differently means the rows are rewritten to the built behaviour after the
claims — never the reverse.

## Touched surfaces

| path | action |
|---|---|
| `.ufo/waves/round-75/drafts/skill-gates-rows.md` | created (this seat's deliverable) |
| `.ufo/waves/round-75/w1/ScribeSkillGates.md` | created (this report) |

Nothing else was created, modified or deleted. `SKILL.md`, `reports/round-75/claims.json`,
`reports/round-75/ledger.json`, `corpus/**`, `LOG.md`, `SCORECARD.md`, the fleet repo, the lane's
git index and jj state are untouched.

## Out of scope (deliberately not done)

- `SKILL.md` was not edited, including the insertion at lines 706/707 that the draft specifies.
- No counter was written, reviewed for correctness, or patched; no `--selftest` receipt exists to file.
- No claim, ledger pair, correction row, lesson row, README index row, LOG or SCORECARD text was authored.
- No source was opened and no evidence capture made (claim C's Gate work belongs to the scouts/executors).
- No gate was run against the lane; the draft asserts nothing about round-75 bytes that a seat measured.

## Findings (for the freeze and for the canonical judge)

1. **Counters absent at read** — `.ufo/waves/round-75/counters/` held only `capture-evidence.py`
   (63,598 B, sha256 `2eb12195c9d944fe49f2302d9a43558eea3c9e04d7198275a063b3c86b95a62c`) and a `fixtures/`
   directory; no round-75 `accept-c.py`/`accept-ca.py` anywhere in the lane. The rows therefore pin no counter
   sha256 and no selftest count: QUALITY 26(d) requires both to be re-derived from installed bytes
   before landing, and round 74 landed a row whose `76d00b88325f…` / `138 checks across 37` existed
   nowhere.
2. **`lands == freeze` is contested and its red set is unnamed** — claim C's `do_nothing_control` says
   that shape FAILS "with the data legs red and FROZENCFG green"; QUALITY 26(c) records that round-74
   `accept-c.py` graded and PASSED it and requires a round relying on it being red to call it a
   do-nothing control only. The draft row does not enumerate the red legs (GROUND and CENSUS grade base
   bytes and may be green by construction); the freeze must name the asserted set and the selftest
   must assert exactly that set.
3. **Claims draft moved during the window** — `reports/round-75/claims.json` was rewritten 19075 → 19300 B
   at 13:57 (now sha256 `0f4fd1b040f75af9af055926058eb28e9b3b5ab7826ce3366ffa5f1d82e16a42`); every cell
   was re-read against those bytes and the fields the rows rest on are unchanged (13/12 leg rosters and
   names, `row_set` S885..S892, `map.sha256` null, both `counter` strings, both controls). Ledger at
   sha256 `48a8bc443fa8a90be7fba0bb497b16279616720f9427b462535a735d29f7d61c`, 11 pairs, `must_track []`.
4. **`--main` is no longer STAMP-only** — Ca `RECEIPTS` pins `--main 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`
   for the nested round-74 run, so the round-74 row's "consumed only by STAMP" is stale for round 75;
   the drafted row says STAMP **and** RECEIPTS and lists the value.
5. **Allowlist is nine executables, not ten** — claims Ca `LEDGER` names
   {git, grep, wc, sha256sum, ls, cat, head, tail, cut}; the round-74 row printed "ten allowlisted
   observe executables". Draft uses nine. (Counted, not copied.)
6. **`map.sha256` is `null`** in the draft claims while FROZENCFG compares `git show <freeze>:<map>` to
   that constant; it must be filled in the freeze commit or the leg cannot pass (round-74 placeholder
   failure, `# frozen map:`).
7. **Round-70 invariant arithmetic** — `gate`/`probe` rows naming a round counter and committed
   `accept-*.py` files both count 45 at base; appending two `gate` rows with their two counter files
   keeps `47 == 47`. A `gate` row without its counter (or the reverse) breaks it; a `note` row would not.
8. **`L75-08` re-located** — the promised sentence exists verbatim at
   `/home/vgpnk/Projects/shokunin/.ufo/reports/round-74/kotodama.md:20`
   (`Lane pushed hash: see the closing line below (git ls-remote origin refs/heads/main)`) and the file's
   last line is the Misroot-sweep sentence, so the pair is grounded; the Error-patterns row cites the
   file line, not the claim's paraphrase.
9. **Precedent for the Error-patterns block** — last addition was round 69 (`e86ed3e`, five signatures);
   rounds 70–74 added gate/`note` rows and repaired that table but added no signature row. The block is
   a decision for the lesson scribe/L1, not a carry-forward, and the seventh candidate
   (`promised-hash-without-line`) is carrier-scoped to the fleet report rather than the lane registry.

## Artifact paths (relative to `/home/vgpnk/Projects/shokunin/kotodama-shokunin`)

- `.ufo/waves/round-75/drafts/skill-gates-rows.md` — the row draft (126 lines, 17,028 B, sha256 `2a6e5d5e8f50aab82699e02f0d61162a140ee06cc32e8779b500deeed0e4484c`)
- `.ufo/waves/round-75/w1/ScribeSkillGates.md` — this report
