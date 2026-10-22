# ReviewCSec05: falsification of claim C, entry section 5 (sublexical parameters)

Seat: KotodamaR51a3.ReviewCSec05 (leaf, read-only on the lane). Recommendation only. I edited no lane file, no SOURCES row, and no lesson. The only lane write is this report.

## 1. Item attacked and verdict

- Item: `corpus/knowledge/linguistics/sign-languages-manual-modality.md` section 5 (lines 81–95). I also checked the five SOURCES rows it cites (S071, S094, S095, S096, S097; `corpus/SOURCES.md:100,123–126`), the in-corpus anchor `corpus/knowledge/linguistics/phonetics-phonology.md:201–203`, and the design-rule table.
- Lane state: HEAD `9feb69e`. The working-copy blob of the entry (`b79c679…`) equals the committed blob at HEAD, so every line I quote is the committed text.
- Verdict: **HOLDS-WITH-FIXES.** The core figures, quotes, minimal pairs and Prosodic Model values check out against primary text. Four medium fixes are needed before section 5 can be called fully supported (M1–M4). No cited claim is false on its primary source, and no source is invented. Section 5 contains no canon decision and no clinical, education-policy or rights ruling.

## 2. Findings

Severity: high = a cited claim is false on its cited source; medium = a cell cites a source that does not say it, or a contested point is stated as settled, or a required calibration is missing; low = precision, wording or terminology. **No high-severity finding.**

### Medium

**M1. The dominance-condition set cites the wrong edition.** Pointer: entry `:92` ("passive hand is limited to a small unmarked set (A, B, 5, G, C, O) (S097, S094)").
- S094 (Battison 1974, issue PDF p. 8 = article p. 6) supports six: "only the six most unmarked hand configurations can serve in the subordinate, stationary position … (1) A … (2) B … (3) 5 … (4) G … (5) C … (6) O", "with a few exceptions".
- S097 (CSLDS Module 7, Dominance Condition paragraph and point (c)) gives seven: "A, S, B, 5, G (i.e., 1), C and O", attributed to "Battison, 1978, p.206". The row cites S097 first for a six-item set that S097 contradicts.
- The 1974 article itself is internally inconsistent: its deletion section (issue PDF p. 11 = article p. 9) says "only the six most unmarked handshapes are allowed in the stationary position-A B S G O C" (S for 5).
- Fix: cite S094 for the six with "Battison 1974"; cite S097 for the seven with "Battison 1978, p. 206"; keep "with a few exceptions". Drop S097 as support for the six. Record the article-p. 9 printing in a superseding S094 row (SOURCES is append-only).

**M2. The nonmanual cell cites S095 for content S095 does not contain.** Pointer: entry `:91` ("which face and body articulators are grammatical — eyebrows, gaze, mouth, head tilt — and what they mark (S095)").
- S095 (Brentari, Fenlon and Cormier; PDF p. 6) says only: "Non-manual behaviors of the face and body are also part of the phonology (see e.g., Pfau & Quer, 2010), but here we focus on manual parameters."
- A search of the full chapter text finds no statement about eyebrows, head tilt, or nonmanual functions. "Gaze" appears only in a perception passage (PDF p. 3); "mouth" only as one head place value (PDF p. 8).
- Fix: keep only "non-manual behaviours are part of the phonology (S095, PDF p. 6)". Take articulators and functions from S098 (§2.1: head and body movements, facial expressions and mouth patterns; §2.3.1: side-to-side headshake as the most common negation marker; §2.3.2: raised eyebrows mark yes/no questions, lowered eyebrows wh-questions). S098 was checked by excerpt only (see section 5).

**M3. Palm orientation is stated as a settled fourth parameter; the cited Stokoe text disputes it.** Pointers: entry `:90` ("Battison added it as a fourth parameter (S094)") and `:83`; SOURCES `:100` (S071 scope "no post-1960 data").
- Battison 1974 does list orientation as a fourth aspect (S094, PDF p. 5). Brentari (S095, PDF p. 9) calls orientation "traditionally regarded as a minor parameter" and treats it as a relation between the active handpart and the place of articulation.
- S071 (the 1978 Linstok reprint named in the row title; full text on archive.org) argues against it: "Handshape and attitude (miscalled orientation) are both ways in which what acts can vary … they are not variable independently of one another, except in a few special circumstances." It also says: "Attempts at isolating orientation as a basic or phonemic contrast in ASL which ignore the tri-aspectual analysis … go against signers' intuition."
- The S071 row scope says "no post-1960 data", but the cited reprint carries 1978 postscript commentary, including this critique.
- Fix: give orientation status C with both sides sourced (S094 p. 5; S095 p. 9; S071 quotes). Correct the S071 scope by a superseding row, not an in-place edit.

**M4. Section 5 carries no calibration codes.** Pointer: entry `:83–:95`. QUALITY.md criterion 2 requires every framework entry to name its status; calibration-registry.md `:35–39` defines R, C, B, H, T.
- Sections 9, 11 and 13 use the codes. Section 5 uses "(design rule)" tags instead of H.
- Uncoded framework claims: the three-aspect model (S071); the four-aspect model and the 45 and 25 counts (S094); the Prosodic Model's four regions by eight values (S095); the symmetry and dominance conditions.
- S094 itself says "Not all of these primes contrast at an underlying level of representation" (PDF p. 6). S095 says the eight place values "may well be language-specific" (PDF p. 9).
- Fix: code each row. Counts: B (ASL, 1974, "approximately"). Prosodic Model values and movement-as-nucleus: C (one model; values language-specific). Symmetry and dominance: B for ASL with exceptions, cross-linguistic reach C. Design rules: H (`calibration-registry.md:38`). Replace "(design rule)" with H.

### Low

**L1. "Movement is the syllable nucleus" is stated as identity.** Pointer: `:89`. S095 PDF p. 11: movement is "analogous to vowels". p. 12: it forms "a unit similar to the syllable nucleus". p. 13: Meier (2012) concludes the sign syllable is "physically distinct". Fix: "movement plays a nucleus-like role in the Prosodic Model (S095 pp. 11–12); whether the sign syllable is the same kind of unit is disputed (S095 p. 13)."

**L2. "Iconicity never excuses skipping contrast (S095)".** Pointer: `:83`. S095 PDF p. 6 says core-lexicon sublexical elements are typically non-iconic, arbitrary, contrastive, and create minimal pairs. It does not say "never". Fix: label as H; cite S095 p. 6 for the arbitrary-and-contrastive basis.

**L3. "Contrast is proven by minimal pairs".** Pointer: `:83`. S096 says phonologists "can make use of minimal pairs to look for phonemes". Fix: "shown by minimal pairs".

**L4. The ~45 handshape count drops its caveat.** Pointer: `:87`. S094 PDF p. 6: "approximately 45 different handshape primes … Not all of these primes contrast at an underlying level of representation." This clause supports the row's own point. Fix: add it.

**L5. Location row: counts not reconciled; caveats missing.** Pointer: `:88`. Battison counts about 25 location primes (S094 PDF p. 6), which the row omits, while it uses the Prosodic Model's 4 × 8 values. S095 PDF p. 8 says "eight major locations" in one sentence and "four major body regions" in the next. Its eight head values are "thought to be contrastive in ASL" (p. 8), and the values "may well be language-specific" (p. 9). Fix: give both counts with sources and the language caveat.

**L6. The two-handed paraphrase drops conditions.** Pointer: `:92`. The 1974 symmetry condition (S094 PDF p. 7) also requires identical or polar-opposite orientations and symmetrical or polar-opposite locations. S097 says "orientation must be either symmetrical or identical." The dominance restriction holds "with a few exceptions" (S094 p. 8; S097 "very few exceptions"). Fix: state the conditions or quote the row.

**L7. The minimal-pair row omits the parameter each pair isolates.** Pointer: `:93`. All four pairs are correct (S094 PDF p. 6): APPLE/ONION differ in location; CAR/WHICH in handshape; OFFER/MAYBE in movement; SHORT/TRAIN in orientation. Fix: name the parameter for each pair.

**L8. "Phonemic inventory" is contested terminology.** Pointer: `:87`. Battison (S094 PDF pp. 5–6) uses "primes" rather than "cheremes", which "avoids involvement with the phoneme and its problems". S096 says Stokoe's units are "phonemes". Fix: "prime (chereme) inventory; whether these are phonemes is disputed."

**L9. "Signification" should be "signation".** Pointers: entry `:16` (section 1, not section 5) and SOURCES `:100` (S071 row: "signification/action"). Stokoe's text: "tab, dez, and sig are shortened forms of the terms tabula, designator, and signation" and "Signation stands for 'the action of making a sign'." Fix: correct entry `:16` to "signation (sig)"; correct the S071 row by a superseding row.

**L10. The S094 page range is wrong.** Pointer: SOURCES `:123` ("article pp. 3–5"). Taking article p. 1 as issue PDF p. 3 (the title page, checked in the page text), the Restrictions section starts on article p. 5 (issue PDF p. 7), its Dominance list is on article p. 6 (PDF p. 8), and the "A B S G O C" line is on article p. 9 (PDF p. 11). Fix: superseding row with the corrected pages.

**L11. A Gate-only URL and a wording mismatch (S071).** Pointer: `corpus/lessons/round-51.md:28`. The Gate quotes the S071 sentence from a second URL, https://www.joshiesworld.com/wp-content/uploads/2025/10/stokoe_1960.pdf, which is not in SOURCES row 100, with "motion" where the registered text reads "action". Registered text (archive.org full text): "Like consonant and vowel, the aspects position, configuration, and action may only be described in terms of contrast with each other." The joshiesworld PDF is image-only for my text tool (extraction incomplete for PDF pp. 1–41), so I could not verify its wording. Fix: quote the registered copy; drop the second URL or register it in its own row.

**L12. The contrast rule and build order.** Pointer: `:95`. "Each parameter must earn its place by contrast (S071, S095)." S071 supports the contrast rule (quote in L11). S095 PDF p. 6 says the "feature units within each parameter" are justified by contrast, which is narrower than "parameter". The build order is uncited and uncoded. Fix: cite S071 for the rule; code the build order H.

**L13. The in-corpus anchor supports less than cited.** Pointer: `:83` cites `phonetics-phonology.md:201-203`. That passage says "handshape, location, movement carry contrast (Sandler & Lillo-Martin 2006)." It does not support Stokoe's terms or orientation. Fix: cite it only for the three parameters it names.

**L14. "Palm orientation" uses the older sense.** Pointer: `:90`. S095 PDF p. 9: earlier descriptions used the palm and fingertip direction; Brentari (1998) treats orientation as a relation between the active handpart and the place of articulation. Fix: define the term in one line, coded per M3.

## 3. What holds (checked on primary text)

- H1: "approximately 45 different handshape primes and 25 different primes for locations" (S094 PDF p. 6). Entry `:87` "~45" matches.
- H2: four simultaneous aspects (location, handshape, movement, orientation); Stokoe "does not explicitly include orientation" (S094 PDF p. 5). Subject to M3.
- H3: four minimal pairs with the parameters in L7 (S094 PDF p. 6). S096 agrees on APPLE/ONION and CAR/WHICH (ASL).
- H4: the Dominance Condition core statement ("For those signs which have non-identical handshapes, one hand must remain static…") is exact at S094 PDF p. 8, and the S097 quotation is exact. The set issue is M1.
- H5: symmetry core (both hands moving means identical handshape and movement) at S094 PDF p. 7 and S097.
- H6: Prosodic Model four regions by eight distinctions (S095 PDF pp. 8–9), with the L5 caveats.
- H7: "fewer minimal pairs … based on orientation alone" (S095 PDF p. 9), exact.
- H8: S071 terms tab, dez, sig (tabula, designator, signation) and the Introduction quote "bring within the purview of linguistics a virtually unknown language" (archive.org full text), exact.
- H9: S096 "Stokoe argued that the handshapes, locations and movements in his model are all phonemes", exact.
- H10: S095 "non-manual behaviours … part of the phonology" (PDF p. 6), exact.
- H11: the failure mode "cross-linguistically rare" is supported in S097 (universally valid, few exceptions).
- H12: all five cited rows list the entry path in used-by (SOURCES `:100,:123–:126`).
- QUALITY 6: none of the five rows cited in section 5 is abstract-only or a publisher description. S094 and S095 were checked in body text; S096 and S097 are tier-B module pages and are used for secondary claims in their rows.
- Scope: section 5 has no canon decision and no clinical, education-policy or rights ruling.

## 4. Sources opened (access date 2026-10-22)

| # | URL | Result | Does the row's quote, tier and scope hold? |
|---|---|---|---|
| 1 | https://ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls (S094) | Direct fetch: HTTP 403. A managed headless Chromium tab (no relay, no login) rendered the same public URL as a 105-page PDF, "Sign Language Studies, Vol. 05, 1974". The same URL fetched from that tab returned HTTP 200, application/pdf, 553,422 bytes. Text extracted with pdftotext. | Quote holds (exact). Tier A holds (primary article body). Scope holds; pages wrong (L10); dominance set (M1); "A B S G O C" printing (M1). |
| 2 | https://ida.gallaudet.edu/sls/5/ | Landing page: Battison article is the first item; PDF 540 KB; repository date 1975 (volume is 1974). | Bibliographic line consistent. |
| 3 | https://api.crossref.org/works/10.1353/sls.1974.0005 | Metadata: Battison 1974, Sign Language Studies vol. 5, pp. 1–19, Project MUSE; abstract matches. | Consistent with S094 row. |
| 4 | https://web.archive.org/web/2025id_/https://ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls | HTTP 404. | Not usable. |
| 5 | https://digitalcommons.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls | DNS failure (getaddrinfo ENOTFOUND). | Not usable. |
| 6 | https://www.academia.edu/118766331/Phonological_Deletion_in_American_Sign_Language | HTTP 403. | Not usable. |
| 7 | https://www.deepdyve.com/lp/crossref/phonological-deletion-in-american-sign-language-N8BYdC32mh | HTTP 403. | Not usable. |
| 8 | https://www.jstor.org/stable/26203099 | "Client Challenge" page; no content. | Not usable. |
| 9 | https://muse.jhu.edu/article/507140 | Verification challenge; no content. | Not usable. |
| 10 | https://api.semanticscholar.org/graph/v1/paper/DOI:10.1353/sls.1974.0005?… | Tool error "Invalid URL format". | Not usable. |
| 11 | http://www.cslds.org/apsl-consortium/sign-linguistics/6-phonetics-and-phonology-minimal-pairs/ (S096) | Read in full. "Stokoe argued…" present; CAR/WHICH and ONION/APPLE listed as ASL pairs; SHORT and CAR cited to Battison 1978. | Quote holds. Tier B holds. Scope holds. A web search summary claimed this page has a PROPOSE/TEMPORARY table attributed to Battison 1974 with an ASL Signbank note. I read the page and grepped it: no "1974", "PROPOSE", "TEMPORARY" or "Signbank". I did not rely on that claim. |
| 12 | http://www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition/ (S097) | Read in full. Seven-item passive-hand list; "Out of the 45 possible handshapes in ASL, only 7 can appear as the passive hand"; "very few exceptions". | Quote holds. Tier B holds. Scope holds, but the entry's six-item citation fails (M1). |
| 13 | https://discovery.ucl.ac.uk/id/eprint/10054130/1/Brentari_Sign%20Language%20Phonology.book.chapter.pdf (S095) | Read in full (text conversion, 369 lines). Page markers used for citations. | Quote holds (exact). Tier A holds. Scope holds for the Prosodic Model; nonmanual cell (M2) and syllable-nucleus wording (L1) overreach. |
| 14 | https://archive.org/details/micro_IA41153455_0834 (S071 item) | Item page: "Sign Language Structure", Stokoe; ERIC microfiche; date shown 1978. | Identity confirmed. |
| 15 | https://archive.org/stream/micro_IA41153455_0834/micro_IA41153455_0834_djvu.txt (S071 full text) | Read via search of the 5,594-line text: Introduction quote exact (lines 667–670 of the read log); tab/dez/sig = tabula, designator, signation (lines 2637–2645); "Like consonant and vowel … action" (lines 2594–2595); "miscalled orientation" (lines 4841–4846); "Attempts at isolating orientation …" (lines 4912–4916); "similar examination of minimal pairs" (line 2764). | Quote holds. Tier A holds for Stokoe's terms. Scope: post-1960 commentary is present (M3). "Signification" wrong (L9). |
| 16 | https://cnlse.es/antiguos/Nonmanuals.their%20grammatical%20and%20prosodic%20roles.pdf (S098, used as the fix for M2) | Excerpts only (text search of the PDF): §2.1 articulator types; §2.3.1 headshake; §2.3.2 eyebrows for questions. | Not fully read. Supports the proposed fix. |
| 17 | https://www.joshiesworld.com/wp-content/uploads/2025/10/stokoe_1960.pdf (Gate-only; not in SOURCES) | Image-only PDF for my text tool: extraction incomplete for PDF pp. 1–41; search returned no matches (no text, so no evidence). | Not verified (L11). |

Two web searches were run. Their output is secondary and is not cited as evidence here.

## 5. Commands and tool calls (exit codes)

- `git log --oneline -4` (exit 0): HEAD `9feb69e`; then `da31d3c`, `35f0d49`, `1f97472`.
- `git ls-tree HEAD -- <entry> <SOURCES.md> <phonetics-phonology.md>` (exit 0): entry `b79c679…`, SOURCES `fff4c27…`, phonetics-phonology `65c68b7…`.
- `git hash-object <entry>` (exit 0): `b79c679…`, equal to HEAD.
- `command -v pdftotext pdfinfo mutool qpdf python3`; Python imports of pypdf and pdfminer; `uv --version` (exit 0 for the last command): present are pdftotext, pdfinfo, qpdf, python3 (/usr/bin); mutool absent; pypdf and pdfminer not installed; uv 0.13.0.
- `pdftotext -f 1 -l 30 -layout <Battison PDF> …txt` (exit 0): 766 lines.
- `pdftotext` per page, issue PDF pp. 3–8, then pp. 9–10, then pp. 11–12 (each exit 0).
- `pdfinfo <Battison PDF>` (exit 0): 105 pages; "Sign Language Studies, Vol. 05, 1974".
- Text search of the extracted article: matches at PDF p. 5 (four aspects), p. 6 (45 and 25; minimal pairs), p. 7 (Restrictions and symmetry), p. 8 (Dominance; six), p. 11 (A B S G O C, line 34–35).
- Page check of PDF pp. 3–6: title on p. 3; "Iconicity vs. Phonology" on p. 4; "Lexical Description" on p. 5.
- Search of the joshiesworld PDF: no matches (no text layer, as above).
- Search of the lane entry for `round-51`, `round51`, `boundary-count`, `lessons/`, `pastoralism` and `reports/round` (exit 0): the only match is `reports/round-28/readme/sweep.py` (line 10), which is not a forbidden string. Claim C's must-not-cite list is satisfied.
- Managed browser: open tab, screenshot, fetch of the PDF from the tab session (HTTP 200), close tab. The tab was released.
- Stokoe-text searches (archive.org text in the session read log): see row 15 above.
- Cleanup: scratch PDF, text files and screenshot in `/tmp` removed after writing this report.

## 6. Tooling record

- Installs or updates: none.
- Used as is: /usr/bin/pdftotext, pdfinfo, qpdf and python3 (poppler and Python already on the host); git, read-only subcommands only (no status, no index writes, no jj); omp's managed headless Chromium (no relay, no login, no stored cookies).
- Pacman: untouched.
- Downloads: none into the lane. The Battison PDF was read into `/tmp` and removed afterward.

## 7. Unrun checks, verification gaps and residual risk

- Unrun (not my assignment): `python3 -B reports/round-51/boundary-count.py`; `python3 -B reports/round-28/readme/sweep.py`; `find corpus/knowledge -name '*.md' | wc -l`; `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json`; `reports/round-51/claims-agree.py`.
- Access route for S094: the direct fetch returned 403. I used a managed headless tab to render the same public URL, then fetched that URL from the tab session. If the lane treats browser access to a bot-gated host as outside bounds, then M1, L4, L7, L10 and H1–H3 rest on an unverified copy and need a non-gated source.
- S098 was checked by excerpt only.
- The joshiesworld Stokoe copy could not be verified (L11).
- Stokoe's text was searched, not read in full (5,594 lines).
- I did not check sections 1–4 and 6–15 beyond the must-not-cite search. I did not check the other Gate S-rows.
- The web search summary about a PROPOSE/TEMPORARY table on the CSLDS Module 6 page was not confirmed by the page and is not used.
- Residual risk: the figures hold; the main risks are the orientation status (M3) and the missing calibration codes (M4). Both are fixable within section 5 plus two superseding SOURCES rows (S071 scope; S094 pages and the "A B S G O C" note). SOURCES is append-only, so those corrections must be new rows, not in-place edits.

## 8. Suggested fix order for the integration owner

1. Section 5 cells: M1 (six versus seven, with editions), M2 (nonmanual cell narrowed; S098 for functions), M3 (orientation status C, both sides), M4 (codes on every row).
2. Low items L1–L8, L12–L14 in section 5 and L9 in section 1 (`signation`).
3. Superseding SOURCES rows: S071 (scope note on the 1978 reprint's post-1960 commentary; `signation`; orientation critique), S094 (pages 5–6 and 9; the article-p. 9 "A B S G O C" printing).
4. L11: quote the registered Stokoe copy in the lesson Gate, or register the second URL in its own row.
5. Re-run the entry's own counters after the edit (not run here).
