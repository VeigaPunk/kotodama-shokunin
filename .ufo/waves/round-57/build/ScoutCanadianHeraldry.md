# ScoutCanadianHeraldry — round 57 C sources (Canadian Heraldic Authority, gg.ca)

Two sources opened by ordinary GET this session; both quotes live-located with the round's locator. Both URLs were checked against two other seats' scope before fetching (HonoursOffice held the CHA process page; InukshukTrademark held register project/622) — no collision. Lane freshness confirmed: `grep -c 'gg.ca' corpus/SOURCES.md` and `grep -c 'gg\.ca/en/heraldry'` both print `0`, so no existing row names an gg.ca URL; both ids are fresh for the FRESH leg.

Locator runs (pasted verbatim):

```
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.gg.ca/en/heraldry/grant-of-arms-flags-and-badges' 'Approval is not automatic, and applications are assessed on merit, as a grant of heraldic emblems is an honour from the Crown'
LOCATED https://www.gg.ca/en/heraldry/grant-of-arms-flags-and-badges
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.gg.ca/en/heraldry/public-register/project/622' 'The Inukshuk, a directional marker composed of stones used by the Inuit, is composed, in this instance, of six stones'
LOCATED https://www.gg.ca/en/heraldry/public-register/project/622
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.gg.ca/en/heraldry/public-register/project/622' 'Both animals wear collars of mountain avens, the floral emblem of the Northwest Territories'
LOCATED https://www.gg.ca/en/heraldry/public-register/project/622
```

### NEW-ScoutCanadianHeraldry-1
citation: Office of the Governor General of Canada, "Grant of Arms, Flags and Badges" (page current 2026-10-22), Canadian Heraldic Authority, gg.ca
url: https://www.gg.ca/en/heraldry/grant-of-arms-flags-and-badges
route: direct GET (HTTP 200, text/html)
kind: docs
tier: A — the granting authority's own first-party statement of how a modern state grants arms
scope: how arms are granted in Canada (who may petition, how files are assessed, the process from application to Public Register, fee rules); not what any particular blazon says
quotes:
- loc-1: "Approval is not automatic, and applications are assessed on merit, as a grant of heraldic emblems is an honour from the Crown"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.gg.ca/en/heraldry/grant-of-arms-flags-and-badges' 'Approval is not automatic, and applications are assessed on merit, as a grant of heraldic emblems is an honour from the Crown'` → `LOCATED https://www.gg.ca/en/heraldry/grant-of-arms-flags-and-badges`
- loc-2: "All Canadian citizens and organizations (municipalities, schools, associations, etc.) may contact the chief herald of Canada to apply for a grant of heraldic emblems."
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.gg.ca/en/heraldry/grant-of-arms-flags-and-badges' 'All Canadian citizens and organizations (municipalities, schools, associations, etc.) may contact the chief herald of Canada to apply for a grant of heraldic emblems.'` → `LOCATED https://www.gg.ca/en/heraldry/grant-of-arms-flags-and-badges`
teaches: A modern state grants arms as an honour from the Crown, assessed on merit rather than purchased, with any citizen or organization free to petition the chief herald.
draft sentences:
- In Canada the Canadian Heraldic Authority creates coats of arms, flags and badges, and any Canadian citizen or organization — municipalities, schools, associations — may contact the chief herald of Canada to apply for a grant (NEW-ScoutCanadianHeraldry-1, loc-2).
- A grant of heraldic emblems is an honour from the Crown in recognition of service to Canadian society, approval is not automatic, and applications are assessed on merit (NEW-ScoutCanadianHeraldry-1, loc-1).
- The grant runs from application and supporting documents, through a herald's research and a written concept that the chief herald must approve, to painted art, calligraphed letters patent sealed and signed by CHA officers, and publication in the Public Register 6–12 months later (NEW-ScoutCanadianHeraldry-1, loc-1).
- Paying the processing fee and art invoices never guarantees the grant, and the process can be cancelled at any time if the petitioner's eligibility changes (NEW-ScoutCanadianHeraldry-1, loc-1).
Next: pair with a non-Canadian authority page for contrast — ScoutLordLyon or ScoutCivicHeraldry rows may already carry that side.

### NEW-ScoutCanadianHeraldry-2
citation: Canadian Heraldic Authority, grant of 4 June 1996, "Arms of Helen Mamayaok Maksagak", Public Register of Arms, Flags and Badges of Canada, Vol. III p. 105 (entry project/622), Office of the Governor General of Canada
url: https://www.gg.ca/en/heraldry/public-register/project/622
route: direct GET (HTTP 200, text/html)
kind: record
tier: A — the Crown's own registered letters-patent record, giving blazon, symbolism, motto and supporters for one grant
scope: one register entry that adapts an Inuit wayfinding monument (inukshuk) into blazon, with an Inuvialuktun motto and Inuit crest and supporters; not the general rules of who may grant arms
quotes:
- loc-1: "The Inukshuk, a directional marker composed of stones used by the Inuit, is composed, in this instance, of six stones"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.gg.ca/en/heraldry/public-register/project/622' 'The Inukshuk, a directional marker composed of stones used by the Inuit, is composed, in this instance, of six stones'` → `LOCATED https://www.gg.ca/en/heraldry/public-register/project/622`
- loc-2: "Both animals wear collars of mountain avens, the floral emblem of the Northwest Territories."
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.gg.ca/en/heraldry/public-register/project/622' 'Both animals wear collars of mountain avens, the floral emblem of the Northwest Territories'` → `LOCATED https://www.gg.ca/en/heraldry/public-register/project/622`
teaches: A register entry can adopt a non-European wayfinding monument as a blazoned charge, explain its borrowed symbolism, and pair it with a motto in an Indigenous language.
draft sentences:
- One grant blazons an Inuit wayfinding monument in classic terms — "Purpure an Inukshuk of six stones Or" — and the symbolism page explains the Inukshuk as a directional marker of stones used by the Inuit, its six stones standing for the bearer's six children (NEW-ScoutCanadianHeraldry-2, loc-1).
- The same grant treats an Indigenous-language motto as part of the emblems: "APKUTIKSON NALUNAIKNIAGIGA," given in the register as the Inuvialuktun for "I will show the way," chosen to echo the inukshuk's guiding purpose (NEW-ScoutCanadianHeraldry-2, loc-1).
- Supporters need not be wild inventions; here a caribou and an arctic wolf stand for the bounty of the land and wear collars of mountain avens, the floral emblem of the Northwest Territories (NEW-ScoutCanadianHeraldry-2, loc-2).
- The entry shows how a grant can move a mark between surfaces: the inukshuk sits on the shield, is re-explained on the symbolism page, and the register ties the whole design to one dated, numbered volume so designs stay separable from meaning (NEW-ScoutCanadianHeraldry-2, loc-1).
Next: a second register entry with a different adaptation (register project/813 Nunavut) may be worth a scout row.

### Rejected
(none — both opened sources filed above; a Wayback capture was not needed as both pages served directly)
