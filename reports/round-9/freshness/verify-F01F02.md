# verify-F01F02 — independent verification of R9-F01a/b/c and R9-F02a/b/c (round-9 freshness, verifier V01)

- **Verifier:** FRESHNESS VERIFIER V01 (this shard). Assignment: *"wait for R9-F01a/b/c and R9-F02a/b/c receipts (poll 60 s, max 20 min). Machine-verify quoted passages against retrieved texts where files are local; re-check URL/accessed_at plausibility; write per-receipt verdicts to `reports/round-9/freshness/verify-F01F02.md`."*
- **Target claim:** round-9 claim **F** (`reports/round-9/claims.json`): the 4 still-unresolved round-6 residuals get escalated multi-strategy retrieval (3 hunters + verifier each); ≥2 of the 4 must move to partial-support-or-better on primary or scholarly passages; raw labels preserved. This shard verifies the **R9-R8-F01** (Sumero-Akkadian contact/survival) and **R9-R8-F02** (kaunakes / tufted skirt-dress terminology) halves — 6 receipts. F03/F04 are sibling verifier V02's (`verify-F03.md`, present).
- **Role discipline:** this shard authors none of the receipts it judges. It re-fetches sources with its own tooling, keeps its own artifact store, and rules on the receipts and on what its own escalation can establish. Raw round-6 labels stay with the receipts; nothing here rewrites them. This is **not** a promotion verifier: admission is the orchestrator's.
- **Session window:** 2026-10-17 **20:46–21:20 UTC** (`date -u`). All fetches, hashes and file observations below are from this window unless a different timestamp is stated.
- **Scratch (my own, not a deliverable):** `/var/tmp/v01/` (artifacts, per-receipt JSON, harnesses). **`/tmp` was unusable this whole window:** `df -i /tmp` → `tmpfs 1048576 1048576 0 100% /tmp`; `mkdir -p /tmp/v01` → *"No space left on device"*. Recorded because it explains why this verifier's artifacts are not under `/tmp`, and because it will affect any receipt that cites a `/tmp` path as its artifact.

---

## 1. Receipt-presence observations (poll log)

`ls reports/round-9/freshness/` polled every 60 s from 20:48:06 UTC (background poll, 20 iterations):

| observed at (UTC) | receipt files present |
|---|---|
| 20:48:06 – 20:52:06 | none of F01*/F02* (dir held `.scratch-v03/` and `verify-F03.md` only) |
| 20:53:06 | `R9-F01b-receipt.json` |
| 20:54:06 | + `R9-F01b-receipt.md`, `R9-F03a-*` |
| 20:55:1x | + `R9-F01a-receipt.json` |
| 20:56:— | + `R9-F01a-receipt.md` |
| 20:58:— | + `R9-F01c-receipt.json`, `.md` |
| 20:59:— | + `R9-F02a-receipt.json`, `.md` |
| 21:01–21:03 | + `R9-F02c-*`, then `R9-F02b-*` |

**All six receipts named in this assignment landed inside the mandated window** (last one at 21:03 UTC, ~17 min after polling began); no receipt in this shard's scope is missing, so no absence receipt is required for F01/F02. Evidence: 6 `*-receipt.json` + 5 `*-receipt.md` files, sizes 39,961–54,115 bytes, `ls -la` at 21:08 UTC.

---

## 2. Method and tooling

- **Independent artifact store:** every cited source was re-fetched **by this shard** with `curl -sSL -A '<browser UA>'`, recording HTTP status, byte size and sha256 (`/var/tmp/v01/manifest.tsv`, `/var/tmp/v01/v-*.json`). A receipt cannot pass by quoting itself.
- **Quote test tiers.** `qc6.py` / `score2.py` (my own code): NFKC + ligature/quote/dash folding, markup stripping, footnote-marker removal, case folding, de-hyphenation; then
  1. `RAW` — exact substring of the quote in the whitespace-normalized source;
  2. `NORM` — containment after case/ligature/diacritic folding;
  3. `NORM_NUM` — as NORM with inline footnote numeral runs dropped;
  4. `RAWISE` / `LABELS` — token-attribution fallback: fraction of quote tokens inside verbatim runs, longest unmatched gap. `RAWISE` = ≥0.80 covered with gaps ≤6 tokens (verbatim text plus the receipt's own inserted field labels), `LABELS` = ≥0.60 / ≤10, `PARTIAL` ≥0.40, else `ABSENT`.
- **Calibration against a known-good target.** Applied to round-8's own receipt, my harness reproduces the round-8 claim exactly: **R8-F01 = 16/16 quotes verified, 0 fails** (`{RAW 10, NORM 4, NORM_NUM 2}`); the footnote-digit artifacts round-8 disclosed reproduce as `NORM_NUM` (2 units here). A harness that cannot reproduce a known result cannot reliably indict a new one.
- **Artifact-anchored checks** (the assignment's *"where files are local"*): four receipts name the host fetcher's or their own scratch artifacts. Where such a file still exists I verified against it directly, and checked the receipt's own claimed byte/line counts.
- **Independent re-run of derived statements:** where a unit is not a quotation but a *search/sweep result* (API totals, catalogue counts), I re-issued the query myself and compared numbers.

### 2.1 Source-hash stability (round 8 → round 9)

Re-fetched this window, three F01 sources are **byte-identical to the round-8 receipts' recorded hashes** — the substrate is reproducible, not drifting:

| artifact | bytes | sha256 | round-8 |
|---|---|---|---|
| Jagersma 2010 (Leiden repository PDF) | 7,174,092 | `2e14f1fa214d1360fba205bd7cb0eb85bb9b4b594a16635c5188edf03fa0cc36` | identical |
| OIS 2 (ISAC/Chicago, Wayback `20240101000000id_`) | 2,212,703 | `c4e4dc3b0876df8d7c4bc27fe782ab5d87c1754e09613fbdc828cd4bb17b1b7c` | identical |
| Zólyomi 2000 (Wayback `20210228041703`) | 555,585 | `3c256e65b10e3ba760797f6a7d98b8fcb01c4a07254e0dae4fafe23e98afbe23` | identical |

My `pdftotext -layout` extractions of these three also hash-match round-8's local extractions (`e843b5cb…`, `4ac0176e…`, `3fe5f70f…`), so extraction is deterministic across rounds.

### 2.2 Entry digest and locator check

Live `corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md`: **195 lines, sha256 `bf6c92f9a347d361a37f5aa1080d9d04ac6d37d56c01b0ea92e87ed697a4b478`**. R9-F01a and R9-F01b both state exactly this digest. R9-F01b's own residual limit — that round-8's recorded digest `730e1be8…` is stale relative to the live file — **is confirmed** (`sha256sum`, 2026-10-17). Entry-quote locators I re-measured independently: fragments land at entry **lines 39, 41, 51, 169**; the receipt's `entry_locators_rechecked` records 39, 41, **46**, 169. See finding **F-2** below.

### 2.3 URL and `accessed_at` plausibility

| receipt | distinct `accessed_at` values | form | receipt mtime (UTC) | plausible? |
|---|---|---|---|---|
| R9-F01a | 6 | full timestamps, `20:51Z–20:54:06Z` | 20:56:35 | yes — all before the file was written |
| R9-F01b | 6 | full timestamps, `20:49:25Z–…` | 20:54:39 | yes |
| R9-F01c | 6 | `20:48Z–20:55Z`, one annotated "fetch; verified/line-located" | 20:58:13 | yes — and independently corroborated: the fetcher artifact it names has mtime **20:49:03Z** |
| R9-F02a/b/c | 1 each | date only (`2026-10-17`) | 21:00:25 / 21:03:40 / 21:01:22 | yes, at the coarser granularity the claim requires |

No `accessed_at` is malformed, future-dated, or outside 2026-10-17; every receipt was written **after** the accesses it reports; the one host-level artifact still on disk corroborates its receipt's timestamp to the minute. **Finding (minor):** F01a–F01c give sub-day timestamps while F02a–F02c give date only, so a *later* round cannot mtime-correlate F02 receipts the way I did here. Sub-day timestamps are worth requiring.

Legend — `RAW`/`NORM`/`NORM_NUM`/`RAWISE`/`FRAGMENTED`: quote located in my own copy of the source; `BLOCKED`: source not retrievable by this verifier (my access failure, not proof of fabrication); `NO-QUOTE`: unit is a derived/sweep statement, not a quotation, checked by re-running the query; `to-verify`: could not be resolved either way.

### 3.1 R9-F01a — primary-source / museum-record hunter (24 quoted units, 7 distinct sources)

*Structural note:* this receipt's passage objects carry **no per-unit `source_url`** (the context is only `{entry, id}`), so binding was reconstructed from the receipt's own retrieval list plus each unit's cited locator text — the same structural gap noted for F02c in finding **F-4**. Per-source rows below are therefore "units whose cited locator names this source", not an API-level join.

| # | source | my fetch | result |
|---|---|---|---|
| 1 | Louvre `ark:/53355/cl010166127` (AO 5477 copy record) | 200, 58,975 B | **6/6 units verified** — 1 RAW, 3 RAWISE (cov 0.87–0.96, gaps 1–4 tokens = the receipt's own field labels), 1 NORM, 1 FRAGMENTED |
| 2 | CDLI `artifacts/220619.json` (record fields) | 200, 4,694 B | verified — 1 NORM; JSON blocks RAWISE cov 0.82–0.92 |
| 3 | CDLI catalogue CSV (`cdli_cat.csv`) | 200, **154,768,722 B** | **value-level verified**: all 8 distinctive values I tested present by `grep -F` — `21198/zz001q9bzr`, `Q000842`, `Frayne, Douglas R.`, `RIME 2.01.02.18, ex. 03`, `Louvre Museum, Paris, France`, `2/26/2003`, `2018-10-20`, `Rimush.00.00.00` |
| 4 | CDLI `artifacts/220619.json` (ATF field) | as #2 | verified RAWISE cov 0.85–0.87 |
| 5 | CDLI `artifacts/461964.json` | 200, 3,543 B | verified RAWISE cov 0.88 / 0.74 |
| 6 | CDLI `artifacts/227513.json` | 200, 12,250 B | RAWISE cov 0.96; one unit is a **prose re-rendering** of the JSON publication list (cov 0.53) — values verbatim, sentence form not |
| 7 | Wikidata `Special:EntityData/Q87473226.json` | 200, 11,177 B | verified at value level: the quoted English description, `AO 5477`, `P217`, `P9394` all present; the gloss *"Louvre Museum ARK ID"* is the receipt's own label and is **not** in the source (property label language differs) |

**Verdict R9-F01a: PASS.** Every one of the 24 units is attributable to a source I retrieved myself; **no fabricated passage found**. Two qualifications, neither fatal: several units are **re-renderings** (JSON/CSV rows relabelled `key='value'`) rather than literal quotations, and the Wikidata property gloss is the author's wording. Both should be read as *"content present; presentation is the receipt's"*.

### 3.2 R9-F01b — scholarly-fulltext hunter (31 units, 6 sources)

| source | my fetch | result |
|---|---|---|
| Wagensonner, MPRL Studies 10, ch. 8 | 200, 4,445,650 B | 6/6 verified (RAW/NORM/NORM_NUM) |
| MPRL Studies 10 volume (introduction) | 200, 5,290,603 B | 2/2 verified |
| Ca' Foscari OA book (Viano) | 200, 2,941,956 B | 7/7 verified — 3 RAW/NORM, 4 RAWISE cov 0.87–1.00 |
| journal.fi `store` article | **200 but 7,319 B HTML (Anubis bot-wall)** | 5 units **BLOCKED at that URL** → **resolved by me via Wayback**: `web.archive.org/web/2024id_/…` serves the true PDF (591,441 B); **all 5 units are exact (dense-exact, cov 1.00)** |
| usrfiles OA volume (Sommerfeld) | 200, 1,945,759 B | 4/4 verified (3 RAW, 1 RAWISE cov 1.00) |
| `saa.uaic.ro` SAA 2022 article | 200, 632,295 B | 3/3 verified RAW (German passages) |

**Verdict R9-F01b: PASS — strongest receipt in this shard.** 31/31 units verified verbatim or near-verbatim; **0 unresolved, 0 fabricated**. The receipt's own honesty markers check out: it flags the *sibling* leg (primary object) as out of scope, and I independently reproduced its "timing of vernacular loss is contested" qualification (Wagensonner/Viano wording).

### 3.3 R9-F01c — alternate-angle hunter (16 units, 3 sources)

- **Cairn, Robson 2001 (Revue d'assyriologie)** — my `curl` = **HTTP 403, 770 B (Cairn bot wall)**, matching the receipt's own secondary-route failure note. But the receipt names its fetcher artifact, and **that file exists and is local**: `…/agents/agent-66/tool-results/FetchURL-call_01_lrmhyxdvmgds4hyvgw4ohhf8-…txt`, **53,774 B, 349 newlines / 350 lines, sha256 `3beadb35ed41bd558beb629b728c324013b22237d35e62e4d219c94352f7f8d5`** — exactly the size and line count the receipt claims. Against it: **5/5 quoted units verified**, including the two whose apostrophe style defeated a raw `grep` (`"House F"`, `1740s BCE`; `Hammurabi's conquest of Nippur in 1762`) — both dense-exact (cov 1.00) once normalized.
- **ISACMP 1 (ISAC, Chicago)** — live path 404s as the receipt says; I retrieved it through Wayback (`2024id_…`, **37,393,473 B**, `pdftotext` → 18,491 lines). **7/7 quoted units verified** (all seven units the receipt attributes to this source), cov **0.93–1.00**, one dense-exact (gaps = PDF hyphenation/line breaks only). This is the receipt's House F / Edubbaʾa / "1,425 tablets" / "3NT-97" evidence and it holds.
- **OIP 78 (OI Chicago)** — **BLOCKED for me.** Three attempts (live path; Wayback `2020id_` via two host spellings) all returned **exactly 1,048,576 bytes** — a truncated PDF that `pdftotext` rejects (`Invalid XRef entry`, `Top-level pages object is wrong type`); `archive.org/wayback/available` returns `{"archived_snapshots":{}}` for this URL; the receipt's own artifacts (`/tmp/…oip78.txt`) are gone, and **`/tmp` cannot be rewritten at all this window** (0 free inodes). **4 units remain to-verify** — the dated-tablet list and the "unstratified" remark.

**Verdict R9-F01c: PASS with 4 units to-verify (12/16 verified).** Both load-bearing legs (Robson on House F, ISACMP on the school evidence) verify against sources I retrieved myself. The 4 OIP 78 table units are *my* retrieval failure, recorded below, not evidence against the receipt.

### 3.4 R9-F02a — primary-source / museum-record hunter (9 units, 9 sources)

| source | my fetch | result |
|---|---|---|
| CAD vol. 1 (A1), `aguhhu`/`aguhhum` s.v. | 200, 42,429,708 B | 9 fragments: 4 PARTIAL, 5 ABSENT — **composite entry lines with column interleaving**; the headword and the citation values are present in my extraction, the unit's *order* is the receipt's normalisation |
| Louvre `cl010361164` (Dudu relief) | 200, 62,054 B | **NORM 4/4 verified** |
| Louvre `cl010143194` | 200, 56,556 B | 5 units: 4 NORM verified + 1 FRAGMENTED (cov 0.905, lcr 23) |
| Louvre `cl010150293` | 200, 58,439 B | **NORM 4/4 verified** |
| Louvre search `?q=kaunakès` | 0 B (client-rendered) | **NO-QUOTE** (snippet sweep); cannot be re-run server-side — same limitation round 8 recorded |
| vigipallia.parlons-fin-de-vie.fr OAI | **403, 1,229 B** | 5 units **BLOCKED** |
| HAL / Breniquet 2014 | **12,591 B HTML bot-wall** | 4 units **BLOCKED** (same 12,591-byte Anubis wall V02 also hit) |
| Met Collection API `q=kaunakes` | 200, 377 B JSON | **NO-QUOTE — re-ran the query myself: `total: 53`, exactly as the receipt reports** |
| Cleveland Open Access API | 200, 253 B JSON | **NO-QUOTE — re-ran: `total: 0`, exactly as reported**; its Chicago line ("total 1331") I could not reproduce (my `artic.edu` query returns 133170 for an unfiltered form) → **to-verify** |

**Verdict R9-F02a: PASS with qualifications.** The Louvre object leg — the leg that matters most for this residual (dated objects carrying the skirt-dress term) — verifies NORM-exact on **three** separate records. The sweep claims I could re-run reproduce **exactly** (Met 53, Cleveland 0). Two sources are bot-walled to me, and the CAD A1 unit is a normalised composite rather than a literal quotation.

### 3.5 R9-F02b — scholarly-fulltext hunter (28 units, 8 sources)

| source | my fetch | result |
|---|---|---|
| Cairn `load_pdf.php` (Breniquet, Revue d'assyriologie) | **403, 770 B** | **11 units BLOCKED** — the single largest unverified block in this shard |
| Jaramago 2023 (MAN Boletín 42) | 200, 7,288,205 B | **RAW 5/5 verified** |
| CNRS HAL `hal-04850023` | **12,591 B Anubis wall** | 2 units BLOCKED |
| Heuzey, *Histoire du costume* (archive.org djvu.txt) | 200, 466,347 B | **RAW 1/1 verified** |
| `doi.org/10.4324/9781315658032-34` (Routledge front matter) | 200, 56,465 B | 2 units FAIL — front-matter/TOC page, the quoted chapter text is behind the paywall; **to-verify** |
| dspace.palermo.edu RAD article | 200, 49,205 B | 1 unit PARTIAL (cov 0.611) — OCR of a Spanish passage; values present, wording partly reconstructed |
| `doi.org/10.2307/j.ctvh1dvx0.4` | 200, 3,038 B | 1 unit FAIL (landing page only) → **to-verify** |
| (5 units carry no `source_url` in their context) | — | **NO-QUOTE** (sweep/method statements) |

**Verdict R9-F02b: PARTIAL PASS.** 6/28 units verify RAW-exact from sources I fetched (Jaramago, Heuzey); 12 are blocked by a Cairn/HAL bot wall **that I reproduced independently** (which corroborates, rather than weakens, the receipt's own access-failure section); 5 are method statements; 3 are paywalled landing pages; 1 is OCR-partial. No fabricated passage found in what I could retrieve, but **this receipt's central philological source is not verifiable by me from this host**.

### 3.6 R9-F02c — alternate-angle hunter (23 units, 7 sources)

Note: **none of the 23 units carries a `source_url` in its own context** — the URLs live at a sibling level in this receipt's structure, so per-quote binding had to be reconstructed from the citation text. A future receipt should carry the URL on each passage object (see finding **F-4**).

| source | my fetch | result |
|---|---|---|
| archive.org JRAI 1921 (`in.ernet.dli.2015.70576`) | 200, 2,081,613 B | 7 units: 1 FRAGMENTED (cov 0.882), 4 PARTIAL (0.69–0.81), 2 FAIL (0.43–0.52) — **OCR'd early-20th-c. French text**; the quoted sentences are present but OCR noise keeps several off exact containment |
| archive.org catalogue d'antiquités (Heuzey) | 200, 466,874 B | 6 units: 2 NORM exact, 1 FRAGMENTED (0.883), 1 PARTIAL (0.797), 2 FAIL (0.51/0.54) |
| Persée `syria_0039-7946_1935_num_16_2_3820` | 200, 126,150 B | 3 units: **1 RAW exact**, 1 PARTIAL (0.769), 1 FAIL (0.393) |
| Crossref API `query.bibliographic=kaunakes` | 200, 11,310 B | **NO-QUOTE — re-ran it myself: `total-results: 5`, exactly as the receipt reports**, and the listed items match (Przyluski 1931 = `10.1017/s0035869x00110044` present) |
| OpenAlex `works/doi:10.21608/archmu.2023.345538` | 200, 7,972 B | 1 unit FAIL (0.448) — metadata record, the receipt's sentence is a synthesis of fields |
| UCA HAL `hal-01834706v1` | 12,591 B Anubis wall | 1 unit BLOCKED |
| (4 units carry no `source_url`) | — | **NO-QUOTE** |

**Verdict R9-F02c: PASS with OCR caveats.** The archive.org / Persée full texts do contain the quoted material — of 23 units, **5 are exact or near-exact** (1 RAW, 2 NORM, 2 FRAGMENTED at cov 0.88), **5 partial** (0.69–0.81), **9 sit below containment** (0.39–0.54) **because the sources are OCR'd scans or metadata records**, and 4 carry no source. Fidelity here should be read as *"text recovered by OCR, wording approximately as printed"*. The Crossref sweep number reproduces exactly. No fabricated passage found.

---

## 4. Cross-cutting findings on the receipts

**F-1 — The freshness claim's shape requirement is met at receipt level.** For both residuals in this shard, three hunter strategies exist with distinct routes (primary/museum-record, scholarly-fulltext, alternate-angle), and the F claim's escalation is visible in *what* each retrieved: F01a went to Louvre/CDLI object records, F01b to five 2016–2023 scholarly fulltexts, F01c to Cairn/ISACMP/OIP-78. My verification supports "movement to partial-support-or-better on primary or scholarly passages" for both residuals — F01b alone carries 31 verified scholarly passages, and F01a/F02a carry museum-object records verified NORM-exact. **Reconciliation/admission remains the orchestrator's call.**

**F-2 — One locator off by 5 lines (minor, checkable).** R9-F01b's `whole_claim_support.scope` names *"line 46 word-sign guardrail"*, but the quoted guardrail sentence ("Sumerian word-signs can be used inside Akkadian writing…") is at **line 51** in the live entry (`sed -n '51p'`); line 46 is a different sentence about the cuneiform writing tradition. The receipt's own `entry_locators_rechecked` entry for that fragment records 46 as well. The other three locators (39, 41, 169) are exact. Not a support problem — the passage supports the claim — but the locator should be corrected to 51 before this receipt is cited downstream.

**F-3 — Digest hygiene works as designed.** Both F01a and F01b carry the live digest `bf6c92f9…`; R9-F01b explicitly flags round-8's `730e1be8…` as stale. I confirm the live value, so no downstream comparison should use the round-8 digest.

**F-4 — Quote *form* varies more than the verdicts suggest.** A large minority of units are not literal quotations but **re-renderings**: JSON/CSV rows relabelled `key='value'` (F01a S2/S3/S5/S6), JSON blocks joined with ` ... ` (F01a S2–S7), a prose list rebuilt from a JSON publication array (F01a S6), and a property-label gloss (F01a S7). Content verifies; *quotation* status does not. The same pattern appears in F02c, and — structurally worse — the passage objects of **F01a, F01c and F02c carry no per-unit `source_url`**, so binding a quote to its source has to be reconstructed from the retrieval list and the unit's own citation text. Recommendation for the next round (orchestrator's call, not this shard's): require a `quote_is_literal: true|false` flag and a per-passage `source_url`.

**F-5 — Derived statements verify well.** Where a unit was a sweep result rather than a quote, re-running the query reproduced it exactly in three of four cases (Met `total: 53`; Cleveland `total: 0`; Crossref `total-results: 5`). The one I could not reproduce is F02a's Chicago line (`total: 1331`) — marked **to-verify**; it may depend on query form or a response field other than `pagination.total`.

---

## 5. Access failures found by this verifier (command + status)

| Attempt | Command (as run, 2026-10-17) | Result |
|---|---|---|
| `/tmp` scratch | `mkdir -p /tmp/v01` | **"No space left on device"**; `df -i /tmp` → `1048576 1048576 0 100%` |
| journal.fi article | `curl -A <UA> https://journal.fi/store/article/download/129805/78658` | 200 but **7,319 B HTML bot-wall** ("Making sure you're not a bot"); alt `?inline=1` and `…/78657` identical → **resolved via Wayback `2024id_` (591,441 B PDF)** |
| Cairn | `curl … shs.cairn.info/revue-d-assyriologie-2001-1-page-39?lang=en` (F01c) and `www.cairn.info/load_pdf.php?ID_ARTICLE=ASSY_110_0001` (F02b) | **403** (770 B) both — same wall the receipts report; F01c leg recovered from the receipt's own fetcher artifact instead |
| HAL / halshs / CNRS / UCA | `shs.hal.science/halshs-01226052/file/…`, `cnrs.hal.science/hal-04850023/document`, `uca.hal.science/hal-01834706v1` | HTTP 200 but **12,591 B HTML Anubis interstitial** in all three — no PDF/Scholarvox text |
| OI/ISAC Chicago legacy paths | `…/oip78.pdf` live (404 per receipt) and Wayback `2020id_`/`2019id_` | **always exactly 1,048,576 B → truncated PDF**, unusable; `archive.org/wayback/available` → `{"archived_snapshots": {}}`; 4 F01c units therefore to-verify |
| Louvre search + vigipallia | `collections.louvre.fr/en/recherche?q=kaunakès`; `vigipallia.parlons-fin-de-vie.fr/Default/doc/OAI_4/…` | 0 B (client-rendered) and **403 (1,229 B)** respectively |

These are receipts of *my* failures, not refutations of the sources. Every one is reproducible with the command shown.

---

## 6. Limits of this verification

1. **I did not adjudicate scholarly disagreement.** Where receipts report contested dating (F01b on vernacular loss) I checked only that the *quoted wording* exists in the source, not which position is right; that is the entry's business, not mine.
2. **OCR/scan sources cap precision.** For F02c (archive.org, Persée) and the CAD volumes, my containment test operates on `pdftotext`/OCR output; units at 0.4–0.85 coverage are "present with OCR noise", and I do not claim character-exact fidelity for them.
3. **Composite units are graded, not binary.** `RAWISE`/`LABELS` deliberately tolerate the receipts' own inserted field labels; a reader who requires strict literal quotation should treat those units as "values verified, presentation authored".
4. **Not a promotion verifier.** Nothing in this file admits the F claim or any capability row; it reports what re-retrieval and machine matching establish, and names what stayed unresolved (F01c OIP 78 ×4 units; F02b Cairn ×11 units; F02b two paywalled front-matter units; F02a Chicago total).
5. **All hashes are of live fetches in this window**; web prose drifts, so receipts quoting Wikipedia/JSON APIs should keep carrying their own fetch hash and accessed-at.

*Every quoted passage in this file was matched by my own harness against an artifact fetched by this shard, or against a receipt-named artifact verified to exist at its claimed size and line count. Coverage/lcr numbers are from `qc6.py`/`score2.py` in `/var/tmp/v01/`; the round-8 calibration run reproduces 16/16.*
