# ScoutFlagDesign — round 57, flags as designed identity marks

Scout seat `KotodamaR57.ScoutFlagDesign`. Assigned item: flags as designed identity marks — NAVA
"Good Flag, Bad Flag" (Ted Kaye) five principles + one official flag-law / flag-protocol page.

## Findings (observed)

- **NAVA booklet.** `nava.org/gfbf` (short link) currently serves a 404 on the rebuilt site
  (checked with the locator UA). The booklet's official electronic edition is captured by Wayback at
  `web.archive.org/web/20010723223146/...` (page 3: the five principles) and
  `web.archive.org/web/20010722170222/...` (page 2: purpose, history, the heraldry tie). All quotes
  below were verified by the round-57 locator against those captures. `nava.org` and `gfbf` appear
  nowhere in `corpus/SOURCES.md` (grep counts 0).
- **Official flag-law page.** United States Code (2024 ed.), 4 U.S.C. §§ 1 and 8, served by the U.S.
  Government Publishing Office on `govinfo.gov` (direct HTTP 200, ordinary GET). § 1 is the statutory
  flag design; § 8 is the respect/protocol law. `govinfo.gov/content/pkg/USCODE-2024-title4/...`
  appears nowhere in `corpus/SOURCES.md` (grep counts 0 for both sec1 and sec8 URLs).
- **Locator route note.** `urllib` gets `Connection refused` for `https://web.archive.org/...` from
  this host while `http://web.archive.org/...` serves the captures; the Wayback URLs are therefore
  reported in their `http://` form, which the locator fetches (verified: every quote line below
  LOCATED with that exact URL). https URLs (govinfo) fetched directly.
- No tools installed; no installs to record. No lane file touched other than this report.

## NEW-ScoutFlagDesign-1

citation: North American Vexillological Association / Ted Kaye, 2001, "Good Flag, Bad Flag — How to
Design a Great Flag" (electronic booklet edition; ©2001 NAVA), nava.org/gfbf (archived).
url: http://web.archive.org/web/20010723223146if_/http://www.nava.org/gfbf/gfbf-3.htm
route: Wayback capture id 20010723223146 (page 2 of the same booklet: capture id 20010722170222)
kind: web (association booklet)
tier: A — the assigned primary source; official NAVA text, stable archived copy, all quotes located.
scope: The five basic principles of flag design; a flag's purpose; the historical link from flags to
heraldry; what marks are put on flags and how they pass between bearers (royal houses → countries →
groups).
quotes:
- LF1: "The flag should be so simple that a child can draw it from memory"
  LOCATED http://web.archive.org/web/20010723223146if_/http://www.nava.org/gfbf/gfbf-3.htm
- LF2: "Limit the number of colors on the flag to three, which contrast well and come from the standard color set"
  LOCATED http://web.archive.org/web/20010723223146if_/http://www.nava.org/gfbf/gfbf-3.htm
- LF3: "Avoid duplicating other flags, but use similarities to show connections"
  LOCATED http://web.archive.org/web/20010723223146if_/http://www.nava.org/gfbf/gfbf-3.htm
- LF4: "Never use writing of any kind or an organization's seal"
  LOCATED http://web.archive.org/web/20010723223146if_/http://www.nava.org/gfbf/gfbf-3.htm
- LF5: "Flags began thousands of years ago, first used for military purposes on land and then as identifying signals at sea"
  LOCATED http://web.archive.org/web/20010722170222if_/http://www.nava.org/gfbf/gfbf-2.htm
- LF6: "They evolved to represent royal houses, then countries and other levels of government, businesses, military ranks and units, sport teams, and political parties"
  LOCATED http://web.archive.org/web/20010722170222if_/http://www.nava.org/gfbf/gfbf-2.htm
- LF7: "Flags grew out of heraldry the practice of designing coats of arms and follow many of the same design principles"
  LOCATED http://web.archive.org/web/20010722170222if_/http://www.nava.org/gfbf/gfbf-2.htm
- LF8: "A flag's purpose is to represent a place, organization, or person, generally on a rectangular piece of cloth"
  LOCATED http://web.archive.org/web/20010722170222if_/http://www.nava.org/gfbf/gfbf-2.htm
teaches: The NAVA booklet's five principles give worldbuilders a working design grammar for flags, from simplicity to meaningful symbolism.
draft sentences:
- A flag's purpose is to represent a place, organization, or person on a rectangular piece of cloth meant to be seen at a distance and reproduced in quantity (NEW-ScoutFlagDesign-1, LF8).
- The first principle of flag design is that a flag should be so simple that a child can draw it from memory (NEW-ScoutFlagDesign-1, LF1).
- Use two or three basic colors that contrast well and come from the standard color set (NEW-ScoutFlagDesign-1, LF2).
- Never use writing of any kind or an organization's seal on a flag (NEW-ScoutFlagDesign-1, LF4).
- Flags should avoid duplicating other flags, but may use similarities to show connections (NEW-ScoutFlagDesign-1, LF3).
- Flags began as military and sea signals and evolved to represent royal houses, then countries and other organizations (NEW-ScoutFlagDesign-1, LF5).
- Flags grew out of heraldry, the practice of designing coats of arms, and follow many of the same design principles (NEW-ScoutFlagDesign-1, LF7).

## NEW-ScoutFlagDesign-2

citation: Office of the Law Revision Counsel / U.S. Government Publishing Office, 2024, United States
Code Title 4, Chapter 1, §§ 1 and 8 (2024 edition), govinfo.gov.
url: https://www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec1.htm
route: direct, HTTP 200
kind: record (official statute)
tier: A — primary, official legal text; the assigned official flag-law page; every quote located.
scope: Statutory description of the national flag's design (stripes, union, stars); protocol rules for
display and handling (dipping, union down, touching); who may dip what flag.
quotes:
- LG1: "The flag of the United States shall be thirteen horizontal stripes, alternate red and white; and the union of the flag shall be forty-eight stars, white in a blue field."
  LOCATED https://www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec1.htm
- LG2: "No disrespect should be shown to the flag of the United States of America; the flag should not be dipped to any person or thing."
  LOCATED https://www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec8.htm
- LG3: "The flag should never be displayed with the union down, except as a signal of dire distress in instances of extreme danger to life or property."
  LOCATED https://www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec8.htm
- LG4: "Regimental colors, State flags, and organization or institutional flags are to be dipped as a mark of honor."
  LOCATED https://www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec8.htm
- LG5: "The flag should never touch anything beneath it, such as the ground, the floor, water, or merchandise."
  LOCATED https://www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec8.htm
teaches: An official flag law fixes a flag's design and handling rules, showing how a state codifies its identity mark.
draft sentences:
- By law, the flag of the United States is thirteen horizontal stripes, alternate red and white, with a union of stars in a blue field (NEW-ScoutFlagDesign-2, LG1).
- The statute, enacted in 1947, specifies forty-eight stars, white, in the blue field — the codified design (NEW-ScoutFlagDesign-2, LG1).
- The national flag is never dipped to any person or thing; state and institutional flags are dipped as a mark of honor (NEW-ScoutFlagDesign-2, LG2).
- The flag should never be displayed with the union down except as a signal of dire distress (NEW-ScoutFlagDesign-2, LG3).
- The flag should never touch anything beneath it, such as the ground, the floor, water, or merchandise (NEW-ScoutFlagDesign-2, LG5).

## Rejected

- Cabinet Office of Japan, National Flag & National Anthem page (https://www.cao.go.jp/en/flag_anthem.html):
  opened; both candidate quotes located. Not registered because the assignment's official-page slot is
  taken by the U.S. flag law (4 U.S.C. §§ 1, 8) as the stronger "flag-law" page. Offered to the L1 as
  a ready fallback or later row: ratio height:width 2:3; red disc centered; diameter three-fifths of
  height; white base; deep red disc.
- Japan Law Translation (www.japaneselawtranslation.go.jp) law-id probes (3197, 3272, 2814): served
  other laws (Hotel Business Act, Stimulants Control Act); no flag-act English text there.
- e-Gov (elaws.e-gov.go.jp) document?lawid=411AC0000000167: current live page is a JavaScript shell
  (no text served); a Wayback capture of it served a different law — not usable.
- Wayback https URLs for the gfbf captures: `urllib` gets Connection refused on
  https://web.archive.org/ from here; the http:// form serves the same captures and is LOCATED (used
  above). Route note, not a source rejection.

## Handoff notes for the L1

- Row 1 (`NEW-ScoutFlagDesign-1`) uses two URLs of the same booklet: the five-principles page
  (gfbf-3.htm) and the purpose/history page (gfbf-2.htm). For the LOCATE leg, put both URLs in the
  row's source cell (at most four allowed; tried in order) so any anchor quote among LF1-LF8 locates.
- Row 2 (`NEW-ScoutFlagDesign-2`) has its anchor quote LG1 on the sec1 page and LG2-LG5 on the sec8
  page. If the anchor cell quotes anything beyond LG1, add the sec8 URL to the row's source cell as
  well: https://www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec8.htm
- All quotes 8-25 words, verbatim from served text, pasted locator output above.
- The 4 U.S.C. § 1 statute still reads "forty-eight stars" (1947 text) while the flag today carries
  fifty — a design-tension fact useful for "how a codified mark drifts from the practice", grounded in
  the opened page's text and its "(July 30, 1947, ch. 389)" note.
- Scratch copies of the fetched pages at /fast/scratch/hyaku/kotodama-r57/ScoutFlagDesign/ if any
  locator output needs re-checking.
