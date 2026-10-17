# R9-F04c — alternate-angle retrieval receipt (residual R8-F04 / prior R6-07-A)

- Round 9, axis **freshness**, strategy **alternate-angle hunter** (the fourth lane of the round-9 escalation).
- Residual: R8-F04, reconciled **unresolved** after round 8 (`reports/round-8/freshness/R8-F04-receipt.json`, raw label there also `partial-support`).
- Entry under test: `corpus/knowledge/civilizations/levant-canaan-phoenician.md`, §4 bullet 1 = **line 78** at this revision (`sha256 2ca21052…`, measured 2026-10-17T20:54:31Z, git HEAD `a7bb205d`).
- Claim: *"The name *mlqrt*, conventionally Melqart, is understood as 'king of the city'; its civic semantics are more productive than assigning the god the modern job 'patron of merchants' alone (Bonnet 1988)."*
- Question: check the king-of-the-city analysis and the limits of a fixed merchant-patron/theological profile against an inscription, philological source or scholarly passage.
- **Worker label: `partial-support`** — both substantive legs now passage-supported on three retrieval channels new to the escalated set; the `(Bonnet 1988)` attribution remains book-level unverified. Reconciled disposition is the reconciler's to set.

Round-9 disposition: partial-support.

## What "alternate angle" means here

Round 8 read Wikipedia + m-saunders.com + the Louvre record + WiBiLex + Euphrosyne. This hunt used four different channels:

1. **Full-text scans of standard works, item-first** (Internet Archive text layers) instead of article-first pages.
2. **Chain-of-citation reversal** — from the tertiary relay sentence to the monograph that is its origin; and from the entry's named authority to **peer reviews of that book** (a route into a book that cannot be opened).
3. **Rival-reading sweep** — testing the entry's hedge "is understood as" against competing glosses in the same open corpus.
4. **Host-level diagnosis** of the repertory that rounds 6–7 could not resolve.

## Passages retrieved (all fetched 2026-10-17, ~20:48–20:54Z)

### 1. Krahmalkov, *A Phoenician-Punic Dictionary* (OLA 90 / Studia Phoenicia XV, 2000) — reference lexicon

Retrieval: `curl -sS -L --max-time 150 -A "Mozilla/5.0 (X11; Linux x86_64)" -o krahmalkov.txt "https://dn721606.ca.archive.org/0/items/phoenician-punic-dictionary-charles-r.-krahmalkov/Phoenician-Punic%20Dictionary%20-%20Charles%20R.%20Krahmalkov_djvu.txt"` → HTTP 200, 898,880 bytes, sha256 `77c9ba63…`.
Locator: entry **MLQRT (B'L SR)**, printed p. 290 (text-layer lines 16216–16231); components MLK III (15869–15879), MLK IV (15881–15888), QRT I (24488–24499).

> "MLQRT (B'L SR) — d. MILQART, principal deity of the city of Tyre; the full name was MILQART, THE BAAL (PROPRIETARY GOD) OF TYRE. KAI 47.1 (Ph) l'dnn Imlqrt b'l sr, <Dedicated> to our lord, Milqart, the proprietary god of Tyre. … Frequent in Ph and Pu personal names, in which the name is sometimes found in the abbreviated form qrt, Qart: see QRT II."

> MLK III: "[Heb. melek] n.m. KING — KAI 1.1 (Ph) 'hrm mlk gbl, 'Ahiram, King of Byblos.'" · QRT I, pl. QORHT: "[Heb. geret, girya] n.f. CITY — KAI 26 A II 9/10 (Ph) … 'And I built this city …'; KAI 26 A III 5 (Ph) kl 'ln grt, 'All the gods of the city.'"

Support: components are lexically *king* + *city*, with published epigraphic citations; the god's standing proprietary title is `b'l sr` (KAI 47.1 quoted verbatim), the civic formula the claim treats as productive; the name abbreviates to `qrt` in personal names (anchor for entry line 146, ʿbdmlqrt).
**Calibration (negative):** Krahmalkov does **not** print the composite "king of the city" — he glosses the god as *Milqart* with the title *Baal of Tyre*. The composite translation is an interpretive gloss carried by the narrative literature (below), not a dictionary headword.
OCR caveat: MLQRT renders as "MLORT", BAAL as "BASAL", qeret as "geret" in the scan's text layer.

Corroboration (discovery only, not counted as passages): Open Library search-inside `https://openlibrary.org/search/inside.json?q=%22mlqrt%22` → **total 76**, hits in Benz *Personal Names in the Phoenician and Punic Inscriptions* (`personalnamesinp0000benz`), Barré *The God-List in the Treaty* (`godlistintreatyb0000barr`), Fulco *The Canaanite God Rešep* (`canaanitegodrese0000fulc`), Huss *Geschichte der Karthager* (`geschichtederkar0000huss` — "Tempel des Mlqrt von Gades").

### 2. Aubet, *Tiro y las colonias fenicias de Occidente* — the relay's own source, read directly

Retrieval: `curl … -o aubet.txt "https://archive.org/download/aubet-ma-eugenia-tiro-y-las-colonias-fenicias-de-occidente/Aubet%2C%20M%C2%AA%20Eugenia%20-%20Tiro%20y%20las%20colonias%20fenicias%20de%20Occidente_djvu.txt"` → HTTP 200, 942,752 bytes, sha256 `6410fc2d…`.
Locator: section **"El templo fenicio y el Melqart de Tiro"**; quotes (a)–(d) between the running heads for printed pp. 140–141, quote (e) between those for pp. 142–146 (text-layer lines 7263–7286, 7416–7498, 7552–7566).

> (b) "En un principio, el Melqart de Tiro pudo ser una divinización del propio rey de la ciudad, el m/k-qrt. De ser así, Melgart, el dios nacional tirio, sería la exaltación teológica del rey … el mismo rey."

> (d) "Con motivo de la fundación de una colonia o enclave comercial, la costumbre tiria exigía construir un templo en honor de Melqart. … la presencia de Melqart garantizaba o advertía de la intervención de la monarquía en toda actividad comercial lejana."

> (e) "la función de los santuarios de Melqart en Occidente consistió en servir de nexo de unión entre Tiro y los centros comerciales mediterráneos. A cambio de velar por la buena marcha de la navegación y del comercio, Melgart recibía la décima parte de las ganancias obtenidas. Su función no fue, así, exclusivamente religiosa, sino básicamente política…"

> (a) "El dios era el señor de la ciudad…" · (c) "Como dios del mar, era el patrón de la navegación y del comercio."

Support: the book Wikipedia relays states the composite analysis itself (king-of-the-city direction) and frames the commercial function as royal **political** integration; and it *does* attribute commerce patronage to the god, as one function — so the entry's "more productive than … alone" wording is right, and must not be tightened into a denial (round-8 limit 6, now demonstrated against the relay's own source).
OCR caveat: `m/k-qrt` is the scan's rendering of the ligature (plausibly *mlk-qrt*); quoted as OCR gives it.

### 3. Jourdain-Annequin, review of Bonnet 1988 — *Revue des Études Anciennes* 92/3-4 (1990) 446–449

Retrieval: `curl -sS --http1.1 --max-time 50 -c cj -b cj -A "Mozilla/5.0" -o page_7ae31a.html "https://www.persee.fr/doc/rea_0035-2004_1990_num_92_3_5573_t1_0446_0000_3"` → HTTP 200, 72,420 bytes, sha256 `24681df7…`.

p. 446 (retrieved page text):

> "Personnification de la planète Saturne (W. Genesius) ou dieu du feu (F. K. Movers) ; divinité solaire (W. W. Baudissin) ou infernale (W. F. Albright) ; dieu de la foudre et de la pluie (Du Mesnil du Buisson), dieu agraire (H. Seyrig) ou figure syncrétique réunissant les fonctions de Baal Hadad … et de Yam ; dieu de la mer (R. Dussaud), Melqart apparaît parfois comme le dieu El lui-même (M. H. Pope) ou bien encore, pour J. Gagé, comme un dieu de la conquête et des conquérants."

Persée's **displayed extract** for the same record (retrieved on `https://www.persee.fr/search?ta=article&q=Melqart+%22roi+de+la+cit%C3%A9%22`, HTTP 200, 304,691 bytes):

> "… et à l'altération du personnage divin appelé Melqart » (P- 9). Melqart (plus correctement vocalisé en Milqart), c'est le « roi de la cité » (mlk qrt), et, fort logiquement, le périple auquel nous convie l'auteur part…"

Support: the composite gloss appears inside a peer review of the entry's named authority, quoting the book itself (p. 9); and the p. 446 text is the strongest passage yet for the "limits of a fixed profile" half — **ten mutually incompatible modern definitions** of the god in one review paragraph.
Mediation caveat: the "roi de la cité (mlk qrt)" sentence is a **Persée displayed extract**, not a page read (the review's pp. 447–449 are behind Persée's viewer; `?page=447/448/449` returns identical HTML).

### 4. Briquel-Chatonnet, review of Bonnet 1988 — *Syria* 70/3-4 (1993) 603–605

Retrieval: `curl … -o page_a7ff4c.html "https://www.persee.fr/doc/syria_0039-7946_1993_num_70_3_8629_t1_0603_0000_3"` → HTTP 200, 70,471 bytes, sha256 `aa6c4d23…`. Locator: p. 603, opening paragraph.

> "Milqart, le grand dieu de Tyr et le protecteur de l'expansion commerciale de la cité, n'avait jusqu'ici, curieusement, fait l'objet que d'articles partiels et souvent vieillis. La synthèse magistrale que nous propose C. Bonnet est donc particulièrement bienvenue."

Support: second independent peer assessment of the unread book; shows a commercial-expansion role inside how specialists summarise the god — calibration against any over-strict reading of the entry's denial.

### 5. Mesnil du Buisson, *Revue de l'histoire des religions* 164-2 (1963) 133–163 — rival reading

Record page retrieved via FetchURL `https://www.persee.fr/doc/rhr_0035-1423_1963_num_164_2_7927` (p. 133 text: Tyrian temple, Herodotus II.44, two betyls, sacred olive, fire on a pyre). Gloss sentences via the same Persée displayed extract (media: displayed extract):

> "… al de Tyr, le « maître de la ville », ou comme son surnom l'indique, le « roi de la cité ». … On a proposé de comprendre le nom de Melqart : « le Roi de la Cité infernale », parce que le monde souterrain est appelé « la Cité » dans un texte…"

Support: the hedge in entry line 78 ("is understood as") is calibrated — the literature carries the conventional gloss, a variant title, and a rival netherworld reading.

## Limit / negative evidence — the repertory question, closed at host level

- `curl -sS -o /dev/null -w "… HTTP %{http_code} …" --max-time 25 "http://melqart.huma-num.fr/"` → `curl: (6) Could not resolve host`, HTTP 000 (third round running).
- Control, same resolver, same session: `map-polytheisms.huma-num.fr` → 134.158.33.75, **HTTP 200**; `www.huma-num.fr` → **HTTP 200**; `huma-num.fr` → **HTTP 200**.
- `https://archive.org/wayback/available?url=melqart.huma-num.fr` → `{"url": "melqart.huma-num.fr", "archived_snapshots": {}}` — **zero snapshots**; archive.org itself is back online this round (HTTP 200).
- Meaning: the failure is host-level (subdomain gone, never archived), not an environment DNS limit — this upgrades round 8's "DNS non-resolution". Named as unrecoverable by these means: the inscription-level repertory.

## Access failures (documented, not source verdicts)

| Target | Attempt | Status |
|---|---|---|
| HAL hal-01996916 `/document` and `/file/…pdf` (Bonnet 2009 chapter, pp. 295–308) | `curl -c/-b jar -L -o hal_step1.html …/document` | HTTP 200 but body = 12,570-byte **bot challenge** ("Making sure you're not a bot!"); metadata API open; deposit confirmed to exist |
| Persée `docAsPDF` for both reviews | `curl -L --http1.1 … /docAsPDF/<id>.pdf` | HTTP 403 — "This resource is protected by altcha"; later review pages unreadable |
| Google Books API (Bonnet 1988 / Lipiński 2002 p. 235) | `curl https://www.googleapis.com/books/v1/volumes?q=…` | HTTP 429, quota 0/day |
| OpenEdition (`rhr/10521`, `mythos/5419`) | FetchURL both | Anubis bot-filter pages; snippets stay discovery-only |
| Gallica SRU (digitized CIS), HathiTrust (babel + catalog), PHI/epigraphy.packhum.org | curl | 403 Cloudflare / 403 (all three hosts) |
| `ia-fts.archive.org` | curl | DNS fail; superseded by Open Library search-inside |

Note for re-runners: the environment's `/tmp` was full, so early curls printed `HTTP 200 size=0` **despite success paths being fine** — artifacts were written inside the lane repo scratch dir instead (deleted after digesting; digests recorded in the JSON).

## Basis, label, limits

- **Name leg:** passage-supported — Aubet (the relay's own source) + RÉA review extract of Bonnet 1988 + Krahmalkov's component entries.
- **Anti-fixing leg:** passage-supported — Aubet's political framing; RÉA's list of ten incompatible modern definitions; Syria review's commercial-expansion framing as calibration.
- **`(Bonnet 1988)` attribution:** still book-level unverified (HAL record metadata-only; no readable copy found this round in archive.org / Google Books / HathiTrust / WebSearch sweeps). Not unapproached any more: two peer reviews and a displayed extract quoting the book's p. 9 were retrieved.
- **Worker label: `partial-support`** (raw label preserved for reconciliation).
- Residual limits still standing: Bonnet 1988 body + its Carthage chapter (pp. 165–201); Bonnet 2009 chapter text; Lipiński 2002 p. 235; the huma-num repertory; the reviews' later pages.
- Coupling implication (for the handoff): model a city god whose profile is assembled from the city's institutional life — proprietary god of the city, divine double of kingship, oath/treaty god, temple network as political-commercial infrastructure — with commercial patronage as one office inside that frame, never the definition; keep the hedge on the name's gloss; date each function to its witness (9th/8th-c. BCE Aramaic stele, 2nd-c. BCE Maltese bilingual, Roman-imperial coins, Punic personal names).
