# ReopenS063 — attack on SOURCES row S063 (UNESCO ICH Cultural space of the Bedu in Petra and Wadi Rum, element 00122)

Seat: `KotodamaR50-2.ReopenS063-21` (leaf, read-only; no subagents, no background jobs).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All lane bytes below read with `git show <sha>:<path>`; the working tree was not used for landed claims.
No lane writes; the only file written is this report. No clone was needed (network reads only, `/tmp` files removed).
No tools installed — pacman is paused host-wide and nothing was needed.

## Verdict: **HOLDS**

The URL opens (browser-class UA, HTTP 200, 151,886 bytes); the Gate quote is verbatim in
**Description ¶2, sentence 2**; the live fetch is byte-identical to the hash the source seat pinned;
the row's three teachings are all supported (¶2 camel husbandry, ¶1 complementarity, ¶3 erosion);
tier A is honest for the row's stated scope under `corpus/QUALITY.md` criterion 6 because the scope
explicitly bounds the source to UNESCO's own inscription record and calls it "dated testimony, not
ethnography"; every `S063` citation in the knowledge entry is supported. Three non-breaking precision
notes and one adjacent entry-level under-citation follow the evidence. No fix is required.

## 1. Row and Gate as landed

Row — `corpus/SOURCES.md:92` (eleven registry fields, header at `corpus/SOURCES.md:28`):

```
| S063 | UNESCO ICH, Cultural space of the Bedu in Petra and Wadi Rum (element 00122) — https://ich.unesco.org/en/RL/cultural-space-of-the-bedu-in-petra-and-wadi-rum-00122 | docs | A | UNESCO's own inscribed description of the Bedu cultural space; dated testimony, not ethnography | Description ¶2 (opening Several Bedu tribes) | traditional pastoral culture and skills including camel husbandry; settled/nomadic complementarity; erosion of skills | mined | 2026-10-21 | 365d | corpus/knowledge/culture-material/pastoralism-animal-husbandry.md |
```

Gate bullet — `corpus/lessons/round-50.md:48`, under `## Gate` at `:27`:

```
- S063 — https://ich.unesco.org/en/RL/cultural-space-of-the-bedu-in-petra-and-wadi-rum-00122 — accessed 2026-10-21 — Description ¶2: "The Bedu communities inhabiting this area keep alive a traditional pastoral culture and related skills." Seat: SrcBedouin.
```

Cohort: S048–S069 sit contiguously at `corpus/SOURCES.md:77-98`, one row per id; `S063` and its URL each
occur once in the registry. Tiers recount A 16 / B 6, matching `reports/round-50/claims.json`. `S063`
is `mined`, its `used-by` names the entry, and `reports/round-50/validation.json` records `"S063": "ok"`.
The Gate's seat is not invented: `.ufo/waves/round-50/build/SrcBedouin.md` (source seat
`ChousaR27R2.SrcBedouin-4`, per `build-assignment-receipt.json:529-531` and `build-assignments.json:49`)
contains the candidate row with the same URL, anchor and a pinned sha256 (`SrcBedouin.md:15`).

## 2. URL re-opened this session

Live page, browser-class UA:

```
$ curl -sS -L --max-time 60 \
    -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36' \
    -H 'Accept-Language: en-US,en;q=0.9' -o /tmp/s063b.htm -w 'http=%{http_code} size=%{size_download} final=%{url_effective} type=%{content_type}\n' \
    'https://ich.unesco.org/en/RL/cultural-space-of-the-bedu-in-petra-and-wadi-rum-00122'
http=200 size=151886 final=https://ich.unesco.org/en/RL/cultural-space-of-the-bedu-in-petra-and-wadi-rum-00122 type=text/html; charset=UTF-8

$ sha256sum /tmp/s063b.htm
97652149c0b9553f61c88b5560618196d25d1e0df030685a30b500c0e1f54ae8  /tmp/s063b.htm
```

That hash is **exactly** the one pinned by the source seat at `.ufo/waves/round-50/build/SrcBedouin.md:15`
(`sha256 97652149c0b9553f61c88b5560618196d25d1e0df030685a30b500c0e1f54ae8`, same 151,886-byte size), so the
live page I read is byte-identical to the page the row was written from.

Route hazard (not disclosed in the Gate or row): the site's bot wall answers a default client
with HTTP 200 and a 47,758-byte TSPD_101 JavaScript challenge that contains none of the text:

```
$ curl -sS -L -m 45 -A 'curl/8' -o /tmp/s063.htm -w 'http=%{http_code} size=%{size_download}\n' '<same URL>'
http=200 size=47758
$ grep -c 'Bedu communities' /tmp/s063.htm
0
$ grep -o 'TSPD_101[^" ]*' /tmp/s063.htm | head -1
TSPD_10130000000cTSPD_101_DID...
```

The seat recorded the same split (`SrcBedouin.md:47-52`): its `read` on the exact URL returned the site's
CAPTCHA interstitial ("What code is in the image?", support ID 5619449045260564149), while a
browser-headered fetch returned HTTP 200, 151,886 bytes with no CAPTCHA marker. S062 and S064 disclose
their routes in the Gate; S063 does not (see precision note 2).

Independent second witness — Wayback capture `20250721082201` of the exact URL, fetched this session:

```
$ curl ... 'https://web.archive.org/web/20250721082201/https://ich.unesco.org/en/RL/cultural-space-of-the-bedu-in-petra-and-wadi-rum-00122'
http=200 size=142105
$ grep -c 'keep alive a traditional pastoral culture and related skills'   # 1
$ grep -c 'erosion of skills developed by the Bedu'                        # 1
$ grep -c 'complementary relationship of both types of communities'        # 3  (visible ¶1 + meta/og description)
```

The capture is ~15 months older than the live page and agrees on every quoted sentence, matching the
seat's own stability check (`SrcBedouin.md:53-56`).

Inscription line, live page: `Inscribed in 2008 (3.COM) on the Representative List of the Intangible
Cultural Heritage of Humanity (originally proclaimed in 2005)`.

Two structural observations: the page has **no literal "Description" heading** (`grep -i description`
over the visible text finds none; the block is the element-description lead under the title), so
"Description ¶2" is the corpus's label for the element-description block, the same convention S062 uses.
The credit lines below the text (`© Jordanian Commission for Oral and Intangible Cultural Heritage`,
three times) sit inside the photo slideshow markup and are **photo credits**, not text authorship.

## 3. Quote and location, paragraph by paragraph

The element description is three paragraphs. Extracted from the live page's own `<p>` elements:

- **¶1** — "The Bedu are settled and nomadic communities living in the southern part of Jordan, particularly near Petra and Wadi Rum… These conditions have allowed for the development and existence in complementary relationship of both types of communities."
- **¶2** (opens "Several Bedu tribes, namely the Bdul, the Ammarin and the Sa’idiyyin…"):
  - sentence 2: **"The Bedu communities inhabiting this area keep alive a traditional pastoral culture and related skills."**
  - sentence 3: "The Bedu of Petra and Wadi Rum have preserved specific knowledge related to the flora and fauna of the area, traditional medicine, camel husbandry, tent-making craftsmanship, and tracking and climbing skills."
- **¶3** — "Over the last fifty years, more and more Bedu groups have settled down… leading, however, to the erosion of skills developed by the Bedu over generations."

Exact-match checks against the extracted paragraphs:

```
gate exact in P2: True
'traditional pastoral culture and related skills' -> paras [2]
'camel husbandry' -> paras [2]
'complementary relationship of both types of communities' -> paras [1]
'the erosion of skills developed by the Bedu over generations' -> paras [3]
'settled and nomadic communities' -> paras [1]
```

The Gate quote is 15 words (within the seat's 25-word cap), verbatim including punctuation, and sits
in ¶2 — the paragraph the row names, whose opening the row's parenthetical correctly describes. The
Gate's "Description ¶2" location is therefore exact.

## 4. Tier and scope under QUALITY criterion 6

`corpus/QUALITY.md:29` (criterion 6) requires tier A to be "primary or authoritative for the exact scope",
with publisher descriptions/abstracts at B for substantive claims. The row's scope is "UNESCO's own
inscribed description of the Bedu cultural space; dated testimony, not ethnography". The source is the
Convention secretariat's own element record: authoritative for what the inscription says and for the
description text it publishes. The scope's second clause explicitly declines ethnographic authority, so
the A is not being used to launder the description into ethnography. The seat's own tier reasoning
(`SrcBedouin.md:63-79`) says the description is "a three-paragraph summary derived from a State Party
nomination", B-grade "for those substantive claims", and states the criterion-6 remedy would be a
superseding B row, never an in-place tier edit. The landed scope adopts the conservative bound. This is
honest under criterion 6; no tier correction is warranted.

The entry's two uses stay inside that bound: `:61` cites the phrase as a **named skill** (scare-quoted),
and `:189` cites the element for **living-practice status**, not for herd mechanics. Nothing in the entry
derives tenure, herd composition, transhumance, sharing or gender from this row.

## 5. Every S063 citation in `pastoralism-animal-husbandry.md`

`git grep -n 'S063'` at the landed commit finds three lines in the entry:

1. **`:7`** — "…S062 UNESCO Mongol ger element; **S063 UNESCO Bedu cultural space**; S064 ETCSL…" — registration summary; accurate (page title: "Cultural space of the Bedu in Petra and Wadi Rum").
2. **`:61`** — Camel row, Mobility and labour column: `caravan and long-range moves; "camel husbandry" as a named skill (S063)`. Supported: ¶2 sentence 3 names "camel husbandry" in the preserved-knowledge list, and the entry quotes the source's phrase. The preceding "caravan and long-range moves" clause is separated by the semicolon and is not attributed to S063; the page does not support it, and the entry does not claim it does.
3. **`:189`** — "**Living-practice flag.** Mongolian, Sámi, Maasai, Bedu, WoDaaBe and Tibetan herding are living practice (S058, S059, S063)." The Bedu clause is supported: the page is present-tense ("keep alive", "continue to use") and is an ICH Representative List inscription; ¶3's erosion/settlement notes qualify but do not negate a living tradition, and the row's "dated testimony" scope is the guard. The sentence as a whole is under-cited — see the adjacent finding below.

## 6. Adjacent finding (entry-level, not chargeable to S063)

`:189` lists six peoples but cites three rows: S058 (WoDaaBe), S059 (Sámi), S063 (Bedu). **Maasai**
appears nowhere else in the entry; **Tibetan** is not named again, but the yak row at `:63` cites S061
(FAO *The Yak*, Qinghai-Tibetan Plateau), which the flag does not cite; the Mongolian support at `:67`
is S060's "five snouts" emic term, which does not itself establish living-practice status. So three of
the six list items lack a citation in the sentence itself. Smallest fixes: cite S061 for Tibetan and
S060 for Mongolian if their contemporary accounts suffice, and either add a Maasai source row or drop
Maasai from the list. This is a claim-C coverage gap, not an S063 defect; S063's Bedu clause is sound.

## 7. Precision notes (non-breaking)

1. **Anchor vs teaches.** The anchor `Description ¶2 (opening Several Bedu tribes)` locates the Gate quote and the camel-husbandry sentence exactly, but the row's other two teachings are in **¶1** (settled/nomadic complementarity) and **¶3** (erosion of skills) of the same three-paragraph description. Under the SOURCES contract the Gate holds the row's URL, access date and verbatim quote, so the anchor is doing its job; the seat's candidate row used the same ¶2 anchor while drawing its teaches from ¶1/¶3, so this is convention-consistent. If a reader wants the anchor to locate every teaching, widen it to `Description ¶1–¶3 (quote ¶2)`. No change required.
2. **"Dated testimony" is undated in the row.** The page dates the record: proclaimed 2005, inscribed 2008 (3.COM). The row's scope could read `2005/2008 dated testimony, not ethnography`, which would make the criterion-6 bound self-contained. Relatedly, the Gate gives the access date but not the route; the source is reachable only with a browser-class UA (reader/default curl gets the CAPTCHA/TSPD wall). S062 and S064 disclose their Wayback/CAPTCHA routes; adding `via browser-headered fetch (reader returns CAPTCHA)` to the Gate bullet would make S063 reproducible the same way.
3. **No literal "Description" heading.** The label is the corpus's name for the element-description block (S062 uses it too), not a rendered section title; the ¶ numbering is nevertheless correct because the block is exactly three `<p>` paragraphs.

## 8. Unresolved

- The page's "Nomination file No. 00122" block is present but empty in the fetched HTML, so the State Party nomination itself was not opened; the description's derivation from that nomination is the source seat's statement (`SrcBedouin.md:194-195`), not something this session read directly. This does not affect the quote, location or the claim-scoped tier.
- The page's thesaurus tallies (Nomads 44, etc.) were not treated as evidence; the landing row does not use them.

## 9. Reproduction / cleanliness

Commands above were run read-only against the live URL, one Wayback capture and `git show` at the
landed commit. `/tmp/s063.htm`, `/tmp/s063b.htm`, `/tmp/s063-wb.htm`, `/tmp/s062.htm` and the three
`/tmp/r50-*.md` extracts were removed after the checks; no clone was created because none was needed.
No lane file was edited; no git/jj state was touched; no tools were installed or updated.
