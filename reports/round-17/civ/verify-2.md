# R17-V02 — independent verification of round-17 C-fixer evidence (group 2 of 2)

- Verifier seat: **C R17-V01/V02** (round-17 C-verifiers). This file covers the
  fixer evidence for **`rapa-nui`, `rome`, `siam-thai`, `polynesia-navigation`,
  `ryukyu`, `scythian-saka`** (the second six of the twelve round-16 stale
  entries). Group 1 (`inuit`, `maya-classic`, `mesoamerica-primary-sources`,
  `mongol`, `muisca`, `persia-sasanian`) is in `verify-1.md`.
- Date: 2026-10-18; verification window ~09:19–09:37Z (all stamps UTC). HEAD
  `9b49a4a` throughout; live 64-worker wave, so every corpus hash below is
  re-checked at write time and pinned in the verdict text.
- Method: identical to `verify-1.md` §"Method" — read the receipt's claims and
  commands, re-run the fetches myself (M04 method, the fixer's stricter forms
  where its claim depends on them), re-download and re-hash claimed artifacts,
  spot-check entry text against the claimed old→new locator / reason trail /
  access date, re-run claimed negative sweeps and gates. Shared artifacts:
  `.scratch/v01/sweep12.json` (my 188-URL M04 sweep, 09:19Z) and
  `.scratch/verify-baseline/` (pre-fix copies + sha256, 09:15:49Z).
- **NON-CANON.** No canon, rank, rights/clearance, freshness or promotion ruling
  is made or implied. "Verified" = the fixer's dated, command-carried claims
  reproduce on my independent re-run.

## Summary table (group 2)

| entry | fixer receipt | disposition | my verdict | corpus sha256 at verification |
|---|---|---|---|---|
| rapa-nui | `reports/round-17/civ/rapa-nui.md` | stale-fixed (receipt; no locator change) | **VERIFIED** — static artifacts byte-exact; dynamic pages noted | `c893805a…fb2a0f57` |
| rome | `reports/round-17/civ/sed77.md` | stale-fixed (receipt + one-line entry edit) | **VERIFIED** — tallies/DOIs/sweep exact | `0b29e05c…cbcfe68c` |
| siam-thai | `reports/round-17/civ/sed80.md` | stale-fixed (2 locator re-pins + receipt) | **VERIFIED**, one CDX wording finding | `8bef2a5b…b7cb6c733` |
| polynesia-navigation | `reports/round-17/civ/polynesia-navigation.md` | stale-fixed (9 locator re-pins + receipt) | **VERIFIED** — every check exact | `a47639dc…76bb5981` |
| ryukyu | `reports/round-17/civ/sed78.md` | stale-fixed (receipt; no locator change) | **VERIFIED** — every check exact | `424fcbb5…819afa5` |
| scythian-saka | `reports/round-17/civ/sed79.md` | stale-fixed (1 locator re-pin + receipt) | **VERIFIED** — every check exact | `cb3a6428…b3ab5c51` |

Findings: **F-V01-1** (sed80 CDX overstatement, §3), **F-V02-1** (sed77
`--compressed` byte column, §2), **F-V02-2** (dynamic-page hash variance,
§1), **F-V02-3** (round-16 map reason text "its 94 distinct cited URLs" is the
7-entry group total, §7).

---

## 1. rapa-nui.md — never-swept 9-URL set (receipt `civ/rapa-nui.md`)

| # | fixer claim | my re-run | verdict |
|---|---|---|---|
| 1 | before `e56906e8…`; after `c893805a82ed953c29a3f8a20472c6e0579119e7c59d6a3db9ee5e86fb2a0f57` | both **identical**; diff vs baseline = the one `verified-at` line (+1/−1) | exact |
| 2 | tally 8 × 200 / 1 × 429 (metmuseum), two runs | my M04 sweep: **8×200 / 1×429**, same URLs | exact |
| 3 | static-resource bodies: archive-title, LangSci `6e320d29…` (37,175 B), Zenodo `0d5689d6…` (82,124 B), Wikipedia Moai `6f477d31…` (427,128 B), moevarua `fe4bc89c…` (373,137 B), PMC `32b38f87…`, Nature ×2 `4d1fc28a…`/`4f26d70d…` | LangSci, Zenodo, Wikipedia, moevarua: **byte counts and sha256 exact**; PMC and both Nature pages: **byte counts exact, sha256 differ** (dynamic page tokens); archive.org 261,672 vs 256,646 B (dynamic view counter) | static exact; dynamic = F-V02-2 |
| 4 | metmuseum 429 host-wide (homepage control also 429) | essay **429**; homepage **429** | exact |
| 5 | Wayback fallback snapshot `20250515201504` 200, 191,068 B, sha256 `9eb85329…` | 200, my fetch 191,074 B, sha256 `b7e07230…` (Wayback wrapper varies run-to-run; content present) | reproduces ±wrapper |
| 6 | negative sweep: 9 URL substrings × rounds 5–16 → 0 hits | **0 hits ×9** | exact |
| 7 | entry: `verified-at` +1/−1, 9 distinct URLs, provenance 2 marks findings=0 | **all identical** | exact |
| 8 | KW02 early-date caution remains open; 2 `(to-verify)` marks unchanged | grep/diff confirm the caution text and marks untouched | exact |

**Verdict: VERIFIED.** The dynamic-page hash differences (F-V02-2) are expected
run-to-run variance — same byte counts for the three token-bearing pages, content
markers present; the fixer's own two runs agreed on codes, not bytes.

## 2. rome.md — never-swept 12-URL set (receipt `civ/sed77.md`)

| # | fixer claim | my re-run | verdict |
|---|---|---|---|
| 1 | before `f0b2747c…`; after `0b29e05c44f0a55e49b7f29ca787eea0809df2d80635e5677f0fa9becbcfe68c` (one-line `verified-at` edit) | **identical**; file carries exactly that one-line change | exact |
| 2 | tally 10 × 200 / 2 × 429, 0 hard fail; OCRE `ric.1(2).aug.206` 200 (balanced-paren extraction) | my sweep (balanced-paren): OCRE **200**, 80,524 B raw, body sha16 **`dfa92e87f8ad338f`** = their digest; the two cambridge URLs 429 as claimed; the M04-regex 404 I saw earlier is my own extraction artifact (paren truncation) | exact |
| 3 | body sha16s: tacitus `8f605172cdba5905`, moneymuseum `ceb36b1e6e8dfbca`, Suetonius `9344cf5845ccb962` | **all three identical** (sizes differ only by `--compressed` wire-vs-raw accounting — F-V02-1) | exact |
| 4 | Crossref content negotiation: `10.1017/CBO9780511843433` → Adams monograph 2013-05-23; `10.2307/300873` → Salway, JRS 84:124–145, 1994-11 | **both identical** (type/title/author/container/volume/pages/issued) | exact |
| 5 | negative sweep: `0 0 0 0 9 6 0 0` for the eight substrings | **identical** (penelope 9, assets.cambridge 6 are other entries' URLs) | exact |
| 6 | header fields 6/6; provenance 0 marks findings=0; couples 15/15 | fields **6/6**, provenance **0 marks findings=0**; couples line untouched (filed V05 count 15 stands; resolver not re-run by me) | exact (couples count cited, not re-derived) |
| 7 | versioning: receipt first written as "no edit performed", then §1 updated after the edit landed | first version I read (207 lines) was internally inconsistent; current version (237 lines) is consistent with the tree | resolved before verdict |

**Verdict: VERIFIED.** F-V02-1: the receipt's byte column is `size_download`
under `--compressed` (wire size); an uncompressed re-run shows larger byte
counts with **identical digests** — re-runners should compare the digest column.

## 3. siam-thai.md — never-swept 14-URL set (receipt `civ/sed80.md`)

| # | fixer claim | my re-run | verdict |
|---|---|---|---|
| 1 | before `cf9269bc…`; after `8bef2a5b3936c2f45d9d0027646e4d107d45b5f58942379cbb4db9fb7cb6c733` | **identical** | exact |
| 2 | 14/14 checked: 12 live (incl. 2 via 301) / 2 Cloudflare 403 / 0 hard fail | my M04 sweep: 11×200 + 1×202 (degruyter DOI) + 2×403 = same 12 live / 2 blocked / 0 hard fail | exact |
| 3 | re-pins: S10 `culturalatlas.sbs.com.au` → `theculturalatlas.org` (301; 200, 118,615 B, title "Thai - Naming — Cultural Atlas"); S4/S5 `…view?docId=ft3j49n8h7…` → `…public/book/many-ramayanas…html` (301; 200, 1,657,019 B) | both old URLs **301** to the new ones; new pages **200** with exactly those titles/sizes | exact |
| 4 | diff = exactly 4 changed lines (1 `verified-at` + 3 URL occurrences) | `4 4` numstat; grep: `theculturalatlas` 1, `public/book` 2, old forms 0 / 0 | exact |
| 5 | provenance 0 marks findings=0; distinct URLs 14 after edit | **identical** | exact |
| 6 | blogs.loc.gov 403 ×4 variants; CDX snapshot `20250810213501` 200, length 7,555 | 403 reproduced (my sweep); CDX API returns that snapshot **status 200, length 7555** | exact |
| 7 | degruyter DOI handle resolves (`responseCode 1`); direct GET 202/0 B | handle API → **responseCode 1**, target `degruyterbrill.com/…`; my sweep 202/0 B | exact |
| 8 | cambridge shortcut: "CDX for this exact shortcut URL → `[]` (no capture)" | CDX API returns **two captures** (2022-06-06 and 2024-10-05, both 301) | **finding F-V01-1** |

**F-V01-1 (evidence-wording, non-dispositional).** The receipt's CDX row for
`www.cambridge.org/9781316641132` says "no capture"; the API returns two 301
captures. The operative conclusion (403 bot wall; locator kept) is unaffected and
the retries are documented; the wording overstates, and a future receipt should
say "no 200 capture" if that is what was queried.

**Verdict: VERIFIED, with F-V01-1.**

## 4. polynesia-navigation.md — never-swept 26-URL set (receipt `civ/polynesia-navigation.md`)

| # | fixer claim | my re-run | verdict |
|---|---|---|---|
| 1 | before `ff72bf11…`; after `a47639dc0774bd7c12782d61099ed07c14b3712d3092f76a1102cd7176bb5981`; 3-line diff | **identical** (`3 3` numstat) | exact |
| 2 | tally 24 × 200 / 2 × 403; 22 content-verified, 2 MUSE interstitials | my sweep: **24×200 / 2×403**; both `10.1353/…` DOIs → `muse.jhu.edu/verify?…`, title "Project MUSE -- Verification required!" | exact |
| 3 | 9 re-pins (8 POLLEX + 1 Wehe), both hosts 301 to new | old pollex URL → **301** → `pollex.org.nz` (200); old wehe → **301** → `wehe.hilo.hawaii.edu` (200); entry: old host 1 (trail) / new 9; old wehe 1 (trail) / new 2 | exact |
| 4 | manoa PDF 200, 7,173,193 B, 24 pp scanned (OCR'd) | **200, 7,173,193 B**, 24 pages, scanned (Quartz context) | exact |
| 5 | sidestone PDF 200, 32,555,644 B | **200, 32,555,644 B** | exact |
| 6 | blocked rows: OUP DOI 403; Royal Society 403 with site-wide wall (root also 403, "Just a moment...") | OUP 403 reproduced (my sweep); royal society root **403, title "Just a moment..."** | exact |
| 7 | replacement attempts: books.google `ISBN 9780190681685` → 200 "Rethinking Oral History and Tradition…"; `ISBN 9780670045617` → 200 "Mau Moko…"; archive.org `numFound: 0` | first two **200 with exactly those titles**; archive.org search claim not re-run (secondary) | exact (2 of 3 re-run) |
| 8 | entry battery: provenance 0 marks findings=0; 26 distinct URLs; file 210 lines (`wc -l`) | **identical** (my Python count 211 lines = wc 210) | exact |

**Verdict: VERIFIED.** The negative sweep's long file list was spot-characterized
(header censuses/apparatus only) rather than fully re-derived; the operative
negative (no prior per-URL status) is inherently satisfied — these receipts are
the first URL sweeps for the entry, and my own sweep was independent.

## 5. ryukyu.md — never-swept 12-URL set (receipt `civ/sed78.md`)

| # | fixer claim | my re-run | verdict |
|---|---|---|---|
| 1 | before `de541d33…`; after `424fcbb5de9f4d226039c7472f92372784801a128f62ee6024a71e590819afa5`; `1 1` numstat | **identical** | exact |
| 2 | tally 11 × 200 / 1 × 403 (MDPI), 0 × 404/000 | my sweep: **11×200 / 1×403**, same URL | exact |
| 3 | sizes: artscape 23,993; kyotoreview 183,135; uhpress 143,867; lingdy PDF 1,679,959; ninjal 6,544; xlsx 1,417,613; okimu 33,895; annai6.pdf 187,658; knowledge.html 33,346; web_rekidaihoan PDF 4,752,224 | **every one exact** (my re-fetches with the same UA) | exact |
| 4 | `sed -n '78p'` probes: knowledge.html line 78 = 沖縄の染織… substantive line; annai6.pdf line 78 = 日本列島の言語 bibliography line | **both lines identical to the quoted text** | exact |
| 5 | negative sweep 12/12 URLs × rounds 5–15 → NONE | **12/12 zero hits** | exact |
| 6 | MDPI 403 bot wall; article content retrieved via "second agent" (full text) | my own fetch-tool retrieval returned the full article (Rots 2019, *Religions* 10(5):298, CC BY) including the quoted "This is not merely an academic debate, however." sentence | exact |
| 7 | Wayback fallback `20261006134243` (availability API: status 200, available true) | availability API returns **that snapshot, status 200, available true** | exact |
| 8 | no locator replaced; entry edit = `verified-at` line only | diff confirms single-line edit; reason trail names `072-083.md §3` | exact |

**Verdict: VERIFIED (every check exact).**

## 6. scythian-saka.md — never-swept 12-URL set (receipt `civ/sed79.md`)

| # | fixer claim | my re-run | verdict |
|---|---|---|---|
| 1 | before `aff3ca0a…`; after `cb3a6428c4b174a4917871185e416f3ac7d3ecdf62a016432f87a486b3ab5c51`; `2 2` numstat | **identical** | exact |
| 2 | tally 11 × 200 / 1 × 403 (academia.edu) | my sweep: **11×200 / 1×403**, same URL | exact |
| 3 | sizes: AJA 120,873; books.google Rudenko 121,684 → `.com.br` 302; Issyk wiki 92,359; Thayer 4A 42,727; Iranica 498,050; Leiden 8,911 | **every one exact** (Rudenko 302 → `books.google.com.br`, 121,684 B) | exact |
| 4 | Leiden old route **301 permanent** → `handle/1887/16379`; new form 200, 8,911 B, title "Scythian elements in Old Iranian" | old URL 301s to the handle form; **new 200, 8,911 B** | exact |
| 5 | entry: new locator `handle/1887/16379` ×1, old form ×0; provenance 0 marks findings=0 | **1 / 0**, provenance **0 marks findings=0** | exact |
| 6 | academia 403 ×4 variants; CDX snapshots `20240903145548` (200, 44,430), `20240903145552` (200, 44,448), `20241214064323` (200, 28,798), plus 2026 301s | CDX API returns **exactly those rows** (301s + the three 200s with those lengths) | exact |

**Verdict: VERIFIED (every check exact).**

---

## 7. Cross-cutting findings and notes (group 2)

- **F-V01-1** (siam-thai CDX wording) — §3 above.
- **F-V02-1** (sed77 byte column = `--compressed` wire size) — §2 above.
- **F-V02-2** (dynamic-page hash variance) — §1 above: for dynamic pages
  (Nature, PMC, archive.org, Wayback wrapper), byte-level sha256 is not stable
  run-to-run even with identical byte counts; static resources (PDFs, Wikipedia
  article bodies at a fixed revision, LangSci/Zenodo/moevarua pages) reproduced
  byte-exactly. Neither pattern is a defect in the receipts; it is a re-runner
  caveat.
- **F-V02-3 (map wording, informational).** The round-16 map's per-entry reason
  for all seven never-swept rows reads "no dated URL-status receipt exists for
  **its 94 distinct cited URLs**"; 94 is the **seven-entry group total**
  (`072-083.md:98`), not any single entry's count (e.g. ryukyu 12, polynesia 26).
  Flagged independently by `sed78.md:35` and `polynesia-navigation.md:16`; the
  parent/map-patch builder should correct the wording in the round-17 patch, not
  by editing the filed round-16 map.
- **Versioning note (sed77).** The first version of `civ/sed77.md` I read was
  internally inconsistent about whether rome's entry was edited; the current
  version (237 lines) is consistent with the tree (`0b29e05c…`, one-line edit).
  No finding stands.
- **Validator classification nuance** (carried from `verify-1.md` §7):
  `reports/round-17/validation.json` reads `fixed_count = 3` because entries that
  keep the old URL inside their old→new trail text classify as `attempted`;
  claim C still passes (`failures: []`). Ground truth from this verification:
  locator swaps landed and content-verified in **inuit, mesoamerica, persia,
  polynesia (9), siam-thai (2), scythian-saka (1)**; unchanged-live dispositions
  in **mongol, muisca, rapa-nui, rome, ryukyu**; couples-gap fix in
  **maya-classic**.
- **Sibling verifier artifacts noted:** `reports/round-17/civ/map-patch.json`
  (V03/V04's row-replacement proposal against the filed round-16 map) exists and
  was not modified by me; their independent sweep agrees with mine row-for-row
  where compared (per their `compare.json` cited in `sed78.md`/`sed79.md`).

## 8. Limits of this verification

- Point-in-time: 2026-10-18 ~09:19–09:37Z, one network path; statuses and dynamic
  bodies are not invariants.
- Secondary rows not re-run by me, marked above: rapa-nui's Wayback wrapper
  bytes (content confirmed, wrapper differs), rome's couples resolver count
  (filed count cited), polynesia's archive.org `numFound: 0` probe.
- "Verified" = reproduction of dated, command-carried claims; not a freshness,
  rank, canon, or rights verdict. The freshness pause stays in force; every
  receipt read here states it.

— C R17-V01/V02, round-17 C-verifier, 2026-10-18. Scratch evidence:
`.scratch/v01/` (`sweep12.json`, per-claim fetch bodies and logs).
