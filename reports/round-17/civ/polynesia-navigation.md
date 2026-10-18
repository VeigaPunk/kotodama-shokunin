# R17-C07 — polynesia-navigation fixer: never-swept URL set live-swept (26/26), 9 moved locators fixed

- worker: C R17-C07 (round-17 C-fixers seat, “never-swept #2 polynesia-navigation”); assignment: live-sweep the entry’s cited URLs, fix dead locators or document; deliver `reports/round-17/civ/polynesia-navigation.md`.
- writes (only): `corpus/knowledge/civilizations/polynesia-navigation.md` (one assigned entry; 3 lines edited) + this file. No commit, no push, no LOG.md touch, no other corpus byte.
- date: 2026-10-18; command times below are UTC. Baseline: `reports/round-17/claims.json` declares `f30b6f8188937632bbedd0e7b29aeefff6f8b07b`; HEAD `9b49a4a` (“round-17: declare loop-2 build-1 claims D/C/O”).
- pre-edit `git status --porcelain -- corpus/knowledge/civilizations/polynesia-navigation.md` → empty; `git diff --stat f30b6f8188937632bbedd0e7b29aeefff6f8b07b -- corpus/knowledge/civilizations/polynesia-navigation.md` → empty. Before-bytes sha256 `ff72bf1143be58fbc10ffce9b1f7b3a22317c6cbf79a0fab2fd7e0c7a4d0c33f` (prefix `ff72bf1143be58fb` = the digest recorded in `reports/round-16/civ-map.json`; byte chain closes on the round-16 map’s bytes).
- **disposition: `stale-fixed`** — the never-swept reason is retired by a dated 26/26 URL-status receipt (this fragment), and 9 moved locators were replaced old → new with 301 + content evidence (§5). 2 locators stay curl-blocked by bot walls (not breakage); replacement attempts named (§6).
- note: the civ worktree is shared with concurrent round-17 C-workers (`inuit.md`, `maya-classic.md`, `mesoamerica-primary-sources.md`, `mongol.md`, `muisca.md`, `persia-sasanian.md`, `rapa-nui.md`, `rome.md`, `ryukyu.md`, `scythian-saka.md`, `siam-thai.md` — among others — modified by other seats during this run); none of that is mine.

## 1. Debt under fix (round-16 reason trail, kept in the entry edit)

`reports/round-16/civ-map.json`, entry 78 (`polynesia-navigation.md`): `"status": "stale-documented"`, reason (verbatim): “no dated URL-status receipt exists for its 94 distinct cited URLs (r16 C07 negative sweep); freshness pause defers the sweep — not evidence of breakage [evidence: reports/round-16/civ/072-083.md]”.

The shard row (`reports/round-16/civ/072-083.md`, row 78) gives this entry **26** distinct cited URLs, `couples_resolved 15`, `url_receipt: null`, open item “same” (no URL-status receipt exists); §3 of that shard records the 7-entry never-status-checked group (94 distinct URLs across persia-sasanian…siam-thai) and names the method a future sweep should use — the M04 method (`reports/round-8/metadata/m04-civ-58-76.md` §2 step 2). The round-8 predecessor receipt is apparatus-only: “No source re-retrieval was performed — live source rechecks are the F claim’s work, not this sweep’s” (`reports/round-8/metadata/m05-civ-77-94.md:7`).

Wording note (reported, not corrected in place): the map reason’s “94” is the 7-entry group total (`reports/round-16/civ/072-083.md` §3 tally); this entry’s own count is **26**, re-measured below. Filed round-16 artifacts are not edited by this worker.

Round-17 claim C (`reports/round-17/claims.json`) requires live locator evidence with access dates; this sweep is executed under that claim. It is not filed as a freshness axis-move (the round-16 freshness-pause note stays historical context; no axis verdict is claimed here).

## 2. Negative claim, with sweep

Claim: before this round, no in-repo receipt carries a per-URL HTTP status for this entry. Sweep (2026-10-18):

```
grep -rln "polynesia-navigation" reports/ LOG.md SCORECARD.md corpus/lessons/ | grep -v "round-16/civ-map.json\|round-16/civ/072-083.md\|round-17/civ/polynesia-navigation.md"
→ reports/supplement-opencode-1/scratch/28-corpus-contract/header-census.txt
  reports/supplement-opencode-1/inventory-after.json
  reports/round-8/metadata/m05-civ-77-94.md
  reports/round-9/metadata/audit.md
  reports/round-9/metadata/v05-civ-77-94.md
  reports/round-9/metadata/v07-synth-13-24.md
  reports/round-9/metadata/v03-civ-39-57.md
  reports/round-10/coverage/review-C08.md
  reports/round-10/coverage/C08.md
  reports/round-10/validation.json
  reports/round-16/civ/map-audit.md
  reports/round-16/validation.json
  reports/round-17/civ/sed77.md
  reports/round-17/civ/sed80.md
  reports/round-17/civ/persia-sasanian.md
  reports/round-17/validation.json
  reports/round-17/report-draft.md
  LOG.md
  corpus/lessons/round-2-triage/Z76.md
  corpus/lessons/round-4-audit/civ-71-77.md
  corpus/lessons/round-16.md
  corpus/lessons/round-17.md
```

All hits characterized (2026-10-18): header censuses / apparatus inventories (`header-census.txt`, `inventory-after.json`, `v05-civ-77-94.md`, `audit.md` — couples counts and marks, no URL statuses); shard-boundary and concurrency notes (`v03-civ-39-57.md`, `v07-synth-13-24.md`, `map-audit.md`); coverage-authoring line-anchor citations (`round-10/coverage/*`, `round-10/validation.json`); bookkeeping and in-flight round-17 files (LOG.md, `corpus/lessons/*`, this round’s drafts/index rows — shared listings, not per-URL receipts for this entry). Zero of them carries a per-URL HTTP status for this entry; the round-16 map’s `url_receipt: null` is reproduced.

Hand-off re-run (same command, 2026-10-18, after sibling seats landed; this receipt’s own fragment excluded) adds: `reports/round-17/civ/sed78.md`, `reports/round-17/civ/sed79.md` (sibling fixer fragments — this entry appears only in their identity-reconciliation lists, e.g. `sed78.md:24`), `reports/round-17/civ/verify-1.md` (verifier listing, `:7`), `reports/round-17/civ/map-patch.json` (map-scribe row for this entry; its `evidence_path` points back to this receipt), `reports/round-17/run-validation.py`, `reports/round-17/validation.json` (this round’s runner and receipt; the C measurement row for this entry is `fixed`, 9 landed locators). Same classes as above — none is an independent per-URL receipt for this entry.

Second negative (characterization of the two non-200s, details in §6): the OUP and Royal Society blocks are bot walls, not link rot — evidence: Cloudflare challenge body `<title>Just a moment...` on the Royal Society 403; `https://www.royalsociety.org.nz/` root also 403 (site-wide wall); OUP 403 body is a 5,469-byte challenge page; the `global.oup.com` catalog page answers 202 with 0 bytes.

## 3. Live sweep — all 26 distinct URLs (2026-10-18)

URL inventory command (round-16 A1 method, C06’s grep form):

```
grep -o 'https\?://[^)>, ;]*' corpus/knowledge/civilizations/polynesia-navigation.md | sed 's/[.,]$//' | sort -u | wc -l
→ 26   (pre-edit and post-edit; the 9 replacements are 1:1, count unchanged)
```

Sweep command (M04 method; retry once on 000; same UA as sibling R17-C06’s sweep):

```
curl -sS -o /dev/null -w '%{http_code} %{url_effective} %{content_type} %{size_download} %{time_total}' -L --max-time 15 -A 'Mozilla/5.0 (compatible; kotodama-metadata-audit/1.0)' <URL>
```

Raw results, pre-edit set (driver `.scratch/r17c07/sweep.py` → `.scratch/r17c07/sweep-run1.json`, 2026-10-18T09:17:23Z):

| # | URL (as cited pre-edit) | status | effective URL | content check |
|---|---|---|---|---|
| 1 | `https://archive.hokulea.com/ike/hookele/hawaiian_star_lines.html` | 200 | — | title “Hawaiian Star Lines” |
| 2 | `https://archive.hokulea.com/ike/hookele/on_wayfinding.html` | 200 | — | title “On Wayfinding / Nainoa Thompson” |
| 3 | `https://archive.hokulea.com/ike/hookele/star_compasses.html` | 200 | — | title “Star Compasses” |
| 4 | `https://blog.tepapa.govt.nz/2016/12/02/the-changing-art-of-tatau-samoan-tattooing/` | 200 | — | title “The changing art of tatau: Samoan tattooing \| Te Papa’s Blog” |
| 5 | `https://doi.org/10.1038/s41598-024-53063-7` | 200 | `https://www.nature.com/articles/s41598-024-53063-7?error=cookies_not_supported…` | title “The invention of writing on Rapa Nui (Easter Island)…” |
| 6 | `https://doi.org/10.1093/oso/9780190681685.001.0001` | **403** | `https://academic.oup.com/book/39618` | no body (bot wall; §6) |
| 7 | `https://doi.org/10.1353/cp.2004.0026` | 200 | `https://muse.jhu.edu/verify?url=%2Farticle%2F51214…` | interstitial title “Project MUSE -- Verification required!” |
| 8 | `https://doi.org/10.1353/ol.2011.0014` | 200 | `https://muse.jhu.edu/verify?url=%2Farticle%2F464587…` | interstitial title “Project MUSE -- Verification required!” |
| 9 | `https://guides.library.manoa.hawaii.edu/c.php?g=105493&p=683341` | 200 | — | title “Secondary Sources - Traditional Hawaiian Tattooing - Research Guides at University of Hawaiʻi at Mānoa” |
| 10 | `https://hilo.hawaii.edu/wehe/?q=k%C4%81pe%CA%BBa` | 200 | `https://wehe.hilo.hawaii.edu/?q=k%C4%81pe%CA%BBa` (301) | title “kāpeʻa — Wehe²wiki² Hawaiian Language Dictionaries” |
| 11 | `https://pollex.eva.mpg.de/entry/fetuqu/` | 200 | `https://pollex.org.nz/entry/fetuqu/` (301) | title “Entries for FETUQU [AN] Star n” |
| 12 | `https://pollex.eva.mpg.de/entry/folau/` | 200 | `https://pollex.org.nz/entry/folau/` (301) | title “Entries for FOLAU [AN] Expedition by sea; sea voyage; travel by sea” |
| 13 | `https://pollex.eva.mpg.de/entry/kau-waka/` | 200 | `https://pollex.org.nz/entry/kau-waka/` (301) | title “Entries for KAU-WAKA [PN] Crew of a canoe: *kau-waka” |
| 14 | `https://pollex.eva.mpg.de/entry/laa.1/` | 200 | `https://pollex.org.nz/entry/laa.1/` (301) | title “Entries for LAA.1 [AN] A sail” |
| 15 | `https://pollex.eva.mpg.de/entry/matagi/` | 200 | `https://pollex.org.nz/entry/matagi/` (301) | title “Entries for MATAGI [OC] Wind, breeze” |
| 16 | `https://pollex.eva.mpg.de/entry/moana/` | 200 | `https://pollex.org.nz/entry/moana/` (301) | title “Entries for MOANA [PN] Sea beyond the reef, ocean” |
| 17 | `https://pollex.eva.mpg.de/entry/waka.a/` | 200 | `https://pollex.org.nz/entry/waka.a/` (301) | title “Entries for WAKA.A [AN] Canoe” |
| 18 | `https://pollex.eva.mpg.de/search/?query=moana&field=protoform` | 200 | `https://pollex.org.nz/search/?query=moana&field=protoform` (301) | title “Pollex Online” |
| 19 | `https://tepapastore.co.nz/products/tatau-a-history-of-samoan-tattooing` | 200 | — | title “Tatau: A History of Sāmoan Tattooing – TePapaStore” |
| 20 | `https://uhpress.hawaii.edu/title/hawaiian-mythology/` | 200 | — | title “Hawaiian Mythology – UH Press” |
| 21 | `https://uhpress.hawaii.edu/title/we-the-navigators-the-ancient-art-of-landfinding-in-the-pacific/` | 200 | — | title “We, the Navigators… (Second Edition) – UH Press” |
| 22 | `https://www.manoaheritagecenter.org/wp-content/uploads/2022/02/Hawaiian-Star-Lines-and-Names-for-Stars.pdf` | 200 | — | application/pdf, 7,173,193 B; OCR p.1 “Hawaiian Star Lines and Names for Stars” (§4) |
| 23 | `https://www.royalsociety.org.nz/150th-anniversary/tetakarangi/mau-moko-the-world-of-maori-tattoongahuia-te-awekotuku-linda-waimarie-nikora-mohi-r-rua-rolinda-karapu-and-becky-nunes-2007` | **403** | — | no body (Cloudflare wall; §6) |
| 24 | `https://www.sidestone.com/books/material-approaches-to-polynesian-barkcloth` | 200 | — | title “Material Approaches to Polynesian Barkcloth” |
| 25 | `https://www.sidestone.com/openaccess/9789088909719.pdf` | 200 | — | application/pdf, 32,555,644 B; pdftotext p.1 “MATERIAL APPROACHES TO POLYNESIAN BARKCLOTH” |
| 26 | `https://www.ucpress.edu/books/on-the-road-of-the-winds/paper` | 200 | — | title “On the Road of the Winds by Patrick Vinton Kirch - Paper - University of California Press” |

Tally (pre-edit set): **24 × 200 / 2 × 403** — of the 200s, 22 delivered real content (title/PDF/OCR-verified, §4) and 2 are MUSE verification interstitials (rows 7–8). Post-edit re-run against the delivered set (driver `.scratch/r17c07/sweep2.py` → `.scratch/r17c07/sweep-run2.json`, 2026-10-18T09:26:28Z, bound to delivered `sha256 a47639dc…`): same tally, 24 × 200 / 2 × 403; the 8 `https://pollex.org.nz/…` rows and the `https://wehe.hilo.hawaii.edu/?q=k%C4%81pe%CA%BBa` row are 200 with no further redirect.

## 4. Content verification (bodies, 2026-10-18T09:19:39Z receipt)

Method: 2xx bodies re-fetched (`curl -sS -o body/NN.bin -L --max-time 60 --max-filesize 40000000`, same UA) → `.scratch/r17c07/bodies.json`; `<title>` extracted from the first 400 kB; PDFs inspected with `pdfinfo` + `pdftotext`; the scanned manoa PDF rendered and OCR’d:

```
pdftoppm -f 1 -l 1 -r 150 -png .scratch/r17c07/body/21.bin .scratch/r17c07/manoa-p1 && tesseract .scratch/r17c07/manoa-p1-01.png -
→ “Hawaiian Star Lines and Names for Stars / The wayfinder memorizes the position of stars…” (24 pp, scanned, no text layer)
```

- 22/24 200s delivered real content matching the cited item (titles in §3; the two PDFs verified above; Nature DOI title matches; hokulea titles match the three cited teaching pages).
- 2/24 200s are verification interstitials, not article pages: `https://doi.org/10.1353/cp.2004.0026` and `https://doi.org/10.1353/ol.2011.0014` → `muse.jhu.edu/verify?…` with title “Project MUSE -- Verification required!”. Both are canonical DOI locators; kept, documented (§7).
- 2/26 no body: the two 403s (rows 6, 23), §6.

## 5. Locator repairs applied (old → new + access evidence)

301 checks (2026-10-18T09:26:17Z, raw output `.scratch/r17c07/301-evidence.txt`):

```
curl -sS -I -A 'Mozilla/5.0 (compatible; kotodama-metadata-audit/1.0)' https://pollex.eva.mpg.de/entry/waka.a/
→ HTTP/1.1 301 Moved Permanently / Location: https://pollex.org.nz/entry/waka.a/
curl -sS -I -A 'Mozilla/5.0 (compatible; kotodama-metadata-audit/1.0)' 'https://hilo.hawaii.edu/wehe/?q=k%C4%81pe%CA%BBa'
→ HTTP/2 301 / location: https://wehe.hilo.hawaii.edu/?q=k%C4%81pe%CA%BBa
```

Nine 1:1 replacements landed in the entry (all new targets 200 + content-verified, §3/§4):

| old (baseline bytes) | new (delivered bytes) | content evidence |
|---|---|---|
| `https://pollex.eva.mpg.de/entry/waka.a/` | `https://pollex.org.nz/entry/waka.a/` | title “Entries for WAKA.A [AN] Canoe” |
| `https://pollex.eva.mpg.de/entry/folau/` | `https://pollex.org.nz/entry/folau/` | title “Entries for FOLAU [AN] Expedition by sea; sea voyage; travel by sea” |
| `https://pollex.eva.mpg.de/entry/fetuqu/` | `https://pollex.org.nz/entry/fetuqu/` | title “Entries for FETUQU [AN] Star n” |
| `https://pollex.eva.mpg.de/entry/matagi/` | `https://pollex.org.nz/entry/matagi/` | title “Entries for MATAGI [OC] Wind, breeze” |
| `https://pollex.eva.mpg.de/entry/laa.1/` | `https://pollex.org.nz/entry/laa.1/` | title “Entries for LAA.1 [AN] A sail” |
| `https://pollex.eva.mpg.de/entry/moana/` | `https://pollex.org.nz/entry/moana/` | title “Entries for MOANA [PN] Sea beyond the reef, ocean” |
| `https://pollex.eva.mpg.de/entry/kau-waka/` | `https://pollex.org.nz/entry/kau-waka/` | title “Entries for KAU-WAKA [PN] Crew of a canoe: *kau-waka” |
| `https://pollex.eva.mpg.de/search/?query=moana&field=protoform` | `https://pollex.org.nz/search/?query=moana&field=protoform` | title “Pollex Online” |
| `https://hilo.hawaii.edu/wehe/?q=k%C4%81pe%CA%BBa` | `https://wehe.hilo.hawaii.edu/?q=k%C4%81pe%CA%BBa` | title “kāpeʻa — Wehe²wiki² Hawaiian Language Dictionaries” |

Why these and not the others: the 9 are host moves proven by 301 (permanent redirect) to the same content under a new canonical host — the cited locators were stale-by-move. The other 15 kept locators delivered their content directly (13) or are DOI/interstitial cases handled in §6–§7; nothing else was changed.

## 6. Blocked locators — replacement attempts (documented, nothing adopted)

Row 6 — `https://doi.org/10.1093/oso/9780190681685.001.0001` (Mahuika 2019; role in the entry: “Bibliography/publisher description checked”). Candidates probed 2026-10-18:

| candidate | result |
|---|---|
| `https://academic.oup.com/book/39618` (DOI target) | 403, 5,469 B challenge body |
| `https://global.oup.com/academic/product/rethinking-oral-history-and-tradition-9780190681685` | 202, 0 B (challenge) |
| `https://openlibrary.org/isbn/9780190681685.json` | 000 timeout (2 attempts, 20 s / 25 s) |
| `https://archive.org/advancedsearch.php?q=title%3A%28rethinking+oral+history%29&output=json` | 200 JSON, `numFound: 0` (no scan) |
| `https://books.google.com/books?vid=ISBN9780190681685` | **200, content-verified** — title “Rethinking Oral History and Tradition: An Indigenous Perspective - Nepia Mahuika” |

Disposition: **not adopted** — the DOI is the canonical persistent identifier and the block is publisher bot protection (403 for non-browser clients), not breakage; the Google Books record is named here as the live alternative if a future round wants a swap.

Row 23 — `https://www.royalsociety.org.nz/150th-anniversary/tetakarangi/mau-moko-…` (Te Awekotuku et al. 2007 record; role: “Bibliographic record and co-authorship checked”). Candidates probed 2026-10-18:

| candidate | result |
|---|---|
| cited page, browser UA + full headers | 403, Cloudflare challenge body `<title>Just a moment...` |
| `https://www.royalsociety.org.nz/` (root) | 403 — wall is site-wide, not page-level |
| `https://natlib.govt.nz/records/21908090` (NZ National Library record) | 302 redirect loop (curl error 47, max 50) / 403 with browser headers — blocked |
| `https://tewaharoa.victoria.ac.nz/discovery/fulldisplay/alma9910999354002386/64VUW_INST:VUWNUI` | 200 but Primo JS app shell — no server-rendered record data (empty `<title>`); not content-verifiable via curl |
| `https://www.penguin.co.nz/books/mau-moko-9780670045617` | 404 (slug guess; no record page found) |
| `https://www.abebooks.com/9780824832537/Mau-Moko-World-Maori-Tatoo-0824832531/plp` | 202, 0 B (challenge) |
| `https://archive.org/advancedsearch.php?q=title%3A%28mau+moko%29&output=json` | 200 JSON, `numFound: 0` (no scan) |
| `https://books.google.com/books?vid=ISBN9780670045617` | **200, content-verified** — title “Mau Moko - Ngahuia Te Awekotuku”; page also names co-authors Nikora and Becky Nunes |

Disposition: **not adopted** — the cited page is Cloudflare-walled to non-browser clients (site-wide), not evidence of breakage; the Google Books record is named as the live alternative if a future round wants a swap. (Candidates were located via web search on 2026-10-18; all probes used the same curl UA except where a browser UA is stated.)

## 7. Entry edit (the only corpus write)

File `corpus/knowledge/civilizations/polynesia-navigation.md`, 3 lines changed, `+3/−3` (`git diff --numstat f30b6f8188937632bbedd0e7b29aeefff6f8b07b -- <path>` → `3 3`; no line added or removed):

- line 174 (POLLEX lexical entry URLs): the 8 locators replaced old → new (pollex.eva.mpg.de → pollex.org.nz), link text unchanged.
- line 175 (Pukui–Elbert Wehe search): locator replaced (hilo.hawaii.edu/wehe → wehe.hilo.hawaii.edu), link text unchanged.
- line 6 (`verified-at`): appends the round-17 C-fix clause — quotes the round-16 stale reason, cites `reports/round-16/civ-map.json` entry 78 and the sweep result (26/26; 22 content-verified, 2 interstitials, 2 bot-blocked with attempts named in this receipt), records the 9 old→new repairs as host forms, and keeps the “locator status is not a re-reading of the cited works” limit. The old→new literal URLs live in this fragment (§5), not in the entry, so the entry’s distinct-URL inventory stays exactly 26.

before-bytes sha256 `ff72bf1143be58fbc10ffce9b1f7b3a22317c6cbf79a0fab2fd7e0c7a4d0c33f` (= round-16 map digest prefix) → after-bytes sha256 `a47639dc0774bd7c12782d61099ed07c14b3712d3092f76a1102cd7176bb5981` (command `sha256sum corpus/knowledge/civilizations/polynesia-navigation.md`, 2026-10-18).

Post-edit battery (2026-10-18, commands + outputs):

```
python3 tools/gates/provenance-audit.py corpus/knowledge/civilizations/polynesia-navigation.md
→ INFO scan: files=1 marks=0 mark-lines=0 findings=0 blocked=0   (exit 0)
```

- Header fields 6/6 (`topic`, `sources`, `couples`, `source`, `verified-at`, `recheck`), couples links 15/15 resolved (reproduces the filed V05 count, `reports/round-9/metadata/v05-civ-77-94.md`; control run printed MATCH for this entry in `reports/round-16/civ/072-083.md` §2.3), `(to-verify)` marks 0 (unchanged), file still 210 lines, URL inventory 26 (command in §3).

## 8. Limits

- **Presence-level verification only** (status codes, effective URLs, titles, PDF/OCR identity). No passage-level re-inspection of the cited works’ arguments; no claim about the quality or currency of their content.
- The sweep is **26/26 of the entry’s URLs** (full, not a sample); retrieval dates are point-in-time (2026-10-18, ~09:17–09:27 UTC) — intermittent availability is not ruled out. The 2 blocked locators are dated facts, not permanent verdicts; their primary URLs are kept for recovery.
- Bot-block classification (403/202/challenge bodies) follows the round-8 M04 precedent (publisher bot blocks ≠ link rot), not an independent liveness proof.
- The 2 MUSE DOI links resolve for curl to a verification interstitial; DOIs are canonical persistent identifiers and were not replaced.
- No freshness axis-move claim; no canon, rights, or clearance ruling. Everything here is NON-CANON lane evidence.
- This fragment does not update the round-16 map (a map-scribe’s work); §9 carries the input row.

## 9. Map-scribe input

```json
{
  "file": "polynesia-navigation.md",
  "path": "corpus/knowledge/civilizations/polynesia-navigation.md",
  "status": "stale-fixed",
  "verified_at": "2026-10-18",
  "distinct_urls_before": 26,
  "distinct_urls_after": 26,
  "old_to_new": [
    {"old": "https://pollex.eva.mpg.de/entry/waka.a/", "new": "https://pollex.org.nz/entry/waka.a/", "why": "host 301-moved; new target 200, title 'Entries for WAKA.A [AN] Canoe'"},
    {"old": "https://pollex.eva.mpg.de/entry/folau/", "new": "https://pollex.org.nz/entry/folau/", "why": "host 301-moved; new target 200, FOLAU entry title"},
    {"old": "https://pollex.eva.mpg.de/entry/fetuqu/", "new": "https://pollex.org.nz/entry/fetuqu/", "why": "host 301-moved; new target 200, FETUQU entry title"},
    {"old": "https://pollex.eva.mpg.de/entry/matagi/", "new": "https://pollex.org.nz/entry/matagi/", "why": "host 301-moved; new target 200, MATAGI entry title"},
    {"old": "https://pollex.eva.mpg.de/entry/laa.1/", "new": "https://pollex.org.nz/entry/laa.1/", "why": "host 301-moved; new target 200, LAA.1 entry title"},
    {"old": "https://pollex.eva.mpg.de/entry/moana/", "new": "https://pollex.org.nz/entry/moana/", "why": "host 301-moved; new target 200, MOANA entry title"},
    {"old": "https://pollex.eva.mpg.de/entry/kau-waka/", "new": "https://pollex.org.nz/entry/kau-waka/", "why": "host 301-moved; new target 200, KAU-WAKA entry title"},
    {"old": "https://pollex.eva.mpg.de/search/?query=moana&field=protoform", "new": "https://pollex.org.nz/search/?query=moana&field=protoform", "why": "host 301-moved; new target 200, 'Pollex Online' search"},
    {"old": "https://hilo.hawaii.edu/wehe/?q=k%C4%81pe%CA%BBa", "new": "https://wehe.hilo.hawaii.edu/?q=k%C4%81pe%CA%BBa", "why": "host 301-moved; new target 200, kāpeʻa Wehe²wiki² title"}
  ],
  "sha256_before": "ff72bf1143be58fbc10ffce9b1f7b3a22317c6cbf79a0fab2fd7e0c7a4d0c33f",
  "sha256_after": "a47639dc0774bd7c12782d61099ed07c14b3712d3092f76a1102cd7176bb5981",
  "sweep": {"date": "2026-10-18", "total": 26, "live_200": 24, "content_verified": 22, "interstitial_200": 2, "blocked_403": 2, "replaced": 9, "command": "curl -sS -o /dev/null -w '%{http_code} %{url_effective} %{content_type} %{size_download} %{time_total}' -L --max-time 15 -A 'Mozilla/5.0 (compatible; kotodama-metadata-audit/1.0)' <URL> (M04 method, retry once on 000)"},
  "reason": "round-16 stale-documented reason ('no dated URL-status receipt exists', reports/round-16/civ/072-083.md §3) retired by a full 26/26 live sweep; 9 moved locators (8 POLLEX + Wehe) replaced old→new with 301+content evidence; entry verified-at line keeps the round-16 reason trail",
  "evidence": ["reports/round-17/civ/polynesia-navigation.md"],
  "reason_trail": ["reports/round-16/civ/072-083.md", "reports/round-16/civ-map.json", "reports/round-8/metadata/m05-civ-77-94.md"],
  "limits": "presence-level verification; point-in-time sweep 2026-10-18; bot-blocks classified per M04 precedent; 2 blocked locators kept with attempts named"
}
```
