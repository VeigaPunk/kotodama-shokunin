# R17-C08 — rapa-nui fixer: never-swept 9-URL set swept live (stale-fixed)

- worker: C R17-C08 (round-17 C-fixers seat, “rapa-nui fixer”, never-swept #3 of the round-16 C07 seven); assignment text: “C R17-C08 (never-swept #3 rapa-nui): same protocol; reports/round-17/civ/rapa-nui.md”
- writes (only): `corpus/knowledge/civilizations/rapa-nui.md` (one assigned entry, `verified-at` line only) + this file; scratch under gitignored `.scratch/r17c08/` (`TMPDIR=$PWD/.scratch` before every scratch-writing command). No commit, no push, no LOG.md touch, no filed round-8–16 artifact modified.
- date: 2026-10-18; command times below are UTC (`date -u` → `2026-10-18T09:20:57Z` at close; sweeps at `09:16:36Z` and `09:19:14Z`).
- baseline: `reports/round-17/claims.json` declares baseline `f30b6f8188937632bbedd0e7b29aeefff6f8b07b`; HEAD at start and close `9b49a4a` (“round-17: declare loop-2 build-1 claims D/C/O”); `git status --porcelain -- corpus/knowledge/civilizations/rapa-nui.md` → empty before the edit.
- byte chain: before-bytes sha256 `e56906e8317ca9a99c3b58a003898ad8dd13623be891b39e323f6491933cc1ec`; first 16 hex = `e56906e8317ca9a9`, exactly the digest the round-16 C07 shard recorded for this file (`reports/round-16/civ/072-083.md:32,121`), and equal to the verify seat’s pre-round baseline copy (`.scratch/verify-baseline/rapa-nui.md`, re-hashed this run).
- note: the civ worktree is shared with concurrent round-17 workers (`inuit.md`, `mongol.md` modified by other seats during this window; `reports/round-17/civ/mongol.md` landed mid-run); none of that is mine.

## 1. Debt under fix (round-16 reason trail, kept in the entry edit)

Round-16 map row (`reports/round-16/civ-map.json`, entries[78], 1-based idx 79 of 94):

```json
{"file": "rapa-nui.md", "status": "stale-documented", "verified_at": "2026-10-18",
 "command": "in-repo verification battery per shard receipt: sha256sum + provenance-audit + couples-resolution (reports/round-16/civ/072-083.md)",
 "reason": "no dated URL-status receipt exists for its 94 distinct cited URLs (r16 C07 negative sweep); freshness pause defers the sweep — not evidence of breakage [evidence: reports/round-16/civ/072-083.md]"}
```

Shard receipts (`reports/round-16/civ/072-083.md`): line 32 — `| 79 | rapa-nui.md | e56906e8317ca9a9 | 15 | 9 | none exists — same named reason | stale-documented (in-entry caution named, §1.1) |`; line 98 — “Distinct-URL inventory for those 7 … rapa-nui 9 … **94 distinct cited URLs have never been status-checked in-repo**. This is the concrete residual the freshness pause is holding: a future operator-unpaused round can sweep exactly these 94 URLs against the M04 method (`m04-civ-58-76.md` §2 step 2).”; machine row line 121 — `{"idx":79,"file":"rapa-nui.md","sha256_16":"e56906e8317ca9a9","status":"stale-documented","couples_resolved":15,"couples_prior":"v05-civ-77-94.md:46","distinct_urls":9,"url_receipt":null,"open_items":["same; KW02 early-date caution rapa-nui.md:7"]}`.

The negative was independently reproduced by the round-16 auditor (`reports/round-16/civ/map-audit.md` §3, C07’s seven rows: “negative claim … tested by me against rounds 5–15 … Negative claim survives.”). Round 17 is the operator-unpaused round the shard named, so this seat runs exactly that sweep for its one assigned entry.

URL set, re-derived (not trusted from the shard):

```
grep -o 'https\?://[^ )"<>]*' corpus/knowledge/civilizations/rapa-nui.md | sed 's/[.,;]$//' | sort -u | wc -l
→ 9   (list saved: .scratch/rapa-nui-urls.txt; matches the shard’s distinct_urls=9)
```

## 2. Negative claim, with sweep

Claim: *no dated URL-status receipt existed in-repo for any of these 9 URLs before this round.* My own sweep, 2026-10-18:

```
for u in mysteryofeaste00rout langsci-press.org/catalog/book/124 moevarua.com PMC11192071 \
         s41586-024-07881-4 s41598-024-53063-7 metmuseum.org/essays/easter-island \
         zenodo.235525 en.wikipedia.org/wiki/Moai; do
  grep -rl "$u" reports/round-5 reports/round-6 reports/round-7 reports/round-8 reports/round-9 \
    reports/round-10 reports/round-11 reports/round-12 reports/round-13 reports/round-14 \
    reports/round-15 reports/round-16; done
→ 0 hits for all 9 substrings across rounds 5–16
```

(The C07 shard records URL *counts*, not URL strings, so it cannot and does not itself constitute a per-URL receipt.) The negative therefore reproduces: this entry’s 9 locators had no prior dated status receipt anywhere in-repo.

## 3. Live sweep and content verification (2026-10-18T09:16:36Z / 09:19:14Z)

Method = M04 (`reports/round-8/metadata/m04-civ-58-76.md` §3): `curl -sS -o /dev/null -w '%{http_code} %{url_effective} %{content_type} %{size_download} %{time_total}' -L --max-time 20 -A 'Mozilla/5.0 (compatible; kotodama-metadata-audit/1.0)' <URL>`, one retry if `000`; classification per M04: 403/429 = bot walls, not rot; 404/000 = rot candidates. Script: `.scratch/r17c08/sweep.py` (run1/run2 JSON receipts `.scratch/r17c08/sweep-run1.json` / `sweep-run2.json`; fetched bodies under `.scratch/r17c08/body/`).

```
export TMPDIR=$PWD/.scratch && python3 .scratch/r17c08/sweep.py sweep-run2.json
```

| # | locator (as cited in the entry) | run1/run2 | effective URL | body bytes / sha256 (run1) |
|---|---|---|---|---|
| 1 | `https://archive.org/details/mysteryofeaste00rout` | 200/200 | same | 256646 / `5412988a9fda69365ea8fb7cf7f8f703cdec4b61bba4c5b784556d0b7e5f7904` |
| 2 | `https://doi.org/10.5281/zenodo.235525` | 200/200 | `https://zenodo.org/records/235525` | 82124 / `0d5689d62e161100ed40447072c2f1a046c94d6aaf543e6e283b63b1f502ad6e` |
| 3 | `https://en.wikipedia.org/wiki/Moai` | 200/200 | same | 427128 / `6f477d315b1a0ad1f6d0134f6e8f1504443452ed942066a01ad6ea0b6a765456` |
| 4 | `https://langsci-press.org/catalog/book/124` | 200/200 | same | 37175 / `6e320d29c799061c19b88e15f291b039232eb70d7646f935a16a226054331a00` |
| 5 | `https://moevarua.com/en/the-eye-of-the-moai-2/` | 200/200 | same | 373137 / `fe4bc89c4b581e7fb5c4970c8cefcb011350434648f0064dcbe9107c43bf1706` |
| 6 | `https://pmc.ncbi.nlm.nih.gov/articles/PMC11192071/` | 200/200 | same | 226047 / `32b38f870935fe462883b6f782e14a262c79553534365e54229fc96bd82b9ce2` |
| 7 | `https://www.metmuseum.org/essays/easter-island` | 429/429 | same | — (bot wall; §3.2) |
| 8 | `https://www.nature.com/articles/s41586-024-07881-4` | 200/200 | `…?error=cookies_not_supported&code=…` (same article) | 683212 / `4d1fc28a4b4bde30a9dc9323a02deac5502cfe466870f24fb2561a911c777918` |
| 9 | `https://www.nature.com/articles/s41598-024-53063-7` | 200/200 | `…?error=cookies_not_supported&code=…` (same article) | 342677 / `4f26d70d72e40f054116af351fed067f83152ecbf2126d554b50167dca194f58` |

Run-to-run variance: none observed — both runs 8 × 200 / 1 × 429 / 0 × 000 / 0 × 404.

### 3.1 Content verification (fetched-body markers, mapped to the entry’s citations)

| Entry citation | Marker found in fetched body | Occurrences |
|---|---|---|
| [R20] Routledge, *The Mystery of Easter Island* (archive.org) | `<title>The mystery of Easter Island; the story of an expedition : Routledge, Katherine Pease, 1866-` ; “Routledge” | title 1 / 12 |
| [K17] Kieviet, *A grammar of Rapa Nui* (LangSci) | “A grammar of Rapa Nui”; “Kieviet” | 5 / 15 |
| [K17] DOI 10.5281/zenodo.235525 | `<title>A grammar of Rapa Nui \| Zenodo`; “Kieviet” | title 1 / 15 |
| [KW02] Kjellgren–Wagelie, “Easter Island” (Met) | *via snapshot, §3.2*: title `Easter Island - The Metropolitan Museum of Art`; “Heilbrunn” ×3; “Kjellgren” ×13 | title 1 |
| [F24] Ferrara et al., rongorongo radiocarbon (Nature) | `<title>The invention of writing on Rapa Nui (Easter Island). New radiocarbon dates on the Rongorongo script \| Scientific Reports`; “Ferrara” | title 1 / 44 |
| [D24] Davis et al., agricultural production (PMC) | “Island-wide characterization of agricultural production challenges the demographic collapse hypothesis for R…”; `PMCID: PMC11192071`; “sciadv.ado1459” | 2 / 1 / 18 |
| [MM24] Moreno-Mayar et al., ancient genomes (Nature) | `<title>Ancient Rapanui genomes reveal resilience and pre-European contact with the Americas \| Nature`; “Moreno-Mayar” | title 1 / 53 |
| [MOAI-EYES] Moai reference trail | `<title>Moai - Wikipedia` | 1 |
| [MOAI-EYES] moevarua overview | `<title>The Eyes of the Moai: Discovering Coral Eyes of Rapa Nui`; “Ahu Nau” ×8; “Coral Eye” | title 1 |

### 3.2 metmuseum.org bot wall (429) — control probes and content check

- Same hour: 3/3 retries `429`; host homepage `https://www.metmuseum.org/` → `429`; browser-like UA probe (Chrome 128 string) → `429`, 34224 bytes. Host-wide bot wall, not a per-page break (M04 classification: bot block, not rot) — the locator is **kept**.
- Fallback content check (not written into the entry): Wayback snapshot `https://web.archive.org/web/20250515201504/https://www.metmuseum.org/essays/easter-island` → `200`, 191068 bytes, sha256 `9eb853291979ae6fba777718af18e54fa1254a84c827df5794d3fdab8a52315e`; body carries the essay title and “Heilbrunn”/“Kjellgren”, matching [KW02].

## 4. Disposition — stale-fixed, locator set unchanged

- **old → new: none (no replacement needed).** All 9 locators resolve live; 8 are content-verified directly against their citations and the 9th (metmuseum) is a host-wide bot wall whose content is verified through a dated snapshot. Replacing live, content-verified locators with mirrors would be churn (same rule as sibling R17-C03/mongol).
- The round-16 stale reason (“no dated URL-status receipt exists … freshness pause defers the sweep — not evidence of breakage”) is **retired by this round’s dated receipt**; the entry’s `verified-at` line keeps the reason trail (names the round-16 C07 finding and `reports/round-16/civ/072-083.md`) and adds the round-17 receipt pointer (§5).
- **Limits:** presence-level verification only (titles/markers match the cited works; no passage-level scholarly re-inspection). This is a URL-status + content-identity receipt for the entry’s own links (claim C’s “live, content-verified source” leg), not a freshness axis-move claim — the freshness pause on axis moves is untouched. The shard’s open item — the in-entry KW02 early-date caution (`rapa-nui.md:7`) — **remains open**; a URL receipt does not re-date KW02, and the entry’s 2 `(to-verify)` marks are unchanged (gate counts, §5).
- All artifacts NON-CANON; no real-world rights/clearance ruling is made or absorbed.

## 5. Entry edit (the only corpus write)

File `corpus/knowledge/civilizations/rapa-nui.md`, `verified-at` line (line 6), diff `+1/−1`; URL count unchanged (9 distinct, re-counted after the edit):

before:
```
- verified-at: 2026-10-17; frontmatter/apparatus audit (M05 metadata sweep): schema, source-list presence, and couples-link resolution checked; body reading limits unchanged (§“Source register and reading limits”); not a fresh retrieval of the listed works.
```
after:
```
- verified-at: 2026-10-17; frontmatter/apparatus audit (M05 metadata sweep): schema, source-list presence, and couples-link resolution checked; body reading limits unchanged (§“Source register and reading limits”); not a fresh retrieval of the listed works. URL-status receipt added 2026-10-18 (round-17 C08): all 9 distinct cited links swept against the M04 method — 8 × HTTP 200 with content markers verified, 1 × 429 host-wide bot wall at metmuseum.org (homepage control probe also 429; not rot) content-checked via a 2025-05-15 Wayback snapshot; closes the round-16 C07 finding “no dated URL-status receipt exists” (round-16 map row reason; receipt: reports/round-16/civ/072-083.md). Per-URL receipts: reports/round-17/civ/rapa-nui.md.
```

after-bytes sha256 `c893805a82ed953c29a3f8a20472c6e0579119e7c59d6a3db9ee5e86fb2a0f57` (command: `sha256sum corpus/knowledge/civilizations/rapa-nui.md`, 2026-10-18T09:20Z). Provenance gate before and after the edit: `python3 tools/gates/provenance-audit.py corpus/knowledge/civilizations/rapa-nui.md` → `INFO scan: files=1 marks=2 mark-lines=2 findings=0 blocked=0` (exit 0, both states).

Regression controls (post-edit, 2026-10-18T09:2xZ, `TMPDIR=$PWD/.scratch`): `python3 tools/check-gate-battery.py` → `battery_exit 0, pass 7, fail 0, unevaluable 0`, live gate tree preserved (28 files hashed before/after, modified/added/deleted 0); `grep -rln rapa tools/gates/frozen/ tools/gates/expected/` → no hit (no frozen manifest or committed baseline pins a snapshot of this entry, so the corpus edit cannot move those pins).

## 6. Map-scribe input

```json
{
  "file": "rapa-nui.md",
  "path": "corpus/knowledge/civilizations/rapa-nui.md",
  "status": "stale-fixed",
  "verified_at": "2026-10-18",
  "urls_checked": 9,
  "live": 8,
  "botwall_content_checked": 1,
  "old_url": "none (locator set unchanged; no replacement needed)",
  "new_url": "none (locator set unchanged; no replacement needed)",
  "old_to_new": "unchanged — 9/9 locators resolve live; 8 content-verified directly, metmuseum.org 429 host-wide bot wall content-checked via Wayback snapshot 20250515201504",
  "sha256_before": "e56906e8317ca9a99c3b58a003898ad8dd13623be891b39e323f6491933cc1ec",
  "sha256_after": "c893805a82ed953c29a3f8a20472c6e0579119e7c59d6a3db9ee5e86fb2a0f57",
  "reason": "round-16 C07 negative ('no dated URL-status receipt exists', url_receipt:null) retired by a dated M04-method sweep 2026-10-18 (two runs, 09:16Z/09:19Z): 8 × HTTP 200 with content markers verified against the [R20]/[K17]/[KW02]/[F24]/[D24]/[MM24]/[MOAI-EYES] citations, 1 × 429 host-wide bot wall (homepage + Chrome-UA control probes also 429) content-checked via Wayback; entry verified-at line keeps the round-16 reason trail and adds the round-17 receipt pointer",
  "evidence": ["reports/round-17/civ/rapa-nui.md", ".scratch/r17c08/sweep-run1.json", ".scratch/r17c08/sweep-run2.json"],
  "reason_trail": ["reports/round-16/civ-map.json", "reports/round-16/civ/072-083.md", "reports/round-16/civ/map-audit.md", "reports/round-8/metadata/m04-civ-58-76.md"],
  "fallback_mirror": "https://web.archive.org/web/20250515201504/https://www.metmuseum.org/essays/easter-island (HTTP 200, sha256 9eb853291979ae6fba777718af18e54fa1254a84c827df5794d3fdab8a52315e; fallback only, not written into the entry)",
  "limits": "presence-level content verification; metmuseum leg snapshot-verified; no passage-level re-inspection; KW02 early-date caution (shard open item) remains open; single-day sweep cannot rule out intermittent failure"
}
```

— C R17-C08, rapa-nui fixer, 2026-10-18. All artifacts NON-CANON; nothing here is a canon, rank, rights, or clearance decision.
