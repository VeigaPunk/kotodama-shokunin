# R17-C10 — never-swept #5 disposition: `ryukyu.md` (URL-status sweep + `sed -n '78p'` content probe)

- Seat: C R17-C10 (claim C, coverage; operator regimen loop 2 of 3, build round 1 of 4, 64 workers). Lane root: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- Date: 2026-10-18 (all commands below run this date; UTC stamps as marked; local `date -u` at first command `2026-10-18T09:16:41Z`, at entry edit `2026-10-18T09:26:53Z`).
- Reference revision: round-17 declare `9b49a4a0fca6ceeab917d401945358fdedeb7e11` ("round-17: declare loop-2 build-1 claims D/C/O"); declared baseline `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` (`reports/round-17/claims.json`).
- Assigned technique: `sed -n '78p'` content probe on each fetched document (§4). Assigned artifact name: this file (`reports/round-17/civ/sed78.md`).
- Write surface: this fragment + the licensed in-place receipt edit of the named entry's `verified-at` line (`corpus/knowledge/civilizations/ryukyu.md`, §6). Zero other corpus bytes touched; no commit, no push, no LOG.md/SCORECARD.md write, no filed round-8…16 artifact modified.
- **NON-CANON.** Evidence only: no canon, no lore acceptance, no real-world rights/clearance/attribution ruling is made or absorbed. Statuses are point-in-time access facts, not content-accuracy or freshness verdicts.
- **Freshness pause respected:** no source-freshness axis-move is claimed. The round-17 claim-C text requires a live, content-verified receipt for a named locator; that is what §3–§4 supply. The pause (`LOG.md:3028`; carried `SCORECARD.md:201-205`) is untouched.

## 0. Target resolution — "never-swept #5" = `ryukyu.md`

Round-17 claim C names 12 round-16 stale-documented entries: inuit (dead Dorais locator) + muisca/mongol/mesoamerica (hard-fail URLs) + maya-classic (couples gap) + **7 never-swept URL sets** (`reports/round-17/claims.json:21`). The 7 never-swept sets are the last 7 stale rows of the round-16 map in map/shard order:

```
python3 -c "import json; m=json.load(open('reports/round-16/civ-map.json')); print([e['file'] for e in m['entries'] if e['status']=='stale-documented'])"
→ ['inuit.md','maya-classic.md','mesoamerica-primary-sources.md','mongol.md','muisca.md',
   'persia-sasanian.md','polynesia-navigation.md','rapa-nui.md','rome.md','ryukyu.md',
   'scythian-saka.md','siam-thai.md']                                        (2026-10-18)
```

Sets #1–#7 = persia-sasanian, polynesia-navigation, rapa-nui, rome, **ryukyu (#5)**, scythian-saka, siam-thai — matching the C07 shard rows 77–83 (`reports/round-16/civ/072-083.md:30-36`) and its distinct-URL inventory (`:98`: 9 + 26 + 9 + 12 + 12 + 12 + 14 = 94).

Dispatch token vs row identity, reconciled: the assignment also carried `sed -n '78p' file`. Slice command `ls corpus/knowledge/civilizations/*.md | LC_ALL=C sort | sed -n '78p'` prints `polynesia-navigation.md` — a *different* seat's entry (C07), not #5. The sibling round-17 fragments settle the numbering: `reports/round-17/civ/sed77.md` is seat C09 covering `rome.md` (map idx 80) and `reports/round-17/civ/sed80.md` is seat C12 covering `siam-thai.md` (idx 83) — in both, the dispatch number equals **slice index − 3** (80−3=77, 83−3=80), so for this seat 81−3=**78** → `ryukyu.md`. The verifier seat's own fixer map agrees independently: `.scratch/r17-v34/compare.json` pairs `ryukyu.md` with fixer scratch `.scratch/r17c10/ryukyu-sweep-2026-10-18.tsv` (this seat's sweep, §3), and pairs `polynesia-navigation.md` with `.scratch/r17c07/…` (C07, whose working-tree edit was already present; this seat wrote zero bytes to polynesia-navigation.md). Both readings recorded so a verifier can check identity without trusting either alone.

Identity legs, all re-run 2026-10-18:

```
sha256sum corpus/knowledge/civilizations/ryukyu.md
→ de541d332cced7aef0a14e28469be15389e93008af7153930e9de4ac21d88883   (before the §6 edit)
```

(a) equals round-16 C07's filed `sha256_16` `de541d332cced7ae` (`reports/round-16/civ/072-083.md` machine rows, idx 81); (b) equals round-9 V05's post-edit digest `ryukyu de541d332cced7ae` (`reports/round-9/metadata/v05-civ-77-94.md:50`); (c) round-16 map row: `{"file":"ryukyu.md","status":"stale-documented",…,"reason":"no dated URL-status receipt exists for its 94 distinct cited URLs (r16 C07 negative sweep); freshness pause defers the sweep — not evidence of breakage"}` (`reports/round-16/civ-map.json`). The byte chain closes on the round-16 map's bytes.

Recorded defect (carried, not repaired here): that per-entry reason text says "its 94 distinct cited URLs" — 94 is the *7-entry total*, not ryukyu's count; ryukyu's own inventory is **12** distinct cited URLs (`reports/round-16/civ/072-083.md:98`). The same wording is on all 7 never-swept rows. Map row text is round-16 filed bytes; this fragment does not rewrite them.

## 1. Round-16 reason trail (kept)

- Round-16 map row (above): stale-documented, reason "no dated URL-status receipt exists…".
- Shard basis: `reports/round-16/civ/072-083.md:96-106` — the negative sweep and its characterization: "**None contains a per-URL status for any of the 7 entries.** The sweep command and date are recorded here; the finding is point-in-time"; and `:104`: "`stale-documented` asserts absence of a receipt (sweep above), **not** that any link is dead".
- Independent audit re-run: `reports/round-16/civ/map-audit.md:74-75` — "**C07's seven rows**: negative claim … tested by me against rounds 5–15 … **Negative claim survives.**"
- Round-16 ran zero live fetches for these rows under the freshness pause (`reports/round-16/civ/072-083.md:107`: "no URL was fetched this round"). Round 17 claim C asks for exactly this missing receipt; §3 supplies it.

## 2. Negative claim, with its sweep

Claim: no dated per-URL status receipt for any of `ryukyu.md`'s 12 distinct cited URLs existed in filed rounds 5–15 before this round.

```
# 2026-10-18T09:24:59Z; input .scratch/r17c10/ryukyu-urls.txt (12 URLs, extracted below)
while read -r u; do grep -rl "$u" reports/round-5 reports/round-6 reports/round-7 reports/round-8 \
  reports/round-9 reports/round-10 reports/round-11 reports/round-12 reports/round-13 reports/round-14 \
  reports/round-15 2>/dev/null; done < .scratch/r17c10/ryukyu-urls.txt
→ 12/12 lines: NONE      (full output .scratch/r17c10/negative-sweep-2026-10-18.txt)
```

URL inventory command (same rule as the C07 shard, `grep -o 'https\?://…' | sort -u | wc -l`):

```
grep -o 'https\?://[^ )>`"]*' corpus/knowledge/civilizations/ryukyu.md | sort -u > .scratch/r17c10/ryukyu-urls.txt
wc -l < .scratch/r17c10/ryukyu-urls.txt → 12          (reproduces the C07 shard's count for idx 81)
```

No hit is a status receipt: the entry's `- source:` line points at the round-9 metadata re-audit (`v05-civ-77-94.md`), which is an apparatus audit, not a URL-status sweep (same characterization as `reports/round-16/civ/072-083.md:100-103`). Negative claim survives, re-established here with this seat's own command.

## 3. Live URL-status sweep (2026-10-18T09:16Z)

```
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'
cat .scratch/r17c10/ryukyu-urls.txt | xargs -P 8 -I{} bash -c \
  'curl -sSL -o /dev/null --max-time 30 -A "$UA" -w "%{http_code}\t%{num_redirects}\t%{url_effective}\t%{content_type}\t%{size_download}" "{}"'
→ .scratch/r17c10/ryukyu-sweep-2026-10-18.tsv
```

| # | cited URL (as in the entry) | code | hops | final URL | type | bytes |
|---|---|---|---|---|---|---|
| 1 | artscape.jp/artscape/eng/focus/2208_01.html | 200 | 0 | same | text/html | 23993 |
| 2 | doi.org/10.18874/jjrs.30.3-4.2003.339-359 | 200 | 3 | nirc.nanzan-u.ac.jp/journal/6/issue/167/article/1127 | text/html | 7607 |
| 3 | kyotoreview.org/issue-3-nations-and-stories/the-rekidai-hoan-documents-of-the-ryukyu-kingdom/ | 200 | 0 | same | text/html | 183135 |
| 4 | lingdy.aa-ken.jp/…/2015-papers-and-presentations-An_introduction_to_Ryukyuan_languages.pdf | 200 | 0 | same | application/pdf | 1679959 |
| 5 | mmsrv.ninjal.ac.jp/okinawago/ | 200 | 0 | same | text/html | 6544 |
| 6 | mmsrv.ninjal.ac.jp/okinawago/okinawa_01.xlsx | 200 | 0 | same | …spreadsheetml.sheet | 1417613 |
| 7 | okimu.jp/exhibition/Bashofu2024/ | 200 | 0 | same | text/html | 33895 |
| 8 | uhpress.hawaii.edu/title/maritime-ryukyu-1050-1650/ | 200 | 0 | same | text/html | 143867 |
| 9 | library.pref.okinawa.jp/about-okinawa/docs/annai6.pdf | 200 | 0 | same | application/pdf | 187658 |
| 10 | library.pref.okinawa.jp/archive/contents/cat38/knowledge.html | 200 | 0 | same | text/html | 33346 |
| 11 | mdpi.com/2077-1444/10/5/298 | **403** | 0 | same | text/html | 398 |
| 12 | pref.okinawa.lg.jp/_res/…/web_rekidaihoan_english_1.pdf | 200 | 0 | same | application/pdf | 4752224 |

Tally: **11 × HTTP 200, 1 × 403, 0 × 404/000, 0 non-DOI redirect migrations** (the one multi-hop final URL is the DOI resolver, item 2, which is normal DOI behaviour and is recorded, not a host migration). Cross-check, not a substitute for the table above: the independent verifier seat R17-V03/V04 swept the same 12 URLs the same day and reports `ryukyu.md n=12 live=11 blocked=1 hard_fail=0` (`.scratch/r17-v34/independent-sweep.json`), with per-URL agreement 12/12 against this seat's TSV (`.scratch/r17-v34/compare.json`).

## 4. Content verification, and the `sed -n '78p'` probe (assigned technique)

Method: each URL GET to a body file (`.scratch/r17c10/ryukyu-docs/01…12.*`), then `sed -n '78p'` on the raw body; for PDFs on `pdftotext -layout` text; for the XLSX on its `xl/sharedStrings.xml` text. Probe output verbatim (`.scratch/r17c10/probe-78-2026-10-18.txt`); keyword counts are the supporting content evidence, because line 78 of a raw HTML body can land on boilerplate.

| # | doc kind (lines) | line 78, verbatim (truncated) | title / keyword receipt (counts) |
|---|---|---|---|
| 1 | raw (726) | *(blank)* | title "A Tribute to the Spirit of Okinawa: Bashofu at the Okura Museum of Art"; Bashofu 24, Okura 13 — matches the entry's C row |
| 2 | raw (109) | `class="text-base"> Nanzan University </a>` (markup) | title "NIRC"; Wacker 2, Onarigami 4 on the raw page; DOI route lands on the JJRS article path (journal 6 / issue 167 / article 1127) cited in the W row |
| 3 | raw (963) | `/*# sourceURL=jetpack-stats-inline-css */` (markup) | title "The Rekidai Hoan: Documents of the Ryukyu Kingdom - Kyoto Review of Southeast Asia"; Rekidai 62, Hoan 63 |
| 4 | pdf-text (10234) | `2.1    Segmentation . . . . . . . . . . . . . . . . . . . . . . . . . . .          37` (ToC line) | first page "An Introduction to Ryukyuan Languages / edited by Michinori Shimoji & Thomas Pellard"; Ryukyuan 359 — matches the L row |
| 5 | raw (159) | `</tr>` (markup) | title "沖縄語辞典"; 沖縄語辞典 9, 首里 1 — matches the D row |
| 6 | sheet-text (4) | *(no line 78 — 4-line XML)* | sharedStrings: 74,733 strings / 30,325 unique; 首里 235; sample glosses `料理の名。ゆでたねぎで魚肉を巻き…`, `biree`, `付き合い。また,仕えること。<hwiree…dusibiree…` — a Shuri-dialect dictionary dataset, as the D row states |
| 7 | raw (677) | `<li class="pull_wrap">` (markup) | title "芭蕉布展 \| 展覧会 \| 沖縄県立博物館・美術館（おきみゅー）"; 芭蕉布 39, bashofu 13 — matches the T row |
| 8 | raw (916) | `<link rel='stylesheet' id='font-awesome.min-css' …>` (markup) | title "Maritime Ryukyu, 1050–1650 – UH Press"; Maritime 35, Ryukyu 63 — matches the H row |
| 9 | pdf-text (104) | `『日本列島の言語』（言語学大事典セレクション）（亀井 孝[ほか]編著、三省堂、1997）      【k80/N77】` (bibliography line) | first page "沖縄県立図書館 調べ方案内No.６ … １．『おもろさうし』とは"; おもろさうし 38 — matches the O row |
| 10 | raw (212) | `<p>沖縄の染織には古来から伝わる染め、織りがあり、他国との交易、文化的交流の中で多種多様に発展していった。…</p>` (substantive) | title "基礎知識 - 沖縄県立図書館 貴重資料デジタル書庫"; 染織 9, 紅型 24 — matches the X row |
| 11 | raw (11) | *(none — 398-byte 403 challenge body; no content served to this agent)* | **second agent**: full article text retrieved; its line 78 reads "This is not merely an academic debate, however. In contemporary Okinawa, local worship traditions are often referred to as 'Ryukyu Shinto'…"; utaki 153, sacred grove 20, Okinawa 154 — matches the R row (Rots 2019, *Religions* 10(5):298) |
| 12 | pdf-text (699) | `of communications between Ryūkyū and … of future diplomatic correspondence, and as a means of reference to past trends in foreign affairs.` (substantive) | first page "An Introduction to The Rekidai Hōan Documents of the Kingdom of Ryukyu / Revised Edition / Okinawa Prefectural Board of Education"; Rekidai 38, Hōan 38 — matches the RH row |

Honest reading of the technique: line 78 lands on substantive text for documents 4, 9, 10, 11 (second agent), 12 and on markup/blank for 1, 2, 3, 5, 6, 7, 8. Where it is not substantive, the dated keyword counts and titles carry the content check; the technique's yield is reported exactly, not dressed up.

Access attempt on the non-live outcome (item 11, 403 to this agent's curl): a second, independent agent (the session fetch tool, 2026-10-18T09:20Z) retrieved the full article text (CC BY, per the retrieved page footer: "© 2019 by the author. Licensee MDPI, Basel, Switzerland. This article is an open access article…"), so the 403 is a bot wall, not rot — same classification rule the lane already uses for 403/429 (`reports/round-16/civ/060-071.md`, C06). Named fallback, not written into the entry: Wayback closest snapshot `http://web.archive.org/web/20261006134243/https://www.mdpi.com/2077-1444/10/5/298` (availability API 2026-10-18: `status 200, available true`).

## 5. Disposition — stale-fixed, locators unchanged

- **old → new: unchanged; 0 of 12 locators replaced.** No cited URL is dead: 11 answer HTTP 200 and the single 403 is a bot wall whose article content was verified through a second agent. Replacing live, content-verified locators would be churn (same disposition rule as `reports/round-17/civ/mongol.md` §4).
- The round-16 stale reason ("no dated URL-status receipt exists") is retired by the dated receipt in §2–§4; the entry's `verified-at` line keeps the round-16 reason trail and adds the round-17 pointer (§6).
- **Limits:** presence/status-level verification only — the cited works are served at the locators with matching titles and keyword receipts; no passage-level scholarly re-inspection, no content-accuracy or canon claim. Counts and statuses are point-in-time 2026-10-18 during a parallel wave; a one-day sweep cannot rule out intermittent failure, and the 403 may lift or harden. Not a freshness axis-move (see header). This seat did not touch any other entry; `polynesia-navigation.md`, `persia-sasanian.md`, `rapa-nui.md`, `rome.md`, `scythian-saka.md`, `siam-thai.md` belong to sibling seats (§0).

## 6. Entry edit (the only corpus write)

File `corpus/knowledge/civilizations/ryukyu.md`, `verified-at` line (line 6), diff `1 insertion / 1 deletion` (`git diff --numstat -- corpus/knowledge/civilizations/ryukyu.md` → `1	1`); distinct URL count unchanged (12, re-counted after the edit).

before:

```
- verified-at: 2026-10-17; passages and institutional pages checked as identified below, not a claim to have read every listed monograph in full.
```

after:

```
- verified-at: 2026-10-17; passages and institutional pages checked as identified below, not a claim to have read every listed monograph in full. Round-17 C-fix (2026-10-18) retires the round-16 stale reason (no dated URL-status receipt existed; reports/round-16/civ/072-083.md §3, reports/round-16/civ-map.json): all 12 distinct cited URLs status-checked live — 11× HTTP 200, 1× 403 bot-wall (MDPI, article content re-verified through a second agent; archive fallback named), 0× 404/000, no non-DOI locator redirect migration, no locator replaced; receipt reports/round-17/civ/sed78.md; status/locator receipt only, not a source-freshness verdict (freshness pause, LOG.md:3028).
```

sha256 before `de541d332cced7aef0a14e28469be15389e93008af7153930e9de4ac21d88883` → after `424fcbb5de9f4d226039c7472f92372784801a128f62ee6024a71e590819afa5` (`sha256sum corpus/knowledge/civilizations/ryukyu.md`, 2026-10-18T09:26:53Z).

## 7. Map-scribe input

```json
{
  "file": "ryukyu.md",
  "path": "corpus/knowledge/civilizations/ryukyu.md",
  "map_idx": 81,
  "status": "stale-fixed",
  "verified_at": "2026-10-18",
  "old_url": "n/a (no locator replaced)",
  "new_url": "n/a (no locator replaced)",
  "old_to_new": "unchanged 12/12 — 11×200, 1×403 bot-wall (content verified via a second agent), 0×404/000, 0 non-DOI redirect migrations",
  "sha256_before": "de541d332cced7aef0a14e28469be15389e93008af7153930e9de4ac21d88883",
  "sha256_after": "424fcbb5de9f4d226039c7472f92372784801a128f62ee6024a71e590819afa5",
  "distinct_urls": 12,
  "reason": "round-16 stale reason (no dated URL-status receipt for the entry's cited URLs) retired by a dated live sweep 2026-10-18: .scratch/r17c10/ryukyu-sweep-2026-10-18.tsv; per-URL content receipts (titles, keyword counts, sed -n '78p' probes) in reports/round-17/civ/sed78.md; entry verified-at line keeps the round-16 reason trail and adds the round-17 receipt pointer",
  "evidence": ["reports/round-17/civ/sed78.md"],
  "reason_trail": ["reports/round-16/civ-map.json", "reports/round-16/civ/072-083.md", "reports/round-16/civ/map-audit.md", "reports/round-9/metadata/v05-civ-77-94.md"],
  "fallback_named": "http://web.archive.org/web/20261006134243/https://www.mdpi.com/2077-1444/10/5/298 (status 200, availability API 2026-10-18)",
  "limits": "status/presence-level verification; 12/12 URLs swept once; the 403 is a bot wall (two agents); no freshness verdict; point-in-time",
  "map_reason_text_defect": "the round-16 per-entry reason says 'its 94 distinct cited URLs' — 94 is the 7-entry total; ryukyu's own count is 12"
}
```

## 8. Commands run by this seat (all 2026-10-18, UTC)

- Identity/digest: `sha256sum corpus/knowledge/civilizations/ryukyu.md`; `git diff --numstat -- corpus/knowledge/civilizations/ryukyu.md`; `ls corpus/knowledge/civilizations/*.md | LC_ALL=C sort | sed -n '77,83p'`.
- Inventory: `grep -o 'https\?://[^ )>`"]*' corpus/knowledge/civilizations/ryukyu.md | sort -u | wc -l` → 12.
- Negative sweep: `grep -rl <url> reports/round-5 … reports/round-15` × 12 → all NONE (`.scratch/r17c10/negative-sweep-2026-10-18.txt`).
- Sweep: `curl -sSL -o /dev/null --max-time 30 -A <UA> -w '%{http_code}\t%{num_redirects}\t%{url_effective}\t%{content_type}\t%{size_download}' <url>` × 12, `xargs -P 8` (`.scratch/r17c10/ryukyu-sweep-2026-10-18.tsv`).
- Bodies: `curl -sSL --max-time 60 -A <UA> <url> -o .scratch/r17c10/ryukyu-docs/<nn>.<ext>` × 12.
- Probes: `sed -n '78p'` on raw body / `pdftotext -layout` text / `xl/sharedStrings.xml` text (`.scratch/r17c10/probe-78-2026-10-18.txt`); keyword counts `grep -o -i <kw> | wc -l`.
- Second agent: session fetch tool on `https://www.mdpi.com/2077-1444/10/5/298` (full article text; copy `.scratch/r17c10/ryukyu-docs/11-mdpi-fetchurl.txt`); Wayback availability API for the named fallback.
- No command was taken from an evidence file; no corpus file other than `ryukyu.md` was written.

— C R17-C10, 2026-10-18. All artifacts NON-CANON.
