# SrcBedouin — frontier source for claim C: UNESCO ICH Cultural space of the Bedu (element 00122)

Seat: ChousaR27R2.SrcBedouin-4, source seat, 2026-10-21. Assigned: open the UNESCO ICH
element for *Cultural space of the Bedu in Petra and Wadi Rum*, quote the located passage
tying herding to social life, and return one SOURCES candidate (URL, access date, kind,
tier + reason, scope, <=25-word verbatim quote with location, what it teaches the entry,
recheck cadence). Author-lane advice, never admission. The lane registry was not edited.

## Result

**Candidate row: L1-assigned id, next free as observed `>= S048`.** (S048 is already
proposed by `SrcUnescoGer.md` in this same wave; this seat proposes no fixed number.)
Paste-ready in `corpus/SOURCES.md` registry format:

| S0NN | UNESCO ICH, Cultural space of the Bedu in Petra and Wadi Rum (element 00122) — https://ich.unesco.org/en/RL/cultural-space-of-the-bedu-in-petra-and-wadi-rum-00122 | docs | A | UNESCO's own inscribed description of the Bedu cultural space of Petra and Wadi Rum — the pastoral-culture/camel-husbandry skill complex, the settled/nomadic complementarity, and the 2005 proclamation/2008 inscription record; scoped to what the page itself states, not to ethnographic herd management, tenure, transhumance or gender | Representative List element page, Description ¶2 (paragraph opening "Several Bedu tribes, namely the Bdul, the Ammarin and the Sa'idiyyin"); inscription block "Inscribed in 2008 (3.COM) … originally proclaimed in 2005"; accessed 2026-10-21 (HTTP 200, 151,886 bytes, sha256 `97652149c0b9553f61c88b5560618196d25d1e0df030685a30b500c0e1f54ae8`) | the page states the Bedu "keep alive a traditional pastoral culture and related skills", and in the same paragraph names "camel husbandry" among preserved skills and a "complex moral and social code" transmitted orally; ¶1 describes settled and nomadic communities as existing "in complementary relationship", and ¶3 records fifty years of settlement, "erosion of skills", and tourism demand for "authentic Bedu culture" — a curatorial summary that establishes the herding↔social-code coupling and the listing, not the mechanics of herd tenure, sharing, transhumance or gender | queued | 2026-10-21 | 365d | — |

At merge: flip `status → mined` and `used-by →
corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` once the entry actually
cites the row; log the old→new in `corpus/lessons/round-50.md` per the SOURCES contract.

## Quotes and location (verbatim, both checked against two independent fetches)

Primary quote, **15 words**:

> The Bedu communities inhabiting this area keep alive a traditional pastoral culture and related skills.

Co-located quote supplying the social half, **24 words** (same paragraph, three sentences later):

> The Bedu have developed an extensive knowledge of their environment and complex moral and social code, all of which is expressed and transmitted orally.

Location: element page → **Description, second paragraph** — the paragraph that opens
"Several Bedu tribes, namely the Bdul, the Ammarin and the Sa'idiyyin, continue to use the
Nabatean water-collecting cisterns and caves near Petra." Q1 is its second sentence, Q2 its
fifth. The same paragraph names the skill bundle exactly: "traditional medicine, camel
husbandry, tent-making craftsmanship, and tracking and climbing skills" (substring verified
verbatim). No single sentence under 25 words contains both herding and the social code, so
the two quotes are given separately at the same location; the tie is the paragraph's, and
that is the honest unit of evidence.

Surrounding located statements used below (all verbatim from the page):

- ¶1: "The Bedu are settled and nomadic communities living in the southern part of Jordan" (14 words), and the two types exist "in complementary relationship".
- ¶3: "Over the last fifty years, more and more Bedu groups have settled down." (13 words); settlement leads "to the erosion of skills developed by the Bedu over generations" (14 words); "The increase of desert tourism and its demand for “authentic Bedu culture” should not be allowed to further degrade the intangible heritage" (22 words).

## Access evidence (why the row can say what it says)

- `read` on the exact URL returned the site's CAPTCHA interstitial ("What code is in the
  image?", support ID 5619449045260564149) — no element text.
- A browser-headered fetch of the same URL returned **HTTP 200, 151,886 bytes**, no CAPTCHA
  marker (`grep -c 'What code is in the image\|Your support ID'` → 0), with the description
  paragraphs and the inscription block present. sha256 pinned in the row above. Paragraph
  boundaries confirmed from the page's own `<p>` elements, not from rendered line order.
- Independent stability control: Wayback capture `20250721082201` of the exact URL returned
  HTTP 200 (121,428 bytes raw, no CAPTCHA) and contains **both quotes verbatim**. A second
  capture tried, `20260922194222`, is itself the CAPTCHA page (48,411-byte download) and was not
  used. The two usable fetches are ~15 months apart and agree on the quoted text.
- Inscription line on the live page: "Inscribed in 2008 (3.COM) on the Representative List
  of the Intangible Cultural Heritage of Humanity (originally proclaimed in 2005)".
- Page metadata facet (optional, not part of the row's anchor): the element is indexed under
  UNESCO thesaurus terms including "Nomads" (tally 44), "Moral values" (67), "Social values"
  (21), "Technical skills" (193). Those numerals are list tallies, never frequency evidence.

## Tier reasoning (QUALITY criterion 6)

Tier **A scoped to** "UNESCO's own inscribed description and listing record". The publisher
is the Convention secretariat and the page is the authoritative record of its own inscription
(2008, 3.COM, Representative List; proclaimed 2005) and of its own description text. This is
not the round-49 publisher-blurb pattern (S034/S038/S039 → S044–S046): those described a
third-party work through a publisher abstract; here the scope *is* UNESCO's own record. It is
also the same call `SrcUnescoGer.md` made for S048 (Mongol Ger), so the entry will not carry
two tiers for one source type.

The narrow scope does the calibration work: the row is **not** authority for herd composition,
tenure, transhumance, sharing or gender. UNESCO's description is a three-paragraph summary
derived from a State Party nomination, so for those substantive claims it is at best B-grade
testimony and must be supplemented or marked `(to-verify)`. If a reviewer reads the scope as
substantive ethnography, the criterion-6 fix is a **superseding tier-B row, never an in-place
tier edit**. If L1 prefers the conservative filing now, the row drops to B with the same text
minus the inscription-record claim.

## What it teaches claim C's entry, by section (section numbers follow the hunting contract model)

1. **§1 register property — the herd as capital, the code as infrastructure.** The page's own
   paragraph couples pastoral skills with a "complex moral and social code" that is orally
   transmitted. Use it for the master claim that a pastoral register is not "people with
   animals" but a production system whose rules of access, inheritance and conduct are part
   of the means of production. ¶1's "complementary relationship" of settled and nomadic
   communities also blocks the ladder framing ("nomads → settled" as progress) at the top of
   the entry.
2. **§2 one-owner boundary — a regional case, not the comparative owner.** The page names one
   cultural space and three tribes (Bdul, Ammarin, Sa'idiyyin) near Petra and Wadi Rum. If a
   `civilizations/` file for the Bedu ever lands, it owns the regional specifics; this entry
   owns the comparative method and cites the case. The page must not be stretched into a Bedu
   ethnography.
3. **§3 production chain / §4 toolkit — the camel as mobile capital and the skill bundle.**
   "Camel husbandry" is named as one item in a preserved-skill list (flora/fauna knowledge,
   traditional medicine, tent-making, tracking, climbing). That is the page's real teaching
   for these sections: herding is a compound skill, not a single task, and it travels with
   tracking and a portable dwelling. For the dwelling logic, couple the S048 Ger row; this
   row supplies the herd-side link only.
4. **§5 seasonal round and mobility — the two poles, no schedule.** The page gives settled
   and nomadic as a complementary pair, and ¶3 gives the direction of travel (settlement).
   It gives **no** routes, distances, seasonal timing or pasture tenure. Use it for the
   continuum and the direction of change; write the round from other rows or `(to-verify)`.
5. **§6/§7 — only the existence of a social code, never its content.** The single social
   statement is "complex moral and social code". The page says nothing about sharing,
   demand-sharing, kill/ownership rules, bridewealth, inheritance, or the gender division of
   labour. Do not derive any of those from this row.
6. **§13 calibration bank — the listing is dated testimony, not a timeless present.** ¶3 is
   the page's own calibration: fifty years of settlement, skills eroding, tourism demand for
   "authentic Bedu culture" framed as a threat. The entry should carry this as a live
   calibration flag: do not write the Bedu case as an unchanged camel-nomad present, and do
   not adopt "authentic culture" as an analytic category — UNESCO puts it in scare quotes as
   a market demand. The description is also a 2005/2008 record; current prevalence needs a
   dated check.

**Cannot support (mark `(to-verify)` or cite elsewhere):** herd species mix or size, camel
breeds, grazing rights and pasture tenure, transhumance distance/seasonality, milk/blood/meat/
wool economy, bridewealth and livestock wealth, gender division of labour, sharing and
demand-sharing rules, tribal genealogy or segmentary structure, current demographic weight.

## Boundary inputs observed this session (for the entry's one-owner table)

- `corpus/knowledge/culture-material/agrarian-field-system-lexicon.md:62` — the agropastoral
  row already owns "fields + pasture + transhumance routes", the herd calendar and manure
  contracts. Cite; do not restate.
- `corpus/knowledge/culture-material/fire-fuel-light.md:37` — dried dung as fuel and the
  manure trade-off ("fuel-poor pastoral cultures pay for it in soil").
- `corpus/knowledge/linguistics/semantic-fields-lexicon-building.md:70` — pastoral wealth
  vocabulary (herd-age/colour/condition) indexes property systems; `:105` — the "steppe
  pastoral" culture-type bundle (herd wealth, clan, raid, pasture). The entry owns production
  facts; the field owns the lexicon.
- `corpus/knowledge/myth-symbol/animal-symbolism.md:73` — Nuer "cattle of money" (cattle as
  social idiom, bridewealth); `:110` — the Mongol five livestock as wealth-language. The
  symbol file owns the idiom; the entry owns the production system.
- `corpus/knowledge/civilizations/mongol.md:40` — mobile pastoralism coexists with urban
  production and documentary administration (anti-ladder caveat); `:131` — fur/wool/felt as
  distinct production chains with unequal access.
- Incidental mentions, **not** register owners: `corpus/knowledge/culture-material/writing-media-surface-economy.md:3`
  ("parchment consumes a herd over years") and `:138` (scriptorium "herd");
  `corpus/knowledge/myth-symbol/direction-symbolism.md:164` (highland herding micro-sketch);
  `corpus/knowledge/linguistics/phonetics-phonology.md:197` (whistled registers for
  long-distance herding); `corpus/knowledge/culture-material/music-instrument-lexicon.md:87`
  (Jabal, tents/livestock).

## Finding that affects claim C's `pastoral-unowned` before-check

Observed 2026-10-21 in the lane: `find corpus/knowledge -name '*.md' | wc -l` → **225**;
`ls corpus/knowledge/culture-material/*.md | wc -l` → **27**; pastoral/husbandry/herd
filename sweep → **0**. The before-state counts match `reports/round-50/claims.json`.

But the exact `pastoral-unowned` evidence command does **not** return 0:

```
grep -rniE '^- topic:.*(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/ | wc -l
→ 1
```

The hit is `corpus/knowledge/culture-material/writing-media-surface-economy.md:3`, whose topic
line contains "parchment consumes a herd over years" (the parchment production chain), with a
second incidental "herd" at `:138`. This is not a pastoral-register owner, but the probe's
`mode: "word"` does not exclude it: "herd" is a word there. As written, the probe cannot read
`0`, so C's before-check will fail or be reported as owner-present. L1 must either (a) exclude
that path and record the exclusion with its incidental context, (b) re-scope the evidence
command to terms that distinguish the register (`pastoral|husbandry|transhuman|livestock`)
while stating why "herd" alone was dropped, or (c) keep the hit and revise the before-check to
"no register owner; one incidental herd reference at writing-media:3". The claim narrative
("0 filename owners, 0 topic owners; existing mentions are cross-references in agrarian,
fire-fuel, semantic-fields, civilizations") also omits the incidental mentions listed above —
they do not change the gap, but the sweep statement should not claim zero mentions.

## Incidental lead (verified, deliberately not filed)

FAO, *Pastoralism in the new millennium* — chapter "Social and cultural institutions of
pastoralism", https://www.fao.org/4/Y2647E/y2647e08.htm, HTTP 200 (9,888 bytes), accessed
2026-10-21. Located under "SOCIAL STRUCTURES":

> The basis of pastoral organization almost everywhere in the world is the clan, a set of patrilineally related households

(19-word verbatim prefix; the full sentence runs to "…traced (in theory) to an apical
ancestor", 26 words, over the 25-word cap). It also contains a "ROLE OF WOMEN IN PASTORAL
SOCIETY" section stating that women are "typically responsible for milking and dairy
processing". Teaches §6 (clan/lineage as the pastoral social unit) and §7 (milking/dairy as a
gendered task), tier B (institutional synthesis, not primary ethnography; publication
metadata is not on this chapter page). Not filed because it is outside my assigned row and
another seat may already hold it; L1 can assign an id if it is still free.

## Confidence and unresolved

- Quote text, paragraph location and inscription line: **high** (live 200 fetch plus an
  independent 2025 capture, both verbatim; sha256 pinned).
- Tier call: **medium-high** — scope-dependent, argument stated above so L1 can overrule with
  a superseding row rather than an edit.
- Not opened: the page's "Nomination file No. 00122" block is present but empty in the
  fetched HTML (no document link resolved), so the State Party nomination file remains a lead;
  the live page was not re-fetched after the first successful capture; Al Sadu (the weaving
  element) was not opened because the assigned question was answered by this element.
- Unresolved for the entry: whether a `civilizations/` Bedu file will exist (none today), and
  which peer-reviewed row will carry the herd-tenure/sharing/gender mechanics this row cannot.

## Unrun checks

Lane validators (`reports/round-28/readme/sweep.py`, `reports/round-49/run-validation.py`)
were not run: source seat, no production edits. No entry was written and no registry row was
inserted; the row above is a candidate for L1. No tools installed or updated. No lane files
outside this report were written (fetches were read in `/tmp` only).
