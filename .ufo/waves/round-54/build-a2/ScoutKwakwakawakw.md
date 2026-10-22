# ScoutKwakwakawakw — claim C source scout (Kwakwaka'wakw masks and masquerade)

Question asked: what may a masks-and-masquerade entry say, at admitted strength, about
a mask as a worn object, an embodied presence and a licensed voice, anchored in a
holding museum's own record and in the community's own institution? Two sources opened
by plain request in this session, both HTTP 200, no browser, no challenge, no login.
Access date for both: 2026-10-22.

Result: two rows drafted below, both usable at tier A within the scopes stated. One
structural finding for the reviewer: the two rows together carry *rights to wear and
display* and *the mask as a returned ancestor's presence*, but they do **not** carry
masquerade-society internal access rules. Do not let the entry imply they do (see
"Attacks and honest gaps", point 3).

## Source rows

### NEW-ScoutKwakwakawakw-1

- citation: U'mista Cultural Society (Alert Bay, British Columbia). "Potlatch" and "Our Masks Come Home", in *Living Tradition: The Kwakwaka'wakw Potlatch on the Northwest Coast*, virtual exhibit published with the Virtual Museum of Canada. Site footer: "© U'mista Cultural Society 2026". No DOI; page URLs below.
- url: https://umistapotlatch.ca/potlatch-eng.php (the file quoted); second page of the same exhibit read and used for locators: https://umistapotlatch.ca/nos_masques_come_home-our_masks_come_home-eng.php
- route: direct plain HTTP GET with curl, HTTP 200, no redirect, no cookie or login, no JavaScript execution (server-rendered PHP), no challenge of any kind. Both pages re-read from the saved bytes to check every quote character by character.
- kind: web (community-institution exhibit)
- tier: A — the U'mista Cultural Society is the Kwakwaka'wakw institution that holds the returned Potlatch Collection and writes here in its own voice about its own ceremony and its own repatriation. Not A outside Kwakwaka'wakw practice, and not A for the legal history and numbers the exhibit states without documentary citation.
- scope: what a potlatch transfers as a right (masks included), who may wear and display regalia, who watches and what they are paid for, and how the returned masks are held and displayed today.
- quotes:
  - Potlatch page, PURPOSES OF THE POTLATCH list, second bullet, third sub-item: "The right to wear, use, and display certain regalia and objects that indicate leadership"
  - Potlatch page, English Translation of Potlatch Means "To Give", third paragraph: "a time for showing the masks and dances owned by the Chief or host giving the potlatch"
  - Potlatch page, CONTEMPORARY POTLATCH, first paragraph: "They are witnesses who are “paid” with gifts for acknowledging a family’s inheritance"
  - Potlatch page, CONTEMPORARY POTLATCH, first paragraph (last sentence): "Families pass down the right to tell certain stories, sing certain songs, dance certain dances"
- teaches: a mask is a right a named family holds and exercises in public before paid witnesses, and the right to tell the story, sing the song or dance the dance is itself inherited rather than implied by having seen it.
- draft sentences:
  - Model the mask as a right held by a named family rather than as an object an individual owns: the exhibit files masks in the class of things a potlatch passes on as "The right to wear, use, and display certain regalia and objects that indicate leadership" (NEW-ScoutKwakwakawakw-1, Potlatch page, PURPOSES OF THE POTLATCH, second bullet, third sub-item).
  - Make public appearance the act that exercises the right: the potlatch is described as "a time for showing the masks and dances owned by the Chief or host giving the potlatch", so a mask never shown is an unexercised claim rather than a hidden treasure (NEW-ScoutKwakwakawakw-1, Potlatch page, English Translation of Potlatch Means "To Give", third paragraph).
  - Give the audience a formal job: guests are "witnesses who are “paid” with gifts for acknowledging a family’s inheritance", which makes attendance paid work and the guest list part of the family's proof (NEW-ScoutKwakwakawakw-1, Potlatch page, CONTEMPORARY POTLATCH, first paragraph).
  - Separate the right to show from the right to copy: "Families pass down the right to tell certain stories, sing certain songs, dance certain dances", so a figure may be lawful to see and still unlawful to reproduce (NEW-ScoutKwakwakawakw-1, Potlatch page, CONTEMPORARY POTLATCH, first paragraph, last sentence).
  - Decide who holds the object and who decides that: on the Our Masks Come Home page the society states that after repatriation each family decided where its regalia would be held, so custody runs through the family even when the building is a community institution (NEW-ScoutKwakwakawakw-1, Our Masks Come Home page, "Return of the Collection", third paragraph).
  - Let the display itself argue about use: the same page states that the returned objects were arranged more or less in potlatch order and are deliberately not in cases, so an institution can refuse the vitrine as a claim that these are working objects (NEW-ScoutKwakwakawakw-1, Our Masks Come Home page, film transcript, third text paragraph).

### NEW-ScoutKwakwakawakw-2

- citation: Museum of Anthropology at UBC, Vancouver. Collection Online record, object number A17140, title field as served: numeric entities (`&#100;&#97;&#9532;&#233;…`) that render as `da┼éda┼éagam┼é`, which is UTF-8 Kwak'wala text mis-decoded as cp1252; the record's own English gloss in parentheses is "(Transformation Mask)". Culture Kwakwaka'wakw; date made c. 1900–c. 1920, acquired by donation January 1973, Walter and Marianne Koerner Collection of First Nations Art. Internal item id (Mkey) 7073.
- url: https://collection-online.moa.ubc.ca/search/item?keywords=transformation+mask+Kwakwaka&row=1&tab=more (record tab "More information"; "Overview" tab of the same item: https://collection-online.moa.ubc.ca/search/item?keywords=transformation+mask+Kwakwaka&row=1). The site has no persistent per-object URL: `?mkey=7073`, `?id=7073` and `?itemid=7073` each return 200 with an empty result. Cite object number A17140 and Mkey 7073 as the stable identifiers; the URL is a search-position link that can drift when the index is rebuilt.
- route: direct plain HTTP GET with curl, HTTP 200, server-rendered HTML, no login, no JavaScript needed, no challenge. Quotes re-checked against the raw bytes of the saved page.
- kind: record (holding museum's catalogue record)
- tier: A for the object's own record fields (materials, mechanism, date, acquisition, object number) and for what the museum states this mask depicts; B inside the same fields wherever the record generalizes about Kwakwaka'wakw ceremony as a whole or reports a named scholar's suggestion, because that text is curatorial synthesis rather than the holding institution's observation.
- scope: how one transformation mask is built and opened, whom it depicts, when in the ceremonial year it appears, and what its opening is said to accomplish; not a general account of Kwakwaka'wakw masking.
- quotes:
  - "History of use", first paragraph: "Outer face opened by means of strings inside at the appropriate moment to reveal the inner character."
  - "History of use", first paragraph: "the deceased carrier of the ancestral name it represents, a high-ranking chief, comes back one last time to pass on his rights and privileges"
  - "History of use", first paragraph: "This particular Imas mask depicts the ancestor Nulis, who came down in the guise of a grizzly bear at Wakanukw"
  - "Physical description" field: "The mask splits down the centre and opens to expose another human/whale face."
- teaches: a transformation mask is a timed mechanism worn by a person standing in for a named ancestor, whose opening discloses a second character at the point where the ancestral name and its rights are handed on.
- draft sentences:
  - Build the reveal into the object rather than into stagecraft: the mask is "opened by means of strings inside at the appropriate moment to reveal the inner character", so the string run and the timing are the wearer's skill (NEW-ScoutKwakwakawakw-2, "History of use", first paragraph).
  - Make the second face a different being, not a mood: the record states that the opened outer face discloses a second mask and that the inner figure is typically a different character (NEW-ScoutKwakwakawakw-2, "History of use", first paragraph).
  - Tie the mask to a name in a line of descent: this one "depicts the ancestor Nulis, who came down in the guise of a grizzly bear at Wakanukw", and the record notes it is one of a series made for the carrier of the Nulis name, so each holder is equipped rather than each generation inventing (NEW-ScoutKwakwakawakw-2, "History of use" and "Narrative").
  - Put the mask at a transfer, not at a spectacle: it belongs to the opening of the Tseka, the winter ceremonial, when "the deceased carrier of the ancestral name it represents, a high-ranking chief, comes back one last time to pass on his rights and privileges" (NEW-ScoutKwakwakawakw-2, "History of use", first paragraph).
  - Record the mechanism as the object's biography: because "The mask splits down the centre and opens to expose another human/whale face", hinge material, cord run and patched paint date its use and its repairs (NEW-ScoutKwakwakawakw-2, "Physical description").
  - Treat the mask as an argument about a being with two states: the record's iconographic note says such masks expressed the dual nature of the mythological and supernatural beings they represent, so closed and open faces are one entity in two conditions, not a disguise and its removal (NEW-ScoutKwakwakawakw-2, "Iconographic meaning").

## Map: what each decision needs, and where it comes from

| Worldbuilding decision | What the opened material supports | Row |
|---|---|---|
| Who may make the mask | Nothing in these two rows. A17140's record carries no artist/maker field at all (the museum does name makers on other masks). | — |
| Who may wear it | Whoever holds the family right; masks are listed among the regalia a potlatch passes on. | 1 |
| Who may see it | Invited guests, who are witnesses paid to acknowledge the claim; returned objects are shown outside cases, in potlatch order. | 1 |
| What it is said to be | An ancestor (Imas) of a named line, shown in two states, worn at the moment that line's rights are handed on; also an expression of a being's dual nature. | 2 |
| When and where it appears | Opening of the Tseka, the winter ceremonial; at a potlatch, in processional order. | 2, 1 |
| What it licenses | Public exercise of a family's right to a name and to the dances, songs and stories that go with it. | 1 |
| What is restricted | Reuse: the right to tell the story, sing the song, dance the dance is itself inherited, so seeing does not license copying. Society-internal rules are not carried by these rows. | 1 |

## Attacks and honest gaps

1. **URL stability (row 2).** The MOA record has no permanent per-object link. The filing
   URL is a keyword-plus-row address and drifts if the collection is re-indexed; a
   recheck must search `transformation mask Kwakwaka` and match object number A17140 /
   Mkey 7073, not the row number. Recording the row number as if it were an accession
   address would be a silent provenance defect.
2. **Tier boundary inside row 2.** "History of use" and "Iconographic meaning" mix three
   voices: the museum's own description, statements attributed to Kwakwaka'wakw
   consultants (the record elsewhere cites "C. George, 1966" and "M. Jacobson, 1954"),
   and a named scholar's suggestion ("Fraser suggests..."). The scope line keeps the row
   at A for the object and its depiction, B for the generalizations. One sentence on the
   record — that transformation masks were "one of the most dramatic and colourful
   aspects of Kwakwaka'wakw ceremonial life, where they reached their highest
   development" — should not be used at all: it is evaluative museum prose with an
   evolutionist cadence, it supports no decision, and it is quoted here only so the L1
   can recognize and refuse it.
3. **Masquerade societies: not covered.** Neither filed row states candidacy, initiation,
   secrecy obligations, or who may enter a dancing society. One adjacent MOA record I
   read (a Hamatsa bird mask, "Worn by Hamats!a", used at a 1904 Gilford Island potlatch)
   names the wearer's society, but it is a third record and is not filed, so nothing in
   these rows may describe society-internal access rules. Either the entry states that
   its access material stops at family-held rights, or another seat files a row carrying
   the society dimension from the community's own public statement. Do not let this
   soften into generic "secret society" prose.
4. **Voice of row 1.** The exhibit is written in the first person plural by the U'mista
   Cultural Society; the film transcripts are Barbara Cranmer's films made for the
   society. That self-account is what makes it tier A, but it is a curated public
   account: it does not disclose restricted knowledge, and the entry must not read its
   silences as permissions.
5. **Orthography.** The exhibit marks stress in the name by underlining the two *a*'s in
   the HTML, so naive text extraction yields "Kwakw a k a 'wakw" with spaces. The quotes
   above avoid the name for that reason. If the entry needs a quote containing it, spell
   the name once in the entry's own orthography and say the source marks stress
   typographically, rather than reproducing the spacing. The MOA record's own title field
   is mojibake in the served HTML (see the citation line), so any entry must either
   write the Kwak'wala word correctly on its own authority and mark it (to-verify), or
   cite the object number alone. Do not reproduce the mojibake as if it were orthography.
6. **"Not in cases" is one institution's choice, not a rule.** The same A17140 record shows a
   Location field reading "Case 027": this mask sits in a display case at MOA. U'mista's
   uncased installation is a local argument about use, so the entry must not generalize
   it into a claim about how masks are kept.
7. **No joining.** Every quote is one contiguous run of its page at or under 25 words.
   The two MOA statements about Nulis sit in different fields ("History of use",
   "Narrative") and are given as separate citations in one sentence for that reason.

## Also read this session, not filed as rows

- https://www.umista.ca/pages/collection-history (HTTP 200): "The History of the Potlatch
  Collection" on the Cultural Centre's own site — the 1921 Dan Cranmer potlatch at
  Village Island, the 45 arrests, sentences suspended on surrender of regalia, the
  dispersal to Ottawa, Toronto, Heye in New York and the British Museum, and the returns
  that followed, the Royal Ontario Museum's coming last in 1988. Strongest community statement on confiscation and return chronology;
  a better row than row 1 for that chronology if a later round needs it, left unfiled
  here to stay inside the two-source bound.
- https://umistapotlatch.ca/intro-eng.php, `/notre_peuple-our_people-eng.php`,
  `/notre_terre-our_land-eng.php`, `/enseignants-education-eng.php` (all HTTP 200): same
  exhibit. "Ceremonial masks tell of our beginning and share our identity and where we
  come from" (Our People page) is usable as a community statement of identity if the
  entry wants that claim rather than the rights claim.

## unopened

- Smithsonian National Museum of the American Indian collection search and the
  Smithsonian Open Access API: `collections.si.edu/search/results.htm` returned HTTP 403
  and `api.si.edu/openaccess/api/v1.0/search` returned HTTP 403. Challenge met, not
  passed — I did not retry through a browser, a proxy or a Wayback copy. NMAI holds part
  of the Potlatch Collection, so this is the obvious next record source for a later
  round if a copy is reachable by ordinary means.
- `http://archive.umista.ca/masks_story/en/ht/index.html` ("The Story of the Masks",
  linked from the U'mista exhibits page): DNS does not resolve (curl error 6, host not
  found). The exhibit appears to be gone, not merely challenging.
- `https://nuyumbalees.com/` and `https://www.nuyumbalees.com/` (Nuyumbalees Cultural
  Centre, Cape Mudge, the other holder of returned Potlatch material): HTTP 503 on both,
  retried once; not opened.
- UBC MOA records A6373 (three-way opening) and A4497 (four-way opening, thunderbird to
  human face): opened and read, not filed, to stay inside the two-source bound. A
  typology of opening directions would need their own rows.
- No tool was installed or upgraded for this seat. Nothing written outside this report
  file.
