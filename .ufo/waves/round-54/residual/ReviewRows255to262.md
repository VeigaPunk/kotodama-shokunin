# Residual review — claim C, rows S255–S262 (seat: ReviewRows255to262)

Attack on `corpus/knowledge/culture-material/masks-masquerade.md` (lane `6a658ca4`). Every citing
sentence for S255–S262 re-checked against a copy the reviewer re-opened today (2026-10-22) by
ordinary means only (plain `curl`, default UA; Wayback where a challenge was met and not passed).
Row checks against `corpus/QUALITY.md` criterion 6 cover kind, tier and used-by cells.

Verdicts: **15 CARRIED, 0 OVER-READ at claim level, 2 WRONG-LOCATOR, 1 OVER-READ (minor strength
inflation), 0 NOT-OPENED** (18 citing sentences/clauses in total). One tier-consistency finding at
row level (S256 A vs S258 B), not an entry-sentence defect.

---

## S255 — Smith et al., *A Dictionary of Greek and Roman Antiquities* (1890), "IMAGO", Perseus

Re-opened: `perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.04.0063:entry=imago-cn` — HTTP 200,
95,362 bytes. Kind `book` OK; tier `B` defensible (1890 synthesis citing classical sources; the
entry's primary claims cite S241/S242 separately).

- **CARRIED** — masks-masquerade.md:60 (ius imaginum, curule offices, withheld after death, Brutus
  and Cassius). Page ("Jus imaginum" section): "the right was confined to those who had filled the
  offices of dictator, consul, censor, praetor, and curule aedile"; "the exhibition of whose masks
  … was not permitted (Tac. Ann. 3.76)".
- **CARRIED** — masks-masquerade.md:95 (alae, titulus of deeds). Page: "under each imago was an
  inscription (titulus) giving the name and deeds of the person represented" (alae/armaria passage).
- **CARRIED** — masks-masquerade.md:98 (laurel on festal days). Page: "the recesses … were thrown
  open, and the busts crowned with laurel".
- **CARRIED** — masks-masquerade.md:99 (mould→fresh cast→atrium, hedged). Page: "it is a probable
  supposition that the services of the pollinctor … [he] fashioned the mask"; "a fresh mask might
  be made from this mould, which was the imago placed in the atrium". The entry's `(to-verify
  against a modern study)` mark is honest, not laundered.

## S256 — UNESCO ICH, "Mask dance of the drums from Drametse" (element 00161)

Direct fetch today met the site's bot challenge (HTTP 200, F5/TSPD captcha body — challenge met,
not passed). Verified against Wayback capture `20250724134112` of the same URL (real page; the
2026-05-14 capture is itself a captcha capture and unusable). The row's claimed direct HTTP 200 at
read time is not contradicted — the challenge is intermittent. Kind `docs` OK.

- **WRONG-LOCATOR** — masks-masquerade.md:62 ("sixteen masked male dancers organized by one
  monastery", cited "Element description, ¶2"). Page: ¶2 has "sixteen masked male dancers wearing
  colourful costumes"; the organizing clause is in ¶1: "The festival … is organized by the Ogyen
  Tegchok Namdroel Choeling Monastery" — strictly the *festival* is organized, not the dancers.
  Smallest fix: locator "Element description, ¶1–¶2" and/or reword "a festival organized by its
  monastery fields sixteen masked male dancers".
- **CARRIED** — masks-masquerade.md:87 (prayer dance in shrine precedes one-by-one courtyard
  appearance; calm/rapid parts). Page ¶2: "perform a prayer dance in the soeldep cham, the main
  shrine, before appearing one by one in the main courtyard"; "a calm and contemplative part that
  represents the peaceful deities and a rapid and athletic part where the dancers embody wrathful
  deities".
- **CARRIED** — masks-masquerade.md:90 ("people come to obtain blessings", ¶3). Page ¶3: "is
  attended by people from Drametse as well as neighbouring villages and districts to obtain
  blessings".

**Tier asymmetry (criterion 6, row-level finding).** S256 is tier A ("for what the inscription
itself states") while S258 — the same UNESCO Representative-List description class used for the
same kind of claim (facts the register entry states) — is tier B ("Secretariat's edited English
summary … not the dossier itself"). The two rows apply different tier rules to identical source
class and usage; under criterion 6 the uniform resolution is either both A (authoritative for the
exact scope "what the entry states") or both B (publisher description for substantive claims).
Smallest fix: one superseding SOURCES row harmonizing the tier — the safer direction is S256 A→B,
matching S258's reasoned note.

## S257 — Amarasinghe & Kariyakarawana 2014, Journal of Social Review 3(1):56–68 (PDF)

Re-opened: `seu.ac.lk/…/5%20Article%20pages%2056%20-%2068.pdf` — HTTP 200, 406,652 bytes (matches
row). `pdftotext -layout`; journal page numbers verified from page footers. Kind `paper`, tier `B`
OK (interview data flagged in-entry as "one informant's memory").

- **CARRIED** — masks-masquerade.md:62 (Oli caste / Garayaka mask, p. 64). Page 64: "only people
  belonging to Oli caste was allowed to make performance wearing the mask of the (Demon) Garâyakâ"
  (informant Norbert, 63).
- **CARRIED** — masks-masquerade.md:63 (Karava carved, Berava verse/drumming; one Berava artist
  doing both; Abstract p. 56, p. 64). Abstract p. 56: "it was the ritual dancers … of Berava
  (tom-tom beaters) caste in Bentota, who contributed singing, playing, words and verse";
  "Carpentry was the duty assigned to Karava caste". P. 64: Norbert "beats the Tom-Tom … and … has
  skill in carving masks".
- **CARRIED** — masks-masquerade.md:81 (mockery gloss; stock parts police constable + Mudaliyar;
  p. 57, Notes p. 65). P. 57: "Mask drama or Kôlam (mockery) is a kind of folk-drama". Notes,
  p. 65, character list includes "Mudali kolama(mudali), … Polis kolama,(Police man)" among "a few
  common characters". Minor gloss drift only (Police man→"constable", mudali→"Mudaliyar").
- **CARRIED** — masks-masquerade.md:116 (kôlam = mockery, p. 57) — same support.

## S258 — UNESCO, "Busó festivities at Mohács" (element 00252)

Row honestly records: direct requests met the bot challenge ("challenge met, not passed"); read
from Wayback capture `20250807133317`. Reviewer re-opened that capture: the plain redirect fetch
transiently 404'd; the `id_` variant and CDX confirm a 200 capture of the real page. Sentence
numbering verified against the full description paragraph.

- **CARRIED** — masks-masquerade.md:63 ("self-organized busó groups pass on mask carving to
  younger generations", sentence 6). Page, sentence 6 verbatim: "The arts underlying the
  festivities are preserved by self-organized groups of busós of all cultural backgrounds, many of
  whom pass on the techniques of mask carving and ritual celebration to younger generations."
- **CARRIED** — masks-masquerade.md:89 ("more than 500 busós arrive in rowboats on the Danube",
  sentence 2). Page, sentence 2: "the arrival of more than 500 busós in rowboats on the Danube for
  a march through the city".

Tier `B` — see asymmetry finding under S256; whichever direction harmonization takes, exactly one
of the two rows needs a superseding row.

## S259 — Albert 1987, "Tubuan: Masks and Men in Southern New Ireland", Expedition 29(1)

Re-opened: `penn.museum/sites/expedition/tubuan/` — HTTP 200, 56,689 bytes. Kind `paper`, tier `A`
OK (first-hand field account by the researcher, scope-limited to public practice per the row).

- **CARRIED** — masks-masquerade.md:66 (all three clauses). Opening section: "initiated into the
  lowest grade of knowledge … 'buying the eye of the tubuan,' i.e., buying the right to see it in
  the triun, the otherwise forbidden spot where seniors construct the masks"; opening: "a hidden,
  virtually alternative society … rigidly excluded women". "General Features of the Tubuan System":
  "Lak masks are usually clan possessions with sanctions against alienation, masks acquired from
  outside the Lak area are personal possessions that can be sold". "Conclusion": "men say it is a
  spirit but clearly know that it is they who make the mask and don it".

## S260 — Agnes Etherington, "Helmet Mask (Sowei or Ndoli Jowei)" M84-144

Re-opened: `agnes.queensu.ca/explore/collections/object/helmet-mask-sowei-or-ndoli-jowei/` — HTTP
200, 183,538 bytes. Kind `docs`, tier `B` correct (museum's curatorial description for the belief
claims, per criterion 6's publisher-description rule).

- **CARRIED** — masks-masquerade.md:67 (commissioned by Sande; worn exclusively by women; catalogue
  text ¶1). Page ¶1: "Commissioned by the Sande society, a powerful Mende women's association … is
  worn exclusively by women, a rarity in African masquerades".

## S261 — Curnow, *The Bright Continent*, ch. 3.4 (LibreTexts copy)

Re-opened: `human.libretexts.org/…/3.04:_Art_and_Youth_Initiation` — HTTP 200, 196,825 bytes.
Kind `book`, tier `B` OK.

- **WRONG-LOCATOR** — masks-masquerade.md:67 ("captions credit the masks to a male artist while
  the performer is a woman", cited "fig. 325 caption"). Fig. 325's caption reads only "Sowei mask,
  Mende male artist, Sierra Leone, 20th century" — no performer half. The conjunction sits verbatim
  in Fig. 324's caption: "Mask performed by women but made by a Mende male artist" (plus the
  section's masquerader-female sentence). Smallest fix: "(S261, fig. 324 caption)" or "figs.
  324–325 captions".
- **OVER-READ (minor)** — masks-masquerade.md:110 ("the *gonde* clown wears an old, damaged sowei
  mask retired from its first function", Sande and Bondo section). Page: "The gonde mask is
  **usually** an old sowei mask that has suffered termite or other damage and has been retired from
  its original function." The entry states it categorically, dropping "usually". Smallest fix:
  "usually an old, damaged sowei mask".

## S262 — Phillips 2009, "The Mask Stripped Bare by its Curators" (actesbranly.336)

Re-opened: `journals.openedition.org/actesbranly/336` — HTTP 200, 141,215 bytes (matches row).
Kind `paper`, tier `A` correctly scoped to Phillips's own fieldwork report (not Mende belief in
general — the row's tier note says so).

- **CARRIED** — masks-masquerade.md:67 (no separate word for "mask"; "the head of sowei"; bare
  headpieces in an enclosure men could not enter; stricter villages brought out only the fully
  costumed figure — all cited ¶2). Page ¶2 verbatim: "do not have a separate word for 'mask'";
  "the phrase that most closely translates the English 'sowei mask' is sowo wui ('the head of
  sowei')"; "did not object to my seeing, measuring, and studying these 'heads'—although sometimes
  in an enclosed area that men could not enter"; "villages in which traditional protocols were more
  strictly observed … brought out the fully masked and costumed figures".

---

## Counts

- Citing sentences/clauses checked: **18** across 8 rows.
- CARRIED 15 · WRONG-LOCATOR 2 (S256:62, S261:67) · OVER-READ 1 (S261:110, minor) · NOT-OPENED 0.
- Row-level findings: tier asymmetry S256(A)/S258(B) under criterion 6 — one superseding row
  needed; both rows' usage patterns are identical register-entry statements.
- All eight sources were re-opened by the reviewer today by ordinary means; none unverifiable.
  S256 and S258: live host serves a bot challenge (met, not passed) — honest per criterion 10 and
  the row notes; verification used named/alternative Wayback captures.

## Unrun checks

- `reports/round-54/accept-c.py`, `tools/check-source-access.py`, `check-claim-separability.py`
  not re-run here (row-review slice only; the closure/integrator owns the gate receipts).
- Nomination dossier for S258 not consulted (row scopes to the register summary, and says so).
- Rows S239–S254 and S263+ are sibling slices; used-by/status cells seen in-range are `mined` and
  name the entry, but a full corpus-wide sweep was not re-done.
- S257 PDF layout was read via `pdftotext -layout`; no OCR re-extraction.

## Tooling

No installs. Used: `curl` (plain requests + Wayback CDX), `pdftotext` (system), `python3` stdlib
for HTML→text. No pacman transaction touched (host-wide pause observed).
