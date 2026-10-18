# R17-C06 — persia-sasanian fixer: never-swept URL set live-swept, 2 stale locators fixed

- worker: C R17-C06 (round-17 C-fixers seat, “never-swept #1 persia-sasanian”); assignment text: “live-sweep the entry's cited URLs (or a documented sample >=5), fix dead locators or document; reports/round-17/civ/persia-sasanian.md”.
- writes (only): `corpus/knowledge/civilizations/persia-sasanian.md` (one assigned entry; 4 lines edited) + this file. No commit, no push, no LOG.md touch, no other corpus byte.
- date: 2026-10-18; command times below are UTC (`date -u` → `2026-10-18T09:21:56Z` pre-edit, `2026-10-18T09:25:42Z` post-edit).
- baseline: `reports/round-17/claims.json` declares baseline `f30b6f8188937632bbedd0e7b29aeefff6f8b07b`; HEAD `9b49a4a` (“round-17: declare loop-2 build-1 claims D/C/O”); pre-edit `git status --porcelain -- corpus/knowledge/civilizations/persia-sasanian.md` → empty (clean), before-bytes sha256 `9d0a65e34dbafddd5999eb1039503228641ad33a7c7dd83dc09f27b3894cb3b9` — the full hash whose prefix `9d0a65e34dbafddd` is the digest recorded in `reports/round-16/civ-map.json` (byte chain closes on the round-16 map’s bytes; also matches `reports/round-16/civ/072-083.md:30`).
- note: the civ worktree is shared with concurrent round-17 C-workers — at start of this run `git status --porcelain -- corpus/knowledge/civilizations/` showed several other entries already modified by other seats (this fragment deliberately does not enumerate them, to keep name-based attribution in the round-17 validator unambiguous; that status output, not this note, is the evidence); none of that is mine. My entry was clean before my edit (§header) and only my 4 lines changed after.

## 1. Debt under fix (round-16 reason trail, kept in the entry edit)

`reports/round-16/civ-map.json` row for `persia-sasanian.md`: `"status": "stale-documented"`, reason `"no dated URL-status receipt exists for its 94 distinct cited URLs (r16 C07 negative sweep); freshness pause defers the sweep — not evidence of breakage [evidence: reports/round-16/civ/072-083.md]"`. The shard itself (`reports/round-16/civ/072-083.md` §3, rows at `:30`, `:98`, `:119`) names the debt: entry 77, `sha256_16 9d0a65e34dbafddd`, 9 distinct URLs, `url_receipt: null`, open item “no URL-status receipt exists (sweep §3); freshness pause defers”; the sweep there lists persia-sasanian as 1 of 7 never-status-checked entries in its partition (9 of the 94 unswept distinct URLs). The round-8 predecessor receipt (`reports/round-8/metadata/m05-civ-77-94.md:7`) is apparatus-only: “No source re-retrieval was performed — live source rechecks are the F claim’s work, not this sweep’s.”

## 2. Negative claim, with sweep

No in-repo receipt carries a per-URL HTTP status for this entry before this round. My own sweep (2026-10-18):

```
grep -rln "persia-sasanian" reports/round-9 reports/round-10 reports/round-11 reports/round-12 \
  reports/round-13 reports/round-14 reports/round-15 reports/round-16 | grep -v round-16/civ
→ reports/round-9/metadata/audit.md
  reports/round-9/metadata/v05-civ-77-94.md
  reports/round-9/metadata/v03-civ-39-57.md
  reports/round-9/metadata/v07-synth-13-24.md
  reports/round-16/validation.json
```

All 5 hits characterized (2026-10-18): `audit.md:106` and `v05-civ-77-94.md` are header censuses / apparatus inventories (V05 records 16 couples links, 1 `(to-verify)` mark — no URL status); `v03-civ-39-57.md:57` and `v07-synth-13-24.md:209` are shard-boundary concurrency notes (the entry name in a sibling-shard list); `round-16/validation.json:8589` is a digest row (the same `9d0a65e3…` before-hash used above). Zero of the 5 carries a per-URL HTTP status for this entry (same command with `| grep -c -iE 'http_code|https?://'` → 0). Rounds 10–15: zero hits. The round-16 map’s `url_receipt: null` is reproduced.

## 3. Live sweep — all 9 distinct URLs (2026-10-18T09:15:41Z driver run, samples through 09:19Z)

URL extraction command (same method as the round-16 inventory, reproduced exactly: 9):

```
grep -o 'https\?://[^)>, ;]*' corpus/knowledge/civilizations/persia-sasanian.md | sed 's/[.,]$//' | sort -u | wc -l  → 9
```

Sweep command (house M04 method, `reports/round-8/metadata/m04-civ-58-76.md` §2 step 2; retry once on 000):

```
curl -sS -o /dev/null -w '%{http_code} %{url_effective} %{content_type} %{size_download}' -L --max-time 15 \
  -A 'Mozilla/5.0 (compatible; kotodama-metadata-audit/1.0)' <URL>
```

Raw results (driver `.scratch/r17c06/sweep.py` → `.scratch/r17c06/sweep-run1.json`; `TMPDIR=$PWD/.scratch`):

| # | URL (as cited) | status | evidence |
|---|---|---|---|
| 1 | `https://doi.org/10.1017/S0041977X00133063` | **429** (bot-block) | resolves to cambridge.org article page; 429 in 2/2 samples incl. browser-UA retry — rate-limit class, **not** link rot (see §4 Crossref check) |
| 2 | `https://doi.org/10.2307/599356` | **200** | resolves to `jstor.org/stable/599356?origin=crossref` |
| 3 | `https://edspace.american.edu/…/Compareti_SR13_2015_pp36_44PlateII.pdf` | **200** | application/pdf, 682753 bytes |
| 4 | `https://sites.uci.edu/sasanika/files/2020/01/Archaeological-08-tahmasbi.pdf` | **200** | application/pdf, 536387 bytes (redirects to `bpb-us-e2.wpmucdn.com` CDN) |
| 5 | `https://sites.uci.edu/sasanika/files/2020/01/e-sas-AR-18-The-EvolutionofReligiousArchitecture.pdf` | **200** | application/pdf, 2928181 bytes |
| 6 | `https://sites.uci.edu/sasanika/sasanika/files/2020/01/e-sas-AR-14-A-Study-of-the-Imagery-and-Place.pdf` | **200** | application/pdf, 976223 bytes |
| 7 | `https://www.academia.edu/125247107/` | **403** (bot-block) | 2/2 samples incl. browser-UA retry; host refuses non-browser clients |
| 8 | `https://www.avesta.org/mp/grb.htm` | **000** (hard fail) | curl error 60: TLS certificate **expired** (`notAfter=Oct 9 23:59:59 2026 GMT`; `openssl s_client`); 9/9 failed samples across `https://www`/`https://bare`/`http://www` (http 301s into the same TLS failure) |
| 9 | `https://www.ucpress.edu/books/a-state-of-mixture/paper` | **200** | text/html, 168710 bytes |

Tally: 6 × 200 live; 1 × 429 bot-block (not rot); 1 × 403 bot-block; 1 × 000 hard fail. Classification follows the M04 precedent (403/429 = publisher bot blocks, not treated as link rot).

## 4. Content verification of the live locators (retrieval receipts)

PDFs downloaded to `.scratch/r17c06/` and inspected with `pdfinfo` + `pdftotext -f 1 -l 1` (titles/pages vs the entry’s citations):

| file | sha256 | title on p. 1 | pages | matches entry |
|---|---|---|---|---|
| `compareti13.pdf` | `c5777781e3ed1a7072889e203788f2602ea4d03c4219b69f250f53677718c5ee` | “Ancient Iranian Decorative Textiles: New Evidence from Archaeological Investigations and Private Collections” (Compareti) | 10 | “Ancient Iranian Decorative Textiles…”, *The Silk Road* 13, pp. 36–44 ✓ |
| `tahmasbi8.pdf` | `fb103c718c42a396f99ace2da812616e30d6acfeb99775f7b4bc5d16ccb7e6ce` | “The Architecture and Status of Iranian Temples in the Sasanian Era” (Tahmasbi) | 11 | “The Architecture and Status of Iranian Temples…”, *Sasanika Archaeology* 8 ✓ |
| `hozhabri18.pdf` | `ac0684730af3f8740a029fee2cf3a2c0000ed7417262f79be369cd8a462b6d7b` | “The Evolution of Religious Architecture in the Sasanian Period” (Sasanika 2013, Archaeology 18) | 40 | “The Evolution of Religious Architecture…”, *Sasanika Archaeology* 18, pp. 1–40 ✓ |
| `malekan14.pdf` | `f7b0c986abc0a51c4cebfc15f0667ee9819546e709ffc5695b18de32bb4d3700` | “A Study of the Imagery and Place of Women in the Sasanian Period: Sigillographic Evidence” (Malekān) | 21 | “A Study of the Imagery and Place of Women…”, *Sasanika Archaeology* 14 ✓ |

Crossref metadata for the two DOI locators (content check of what the DOIs point at, avoiding the blocked publisher pages):

```
curl -sS 'https://api.crossref.org/works/10.1017/S0041977X00133063'
→ title "Some Reflections on Zurvanism"; BSOAS 19(2), pp. 304-316; Boyce, Mary; 1957-06   = entry line 10 ✓
curl -sS 'https://api.crossref.org/works/10.2307/599356'
→ title "On the Zoroastrian Temple Cult of Fire"; JAOS, p. 454                        = entry line 13 ✓
```

Replacement locator content check (`compareti14.pdf`, retrieved 200 application/pdf 948943 bytes): title page “OBSERVATIONS ON THE ROCK RELIEFS AT TAQ-I BUSTAN: A LATE SASANIAN MONUMENT ALONG THE ‘SILK ROAD’”, Matteo Compareti, 13 pages, The Silk Road 14 — the exact Ṭāq-e Bostān companion paper the entry cites at pp. 71–83.

Archive fallback content checks for the hard-fail host: Wayback CDX `avesta.org/mp/grb*` last index captures — `20260915232122 200` (and `20260909110751 200` for `grb.epub`); the 2026-09-15 snapshot of `grb.htm` retrieved live (200, 127643 bytes, `<title>Greater Bundahishn [introduction]`), and it links the cited chapters’ groupings: `grb1.htm#chap1…#chap3`, `grb12.htm#chap18`, `grb12.htm#chap24`, `grb27.htm#chap28`, `grb27.htm#chap34`, `grb27.htm#chap36`; the three archived chapter-group pages re-checked live the same hour: `grb1.htm` 200 (124598 B), `grb12.htm` 200 (134607 B), `grb27.htm` 200 (94861 B). Archived EPUB re-checked: 200, 395055 bytes, `dc:title` “Greater Bundahishn”. Named as fallback evidence; the entry carries the index-snapshot link.

## 5. Disposition — stale-fixed ×2, verified-live ×6, bot-block documented ×1

- **Fixed (replacement locator now present in the corpus entry bytes):**
  - `https://www.academia.edu/125247107/` → `https://edspace.american.edu/silkroadjournal/wp-content/uploads/sites/984/2017/09/Compareti_SR14_2016_71_83.pdf` (same paper, live, content-checked; old URL 403 bot-block). Old→new recorded; entry line 19 edited.
  - `https://www.avesta.org/mp/grb.htm` → **unchanged as primary** (canonical citation; host may recover), dated **archived-copy fallback added**: `https://web.archive.org/web/20260915232122/https://www.avesta.org/mp/grb.htm` (live, content-checked, links the cited chapters). Entry line 14 edited; §11 “Verification boundary” line updated so the entry no longer calls the edition plainly “accessible”.
- **Verified-live, no change needed:** the six 200s in §3 (two DOIs content-checked via Crossref; four PDFs content-checked by retrieval).
- **Documented bot-block, no change:** Cambridge DOI 429 — the DOI resolves to the correct article (Crossref title/volume/issue/pages match); a publisher rate limit is not link rot. No replacement sought.
- Distinct-URL count after edit: **10** (was 9; −1 academia.edu, +2 edspace PDF + Wayback snapshot) — command: `grep -o 'https\?://[^)>, ;]*' … | sed 's/[.,]$//' | sort -u | wc -l`.

## 6. Entry edit (the only corpus write)

File `corpus/knowledge/civilizations/persia-sasanian.md`, 4 lines changed, `+4/−4` (no line added or removed; `git diff --numstat` → `4 4`):

- line 14 (Anklesaria digitized edition): adds dated unreachable note (expired TLS cert, 9/9 samples; R17-C06) + archived-copy link.
- line 19 (Compareti companion paper): locator replaced + dated note (former academia.edu 403; replacement 200, content-checked).
- line 22 (`verified-at`): appends the round-17 C-fix clause — quotes the round-16 stale reason (“no dated URL-status receipt exists”) and cites `reports/round-16/civ/072-083.md §3` (reason trail kept), names the sweep result and this receipt.
- line 202 (§11 verification boundary): “The accessible Anklesaria edition” → “The Anklesaria edition (reachable 2026-10-18 only through its archived copy — see the source list)” (consistency sweep for text describing the old access state).

before-bytes sha256 `9d0a65e34dbafddd5999eb1039503228641ad33a7c7dd83dc09f27b3894cb3b9` (= round-16 map digest) → after-bytes sha256 `20e7513e1f3b288e167f2cd56163caba2cbc238c92b0b6524b655a6f40ca7e2e` (command `sha256sum corpus/knowledge/civilizations/persia-sasanian.md`, 2026-10-18T09:25:42Z). Provenance gate re-run after the edit: `python3 tools/gates/provenance-audit.py corpus/knowledge/civilizations/persia-sasanian.md` → `files=1 marks=1 findings=0 blocked=0`, exit 0 (mark count unchanged: the round-16 shard recorded 1). Couples line untouched.

## 7. Limits

- **Presence-level verification only** (titles, page counts, Crossref metadata, archive contents); no passage-level scholarly re-inspection of the cited arguments. The retrieval dates are point-in-time (one hour, 2026-10-18); intermittent availability is not ruled out — the avesta.org TLS expiry is a dated fact, not a permanent verdict, and the primary URL is kept for recovery.
- The sweep is **9/9 of the entry’s URLs** (full, not a sample); the bot-block classification (403/429) is the round-8 M04 precedent, not an independent liveness proof.
- No freshness axis-move claim; no canon, rights, or clearance ruling. Everything here is NON-CANON lane evidence.
- This fragment does not update the round-16 map (a map-scribe’s work); §8 carries the input row.
- **Validator note (2026-10-18, for the C-verifiers):** the round-17 counting command (`python3 reports/round-17/run-validation.py`, run by this seat at 09:27Z and re-run 09:30Z) classifies this entry `fixed`, `attribution 0`, `chosen_fragment reports/round-17/civ/persia-sasanian.md`, `trail: true`, `dated: true`, `command_carried: true`. Its attribution is name-based, so this fragment deliberately names no sibling entry (an earlier revision that listed concurrent workers’ filenames in the header note caused the runner to pick this fragment as chosen evidence for three sibling entries — that revision was corrected; the gap those mentions had masked is now visible to the runner). The 09:30Z re-run reports two sibling entries in this shard with only shared-sweep index mentions and no per-entry disposition fragment yet (named in the runner’s own `validation.json` `failures`, not here); those are other seats’ in-flight work. The 09:30Z `validation.json` therefore records C FAIL (5 fixed / 5 attempted of 12) plus the expected D/O missing-dependency failures; the integrator must re-run after all seats land.

## 8. Map-scribe input

```json
{
  "file": "persia-sasanian.md",
  "path": "corpus/knowledge/civilizations/persia-sasanian.md",
  "status": "stale-fixed",
  "verified_at": "2026-10-18",
  "distinct_urls_before": 9,
  "distinct_urls_after": 10,
  "old_to_new": [
    {"old": "https://www.academia.edu/125247107/", "new": "https://edspace.american.edu/silkroadjournal/wp-content/uploads/sites/984/2017/09/Compareti_SR14_2016_71_83.pdf", "why": "old 403 bot-block; new 200 application/pdf 948943 B, title/pages content-checked (Compareti, Taq-i Bustan, Silk Road 14)"},
    {"old": "https://www.avesta.org/mp/grb.htm", "new": "unchanged primary + archived fallback https://web.archive.org/web/20260915232122/https://www.avesta.org/mp/grb.htm", "why": "host 000 (expired TLS cert 2026-10-09, 9/9 samples); snapshot 200, 127643 B, links cited chapters"}
  ],
  "sha256_before": "9d0a65e34dbafddd5999eb1039503228641ad33a7c7dd83dc09f27b3894cb3b9",
  "sha256_after": "20e7513e1f3b288e167f2cd56163caba2cbc238c92b0b6524b655a6f40ca7e2e",
  "sweep": {"date": "2026-10-18", "total": 9, "live_200": 6, "bot_block": 1, "hard_fail": 1, "replaced": 1, "command": "curl -sS -o /dev/null -w '%{http_code}' -L --max-time 15 -A 'Mozilla/5.0 (compatible; kotodama-metadata-audit/1.0)' <URL> (M04 method)"},
  "reason": "round-16 stale-documented reason ('no dated URL-status receipt exists', reports/round-16/civ/072-083.md §3) retired by a full 9/9 live sweep; 2 stale locators fixed in the entry with content-verified replacements/fallbacks; entry verified-at line keeps the round-16 reason trail",
  "evidence": ["reports/round-17/civ/persia-sasanian.md"],
  "reason_trail": ["reports/round-16/civ/072-083.md", "reports/round-16/civ-map.json", "reports/round-8/metadata/m05-civ-77-94.md"],
  "limits": "presence-level verification; point-in-time sweep 2026-10-18; bot-blocks classified per M04 precedent"
}
```
