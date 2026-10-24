# ScribeEntryBody — entry spec for `games-play-sport-contests.md` (claim C, pre-data)

Seat: pre-read/design (scribe), round 65 v2 wave, lane `kotodama-shokunin` at
`17c32302c6845c8f164b985a8cb312d3181c8788`. Deliverable written to
`.ufo/waves/round-65/stage/entry-spec.md` (20878 bytes). No product code, registry, README or
knowledge file was edited; no git/jj write, no tool install.

## Behavior

Produced the entry skeleton and the constraint set the assembly seat and the L1 will build
against, derived from `reports/round-65/accept-c.py` revision 1 (not from prose summaries):

- **Skeleton**: one H1, a four-line head block (`- topic:`, `- source:`, `- verified-at:`,
  `- recheck:`) modelled byte-for-byte on
  `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`, then **13 H2**
  (limit 16; zero H3), 26 bullet slots, a worldbuilder decision table, and a handoff that
  names lore-shokunin and `corpus/knowledge/synthesis/worldbible-integration-contract.md`.
- **Topic text**: one line, no ids, no URLs, no backticks, no pipe —
  `games, play, sport and contests as a culturally organized register across board and race
  games, lots, dice and spinning toys, ball courts and stick games, athletic festivals,
  children's playground lore, and the play-theory shelf — a sourced design reference for
  fictional pastimes, not a universal classification`.
- **Slot map**: one slot per id S750-S775, grouped by game class and assigned to a section —
  theory shelf S757/S758/S759 (§2); classification S750 (§3); board and race S751/S752/S753/
  S763/S764/S765/S773/S775 (§4); lots, dice and spinning S755/S767/S768 (§5); ball, court and
  stick S761/S762/S771 (§6); strength/team/ritual S754/S772 (§7); sport institution S756/S760
  (§8); cards S766 (§9); children's lore S769/S770 (§10); target games S774 (§11).
- **RESTATE rules**: exact counter semantics per rule (shape `^\s*-\s+(.*?)\s*\(S###\)\s*$`;
  one id per line; no `(to-verify|unverified|todo|fixme|tbd|draft`; >=5 `content_words`;
  >=3 content words in-order from the quote; >=1 novel content word; copied run <=12;
  teaches near-copy <0.80 in-order `[\w]+` token coverage), plus the tension between the
  quote-echo and novelty rules and a safe target of <=0.60 coverage.
- **README recipe**: four content-anchored edits — revision 2.17 block; `## culture-material/
  (31)` -> `(32)`; index row inserted between `furniture-interior-lexicon.md` and
  `garment-lexicon-crosslinguistic.md` carrying the topic verbatim on one line; totals
  `238` -> `239` and footer `(total 238 files; directory totals 30/29/31/29/24/95)` ->
  `(total 239 files; directory totals 30/29/32/29/24/95)` with the measurement date bumped —
  plus the three verification commands.

## Gates exercised (and what was only read)

Read, not run: `reports/round-65/accept-c.py` (all 448 lines), `claims.json` claim C,
`corpus/SOURCES.md` head + S745-S749, `corpus/README.md` (head, culture-material section,
footer), `reports/round-28/readme/sweep.py` (parse/footer logic), `tools/check-cited-lines.py`
(`scan_line`), `tools/check-readme-revisions.py` (docstring), the seven census `awk` commands
in `reports/round-49/run-validation.py`, and the row-fragment contract in
`.ufo/waves/round-65/spec-v2.json`.

Measured at HEAD (read-only):
- `git rev-parse HEAD` -> `17c32302c6845c8f164b985a8cb312d3181c8788` (lane HEAD == claim base).
- `git status --porcelain` -> only `?? .ufo/waves/round-65/`, `?? reports/round-65/`,
  `?? tools/check-row-fragments.py`; registry/README/knowledge clean at base.
- `grep -c '^| S' corpus/SOURCES.md` -> 675; last row S749 at line 704; table followed by a
  blank line then `## Paths` (append point for S750-S775).
- `ls corpus/knowledge/*/*.md | wc -l` -> 238; `.../culture-material/*.md` -> 31.
- README coordinates: `## culture-material/ (31)` line 364; `furniture-interior-lexicon.md`
  row 380; `garment-lexicon-crosslinguistic.md` row 381; `Total knowledge entries: 238.`
  line 682; live footer 684-686.

Executed control (the spec's preflight snippet, verbatim from the file, ENTRY pointed at the
round-64 model entry): `bad []`, `cited 26 unique 26`, `complete False` (expected — S718-S743,
not S750-S775). The snippet therefore reproduces the counter's RESTATE math and is
copy-paste-valid.

Near-copy measurements on S718's teaches cell (same import of accept-c):
`verbatim` 1.000 FAIL; `verbatim + "always"` 0.941 FAIL; one synonym in four (3/16 tokens)
0.875 FAIL; sentence re-woven 0.188 PASS; quote paraphrase 0.231 PASS.

## Touched surfaces

- `.ufo/waves/round-65/stage/entry-spec.md` (new; the deliverable).
- `.ufo/waves/round-65/w1/ScribeEntryBody.md` (this report).
Nothing else. No `corpus/`, `reports/`, `tools/` edits; no lane index/jj mutation.

## Findings (attack surface for the L1 / reviewers)

1. **The 80% near-copy rule is stronger than the round-64 bypass but still leaves a narrow
   band**: 3 substitutions in 16 tokens scores 0.875 and fails, but a clause of 6 tokens with
   4 matched tokens (0.667) passes while keeping the teaches cell's frame. The spec's safe
   target (<=0.60) is a design rule, not a counter leg.
2. **RESTATE rules 4 and 5 pull against each other**: >=3 clause content words must appear
   in-order in the quote, while >=1 must be absent from it. A clause that is a pure quote
   paraphrase can fail novelty; a fully invented clause fails in-order. Only a mixed
   paraphrase passes both.
3. **`LINK` uses substring containment** (`url in line`, `url in text`): one row's live URL
   being a prefix of another's path (e.g. a wiki page vs its disambiguated title) yields
   `registry_hits=2` and fails LINK. Row seats were told to grep for uniqueness, but the
   counter does not normalise before the substring test.
4. **`source` cell first-URL hazard**: `URL_RE.findall(source)[0]` is treated as the live URL.
   A DOI/citation link placed before it is read as the live URL, and then the capture
   normalisation fails. The fragment template (`<source name> - <live URL> ; web.archive.org/
   web/<ts>id_/<original> .`) is safe only if the source name carries no URL.
5. **`anchor` cell first-quote hazard**: `QUOTE_RE.search` takes the first `"..."` or `“...”`
   run in the cell. A quoted title before the quote (e.g. `Section "Title": "quote"`) becomes
   the measured quote.
6. **Census vs accept-c gap**: the seven census `awk` commands require `NF == 13` and
   `kind ∈ {spec,docs,paper,code,tool,dataset,talk,book,community}`, and flag tier A +
   community as tier-inflation. `accept-c.py` checks neither `kind` nor that combination, so a
   row can pass ROWS and fail the end census. The spec's §5 carries this so fragments are
   caught early.
7. **S-id ranges are fatal**: writing `S750-S775` anywhere (prose, heading, table) yields two
   ids on one line -> `check-cited-lines.py` MULTI-ID -> ONEID fails. The spec forbids ranges
   explicitly; the skeleton uses per-slot placeholders.
8. **README topic match is exact and one-line**: `sweep.py`'s `topic_of()` strips and
   space-joins continuation lines, but its index-row regex captures one line only. A wrapped
   README row silently mismatches; a multi-line `- topic:` would compare as a joined string.
9. **Footer is a dated claim**: the `Counts checked <date>` line must carry the date the
   inventory command is actually run, and the command must re-derive
   `239 / 30/29/32/29/24/95`. The preserved-history paragraph below it must not be edited.
10. **`NOHARM` forbids any other knowledge edit**, so one-way pointing to partial owners can
    only be prose inside the new entry (file names, no ids, no URLs). Any edit to an existing
    entry fails the leg even if it is a legitimate cross-reference.

## Out of scope / limits

- No entry and no row fragments exist yet (`rows/` is empty), so nothing here was validated
  against real S750-S775 data; the only executed control is the round-64 entry.
- The README recipe was not executed (the entry does not exist); the line numbers are base
  locators and the recipe is content-anchored for that reason.
- The revision-block clause "0 filename owners and 0 topic-line owners" depends on the gap
  seat's receipt; this seat did not re-derive the gap.
- `accept-c.py` was not run as a verdict (it is red at base by design); running it is the L1's
  gate. `tools/check-row-fragments.py` and the other round-65 counters were not exercised.
- The spec does not choose sources, quotes, teaches cells or bullet clauses; sentence support
  and topic fit stay review-only per `claims.json`.

## Artifacts

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-65/stage/entry-spec.md`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-65/w1/ScribeEntryBody.md`
