# README patch — claim C, round 65 (`games-play-sport-contests.md`)

Status: **READY-TO-APPLY after the entry lands.** One unresolved dependency: the entry
does not exist at HEAD, so the index row's topic text cannot be finalised (DEP-1) and the
frontier bullet's gloss clause cannot be finalised (DEP-2). Every other byte below is
measured against the live README, not assumed.

## Provenance (measured 2026-10-24)

- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; `git rev-parse HEAD` =
  `17c32302c6845c8f164b985a8cb312d3181c8788` (claim C's declared base);
  `git status --porcelain corpus/README.md` empty (README unmodified).
- `corpus/README.md`: 713 lines, pre-edit sha256
  `c131ffd99196eed96c3251c1790c5c98ba65f9fc6abef23c6a287e551762da32`.
- Live partition counts (`ls corpus/knowledge/<part>/*.md | wc -l`):
  linguistics 30, myth-symbol 29, culture-material 31, synthesis 29, verification 24,
  civilizations 95 — **238** total. This matches README's own footer and section headers.
- Baseline instrument, pre-landing: `python3 -B reports/round-28/readme/sweep.py` →
  exit 0, `total_rows == total_files == 238`, `topic_mismatch 0`, `header_drift {}`,
  `totals_line 238`, footer `{total 238, dir_totals [30,29,31,29,24,95]}`, no footer findings.
- Target after landing: culture-material **32**, total **239**, footer vector
  **30/29/32/29/24/95**.

Section order used by the sweep's footer leg (PARTS): linguistics / myth-symbol /
culture-material / synthesis / verification / civilizations — so the vector is
`30/29/32/29/24/95`, not a permutation.

## E1 — section header (line 364)

```
-old: ## culture-material/ (31)
+new: ## culture-material/ (32)
```

Sweep `SECTION_RE` is `^## ([a-z-]+)/ \((\d+)\)\s*$`; keep the single space before `(32)`
and no trailing space.

## E2 — index row (insert as one new line between current lines 380 and 381)

Anchors (unchanged, byte-exact prefixes):

- line 380 prefix: ``- `furniture-interior-lexicon.md` — furniture and the interior as a cultural system for fictional cultures — ``
- line 381 prefix: ``- `garment-lexicon-crosslinguistic.md` — how real languages name garments — ``

New row (one physical line, no hard wrap, no trailing whitespace, em dash U+2014 with a
single space either side):

```
- `games-play-sport-contests.md` — <DEP-1: the entry's `- topic:` text, verbatim>
```

Filename-order justification: `furniture-` < `games-` (`f` < `g`) and `games-` <
`garment-` (`m` < `r`). No other culture-material filename falls between them.

### DEP-1 — derive the topic text mechanically; do not retype it

The sweep compares the row body to `topic_of(entry)`: the `- topic:` head-block field with
continuation lines space-joined. Reproduce it exactly:

```
python3 - <<'EOF'
import re, pathlib, sys
t = pathlib.Path('corpus/knowledge/culture-material/games-play-sport-contests.md').read_text(encoding='utf-8')
m = re.search(r'^- topic:(.*?)(?=\n- \w)', t, re.M | re.S)
sys.exit('NO_TOPIC_FIELD') if not m else None
print(' '.join(p.strip() for p in m.group(1).strip('\n').splitlines() if p.strip()))
EOF
```

Row rules that a paraphrase violates:
- the row is the entry's text **verbatim** — no condensation, no added emphasis, no
  backticks/bold inside the topic;
- keep a trailing period if the topic has one (round-64's row keeps `sequence.`);
- if the topic spans several source lines, the row is still ONE physical line with single
  spaces between joined lines;
- the row must start with the literal ``- `games-play-sport-contests.md` — `` (sweep
  `ROW_RE = ^- \`([^\`]+\.md)\` — (.*)$`).

Substring check the row will also be subjected to (accept-c SWEEP leg:
`topic_text in row_line`): a substring test passes even with a mangled prefix, so the
sweep's byte-equality is the binding gate.

## E3 — frontier bullet (insert after the round-64 bullet)

Placement: the `## Known gaps (frontier)` section runs from line 554; its last bullet is
the round-64 one at line 680, followed by a blank line 681 and `Total knowledge entries:
238.` at 682. Insert the new bullet as a new line **after line 680** (one physical line, no
hard wrap, following the round-64 bullet style):

```
- Round 65 adds one culture-material entry, `culture-material/games-play-sport-contests.md` (<DEP-2: the entry's leading topic clause, verbatim>), closing the games / play / sport / contests frontier gap (frontier -> core). The topic had 0 filename owners and 0 topic-line owners before it — word-bounded counts; a raw substring scan matches only `transport-mobility-lexicon.md` (`sport` inside "transport") and `sumptuary-law-rank-display.md` (`play` inside "display"), which are not owners — and a word-boundary scan of `- topic:` lines returns one incidental mention that is not an owner, `music-instrument-lexicon.md`:3 ("musical contests"); partial one-way owners remain `civilizations/taino.md` (ballgame, line 90), `civilizations/greece-classical.md` (athletic competition, line 89), and `culture-material/calendar-festival-systems.md` (assembly and games cycles, line 124).
```

### Conflict recorded verbatim (claim C's stated base command)

`reports/round-65/claims.json` claim C justifies "0 filename owners" with:

```
git ls-tree -r --name-only 17c32302 -- corpus/knowledge | grep -ciE 'game|play|sport|contest|toy|mancala'
```

Run at the declared base it prints **2**, not 0:

```
$ git ls-tree -r --name-only 17c32302 -- corpus/knowledge | grep -ciE 'game|play|sport|contest|toy|mancala'
2
$ ... | grep -iE 'game|play|sport|contest|toy|mancala'
corpus/knowledge/culture-material/sumptuary-law-rank-display.md
corpus/knowledge/culture-material/transport-mobility-lexicon.md
```

The ownership property holds under word boundaries (0 filename owners); the command as
written does not demonstrate it. No accept-c leg runs this command, so the frozen predicate
is unaffected — but the bullet must not repeat a bare "0 filename owners" that a reader's
re-run contradicts, hence the wording above. For the canonical judge: the
statement's evidence clause and this reading disagree; the patch does not edit
`claims.json` (frozen pre-wave).

### Ownership evidence behind that wording (measured at HEAD `17c32302`, 2026-10-24)

Filename owners — 0 lines:

```
ls corpus/knowledge/*/ | grep -inE '(^|[-_])(game|games|sport|sports|play|plays|contest|contests|athletic|athletics|ludic)([-_.]|$)'
```

Topic-line owners — exactly 1 line, `culture-material/music-instrument-lexicon.md:3`:

```
grep -rniE '^- topic:.*\b(games?|sports?|plays?|playing|contests?|athletics?|ludic)\b' corpus/knowledge
```

Body mentions (partial one-way owners), word-bounded, read not just counted:

- `civilizations/taino.md`:90,:100,:104,:105 — ballgame / sports
- `civilizations/olmec.md`:131 — ballplayers, ritual ballgame
- `civilizations/greece-classical.md`:89 — athletic competition at Olympia; :107 — funerary games
- `culture-material/calendar-festival-systems.md`:124 — assembly and games cycles, Olympiad dating
- `culture-material/music-instrument-lexicon.md`:90 — musical contest as jurisdiction, Apollo–Marsyas

Wording follows README revision 2.9's precedent — "0 filename owners and 1 topic-line
mention that is not an owner, `music-instrument-lexicon.md:3`" — rather than a bare
"0 topic-line owners", because a literal `\bcontest` scan does hit that line. Stating the
mention keeps the bullet true under a reader's re-run; claiming zero mentions would not.

DEP-2: the parenthetical gloss must be lifted from the landed `- topic:` line, not
invented. If the landed topic's leading clause is already quoted in E2's row, the gloss
should not paraphrase past it (the entry's own calibration language, e.g. what the entry
refuses to claim, is the safe source).

## E4 — totals line (currently line 682)

```
-Total knowledge entries: 238.
+Total knowledge entries: 239.
```

Sweep `TOTALS_RE = ^Total knowledge entries: (\d+)\.\s*$` — keep the final period, no
other change.

## E5 — counts footer (currently lines 684–686)

```
-Counts checked 2026-10-23 from the repo root:
+Counts checked 2026-10-24 from the repo root:
 `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
-(total 238 files; directory totals 30/29/31/29/24/95).
+(total 239 files; directory totals 30/29/32/29/24/95).
```

The footer is a present-tense, dated claim: use the day the inventory command is actually
run. Round 64 (commit `95c9194`) landed on 2026-10-24 but left this date at `2026-10-23`;
that staleness is not enforced by any instrument, so do not copy it. The date is captured
by `FOOTER_RE` but never checked for freshness.

## Optional — revision 2.17 block (NOT one of the four named edits; L1's call)

Round 64 landed **without** a revision block: the top block is still `revision: 2.16 —
Round-63` (line 3), so the four edits above follow the most recent landed precedent. If
L1 prefers the older convention (revisions 1.3–2.16 each carry a block), insert above line
3, followed by one blank line:

```
revision: 2.17 — Round-65 culture-material landing (2026-10-24): one
culture-material entry landed (`games-play-sport-contests.md`, <DEP-2 gloss>; before it,
0 filename owners and 0 topic-line owners, with one incidental topic-line mention that is
not an owner in `music-instrument-lexicon.md`, and partial owners cited one-way in its §2),
its row added in filename order between `furniture-interior-lexicon.md` and
`garment-lexicon-crosslinguistic.md` with the entry's `- topic:` text verbatim;
`## culture-material/` moved 31 → **32**; the totals and footer moved 238 → **239**.
```

`tools/check-readme-revisions.py` requires unique labels, no truncated stub, and
non-increasing order (newest first): 2.17 above 2.16 satisfies all three. Do not renumber
2.16 — its prose is a true statement about round 63.

## Post-apply gates and expected readings (read-only; run from the lane root)

1. `python3 -B reports/round-28/readme/sweep.py` → exit 0; `total_rows == total_files ==
   239`; `topic_mismatch 0 []`; `header_drift {}`; `totals_line 239 totals_ok True`;
   footer `total 239`, `dir_totals [30,29,32,29,24,95]`; `footer_findings []`.
2. `python3 tools/check-readme-heading.py` → exit 0 (still one H1; the culture-material H2
   text is unchanged apart from its count, so no duplicate-heading finding).
3. `python3 tools/check-readme-revisions.py` → exit 0 with the same advisory warnings as
   before the edit if the optional block is skipped (pre-existing REVISION-ORPHAN at the
   revision-1.9 body and the REVISION-GAP class are warnings, not findings).
4. `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` →
   `totals.files == 239`.
5. `python3 -B reports/round-65/accept-c.py --root .` → `SWEEP PASS` (that leg is sweep
   exit 0 **and** `topic_text in row_line`; legs FILE/ROWS/ONEID/APPEND/LIVE still depend on
   the entry and registry rows landing).

## False friends (why these counts must be word-bounded and read, not grepped plainly)

- `culture-material/transport-mobility-lexicon.md` — filename contains `sport` inside
  "transport"; a plain `grep -ci 'sport'` counts it. Not an owner.
- `culture-material/sumptuary-law-rank-display.md` — `play` inside "display". Not an owner.
- `culture-material/hunting-foraging-subsistence.md` — `game` = quarried animals ("big
  game", lines 100/126/143). Not ludic.
- `civilizations/maya-classic.md` and the other civilization files match on incidental
  words (`contests`, `playing`) inside unrelated prose; only the files named in E3 carry
  standing game content.

This is the same bypass class the round-65 counters hardened against (round-64 routed
`RESTATE` near-copy; `check-rows.py` URL normalization): a substring count is not a count.

## Limits

- DEP-1 and DEP-2 are unresolved: at write time
  `corpus/knowledge/culture-material/games-play-sport-contests.md` is absent and no draft of
  it exists under `.ufo/waves/round-65/` (`.ufo/waves/round-65/rows/` empty;
  `.ufo/waves/round-65/stage/` contained only this file). The row text is therefore a
  labelled placeholder plus a derivation command, never a guess.
- No edit was applied: `corpus/README.md` on disk is still the pre-edit sha
  `c131ffd9…2da32`. No git/jj write was performed.
- The baseline sweep reading (exit 0 at 238) says nothing about the post-landing tree; item
  5 above is the only leg that binds the row text to the entry.
- The optional revision block is a proposal, not part of the four named edits; if L1 adds
  it, the block's gloss inherits the same DEP-2 constraint.
