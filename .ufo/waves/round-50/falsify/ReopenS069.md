# ReopenS069 — attack on SOURCES row S069 (UNESCO ICH 14.COM 10.B.2)

Lane: kotodama-shokunin, attack-only leaf seat. Corpus/claim bytes read at landed commit
`1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad2683`); the committed seat report was
read from the working tree and its Q4 line verified identical via `git show`.
Access date for live routes: 2026-10-21. Read-only; no installs, no repo writes beyond this file.

## Verdict

**HOLDS.** The row is registered once, the decision URL answers 200 with the Gate quote
byte-identical (one occurrence, sentence 4 of the summary description paragraph), the element
page sentence-1 anchor is byte-identical, tier A is used only inside the record scope the row
declares, `used-by` is complete, and the sole in-entry citation (`entry:49`) is supported.
Four advisory notes (A1–A4) are locator/hedge/adjacent-cell observations, none blocking.

## Item attacked

| artifact | location at landed commit |
|---|---|
| registry row | `corpus/SOURCES.md:98` (S069) |
| Gate bullet | `corpus/lessons/round-50.md:54` |
| entry citation | `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:49` (only citation; `:7`, `:9` are range mentions, not citations) |
| tier rule | `corpus/QUALITY.md:29` (criterion 6); tier definitions `corpus/SOURCES.md:14–22` |
| seat report | `.ufo/waves/round-50/build/SrcUnescoTranshumance.md` (committed; Q4 at "summary paragraph, sentence 4") |

## Observed facts

### 1. Row shape and values

`git -C … show 1c779e4…:corpus/SOURCES.md | sed -n '98p'` gives an 11-column row matching the
header at `SOURCES.md:28`:

- source: `UNESCO ICH, decision 14.COM 10.b.2 inscribing Transhumance, the seasonal droving of livestock (Austria, Greece, Italy, 2019; extended 2023 as element 01964) — https://ich.unesco.org/en/decisions/14.COM/10.B.2`
- kind `docs`; tier `A`
- scope: `the Committee's own inscription decision and element description; Representative List record, not a survey of transhumant practice`
- anchor: `decision text, sentence 4; element page https://ich.unesco.org/en/RL/transhumance-the-seasonal-droving-of-livestock-01964 sentence 1`
- teaches: `transhumance is the seasonal movement of people with their livestock between regions; horizontal (plain or plateau) and vertical (mountain) types`
- status `mined`; opened `2026-10-21`; recheck `365d`; used-by `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`

`grep -c '^| S069 '` over the landed `SOURCES.md` = **1**; S067/S068/S069 sit in order at
`:96–98`. The Gate bullet at `round-50.md:54` names the same URL, access date and quote, and
the seat `SrcUnescoTranshumance`.

### 2. Routes

Browser-UA fetch (the seat report documents this route; read-only, no login):

```
$ curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36' \
    'https://ich.unesco.org/en/decisions/14.COM/10.B.2'
STATUS:200 URL:https://ich.unesco.org/en/decisions/14.COM/10.B.2 SIZE:136309 CT:text/html; charset=UTF-8

$ curl -sSL -A '<same>' 'https://ich.unesco.org/en/RL/transhumance-the-seasonal-droving-of-livestock-01964'
STATUS:200 URL:https://ich.unesco.org/en/RL/transhumance-the-seasonal-droving-of-livestock-01964 SIZE:176400 CT:text/html; charset=UTF-8

$ curl -sSL -A '<same>' 'https://ich.unesco.org/en/RL/transhumance-the-seasonal-droving-of-livestock-01470'
STATUS:200 URL:https://ich.unesco.org/en/RL/transhumance-the-seasonal-droving-of-livestock-01964 SIZE:176400
```

The `-01470` slug is not a second element: it serves the `-01964` page (redirect; the seat
report recorded the same). Default curl UA hits the site's CAPTCHA interstitial: `STATUS:200
SIZE:44502`, `grep -c 'Two broad types'` = **0**, `captcha` ×2. The row's access is honest
under the documented browser-UA route; the Gate does not state the UA (A4).

### 3. Quote and location — exact

Python extraction of the rendered text, then byte comparison:

```
decision page, q4 = 'Two broad types of transhumance can be distinguished: horizontal transhumance, in plain or plateau regions; and vertical transhumance, typically in mountain regions.'
  exact present: True   count: 1
element page, q1 = 'Transhumance refers to the seasonal movement of people with their livestock between geographical or climatic regions.'
  exact present: True   count: 1
```

Raw-HTML check: q4 is a contiguous substring of `s069dec.html` and occurs once, inside the
visible summary paragraph, not in a meta tag (the `<META NAME="DESCRIPTION">` carries the
"Takes note that …" sentence instead). The Gate quote at `round-50.md:54` is identical to q4;
the row's anchor points to the same sentence.

Location: q4 is sentence 4 of the summary description paragraph under **"Decision of the
Intergovernmental Committee: 14.COM 10.B.2"**, immediately after *"In many cases, the herders’
families also travel with the livestock."* The preceding decision-body sentence is *"Takes note
that Austria, Greece and Italy have nominated … (No. 01470) …:"*, so counting the decision body
from its first sentence makes q4 sentence 5; counting the summary paragraph (the seat report's
own Gate line) makes it sentence 4. The integrated wording "decision text, sentence 4" is a
locator compression, not a quote defect (A1).

Context confirmed on the same page:

- `Takes note that Austria, Greece and Italy have nominated … (No. 01470) …`
- `Decides to inscribe Transhumance, the seasonal droving of livestock along migratory routes in the Mediterranean and in the Alps on the Representative List …`
- final paragraph: `encourages the submitting States Parties to work towards an extended nomination with Spain and any other interested States.` (rendered text; `encourages` is `<u>`-wrapped in the raw HTML) — this is the row's own primary URL supporting the word **extended**.

Element page record: `Inscription: 18.COM 8.b.14 Previous: 14.COM 10.b.2`; `Inscribed in 2023
( 18.COM )`; nomination file `No. 01964`. The 2023 decision `18.COM 8.B.14` (opened for this
check) lists ten States and records `(No. 01964)`, and `Decides to inscribe Transhumance, the
seasonal droving of livestock on the Representative List …`; its R.4 records `In 2018, Italy, Austria and Greece initiated the
nomination, leading to the inscription of the element in 2019.` The row's `(Austria, Greece,
Italy, 2019; extended 2023 as element 01964)` is supported; the 2023 act is formally an
inscription of the extended nomination, which is why the row's word "extended" is a
characterization, not the decision's verb (A4).

### 4. Tier and scope under QUALITY criterion 6

`QUALITY.md:29` reserves A for sources "primary or authoritative for the exact scope" and
demotes publisher descriptions/abstracts to B. The row's scope is explicitly the
**record** — "the Committee's own inscription decision and element description; Representative
List record, not a survey of transhumant practice". The decision is the Committee's adopted
text; the element page is UNESCO's own inscription record. The entry draws only a definition
from it, no ethnography, herd figures, tenure or regional case. A is scoped, not inflated.

Wording nuance, not a tier defect: the decision's summary description is the nominating States'
text that the Committee "takes note" of, not independent Committee analysis, and the element
page's summary sits in a `wiki-text` paragraph (the page class). The scope's operative
disclaimer is "record, not a survey", so the A assignment survives criterion 6; "the Committee's own …
element description" is loose about authorship, not about the scope of what is claimed.

### 5. Entry citation support (`entry:49`)

`git show …:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md | grep -n 'S069'`
→ `:7`, `:9`, `:49`. Lines 7 and 9 are the external-shelf list and the source-authority line
(range `S048–S069`); only line 49 is a citation:

```
| Transhumant | seasonal movement of people with their livestock; horizontal in plains or plateaus, vertical in mountains (S069) | two bases; the route is infrastructure | a herd party travels, households stay; herd splitting (S048) | route access is the exposure |
```

The `(S069)` cell is supported:

- element page sentence 1 → "seasonal movement of people with their livestock" (the page says
  "between geographical or climatic regions"; the cell omits that qualifier, and the row's
  `teaches` compresses it to "between regions", without changing the claim);
- decision sentence 4 → "horizontal … in plain or plateau regions; and vertical … typically in
  mountain regions".

The cell drops the source's hedge **"typically"** ("vertical in mountains"; the row's `teaches`
also writes "vertical (mountain) types"). This is an overgeneralization at the margin, not a
false claim, and the Gate quote preserves the hedge (A2).

### 6. used-by completeness and status

Tree-wide `git grep -n 'S069' 1c779e4… -- .` returns only `corpus/SOURCES.md:98`,
`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:49` (plus the Gate bullet at
`corpus/lessons/round-50.md:54` and the `S048–S069` range mentions at `entry:7`, `entry:9`,
`corpus/SOURCES.md:8`, `corpus/SOURCES.md:142`, `corpus/lessons/round-50.md:6`, `:29`, `:58`,
`:61`), and the falsify fixture
`.ufo/waves/round-50/build/ExecSepFixture.md:83`. No other knowledge file cites S069. The row's
`used-by` names the entry and nothing else; `status: mined` is correct. `opened: 2026-10-21`
matches the Gate access date.

## Advisory (author lane, not admission)

- **A1 — locator precision.** `SOURCES.md:98` and `round-50.md:54` say "decision text, sentence
  4"; the quoted sentence is sentence 4 of the **summary description paragraph**, and sentence
  5 if the preceding "Takes note …" is counted as the decision's first sentence. Smallest fix:
  restore the seat report's wording, `summary paragraph, sentence 4`, in both places.
- **A2 — dropped hedge.** The source says "vertical transhumance, **typically** in mountain
  regions"; `entry:49` and the row's `teaches` drop "typically". Smallest fix: `vertical,
  typically in mountains` / `vertical (mountain, typically)`.
- **A3 — adjacent cell, not an S069 citation defect.** The same table row's Labour cell says
  "a herd party travels, households stay". S069 itself says "In many cases, the herders’
  families also travel with the livestock." FAO S048 supports a permanent base — "Transhumant
  pastoralists often have a permanent homestead and base at which the older members of the
  community remain throughout the year" — so the cell is not unsupported, but "households
  stay" is too absolute for the family-travel case. Smallest clarity edit: `a herd party
  travels; a base is held (families may travel); herd splitting (S048)`.
- **A4 — name change and route.** The 2019 decision's inscribed title is "Transhumance, the
  seasonal droving of livestock along migratory routes in the Mediterranean and in the Alps"
  (No. 01470); the short title in the row is the 2023 element name (01964). The parenthetical
  covers the extension; optionally add the 2019 title or "renamed at extension". Separately,
  the browser-UA requirement is documented in the seat report but not in the Gate; a future
  reader using default curl sees a CAPTCHA 200, not a 403.

## Inference and unresolved gaps

- [INFERENCE] Tier A is defensible under criterion 6 because the row's scope narrows to the
  record and the entry draws only a definition; a reviewer who treats the UNESCO summary prose
  as secondary would demote it, but the row pre-empts that with "not a survey" and the entry
  stays inside the declared scope.
- [INFERENCE] The 2023 act is an inscription of an extended nomination (the element page's
  `Previous: 14.COM 10.b.2` plus the 2019 decision's "extended nomination" sentence); the word
  "extended" is therefore accurate, though the 2023 decision's operative verb is "inscribe".
- Unresolved: the element page's `wiki-text` summary may be secretariat prose distinct from
  the nominating States' filed description; the row's scope covers "record", so this does not
  change the verdict. `SOURCES-CONTRACT-v1.md` is not present in the lane tree at the landed
  commit (as the S068 seat also found), so row shape was checked against `SOURCES.md:14–22`
  and `:28` and QUALITY criterion 6 only.
- Not evaluated here: other S-rows, the entry's other citations, and the O/Ca claims. No lane
  file was edited; only this report was written.

## Confidence

High (observed): single registration, both URLs reachable under the documented route,
Gate quote byte-identical and unique, element sentence-1 anchor byte-identical, `used-by`
completeness, `status`/`opened` correctness, the sole in-entry citation supported.
Medium-high (judgement): tier A under the declared record scope; the "Committee's own"
authorship wording is a nuance, not a tier inflation.

Author-lane advice, not admission.
