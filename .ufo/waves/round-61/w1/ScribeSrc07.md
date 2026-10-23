# Round 61 W1 — ScribeSrc07 source findings

## Behavior and axis

**Coverage:** drafted four candidate source rows and one entry clause per row: two Inuit kamik/Arctic-footwear sources and two Chinese bound-footwear sources. Draft IDs S656–S659 avoid the blocks reported by Src08 (S652–S655), Src09 (S668–S673), and Src10 (S674–S679). These are integration drafts only; no corpus entry or SOURCES registry row was changed here.

## Source drafts

### S656 — Pre-Dorset kamik

| S656 | Northwest Territories Timeline, “Kamik (Boot)” — Prince of Wales Northern Heritage Centre object PWNHC/982.50.480 (page modified 2023-05-10) — https://www.nwttimeline.ca/stories/2500-year-old-kamik-boot/ | docs | A | one Pre-Dorset child’s sealskin kamik, its age, construction, and Banks Island find context | story paragraph below the 2500 Years Ago label: "Made over 2,500 years ago, this child’s boot or kamik is one of the oldest examples of footwear found in the Canadian Arctic." | one child’s sealskin kamik found on Banks Island, made over 2,500 years ago, with a sewn sole and waterproof seam | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

Entry clause: `- This child’s kamik is among the oldest footwear found in the Canadian Arctic (S656)`

Gate: `- S656 | https://www.nwttimeline.ca/stories/2500-year-old-kamik-boot/ | 2026-10-23 | "Made over 2,500 years ago, this child’s boot or kamik is one of the oldest examples of footwear found in the Canadian Arctic."`

### S657 — Arctic footwear design

| S657 | Art & Innovation: Traditional Arctic Footwear from the Bata Shoe Museum Collection — Bata Shoe Museum (published 2018-03-02; modified 2025-08-26) — https://batashoemuseum.ca/artandinnovation/ | docs | A | Inuit kamik design and fur-inlay techniques, including a 1987 Iglulingmiut polar-bear pair by Leah Okadluk | Polar Bear Kamiks caption, design paragraph: "Traditional designs are geometric but more contemporary boots feature highly curvilinear patterns." | the page describes geometric traditional designs, curvilinear patterns on newer boots, and fur inlay by Inuit seamstresses | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

Entry clause: `- More contemporary boots use curvilinear patterns (S657)`

Gate: `- S657 | https://batashoemuseum.ca/artandinnovation/ | 2026-10-23 | "Traditional designs are geometric but more contemporary boots feature highly curvilinear patterns."`

### S658 — V&A shoes for bound feet

| S658 | Pair of Shoes, unknown maker — Victoria and Albert Museum (object dated 19th century; record created 2004-01-14) — https://collections.vam.ac.uk/item/O89378/pair-of-shoes-unknown/ | docs | A | a 19th-century Chinese green-silk pair for bound feet, with embroidery and construction details | main object-description paragraph: "The shoes are made for bound feet. The shoes are embroidered with a peach blossom motif." | a green-silk pair made for bound feet, with peach-blossom embroidery, ribbon cuffs, straps, and curved wooden soles | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

Entry clause: `- These shoes are made for bound feet and have peach-blossom embroidery (S658)`

Gate: `- S658 | https://collections.vam.ac.uk/item/O89378/pair-of-shoes-unknown/ | 2026-10-23 | "The shoes are made for bound feet. The shoes are embroidered with a peach blossom motif."`

### S659 — Bata exhibition on lotus shoes

| S659 | Every Step a Lotus: Shoes in the Lives of Women in Late Imperial China — Bata Shoe Museum (curated by Dr. Dorothy Ko; page published 2025-03-05) — https://batashoemuseum.ca/timeline/every-step-a-lotus/ | docs | A | the Bata exhibition’s framing of footbinding and women’s lives in late imperial China | opening exhibition sentence after the title: "Shoes in the Lives of Women in Late Imperial China, curated by Dr. Dorothy Ko was one of our most popular exhibitions" | the exhibition explored footbinding’s cultural meanings through stages of a Chinese woman’s life in late imperial China | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

Entry clause: `- Dorothy Ko curated an exhibition about women’s shoes in Late Imperial China (S659)`

Gate: `- S659 | https://batashoemuseum.ca/timeline/every-step-a-lotus/ | 2026-10-23 | "Shoes in the Lives of Women in Late Imperial China, curated by Dr. Dorothy Ko was one of our most popular exhibitions"`

## Gates, commands, and provenance

All four kept pages were opened with ordinary static reads and their exact anchor quotes were re-opened live with the required locator. Commands and locator output (exit status):

- `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py "https://www.nwttimeline.ca/stories/2500-year-old-kamik-boot/" "Made over 2,500 years ago, this child’s boot or kamik is one of the oldest examples of footwear found in the Canadian Arctic."` → `LOCATED https://www.nwttimeline.ca/stories/2500-year-old-kamik-boot/` (exit 0).
- `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py "https://batashoemuseum.ca/artandinnovation/" "Traditional designs are geometric but more contemporary boots feature highly curvilinear patterns."` → `LOCATED https://batashoemuseum.ca/artandinnovation/` (exit 0).
- `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py "https://collections.vam.ac.uk/item/O89378/pair-of-shoes-unknown/" "The shoes are made for bound feet. The shoes are embroidered with a peach blossom motif."` → `LOCATED https://collections.vam.ac.uk/item/O89378/pair-of-shoes-unknown/` (exit 0).
- `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py "https://batashoemuseum.ca/timeline/every-step-a-lotus/" "Shoes in the Lives of Women in Late Imperial China, curated by Dr. Dorothy Ko was one of our most popular exhibitions"` → `LOCATED https://batashoemuseum.ca/timeline/every-step-a-lotus/` (exit 0).

Registry checks used `functions.grep` on `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`, case-insensitive, and returned `No matches found.` for each kept URL’s host+path pattern:

- `nwttimeline\.ca/stories/2500-year-old-kamik-boot`
- `batashoemuseum\.ca/artandinnovation`
- `collections\.vam\.ac\.uk/item/O89378`
- `batashoemuseum\.ca/timeline/every-step-a-lotus`

Screened-out attempts:

- UBC Museum of Anthropology `kamiik (Boots)`, `https://collection-online.moa.ubc.ca/search/item?person%5B0%5D=4533&row=1&tab=more`, was readable, but the required locator refused its query-bearing `/search/item` URL. The attempted command was `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py "https://collection-online.moa.ubc.ca/search/item?person%5B0%5D=4533&row=1&tab=more" "The other pieces of the boots are sewn together with an overcast stitch."`; output `NOT_LOCATED https://collection-online.moa.ubc.ca/search/item?person%5B0%5D=4533&row=1&tab=more search-url` (exit 1), so it was not kept.
- An initial Bata title quote, `Every Step a Lotus: Shoes in the Lives of Women in Late Imperial China`, was refused because the URL reflects the quote: `NOT_LOCATED https://batashoemuseum.ca/timeline/every-step-a-lotus/ url-reflects-quote` (exit 1). S659 uses the separate 22-word opening-sentence span that later located live.
- Smithsonian `https://www.si.edu/object/pair-shoes-bound-feet:nmnhanthropology_8428831` returned HTTP 403 on ordinary read. Access challenge met, not passed. The ordinary Wayback availability command `timeout 300 curl -sS 'https://archive.org/wayback/available?url=https%3A%2F%2Fwww.si.edu%2Fobject%2Fpair-shoes-bound-feet%3Anmnhanthropology_8428831'` returned `{"url": "https://www.si.edu/object/pair-shoes-bound-feet:nmnhanthropology_8428831", "archived_snapshots": {}}` (exit 0); no capture was available, and the page was not included.

## Touched surfaces, scope, and limits

- **Touched:** only this requested report artifact, `.ufo/waves/round-61/w1/ScribeSrc07.md`.
- **Not changed:** `corpus/SOURCES.md`, the footwear entry, `corpus/README.md`, tools, counters, or any product code. No tools were installed; no tests or `ACCEPT-C-61` run. The four drafts are not evidence that the overall frozen coverage predicate passes; integration and the acceptance run remain with the lane owner.
- **Out of scope:** operability claim O, additional footwear topics, and Smithsonian material without an accessible live or archived page.

## Artifact path

`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-61/w1/ScribeSrc07.md`
