# S931 / S932 / S933 — quote receipts (kotodama round 88, seat ScoutSources)

Access date for every live fetch: **2026-11-04**. No tool was installed for this seat; only
`curl`, `python3` (stdlib) and the lane's own read-only checkers were used.

## Extraction scope (stated per QUALITY 33)

- **S931 (Terrain)**: the article body only — the 41 `<p class="texte">` blocks of the OpenEdition
  page, each carrying the publisher's own `<span class="paranumber">N</span>` marker, numbered
  1..41 monotonically ascending. Locator = the publisher's paragraph number. Navigation,
  abstracts, figure captions and the reference list are outside the scope.
- **S932 / S933 (MacTutor)**: the article body only — the block sequence between the page's
  first body sentence and its `References` heading, split on block boundaries, numbered from 1
  in reading order. Page furniture (nav bar, sidebar, footer, `References`/`Additional Resources`
  blocks) is outside the scope. MacTutor pages carry no publisher paragraph numbers, so the
  locator is this seat's block index under the stated scope, not an article-asserted ordinal.

Every quote below is verbatim from the served body, ≤ 25 words, and was located exactly once.

| id | locator | words | hits in served body | quote |
|---|---|---|---|---|
| S931 | Terrain ¶7 | 14 | 1 | "All numerical notations fall into five basic typological categories, across two dimensions (fig. 1)." |
| S931 | Terrain ¶7 | 13 | 1 | "How are the signs formed and combined within any power of the base?" |
| S931 | Terrain ¶8 | 9 | 1 | "We may call these, respectively, intraexponential and interexponential principles." |
| S931 | Terrain ¶8 | 7 | 1 | "There are only three basic intraexponential principles." |
| S931 | Terrain ¶8 | 7 | 1 | "Similarly, there are only two interexponential principles." |
| S931 | Terrain ¶8 | 13 | 1 | "Cumulative systems are those where signs are repeated and added within each power" |
| S931 | Terrain ¶8 | 11 | 1 | "Multiplicative systems use two signs per power, which are multiplied together." |
| S931 | Terrain ¶9 | 15 | 1 | "Combining these two principles provides six possible types, of which one (multiplicative-positional) is logically excluded" |
| S931 | Terrain ¶9 | 13 | 1 | "because multiplicative systems express power through special power signs, not through place value" |
| S931 | Terrain ¶9 | 9 | 1 | "The Babylonian sexagesimal (base 60) numerals exemplify cumulative-positional notation" |
| S931 | Terrain ¶10 | 10 | 1 | "all known systems use these five principles, and no others" |
| S931 | Terrain ¶10 | 11 | 1 | "This avoids the teleological argument of Ifrah (1987) and Dehaene (1997)" |
| S931 | Terrain ¶10 | 9 | 1 | "it is evident that there is no perfect system" |
| S931 | Terrain ¶19 | 8 | 1 | "the early hieroglyphic numerals used in predynastic Egypt" |
| S931 | Terrain ¶19 | 2 | 1 | "are cumulative-additive" |
| S931 | Terrain ¶25 | 17 | 1 | "Cumulative-positional numeral systems are cross-culturally very rare, in fact the rarest of the five types described above." |
| S931 | Terrain ¶25 | 19 | 1 | "while this structure is excellent for manipulating numbers, it is among the least concise ways to write a number" |
| S931 | Terrain ¶25 | 15 | 1 | "Because numerical notation is, first and foremost, a system for numerical representation, not for computation" |
| S932 | MacTutor body ¶2 | 15 | 1 | "the Babylonians only had to learn two symbols to produce their base 60 positional system" |
| S932 | MacTutor body ¶3 | 23 | 1 | "the 59 numbers, which go into one of the places of the system, were built from a 'unit' symbol and a 'ten' symbol" |
| S932 | MacTutor body ¶10 | 19 | 1 | "A much more serious problem was the fact that there was no zero to put into an empty position." |
| S933 | MacTutor body ¶3 | 11 | 1 | "The Egyptians had a bases 10 system of hieroglyphs for numerals." |
| S933 | MacTutor body ¶3 | 20 | 1 | "separate symbols for one unit, one ten, one hundred, one thousand, one ten thousand, one hundred thousand, and one million" |
| S933 | MacTutor body ¶22 | 19 | 1 | "the hieratic numerals did not form a positional system so the particular numerals could be written in any order" |
| S933 | MacTutor body ¶22 | 12 | 1 | "The number 9999 had just 4 hieratic symbols instead of 36 hieroglyphs." |

## Durability re-check — the same quote in the archived capture of the same page

| id | locator | in served live body | in the same page's Wayback capture |
|---|---|---|---|
| S931 | Terrain ¶7 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶7 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶8 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶8 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶8 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶8 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶8 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶9 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶9 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶9 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶10 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶10 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶10 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶19 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶19 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶25 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶25 | yes (1 block) | yes (1 block) |
| S931 | Terrain ¶25 | yes (1 block) | yes (1 block) |
| S932 | MacTutor body ¶2 | yes (1 block) | yes (1 block) |
| S932 | MacTutor body ¶3 | yes (1 block) | yes (1 block) |
| S932 | MacTutor body ¶10 | yes (1 block) | yes (1 block) |
| S933 | MacTutor body ¶3 | yes (1 block) | yes (1 block) |
| S933 | MacTutor body ¶3 | yes (1 block) | yes (1 block) |
| S933 | MacTutor body ¶22 | yes (1 block) | yes (1 block) |
| S933 | MacTutor body ¶22 | yes (1 block) | yes (1 block) |

Capture manifest (sha256 over the bytes actually read):

| capture | bytes | sha256 |
|---|---|---|
| live `https://journals.openedition.org/terrain/17506?lang=en` — Anubis challenge page, challenge met, not passed | 5281 | `08b78577f65551e169a0d7d2ca0b17dff02b92401157f795b30fbcaff53e002d` |
| Wayback `20251211231049id_` of that same URL — the article body was read here | 190162 | `8477889773d7b61fd9cdc0bdb961f35955f454eaeab7949c4180a4891dad396f` |
| the 41 numbered body paragraphs extracted from `s931-terrain-wb.html` | 48755 | `9f031d00f703b5cda43f6a8483f1f9d5da9237e52c4114bdfb14ffbf3e7b1cb7` |
| CDX prefix listing for `journals.openedition.org/terrain/17506` (capture choice evidence) | 2829 | `a4202e4a038a6cde1f6286fcf4c3b942dc880131e89926e927fd7e2d0760e752` |
| live `https://mathshistory.st-andrews.ac.uk/HistTopics/Babylonian_numerals/` | 65959 | `ac4701fbcc05c878372e95f8c62334bd3d80f39c429844083bdbb9eb476f9d5f` |
| body text extracted from `s932-babylonian.html` | 14995 | `57551cddc0008edf1c24ced6f22f231470e5ee564e507cd54f41943d35172974` |
| Wayback `20200708131715id_` of the same MacTutor URL | 62852 | `ed38408061c08f05bd5f676fb2c25ba0337c0228d32e3f0bf15fb25c60501052` |
| live `https://mathshistory.st-andrews.ac.uk/HistTopics/Egyptian_numerals/` | 23397 | `5f6ef5ee12caca32f77c51673bb0ab17763d15ed6c6d0ee34a024d15a018d1b5` |
| body text extracted from `s933-egyptian.html` | 5325 | `033debbc3c814012e927577ab0e04d00e7d8a25649b5954b4492ffd91dfd6924` |
| Wayback `20200724192341id_` of the same MacTutor URL | 20186 | `0e95472bbeffdbd03b8ab0f88d097999741532263e63d35e840d254d9f60e3f1` |
