# R17-C11 — never-swept #6 disposition: `scythian-saka.md` (URL-status sweep + `sed -n '79p'` content probe)

- Seat: C R17-C11 (claim C, coverage; operator regimen loop 2 of 3, build round 1 of 4). Lane root: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- Date: 2026-10-18 (all commands below run this date; UTC times as marked). Reference revision `9b49a4a0fca6ceeab917d401945358fdedeb7e11` (round-17 declare); baseline `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` (round-16 admit, `reports/round-17/claims.json`).
- Technique assigned: `sed -n '79p'` content probe on each fetched document (§4). Write surface: this fragment + the licensed in-place edit in `corpus/knowledge/civilizations/scythian-saka.md` (one of the 12 named entries; `verified-at` line + one permanent-301 locator re-pin; round-16 reason trail kept). Zero other corpus bytes touched; no commit, no push; `TMPDIR=$PWD/.scratch` before every scratch-writing command.
- **NON-CANON** evidence: no canon, no lore acceptance, no real-world clearance/rights ruling, no axis verdict beyond the dated status receipt. Statuses are point-in-time access facts.

## 0. Target resolution — “never-swept #6” = `scythian-saka.md`

Round-17 claim C names 12 round-16 stale-documented entries = inuit (Dorais 2010 dead locator) + muisca/mongol/mesoamerica (hard-fail URLs) + maya-classic (couples gap) + **7 never-swept URL sets** (`reports/round-17/claims.json:21`). The 7 never-swept sets are the last 7 stale rows of the round-16 map in map/shard order:

```
python3 -c "import json; m=json.load(open('reports/round-16/civ-map.json')); print([e['file'] for e in m['entries'] if e['status']=='stale-documented'])"
→ ['inuit.md','maya-classic.md','mesoamerica-primary-sources.md','mongol.md','muisca.md',
   'persia-sasanian.md','polynesia-navigation.md','rapa-nui.md','rome.md','ryukyu.md',
   'scythian-saka.md','siam-thai.md']                                        (2026-10-18)
```

The last 7 of that list are the never-swept sets #1–#7, matching the C07 shard table rows 77–83 (`reports/round-16/civ/072-083.md:30-36`) and its negative-sweep inventory (`:98`): persia-sasanian 9, polynesia-navigation 26, rapa-nui 9, rome 12, ryukyu 12, **scythian-saka 12**, siam-thai 14 distinct cited URLs (9+26+9+12+12+12+14 = 94).

Ordinal cross-checks against sibling seats' own filed fragments (read 2026-10-18T09:2xZ, all under `reports/round-17/civ/`):

- `rapa-nui.md:3` — “never-swept #3 of the round-16 C07 seven” → #3 = `rapa-nui.md`.
- `sed80.md:1,19` — “never-swept #7 = `siam-thai.md`” → #7 = `siam-thai.md`.

Slice order 77→83 gives #1 persia-sasanian, #2 polynesia-navigation, #3 rapa-nui, #4 rome, #5 ryukyu, **#6 scythian-saka**, #7 siam-thai; both landed sibling ordinals agree. **This seat's target: `scythian-saka.md`** (row 82, 12 distinct cited URLs).

Assignment-locator note (kept for auditability): the seat text was “C R17-C11 (never-swept #6): sed -n '79p' file, excluding already-claimed ones”. A literal `sed -n '79p'` over the `LC_ALL=C`-sorted civ list lands on `rapa-nui.md` (entry 79), which was already claimed by C08 (`.scratch/rapa-nui-urls.txt`, landed fragment `reports/round-17/civ/rapa-nui.md`); the “excluding already-claimed ones” clause plus the #6 ordinal (validated by the two sibling fragments above) resolve the target to `scythian-saka.md`. The assigned depth 79 is executed as the content-probe technique on each fetched document (§4).

Already-claimed entries excluded, scratch/fragment evidence observed 2026-10-18T09:15–09:27Z: persia-sasanian (`.scratch/persia-sasanian-urls.txt`, fragment `persia-sasanian.md`), polynesia-navigation (`.scratch/r17c07/urls.txt`, `sed78.md`), rapa-nui (`.scratch/rapa-nui-urls.txt`, `rapa-nui.md`), rome (`.scratch/r17-c09/sweep.json` entry field, `sed77.md`), ryukyu (`.scratch/r17c10/ryukyu-urls.txt`), siam-thai (`.scratch/siam-thai-urls.txt`, `sed80.md`), plus the five non-never-swept fixers (inuit/muisca/mongol/mesoamerica/maya-classic). `scythian-saka` had no sibling claim; the URL-set intersection of this seat's 12 URLs against the six sibling fixer URL lists is **0** (python3 set intersection over the six lists, 2026-10-18).

## 1. Round-16 reason trail (kept)

Quoted from the filed artifacts (round-16 is read-only here):

- Map reason, entry `scythian-saka.md` (`reports/round-16/civ-map.json`): “no dated URL-status receipt exists for its 94 distinct cited URLs (r16 C07 negative sweep); freshness pause defers the sweep — not evidence of breakage [evidence: reports/round-16/civ/072-083.md]”.
- Shard row (`reports/round-16/civ/072-083.md:33`): `scythian-saka.md`, sha256-16 `aff3ca0aa3a31e47`, couples 14, distinct cited URLs 12, external-URL receipt “none exists — same named reason”, status **stale-documented**.
- Shard negative sweep (`reports/round-16/civ/072-083.md:96`, 2026-10-17): no in-repo receipt contained a per-URL status for any of the 7 entries; machine row `:124` carries `"url_receipt":null`.
- Independent reproduction of the negative: round-16 auditor (`reports/round-16/civ/map-audit.md:69`): “stale-documented = no dated URL-status receipt exists in-repo (absence, not breakage)”.

Discharge: the round-16 deferral clause (“freshness pause defers the sweep”) is superseded by the round-17 claim C declaration, which requires live content-verified locators (`reports/round-17/claims.json:22`); the sweep below is that required work, dated. The distinctive token “no dated URL-status receipt exists” is quoted here and kept in the entry's own `- verified-at:` line (§6).

## 2. Inventory (command + date)

```
grep -o 'https\?://[^ )"<>]*' corpus/knowledge/civilizations/scythian-saka.md | sort -u | wc -l
→ 12                          (2026-10-18, on baseline bytes; sha256 aff3ca0a…)
grep -n -o 'https\?://[^ )"<>]*' corpus/knowledge/civilizations/scythian-saka.md
→ 4 URLs on line 179 (Herodotus), 1 each on 180–184, 2 on 185, 1 on 186
```

Matches the round-16 count 12 exactly (shard row `:33`); independently corroborated by the verifier baseline inventory `.scratch/verify-baseline/url-inventory.txt` — “scythian-saka: 12 occurrences, 12 distinct” (2026-10-18). Pre-edit byte identity: `sha256sum` = `aff3ca0aa3a31e477a21a08d6aa94561a028466e55ec9202e3e6dd9572e95e00` (full), first 16 hex `aff3ca0aa3a31e47` = the round-16 shard value; `git status --porcelain -- corpus/knowledge/civilizations/scythian-saka.md` → empty before the edit; HEAD `9b49a4a` at open and close.

## 3. URL-status sweep (2026-10-18T09:22:29Z; script `.scratch/r17c11/sweep.py`; raw JSON `.scratch/r17c11/sweep-run1.json`; bodies `.scratch/r17c11/body/`)

Method: M04 method — `curl -sS -o <body> -w '%{http_code} %{url_effective} %{content_type} %{size_download} %{time_total}' -L --max-time 15 -A 'Mozilla/5.0 (compatible; kotodama-metadata-audit/1.0)'`, one retry on 000 (`reports/round-8/metadata/m04-civ-58-76.md` §2 step 2). All 12 URLs resolved on attempt 1; no retries fired.

| # | anchor (entry line) | URL | status | bytes | effective URL / note |
|---|---|---|---|---|---|
| 01 | Simpson–Pankova 2017, l.184 | https://ajaonline.org/online-museum-review/3680/ | 200 | 120,873 | same |
| 02 | Rudenko 1970, l.182 | https://books.google.com/books?vid=ISBN0520013956 | 200 | 121,684 | 302 geo-redirect → https://books.google.com.br/books?vid=ISBN0520013956&redir_esc=y |
| 03 | Rolle 1989, l.183 | https://books.google.com/books?vid=ISBN0520068645 | 200 | 112,822 | 302 geo-redirect → https://books.google.com.br/books?vid=ISBN0520068645&redir_esc=y |
| 04 | Issyk inscription, l.185 | https://en.wikipedia.org/wiki/Issyk_inscription | 200 | 92,359 | same |
| 05 | Ukok “Ice Maiden”, l.186 | https://en.wikipedia.org/wiki/Siberian_Ice_Maiden | 200 | 247,430 | same |
| 06 | Herodotus 4.5–10, l.179 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Herodotus/4A*.html | 200 | 42,727 | same (the `*` is a literal character in Thayer's filenames) |
| 07 | Herodotus 4.17–24, l.179 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Herodotus/4B*.html | 200 | 70,253 | same |
| 08 | Herodotus 4.52–80 incl. 4.70, l.179 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Herodotus/4C*.html | 200 | 76,005 | same |
| 09 | Herodotus 7.64, l.179 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Herodotus/7B*.html | 200 | 149,694 | same |
| 10 | Lubotsky 2002, l.180 | https://scholarlypublications.universiteitleiden.nl/access/item%3A2882853/view | 200 | 8,911 | **301 permanent** → https://scholarlypublications.universiteitleiden.nl/handle/1887/16379?rep=01&m=9940747172202711 (re-pinned, §6) |
| 11 | Issyk reading proposal, l.185 | https://www.academia.edu/104775728/ | **403** (challenge) | 5,469 | same; Cloudflare bot wall, §5 |
| 12 | Emmerick 2009 via Iranica, l.181 | https://www.iranicaonline.org/articles/khotan-parent/khotan-iv-khotanese-language/ | 200 | 498,050 | same |

Tally: 12/12 status-checked — **11 live** (9 direct + 1 via temporary 302 geo-redirect + 1 via permanent 301), **1 Cloudflare bot wall (403)**, **0 hard fails (000/404)**. Redirect statuses measured with `curl -sIL` header dumps (2026-10-18T09:23:3xZ): books.google.com → `HTTP/2 302` + `location: …books.google.com.br…`; Leiden access route → `HTTP/1.1 301 Moved Permanently` + `Location: …/handle/1887/16379?rep=01&m=…`; bare `https://scholarlypublications.universiteitleiden.nl/handle/1887/16379` → 200, 8,911 B (same bytes as the redirect target).

## 4. `sed -n '79p'` content probes (2026-10-18T09:22:3xZ)

Method (assigned technique): the GET bodies from §3 were probed with `sed -n '79p'`; keyword counts are supporting content evidence, because line 79 of a raw HTML body can land on markup. Reported verbatim, not dressed up.

| # | doc | lines | line 79 (truncated) | keywords (counts) / title |
|---|---|---|---|---|
| 01 | ajaonline review | 1,136 | `.wp-block-image>a,.wp-block-image>figure>a{display:inline-block}…` (CSS) | Scythians 50, Pankova 10, Simpson 11; og:description “The BP Exhibition: Scythians. Warriors of Ancient Siberia…” |
| 02 | books.google Rudenko | 1,698 | `/* #gbi4id - gaia bar placeholder profile image */` (CSS) | Frozen Tombs 5, Rudenko 8, Pazyryk 21; title “Frozen Tombs of Siberia: The Pazyryk Burials of Iron Age Horsemen” |
| 03 | books.google Rolle | 1,698 | `/* #gbi4id - gaia bar placeholder profile image */` (CSS) | World of the Scythians 7, Rolle 8; title “The World of the Scythians - Renate Rolle” |
| 04 | wiki Issyk | 856 | `</ul>` | Issyk 91, undeciphered 7, Kushan 26; title “Issyk inscription - Wikipedia” |
| 05 | wiki Ice Maiden | 1,324 | `</ul>` | Ukok 53, Ice Maiden 46, Pazyryk 24; title “Siberian Ice Maiden - Wikipedia” |
| 06 | Thayer 4A | 983 | `</A></SPAN></P>` | Targitaus 3, Scythians 28 — the 4.5–7 origin account is present in-text (“a man whose name was Targitaus”) |
| 07 | Thayer 4B | 1,556 | `</A></SPAN></P>` | Callippidae 2, Scythia 36 — Callippidae is the first group named in 4.17 |
| 08 | Thayer 4C | 1,499 | `bit.ly/Herodotus4CE<!-- NOT CHECKED -->` | oath 1 — the 4.70 oath passage is present (“when the Scythians will swear their mightiest oath”); Scythian 79 |
| 09 | Thayer 7B | 2,987 | `bit.ly/Herodotus7BE<!-- NOT CHECKED -->` | Sacae 4, Scythians 3 — 7.64 in Godley's spelling (“Sacae, who are Scythians, had on their heads tall caps…”) |
| 10 | Leiden handle page | 140 | `<li class="file_license">` | Lubotsky 2, “Scythian elements” 3; `<title>Scythian elements in Old Iranian</title>`, `citation_author: Lubotsky, A.M.` |
| 11 | academia.edu | 1 | — (403 challenge body, 1 line) | cf_chl 10, challenge 8; title “Just a moment...” |
| 12 | Iranica “Khotan iv” | 508 | `body.setAttribute("style", "--scroll-bar-w: 0px");` (inline script) | Khotanese 175, Emmerick 43, Tumshuqese 11; title “KHOTAN iv. The Khotanese Language - Encyclopaedia Iranica” |

Honest reading: line 79 lands on markup for 01–03, 10, 12 and on closing tags for 04–07, 09; it is substantive for none of the twelve (the Thayer line 79 hits are the site's own short-link annotations, and the entry already says “Website editorial annotations are not Herodotus's testimony”, l.179). Where line 79 is not substantive, the keyword counts and titles above (dated, same commands) carry the content-verification; the technique's yield is reported exactly.

## 5. Access attempts on the non-live outcome (2026-10-18T09:23–09:24Z)

- **11 academia.edu/104775728** — 403 across 4 variants: lane UA HTTP/2 (5,469 B), `curl/8` (5,362 B), HTTP/1.1 lane UA (5,490 B), Firefox UA + Accept headers + `--compressed` (3,230 B); every body is a Cloudflare challenge (cf_chl tokens). CDX availability for `academia.edu/104775728*`: snapshots exist — `20240903145548` status 200 length 44,430; `20240903145552` 200/44,448; `20241214064323` 200/28,798 (plus 2026 301s). Access outcome (bot wall), not proof of death; locator kept unchanged, attempt documented here.
- **10 Leiden** — old route's CDX shows 200 snapshots (`20210428231814`, `20250221205756`); the 301 is a server-side permanent move of the same repository item (both forms 200, 8,911 B), so the locator was re-pinned rather than kept (§6).
- **02/03 books.google.com** — the 302 to `books.google.com.br` is a geo-redirect, not a canonical move; locators kept.

## 6. Disposition: **stale-fixed** — entry edits (2026-10-18T09:25–09:26Z)

One permanent-301 move re-pinned in `corpus/knowledge/civilizations/scythian-saka.md` (old→new; evidence §3/§5):

- **Lubotsky 2002 (l.180):** `https://scholarlypublications.universiteitleiden.nl/access/item%3A2882853/view` → `https://scholarlypublications.universiteitleiden.nl/handle/1887/16379` (301; new form 200, 8,911 B; title “Scythian elements in Old Iranian”, citation_author “Lubotsky, A.M.” — same repository item).

`- verified-at:` now carries (verbatim from the edited entry):

> `- verified-at: 2026-10-17; frontmatter/apparatus audit (M05 metadata sweep): schema, source-list presence, and couples-link resolution checked; body provenance limits unchanged (§“Provenance cautions and source anchors”); not a fresh retrieval of the listed works. URL-status receipt added 2026-10-18 (round-17 C11): all 12 distinct cited URLs swept against the M04 method — 11 × HTTP 200 with content markers verified (Herodotus 4A/4B/4C/7B text pages, the Lubotsky chapter record, the Rudenko and Rolle catalogue records, the AJA review, Iranica “Khotan iv”, and the two Wikipedia reference trails), 1 × 403 Cloudflare bot wall at academia.edu (retries and header variants recorded; access outcome, not rot), and the Leiden repository locator re-pinned to its permanent 301 target; closes the round-16 C07 finding “no dated URL-status receipt exists” (round-16 map row reason; receipt: reports/round-16/civ/072-083.md). Per-URL receipts: reports/round-17/civ/sed79.md.`

The round-16 reason trail is therefore kept in the entry line itself (distinctive token + shard path). `- source:` and `- recheck:` unchanged.

Post-edit checks (all 2026-10-18, lane root, `TMPDIR=$PWD/.scratch`):

- `git diff --stat -- corpus/knowledge/civilizations/scythian-saka.md` → 1 file changed, 2 insertions(+), 2 deletions(-) — exactly the `verified-at` line and the Leiden URL; nothing else.
- sha256 before `aff3ca0aa3a31e477a21a08d6aa94561a028466e55ec9202e3e6dd9572e95e00` (equals the round-16 shard digest) → after `cb3a6428c4b174a4917871185e416f3ac7d3ecdf62a016432f87a486b3ab5c51`.
- Distinct-URL recount after edit → 12 (one set member changed, cardinality unchanged).
- New locator present in bytes: `grep -c 'handle/1887/16379'` → 1; old form `grep -c 'access/item%3A2882853/view'` → 0.
- `python3 tools/gates/provenance-audit.py corpus/knowledge/civilizations/scythian-saka.md` → `files=1 marks=0 mark-lines=0 findings=0 blocked=0` (exit 0).
- Couples-link resolution (round-16 C07 resolver form: brace expansion + `corpus/knowledge/`-relative anchors) → 14/14 resolved, equal to the filed V05 count (`reports/round-9/metadata/v05-civ-77-94.md:46`).
- Seat's corpus dirty scope: `git status --porcelain corpus/knowledge/civilizations/scythian-saka.md` → ` M` for this file only from this seat (inuit/maya-classic/mesoamerica/mongol/muisca/persia-sasanian/polynesia-navigation/rapa-nui/rome/siam-thai edits belong to sibling seats).

## 7. Independent corroboration (not this seat's claim)

Verifier seats V01 and V03/V04 independently swept the same baseline URL set on 2026-10-18 09:16–09:19Z (`.scratch/v01/sweep12.json`, `.scratch/r17-v34/independent-sweep.json`); their scythian-saka summary is **n=12, live=11, blocked=1, hard_fail=0** (V01 code tally: `{"200": 11, "403": 1}`) — identical to §3, with matching sizes and effective URLs row-for-row where compared (01 120,873 B; 02 121,684 B → books.google.com.br; 06 42,727 B; 08 76,005 B; 10 8,911 B; 12 498,050 B). Recorded as corroboration; the verifiers' own receipts are theirs.

## 8. Negative claims + sweeps

- **Before this round, no in-repo receipt carried a per-URL status for `scythian-saka`** — re-run of the round-16 C07 sweep form (2026-10-18): `grep -rln 'scythian-saka' reports/ LOG.md SCORECARD.md | grep -v 'round-9/metadata/v05|round-8/metadata/m05|round-16/civ'` → `reports/supplement-opencode-1/scratch/28-corpus-contract/header-census.txt`, `reports/supplement-opencode-1/inventory-after.json`, `reports/round-9/metadata/audit.md`, `reports/round-9/metadata/v03-civ-39-57.md`, `reports/round-9/metadata/v07-synth-13-24.md`, `reports/round-16/validation.json`, `reports/round-17/civ/sed77.md`, `reports/round-17/civ/sed80.md`, `reports/round-17/validation.json` — header censuses, bookkeeping, shard-boundary mentions, and this round's sibling fragments listing the entry among their targets; none contains a URL status for it. This round's §3 is the receipt that ends the round-16 negative claim.
- **No dead links found among the 12**: 0 hard fails (000/404) in §3; the single non-live outcome is a Cloudflare 403 access outcome with recorded retries (§5).
- **No other corpus bytes touched by this seat**: §6 dirty-scope check; the 12-target edit audit in `reports/round-17/run-validation.py` is the runner's to make.
- **No real-world rights/clearance/canon ruling**: NON-CANON; statuses are point-in-time access facts, not permissions or canon.

## 9. Limits

- Point-in-time 2026-10-18 during a parallel wave; scope is `scythian-saka.md`'s 12 URLs only.
- The `sed -n '79p'` technique pins one fixed-depth line; where it lands on markup/closing tags the content evidence is the keyword counts and titles (commands in §4). Not a full-document verification, and not presented as one.
- 403 outcomes are access outcomes (round-16 rule, `reports/round-16/civ/060-071.md:139`), not proof of link death; the affected locator was kept and the retries documented.
- The re-pinned Leiden form is the repository's canonical handle route; the entry's 2026-10-17 inspection date text is unchanged, since the re-pin does not alter what was inspected.
- No freshness-axis claim, no ranking, no LOG.md/SCORECARD write; the parent integrates.

## 10. Machine-readable rows (for the round-17 map / runner)

```json
{"round":17,"seat":"R17-C11","technique":"sed -n '79p'","date":"2026-10-18","entry":"scythian-saka.md","entry_status_before":"stale-documented","disposition":"stale-fixed","round16_trail":"reports/round-16/civ/072-083.md:33 — status stale-documented; no dated URL-status receipt exists (r16 C07 negative sweep §3; map reason carries the same token)","distinct_urls":12,"sweep":{"date_utc":"2026-10-18T09:22:29Z","command":".scratch/r17c11/sweep.py (curl -sS -o body -w '%{http_code} ...' -L --max-time 15; M04 method, retry on 000)","live":11,"blocked_403":1,"hard_fail":0},"probe":{"date_utc":"2026-10-18T09:22:3xZ","command":".scratch/r17c11/sweep.py bodies + sed -n '79p' + keyword counts","content_verified":11},"replacements":[{"source":"Lubotsky 2002 l.180","old":"https://scholarlypublications.universiteitleiden.nl/access/item%3A2882853/view","new":"https://scholarlypublications.universiteitleiden.nl/handle/1887/16379","evidence":"301 permanent; 200 8911 B; title 'Scythian elements in Old Iranian'; citation_author Lubotsky, A.M."}],"attempts":[{"url":"https://www.academia.edu/104775728/","outcome":"403 Cloudflare x4 variants (3230-5490 B challenge bodies); CDX 200 snapshots 20240903145548/20241214064323; locator kept"}],"entry_sha256":{"before":"aff3ca0aa3a31e477a21a08d6aa94561a028466e55ec9202e3e6dd9572e95e00","after":"cb3a6428c4b174a4917871185e416f3ac7d3ecdf62a016432f87a486b3ab5c51"},"corroboration":".scratch/v01/sweep12.json; .scratch/r17-v34/independent-sweep.json (n=12 live=11 blocked=1 hard_fail=0)"}
```
