# ReopenS062 — attack on SOURCES row S062 (UNESCO ICH Mongol Ger, element 00872)

Seat: `KotodamaR50-2.ReopenS062-21` (leaf, read-only; no subagents, no background jobs).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All lane bytes below read with `git show <sha>:<path>` (no working-tree claim trusted). No lane writes;
the only file written is this report. No clone needed (network reads only, files kept in `/tmp` and removed
afterwards). No tools installed — pacman is paused host-wide, and nothing was needed.

## Verdict: **HOLDS**

The URL opens; the Gate quote is verbatim, and is literally the third sentence of the element-description
paragraph in **three** independent renders (2024 Wayback capture, 2026 Wayback capture, live page);
the two captures' description paragraph is byte-identical as the row claims; tier A is honest for the row's
stated scope under `corpus/QUALITY.md` criterion 6; and every S062 citation in the knowledge entry is
supported by what was read. Three non-breaking precision notes follow the evidence; no fix is required.

## 1. Row and Gate as landed

Row — `corpus/SOURCES.md:91` (11 registry fields, matching the header at `corpus/SOURCES.md:28-29`):

```
| S062 | UNESCO ICH, Traditional craftsmanship of the Mongol Ger and its associated customs (element 00872) — https://ich.unesco.org/en/RL/traditional-craftsmanship-of-the-mongol-ger-and-its-associated-customs-00872 (live page CAPTCHA; read via Wayback captures 20241219152138 and 20260103060250, byte-identical description) | docs | A | UNESCO's own inscription record and description of the ger; not pastoral ecology or herd management | Description paragraph, third sentence | the ger's portability as a derived requirement of the nomadic round; wool to felt as household processing | mined | 2026-10-21 | 365d | corpus/knowledge/culture-material/pastoralism-animal-husbandry.md |
```

Gate bullet — `corpus/lessons/round-50.md:47`:

> - S062 — https://ich.unesco.org/en/RL/traditional-craftsmanship-of-the-mongol-ger-and-its-associated-customs-00872 — accessed 2026-10-21 via Wayback 20260103060250 (live page CAPTCHA) — Description, third sentence: "It is light enough for nomads to carry; flexible enough to fold and pack; and sturdy enough to be dismantled and reassembled." Seat: SrcUnescoGer.

Cohort: S048–S069 sit contiguously at `corpus/SOURCES.md:77-98`, one row per id, `S062` occurs once in the
registry. The seat exists: `.ufo/waves/round-50/build/SrcUnescoGer.md` (source seat `ChousaR27R2.SrcUnescoGer-4`),
and `SrcUnescoGer` appears in `build-spec.json`/`build-dispatch.json`, so the Gate attribution is not invented.

## 2. URL re-opened this session (three routes)

```
$ curl -sS -L -m 60 -o ger-live.html -w 'HTTP %{http_code} final=%{url_effective} size=%{size_download}\n' \
    https://ich.unesco.org/en/RL/traditional-craftsmanship-of-the-mongol-ger-and-its-associated-customs-00872
HTTP 200 final=https://ich.unesco.org/en/RL/traditional-craftsmanship-of-the-mongol-ger-and-its-associated-customs-00872 size=47722

$ curl -sS -L -m 60 -o ger-2026.wb.gz -w 'HTTP %{http_code} size=%{size_download}\n' \
    'https://web.archive.org/web/20260103060250id_/https://ich.unesco.org/en/RL/traditional-craftsmanship-of-the-mongol-ger-and-its-associated-customs-00872'
HTTP 200 size=20222        # gzip; decompresses to 138081 bytes

$ curl -sS -L -m 60 -o ger-2024.html -w 'HTTP %{http_code} size=%{size_download}\n' \
    'https://web.archive.org/web/20241219152138id_/https://ich.unesco.org/en/RL/traditional-craftsmanship-of-the-mongol-ger-and-its-associated-customs-00872'
HTTP 200 size=117169
```

Both named capture timestamps are real and serve the exact URL:

```
$ curl -sS 'http://web.archive.org/cdx/search/cdx?url=ich.unesco.org/en/RL/traditional-craftsmanship-of-the-mongol-ger-and-its-associated-customs-00872&output=text&fl=timestamp,statuscode,digest,length&from=2024&to=2026'
20241219152138 200 T5H6IGCS6QFSBTCH4HPZG3RXATF733IX 20722
20260103060250 200 SSSWMEOXN2POEINOIUNLILGG7VIJHXGJ 21832
... (31 captures in the 2024→2026 slice; 111 captures total 20170510145323→20261010110819, matching the seat report)
```

(The fetch transcripts above are the commands as run; the session's output files were md5-named temp files,
renamed here for readability. The CDX and grep outputs are verbatim.)

Live page, default curl UA: the UNESCO anti-bot CAPTCHA interstitial — no element text, so the row's
"live page CAPTCHA" access note reproduces exactly:

```
$ grep -o -i "This question is for testing[^<]*\|support ID is:[^<]*\|captcha_audio" ger-live.html
This question is for testing whether you are a human visitor and to prevent automated spam submission.
support ID is: 5619449045258674156.
captcha_audio
$ grep -c "light enough for nomads to carry" ger-live.html
0
```

Live page, browser UA: HTTP 200, 153023 bytes, full element page (this is extra information beyond what the
row claims, see note N1):

```
$ curl -sS -m 60 -A 'Mozilla/5.0 ... Chrome/126.0 Safari/537.36' -o ger-live-ua.html -w 'HTTP %{http_code} size=%{size_download}\n' <row URL>
HTTP 200 size=153023
```

Inscription facts on the live page: `Inscribed in 2013 (8.COM) on the  Representative List of the Intangible
Cultural Heritage of Humanity` — element number `00872` appears 13 times, and the page title is
`Traditional craftsmanship of the Mongol Ger and its associated customs - UNESCO Intangible Cultural Heritage`.
The row's identity/`element 00872` claim is therefore correct.

## 3. Quote, location, and byte-identity — exact

Extracted the element-description paragraph (`<p class="wiki-text">` immediately after the
`Inscribed in 2013 (8.COM)…` line) from all three renders and compared:

```
                       raw <p> sha256                                                     normalized text sha256 / length
2024 capture   6bb66f99ba388029e5feb66cf6b5c72324a777f54b7d0ef6ee80d8aef4b2814e   d26bf0c0d9532bdf2e4198cd06b4b89d1511d854bbf34cfaf6e4d8abc7d54ae6  1245
2026 capture   6bb66f99ba388029e5feb66cf6b5c72324a777f54b7d0ef6ee80d8aef4b2814e   d26bf0c0d9532bdf2e4198cd06b4b89d1511d854bbf34cfaf6e4d8abc7d54ae6  1245
live (browser) 6bb66f99ba388029e5feb66cf6b5c72324a777f54b7d0ef6ee80d8aef4b2814e   d26bf0c0d9532bdf2e4198cd06b4b89d1511d854bbf34cfaf6e4d8abc7d54ae6  1245
```

So the row's "byte-identical description" is literally true, and the live page now agrees with both captures.

Sentence split of that paragraph (9 sentences):

1. "Craftsmanship of the Mongol Ger is a traditional enterprise involving the labour of a household or group, … felt-making."
2. "The Ger is a round structure of walls, poles and a peaked roof covered with canvas and felt, and tightened with ropes."
3. **"It is light enough for nomads to carry; flexible enough to fold and pack; and sturdy enough to be dismantled and reassembled."** ← Gate quote, exact equality (`sents[2] == Gate quote` → `True`)
4. "The Ger can withstand Mongolia’s fierce spring winds." …

The Gate quote occurs exactly once in each render (Python `str.count` of the full sentence → 1 in the 2024
capture, the 2026 capture and the live page) and matches the Gate bullet's string character-for-character
(ASCII `;` and `,`, no ellipsis, no reflow). Location claim "Description paragraph, third sentence" is exact
as to paragraph and sentence ordinal.

## 4. Tier and scope under QUALITY criterion 6

Criterion 6 (`corpus/QUALITY.md:29`): publisher descriptions/abstracts are tier B for substantive claims
*about a work*; tier A is reserved for sources primary or authoritative for the exact scope.

- The page is UNESCO's own element record for element 00872: it carries the inscription decision (8.COM),
  the 2013 Representative-List inscription, and the element description. For the row's scope — "UNESCO's own
  inscription record and description of the ger" — UNESCO is the publisher and the primary record, not a
  third-party blurb. This is the S057 contrast: S057 is a **B** publisher description *of a book*; S062 is the
  **primary record itself**.
- The scope does the calibration work the criterion asks for: "not pastoral ecology or herd management".
  The entry's only substantive S062 use (see §5) is the dwelling's portability, inside that scope. The seat
  report's own boundary list (`.ufo/waves/round-50/build/SrcUnescoGer.md`, "Cannot support") matches the page:
  it has no herd-management content (animals appear only as materials: sheep's wool, animal hair, "Leather" tag).
- The row's `teaches` items are supported: "portability as a derived requirement of the nomadic round" ←
  "It is light enough for nomads to carry" and "As a traditional dwelling, the Mongol Ger plays an important
  social and cultural role for nomadic families"; "wool to felt as household processing" ← "Cutting and
  preparing sheep’s wool, making felt, stitching canvas and preparing woodwork are usually communal
  endeavours" plus "the labour of a household or group".

Tier A stands for the stated scope. Note N2 records the one wording nuance.

## 5. Every S062 citation in the entry

`git grep -n 'S062' <sha> -- corpus/` returns exactly four hits: the registry row, two lines in the entry
(`:7`, `:47`), and the lesson bullet. Inside
`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`:

- `:7` — shelf bibliography: "S062 UNESCO Mongol ger element" inside the S048–S069 enumeration. Bibliographic,
  accurate (page title = "Traditional craftsmanship of the Mongol Ger and its associated customs").
- `:47` — typology table, Nomadic row, Settlement column:
  `| Nomadic | household and herd move on a forage cycle | portable dwelling — the ger is "light enough for nomads to carry" (S062) | … |`
  The quoted fragment is a verbatim substring of sentence 3, and "portable dwelling" is the plain reading of
  "As a traditional dwelling … for nomadic families" + "light enough for nomads to carry". Supported.

No other corpus file cites S062, so the row's `used-by` = `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`
is complete. The entry's C-claim acceptance predicate (S-id resolves to a row whose `used-by` names the entry)
also passes for S062 specifically: `rows['S062']` contains that path.

## 6. Non-breaking precision notes (no fix required)

- **N1 — "live page CAPTCHA" describes the tool-client route, not a permanent wall.** With a browser UA the
  live page returns HTTP 200 and the full element page, paragraph hash-identical to the captures. The row is
  still honest: the seat's client got the UNESCO CAPTCHA interstitial (support-ID text reproduced), and the
  quote really was read from the two captures. If a future round wants live corroboration, use a browser UA
  or the captures; no row change is owed (the registry's append-only rule would force a superseding row for a
  cosmetic note, disproportionate here).
- **N2 — "UNESCO's own … description" = publication attribution.** The description text is the nomination
  summary UNESCO publishes; the page does not attribute an author. The phrase is accurate as to publication
  and the scope already bars ethnography/ecology use, so tier A is not claimed for independent research. If a
  later claim tried to use S062 for pastoral ecology, the criterion-6 remedy is a superseding tier-B row (as
  the seat report itself states), never an in-place tier edit.
- **N3 — "Description" is a conventional label, not a printed heading.** Neither capture nor the live page has
  an `<h2>Description</h2>` (only `meta name="description"` / `og:description`); the paragraph is
  `<p class="wiki-text">` directly after the inscription line. "Description paragraph, third sentence" still
  identifies the text unambiguously and the ordinal is exact; anyone reopening the page lands on the same
  paragraph.

## 7. Verification status

No lane command was run that mutates state; no clone was created; `/tmp` fetches were removed. This report is
author-lane advice, not admission.
