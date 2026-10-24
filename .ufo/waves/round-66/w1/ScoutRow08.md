# ScoutRow08 — ROW-OPENING S791 + S792 (claim C)

Two registry rows drafted at `.ufo/waves/round-66/rows/ScoutRow08/row-S791.txt` and `row-S792.txt`; rejects logged in `.ufo/waves/round-66/rows/ScoutRow08/rejects.txt`.

## S791 — pomander and plague-era scent prophylaxis (ACCEPTED)

- Source: Victoria and Albert Museum, "Pomander", Explore the Collections object O105969 (museum no. 918:1,2-1853; German, late 15th–early 16th c.; currently displayed Medieval & Renaissance Room 62). Tier A (national museum catalogue). Kind `docs`.
- Live `curl` GET: HTTP 200, 61,493 bytes, quote in body text Y: "strong-scented substances had the power to disinfect the air and to ward off plague and other diseases". Page also states pomanders hung "from the neck or waist, especially as a preservative against infection" and cites Lightbown's 1287 pomum de ambra record.
- Wayback: snapshot 20240914050836, `id_` replay HTTP 200; a fresh `/save` POST returned 302 to the existing snapshot. URL has no query string; query-aware normalization = equal.
- Uniqueness: grep for `O105969`/`pomander` over `corpus/SOURCES.md` + all `corpus/knowledge` fragments — no collision.

## S792 — Aztec and Maya flower/scent codes (ACCEPTED)

- Source: Sarah Newman (U. Chicago) & Stephen Houston (Brown), "Paraíso perfumado: Crear y recrear los mundos olfativos de los mayas del período Clásico", Boletín OPCA #22, Universidad de los Andes (2022). Tier A (peer-authored scholarly bulletin by leading Mesoamericanists; OPCA is a university heritage bulletin). Kind `paper`.
- Live `curl` GET: HTTP 200, 184,018 bytes, quote in body text Y: "como lo registraron observadores españoles con respecto a los palacios aztecas de Centroamérica en el siglo XVI" (Sahagún Book 9 citation — fragrant flowers as an opening "dish" of Aztec palace banquets). Article's own claims: Maya Flower Mountain paradise recreated through scent ("fragantes aromas de las flores"), music and breeze; flowers mark breath/soul rather than masking bad smells. Aztec+Maya coverage explicit.
- Wayback: snapshot 20240818230454. HTTPS `id_` replay intermittently fails (curl 000, likely replay node flakiness); HTTP replay verified HTTP 200, 168,231 bytes with matching body text. Note for re-opener: use `http://web.archive.org/...` if https flakes; canonical `web/` (non-id_) replay also fine.
- Uniqueness: grep for `uniandes`/`opca` over SOURCES.md + fragments — no collision.
- Language: article is Spanish; anchor quote kept verbatim in Spanish (row format does not prohibit non-English anchors; teaches cell states the content in English). Flag for L1 if an English-only convention is enforced — fallback is Acta Horticulturae 964.20 (ISHS, DOI 10.17660/ActaHortic.2012.964.20), live HTTP 200, but Maya-only title and members-gated PDF.

## Rejects (7, all in rejects.txt)

SMG gilt pomander and Cambridge CAJ abstract: 429 rate-limit/challenge. Wellcome works page: 405. JSTOR 20167622: 200 but Anubis challenge page. ISHS 964_20: 404 old record (moved to actahort.org; Maya-only scope). Dumbarton Oaks hummingbird-bloodletter: 202 + empty body. Mexicolore: TLS cert expired today + below tier.

## Tooling

No installs required/recorded — used preinstalled curl and pdftotext (pdftotext checked but unused; both sources are HTML). Pacman untouched per guard.

## Confidence / gaps

- S791: high — museum-tier A, verbatim quote, live+archive both 200.
- S792: high on source quality and Aztec+Maya fit; residual risks are (a) Spanish-language anchor if the entry wants English-only, (b) Wayback https-id_ flakiness (http replay verified). Remaining unknown: whether OPCA bulletin counts as tier A "university scholarly publication" vs B — conservative L1 may mark B; the row is defensible at A but B-compliant too.
