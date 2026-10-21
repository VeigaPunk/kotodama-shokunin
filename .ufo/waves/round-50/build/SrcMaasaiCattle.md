# SrcMaasaiCattle — frontier source for claim C: UNESCO ICH Maasai element 01390

Seat: `ChousaR27R2.SrcMaasaiCattle-4` (scout, leaf; no delegation). Round 50, claim C
(coverage / pastoralism entry). Base `4ad26836552462d28a946ca3b067cab0b5ce3532`.
Read-only: no lane file edited, no clone, no patch, no git/jj mutation. Author-lane advice,
never admission.

## Assigned item

Open UNESCO ICH *Enkipaata, Eunoto and Olng'esherr* (Maasai, 2018) or an authoritative
page; quote a located passage; return one SOURCES candidate (URL, access date 2026-10-21,
kind, tier with reason, scope, ≤25-word verbatim quote with location, what it teaches the
entry and which section, recheck cadence).

Both the element record **and the nomination file it links** were opened. Two candidate rows
below; they are the same element but distinct documents. If L1 wants one row, take
**candidate B** (the nomination file) — it is the load-bearing source — and cite the element
page URL inline for inscription facts.

Registry state observed 2026-10-21: 47 rows, last id **S047** (`corpus/SOURCES.md:76`;
header `:28`, `## Registry` `:26`), no `S048`–`S050`. Sibling seats also propose S048+ (the
Ger seat, for one), so **do not paste by id until L1 assigns**; ids below are placeholders.

## Result — candidate A (assigned object): element page

| S0NN | UNESCO ICH, Enkipaata, Eunoto and Olng'esherr, three male rites of passage of the Maasai community (element 01390), Kenya — https://ich.unesco.org/en/USL/enkipaata-eunoto-and-olng-esherr-three-male-rites-of-passage-of-the-maasai-community-01390 | docs | A | UNESCO's own 2018 inscription record and description of the three Maasai male rites only — the rites as age-grade institutions, livestock rearing named as transmitted indigenous knowledge, and land-tenure reform plus climate change named as threats to cattle survival; not Maasai pastoral ecology, herd management, species mix, mobility, transhumance, bridewealth or diet | element page, description paragraph immediately after "Inscribed in 2018 (13.COM) on the List of Intangible Cultural Heritage in Need of Urgent Safeguarding"; live page read 2026-10-21, description paragraph sha256 `aacea760fbe2c8a28e367c0119ca913697e130950af568d8bc45777d274bf98a` byte-identical across two fetches | the rites induct boys to moranhood and morans to eldership, with Olng’esherr a meat-eating ceremony; livestock rearing is listed among the indigenous knowledge transmitted by the rites; decline is attributed to agriculture as a main income, land-tenure reform and climate change affecting the survival of cattle | queued | 2026-10-21 | 365d | — |

**Quote (18 words), element page, description paragraph, final sentence** (the sentence that
begins "However, while the rites still attract relatively sizeable crowds, the practice appears
to be rapidly declining due to the fast emergence of agriculture as a main source of income, …"):

> reforms of the land tenure system and the impact of climate change that affects the survival of cattle

Second located passage, same paragraph (12 words), for the institutions/transmission section:

> the transmission of indigenous knowledge, such as in relation to livestock rearing

Page metadata read in the same fetch: **Nomination file No. 01390**; "Inscribed in 2018
(13.COM) on the List of Intangible Cultural Heritage in Need of Urgent Safeguarding";
Decision "13.COM 10.a.5", Previous "11.COM 3.BUR 4"; periodic report submitted 15/12/2022,
next due 30/06/2027.

## Result — candidate B (linked primary document, recommended): nomination file

| S0NN | UNESCO ICH nomination file No. 01390, Kenya, Enkipaata, Eunoto and Olng’esherr, three male rites of passage of the Maasai community (13.COM, 2018), Word document — https://ich.unesco.org/doc/src/38964-EN.doc?v=1520351061 | docs | A | Kenya's own 2018 nomination assertions about the element and its viability only — cattle as the Maasai "lifeline", bulls given for the rite, a shift from a pastoral-based to an agricultural-based economy, communal-land subdivision and drought as threats; not independent ethnography of herd management, species mix, mobility or bridewealth | nomination file §2 "Need for urgent safeguarding", subsection "Sustainability and threats to the element"; fetched 2026-10-21, 212,992 bytes, document properties 15 pages / 8,726 words, converted to UTF-8 text (56,719 bytes) and the quoted span re-verified in the raw .doc bytes | the nomination states the Maasai lifeline depends on cattle and that households give bulls for the rites; it attributes declining enactment to a pastoral-to-agricultural economic shift, land-tenure change and subdivision of communal ritual sites, and drought-driven cattle loss | queued | 2026-10-21 | 365d | — |

**Quote (9 words), §2 "Need for urgent safeguarding" → "Sustainability and threats to the
element",** in the paragraph beginning "Exposure to the western lifestyles…":

> the lifeline of the Maasai is dependent on cattle

Other located passages in the same subsection (each verified verbatim, not part of the row's
single anchor quote):

- 14 words: "change in the lifestyle of the Maasai Community from a pastoral-based to agricultural-based economy"
- 15 words: "many Maasai used to give and are still willing to give a bull or two"
- 15 words: "The changing pattern of pastoral lifestyle continue to pose a great challenge to this practice"

## Access route — what was actually opened

Element page:

- URL as in candidate A, browser User-Agent: **HTTP 200, 161,188 bytes**, final URL
  identical; full description renders. The `…-01388` and `/en/RL/` guesses both redirected
  to the site root and are not the record — do not use them.
- Second fetch, same route/UA: HTTP 200, 161,188 bytes; description paragraph
  byte-identical (`aacea760…`, 1,257 chars, 203 words). Corruption control.
- Non-browser UA (`curl/8.9.1`): HTTP 200 but a 49,838-byte bot-management interstitial
  (`window["bobcmn"]`, `TSPD_101`), no description. A scripted re-verifier needs a browser
  UA or a browser.
- Wayback availability API: **timed out** (45 s, `curl: (28)`); no capture opened, none used.

Nomination file:

- `https://ich.unesco.org/doc/src/38964-EN.doc?v=1520351061` with browser UA: **HTTP 200,
  212,992 bytes**, `application/msword`; document properties: 15 pages, 8,726 words,
  created 2018-03-06; header: 13th session, Port-Louis, 26 Nov–1 Dec 2018, Nomination file
  No. 01390; doc sha256 `83063e65af7c857ce4719dc58b650bfdcc4b10b98c4e72ac8fbcf7db22cabe4d`.
- Converted read-only in `/tmp` with the host's LibreOffice 26.8.1.1 (`soffice --headless
  --convert-to txt`, temporary profile under `/tmp`); output 56,719 bytes, sha256
  `2b29319574295d329d5c83ec9bce66043afc1e7f390699a5d22823d2fcd59ebd`.
- Converter fidelity controlled by re-checking each quoted span with `strings -a` on the raw
  .doc (code-page 1252 text): every quote above returns exactly one raw hit. No install was
  needed or attempted.

## Tier reasoning (QUALITY criterion 6, `corpus/QUALITY.md:29`)

**A** for both, each scoped to the publisher's own record, because UNESCO is the primary
publisher of its list record and of the nomination it receives; neither is a third-party
publisher blurb (the round-49 S034/S038/S039 → S044–S046 failure mode). The scopes do the
calibration:

- Candidate A is authoritative for *the inscription record and UNESCO's description*.
- Candidate B is authoritative for *what Kenya's nomination asserts*, which is advocacy
  text, not measurement. The entry must attribute it ("the 2018 nomination states…") and
  must not present "livelihoods are shifting" as an independently measured trend.

Neither row is authority for herd composition, grazing, mobility, transhumance, bridewealth
or diet. The element page never uses *pastoral*, *nomad* or *herd* (observed counts 0 / 0 / 0;
*livestock* 1, *cattle* 1); the nomination file uses *pastoral* 2, *livestock* 2, *cattle* 3,
*herd* 0, *transhumance* 0. If a reviewer reads either scope as substantive ethnography, the
criterion-6 fix is a **superseding tier-B row**, never an in-place tier edit.

## What it teaches claim C's entry, by section

1. **§1 register property / institutions.** Livestock rearing is named as *transmitted
   indigenous knowledge* carried by age-grade rites (A), and the nomination states the
   community's lifeline depends on cattle (B). Production knowledge is institutional, taught
   through a curriculum, not only household apprenticeship — a pastoral culture can encode
   herd knowledge in initiation.
2. **§6 sharing/distribution + §8 ritual boundary.** Olng’esherr is "the meat-eating ceremony
   that marks the end of moranism and the beginning of eldership" (A), and households give "a
   bull or two for the practice of the element" (B). Herd product is converted into a status
   transition and into ritual finance — a design pattern (feast + beast donation as grade
   transition) bounded to what the documents state; distribution rules are not given.
3. **§7 gendered division of labour (bounded).** Rites are "mainly practised by young men …
   aged between fifteen and thirty, but women also undertake certain tasks" (A). Not a
   division-of-labour finding; do not inflate it.
4. **§13 calibration bank / change.** The dated pressure set: agriculture as a main income,
   land-tenure reform, subdivision of communal land, drought and cattle loss, a
   pastoral-to-agricultural shift (A + B). This is the anti-static-culture row: state the
   pressures and the date (2018), quote the attribution, never the magnitude — neither
   document measures "rapidly declining".
5. **§2 one-owner boundary.** The entry owns pastoral *production*; the rites are owned by
   `myth-symbol/ritual-liminality.md:29` (puberty → adult age-set member) and `:40`
   (status-elevation vs reversal). Cite, do not re-own the ritual analysis.

**Cannot support:** species mix, herd size, grazing rotation, pasture tenure, mobility or
transhumance, bridewealth, dairy/meat economy, the number or names of age sets, or the bare
claim "the Maasai are pastoralists" (candidate A never says it; candidate B says
"pastoral-based economy", which supports the *shift*, not a general ethnography). Both are
one State Party's submission about three rites, not ethnography of a herd economy.

## Optional third source — no sibling seat owns it

Opened this session as corroboration for a substantive Maasai row beside the UNESCO
documents. Propose only if the C author wants a peer-reviewed anchor.

- **McCabe, Leslie and DeLuca 2010**, "Adopting Cultivation to Remain Pastoralists: The
  Diversification of Maasai Livelihoods in Northern Tanzania", *Human Ecology* 38(3):321–334,
  doi `10.1007/s10745-010-9312-8`, PMID 21915157, PMCID `PMC3170717` (author manuscript,
  NIHMS313379) — https://pmc.ncbi.nlm.nih.gov/articles/PMC3170717/ — opened 2026-10-21,
  HTTP 200, 210,514 bytes.
- Quote (19 words), **"The People" section**, immediately before the three-institutions
  sentence:

  > all three Maasai groups practiced a form of pure pastoralism, based on the raising of cattle, goats, and sheep

- Also located in **"The Environmental Context"**: "This signifies an important shift for the
  'people of the cattle.'" (10 words) — the cattle idiom and its erosion in the authors' own
  analysis.
- Tier **B**, scope: the study area's historical species mix and "pure pastoralism" baseline,
  plus the study's own finding that cultivation was integrated *to remain pastoral*. Reason:
  the baseline sentences synthesize prior ethnography, and the study is single-site; strong
  secondary, never A for comparative claims. The title is itself the anti-essentialism
  calibration ("remain pastoralists", not "stop being pastoralists").
- Recheck 365d; the deposit is an author manuscript — wording may differ from the version of
  record.

## Boundary inputs observed this session (for the entry's one-owner table)

- `corpus/knowledge/culture-material/agrarian-field-system-lexicon.md:62` — the agropastoral
  row already owns "fields + pasture + transhumance routes"; mixed systems stay there.
- `corpus/knowledge/linguistics/semantic-fields-lexicon-building.md:70` — pastoral wealth
  vocabulary (herd-age, colour, condition) indexes property systems; `:105` the "steppe
  pastoral" culture-type bundle. The entry owns production facts; the field owns the lexicon.
- `corpus/knowledge/myth-symbol/animal-symbolism.md:73` — Nuer "cattle of money", cattle as
  social idiom, not primarily food; `:110` decide the culture's idiom of value. Do not re-own
  animal symbolism.
- `corpus/knowledge/culture-material/trade-economy-lexicon.md:69-70` — *pecūnia* < *pecus*,
  "wealth counted by heads"; cite, do not re-own the etymology.
- `corpus/knowledge/myth-symbol/ritual-liminality.md:29` (puberty rite → adult age-set member),
  `:40` (status elevation vs reversal) — owns the age-set ritual theory.
- `corpus/knowledge/culture-material/adornment-body-codes.md:18` — Maasai bead composition
  encoding age-set, clan and community (Spencer 1988); the adornment entry owns that register.
- `corpus/knowledge/myth-symbol/color-symbolism.md:84` — Maasai red ochre at the eunoto; the
  colour entry owns the substance symbolism.
- `corpus/knowledge/civilizations/zimbabwe-shona.md:163` — the anti-pastiche rule ("Do not
  assemble 'African costume' from unrelated … Maasai cloth …"); cite it when the entry uses
  Maasai material as a worked case.

## Gap-premise re-measure (for the C author)

Measured 2026-10-21 from the lane root:

- `find corpus/knowledge -name '*.md' | wc -l` → **225**; `ls corpus/knowledge/culture-material/*.md | wc -l` → **27**.
- filename sweeps `*pastoral*`, `*husband*`, `*herd*` → **0** each.
- **Flag on the claims.json `pastoral-unowned` before-check**: the literal command
  `grep -rniE '^- topic:.*(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/`
  returns **one hit** — `corpus/knowledge/culture-material/writing-media-surface-economy.md:3`
  ("parchment consumes a herd over years", a cost example in the surface-economy topic line).
  It is not a pastoral owner, but the check as written cannot honestly report "0 hits". The
  model entry handled the same situation by citing its partial hits and explaining them
  (`hunting-foraging-subsistence.md:5`: "2 hits, both partial owners, not this register").
  The C author/verifier should do the same rather than claim an empty sweep.

## Duplicate-avoidance note

`build-assignments.json` lists sibling seats **SrcFaoPastoralism** and
**SrcUnescoTranshumance**; their pages (`fao.org/pastoralist-knowledge-hub`,
`ich.unesco.org/en/RL/transhumance-…-01964`) were opened here only as register context and
are **not** proposed as rows — do not double-register them. The Ger seat proposes its own
S048; id assignment stays with L1.

## Confidence and unresolved

- Quotes, locations, inscription metadata, converter-to-raw-byte agreement: **high**.
- Tier calls: **medium-high** — both A's are narrow and argued; L1 can overrule with a
  superseding row, not an edit.
- Coverage contribution: **medium-high** with candidate B included — institutions,
  transmission, cattle-as-lifeline, ritual finance, and a dated pressure set; still silent on
  herd ecology, species mix, mobility and tenure rules. The entry needs the sibling pastoral
  rows for those.
- Unresolved: whether the live element page differs from the text read (only same-client
  fetches, no independent archive — Wayback API timed out); the nomination file's complete
  text was not audited beyond the quoted sections; the "rapidly declining" clause has no
  measurement behind it in either document.

## Unrun checks / bounds honoured

- No lane gate run (`reports/round-28/readme/sweep.py`, `reports/round-49/run-validation.py`)
  — source seat, no production edits.
- No install attempted or needed (host pacman paused; nothing to record); LibreOffice was
  already present and used read-only on a `/tmp` copy.
- No `git add`/`commit`/`checkout`/`reset`, no jj command, no fleet-repo write; only this
  report written under the lane's `.ufo/waves/round-50/build/`.
