# Round 61 W1 — ScribeSrc10 source report

## Axes and outcome

- **Coverage:** six source drafts across the three assigned topics; two retained sources per topic.
- **Traceability:** all six retained anchor quotes were located by the round-61 locator on the cited live URL; the scholarly PDF was read with the mandated `pypdf==5.4.0` route.
- **Scope fidelity:** entry lines below paraphrase only their quoted clauses. The second opanci record is explicitly a public-library Folk Arts Collection record, not an ethnographic museum record.
- **Outcome:** six locatable drafts are handed to the integration owner. This subset does not by itself meet claim C's 20-row floor. No product entry or SOURCES row was integrated by this seat, and no ACCEPT-C/ACCEPT-O score was run.

## Draft source rows, entry lines, and Gate lines

The rows use the lane registry's current 11-field schema (13 pipe-delimited tokens including the boundary blanks). IDs S674–S679 were coordinated as this seat's draft block; the rows remain drafts for the sole integration owner.

### 1. Indian paduka toe-knob sandals

| S674 | Victoria and Albert Museum, London, “Sandal”, record O232311 / accession IS.7-2022; made in Kutch, India, 1850–1900; record created 14 May 2009 — https://collections.vam.ac.uk/item/O232311/sandal-unknown/ | docs | A | one V&A pair of toe-knob sandals from Kutch and the museum label's bridal-gift description | 2015–2016 gallery label, “Silver Sandals for the Bride”, sentence beginning “The epitome”: “The epitome of luxury, these ornately worked toe-knob sandals, known as paduka, were one of the many often extravagant presents a bride might receive.” | the V&A label says toe-knob paduka were among the often extravagant presents a bride might receive | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

- A bride might receive toe-knob paduka among the often extravagant presents. (S674)
- S674 | https://collections.vam.ac.uk/item/O232311/sandal-unknown/ | 2026-10-23 | “The epitome of luxury, these ornately worked toe-knob sandals, known as paduka, were one of the many often extravagant presents a bride might receive.”

| S675 | Victoria and Albert Museum, London, “Ritual object”, record O482201 / accession IS.2199-1883; record created 25 June 2009 — https://collections.vam.ac.uk/item/O482201/ritual-object/ | docs | A | a V&A ritual-object record identifying the sandal (paduka) knobs between the toes | Physical description, sentence beginning “These also”: “These also have the knobs of sandals (paduka) protruding between the toes.” | the V&A description says sandal (paduka) knobs protrude between the toes of the described object | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

- The ritual object has sandal knobs protruding between the toes. (S675)
- S675 | https://collections.vam.ac.uk/item/O482201/ritual-object/ | 2026-10-23 | “These also have the knobs of sandals (paduka) protruding between the toes.”

### 2. Balkan opanci / opanak

| S676 | Ethnographic Museum in Belgrade, “Crafts” collection page (undated) — https://etnografskimuzej.rs/en/zbirka/crafts/ | docs | A | the museum's craft collection and an opančar workshop for traditional leather opanci | Crafts Collection description, workshop sentence: “an opančar workshop (for making opanci—traditional leather footwear)” | the museum's Crafts Collection includes an opančar workshop for making traditional leather opanci | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

- The museum’s collection includes an opančar workshop for making traditional leather opanci. (S676)
- S676 | https://etnografskimuzej.rs/en/zbirka/crafts/ | 2026-10-23 | “an opančar workshop (for making opanci—traditional leather footwear)”

| S677 | Cleveland Public Library Digital Gallery, Folk Arts Collection, “Serbian Shoes, Child's (Opanci)”, record 836 (undated) — https://cplorg.contentdm.oclc.org/digital/api/singleitem/collection/p4014coll10/id/836 | docs | A | one Folk Arts Collection catalogue record's description of leather-shoe sole and upper construction | Description field in the record JSON: “A pair of leather shoes, their soles are attached to the uppers with knotted leather thongs.” | the library record describes leather shoes whose soles are attached to the uppers with knotted leather thongs | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

- A pair of leather shoes has soles attached to the uppers with knotted leather thongs. (S677)
- S677 | https://cplorg.contentdm.oclc.org/digital/api/singleitem/collection/p4014coll10/id/836 | 2026-10-23 | “A pair of leather shoes, their soles are attached to the uppers with knotted leather thongs.”

### 3. Shoe sole / shoe-throwing insult

| S678 | Martin Asser, BBC News, “Bush shoe-ing worst Arab insult”, 15 December 2008 — http://news.bbc.co.uk/2/hi/middle_east/7783325.stm | news | B | the BBC report's statement about displaying a shoe sole in Arab culture | Opening body paragraph, sentence beginning “In Arab culture”: “In Arab culture it's considered rude even to display the sole of one's shoe to a fellow human being.” | the BBC report says displaying a shoe's sole to another person is considered rude in Arab culture | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

- Displaying a shoe’s sole to another person is considered rude in Arab culture. (S678)
- S678 | http://news.bbc.co.uk/2/hi/middle_east/7783325.stm | 2026-10-23 | “In Arab culture it's considered rude even to display the sole of one's shoe to a fellow human being.”

| S679 | Hana, Yafia Yousif Jamil. 2024. “Shoes in the Arabic Socio-Cultural Space and in the Lexical-Semantic Field.” *Vestnik of Saint Petersburg University. Asian and African Studies* 16(3): 604–612; published 28 December 2024; DOI 10.21638/spbu13.2024.308 — https://aasjournal.spbu.ru/article/download/20521/12582/76573 | paper | A | the author's analysis of shoe meanings in Iraqi dialect and Arab society | Introduction, printed p. 604 of publisher PDF: “For instance, a deliberate demonstration of the soles of shoes is considered indecent in Arab society;” | the paper states that deliberate display of shoe soles is considered indecent in Arab society | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

- Deliberately displaying shoe soles is considered indecent in Arab society. (S679)
- S679 | https://aasjournal.spbu.ru/article/download/20521/12582/76573 | 2026-10-23 | “For instance, a deliberate demonstration of the soles of shoes is considered indecent in Arab society;”

## Gates and exact evidence

### Source URL reuse check

Used `functions.grep` against `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md` with this host+path pattern:

```text
collections\.vam\.ac\.uk/item/O232311|collections\.vam\.ac\.uk/item/O482201|etnografskimuzej\.rs/en/zbirka/crafts|cplorg\.contentdm\.oclc\.org/digital/api/singleitem/collection/p4014coll10/id/836|news\.bbc\.co\.uk/2/hi/middle_east/7783325\.stm|aasjournal\.spbu\.rs/article/download/20521/12582/76573
```

Full output: `No matches found`. Thus no kept live URL host+path was found in the current registry.

### Quote locator commands and outputs

Each command below was run with the round-61 `reopen-quote.py`; the output and command exit are shown verbatim.

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://collections.vam.ac.uk/item/O232311/sandal-unknown/' "The epitome of luxury, these ornately worked toe-knob sandals, known as paduka, were one of the many often extravagant presents a bride might receive."; echo exit=$?
LOCATED https://collections.vam.ac.uk/item/O232311/sandal-unknown/
exit=0
```

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://collections.vam.ac.uk/item/O482201/ritual-object/' "These also have the knobs of sandals (paduka) protruding between the toes."; echo exit=$?
LOCATED https://collections.vam.ac.uk/item/O482201/ritual-object/
exit=0
```

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://etnografskimuzej.rs/en/zbirka/crafts/' "an opančar workshop (for making opanci—traditional leather footwear)"; echo exit=$?
LOCATED https://etnografskimuzej.rs/en/zbirka/crafts/
exit=0
```

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://cplorg.contentdm.oclc.org/digital/api/singleitem/collection/p4014coll10/id/836' "A pair of leather shoes, their soles are attached to the uppers with knotted leather thongs."; echo exit=$?
LOCATED https://cplorg.contentdm.oclc.org/digital/api/singleitem/collection/p4014coll10/id/836
exit=0
```

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'http://news.bbc.co.uk/2/hi/middle_east/7783325.stm' "In Arab culture it's considered rude even to display the sole of one's shoe to a fellow human being."; echo exit=$?
LOCATED http://news.bbc.co.uk/2/hi/middle_east/7783325.stm
exit=0
```

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://aasjournal.spbu.ru/article/download/20521/12582/76573' "For instance, a deliberate demonstration of the soles of shoes is considered indecent in Arab society;"; echo exit=$?
LOCATED https://aasjournal.spbu.ru/article/download/20521/12582/76573
exit=0
```

### PDF extraction provenance

The required direct-PDF route succeeded with `pypdf==5.4.0` under `uv run --no-project --quiet --with`; response was `application/pdf`, 1,001,970 bytes, prefix `%PDF-1.7`, nine pages. The located anchor is in the Introduction on printed p. 604. The earlier URL `/article/view/20521/12582` returned HTML rather than a PDF and pypdf raised `invalid pdf header: b'<!DOC'` / `PdfStreamError`; that failed attempt was not used as evidence.

Successful command:

```text
timeout 300 uv run --no-project --quiet --with pypdf==5.4.0 python3 -B -c 'import io, urllib.request, pypdf; u="https://aasjournal.spbu.ru/article/download/20521/12582/76573"; q=urllib.request.Request(u, headers={"User-Agent":"Mozilla/5.0"}); x=urllib.request.urlopen(q, timeout=60); d=x.read(); print("url", x.url, "content-type", x.headers.get("Content-Type"), "bytes", len(d), "prefix", repr(d[:8])); r=pypdf.PdfReader(io.BytesIO(d)); print("pages", len(r.pages)); print("\n".join((p.extract_text() or "") for p in r.pages))'
```

The first failed attempt used the same command pattern with `u="https://aasjournal.spbu.ru/article/view/20521/12582"`; pypdf failed because that URL returned HTML. No permanent tool installation/update was performed; `pypdf==5.4.0` was invoked via the required temporary `uv run` dependency route.

## Findings and access limits

- The Belgrade Ethnographic Museum page directly says its Crafts Collection includes an opančar workshop for making opanci—traditional leather footwear.
- The second opanci source is explicitly Cleveland Public Library's Folk Arts Collection, not an ethnographic museum; its official record supplies one pair's leather sole/upper construction. A second ethnographic-museum object record was not retained.
- The V&A O232311 gallery label supplies the toe-knob paduka / bride-gift statement. The separate V&A O482201 record identifies sandal knobs (paduka) protruding between the toes.
- The 2024 article's scope is the author's study of shoes in Arabic social and lexical contexts, with examples especially from Iraqi dialect; the entry draft only carries its scoped Arab-society sentence. The BBC article is a 2008 news account, not a scholarly survey.
- British Museum candidates were not retained: live collection reads returned HTTP 403. The Wayback availability request for `H_Eu1997-04-125-a-b` returned no snapshots. The availability request for paduka record `A_1993-0717-12` returned capture `20240601073009`, but the archive locator request returned `NOT_LOCATED ... HTTPError`, exit 1. Those challenges were met but not passed; no bypass was attempted.
- Other discarded leads: the Zagreb catalogue read failed certificate verification and its Wayback availability response had no snapshot; the Met collection API returned HTTP 410 and the Met collection page HTTP 429; the Royal Ontario Museum and Smithsonian pages returned HTTP 403. No source was taken from these failed reads.

## Touched surfaces, out of scope, and artifacts

- **Written by this seat:** this report only: `.ufo/waves/round-61/w1/ScribeSrc10.md`.
- **Not edited:** `corpus/SOURCES.md`, `corpus/README.md`, the new footwear entry, counters, lint tool, tests, or product code. Source rows, bullets, and Gate lines above are drafts for integration, not lane changes.
- **Not run:** ACCEPT-C/ACCEPT-O, builds, tests, lint, formatters, git/jj commands. No citations were added to the corpus and no claim-level result is asserted.
- **Other tools:** no tool installation/update. Source reading used `read`, the specified locator, `curl` for Wayback availability, and `uv run` with the mandated pypdf version. All invoked processes had `timeout` limits; the one automatically backgrounded pypdf attempt completed with its reported error, and no process remained.
- **Artifact path:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-61/w1/ScribeSrc10.md`.
