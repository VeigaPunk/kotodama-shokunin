# RevClaimC — attack on claim C's before-state (round 65, hyaku 5)

Seat: RevClaimC (independent leaf). Scope: re-derive the claim-C gap at base
`17c32302c6845c8f164b985a8cb312d3181c8788`; separate filename owners from incidental
mentions (round-64 closure method); name a partial owner the 0-owners claim would miss
(do-nothing control on the before-value). Read-only git; no writes outside this file.

**Bottom line.** The *conclusion* ("no entry owns the games/play/sport/contests register")
survives. The *stated before-value* does not: the claim's own literal command prints **2, not
0**, "0 topic-line owners" is false under a word-bounded topic-line grep (**2** files), and
**four substantive partial owners** exist that the 0 scan misses — including a wagering/contest
owner in a file with no keyword in its name. No accept-c leg re-derives any of this, so
`ACCEPT-C-65` can print all-PASS over a falsified antecedent.

## Counts (all measured at base 17c32302, not asserted)

| quantity | command | value |
|---|---|---|
| corpus/knowledge files | `git ls-tree -r --name-only 17c32302 -- corpus/knowledge \| wc -l` | **238** (0 non-`.md`) |
| culture-material files | same, `-- corpus/knowledge/culture-material` | **31** |
| registry rows | `git show 17c32302:corpus/SOURCES.md \| grep -cE '^\| *S[0-9]{3} '` | **675** |
| README index rows (strict `^- \`*.md\` — `) | `git show 17c32302:corpus/README.md` | **238** (files == rows at base) |
| **claim's literal filename grep** | `git ls-tree … -- corpus/knowledge \| grep -ciE 'game\|play\|sport\|contest\|toy\|mancala'` | **2** |
| word-bounded filename grep | `… \| grep -ciE '\b(game\|games\|play\|plays\|player\|players\|playing\|sport\|sports\|contest\|contests\|toy\|toys\|mancala)\b'` | **0** |
| word-bounded **topic-line** grep, keyword set | `git grep -cEi '^- topic:.*\b(game\|…\|mancala)\b'` | **2** |
| synonym topic-line grep (leisure/gambl/chess/dice/athlet/olympiad/arena/…) | `git grep -nEi '^- topic:.*\b(…)\b'` | **1** |
| heading-level owner sweep (corrected, `-P`, real boundaries) | `^#{1,4} .*\b(games?\|…\|gambl\w*)\b` | **3**, all idiomatic/theatrical `play` |
| files with word-bounded body `\bgames?\b` | `git grep -cP` | **23** (38 unbounded) |
| files with false-negative register vocabulary (athletic/chess/dice/wrestl/ball game/gambl/olympiad/stadium/arena) | `git grep -lEi` | **17** |

## Findings

### HIGH-1 — The claim's stated before-value is falsified by its own command (prints 2, not 0)

`reports/round-65/claims.json` claim C says verbatim: "0 filename owners … (`git ls-tree -r
--name-only 17c32302 -- corpus/knowledge | grep -ciE 'game|play|sport|contest|toy|mancala'`
prints 0 …)". At the pinned base that command prints **2**:

- `corpus/knowledge/culture-material/sumptuary-law-rank-display.md` — substring `play` in "display"
- `corpus/knowledge/culture-material/transport-mobility-lexicon.md` — substring `sport` in "transport"

Reproduced with and without the trailing-slash pathspec (2 both ways). The same regex
word-bounded prints 0, which is the value the claim intends and the only defensible form for a
before-value. The claim therefore publishes an unreproducible receipt: any reviewer who runs the
quoted command gets a contradiction of the quoted number. This is precisely the class the
round-64 closure was supposed to kill (claimed measurement not equal to runnable measurement).

Consequence: **no counter leg covers the before-value at all.** `reports/round-65/accept-c.py`
uses `BASE` only at lines 196–203 (registry baseline for APPEND) and 413–415 (`LOCATOR` pin);
the 0-owner antecedent exists only as docstring prose (line 5) and in `claims.json`. Legs are
FILE, ROWS, ONEID, RESTATE, HOSTS, LINK, APPEND, NOHARM, SWEEP, LIVE — none of them reads
`corpus/knowledge` file names or topic lines at base. `ACCEPT-C-65` is structurally blind to the
falsified leg.

Minimal repair (does not touch the frozen predicate sentence): change the quoted command to the
word-bounded form in `claims.json`'s statement, and either add a `BEFORE` leg that re-runs it
against `BASE` (expect 0) or strike the command and say "0 owners (word-bounded, read-verified;
named incidental mentions below)".

### HIGH-2 — "0 topic-line owners" is false as worded; the true statement is a semantic one

Word-bounded grep of `^- topic:` lines at base yields **2** entries, both genuine whole-word
matches (verified by extracting context, not by count alone):

- `music-instrument-lexicon.md:3` — "…named divine instruments, **musical contests**, talking drums…"
- `transport-mobility-lexicon.md:4` — "…Mesoamerican **wheeled toys** ~1500 BCE…"

The claim is true only under the reading "no entry's declared topic *is* the register", which is a
judgment about ownership, not the mechanical test the sentence presents. The round-64 closure
made exactly this distinction explicitly and *named* its incidental hits
(`corpus/lessons/round-64-verifier-spotcheck.md:34`: `git grep -il 'socialization\|socialisation'
ff30a205 -- corpus/knowledge` → "3 incidental mentions (hopi, dialect-register-consistency,
linguistic-anthropology), no owner entry"). The round-65 C statement adopts the round-64 *label*
("0 filename/topic-line owners") but not the round-64 *method* (enumerate and name the mentions).
A 0 with no mention list is indistinguishable from an unrun scan — the exact failure mode the
round-64 spot-check routed.

### HIGH-3 — Four partial owners the 0-scan misses, one of them a wagering/contest owner with no keyword in its name

Do-nothing control on the before-value (does the base already contain the register's content?):

1. `corpus/knowledge/linguistics/orality-formulaic-language.md` §7, heading at line 91 —
   "Riddles: taxonomy exams **under a license to play**". Body line 93: "Vedic **brahmodya** —
   riddle-debate as ritual and philosophical **contest** (Ṛgveda 1.164…)"; "Norse wisdom duels
   (Vafþrúðnismál: Odin **wagers** his head)". A real treatment of the contest + wager genre.
   Filename and topic line carry **no** keyword — invisible to every grep in the claim.
2. `corpus/knowledge/culture-material/music-instrument-lexicon.md:90` —
   "| **musical contest as jurisdiction** | Apollo–Marsyas (who may play what, for whom)…|", plus
   line 122 "install … a contest myth to set jurisdiction". Contest owner at table-row level.
3. `corpus/knowledge/civilizations/taino.md:92,97,103–105` — ball play as the bodily-performance
   register ("Colonial descriptions of elastic-ball play…"; "| Bodily | Ball play and coordinated
   movement. |"; and the craft warning "keep the **sports mechanics** separate"). Sport owner.
4. `corpus/knowledge/culture-material/calendar-festival-systems.md:124` — "Assembly and **games
   cycles**: Olympiad dating (from 776 BCE…)… Aztec 18 veintenas…". Games-cycle owner.

Why this is HIGH and not cosmetic: the claim's own `review_only` requires "one-way pointing to
partial owners instead of restatement", yet it names no partial owner and no leg can check
pointing. `LINK` only asserts the new URLs are absent from the entry; `NOHARM` only asserts the
diff is exactly the new file. A build seat can restate the Apollo–Marsyas contest, the Taino ball
game, or the Olympiad assembly cycle and every leg still prints PASS. The named targets are what
makes the review_only checkable; without them the requirement is unenforceable.

### MEDIUM-4 — Keyword set confounded in the other direction (`game` = prey)

`hunting-foraging-subsistence.md` has 7 word-bounded `\bgames?\b` hits, all the **prey** sense
(line 100 "big game, berries"; line 132 "dangerous game breeds circumlocution"; line 143 "Hunts
big cooperative game"). A body-level version of the claim's scan would count hunting as a games
owner; a filename/topic-level scan never sees 17 files that do carry register vocabulary
(athletic/chess/dice/wrestl/ball game/gambl/olympiad/stadium/arena). So "0" is not robust to the
level at which it is evaluated — it must state its level (filenames + declared topic), which the
current wording does not.

### MEDIUM-5 — Method hygiene: the author's tool must be nameable

During this attack my first heading sweep omitted the closing `\b` and thereby matched
"**contest**ed" in 57 headings. The corrected sweep (`git grep -P`, boundaries both sides) gives
3 hits, all idiomatic/theatrical `play` ("license to play", "early play witnesses", "contracts in
play") — none an owner. I record this because it is the same error shape as HIGH-1: an unbounded
alternative inside a boundary-anchored pattern manufactures both false zeros and false owners.
Any before-value claim should carry the exact command *and* its boundary discipline.

### MEDIUM-6 — NOHARM is keyed to the literal ref `main`, which is pinned at the base in this jj lane

`reports/round-65/accept-c.py:387` runs `git diff --name-only <BASE> main -- corpus/knowledge`.
In the lane as it stands: `git rev-parse HEAD` = `17c32302c684` (detached), `git branch` shows
`main` plus two `hyaku/*` branches, and `main` **equals the base**. So the leg's greenness depends
on the integrator's commit landing on the ref literally named `main`. If the L1 integrates by
moving a `hyaku/*` bookmark, or by advancing the detached working copy, NOHARM prints
`diff=[]`/FAIL while the entry has in fact landed — a false red on the claim's terminal leg, the
mirror image of the false green in HIGH-1. Either pin NOHARM to `HEAD` (with a separate check that
HEAD is the integration target) or state in the claim which ref receives the commit.

## Dependency (cannot attack post-state)

- `corpus/knowledge/culture-material/games-play-sport-contests.md` absent from the worktree;
  `.ufo/waves/round-65/rows/` contains **0** files; `HEAD` is the base `17c32302c684`. The
  after-value legs (FILE/ROWS/RESTATE/HOSTS/LINK/LIVE) and the 238→239 / 31→32 / 675→701
  arithmetic cannot be attacked yet — my `238`/`31`/`675`/`238-row` figures are the base side
  and are consistent with `reports/round-65/telemetry/dry-run-c.txt` (`base=675 measured=675
  +26=False`, `missing_base_lines=0`).
- `reports/round-65/separability-manifest.json` is **absent**, though `claims.json`
  `separability.check` names it and `tools/check-claim-separability.py` exists. As of this
  reading the separability check cited by the claims cannot run.

## Residual risk

- Round-64 precedent plus this lane's dry-run receipt show the after-state figures are anchored;
  the risk is not arithmetic but **unfalsifiable prose**: two before-value legs (footnote 0-owner
  and 0-topic-line) live only in statement text, so a green `ACCEPT-C-65` certifies the
  after-state and silently inherits both.
- If the entry restates any of the four partial owners, no leg catches it; only a reviewer reading
  the entry against `taino.md`/`music-instrument-lexicon.md`/`orality-formulaic-language.md`/
  `calendar-festival-systems.md` will.

## Verification gaps

- Could not run `accept-c.py` end-to-end meaningfully: FILE fails by construction at base and the
  entry does not exist yet (`dry-run-c.txt` records that state). All before-state numbers above are
  from raw `git ls-tree` / `git grep` / `git show` at the pinned base.
- `sweep.py` was not executed (read-only in principle, but its greenness at base belongs to the
  round-65 SWEEP leg, not to the before-value); the README/files equality was measured directly
  (238 == 238 with the strict row shape).
- No `lsp` server applies: this is a corpus/prose and shell-instrument review, not code with
  definitions and references. Semantic checks here are grep-plus-read by nature; I state that
  substitution explicitly rather than presenting grep as semantic proof (the grep results are
  corroborated by quoted context in every finding).

## Tool record

No installs or upgrades. Tools used: `git` (read-only: `ls-tree`, `show`, `grep`, `rev-parse`),
`grep`, `awk`, `comm`, `mktemp`. No pacman/uv/npx transactions.

Report: .ufo/waves/round-65/w1/RevClaimC.md
