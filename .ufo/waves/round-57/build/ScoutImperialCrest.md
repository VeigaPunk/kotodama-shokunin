# ScoutImperialCrest — round 57, claim C (imperial chrysanthemum crest; Tokugawa aoi restriction)

Two sources opened this session by ordinary GET, both located live with the round locator. No tools installed; `pypdf 5.4.0` entered the uv cache only as `reopen-quote.py`'s own declared PDF dependency (5.7 MB, 8.5 MB, 31 MB PDFs fetched for inspection). Quote picks are English server-rendered text — Japanese pages cannot meet the locator's 8-word minimum, which ruled out most Japanese official/museum pages.

### NEW-ScoutImperialCrest-1
citation: Kyoto National Museum (National Institutes for Cultural Heritage, Japan). "Long Sword (Tachi) with Chrysanthemum Crest inscribed; named 'Kiku Gosaku'", blade, Kamakura period/13th century, collection E甲211, sword length 78.1 cm. e-Museum object record (National Treasures & Important Cultural Properties database), content_base_id 101117, English page.
url: https://emuseum.nich.go.jp/detail?langId=en&webView=&content_base_id=101117&content_part_id=0&content_pict_id=0
route: direct (plain GET, HTTP 200, no challenge; server-rendered English text)
kind: record
tier: A — official English object record of a Japanese national museum; static served text, no paywall or permission question.
scope: what the imperial chrysanthemum crest is attached to (incised on a sword tang), the hedged origin attribution to Emperor Gotoba, the crest's stated purpose (encouraging martial spirit), the crest standing in for the emperor in a blade's name, and the court's licensed-swordsmith rotation system.
quotes:
- rq-1a: "He is also said to have incised the tang with the imperial chrysanthemum crest, in order to encourage a martial spirit among his subjects."
  LOCATED https://emuseum.nich.go.jp/detail?langId=en&webView=&content_base_id=101117&content_part_id=0&content_pict_id=0
- rq-1b: "blade is said to be one of the swords the cloistered emperor Gotoba (1180-1239, r. 1183-98) forged"
  LOCATED https://emuseum.nich.go.jp/detail?langId=en&webView=&content_base_id=101117&content_part_id=0&content_pict_id=0
- rq-1c: "The blade is named \"Kiku Gosaku,\" which means \"Made by the Chrysanthemum (Emperor).\""
  LOCATED https://emuseum.nich.go.jp/detail?langId=en&webView=&content_base_id=101117&content_part_id=0&content_pict_id=0
teaches: A national museum record keeps the emperor-chrysanthemum origin story hedged, saying Gotoba is said to have incised the crest on a tang to encourage martial spirit.
draft sentences:
- A ruler's crest can be asserted where nobody sees it: the record describes the imperial chrysanthemum crest incised on the tang of a sword blade, the hidden heart of the weapon (NEW-ScoutImperialCrest-1, rq-1a).
- The crest is given an explicit political job, incised "in order to encourage a martial spirit among his subjects" — a mark as persuasion rather than ornament (NEW-ScoutImperialCrest-1, rq-1a).
- Keep origin stories at the strength the record uses: the blade "is said to be" one that the cloistered emperor Gotoba forged in the years before the Jokyu Rebellion of 1221, tradition and not documented fact (NEW-ScoutImperialCrest-1, rq-1b).
- A crest can stand in for its bearer in a name: the blade is named "Kiku Gosaku," meaning Made by the Chrysanthemum (Emperor), so the flower says emperor-as-maker (NEW-ScoutImperialCrest-1, rq-1c).
- The same record bounds who may make the marked object: the assisting smiths were famous men appointed from particular provinces connected to the court and served in fixed monthly rotations, so the mark and its licensed makers are both court-controlled (NEW-ScoutImperialCrest-1, rq-1b).

### NEW-ScoutImperialCrest-2
citation: The Walters Art Museum, Baltimore. "Tsuba with Fan and New Year's Decorations", accession 51.354, and "Tsuba with Hollyhock Crests ('Aoi mon')", Kinoshita Yoshikatsu, early 19th century (Edo period), accession 51.271; collection catalog records, English.
url: https://art.thewalters.org/object/51.354/ (primary, anchor quote), https://art.thewalters.org/object/51.271/ (second record, rq-2b)
route: direct (plain GET, HTTP 200, no challenge; server-rendered catalog text)
kind: record
tier: A — museum collection records with curatorial descriptions; static served text, open access.
scope: the Tokugawa hollyhock (aoi) crest's name and bearers, its placement on sword guards (tsuba), the restriction to the ruling family with permission granted to an outside metalworking lineage, the 1615-1867 rule span, and crest-and-maker-signature coexistence on one object.
quotes:
- rq-2a: "This crest was a symbol of the ruling Tokugawa family and was used by the Shimosaka Yasutsugu line of metalworkers with Tokugawa permission."
  LOCATED https://art.thewalters.org/object/51.354/
- rq-2b: "The hollyhock crest was used by the Tokugawa family, who ruled Japan and three of its provinces from 1615 to 1867."
  LOCATED https://art.thewalters.org/object/51.271/
teaches: The Tokugawa hollyhock crest marked the ruling family, yet a metalworking lineage bore it with Tokugawa permission, so the restriction worked by granted exceptions.
draft sentences:
- Restrict a ruling house's crest but keep a license valve: the hollyhock crest was a symbol of the ruling Tokugawa family, and the Shimosaka Yasutsugu line of metalworkers used it "with Tokugawa permission" (NEW-ScoutImperialCrest-2, rq-2a).
- Put a crest on equipment the bearer carries daily: both records place hollyhock crests on tsuba, the guards of swords (NEW-ScoutImperialCrest-2, rq-2b).
- A crest's exclusivity tracks the dynasty's span: the record ties the hollyhock crest's use to 1615-1867, the years the Tokugawa family ruled Japan and three of its provinces (NEW-ScoutImperialCrest-2, rq-2b).
- Mark of owner and mark of maker can share one object: the 51.354 guard bears a named smith's signed inscription and the Tokugawa crest granted to that smith's lineage (NEW-ScoutImperialCrest-2, rq-2a).
- The popular shorthand "only the family could bear it" over-reads the rule: the museum record itself documents an authorized outside bearer, which a worldbuilder can reuse as granted-exception texture (NEW-ScoutImperialCrest-2, rq-2a).

### Rejected
- Imperial Household Agency, "Guided Tour of the Imperial Palace" English PDF (https://www.kunaicho.go.jp/wp-content/uploads/2026/03/illustrationmap-e.pdf) — opened (8.5 MB); pages are images with no text layer (pypdf extraction ≈ empty), so the locator can never find a quote; not filed. Search-engine snippets attribute text like "The triple hollyhock design is the family crest of the Tokugawa" to it, but the served file cannot vouch for any quote.
- MOFA, Diplomatic Bluebook 2017, ch. 4 sec. 2 (passport "featuring the emblem of a chrysanthemum") — plain GET returns Akamai "Access Denied" 403 with a desktop User-Agent; challenge met, not passed; not filed.
- The Metropolitan Museum of Art object records 894754 (itomaki-tachi mountings "restricted to the family of the Shōgun") and 60501 ("imperial crest (mon): a chrysanthemum with thirty-two petals", presentation gifts to foreign dignitaries) — served HTML is a client-rendered shell (34 KB, description text absent); Wayback capture of 60501 (20250905231649) fetched only a 620-byte stub; not filed.
- VCU Scholars Compass PDF on the imperial chrysanthemum — Cloudflare "Just a moment..." interstitial to plain GET; challenge met, not passed; not filed.
- Japan Search (jpsearch.go.jp) curated kamon course — served page text is Japanese, unusable under the locator's 8-word minimum; not filed.
- Popular accounts of the aoi ban (touken-world, note.com essays, a samurai-history substack citing a 1723 Yoshimune prohibition and a 1768 reissue) — surfaced in search only, not opened; community/popular sources outside the assigned official/scholarly/museum bound.

### Freshness evidence (corpus/SOURCES.md, run this session)
- `grep -c 'nich.go.jp' corpus/SOURCES.md` → 0
- `grep -c 'art.thewalters.org/object/51.354' corpus/SOURCES.md` → 0
- `grep -c 'art.thewalters.org/object/51.271' corpus/SOURCES.md` → 0
- Host note: `grep -c 'art.thewalters.org' corpus/SOURCES.md` → 1 (S344, a different URL, an Ottoman manuscript; my object URLs are unnamed by any row), and `grep -c 'metmuseum.org/art/collection/search/60501'` → 0 (rejected row anyway).
