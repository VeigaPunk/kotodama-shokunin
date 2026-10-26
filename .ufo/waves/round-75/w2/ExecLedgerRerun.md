# ExecLedgerRerun — round 75 / wave 2 — claim-Ca ledger attack

Seat: `ExecLedgerRerun` (executor, leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Base: `f556d1049fe651d3d63975600b13acd9fb686f15`. Target: `reports/round-75/ledger.json` (claim Ca, 10 pairs,
NOT frozen — not edited by me). Scratch clone: `/fast/scratch/hyaku/kotodama-r75/ExecLedgerRerun/clone`
(`git clone --no-hardlinks <lane> clone`, `git rev-parse --show-toplevel` = that dir, `git checkout` at base).
The lane worktree's uncommitted edits (`SHONEN.md`, `SKILL.md`, `reports/round-28/readme/sweep.py`) were never
read or graded; every measurement below is `git show <base>:<path>` or an argv run inside the base clone.

## Verdict

**Claim Ca fails as declared at LEDGER/BASEMISMATCH, under both readings of the counter's metacharacter guard,
and at REPAIR for L75-02/L75-03.** Two pairs (L75-08, L75-09) are *unobservable by construction*: their
`parse` is the non-regex string `count-presence` (0 capture groups) and cannot produce the declared token
`present` from `git grep -c` stdout, so at most 8 of 10 pairs are red-observable, against a leg that requires
`>= 10` red and `none is unobservable`. Four further pairs are refused by the guard the round-74 counter
actually implements (backtick in L75-04, `|` in L75-05/06/07). Two REPAIR pairs (L75-02/03) cannot reach a
green after-state: their `statement_after.parse` is `^`-anchored and the inherited reader compiles it with no
flags (no match ever), and even with `(?m)` the REPAIR absence clause contradicts APPENDONLY because the base
heading text survives verbatim at `corpus/README.md:785`/`:805`, lines APPENDONLY forbids changing.

Hostile pairs are cheaply repairable (exact metachar-free equivalents measured below); I do not edit the ledger.

## Per-pair table (all measured in the base clone, argv, cwd = clone)

`stated` = `stated_parse` applied to `stated_text`; `obs` = `parse` applied to `observe_cmd` stdout; `grp` = number
of capture groups in `parse`. "guard" = result of the inherited round-74 guard primitive
(`reports/round-74/accept-ca.py` at base, imported and called directly, see Receipt R2).

| pair | disp | stated_at | stated_text on exact base line | stated | obs | red | expected_after | argv[0] in allowlist | metachar hit | grp | guard | observable |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L75-01 | REPAIR | SHONEN.md:6 | yes | 412 | **808** | yes | 808 | git ✔ | none | 1 | OK | yes |
| L75-02 | REPAIR | corpus/README.md:344 | yes | 30 | **32** | yes | 32 | git ✔ | none | 1 | OK | observation yes; **after-state no** (F4, F5) |
| L75-03 | REPAIR | corpus/README.md:407 | yes | 36 | **40** | yes | 40 | git ✔ | none | 1 | OK | observation yes; **after-state no** (F4, F5) |
| L75-04 | ANNOTATE | corpus/README.md:813 | yes | 249 | **247** | yes | 247 | git ✔ | `` ` `` in pattern | 1 | **REFUSED** | no (strict) / yes (lenient) |
| L75-05 | REPAIR | SHONEN.md:6 | yes | 367 | **713** | yes | 713 | git ✔ | `\|` in pattern | 1 | **REFUSED** | no (strict) / yes (lenient) |
| L75-06 | REPAIR | SHONEN.md:6 | yes | 35 | **58** | yes | 58 | git ✔ | `\|` in pattern | 1 | **REFUSED** | no (strict) / yes (lenient) |
| L75-07 | REPAIR | SHONEN.md:6 | yes | 10 | **37** | yes | 37 | git ✔ | `\|` in pattern | 1 | **REFUSED** | no (strict) / yes (lenient) |
| L75-08 | ANNOTATE | corpus/lessons/round-74.md:37 | yes | absent | **None** (`parse-miss`) | intended yes, mechanically no | present | git ✔ | none | **0** | OK | **NO** |
| L75-09 | ANNOTATE | corpus/lessons/round-74.md:38 | yes | absent | **None** (`parse-miss`) | intended yes, mechanically no | present | git ✔ | none | **0** | OK | **NO** |
| L75-10 | ANNOTATE | LOG.md:4318 | yes | 43 | **44** | yes | 44 | git ✔ | none | 1 | OK | yes |

All 10 `stated_text`s are found on the *exact* named base line (`git show <base>:<path>` line N, whitespace-normalized
substring); no pair is off by a line. All 10 `parse` regexes compile; 8 capture, 2 (L75-08/09) do not. All 10
`rederive` strings `shlex.split` to exactly their `observe_cmd` argv (equals for all 10; so the ANNOTATE rows'
re-derivation commands are argv-equivalent where the pair is observable). Pins resolve: base commit, the empty
tree `4b825dc6…`, and every operand path exist in the clone. Ledger `fleet_report` is honest:
`git -C <fleet> cat-file -e 3a740160…` OK, `git show 3a740160….ufo/reports/round-74/kotodama.md` blob
`5df0118b9152a23830cc9f0912c004c095c90459`, sha256
`354273bc972d8b86a012a8aac024618d5defa73e72ea1eae5a960fdf64f84107` — both equal the ledger's constants.

Uniqueness: 10 distinct ids and 10 distinct (stated_at, stated token, observation) triples. Four pairs
(L75-01/05/06/07) deliberately share `SHONEN.md:6` and measure four different fields of the same sentence; the
four `statement_after` parses are prefix-monotone, so one repaired line satisfies all four
(`Registry counts at round 75 Ca landing — rows: 808, mined: 713, queued: 58, rejected: 37`) — verified by
construction in Receipt R5.

## Findings

### F1 (blocking) L75-08/L75-09: `parse` is not a regex and cannot yield the declared token
`"parse": "count-presence"` compiles (as a literal) with **0 capture groups**, so it violates LEDGER's
"compiling parse with a capture group". Runtime: stdout is `<sha>:reports/round-74/evidence/S883.txt:1`, the
literal `count-presence` never occurs → `parse-miss` → token `None` → pair **unobservable** at base. The inherited
primitive returns exactly that (Receipt R2: `token=None ok=False why=parse-miss(exit=0) groups=0`).
BASEMISMATCH then fails twice over: "none is unobservable" and "the number of such pairs >= 10" (max 8 red).
The semantic claim is fine (both anchors are present, `git grep -c` = 1 on each evidence file, exit 0); it is the
declared grammar that is broken. Same root cause for both pairs.

### F2 (blocking, strict reading) L75-04/L75-05/L75-06/L75-07: shell metacharacters in argv elements
The round-74 counter this round inherits (`reports/round-74/accept-ca.py:175` at base) sets
`SHELL_META = ("|", "&", ";", "<", ">", "`", "$(", "\n", "\r")` and scans **every** argv element
(`observe_problem`, lines 809-811). Under it:
- L75-04's pattern `` ^- `[^`]+\.md` — `` carries two backticks → `shell construct '`'`;
- L75-05/06/07's patterns `^\|…\|[[:space:]]*mined…\|` carry `|` → `shell construct '|'`.
All four are refused (`invalid-observe_cmd`) and therefore unobservable, dropping the red count to 4. The
round-74 ledger was clean of metacharacters in every element (verified: 13/13 pairs, `meta_hits=[]`), so this is a
regression, not an accepted convention. If the round-75 counter narrows the guard to `argv[0]` only ("whose
**executable** is in a read-only allowlist that EXCLUDES … shell metacharacters"), these four become observable
and only F1/F4/F5 remain — the claim still fails.

### F3 (requirement, measured) zero-match behaviour and what the counter must do
Measured: `git grep -c -E '^. Z[0-9]{3}' <base> -- corpus/SOURCES.md` prints **nothing** and exits **1**.
The inherited `run_observe` substitutes the whole stdout with `"0"`, then `observed_token` applies `parse`
(`:([0-9]+)$`), which does not match bare `0` → `parse-miss` → **unobservable** (Receipt R3). Asymmetry:
`git diff --shortstat` with zero changed files prints nothing and exits **0**, which the same code also treats as
unobservable. Required counter behaviour: map `git grep -c|-l` exit 1 + empty stdout to a count of 0 **and**
accept a bare `0` as the count token, otherwise a genuine zero silently becomes "unobservable" instead of a zero
observation; and treat empty stdout + exit 0 from `git diff --shortstat` as `0`. None of the ten pairs is an
absence pair today (L75-08/09 base count is 1, not 0), so this is a guardrail, not a current red.

### F4 (blocking, REPAIR) L75-02/L75-03 `statement_after.parse` is `^`-anchored and the inherited reader has no `re.M`
`statement_after` in the round-74 counter compiles with `re.compile(parse)` — no flags (base file, the
`statement_after` function). `^## linguistics/ \((\d+)\)` and `^## culture-material/ \((\d+)\)` then never match
below line 1. Receipt R4: `L75-02 r74_statement_after= (None, False, 'statement_after no-match in corpus/README.md')`
(same for 03; with an inline `(?m)^` the same call returns `('30', True, '')`). Round 74's own single
`statement_after` avoided this by writing the flag inline (`(?s).*civilizations/\` — (\d+) entries`). Fix: drop the
`^` (the heading text is unique) or write `(?m)^…`.

### F5 (blocking, REPAIR + APPENDONLY contradiction) the base heading text survives in README
REPAIR requires "no base `stated_text` remains at the statement path". The statement path for L75-02/03 is the
whole file `corpus/README.md`, and both base strings survive verbatim in the historical blocks:
- `corpus/README.md:785`: "…The `## linguistics/ (30)` heading and the revision block above stay as filed (append-only: an in-place heading edit would be a rewrite)…"
- `corpus/README.md:805`: "`## culture-material/ (36)` heading is left as filed and named as stale: the live directory holds 40 files and the section 38 rows."
Measured on a candidate Ca tree whose only README edits are the two declared heading repairs:
`L75-02 … statement_path= corpus/README.md stated_text_present_in_statement_path= True`,
`L75-03 … True` (Receipt R5, block C). Clearing them is impossible without breaking Ca's own APPENDONLY leg:
"changed lines elsewhere are a subset of stated_at lines of REPAIR pairs plus appended lines" — lines 785/805 are
not `stated_at` lines, and their appendix says the headings "stay as filed". So either the counter scopes the
absence clause to the `stated_at` line (deviating from the round-74 file-wide implementation and from the leg's
own "at the statement path" wording), or L75-02/03 stay red forever. Note the *heading* repair itself is correct
and self-consistent: README:806 already says the live directory holds 40 files, and the base index has
247 rows = 249 files − 2 unindexed culture-material files, so 32/40 headings plus Ca's two added index rows make
the footer relation exact (independent count: linguistics 32, culture-material 40, myth-symbol 29, synthesis 29,
verification 24, civilizations 95, total 249).

### F6 (order dependence, QUALITY 7) L75-01 and L75-05 are valid only at Ca-before-C
Every `observe_cmd` hard-pins the base revision, so all ten observations are lands-invariant by construction:
the same token is returned at base, at Ca-lands and at any combined tree. What the landing must do is write the
statement so `statement_after` captures that pinned token. Consequence: the pair cannot detect a *false* repaired
figure — a tree that writes "rows: 808" while the live registry already holds 817 still grades green.
Simulation (synthetic 9-row append S885–S893, status `mined`, Receipt R5 block D, clearly synthetic and not
evidence for claim C):
- L75-01 live count at C+Ca = **817**, ledger `expected_after` = 808;
- L75-05 live = **722**, ledger = 713;
- L75-06 = **58**, L75-07 = **37** (unchanged; the nine rows are mined), sums 817 = 722+58+37 ✔.
So: at `<Ca-lands>` without C, `statement_after` = 808/713/58/37 = the observation → green. At a combined tree,
claim C's INDEX leg *also* requires `SHONEN.md:6` to read 817/722/58/37, which then contradicts both
`expected_after` (808/713) and the base-pinned observation (808/713) → L75-01 and L75-05 red under either
comparison rule; L75-06/07 survive because their numbers do not move. **Ca must land before C**, and C must
rewrite the same line. L75-01's `why` declares this handoff; L75-05/06/07 only say "shares the in-place repair
line", so the coupling is under-declared for three of the four.
Separability otherwise holds: no observation reads a C-added byte (no S885–S893, no
`narrative-structure-frameworks*`), no `stated_at` path is `corpus/SOURCES.md`, `corpus/knowledge/**`,
`reports/round-75/evidence/**` or the assimilation dir; the only C-owned non-appended README line is the
myth-symbol heading and no pair touches it. Residual interface gap on the C side: C's `owned_inplace` lists only
that README heading, yet C's INDEX leg requires it to rewrite `SHONEN.md:6` — legal only because that line is a
Ca REPAIR `stated_at` line, and only if the Ca counter reads APPENDONLY as permitting it.

### F7 (definitional gap) "SHONEN.md's mark lines"
APPENDONLY protects "SHONEN.md's mark lines". SHONEN.md:14 defines Marks as `[~]`/`[x]` item markers, which sit on
the `- [..]` item lines (e.g. line 5), not on the `asserted:` continuation (line 6). A counter that protects the
*whole* file, or a whole marked item block, would block L75-01/05/06/07's repair and make Ca unsatisfiable. The
leg must pin the reading "lines matching the mark form `^- \[[~x ]\]`".

### F8 (casting) L75-04 measures a different quantity from the stated one
Stated `Total knowledge entries: 249.` is a *file* count; the observation counts *index rows* (247). The 2-row gap
is already self-documented in README (two `heritage-taxonomy-models*` files named unindexed at lines 809-811), and
Ca's own REPAIR leg closes it by adding the two index rows (sweep.py "zero missing rows"). So the pair is red only
as a files-vs-rows category mismatch, not a stale figure; as an ANNOTATE pair it is honest provided the SCORECARD
row says exactly that ("249 files, 247 rows at base"). Also note L75-10's observation counts only *top-level*
`*.md` (44 = 44 seat reports); the directory holds 47 `.md` because `w2/drafts/{log-entry,report-draft,scorecard-axes}.md`
are nested and excluded by `:(glob)…/w2/*.md` — correct, but the row must say "top-level" or a later seat will
recount 47 and call it a defect.

## After-state at a lands tree (REPAIR pairs)

No landing is staged for these paths at this wave instant: `w2/stage/` holds only
`reports/round-75/evidence/S885…S893.txt` (9 files, claim C's) — no `SHONEN.md`, no `corpus/README.md`, no
`corpus/SOURCES.md`. So the after-state was computed, not measured, on a candidate tree carrying exactly the
declared repairs (Receipt R5):

| pair | observation re-run at candidate Ca-lands (base-pinned) | statement_after last match | expected_after | after-state |
|---|---|---|---|---|
| L75-01 | 808 | 808 | 808 | green at Ca-lands; 817/red at any C+Ca tree (F6) |
| L75-05 | 713 | 713 | 713 | green at Ca-lands; 722/red at any C+Ca tree (F6) |
| L75-06 | 58 | 58 | 58 | green at both |
| L75-07 | 37 | 37 | 37 | green at both |
| L75-02 | 32 | **no match** (F4) | 32 | red (statement_after), red (absence clause, F5) |
| L75-03 | 40 | **no match** (F4) | 40 | red (statement_after), red (absence clause, F5) |

The two heading repairs are the live counts at base and stay true after C (C adds nothing under
`corpus/knowledge/linguistics/` or `culture-material/`), so the values are not stale — only the clauses are.

## Minimal fixes (for the L1; I do not edit the ledger)

1. L75-04: `parse` unchanged, `observe_cmd` pattern → `^- .{1}[^ ].*\.md. —` — measured **247** at base, no
   metacharacter (Receipt R6).
2. L75-05/06/07: patterns → `S[0-9]{3,}.*[[:space:]]<status>[[:space:]]. [0-9]{4}-` — measured **713 / 58 / 37**
   at base (the loose form without the `. ` date anchor over-counts mined to 716). No metacharacter.
3. L75-08/09: replace `parse:"count-presence"` with a real capture. Either keep `git grep -c` and `parse:":([0-9]+)$"`
   (observed token `1`, and the SCORECARD row must then name `1`, not `present`), or take the round-74 LC-16 idiom
   `git grep -h -o -E '(非凡特性来自最初造物主)'` + `parse:"(非凡特性来自最初造物主)"` (observed token = the matched
   span). Whichever is chosen, the ANNOTATE row's named "observed token" must be the token the counter returns.
4. L75-02/03: `statement_after.parse` → `(?m)^## linguistics/ \((\d+)\)` / `(?m)^## culture-material/ \((\d+)\)`;
   and pin the absence clause to the `stated_at` line (README:344/407) or record that these two pairs stay red
   (F5) — do not plan to edit README:785/805, APPENDONLY forbids it.
5. Pin APPENDONLY's "mark lines" reading (F7), the zero-count reading (F3), and state in the ledger that
   L75-01/L75-05's `expected_after` are Ca-lands-only values (F6).

## Receipts

R1 clone/pins: `git clone --no-hardlinks <lane> clone`; `git rev-parse --show-toplevel` →
`/fast/scratch/hyaku/kotodama-r75/ExecLedgerRerun/clone`; `git checkout -q f556d104…`; `git rev-parse HEAD` →
`f556d1049fe651d3d63975600b13acd9fb686f15`. Pins present: base commit, empty tree `4b825dc6…`, every operand path.

R2 inherited guard + observation (round-74 `accept-ca.py` extracted from base and imported):
```
SHELL_META= ('|', '&', ';', '<', '>', '`', '$(', '\n', '\r')
L75-01 prob=None token='808' ok=True why=exit=0 groups=1 stated='412'
L75-02 prob=None token='32'  ok=True why=exit=0 groups=1 stated='30'
L75-03 prob=None token='40'  ok=True why=exit=0 groups=1 stated='36'
L75-04 prob=shell construct '`' in argv element '^- `[^`]+\\.md` —' token=None ok=False why=invalid-observe_cmd:… groups=1 stated='249'
L75-05 prob=shell construct '|' in argv element '^\\|[[:space:]]*S[0-9]{3,}.*\\|[[:space:]]*mined[[:space:]]*\\|' token=None ok=False groups=1 stated='367'
L75-06 prob=shell construct '|' in argv element '^\\|…queued…' token=None ok=False groups=1 stated='35'
L75-07 prob=shell construct '|' in argv element '^\\|…rejected…' token=None ok=False groups=1 stated='10'
L75-08 prob=None token=None ok=False why=parse-miss(exit=0) groups=0 stated='absent'
L75-09 prob=None token=None ok=False why=parse-miss(exit=0) groups=0 stated='absent'
L75-10 prob=None token='44' ok=True why=exit=0 groups=1 stated='43'
```
Raw observations at base: `:808`, `32 files changed, 5689 insertions(+)`, `40 files changed, 5590 insertions(+)`,
`:247`, `:713`, `:58`, `:37`, `…/S883.txt:1`, `…/S884.txt:1`, `44 files changed, 13810 insertions(+)`.

R3 zero-match: `git grep -c -E '^. Z[0-9]{3}' <base> -- corpus/SOURCES.md` → stdout empty, `exit=1`;
`run_observe` → `('0', 'exit=1 (zero matches)')`; `observed_token` → `(None, False, 'parse-miss(exit=1 (zero matches))')`.

R4 statement_after flags: `r74 statement_after ^-anchored: (None, False, 'statement_after no-match in corpus/README.md')`;
`with inline (?m): ('30', True, '')`; per pair at base: L75-01/05/06/07 `no-match` (expected — repaired text absent at
base), L75-02/03 `no-match` (defect). Round-74 ledger's only statement_after parse: `(?s).*civilizations/` — (\d+) entries`.

R5 candidate Ca-lands (worktree edits in the scratch clone only; no commit anywhere): SHONEN.md:6 clause
`(412 rows after round 56 — 367 mined, 35 queued, 10 rejected` → `(Registry counts at round 75 Ca landing — rows: 808,
mined: 713, queued: 58, rejected: 37`; README:344 → `## linguistics/ (32)`; README:407 → `## culture-material/ (40)`.
Then: pinned observations 808/32/40/247/713/58/37/None/None/44; statement_after last matches 808/713/58/37 for
01/05/06/07 and `None` for 02/03; `stated_text_present_in_statement_path` = False for 01/05/06/07, **True** for
02/03. Synthetic C append (9 rows S885–S893, 11 cells, status `mined`, opened 2026-10-27) then live re-count with the
ledger patterns (rev argument dropped, worktree read): 817 / 722 / 58 / 37.

R6 metachar-free equivalents (base clone, `git grep -c -E`, no `|` and no backtick in any element):
`S[0-9]{3,}.*[[:space:]]mined[[:space:]]. [0-9]{4}-` → 713;
`…queued…` → 58; `…rejected…` → 37; `^- .{1}[^ ].*\.md. —` on `corpus/README.md` → 247.
(Control: `S[0-9]{3,}.*[[:space:]]mined[[:space:]]` → 716, three over-counted pre-existing rows.)

R7 independent counts at base: knowledge `.md` files 249; linguistics 32; culture-material 40; myth-symbol 29;
synthesis 29; verification 24; civilizations 95. README footers `Total knowledge entries:` at lines 749 (243),
792 (247), 813 (249). SOURCES rows 808 = mined 713 + queued 58 + rejected 37. Round-74 w2 `.md`: 47 recursive,
44 top-level (`drafts/` holds 3).

## Not done / out of scope

- No landing was applied or committed; nothing outside the scratch clone and this report was written; the lane's
  git/jj state, the fleet repo (read-only `cat-file`/`show` only), `.ufo/state`, and shokuknow were untouched.
- No build/lint/test gate run (wave-in-flight rule; the parent owns post-integration gates).
- Tool installs: none (no `pacman`, no upgrades needed).

Files written: this report only. Scratch `/fast/scratch/hyaku/kotodama-r75/ExecLedgerRerun/` deleted before yield.
