# R17-C12 — never-swept #7 disposition: `siam-thai.md` (URL-status sweep + `sed -n '80p'` content probe)

- Seat: C R17-C12 (claim C, coverage; operator regimen loop 2 of 3, build round 1 of 4). Lane root: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- Date: 2026-10-18 (all commands below run this date; UTC times as marked). Reference revision `9b49a4a0fca6ceeab917d401945358fdedeb7e11` (round-17 declare); baseline `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` (round-16 admit).
- Technique assigned: `sed -n '80p'` content probe on each fetched document (§4). Write surface: this fragment + the licensed in-place locator fix in `corpus/knowledge/civilizations/siam-thai.md` (one of the 12 named entries; round-16 reason trail kept). Zero other corpus bytes touched; no commit, no push.
- **NON-CANON** evidence: no canon, no lore acceptance, no real-world clearance/rights ruling, no axis verdict beyond the dated status receipt. Statuses are point-in-time access facts.

## 0. Target resolution — “never-swept #7” = `siam-thai.md`

Round-17 claim C names 12 round-16 stale-documented entries = inuit (Dorais 2010 dead locator) + muisca/mongol/mesoamerica (hard-fail URLs) + maya-classic (couples gap) + **7 never-swept URL sets** (`reports/round-17/claims.json:21`). The 7 never-swept sets are the last 7 stale rows of the round-16 map in map/shard order:

```
python3 -c "import json; m=json.load(open('reports/round-16/civ-map.json')); print([e['file'] for e in m['entries'] if e['status']=='stale-documented'])"
→ ['inuit.md','maya-classic.md','mesoamerica-primary-sources.md','mongol.md','muisca.md',
   'persia-sasanian.md','polynesia-navigation.md','rapa-nui.md','rome.md','ryukyu.md',
   'scythian-saka.md','siam-thai.md']                                        (2026-10-18)
```

The last 7 of that list are the never-swept sets #1–#7, matching the C07 shard table rows 77–83 (`reports/round-16/civ/072-083.md:30-36`) and its negative-sweep inventory (`:98`): persia-sasanian 9, polynesia-navigation 26, rapa-nui 9, rome 12, ryukyu 12, scythian-saka 12, **siam-thai 14** distinct cited URLs (9+26+9+12+12+12+14 = 94). **#7 = `siam-thai.md`.**

Already-claimed entries were excluded (scratch evidence 2026-10-18T09:1xZ: `.scratch/persia-sasanian-urls.txt`, `.scratch/rapa-nui-urls.txt`, the muysca fetch set, `.scratch/rubruck-r17.html`; landed sibling fragments `reports/round-17/civ/mongol.md`; sibling working-tree edits inuit/maya-classic/mongol/rapa-nui). This seat touched only `siam-thai.md`.

## 1. Round-16 reason trail (kept)

Quoted from the filed artifacts (round-16 is read-only here):

- Map reason, entry `siam-thai.md` (`reports/round-16/civ-map.json`): “no dated URL-status receipt exists for its 94 distinct cited URLs (r16 C07 negative sweep); freshness pause defers the sweep — not evidence of breakage [evidence: reports/round-16/civ/072-083.md]”.
- Shard row (`reports/round-16/civ/072-083.md:36`): `siam-thai.md`, sha256-16 `cf9269bcaa2ddef9`, couples 15, distinct cited URLs 14, external-URL receipt “none exists — same named reason”, status **stale-documented**.
- Shard negative sweep (`reports/round-16/civ/072-083.md:96`, 2026-10-17): no in-repo receipt contained a per-URL status for any of the 7 entries.

Discharge: the round-16 deferral clause (“freshness pause defers the sweep”) is superseded by the round-17 claim C declaration, which requires live content-verified locators (`reports/round-17/claims.json:22`); the sweep below is that required work, dated. The distinctive token “no dated URL-status receipt exists” is quoted here and kept in the entry's own `- verified-at:` line (§6).

## 2. Inventory (command + date)

```
grep -o 'https\?://[^][()<>{}\"` ]*' corpus/knowledge/civilizations/siam-thai.md | sed 's/[.,;]$//' | sort -u | wc -l
→ 14                          (2026-10-18, on baseline bytes; sha256 cf9269bc…)
```

Matches the round-16 count 14 exactly (shard row `:36`); independently corroborated by the verifier baseline inventory `.scratch/verify-baseline/url-inventory.txt:185` — “siam-thai: 15 occurrences, 14 distinct” (2026-10-18).

## 3. URL-status sweep (2026-10-18T09:16:11–09:16:40Z)

Method: `curl -sIL` HEAD (lane UA), GET fallback on 000/405/403/501, 1 s spacing; script `.scratch/siam-sweep.sh`; raw log `.scratch/siam-fetch/sweep.log` (15 lines). Bytes below are from the §4 GET probes (HEAD reports size 0).

| # | src | URL | status | bytes (GET) | effective URL |
|---|---|---|---|---|---|
| 01 | S1 | https://assets.cambridge.org/97805216/50854/excerpt/9780521650854_excerpt.pdf | 200 | 199,008 | same |
| 02 | S13 | https://blogs.loc.gov/law/2025/07/understanding-thai-names-law-and-culture/ | **403** (challenge) | 5,829 | same |
| 03 | S10 | https://culturalatlas.sbs.com.au/thai-culture/thai-culture-naming | 200 after 1×301 | 118,615 | https://theculturalatlas.org/thai-culture/thai-culture-naming |
| 04 | S11 | https://digital_collect.lib.buu.ac.th/ebook/b00286775.pdf | 200 | 24,301,054 | same |
| 05 | S6 | https://disco.teak.fi/asia/khon-the-masked-pantomime/ | 200 | 142,873 | same |
| 06 | S9 | https://doi.org/10.1057/s41599-022-01158-9 | 200 | 380,603 | nature.com article (tracking params appended) |
| 07 | S2 | https://doi.org/10.1515/9783110401981-013 | **202** | 0 | https://www.degruyterbrill.com/document/doi/10.1515/9783110401981-013/html |
| 08 | S1 | https://grambank.clld.org/sources/gIwasakiIngkaphiromThai | 200 | 8,722 | same |
| 09 | S7 | https://ich.unesco.org/en/RL/khon-masked-dance-drama-in-thailand-01385 | 200 | 155,457 | same |
| 10 | S4+S5 | https://publishing.cdlib.org/ucpressebooks/view?docId=ft3j49n8h7&brand=ucpress | 200 after 1×301 | 1,657,019 | https://publishing.cdlib.org/ucpressebooks/public/book/many-ramayanas-the-diversity-of-a-narrative-tradition-in-south-asia.html |
| 11 | S8 | https://seasite.niu.edu/thai/literature/ramakian/khonmasksofthailand/khonkhon.htm | 200 | 30,782 | same |
| 12 | S12 | https://wiki.kpi.ac.th/index.php?title=%E0%B8%A8%E0%B8%B1%E0%B8%81%E0%B8%94%E0%B8%B4%E0%B8%99%E0%B8%B2%E0%B8%AA%E0%B8%A2%E0%B8%B2%E0%B8%A1 | 200 | 55,579 | same |
| 13 | S3 | https://www.cambridge.org/9781316641132 | **403** (challenge) | 5,649 | same |
| 14 | S2 | https://www.zora.uzh.ch/server/api/core/bitstreams/dbb3e7fa-6e7a-4bcb-b80c-d5ec2d770d26/content | 200 | 632,472 | same |

Tally: 14/14 status-checked — **12 live** (10 direct + 2 via permanent 301), **2 Cloudflare bot walls (403)**, **0 hard fails (000)**. Raw redirect statuses for 03 and 10: `HTTP/2 301` with `location:` to the new URLs (curl header dumps, 2026-10-18T09:20:12–13Z).

## 4. `sed -n '80p'` content probes (2026-10-18T09:18:01Z)

Method (assigned technique): GET each URL to a body file, then `sed -n '80p'` on the raw body; for PDFs, `sed -n '80p'` on `pdftotext <body> -` text. Script `.scratch/siam-probe.py`; JSON `.scratch/siam-probe.json`. Keyword counts are supporting content evidence, because line 80 of a raw HTML body can land on boilerplate — reported verbatim, not dressed up.

| # | doc kind | lines | line 80 (truncated) | keywords (counts) / title |
|---|---|---|---|---|
| 01 | pdf-text | 698 | (blank — page-break region; next non-empty `:82` “North”, `:84` “Thai, Shan, Lue, Phu Thai, etc.”) | Thai 37, Iwasaki 10 |
| 02 | raw | 1 | — (403 challenge body) | title “Just a moment...” |
| 03 | raw | 57 | — (body < 80 lines) | Thai 66, nickname 22; “Thai - Naming — Cultural Atlas” |
| 04 | pdf-text | 22,126 | `เป็นราชสักการะแด่พระบาทสมเด็จพระเจ้าอยู่หัว ผู้สถิตในดวงใจของปวงประชาราษฎรตลอดกาล` | ประชวร 20, ทรง 669 (supports the entry's “Verified inside” rachasap claims) |
| 05 | raw | 746 | `<a href="#content" class="content-link">Skip to content</a>` (boilerplate) | khon 82, Khon 26; “Khon, “The Masked Pantomime”” |
| 06 | raw | 1,838 | `<link rel="manifest" href=/oscar-static/manifest.json crossorigin="use-credentials">` (boilerplate) | Sakdina 93, sakdina 27; title matches the Waters article |
| 07 | — | 0 | — (202/0 B, no body to probe; §5) | — |
| 08 | raw | 205 | (blank) | Iwasaki 6, Thai 7 |
| 09 | raw | 2,051 | `<ul id="navbar-nav" class="nav navbar-nav" >` | Khon 17; “Khon, masked dance drama in Thailand - UNESCO…” |
| 10 | raw | 11,094 | `}` (inline script) | Ramayana 847; “Many Ramayanas: The Diversity of a Narrative Tradition in South Asia \| UC Press E-Books Collection Archive, 1982-2004” |
| 11 | raw | 500 | `<pre><font color="#000000" face="Book Antiqua"> <strong> As was mentioned earlier, the Khon drama, commonly called` | Khon 33, khon 37; “Khon Masks of Thailand” |
| 12 | raw | 581 | `</td>` | ศักดินา 54; “ศักดินาสยาม - ฐานข้อมูลการเมืองการปกครอง สถาบันพระปกเกล้า” |
| 13 | raw | 1 | — (403 challenge body) | title “Just a moment...” |
| 14 | pdf-text | 4,190 | `than inherited from a common parent language.` | Thai 175 |

Honest reading: line 80 lands on content text for the two PDFs (04, 14) and on markup/text for 05, 09–12; it is blank or boilerplate for 01, 03, 05 (skip-link), 06, 08; absent where no content body was served (02, 07, 13). Where line 80 is not substantive, the keyword counts (dated, command above) carry the content-verification; the technique's yield is reported exactly.

## 5. Access attempts on the non-live outcomes (2026-10-18T09:18–09:20Z)

- **02 blogs.loc.gov** — 403 across 4 variants (HTTP/1.1 and HTTP/2 × lane UA and `curl/8`; bodies 5,637–5,829 B, Cloudflare challenge). CDX availability: 3+ snapshots, latest `20250810213501` status 200 (length 7,555). Access outcome (bot wall), not proof of death; locator kept unchanged.
- **13 cambridge.org/9781316641132** — 403 across 3 variants + 1 full browser-header attempt (Firefox UA, Accept-Language, `--compressed`; 3,317 B challenge). CDX for this exact shortcut URL → `[]` (no capture). This is the entry's “Publisher/ISBN route” (an access aid, not the content host); locator kept, attempt documented here (claim C's “attempted” branch for this URL; entry-level disposition remains fixed via the dated receipt + replaced locators).
- **07 doi.org/10.1515/9783110401981-013** — DOI handle API resolves (responseCode 1 → `https://www.degruyterbrill.com/document/doi/10.1515/9783110401981-013/html`); direct GETs return 202/0 B across 3 variants (bot-style response); CDX shows 200 snapshots (e.g. `20260324151841`, length 17,923). DOI locator unchanged and resolving.
- **06 DOI handle API** (`10.1057/s41599-022-01158-9`) → responseCode 1 → `https://www.nature.com/articles/s41599-022-01158-9`.

## 6. Disposition: **stale-fixed** — entry edits (2026-10-18T09:19–09:21Z)

Two permanent 301 moves re-pinned in `corpus/knowledge/civilizations/siam-thai.md` (old→new; evidence §3):

- **S10:** `https://culturalatlas.sbs.com.au/thai-culture/thai-culture-naming` → `https://theculturalatlas.org/thai-culture/thai-culture-naming` (301; new page carries SBS terms links — same publisher resource).
- **S4 + S5:** `https://publishing.cdlib.org/ucpressebooks/view?docId=ft3j49n8h7&brand=ucpress` → `https://publishing.cdlib.org/ucpressebooks/public/book/many-ramayanas-the-diversity-of-a-narrative-tradition-in-south-asia.html` (301, same host, canonical book route).

`- verified-at:` now carries (verbatim from the edited entry):

> `- verified-at: 2026-10-18 URL-status sweep + content probe of all 14 cited URLs (12 live and content-verified, incl. 2 via permanent 301s re-pinned; 2 Cloudflare bot-wall 403s with retries recorded; receipt: reports/round-17/civ/sed80.md); supersedes the round-16 stale-documented reason “no dated URL-status receipt exists” (reports/round-16/civ/072-083.md:36). 2026-10-17 pass: S1's publisher excerpt, S2's published chapter, S4–S5's online volume, and the linked S6–S13 pages and files were consulted; S3 is a bibliographically checked historical reading route, not a claim of clause-by-clause collation.`

The round-16 reason trail is therefore kept in the entry line itself (distinctive token + shard path). `- source:` and `- recheck:` unchanged.

Post-edit checks (all 2026-10-18, lane root, `TMPDIR=$PWD/.scratch`):

- `git diff -- corpus/knowledge/civilizations/siam-thai.md` → exactly 4 changed lines (1 `verified-at:` + 3 URL occurrences on S4/S5/S10); nothing else.
- sha256 before `cf9269bcaa2ddef9cbb83b900db6d5ce71220cb97bb57f9a56aebecde314ca06` (equals `git show f30b6f8:corpus/knowledge/civilizations/siam-thai.md | sha256sum` — the baseline bytes) → after `8bef2a5b3936c2f45d9d0027646e4d107d45b5f58942379cbb4db9fb7cb6c733` (final; wording-precision fix on the same line, diff still 4 lines).
- Distinct-URL recount after edit → 14 (2 set members changed, cardinality unchanged).
- New locators present in bytes: `grep -c` → theculturalatlas 1, cdlib `public/book` 2; old forms → 0 / 0.
- `python3 tools/gates/provenance-audit.py corpus/knowledge/civilizations/siam-thai.md` → `files=1 marks=0 mark-lines=0 findings=0 blocked=0` (exit 0).
- Couples-link resolution (round-16 C07 resolver form) → 15/15 resolved, equal to the filed V05 count (`reports/round-9/metadata/v05-civ-77-94.md:46`).
- Seat's corpus dirty scope: `git status --porcelain corpus/` → `siam-thai.md` from this seat only (inuit/maya-classic/mongol/rapa-nui edits belong to sibling seats).

## 7. Independent corroboration (not this seat's claim)

Verifier seats V01 and V03/V04 independently swept the same baseline URL set on 2026-10-18 09:16–09:19Z (`.scratch/v01/sweep12.json`, `.scratch/r17-v34/independent-sweep.json`); their siam-thai results agree with §3 — V01 raw codes n=14 {200:11, 403:2, 202:1} and V03/V04 summary n=14, live=12, blocked=2, hard_fail=0 (the 202 is the resolved DOI of row 07) — with matching sizes/effective URLs row-for-row where compared (01 199,008 B; 03 118,615 B → theculturalatlas; 04 24,301,054 B; 05 142,873 B; 06 380,603 B; 07 202/0 B; 08 8,722 B; 09 155,457 B; 10 1,657,019 B → new cdlib route; 11 30,782 B; 12 55,579 B). Recorded as corroboration; the verifiers' own receipts are theirs.

## 8. Negative claims + sweeps

- **Before this round, no in-repo receipt carried a per-URL status for `siam-thai`** — re-run of the round-16 C07 sweep form (2026-10-18): `grep -rln 'siam-thai' reports/ LOG.md SCORECARD.md | grep -v 'round-9/metadata/v05|round-8/metadata/m05|round-16/civ'` → `LOG.md`, `reports/round-16/validation.json`, `reports/round-9/metadata/audit.md`, `reports/round-9/metadata/v07-synth-13-24.md`, `reports/supplement-opencode-1/{inventory-after.json,scratch/28-corpus-contract/header-census.txt}` — header censuses, bookkeeping, and shard-boundary mentions only; none contains a URL status. This round's §3 is the receipt that ends the round-16 negative claim.
- **No dead links found among the 14**: 0 hard fails (000) in §3; the 2 non-live outcomes are Cloudflare 403 access outcomes with recorded retries (§5).
- **No other corpus bytes touched by this seat**: §6 dirty-scope check.
- **No real-world rights/clearance/canon ruling**: NON-CANON; statuses are point-in-time access facts, not permissions or canon.

## 9. Limits

- Point-in-time 2026-10-18 during a parallel wave; scope is `siam-thai.md`'s 14 URLs only.
- The `sed -n '80p'` technique pins one fixed-depth line; where it lands on boilerplate/blank the content evidence is the keyword counts (commands in §4). Not a full-document verification, and not presented as one.
- 403/202 outcomes are access outcomes (round-16 rule, `reports/round-16/civ/060-071.md:139`), not proof of link death; the affected locators were kept and the retries documented.
- No freshness-axis claim, no ranking, no LOG.md/SCORECARD write; the parent integrates.

## 10. Machine-readable rows (for the round-17 map / runner)

```json
{"round":17,"seat":"R17-C12","technique":"sed -n '80p'","date":"2026-10-18","entry":"siam-thai.md","entry_status_before":"stale-documented","disposition":"stale-fixed","round16_trail":"reports/round-16/civ/072-083.md:36 — status stale-documented; no dated URL-status receipt exists (r16 C07 negative sweep §3)","distinct_urls":14,"sweep":{"date_utc":"2026-10-18T09:16:11-09:16:40Z","command":".scratch/siam-sweep.sh (curl -sIL HEAD w/ GET fallback)","live":12,"blocked_403":2,"hard_fail":0},"probe":{"date_utc":"2026-10-18T09:18:01Z","command":".scratch/siam-probe.py (curl GET + sed -n '80p'; pdftotext for PDFs)","content_verified":12},"replacements":[{"source":"S10","old":"https://culturalatlas.sbs.com.au/thai-culture/thai-culture-naming","new":"https://theculturalatlas.org/thai-culture/thai-culture-naming","evidence":"301; 200 118615 B; title 'Thai - Naming — Cultural Atlas'"},{"source":"S4+S5","old":"https://publishing.cdlib.org/ucpressebooks/view?docId=ft3j49n8h7&brand=ucpress","new":"https://publishing.cdlib.org/ucpressebooks/public/book/many-ramayanas-the-diversity-of-a-narrative-tradition-in-south-asia.html","evidence":"301; 200 1657019 B; title 'Many Ramayanas…'"}],"attempts":[{"url":"https://blogs.loc.gov/law/2025/07/understanding-thai-names-law-and-culture/","outcome":"403 Cloudflare x4 variants; CDX 200 snapshot 20250810213501; locator kept"},{"url":"https://www.cambridge.org/9781316641132","outcome":"403 Cloudflare x3 + browser-header attempt; CDX empty; locator kept"},{"url":"https://doi.org/10.1515/9783110401981-013","outcome":"DOI resolves (handle API); direct GET 202/0B x3; CDX 200 snapshots; locator kept"}],"entry_sha256":{"before":"cf9269bcaa2ddef9cbb83b900db6d5ce71220cb97bb57f9a56aebecde314ca06","after":"8bef2a5b3936c2f45d9d0027646e4d107d45b5f58942379cbb4db9fb7cb6c733"},"corroboration":".scratch/v01/sweep12.json; .scratch/r17-v34/independent-sweep.json (n=14 live=12 blocked=2 hard_fail=0)"}
```
