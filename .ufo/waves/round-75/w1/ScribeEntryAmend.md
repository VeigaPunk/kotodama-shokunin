# ScribeEntryAmend — amendment drafts for claim C (narrative-structure-frameworks)

Seat: scribe, leaf. Round 75 (hyaku run 10), lane `kotodama-shokunin`, base `f556d1049fe651d3d63975600b13acd9fb686f15`.
No subagent, no background job, no mutation of the lane tree, git/jj state, registry, claims, ledger or lesson.

## 1. Behavior — what this seat produced

Two draft files, both under `.ufo/waves/round-75/drafts/`, neither written into `corpus/`:

| path | source | shape |
|---|---|---|
| `narrative-structure-frameworks.amend-2026-10-23.md` | rebuilt from staged `…amend-2026-10-23.md` | 11 968 B, 5 sections, 1 452 body words |
| `narrative-structure-frameworks.amend-2026-10-23b.md` | combined from staged `…amend-2026-10-23b.md`, `…-23c.md`, `…-2026-10-24.md` | 10 186 B, 6 sections, 1 156 body words |

Both carry the lane's provenance header in order — `source:` ×3, `verified-at:`, `recheck:`, `ground:`, `topic:`, `gap filled:`, `sources:`, `couples:`, `scope:` — a title of the form `# Amendment — …`, at least one `## ` section, and no placeholder token or angle-bracket field value.

The second file is a **candidate for a later round, not for this landing**: claim C's frozen `entries` list names two paths, so `-23b.md` must not enter `corpus/knowledge/` this round (see §6.2).

## 2. Read set (all reads, no edits)

- `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23{,b,c}.md` and `…amend-2026-10-24.md` (read-only staging).
- `reports/round-75/claims.json`, `reports/round-75/ledger.json` (draft, pre-data; read only).
- The three documents themselves, fetched in this seat's own scratch (see §3) — the staged quotes were **not** trusted.
- Lane gate material: `corpus/QUALITY.md` §10 and the UA paragraph at line 70, `tools/check-cited-lines.py`, `.ufo/waves/round-75/w1/ScoutPersee1113.md`, `…/ScoutPersee1120.md`, `…/ScoutPersee1114.md`, `…/ScoutUnigeSZ.md`, `…/ScoutUnipaWayback.md`, `…/ScoutThemeTriage.md`, and the sibling drafts `narrative-structure-frameworks.md`, `lesson.md`.

Base-state facts re-derived in this lane (read-only `git show`):

```
git ls-tree -r --name-only <base> corpus/knowledge | grep -ci narrative            -> 0
git show <base>:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' -> 808
git show <base>:corpus/SOURCES.md | grep -c 'comm_0588-8018_1966'                  -> 0
```

## 3. Fetch record — each User-Agent bound to the response it got (QUALITY 22)

All requests were plain `curl` GETs: `automation: none`, no browser automation, no login, no challenge present in any body used. Scratch: `/fast/scratch/hyaku/kotodama-r75/ScribeEntryAmend/` (deleted on exit; nothing below points at it).

UA `Mozilla/5.0 (X11; Linux x86_64) hyaku-r75-scribe/1.0`:

| page | URL suffix | HTTP | bytes | sha256 |
|---|---|---:|---:|---|
| Barthes p. 5 | `…_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0005_0000` | 200 | 4 286 | `8998f55ea7e913d0a82fbed9aacbf312d3fbdb3b1a33066288688c102834fbdf` |
| Barthes p. 6 | `…/T1_0006_0000` | 200 | 3 811 | `efee74ba5aaa3723f32e2fe2f983467645d0db3c6db7ec223194c82cd2f0348d` |
| Barthes p. 11 | `…/T1_0011_0000` | 200 | 4 061 | `9cbf7c9485a6683c709a6f94d72d0251f5c746028f5a233b72cadd1ecd885143` |
| Barthes p. 26 | `…/T1_0026_0000` | 200 | 4 390 | `fbe16353fb945c97811db21b9f5d414c04f39f0c1be513e67668fe32b356807b` |
| Todorov p. 139 | `…_num_8_1_1120/…_T1_0139_0000` | 200 | 3 939 | `16992c94b5e8b314afc2fb8c4ccc297cdc3199855d6fff68f518006b4e17d724` |
| Todorov p. 140 | `…/T1_0140_0000` | 200 | 3 933 | `1930e5ab152ef7aacc652b95b895aa7254d63f0b7e5a2a47221548ffe6f5878d` |
| Todorov p. 141 | `…/T1_0141_0000` | 200 | 3 936 | `b661bca320c147bd40f37ed6651f242a5f92006276aa7c2bf7d9172e2e0ad4b1` |
| Greimas p. 29 | `…_num_8_1_1114/…_T1_0029_0000` | 200 | 3 451 | `84557aef3cac190d5f838e03aa2d1abcf24420e51b4c99c5671c48afe6e42773` |
| Greimas p. 30 | `…/T1_0030_0000` | 200 | 3 737 | `2502768202dbd0e0b17f6310ad4b0c6cfe7e3d1edbd490efab5f7c4f71fe082f` |
| Greimas p. 31 | `…/T1_0031_0000` | 200 | 3 856 | `9aede241c8e9f05ff396b6c0dbb5ddcdc9aeb31adabc5f44f3b941bcf792f1c6` |
| Geneva S/Z fiche (live) | `https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html` | 200 | 44 337 | `190379803c7d00ecf8ad57301bb842d73de80deb03def7162b7713a0bf73bd95` — **challenge body**, not the article |
| Geneva S/Z fiche (Wayback, `id_`, 20041220223357) | `https://web.archive.org/web/20041220223357id_/http://www.unige.ch:80/lettres/framo/cernet/biblio/barth70.html` | 200 | 3 898 | `69b5987240ccd7287e4e297f7333be9ed2ceb47a91cf697d196d5cd6b1f2b494` |
| Palermo deposit (live) | `…/iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf` | 403 | 5 697 | `9a9306f9bce3fba250f1abf5900ad5b80fac05fccf06969c7970164be4de921d` |
| Palermo deposit (Wayback, `if_`, 20251111222249) | `https://web.archive.org/web/20251111222249if_/https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf` | 200 | 763 802 | `8c0303670ff5db8625d034be958ad5729a2c79fa77f3642efc5f6341fb25a19a` |

UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`:

| page | HTTP | bytes | sha256 |
|---|---:|---:|---|
| Barthes p. 10 (`…/T1_0010_0000`) | 200 | 4 320 | `8fe43d677a3cec8689184ec0129763650cebd4bce5b895e5b0b539df6da4fcd4` |
| Geneva fiche (live, re-probe) | 200 | 43 676 | challenge body (`What code is in the image`), not the article |
| Palermo deposit (live, re-probe) | 403 | 5 867 | `cf-mitigated: challenge` per ScoutUnipaWayback's record of the same URL |

The four Barthes page bodies, the Todorov p. 139 body and the Greimas p. 30 body are **byte-identical** to the same URLs fetched by the scouts under a Firefox UA (`ScoutPersee1113`, `ScoutPersee1120`, `ScoutPersee1114` records) — cross-UA stability, and independent of the seat that proposed the quote.

Both walls held under both UAs (QUALITY 10, line 70): the Geneva page's live body is a JavaScript/bot challenge under the custom and the Chrome UA alike; the Palermo deposit is 403 under both. The challenge was met and not passed; each document was then read from the ordinary archive capture of the same path, which is the lane's ordinary-means route, and neither file claims anything about the live pages' present content.

## 4. Draft 1 — `.ufo/waves/round-75/drafts/narrative-structure-frameworks.amend-2026-10-23.md`

Cites S885 (Barthes, pp. 5 and 26, with pp. 6, 10, 11 read for the sibling file), S886 (Todorov, pp. 139–141), S887 (Greimas, pp. 29–31). Five sections: Todorov's three categories and the temporal seam; Greimas's two isotopies and the equivalence to establish; Barthes's levels and the two readings; what the three do together and where they differ; provenance limits.

Every quoted span below was located **exactly once** in the extracted body after NFKC + whitespace folding, and its word/character count in the draft is the count measured on the normalized span:

- p. 139 — "où s'exprime le rapport entre le temps de l'histoire et celui du discours" (13 w); "Le temps du discours est, dans un certain sens, un temps linéaire, alors que le temps de l'histoire est pluridimensionnel." (20 w); "Les formalistes russes voyaient dans la déformation temporelle le seul trait du discours qui le distingue de l'histoire" (18 w); "la nature des événements compte peu, seule importe la relation qu'ils entretiennent" (12 w).
- p. 140 — "L'enchaînement consiste simplement à juxtaposer différentes histoires" (7 w); "L'enchâssement, c'est l'inclusion d'une histoire à l'intérieur d'une autre" (9 w).
- p. 141 — "l'aspect reflète la relation entre un il (dans l'histoire) et un je (dans le discours), entre le personnage et le narrateur" (21 w).
- p. 29 — "Le récit, pour avoir un sens, doit être un tout de signification et se présente, de ce fait, comme une structure sémantique simple." (23 w).
- p. 30 — "se situe, lui aussi, sur deux iso- topies à la fois" (11 w, damage marked); "donne lieu à deux lectures différentes, l'une sur le plan discursif, l'autre, sur le plan structurel" (16 w); "par isotopie nous entendons un ensemble redondant de catégories sémantiques qui rend possible la lecture uniforme du récit" (18 w).
- p. 31 — "est celui de l'équivalence à établir entre les lexemes et les énoncés constitutifs des séquences narratives et les articulations structurelles des contenus qui leur correspondent" (22 w); "Une telle conception du message qui serait lisible sur les deux isotopies distinctes et dont la première ne serait que la manifestation discursive de la seconde, n'est peut-être qu'une formulation théorique" (31 w); "l'enchevêtrement, dans une seule narration, des séquences situées tantôt sur l'une, tantôt sur l'autre des deux isotopies" (17 w).
- p. 5 — "Ce concept est celui de niveau de description" (8 w); "aucun niveau ne peut à lui seul produire du sens" (10 w); "toute unité qui appartient à un certain niveau ne prend de sens que si elle peut s'intégrer dans un niveau supérieur" (21 w); "projeter les enchaînements horizontaux du « fil » narratif sur un axe implicitement vertical" (14 w).
- p. 26 — "la dystaxie oriente une lecture « horizontale », mais l'intégration lui superpose une lecture « verticale »" (17 w); "très souvent une même unité peut avoir deux corrélats, l'un sur un niveau (fonction d'une séquence) l'autre sur un autre (indice renvoyant à un actant)" (25 w).

Staged elements **dropped or corrected**, each against located text:

1. "characters' words against the narrator's" — not located on pp. 139–141; dropped. What the pages carry is the *aspect* relation (character vs narrator as *il* vs *je*), which the draft states that way.
2. "the level of appreciation carried by each part of a story" — not located; dropped.
3. "the two must be set equivalent" (Greimas) — the page states an equivalence **to establish** between lexemes/utterances and content articulations, and then hedges the whole two-plane model as possibly "une formulation théorique" that may hold only for folk tales. The draft carries the hedge instead of the identity.
4. "the full text was readable because the per-page transcription returns all 27 pages" — superseded by what was actually fetched: 11 pages this seat, and ScoutPersee1113 measured all 27 endpoints returning 200 (a notice-only body is p. 1, not the whole article). The draft scopes itself to the pages it read.

## 5. Draft 2 — `.ufo/waves/round-75/drafts/narrative-structure-frameworks.amend-2026-10-23b.md` (candidate, later round)

Cites S885 (Barthes pp. 6, 10, 11), S891 (Geneva *S/Z* reading sheet, via the 2004 capture), S892 (Marrone, *SIGNATA* 5, printed p. 58, via the 2025 capture). Six sections: the article's three levels and their credits; the functional level's four classes; the five codes as a reading sheet names them; the peer's *partial* relation; what the lane does with it; provenance limits.

All quoted spans located exactly once: p. 6 "On propose de distinguer dans l'œuvre narrative trois niveaux de description" (11 w) plus the three credited level names; p. 6 "un profil provisoire, dont l'avantage est encore presque exclusivement didactique"; p. 11 the two halves of "Noyaux et catalyses, indices et informants (encore une fois peu importe les noms), telles sont" / "les premières classes entre lesquelles on peut répartir les unités du niveau fonctionnel" (15 w + 13 w, split because the OCR breaks "semble- t-il" between them); "Les indices impliquent une activité de déchiffrement"; "les informants apportent une connaissance toute faite"; "un opérateur réaliste"; "l'informant (par exemple l'âge précis d'un personnage) sert à authentifier la réalité du réfèrent"; "une unité peut appartenir en même temps à deux classes différentes"; p. 10 "Disons qu'on ne peut supprimer un noyau sans altérer l'histoire, mais qu'on ne peut non plus supprimer une catalyse sans altérer le discours." (23 w); S891 "Fiche de lecture", "(DKW, mai 2000)", "cinq grands codes que vont rejoindre tous les signifiés du texte" (11 w), the five glossed names, "le lieu de disparition des voix dont est tissé le texte" (11 w); S892 "Mais combien, et de quelle nature, sont ces codes ?" (10 w, 51 chars), "ces cinq codes sont en partie une reformulation des quatre niveaux du récit individués dans l'« Introduction à L'analyse structurale des récits » (1966) : fonctions, actions, indices et informants" (30 w), "Le code proaïretique est en quelque sorte une synthèse des fonctions et actions" (13 w), "proaïretique, sémantique, culturel, herméneutique" (4 w).

Material corrections the second file records, all from located text:

1. The Geneva document is a **fiche de lecture** signed "(DKW, mai 2000)", a secondary reading sheet about *S/Z* — not "the accessible French excerpt of the primary text" the staged file called it.
2. Its five names are **herméneutique, sémique, symbolique, proaïrétique, gnomique** (with "code culturel" as the gloss of *gnomique*); the staged English list said "semantic" and "cultural", which are the peer's labels, not this page's.
3. The staged "a set of simultaneous voices" is not what the page says: the codes are "le lieu de disparition des voix dont est tissé le texte".
4. The 1966 article names **three levels** (fonctions, actions, narration, each credited) and divides **one** level into four classes (noyaux/catalyses, indices/informants). The "four levels" in the scholarship is a compression; S892's own word is *en partie*.
5. The noyau/catalyse criterion is **not** on p. 11 (which opens after it); it is on p. 10 and is a deletion test.
6. The two secondary lists differ in two labels (sémique/sémantique, gnomique/culturel), which is why the entry keeps both and claims only the five-part structure.

Refusal notes for the lesson (staged `-23c` and `-2026-10-24`, and the separate-file status of `-23b`):

- `narrative-structure-frameworks.amend-2026-10-23b.md` (staged): the cited document **does** open by ordinary means (2004 capture of the Geneva page; live page challenged under both UAs) and contains the five-code paragraph. Refused **only** as a landing this round: claim C's frozen `entries` list is two paths. Flip: land as an appended amendment in a later round, citing S891, with the corrections in §5.1–5.3 applied.
- `narrative-structure-frameworks.amend-2026-10-23c.md` (staged): its p. 11 claims locate (S917's URL class = lane S885), but the file also defines noyaux/catalyses from memory — the definitions are on p. 10, not p. 11. Refused as a separate file; content folded into the `-23b` draft with the locator corrected. Flip: none needed beyond the same later-round landing.
- `narrative-structure-frameworks.amend-2026-10-24.md` (staged): both cited documents open (S892 via capture; p. 6 page text). Its "four levels ... individually named in the 1966 Introduction" is wrong as stated — three levels plus four classes. Refused as a separate file; content folded into the `-23b` draft with that correction. Flip: same later-round landing.

## 6. Gates applied, and what the drafts still need from other seats

Checks this seat actually ran, on both files (no other verification was performed):

```
python3 -B tools/check-cited-lines.py .ufo/waves/round-75/drafts/narrative-structure-frameworks.amend-2026-10-23{,-23b}.md
CITED-LINES: 0 finding(s) in 2 file(s)
```

Plus: one S-id per line (no `MULTI-ID`), no `TABLE-ID`, header field order and placeholder sweep (§1), body words 1 452 and 1 156 against the 478-word floor.

Handed to other seats, because this seat cannot do them:

1. **Gate/evidence (ExecEvidence, ScribeLesson).** Rows S885, S886, S887 need the `## Gate` record with URL + 2026-10-27 + a located quote ≤25 tokens and ≤80 chars + locator, and `reports/round-75/evidence/<id>.txt` windows. Candidate Gate quotes from the verified spans: S885 "aucun niveau ne peut à lui seul produire du sens" (10 w, 48 c) or ScoutPersee1113's "Ce concept est celui de niveau de description" (8 w, 45 c); S886 "voyaient dans la déformation temporelle le seul trait du discours" (10 w, 65 c); S887 "deux lectures différentes" (3 w, 24 c) — a longer clean alternative is "donne lieu à deux lectures différentes" (6 w, 40 c). For the candidate file: S891 "cinq grands codes que vont rejoindre tous les signifiés du texte" (11 w, 64 c); S892 "Mais combien, et de quelle nature, sont ces codes ?" (10 w, 51 c).
2. **Registry (executors).** `used-by` for S885 must name every admitted entry whose `source:` line cites it — as drafted that is `myth-symbol/narrative-structure-frameworks.md`, `…amend-2026-10-23.md`, and (only if it lands) `…amend-2026-10-23b.md`. S886/S887: the `-23` amendment only. S891/S892: the `-23b` candidate only.
3. **S885 scope/tier.** ScribeEntryBase's base-entry draft now carries a two-branch table and defers the tier to the Gate; my amendment cites S885 at pp. 5, 6, 10, 11, 26 as tier A. Both read against whichever branch the Gate records; the report's §3 is the fetch binding that branch needs.

   **Deliberate decision on used-by for S885.** The staged `…amend-2026-10-23.md` is two amendments in one path: the Todorov/Greimas half, and a second half headed "the Western anchor, read at the level of description" that cites S885 at pp. 5 and 26. That second half is **rebuilt, not dropped**: it is §3 of draft 1. So S885's `used-by` is, as drafted, the base entry plus `…amend-2026-10-23.md` (plus the `-23b` candidate if that ever lands) — not the base entry alone.
4. **README (ScribeReadmeIndex).** Sent the exact `- topic:` text for the `-23` amendment and flagged the staged topic as superseded.

## 7. Conflicts, reported verbatim and unresolved

1. **Row-set contiguity vs the lesson draft.** `reports/round-75/claims.json` pins `row_set` to eight rows, contiguous `S885..S892`; the lesson draft's claims line says "eight rows S885–S892 opened and mined (plus S893, the re-opened S870 document)". A ninth row is not in the frozen row set and `ROWS` admits exactly the frozen set. Either claim C is amended pre-freeze or S870/S893 must not be appended; the two texts cannot both stand.
2. **REPOINTED leg vs lane ids.** The leg says "staged ids S864..S876 and S885..S921 appear in neither entry as lane rows", while the row set itself allocates S885–S892 and the seat instructs citing S885/S886/S887. The `id-renumber-map.json` reads staged→lane *by document*, and staged S885/S917/S921 are the same document as lane S885. The leg needs the exemption "staged ids that are not adopted lane ids"; as written it would fail its own frozen row set.
3. **S885's role.** Staged text: the Western claims rest on the notice and the opening paragraph only. This seat: plain GET, no challenge, page-level bodies for pp. 5, 6, 10, 11, 26 (hashes §3), tier A for the article's own wording. ScoutPersee1113: ADMIT page-level, all 27 endpoints 200. ScoutPersee1113 also notes the page-level endpoints have **no** Wayback capture (CDX `[]`), so they must not be described as archived. Not resolved here; the Gate record decides.
4. **Base entry's `couples:` line** names "the S/Z codes" as belonging to `…amend-2026-10-23.md`, which does not carry them (they are in the `-23b` candidate). Flagged to ScribeEntryBase; no edit made by this seat.

## 8. Out of scope for this seat

Registry rows, id-renumber map, Gate records, evidence windows, `corpus/README.md` index rows, the lesson text, `claims.json`/`ledger.json`, counters, controls, commits. No tool was installed and no tool was upgraded. No file outside the two draft paths and this report was created, modified or deleted; `/fast/scratch/hyaku/kotodama-r75/ScribeEntryAmend/` is removed before this seat yields, and no evidence above cites a scratch or `/tmp` path.

## 9. Artifacts

- `.ufo/waves/round-75/drafts/narrative-structure-frameworks.amend-2026-10-23.md`
- `.ufo/waves/round-75/drafts/narrative-structure-frameworks.amend-2026-10-23b.md` (candidate; do not land this round)
- `.ufo/waves/round-75/w1/ScribeEntryAmend.md` (this report)
