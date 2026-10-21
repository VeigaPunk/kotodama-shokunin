# ReopenS068 — attack on SOURCES row S068 (Yacobaccio 2021)

Lane: kotodama-shokunin, attack-only leaf seat. Bytes read at landed commit
`1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad2683`), never the working tree.
Access date for live routes: 2026-10-21. Read-only; no installs, no repo writes beyond this file.

## Verdict

**HOLDS.** The row is registered once, its bibliographic identity is confirmed by the
publisher's DOI metadata, the Gate quote is byte-identical to the article's Introduction ¶1,
the A tier is used only inside the scope the row itself declares, `used-by` is complete, and
both citations in the entry are supported by the passage. Three advisory notes (A1–A3) are
wording/route observations, none blocking.

## Item attacked

| artifact | location at landed commit |
|---|---|
| registry row | `corpus/SOURCES.md:97` (S068) |
| Gate bullet | `corpus/lessons/round-50.md:53` |
| entry citations | `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:7` (shelf list), `:65` (species table) |
| tier rule | `corpus/QUALITY.md:29` (criterion 6); `corpus/SOURCES.md:14–22` (tier definitions) |

## Observed facts

### 1. Row shape and values

`git -C … show 1c779e4…:corpus/SOURCES.md | sed -n '97p'` gives an 11-column row matching the
header at `SOURCES.md:28`:

- source: `Yacobaccio 2021, The domestication of South American camelids: a review, Animal Frontiers 11(3):43–51, doi 10.1093/af/vfaa065 — https://doi.org/10.1093/af/vfaa065 (full text PMC8214430)`
- kind `paper`; tier `A`; anchor `Introduction ¶1`
- scope: `the author's own synthesis of South-Andean camelid domestication evidence; reported site details are B`
- teaches: `camelids are the only domesticated ungulates of the Americas; the Andes sustained the only pre-Hispanic pastoral societies`
- status `mined`; opened `2026-10-21`; recheck `365d`; used-by `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`

### 2. Identity — Crossref CSL record for the DOI

```
$ curl -sS -L -H 'Accept: application/vnd.citationstyles.csl+json' https://doi.org/10.1093/af/vfaa065
CSL:200 https://api.crossref.org/v1/works/10.1093%2Faf%2Fvfaa065/transform
title            = The domestication of South American camelids: a review
container-title  = Animal Frontiers
volume = 11   issue = 3   page = 43-51   issued = 2021
author = Hugo D Yacobaccio (CONICET-Universidad de Buenos Aires)
DOI = 10.1093/af/vfaa065   type = journal-article   publisher = Oxford University Press
```

Every bibliographic element of the row's `source` cell matches. No second row registers the
same source: `grep -n -i 'yacobaccio\|vfaa065'` over the committed `SOURCES.md` returns only
line 97; row-id duplicate scan (`grep -o '^| S0[0-9][0-9] ' | sort | uniq -d`) is empty.

### 3. Route and location

```
$ curl -sS -L -w 'DOI_FINAL:%{http_code} %{url_effective}\n' https://doi.org/10.1093/af/vfaa065
DOI_FINAL:403 https://academic.oup.com/af/article/11/3/43/6306456
$ curl -sS -I https://academic.oup.com/af/article/11/3/43/6306456
HTTP/2 403
cf-mitigated: challenge
$ curl -sS -L -w 'PMC_FINAL:%{http_code} … size=%{size_download}\n' https://pmc.ncbi.nlm.nih.gov/articles/PMC8214430/
PMC_FINAL:200 … size=156344
```

The DOI redirect itself lands on the correct OUP article (`/af/article/11/3/43/6306456` —
volume 11, issue 3, first page 43); the publisher page is behind a Cloudflare challenge for
automated clients. The row names the PMC full-text route in the same cell, and the Gate bullet
names it as the access route (`accessed 2026-10-21 (full text PMC8214430)`), so the access
claim is honest rather than concealed. This is the same pattern as S050 in the same Gate
(PNAS DOI 403, PMC full text used).

PMC page metadata confirms it is the published article, not a preprint:
`Anim Front. 2021 Jun 19;11(3):43–51. doi: 10.1093/af/vfaa065`, PMCID PMC8214430, PMID 34158988,
title and author identical to Crossref.

### 4. Quote and anchor — exact

The raw PMC HTML has:

```
<h2 class="pmc_sec_title">Introduction</h2>
<p>South American camelids are the only domesticated ungulates in the Americas, and the Andean
region sustained the only pastoralist societies in the pre-Hispanic New World. South American
Camelids are composed by two genera and four species, …
```

so the sentence is the first paragraph under the Introduction heading (nothing intervenes; the
preceding `</ul></section>` closes the bulleted list from the previous section).

Byte comparison against `round-50.md:53`:

```
INTRO_P1_FIRST_SENT: 'South American camelids are the only domesticated ungulates in the Americas, and the Andean region sustained the only pastoralist societies in the pre-Hispanic New World.'
GATE_QUOTE      :    'South American camelids are the only domesticated ungulates in the Americas, and the Andean region sustained the only pastoralist societies in the pre-Hispanic New World.'
EXACT_EQUAL: True     LEN: 170 170
```

No ellipsis, no altered punctuation, 25 words.

### 5. Tier scope under QUALITY criterion 6

`QUALITY.md:29` requires authority to stay claim-scoped and reserves A for sources that are
"primary or authoritative for the exact scope". The row does that work itself: A is declared
for "the author's own synthesis", and reported site details are explicitly demoted to B. The
entry draws nothing site-specific from S068 — its only content citation is the Introduction
framing sentence at `entry:65`, which is exactly the author's own synthesis; the other mention
(`entry:7`) is a shelf enumeration ("S068 Yacobaccio 2021 (South American camelid
domestication)"), accurate as a label.

Contrast with S051 (`SOURCES.md:80`), the other review in the same round: it is tier B because
its anchor is the Abstract and its scope is "what Sherratt's thesis claims and this review's
three-region critique; not primary for Sherratt" — criterion 6's abstract rule. S068's quote is
the author's own Introduction text and its scope is that synthesis, so the A assignment is not
the S051 case.

### 6. Entry citation support (`entry:65`)

Cell: `Llama / alpaca | Andean puna; the only domesticated ungulates and pre-Hispanic pastoral
societies of the Americas (S068) | fibre, pack, meat | …`

- Uniqueness clause: supported verbatim by the quoted sentence ("the only domesticated
  ungulates in the Americas"; "the Andean region sustained the only pastoralist societies in
  the pre-Hispanic New World").
- "Andean puna": also supported by the article independently — "During pre-Hispanic times, the
  domestic llamas were circumscribed to the Andean regions of Perú, Bolivia, Chile, and
  Argentina, but alpacas had a more restricted habitat in the high and humid punas (bofedales)
  of Perú, Bolivia, and northern Chile."
- "Llama / alpaca" as the domestic camelids: supported — "two domestic (llamas Lama glama …
  and alpacas Lama pacos …)".

### 7. used-by completeness

Tree-wide `git grep -n 'S068' 1c779e4… -- .` returns exactly four lines: `SOURCES.md:97`,
`entry:7`, `entry:65`, `round-50.md:53`. The row's `used-by` names the entry and nothing else
cites S068, so `status: mined` is correct. `opened: 2026-10-21` matches the Gate access date.

## Advisory (author lane, not admission)

- **A1 — route.** The DOI URL 403s to automated readers today (Cloudflare `cf-mitigated:
  challenge`); the row's parenthetical PMC id makes this honest, but a future reader who strips
  the parenthetical will hit a wall. Cheapest hardening: make the full-text route explicit as
  S050 does in the Gate, e.g. append "PMC only (DOI behind Cloudflare)" to the row.
- **A2 — entry wording, not support.** `entry:65` compresses the quote and drops the region as
  grammatical subject, so the cell can be misparsed as "llama/alpaca are … pre-Hispanic
  pastoral societies". All propositions are supported, but the smallest clarity fix is:
  `Andean puna; the region held the only domesticated ungulates and the only pre-Hispanic
  pastoral societies of the Americas (S068)`.
- **A3 — adjacent, out of row scope.** The same table row's Products cell (`fibre, pack, meat`)
  carries no citation, and S068's full text contains "pack" but never "meat", "wool" or
  "fibre" (counts: pack 3, meat 0, wool 0, fibre 0, fiber 1 — the one "fiber" is palm-leaf rope).
  S068 cannot be read as backing that column. This is not an S068 citation defect (no marker on
  that cell), but if the table's single marker is read as row-wide, the products have no
  support in this row.

## Inference and unresolved gaps

- [INFERENCE] The PMC HTML is the publisher-deposited version of the OUP article (metadata match,
  OUP copyright line, identical volume/issue/pages); the OUP rendering itself was not readable,
  so "quote appears in the publisher's own HTML" is **unverified**, while "quote appears in the
  article's Introduction ¶1 as served by PMC8214430" is observed.
- [INFERENCE] Tier A is defensible under criterion 6 only because the row's scope narrows to
  "the author's own synthesis" and the entry cites nothing site-specific; a reviewer who reads
  any review as a "survey" (the B definition) would call it inflation. The row pre-empts that by
  demoting reported site details to B in the same cell, and the entry stays inside the A scope.
- `SOURCES-CONTRACT-v1.md`, named at `SOURCES.md:4`, is not present in the lane tree at the
  landed commit, so row-shape rules were checked against the `SOURCES.md` header (`:14–22`,
  `:28`) and QUALITY criterion 6 only.
- Unresolved: whether the publisher's OUP page carries the same sentence word-for-word; not
  reachable without defeating a bot challenge, and not required by the row, which names PMC.

## Confidence

High (observed): bibliographic identity, quote verbatim, Introduction ¶1 anchor, both entry
citations supported, single registration, `used-by` completeness, `status` correctness.
Medium-high (judgement): tier A — correct under the row's declared scope, contingent on reading
"the author's own synthesis" as primary for the claim it licenses.
