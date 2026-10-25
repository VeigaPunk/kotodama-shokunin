# Seat ScribeSkillGates — round-74 SKILL.md §Gates and probes rows (draft)

Measured 2026-10-25 at lane base `f7104cbce186bc2e1522abf0cfd619cc834628bb`
(`git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse HEAD` == base; the worktree is
detached there and carries the inherited uncommitted round-73 w2 files, which were not read for
edits and not touched).

Artifact: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-74/drafts/skill-gates-rows.md`
(282 lines, 25,175 bytes). SKILL.md was not edited.

## Behavior delivered

The draft carries exactly what the registry needs, in the registry's own shape:

1. **Two insertions** — `accept-c-74` and `accept-ca-74` as 8-cell rows in the column shape of the
   last existing row (`accept-ca-73`), anchored after `SKILL.md:704` and before the blank line 705.
   Both entry commands carry `--freeze <40-hex>` (C: `--root . --lands --freeze
   [--fleet-root]`; Ca: `--root . --lands --freeze --fleet-root`). Both verdict cells use the
   required placeholder string `legs=<legs>/<legs>` for both the PASS and FAIL branches and state
   that the L1 fills the final number from the implemented leg count at freeze (the draft claims
   name twelve C legs `ENTRIES`..`FROZENCFG` and eleven Ca legs `LEDGER`..`STAMP`; the registry
   cell says so but does not assert a number).
2. **Stale-tree behaviour**, stated in both rows' write-scope cells and detailed in draft §6:
   the worktree is never graded; C and Ca read a clone materialized at `--lands`; config comes
   from `git show <freeze>:`; a stale or dirty worktree is disclosed only as the measured-revision
   header and cannot move a leg — Ca's `STAMP` excepted, because it binds measured == `--lands`.
   Exit 2 on missing `.git`, missing/non-40-hex/tree-absent `--lands` or `--freeze`, bad
   `--fleet-root`, or materialization failure; a well-formed `--freeze` that is not a strict
   ancestor fails the `FROZENCFG` leg (exit 1).
3. **Round introduced: 74**, stated for both rows together with the fact that neither
   `reports/round-74/accept-c.py` nor `reports/round-74/accept-ca.py` exists at base.
4. **Round-73 row corrections** — `accept-ca-73`'s self-test cell (adds the counter revision and
   sha, the `SELFTEST OK: 10 scenarios` receipt, and the expected `ERROR: base … is not a commit`
   stderr line that routed defect 3 names; the freeze-time r1 bytes printed **9**) and, marked
   optional, `accept-c-73`'s verdict cell (the `1/11` receipt vs the unsourced `10/11`).
5. **Insertion vs in-place map** with the Ca APPENDONLY authorization: rows are pure appends;
   each in-place cell edit needs a round-74 ledger REPAIR pair naming `SKILL.md:<line>`, because
   round 74's wording permits in-place edits only in files a ledger pair names (round-73's wording
   explicitly tolerated the registry surface). The surviving "9 scenarios" statements in
   `LOG.md:4297` and the fleet report are append-only and get an ANNOTATE pair instead; a pasteable
   allowlisted pair is in draft §4.3.

## Gates exercised (all read-only)

| gate/check | command | result |
|---|---|---|
| anchor + row shape | `grep -n 'Gates and probes' SKILL.md`; header at `648`; last row `704` | `619:## Gates and probes`, header line 648, rows 649-704, blank 705 |
| drafted cell count | `awk -F'\|' '/^\| accept-c-74 \|/ \|\| /^\| accept-ca-74 \|/'` on the draft | `accept-c-74 NF=10`, `accept-ca-74 NF=10` (8 cells each; no in-cell pipe) |
| placeholder discipline | `grep -c 'legs=<legs>/<legs>'`; `grep -n '<n>'` | 3 occurrences (both rows + the placeholder table); `<n>` appears only inside quoted *existing* row text, never in the new rows |
| registry/counter invariant | `git show base:SKILL.md \| grep -c '^\| accept-'`; `git ls-tree -r --name-only base reports \| grep -c 'accept-.*\.py$'` | `43` and `43` (equal); inserting the two rows requires both counters to land → expected `45 == 45` |
| inherited exit 2, C | `--root <empty mktemp> --lands <base>`; `--lands deadbeef`; `--lands 000…0` | exit 2 with the three recorded messages |
| inherited exit 2, Ca | `--lands deadbeef`; `--lands 000…0 --fleet-root <fleet>` | exit 2 with both recorded messages |
| CLI shapes | `--help` on both round-73 counters | captured verbatim in draft §7 |
| materializing run | `accept-c.py --root . --lands 2d1cd914…` | exit 2, `materialize 2d1cd9140d3a failed (git rc=0, tar rc=2)` — blocked by host `/tmp` pressure, not a counter verdict (see Findings) |

## Touched surfaces

- Written: `.ufo/waves/round-74/drafts/skill-gates-rows.md` (assigned draft path) and this report.
- Read (no writes): `SKILL.md` and its base bytes, `reports/round-74/claims.json`,
  `reports/round-73/{accept-c.py,accept-ca.py,counter-revisions.md,ledger.json}`,
  `reports/round-73/telemetry/*` (selftest r1/r2/r3, controls c/ca), `corpus/lessons/round-73.md`,
  `corpus/lessons/round-73-verifier-spotcheck.md`, `SCORECARD.md` corrections section, `LOG.md:4297`,
  the fleet `.ufo/reports/round-73/kotodama.md`, `.ufo/waves/round-73/w1/ExecCaCounter.md`,
  `.ufo/waves/round-73/w2/ExecSkillRows.md`, `.ufo/waves/round-74/w1/{spec.json,dispatch.json}`,
  and the round-73 w1 draft `skill-gates-rows.md` (structure precedent).
- Scratch: `/tmp/scg-74-*` mktemp dirs created by the exit-code probes were removed; a manual
  `git archive` extraction (167,229,440-byte archive) was removed with them. Nothing remains in
  `/tmp` from this seat.
- No installs (no package manager was invoked; pacman is paused host-wide and nothing was needed).
  No network fetch was made, so no User-Agent record applies.

## Findings (carried into the draft; also relevant to claim Ca)

1. **The Ca counter's docstring undercounts its legs.** `reports/round-73/accept-ca.py:45` says
   `LEGS (8, …)` and omits `TRACKED`; the code implements it (`:817-830`) and the receipt
   denominator is 9 (`controls-ca-r3.txt`, `ACCEPT-CA-73: FAIL legs=4/9`). SKILL.md's `/9` is
   correct; the docstring is the stale artefact.
2. **The selftest scenario count is revision-dependent**: r1 `f8ebb5d8…` and r2 `be1917…` print
   `9 scenarios`; r3 `222d4dd6…` prints `10 scenarios`. Base SKILL.md says 10 with no revision
   pin, and the `ERROR: base 8841ad3b… is not a commit` line is the expected stderr of the
   frozen-base-absent control (`accept-ca.py:1322-1325`), unlabelled today. This is routed defect
   3; the draft's C1 pins r3 + sha + receipt and labels the line.
3. **`STAMP` binds a receipt to the tree.** `leg_stamp` (`accept-ca.py:833-860`) requires
   measured == `--lands`, and measured resolves from `--main` (default `main`). A fresh clone of
   a lane at `f7104cbc…` cannot produce the round-74 `RECEIPTS` leg's PASS-at-lands receipt for
   `ACCEPT-CA-73` at `2d1cd914…` unless the clone's `main` is repointed (or `--main 2d1cd914…` is
   passed). The draft says this in the Ca row and §6 so the L1 plans for it.
4. **Round-73 C's config loader is the survivor round 74 closes**: `load_config`
   (`accept-c.py:432-448`) falls back to the lane worktree when the materialized tree has no
   claims; the new rows state the `git show <freeze>:` pin instead.
5. **Host `/tmp` pressure blocked one materializing run.** `df -h /tmp` read `12M` free (100 %
   used) at the time; the C counter's materialization failed with `tar rc=2` but its message
   prints **git's** stderr (`accept-c.py:194-198`), which was empty, so the cause is not in the
   receipt. The 167 MB archive size makes a full run need roughly twice that in `/tmp`. The draft
   records this as environment plus one diagnosability defect and does **not** claim the
   stale-tree legs were observed.
6. **Two cells in the new rows are placeholders by instruction** (`legs=<legs>/<legs>`, the
   self-test count) and one sentence is inherited rather than measured: the `FROZENCFG`
   non-ancestor mapping (leg FAIL, exit 1) is the frozen claim's wording; the builder brief says
   "refuse unless", so the built counter may use exit 2. Draft §8 F7 tells the L1 to reconcile
   that sentence at freeze. Nothing else in the new rows is asserted beyond base measurements.

## Out of scope / not done

- No SKILL.md edit, no claims.json/ledger.json edit, no counter written or installed, no fleet,
  sibling-lane, `.ufo/state`, watchdog, LOG, SCORECARD, lesson, QUALITY, SOURCES or shokuknow
  write. `/home/vgpnk/Projects/shokuknow` was not used for this deliverable.
- No round-74 counter command exists to run; every round-74 cell is a prospective description,
  labelled as such.
- No full round-73 C run at its lands revision (blocked by the `/tmp` condition); the exit-2
  branches the new rows mention were measured directly and the verdict data was read from the
  committed receipts.
- No external sources, so no quotes, no word counts and no Wayback probes apply.

## Post-wave update (final claims, literal fractions, LC-09/LC-10)

The final `reports/round-74/claims.json` (status FINAL) supersedes the pre-freeze numbers this report
was written against: the C claim has **13** legs (`ENTRIES` … `FROZENCFG`, `INDEX`) and Ca **11**
(`LEDGER` … `STAMP`). The draft
`.ufo/waves/round-74/drafts/skill-gates-rows.md` was rewritten in place; it now carries literal
fractions and no placeholders.

What the rewritten draft delivers:

1. **Two gate rows** in the 8-column shape of `accept-ca-73` (the last row at base `f7104cbc…`),
   appended after `SKILL.md:704`: `accept-c-74` with `ACCEPT-C-74: PASS legs=13/13` and
   `accept-ca-74` with `ACCEPT-CA-74: PASS legs=11/11`, both commands naming
   `reports/round-74/accept-{c,ca}.py`, both self-test cells naming
   `reports/round-74/telemetry/selftest-{c,ca}.txt`, and both write-scope cells stating the
   clone-at-`lands` + `git show <freeze>:` grading model.
2. **The LEGCOUNT refusal** at exit 2, with the literals this build prints: C
   `ACCEPT-C-74: FAIL legs=0/13 (refused: …)` (`len(LEGS)` = 13) and Ca
   `ACCEPT-CA-74: FAIL legs=0/11 (REFUSED: …)`. The C counter compares the frozen `legs[]` list to
   its own table and refuses on mismatch; its selftest asserts a twelve-leg list is refused.
3. **The two controls.** C: a no-data lands tree FAILs the data legs with `FROZENCFG` green (exit 1),
   and `lands == base` is a refusal that still prints FAIL (exit 2). Ca: `lands == freeze` is graded
   (REPAIR/ANNOTATE/RECEIPTS red, FROZENCFG/LEDGER green, exit 1) and `lands == base` is
   `FAIL legs=0/11 (REFUSED: --lands equals the frozen base …)`. The draft records that a literal
   `--freeze == --lands` is refused by the C counter (its `freeze-eq-lands` selftest scenario), so
   the claim's "lands == `<freeze>`" control is the no-data fixture, not that pair.
4. **The round-73 correction row**, appended as `kind = note` (deliberately not matched by the
   round-70 claim-O gate regex, so the row count stays `45 == 45` counter files). It records: the Ca
   selftest prints `SELFTEST OK: 10 scenarios` only at counter r3 (sha256 `222d4dd6…`,
   `reports/round-73/telemetry/selftest-r3.txt`) while the freeze bytes (`f8ebb5d8…`) print 9, and
   r3's `ERROR: base 8841ad3b… is not a commit` stderr line is the expected control output;
   `accept-c-73` reaches `PASS legs=11/11` at its lands only when the census script is named
   (`--fleet-root /home/vgpnk/Projects/shokunin` measured in `ExecReceiptRerun73.md` §2, or
   `--census-sh <path>` on the same code branch, unmeasured), the flagless form reading
   `FAIL legs=10/11`; `accept-ca-73` reaches `PASS legs=9/9` only with
   `--main 2d1cd9140d3a6c42296d71e4f29587582a4a88c0`, the documented form reading `FAIL legs=8/9`.
   These are appends, not in-place edits: `ledger-final.json` has 13 pairs and only `LC-09`/`LC-10`
   at `SKILL.md:594`, and Ca's APPENDONLY leg permits non-append changes only on a REPAIR pair's
   `stated_at` line.
5. **The exact LC-09/LC-10 edit**, both pairs on the same base line:
   `- \`corpus/knowledge/civilizations/\` — 94 entries: 92 earlier-civilization` →
   `… — 95 entries: 93 earlier-civilization`, line 595 untouched. Measured truths:
   `95 files changed` (all `civilizations/*.md`) and `93 files changed` excluding
   `*primary-sources.md`; the single occurrence of the old token is line 594; the round-74 entries
   land under `culture-material/`, so the repaired numbers stay true at lands.

Measured this update (`/tmp/scg74` scratch, removed at close):

| command | exit | output |
|---|---|---|
| `.ufo/waves/round-74/counters/accept-ca.py --selftest` (sha `76d00b88…`) | 0 | `SELFTEST OK: 138 checks across 37 scenarios reported-fail=0: do-nothing, clean, lands-eq-base, legcount, …` |
| `.ufo/waves/round-74/counters/accept-c.py --selftest` (self-stamp sha `b038f345…`, file ending `b5bfb98b…`) | 1 | `SELFTEST: 68/69 scenarios`; sole failure `lands==freeze: expected graded FAIL exit 1, got 0` — the counter printed `ACCEPT-C-74: PASS legs=13/13` on a no-data tree |
| `ast.parse` on `accept-ca.py` (sha `2ddebefc…`) | 0 | parses |
| `git show f7104cbc…:SKILL.md \| grep -n '94 entries\|92 earlier-civilization'` | 0 | single hit, line 594 |
| the two `git diff --shortstat` count commands | 0 | `95` and `93` files changed |

Build-state items handed to the L1 (detailed in draft §5): `map.sha256` in the frozen claims still
reads `FILLED-AT-FREEZE` and FROZENCFG compares that constant, so it must be filled in the freeze
commit; the C counter's own selftest is **red** at the build this seat ran — `SELFTEST: 68/69`,
`lands==freeze: expected graded FAIL exit 1, got 0`, i.e. the do-nothing shape currently PASSes
`legs=13/13`, so the control reads green when it must read red (the C file was being written
throughout: `0b63cdc6…` → `b5bfb98b…`, selftest self-stamp `b038f345…`); the Ca counter changed after
the measured run (`76d00b88…` → `2ddebefc…`), so its selftest should be re-run at freeze. Also noted:
the current C `main` no longer refuses a non-strict `--freeze` (only the `--freeze` help text still
says "strict ancestor"), so `lands == freeze` is graded, not refused, and its `--selftest` asserts
that graded shape.

Written this update: the draft (rewritten) and this section. SKILL.md, claims, ledger, counters,
receipts, fleet and sibling lanes untouched; no installs; no network fetch, so no User-Agent record.
