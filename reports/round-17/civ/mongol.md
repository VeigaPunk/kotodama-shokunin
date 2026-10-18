# R17-C03 — mongol fixer: `rubruck.html` live re-attempt (stale-fixed)

- worker: C R17-C03 (round-17 C-fixers seat, “mongol fixer”); assignment text: “same protocol for rubruck.html in mongol.md; reports/round-17/civ/mongol.md”
- writes (only): `corpus/knowledge/civilizations/mongol.md` (one assigned entry, `verified-at` line only) + this file. No commit, no push, no LOG.md touch.
- date: 2026-10-18; command times below are UTC (`date -u` → `2026-10-18T09:15:27Z` at start, `2026-10-18T09:18:28Z` for the sample battery).
- baseline: `reports/round-17/claims.json` declares baseline `f30b6f8188937632bbedd0e7b29aeefff6f8b07b`; HEAD at start `9b49a4a` (“round-17: declare loop-2 build-1 claims D/C/O”); `git status --porcelain -- corpus/knowledge/civilizations/mongol.md` → empty before the edit; before-bytes sha256 `0c85e10f14f3295d4dcd99e266a05bf5f98fe727bf5c871099afd1fdf7a6a892` = the hash recorded in `reports/round-16/civ-map.json` (byte chain closes on the round-16 map’s bytes).
- note: the civ worktree is shared with concurrent round-17 workers (`inuit.md` modified by another seat during this run); none of that is mine.

## 1. Debt under fix (round-16 reason trail, kept in the entry edit)

`reports/round-16/civ-map.json` row: `mongol.md | stale-documented | 1 hard-fail 000 URL (rubruck.html) (r16 C06 in-repo verification) [evidence: reports/round-16/civ/060-071.md]`. The shard itself (`reports/round-16/civ/060-071.md:94,125`) names the debt: “1 hard-fail (000) URL from M §3: `depts.washington.edu/silkroad/texts/rubruck.html`; no re-attempt rounds 9–15”. Origin receipt: `reports/round-8/metadata/m04-civ-58-76.md` §4 sweep run A — `000  mongol.md  https://depts.washington.edu/silkroad/texts/rubruck.html`, classified there as “DNS/TLS/connection, retried once” (one of 9 × 000 in that sweep; the other 54 non-live were 403/429 bot-blocks).

## 2. Negative claim, with sweep

No live re-attempt of this locator exists between round 8 and round 16. My own sweep (2026-10-18T09:16Z):

```
grep -rln "rubruck" reports/round-9 reports/round-10 reports/round-11 reports/round-12 \
  reports/round-13 reports/round-14 reports/round-15 reports/round-16
→ reports/round-16/civ/060-071.md
  reports/round-16/civ-map.json
```

Both hits are in-repo restatements of the inherited debt (round 16 ran zero live fetches under the freshness pause); rounds 9–15: zero hits.

## 3. Live re-attempt and content verification (2026-10-18T09:18Z)

```
for i in 1 2 3 4; do curl -sS -o /dev/null -w "sample$i code=%{http_code} bytes=%{size_download} final=%{url_effective}\n" \
  --max-time 30 -L "https://depts.washington.edu/silkroad/texts/rubruck.html"; sleep 1; done
→ sample1..4: code=200 bytes=289660 final=https://depts.washington.edu/silkroad/texts/rubruck.html
  (4/4 HTTP 200; earlier same-hour samples at 09:15Z also 4/4 200, incl. no-redirect and http:// variants)
```

Saved copy (scratch, `TMPDIR=$PWD/.scratch`): `.scratch/rubruck-r17.html`, 289660 bytes, sha256 `2bcad68dcd9a5a379b61afb30abc95d57182f680816902d24d79cda89067efc6`; `<title>William of Rubruck's Account of the Mongols</title>`.

Content receipts — occurrence counts (`grep -o -i … | wc -l`) on the fetched body, mapped to what mongol.md cites:

| Cited in mongol.md | Fetched-page receipt (quoted, location = rubruck.html body) | Occurrences |
|---|---|---|
| Dress: right-side fastening (`mongol.md:124,126`) | “the Turks tie their gowns on the left, the Tartars always on the right” | 1 |
| Dress: `bocca` headdress, costly silk (`mongol.md:124,134`) | “a head-dress, which they call <i>bocca</i>… This <i>bocca</i> they cover with costly silk stuff” | 5 |
| Divination: `qam/kam/cham` (`mongol.md:97`) | “All soothsayers are called <i>cham</i>” | 7 |
| Credential: tablet / Theodulus (`mongol.md:115`) | “a highly-polished tablet of ivory about a cubit long”; Theodulus passages | tablet 2 / Theodulus 4 |
| Court letter: Möngke to Louis IX (`mongol.md:86,116`) | “the word of Mangu Chan to the lord of the French, King Louis”; “The Khan's letter to the King of France” | Mangu 128 / “King Louis” 4 |

Fallback mirror checked the same hour: `https://web.archive.org/web/2026/https://depts.washington.edu/silkroad/texts/rubruck.html` → HTTP 200, resolved to snapshot `web.archive.org/web/20261012155833/…` (2026-10-12 snapshot). Named as fallback only; not written into the entry.

## 4. Disposition — stale-fixed, locator unchanged

- **old → new: unchanged.** `https://depts.washington.edu/silkroad/texts/rubruck.html` → same URL. No replacement locator was needed: the round-8 `000` (connection-class, one of 9 transient 000s) does not reproduce — 8/8 samples across two times in this round are HTTP 200 with the cited content present. Replacing a live, content-verified locator with a mirror would have been churn.
- The round-16 stale reason is retired by the live re-attempt; the entry’s `verified-at` line keeps the round-16 reason trail (names `reports/round-16/civ/060-071.md` and the 1 hard-fail 000 URL) and adds the round-17 receipt pointer.
- **Limits:** presence-level verification only (the cited passages exist at the locator; no passage-level scholarly re-inspection was performed). Only this 1 of the entry’s 10 distinct URLs was re-attempted live this round (assignment scope); the other 9 were live in round 8 and are not re-swept here. A one-day re-attempt cannot prove absence of intermittent failure; if the parent wants an invariant, the verifier seat should re-sample on a later day. This is not a freshness axis-move claim (the round-17 claim C text requires live content verification for the named locator; the freshness pause on axis-move claims is untouched).
- All artifacts NON-CANON; no real-world rights/clearance ruling is made or absorbed.

## 5. Entry edit (the only corpus write)

File `corpus/knowledge/civilizations/mongol.md`, `verified-at` line (line 18), diff `+1/−1`; URL count unchanged (10 distinct, re-counted after the edit):

before:
```
- verified-at: 2026-10-17; round-8 metadata pass only — entry frontmatter checked and all 10 cited links status-swept on 2026-10-17 (9 live, 1 non-2xx or failed); no passage, catalogue, or dated-object re-inspection in this pass
```
after:
```
- verified-at: 2026-10-17; round-8 metadata pass only — entry frontmatter checked and all 10 cited links status-swept on 2026-10-17 (9 live, 1 non-2xx or failed); no passage, catalogue, or dated-object re-inspection in this pass; round-17 C-fix (2026-10-18) retires the round-16 stale reason (1 hard-fail 000 URL; reports/round-16/civ/060-071.md): the Rubruck locator re-attempted live — 4/4 samples HTTP 200, fetched body content-verified against the dress, divination, credential, and court-letter passages cited below — and kept unchanged (no replacement needed); receipt reports/round-17/civ/mongol.md
```
after-bytes sha256 `e60b3903402034bcd897617fac589340fb9c70439a028583fbe193fec14c1163` (command: `sha256sum corpus/knowledge/civilizations/mongol.md`, 2026-10-18T09:19Z).

## 6. Map-scribe input

```json
{
  "file": "mongol.md",
  "path": "corpus/knowledge/civilizations/mongol.md",
  "status": "stale-fixed",
  "verified_at": "2026-10-18",
  "old_url": "https://depts.washington.edu/silkroad/texts/rubruck.html",
  "new_url": "https://depts.washington.edu/silkroad/texts/rubruck.html",
  "old_to_new": "unchanged (no replacement needed; 000 was transient-class)",
  "sha256_before": "0c85e10f14f3295d4dcd99e266a05bf5f98fe727bf5c871099afd1fdf7a6a892",
  "sha256_after": "e60b3903402034bcd897617fac589340fb9c70439a028583fbe193fec14c1163",
  "reason": "round-8 m04 sweep run A hard-fail 000 URL re-attempted live 2026-10-18: 4/4 samples HTTP 200, 289660 bytes, sha256 2bcad68dcd9a5a379b61afb30abc95d57182f680816902d24d79cda89067efc6; body content-verified against the dress (right fastening, bocca), divination (cham), credential (tablet/Theodulus) and court-letter (Mangu to King Louis) passages cited in-entry; entry verified-at line keeps the round-16 reason trail and adds the round-17 receipt pointer",
  "evidence": ["reports/round-17/civ/mongol.md"],
  "reason_trail": ["reports/round-16/civ/060-071.md", "reports/round-16/civ-map.json", "reports/round-8/metadata/m04-civ-58-76.md"],
  "fallback_mirror": "https://web.archive.org/web/20261012155833/https://depts.washington.edu/silkroad/texts/rubruck.html (HTTP 200, 2026-10-18)",
  "limits": "presence-level verification; 1/10 URLs re-attempted this round; intermittent failure not ruled out"
}
```
