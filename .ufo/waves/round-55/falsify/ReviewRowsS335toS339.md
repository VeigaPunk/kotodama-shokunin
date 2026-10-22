# Review: rows S335-S339 (monsters-hybrid-beings.md), round-55 FALSIFY

Seat: KotodamaR55.ReviewRowsS335toS339, 2026-10-22. Tooling: curl, preinstalled pdftotext (poppler), Python stdlib only — no installs.

## Verdict

The five rows hold: all 21 anchor quotes in SOURCES.md S335-S339 are verbatim at their stated locators (re-opened today by plain request; S338 via the cited Wayback capture). All five Gate lines (lessons/round-55.md:119-123) are present with verbatim anchors. The entry's S339 sentence is carried at stated strength. **Six defects found: four in `corpus/knowledge/myth-symbol/monsters-hybrid-beings.md` (two wrong locators, one dropped hedge, two "English writers" over-reads — the page nowhere says English writers), and one in the corpus/SOURCES.md S337 access note (the cited URL returns 301, not 200; content verified at the redirect target).** Per the claim's falsifier, the two "English writers" sentences are entry sentences the cited page does not carry and need the routed fix.

## Checked items

**S335 row (SOURCES.md:364) — CARRIED.** API `description` opens verbatim: "As a mythical creature believed to make rain, the dragon served as a symbol of rulers in premodern East Asia."; `description` sentences 2-3 and `did_you_know` tail "the image of dragons was used exclusively for the king's paraphernalia" all verbatim; accession 1986.85, 1700s, Korea Joseon confirmed.

**S335 Gate (lessons/round-55.md:119) — CARRIED.** Anchor verbatim in `description`[0]; grounds (rain, royal authority, jewel to pursue) carried.

**monsters-hybrid-beings.md:101 (S335 cite) — WRONG-LOCATOR.** The paraphernalia clause lives in the `did_you_know` field, not `description`; the entry cites only "(S335, description)". Strength otherwise preserved ("used only" = "exclusively").
Fix: replace `(S335, description)` with `(S335, description; did_you_know)`.

**S336 row (SOURCES.md:365) — CARRIED.** All six anchors verbatim in the V&A JSON (`summaryDescription`, `physicalDescription`): "Robes made for the emperor featured the Twelve Imperial Symbols of Sovereignty", "There are five-clawed dragons on the back and front", colour rule "Only the emperor and empress were allowed to wear bright yellow." Accession T.12-1950, 1750-1800, Given by the Forrer Family confirmed.

**S336 Gate (lessons/round-55.md:120) — CARRIED.** "In imperial China, official dress was highly regulated." verbatim; grounds carried.

**monsters-hybrid-beings.md:101 (S336 cite) — WRONG-LOCATOR.** "five-clawed" is carried by Physical description, not Summary; entry cites "(S336, Summary)".
Fix: replace `(S336, Summary)` with `(S336, Summary; Physical description)`.

**S337 row (SOURCES.md:366) — DEFECT (stale URL, access note unreproducible).** Plain request (curl, no -L) to https://www.abdn.ac.uk/bestiary/translat/66r.hti returns HTTP 301 (249 bytes) to https://www.abdn.ac.uk/bestiary/ms24/f66r; Wayback CDX shows that URL answering 301/302 since at least 2024-08-07, so "HTTP 200, 15,121 bytes" matches no record. All six anchor quotes were re-verified verbatim at the redirect target ("Dragons are born in Ethiopia and India, where it is hot all year round."; "The Devil is like the dragon; he is the most monstrous serpent of all").
Fix (SOURCES.md:366): replace `— https://www.abdn.ac.uk/bestiary/translat/66r.hti (direct plain request (curl), HTTP 200, 15,121 bytes, no challenge, 2026-10-22)` with `— https://www.abdn.ac.uk/bestiary/ms24/f66r (the old translation-page URL https://www.abdn.ac.uk/bestiary/translat/66r.hti now returns HTTP 301 here; plain request (curl) to the live page, HTTP 200, no challenge, 2026-10-22; translation text verified unchanged)`.

**S337 Gate (lessons/round-55.md:121) — CARRIED at the redirect target; URL mirrors the stale .hti.**
Fix: replace `https://www.abdn.ac.uk/bestiary/translat/66r.hti` with `https://www.abdn.ac.uk/bestiary/ms24/f66r`.

**monsters-hybrid-beings.md:101 (S337 cite) — CARRIED.** "born in Ethiopia and India" and the Devil allegory both verbatim on the live page.

**S338 row (SOURCES.md:367) — CARRIED.** Wayback capture 20260921201758 (HTTP 200, 661,019 bytes vs claimed 661,021 — trivial serving delta) carries all four anchors verbatim, incl. "Others refer to them as dragons – many taniwha looked like reptiles, had wings and ate people." and "Others were kaitiaki, or protectors of iwi (tribes) and hapū (sub-tribes)."; karakia-and-offering at dens, shape-changing, rua taniwha, Waikato proverb all carried.

**S338 Gate (lessons/round-55.md:122) — CARRIED.** Anchor verbatim: "Taniwha are supernatural creatures whose forms and characteristics vary according to different tribal traditions."

**monsters-hybrid-beings.md:102 (S338 cite, §8) — OVER-READ (hedge dropped).** Page says "In some traditions, taniwha were terrifying creatures that captured people and ate them."; the entry's "some taniwha captured and ate people" deletes the tradition hedge the row is required to preserve.
Fix: replace `Te Ara records that some taniwha captured and ate people while others were *kaitiaki*, protectors of iwi and hapū, given karakia and offerings (S338, A creature of many forms).` with `Te Ara records that in some traditions taniwha captured and ate people while others were *kaitiaki*, protectors of iwi and hapū, given karakia and offerings (S338, A creature of many forms).`

**monsters-hybrid-beings.md:113 (S338 cite, §9) — OVER-READ / UNSUPPORTED.** The page attributes the dragon label only as "Others refer to them as dragons"; "English writers", "European", "writers" have zero hits in the page body (checked stripped main text and raw HTML — only site navigation). The entry upgrades an unnamed "others" to "English writers".
Fix: replace `Te Ara notes that English writers have called taniwha dragons (S338, A creature of many forms).` with `Te Ara notes that others refer to taniwha as dragons (S338, A creature of many forms).`

**monsters-hybrid-beings.md:171 (S338 cite, §14) — OVER-READ / UNSUPPORTED (same defect).**
Fix: replace `English writers have called taniwha dragons (S338, A creature of many forms). The count comes from the English label.` with `others refer to taniwha as dragons (S338, A creature of many forms). The count comes from the English label.`

**monsters-hybrid-beings.md:177 (S338 cite, §14) — CARRIED.** "some taniwha are protectors" is carried verbatim-adjacent by "Others were kaitiaki, or protectors of iwi (tribes) and hapū (sub-tribes)."

**S339 row (SOURCES.md:368) — CARRIED.** PDF re-fetched: HTTP 200, application/pdf, 251,051 bytes (exact), 15 pages covering pp. 179-193. Both p. 193 English-summary anchors verbatim ("spirits of natural loci (the wood, water and field goblins; leshy, vodyanoy, polevik, respectively)"; "the combination of several different types of house spirits named domovik"); both Russian body anchors verbatim by string match on pp. 185 and 186.

**S339 Gate (lessons/round-55.md:123) — CARRIED.** Anchor verbatim at English summary, p. 193; "evidence is thin" matches "represented by scant, isolated evidence."

**monsters-hybrid-beings.md:104 (S339 cite, §8) — CARRIED at stated strength.** Natural-loci classification carried at pp. 182 and 193; "whose presence the household needs" carried by p. 182 (domovik must dwell in every house; without him household affairs will not succeed — "без него хозяйственные дела не пойдут успешно"); tier B and Polesye scope preserved; catalogue record not read as a study.

## Residual risk

- The S338 capture is a moving Wayback target; a 2-byte size delta vs the row note is serving variance, not a content change.
- Row S337's "15,121 bytes" figure matches nothing observable; if the scout measured some other artifact (print view, cached copy), that history is unrecoverable — the fix above describes today's state.
- Entry §14 line 171 leans on S351 for the cover-term frame; S351 is outside my slice and was not opened.

## Unrun checks

- reports/round-55/accept-c.py and the claim O gate checker were not re-run (other seats' scope).
- The CMA public page clevelandart.org/art/1986.85 and the V&A HTML page were not fetched; the rows declare the API JSON as the quoted source, and only that was checked.
- Later pages of the Te Ara taniwha story were not opened; row S338 is page 1 only, and every entry locator says "A creature of many forms", so page 1 was the page of record.
