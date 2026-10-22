# ScoutAnchorFixes - round 55 carried registry items (S248, S254, S275 anchor cells)

Scope: three anchor cells in `corpus/SOURCES.md` carried from the round-54 closure
(`corpus/lessons/round-54-verifier-spotcheck.md` section 5 item 4; `corpus/lessons/round-54.md`
lines 182-185). I re-opened every row's URL by ordinary means on 2026-10-22, located each anchor
quote on the page, and drafted the corrected cell. No file in the lane was edited; the cells below
are for the L1 to paste.

## Result

All three cells are correctable from the pages as served. Two locator classes were wrong, and one
cell was missing the quotes for the page it already cited.

| row | carried defect | what the page actually shows | verdict |
|---|---|---|---|
| S248 | anchor repeats the "para. 2" error | quote 4 (counting the masks back into the trunk) is in **para. 3**, not para. 2; quotes 1-3 are in para. 2; the `teaches` claim "the festival that returns the set to a temple" had **no quote at all** (it is para. 5) | WRONG-LOCATOR confirmed, plus one unsupported clause |
| S254 | anchor lacks locators for the Come Home quotes | the row cites the Come Home page in its own citation cell and the entry uses it twice, but the anchor cell quotes only the Potlatch page | MISSING-LOCATOR confirmed; two Come Home quotes added |
| S275 | anchor locator nit | the two "used once" quotes sit in **"Malagan traditions" para. 3**, the paragraph that opens with Susanne Kuechler's quotation, not "the paragraph after the Michael Gunn attribution" (Gunn is named in para. 1); the marada quotes are in **"Calling for rain" para. 2** | WRONG-LOCATOR confirmed (the nit is substantive) |

## Sources opened this session

All four pages opened by direct plain `curl`, HTTP 200, no redirect, no cookie, login or challenge,
access date 2026-10-22. Quotes were checked as contiguous substrings of the saved bytes after
collapsing runs of spaces and newlines.

- `https://en.chinaculture.org/library/2008-01/17/content_56863_6.htm` - HTTP 200, `text/html`,
  14,024 bytes, redirects 0 (the same byte count the S248 row records; all four of the row's quotes
  and the fifth I add are present in these bytes).
- `https://umistapotlatch.ca/potlatch-eng.php` - HTTP 200, `text/html; charset=UTF-8`, 74,806 bytes,
  redirects 0.
- `https://umistapotlatch.ca/nos_masques_come_home-our_masks_come_home-eng.php` - HTTP 200,
  `text/html; charset=UTF-8`, 54,814 bytes, redirects 0.
- `https://collection-lacharriere.quaibranly.fr/en/malagan-head` - HTTP 200,
  `text/html; charset=UTF-8`, 135,464 bytes, redirects 0.

## Paragraph maps used as locators

S248, the Guichi section of the chinaculture page. The bold section marker
`** Nuo drama in Guichi, Anhui Province` is itself a paragraph element on the page, and the inline
image shares a paragraph with the drama-night text, so the counting rule has to be stated in the
cell. Five body paragraphs follow the heading:

1. `In Guichi, a nuo performance consists of three parts ...`
2. `In the evening, hundreds of villagers travel dozens of miles ...`
3. `The nuo drama begins around 7 pm ... After the performance, the masks are carefully and cautiously counted ...`
4. `The worship of the god of earth is held during the day ...`
5. `At the Yuanxiao Festival, which falls on the 15th day of the first lunar month ...`

S275, `Malagan traditions` (page section, heading as served): para. 1 opens `Art from New Ireland and
the Tabar Islands ... According to Michael Gunn ...`; para. 2 opens `These malagan artefacts ...`;
para. 3 opens `As Susanne Kuechler points out ...` and continues, after the closing quotation mark
and footnote 4, `As surprising as it may seem, these highly elaborate objects were only used once.`

S275, `Calling for rain`: para. 1 opens `Many malagan cultural sub-traditions exist ... As Philippe
Peltier explains ...`; para. 2 opens `Some of these heads - wrongly called 'masks' ...` and carries
both quotes.

S254, `Our Masks Come Home` page, `RETURN OF THE COLLECTION`: para. 1 opens `Once potlatching became
legal again ...`; para. 2 opens `The Kwakwaka'wakw began a concerted effort ...`; para. 3 opens `The
Kwakwaka'wakw were able to demonstrate that Indian Agent Halliday ...` and carries `Each family
decided where their regalia was to be held`.

S254, `Our Masks Come Home` page, the film block: paragraph 1 is the credit line `Film: Barbara
Cranmer`, then three transcript paragraphs (`For some years, we negotiated ...`, `"We did not have
such a thing ..."`, `The objects in the Potlatch Collection have been arranged ...`). So the objects
paragraph is the fourth paragraph element of the block and the third transcript paragraph: the
entry's `film transcript para. 3` holds only if the credit line is skipped. The corrected cell
therefore names the paragraph by its opening words.

## Corrected cells

### S248 - `corpus/SOURCES.md` line 277, anchor cell (column 6)

old:

```
Guichi section, para. 2: "hundreds of villagers travel dozens of miles to fetch the nuo mask trunk from the temple or another clan"; Guichi section, para. 2: "A specially designated person arranges the sacred nuo masks in a prescribed manner."; Guichi section, para. 2: "Every household makes offerings at the hall to honor their ancestors and the gods, and offers chicken blood to welcome the masks."; Guichi section, para. 2: "the masks are carefully and cautiously counted and placed back into the trunk"
```

new:

```
Guichi section, para. 2 (the fetching and offering paragraph): "hundreds of villagers travel dozens of miles to fetch the nuo mask trunk from the temple or another clan"; Guichi section, para. 2: "A specially designated person arranges the sacred nuo masks in a prescribed manner."; Guichi section, para. 2: "Every household makes offerings at the hall to honor their ancestors and the gods, and offers chicken blood to welcome the masks."; Guichi section, para. 3 (the drama night paragraph): "the masks are carefully and cautiously counted and placed back into the trunk"; Guichi section, para. 5 (the Yuanxiao festival paragraph): "all of the clan members carry the nuo mask trunk to Qingshan Temple to worship the nuo gods" (paragraph numbers count the five body paragraphs after the bold section heading, which is itself a page paragraph and is not counted)
```

What changed: the fourth quote moves from para. 2 to para. 3; a fifth quote is added for para. 5,
which is the only paragraph that supports the `teaches` clause "the festival that returns the set to
a temple"; and a counting note fixes the rule that the bold heading is not counted, so the next
reviewer does not re-derive a different number.

### S254 - `corpus/SOURCES.md` line 283, anchor cell (column 6)

old:

```
Potlatch page, PURPOSES OF THE POTLATCH list, second bullet, third sub-item: "The right to wear, use, and display certain regalia and objects that indicate leadership"; Potlatch page, English Translation of Potlatch Means "To Give", third paragraph: "a time for showing the masks and dances owned by the Chief or host giving the potlatch"; Potlatch page, CONTEMPORARY POTLATCH, first paragraph: "They are witnesses who are “paid” with gifts for acknowledging a family’s inheritance"; Potlatch page, CONTEMPORARY POTLATCH, first paragraph (last sentence): "Families pass down the right to tell certain stories, sing certain songs, dance certain dances"
```

new:

```
Potlatch page, PURPOSES OF THE POTLATCH list, second bullet, third sub-item: "The right to wear, use, and display certain regalia and objects that indicate leadership"; Potlatch page, English Translation of Potlatch Means "To Give", third paragraph: "a time for showing the masks and dances owned by the Chief or host giving the potlatch"; Potlatch page, CONTEMPORARY POTLATCH, first paragraph: "They are witnesses who are “paid” with gifts for acknowledging a family’s inheritance"; Potlatch page, CONTEMPORARY POTLATCH, first paragraph, last sentence: "Families pass down the right to tell certain stories, sing certain songs, dance certain dances"; Our Masks Come Home page, film transcript, the paragraph beginning The objects in the Potlatch Collection: "arranged in this big house space, more or less in the order that they would appear in a potlatch, and they're not in cases"; Our Masks Come Home page, RETURN OF THE COLLECTION, third paragraph: "Each family decided where their regalia was to be held"
```

What changed: the four Potlatch-page quotes and their locators are kept (all four verified in the
paragraphs the cell names, including the third sub-item of the nested list under the second
`PURPOSES OF THE POTLATCH` bullet); `(last sentence)` becomes `, last sentence` for the same locator
without a second bracketed locator; and two `Our Masks Come Home` page quotes are added for the two
sentences the entry actually draws from that page (the display-order sentence and the repatriation
decision sentence), each with an exact locator.

### S275 - `corpus/SOURCES.md` line 304, anchor cell (column 6)

old:

```
"Malagan traditions", paragraph after the Michael Gunn attribution: "these highly elaborate objects were only used once"; "Malagan traditions", same paragraph: "they were then destroyed, abandoned or sold once the ceremonies were over"; "Calling for rain", paragraph on the marada heads: "wrongly called ‘masks’ (because of their size, they could not be worn)"; "Calling for rain", same paragraph: "they were displayed in special enclosures that the uninitiated were not allowed to enter"
```

new:

```
"Malagan traditions", third paragraph (the one that opens with Susanne Küchler's quotation): "these highly elaborate objects were only used once"; "Malagan traditions", third paragraph: "they were then destroyed, abandoned or sold once the ceremonies were over"; "Calling for rain", second paragraph (the one after the Peltier paragraph): "wrongly called ‘masks’ (because of their size, they could not be worn)"; "Calling for rain", second paragraph: "they were displayed in special enclosures that the uninitiated were not allowed to enter"
```

What changed: `paragraph after the Michael Gunn attribution` and its `same paragraph` shorthand
become `third paragraph (the one that opens with Susanne Kuechler's quotation)`, and `paragraph on
the marada heads` and its `same paragraph` shorthand become `second paragraph (the one after the
Peltier paragraph)`. Each quote now carries its own locator and no locator depends on the previous
one.

## Verification performed

A script extracted each page's paragraphs, took the current row from `corpus/SOURCES.md` (11 columns,
anchor at index 5), and asserted, for all 15 quotes in the three new cells:

- the quote is a contiguous substring of the saved page text (whitespace normalised), so no fragment
  was joined and no word was rewritten;
- the quote is inside the paragraph the new locator names (15 of 15 pass);
- the quote is 25 words or fewer (the longest is 24, the S254 display-order quote);
- the old cell string equals the current row byte for byte, so the change log diff applies cleanly;
- no new cell contains a `|` character, so the table row keeps its 11 columns.

All 15 checks pass. Nothing in this report rests on a re-run of another seat's tool.

## Routing notes for the L1 (not edits I may make)

1. `corpus/knowledge/culture-material/masks-masquerade.md:59` cites
   `(S254, Our Masks Come Home page, para. 3)` for "After repatriation each family decided where its
   regalia would be held". That locator identifies nothing on the page. Counted at page level, the
   third paragraph falls in the exhibit's opening caption block, which is a photo credit or the
   video-player notice; counted as the film transcript it is the `We did not have such a thing among
   our people` paragraph. The sentence is in `RETURN OF THE COLLECTION, third paragraph`. Suggested
   replacement cite: `(S254, Our Masks Come Home page, RETURN OF THE COLLECTION, para. 3)`.
2. `corpus/knowledge/culture-material/masks-masquerade.md:105` cites `film transcript para. 3` for
   the display-order sentence, which is ambiguous for the reason above. Suggested replacement cite:
   `(S254, Our Masks Come Home page, film transcript, the paragraph beginning The objects in the
   Potlatch Collection)`.
3. `masks-masquerade.md:105` also drops the source's hedge: the entry says the objects were arranged
   "in potlatch order", the page says "more or less in the order that they would appear in a
   potlatch". Restoring "more or less" or "roughly" removes a small over-read.
4. If any of these cells is copied into a round-55 `## Gate` line, note that the S254 section name
   contains quotation marks of its own (`English Translation of Potlatch Means "To Give"`). Written
   as-is, the line carries a straight-quoted span inside the locator before the real quote, which is
   the shape the new `doubled-locator` finding is meant to catch. In a Gate line write the section
   name as `English Translation of Potlatch Means To Give`, or put the title in single quotes.
5. The S275 tier note says "the ethnographic sentences it quotes from Gunn, Peltier and Kuechler are
   second hand in this row". With the corrected locator it is visible that the two "used once"
   sentences are the museum's own prose in para. 3, placed after the Kuechler quotation and its
   footnote, not a quotation from Kuechler. The scope is unchanged; the note could say so, since the
   `teaches` cell leans on those two sentences.
6. `corpus/SOURCES.md` row S248 stays at `mined` with `365d`; the corrected cell does not change the
   row's status, tier or used-by.

## Unrun checks and limits

- I did not run `tools/check-source-access.py` or any other lane tool, and ran no `git` or `jj`
  command that writes. The one read-only git command I ran in the lane was `git status --porcelain`,
  to confirm that the only path I created was this report; the other entries it printed
  (`gen-build-spec.py` modified, `build-dispatch.json`, `build-sent-payload.json`, `build-spec.json`,
  and the `build/` directory) are other seats' work, not mine. Validation of a landed row belongs to
  whoever pastes the cells.
- I did not re-read the Nanfeng (S247, S249) or Kuechler (S276) sources; the S248 tier note's
  "must not be merged with the Jiangxi rows" warning is untouched and unverified here.
- The S254 village-level statements about which family holds which regalia were not re-checked
  against any other page: only the two pages the row already cites were opened.
- `S248`'s page carries no byline, so "unnamed state culture-portal explainer" in the tier note is
  still accurate; I found no author or source note to add.

## Confidence

- S248 para. numbering and the para. 3 error: high. The five body paragraphs are unambiguous in the
  page bytes and the fourth quote is in the third of them.
- S254 missing Come Home locators and the two added quotes: high. Both quotes are verbatim and the
  paragraph identities are clear; the only judgement call is naming paragraphs by their opening
  words instead of a bare ordinal.
- S275 locator correction: high for `Calling for rain` para. 2; high for `Malagan traditions`
  para. 3, with one caveat: I call it the third paragraph by counting body paragraphs under the
  heading, and the page places four figure captions between paras. 1 and 2 (and two more between
  paras. 2 and 3), so a counting rule that
  includes captions would number it differently. The cell's parenthetical names the paragraph's own
  opening words, which removes the ambiguity either way.
- Entry routing notes 1-3: medium-high. They are off-by-one and hedge issues read straight off the
  page; whether the L1 treats them as this round's work is their call, not a fact question.
