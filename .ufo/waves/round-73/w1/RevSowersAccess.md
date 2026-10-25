# RevSowersAccess — round 73 wave 1 report

Seat: reviewer. Task: falsifiable hypothesis H — "the Sowers-Wills 2024 article (doi
10.1017/cnj.2024.21) and the Palgrave chapter doi 10.1007/978-3-032-03277-5_15 cannot be
opened by ORDINARY means (QUALITY 10), so staged rows S894/S910 must be refused this round."

Date of all probes: 2026-10-25. User-Agent for every live fetch recorded below as UA-B;
plain `curl` default UA was not used for any publisher fetch this round.

UA-B = `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

No browser automation, no challenge bypass used (QUALITY 10). All downloads under
/tmp/RevSowersAccess/ (crossref-cnj.json, crossref-palgrave.json, s2-cnj.json,
s2-palgrave.json, openalex-cnj.json, openalex-palgrave.json, unpaywall-cnj.json,
springer-chapter.html, cambridge-article.html, cambridge-oa.pdf).

## VERDICT: H FALSIFIED — both rows adoptable (with located anchors)

The publisher tier is indeed walled (Cambridge 429, Springer JS client challenge), but the
spans each staged row actually quotes are record-tier payloads, and every one of them was
opened by plain requests this round. The hypothesis conflates "publisher page unreachable"
with "quoted span unreachable"; the rows' own Tier-B clauses cite the DOI-resolved records,
which serve byte-present on three independent APIs (S894) and on Crossref (S910).

## S894 — Sowers-Wills 2024, CJL 69(3):307-332, doi 10.1017/cnj.2024.21

| Endpoint | Status | Bytes | Quoted span present? |
|---|---|---|---|
| https://doi.org/10.1017/cnj.2024.21 (UA-B, -L) | 302 → https://www.cambridge.org/core/product/identifier/S0008413124000215/type/journal_article → **429** | 1302 | publisher page not served |
| https://api.crossref.org/works/10.1017/cnj.2024.21 (UA-B) | 200 | 6670 | YES — `abstract` field, full text |
| https://api.semanticscholar.org/graph/v1/paper/DOI:10.1017/cnj.2024.21?fields=title,abstract,venue,year,externalIds (UA-B) | 200 | 3658 | YES — `abstract` field identical span |
| https://api.openalex.org/works/doi:10.1017/cnj.2024.21 (UA-B) | 200 | 12894 | YES — `abstract_inverted_index` reconstructs same text |
| https://api.unpaywall.org/v2/10.1017/cnj.2024.21 (UA-B) | 200 | 3148 | n/a — is_oa=true, bronze; sole OA PDF is the cambridge.org aop-cambridge-core URL |
| Cambridge OA PDF `…/S0008413124000215a.pdf/…` (UA-B) | **429** | 364 | full text not served |
| https://www.cambridge.org/core/journals/…/article/phonology-from-the-inside-out-…/649F8BEDBF579512088F614EB2794B59 (UA-B) | **429** | 1302 | classic slug also walled |

Wayback CDX probes (filed per QUALITY 21, UA-B):
- `web.archive.org/cdx/search/cdx?url=doi.org/10.1017/cnj.2024.21&fl=timestamp,original,statuscode&limit=8` → 2 captures, both status 302 (redirect stubs only: 20241101042851, 20241101082618); `filter=statuscode:200` → 0 rows.
- `web.archive.org/cdx/search/cdx?url=www.cambridge.org/core/product/identifier/S0008413124000215/type/journal_article&filter=statuscode:200` → 0 rows.
- `web.archive.org/cdx/search/cdx?url=cambridge.org/core/journals/canadian-journal-of-linguistics-revue-canadienne-de-linguistique/article/phonology-from-the-inside-out-constructed-language-as-a-pedagogical-tool*&matchType=prefix` → 0 rows.
- CDX sanity control: `url=cambridge.org/core` returns live captures — the empties above are genuine absence, not a dead API.

Located quote (18 words, `wc -w` counted, verbatim from the Crossref `abstract` field,
first sentence): "This paper reflects on a project-based curriculum employing constructed
languages to teach linguistics, with a focus on phonology." Location: Crossref record for
10.1017/cnj.2024.21, `message.abstract`, first sentence. The staged row's recheck token
`project-based curriculum` is byte-present in Crossref, S2, and OpenAlex copies.

## S910 — Windsor 2026, Palgrave Handbook ch. 15, doi 10.1007/978-3-032-03277-5_15

| Endpoint | Status | Bytes | Quoted span present? |
|---|---|---|---|
| https://doi.org/10.1007/978-3-032-03277-5_15 (UA-B, -L) | 302 → https://link.springer.com/10.1007/978-3-032-03277-5_15 → **200** | 3038 | body is a `<title>Client Challenge</title>` JS wall, not the chapter page |
| https://link.springer.com/chapter/10.1007/978-3-032-03277-5_15 (UA-B, -L) | **200** | 3038 | same challenge wall — chapter metadata absent from body |
| https://api.crossref.org/works/10.1007/978-3-032-03277-5_15 (UA-B) | 200 | 14874 | YES — every quoted field byte-present |
| https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/978-3-032-03277-5_15 (UA-B) | 404 | 69 | S2 does not index this chapter (irrelevant: row cites Crossref) |
| https://api.openalex.org/works/doi:10.1007/978-3-032-03277-5_15 (UA-B) | 200 | 10922 | record exists (type book-chapter), no abstract — row quotes no abstract |

The staged row's quoted span IS the Crossref record itself ("the Crossref record's title /
container-title / publisher / page / ISBN / issued fields"). Verified byte-present at
api.crossref.org, fetched 2026-10-25: title = "Conlangs in Theoretical Linguistics";
container-title = "The Palgrave Handbook of Constructed Languages"; publisher = "Springer
Nature Switzerland"; page = "343-363"; ISBN = 9783032032768 / 9783032032775; issued =
date-parts [[2026]]; type = book-chapter.

Located quote (6 words, `wc -w` counted): "The Palgrave Handbook of Constructed Languages."
Location: Crossref record for 10.1007/978-3-032-03277-5_15, `message.container-title[0]`.

Wayback CDX probes (UA-B):
- `web.archive.org/cdx/search/cdx?url=doi.org/10.1007/978-3-032-03277-5_15&filter=statuscode:200` → 0 rows.
- `web.archive.org/cdx/search/cdx?url=link.springer.com/chapter/10.1007/978-3-032-03277-5_15&filter=statuscode:200` → 0 rows.
- Genuinely uncaptured (new 2026 DOI); irrelevant to adoption since the quoted span is the
  live Crossref record, which serves 200.

## Consequences for claim C

- REJECTS leg: the "staged S894/S910 if their payload stays unreachable by ordinary means"
  condition does not trigger — both payloads are reachable by plain requests today. The
  lesson must NOT refuse S894/S910 on unreachable-payload grounds.
- ROWS/GATE legs: both rows carry record-tier Tier-B claims, which is exactly what was
  verified. Adoptable as lane rows S-pending (map by document at freeze); each gets a Gate
  record with access date 2026-10-25 and the located quotes above.
- Honest caveats the landing must keep: Cambridge publisher tier still 429s under UA-B
  (matches the staged row's own note); Springer chapter HTML is a JS client-challenge wall —
  the Crossref record is the opened artefact, full chapter text never opened. Any rewrite
  that upgrades these rows beyond record-tier claims would be unsupported by this evidence.

## Residual risk / gaps

- Springer "Client Challenge" wall means the link.springer.com URL may block future human
  rechecks too; the row's recheck command should (and does) target Crossref, not Springer.
- S2 404 for the Palgrave DOI means S2 cannot corroborate S910 metadata; Crossref + OpenAlex
  suffice (two independent records agree on title/container/publisher/pages).
- Wayback has no archival fallback for either publisher page; if both Crossref and the
  DOI-resolved record tier later die, the quotes would need re-derivation. Not a blocker.

No tooling installed (system curl + python3 sufficed); pacman untouched per host-wide pause.
