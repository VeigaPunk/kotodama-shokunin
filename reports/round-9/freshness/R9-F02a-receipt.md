# R9-F02a — freshness receipt (primary-source / museum-record hunter)

- **Round 9, F / freshness, residual R8-F02 = R6-02-B** (kaunakes / tufted-skirt terminology vs
  a dated object or scholarly source; naming vs pictured texture vs fibre/construction).
- **Entry under test:** `corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md`
  (sha256 `bf6c92f9a347d361a37f5aa1080d9d04ac6d37d56c01b0ea92e87ed697a4b478`, 195 lines — unchanged
  since round 8; the word "kaunakes" does not occur in it: `grep -n -i "kaunak" …` → no match, exit 1).
- **Row bounded:** line 142, "Early Dynastic votive and elite imagery".
- **Date of all retrievals:** 2026-10-17 (write at 20:57Z).
- **Machine form:** `reports/round-9/freshness/R9-F02a-receipt.json` (read that for fields, counts,
  commands and full excerpts).

## Raw labels preserved (verbatim, prior rounds)

| Layer | Label |
|---|---|
| Round-6 worker | verdict `supported`, support_scope `whole-bounded-claim` |
| Round-6 parent reconciliation | `unresolved`; main passage not eligible; effective source kind `tertiary`; limits: "Named books, Breniquet's article and first-hand dated-object texture descriptions were not retrieved." |
| Round-8 receipt | disposition `resolved`, with three explicit non-resolutions (Breniquet body unread; LSJ papyri citation-only; fibre/construction an open plurality) |

Round 9 adds a third layer below; it does not overwrite those labels.

## Escalation strategies run (4)

1. **First-hand dictionary read of the native-term candidate** — streamed the official ISAC scan of
   CAD vol. 1 (A/1), read `aguhhu` at printed pp. 159-160 (pdf pp. 194-195), default + `-layout`
   pdftotext modes. Volume identity taken from the scan's own title pages (1964; ISBN 0-918986-06-0;
   fourth printing 1998).
2. **Multi-institution dated-object museum sweep** — three new Louvre notices opened first-hand; Met
   (v1.1), Cleveland, Art Institute of Chicago, Ashmolean, British Museum, Penn, UrOnline, Brooklyn,
   Yale probed with controls.
3. **First-hand scholarly text** — the authorial abstract of Breniquet 2016 (article body still
   paywalled) plus the open-access HAL PDF of Breniquet & Michel 2014.
4. **Tablet-level probe** (CDLI / ORACC-ePSD2 / Archibab) — attempted; blocked; documented so that
   silence is not read as absence.

## The findings that matter

### 1. CAD vol. 1 (A/1), 1964, s.v. `aguhhu` — the only native candidate term is read as a sash

Source: [cad_a1.pdf](https://isac-assets.s3.amazonaws.com/isac-publications/cad_a1.pdf) (ISAC
publication page: [Chicago Assyrian Dictionary](https://isac.uchicago.edu/research/publications/chicago-assyrian-dictionary)),
retrieved 2026-10-17 by `curl | pdftotext` (42,429,708 bytes; Last-Modified 2026-06-07).

> `aguhhu s.; 1. (an article of clothing, perhaps a sash), 2. (uncert. mng.); OAkk., OB, SB.`
> lex: `… a-gu-uh-hu = me-sir-ru Malku II 230; a-gu-hu = MIN (= lu-bu-su) DINGIR dress of a god
> Malku VI 81 …`; `tug.bar.la.a.gu.hum = a kusitu-garment with an a. Hh. XIX 113`
> mng. 1c: `in OB: 2 TUG a-gu-uh-hu I.A TLB 1 69:14, see Leemans, SLB 1/1 p. 1.`
> mng. 1d: `… Gilgames agusu itepramma rakis a-gu-uh-hu "Gilgames put on his tiara, fastening on
> the a." Gilg. VI 5`
> discussion: `The article of clothing called aguhhu is worn, according to the attested instances,
> after the Ur III period by Istar, by demons, and once by Gilgames. … It is made of wool or
> leather, and the vocabularies as well as the Gilg. ref. (rakasu) indicate that it was a belt or
> sash.`

Why it matters: round 8's native-term hedge rested on a *second-hand* quotation (Jaramago 2023 fn. 26
quoting Breniquet 2016:9, "aguhhum pourrait désigner un textile tissé … avec de longues mèches de
laine"). The dictionary's own article reads the term differently in kind — a sash/belt of wool or
leather, equated with *mēšerru* in the synonym list Malku II 230, attested after Ur III.
Additional negative: `curl … | pdftotext -f 194 -l 195 - - | grep -c -i "mari"` → **0** — the 1964
article cites no Mari text, so it neither corroborates nor refutes the Mari-based reading.

*Fidelity note:* the ASCII extraction garbles some diacritics/sign names (`kusitu`, `Istar`,
`DINGIR.MES`); only wording legible without ambiguity is quoted, and the garbling is flagged rather
than silently corrected.

### 2. Three new first-hand Louvre notices (five in total with round 8)

- **AO 30207** ([cl010361164](https://collections.louvre.fr/en/ark:/53355/cl010361164)) — *"Statuette
  d'orant imberbe crâne rasé, mains jointes, vêtu d'une jupe de **mèches laineuses dite kaunakès**,
  queue à l'arrière … Anépigraphe."* Date **Dynastique archaïque III (-2600 - -2340)**; albâtre (?),
  gypse (?); discovered in Iraq; now on long-term loan at Cannes; notice last updated 18.10.2022.
  This is the closest thing to a museum-level material statement found: the institution describes
  locks of wool **and** marks the term as a name ("dite"), i.e. naming and material kept separate.
- **AO 18379 ; M. 180** ([cl010143194](https://collections.louvre.fr/en/ark:/53355/cl010143194)) —
  *"Bas du corps d'une adorante, vêtue du kaunakès, dont il subsiste deux rangs."* **DA IIIB
  (-2500/-2340)**; findspot **"Mari temple d'Ishtar cella 17 (près de la porte)"**; discovered
  **23 January 1934** (Parrot mission 1933-34); acquisition 1934, partage après fouilles;
  bibliography **Parrot, MAM I (1956), p. 107, pl. XLIII, n° 91**; notice last updated 30.07.2025.
  Same cella as round 8's Ebih-Il (AO 17551) — a concrete "check it object by object" data point.
- **AO 32526** ([cl010150293](https://collections.louvre.fr/en/ark:/53355/cl010150293)) — *"Fragment
  de statuette ; personnage vêtu du kaunakès"*, calcaire, Mari (Tell Hariri), no date line in the
  fetched notice. Useful counter-example: not every "kaunakès" notice is a dated witness.

The term is a catalogue class at the Louvre (nine notices enumerated through a search-engine result
set — the museum's own search page is bot-walled): `cl010119549`, `cl010155901`, `cl010361164`,
`cl010118550`, `cl010150293`, `cl010142255`, `cl010194671`, `cl010174443`, `cl010143194`. Three were
opened first-hand this round (the three above); two were opened first-hand in round 8.

### 3. The scholarly leg, now first-hand

- **Breniquet 2016, authorial abstract** (record mirror:
  [archive record](https://vigipallia.parlons-fin-de-vie.fr/Default/doc/OAI_4/_b64_b2FpLWNhaXJuLmluZm8tQVNTWV8xMTBfMDAwMQ%3D%3D/que-savons-nous-exactement-du-kaunakes-mesopotamien?_lg=fr-FR);
  HAL record via the public API: [hal-01834706](https://uca.hal.science/hal-01834706v1), `files: 0`):
  > *"Toison d'animal pour certains, étoffe pour d'autres, on ne s'est jamais vraiment accordé sur la
  > véritable nature de cette pièce vestimentaire … faute de découverte archéologique non équivoque."*
  > EN: *"It remains unclear if this piece is an animal fleece or a true fabric, as no archaeological
  > sample of this cloth was found."*
  Plus: the label is a 19th-century orientalist habit ("les archéologues orientalistes ont pris
  l'habitude d'appeler « kaunakès »"), and the Aristophanes route is anachronistic for the Sumerian
  period. **This is the author's own text**, replacing round 8's third-party quotations for those
  propositions; the article body remains unread.
- **Breniquet & Michel 2014, open-access PDF**
  ([halshs-01226052](https://shs.hal.science/halshs-01226052/file/Breniquet-Michel_2014_Wool%20Economy_Introduction.pdf),
  718,471 bytes, retrieved first-hand): *"Because of the poor state of the rare textile remains from
  Mesopotamia…"*; *"As it is not possible to correlate directly bones and fleeces, iconography is
  integrated into the scientific approach as a mean of confirmation"*; Chalcolithic sheep of "a hairy
  coat" vs "a woolly coat" "both found on images". Term check: `grep -c -i "kaunak"` = **0**.

### 4. Counted museum negatives (with commands)

- **Met:** `v1.1/search?q=kaunakes` → 53 objects; full-JSON substring test over all 53 → **0 literal
  hits**; first hit is objectID 660091, a 1946 mugshot of a person named *Kanakes* (fuzzy match, not
  a term index). The v1 search endpoint's own retirement message was retrieved: retired 2026-10-01,
  use v1.1 (Elastic-backed, paginated).
- **Cleveland:** `q=kaunakes` → `total: 0`.
- **Chicago:** `q=kaunakes` and control `q=zzznope` → both `total 133170` (parameter ignored).
- **Ashmolean:** client-rendered page, 231,643 bytes, zero occurrences of "kaunak" in the HTML.

## Deeper-limit receipt (what stays unreadable, named exactly)

1. **Breniquet 2016 article body** — Cairn 403, JSTOR "Client Challenge", ResearchGate 403 (three
   independent routes, all re-attempted 2026-10-17); HAL confirms no deposited full text. Substitute:
   the authorial abstract (first-hand).
2. **Fibre/construction of any specific object** — no fetched museum record states a fibre analysis or
   construction; the strongest wording is the Louvre's descriptive "mèches laineuses dite kaunakès".
   The methodological reason is now documented first-hand (rare, poorly preserved Mesopotamian
   textile remains; bones/fleeces not directly correlatable).
3. **Tablet-level collation** of the dictionary's cited witnesses (TLB 1 69:14; Kocher, MIO 1 76
   iv 50; Gilg. VI 5; KAR 306:24; KAR 357:28) — CDLI's JSON search ignores the query parameter
   (identical payloads for `aguhhum`, `tug2` and the control `zzznotaword`), ORACC ePSD2 term paths
   404, Archibab exposes no public endpoint from this host. No counted tablet-level negative is
   claimable this round.
4. **Parrot, MAM I (1956), pl. XLIII n° 91** (published plate for the findspot-dated Mari object) —
   citation-only pointer from the museum record.
5. **BM / Penn / Ashmolean / Brooklyn / Yale / UrOnline** — 403, 403, SPA-only, 429, 404, connection
   timeouts (commands and statuses in the JSON `access_failures`). Unreached ≠ absent.

## Disposition (this leg)

**Partial-support-or-better achieved for the primary-source / museum-record leg.** First-hand passages
now carry the three legs round 6 marked missing: a dictionary reading of the native candidate term,
dated-object museum records, and the author's own scholarly text. The fibre/construction question
remains an open plurality *by design*, exactly as the entry's limit column requires. **No entry edit
is proposed.** Sibling round-9 freshness receipts were not present in the tree at write time
(only a peer scratch directory `.scratch-v03`), so this receipt makes no claim about other legs.

## Reproduce

```bash
cd kotodama-shokunin
sha256sum corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md        # bf6c92f9… (195 lines)
grep -n -i "kaunak" corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md   # no match (exit 1)
# CAD A/1 aguhhu (pp. 159-160 of the printed volume; pdf pp. 194-195):
curl -sSL https://isac-assets.s3.amazonaws.com/isac-publications/cad_a1.pdf \
  | pdftotext -layout - - | awk '{n=gsub(/\f/,"",$0); p+=n; printf "PG%d|%s\n", p, $0}' \
  | grep -E "aguhhu" | head -40
# Met negative sweep (53 objects -> 0 literal):
curl -sS "https://collectionapi.metmuseum.org/public/collection/v1.1/search?q=kaunakes&limit=50"
# self-check of this receipt:
python3 -c "import json;d=json.load(open('reports/round-9/freshness/R9-F02a-receipt.json'));print(d['id'],len(d['fresh_retrievals']),sum(1 for r in d['fresh_retrievals'] if r['retrieved_passage']),len(d['access_failures']),len(d['escalation_strategies']),len(d['negative_sweeps']))"
```
