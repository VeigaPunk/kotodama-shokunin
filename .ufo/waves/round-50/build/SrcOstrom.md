# SrcOstrom — frontier source for claim C: Ostrom on the commons (2009 lecture; 1990 book record)

Seat `ChousaR27R2.SrcOstrom-4` (source seat, leaf). Round 50, claim C (coverage,
pastoralism/animal-husbandry entry). Base `4ad26836552462d28a946ca3b067cab0b5ce3532`.
Assigned: open the Cambridge page for Ostrom, *Governing the Commons* (1990) **or** the
Nobel lecture (nobelprize.org 2009), quote a located passage on common-pool
resources/pastures, and return a SOURCES candidate (URL, access date 2026-10-21, kind,
tier + reason, scope, ≤25-word verbatim quote with location, what it teaches the entry,
recheck cadence). Author-lane advice, never admission.

Read-only: no lane file, clone, patch, git index or jj state touched; nothing written
under `/home/vgpnk/Projects/shokunin/.ufo`.

## Result

Both routes opened. The **Nobel lecture is the primary candidate (tier A)**; the
**Cambridge book record is a second, optional candidate (tier B)**. Live Cambridge Core
returned HTTP 429 to this host on every direct attempt, so the book record was read from
two Wayback captures of the exact URL (identical description text). No book text was
obtained, so no 1990 wording is quoted.

| Route | Outcome |
|---|---|
| `https://www.nobelprize.org/prizes/economic-sciences/2009/ostrom/lecture/` | **opened** (native, full page). Title "Beyond Markets and States: Polycentric Governance of Complex Economic Systems"; "delivered her Prize Lecture on 8 December 2009 at Aula Magna, Stockholm University"; links "Read the Lecture" PDF (2.49 MB) and lecture slides |
| `https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf` | **opened** (PDF converted in full, 37 pp.). Title page "Prize Lecture, December 8, 2009 by Elinor Ostrom"; §4E read; page map verified against page markers |
| `https://www.cambridge.org/core/books/governing-the-commons/7AB7AE11BADA84409C34815CC288CD79` | **HTTP 429** |
| `.../7AB7AE11BADA84409C34815CC288CD79/listing` | **HTTP 429** |
| `.../9780511807763c3_p58-102_CBO.pdf` (chapter 3 extract) | **HTTP 429** |
| `https://web.archive.org/web/20250108112740/https://www.cambridge.org/core/books/governing-the-commons/7AB7AE11BADA84409C34815CC288CD79` | **opened** (full). Book description, DOI `10.1017/CBO9780511807763`, print ISBN `9780521371018`, 1990-11 / online 2012-06, contents with page spans |
| `https://web.archive.org/web/20261015114116/https://www.cambridge.org/core/books/governing-the-commons/7AB7AE11BADA84409C34815CC288CD79` | **opened** (full). Description text identical to the 2025 capture; same DOI/ISBNs; chapter 3 listed "pp 58-102" |
| `https://web.archive.org/web/20260211005523/https://www.cambridge.org/core/books/abs/governing-the-commons/analyzing-longenduring-selforganized-and-selfgoverned-cprs/93E337E42A79624A35EF138DC05A58B1` | **opened** (chapter 3 metadata only). No abstract/extract; chapter DOI `10.1017/CBO9780511807763.005`, pp. 58–102 |
| a mistyped DOI (…`51807305`) resolved by Crossref to **an unrelated book** ("Gender and Health") | recorded as a failure mode, **not used**; the row's DOI is copied from the publisher page (…`51807763`) |

Id assignment is L1's. S048 is already proposed by two source seats — `SrcUnescoGer`
(`build/SrcUnescoGer.md:11`) and `SrcDysonHudson` (`build/SrcDysonHudson.md:38`); if L1
serialises those as S048/S049, the next free ids are S050/S051, which the two rows below use
as suggested slots. `grep -rn 'S048\|S049' corpus tools reports` returns nothing — the
registry still ends at S047, so no id is yet consumed in production.

## Candidate 1 (recommended primary) — Ostrom 2009 Nobel lecture, tier A

Paste-ready row (11 columns, `corpus/SOURCES.md:25` header). `used-by` stays `—` until the
entry actually cites it; then flip `status` to `mined` and put
`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` there.

```
| S050 | Ostrom, "Beyond Markets and States: Polycentric Governance of Complex Economic Systems", Prize Lecture, 8 December 2009, NobelPrize.org — https://www.nobelprize.org/prizes/economic-sciences/2009/ostrom/lecture/ | paper | A | Ostrom's own 2009 statement of the commons design principles (updated list as developed by Cox, Arnold and Villamayor-Tomás 2009), the four-goods classification, and the caveat that the principles are analyst regularities rather than rules users hold in mind — not pastoral ethnography, not the 1990 book's wording | Prize Lecture, §4E "Long-Surviving Resource Institutions", PDF p. 15 (design-principles paragraph); lecture page → "Read the Lecture" PDF, 2.49 MB, 37 pp.; opened 2026-10-21 | the design principles (1A/1B user and resource boundaries; 2A congruence with local conditions; 2B appropriation congruent with provision; 3 collective-choice arrangements; 4A/4B monitoring users and resource; 5 graduated sanctions; 6 conflict-resolution mechanisms; 7 minimal recognition of rights; 8 nested enterprises) are regularities synthesised from long-surviving user-governed commons; Ostrom reports Cox et al.'s review of over 100 studies with two-thirds confirming; the list is the 2009 revision, not the 1990 wording; "a pasture open to all" is Hardin's assumption under critique; pastoralists appear only among the fishers, irrigators and others whose long-surviving systems the principles synthesise | queued | 2026-10-21 | 365d | — |
```

### Anchor quote (25 words, verbatim)

> The design principles appear to synthesize core factors that affect the probability of long-term survival of an institution developed by the users of a resource.

Location: §4E "Long-Surviving Resource Institutions", **PDF p. 15**, first sentence after the
numbered principles 1A–8.

### Second located passage — the pasture (23 words, verbatim)

> the users of a common-pool resource – a pasture open to all – being trapped in an inexorable tragedy of overuse and destruction

Location: §4 opening (before 4A), **PDF p. 10**, the sentence introducing Hardin (1968). The
next sentences supply the correction: "Many presumed that all common-pool resources were owned by no one." (11 words, same paragraph).

### Third located passage — calibration caveat (18 words, verbatim)

> I did not mean that the fishers, irrigators, pastoralists, and others overtly had these principles in their minds

Location: §4E, **PDF p. 15**, same paragraph as the anchor; sentence continues "…when they
developed systems that survived for long periods of time." Footnote 5 on the same page:
"Perhaps I should have used the term “best practices” to describe the rules and structure of robust institutions." (18 words).

### Fourth located passage — tenure typology (20 words, verbatim)

> A common-pool resource can be owned and managed as government property, private property, community property, or owned by no one

Location: §4C "The Bundles of Property Rights Related to Common-Pool Resources", **PDF p. 12**
(the Bromley 1986 citation follows the sentence). The same page lists the five property
rights — access, withdrawal, management, exclusion, alienation (Schlager and Ostrom 1992).

### Fifth located passage — goods classification (15 words, verbatim)

> shares the attribute of subtractability with private goods and difficulty of exclusion with public goods

Location: §2B "Doubling the Types of Goods", item 3, **PDF p. 5** (the clause defines
common-pool resources).

### Tier reasoning (QUALITY criterion 6)

Tier **A**, scoped to "Ostrom's own 2009 formulation". The PDF is Ostrom's authored lecture
text published by the Nobel Foundation, the awarding body — primary for what Ostrom said in
2009, not a publisher's description of someone else's work. This is **not** the round-49
publisher-blurb pattern (S034/S038/S039 → S044–S046): no third-party summary sits between
the claim and the text. The scope is deliberately narrow: the lecture is **not** authority
for the 1990 book's exact wording, for any pastoral ethnography, or for the empirical
literature after 2009. If a reviewer wants the 1990 text itself, the criterion-6 fix is a
new row whose anchor is the opened book text, never an in-place tier edit.

## Candidate 2 (optional) — Cambridge record of *Governing the Commons* (1990), tier B

Offer this only if L1 wants the book's identity and scope pinned in the registry; candidate 1
alone supports the entry's Ostrom citation. Live page 429s, so the row names the captures.

```
| S051 | Ostrom, Governing the Commons: The Evolution of Institutions for Collective Action, Cambridge University Press, 1990 — https://www.cambridge.org/core/books/governing-the-commons/7AB7AE11BADA84409C34815CC288CD79 | book | B | the publisher's description of the 1990 book's scope and case set, plus bibliographic identity (DOI, ISBNs, series, chapter page spans) — not the book's text, not a grazing-specific case, not pastoral ethnography | Cambridge Core book page, "Book description" paragraph, final sentence; live page HTTP 429 to this host on 2026-10-21, read via Wayback captures 20250108112740 and 20261015114116 (description text identical in both); DOI 10.1017/CBO9780511807763; print ISBN 978-0-521-37101-8; publication 30 November 1990, online 5 June 2012; series Political Economy of Institutions and Decisions | the book argues against the tragedy-of-the-commons proposition — common pool problems sometimes solved by voluntary organisations rather than a coercive state — over communal tenure in meadows and forests, irrigation communities and other water rights, and fisheries; Chapter 3 (pp. 58–102, DOI …7763.005) is the long-enduring-CPR analysis chapter; the description names meadows but no grazing case, so Alpine pasture commons and Törbel stay (to-verify) until the text is opened | queued | 2026-10-21 | 365d | — |
```

### Anchor quote (19 words, verbatim)

> Among the cases considered are communal tenure in meadows and forests, irrigation communities and other water rights, and fisheries.

Location: Cambridge Core book page, **"Book description" paragraph, final sentence** (also the
page's `citation_abstract` metadata), captures 20250108112740 and 20261015114116.

Thesis sentence, same paragraph (15 words, verbatim): "common pool problems sometimes are solved by voluntary organisations rather than by a coercive state".

### Tier reasoning (QUALITY criterion 6)

Tier **B**. This is exactly the S044–S046 archetype: a publisher description of a work is a
strong secondary for claims about the work's scope and case set, never A. The bibliographic
facts (DOI, ISBNs, dates, chapter spans) are publisher-deposited and corroborated across two
captures 21 months apart, but they remain metadata, not text. The row must **never** be cited
for the book's arguments in Ostrom's own words; use candidate 1 for Ostrom's formulation and
mark book-text quotations `(to-verify)`.

## Gate lines for the round lesson (paste-ready, `ScribeLesson.md` form)

```
- S050 — https://www.nobelprize.org/prizes/economic-sciences/2009/ostrom/lecture/ — accessed 2026-10-21 — Prize Lecture §4E, PDF p. 15: "The design principles appear to synthesize core factors that affect the probability of long-term survival of an institution developed by the users of a resource." Grounds: the 2009 design-principles list (1A–8) and its calibration caveat. Tier: A per QUALITY criterion 6.
- S051 — https://www.cambridge.org/core/books/governing-the-commons/7AB7AE11BADA84409C34815CC288CD79 — accessed 2026-10-21 — Book description, final sentence (Wayback 20250108112740 and 20261015114116): "Among the cases considered are communal tenure in meadows and forests, irrigation communities and other water rights, and fisheries." Grounds: the 1990 book's scope and case set. Tier: B per QUALITY criterion 6.
```

## What it teaches claim C's entry, by section

Section numbers follow the model entry
`corpus/knowledge/culture-material/hunting-foraging-subsistence.md` (§1 register property …
§15 scope). The pastoralism entry does not exist yet; this is the mapping the author can use.

1. **§1 register property — a pasture is a common-pool resource, by construction.** The lecture
   classifies CPRs as high subtractability plus high difficulty of exclusion (p. 5). A herding
   register therefore starts from a *governance* problem — who may take grass/water, when, and
   how much — not from "communal ownership" as a mood. Decision-table consequence: the entry's
   first axis is the **rule set**, not the species list.
2. **§2 one-owner boundary — tenure is a bundle, not a label.** The p. 12 sentence gives the
   four ownership forms (government / private / community / no one); the five rights (access,
   withdrawal, management, exclusion, alienation; Schlager and Ostrom 1992) are listed
   pp. 12–13. This is the entry's tenure typology:
   "communal pasture" splits into which of the five rights the herders actually hold. It also
   supplies the entry's sharpest correction: Hardin's "pasture open to all" (p. 10) is the
   *no-property* case, not a commons — the entry must not use "tragedy of the commons" as a
   synonym for communal tenure.
3. **§9 decision table — the eight principles as grazing-commons rows.** The pastoral gloss:
   1A who is a legitimate herder (membership/kin/residence); 1B the pasture's boundary against
   the wider landscape (winter/summer range, reserve grass); 2A rules congruent with local
   ecology and herd size; 2B offtake rules congruent with provision (rest seasons, stocking
   limits, water maintenance); 3 herders (not only officials) can change the rules; 4A/4B
   monitoring of users and of range condition; 5 graduated sanctions (fine, then exclusion);
   6 fast local conflict arenas (water points, crop damage); 7 the state recognises local
   rule-making; 8 nested enterprises for ranges that cross village/state jurisdictions — the
   only principle that speaks to transhumance, and it speaks to *authority*, not distance.
   Each row is a design question; the table's "failure mode" column is the principle absent.
4. **§13 calibration bank — status: mainstream, contested at the margins; analyst category, not
   emic rule.** Ostrom's own caveat (p. 15) and footnote 5 ("best practices") forbid reading the
   principles as rules herders hold in their minds. Evidence status as Ostrom reports it:
   Cox, Arnold and Villamayor-Tomás (2009) reviewed over 100 studies, two-thirds confirming that
   robust systems show most principles and failures do not; some studies found them inadequate
   and, in Ostrom's reading, interpreted them too rigidly. Corpus status line for the entry:
   **mainstream research programme, contested as a predictive law, diagnostic not prescriptive**.
   A worldbuilder's culture that follows all eight is not "correct"; one that follows none is
   not doomed — the table predicts durability, it does not grade cultures.
5. **§14 recheck.** The lecture is a fixed 2009 text; the live literature around the principles
   is not. Recheck the claim-status line against a current commons review before quoting a
   confirmation fraction.
6. **Explicitly not fed.** §3 production chain (herd growth, lactation, slaughter), §4 toolkit,
   §5 seasonal round's mobility mechanics, §6 storage, §7 gendered division, §8 taboo/ritual,
   §12 worked example. The lecture contains no pastoral production content. Ostrom names
   pastoralists once, in the caveat sentence; she is not an ethnographer of herders.

## Boundary inputs verified this session (for the entry's one-owner table)

- `corpus/knowledge/culture-material/agrarian-field-system-lexicon.md:62` — the agropastoral
  row already owns "fields + pasture + transhumance routes"; mixed crop-herd systems stay
  there, the new entry owns the herd-only register.
- `corpus/knowledge/linguistics/semantic-fields-lexicon-building.md:70` — pastoral wealth
  vocabulary (herd-age/colour/condition) belongs to the lexicon entry; the new entry supplies
  the production facts the vocabulary indexes.
- `corpus/knowledge/civilizations/mongol.md:40` — mobile pastoralism coexists with urban
  production and documentary administration (anti-ladder caveat); cite, do not restate the
  Mongol file's own ownership.
- `corpus/knowledge/culture-material/fire-fuel-light.md:37` — dried dung as fuel against the
  manure trade-off; the entry cites it, does not re-own fuel.
- Census, lane worktree 2026-10-21: `find corpus/knowledge -name '*.md' | wc -l` → **225**;
  `ls corpus/knowledge/culture-material/*.md | wc -l` → **27**. Matches `reports/round-50/claims.json`
  before-state; no pastoral filename exists.

## Anti-laundering notes for the C author (the r49 and r50 failure modes)

1. **The 2009 list is not the 1990 list.** The splits 1A/1B, 2A/2B, 4A/4B and the rewording of
   1, 2 and 4 are Cox et al. (2009) as adopted by Ostrom in the lecture; the 1990 book states
   the principles differently. Never quote the 2009 list as a 1990 quotation.
2. **"A pasture open to all" is Hardin's assumption, quoted by Ostrom to reject it.** Do not
   attribute the phrase to Ostrom as her model of pastoral tenure.
3. **No pastoral ethnography.** The lecture supports governance claims only. Sentences about
   herd composition, species, mobility distance, bridewealth, milk economy or camp organisation
   need other rows or `(to-verify)`.
4. **"Meadows" is not "grazing pasture".** The book description names communal tenure in
   meadows and forests; it does not name a grazing case. Any Törbel/Alpine grazing-commons
   sentence is `(to-verify)` until the book text is opened (chapter 3 extract 429'd).
5. **Copy the DOI, never reconstruct it.** `10.1017/CBO9780511807763` is what the publisher page
   records in both captures; a mistyped DOI ending `…305` resolves to an unrelated book
   ("Gender and Health"). Registry rows must be copied from the opened page.
6. **"Two-thirds of over 100 studies" is Ostrom reporting Cox et al. (2009).** Cite the chain;
   do not upgrade to "proven" or to a universal.
7. **Tier discipline.** The lecture is A only for Ostrom's own formulation; the publisher
   description is B (criterion 6). Neither row is A for pastoral practice.

## Recheck cadence

**365d for both.** The lecture PDF is a fixed 2009 text (Nobel Foundation re-uploads do occur —
the linked PDF path is a 2018 upload); the book record is a publisher metadata page whose
description could change if Cambridge revises the entry, and the catalogue is already
"no longer available to purchase". Cheaper than 365d buys nothing; the live literature the
entry's calibration line depends on should be re-opened separately, on the entry's own recheck.

## Confidence and unresolved

- Lecture quotes, locations and page numbers: **high** — full PDF opened, five passages
  matched verbatim in the converted text against PDF page markers.
- Book metadata (DOI, ISBNs, dates, chapter spans): **high** — two captures 21 months apart,
  identical description text; live page 429 on three routes.
- Book text (1990 wording, chapter 3 content, any grazing case): **unopened** — no extract, no
  abstract; the chapter page carries metadata only.
- Tier calls: **A** for the lecture scope, **B** for the book record; argument stated so L1 can
  overrule with a superseding row rather than an in-place edit.
- Id slots: suggested S050/S051 only; S048/S049 are contested by two other source seats and
  assignment is L1's.

## Unrun checks / bounds honoured

- No lane validators (`reports/round-28/readme/sweep.py`, `reports/round-49/run-validation.py`)
  run — source seat, no production edits; the entry's own sweeps belong to its executor.
- No installs (no pacman/uv/npx transaction); nothing to record under the tooling directive.
- No clone and no patch — scout/source seat, not executor.
- No file outside this report was written; no git or jj command run in the lane.
