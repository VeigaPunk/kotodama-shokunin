# ScoutHaudenosauneeStatement — the Grand Council's medicine-mask policy (round 54, claim C)

- seat: KotodamaR54a2.ScoutHaudenosauneeStatement (leaf; no delegation, no background job of my own, no tool installed)
- date: 2026-10-22. Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, claim base `260c68d58c5d3c2b9a6463ca5c667b7e0fff5987`. Every source below was opened in this session; nothing from attempt 1's scratch was read.
- assigned question: the Haudenosaunee Grand Council of Chiefs' public statement on the display and sale of medicine masks (the masks often called False Face masks). Quote only the statement's own rules, and feed the access-rule section of `corpus/knowledge/culture-material/masks-masquerade.md`.
- result: two opened sources reported as rows (`NEW-ScoutHaudenosauneeStatement-1`, `-2`), one of them the full policy text and the other the Confederacy's own statement of what happens to masks after return. The policy's rules are the ones a worldbuilder needs: making is licensed by use, the mask is empowered by being made rather than by a later rite, the image belongs to a medicine society, public exhibition and image reproduction are forbidden, and authority is held by the using society under the Grand Council with no individual and no institution able to stand in for it. Two further copies were opened as corroboration (a partial scan of the signed 1993 letter and the Onondaga Nation's own repatriation page) and are recorded below without rows.

## Route notes (ordinary means only)

| source | file actually read | route | access date |
|---|---|---|---|
| Grand Council policy, 1995 printing | http://www.nativetech.org/cornhusk/maskpoli.html | direct plain `curl`, HTTP 200, full HTML (8,837 bytes), text extracted locally | 2026-10-22 |
| Haudenosaunee Confederacy, Repatriation Committee | https://www.haudenosauneeconfederacy.com/departments/haudenosaunee-repatriation-committee/ | direct plain `curl`, HTTP 200, full HTML | 2026-10-22 |
| 1993 signed letter (corroboration) | https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/1424/Nasc/f02f6885-e135-4550-9aa7-6b87cd247f43/Haudenosaunee-Onondaga-Nation-on-Medicine-Societies-October-18-1993.pdf | direct plain `curl`, HTTP 200, `application/pdf`, 4 pages, no text layer; read by rasterising locally and OCR (tesseract 5.5.3), OCR used for checking only, never as a quote source | 2026-10-22 |
| Onondaga Nation, "Haudenosaunee Statement On Repatriation" (corroboration) | http://web.archive.org/web/20241206171454/https://www.onondaganation.org/government/policy/haudenosaunee-statement-on-repatriation/ | the live host failed DNS resolution twice (curl 28, "Resolving timed out"); read from Wayback capture `20241206171454`, HTTP 200 | 2026-10-22 |

No bot challenge, captcha, paywall or login stood in the way of either reported row, so there is nothing to report as "challenge met, not passed" for them. A DuckDuckGo HTML search I used to find copies returned HTTP 202 (a bot interstitial); I did not pass it and did not route around it — the rows below come from direct requests and one Wayback capture. Every quote below was checked as a literal substring of the fetched text after whitespace normalisation.

---

### NEW-ScoutHaudenosauneeStatement-1

citation: Grand Council of the Haudenosaunee (Six Nations Iroquois Confederacy), signed Chief Leon Shenandoah, Tadadaho. 1995. "Haudenosaunee Confederacy Announces Policy on False Face Masks." *Akwesasne Notes*, Spring, vol. 1 — full transcription hosted by NativeTech (page credit: Tara Prindle), page "Why there are No Images of Cornhusk Masks".
url: http://www.nativetech.org/cornhusk/maskpoli.html
route: direct plain request, HTTP 200 (NativeTech HTML), 2026-10-22
kind: web (transcribed policy statement)
tier: A for the policy's rules as the issuing authority states them; the copy is a transcription of the newspaper printing, so it carries scanning slips ("he" for "be", "tile" for "the") and its authority is the Grand Council's text, not the hosting page. Clauses outside the transcribed sections were cross-checked against a partial scan of the signed 1993 letter (see "also opened").
scope: the Grand Council's rules on medicine masks — what they are said to be, who may make them, commercial sale, who holds authority, public exhibition, images and reproductions, and return of masks held by non-Indians. It is a policy statement about the masks' custody, access and display; it is not an ethnographic description of ceremonies and it does not describe mask-making technique.
quotes:
- "Medicine Societies", paragraph 2: "Among these medicine societies are those that utilize the wooden masks and corn husk masks, which represent the shared power of the original medicine beings"
- "Status of Masks", paragraph 1: "By their very nature, masks are empowered the moment they are made."
- "Exhibition of Medicine Masks", paragraph 1: "The public exhibition of all medicine masks is forbidden."
- "Authority over Medicine Masks", paragraph 1: "No institution has the authority over medicine masks, as they are the sole responsibility of the medicine societies and the Grand Council of Chiefs."
teaches: a mask policy written by the mask-owning authority itself — sacred from the moment of making, made only for use inside a medicine society, forbidden to exhibit or reproduce, interpreted by nobody outside the societies, and with the veto placed in the using society and the Grand Council rather than in any individual or museum.
draft sentences:
- Making is licensed by use, not by skill or demand: the policy says masks should not be made unless they are to be used by members of the medicine society according to established tradition, so a worldbuilder should tie the maker's right to the using body rather than to a craft guild or a market (NEW-ScoutHaudenosauneeStatement-1, "Status of Masks", paragraph 2).
- The mask is empowered by being made, not by a later rite: the statement holds that masks are empowered the moment they are made and denies that any ceremony or tobacco is needed to make them powerful, so a design that gates power behind a consecration rite is choosing against this model (NEW-ScoutHaudenosauneeStatement-1, "Status of Masks", paragraph 1).
- What the mask is decides who may see it: the masks represent the shared power of the original medicine beings and each has a purpose solely for the members of its respective society, which makes the mask an image held by a body of members rather than a portrait owned by one wearer (NEW-ScoutHaudenosauneeStatement-1, "Medicine Societies", paragraph 2).
- The restricted act is seeing and reproducing: public exhibition of all medicine masks is forbidden, the ban reaches reproductions, castings, photographs and illustrations in exhibitions, and the non-Indian public is said to have no right to examine, interpret or present the societies' beliefs and duties — decide whether your culture's restriction attaches to the object, to its image, or to the knowledge (NEW-ScoutHaudenosauneeStatement-1, "Exhibition of Medicine Masks", paragraphs 1, 3 and 4).
- Authority is layered and cannot be delegated: each reservation has a medicine mask society with authority over the use of masks, the Grand Council of Chiefs has authority over all societies, no individual may speak for a society or decide the displacement of a mask, and no institution holds authority at all — place the veto with the using society, not with a ruler or a museum (NEW-ScoutHaudenosauneeStatement-1, "Authority over Medicine Masks", paragraph 1).
- Commerce and licensed voice are the same rule seen twice: no masks may be made for commercial purposes, and information about the medicine societies is not meant for general distribution; a fiction that manufactures masks for sale or gives the mask a public oracle voice is contradicting the policy it is borrowing from (NEW-ScoutHaudenosauneeStatement-1, "Sales of Masks", paragraph 1; "Exhibition of Medicine Masks", paragraph 3).

### NEW-ScoutHaudenosauneeStatement-2

citation: Haudenosaunee Confederacy, Haudenosaunee Repatriation Committee, section "Repatriation" — site page "Haudenosaunee Repatriation Committee"; undated page, site content current at access (newsletters listed to Winter 2018).
url: https://www.haudenosauneeconfederacy.com/departments/haudenosaunee-repatriation-committee/
route: direct plain request, HTTP 200 (Haudenosaunee Confederacy site HTML), 2026-10-22
kind: web (official confederacy department page)
tier: A for what the Confederacy says about its own repatriation practice and the destination of returned masks; the page speaks from the Grand River Council's position, so it is not evidence for every Haudenosaunee community's practice.
scope: the receiving end of the policy — who arranges returns, which classes of object are sought, how many medicine masks have come back, where they go, what condition they arrive in, and which institutions are still in negotiation. It does not describe how masks are used and does not state a rule of access.
quotes:
- "Repatriation", paragraph 2: "we have secured the return of over 800 medicine masks"
- "Repatriation", paragraph 2: "The masks are returned to the Societies that use and protect them"
- "Repatriation", paragraph 2: "Some masks have been contaminated with arsenic and other heavy metals."
- "Repatriation", paragraph 1: "Alone among Haudenosaunee communities, the Grand River Council has decided"
teaches: return is not a single restitution to a generic tribe — masks go back to the specific societies that use and protect them, the count is in the hundreds and the negotiations are named and ongoing, and the receiving custodian does conservation work (arsenic removal) as part of its responsibility.
draft sentences:
- Custody follows use: returned masks go to the Societies that use and protect them rather than to a general repository, so a worldbuilder should make repatriation a transfer to the using body and not to a national museum or a central archive (NEW-ScoutHaudenosauneeStatement-2, "Repatriation", paragraph 2).
- Repatriation is a long ledger with named counterparties: over 800 medicine masks have been secured over 25 years, and negotiations continue with the Canadian Museum of History, the Royal Ontario Museum and the Smithsonian National Museum of the American Indian (NEW-ScoutHaudenosauneeStatement-2, "Repatriation", paragraph 2).
- The receiving body must be able to care for what it reclaims: some returned masks were contaminated with arsenic and other heavy metals, and the Confederacy developed ways to remove the poisons without injuring the masks, which makes technical competence part of the custodian's standing (NEW-ScoutHaudenosauneeStatement-2, "Repatriation", paragraph 2).
- Claims are selective and argued from the community's own ritual capacity: the Grand River Council does not seek the return of human remains or funerary objects because it has no reburial ceremony, and concentrates on wampum records, medicine masks and ceremonial objects (NEW-ScoutHaudenosauneeStatement-2, "Repatriation", paragraph 1).
- The page speaks for one council inside a confederacy: the phrase "alone among Haudenosaunee communities" marks this as the Grand River position, so a worldbuilder must not turn one nation's repatriation stance into a confederacy-wide rule (NEW-ScoutHaudenosauneeStatement-2, "Repatriation", paragraph 1).

---

## Also opened (corroboration, no row)

**1993 signed letter, partial scan.** URL above; HTTP 200, PDF, 4 pages, no text layer. Page 1 carries the Grand Council letterhead (Onondaga Nation, Hemlock Road, Nedrow, New York), the date "October 18, 1993", and the same opening sentence the transcription carries (the Grand Council of the Haudenosaunee, the Six Nations Iroquois Confederacy, issuing its policy statement on all medicine masks of the Haudenosaunee), with the "Medicine Societies" and "Status of the Masks" sections and the beginning of "Sales of Masks". Page 3 carries the "Return of Medicine Masks" closing and the signature block "Chief Leon Shenandoah, Tadadaho, Grand Council of the Haudenosaunee". Pages 2 and 4 carry no letter text (page 2 rasterises blank, page 4 shows only stray marks), so the scan is missing the middle of the letter — "Authority over Medicine Masks" and "Exhibition of Medicine Masks" are **not** in this copy. What it establishes: the policy predates the 1995 *Akwesasne Notes* printing (a 1993 statement, printed 1995), the signer is the same, and the clauses it does carry match the transcription except for small variants (the transcription reads freedom where the scan's OCR reads religious freedom; the transcription's "he" for "be" is a scanning slip, the scan reads be). OCR was used to read the scan and is not a quote source anywhere in this report.

**Onondaga Nation, "Haudenosaunee Statement On Repatriation"** (Wayback `20241206171454`; the live host failed DNS twice). The Onondaga Nation's own government page narrates the same return: the NMAI's predecessor "had acquired hundreds of culturally-sensitive items belonging to the Haudenosaunee and its member nations", and the masks came back "to be used by the traditional Haudenosaunee for their ongoing health and well-being", after "nearly 30 years of efforts". It is a second nation-level voice for the return and its purpose; it adds no new rule, so I did not make it a row.

## Notes for the L1 (precision, not judgment of existing rows)

- **Name the object as the issuing authority names it.** The statement's own words are "medicine masks", "wooden masks and corn husk masks". "False Face" appears in the statement only in the newspaper headline and in the framing sentence the entry would be quoting from a 1995 reprint. Keep "False Face" as the historical-literature label and "medicine masks" as the policy's term.
- **Date the policy carefully.** The statement text is dated by its printing (Spring 1995, *Akwesasne Notes* vol. 1), and the signed letter is dated 18 October 1993. A sentence that says "1993" or "1995" alone is answerable; a sentence that says "the 1990s policy" wastes the distinction.
- **Tier caveat to carry into the row.** The 1995 text reaches us as a transcription on a third-party educational site with visible scanning slips. Two independent checks exist (the partial 1993 scan; the Confederacy's own repatriation page, which presupposes the same return policy), but the printed *Akwesasne Notes* issue itself was not opened. Write the row's tier note so a reader knows the exact artifact behind the quotes.
- **Do not import ceremony.** Neither row describes mask-making, songs, medicines, curing procedure or who wears what. The only licensed-use statement is institutional: masks are for members of the respective medicine societies, and information about the societies is not for general distribution. The entry's access-rule section should stop where the statement stops.
- **Two different bodies, two different claims.** Row 1 is the Grand Council's rule; row 2 is one council's (Grand River) repatriation practice. A design table that puts "who may make / who may see / who may speak / who may hold" on one axis can use row 1 for the rule and row 2 for what happens when the rule is enforced against museums — but the second must stay labelled Grand River.

Proposed `corpus/SOURCES.md` cells (L1 assigns the S-ids and the status/opened/recheck/used-by cells):

```
| NEW-ScoutHaudenosauneeStatement-1 | Grand Council of the Haudenosaunee (Six Nations Iroquois Confederacy), signed Chief Leon Shenandoah, Tadadaho. 1995. "Haudenosaunee Confederacy Announces Policy on False Face Masks." Akwesasne Notes, Spring, vol. 1; full transcription hosted by NativeTech — http://www.nativetech.org/cornhusk/maskpoli.html | web | A | the Grand Council's own rules on medicine masks: what they are said to be, who may make them, sale, authority, exhibition, images, return; a policy statement, not an ethnographic description of ceremony | "Medicine Societies" par. 2; "Status of Masks" par. 1; "Exhibition of Medicine Masks" par. 1; "Authority over Medicine Masks" par. 1 (transcription with scanning slips; partial 1993 signed-letter scan at thrillshare asset f02f6885-e135-4550-9aa7-6b87cd247f43 corroborates date and clauses) | masks are sacred from the moment of making, made only for use inside a medicine society, forbidden to exhibit or reproduce, and no individual or institution may speak for the societies | |
| NEW-ScoutHaudenosauneeStatement-2 | Haudenosaunee Confederacy, Haudenosaunee Repatriation Committee, "Repatriation" section — https://www.haudenosauneeconfederacy.com/departments/haudenosaunee-repatriation-committee/ | web | A | what the Confederacy states about its own repatriation practice: destination of returned masks, counts, condition, counterpart institutions; the Grand River Council's position, not every community's | "Repatriation" par. 1 and 2 | over 800 medicine masks returned to the Societies that use and protect them, some contaminated with arsenic and treated without injury, negotiations continuing with named museums | |
```

## unopened

- The printed *Akwesasne Notes*, Spring 1995, vol. 1 itself: no public copy found; only the NativeTech transcription was opened. This is the gap behind the tier caveat on row 1.
- https://app.pch.gc.ca/application/bibicc-ccilib/detailler-detail.app?rID=ccicat20947&pID=2&ssm=true — a Canadian Heritage bibliography record for a Royal Ontario Museum item whose snippet quotes the policy. Two plain requests were reset ("Recv failure: Connection reset by peer"), and the Wayback availability API returned no snapshot; not opened, so nothing here rests on it.
- https://www.onondaganation.org/government/policy/haudenosaunee-statement-on-repatriation/ — live host did not resolve (two attempts, DNS timeout); the Wayback capture was opened instead and is recorded above.
- The 1993 scan's middle pages (the "Authority" and "Exhibition" sections): pages 2 and 4 of the PDF carry no letter text, so that copy is partial and could not confirm those sections.
