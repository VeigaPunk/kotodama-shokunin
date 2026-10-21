# SrcBarfield — frontier source opening for claim C (pastoralism entry)

Assigned item: open Thomas Barfield's *The Nomadic Alternative* (1993) publisher/library page,
quote the scope statement, return one SOURCES candidate (URL, access 2026-10-21, kind, tier with
reason, scope, ≤25-word located quote, what it teaches the entry, recheck cadence). Leaf seat:
no dispatch, no lane edits, no installs.

**Result: opened; row proposed as S048 (id assignment stays with L1). No source failure.**

## 1. What was actually opened this session (2026-10-21)

| Page | URL | What it gave |
|---|---|---|
| Virginia Tech library repository (VTechWorks, DSpace 7) item page | https://vtechworks.lib.vt.edu/items/9683d150-cd4e-4762-b879-72333e87c8ac (handle 10919/66221) | Title, author, 162-word abstract, publisher, ISBN |
| VTechWorks DSpace REST item record | https://vtechworks.lib.vt.edu/server/api/core/items/9683d150-cd4e-4762-b879-72333e87c8ac (JSON) | Machine-readable `dc.*` metadata; full untruncated abstract |
| HathiTrust catalog record 003556652 | https://catalog.hathitrust.org/Record/003556652 | Edition corroboration: pagination, imprint, subjects, viewability |

Observed metadata (VTechWorks API): `dc.title` "The Nomadic Alternative"; `dc.contributor.author`
"Barfield, T. J."; `dc.date.issued` "1993"; `dc.publisher` "Englewood Cliffs, Nj.: Prentice Hall";
`dc.identifier.isbn` "0-13-624982-5"; `dc.identifier.uri` http://hdl.handle.net/10919/66221;
`dc.description` "Metadata only record"; `dc.type` "Abstract"; `dc.type.dcmitype` "Text";
subjects include Nomadism, Pastoralism, Social change, Rural development, Governance, Africa.
The abstract field itself ends with "(CAB Abstracts)" — it is an aggregator abstract, not publisher
copy, and the record holds no full text.

Observed metadata (HathiTrust): "Englewood Cliffs, N.J. : Prentice Hall, c1993."; "x, 230 p. :
ill., map ; 23 cm"; ISBN 0136249825; subjects "Nomads > Economic conditions" and "Nomads > Social
conditions"; item link "Limited (search only)", University of Michigan.

Handle check (same session): `https://hdl.handle.net/10919/66221` → HTTP 302 →
`https://vtechworks.lib.vt.edu/handle/10919/66221` → 200, and that page renders the same abstract
verbatim (read this session). The row below uses the `/items/` URL I read; L1 may substitute
`https://hdl.handle.net/10919/66221` as the durable locator — it resolves to the same record.

No failure and no login wall on either page.

## 2. Proposed SOURCES row (paste-ready; id S048 is a placeholder assigned by L1)

| S048 | Barfield, The Nomadic Alternative, Prentice Hall, Englewood Cliffs NJ 1993 — https://vtechworks.lib.vt.edu/items/9683d150-cd4e-4762-b879-72333e87c8ac | book | B | the book's stated programme, chapter themes and five-case coverage as summarised in a bibliographic abstract — not its argument, evidence or page-level claims | VTechWorks item 10919/66221, Abstract field (CAB Abstracts), sentence 1; DSpace metadata: dc.date.issued 1993, dc.publisher "Englewood Cliffs, Nj.: Prentice Hall", ISBN 0-13-624982-5, dc.description "Metadata only record", dc.type "Abstract" | programme is an ethnographic and historical comparison of several nomadic pastoral societies by theme — ecology of nomadic pastoralism, comparative social organization, nomad–outside political relations, steppe-empire rise and fall, the modern future — across five herd cases (East African cattle keeping, desert Bedouin camel nomadism, southwest Asian shepherding, Eurasian steppe horse nomads, Tibetan yak breeding); separates internal evolution from adaptation to the outside world, a design dial rather than a stage ladder | queued | 2026-10-21 | 365d | — (proposed used-by: corpus/knowledge/culture-material/pastoralism-animal-husbandry.md) |

**Tier B — reason (QUALITY.md:29, criterion 6).** "publisher descriptions and abstracts are tier B
for substantive claims about a work". This is a CAB Abstracts summary on a metadata-only repository
record, so B is the ceiling; A is unavailable because the book body was never opened and the record
says "Metadata only record". The HathiTrust catalog record is tier A only for *bibliographic
identity* (edition, pagination, imprint); it says nothing substantive, so it is folded into the
anchor as corroboration rather than minted as a second row. If L1 prefers a separate
bibliographic-identity row, the HathiTrust quote is: "Englewood Cliffs, N.J. : Prentice Hall,
c1993." (7 words, "Published" line).

## 3. Verbatim quotes, with location and word counts

All from the VTechWorks item page, Abstract field (CAB Abstracts), accessed 2026-10-21.

1. Scope statement, sentence 1 (13 words):
   > "The book offers an ethnographic and historical examination of several nomadic pastoral societies."
2. Themes list, sentence 3 (19 words):
   > "the ecology of nomadic pastoralism; comparative social organization of pastoral peoples; political relations between nomads and the outside world"
3. Case list, sentence 6 (20 words):
   > "cattle keeping in East African pastoralism; the camel nomadism of the desert Bedouins; shepherding amongst pastoral tribes of southwest Asia"
4. Not quoted: the internal-evolution/adaptation sentence is 30 words, over the ≤25 limit. Paraphrase
   (sentence 5, same field): the book distinguishes developments explained by internal evolution from
   those explained as adaptations to the outside world. Do not quote it; any use must be a paraphrase
   or a trimmed verbatim span of ≤25 words with the omission marked.

## 4. What it teaches the entry, by section

Section numbers below are the model skeleton of `hunting-foraging-subsistence.md`; the new entry may
renumber, but these are the seats the source feeds.

- **Head `- sources:` / `- source:`** — external shelf row: URL above, "Abstract field (CAB
  Abstracts)" as the opened part, and an explicit note that the body is unread. This is the same
  disclosure pattern S032/S035 use for record-only rows.
- **§1 register property (charter)** — pastoralism is an argument about landscape, season, water
  and movement, with the herd as capital that eats. The abstract's "ecology of nomadic pastoralism"
  is the licence for that framing; the comparative programme is the licence to write a method, not
  "the pastoralist".
- **§2 one-owner boundary** — the source's own breadth (five cases across culture areas, each with
  ethnographic detail) is the argument for a comparative owner that does not restate regional
  entries. Hand off,
  do not duplicate: regional histories (`civilizations/mongol.md:40` mobile pastoralism coexists
  with urban production and administration; `civilizations/scythian-saka.md:70` do not equate
  pastoralism with the absence of farming; `civilizations/finnic-sami.md:140` do not map herding
  status onto identity, `:150` large-scale pastoralism has a history; `civilizations/dine-navajo.md:125`
  the Spanish-introduced sheep transformation); wealth symbolism
  (`myth-symbol/animal-symbolism.md:73` Nuer "cattle of money", `:110` faunal economy writes the
  idiom, Mongol five livestock); the field bundle
  (`linguistics/semantic-fields-lexicon-building.md:70` pastoral wealth vocabulary indexes property
  systems, `:105` "steppe pastoral" bundle); dung-as-fuel trade-off
  (`culture-material/fire-fuel-light.md:37`); the agropastoral/transhumance row
  (`culture-material/agrarian-field-system-lexicon.md:62`); the DRAFT layer of transport
  (`culture-material/transport-mobility-lexicon.md:3` ox/horse/camelid porterage and routes);
  wool processing (`culture-material/textile-technology.md:3`); milk/meat as meal
  (`culture-material/cuisine-food-lexicon.md:3`); livestock as market value
  (`culture-material/trade-economy-lexicon.md:3`). The entry owns the livestock *production system*;
  those files own their registers.
- **§3 production chain** — the case list is a species parameter, not a single chain: cattle,
  camel, sheep/goats, horse, yak × biome. The entry's chain should be written so the species and the
  pasture/water regime are inputs, not scenery. The abstract supports the *existence* of that
  variation; it does not supply any chain link's detail.
- **§5 seasonal round and mobility** — the abstract's title word "nomadic" is a cover term, not a
  typology. It does not give nomadism vs transhumance vs sedentary pastoralism, distances, camp
  moves or verticality. Those rows need the body or another source and should be `(to-verify)`
  until opened; do not let the title generate a mobility model.
- **§9 decision table / §11 decision record** — the internal-evolution vs outside-adaptation
  distinction is a genuine design dial: for each pastoral feature, decide whether it is internally
  evolved or borrowed/forced by neighbours, and make the material signature differ. This is the one
  analytic move the abstract states plainly enough to use (as a paraphrase).
- **§13 calibration bank** — candidates the source can ground or bound: "pastoralism is a stage
  between foraging and farming" (reject — a lane calibration supported by the book's comparative
  programme and `mongol.md:40`, not a claim the abstract makes); "the pastoralist" as one type
  (reject — five cases); "nomads
  are warlike/stateless by nature" (reject as a universal; the abstract's political-relations theme
  is exactly the place to state it as a variable); "a 1993 synthesis is current scholarship"
  (bounded, `(to-verify)` against current pastoralism research). The abstract's own "future of
  nomads in the modern world" is a 1990s development-studies frame, not a design claim.
- **§14 recheck** — re-open the record and, before anything load-bearing, obtain the body or a
  reviewed source; re-check the five-case list against the book's table of contents.
- **§15 scope** — the entry's scope statement can cite this row for what the comparative method is
  *for*; it cannot cite it for what any real pastoral society does.

## 5. What the row cannot support (hard limits)

- **No body, no page numbers.** The record is metadata-only. Any specific claim — herd composition,
  milk yields, camp size, descent/segmentary organization, bridewealth, commons tenure, raiding,
  state relations, gendered dairy work, taboo — is unread and must be `(to-verify)`.
- **Nomadic pastoralism only.** Animal husbandry in the mixed-farm, penned, fodder-fed, breeding-
  and-veterinary sense is *not* covered by this book's stated programme. Claim C's title is
  "pastoralism and animal husbandry"; this source can charter only the pastoral half. The husbandry
  half still needs its own opened rows (leads below, all unopened and not citable).
- **Dated synthesis.** 1993; applied-development framing (record sits in the SANREM sustainable-
  agriculture knowledgebase; subjects Rural development, Governance). Treat as a period piece for
  the history of the field, not current evidence.
- **Aggregator abstract.** CAB Abstracts wrote the summary; it is tier B by criterion 6 even where
  accurate. Do not quote it as Barfield's own words.
- **Five-case list is a claim about the book.** Verify the case list in the book's contents before
  building the entry's case table. The abstract lists five cases; other retailer/Google Books
  snippets suggest a longer group list, but I did **not** open those pages, so they are leads only
  (below), never evidence.

## 6. Leads (unopened — not evidence, not citable)

- Barfield, *The Perilous Frontier* (1989) — the steppe-empire/China-relations companion; would feed
  the political-relations section only if opened. Not opened this session.
- The book's table of contents / a published review of *The Nomadic Alternative* — needed to verify
  the five-case list and the chapter themes. Not opened.
- Current pastoralism scholarship (e.g. open-access work on mobility, commons and non-equilibrium
  ecology) — needed for the modern half and for any claim the 1993 frame cannot carry. Not opened.

## 7. Freshness evidence and one mined mistake candidate (for the round lesson)

Commands run at lane HEAD `4ad2683` (read-only; no writes):

- `grep -rn -i 'barfield' corpus/` → no output; the source is genuinely unused in the corpus.
- `find corpus/knowledge -iname '*pastoral*' -o -iname '*husband*' -o -iname '*herd*' | wc -l` → `0`.
- `grep -rniE '^- topic:.*(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/` → **1
  hit, a false positive**: `corpus/knowledge/culture-material/writing-media-surface-economy.md:3`
  matches because "sherd" contains "herd". The claim C `before_checks` evidence command is that
  exact grep; copied literally it reports a spurious hit. **Mined mistake candidate:** put word
  boundaries in the evidence command (`\b(pastoral|herd|husbandr|transhuman|livestock)\b`) or cite
  the tokenized probe instead, and record that "sherd" is the only hit. The substantive gap premise
  still holds: no `- topic:` line owns pastoralism/herding/husbandry, and no filename names it.

## 8. Gate fragment for `corpus/lessons/round-50.md` (paste-ready)

- S048 — https://vtechworks.lib.vt.edu/items/9683d150-cd4e-4762-b879-72333e87c8ac — accessed
  2026-10-21 — Abstract field (CAB Abstracts), sentence 1: "The book offers an ethnographic and
  historical examination of several nomadic pastoral societies." Grounds: stated comparative
  programme; VTechWorks record is metadata-only (ISBN 0-13-624982-5, Prentice Hall 1993), so tier B.

## 9. Unrun checks / caveats on this report

- Did not open the book body or a table of contents; every content statement above is bounded by the
  abstract.
- Did not open the retailer/Google Books pages that list further groups; those groups are not
  asserted here.
- Did not run lane gates, sweeps beyond §7, or any mutation; this is an author-lane scout report, not
  an admission. No tools installed (nothing needed; no pacman/uv/npx run).
- Word-count figures in §3 were computed mechanically on the exact strings.
