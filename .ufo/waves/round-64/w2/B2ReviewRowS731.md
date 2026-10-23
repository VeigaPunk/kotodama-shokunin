# B2ReviewRowS731 — falsification review of ScribeRowS731/row.txt

Fetches (2026-10-23):
- LIVE `200 https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/`
- CAPTURE `200 https://web.archive.org/web/20250424085946id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/`
- Lane locator: `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/`

| field | draft value | verified? | evidence (verbatim) | required fix |
|---|---|---|---|---|
| row shape | 11 cells, paper, mined, 2026-10-23, 180d, used-by names entry | YES | row parses to 11 cells; ROWS-shape rules all satisfied | none |
| live URL | https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/ | YES | `LIVE 200`, same-page capture original matches | none |
| capture | web.archive.org/web/20250424085946id_/… | YES | `CAPTURE 200`; `original=` live URL | none |
| anchor quote | "the results from the current study indicated that children's diagnosis did not have an effect on the frequency of intrasentential code-switching." | YES | quote found verbatim+contiguous in live body (pos 63667) and capture (pos 63722); context: "similar to gutiérrez clellen et al 2009 the results from the current study indicated that children s diagnosis did not have an effect on the frequency of intrasentential code switching this study lends more support…"; 23 normalised words (8–25 OK); body paragraph text, not heading/caption/attr | none |
| anchor locator text | "Discussion, Code-Switching and Language Proficiency paragraph" | WRONG | page heading list shows the quote sits under Discussion subsection `Code-Switching and DLD`; `Code-Switching and Language Proficiency` is a different Discussion subsection | change locator to "Discussion, Code-Switching and DLD paragraph" (quote itself unchanged) |
| citation authors | Maria Kapantzoglou et al. | YES | citation_author meta: Maria Kapantzoglou, Julie Esparza Brown, Lauren M Cycyk, Gerasimos Fergadiotis | none |
| citation year | 2021 | YES | citation_publication_date "2021 Apr 13" | none |
| citation title | Code-Switching and Language Proficiency in Bilingual Children With and Without Developmental Language Disorder | YES | citation_title meta identical | none |
| journal/vol/pages | JSLHR 64(5): 1605–1620 | YES | citation_journal_title "Journal of Speech, Language, and Hearing Research : JSLHR"; volume 64, issue 5, firstpage 1605; printed range "1605–1620" in page refs | none |
| tier A for scope | "whether DLD diagnosis relates to intrasentential code-switching frequency in 5–7-year-old Spanish–English children" | YES | primary research article reporting that exact analysis; "in 5- to 7-year-old Spanish–English-speaking children … with DLD and their peers with TLD"; DOI 10.1044/2020_JSLHR-20-00182 | none |
| BULLET vs quote | "Children's diagnosis showed no link to switch frequency in this sample, letting worldbuilders avoid diagnostic shorthand in bilingual dialogue." | YES (minor soften) | RESTATE metrics on draft clause: content words 14 (≥5), in-order hits 3 (≥3), longest copied run 3 (≤12), novel words present. Quote supports the frequency claim; paper additionally found diagnosis did not affect intersentential CS or total CS count ("replicating them for intersentential code switching and the total number of csw"), so "switch frequency" unqualified does not overreach. Caveat: same subsection reports a prevalence difference ("fewer children with DLD did so"), i.e. diagnosis related to *whether* children switched, not *how often*; the bullet's "in this sample" hedge keeps it honest | optional: could add "among children who switched" for precision; not required |

VERDICT: FIX-REQUIRED anchor locator names the wrong Discussion subsection — the quote sits under "Code-Switching and DLD", not "Code-Switching and Language Proficiency"; all other fields verified clean (HTTP 200 live+capture, quote LOCATED verbatim, citation/tier/bullet sound).
