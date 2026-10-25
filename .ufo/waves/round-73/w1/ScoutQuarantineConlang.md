# ScoutQuarantineConlang — quarantine hand-check (round 73, w1)

Seat: `ScoutQuarantineConlang` (kotodama round 73, hyaku run 7, leaf).
Task: hand-check the three item-10 quarantine rows listed in the absent-defect
register (`/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`)
against their cited sources; probe the Wayback CDX for each canonical slug; rule on
the base staged entry's "a conference paper (S728)" clause.

No tools were installed (curl/python3/pdftotext already available). All downloads
were written to `/tmp/ScoutQuarantineConlang/` only. Nothing was written into the
fleet repo, the lane repo, or shokuknow.

Fetch User-Agent used for every request (recorded per QUALITY 21/22 draft):
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

---

## 1. Rows under check

| register id | register class | cited source | staged id | staged gate quote |
|---|---|---|---|---|
| S786 (kotodama r1) | payload-absent | http://conlang.org/26c3.pdf | S869 | "conlanging (n): the art and craft of making your very own language" — title-page epigraph, p. 1 |
| S812 (kotodama r3) | never-checked (fetch failed) | https://doi.org/10.1017/cnj.2024.21 | S894 | "This paper reflects on a project-based curriculum employing constructed languages to teach linguistics, with a focus on phonology" — Abstract |
| S827 (kotodama r5) | payload-absent | https://doi.org/10.1007/978-3-032-03277-5_15 | S910 | "Conlangs in Theoretical Linguistics" — container-title "The Palgrave Handbook of Constructed Languages", publisher "Springer Nature Switzerland", page 343-363, issued 2026 — Crossref record |

Quotes were derived by ROW (not by Gate heading). Confirmed gate-heading
off-by-one: in `lanes/kotodama/round3/SOURCES-PROPOSED.md` the block `## Gate —
S895` carries S894's quote (row S894 is the table row above it). In the root
`lanes/kotodama/SOURCES-PROPOSED.md`, S869's own gate is correctly headed
`## Gate — S869`; duplicated/off-by-one headings exist for S864–S868.

---

## 2. S786 → staged S869 (conlang.org/26c3.pdf)

### Fetch (live)
- `http://conlang.org/26c3.pdf` → 301 → `https://conlang.org/26c3.pdf` → 301 →
  `https://conlang.org/cl101.pdf` → **HTTP 200**, `application/pdf`, 753,374 bytes,
  last-modified 2010-01-01 (fetched 2026-10-25, browser-shaped UA).
- Saved: `/tmp/ScoutQuarantineConlang/26c3.pdf` (+ `26c3.headers.txt`, `26c3.txt`).

### Quote check
- "conlanging (n): the art and craft of making your very own language" — found
  **verbatim** at extracted lines 4–5 of the PDF text (title-page epigraph,
  p. 1). `wc -w` = 12 (≤25).
- Second quote listed on register row S786 (Chinese: 「我喜欢把写小说想象成邀请读者走进一个由我搭建的幻想屋…」) is **absent** from 26c3.pdf (0 hits). That span belongs to the chinawriter article that is staged S870's source — the register row carries a URL↔quote mispairing, not payload loss for the staged row's own gate quote (same class as round-71 S779/S814 findings).

### Wayback CDX probe (filed probed URLs)
- `https://web.archive.org/cdx/search/cdx?url=conlang.org/26c3.pdf&output=json&filter=statuscode:200&collapse=digest` → **1 capture**: `20100107110431` (status 200, application/pdf).
- `https://web.archive.org/cdx/search/cdx?url=conlang.org/cl101.pdf&output=json&filter=statuscode:200&collapse=digest` → **1 capture**: `20130430082956` (status 200; same digest as the 2010 capture → same bytes).
- Capture `20100107110431` downloaded and re-checked: quote present verbatim (lines 4–5), confirming the anchor on an archived copy (artifact `/tmp/ScoutQuarantineConlang/wb_26c3_2010.pdf`).

### Verdict: **PRESENT** — adoptable with located anchor: title-page epigraph, p. 1
(live `https://conlang.org/cl101.pdf` after redirect chain; Wayback capture `20100107110431`). The register's `payload-absent` class for this row is contradicted by the hand-check (the English gate quote is genuinely present; the register's Chinese quote is a mispairing).

---

## 3. S812 → staged S894 (doi.org/10.1017/cnj.2024.21)

### Fetch
- DOI resolves (302) to `https://www.cambridge.org/core/product/identifier/S0008413124000215/type/journal_article`.
- Cambridge live page: **HTTP 429 "Too many automated requests from this network"** (Cloudflare/Varnish bot-management rate limit) on two attempts with the browser-shaped UA, honoring `retry-after: 5` between attempts. Not a CAPTCHA wall; not bypassed (no browser automation). Artifacts: `cnj.html`, `cnj2.html` (+ headers).
- Alternative authoritative record for the same DOI fetched cleanly: `https://api.crossref.org/works/10.1017/cnj.2024.21` → **HTTP 200** (artifact `crossref_cnj.json`). Record: title "Phonology from the Inside Out: Constructed Language as a Pedagogical Tool"; container "Canadian Journal of Linguistics/Revue canadienne de linguistique" 69(3):307–332; publisher Cambridge University Press (CUP); author Sara Sowers-Wills; issued 2024-09 — all match the staged row's source cell.

### Quote check
- "This paper reflects on a project-based curriculum employing constructed languages to teach linguistics, with a focus on phonology" — found **verbatim** as the first sentence of the `abstract` field in the Crossref record for this exact DOI. `wc -w` = 18 (≤25). This is the same DOI-resolved abstract record the staged gate (head S895, row S894) says it opened.

### Wayback CDX probe (filed probed URLs)
- `https://web.archive.org/cdx/search/cdx?url=doi.org/10.1017/cnj.2024.21&output=json&filter=statuscode:200&collapse=digest` → **0 captures**.
- `https://web.archive.org/cdx/search/cdx?url=cambridge.org/core/product/identifier/S0008413124000215/type/journal_article&output=json&filter=statuscode:200&collapse=digest` → **0 captures**.
- `https://web.archive.org/cdx/search/cdx?url=cambridge.org/core/product/identifier/S0008413124000215&matchType=prefix&output=json&filter=statuscode:200` → **0 captures**.

### Verdict: **PRESENT** (span located verbatim in the DOI's Crossref abstract record;
anchor: Abstract, Crossref record for DOI 10.1017/cnj.2024.21) — **with a payload-reachability caveat**: the publisher landing page itself stays unreachable by ordinary means (HTTP 429 under browser UA; zero Wayback captures). The staged row's scope cell already declares the opened artefact is the DOI-resolved abstract record, so the row as scoped holds; but the article's full-text payload remains unverifiable — if the adoption rule requires opening the publisher page, treat the row as unverifiable (not fabrication), per the claim-C REJECTS leg's "if their payload stays unreachable by ordinary means" clause.

---

## 4. S827 → staged S910 (doi.org/10.1007/978-3-032-03277-5_15)

### Fetch
- DOI resolves (302) to `https://link.springer.com/10.1007/978-3-032-03277-5_15` → **HTTP 200** but the body is a Fastly "Client Challenge" (JavaScript) shell — the chapter page's content is behind a challenge; not bypassed (no browser automation). Artifact: `springer.html` (+ headers).
- Crossref record for the DOI fetched cleanly: `https://api.crossref.org/works/10.1007/978-3-032-03277-5_15` → **HTTP 200** (artifact `crossref_springer.json`).

### Quote check
- "Conlangs in Theoretical Linguistics" → ver `title` field, **verbatim**.
- "The Palgrave Handbook of Constructed Languages" → `container-title`, **verbatim**.
- "Springer Nature Switzerland" → `publisher`, **verbatim**.
- Supporting fields all match the staged row: page 343-363; issued 2026; author Joseph W. Windsor; ISBN print 9783032032768 / electronic 9783032032775; type book-chapter. Combined quote units = 13 tokens (`wc -w`).

### Wayback CDX probe (filed probed URLs)
- `https://web.archive.org/cdx/search/cdx?url=doi.org/10.1007/978-3-032-03277-5_15&output=json&filter=statuscode:200&collapse=digest` → **0 captures**.
- `https://web.archive.org/cdx/search/cdx?url=link.springer.com/10.1007/978-3-032-03277-5_15&output=json&filter=statuscode:200&collapse=digest` → **0 captures**.
- `https://web.archive.org/cdx/search/cdx?url=link.springer.com/chapter/10.1007/978-3-032-03277-5_15&output=json&filter=statuscode:200&collapse=digest` → **0 captures**.
- `https://web.archive.org/cdx/search/cdx?url=link.springer.com/chapter/10.1007/978-3-032-03277-5_15&matchType=prefix&output=json&filter=statuscode:200` → **0 captures**.

### Verdict: **PRESENT** (span fields located verbatim in the DOI's Crossref metadata
record; anchor: Crossref record for DOI 10.1007/978-3-032-03277-5_15 — title/container-title/publisher/page/issued) — **with the same payload-reachability caveat**: the chapter's full text is behind a Fastly JS challenge and has zero Wayback captures; the staged row's scope cell already limits the row to "the publisher's DOI metadata record", so the row as scoped holds, but the chapter text itself stays unverifiable by ordinary means.

---

## 5. Base entry "a conference paper (S728)" clause — disposition

Base staged entry `merge/kotodama/knowledge/corpus/knowledge/linguistics/conlang-scholarship.md`
line 11: *"Round 1 added a conference paper (S728) because no venue could be reached."*

- **S728 is a campaign-id defect.** Lane registry `corpus/SOURCES.md` row S728 =
  Henrike Frye (2022), "Corrective input", *Child-directed Speech in Qaqet* (ANU
  Press, ch. 8) — an unrelated document (Qaqet child-directed speech). Open id
  names an unrelated lane document → the clause as written is a defect.
- The conference paper the clause means is staged **S869** (Sai Emrys, Alex Fink &
  David Peterson, "Conlanging 101", 26C3 talk, 2009-12-28; span verified PRESENT
  above). The clause's factual claim ("a conference paper … because no venue could
  be reached") remains true and is supportable by S869.
- **Disposition: re-pointed, not cut.** Replace the campaign id `S728` with the
  lane id adopted for the 26C3 document (by document, per the wave's by-document
  map; never by arithmetic on S728). If the lane instead declines to adopt the
  26C3 row (e.g., keeping the theme to peer-reviewed venues), the clause must be
  cut or superseded, because an admitted entry may cite only adopted rows.
- Adjacent observations for the theme: the same campaign-id defect class appears in
  the conlang amendment entries — `conlang-scholarship.amend-2026-10-23c.md`
  cites S769 and `conlang-methodology.amend-2026-10-24.md` cites S806 (both
  staged-only ids; by-document check mandatory before round-73 admission, matching
  claim-C REPOINTED leg).

---

## 6. Summary

| staged row | register | span verdict | anchor | payload reachability |
|---|---|---|---|---|
| S869 | S786 | **PRESENT** | title-page epigraph p. 1 (live; Wayback 20100107110431) | live HTTP 200 + capture |
| S894 | S812 | **PRESENT** (metadata) | Abstract, Crossref record for the DOI | Cambridge live HTTP 429; 0 captures |
| S910 | S827 | **PRESENT** (metadata) | title/container-title/publisher, Crossref record | Springer challenge shell; 0 captures |

Base clause: re-point S728 → adopted 26C3 lane id (or cut if S869 not adopted).

Artifacts in `/tmp/ScoutQuarantineConlang/`: `26c3.pdf/.txt/.headers.txt`,
`wb_26c3_2010.pdf/.txt`, `cnj.html`, `cnj2.html`(+headers), `springer.html`(+headers),
`crossref_cnj.json`, `crossref_springer.json`, `s2_cnj.json` (HTTP 429 response).
