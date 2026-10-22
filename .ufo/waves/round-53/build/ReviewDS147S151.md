# ReviewDS147S151 — claim D falsifier, entry lines 76 and 79 (S147, S146, S151 re-opened)

Author-lane advice, not admission. Seat: leaf, no subagents. Report path per trailer.
Axes (godspeed): A1 source fidelity (each row re-opened by ordinary means, verbatim quotes with locations); A2 clause audit (every clause on entry lines 76 and 79 checked against the re-opened rows); A3 falsifier verdict (what a repaired line must and must not say for claim D to hold).

No language server applies here (corpus markdown plus external PDFs; no code symbols): semantic checks are by direct re-open of the sources; text grep was used only to locate the S146/S147/S151 rows in corpus/SOURCES.md and the routed strings in the entry. Tooling installs: none (curl and poppler already present; nothing installed or upgraded).

## 1. Routes (all opened 2026-10-22, ordinary means only)

- **S147** — `curl` direct to http://www.icphs2007.de/conference/Papers/1286/1286.pdf → 4-page PDF (337,860 bytes). Printed page numbers 838 and 839 confirmed in the page footers (pdftotext per page); paper spans proceedings pp. 837–840, matching the S147 SOURCES row anchor (`corpus/SOURCES.md:176`). Direct route; no challenge met.
- **S146** — `curl` direct to https://www.isca-archive.org/interspeech_2005/meyer05_interspeech.pdf → 4-page PDF (237,362 bytes), DOI 10.21437/Interspeech.2005-36. The text layer shows no printed page numbers; locations below are by section and PDF page (Turkish §3.1.2 = PDF p. 2; consonants §3.2.1 = PDF p. 3). Direct route; no challenge met.
- **S151** — `curl` direct to https://archive.mpi.nl/tla/islandora/object/lat%3A1839_00_0000_0000_0016_B509_0 → deposit page CAM20459 (HTML). The parent collection page (lat%3A1839_00_0000_0000_0016_B4F7_7, "Sochiapam Chinantec Whistled Speech") was also fetched for completeness. Direct route; no challenge met, no Wayback needed.

Pre-landing counter state observed this session, from the lane root: `python3 -B reports/round-53/d-count.py` prints `OPEN 18`, `SID_BAD 0 [] cited 50`, exit 1 — exactly the declared before value in reports/round-53/claims.json, with OVER3 at entry line 76 and OVER4 at entry line 79.

## 2. S147 (Meyer 2007, ICPhS XVI paper 1286) — what it says about Turkish whistled consonants

All quotes verbatim from the PDF text layer read down their own column (the two-column layout interleaves in naive extraction; `pdftotext -layout` confirms each fragment's position).

1. Which stop merges with which — **[p] with [k], and only [p]**. P. 839, §3.1.1: "The occlusive [p] is expressed mainly with this process and is therefore very similar to [k] in whistles." The preceding sentence names the process: "the fixed lips modify the labial articulation of [m], [p] and [b] which all use in compensation a glottal occlusion" (p. 839, §3.1.1). So [b] shares the glottal-occlusion compensation with [m] and [p]; no merger of [b] with [k] is stated anywhere. Figure 4 caption (p. 839): "Turkish syllables /kom-jun-kop/ recorded near the whistler: the use of the glottal constriction for [m] and [k] is visible."
2. [b]'s other treatment — intermediate, not merged. P. 839, §3.1.1: "Some consonants are more difficult to classify because they bear intermediate positions between two of these categories, like [n], [b], [v] and [f]."
3. Consonants as modulations and gaps. P. 839, §3: "Whistled consonants are modulations in frequency and amplitude of the simple signal of a whistle." and "When the amplitude modulation shuts off the whistle, consonants are also characterized by silent gaps." Note for the "silence for stops" clause: §3.2.1 (p. 840) measures stops as onsets, not silences — "the five consonants /t/, /d/ and /k/, /p/, /g/ bear systematically a very rapid and clear first peak amplitude onset".
4. Vowels and harmony (entry cell 1). P. 838: "Such a complex vocalic system of eight whistled frequency intervals highlights four groups" and "The four inter-syllabic relations created by harmony rules simplify the vowel identification of the four whistled statistical groups of vowel frequencies." Four groups is S147's number.
5. Nothing about learning age. Chinantec appears in S147 only in the §1 strategy typology (p. 837): "in most tone languages (like Mazatec, Chinantec, Akha, Hmong) whistling selects primarily Fo cues carrying tone registers and tone contours". No children, no acquisition claim.

## 3. S146 (Meyer 2005, Interspeech) — what it says about Turkish

1. Eight bands, **three** groups. §3.1.2 (PDF p. 2): "The 8 vowels of Turkish (i, y, 1, e, 9,a, o, u) are whistled in 8 bands of frequencies decreasing in pitch" and "grouped in three reductive groups of bands as follows: [(i, y, 1, u), (e, 9),(a, o)] centered respectively on 2600, 2100 and 1600 Hz".
2. Harmony. §3.1.2: "The influence of vowel harmony rules of Turkish help the whistlers to get rid of some ambiguities."
3. Consonants: no Turkish-specific stop-merger statement, and **/b/ is not named anywhere in S146** (no [b] token in the text layer). §3.2.1 (PDF p. 3): "The main categories of whistled consonants described in Silbo and Turkish are still available in Greek. The occlusive stop consonants can be grouped in three types of loci movements: [P, T, K] equivalent to those of the formant 2 of spoken speech." Voicing is kept differently: "The voicing is sometimes reproduced by a slight continuation in the amplitude." (§3.2.1).
4. Learning, and who was recorded. Abstract (PDF p. 1): listeners recognize "if they have overcome a long period of learning" — a listener-learning claim about whistled languages generally, not an acquisition-age claim, and S146 never mentions Chinantec. §2 (PDF p. 1): "It relies on data of male adult whistlers (women and children have a higher pitch)." — corpus composition of the 2005 fieldwork, not acquisition.

## 4. S151 (MPI deposit CAM20459) — who was recorded, and whether anything says "learned young"

- The deposit page (Details → Description) says exactly: "David Yetman and Mark Sicoli elicit spoken and whistled Chinantec from children in San Pedro Sochiápam" (the collection listing view shows the same sentence with a final period). Persistent identifier https://hdl.handle.net/1839/00-0000-0000-0016-B509-0. Breadcrumb: MPI-PL Archive > Language and Cognition > mesoamerica > Otomanguean > Sicoli > Sochiapam Chinantec Whistled Speech > CAM20459. Automatic citation: '[author(s)] (2011). Item "CAM20459" in collection "Sicoli". The Language Archive.'
- Who was recorded: children, as the consultants from whom spoken **and whistled** Chinantec was elicited, at San Pedro Sochiápam. The page locates the event, not the children's provenance — "of the village" is the entry's addition, though the parent collection's sibling sessions make it comfortable: "David Yetman and Mark Sicoli discuss Sochiápam Chinantec Language and Culture and elicit some whistled speech from children." and "…discuss Sochiápam Chinantec Language and Culture while walking with children of Sochiápam." (parent collection page, session descriptions).
- Learned young: **nothing on the deposit page or the parent collection page says the register is learned or transmitted young.** The words learn, young, acquisition, transmitted have zero hits on either page. The parent collection description is only: "Archive for NSF Rapid NSF1126027 "Documenting Whistled Speech among Chinantecans" PI David Yetman, Co-PI Mark Sicoli." That children can produce the register shows use by children; it does not state an acquisition age, still less the norm that the register is learned young.

## 5. Clause-by-clause audit of entry line 76 (Whistled Turkish row)

Current line 76 (`corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:76`), cited rows S147 and S146 (distance cell cites S148; S149 — not re-opened in this scope).

Carried by the re-opened rows:
- "eight vowels as eight pitch bands" — S147 p. 838 (eight intervals) and S146 §3.1.2 ("8 bands of frequencies decreasing in pitch"). Both.
- "disambiguated by vowel harmony" — S147 p. 838 (§2.2) and S146 §3.1.2. Both.
- "consonants as frequency and amplitude modulations" — S147 p. 839 §3 verbatim; S146 §1.1 generally. Both.
- "band overlap between vowels" — S147 p. 838 ("intervals … that overlap a lot"); S146 §3.1 ("As these bands sometimes overlap"). Both.

Not carried:
1. **"/b/ … merging with /k/ in the whistle (S147)"** — the routed defect OVER3, still present at the worktree. S147 states the similarity to [k] for [p] only (p. 839 §3.1.1); [b] is named only for glottal-occlusion compensation shared with [m] and [p], and for intermediate classification ([n], [b], [v], [f]). S146 never names /b/. No re-opened page carries a /b/–/k/ merger. A repaired line must attribute the merger to /p/ alone (or mark (to-verify)).
2. **"in four groups" as a joint (S147; S146) claim** — S146 says three reductive groups [(i, y, 1, u), (e, 9), (a, o)] (§3.1.2); "four groups" is S147-only. Review note, not a routed defect: the repaired line should hang the group count on S147 alone, or say "three-to-four statistical groups" (the S146 row's own teaches wording), so the dual citation is honest.
3. **"silence for stops"** — carried only loosely by S147 §3's silent-gaps sentence, which is about consonants generally when amplitude shuts off; §3.2.1 measures stops as rapid onset peaks. Not carried by S146 at all. Compression, review note only.
4. **"lip-locked"** — neither page says "lip-locked"; both describe fixed lips (S147 p. 839 "the fixed lips modify the labial articulation…"; S146 §3.2.1 "When the jaws are fixed by the finger and/or the tighten lips"). Acceptable compression; flag only.

## 6. Clause-by-clause audit of entry line 79 (Chinantec row), cell 3

Current cell 3: "Oaxaca; the archive deposit was made with children of the village, so the register is learned young (S151)".

Carried:
- "the archive deposit was made with children" — the Description sentence quoted in §4 (elicitation from children). "of the village" is an addition the page does not state for the children themselves (it names the place of the event); the sibling sessions ("children of Sochiápam") support it if the parent page is counted in the row's scope — the S151 row's anchor names only the deposit page, so strictly the phrase rides on the sibling descriptions.
- "Oaxaca" — the deposit page says "San Pedro Sochiápam" but not the state; "Oaxaca" comes from the row's own scope text, not the page.

Not carried:
- **"so the register is learned young (S151)"** — the routed defect OVER4, still present at the worktree. Neither the deposit page nor the collection page makes any acquisition-age or transmission claim (zero hits, §4). The page supports only: a Sochiapam Chinantec deposit exists in which spoken and whistled Chinantec was elicited from children. A repaired line must drop "learned young" or mark it (to-verify).
- Row-level note: corpus/SOURCES.md:180's S151 teaches cell ends "— the register is transmitted young", the same inference the routed repair targets. If the entry must mark or drop it, the row's teaches cell carries the identical over-read and the integrator should treat the two together.

Cells 1–2 of line 79 cite S135, which is outside this seat's re-open set (ReviewDS135's scope); no verdict here.

## 7. Falsifier verdict for claim D (this scope)

- The pre-landing counter value is exactly the declared before value (OPEN 18, SID_BAD 0, exit 1), so the claim's baseline measurement is reproducible as stated.
- Neither routed wording survives contact with its cited page: the /b/–/k/ merger is contradicted by S147's [p]-only statement plus [b]'s intermediate classification, and "learned young" has no support on S151's pages. The D repair MUST alter both clauses; if the landed line 76 still asserts /b/ merging with /k/, or line 79 still asserts "learned young", without a (to-verify) mark, that is a claim-D falsifier on the evidence re-opened here.
- No S187+ id, gesture entry, or round-53 lesson is cited on lines 76 or 79 (only S147; S146; S135; S151; S148; S149), so the must-not-cite constraint is respected in this scope.

Suggested supported wording (advice): line 76 drops cell: "band overlap between vowels, and lip-rounded /p/ near-identical to /k/ in the whistle through glottal-occlusion compensation, [m], [p], [b] so compensated (S147)"; line 79 cell 3: "Oaxaca; deposit CAM20459 records Yetman and Sicoli eliciting spoken and whistled Chinantec from children in San Pedro Sochiápam (S151); acquisition age (to-verify)".

## 8. Residual risk and unrun checks

- S148/S149 distance figures on line 76 and the S135 cells on line 79 were not re-opened here (other seats' scope).
- S146 printed page numbers are absent from the PDF text layer; locations given by section and PDF page. The ISCA metadata page for the DOI could confirm proceedings pagination — unrun.
- No second independent source for the [p]–[k] similarity was re-opened (S146 gives [P, T, K] locus classes but no merger); the S147 figure rests on the 1967 Busnel expedition and 2003 recordings.
- The quote "in most tone languages (like Mazatec, Chinantec, Akha, Hmong) whistling selects primarily Fo cues…" renders F0 as "Fo" as printed; quoted as printed.
