# ReopenS107: falsify check of SOURCES rows S107–S112

- Seat: KotodamaR51a3.ReopenS107 (leaf; read-only on the lane).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, HEAD `9feb69e` (read with `git --no-optional-locks`).
- Access date for every URL below: 2026-10-22 (UTC date from `date -u`).
- Writes: this file only. Downloaded copies sit in `/fast/scratch/hyaku/kotodama-r51a3-falsify/ReopenS107/`, outside the lane.

## Item attacked

SOURCES rows S107–S112 (`corpus/SOURCES.md` lines 136–141), their Gate bullets (`corpus/lessons/round-51.md` lines 64–69), and each row's used-by cell. Claim C cites all six from `corpus/knowledge/linguistics/sign-languages-manual-modality.md`.

## Verdict: HOLDS-WITH-FIXES

- All six Gate quotes are verbatim in the opened sources. Five sit at the stated location. The S112 quote sits on excerpt page 4; the row and its Gate bullet say page 3.
- Every primary source URL returned HTTP 200. Three secondary pages refused access (HTTP 403, HTTP 429, and a verification challenge). No quote depends on them.
- Kinds fit. Tiers follow QUALITY criterion 6: no community source is tier A; the abstract (S109) and the two publisher excerpts (S110, S112) are tier B; S107, S108 and S111 are tier A for the scope they carry, which needs the caveats below.
- `used-by` names the entry path on all six rows, and the entry cites each row (entry lines 128, 129, 135, 139, 140, 141). Claim C's S-id falsifier (an S-id cited by the entry but missing from SOURCES, or lacking the entry path in used-by) is not triggered.
- Four findings are medium: S107's missing Glottolog caveat (M1), S112's page anchor (M2), and two entry citations at lines 139 and 140 (M3, M4). The rest are low.

The SOURCES header makes rows append-only. Anchor, teaches and scope fixes therefore need a new row whose teaches opens `supersedes S1NN —`, logged in the round-51 lesson. Entry fixes are plain edits to the entry.

## Results by row

| Row (line) | Gate quote | Kind | Tier (QUALITY 6) | Scope | Anchor | used-by | Verdict |
|---|---|---|---|---|---|---|---|
| S107 (136) | verbatim, newick field; 8 tokens | dataset, fits | A, only as Glottolog's recorded classification (M1) | "membership of BSL/Auslan/NZSL" has no qualifier (M1) | holds (JSON newick field) | entry path; cited at line 128 | HOLDS-WITH-FIXES |
| S108 (137) | verbatim, Greek in section 422e; 18 words | book, fits | A, holds (primary text for its wording) | holds ("wording only") | holds | entry path; line 129 | HOLDS (note L6) |
| S109 (138) | verbatim, abstract paragraph 1; 17 words | docs, fits | B, holds (abstract) | holds | holds | entry path; lines 135, 139 | HOLDS |
| S110 (139) | verbatim, PDF page 1; 23 words | book, fits | B, holds (publisher description) | "Great-Basin" not in the excerpt (L4) | holds: p. 1; ch. 5 pp. 72–84; App. 3 pp. 197–201 | entry path; line 140 | HOLDS-WITH-FIXES |
| S111 (140) | verbatim, §106.3; 15 words | docs, fits | A for what the 1995 Guide describes; basis date not stated (L5) | holds; basis date missing (L5) | holds | entry path; line 140 | HOLDS-WITH-FIXES |
| S112 (141) | verbatim, but on excerpt page 4 not 3; 22 words | book, fits | B, holds | holds; dates presented as settled (L2) | page wrong (M2) | entry path; line 141 | HOLDS-WITH-FIXES |

Gate URLs equal the row source URLs for S107 and S109–S112. S108's Gate adds a second URL (the Perseus hopper page), which I opened and verified.

## Findings

Severity: high, none. Medium, four. Low, eight.

### Medium

**M1. S107 leaves out caveats that its own sources state.** Pointer: `corpus/SOURCES.md:136` (scope and teaches cells).

- Evidence. The JSON record (https://glottolog.org/resource/languoid/id/banz1243.json) sets `"category": "Pseudo Family"` for BANZSL. The Glottolog information page (https://glottolog.org/glottolog/glottologinformation) says:
  - "The L1 Sign Languages are further classified into families, resembling genealogical families for spoken languages."
  - "In lieu of a well-developed methodology, Glottolog sign languages are (sub-)grouped on lexical and/or historical evidence on transmission."
  - "It is expected that the quality of the classification of signed languages in Glottolog is far inferior to that of the spoken languages."
  The same page lists "Sign Language" among the non-genealogical trees. The row's scope, "membership of BSL/Auslan/NZSL", does not say that this is Glottolog's recorded grouping. The entry's line 128 is partly protected by "argued on lexical and historical evidence", so the entry is not false. The registry row that carries the membership claim omits the limit.
- Smallest fix. In a superseding row, scope the tier-A claim to "Glottolog 5.3's recorded classification", quote the "far inferior" sentence, and add the information page as a second source in the Gate bullet. The "Pseudo Family" label is already in the JSON the row cites.

**M2. S112's page anchor is one page early.** Pointers: `corpus/SOURCES.md:141` (anchor cell) and `corpus/lessons/round-51.md:69` (Gate bullet).

- Evidence. Per-page split of https://assets.cambridge.org/97805211/23938/excerpt/9780521123938_excerpt.pdf (10 pages). The Gate quote "Rather than relinquish their ideal of silence as an essential virtue, the monks of Cluny created a silent language of hand signs" occurs only on excerpt page 4. Page 3 carries the section head "Introduction: the dormant language" but not the quote. The section anchor is right; the page is wrong.
- Smallest fix. Superseding row with the anchor "Introduction ('The dormant language'), p. 4 (excerpt PDF)". Log the correction in the lesson's Mistakes table.

**M3. Entry line 140 cites rows for claims they do not carry.** Pointer: `corpus/knowledge/linguistics/sign-languages-manual-modality.md:140`.

- "a 1930 council was filmed to record it (S111)": the NARA page does not mention a council (checked; "council" is absent in any case). The council films are in S110: Contents 5.1 "The Indian Sign Language Council, 1930" (p. 72), 5.2 "Film dictionary of Indian Sign Language", and Appendix 3 "Introductions to films of the 1930 Indian Sign Language Council". That NARA's 1930–31 film project is the same film set is an inference that neither source states.
- "signers across nations — hearing and Deaf (S110)": the excerpt says "a primary language of American Indians who are deaf". The words "hearing" and "Deaf" do not appear in the excerpt (checked).
- Smallest fix. Cite S110 for the council films, mark the film identity "(inference)", and change the signer cell to what S110 says, or cite a row that carries hearing use.

**M4. Entry line 139: the Warlpiri mourning trigger has no Warlpiri source and is not marked.** Pointer: `corpus/knowledge/linguistics/sign-languages-manual-modality.md:139`.

- S109, the only Warlpiri row, contains no mourning, death, names-of-the-dead or bereavement text (each term checked on the page; all absent). The trigger's only support is `politeness-taboo-euphemism.md:75`, a general domain list that names "death and corpses" and "names — the dead, and rulers", with no Warlpiri or sign content. The "(to-verify)" mark sits only on "bereaved women" in the next cell. The round-51 lesson's Frontier already lists "Warlpiri widows' signing" among the to-verify marks (`corpus/lessons/round-51.md:109`).
- Smallest fix. Mark the trigger "(to-verify)" inline, or add a Warlpiri-specific row and cite it.

### Low

**L1. S107 teaches blurs the tree.** `corpus/SOURCES.md:136` (teaches). In the newick, BSL and NZSL sit directly under BANZSL. Auslan sits under Auslanic, which is the direct child. The parenthetical "(with Auslanic/Auslan) are children of BANZSL" blurs this. Fix in the M1 superseding row: "BSL and NZSL are direct children of BANZSL; Auslan sits under its Auslanic node."

**L2. S112 presents contested dates as settled.** `corpus/SOURCES.md:141` (teaches: "customaries (Bernard c. 1078, Ulrich c. 1079–1084)"). Page 9 of the excerpt gives Hallinger's 1959 chronology (Bernard around 1074; Ulrich around 1083; a second Bernard redaction c. 1084–1086) and Wollasch's challenge to it. Page 10 calls the 1078 and 1079–1084 dating "a conservative – and now generally accepted – redating". Footnote 29 says that "The validity of his findings has recently been questioned by Isabelle Cochelin", and that "A definitive resolution to this issue must await the appearance of critical editions". No entry text uses these dates (checked: no 1078, 1079 or 1084 in the entry). Fix: the superseding row says the dates are Wollasch's, adopted by Bruce, and disputed.

**L3. S112's year (2007) is not in the cited excerpt.** The excerpt's ten pages carry no year. Support comes from search snippets only: a MUSE review citing "New York: Cambridge University Press. 2007" (https://muse.jhu.edu/pub/16/article/257132); a review in the Canadian Journal of History citing "Cambridge, Cambridge University Press, 2007" (https://utppublishing.com/doi/abs/10.3138/cjh.43.3.518); and a Cambridge Core bibliography listing "October 2007" (https://www.cambridge.org/core/books/abs/silence-and-sign-language-in-medieval-monasticism/bibliography/FB95B45488286FD9D8F17104560D4C59). The last page returned HTTP 429 when opened. Fix: cite the title page or catalogue record for the year, or record the year as "from search snippets; primary page not opened".

**L4. S110's scope term "Great-Basin" is not in the excerpt.** `corpus/SOURCES.md:139` (scope: "Plains/Great-Basin sign"). Page 1 says "American Indian nations of the Great Plains and cultural groups bordering this geographic area". "Basin" appears on none of the ten pages. Fix: the superseding row scopes it as "Great Plains and bordering groups (p. 1)".

**L5. S111's tier A rests on a dated description.** `corpus/SOURCES.md:140`. The page says "Web version based on Guide to Federal Records … Washington, DC: National Archives and Records Administration, 1995" and "last reviewed on August 15, 2016". The row says "what the National Archives holds" with no date. Tier A still holds for what the Guide describes; the scope should say so. Present holdings would need a check against the NARA catalogue, which I did not open. Fix: scope "as described in the NARA Guide (1995; web version reviewed 2016)".

**L6. S108's gloss source and branch URL are not pinned.** `corpus/SOURCES.md:137`; Gate `corpus/lessons/round-51.md:65`. The Gate's English gloss comes from a second URL that the row does not list: https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Crat.:page=422 (the Fowler translation, Loeb 1921, as printed on the page). The row's source is a `master` branch URL, which moves. The copy I read on 2026-10-22 has sha256 `21f5714a6d7f6d9e79831d684838922a3993bf5d94577186153505f170d17746`. Fix: add the translator and the hash to the Gate bullet; pin a commit if the text is used again.

**L7. S111's quoted title uses an en dash.** `corpus/SOURCES.md:140` (teaches). Inside the quotation marks the row has "1930–31"; NARA prints "1930-31". Cosmetic. Fix: use the hyphen inside the quotation marks.

**L8. Entry line 141 goes beyond S112's wording.** `corpus/knowledge/linguistics/sign-languages-manual-modality.md:141`: "vows of silence under a religious rule". The excerpt says "discipline of silence" and "monastic discipline". "Vow" appears only in an unrelated angel anecdote; "rule" appears only in the title of footnote 6, "Rule of Saint Benedict". Fix: "silence as monastic discipline (S112)".

## Checked and held (no finding)

- S107: the Gate's newick substring is verbatim (`'British Sign Language [brit1235][bfi]-l-':1,'New Zealand Sign Language [newz1236][nzs]-l-':1`). BSL and NZSL are direct children of BANZSL. "Glottolog 5.3" matches the live citation text accessed 2026-10-22.
- S108: the Greek quote (18 words) appears once, inside section 422e (after the 422e milestone at character 127816 and before the next section marker at 128132). The TEI sourceDesc is Platonis Opera, ed. John Burnet, Clarendon Press 1905, so "Burnet ed." holds. The English gloss is verbatim under [422e] (20 words).
- S109: the Gate quote is verbatim (17 words). Author and title match. "for cultural reasons" and "between 1978 and 1986" are present. The row's paraphrase drops "either" from "either impractical or disallowed"; the claim is unchanged.
- S110: the Gate quote is verbatim on page 1 (23 words). "Davis 2010" holds ("First published 2010"; "© Jeffrey E. Davis 2010"). The Contents anchors hold: chapter 5 starts on p. 72 and chapter 6 on p. 85; Appendix 3 starts on p. 197, and the Glossary on p. 202.
- S111: the Gate quote is verbatim (15 words) under §106.3 "Motion Pictures (General) 1903-50". "(13 reels)" and "ca. 1930-31" are present.
- S112: the Gate quote is verbatim (22 words). "custom of using signs in place of speech had become widespread in religious communities throughout western Europe" and "end of the twelfth century" are on page 4.

## Sources opened (access date 2026-10-22)

| # | URL | Method | Result | Used for |
|---|---|---|---|---|
| 1 | https://glottolog.org/resource/languoid/id/banz1243.json | reader; curl; HEAD | HTTP 200, 1094 bytes, sha256 `502a4aee…`; Date 2026-10-22 | S107 |
| 2 | https://glottolog.org/glottolog/glottologinformation | reader; curl | HTTP 200, 62524 bytes, sha256 `d046c818…`; title "Glottolog 5.3" | S107 caveat (M1, L1) |
| 3 | https://glottolog.org/ | reader (content negotiation) | "Glottolog 5.3 … Accessed on 2026-10-22" | S107 version label |
| 4 | https://raw.githubusercontent.com/PerseusDL/canonical-greekLit/master/data/tlg0059/tlg005/tlg0059.tlg005.perseus-grc2.xml | curl; HEAD; parsed locally (too large for the reader) | HTTP 200, 293072 bytes, sha256 `21f5714a…`; ETag `dc2c4f2e…` | S108 |
| 5 | https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Crat.:page=422 | reader; curl | HTTP 200, 50701 bytes, sha256 `c804927e…`; Fowler translation, Loeb 1921 | S108 Gate second URL (L6) |
| 6 | https://konferens.ht.lu.se/kendonsymposium2023/abstracts/ | reader; curl | HTTP 200, 36166 bytes, sha256 `0e06571e…`; Green abstract present | S109 |
| 7 | https://assets.cambridge.org/97805216/90300/excerpt/9780521690300_excerpt.pdf | reader; curl; pdfinfo; pdftotext | HTTP 200, 175994 bytes, 10 pages, sha256 `e25b27e8…`; Last-Modified 2022-03-01 | S110 |
| 8 | https://www.archives.gov/research/guide-fed-records/groups/106.html | reader; curl | HTTP 200, 40896 bytes, sha256 `2055e011…`; 1995 Guide, reviewed 2016 | S111 |
| 9 | https://assets.cambridge.org/97805211/23938/excerpt/9780521123938_excerpt.pdf | reader; curl; pdfinfo; pdftotext | HTTP 200, 164715 bytes, 10 pages, sha256 `2f4c89d1…`; Last-Modified 2009-11-28 | S112 |
| 10 | https://www.cambridge.org/9780521123938 | reader | HTTP 403; not retried, not bypassed | S112 year (failed) |
| 11 | https://www.cambridge.org/core/books/abs/silence-and-sign-language-in-medieval-monasticism/bibliography/FB95B45488286FD9D8F17104560D4C59 | reader | HTTP 429; not retried | S112 year (failed) |
| 12 | https://muse.jhu.edu/article/540545/summary | reader | MUSE verification challenge; not bypassed | S112 year (failed) |
| 13 | https://muse.jhu.edu/pub/16/article/257132 and https://utppublishing.com/doi/abs/10.3138/cjh.43.3.518 | web_search snippets only (not opened in full) | both show a 2007 print year | S112 year (secondary, L3) |

HEAD responses for sources 1, 4, 6, 7, 8, 9 and 5 returned Date headers of 2026-10-22, consistent with the access date.

## Commands run

| # | Command (abridged) | Exit | Key output |
|---|---|---|---|
| 1 | `date -u`; `command -v` for curl, python3, pdftotext, jq, uv; `python3 -c 'import pypdf'` and `import pdfminer` | no error reported; import probes exit 1 (not needed) | 2026-10-22T09:48:39Z; curl, python3, pdftotext and jq present; uv at ~/.local/bin; Python 3.14.8 |
| 2 | `git --no-optional-locks log --oneline -n 6`; `log -n 4 -- corpus/SOURCES.md`; `sha256sum corpus/SOURCES.md` and `git show main:corpus/SOURCES.md \| sha256sum`; `grep -c` for rows S107–S112 | 0 | HEAD 9feb69e; SOURCES last changed in da31d3c; both hashes `8000acb2…`; count 6 |
| 3 | `_grep` for `S10[7-9]\|S11[0-2]` in the sign-language entry | tool | Matches at entry lines 128, 129, 135, 139, 140, 141 |
| 4 | `curl -sS -L -o … -w` for the seven source URLs into scratch | 0 each | HTTP 200 for all seven (sizes in the table above) |
| 5 | `pdfinfo` on both excerpts; `pdftotext -layout` and plain `pdftotext` on both | 0 | 10 pages each; text copies written to scratch |
| 6 | python: Greek quote count, 422e milestone, TEI header | 0 | Quote present once; sourceDesc Burnet 1905. The first context print showed a different occurrence of the opening phrase (at 416c); the exact-match checks are the ones relied on |
| 7 | python: Perseus gloss, Kendon abstract, NARA entry | 0 | Gloss, abstract and NARA phrases present; "mourning", "death", "names of the dead", "bereave" absent on the Kendon page; "council" absent on the NARA page |
| 8 | python: page split of both excerpts (first try passed the PDF file, got UnicodeDecodeError, exit 1; re-run on the text copies) | 1, then 0 | S110 quote on page 1 only; "Basin" absent; S112 quote on page 4 only |
| 9 | `_grep` for `Basin\|Great Plains\|…` in the S110 text | tool | Only "Great Plains" (lines 17, 109) |
| 10 | `_grep` for `1078\|1079\|1084\|Bernard\|Ulrich\|customar\|dormant\|S112\|Cluni` in the entry | tool | Only line 141 (Cluny, S112); no date matches |
| 11 | python NFKC checks: S110 films and Great Basin; S112 quotes and dispute sentences; NARA council, 1995 and 2016 | 0 | As recorded in the findings |
| 12 | `curl -sS -I` (HEAD) on the seven URLs | 0 each | Date headers 2026-10-22; Last-Modified as listed |
| 13 | `sha256sum` on all downloaded copies | 0 | Hashes in the sources table |
| 14 | `_read` on Glottolog information and home pages | tool | "Glottolog 5.3 … Accessed on 2026-10-22" |
| 15 | curl Glottolog information page into scratch; python phrase check; count of "seudo" | 0 | "far inferior", "lexical and/or historical", "weaker theoretical basis" all true; "seudo" 0 hits |
| 16 | python parse of the BANZSL newick depths and category | 0 | BSL and NZSL depth 1; Auslanic depth 1; Auslan depth 2; category Pseudo Family |
| 17 | python year check on the S112 text | 0 | "2007" false; "2009" false; "2010" false; "First published" false; "©" true (running footers only) |
| 18 | `_read` on the CUP product page, the CUP bibliography page and the MUSE article; web_search for the Bruce year | tool | 403; 429; verification challenge; search snippets with 2007 |
| 19 | `git --no-optional-locks status --porcelain`; `rev-parse --short HEAD` | 0 | Only `?? .ufo/waves/round-51/` (pre-existing wave folder); HEAD 9feb69e |
| 20 | `pdftotext -v`; `curl --version`; `python3 --version` | 0 | pdftotext 26.08.0; curl 8.23.0; Python 3.14.8 |
| 21 | `_grep` for `S07[1-9]\|S0[89][0-9]\|S1[0-9][0-9]` in the pastoralism entry; positive control with the same pattern on the sign-language entry | tool | Pastoralism: no matches. Control: matches found, so the pattern works |
| 22 | `_glob` and `_read` of `politeness-taboo-euphemism.md` lines 69–83 | tool | Line 75 is the domain list: death and corpses; names, the dead and rulers; occupational bans |
| 23 | python word counts of the seven Gate quotes | 0 | S107 8 tokens; S108 18 and 20; S109 17; S110 23; S111 15; S112 22; all at most 25 |
| 24 | python 422e interval check | 0 | 127816 < 128014 < 128132: true |
| 25 | `realpath -m` on the report path; `ls` of the falsify folder; existence test | 0 | Target absent before writing; folder holds other seats' reports; parent is a plain directory |
| 26 | `ls` of the build-wave folder for ScribeSec08Diachrony, ScribeSec09Alternate, ScribeSec13Calibration, ScribeHeadScope | 0 | All four exist; existence only, not used as evidence |
| 27 | python check of entry phrases against the excerpts | 0 | "hearing" absent; "Deaf" absent (S110); lowercase "rule" absent and "Rule" only in footnote 6 (S112); "vow" only in an angel anecdote |
| 28 | `_read` of the Glottolog sign-language section (lines 301–420 of the reader output) | tool | Sentences used in M1 confirmed; exact-match python check on the fetched copy (command 15, exit 0) |
| 29 | python exact-match of four Glottolog sentences used in M1 | 0 | All four true |

## Unrun checks

- Claim D counter `python3 -B reports/round-51/boundary-count.py`: not run; outside this seat's item.
- Claim C count `find corpus/knowledge -name '*.md' | wc -l` and `python3 -B reports/round-28/readme/sweep.py`: not run; outside this seat's item.
- `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json`, `reports/round-51/claims-agree.py`, and `python3 -B tools/gates/provenance-audit.py corpus/knowledge/linguistics/sign-languages-manual-modality.md`: not run.
- Cambridge product and bibliography pages (HTTP 403 and 429): not retried. The MUSE page (verification challenge): not bypassed.
- NARA present-day holdings: not checked against the NARA catalogue; not opened.

## Tooling

No installs or updates. Tools used, all already present: curl 8.23.0 (`/usr/bin/curl`, release 2026-10-14); pdftotext and pdfinfo, poppler 26.08.0 (`/usr/bin/pdftotext`); Python 3.14.8 (`/usr/bin/python3`). pypdf and pdfminer are not installed and were not needed. No pacman transactions (paused host-wide).

## Residual risk and gaps

- The S112 year rests on search snippets; the primary pages refused access.
- The S108 raw XML comes from a moving `master` branch; the hash covers only the 2026-10-22 copy.
- S111 describes a 1995 print guide; present holdings are unverified.
- The film identity in M3 is an inference, and the finding says so.
- I did not review the content of the build-wave seat reports. I confirmed that the four named ones exist and treated them as author-lane context only.
- I did not review the other mined rows or the rest of the entry; those belong to other seats.
