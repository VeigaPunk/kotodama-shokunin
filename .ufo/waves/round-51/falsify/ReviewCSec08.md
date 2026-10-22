# ReviewCSec08: falsify attack on claim C, section 8

**Item attacked:** `corpus/knowledge/linguistics/sign-languages-manual-modality.md`, section 8 "Emergence, families and diachrony" (lines 122–131), and the registry rows it cites: S080, S104, S105, S106, S107, S108. Cross-checked because section 8 depends on them: S073 (`corpus/SOURCES.md:102`) and S087 (`corpus/SOURCES.md:116`).

**Seat:** KotodamaR51a3.ReviewCSec08. Leaf seat, read-only on the lane. No subagents, background jobs or sandboxes. No lane file edited.

**Lane state seen:** `git log` head is `9feb69e`, then `da31d3c` (claim C) and `35f0d49` (claim D). Untracked: `.ufo/waves/round-51/`.

"Gate" below means the round lesson's located-quote record (`corpus/lessons/round-51.md`). "teaches" is the registry column of that name.

## Verdict: FAILS (section 8 as written)

No source is invented. All six cited URLs resolved, and each registry quote is found in its source. The failures are in what the cells say the sources say:

- Row 2 calls the sign-language families "genealogical". The cited Glottolog pages and the lane's own S073 row say the opposite (finding 1).
- Four cells attribute wording to cited sources that do not contain it (findings 2, 5, 6, 7).
- The "about 25 years" figure is in its source, but it has no recorded quote and no date (finding 4).

I expect HOLDS-WITH-FIXES once findings 1–7 land. Findings 8–14 are fix-when-touched. The claim C verdict is the main agent's call.

## Scope coverage

- Section 8 cited rows opened and checked: 6 of 6 (S080, S104, S105, S106, S107, S108).
- Cross-check sources opened: S073 page, S087 PDF, Glottolog about page, and five Glottolog nodes (JSON or HTML).
- Not covered by this seat: the rest of the entry, the other sections' rows, and the counters (see Unrun checks).

## Commands run

| # | Command or call | Output (summary) | Exit |
|---|---|---|---|
| 1 | bash in lane: `ls -la corpus/`; `wc -l corpus/SOURCES.md`; `grep -n` on registry headings, piped to `head -80` | corpus listing; SOURCES.md is 251 lines; rows S071–S124 present | 0 (pipeline status; the first two commands' own status was not echoed; output complete) |
| 2 | bash in lane: `jj --ignore-working-copy log -r @ -n 1 \| head -5`; `git log --oneline -n 3`; `git status --short \| head -20`; `echo exit=$?` | working copy empty (`2e25676f`); heads `9feb69e`, `da31d3c`, `35f0d49`; `?? .ufo/waves/round-51/` | 0. `git status` is not on the read-only list and may refresh the index stat cache; no git write subcommand was run |
| 3 | bash in lane: `grep -n` for section-8 terms in the entry, piped to `cut` | matches at entry lines 58, 60, 126, 127, 131 | 0 (cut's status) |
| 4 | bash in lane: same terms over `corpus/SOURCES.md`, piped to `cut` | one match, line 117 (S088, "1817") | 0 (cut's status) |
| 5 | bash in lane: same terms over `corpus/lessons/round-51.md`, piped to `cut` | no matches (grep's own status 1 is hidden by the pipe) | reported 0 (cut's status) |
| 6 | bash in lane: `grep -n` for S073–S108 ids in the entry, piped to `cut` | lines 20, 127–131 | 0 (cut's status) |
| 7 | bash in lane: `realpath -m .ufo/waves/round-51/falsify`; `ls -ld` on it | canonical path equals the lane path (no symlink); directory exists | 0 |
| 8 | grep tool on `corpus/lessons/round-51.md` (S07x–S12x and section-8 terms) | Gate lines 37 (S080), 61–65 (S104–S108); line 88 (S080 kept at tier B) | n/a |
| 9 | grep tool on the Perseus XML text for `422` and `ἐνεο` | line 1416 (section 422); line 1452 (milestone 422e) | n/a |
| 10 | read tool, local: `skill://godspeed`; `/home/vgpnk/.omp/agent/RULES.md`; `reports/round-51/claims.json`; `corpus/QUALITY.md`; `corpus/SOURCES.md:1-25`, `:155-210`, `:116`; `corpus/knowledge/verification/calibration-registry.md:30-40`; `round-51.md:65`; the entry in full | read as stated | n/a |
| 11 | read tool, remote: the URLs in the table below | each returned the stated content | n/a |

Tooling: RULES.md read. No installs. No pacman, sudo or package managers used.

## Sources opened (all 2026-10-22; none failed)

| URL | Type | What it says at the anchor | Row check |
|---|---|---|---|
| https://pubmed.ncbi.nlm.nih.gov/15375269/ (S080) | PubMed abstract (NCBI) | "A new sign language has been created by deaf Nicaraguans over the past 25 years …" and "Successive cohorts of learners extended this procedure, transforming Nicaraguan signing from its early gestural form into a linguistic system." | Gate quote holds exactly. Tier B holds (abstract only). The 25-year sentence is recorded nowhere. "peer", "re-analysis" and "regularized" are absent. |
| https://glottolog.org/resource/languoid/id/lsfi1234 (S104) | Glottolog HTML | Heading "Pseudo Family: LSFic". Tree collapsed. | Heading holds. "FSL and ASL classify under it" is not shown on this page (see lsfi1234.json below). |
| https://glottolog.org/resource/languoid/id/amer1248.json (S105) | JSON | classification: Sign Language (sign1238) → L1 Sign Language (deaf1237) → LSFic (lsfi1234) → ASLic (asli1244) → American Sign (amer1258). Category "Sign Language". | Array holds. "genealogical placement" and "lineage" are not shown: the array shows membership only. |
| https://glottolog.org/resource/languoid/id/bsli1234 (S106) | Glottolog HTML | Heading "Pseudo Family: BSLic". Comment: "The BANZSL subgroup is argued by Adam Schembri … (2010) and Johnston, Trevor (2003)." Lexicostatistics (Johnston & Schembri 2007; Woll 1987) and history (Woll et al. 2001; Kyle & Woll 1985) attach to the BSLic core and to BSL's origin. | Quote holds. "argued on lexical and historical evidence" is not what the BANZSL sentence says. |
| https://glottolog.org/resource/languoid/id/banz1243.json (S107) | JSON | newick: BANZSL → Auslanic (Auslan, Fiji SL, PNG SL, Solomon Islands SL), British Sign Language, New Zealand Sign Language. Category "Pseudo Family". Classification ends at BSLic. | Quote holds. The §8 membership list is partial. |
| https://raw.githubusercontent.com/PerseusDL/canonical-greekLit/master/data/tlg0059/tlg005/tlg0059.tlg005.perseus-grc2.xml (S108) | TEI XML; editor John Burnet (Platonis Opera, Clarendon 1905) | line 1452, milestone 422e: "… εἰ φωνὴν μὴ εἴχομεν μηδὲ γλῶτταν … ἆρʼ οὐκ ἄν, ὥσπερ νῦν οἱ ἐνεοί, ἐπεχειροῦμεν ἂν σημαίνειν ταῖς χερσὶ καὶ κεφαλῇ καὶ τῷ ἄλλῳ σώματι;" | Quote holds exactly. Tier A holds for the Greek text. The row omits the clause "ὥσπερ νῦν οἱ ἐνεοί" ("as the speechless do now"). |
| https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Crat.:page=422 | Perseus HTML; Fowler translation (Loeb, 1921) | 422e: "should we not try, as dumb people actually do, to make signs with our hands and head and person generally?" | The Gate's second URL for S108. No SOURCES row registers it. |
| https://glottolog.org/glottolog/glottologinformation | Glottolog about page | "In addition to the genealogical trees (families and isolates), … the following non-genealogical trees: … Sign Language." "For signed languages, such a methodology remains to be articulated." Sign languages are "classified on a weaker theoretical basis." | Not a registered row. Decisive for the S073 and S105 scopes. |
| https://glottolog.org/resource/languoid/id/sign1238 (S073) | Glottolog HTML | Heading "Pseudo Family: Sign Language". | Heading holds. The phrase "genealogy not established" is not on this page; the closest verbatim statement is on the about page. The scope "genealogical classification" fails. |
| https://glottolog.org/resource/languoid/id/lsfi1234.json | JSON | category "Pseudo Family". newick places ASLic → American Sign → ASL and French Sign Language (fren1243) under LSFic. child_language_count 59. | Supports S104's children claim. S104 does not cite it. |
| https://glottolog.org/resource/languoid/id/fren1243.json | JSON | classification: Sign Language → L1 Sign Language → LSFic. | Supports "FSL classifies under LSFic". |
| https://glottolog.org/resource/languoid/id/asli1244 | Glottolog HTML | Heading "Pseudo Family: ASLic". | ASLic is also a pseudo-family, on the ASL path. |
| https://glottolog.org/resource/languoid/id/amer1248 | Glottolog HTML | Heading "Sign Language: American Sign Language". Comments discuss ASL provenance (Supalla & Clark 2015; Woll et al. 2001). No comment on the LSFic placement. | The LSFic link rests on the classification alone. |
| https://linguistics.stonybrook.edu/faculty/mark.aronoff/files/Emerging%20sign%20languages.pdf (S087, cross-check) | PDF author manuscript (Meir, Sandler, Padden & Aronoff), converted by markit | PDF p. 7: Woodward (1978) found "between 50-60%" of ASL and LSF vocabulary "identical or similar", and "argued that other sign languages in America … must have played a role in the emergence of ASL." PDF pp. 7–8: "Within two decades" after the 1977 school, a common language formed from intermingled home sign systems and "possibly" visiting signers. PDF p. 10: NSL "dating from the founding of the Managua deaf school in 1977." PDF p. 12: "Language interference from the spoken language" (Adamorobe "sign supported Akan"; mouthing). | Supports §3's "NSL since 1977". Contradicts treating ASL's ancestry as settled. Shows spoken-language influence. |

## Findings

Severity is HIGH, MEDIUM or LOW. Line numbers are the entry's unless marked.

**1. HIGH: §8 calls the sign-language families "genealogical".**
- Where: entry line 127 ("Genealogically to other signed languages, not spoken neighbours …"). Scope cells: `SOURCES.md:134` (S105, "ASL's genealogical placement") and `SOURCES.md:102` (S073, "genealogical classification").
- Evidence: the Glottolog about page lists the Sign Language tree among its non-genealogical trees and says the method for signed languages "remains to be articulated." LSFic, ASLic and BSLic/BANZSL carry the "Pseudo Family" category (sources 2, 4, 5, 12). The lane's own S073 row already says "genealogy not established" (`SOURCES.md:102`). S087 PDF p. 7 records Woodward's argument that other American sign languages shaped ASL, and §8 leaves that out. The calibration registry (`calibration-registry.md:36`, code C) says a contested reading must not be reported as settled. "Not spoken neighbours" is not shown either: membership in a sign-only tree does not establish that there was no spoken input.
- Smallest fix: replace row 2 with: "What do they belong to? | Glottolog places ASL inside LSFic, a pseudo-family named for French Sign Language. Glottolog calls its sign-language classification non-genealogical and says its method 'remains to be articulated' (C). Woodward (1978) found 50–60% of ASL and LSF vocabulary identical or similar and argued that other American sign languages also shaped ASL (S087, PDF p. 7) | S104, S105, S087, plus a new row for the Glottolog about page | C". Add superseding rows that narrow the S073 and S105 scopes to Glottolog's catalogue placement (QUALITY criterion 6, `QUALITY.md:29`; no in-place scope edit).

**2. MEDIUM: §8 row 3 gives BANZSL an evidence type its source does not give.**
- Where: line 128 ("argued on lexical and historical evidence"); also `SOURCES.md:135` (S106 teaches).
- Evidence: the anchored comment names two authors for BANZSL and states no evidence type. The lexicostatistics and history it reports belong to the BSLic core and to BSL's origin. Tier A is over-scoped for a catalogue's summary of other people's evidence (`QUALITY.md:29`).
- Smallest fix: "BANZSL is argued by Schembri et al. 2010 and Johnston 2003 (Glottolog comment; evidence type not stated there)." Move the lexicostatistics and history to the BSLic core. If the evidence claim stays, add a tier B superseding row for it.

**3. MEDIUM: pseudo-family flags and calibration codes are uneven or missing.**
- Where: line 127 flags LSFic as a pseudo-family. Line 128 does not flag BSLic or BANZSL, which Glottolog also catalogues as pseudo-families (sources 4, 5). ASLic on the ASL path is one too (source 12). Section 8 has no calibration code on any row. QUALITY criterion 2 (`QUALITY.md:9`) requires a status on framework entries.
- Smallest fix: name the pseudo-family status for every node in the chain. Add code C with the reason: no established method for sign-language genealogy, per the about page.

**4. MEDIUM: the "about 25 years" figure is correct in its source but unrecorded and unscoped.**
- Where: line 126.
- Evidence: the PubMed abstract says "over the past 25 years" (2004 publication). But (a) the sentence is not in S080's teaches (`SOURCES.md:109`) or in the Gate for S080 (`lessons/round-51.md:37`, which quotes only the "Successive cohorts" sentence), so the number has no located quote in the record; (b) the entry gives no date, although calibration code B asks for the period (`calibration-registry.md:37`); (c) §3 line 60 dates NSL from 1977, and S087 says the common language formed "within two decades" after the school (PDF pp. 7–8, 10). §3 and §8 give two NSL timeframes without reconciling them.
- Smallest fix: "Nicaraguan Sign Language was created 'over the past 25 years', as of the 2004 abstract (B); S087 dates the school to 1977 and the common language to 'within two decades' (PDF pp. 7–8)." Add the 25-year sentence as a located quote in the S080 Gate.

**5. MEDIUM: "peer learning" and "a school or village generation" are credited to S080 without support.**
- Where: line 131.
- Evidence: the abstract says that in the first cohort's "initial creation of the language, children analyzed complex events into basic elements and sequenced these elements into hierarchically structured expressions." Neither "peer" nor "school or village generation" appears in it.
- Smallest fix: "the first cohort of child learners, whose early signing analysed events into basic elements and sequenced them (S080 abstract)." Drop "peer" and "school or village generation" unless a located source is added.

**6. MEDIUM: "re-analysis" and "regularized grammar" are credited to S080 without support.**
- Where: line 131.
- Evidence: neither word is in the abstract. The abstract says successive cohorts "extended this procedure."
- Smallest fix: "later cohorts extended the same segmentation and sequencing (S080 abstract)."

**7. MEDIUM: the Plato row drops the passage's own comparison and calls a hypothetical "attestation."**
- Where: line 129 and `SOURCES.md:137` (S108 teaches).
- Evidence: the Greek (line 1452) reads "ὥσπερ νῦν οἱ ἐνεοί" ("as the speechless do now"). Fowler renders it "as dumb people actually do" (second URL, above). The row omits this clause. The heading "Deep attestation" uses a documentary term for a hypothetical. "Not evidence of a Greek signing community" is the lane's reading, with no source and no code.
- Smallest fix: rename the heading "Early mention (hypothetical)"; quote the comparison clause; code the reading H (`calibration-registry.md:38`).

**8. LOW: "never the ambient spoken language" is an absolute with no source.**
- Where: line 131.
- Evidence: S104 and S106 do not say it. S087 PDF p. 12 documents spoken-language influence (Adamorobe "sign supported Akan"; mouthing and loan translations).
- Smallest fix: drop "never." Record spoken-language influence (mouthing, word order, loan signs) on its own line, coded H.

**9. LOW: S104's children claim goes beyond its anchor.**
- Where: `SOURCES.md:133`. It says FSL and ASL "classify under" LSFic. Its only anchor is the page heading, which does not show that. The children are in lsfi1234.json and fren1243.json (sources 10, 11), which S104 does not cite.
- Smallest fix: add the lsfi1234.json newick as a located quote in the S104 Gate (`lessons/round-51.md:61`). The teaches column cannot change in place; supersede the row if the claim changes.

**10. LOW: a Gate URL with no registry row.**
- Where: `lessons/round-51.md:65` quotes a second S108 URL (Perseus HTML, Fowler). The SOURCES preamble says the Gate holds each row's URL, and no row registers this one.
- Smallest fix: register the Perseus page as a new row, or remove it from the Gate.

**11. LOW: partial BANZSL membership.**
- Where: line 128 lists BSL, Auslan and NZSL only. banz1243.json has six child languages, including Fiji, Papua New Guinean and Solomon Islands sign languages under Auslanic (source 5).
- Smallest fix: write "including", or list all six.

**12. LOW: row scope is wider than the evidence.**
- Where: row 1, "How do sign languages arise?" (line 126), answers from one case. Row 2 (line 127) generalizes from ASL and BSL to all sign languages.
- Smallest fix: retitle the rows "How did Nicaraguan Sign Language arise?" and "What do ASL and BSL belong to?"

**13. LOW: "not from nothing" has no source in S080.**
- Where: line 126. S087 PDF pp. 7–8 supports the idea: home sign systems intermingled, possibly with visiting signers.
- Smallest fix: cite S087 for the gloss.

**14. LOW, outside section 8 (for the integrator).**
- (a) Line 16: "does not derive from any spoken language (S071; S072)." Neither anchor says so. S071 (`SOURCES.md:100`) is quoted as "bring within the purview of linguistics a virtually unknown language"; S072 (`SOURCES.md:101`) is a publisher description about asking the same questions.
- (b) Line 20: "(S071; S073)" for "emergent village/shared sign systems." S073 (`SOURCES.md:102`) does not mention emergence.
- (c) Line 60: "NSL since 1977 (S087)." Supported by S087 PDF pp. 7 and 10, but the S087 row (`SOURCES.md:116`) does not carry the date (a records gap).

## Residual risk and verification gaps

- The Senghas et al. 2004 full text was not opened (Science; paywalled; no bypass). "Peer", "re-analysis" and "regularized" may appear in the full paper. Findings 5 and 6 concern the anchored claim, so they stand as written.
- Not opened, because they are not registered rows: Woodward 1978; Schembri et al. 2010; Johnston 2003; Johnston & Schembri 2007; Woll et al. 2001; Kyle & Woll 1985. The BANZSL evidence type is therefore unverified at source.
- S087 is an author manuscript converted by markit. Its PDF page numbers are the converter's markers, not the printed pages.
- The Glottolog pages are live. The LSFic tree is collapsed in the HTML, so child relations were read from JSON.
- The S073 phrase "genealogy not established" is not on the page I opened.

## Unrun checks

- `find corpus/knowledge -name '*.md' | wc -l` (claim C count): not run by this seat.
- `python3 -B reports/round-28/readme/sweep.py` (claim C sweep): not run by this seat.
- `python3 -B reports/round-51/boundary-count.py` (claim D count): not run by this seat.
- `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json`: not run by this seat.

These are outside section 8 and were not assigned to this seat.

## Tooling and lane discipline

- No installs. No pacman, sudo or package managers. RULES.md read before any tool use.
- No lane file edited. No sandbox or clone. No read of `reports/round-51/calibration/` or of any `/fast/scratch` path.
- This report is the only file written. Its absolute path was checked with `realpath` before writing.
