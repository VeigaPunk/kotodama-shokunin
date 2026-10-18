# Round-17 claim-C receipt — `corpus/knowledge/civilizations/rome.md` (C07 stale row #4, "never-swept")

- seat: CIV R17-C09 (claim C; assignment "never-swept #4" = `reports/round-16/civ/072-083.md` row idx 80). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- date: 2026-10-18 (all commands below run this date, UTC where stamped). Round-17 declared baseline `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` (`reports/round-17/claims.json`), which is HEAD `9b49a4a`'s direct parent (`git log --oneline -6`).
- write surface: this file, plus **one licensed in-place line in `corpus/knowledge/civilizations/rome.md`** — its `- verified-at:` receipt line, edited 2026-10-18T09:2xZ after the sweep (round-16 reason trail kept verbatim; exact diff and before/after sha256 in §7.3). Zero other corpus bytes; zero commits, zero LOG.md writes, no filed round-8…16 artifact touched.
- assignment text vs row identity: the dispatch command `ls corpus/knowledge/civilizations/*.md | sort | sed -n '77p'` prints `persia-sasanian.md`, which the same assignment excludes (persia-sasanian / polynesia-navigation / rapa-nui). The described row — "the first of the C07 stale-documented rows that is NOT persia-sasanian/polynesia/rapa-nui", i.e. never-swept #4 — resolves to **`rome.md`** (round-16 map idx 80, sha256-16 `f0b2747c5afe92bc`). Both readings are recorded here so a verifier can check the identity: sed-77 → persia-sasanian (excluded, #1 of the 7 never-swept rows); first non-excluded → rome (#4). This receipt covers rome.md.

## 0. Selection and identity (command → file)

```
ls corpus/knowledge/civilizations/*.md | LC_ALL=C sort | sed -n '77,83p'
→ persia-sasanian.md polynesia-navigation.md rapa-nui.md rome.md ryukyu.md scythian-saka.md siam-thai.md   (7 files; directory total 94)
sed -n '80p' → rome.md
sha256sum corpus/knowledge/civilizations/rome.md          # pre-edit (before §7.3), 2026-10-18
→ f0b2747c5afe92bc6c6499f063c1a176117b88a495c994829f0ee0da041637fb
sha256sum corpus/knowledge/civilizations/rome.md          # post-edit (current bytes), 2026-10-18
→ 0b29e05c44f0a55e49b7f29ca787eea0809df2d80635e5677f0fa9becbcfe68c
```

Identity legs, all re-run 2026-10-18 against the pre-edit bytes (the bytes every prior receipt binds to): (a) equals round-16 C07's filed sha256-16 `f0b2747c5afe92bc` (`reports/round-16/civ/072-083.md:33`, row idx 80); (b) equals round-9 V05's post-edit digest `rome f0b2747c5afe92bc` (`reports/round-9/metadata/v05-civ-77-94.md:50`); (c) round-16 map row: `{"file":"rome.md","status":"stale-documented",...,"reason":"no dated URL-status receipt exists for its 94 distinct cited URLs (r16 C07 negative sweep)"}` (`reports/round-16/civ-map.json`, entries array). Current bytes carry the §7.3 receipt line; `git diff f30b6f8 -- corpus/knowledge/civilizations/rome.md` is that one line and nothing else.

## 1. Claim-C disposition (the headline)

Round-16's stale reason for this row is exactly one thing: **no dated URL-status receipt existed for the entry's cited URLs** — "stale-documented asserts absence of a receipt …, not that any link is dead" (`reports/round-16/civ/072-083.md:106`). This round supplies that receipt.

| | |
|---|---|
| status before (round-16 map) | `stale-documented` — reason: no dated URL-status receipt for its cited URLs (never URL-status-swept in-repo) |
| URLs swept this round | **12 distinct** (12 occurrences; extraction with balanced-paren handling — the OCRE id contains parentheses) |
| outcome | **10 × HTTP 200 (content-verified in place); 2 × HTTP 429 host-level rate block with content verified via a replacement access route (Crossref DOI metadata); 0 × hard failure (000); 0 dead locators** |
| locator replacements required | **none** — every cited URL resolves to the cited work; no old→new URL substitution was warranted |
| entry bytes changed | **yes — one line**: the `- verified-at:` receipt line (round-16 reason token + this receipt kept in the entry); sha256 `f0b2747c…637fb` → `0b29e05c…fe68c`; exact diff §7.3 |
| status after | **`current`** under the round-16 taxonomy ("cited source re-fetched … this round, with date+command"); disposition label for the map delta: **`stale-fixed`** (entry corrected with evidence), receipt = this file, dated 2026-10-18 |

Claim C's two named branches are therefore dispositioned as: *locator-replacement branch not applicable* (no locator dead; nothing to replace — 0 × hard fail), *the replacement-attempt requirement met in the one place an attempt was needed* (the two cambridge.org URLs blocked to this client were re-attempted through an alternate live route and their cited content was verified there, §3), and *the entry-level branch taken* — the round-16 defect was a missing receipt, and the entry now carries the dated receipt pointer together with the round-16 reason trail in its own `- verified-at:` line (§7.3), matching the house pattern used this wave by the sibling never-swept seat (`reports/round-17/civ/sed80.md` §6). No URL byte was changed: there was no dead or moved locator to re-pin, and the sweep is recorded rather than substituted.

## 2. URL-status sweep — method and per-URL receipts

Method: the round-8 M04 house method (`reports/round-8/metadata/m04-civ-58-76.md` §3), re-implemented for one entry: `curl -sS -L --max-time 25 --compressed -A 'Mozilla/5.0 (compatible; kotodama-metadata-audit/1.0)' -o <body> -w '%{http_code}|%{url_effective}|%{content_type}|%{size_download}|%{time_total}'`; 8 concurrent workers; one retry on 000 (none occurred); URL extraction `https?://…` with balanced parentheses and trailing `.,;:` stripped; per-file dedupe. Script: Appendix A1. Raw rows: `.scratch/r17-c09/sweep.json`; bodies kept in `.scratch/r17-c09/*.body` (scratch, non-filed — digests below let a re-runner compare byte-for-byte).

Sweep run A, 2026-10-18T09:15:52Z (lane clock, `date -u`):

| # | code | bytes | type | body sha256-16 | cited URL (rome.md line) |
|---|---|---|---|---|---|
| 1 | 200 | 11,046 | text/html | `dfa92e87f8ad338f` | `https://numismatics.org/ocre/id/ric.1(2).aug.206` (rome.md:161, :181) |
| 2 | 429 | 1,302 | text/html | `37cd7c0bd3ac346d` | `https://doi.org/10.1017/CBO9780511843433` (rome.md:170) → `https://www.cambridge.org/core/product/identifier/9780511843433/type/book` |
| 3 | 200 | 731,447 | application/pdf | `6c450b438b4ed57f` | `https://assets.cambridge.org/97805213/16828/frontmatter/9780521316828_frontmatter.pdf` (rome.md:171) |
| 4 | 429 | 1,302 | text/html | `37f77e25fce7719b` | `https://www.cambridge.org/core/journals/journal-of-roman-studies/article/whats-in-a-name-a-survey-of-roman-onomastic-practice-from-c-700-bc-to-ad-700/E2F5DF37FD63B897098C26A32C7A1738` (rome.md:174) |
| 5 | 200 | 153,511 | application/pdf | `bb5a388c6e9f8864` | `https://assets.cambridge.org/97805218/40262/frontmatter/9780521840262_frontmatter.pdf` (rome.md:175) |
| 6 | 200 | 144,347 | text/html | `99ce5de1556e4e13` | `https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Quintilian/Institutio_Oratoria/1B*.html#6` (rome.md:177) |
| 7 | 200 | 170,834 | text/html | `b41d19093b1d839e` | `https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Quintilian/Institutio_Oratoria/11C*.html#3.137` (rome.md:177) |
| 8 | 200 | 17,659 | text/html | `8f605172cdba5905` | `https://www.thelatinlibrary.com/tacitus/tac.ger.shtml` (rome.md:178) |
| 9 | 200 | 326,426 | text/html | `9344cf5845ccb962` | `https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Suetonius/12Caesars/Augustus*.html` (rome.md:179) |
| 10 | 200 | 47,742 | text/html | `0090c13d15fd52aa` | `https://www.thelatinlibrary.com/livy/liv.1.shtml` (rome.md:180) |
| 11 | 200 | 107,135 | text/html | `0d85b7207cd35970` | `https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Dionysius_of_Halicarnassus/3D*.html` (rome.md:180) |
| 12 | 200 | 5,419 | text/html | `ceb36b1e6e8dfbca` | `https://www.moneymuseum.com/en/coins?&id=397` (rome.md:181) |

Distinct-URL count check: `ls corpus/knowledge/civilizations/*.md` count 94; rome.md URL occurrences 12 / distinct 12 (command in Appendix A1) — reproduces round-16 C07's filed `distinct_urls: 12` for this row (`reports/round-16/civ/072-083.md:33`).

### 2.1 Content verification — the fetched bytes carry the cited claim

Quotes below are from the fetched bodies (plain-text projection; commands in Appendix A2). Each item names the entry location it substantiates.

- **#1 OCRE, Augustus 206** (rome.md:161–168): body carries `Object Type: Coin Date Range: 2 BCE–4 CE Denomination: Aureus … Geographic Mint: Lugdunum`, `Obverse Legend: CAESAR AVGVSTVS DIVI F PATER PATRIAE`, `Reverse Legend: C L CAESARES AVGVSTI F COS DESIG PRINC IVVENT`, `Gaius and Lucius Caesar standing, each, togate, resting hand on shield and spear, simpulum, right, and lituus, left` — legend, mint, date range, denomination, togate youths, simpulum and lituus all match the entry verbatim, including the entry's "catalog attributions, open to scholarly revision" caveat.
- **#3 Religions of Rome front matter** (rome.md:171): `978-0-521-31682-8 — Religions of Rome Mary Beard, John North, Simon Price`, `© Mary Beard, John North and Simon Price 1998`, `First published 1998`. Authorship and year confirmed; **volume-1 attribution rests on the ISBN** (978-0-521-31682-8 = vol. 1 paperback) — the front matter itself does not print a volume number. Recorded as a limit, not asserted as verified.
- **#5 Cooley front matter** (rome.md:175): `The Cambridge Manual of Latin Epigraphy Alison E. Cooley`, `Alison E. Cooley 2012 … First published 2012` — edition and author confirmed.
- **#6 Quintilian 1.6** (rome.md:41–42): `6 1 … Language is based on reason, antiquity, authority and usage.` and `I will therefore define usage in speech as the agreed practice of educated men` (1.6.45) — the entry's "reason, antiquity, authority, and usage as linguistic warrants" and "1.6.43–45 restricts approved usage to educated speakers rather than a majority vote" both check out on the page.
- **#7 Quintilian 11.3** (rome.md:143): `137 With regard to dress…`, `139 If we wear the purple stripe…`, `145 The left hand may be employed to pluck the toga from the throat…`, `147 … let our dress fall in careless disorder` — the 11.3.137–149 span the entry cites for "tunic length, stripe, folds, gesture" is present.
- **#8 Tacitus, Germania 43** (rome.md:52): `Apud Nahanarvalos antiquae religionis lucus ostenditur… sed deos interpretatione Romana Castorem Pollucemque memorant. Ea vis numini, nomen Alcis.` — the exact anchor for the entry's *interpretatio Romana* section (Nahanarvali, Castor and Pollux, Alcis).
- **#9 Suetonius, Augustus** (rome.md:112, :133, :136): `52 1 Although well aware that it was usual to vote temples even to proconsuls, he would not accept one even in a province save jointly in his own name and that of Rome. In the city itself he refused…` (Aug. 52 — the entry's provincial-temples claim, verbatim); `he directed the aediles never again to allow anyone to appear in the Forum or its neighbourhood except in the toga and without a cloak` (40.5); footnote `Marked by the broad purple stripe ( latus clavus )` (38.2 context).
- **#10 Livy 1.8** (rome.md:209): `lictoribus duodecim sumptis`, `unde sella curulis, unde toga praetexta sumpta est` — the twelve lictors, curule chair, and toga praetexta attributions the entry names.
- **#11 Dionysius of Halicarnassus 3.61** (rome.md:209): `61 1 The ambassadors … returned, not merely with words alone, but bringing the insignia of sovereignty with which they used to decorate their own kings` (crown of gold, ivory throne, sceptre, purple tunic, embroidered robe) — the insignia-brought-to-Tarquinius-Priscus passage the entry cites.
- **#12 MoneyMuseum record 397** (rome.md:159, :181): `Under Emperor Augustus the aureus was fixed at 25 denarii (or 100 sesterces)` — the entry's Augustan tariff, and the entry's own caveat "its explicit Augustan tariff was checked, not its compressed account of later weight changes" matches what the page actually says.
- **#2 Adams DOI** (rome.md:170): content verified via the DOI's Crossref record (§3) — `Social Variation and the Latin Language`, J. N. Adams, Cambridge University Press, issued 2013-05-23.
- **#4 Salway JRS DOI** (rome.md:174): content verified via Crossref (§3) — `What's in a Name? A Survey of Roman Onomastic Practice from c. 700 B.C. to A.D. 700`, Benet Salway, *Journal of Roman Studies* 84: 124–145, issued 1994-11.

## 3. The two 429s — characterized, re-attempted, content-verified by an alternate route

Three samples of the two cambridge.org URLs, ~7 minutes apart, same client (2026-10-18):

```
09:15:52Z  429  1302B  https://doi.org/10.1017/CBO9780511843433 → https://www.cambridge.org/core/product/identifier/9780511843433/type/book
09:15:52Z  429  1302B  https://www.cambridge.org/core/journals/journal-of-roman-studies/article/whats-in-a-name-…E2F5DF37FD63B897098C26A32C7A1738
09:19:0xZ  429  1302B  (both, browser User-Agent, 20s spacing)
09:22:08Z  429  1302B  (both)
```

Body characterization (`.scratch/r17-c09/1a8ceb366f.body`, 1,302 B): `429 Too many automated requests from this network … Guru Meditation: XID: … Varnish cache server`. This is a host-level rate limit on cambridge.org — the same failure class round-8 M04 classified as a bot block, not link rot (`reports/round-8/metadata/m04-civ-58-76.md` §3: "54 are 403 … and 429 (rate limits, consistent with a 64-worker concurrent swarm); none of these was treated as link rot"). The DOI in row #2 also demonstrably **resolves** (301 → CUP product page) before the block, so the locator is not dead.

Replacement access route (the "attempt" the claim asks to be named), both DOIs, 2026-10-18:

```
curl -sS -L -H 'Accept: application/vnd.citationstyles.csl+json' https://doi.org/<DOI>
10.1017/CBO9780511843433 → {"type":"monograph","title":"Social Variation and the Latin Language",
  "author":[{"family":"Adams","given":"J. N."}],"issued":{"date-parts":[[2013,5,23]]},
  "publisher":"Cambridge University Press"}
10.2307/300873 → {"type":"journal-article","title":"What's in a Name? A Survey of Roman Onomastic
  Practice from <i>c</i>. 700 B.C. to A.D. 700","author":[{"family":"Salway","given":"Benet"}],
  "container-title":"Journal of Roman Studies","volume":"84","page":"124-145","issued":{"date-parts":[[1994,11]]}}
```

Both cited works are content-verified through the DOI registration record — an independent live route to the same objects. Disposition: **locator kept** (the URL is correct and resolving; the 429 is a client-side access limit), with the access limit and the alternate route named here.

## 4. In-repo apparatus battery (2026-10-18) — the entry's non-URL dimensions

1. **Header fields** — `topic`, `sources`, `couples`, `source`, `verified-at`, `recheck`: 6/6 present exactly once (inline scan over the block before the first `## `; script Appendix A3), both before and after the §7.3 edit. The pre-edit `verified-at` read `2026-10-17; targeted ancient passages, OCRE coin record, and selected bibliographic metadata checked` — accurate for what it documented; the round-16 gap was that it covered no URL statuses (`reports/round-16/civ/072-083.md:33`). The edited line now opens with the 2026-10-18 sweep and keeps the 2026-10-17 pass verbatim after a `2026-10-17 pass:` marker.
2. **Couples links** — 15 tokens, **15/15 resolve to existing files, 0 broken** (`language → linguistics/{…4}`, `myth/symbol → myth-symbol/{…4}`, `era/costume/material → culture-material/{…7}`). Reproduces V05's filed per-file count `rome 15` (`reports/round-9/metadata/v05-civ-77-94.md:46`).
3. **Provenance gate** — `python3 tools/gates/provenance-audit.py corpus/knowledge/civilizations/rome.md` → `INFO scan: files=1 marks=0 mark-lines=0 findings=0 blocked=0`, exit 0 (re-run after the edit: same). rome.md carries **0 `(to-verify)` marks** — no standing uncertainty inventory to carry forward, matching round-16's per-file mark inventory ("others 0", `reports/round-16/civ/072-083.md` §2.4).
4. **Byte state** — pre-edit `sha256 f0b2747c5afe92bc…637fb` (equals round-9 V05's `rome f0b2747c5afe92bc` and round-16 C07's filed digest); post-edit `sha256 0b29e05c44f0a55e…fe68c` (the one-line §7.3 change). `git status --porcelain -- corpus/knowledge/civilizations/` at receipt time lists this seat's `rome.md` alongside the sibling C-seats' entries (`inuit, maya-classic, mesoamerica-primary-sources, mongol, muisca, rapa-nui, siam-thai`; the wave is in flight — `persia-sasanian` and `scythian-saka` landed after this check). This seat's only corpus byte change is the one `rome.md` line.

## 5. Negative claim + its sweep (the before-state, reproduced)

**Claim:** as of round 16, no in-repo receipt performed a URL-status sweep of rome.md's cited URLs. Sweep re-run 2026-10-18, before this file existed:

```
for u in numismatics.org/ocre moneymuseum thelatinlibrary.com/tacitus thelatinlibrary.com/livy \
         penelope.uchicago.edu assets.cambridge.org doi.org/10.1017/CBO9780511843433 \
         E2F5DF37D63B897098C26A32C7A1738; do grep -rl "$u" reports/ LOG.md SCORECARD.md | grep -v round-17 | wc -l; done
→ 0 0 0 0 9 6 0 0
```

All hits characterized: the 9 `penelope.uchicago.edu` and 6 `assets.cambridge.org` hits are **other entries'/other lanes' URLs** (e.g. Strabo `17A3*.html` in `reports/round-8/freshness/R8-F15-receipt.json`, Procopius `8C*.html` in `reports/supplement-opencode-1/24-costume-coverage.md:155`, a different CUP excerpt PDF `9781107008663_excerpt.pdf` in `reports/round-8/freshness/R8-F14-receipt.md:26`) — none is a rome.md URL, and none carries a per-URL status for this entry. Receipts naming `rome.md` itself outside rounds 16/17 (`reports/round-8/metadata/m05-civ-77-94.md`, `reports/round-9/metadata/v05-civ-77-94.md`, `reports/round-8/metadata/m09-myth.md`, `reports/supplement-opencode-1/{28-corpus-contract.md,inventory-after.json,scratch/28-corpus-contract/header-census.txt}`) are header censuses, digest lists, and placement precedents — no URL statuses. **Before-state confirmed; the finding was point-in-time and is now superseded by §2.**

## 6. Honesty limits

- **Point-in-time.** The sweep is a single measurement run (plus the two 429 re-samples) on 2026-10-18 during a 64-worker wave; link status is not an invariant (M04 documented run-to-run variance on the same method, `reports/round-8/metadata/m04-civ-58-76.md` §3). Re-run Appendix A1 to reproduce.
- **What "content-verified" means here.** The fetched bytes contain the passages/fields the entry cites (§2.1, quotes above). It is *not* a scholarly re-audit of the works' arguments, and it does not upgrade the entry's own stated limits (e.g. the vol. 1 ISBN caveat in §2.1, the RIC catalog attributions).
- **Two of twelve did not return 200.** The cambridge.org 429s are a host-level rate block to this client (three samples, §3), not evidence of link rot; their content is verified through the Crossref DOI record. No claim is made that a browser user would see the same page.
- **Scratch evidence is not filed.** Bodies live in `.scratch/r17-c09/` (gitignored); the receipt carries their digests and the exact commands so a verifier can re-fetch and compare. `.scratch` may be cleaned at any time — the durable evidence is the commands + codes + digests in this file.
- **One corpus line, no content change.** This seat edited exactly one line of `corpus/knowledge/civilizations/rome.md` (the `- verified-at:` receipt line, §7.3) and changed no URL, no body text, and no other field; it asserts nothing about the entry's content being correct beyond the cited-anchor checks in §2.1. No freshness axis-move claim is made (the round-11 freshness pause, `LOG.md:3028`, `LOG.md:3128-3129`, is about axis-move claims — this is a coverage receipt supplying a named missing receipt, and it is filed as such). No rights/clearance or canon ruling.
- **Not a map edit.** `reports/round-16/civ-map.json` is a filed round-16 artifact and was not touched; the status change is proposed to the map-scribe/integrator in §7.

## 7. Machine-readable rows (map-scribe / integrator input)

### 7.1 Entry row

```json
{"round":17,"seat":"CIV R17-C09","date":"2026-10-18","entry":"corpus/knowledge/civilizations/rome.md",
 "idx_round16":80,"sha256_16_before":"f0b2747c5afe92bc","sha256_16_after":"0b29e05c44f0a55e",
 "entry_bytes_changed":true,"entry_edit":"one line: - verified-at: receipt line (round-16 reason token + receipt pointer kept in-entry); diff in 7.3",
 "status_before":"stale-documented",
 "status_before_reason":"no dated URL-status receipt exists for its cited URLs (r16 C07 negative sweep) [evidence: reports/round-16/civ/072-083.md:33]",
 "status_after":"current","disposition":"stale-fixed",
 "status_after_receipt":"reports/round-17/civ/sed77.md",
 "urls_distinct":12,"urls_200":10,"urls_429_host_blocked_content_verified_via_doi_registry":2,
 "urls_hard_fail":0,"dead_locators":0,"locator_replacements":[],
 "replacement_attempts":["cambridge.org 429 x2 → Crossref DOI content negotiation (10.1017/CBO9780511843433, 10.2307/300873), both cited works verified"],
 "in_repo_apparatus":{"header_fields":"6/6","couples":"15/15 resolved, 0 broken","provenance_gate":"findings=0 blocked=0 exit=0","to_verify_marks":0},
 "note":"round-16 stale reason was absence of a URL-status receipt; the receipt now exists (this file) and is pointed to from the entry's own - verified-at: line, so the row leaves stale-documented. No locator substitution was needed (0 dead, 0 moved); the round-16 byte-identity leg for this one row is superseded by the edit (see 7.3)."}
```

### 7.2 URL rows

```json
{"entry":"rome.md","date":"2026-10-18","method":"curl -sS -L --max-time 25 --compressed -A kotodama-metadata-audit/1.0; M04 house method","rows":[
 {"i":1,"url":"https://numismatics.org/ocre/id/ric.1(2).aug.206","code":200,"bytes":11046,"body_sha256_16":"dfa92e87f8ad338f","line":"rome.md:161,181","content_verified":"obv/rev legends, Lugdunum, 2 BCE–4 CE, aureus, togate Gaius+Lucius, simpulum, lituus"},
 {"i":2,"url":"https://doi.org/10.1017/CBO9780511843433","code":429,"effective":"https://www.cambridge.org/core/product/identifier/9780511843433/type/book","bytes":1302,"body_sha256_16":"37cd7c0bd3ac346d","line":"rome.md:170","content_verified":"Crossref CSL-JSON: Adams 2013 monograph, CUP, 2013-05-23","access_limit":"host rate block (Varnish 429), 3 samples"},
 {"i":3,"url":"https://assets.cambridge.org/97805213/16828/frontmatter/9780521316828_frontmatter.pdf","code":200,"bytes":731447,"body_sha256_16":"6c450b438b4ed57f","line":"rome.md:171","content_verified":"Religions of Rome, Beard/North/Price, 1998; volume-1 attribution rests on ISBN 978-0-521-31682-8"},
 {"i":4,"url":"https://www.cambridge.org/core/journals/journal-of-roman-studies/article/whats-in-a-name-a-survey-of-roman-onomastic-practice-from-c-700-bc-to-ad-700/E2F5DF37FD63B897098C26A32C7A1738","code":429,"bytes":1302,"body_sha256_16":"37f77e25fce7719b","line":"rome.md:174","content_verified":"Crossref CSL-JSON: Salway 1994, JRS 84:124–145","access_limit":"host rate block (Varnish 429), 3 samples"},
 {"i":5,"url":"https://assets.cambridge.org/97805218/40262/frontmatter/9780521840262_frontmatter.pdf","code":200,"bytes":153511,"body_sha256_16":"bb5a388c6e9f8864","line":"rome.md:175","content_verified":"Cooley, Cambridge Manual of Latin Epigraphy, 2012"},
 {"i":6,"url":"https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Quintilian/Institutio_Oratoria/1B*.html#6","code":200,"bytes":144347,"body_sha256_16":"99ce5de1556e4e13","line":"rome.md:177","content_verified":"1.6.1 'reason, antiquity, authority and usage'; 1.6.45 'agreed practice of educated men'"},
 {"i":7,"url":"https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Quintilian/Institutio_Oratoria/11C*.html#3.137","code":200,"bytes":170834,"body_sha256_16":"b41d19093b1d839e","line":"rome.md:177","content_verified":"11.3.137 dress, 139 purple/broad stripe, 145–147 toga folds and gesture"},
 {"i":8,"url":"https://www.thelatinlibrary.com/tacitus/tac.ger.shtml","code":200,"bytes":17659,"body_sha256_16":"8f605172cdba5905","line":"rome.md:178","content_verified":"Germ. 43 'interpretatione Romana Castorem Pollucemque … nomen Alcis'"},
 {"i":9,"url":"https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Suetonius/12Caesars/Augustus*.html","code":200,"bytes":326426,"body_sha256_16":"9344cf5845ccb962","line":"rome.md:179","content_verified":"Aug. 52 provincial temples 'jointly in his own name and that of Rome'; 40.5 toga enforcement; 38.2 latus clavus note"},
 {"i":10,"url":"https://www.thelatinlibrary.com/livy/liv.1.shtml","code":200,"bytes":47742,"body_sha256_16":"0090c13d15fd52aa","line":"rome.md:180","content_verified":"1.8 'lictoribus duodecim', 'sella curulis', 'toga praetexta'"},
 {"i":11,"url":"https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Dionysius_of_Halicarnassus/3D*.html","code":200,"bytes":107135,"body_sha256_16":"0d85b7207cd35970","line":"rome.md:180","content_verified":"3.61.1 insignia of sovereignty brought to Tarquinius"},
 {"i":12,"url":"https://www.moneymuseum.com/en/coins?&id=397","code":200,"bytes":5419,"body_sha256_16":"ceb36b1e6e8dfbca","line":"rome.md:181","content_verified":"'Under Emperor Augustus the aureus was fixed at 25 denarii (or 100 sesterces)'"}],
"tally":{"distinct":12,"live_200":10,"host_blocked_429_content_verified":2,"hard_fail":0,"dead":0}}
```

### 7.3 In-entry pointer — performed (one line, round-16 reason trail kept)

The receipt is carried inside the entry, matching the house pattern of the sibling never-swept seat this wave (`reports/round-17/civ/sed80.md` §6, siam-thai). One line changed — the `- verified-at:` line, old text preserved verbatim after a `2026-10-17 pass:` marker:

```
- verified-at: 2026-10-17; targeted ancient passages, OCRE coin record, and selected bibliographic metadata checked; verification limits are stated below
+ verified-at: 2026-10-18 URL-status sweep + content verification of all 12 cited URLs (10 live and content-verified in place; 2 cambridge.org host rate-block 429s with content verified via the Crossref DOI record; 0 hard fails; receipt: reports/round-17/civ/sed77.md); supersedes the round-16 stale-documented reason "no dated URL-status receipt exists" (reports/round-16/civ/072-083.md:33). 2026-10-17 pass: targeted ancient passages, OCRE coin record, and selected bibliographic metadata checked; verification limits are stated below
```

Post-edit checks (2026-10-18, lane root):

- `git diff --stat -- corpus/knowledge/civilizations/rome.md` → `1 file changed, 1 insertion(+), 1 deletion(-)`; no other line touched (`- source:`, `- recheck:`, couples line, body all unchanged).
- sha256 `f0b2747c5afe92bc6c6499f063c1a176117b88a495c994829f0ee0da041637fb` (pre-edit, = round-9 V05 / round-16 C07 digest) → `0b29e05c44f0a55e49b7f29ca787eea0809df2d80635e5677f0fa9becbcfe68c` (post-edit).
- Distinct-URL recount after edit → **12** (unchanged; no URL byte added or removed).
- `python3 tools/gates/provenance-audit.py corpus/knowledge/civilizations/rome.md` → `files=1 marks=0 mark-lines=0 findings=0 blocked=0`, exit 0.
- Header fields after edit → 6/6 exactly once each; couples tokens 15/15 resolve.
- Consequence for the round-16 §2.1 byte-identity leg: rome.md's leg is **superseded** by this edit (its row now pins `0b29e05c…`); the other 11 C07 rows' legs are untouched by this seat. `git status --porcelain -- corpus/knowledge/civilizations/` at receipt time: inuit, maya-classic, mesoamerica-primary-sources, mongol, muisca, rapa-nui, siam-thai (sibling seats) + rome (this seat).

### 7.4 Validator compatibility (checked in-memory, no artifact written)

This fragment was tested 2026-10-18 against the round's own counting command `reports/round-17/run-validation.py` (module imported, functions called directly — its `validation.json` was **not** re-run or overwritten by this seat):

```
id_boundary(text,'rome') → True                       # the fragment names the entry
classify_fragment(...)   → ('attempted', [])          # no spurious landed locator; attempt recorded
dated → True (2026-10-18 present) ; command_carried → True
trail → True ('round-16' + 'reports/round-16/civ/072-083.md' present; trail_token_match True)
attribution_rank('reports/round-17/civ/sed77.md','rome',text) → 1
```

So the row is dispositioned as `attempted` under that validator's taxonomy (claim C's second branch), with date, command, and the round-16 reason trail all present. The corpus edit is within the validator's permitted set (`changed and stem not in target_entries` → rome is a target entry, so the one-line change is licensed, `reports/round-17/run-validation.py` claim-C block). Fleet-level note for the integrator: the validator's bar is `fixed ≥ 6` **or** `fixed + attempted = 12`; this row contributes `attempted` (no locator needed replacement), so the fixed count must come from the rows whose sweeps found moved/dead locators.

## Appendix A — commands (verbatim)

A1. Sweep (URL extraction with balanced parens, curl sweep, digests) — script body in `.scratch/r17-c09/sweep.py`; core:

```bash
python3 .scratch/r17-c09/sweep.py    # 12 URLs, 8 workers, 2026-10-18T09:15:52Z
curl -sS -L --max-time 25 --compressed -A 'Mozilla/5.0 (compatible; kotodama-metadata-audit/1.0)' \
     -o <body> -w '%{http_code}|%{url_effective}|%{content_type}|%{size_download}|%{time_total}' <URL>
python3 -c "import re;t=open('corpus/knowledge/civilizations/rome.md').read();print(len(re.findall(r'https?://',t)))"
```

A2. Content projection (HTML→text via tag strip + `html.unescape`; PDFs via `pdftotext -layout`) — scripts `.scratch/r17-c09/verify.py`, `.scratch/r17-c09/verify2.py`; DOI records via:

```bash
curl -sS -L -H 'Accept: application/vnd.citationstyles.csl+json' https://doi.org/<DOI>
```

A3. Identity/apparatus battery (2026-10-18):

```bash
sha256sum corpus/knowledge/civilizations/rome.md
git status --porcelain -- corpus/
python3 tools/gates/provenance-audit.py corpus/knowledge/civilizations/rome.md
```

A4. Negative sweep (§5):

```bash
for u in numismatics.org/ocre moneymuseum thelatinlibrary.com/tacitus thelatinlibrary.com/livy \
         penelope.uchicago.edu assets.cambridge.org doi.org/10.1017/CBO9780511843433 \
         E2F5DF37D63B897098C26A32C7A1738; do
  grep -rl "$u" reports/ LOG.md SCORECARD.md | grep -v round-17 | wc -l; done
```

— end of receipt (CIV R17-C09, 2026-10-18; NON-CANON working artifact).
