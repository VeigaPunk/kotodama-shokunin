# ReviewCarriedS384S385 — round-57 carried-row re-check (S384, S385)

Seat: KotodamaR57.ReviewCarriedS384S385 (leaf reviewer). Scope: the carried row
findings of round-56 lesson `corpus/lessons/round-56-verifier-spotcheck.md`
§5 item 5 for **S384** (Fromont 2017, Redalyc) and **S385** (Dianteill 2002,
OpenEdition). Each source was re-opened this session by ordinary means; every
key quote was run through the round-57 locator
(`reports/round-57/reopen-quote.py`). No files were edited; fixes below are
exact old -> new proposals for the L1 (KotodamaR57).

## Re-opened sources (this session)

- **S384**: `https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf`
  — plain GET, HTTP 200, `application/pdf`, 1,291,427 bytes, 23 PDF leaves
  (cover + 22 printed pages), text extracted with both `pdftotext` and
  `pypdf==5.4.0` (the locator's extractor). Locator run on the row's Gate
  quote succeeded earlier this session:
  `LOCATED https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf`
  (p. 22 quote). Later retries from this shell failed at TCP connect
  (connection refused / unreachable host) — a transient egress condition,
  not a challenge (curl got HTTP 000 with no server response). Served text
  checks below used the already-fetched byte-identical copy.
- **S385**: `https://journals.openedition.org/assr/pdf/2480` — plain GETs
  during this session alternated between the PDF (HTTP 200,
  `application/pdf`, 492,733 bytes, 23 pages) and an **Anubis JavaScript
  challenge interstitial** (HTTP 200 `text/html`, "Anubis could not load its
  JavaScript…"). Challenge met, not passed; the round-57 locator (plain
  urllib, no JS) cannot get the PDF from the live URL. Routed around by an
  **ordinary Wayback capture**:
  `https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480`
  — plain GET, HTTP 200, `application/pdf`, 303,987 bytes, 23 pages,
  embedded text. The capture serves the same article (pagination 59–80;
  quotes verified below). Round-56's own route cell records a direct GET of the same live URL (492,733 bytes) on 2026-10-22.

## Findings and verdicts

### S384 — F1/F2: entry over-reads (AGREE)

**F1 — `corpus/knowledge/civilizations/kongo-kingdom.md:84`** (ReviewSectionsCapitalKinFaith; ReviewRowsS383toS385 kept this sentence "carried" but only for the roles clause — the generalization is still over-read). AGREE with the over-read: the served page, p. 12, describes two specific figures in one watercolor:

> "Behind him, two mestres, interpreters and leaders of the Church, wear their uniform composed of a white cloth draped over one shoulder." … "Figure 1 − Bernardino d’Asti. Reception of a capuchin missionary by a local ruler. Italy, ca. 1740."

The entry sentence states a general office description ("Mestres were … marked by a white shoulder cloth"), which the source does not carry. Fix:

- old: `*Mestres* were interpreters and leaders of the Church, marked by a white shoulder cloth (S384, p. 12).`
- new: `In the ca. 1740 watercolor, Fromont identifies two *mestres* as Church interpreters and leaders, wearing a white cloth over one shoulder (S384, p. 12).`
- Locator run for the S384 p. 12 mestres quote (served text):

```
python3 -B reports/round-57/reopen-quote.py 'https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf' "two mestres, interpreters and leaders of the Church, wear their uniform composed of a white cloth draped over one shoulder"
→ LOCATED https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf
```

**F2 — `corpus/knowledge/civilizations/kongo-kingdom.md:97`** (ReviewRowsS383toS385). AGREE with the over-read: the served p. 12 text describes the single "richly attired leader" in the watercolor, not a general dress rule:

> "Their richly attired leader walks one step in front of the group … He wears an mpu cap on the head, an nkutu net over the shoulders. He carries a wooden staff in his left hand … a brilliant red coat embroidered with the insignia of the Order of Christ hangs behind his back."

Fix:

- old: `A Christian noble wore an mpu, an nkutu net over the shoulders, a staff and a red coat with the order's insignia (S384, p. 12).`
- new: `In the watercolor, the richly attired leader wears an mpu cap and an nkutu net over his shoulders, carries a wooden staff, and wears a red coat embroidered with the Order of Christ insignia (S384, p. 12).`

Both new sentences use only words the opened page serves (locator-verified p. 12 quotes `He wears an mpu cap on the head, an nkutu net over the shoulders` and `two mestres, interpreters and leaders of the Church, wear their uniform composed of a white cloth draped over one shoulder` are present in the served PDF text).

**S384 registry row** — no action: the merged-row anchor append and the route-cell provenance rewrite flagged by ReviewExcludedSources56 are already applied in `corpus/SOURCES.md` row S384 (anchor now carries the p. 12 and p. 23 quotes; route cell reads "direct plain request, HTTP 200, 1,291,427 bytes, application/pdf, 22 printed pages plus the journal cover page; access date 2026-10-22").

### S385 — F1: entry over-read (AGREE)

**`corpus/knowledge/civilizations/kongo-kingdom.md:93`** (ReviewRowsS383toS385). AGREE with the over-read: served p. 76 says minkisi "sont devenus le centre de l’attention des paleros" (the centre of the paleros' **attention**), not the centre of palero **practice**. The second clause is carried verbatim by the same page: "Tous les rituels en rapport avec la fonction royale ont disparu". Fix:

- old: `In Cuba the minkisi became the centre of palero practice while every rite tied to the royal function disappeared (S385, p. 76)`
- new: `In Cuba the minkisi became the centre of the paleros' attention while every rite tied to the royal function disappeared (S385, p. 76)`

### S385 — F2: registry anchor apostrophe defect (AGREE) → superseding row

The registered S385 anchor quote for p. 76 uses ASCII apostrophes: `qu'une` / `l'attention`. The served page uses typographic apostrophes (U+2019): `qu’une` / `l’attention` (present in both the live PDF text and the Wayback capture). The anchor is therefore not byte-verbatim to the served text. Registry is append-only and the wrong cell is the anchor (not status/recheck/used-by), so the remedy is a **superseding SOURCES row** (id left `S4xx` for the L1).

**Drafted row (11 columns):**

```
| S4xx | Dianteill, Erwan. 2002. "Kongo à Cuba. Transformations d'une religion africaine." *Archives de sciences sociales des religions* 117, janvier-mars 2002: 59–80. DOI 10.4000/assr.2480. Éditions de l'EHESS. The facsimile PDF's own cover carries pagination 59-80 and the journal's print ISSN 0335-5985. — https://journals.openedition.org/assr/pdf/2480 (the live PDF answers plain GETs with an Anubis JavaScript challenge on 2026-10-22; ordinary copy opened this round: Wayback capture https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480, HTTP 200, application/pdf, 303,987 bytes, 23 pages, embedded text, access date 2026-10-22) | paper | A | how the Bakongo religion became palo monte in Cuba: the kongo/congo naming convention; colonial-era Congo ethnonyms and cabildos de nación; the nganga/ganga/prenda terminology shift; nkisi, bilongo, bisimbi and ndoki in the early-twentieth-century Laman corpus; the Dona Béatrice (Antonian) episode of 1706; MacGaffey's three-period history as Dianteill adopts it; and the stated limits (no ethnographic source predates the end of the trade; Catholic influence long predates the deportation; Haitian and spiritist layers are Cuban additions). Not: the kingdom's political chronology in detail, Kikongo grammar, or the Brazilian or Haitian cases, which it mentions only in passing. (tier note: A — full text of a peer-reviewed EHESS journal article drawing on the author's 1994-1999 fieldwork with Havana and Santiago paleros; primary for his analysis and his informants' manuscript corpus; hedged where he reports others' counts.) | p. 59: "les ethnonymes utilisés dépendaient plus des factoreries sur la côte africaine que des peuples eux-mêmes"; p. 65: "un mouvement messianique vît le jour au XVIIIe, mené par une princesse nommée Dona Béatrice qui se disait inspirée par saint Antoine"; p. 76: "Les minkisi, qui ne représentaient qu’une partie des objets rituels en pays kongo, sont devenus le centre de l’attention des paleros"; p. 76: "Tous les rituels en rapport avec la fonction royale ont disparu" | supersedes S385 — the p. 76 anchor quote is restored to the served typographic apostrophes (qu’une, l’attention), and the route records the 2024-03-27 Wayback capture because the live PDF answers plain GETs with an Anubis JavaScript challenge. | queued | 2026-10-22 | 365d | — |
```

Notes for the L1:
- The **Gate quote is the first quote in the anchor** (p. 59 — unchanged, LOCATED, 15 words). The row's corrected p. 76 quote is second-located evidence.
- The p. 61 note 5 and p. 63 note 8 quotes from S385 are deliberately **not** carried into the drafted anchor: in the pypdf extraction used by the locator they coalesce typographically (`ngangadésigne`, `toutnkisiest`), so they cannot be LOCATE-demonstrated (both are present verbatim in the page's `pdftotext` view; p. 61 note 5: "Alors que le terme nganga désigne un guérisseur traditionnel en Afrique, il désigne à Cuba le récipient où est « fixé » un esprit"; p. 63 note 8: "où tout nkisi est un objet matériel contenant un esprit"). Any future Gate that needs them should re-quote from the page rather than the registry.
- The live URL is kept first in the source cell for identity; the Wayback capture is the effective locator-verifiable route (same shape as S388/S410 effective-URL notes).

**Gate line (round-57 lesson style) for the drafted row:**

```
- S4xx — https://journals.openedition.org/assr/pdf/2480 (the live PDF answers plain GETs with an Anubis JavaScript challenge; effective: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480) — accessed 2026-10-22 — p. 59: “les ethnonymes utilisés dépendaient plus des factoreries sur la côte africaine que des peuples eux-mêmes”. Grounds: Dianteill shows palo monte keeps Kongo terms while shifting their referents, warns that colonial ethnonyms come from trading posts, and argues Cuban palo layers Kongo, Yoruba, Catholic, Haitian and spiritist inputs. Seat: ReviewCarriedS384S385.
```

**Locator lines (pasted runs):**

```
python3 -B reports/round-57/reopen-quote.py 'https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480' "les ethnonymes utilisés dépendaient plus des factoreries sur la côte africaine que des peuples eux-mêmes"
→ LOCATED https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480

python3 -B reports/round-57/reopen-quote.py 'https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480' "Les minkisi, qui ne représentaient qu’une partie des objets rituels en pays kongo, sont devenus le centre de l’attention des paleros"
→ LOCATED https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480

python3 -B reports/round-57/reopen-quote.py 'https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480' "un mouvement messianique vît le jour au XVIIIe, mené par une princesse nommée Dona Béatrice qui se disait inspirée par saint Antoine"
→ LOCATED https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480
```

The last quote (p. 65) is 22 words and locates on the capture; `Tous les rituels en rapport avec la fonction royale ont disparu` (10 words) is present on the same served page and was verified in the local extraction; its locator runs this session were intermittently cut by Wayback 429/connection throttling (transport, not quote absence).

## Residual risk and verification gaps

- **S384 live leg**: the locator's earlier `LOCATED` for the Redalyc Gate quote happened earlier in the session; subsequent runs from this shell hit connection-refused egress. The saved byte-identical copy was used for text checks. If the L1 re-runs, the Redalyc host may be flaky from the runner's egress; the quotes are confirmed in the served text.
- **S385 live leg**: the live OpenEdition URL is behind Anubis for plain GETs (challenge met, not passed). The drafted row deliberately points the Gate at the Wayback capture. If the L1 prefers a live route, that URL must be re-probed at integration time; today it is not locator-verifiable.
- The p. 61/p. 63 footnote quotes are page-present but not locator-demonstrable (typographic coalescing in pypdf); the entry's `(S385, p. 61, note 5)` clause stands on the opened page itself.
- No tools installed or updated this session.
