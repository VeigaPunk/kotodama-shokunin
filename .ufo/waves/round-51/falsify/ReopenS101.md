# ReopenS101: falsify attack on SOURCES rows S101–S106

Seat: KotodamaR51a3.ReopenS101 (leaf; read-only on the lane; this file is its only write).
Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin, HEAD 9feb69e. corpus/SOURCES.md, corpus/lessons/round-51.md and corpus/knowledge/linguistics/sign-languages-manual-modality.md are byte-identical to HEAD (checked read-only).
Access date for every URL below: 2026-10-22.
Installs: none. No tool was installed or updated, so RULES.md was not consulted.

## 1. Item attacked

SOURCES rows S101–S106 (corpus/SOURCES.md:130–135), their Gate bullets (corpus/lessons/round-51.md:58–63), and how the C entry uses them (corpus/knowledge/linguistics/sign-languages-manual-modality.md:112–131).

Checks per row: kind; tier under QUALITY criterion 6 and the SOURCES preamble (community is never A; abstracts and publisher descriptions are B); Gate quote verbatim at its stated location and at most 25 words; scope; anchor; used-by; status.

## 2. Commands run

| # | Command or call | Output | Exit |
|---|---|---|---|
| 1 | `git --no-optional-locks rev-parse --short HEAD` | 9feb69e | 0 |
| 2 | `git --no-optional-locks diff --quiet -- corpus/SOURCES.md` | no difference from HEAD | 0 |
| 3 | `git --no-optional-locks diff --quiet -- corpus/lessons/round-51.md` | no difference from HEAD | 0 |
| 4 | `git --no-optional-locks diff --quiet -- corpus/knowledge/linguistics/sign-languages-manual-modality.md corpus/SOURCES.md corpus/lessons/round-51.md` | no difference from HEAD | 0 |
| 5 | `realpath -m .ufo/waves/round-51/falsify/ReopenS101.md` | /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-51/falsify/ReopenS101.md | 0 |
| 6 | Read calls: SOURCES.md:1–40 and :128–137 (raw); round-51.md grep `^- S10[1-6] ` (lines 58–63); entry grep for S10[1-6] (lines 112–131) and for genealogy and calibration terms; entry reads :1–30, :108–135, :197–223; calibration-registry.md:30–42; claims.json; QUALITY.md; glob of .ufo/waves/round-51/ | returned as expected | n/a |
| 7 | `web_search` (Taub 2001; Frishberg 1975) | search snippets only; no page opened from these | n/a |
| 8 | `_web_search_placeholder` (mistaken tool name) | error "Tool web_search_placeholder not found"; no effect | n/a |

Not run (outside this item): `python3 -B reports/round-51/boundary-count.py`, `find corpus/knowledge -name '*.md' | wc -l`, `python3 -B reports/round-28/readme/sweep.py`, `tools/gates/provenance-audit.py`, and the separability check.

## 3. Source URLs opened (access date 2026-10-22)

| # | URL | What I found |
|---|---|---|
| 1 | https://www.benjamins.com/catalog/gest.13.3.03pad | HTTP 200. The abstract (meta-citation_abstract) is one block; the S101 quote is its fourth sentence. The page shows "authorization required" and "Get fulltext from our e-platform". Authors, Gesture 13:3, pp. 287–308 and DOI match the row. |
| 2 | https://jbe-platform.com/content/journals/10.1075/gest.13.3.03pad | HTTP 403. Not read. |
| 3 | https://eric.ed.gov/?id=EJ124326 | HTTP 200. The author-supplied abstract ("Author/CLK") contains the S102 quote verbatim. Frishberg, Language 51(3), 696–719, September 1975. |
| 4 | https://www.jstor.org/stable/412894 | "Client Challenge" page, not the article. This is consistent with "JSTOR full text blocked". A search snippet (not opened) gives a JSTOR abstract reading "a strong tendency"; the row quotes the ERIC wording. |
| 5 | https://www.cambridge.org/core/journals/language/article/arbitrariness-and-iconicity-historical-change-in-american-sign-language/672E4A607647636A15804CC7D18B3C36 | HTTP 429. Consistent with the S102 scope note. |
| 6 | https://assets.cambridge.org/97805217/70620/excerpt/9780521770620_excerpt.pdf | HTTP 200 (PDF text, pp. 1–10). The S103 quote is on p. 2, verbatim. The ASL, Danish and Chinese TREE passage is on p. 8. Header ISBN-10 0521770629, which matches the row's ISBN-13 9780521770620 (my hand check of the ISBN-13 check digit gives 0). |
| 7 | https://www.cambridge.org/core/books/language-from-the-body/1A402ECC381DBC286CF1CC47C639C4FC | HTTP 429. |
| 8 | https://www.librarycat.org/lib/signs2go/item/146794133 | HTTP 429. The 2001 date appears only in a search snippet (not opened). |
| 9 | https://glottolog.org/resource/languoid/id/lsfi1234 | HTTP 200. Heading "Pseudo Family: LSFic". Title "Glottolog 5.3". |
| 10 | https://glottolog.org/resource/languoid/id/lsfi1234.json | HTTP 200. category "Pseudo Family". Newick: French Sign Language [fren1243] is a direct child; American Sign Language [amer1248] sits under ASLic [asli1244], which sits under LSFic. |
| 11 | https://glottolog.org/resource/languoid/id/fren1243.json | HTTP 200. Classification: Sign Language (sign1238), L1 Sign Language (deaf1237), LSFic (lsfi1234). |
| 12 | https://glottolog.org/resource/languoid/id/amer1248.json | HTTP 200. Classification array: Sign Language (sign1238), L1 Sign Language (deaf1237), LSFic (lsfi1234), ASLic (asli1244), American Sign (amer1258). category "Sign Language". No spoken-language node appears. |
| 13 | https://glottolog.org/resource/languoid/id/bsli1234 | HTTP 200. Heading "Pseudo Family: BSLic". The "Comments on subclassification" section holds the S106 quote. The comment names Schembri et al. 2010 and Johnston 2003 for the BANZSL subgroup and gives no evidence type for it. |
| 14 | https://glottolog.org/resource/languoid/id/sign1238 | HTTP 200. Heading "Pseudo Family: Sign Language". |
| 15 | https://glottolog.org/glottolog/glottologinformation | HTTP 200, read in full (three ranges). Section "About Languoids": "In addition to the genealogical trees (families and isolates), the Families page also includes the following non-genealogical trees:"; the list includes "Sign Language". Section "On the classification of sign languages": "L1 Sign Languages are further classified into families, resembling genealogical families for spoken languages"; "For signed languages, such a methodology remains to be articulated"; "In lieu of a well-developed methodology, Glottolog sign languages are (sub-)grouped on lexical and/or historical evidence on transmission." Principle 4 (section "Is the modality speech?"): sign languages "are classified on a weaker theoretical basis." This page is not a SOURCES row. |

## 4. Per-row results

| Row (SOURCES line) | Kind | Tier | Gate quote (lesson line) | Scope and anchor | used-by, status | Verdict |
|---|---|---|---|---|---|---|
| S101 (:130) | paper | B: holds (abstract only) | Verbatim in URL 1; 23 words; location "Abstract, ¶2" (lesson :58) is not checkable (see F8) | Scope omits the elicitation task (F4); anchor "¶2–3" is not checkable (F8) | entry path; mined | HOLDS-WITH-FIXES |
| S102 (:131) | paper | B: holds (abstract only) | Verbatim in URL 3; 20 words | Scope holds; access notes reproduced (URLs 4 and 5); teaches drop a hedge (F7) | entry path; mined | HOLDS-WITH-FIXES |
| S103 (:132) | book | A: holds for Taub's own claims in pp. 1–10 | Verbatim on p. 2 (URL 6); 17 words | Scope lists "shape/outline strategies", which pp. 1–10 do not treat beyond the TREE example (F12); entry misreports the TREE passage (F3) | entry path; mined | HOLDS-WITH-FIXES |
| S104 (:133) | dataset | A: holds for Glottolog's node naming | Verbatim heading (URL 9); 3 words | Existence and naming hold. FSL and ASL membership is true (URLs 10–12) but the anchor "Page heading" does not show it (F11) | entry path; mined | HOLDS-WITH-FIXES |
| S105 (:134) | dataset | A fails for "genealogical placement" | Verbatim across two adjacent JSON lines (URL 12); short | Scope "ASL's genealogical placement" and teaches "lineage" contradict Glottolog's own non-genealogical statement (URL 15) (F1) | entry path; mined | FAILS |
| S106 (:135) | dataset | A holds for Glottolog's attribution | Verbatim (URL 13); 24 words | "Argued on lexical and historical evidence" is not stated for BANZSL in the comment (F2) | entry path; mined | HOLDS-WITH-FIXES |

All six rows: kind, status, opened date and used-by name the entry, and the Gate bullet URL equals the row URL. All six quotes are at most 25 words.

## 5. Findings

Severity is given first. Pointers are to corpus paths (lane-relative) or URL numbers from section 3.

**F1. HIGH. S105 scope and teaches exceed its tier-A source.**
- Pointer: corpus/SOURCES.md:134 (scope "ASL's genealogical placement"; teaches "ASL's lineage runs through LSFic, not through English"). Used at corpus/knowledge/linguistics/sign-languages-manual-modality.md:127 ("Genealogically to other signed languages …") and :131 ("which manual family it descends from, never the ambient spoken language").
- Evidence: URL 15 lists "Sign Language" among the non-genealogical trees. It says sign-language families only "resemble" genealogical families and that the method "remains to be articulated". URL 14 labels the sign root "Pseudo Family: Sign Language", and URL 10 gives LSFic the category "Pseudo Family". "Not through English" is a property of how the sign tree is built (URL 12 has no spoken-language node). It is not evidence about descent.
- QUALITY criterion 6 (tier A only for the exact scope) is not met for the genealogical claim.
- Smallest fix: do not edit S105 in place (SOURCES is append-only). Add a superseding row whose teaches opens "supersedes S105 —", scoped to "Glottolog's placement of ASL (amer1248) under LSFic in its non-genealogical Sign Language tree", with URL 15 and URL 12 as anchors, tier A for that scope. Then at entry :127 drop "Genealogically" and cite the new row. At entry :131 delete the descent clause or code it C (calibration-registry.md:36: "do not report one reading as settled").

**F2. MEDIUM. S106 teaches overstate the comment.**
- Pointer: corpus/SOURCES.md:135 (teaches "the BANZSL subgroup is argued on lexical and historical evidence"); repeated at entry :128.
- Evidence: URL 13 attributes the BANZSL subgroup to Schembri et al. 2010 and Johnston 2003 and states no evidence type for it. The lexicostatistical and historical evidence in that section concerns the BSLic core and the origin of BSL. The row's scope also drops Glottolog's "Pseudo Family" label.
- Smallest fix: teaches to "Glottolog attributes the BANZSL subgroup to Schembri et al. 2010 and Johnston 2003; the comment does not state the evidence type". Scope to "Pseudo Family: BSLic (Glottolog) and its BANZSL subgroup". Entry :128 to "argued by Schembri et al. 2010 and Johnston 2003 (S106)", dropping "on lexical and historical evidence" unless those papers get their own row.

**F3. MEDIUM. The entry misreports S103.**
- Pointer: corpus/knowledge/linguistics/sign-languages-manual-modality.md:118 ("Shape | the hands trace the referent's outline — ASL, Danish and Chinese TREE are equally iconic yet trace differently (S103)").
- Evidence: URL 6, p. 8: in ASL TREE "the hands and forearms are positioned to resemble a tree growing out of the ground". Only the Danish (outline of branches and trunk) and Chinese (outline of trunk) forms trace an outline.
- Smallest fix: "Shape | the hands trace the referent's outline (Danish and Chinese TREE); ASL TREE positions the hands to resemble a growing tree (S103, p. 8)".

**F4. MEDIUM. S101 scope drops the elicitation restriction.**
- Pointer: corpus/SOURCES.md:130 (scope "three unrelated sign languages versus hearing silent gesturers"). Entry :112 and :120 generalize to "lexical strategies whose distribution differs".
- Evidence: URL 1 abstract, third sentence: the comparison comes "in an elicitation task featuring pictures of hand-held manufactured tools".
- Smallest fix: add "(elicitation task with pictures of hand-held manufactured tools)" to the S101 scope. At entry :112 and :120 add "for hand-held tools".

**F5. MEDIUM. A universal negative is cited to rows that cannot carry it.**
- Pointer: corpus/knowledge/linguistics/sign-languages-manual-modality.md:131 ("never the ambient spoken language (S104, S106)").
- Evidence: S104 is a classification node. S106 covers sign-to-sign derivation only (Maritime from BSL; Namibian possibly from South African Sign Language). Neither row says anything about spoken-language ancestry.
- Smallest fix: delete the clause, or code it H with its own source.

**F6. MEDIUM. No calibration code or recheck pointer covers the family claims.**
- Pointer: corpus/knowledge/linguistics/sign-languages-manual-modality.md:197–211 (§13 calibration bank) and :217–219 (§14 recheck). The claims at :127, :128 and :131 have no entry.
- Evidence: calibration-registry.md:36 (C: "preserve alternatives, scope, and discriminating evidence; do not report one reading as settled"). URL 15 says the method "remains to be articulated".
- Smallest fix: add a §13 row coded C for "sign-language families are genealogical", with the stop rule. Add to §14: "re-open S104–S106 and the Glottolog sign-language section before citing a descent or family claim".

**F7. LOW. S102 teaches drop the hedge.**
- Pointer: corpus/SOURCES.md:131 (teaches "formational changes favour language-internal consistency at the expense of transparency").
- Evidence: URL 3: "Changes at the formational level are seen as contributing to language-internal consistency, at the expense of transparency."
- Smallest fix: "formational changes are seen as contributing to language-internal consistency, at the expense of transparency".

**F8. LOW. S101 paragraph anchor cannot be checked, and row and lesson disagree.**
- Pointer: corpus/SOURCES.md:130 ("Abstract, ¶2–3 (catalog page)") against corpus/lessons/round-51.md:58 ("Abstract, ¶2"). URL 1 gives the abstract as one block.
- Smallest fix: anchor "Abstract (catalog page, single block; quoted sentence is the fourth)", and make lesson :58 match.

**F9. LOW. S101 teaches add "not free pantomime", which the abstract does not say.**
- Pointer: corpus/SOURCES.md:130 (teaches "iconicity is organized in grammar, not free pantomime"). Entry :112 ("patterned, not pantomime … (S101)").
- Evidence: URL 1 says patterns are "organized in the grammars of sign languages". "Pantomime" does not appear. The "not mime" claim is S103's (URL 6, p. 2).
- Smallest fix: strike "not free pantomime" from the S101 teaches. At entry :112 cite S101 for "patterned" and S103 for "not pantomime".

**F10. LOW. The entry's definition of "handling" is not in S101's abstract.**
- Pointer: corpus/knowledge/linguistics/sign-languages-manual-modality.md:116 ("Handling | the hand holding or manipulating the tool (S101)").
- Evidence: URL 1 names the "handling strategy" but does not define it. The full text is not reachable (URL 2 gives HTTP 403; the catalog page shows "authorization required").
- Smallest fix: mark the definition "(to-verify)", or cite the full text once it is opened.

**F11. LOW. S104 anchor does not show the membership it teaches.**
- Pointer: corpus/SOURCES.md:133 (anchor "Page heading"; teaches "FSL (fren1243) and ASL (amer1248) classify under it").
- Evidence: the heading shows the node exists. Membership is shown by URL 10 (newick) and URLs 11–12. "FSL-rooted" is the row's gloss. The scope drops the "Pseudo" label.
- Smallest fix: anchor "Page heading; JSON newick field of lsfi1234.json". Scope "Pseudo Family LSFic (lsfi1234), named for LSF".

**F12. LOW. S103 scope and teaches run wider than the excerpt, and the entry states them as flat fact.**
- Pointer: corpus/SOURCES.md:132 (scope "shape/outline strategies"; teaches "conventional features … found in standard textbooks and dictionaries"). Entry :112 and :120.
- Evidence: pp. 1–10 treat shape and outline only through the TREE comparison (p. 8). The "textbooks and dictionaries" line (p. 2) refers to the four introductory examples. The entry presents these as Taub's views without attribution.
- Smallest fix: scope "the TREE comparison (p. 8) and the not-mime passage (p. 2)". Teaches "the book's four introductory examples". Entry: "Taub (2001, ch. 1–2) argues …".

**F13. LOW. Unsupported inference in the entry.**
- Pointer: corpus/knowledge/linguistics/sign-languages-manual-modality.md:112 ("a young sign language reads more iconic than an old one").
- Evidence: no row supports it. S102 supports only the historical drift toward arbitrariness.
- Smallest fix: mark it H (calibration-registry.md:38) or cite a source.

## 6. Verdict

- S101: HOLDS-WITH-FIXES (F4 medium; F8, F9, F10 low)
- S102: HOLDS-WITH-FIXES (F7 low)
- S103: HOLDS-WITH-FIXES (F3 medium; F12 low)
- S104: HOLDS-WITH-FIXES (F11 low; the entry-side defects are F1 and F5)
- S105: FAILS (F1 high)
- S106: HOLDS-WITH-FIXES (F2 medium)

Item verdict: FAILS. S105 fails its stated scope, and the C entry's genealogical claims at :127 and :131 rest on it. The item would move to HOLDS-WITH-FIXES after a superseding row for S105, the entry edits at :127 and :131, and the medium fixes F2–F6.

## 7. Unrun checks and verification gaps

- Taub 2001 publication year: not verified by opening. Cambridge (URL 7) and librarycat (URL 8) returned HTTP 429. The year appears only in search snippets.
- Frishberg full text: not opened (URL 4 is a challenge page; URL 5 returned HTTP 429).
- Padden et al. 2013 full text: not reachable (URL 2 returned HTTP 403). The "handling" definition and "not free pantomime" could not be checked against the full text.
- Schembri et al. 2010 and Johnston 2003 (cited by S106): not opened, and no SOURCES row exists for them.
- URL 15 (Glottolog classification principles) is not a SOURCES row. Its tier-A status for the non-genealogical point is my recommendation for the superseding row, not an admitted row.
- Gate bullets: URLs, access dates and seat names match the rows for all six. The only mismatch is the S101 paragraph label (F8).

## 8. Residual risk

- S001 (corpus/SOURCES.md, Glottolog About, tier A for "genealogy") does not carry the sign-language exception shown in URL 15. S107 (BANZSL membership from a JSON newick) is in the same family. Neither is in this item; both need the same review.
- The Glottolog classification (URLs 9–14) is editor judgment, and URL 15 says so. Tier A is for what Glottolog says, not for the scholarly argument behind it.
