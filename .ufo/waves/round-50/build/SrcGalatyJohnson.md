# SrcGalatyJohnson — Salzman 2004 publisher page (claim C frontier), with Galaty & Johnson attempts logged

Seat: `ChousaR27R2.SrcGalatyJohnson-4` (scout, leaf). Round 50, claim C (coverage / pastoralism entry).
Lane base `4ad26836552462d28a946ca3b067cab0b5ce3532`. Read-only: no lane production file, clone,
patch, git index or jj state touched. Every URL below was opened from this host on **2026-10-21**.
Tool installs: **none** (no pacman, no uv, no binary; host-wide pacman pause respected).

## 1. Assigned item

Open a publisher/library page for **Galaty & Johnson (eds.), *The World of Pastoralism* (Guilford 1990)**
**or Salzman, *Pastoralists: Equality, Hierarchy, and the State* (2004)**; quote scope (tier B); return a
SOURCES candidate: URL, access date, kind, tier + reason, scope, ≤25-word verbatim quote with location,
what it teaches the entry and which section, recheck cadence. Open it for real; if unreachable, report
the failure and stop on that source.

**Outcome: the Salzman route delivered a publisher page with description and table of contents.**
The Galaty & Johnson route did not yield an openable page carrying scope text; every attempt is logged
in §2 and nothing from it is registered as a row.

## 2. What was actually opened (fetch order, honest)

| # | URL | Result |
|---|---|---|
| 1 | `https://www.routledge.com/Pastoralists-Equality-Hierarchy-And-The-State/Salzman/p/book/9780813338149` | **opened, HTTP 200, full page** (`Method: native`). `1st Edition`, `Copyright 2004`, `204 Pages` (page also carries a `208 Pages` line), ISBN `9780813338149`, full **Description**, full **Table of Contents**, author bio. This is the row's URL. |
| 2 | `https://www.taylorfrancis.com/books/mono/10.4324/9780429498459/pastoralists-philip-carl-salzman` | **opened, HTTP 200** (`Method: native`); page metadata only, but it carries `meta-citation_abstract` with the **identical description text**, `meta-citation_publication_date: 2018/02/13`, `meta-citation_publisher: Routledge`, `meta-books:page_count: "208"`, ISBN `9780429498459`, DOI `10.4324/9780429498459`. The 2018 Routledge ebook of the same work. |
| 3 | `https://api.crossref.org/works/10.4324/9780429498459` | **opened, JSON**. DOI `10.4324/9780429498459`; type `book`; publisher `Routledge`; title `Pastoralists`; subtitle `Equality, Hierarchy, and the State`; author Philip Carl Salzman; issued/published-online 2018-02-13; electronic ISBN `9780429498459`. Bibliographic cross-check for route 2. |
| 4 | `https://collection.sl.nsw.gov.au/record/74Vv0PW5zLXM` (State Library of NSW record for Galaty & Johnson) | **HTTP 403** — not read, not used. |
| 5 | `https://www.si.edu/object/siris_sil_772566` (Smithsonian SIRIS record for Salzman) | **HTTP 403** — not read, not used. |
| 6 | `https://archive.org/advancedsearch.php?q=title%3A%28%22world+of+pastoralism%22%29…` and `https://archive.org/services/search/v1/scrape?q=title%3A%22world%20of%20pastoralism%22…` | **timeout** on both attempts — no Galaty & Johnson record obtained. |
| 7 | `https://www.jstor.org/stable/2563702` (Mikesell 1992 review of Galaty & Johnson, *Annals of the AAG*) | **"Client Challenge"** bot wall — not read, not used. |
| 8 | `https://www.googleapis.com/books/v1/volumes?q=intitle:%22world+of+pastoralism%22` | **HTTP 429** — no record obtained. |
| 9 | `https://openlibrary.org/works/OL19603240W.json` (Open Library work record for Galaty & Johnson) | **opened**, but it returns only authors, cover and subjects (`Pastoral systems, Sf140.p38 w67 1990, 636.08/4`). **No description, no table of contents, no scope prose.** Identity-only, community-maintained catalogue; **not registered as a row**, because a row with no content invites attribution it cannot support. |

Net: one usable publisher page (Salzman 2004), one corroborating ebook page plus Crossref metadata, and
a logged failure to open any Galaty & Johnson page that states the book's scope. The assignment's "or"
is satisfied by Salzman; the Galaty & Johnson side remains an unopened-scope lead, not evidence.

## 3. SOURCES row — ready to paste (L1 assigns the id; next free is S048)

Exact 11-column shape per `corpus/SOURCES.md:28`
(`| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`).
All cells pipe-free and double-quoted where they contain commas.

```markdown
| S048 | Salzman 2004, Pastoralists: Equality, Hierarchy, and the State, Routledge — https://www.routledge.com/Pastoralists-Equality-Hierarchy-And-The-State/Salzman/p/book/9780813338149 | book | B | the book's stated programme and chapter list only — a comparative typology of pastoral societies (segmentary tribes, tribal chiefdoms, peasant pastoralists) and the equality–hierarchy–state problem; the ethnography, definitions and conclusions are unread | Routledge product page, Description paragraph 1 and Table of Contents; Copyright 2004, 204/208 pp. as listed on the two publisher pages, ISBN 9780813338149; ebook DOI 10.4324/9780429498459, Taylor & Francis, published 2018-02-13 (Crossref confirms book/Routledge/2018-02-13); accessed 2026-10-21 | publisher's own summary: divergent pastoral society types — segmentary tribes, tribal chiefdoms and peasant pastoralists — plus the analytic axes ecological and cultural variation, equality and inequality, hierarchy and the basis of power, state power and resistance; chapter list runs Equality and Anarchy, Hierarchical Image and Reality, Accommodation and Resistance to the State; a publisher description, so orientation for a social-organization axis, never authority for the ethnography | queued | 2026-10-21 | 365d | — |
```

Field notes for the integrator:
- **`id`** — do not take `S048` as fixed; L1 assigns. Everything else is paste-ready.
- **status** — `queued` at open. When the entry cites it, flip to `mined` and set `used-by` to
  `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`; log the old→new change in
  `corpus/lessons/round-50.md` per the registry rule (`corpus/SOURCES.md:8-13`).
- **Tier `B`, not `A`** — `corpus/QUALITY.md:29` (criterion 6) is explicit: publisher descriptions and
  abstracts are tier B for substantive claims about a work, even when accurate. This is the S044–S046
  precedent applied to a 2004 book. A would require the book's own text or an author/maintainer statement.
- **Edition** — the row cites the 2004 Routledge edition (the page's `Copyright 2004`, ISBN
  `9780813338149`; the page lists both `204 Pages` and `208 Pages`); the 2018 Taylor & Francis ebook
  (DOI `10.4324/9780429498459`) carries the same description and is the stable identifier if a DOI is
  wanted. Do not silently call the 2018 ebook "the
  2004 book": same work, two publisher records, and the row names both.

## 4. Verbatim quotes (≤25 words each) and their locations

**Q1 — the social-organization typology (17 words):**
> "provides detailed analyses of divergent types of pastoral societies, including segmentary tribes, tribal chiefdoms, and peasant pastoralists"

Location: Routledge product page, **Description, paragraph 1, sentence 2** (sentence begins "At an
ethnographic level, the concise volume…"), read 2026-10-21.

**Q2 — the analytic axes (18 words):**
> "ecological and cultural variation, equality and inequality, hierarchy and the basis of power, and state power and resistance"

Location: Routledge product page, **Description, paragraph 1, sentence 3** (sentence begins "At the same
time, it addresses a set of substantive theoretical issues:"), read 2026-10-21.

**Table of contents (publisher metadata, quoted as a list, not as prose):**
`Preface -- Introduction -- Agency and Adaptation -- Equality and Anarchy -- Hierarchical Image and
Reality -- Accommodation and Resistance to the State -- What can we Learn from Pastoral Peoples about
Equality, Freedom, and Democracy? -- The Dynamics of Pastoral Worlds -- Appendix`.
Location: Routledge product page, **Table of Contents** block.

The same description text is repeated verbatim on the Taylor & Francis ebook page as
`meta-citation_abstract` (route 2), which is same-publisher corroboration, not independent evidence.

## 5. Scope, tier reason, recheck

- **Scope in one line:** *the book's stated programme and chapter list* — a comparative typology of
  pastoral societies and the equality/inequality/hierarchy/state question.
- **Not a source for:** definitions of nomadic / semi-nomadic / transhumant / agro-pastoral / ranching
  (that is the mobility typology, §3 sibling rows); species ecology and herd composition (§4); products
  and the secondary-products revolution (§6); bridewealth, stock partnerships, raiding (§7 detail);
  tenure rules and commons theory (§8); any ethnographic fact or quotation from inside the book. The
  publisher page states none of these, and the book itself was not opened.
- **Tier reason, stated the way criterion 6 asks:** the page is the publisher's own description of the
  work, not the author's text. It is strong secondary orientation for what the book covers and how it
  organizes the topic (B), and it is **not** primary/authoritative for any substantive claim about
  pastoralism or about the book's arguments (not A).
- **Recheck: `365d`.** A 2004 monograph's description and ToC do not churn; recheck only to see whether
  the publisher page changes edition metadata or disappears. Trigger-based re-open before any claim from
  the book itself is used — that requires the body, not this row.

## 6. What it teaches the entry, by section

The entry does not exist yet; section numbers follow the round-50 build spec (§1 register property,
§2 boundary, §3 typology, §4 species/ecology, §5 herd lexicon, §6 products, §7 herd as wealth/exchange,
§8 tenure/commons, §9 pastoral–sedentary relations, §13 calibration bank).

1. **§3 typology — a second axis, not a substitute row.** Q1 names three *social/political* types:
   segmentary tribes, tribal chiefdoms, peasant pastoralists. The sibling §3 draft
   (`ScribeSec03Typology.md` §1) sorts by *mobility* (nomadic / semi-nomadic / transhumant /
   agro-pastoral / enclosed). **Do not merge the two axes**: a transhumant community can be segmentary
   or chiefly, and a peasant pastoralist is a settlement/tenure position, not a mobility pattern. Best
   use: a short "political organization of herders" paragraph or a second small table beside the
   mobility table, with the labels attributed to the book's chapter themes (tier B).
2. **§7 herd as wealth and exchange / §8 tenure and hierarchy.** Q2 supplies the exact analytic axes
   the entry's wealth and tenure sections must answer: equality and inequality, hierarchy and the basis
   of power. The ToC's `Equality and Anarchy` → `Hierarchical Image and Reality` sequence is a design
   instruction: equality is an empirical outcome of a herding economy, not a stage before hierarchy.
   This is the strongest use of the row.
3. **§9 pastoral–sedentary relations.** Q2's "state power and resistance" plus the chapter
   `Accommodation and Resistance to the State`: the state relation is two-way (accommodation *and*
   resistance), which is the calibration against "barbarian" stereotyping and against pure-victim
   framing.
4. **§13 calibration bank — two flags this row earns:**
   - *"pastoralists" is one type* — the publisher's own summary says the book "validates 'pastoralists'
     as a conceptual category even as it reveals the diversity of societies, subsistence strategies,
     and power arrangements subsumed by that term" (Description, paragraph 1, final sentence; paraphrase
     of the page's wording, not a second quote). Flag any entry sentence that treats the category as
     homogeneous.
   - *equality → hierarchy as a stage* — R/candidate; the ToC presents both as coexisting outcomes.
     The entry should say "herding economies vary in equality/hierarchy", never "herders evolve from
     egalitarian bands to chiefdoms".
   - The publisher's phrase "authoritative synthesis" is marketing copy. Do not repeat it as the lane's
     assessment; at tier B the row cannot certify authority.

## 7. Anti-laundering notes for the C author

1. **Do not attribute definitions to Salzman.** The page gives chapter themes and type labels; it gives
   no definitions. A sentence like "Salzman defines pastoralism as…" would be fabricated from this row.
2. **Do not quote the book.** Every verbatim string in this report is the publisher's blurb. The book's
   own prose was not opened this session.
3. **Do not use the open search snippets** that describe Galaty & Johnson's plains/desert/tundra/mountain
   division (seen in a university PDF snippet) or the Smithsonian chapter subtitles (seen in a search
   snippet). Those routes returned 403/timeout, and `corpus/SOURCES.md:119-121` says a lead is not
   evidence and never a row. If the entry needs that division, a page carrying it must be opened.
4. **Do not let the B row become sole support** for the §7/§8/§9 claims it orients. It pairs naturally
   with the Khazanov/Barfield/Fratkin/Aryal rows opened by sibling seats (see
   `ScribeSec03Typology.md` §2) and with an opened ethnographic or theoretical text for any contested
   claim.
5. **Coverage consequence:** this candidate supports a B-level social-organization axis and two
   calibration flags. It does **not** fill §1, §4, §5, §6, §7 detail or §8 rules. Claim C's coverage
   argument rests on the full row set, not on this row alone.

## 8. Gate block for the round-50 scribe (paste into `corpus/lessons/round-50.md`)

- Opened: `https://www.routledge.com/Pastoralists-Equality-Hierarchy-And-The-State/Salzman/p/book/9780813338149`,
  2026-10-21, HTTP 200. Salzman 2004, *Pastoralists: Equality, Hierarchy, and the State*, Routledge,
  ISBN 9780813338149.
- Quote Q1 (17 words): "provides detailed analyses of divergent types of pastoral societies, including
  segmentary tribes, tribal chiefdoms, and peasant pastoralists" — Description, paragraph 1, sentence 2.
- Quote Q2 (18 words): "ecological and cultural variation, equality and inequality, hierarchy and the
  basis of power, and state power and resistance" — Description, paragraph 1, sentence 3.
- Corroboration: Taylor & Francis ebook page `https://www.taylorfrancis.com/books/mono/10.4324/9780429498459/pastoralists-philip-carl-salzman`
  (2018-02-13, same description, DOI 10.4324/9780429498459) and Crossref `https://api.crossref.org/works/10.4324/9780429498459`
  (book, Routledge, 2018-02-13, ISBN 9780429498459).
- Failed routes, reported not mined: State Library of NSW 403; Smithsonian SIRIS 403; archive.org
  search timeout ×2; JSTOR review "Client Challenge"; Google Books API 429; Open Library work record
  (identity only, no scope text).
- Tier B reason: publisher description/ToC, `corpus/QUALITY.md:29` criterion 6 → B for substantive
  claims about the work; S044–S046 precedent.

## 9. Unrun checks / bounds honoured

- Did **not** open the book body or any excerpt; not reachable from the opened page and not attempted.
- Did **not** verify the 2004 print edition against a national-library catalogue (both attempted
  catalogues returned 403/429/timeout); the 2004 date comes from the publisher page's own
  `Copyright 2004` line.
- Did **not** run any lane gate, sweep, selftest or the entry's gap checks — not this seat's question.
- Did **not** write outside this report; no clone, no patch, no git/jj command.
- No installs or updates, so no tool/version/channel to record.
