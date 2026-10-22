# Residual falsify check — claim C, rows S263–S270 (Kotodama round 54 attempt 2)

Reviewer seat: `KotodamaR54a2.ReviewRows263to270`, 2026-10-22. Attack only; no fixes applied.
Entry under review: `corpus/knowledge/culture-material/masks-masquerade.md` at lane commit `6a658ca4fe9230f70eaa3b421e6c9d78da5c1633` (landed bytes verified with `git show`; read-only git in the lane). Rows: `corpus/SOURCES.md:292-299`. Every URL below was re-opened this session by plain `curl` (no user-agent header) or the route's named Wayback capture; PDFs read via `pdftotext -layout` (poppler, already installed — no installs performed). Sources opened: S263 PDF HTTP 200 (873,781 B, matches row), S265 HTTP 200, S266 HTTP 200, S267 PDF HTTP 200 (639,744 B), S268 PDF HTTP 200 (1,472,382 B), S269 docslib HTTP 200 (62,650 B; first attempt 503, retried), S264 and S270 via their routes' named Wayback captures (HTTP 200). No challenge was passed by any means.

**Mid-review divergence (not a finding against the claim):** while this review ran, the working tree of `masks-masquerade.md` dropped two S267 claims that are present in landed `6a658ca4` — "One voice, many bodies" (landed line 79) and the Kòmò after-sunset clause (landed line 85). Both verified CARRIED below; `agent://KotodamaR54a2.ExecIntegrateRows` notified. Verdicts below are keyed to the landed bytes.

## S263 — Drewal 2008, *Homage to Thomas Moulero* — CARRIED
- Entry: `masks-masquerade.md:68` — mothers can prevent the mask from being removed after the festival; mask brought out to photograph only as an exception (interview transcript, PDF pp. 5 and 8).
- Row: SOURCES.md:292, kind `book`, tier A.
- Page: PDF p. 5, TM answer: "they can prevent the mask from being removed after the festival." PDF p. 8, TM: "It was only for me that they brought it out so it could be photographed."
- Locator verified: interview transcript begins p. 5 ("On May 15, 1971 … interviewed him"); both locators sit inside the transcript, speaker tag `TM:` (Moulero) on both. Strength exact. Tier A correct — the row is the primary publication itself.
- Smallest fix: none.

## S264 — UNESCO, Oral heritage of Gelede — CARRIED
- Entry: `masks-masquerade.md:68` — "the only known masked society, which is also governed by women" (Description, ¶2), flagged as UNESCO's own superlative.
- Row: SOURCES.md:293, kind `docs`, tier B; route = Wayback `20191019004218` after challenge met, not passed.
- Page (named capture, re-fetched HTTP 200): "It is the only known masked society, which is also governed by women." Description ¶1 begins "The Gelede is performed by the Yoruba-Nago community…"; the quote sits in ¶2 (same paragraph as "The ceremony usually takes place at night on a public square"), matching the row's own ¶2 quote convention. Strength exact; attribution framing honest. Tier B correct for a register description (QUALITY.md ¶6).
- Smallest fix: none.

## S265 — Haudenosaunee policy on False Face Masks (NativeTech copy) — CARRIED
- Entry: `masks-masquerade.md:69` — "The public exhibition of all medicine masks is forbidden"; no institution has authority (sections "Exhibition of Medicine Masks"; "Authority over Medicine Masks").
- Row: SOURCES.md:294, kind `community`, tier B.
- Page (HTTP 200): both headings present verbatim; "The public exhibition of all medicine masks is forbidden." under Exhibition; "No institution has the authority over medicine masks, as they are the sole responsibility of the medicine societies and the Grand Council of Chiefs." under Authority. Strength exact, locators correct. Tier B correct for a community statement.
- Smallest fix: none.

## S266 — Hopi Cultural Preservation Office — WRONG-LOCATOR (minor)
- Entry: `masks-masquerade.md:69` — sacred rituals "exposed out of context and without Hopi permission" (S266, "Intellectual Property Rights", **¶3**).
- Row: SOURCES.md:295, kind `community`, tier B.
- Page (HTTP 200): the sentence lives in **¶4**: "Through these thefts, sacred rituals have been exposed to others out of context and without Hopi permission." Real ¶3 is "All of these actions are breaches of Hopi intellectual property rights…". The row's own quote field counts "Through the decades…" as ¶2, so the entry's ¶3 also contradicts the row's counting convention. Sentence fully carried; only the paragraph number is off by one.
- Smallest fix: change `¶3` to `¶4` at `masks-masquerade.md:69`.
- Row hygiene note (cells are correct, text is not): SOURCES.md:295 carries two contradictory tier notes — a stale "(tier note: A — the tribe's own standing statement…)" followed by "(tier B: …not tier-inflated)". Filed cells `community | B` conform to QUALITY.md ¶6; the stale A-note should have been removed by a superseding row when the tier settled at B. Smallest fix: superseding SOURCES row deleting the stale note.
- Kind/tier per ¶6: correct.

## S267 — Driver 2017, Buzz Aesthetic and Mande Music — CARRIED (all 4 landed claims)
- Entry lines (landed): `masks-masquerade.md:75`, `:76`, `:79`, `:85`. Row: SOURCES.md:296, kind `paper`, tier A. PDF re-opened HTTP 200.
- L75: "The most widespread devices used for disguising the human voice for spiritual purposes in sub-Saharan Africa are those that employ a vibrating membrane." — in §"The buzz aesthetic in Africa – possible explanations"; entry's "§The buzz aesthetic in Africa" is an unambiguous truncation of that heading. Carried.
- L76: "The auditory aspect of these masks is particularly important to non-initiates (normally women and children) who are forbidden from seeing the headpieces." — §Sources of power within the Mande buzz aesthetic. Carried ("spirit is only sound" is the entry's fair inference from "first of all a voice" + access rule).
- L79: "created not by a mirliton, but by the sum of several friction drums held by the mask bearers. The 'roar' of each drum contributes to the perception of a single, omnipresent voice" — same section. Carried.
- L85: "emerge after sunset during the seasonal 'coming out' of the Kòmò" — same section. Carried.
- Tier A correct — primary journal article for its own findings. Both section locators are shortened but resolve uniquely in the PDF.
- Smallest fix: none (optionally expand the L75 section name).

## S268 — Potter 2020, West African Voice Disguisers — CARRIED (both claims)
- Entry: `masks-masquerade.md:75`, `:78`. Row: SOURCES.md:297, kind `paper`, tier A. PDF re-opened HTTP 200.
- L75: bone tube — "cylindrical tube… made from bone… Measuring a mere 3.7cm in diameter and 5.6cm in length… makes the spider silk membrane vibrate" ("small" is fair); quote exact: "the human speaks and a spirit is heard." Section heading "The voice-disguiser – an auditory object?" exists verbatim and contains both passages.
- L78: "During important visitations of spiritual beings, women were relegated to the outskirts of the neighbourhood… the soundscape was gendered concentrically" — same section. Carried.
- Tier A correct (primary AAM of the refereed article).
- Smallest fix: none.

## S269 — Blench 2006, coded language of the orìm (docslib mirror) — CARRIED (all 3 claims)
- Entry: `masks-masquerade.md:76`, `:77` (two claims). Row: SOURCES.md:298, kind `docs`, tier B.
- Page (HTTP 200 this session; first attempt 503, retried): Abstract carries verbatim "Orìm are mostly heard, but emerge as masked figures under some circumstances" and "speak through voice disguisers in a language dotted with code words although framed in normal Tarok syntax and their utterances are interpreted by unmasked figures". §1 is rendered on the opened page and carries the triad "a) Substitution languages… b) Replacement languages… c) Surrogate languages" — the entry's "surrogate tone-speech" is a fair paraphrase of the surrogate/whistle-speech class. Locators Abstract and §1 correct; consistent with the row's note that only title page, abstract and §1 rendered. Tier B conservative and conformant.
- Smallest fix: none.

## S270 — UNESCO, Carnival of Binche — CARRIED (claim 1) / WRONG-LOCATOR (claim 2)
- Entry: `masks-masquerade.md:85`, `:91`. Row: SOURCES.md:299, kind `docs`, tier B. Named Wayback capture `20241225020014` re-fetched HTTP 200.
- L85: description **sentence 2** = "Each year, during the three days preceding Lent, it is host to carnival festivities…" — correct number and text (description opens "The town of Binche is situated south of Brussels…"; 13 sentences total). CARRIED.
- L91: entry claims financial commitment then wax mask, citing "sentences **8 and 12**" — transposed. Sentence 8 is the wax-mask sentence ("…wax masks with small spectacles, parade through the town…"); sentence 12 is the financial one ("…renowned for its spontaneity and the substantial financial commitment of its participants."). Both claims fully carried; both numbers point at the other claim.
- Smallest fix: cite "(S270, description, sentences 12 and 8)" or reorder the claims at `masks-masquerade.md:91`.
- Tier B correct for the Secretariat's edited description.

## Kind/tier vs QUALITY.md criterion 6
8/8 rows conform: S263 `book/A` and S267, S268 `paper/A` are primary sources for their exact scopes; S264, S269, S270 `docs/B` and S265, S266 `community/B` are descriptions/statements kept at B. No tier inflation found. Sole ¶6-adjacent defect is the stale contradictory tier-note text inside S266's row (see above), not a cell error.

## Counts
- Rows attacked: 8/8 (S263–S270). Citing sentences checked: 15.
- CARRIED: 13. WRONG-LOCATOR: 2 (S266 ¶3→¶4; S270 sentence-order transposition at landed line 91). OVER-READ: 0. NOT-OPENED: 0.
- Kind/tier conformance: 8/8 cells; 1 row-text hygiene defect (S266 stale tier note).
- Challenges: met and routed around by Wayback only where the row's route already named the capture (S264, S270); the docslib download-endpoint check was not attempted (stayed on the rendered public page, matching the row's note).

## Unrun checks / residual risk
- Live `ich.unesco.org` bot challenge for S264/S270 not re-tested by this seat; verdicts rest on the routes' named Wayback captures (both re-fetched HTTP 200 today).
- S267: ~10 lines of figure captions between printed pp. 15–17 not re-read (row's own note; no cited claim lives there). S268: trailing figure-list lines not re-read.
- S266 ¶2's full enumerated-violations list not re-verified word-for-word (the entry cites only the ¶4 sentence, which was verified verbatim).
- Mid-review working-tree removal of the two S267 claims not audited beyond confirming the landed commit still carries them; if that removal is meant to land, re-run this slice's S267 check against the new tip.
- `idmap.tsv` not consulted (verdicts keyed by S-id; no draft-id ambiguity encountered).
