# ScribeScorecardFinal — round 75, wave 2 (claim Ca scorecard staging)

Seat ScribeScorecardFinal (leaf; no delegation, no `task` spawn, no background job). Lane
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `f556d1049fe651d3d63975600b13acd9fb686f15`
(`git -C . rev-parse HEAD` → that hash). This seat wrote no tracked lane file: the only modified entries in
`git status` (`SHONEN.md`, `SKILL.md`, `reports/round-28/readme/sweep.py`) are other seats' uncommitted
working-tree edits, which no measurement here reads or grades. Fleet root read-only.
Scratch `/fast/scratch/hyaku/kotodama-r75/ScribeScorecardFinal/` (a `--shared` clone of the lane, detached at
base), removed before yield; every measurement below was taken inside it. The whole scratch tree vanished once
mid-seat (an external sweep, not this seat's doing) after the leg simulations were recorded; it was recreated
with the same command and the `BASEMISMATCH` measurement re-run against the fresh clone, with the same result.
Python 3.14.8, git 2.56.0. No tool installed, upgraded or removed (nothing needed it).

Inputs, hashed at the time of measurement:

| input | sha256 |
|---|---|
| `.ufo/waves/round-75/counters/accept-ca.py` (candidate counter) | `d167093537864fc9572fedec2ee8cd0f8e1f86c7c6daa380e81bfde893975bdb` |
| `reports/round-75/ledger.json` | `a820f2117409a4e4a5c9f0b2b24511c85fd6e9d54d79b0159b3140e3518cc926` |
| `reports/round-75/claims.json` | `d753e5f12139e02623660b1de0f0dc7ce19ab81014008f7a86955c8474221abf` |

## Files written (only these; both under `w2/stage/`)

| path | bytes | sha256 |
|---|---|---|
| `.ufo/waves/round-75/w2/stage/SCORECARD.md.append` | 2699 | `f5aed3a0cab6cc325e42d091924e8f42b86651422a462208ec1dddb5be3e9985` |
| `.ufo/waves/round-75/w2/stage/SCORECARD.round75-claims.append` | 1765 | `7d04ca4bd2d95bcc99514ee3018cf869d7d1d2d27644ba78a436a4e76a6f49fb` |

Both files are append fragments: `cat SCORECARD.md.append >> SCORECARD.md` at lands. The rows were generated
mechanically from `ledger.json` (the CJK patterns, the em dash and the two backticks are byte-copied, not
transcribed), then verified with the counter's own functions and legs.

## Item 1 — `## Corrections — round 75` rows: the ANNOTATE set, verified against the file

`reports/round-75/ledger.json` holds **10** pairs: `REPAIR` = L75-01, -02, -03, -05, -06, -07; `ANNOTATE` =
**L75-04, L75-08, L75-09, L75-10**. The brief's list is right; the wave-1 draft
`.ufo/waves/round-75/drafts/scorecard-corrections.md` is **stale** and must not be landed: it states "The ledger
holds 11 pairs; the five `ANNOTATE` pairs are L75-05, L75-06, L75-08, L75-09, L75-10" and its L75-05/L75-06 rows
carry old token `was absent from the page it was bound to` / `was the Sowers-Wills clause, absent from this page`
and new token `1`. In the file that is now filed, L75-05/06/07 are REPAIR pairs with different observations
(713/58/37), and the S883/S884 presence pairs are L75-08/09. Landing the draft's five rows would file two false
records (wrong ids for wrong pairs) and leave L75-04 unannotated.

One row per ANNOTATE pair, cells = the counter's tokens (not paraphrases):

| pair | `stated_parse` capture (base) | observed token at base | row's re-derivation command |
|---|---|---|---|
| L75-04 | `249` | `247` | `git grep -c -E '^- `[^`]+\.md` —' f556d104… -- corpus/README.md` |
| L75-08 | `absent` | `present` | `git grep -c '非凡特性来自最初造物主' f556d104… -- reports/round-74/evidence/S883.txt` |
| L75-09 | `absent` | `present` | `git grep -c '这个我肯定考虑过' f556d104… -- reports/round-74/evidence/S884.txt` |
| L75-10 | `43` | `44` | `git diff --shortstat 4b825dc6… f556d104… -- ':(glob).ufo/waves/round-74/w2/*.md'` |

`L75-10`'s stated token is **`43`**, not the phrase `43 of 44`: `stated_parse` is
`(\d+) of 44 report files present at filing` and `stated_token` returns group 1. The row's old-token cell
therefore carries `43`; the `LOG.md:4318` phrase appears in the section's notes so the reader still sees it (and
`token_in` would also accept `43 of 44`). `L75-04`'s old/new pair is the footer-vs-index mismatch: `corpus/README.md:813`
reads `Total knowledge entries: 249.` while the index rows above it number 247 at the pinned base.

Every stated_text was confirmed on its own stated_at line in the base tree (LEDGER's line check):

```
corpus/README.md:813            Total knowledge entries: 249.
corpus/lessons/round-74.md:37   | staged S899's quoted span was absent from the page it was bound to … | refused |
corpus/lessons/round-74.md:38   | staged S900's quoted span was the Sowers-Wills clause, absent from this page … | refused |
LOG.md:4318                     … (44 seats, reports in `.ufo/waves/round-74/w2/`; 43 of 44 report files present at filing) …
```

### Every re-derivation command, run at the pinned base in the scratch clone

Run as the counter runs it (`shlex.split` → argv, cwd = clone), i.e. **never through a shell** — L75-04's
pattern carries two backticks, which a shell would treat as command substitution, so quoting it here as a shell
line would be a different (and unsafe) operation. Raw stdout, normalised:

```
L75-04  f556d104…:corpus/README.md:247                                     parse '247'
L75-08  f556d104…:reports/round-74/evidence/S883.txt:1                     count-presence 'present'
L75-09  f556d104…:reports/round-74/evidence/S884.txt:1                     count-presence 'present'
L75-10   44 files changed, 13810 insertions(+)                             parse '44'
```

The three that execute replay to exactly the observed token (`ANNOTATE`'s equality check:
`norm(replay) == norm(obs)` → `True`). L75-04 does not execute — see the blocking finding.

### Row grammar, checked with the counter's own primitives

`SCORECARD.md.append` appended to the base `SCORECARD.md` gives `correction_rows(..., 75)` = 25 rows, with
**exactly one** row leading each ANNOTATE id (`row_starts_with_id`). No prose line leads with a pair id (the
notes lead with a path, a bullet lead, or `The`/`Four`), so no second candidate row exists for any pair. `NOSTUB`
shape per row: `norm(rederive)` present verbatim, old token and new token boundary-matched — `True` for all four.
`APPENDONLY`: the fixture commit (base + this append, in the scratch clone) gives
`git diff --numstat base..append-fixture -- SCORECARD.md` → `33  0  SCORECARD.md` (1466 → 1499 lines): 33
insertions, **0 deletions**, and `SCORECARD.md`'s frozen scope is `whole`. `SEPARABLE`: scanning every
corrections row for the frozen lane ids `S885…S893` and the family literal `narrative-structure-frameworks` →
no hits (the only S-ids in the section are `S883`/`S884` in two re-derivation commands, outside the lane row set).

## BLOCKING FINDING (pre-freeze, not mine to fix) — four ledger observations are refused by the counter's guard

The candidate counter's `observe_problem` refuses any argv element containing a shell metacharacter
(`SHELL_META = ("|", "&", ";", "<", ">", "`", "$(", "\n", "\r")`; the check runs before the clone half). Four
filed pairs carry one:

```
L75-04  shell construct '`' in argv element '^- `[^`]+\.md` —'
L75-05  shell construct '|' in argv element '^\|[[:space:]]*S[0-9]{3,}.*\|[[:space:]]*mined[[:space:]]*\|'
L75-06  shell construct '|' in argv element '^\|[[:space:]]*S[0-9]{3,}.*\|[[:space:]]*queued[[:space:]]*\|'
L75-07  shell construct '|' in argv element '^\|[[:space:]]*S[0-9]{3,}.*\|[[:space:]]*rejected[[:space:]]*\|'
```

The frozen claim text is on the counter's side ("argv observe_cmd whose executable is in a read-only allowlist …
that EXCLUDES interpreters and echo/printf/true-style constant printers and shell metacharacters"), so the fix
cannot be in `claims.json` (final for this wave) and must be in `ledger.json` before freeze. With the ledger as
it stands, the legs print (measured, with my staged rows and lands = base):

```
LEG FAIL LEDGER       pairs=10 min=10 source=freeze problems=4 [the four above]
LEG FAIL BASEMISMATCH red=6 min=10 ids=['L75-01','L75-02','L75-03','L75-08','L75-09','L75-10']
                      unobservable=["L75-04:…shell construct '`'…", "L75-05:…'|'…", "L75-06:…'|'…", "L75-07:…'|'…"]
LEG FAIL NOSTUB       stubs=['L75-04:new-token', "L75-04:rederive shell construct '`' …"]
LEG FAIL ANNOTATE     rows=25 annotate-pairs=4 unannotated=1 ["L75-04(unobservable:invalid-observe_cmd:shell construct '`' …)"]
```

Note that only **one** ANNOTATE pair is unannotated (L75-04); L75-08/09/10 pass both `ANNOTATE` and `NOSTUB`
against the candidate counter as staged.

### The re-cut, measured (same tokens, no metacharacter)

| pair | replacement pattern | measured at base | `observe_problem` |
|---|---|---|---|
| L75-04 | `^- .*[.]md. —` | `corpus/README.md:247` | `None` |
| L75-05 | `^. S[0-9]{3,}.* mined . 20` | `corpus/SOURCES.md:713` | `None` |
| L75-06 | `^. S[0-9]{3,}.* queued . 20` | `corpus/SOURCES.md:58` | `None` |
| L75-07 | `^. S[0-9]{3,}.* rejected . 20` | `corpus/SOURCES.md:37` | `None` |

(`.` matches the cell pipe/backtick, and `. 20` binds the status cell to the following date cell; the loose form
without the date anchor over-counts `mined` to 714.) The sibling seat `w2/ExecLedgerRerun.md` proposes
`^- .{1}[^ ].*\.md. —` and `S[0-9]{3,}.*[[:space:]]<status>[[:space:]]. [0-9]{4}-`; I measured those too and they
return the same `247/713/58/37`, so either spelling is safe — the L1 should pick one and keep it consistent with
whatever the REPAIR seats assume.

End-to-end proof that the re-cut is sufficient (pairs re-cut in memory only, plus cell 4 of the L75-04 row
swapped to the re-cut string, ledger.json on disk untouched):

```
LEG PASS LEDGER        pairs=10 min=10 source=freeze
LEG PASS BASEMISMATCH  red=10 min=10 ids=['L75-01' … 'L75-10']
LEG PASS NOSTUB        stubs=[]
LEG PASS ANNOTATE      rows=25 annotate-pairs=4 unannotated=0 []
```

**Action for the L1 at freeze:** (1) re-cut the four `observe_cmd`/`rederive` strings as above; (2) replace cell
four of the L75-04 row in `SCORECARD.md.append` with the re-cut `rederive` string (one line; the token cells
`249`/`247` do not change). Without (1) claim Ca cannot pass `LEDGER`, `BASEMISMATCH`, `NOSTUB` or `ANNOTATE`
however the scorecard is written.

## Item 2 — per-claim SCORECARD rows (`SCORECARD.round75-claims.append`)

Two rows only, in the round-74 claim-row shape (`axis | verdict | before → after / observation | re-run command |
measured evidence`), under `## Axes — round 75 (2026-10-27, hyaku run 10, kotodama), author-side verdicts, pending
non-author closure`:

- **coverage (claim C)** — base quantities re-measured by me at `f556d104`: `git ls-tree … | grep -ci 'narrative'`
  = **0**; `… | grep -c '\.md$'` = **249**; `git show …:corpus/SOURCES.md | grep -cE '^ {0,3}\|…S[0-9]{3,}…\|'` = **808**.
  After-side (`252` files, `817` rows, `S885-S893`) is claim C's declared after-state, not something I measured.
- **calibration (claim Ca)** — 10 pairs (6 REPAIR, 4 ANNOTATE); the row states today's measured structure
  (`6 measured red, 4 refused by the guard`) alongside the intended after-state, so the row cannot be read as a
  PASS it did not earn. `LANDS: <filled by the L1>` appears 4 times (two per row, `--lands` and `--freeze`).
  The file contains no `L75-` id, so appending it before or after the Corrections section cannot make the
  `correction_rows`/`SEPARABLE` read set pick up an axes row.

I did **not** write the round-74 "depth / quality / operability / freshness / adjacency | unchanged" row: no
counter measures those axes, and this seat has no mandate to assert them.

## Conflicts to carry to the canonical judge (verbatim, unresolved by me)

1. `w2/ExecLedgerRerun.md` F1 says L75-08/L75-09 are unobservable because `"parse": "count-presence"` "compiles
   (as a literal) with 0 capture groups … the literal `count-presence` never occurs → parse-miss". That holds for
   the **inherited round-74** counter (its Receipt R2 says it imported `reports/round-74/accept-ca.py`), not for
   the round-75 candidate: `accept-ca.py:1130-1137` special-cases `count-presence` (returns `present`/`absent`)
   and `leg_ledger:1286` exempts it from the capture-group check. Measured against the candidate: both pairs give
   `('present', True, 'exit=0')` and `ANNOTATE`/`NOSTUB` PASS with the `present` cells staged above. **If the freeze
   instead inherits the r74 grammar, both rows must say `1`, not `present`.** The row text depends on which
   counter is frozen; the token cannot be guessed.
2. `w2/ExecLedgerRerun.md` F4 (`statement_after.parse` lacks `re.M`) reproduces against the candidate too:
   `statement_after` compiles with `re.compile(parse)` and no flags (`accept-ca.py:1214-1218`), so
   `^## linguistics/ \((\d+)\)` / `^## culture-material/ \((\d+)\)` cannot match below line 1. REPAIR, not my row.
3. `w2/ExecLedgerRerun.md` F6 (L75-01/L75-05 `expected_after` are Ca-lands-only) touches the combined tree, not
   the four rows staged here; not independently re-measured by this seat.

## Out of scope / known limits

- The other eight Ca legs (`REPAIR`, `APPENDONLY`, `R1EXEMPT`, `SEPARABLE`, `RECEIPTS`, `COMBINED`, `FROZENCFG`,
  `STAMP`) need `<lands>`/`<freeze>`; I measured only the `SCORECARD.md`-side facts they depend on (0 deletions,
  no lane-id citations, one leading row per pair) and report those, not the legs.
- `APPENDONLY`'s fleet clause and the `## Corrections` prose's `<lands>`/`<freeze>` are inherited wording from the
  filed round-74 section; I left them as the house shape.
- I did not run `accept-ca.py --selftest`, the do-nothing/junk controls, or the C counter (not this item); no
  claim is made about them.
- The `## Axes — round 75` heading's L1 identification is left to the L1; nothing in either counter parses it.
