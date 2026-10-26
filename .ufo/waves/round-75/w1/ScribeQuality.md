# ScribeQuality — QUALITY 23 addendum, QUALITY 27, and the round-75 correction rows

Seat: ScribeQuality (leaf scribe, wave 1). Date: 2026-10-27. Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
(hyaku run 10, round 75). Lane base `f556d1049fe651d3d63975600b13acd9fb686f15`. Fleet root read only, never written.
No delegation, no background jobs, no subagents; no tool installed or upgraded (python3, git, coreutils only; `pacman` not
run); no live fetch made, so no User-Agent is bound to any response in this report.

## 1. Deliverables

| path | what it is |
|---|---|
| `.ufo/waves/round-75/drafts/quality-additions.md` | (1) criterion 23 addendum as verbatim insertion text + measured grounding; (2) criterion 27 as verbatim append text + measured grounding; placement and append-only notes |
| `.ufo/waves/round-75/drafts/scorecard-corrections.md` | the `## Corrections — round 75` section text to append (lead + 5 ANNOTATE rows + `Notes.` paragraph), the inherited row contract with counter line citations, per-row measured verification, and the three blocking `ledger.json` fixes as an old→new table |

Both files are drafts. `reports/round-75/claims.json` and `reports/round-75/ledger.json` were read and **not** edited;
`reports/round-75/telemetry/` is still empty (no receipt was fabricated).

## 2. Claim-antagonism record — the five ANNOTATE rows against the drafted ledger

The round-74 counter's contract (inherited verbatim by the round-75 draft, `reports/round-74/accept-ca.py`):
`ANNOTATE` (`:1290-1345`) takes the row whose **first cell** is the pair id (`:312`), requires
`token_in(row, stated_token)` and `token_in(row, observed_token)` (`:269`, boundary-matched), then **re-runs the pair's
own `rederive`** (`shlex.split` → argv) with cwd in the lane clone at `<lands>` and requires that run to return the
observed token; `NOSTUB` (`:1470-1512`) requires `norm(rederive)` to appear verbatim inside the row, refuses a shell
metacharacter (`SHELL_META`, `:175`) and any `git -C`/`-c`/`--git-dir` (`GIT_GLOBAL_OPTS`, `:603-604`); a **numeric**
`expected_after` must name the frozen **base** revision in `observe_cmd` (`:1316`); `LEDGER` requires the pair's `parse`
to compile **with a capture group** (`:1043`).

### 2.1 Per pair

| pair | stated token (from `stated_parse`) | observed token (from `parse`) | drafted `rederive` runnable? | result |
|---|---|---|---|---|
| L75-05 | `was absent from the page it was bound to` | `1` | yes, verbatim | row as drafted passes both legs |
| L75-06 | `was the Sowers-Wills clause, absent from this page` | `1` | yes, verbatim | row as drafted passes both legs |
| L75-08 | `see the closing line below` | `1` | **no** — `git -C <abs>` refused | blocked on the ledger (2.3) |
| L75-09 | `FAIL` | `FAI` | **no** — pipeline refused, and it prints `son` | blocked on the ledger (2.2) |
| L75-10 | `43` | drafted: `.md` (no capture group) | **no** — pipeline refused | blocked on the ledger (2.4) |

### 2.2 L75-09 — the drafted `rederive` cannot return the observed token

Drafted: `git show f556d10…:reports/round-73/telemetry/selftest-r3.txt | tail -c 4`.
Measured at base: that pipeline prints `son` — the file's last four bytes (`…scenarios\n`), not `FAI`. As an argv it is
refused outright: `SHELL_META` contains `|`, so `observe_problem` returns `shell construct '|' in argv element '|'`.
Replacement measured in the fresh clone: `git grep -h -o -E 'min-pairs gate [A-Z]+' f556d10… -- reports/round-73/telemetry/selftest-r3.txt`
→ `min-pairs gate FAI` (exit 0), and `token_in(out, "FAI")` holds (the neighbouring `FAIL` on the same physical line does
not match, because `FAI` there is followed by `L`). The pair's own `observe_cmd` (`git show <base>:<path>`) and its
`parse` (`min-pairs gate (\S+)$`) are fine: with `re.M` the first line ending yields `FAI`.

### 2.3 L75-08 — fleet-anchored pair, refused git option, and a base-pin conflict

Drafted: `git -C /home/vgpnk/Projects/shokunin grep -c 'see the closing line below' 3a74016… -- .ufo/reports/round-74/kotodama.md`.
`git -C` is in `GIT_GLOBAL_OPTS` → refused (`:642-643`). Even without `-C`, the 40-hex is a **dead pin in the lane clone**
(measured: `git cat-file -e 3a74016…` exits 1 in `/fast/scratch/…/lane-clone`), because it is the *fleet* commit.
Run in the fleet repo it prints `3a74016…:.ufo/reports/round-74/kotodama.md:1` (exit 0). Fix for the freeze: drop `-C`,
use the round-74 fleet grammar `stated_fleet` (`:1073-1110`: `path`/`pin`/`line`/`sha256` resolved with
`git -C <fleet> show <pin>:<path>`), and run that pair's observation against `--fleet-root` — measured values for the
object are in the draft. One more catch the L1 must decide: `ANNOTATE`'s count-pair rule (`:1316`) demands the frozen
**base** in `observe_cmd` when `expected_after` is numeric, and this pair's observable rev is the fleet pin
`3a74016…`; either the round-75 counter accepts `ledger.fleet_pin` as the pin for a `stated_fleet` pair, or
`expected_after` becomes non-numeric. The row carries `1` under both choices.

### 2.4 L75-10 — the observation itself is broken, not only its re-run

Measured facts: (a) the drafted `parse` `\.md$` has **no capture group** → `LEDGER` refuses the pair (`:1043`);
(b) `ls .ufo/waves/round-74/w2` cannot return a count, so `expected_after: "44"` is unobservable; (c) the drafted
`rederive` is a pipeline (refused). Replacement that satisfies all three and was measured in the clone:
`git diff --shortstat 4b825dc… f556d10… -- ':(glob).ufo/waves/round-74/w2/*.md'` → ` 44 files changed, 13810 insertions(+)`.
The `:(glob)` magic matters: the same pathspec without it also matches `w2/drafts/*.md` and reports **47**
(`.ufo/waves/round-74/w2/drafts/{log-entry,report-draft,scorecard-axes}.md` are the three extras). The guard accepts the
replacement: `_pathspec_ok` passes any `:`-prefixed operand (`:629-634`) and `_git_rev_problem` exempts the empty tree
(`:608-612`). `git ls-tree` over the directory itself lists 44 `.md` files at base and in the worktree.

### 2.5 Clean pairs and the absence-pair rule

L75-05 and L75-06 need no change: both drafted `rederive` strings pass the allowlist and return the observed token
(measured in the clone, §3). Neither is an absence-observation pair (both read 1 at base; the pair is red because the
stated token differs, not because a count is zero), and both observe_cmds pin the base revision.

## 3. Measured outputs (verbatim; the clone is the ANNOTATE execution context)

```
$ cd /fast/scratch/hyaku/kotodama-r75/ScribeQuality/lane-clone   # git clone --shared of the lane
$ git rev-parse --show-toplevel
/fast/scratch/hyaku/kotodama-r75/ScribeQuality/lane-clone
$ git cat-file -e 4b825dc642cb6eb9a060e54bf8d69288fbee4904 && echo empty-tree-exists
empty-tree-exists
$ git diff --shortstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 f556d1049fe651d3d63975600b13acd9fb686f15 -- ':(glob).ufo/waves/round-74/w2/*.md'
 44 files changed, 13810 insertions(+)
$ git diff --shortstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 f556d1049fe651d3d63975600b13acd9fb686f15 -- '.ufo/waves/round-74/w2/*.md'
 47 files changed, 14102 insertions(+)
$ git grep -h -o -E 'min-pairs gate [A-Z]+' f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-73/telemetry/selftest-r3.txt
min-pairs gate FAI
$ git grep -c '非凡特性来自最初造物主' f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-74/evidence/S883.txt
f556d1049fe651d3d63975600b13acd9fb686f15:reports/round-74/evidence/S883.txt:1
$ git grep -c '这个我肯定考虑过' f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-74/evidence/S884.txt
f556d1049fe651d3d63975600b13acd9fb686f15:reports/round-74/evidence/S884.txt:1
$ git cat-file -e 3a7401609325341eb3fe0efd42d0eec29d06be3c; echo lane-has-fleet-rev-exit=$?
lane-has-fleet-rev-exit=1
$ git show f556d10:reports/round-73/telemetry/selftest-r3.txt | tail -c 4
son
```

In the fleet root (read-only): `git cat-file -t 3a7401609325341eb3fe0efd42d0eec29d06be3c` → `commit`;
`git show 3a74016….ufo/reports/round-74/kotodama.md | wc -l` → `45`; line 20 =
`LOG.md round-74 entry and SCORECARD … Lane pushed hash: see the closing line below (…).`; its tail is the
stale-lane/misroot lines (no closing line carries a pushed hash; its only 40-hex values are the lane base `f7104cb`,
freeze `00c408a0`, and lands `5e4796c0`/`c4bf61a8`); sha256 of the pinned blob
`354273bc972d8b86a012a8aac024618d5defa73e72ea1eae5a960fdf64f84107`.

Lane, read-only:

```
$ git grep -c 'SELFTEST' f556d10 -- reports/round-72/telemetry   # no output
exit=1
$ git ls-tree --name-only f556d10 reports/round-72/telemetry/
…/baseline.txt …/census-start.txt …/census-end.txt …/controls-c.txt …/controls-ca.txt …/gap-sweep.txt …/measures-c.txt …/measures-ca.txt
$ git show --stat --oneline 5897ddf
5897ddf round-72: Gate reject verdict column + counter hardening (GROUND receipt path, APPENDONLY numstat crosscheck …)
 corpus/lessons/round-72.md    |  8 ++++----
 reports/round-72/accept-c.py  |  5 +++--
 reports/round-72/accept-ca.py | 11 ++++++++---
$ git show 5897ddf -- reports/round-72/accept-c.py | grep '^[-+][^-+]'
+GROUND_RECEIPT = "reports/round-72/telemetry/gap-sweep.txt"
-        receipt = show(root, lands, RECEIPT)
+        receipt = show(root, lands, GROUND_RECEIPT)
-        bad.append("receipt missing: %s" % RECEIPT)
+        bad.append("receipt missing: %s" % GROUND_RECEIPT)
```

The criterion-23 addendum's limb-(i) detector, over five counters (bash one-liner in the draft file):

| counter | limb (i) output |
|---|---|
| `reports/round-72/accept-c.py` | `GROUND_RECEIPT` |
| `reports/round-73/accept-c.py` | *(empty)* — writes `GROUND_RECEIPT` from `GROUND_RECEIPT_TEXT` at `:1593`/`:1596` |
| `reports/round-73/accept-ca.py` | *(empty)* |
| `reports/round-74/accept-c.py` | *(empty)* |
| `reports/round-74/accept-ca.py` | *(empty)* |

Limb (ii) evidence: `reports/round-74/telemetry/selftest-ca.txt:2` = `selftest: clean -> exit=0 LEDGER=PASS … STAMP=PASS`;
`selftest-c.txt` = `SELFTEST: 69/69 scenarios`; `reports/round-74/accept-c.py:2857-2875` asserts the clean fixture
(`ACCEPT-C-74: PASS legs=13/13`, stamped receipt) as a scenario and returns `0 if passed == total`, so a red clean
fixture fails the selftest. The red-before is `.ufo/waves/round-74/w1/ExecSelftest72.md:37-38`:
`SELFTEST: 10/11` / `--- clean fixture: expected PASS 10/10, got exit=1`.

## 4. Grounding read for criterion 27 (nothing re-run to decorate it)

`corpus/lessons/round-74.md:37` and `:38` are the two reject rows as filed; `## Quarantine` bridging at `:143-144`;
R74-M5 at `:172` ("The fabrication class is the register pair as filed, not the pages and not the staged row text");
routed item 4 at `:186-198`; routed item 5 at `:211`. Wave-2 measured findings:
`.ufo/waves/round-74/w2/RevLessonGate.md:42-83` (F1: `非凡特性来自最初造物主` 1 hit on the 2025 page, 0 on the 2022 page;
`这个我肯定考虑过` 0 on 2025, 1 on 2022; the staged cell anchors are on their own pages; the Sowers-Wills clause belongs to
lane S880) and `.ufo/waves/round-74/w2/ScoutRejectProbes.md:63-72` (F2: the Sowers-Wills clause is staged **S901**'s
anchor; `census-adjudication.json` S758/S759 carry row N's `url` with row N+1's `quote`). The routing record I could
cite by bytes is `reports/round-75/claims.json` claim Ca `before` and `reports/round-75/ledger.json` L75-05/06 `why`
(the closure report itself is not in the lane tree: `.ufo/waves/round-74/` has no closure file, and the fleet's
`.ufo/reports/round-74/` holds only the four lane reports). The two `git grep -c` counts in §3 are the criterion's own
red-before demonstration.

## 5. Gates I ran / did not run

- Ran: every command quoted in §3, plus the five limb-(i) probes, plus anchor checks for each pair's `stated_at`
  (`round-74.md:37`, `:38`; `selftest-r3.txt:6`; `LOG.md:4318` — all carry their `stated_text`), plus
  `git grep -c 're-pointed read path' <base> -- corpus/QUALITY.md` → no output, exit 1 (L75-07's before-value, unchanged
  by me).
- Did **not** run: the round-75 counters (they do not exist yet — `reports/round-75/` holds only `claims.json`,
  `ledger.json`, an empty `telemetry/`), the round-74/73 counters, any selftest, any live fetch, any campaign tool, and
  nothing against `shokuknow`. No build/lint/test of any kind applies to a markdown deliverable; the main agent owns
  verification of these drafts.

## 6. Touched surfaces

- Written (3 files, all new): `.ufo/waves/round-75/drafts/quality-additions.md`,
  `.ufo/waves/round-75/drafts/scorecard-corrections.md`, `.ufo/waves/round-75/w1/ScribeQuality.md`.
- Not written: the fleet repo (no byte under `/home/vgpnk/Projects/shokunin/**`), `reports/round-75/claims.json`,
  `reports/round-75/ledger.json`, `reports/round-75/telemetry/**`, `corpus/QUALITY.md`, `SCORECARD.md`, `LOG.md`,
  `SKILL.md`, `corpus/SOURCES.md`, `corpus/lessons/**`, `.ufo/state`, `.ufo/watchdog.log`, any sibling lane, `shokuknow`.
- Lane git state untouched: read-only `git show`/`grep`/`ls-tree`/`cat-file`/`diff`/`status` inside the lane and the
  fleet; the only clone is my own scratch (`git clone --shared` there writes nothing into the lane).
- Scratch `/fast/scratch/hyaku/kotodama-r75/ScribeQuality/` (the `lane-clone`) is deleted before this seat ends; every
  measured output it produced is transcribed in §3, so no receipt is lost with it.

## 7. Findings handed to the L1 (all measured, none repaired by this seat)

1. **L75-08, L75-09, L75-10 are unlandable as drafted** — each fails `ANNOTATE` (and L75-10 also fails `LEDGER`) for the
   reasons in §2.2–§2.4. Exact replacement strings and field changes are in
   `drafts/scorecard-corrections.md` §"Blocking ledger fixes". This is a pre-freeze ledger edit only the L1/ExecLedger may
   make; if the text is frozen as drafted, the honest consequence is that three of the five ANNOTATE pairs cannot close
   and claim Ca fails as declared — not that the rows are rewritable to a friendlier token.
2. **L75-08 needs a counter capability, not just a string fix**: a `stated_fleet` pair's observation must run against
   `--fleet-root`, and the numeric-`expected_after` base-pin rule (`:1316`) must accept `ledger.fleet_pin` for such a pair
   (§2.3). Flagged to ExecCaCounter's lane, not decided here.
3. **L75-10's before-value is right, its observation is wrong**: 44 `.md` files at base (`git ls-tree`), but the drafted
   `ls` cannot return a count and the drafted `parse` has no capture group; the un-globbed pathspec over the same
   directory reports 47 because `w2/drafts/*.md` matches (§2.4).
4. **The criterion-23 addendum replaces criterion 23's first limb with a cause** — criterion 23 as filed names R73-M4 by
   its symptom (`SELFTEST: 10/11`, capture-by-none); the addendum names the mechanism (`5897ddf` re-pointed the read and
   left `build_fixture` writing the old path) and the second condition (mutant redness against a green fixture). The
   round-72 telemetry holds no selftest receipt at all (8 receipts, `git grep -c 'SELFTEST'` exits 1), which is the
   capture-by-none the addendum's limb (ii) makes visible.
5. **Criterion 27 is anchored to a row class the corpus now has on record**: the two round-74 reject rows are the first
   red-before instance, and the class (register URL↔quote off-by-one, R74-M5) stays open — the criterion binds the
   *reason cell*, not the register's checker, so routed item 5's adjacency guard is still owed.

## 8. Limits, stated

- `token_in` is boundary-matched, so a row must carry the ledger's own token strings; my rows use the ledger's
  `expected_after` values as new tokens and its `stated_parse` captures as old tokens. If the L1 changes any
  `stated_parse`/`parse`, the corresponding cell must change with it.
- The limb-(i) detector is a name-shape grep: an inline path or an aliased constant escapes it, and it cannot prove a leg
  and its fixture name the *same* path — only that the constant is referenced inside `build_fixture` (§draft, Limits).
- The criterion-27 check is a per-row re-open; it cannot tell whose clause a quoted span means, and a reason that names
  no span falls to criterion 12.
- I did not attempt to locate a round-74 closure report inside the lane tree beyond the searches recorded in §4; the
  routing record I cite is the round-75 claim/ledger text plus the wave-2 measured reports.
