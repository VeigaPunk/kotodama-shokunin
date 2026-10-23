# ScribeSrc03 — Round 61 wave 1 source findings

**Axis:** coverage. **Scope:** Roman military footwear / Vindolanda shoes, and medieval pointed poulaines plus sumptuary rules. Task provenance states lane revision `78ad4b176695e9fcd490ab607cb8218e2ce62738`; I did not run git/jj to independently verify it.

## Draft sources and entry lines

IDs below are proposed from the reserved S652–S699 block; they are not committed. The L1 integration owner must reconcile IDs against concurrent drafts before landing them.

| S652 | The Vindolanda Trust, “The Curator’s Favourite Shoes” (published 22 September 2020; updated 6 February 2021; no author byline shown) — https://www.vindolanda.com/blog/the-curators-favourite-shoes (direct read and live quote locator, accessed 2026-10-23; no access challenge observed) | docs | A | Vindolanda curator’s description of iron studs securing leather layers in Roman shoe soles | Lady’s shoe sole paragraph: “The iron studs on any Roman shoe are there as a way of holding the numerous layers of leather which make up the sole together” | Iron studs joined the leather layers making up a Roman shoe’s sole. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
| S653 | Sonya Galloway, “Magna Shoes,” The Vindolanda Trust (page published 30 June 2025; press release dated 2 July 2025) — https://www.vindolanda.com/news/magna-shoes (direct read and live quote locator, accessed 2026-10-23; no access challenge observed) | news | A | The Trust’s shoe-collection description, including marching boots and sandals | Vindolanda shoe-collection paragraph: “The collection includes tiny baby booties, elaborate summer sandals and marching boots” | The collection includes tiny baby booties, elaborate summer sandals and marching boots. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
| S654 | Victoria and Albert Museum, “Leather shoe,” object O74164, accession T.111&A-1918 (made 1370–1500; record created 11 February 2003) — https://collections.vam.ac.uk/item/O74164/ (direct read and live quote locator, accessed 2026-10-23; no access challenge observed) | docs | A | V&A object description of a poulaine and its pointed toe | Summary description: “This is part of a poulaine, a type of medieval man’s shoe with a long pointed toe” | A poulaine is a medieval man’s shoe with a long pointed toe. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
| S655 | London Museum, “Pointy shoes & sexuality in medieval London” (writing/research credit: Andrew Millar; no date shown) — https://www.londonmuseum.org.uk/collections/london-stories/pointy-shoes-sexuality-medieval-london/ (direct read and live quote locator, accessed 2026-10-23; no access challenge observed) | docs | B | London Museum account of English sumptuary laws setting poulaine length by station | “Why was there backlash against poulaines?” paragraph: “England then passed sumptuary laws (laws governing dress and behaviour) which set out regulations for how long somebody's poulaines could be based on their station” | England’s sumptuary laws set regulations for poulaine length by station. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

Entry lines (one clause and one ID each):

- Iron studs joined the leather layers making up a Roman shoe’s sole. (S652)
- The collection includes tiny baby booties, elaborate summer sandals and marching boots. (S653)
- A poulaine is a medieval man’s shoe with a long pointed toe. (S654)
- In England, sumptuary laws set regulations for poulaine length by station. (S655)

## Gate lines

- S652 | https://www.vindolanda.com/blog/the-curators-favourite-shoes | 2026-10-23 | “The iron studs on any Roman shoe are there as a way of holding the numerous layers of leather which make up the sole together”.
- S653 | https://www.vindolanda.com/news/magna-shoes | 2026-10-23 | “The collection includes tiny baby booties, elaborate summer sandals and marching boots”.
- S654 | https://collections.vam.ac.uk/item/O74164/ | 2026-10-23 | “This is part of a poulaine, a type of medieval man’s shoe with a long pointed toe”.
- S655 | https://www.londonmuseum.org.uk/collections/london-stories/pointy-shoes-sexuality-medieval-london/ | 2026-10-23 | “England then passed sumptuary laws (laws governing dress and behaviour) which set out regulations for how long somebody's poulaines could be based on their station”.

## Locator commands and outcomes

Commands were run with `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py URL "QUOTE"; echo exit=$?` (the exact invocations are below). All kept quotes are body text, 8–25 words, contain footwear lexicon terms, and were LOCATED live (exit 0). No Wayback captures were needed.

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.vindolanda.com/blog/the-curators-favourite-shoes' "The iron studs on any Roman shoe are there as a way of holding the numerous layers of leather which make up the sole together"; echo exit=$?
LOCATED https://www.vindolanda.com/blog/the-curators-favourite-shoes
exit=0

timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.vindolanda.com/news/magna-shoes' "The collection includes tiny baby booties, elaborate summer sandals and marching boots"; echo exit=$?
LOCATED https://www.vindolanda.com/news/magna-shoes
exit=0

timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://collections.vam.ac.uk/item/O74164/' "This is part of a poulaine, a type of medieval man’s shoe with a long pointed toe"; echo exit=$?
LOCATED https://collections.vam.ac.uk/item/O74164/
exit=0

timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.londonmuseum.org.uk/collections/london-stories/pointy-shoes-sexuality-medieval-london/' "England then passed sumptuary laws (laws governing dress and behaviour) which set out regulations for how long somebody’s poulaines could be based on their station"; echo exit=$?
LOCATED https://www.londonmuseum.org.uk/collections/london-stories/pointy-shoes-sexuality-medieval-london/
exit=0

timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.londonmuseum.org.uk/collections/london-stories/pointy-shoes-sexuality-medieval-london/' "England then passed sumptuary laws (laws governing dress and behaviour) which set out regulations for how long somebody's poulaines could be based on their station"; echo exit=$?
LOCATED https://www.londonmuseum.org.uk/collections/london-stories/pointy-shoes-sexuality-medieval-london/
exit=0
```

The last source was first tried with a typographic apostrophe in `somebody’s` and also located (exit 0); the final gate quote and command use the body’s straight apostrophe exactly.

## URL reuse checks

`grep` tool searches against `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md` (host+path):

- `vindolanda\.com/(blog/the-curators-favourite-shoes|news/magna-shoes|blog/winter-research-hipposandals)` → `No matches found`.
- `collections\.vam\.ac\.uk/item/O74164` → `No matches found`.
- `londonmuseum\.org\.uk/collections/london-stories/pointy-shoes-sexuality-medieval-london` → `No matches found`.

## Findings, limits, and gates

- Axis coverage: four source drafts, two per requested sub-topic. The V&A object record supplies a museum description of a poulaine; the London Museum page supplies the station-based sumptuary rule.
- Roman limit: the kept passages describe iron studs on Roman shoes and marching boots, but neither quote explicitly names *caligae* or uses “hobnail.” Do not claim these passages independently establish that specific footwear term or a military caligae pattern.
- A second V&A record, O107559 (“Shoe,” late 14th century), was opened but not retained; its pointed-poulaine description duplicated the selected V&A object record. No quote locator was run for it.
- No access challenge was observed on the four kept pages. Discovery-only endpoints were not used as sources: the British Museum caligae search and Portable Antiquities Scheme search returned fetch failures/HTTP 403; Google Search returned its access-trouble page and Bing yielded no useful search result. No challenge was bypassed; no Wayback substitution was made.
- **ACCEPT-C-61 and build gates were not run.** This seat made no product, counter, judge, corpus, README, or entry changes. No installs were made. The only in-repository write is this report; no scratch files were created.

**Artifact:** `.ufo/waves/round-61/w1/ScribeSrc03.md`
