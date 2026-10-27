# SKILL.md §Gates and probes — round-75 rows (W1 draft), plus `## Error patterns` candidates

Seat `ScribeSkillGates`, wave 1, round 75 (hyaku run 10). **SKILL.md is not edited by this seat and
must not be landed from this file before the freeze commit exists.** The canonical writer (L1) applies
the two `gate` rows; the `## Error patterns` block is a proposal, not a queued edit.

- Lane base and worktree HEAD at every read below: `f556d1049fe651d3d63975600b13acd9fb686f15`
  (`git rev-parse HEAD`; `git status --porcelain` shows only the untracked round-75 wave and report dirs).
- Claims read (DRAFT, `frozen: null`, sha256 `0f4fd1b040f75af9af055926058eb28e9b3b5ab7826ce3366ffa5f1d82e16a42`,
  19300 B at 13:57): claim C `legs` 13, claim Ca `legs` 12. Ledger read (DRAFT, sha256
  `48a8bc443fa8a90be7fba0bb497b16279616720f9427b462535a735d29f7d61c`): 11 pairs `L75-01`…`L75-11`,
  `fleet_pin 3a7401609325341eb3fe0efd42d0eec29d06be3c`, `must_track []`. Both files were rewritten
  during this seat's window (claims 19075 → 19300 B); the fields these rows rest on were re-read after
  the rewrite and are unchanged (leg rosters and names, `row_set` S885..S892, `map.sha256` null, both
  `counter` strings, both `do_nothing_control` sentences).
- **Counters do not exist at this read.** `.ufo/waves/round-75/counters/` holds only
  `capture-evidence.py` (63,598 B, sha256 `2eb12195…`, written 14:00) and a `fixtures/` directory;
  `reports/round-75/accept-c.py` and `reports/round-75/accept-ca.py` are absent and
  `reports/round-75/telemetry/` is empty (`ls` at 13:55 and 14:00). Every behavioural clause below is
  therefore read from the frozen-shape contract (claims C/Ca, QUALITY 25/26) and is **contract-only:
  nothing in this file is a measurement of a round-75 counter**. The rows deliberately pin no counter
  sha256 and no selftest count; QUALITY 26(d) requires both to be re-derived from the installed bytes
  before landing, and round 74 landed a row whose sha256 and scenario count existed nowhere
  (`corpus/lessons/round-74.md` Corrections, `SKILL.md` row `accept-ca-74`).

## 1. Anchor (measured, read-only)

| probe | command | result |
|---|---|---|
| section heading | `git show f556d10…:SKILL.md \| grep -n 'Gates and probes'` | `619:## Gates and probes` |
| header row, main table | `git show f556d10…:SKILL.md \| grep -n '^| name | kind |'` | line `648` (and line `761`, the bounded D3 table, same eight columns) |
| last registry rows | `git show f556d10…:SKILL.md \| grep -n '^| accept-' \| tail -4` | `704 accept-ca-73`, `705 accept-c-74`, `706 accept-ca-74`, `707 accept-c-73 / accept-ca-73 correction (note)` |
| `gate`/`probe` rows naming a round counter | `git show f556d10…:SKILL.md \| grep -cE '^\| [^|]+ \| (gate\|probe) \| .*reports/round-[0-9]+/accept-[a-z]+\.py'` | `45` |
| counter source files under `reports/` | `git ls-tree -r --name-only f556d10… reports \| grep -c 'accept-.*\.py$'` | `45` |
| `## Error patterns` table | `git show f556d10…:SKILL.md \| sed -n '505,535p'` | `\| Observation \| Reading \|`; last five rows are the round-69 signatures |

Insert the two rows **after line 706 (`accept-ca-74`) and before line 707 (the round-73 correction
`note`)**: registry rows stay in round order and `note` rows trail, which is how round 74's three rows
were placed. Column shape is line 706's, eight cells, and no cell below contains a `|`.

Arithmetic the landing must keep: two new `gate` rows naming `reports/round-75/accept-c.py` and
`reports/round-75/accept-ca.py`, landed together with both counter files, move the invariant from
`45 == 45` to `47 == 47`. A `gate` row without its counter file (or the reverse) breaks it; a `note`
row would not.

## 2. Rows to append (verbatim)

| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |
|---|---|---|---|---|---|---|---|
| accept-c-75 | gate | `python3 -B reports/round-75/accept-c.py --root . --lands <40-hex> --freeze <40-hex> [--fleet-root /home/vgpnk/Projects/shokunin]` | Output ends `ACCEPT-C-75: PASS legs=13/13` (exit 0) or `: FAIL legs=<n>/13` (exit 1, n = passing legs). A refused run prints `ACCEPT-C-75: FAIL legs=0/13 (refused: …)` and exits 2: missing, malformed or tree-absent `--lands` or `--freeze`; `--root` without `.git`; `--freeze` not an ancestor of `--lands` on the lands first-parent chain (a stale tree); `lands` equal to the frozen base; an unreadable frozen `claims.json`; a frozen `legs[]` list that is not exactly the thirteen implemented legs (LEGCOUNT); or a materialization failure. The `legs=` denominator is the frozen `legs[]` length read with `git show <freeze>:reports/round-75/claims.json`, never the graded tree, so the fraction is fixed at freeze time and a mismatch refuses instead of renumbering. `lands == freeze` is graded, never passed (QUALITY 25(a), 26(c)): the data legs read red with FROZENCFG green, exit 1 — the claim does not enumerate them, and of the thirteen only GROUND and CENSUS grade base bytes and may be green at that shape by construction, so the freeze must name the red set the control asserts. | `python3 -B reports/round-75/accept-c.py --selftest` — mktemp fixture repos asserting a clean `PASS legs=13/13`, the graded `lands == freeze` FAIL (every data leg red, FROZENCFG green), the `lands == base` refusal, the stale-tree refusal and a twelve-leg LEGCOUNT refusal; receipt `reports/round-75/telemetry/selftest-c.txt` is carried by the freeze commit (QUALITY 26(a)), and its self-stamp sha256 and selftest count are re-derived from the installed bytes before landing (QUALITY 26(d)). | round introduced 75; base `f556d1049fe651d3d63975600b13acd9fb686f15`; constants read by `git show <freeze>:reports/round-75/claims.json` — the eight adopted rows S885..S892, the staged ids S864..S876 and S885..S921 which appear in no entry as lane rows, the two `corpus/knowledge/myth-symbol/narrative-structure-frameworks*` entry paths, the by-document map `.ufo/waves/round-75/assimilation/id-renumber-map.json` with its sha256 (null in the draft, filled in the freeze commit), the eight gap-sweep fragments and two terms, the access date 2026-10-27, and the thirteen-leg roster ENTRIES, ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS, SCRATCHMIRROR, COLLCHECK, FROZENCFG, INDEX; `claims.json` at `<lands>` must be byte-identical to the freeze blob; no counter sha256 and no selftest count is pinned here (QUALITY 26(d)). | read-only; every graded byte comes from a temp clone checked out at `--lands` plus a `git archive` of the base, and the counter's own constants from `<freeze>`; the worktree is disclosed only; selftest fixtures live in mktemp dirs | kotodama-shokunin |
| accept-ca-75 | gate | `python3 -B reports/round-75/accept-ca.py --root . --lands <40-hex> --freeze <40-hex> --fleet-root /home/vgpnk/Projects/shokunin` | Output ends `ACCEPT-CA-75: PASS legs=12/12` (exit 0) or `: FAIL legs=<n>/12` (exit 1). Refusals print `ACCEPT-CA-75: FAIL legs=0/12 (REFUSED: …)` and exit 2: missing or malformed `--lands` or `--freeze`; missing or non-directory `--fleet-root`; an absent revision; `--freeze` not an ancestor of `--lands` on the lands first-parent chain (a stale tree); `lands` equal to the frozen base; an unreadable frozen `ledger.json` or `claims.json`; a frozen leg table that is not exactly the twelve implemented legs (LEGCOUNT); or a materialization failure. The denominator is the frozen leg table read at `--freeze`. `lands == freeze` is graded: REPAIR, ANNOTATE and R1EXEMPT red with FROZENCFG and LEDGER green, exit 1 — and a run that is green at `lands == freeze` is itself refused (the round-74 shape). `--main` defaults to `main`, is consumed by STAMP, and is the branch pin RECEIPTS hands to the nested round-74 run. | `python3 -B reports/round-75/accept-ca.py --selftest` — mktemp repositories asserting the clean `PASS legs=12/12`, the graded `lands == freeze` FAIL, the `lands == base` refusal, the stale-tree refusal, LEGCOUNT, and R1EXEMPT both ways (a rule-2 cell edit on a pre-existing row green, a teaches-cell edit red); receipt `reports/round-75/telemetry/selftest-ca.txt` is carried by the freeze commit (QUALITY 26(a)), and its sha256 and check count are re-derived from the installed bytes before landing (QUALITY 26(d)). | round introduced 75; base `f556d104…`; freeze-read `claims.json` and `ledger.json` (the eleven draft pairs L75-01..L75-11; `min-pairs` 10); the nine allowlisted observe executables git, grep, wc, sha256sum, ls, cat, head, tail, cut; the fleet pin `3a7401609325341eb3fe0efd42d0eec29d06be3c`; the round-74 lands `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3` with its freeze `00c408a0af2fa5ddf65af2224152ce258b26d896`, the `--main` value `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3` RECEIPTS pins, and the required line `ACCEPT-CA-74: PASS legs=11/11`; the R1EXEMPT fixture receipts `r1exempt-green.txt` and `r1exempt-red.txt`; the COMBINED receipt `measures-ca-head.txt`; `claims.json` and `ledger.json` at `<lands>` byte-identical to the freeze blobs; no counter sha256 and no check count is pinned here (QUALITY 26(d)) | read-only; clones at `--lands`, at base and at the round-74 lands for RECEIPTS, temp dirs removed on exit; no worktree byte is graded; selftest fixtures live in mktemp dirs | kotodama-shokunin |

## 3. Receipts the freeze must carry, and the ones that arrive after it

QUALITY 26(a) (binds from round 75) splits the set; the rows above must not be read as saying the
freeze holds all of them.

| receipt | round-75 path | when |
|---|---|---|
| both counters | `reports/round-75/accept-c.py`, `reports/round-75/accept-ca.py` | freeze commit |
| frozen config | `reports/round-75/claims.json`, `reports/round-75/ledger.json`, `.ufo/waves/round-75/assimilation/id-renumber-map.json` | freeze commit |
| do-nothing controls | `reports/round-75/telemetry/controls-c.txt`, `controls-ca.txt` | freeze commit |
| selftest receipts | `reports/round-75/telemetry/selftest-c.txt`, `selftest-ca.txt` | freeze commit |
| R1EXEMPT fixtures and proofs | freeze-committed fixture commits; `reports/round-75/telemetry/r1exempt-green.txt`, `r1exempt-red.txt` | freeze commit (fixtures) / with the run |
| junk landings | `reports/round-75/telemetry/junk-c.txt`, `junk-ca.txt` (+ `counters/junk-fixtures.py`) | **after** the freeze, on top of the landing |
| claim-C telemetry named by the legs | `reports/round-75/telemetry/gap-sweep.txt`, `.ufo/waves/round-75/assimilation/validate-receipt.txt` | with the landing |
| claim-Ca receipts named by the legs | `reports/round-75/telemetry/accept-ca-74-at-lands.txt`, `measures-ca-head.txt` | with the landing |

QUALITY 23 also wants each `--selftest` counter run **at the freeze commit** (receipts present,
landing absent) before the falsify wave, because a base-only control cannot see artifact-vs-leg shape
mismatches (round 73: GROUND, SCRATCHMIRROR and COLLCHECK read receipts in shapes the receipts did
not have). Nothing in this draft can be checked that way yet: no counter exists.

## 4. `## Error patterns` — candidates (proposal; adopt only what the round-75 lesson files)

Precedent, measured: the last five signature rows were added by round 69 (`e86ed3e`, "five error
signatures (D2)"); the following fourteen `SKILL.md` commits (rounds 70–74 and the round-69 attempt-2
repairs) contain no addition to this table — `975e8f2` *edited* the same five rows, and every later
hunk sits in the gate-row region. So adding rows here is a decision, not a routine carry-forward.

Append after the current last signature row (`SKILL.md:535`, `scope-limiter-missing`) if the lesson's
`## Mistakes` table names the class. Style is that table's own: dash token, then the reading with its
pointer. The first five are visible in lane bytes; the sixth is carrier-scoped to the fleet report and
should be added only if `ScribeLesson` files it.

```
| staged-id-as-lane-row | an entry or Gate cell cites a campaign/staged id (S864..S876, S885..S921) as if it were a lane registry row — lane ids exist only in `corpus/SOURCES.md`, so the citation is repointed to the registering row or dropped (claim C `REPOINTED` leg; round-74 old→new map by document, `corpus/lessons/round-74.md` Collision guard section) |
| rejection-inherited-from-register | a Gate reject reason states that the spanned quote is absent from the page while what is absent is the nearest register row's mispaired span — re-locate on the opened page before writing the reason (`corpus/lessons/round-74.md:37-38`; round-75 ledger pairs L75-05 and L75-06) |
| rule2-edit-read-as-removal | a changed `status`, `recheck` or `used-by` cell on a pre-existing registry row is not a removed line (SOURCES contract rule 2, restated at `corpus/SOURCES.md:9-12`) — a change in any other cell of that row is one (claim Ca `APPENDONLY` and `R1EXEMPT` legs; the round-74 combined-tree conflict, `corpus/lessons/round-74.md` Corrections item 1) |
| window-padded-to-floor | an evidence window claims a minimum length on a page whose whole extracted text is shorter — store the whole document with `visible-chars:` and make the EVIDENCE leg read the floor or drop it (round-74 R74-M6; `reports/round-74/evidence/S882.txt`, 2953 chars against a 4096 floor) |
| lands-eq-freeze-green | a counter that PASSes when `--lands` equals `--freeze` grades the do-nothing control green — that shape must FAIL its data legs, and only an external pin decides a junk freeze (`corpus/QUALITY.md` criterion 26(c); `corpus/lessons/round-74.md` Corrections item 3) |
| mutant-red-on-red-fixture | a mutant's redness is shown on a clean fixture that is itself red, or that reads a path the fixture never wrote — a re-pointed read path lands with its fixture in the same commit, and redness is shown against a fixture that is green first (`corpus/lessons/round-74.md:205-210`, routed item 4 / R73-M4; QUALITY 23 addendum owed by this round) |
| promised-hash-without-line | a filed report promises a closing line carrying the pushed lane hash and no closing line carries it — a delivery promise is not a delivery (round-75 ledger pair L75-08; `/home/vgpnk/Projects/shokunin/.ufo/reports/round-74/kotodama.md:20` carries `Lane pushed hash: see the closing line below`, the file's last line does not) |
```

## 5. Conflicts and gaps this draft hands to the freeze (read-only findings)

1. **The two counters do not exist**, so every verdict/refusal clause above is contract-derived. If
   the built counters refuse in a different set than the claims name (round 74 differed: `accept-ca.py`
   refused `lands == freeze` only when green, `accept-c.py` passed it), the **claims** are the
   authority and the rows must be rewritten to the built behaviour, not the reverse.
2. **`lands == freeze` is contested between the draft claim and the criterion, and its red set is
   unnamed.** Claim C's `do_nothing_control` says that shape FAILS "with the data legs red and
   FROZENCFG green"; QUALITY 26(c) records that round-74 `accept-c.py` graded and PASSED that shape and
   requires a round relying on it being red to call it a do-nothing control only. The row above states
   the claim's shape and refuses to enumerate the red legs: GROUND and CENSUS grade base bytes, so the
   freeze must name the asserted set, and the counter's selftest must assert exactly that set.
3. **`map.sha256` is `null`** in the draft claims, and the FROZENCFG leg compares
   `git show <freeze>:<map.path>` to that constant; a null must be filled in the freeze commit or the
   leg cannot pass (the round-74 placeholder failure, `# frozen map:`).
4. **`L75-08` is grounded but was re-located by this seat**: the promised sentence exists verbatim on
   `.ufo/reports/round-74/kotodama.md:20` (**Lane pushed hash: see the closing line below (git ls-remote
   origin refs/heads/main)**), and the file's final line is the Misroot-sweep sentence, so no closing
   line carries a hash. Claim Ca's `before` item (f) paraphrases it; the Error-patterns row cites the
   file line, not the claim.
5. **The count of ledger pairs is 11, not 12**, while claim Ca's `legs` fixes `min-pairs` at 10. The
   row says "eleven draft pairs, minimum ten" so an ExecLedger drop to ten does not falsify it.
6. **Allowlist size is nine**, not the ten the round-74 row printed; the round-74 row's "ten" is not
   this round's constant.
7. **The claims draft moved under this seat.** `reports/round-75/claims.json` was rewritten at 13:57
   (19075 → 19300 B); the row cells rest on the 13:57 bytes, and the freeze will replace them. A later
   edit to a `legs[]` entry or a `counter` string invalidates the cells above — re-read the row against
   the freeze blob, not against this draft.
8. Nothing in this seat was executed against the lane: no counter run, no clone, no fetch, no install,
   no scratch dir (none was needed, so none was created under
   `/fast/scratch/hyaku/kotodama-r75/ScribeSkillGates/`). No network access, hence no User-Agent record.
