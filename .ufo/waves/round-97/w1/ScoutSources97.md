# ScoutSources97 — Report (round 97 w1, sourcing the verbal-duelling entry)

Seat: ScoutSources97 (scout; leaf member, no subagent dispatch). Read-only research; writes confined to my stage dir, my captures, and my Report. Nothing committed.

## What I did

1. Read the frozen round-97 inputs first: `reports/round-97/claims.json` (claims O and C; C needs ≥ 3 new tier A|B registry rows S985 upward opened 2026-11-05, capture-backed) and `reports/round-97/predispatch.py` (legs O0–O4, C1–C8; C7: qualifying ids need captures under `reports/round-97/evidence/`; C2 needs tier A|B, status mined, opened 2026-11-05, used-by exactly the entry path).
2. Read the `corpus/SOURCES.md` header (11-cell registry grammar: id, source, kind, tier, scope, anchor, teaches, status, opened, recheck, used-by; tiers scoped per row; C is lead-only; A = primary/authoritative, B = strong secondary). Registry row count at check: `grep -c -E '^\| S[0-9]+' corpus/SOURCES.md` → 908, rc 0 (matches the claims before-state).
3. Dedup before opening: every one of the 16 candidate URLs checked with `grep -c -F` on the full URL and on host+path against `corpus/SOURCES.md` — all `full=0 hostpath=0`, rc 0 each. No candidate is a registry duplicate.
4. Ran 13 `web_search` queries (8 results each; full log in `stage/ScoutSources97/candidates.md`): Dundes-Leach-Özkök, Labov rules, Dunbar-Kennedie flyting, Lokasenna/Bellows, Inuit song duel/Hoebel, Naqa'id Jarir-Farazdaq, Pagliai verbal art as contest, Unferth flyting, bertsolaritza/Oral Tradition, balagtasan, contrapunteo/son huasteco, Zulu izibongo, Nicholson Literary History of the Arabs.
5. Opened candidates with plain `curl -L -sS --max-time 30` and the default user agent. Transient failures (429/5xx/timeout/connection error) retried up to 3 times with 20 s backoff; 403 walls recorded, never bypassed (no `-k`, no login, no headless browser).

## Results

- **8 candidates admitted** (7 tier A + 1 tier B; target was ≥ 4 tier A|B): pagliai_2009 (Oral Tradition 24.1 2009), hoebel_1954 (The Law of Primitive Man, archive.org scan), lokasenna_bellows (Wikisource Poetic Edda), dunbar_kennedie_murphy (Murphy edition of the Flyting of Dunbar and Kennedy), ruszkiewicz_2020 (Prace Filologiczne. Literaturoznawstwo 10(13) 2020, DOI 10.32798/pflit.575, CC BY), garzia_2007 (Oral Tradition 22.2), nadera_2019 (SARE 56(1) 2019), nicholson_1907 (Gutenberg #37985).
- Every admitted candidate has: URL, access date 2026-11-05, HTTP status, byte size, sha256 capture under `stage/ScoutSources97/captures/` (PDFs additionally as `.txt` via `pdftotext -layout`, rc 0 ×5), a tier, and one located quote ≤ 25 words with byte count == 1 (verified by `python3` `read_bytes().count(...)`; asserted for all 8 in the writer run).
- Coverage across the entry's surfaces: theory/typology (Pagliai), song duels and juridical adjudication (Hoebel), senna primary text (Lokasenna), flyting primary text + peer-reviewed definition (Murphy; Ruszkiewicz), improvised contest with judges (Garzia), moderated poetic debate (Nadera), naqa'id invective with partisan audience adjudication (Nicholson).
- **2 candidates opened but not admitted** for quote-uniqueness reasons: bevan_nakaid_edition (Arabic OCR has no clean English; title string repeated 6× on the details page) and labov_chapter (Springer mirrors the preview ≥ 5× in page metadata; 11 spans probed, none unique; Penn self-bibliography 403).
- **7 wall rejects recorded** with every attempt: Northwestern bepress 403×4, sacred-texts 403×4, UTexas dSpace 403×1, SOAS worktribe 403×1, LSU repository 403×1, JSTOR Dundes HTTP 200 but 3038-byte HTML interstitial (login shell, not article bytes), PMC HTTP 200 but 1816-byte HTML block page. Each reject carries a flip condition; three flips resolved to admitted alternatives (Hoebel 1954, Wikisource, Nicholson/Ruszkiewicz). Open gap: no admitted African (Zulu izibongo) or Mexican (contrapunteo) source this round — both walls; flip conditions recorded in candidates.json.

## Files written

- `stage/ScoutSources97/candidates.json` — machine-readable candidates + rejects (8 admitted / 2 unadmitted / 7 wall rejects), sha256 cc940051577528f69e6b61b069c4943197e9c146fdde1303f164dc1955a50953.
- `stage/ScoutSources97/candidates.md` — candidate table, search log, rejects, commands with rc.
- `stage/ScoutSources97/captures/` — C1_pagliai.pdf(+.txt), C2_hoebel1954_djvu.txt, C3_lokasenna_wikisource.html, C4_flyting_murphy.pdf(+.txt), C5_flyting_ignatianum.pdf(+.txt), C6_naqaid_bevan_details.html, C6b_naqaid_bevan_djvu.txt, C6c_naqaid_vol3_djvu.txt, C6d_nicholson_gutenberg.txt, C8_balagtasan_sare.pdf(+.txt), C9_garzia_bertso.pdf(+.txt), C10_labov_springer.html. No S-ids assigned (registry minting is not mine).

## Notes for downstream seats

- The entry writer (registry/entry seats) may mint S-ids from the admitted 8; the quotes and byte counts are already located and re-runnable. For the naqa'id, the admitted anchor is Nicholson 1907 (clean text); Bevan remains the critical edition of record if a seat wants the primary Arabic edition registered with an anchor that survives evidence discipline only as edition identity — the current captures cannot yield a count==1 English quote for it.
- Claims discipline: I did not verify "operability" (claim O) anything; my lane is claim C coverage only.

## Tooling authorization

None installed, none upgraded. `pdftotext` (poppler 26.10.0) already present at /usr/bin/pdftotext. No pacman use. No host sysctls touched.

## Incident note

One batch of curls initially wrote captures with bare filenames, landing them in the fleet root cwd. Caught immediately: all good captures moved into `stage/ScoutSources97/captures/`, all junk 403 bodies deleted; final stray check `find <fleet-root> -maxdepth 1 -name 'C*_*' -o -name 'curlerr_*' -o -name 'err_*.log' | wc -l` → 0. Scratch deleted before yield.

## Blockers

None. No dependency waits; nothing committed; scratch removed.
