# Falsify — SOURCES S053 (Eczet 2020, OpenEdition tc/14002)

- **Item attacked:** `corpus/SOURCES.md:82` row S053 (landed at `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`), its Gate bullet `corpus/lessons/round-50.md:38`, and every S053 citation in `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` (`:7`, `:11`, `:181`, `:195`).
- **Verdict:** **HOLDS** — quote byte-identical, anchor location exact, tier A claim-scoped honestly, all four entry citations supported by the live full text. Three precision notes below, none of which breaks a named claim.
- **Base/commit read:** all lane bytes via `git -C … show 1c779e4a…:<path>`; no working-tree reads, no lane edits, no clone needed.

## 1. Route and HTTP status (live, 2026-10-21)

`journals.openedition.org` is behind **Anubis v1.26.2** proof-of-work for non-JS clients. Plain fetch of the row URL:

```
$ curl -sS -A '<Chrome/124 UA>' -L https://journals.openedition.org/tc/14002
HTTP:200 SIZE:5281 TYPE:text/html; charset=utf-8
```

That 5,281-byte body is `#anubis_challenge` (difficulty 2, method `fast`), **not** the article. Solved the challenge honestly in-session (sha256(randomData+nonce) with two leading hex zeros; nonce 23), submitted `/.within.website/x/cmd/anubis/api/pass-challenge?…` → `302` + `set-cookie: techaro.lol-anubis-auth=…`, then re-fetched the row URL:

```
HTTP:200 SIZE:203819 TYPE:text/html; charset=UTF-8
<title>Logiques totémiques dans le cattle complex</title>
```

No login, no credentials. **Operational finding:** a future re-opener that only curls the URL sees an HTTP 200 challenge page and no article text; re-verification of this row needs a JS/PoW-capable client. Do not read the 200 as "article gone" or as "text absent".

## 2. Quote and location

Page metadata (`<meta>`): `citation_publication_date = 2020/juil./01` (the page's embedded publication timestamp is `2020-07-01T00:00:00+02:00`), `citation_journal_title = Techniques & Culture. Revue semestrielle d’anthropologie des techniques`, `citation_doi = 10.4000/tc.14002`; byline **Jean-Baptiste Eczet**; breadcrumb **Suppléments aux numéros 2020 → Suppléments au n°73**. Row title/authorship/year/journal/URL all match.

The Gate quote at `corpus/lessons/round-50.md:38`, between the quotation marks, is **172 characters**; the first `<p class="paragraphesansretrait">` inside `<div class="text wResizable">` ("Texte intégral") begins with exactly those 172 characters:

```
L’omniprésence des bovins dans les pratiques et les discours des populations nilotiques d’Afrique de l’Est fut à l’origine de l’expression cattle complex (Herskovits 1926).
```

Programmatic check (`l[i+1:j] == page_paragraph[:172]`): **True**, character-for-character (curly apostrophes included). The sentence is *not* the abstract — the Résumé opens "De nombreux gestes et pratiques des pasteurs d’Afrique de l’Est furent interprétés…", so the anchor "Texte intégral, opening paragraph" is precise, not an abstract-attribution slip. `(Herskovits 1926)` is present; the page italicises *cattle complex* via `<em>`, text otherwise verbatim.

Evidence that the attribution is real, not a mis-citation — the article's bibliography: `Herskovits, M. 1926 « The cattle complex in East Africa », American Anthropologist 28 : 230-272, 361-388, 494-528, 633-664.`

## 3. Tier and scope under QUALITY criterion 6

`corpus/QUALITY.md:29` (criterion 6): A is reserved for sources primary or authoritative for the exact scope; publisher descriptions/abstracts are B for substantive claims. Row scope is *"the article's own attribution … and its critique of the analyst vocabulary; not Herskovits' text"* — for its own attribution and critique the article is primary, so **A is honest**, and the row explicitly excludes the one thing that would need Herskovits himself.

Substance confirmed in the live full text (¶1, note 1):

> « Pour justifier ces pratiques dépassant la production de protéines lactées et carnées, une obsession pour l’animal est parfois avancée. Déjà présente chez Evans-Pritchard … reprise par Hardin (1968) pour illustrer sa notion de « tragédie des communs », impliquant un manque de rationalité dans l’élevage … Elle laisse libre cours à des analyses psychologisantes … Ces dérives analytiques sont rendues possible … par l’usage de plusieurs notions, dont on ne sait parfois si elles ont une valeur émique … ou étique (la traduction d’une pratique dans les termes de l’analyste) : imitation, identification et équivalence … »

So "critique of the analyst vocabulary" is the article's own stated programme, including the émique/étique distinction, and it extends to the irrationality/"obsession" reading that underwrites the prestige-pathology claim.

## 4. Every S053 citation in the knowledge entry

| Entry line | Sentence citing S053 | Holds? |
|---|---|---|
| `:7` | "S053 Eczet 2020 (the \"cattle complex\" label and its critique)" | **Yes** — attribution + critique both verified above. |
| `:11` | "open the Herskovits 1926 text before quoting him (only S053's attribution is opened)" | **Yes** — the row itself says "not Herskovits' text" and "Herskovits 1926 itself unopened". |
| `:181` | "C — S053 attributes the label to Herskovits 1926 and criticises its analyst vocabulary; the 1926 text is unopened `(to-verify)`" | **Yes** — exactly the article's first sentence + ¶1 critique; the unopened flag is honest. |
| `:195` | "(only S053 and S055 are opened)" | **Yes** — consistent with the row and `:11`. |

The §13 status **C (contested)** is defensible: the article names Hardin's reuse as implying « un manque de rationalité dans l’élevage » and attacks the psychologising analyses that turn the cattle relation into pathology, which is the mechanism behind the "hoard for prestige" framing.

## 5. Precision notes (smallest fixes; none falsifies the row)

1. **Row "teaches" gloss over-reads slightly.** `corpus/SOURCES.md:82` says "the cattle-complex label is an etic analyst construct **of contested standing**". The article does treat the label as analyst coinage (Herskovits 1926, from Graebner's *cultural complex*), but it does **not** contest the label's validity — it retains and extends it: "j’ai, ailleurs, proposé qu’à la notion de cattle complex puisse s’ajouter celle de colour complex (Eczet 2010)". The contested thing is the imitation/identification/équivalence vocabulary and the irrationality reading. Smallest fix: replace "of contested standing" with "and the vocabulary used to describe the relation is criticised; the author retains and extends the label (colour complex)". The entry's own `:181` sentence is already narrower than the gloss and needs no change.
2. **`:181` third column is unsourced by S053.** "herd size answers labour, risk and tenure" is not in the article. Term counts over the extracted full text (52,180 chars, re-fetched and reproduced identically): `prestige` 0, `hoard` 0, `thésauris` 0, `accumul` 0, `tenure` 0, `main-d’œuvre` 0, `taille du troupeau` 0; `risque` has 1 hit, unrelated ("au risque de percuter l’assemblée", dancers). It reads as lane synthesis sitting in a row whose only source marker is S053. Smallest fix: mark it "(lane synthesis; cf. S048/S049)" or drop it from the S053 row.
3. **`corpus/lessons/round-50.md:38` universal.** "Herskovits 1926 itself unreachable on every route" is stronger than the row's honest "unopened". Not falsified here (archive.org was offline today; Wiley/AnthroSource and JSTOR are gated, though JSTOR's stable record advertises Part I as free-to-read — search snippet, not opened). Smallest fix: soften to "unopened this round (archive.org offline; Wiley/JSTOR gated)". The row itself needs no change.

## 6. Not found / unresolved

- `corpus/README.md:297` carries the pastoralism entry at entry level and no S053 id, so there is no row-level README claim to check for this source.
- No full-text copy of Herskovits 1926 was obtained (out of scope; row correctly claims only attribution).
- The Anubis challenge makes the row URL's content unverifiable by a plain HTTP re-opener; that is a method note for the Gate's recheck step, not a row defect.
- No installs or upgrades were performed (curl + Python 3 stdlib + preinstalled BeautifulSoup 4.15.0 only); temp fetch artifacts under `/tmp` were deleted.
