# ReviewDKongoA59 — claim D falsify, fixes 18, 65, 82, 84a, 84b

Seat: KotodamaR59.ReviewDKongoA59 (reviewer, leaf). Date 2026-10-23 UTC. Scratch: `/fast/scratch/hyaku/kotodama-r59/ReviewDKongoA59/`.
Entry: `corpus/knowledge/civilizations/kongo-kingdom.md` (base lines 18, 65, 82, 84). Sources re-opened by plain GET (reopen-quote.py, curl, archive.org metadata/djvu.xml). No installs.

**Verdict: AGREE on all five.** No new sentence overreads its page. In none of the five was the old text the better reading: the old text was wrong in 18, 82 and 84b, and an overstatement or overgeneralisation in 65 and 84a. Severity of findings: none blocking; three low notes (65, 84a, 82 fetch) below.

| Fix | Verdict | Old text right? | Locator line |
|---|---|---|---|
| 18 | agree | no (p. 469 wrong) | `LOCATED https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt` |
| 65 | agree | no (overstates) | `LOCATED https://www2.historia.uff.br/tempo/wp-content/uploads/2024/11/artg6-7.pdf` |
| 82 | agree | no ("royal" overreads) | `LOCATED https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693` |
| 84a | agree | defensible, broader | `LOCATED https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf` |
| 84b | agree | no ("object" mislabels) | `LOCATED https://www.metmuseum.org/art/collection/search/318318`; `LOCATED https://web.archive.org/web/20260314181520id_/https://www.metmuseum.org/art/collection/search/318318` |

`rowcheck.not_same_page(support_urls)` returns `[]` for all five (same-page rule clean).

## 18 — doc. 142, p. 469 → p. 470 — AGREE

Served sentence (djvu.txt, Afonso I to D. João III, 6 July 1526):
> "E nam avemos este dano por tamanho, como hé que os ditos mercadores leuam cada dia nossos naturaes, filhos da terra e filhos de nossos fidallgos e vassallos, e nossos parentes, por que os ladrões e homés de maa cÕcyécya, os furtam …"

Page evidence. The page number is printed at the **bottom** of each leaf: in `_djvu.xml` the numeral words sit at y≈1224–1243 on a leaf of height 1556. Checked against the TOC: leaf 0536 opens doc. 144 and its footer reads `475`, and the TOC gives doc. 144 → 475. Footers by leaf:
- 0526 `465`, 0527 `466`, 0528 `4 6 7`.
- 0529 has no footer. It opens doc. 142 ("142 CARTA DO REI DO CONGO A D. JOÃO III (6-7-1526)"), so it is p. 468, matching the TOC line "Carta do Rei do Congo a D. João III, Cidade de Congo, 6 de Julho dc 1526 468".
- 0530 `4 *9` (469).
- **0531 `* 7 °` (470).** This leaf runs from "Senhor, v.a. saberá como nosso Reyno se vay a perder" through the support quote.
- 0532 has no footer (471). It runs from "trato de esprauos nem sayda pera elles" to the end of the letter, "ATT—CC-I-34-94".
- 0533 `47-` (472), doc. 143, matching the TOC's 472.

So the quote is on p. 470. In the flat `_djvu.txt` the `469` marker comes just *before* the passage, which is why someone reading it as a running head would land on 469. The new text is correct.

Residual note for fix 140, which is not in my set and shares this locator: the "no slave trade" wish crosses a page break. "porque nossa vontade hé que nestes Reynos nam aja" ends p. 470, and "trato de esprauos nem sayda pera elles" opens p. 471. "p. 470" points to where the sentence begins; "pp. 470–471" would be exact. This is review-only; the frozen `new` strings are not mine to change.

## 65 — Regimento titles — AGREE

Served sentence (Tempo artg6-7.pdf, PDF p. 7, under the section "Conversão e catolização", which opens on PDF p. 4 with no intervening heading):
> "Assim, a justiça do Estado passou a se guiar pela normas portuguesas, a partir da embaixada de Simão da Silva, portador do Regimento de 1512, e os antigos chefes de linhagem das províncias passaram a intitular -de de condes, marqueses, duques."

The new text, "the old lineage heads of the provinces began styling themselves as counts, marquises and dukes", renders *antigos chefes de linhagem das províncias passaram a intitular-se* faithfully. The old text was weaker on two counts. "Carried the Portuguese titles" implies the titles were formally held or granted, while the page says the chiefs styled themselves. And "provincial chiefs" drops "lineage heads".

Low note: in the page's sentence, "a partir da embaixada … portador do Regimento de 1512" grammatically governs the justice clause, and the titles clause is joined to it by *e*. "After the 1512 Regimento" is therefore a fair compression of the paragraph's timeline (the *aportuguesamento* under Afonso I), but not a word-for-word attribution. Not an overread worth blocking.

## 82 — "royal control" → "Kongo's control" — AGREE

Served sentence (Cambridge Extract, second `<p>` of the abstract, in both the 2026-02-03 and 2024-09-09 captures):
> "Kongo's control over the theological content allowed the religion to gain mass acceptance while its control over the Church organization and finance allowed it never to be an instrument for foreign domination, in spite of Portuguese attempts to use it as a 'fifth column'."

"Its" refers to Kongo, the country, not the crown. So the old "royal control" narrowed Thornton's subject to the monarchy, which the Extract does not do. The new text is faithful.

Locator check: the Extract has two `<p>` paragraphs. Paragraph 1 ends "…as being the religion of the country." Paragraph 2 runs from "This was possible because Kongo, as a voluntary convert…" to the end. The sentence's two halves therefore sit in paras. 1 and 2, as "paras. 1–2" says.

Low note (fetch fragility, not fidelity): `support_urls[1]` (the `20240909103530id_` capture) returned `NOT_LOCATED … HTTPError` on two reopen-quote runs. A direct urllib probe showed `HTTPError 429 Too Many Requests`, while curl got HTTP 200 (499,103 bytes) and the body carries the quote. `support_urls[0]` (non-`id_` 2026 capture) LOCATED, so CARRY passes on the first URL. If Wayback throttles both URLs at acceptance time, fix 82 has no live fallback; the live cambridge.org page returned 429 to curl.

## 84a — mestres — AGREE

Served sentence (Fromont 2017, printed p. 12 = PDF p. 3, describing Figure 1):
> "Behind him, two mestres, interpreters and leaders of the Church, wear their uniform composed of a white cloth draped over one shoulder."

The caption on the same page reads: "Figure 1 − Bernardino d'Asti. Reception of a capuchin missionary by a local ruler. Italy, ca. 1740. Watercolor on paper".

The new text ties the claim to the watercolor and to Fromont's reading of it, which is faithful, and the date "ca. 1740" comes from the p. 12 caption. The old text was a defensible generalisation, since Fromont's "their uniform" does imply a standing marker. Still, it stated as a general fact what the page offers as a description of one image, so the new text is the safer reading. Neither version is wrong.

Low note: the body text on p. 13 says the *Missione in Prattica* was "composed around 1750", and p. 8 speaks of "friar Bernardino's 1750s watercolors". The source contradicts itself, and the new text takes the caption's date. That is acceptable because the caption sits at the cited p. 12, but a reader may notice the 1740/1750 tension.

## 84b — "object 318318" → "record 318318" — AGREE

Served sentence (Met Overview label, live and 2026-03-14 `id_` capture):
> "Uniting symbols of Kongo religious and secular power, this prestige staff was used as an insignia of office by a Kongo chief. At its summit is a brass pendant of St. Anthony of Padua, one of the most beloved saints in Kongo Christianity."

The same page's tombstone reads "Object Number: 1999.295.2". 318318 is the collection record / objectID in the URL (`/art/collection/search/318318`). "Object 318318" therefore collides with the Met's own "Object Number" field; "record 318318" is correct. The page has one "Overview" heading, so the locator holds.

The surrounding sentence ("A Kongo chief's staff topped by Saint Anthony of Padua, held by the Met, served as an insignia of office") matches "At its summit is a brass pendant of St. Anthony" and "used as an insignia of office by a Kongo chief". There is no overread.

## Residual risk and verification gaps

- Fix 82 depends on Wayback availability at acceptance time. One of the two listed captures was throttled (429) twice in this session under urllib.
- The Met live page answered curl with 429 once, but reopen-quote LOCATED it on the live URL, and the `id_` capture also LOCATED it.
- Fix 18's page call rests on archive.org's `_djvu.xml` footer coordinates plus three TOC cross-checks (468, 472, 475); I did not open the page images. `scandata.xml` asserts no `pageNumber` for leaves 526–533.
- Not checked (not assigned): fixes 85, 89, 93, 97a, 97b, 110, 140, 141, 146, and the speech re-points. For fix 140, see the p. 470–471 page-break note under fix 18.
- I did not run `accept-d.py`; that check belongs to the main agent.
