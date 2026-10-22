# Residual falsify check — claim C, rows S279–S284 ( KotodamaR54a2.ReviewRows279to284 )

2026-10-22. Lane commit checked: `6a658ca4fe9230f70eaa3b421e6c9d78da5c1633` ("round-54: claim C lands"). Worktree bytes = commit bytes for both cited lands (md5 entry `ea9eec0c…`, SOURCES `17b068ac…` in commit == worktree). Attack only; nothing modified in the lane. Fetch artifacts: `/fast/scratch/hyaku/kotodama-r54-a2/ReviewRows279to284/`. No tool installs (used stock `curl`, `python3`, `pdftotext` 3.x already at /usr/bin). All six URLs re-opened by ordinary means in this session: four direct plain requests (HTTP 200), one direct PDF download (HTTP 200 `application/pdf`), and for S283 the direct PDF (HTTP 403 — challenge met, not passed, reproduced) plus both Wayback captures the row names (PDF `20230523044652if_`, 12,306,262 bytes; landing `20240603102111id_`).

Citing sentences audited: 10, at masks-masquerade.md lines 114 (×2), 115 (×2), 140 (×3), 145 (×3).

## S279 — LSJ, πρόσωπον (SOURCES.md:308)

- Verdict: **CARRIED** (both sentences).
- Entry lines: `corpus/knowledge/culture-material/masks-masquerade.md:114`.
- Row: `corpus/SOURCES.md:308` — book, A, mined, used-by names the entry.
- Page says: sense I "face, countenance … always in pl."; sense III "= προσωπεῖον, mask, D.19.287"; under III "of the Roman imagines, Plb.6.53.5; bust or portrait"; sense IV "προσώπῳ, οὐ καρδίᾳ in person, in bodily presence, 1 Ep.Thess.2.17" (Perseus hopper, entry pro/swpon, fetched HTTP 200 today).
- Check: "first face … mask third … imagines under III … fourth sense person/in bodily presence" — sense ordering I→II→III→IV matches the page exactly; the entry's two sense locators are right.
- Kind/tier vs QUALITY 6: book/A compliant — standard critical lexicon is primary for attested senses; tier note correctly withholds authority over ritual practice.
- Smallest fix: none.

## S280 — Lewis & Short, persōna (SOURCES.md:309)

- Verdict: **CARRIED** (three citing clauses: line 115 ×2, line 140).
- Entry lines: `masks-masquerade.md:115`, `:140`.
- Row: `corpus/SOURCES.md:309` — book, A, mined.
- Page says: bracket before sense I "acc. to Gabius Bassus ap. Gell. 5, 7, 1 sq., from per-sŏno, to sound through"; sense I "covered the whole head, and was varied according to the different characters"; II.B example list, Sen. Ben. 2, 17, 2 "hanc personam induisti: agenda est"; II.B.2 (γ) "a being having legal rights and obligations (including the state, etc.; not including slaves" (Perseus hopper, entry persona, HTTP 200 today).
- Check: line 115's "whole head, varied by character … once assumed must be acted" — carried by I and the II.B Seneca quotation; line 115's "exclusion in the same clause" is verbatim the parenthetical; line 140's "report the derivation as Gabius Bassus's … not as their own finding" is exactly the "acc. to" bracket. Locator II.B.2 matches the page's numbering (2, item γ, law). Row's scope cell "material and mouth-opening detail" also verified (clay/bark; "The opening for the mouth was very large").
- Kind/tier vs QUALITY 6: book/A compliant; tier note honestly limits A to senses and to the dictionary's attributed reporting, not the derivation's truth.
- Smallest fix: none.

## S281 — Gellius, Noctes Atticae 5.7, LacusCurtius (SOURCES.md:310)

- Verdict: **CARRIED**.
- Entry line: `masks-masquerade.md:140`.
- Row: `corpus/SOURCES.md:310` — book, A, mined.
- Page says (penelope.uchicago.edu book 5, HTTP 200 today): chapter heading "How cleverly Gavius Bassus explained the word persona"; 5.7.1 "Cleverly, by Heaven! and wittily, in my opinion, does Gavius Bassus explain the derivation"; 5.7.2 "shut in on all sides … clearer and more resonant", "the o being lengthened".
- Check: "Gellius calls it clever and witty (S281, 5.7.1)" — both words in 5.7.1; locator exact.
- Kind/tier vs QUALITY 6: book/A compliant; tier note correctly refuses support for Gellius's exact Latin (translation only, not opened in a Latin edition).
- Smallest fix: none.

## S282 — Nasser & Beccari 2025, Estudos Linguísticos (SOURCES.md:311)

- Verdict: **CARRIED**.
- Entry line: `masks-masquerade.md:140`.
- Row: `corpus/SOURCES.md:311` — paper, B, mined.
- Page says (PDF re-downloaded direct today, HTTP 200 `application/pdf`, 16 pages, pp. 721–736): Resumo, p. 721 "Este artigo apresenta uma etimologia antiga possível nas Noites Áticas (Noctes Atticae)".
- Check: "a 2025 study files it as ancient etymology (S282, Resumo, p. 721)" — abstract is on the printed p. 721 (folio in the page footer), says exactly that; entry's calibration strength ("state it only as an attributed ancient argument") does not exceed the source. Row's other evidence quotes (Gávio Basso; "o vocábulo 'máscara' (personae) é influenciado pelo uso do objeto na realidade"; "lastro do nome … persona") found in the PDF text, position consistent with p. 728.
- Kind/tier vs QUALITY 6: paper/B compliant — this is criterion 6's exact case: the cited support is the article's abstract ("publisher descriptions and abstracts are tier B"), and B is sufficient here, not sole-support-restricted (that is C only).
- Smallest fix: none.

## S283 — Neveu 2010, "The Space of the Mask" (SOURCES.md:312)

- Verdict: **CARRIED** (both citing sentences).
- Entry lines: `masks-masquerade.md:145` (×2).
- Row: `corpus/SOURCES.md:312` — paper, A, mined.
- Page says (Wayback PDF `20230523044652if_`, opened today): p. 149 chapter opening "During the carnival season, masking was regulated and required for entry into interior public spaces such as ridotti (gaming halls) and theaters."; p. 155 "a law from 1732 required patrons to mask their faces and their clothing when attending the theater, specifically with the bauta e tabarro"; p. 155 "The white mask allowed the wearer to speak freely … the wearer was unable to speak."
- Check: both p. 155 locators sit between the printed folios 154 and 156 in the extracted text; the chapter opening is the first page of the chapter (repository metadata: pages 149–168), consistent with the row's honest pagination note ("149–163 in the repository PDF; landing page gives 149–168" — the landing's Recommended Citation indeed reads 149-168 and the last extracted folio is 163). The entry attributes the 1732 law to Neveu's account, which matches the tier note's B carve-out for the law's archival warrant — no over-read. Access route honest: direct PDF 403 reproduced today (bot interstitial, challenge met, not passed); both named Wayback captures open.
- Kind/tier vs QUALITY 6: paper/A claim-scoped compliant — author's own published chapter, authoritative for its documented statements; the archival-warrant carve-out is recorded in the row, and the entry does not cite the decree itself.
- Smallest fix: none.

## S284 — MUVE "Forma per maschera Bauta" (SOURCES.md:313)

- Verdict: **CARRIED**.
- Entry line: `masks-masquerade.md:145`.
- Row: `corpus/SOURCES.md:313` — docs, A, mined.
- Page says (visitmuve.it, HTTP 200 today): sentence 2 "la bauta era quella che aveva il maggior permesso di vagare per calli e campi … quando le altre maschere erano bandite"; sentence 4 "il labbro superiore deformato ed allungato in modo da deformare anche la voce di chi la indossa".
- Check: entry's "widest permission to roam when other masks were banned" and "its upper lip deformed the wearer's voice" with locator "sentences 2 and 4" — both quotes verified and the sentence counts check out (1 "Comparve a Venezia…", 2 "Tra tutte…", 3 "A Venezia indossare…", 4 "La maschera in genere… peculiarità della bauta è il labbro superiore…"). Object fields in the row match the record: Autore Sconosciuto, XVIII secolo, Casa di Carlo Goldoni, Bronzo, L 14,5 × H 16 cm, Inventario Cl XI n° 1421. The page gives no decree or date for any mask law, as the row says.
- Kind/tier vs QUALITY 6: docs/A compliant — holding museum authoritative for its own object's fields and published description; the entry's §12 museum-records calibration line even encodes the limit.
- Smallest fix: none.

## Counts and residual

- Rows checked: 6/6 (S279–S284, all in the declared S239+ span; all `mined`; all used-by name the entry; each has exactly one SOURCES row).
- Citing sentences: 10; verdicts — CARRIED 10, OVER-READ 0, WRONG-LOCATOR 0, NOT-OPENED 0.
- Kind/tier vs QUALITY 6: 6/6 compliant, no tier corrections needed; no superseding rows warranted.
- Claim-level access leg corroborated: criterion 10 route for S283 (403 → Wayback) reproduced independently by a fresh session today.

### Unrun checks / gaps

- Printed folios 149 and 150 are not legible in the `pdftotext` extraction of the Wayback PDF (running heads surface from 151); the p. 149 locator rests on the chapter-opening position plus the repository's own "149–168" metadata, not on a visible "149" folio. A pixel-level look at the scan's first chapter page would close this fully.
- L&S locator "II.B" verified structurally in flattened HTML (the "B. Also, transf. beyond the scenic lang." block and the "2. (γ) Law t.t." sub-item are present, with the Seneca quotation in the II.B list); the literal two-character heading string was not isolated as such under tag-stripping.
- S282's p. 728 folio attribution for the row's non-cited evidence quotes inferred from extraction position, not read off a footer; the entry itself cites only Resumo p. 721, which was verified directly.
- Latin text of Gellius not opened (row already discloses this and scopes its tier accordingly); row evidence beyond what the entry cites was spot-checked, not exhaustively re-quoted.
- Lane instruments (accept-c.py legs, sweep, check-source-access.py) not re-run here — outside this seat's assignment; falsify scope was the six rows' sentences, locators, and tier cells.
