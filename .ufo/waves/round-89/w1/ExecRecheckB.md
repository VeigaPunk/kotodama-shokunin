# ExecRecheckB — round 89 claim F recheck, rows S104 S105 S106 S107 S142 S157 S163 S875

Result: **8 LOCATED / 0 NOT-LOCATED.** All 8 fetches returned 200 directly. No Wayback fallback was needed. S142's row URL is already a web.archive.org capture, so that capture is what was fetched.

## Paths written (stage `.ufo/waves/round-89/w1/stage/ExecRecheckB/`)
- `S104.txt` … `S875.txt` — plain-text captures. HTML went through python html.parser, keeping text outside script/style/noscript/template. JSON is kept as served. The PDF went through `/usr/bin/pdftotext -enc UTF-8`, which was already installed. The manifest's `sha256` is the hash of these files.
- `manifest-part.json` — one entry per row: url, http_status, fetched_at (-03:00), capture, sha256, raw_sha256, quote, verdict, supports_teaches, attempts.
- `rows.md` — one disposition line per id.

## Commands (observed)
- `curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64) kotodama-r89-recheck' --max-time 60` for each row URL, between 2026-11-04T19:07:29 and 19:07:40 -03:00. All returned 200: text/html for S104, S106, S157, S163 and S875; application/json for S105 and S107; application/pdf for S142.
- Every quote was checked with `measure89.contains(capture, quote)` and `measure89.quote_ok`, rc=0. All 8 returned True. Word counts are 6/10/24/9/25/15/16/9, and every quote is at least 45 normalised characters.
- Scratch `/fast/scratch/hyaku/kotodama-r89/ExecRecheckB` was removed. No tools were installed.

## Findings to flag (not fixed)
1. **S104 — only part of the teaches cell is in the text capture.** The page heading "Pseudo Family: LSFic" is there, so the node's existence and name are shown; that matches the row anchor "Page heading". The second clause, "FSL (fren1243) and ASL (amer1248) classify under it", appears only inside the `GLOTTOLOG3.Tree.init(...)` script JSON. The required converter drops script content, so that clause is not in the capture. ASL-under-LSFic is shown independently by S105. L1 should decide whether partial support is enough to advance S104.
2. **S142 — the anchor wording doesn't match the PDF.** The row anchor quotes "The style of notation used *by* these hunting signals…". The PDF reads "used *for* these hunting signals". The teaches cell itself is supported. The quoted passage covers the orally transmitted teacher-to-pupil repertoire, and "pour le chien" (for the dog) and "la retraitte" (retreat) are also present.
3. **S157 — the teaches cell is fine but undersells the biome tags.** The UNESCO Biomes block now lists Agro-ecosystems, Marine/coastal/island areas and Mountains, not Mountains alone. The cell's "under a mountain biome" is still true.
4. **S875 — the period ladders check out; the domain list was only partly checked.** I checked the 時代 ladders: 旧石器…令和 [日本] plus the China and Korea ladders. I did not re-count the 16 top-level 分野 values in the anchor beyond spot checks (建造物, 伝統的建造物群, 絵画, 版画, 彫刻, 工芸 are present). The teaches cell is supported.

No teaches cell looks wrong. Captures sit in my stage dir; L1 copies them to `reports/round-89/rechecks/` when integrating.
