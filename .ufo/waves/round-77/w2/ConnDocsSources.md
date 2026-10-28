# ConnDocsSources — round 77, wave 2 — document-level graph cross-check

Seat: `ConnDocsSources` (connector, leaf member, no subagent dispatch). Base `211f9526800906e0c585d878d265c37e5e090c15`. Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Read-only against the lane: no lane git/jj/index writes, no production file writes. Only writes: this report and `.ufo/waves/round-77/w2/stage/ConnDocsSources/` (checker `graph_check.py`, output `graph_check.out`). Scratch `/fast/scratch/hyaku/kotodama-r77/ConnDocsSources` held two base blobs; it is deleted before yield.

Inputs are the W1 drafts and receipts (`w1/drafts/`, `w1/stage/`, `w1/*.md`). I cross-checked them against each other and against base blobs. I did not re-fetch live sources; live-byte facts below are the W1 stored bodies and receipts, named by file.

## Verdict

The graph does **not** close at draft. The checker reports 40 edge lines: 19 OK, 15 FAIL, and 6 PENDING the L1 landing. The table below groups them into 37 rows. Every FAIL is a concrete line-level disagreement, and most can be fixed in drafts before freeze. The two largest problems are (a) the S897 registry row contradicts its own Gate and the evidence on tier, per-UA status, and recheck window; (b) the README plan would fail the INDEX verbatim-topic leg, and its heading count contradicts the lesson.

The part that holds: the two documents map one-to-one to the two lane ids, the two live URLs are identical across row, entry, and lesson, the entry has exactly one `- source:` line per adopted document with no legacy ids, every quoted span in the entry locates in the stored text of its document (13/13 CJK spans, 8/8 English spans), the D2 page locators match the PDF, and the base counts add up.

## Nodes

| node | where | identity |
|---|---|---|
| D1 document (魏斌, cssn.cn) | staged S897 → lane **S897** | live `http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml`; capture `web/20240111092427id_` |
| D2 document (Kałużyńska 2025, *Onomastica* LXIX) | staged S903 → lane **S898** | live `https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/`; captures `20260901045105id_` (byte-identical) and `20251231111748id_` (regenerated) |
| R1 row S897 | `w1/stage/ExecCensusEnd/rows-897-898.md` line 1 | 11 cells, id/source/kind/tier/scope/anchor/teaches/status/opened/recheck/used-by |
| R2 row S898 | same file line 2 | same shape |
| E entry | `w1/drafts/corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md` | `- source:` lines 3 (S897), 4 (S898); `- topic:` line 11; `- recheck:` line 6; §8 lines 109–115; §9 line 119; §10 line 123 |
| L lesson Gate | `w1/drafts/corpus/lessons/round-77.md` | Gate rows lines 19 (S897) and 20 (S898); Census line 86; Routed item 3 line 96 |
| M map | `w1/ScoutIdMap.md` lines 11–12, 21 | staged → normalized document → lane id (no frozen file yet) |
| B README | base `corpus/README.md` (836 lines) and plan `w1/stage/ScoutReadmeIndex/readme-plan.md` | heading line 344; row insert after 355; footers 834/836 |
| EV evidence | `w1/stage/ScoutDocS897/evidence.txt`, `w1/stage/ScoutDocS898/evidence.txt`, `w1/stage/ScribeEntryA/fetch-log.txt` | W1 receipts; lane targets `reports/round-77/evidence/S897.txt`, `S898.txt` absent |

## Edges and status

Status: OK = checked and holds; FAIL = checked and contradicted; PENDING = target exists only after landing. Full raw output: `w2/stage/ConnDocsSources/graph_check.out`.

| # | edge | status | evidence (file:line) |
|---|---|---|---|
| 1 | M: S897 → D1 → lane S897 | OK | `ScoutIdMap.md:11`; L line 19 |
| 2 | M: S903 → D2 → lane S898 | OK | `ScoutIdMap.md:12`; L line 20 `(staged S903, tier A)` |
| 3 | REG: S897 and S898 unused in base; base 820 rows, unique ids, max S896 | OK | `base SOURCES` grep `^\| S89[78] \|` → 0 |
| 4 | URL D1 identical in R1 cell, E, L | OK | R1 cell 1; E line 3; L line 19 |
| 5 | URL D2 identical in R2 cell, E, L | OK | R2 cell 1; E line 4; L line 20 |
| 6 | E: exactly one `- source:` per adopted doc (S897, S898) | OK | E lines 3–4 |
| 7 | E: only lane ids cited; legacy S886/S888/S889/S890/S891/S896 and S903 absent | OK | `grep -o S[0-9]{3}` on E → S897, S898 only |
| 8 | E: one physical `- topic:` line | OK | E line 11 |
| 9 | E quotes: every CJK span locates in D1 stored text | OK | 13/13 (ellipsis span split on `…`); `ScribeEntryA/d1-live.text` |
| 10 | E quotes: every English span locates in D2 stored text | OK | 8/8 in `d2-live.text` and `RevQualityFit-2/D2-onomastica.txt` |
| 11 | E locators D1: opening / §一 / §二 / §四 | OK | quote positions in `d1-live.text`: opening 240–252; §二 635; §一 380, 608; §四 1466–1506; headings at 289, 634, 997, 1456 |
| 12 | E locators D2 pages (PDF = journal −110): 88-term, 10-word scope, §2 labels → p4/114; 2,500 and 17-term lead-in → p5/115; list heading → p6/116; "Six of these" → p11/121; "frequency position" → p12/122 | OK | `d2-live.text` form-feed pages; running heads 114 (p4), 115 (p5), 116 (p6), 121 (p11), 122 (p12) |
| 13 | E §8 sha/bytes D2: live = capture 20260901045105 = `5d1bfa5a…29bc`, 417093; capture 20251231111748 = `1b4c60f2…2ff9`, 546440 | OK | `ScoutDocS898/evidence.txt:7,10` |
| 14 | E §8 CDX sizes: 41417 (D1 cap), 406446 and 426128 (D2 caps) | OK | `ScribeEntryA/fetch-log.txt` CDX rows |
| 15 | E outbound couples: naming-systems, toponymy-place-names, semantic-fields-lexicon-building exist at base | OK | base blob check |
| 16 | E outbound pipeline anchors: base §2, §6, §7 and steps 2 "Slot inventory" and 4 "Lexify" exist | OK | base `naming-systems.md` lines 44, 87, 109, steps 2 and 4 |
| 17 | E outbound "~ancient" row (§7 line 107) | OK | base `naming-systems.md:54` |
| 18 | R1 tier == L and E tier (B) | **FAIL** | R1 cell 3 = `A`; L line 19 `tier B`; E line 13 `tier B for the claims used here`; claims D1 `tier B` |
| 19 | R1 status cell == per-UA record (plain 403, browser 200) | **FAIL** | R1 cell 1: `live answered HTTP 403 to both the plain and the browser-shaped request`; `ScoutDocS897/evidence.txt:8–9` (browser 200, 143252 B); `SentinelSources/receipts/s897-live-probe.txt` (browser 200 each run) |
| 20 | R1 anchor names the same located source as L/claims (browser-UA live copy) | **FAIL** | R1 cell 5: `capture 20240111092427, article body`; L line 19 `browser-UA live copy is the located source` |
| 21 | R1 recheck == E recheck | **FAIL** | R1 cell 9 `365d`; E line 6 `recheck: 180d` |
| 22 | R2 recheck == E recheck | **FAIL** | R2 cell 9 `365d`; E line 6 `180d` |
| 23 | R2 opened == evidence access-date == E/L date | **FAIL** | R2 cell 8 and L line 11 `2026-10-27`; `ScoutDocS898/evidence.txt:32` `access-date: 2026-10-28`, line 8 `fetched: 2026-10-28T01:26:13Z` |
| 24 | R1 opened == evidence access-date | OK (note) | `ScoutDocS897/evidence.txt:39` `2026-10-27`; line 6 `fetched 2026-10-28T01:31:09Z` (UTC rollover, see X5) |
| 25 | R2 author == PDF author | **FAIL** | R2 cell 1 `Kałużyńska, Iwona (2025)`; `d2-live.text:55` `Irena Kałużyńska`; `pdfinfo` Author `Irena Kałużyńska` (`w1/ScoutDocS898.md:15`); E and L say Irena |
| 26 | D1 institution: E line 3 == R1 cell 1 / L line 19 | **FAIL** | E line 3 `中國社會科學院古代史研究所` (copyright footer `d1-live.text:2952`); R1 cell 1 and L line 19 `中国社会科学院 历史研究所` (page title line 1) |
| 27 | E line 6 "both HTTP 200 to a plain client" == E §8 + recheck detail | **FAIL** | E line 6 vs E line 8 (`curl/8.7.1` → 403, 162 B) and `ScoutDocS897/evidence.txt:8` |
| 28 | E §8 "no wall is recorded against it" == R1 "wall met, not passed" and EV "challenge: ua-gate … met, not passed" | **FAIL** | E line 111 vs R1 cell 1 and `ScoutDocS897/evidence.txt:32`; capture under browser UA returned HTTP 429 "suspected abusive bot traffic" (`ScribeEntryA/fetch-log.txt:11`, `:37`) — not recorded in E |
| 29 | EV S898 header quote-words/chars == quote line | **FAIL** | `ScoutDocS898/evidence.txt:13–14` `quote-words: 10`, `quote-chars: 65`; line 42 quote is 17 words / 111 chars |
| 30 | E §10 back-edge: base `naming-systems.md` points to amend via `couples:` | **FAIL** | `git -C … grep 'amend-2026-10-23' 211f952… -- corpus/knowledge/linguistics/naming-systems.md` → no hits in `naming-systems.md` (the README hits belong to other amendments). E line 123 claims otherwise |
| 31 | B README row body == E topic line (verbatim) | **FAIL** | `readme-plan.md:29` body is the round-4 staged topic (plan lines 32–34 cite staged file lines 10–14), not E line 11 |
| 32 | B heading `## linguistics/ (N)` == live count after landing | **FAIL** | `readme-plan.md:16` requires `(33)`; L line 86 `named stale and left as filed`; L line 96 routed item 3 open. r76 INDEX grades all headings against live counts (`ScoutReadmeIndex.md:14`) |
| 33 | B footers: five base `Total knowledge entries` blocks 243/247/249/252/253; plan adds 254; partition sum 253 → 254 | OK | base lines 755/798/819/830/834; partitions civilizations 95, culture-material 41, linguistics 32, myth-symbol 32, synthesis 29, verification 24 = 253 |
| 34 | claims cite `corpus/CORPUS.md` ("CORPUS.md rule 1") | **FAIL** (low) | `corpus/CORPUS.md` absent at base; only `reports/round-33/adj/A05-corpus.md` matches `corpus.md` |
| 35 | R1/R2 used-by == E path | OK (string); PENDING (file) | both cells `corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`; file absent until C-lands |
| 36 | L S897 Gate quote and locator cells | PENDING | L line 19 `L1-FILL`; `ScoutDocS897/evidence.txt:15,30,45–49` already holds the quote (23 chars), `chars=2617` window, locator "lead paragraph 2, sentence 3" |
| 37 | lane `reports/round-77/evidence/S897.txt`, `S898.txt`, census-end, frozen map | PENDING | absent at draft; committed by L1 |

Rows 1–17, 24 and 33 are the verified-OK set. Rows 18–23, 25–32 and 34 are FAILs (15 rows). Rows 35–37 are PENDING, or string-match only.

## Dangling or contradicted edges (explicit)

- **X1 — S897 row tier.** R1 cell 3 says `A`; the Gate, the entry, and the claims say `B`. The claims' tier reason (its periodization is its own argument; institutional reprint; no printed pages) is the reason for B. Correct R1 cell 3 to `B`.
- **X2 — S897 row status.** R1 cell 1 still records the superseded 22:22 text ("HTTP 403 to both"). Replace with the per-UA record: plain curl 403 (162 B), browser-shaped 200 (143252 B), capture 20240111092427 200 (143457 B). The lesson already records this (L lines 24–26) and says the 22:22 text is superseded.
- **X3 — S897 located source.** R1 cell 5 locates the quote in the capture; L line 19 and the claims locate it in the browser-UA live copy. Choose one, and make the row, the Gate, and the evidence file name the same one.
- **X4 — recheck windows.** Both rows carry `365d`; the entry carries `180d` (line 6). Make one value. The entry's recheck detail (re-open both rows with the stated requests) is the operational one, so the row should take `180d` unless the claims say otherwise.
- **X5 — access date.** L, R1, R2, and E say `2026-10-27`. `ScoutDocS898/evidence.txt:32` says `access-date: 2026-10-28` (fetched `2026-10-28T01:26:13Z`); `ScoutDocS897/evidence.txt` fetched `2026-10-28T01:31:09Z` with access-date `2026-10-27`. Use one date everywhere; if the UTC timestamp is the truth, the row's `opened` must say `2026-10-28` and the entry and lesson must follow.
- **X6 — S898 author.** R2 cell 1 says `Iwona`. The PDF says `Irena Kałużyńska` (`d2-live.text:55`, pdfinfo author). Correct to `Irena`.
- **X7 — D1 institution.** E line 3 names the copyright-footer institute (`中國社會科學院古代史研究所`, `d1-live.text:2952`). R1 cell 1 and L line 19 name the title-line institute (`中国社会科学院历史研究所`, `d1-live.text:1`). Both are on the page. Pick one, or name both in the same form in E line 3 and R1 cell 1.
- **X8 — entry line 6 false per-UA claim.** "Both documents answered HTTP 200 to a plain client on 2026-10-27". D1 plain is 403 (E lines 7–8, §8 line 111). Replace with the per-UA record: D1 plain 403, D1 browser 200; D2 plain 200.
- **X9 — entry §8 wall claim.** E line 111 says "no wall is recorded against it" and "no automation". R1 cell 1 and the evidence say a wall was met and not passed (`challenge: ua-gate`). The archive capture under the browser UA returned 429 "suspected abusive bot traffic" on the first attempt (`fetch-log.txt:11`). State both.
- **X10 — S898 evidence header.** `ScoutDocS898/evidence.txt:13–14` says 10 words / 65 chars; the quote on line 42 is 17 words / 111 chars. The committed `reports/round-77/evidence/S898.txt` must carry the 17-word form, as the lesson's routed item 1 requires.
- **X11 — claimed back-edge.** E §10 (line 123) says the base `naming-systems.md` "points here through its `couples:` line" and that the amendment "appends to" it. The base file has no reference to the amend, and the claims adopt exactly one file. Remove the claim, or state the follow-up as not made this round. E line 14 (`couples`) likewise states edits to the base §2 and §7 that this round does not make.
- **X12 — claims → CORPUS.md.** `CLAIMS-DRAFT.md:12` cites `CORPUS.md rule 1`. `corpus/CORPUS.md` is absent at base. Cite the rule's real location or drop the reference (low).
- **X13 — README row body.** `readme-plan.md:29` uses the round-4 staged topic. The landed row must equal E line 11 verbatim, because `accept-c.py:4375–4386` reads only the one `topic:` line. Replace the row body with E line 11, minus the `- topic: ` prefix. Without this the INDEX leg is red whatever the row says.
- **X14 — README heading.** The plan (line 16) requires `## linguistics/ (33)`; the lesson (Census line 86; routed item 3 line 96) says leave `(32)` "stale and left as filed". Under the r76 INDEX rule the lesson's choice fails (live count 33). Bump the heading and say so in the lesson; the footer stack stays append-only.
- **X15 — pending landing targets.** E path (used-by in R1 and R2), `reports/round-77/evidence/S897.txt`, `S898.txt`, `reports/round-77/telemetry/census-end.txt`, and the frozen by-document map are absent at draft. These are owed at C-lands, not defects of the drafts. Also owed: L line 19 quote and locator cells (`L1-FILL`), which `ScoutDocS897/evidence.txt` already supplies.
- **X16 — E §9 points at non-lane locations.** E line 119 says the round-3 material is "left where it lives — in the staged corpus and in the lane's sour[ces]". Neither is a lane path, so a reader cannot resolve it. Remove the pointer, or name a real repository path.
- **X17 — refused and held candidates have no registry node.** S933, S934 (same document as D2), S936 (same document as S918), and the held S906–S988 chain are recorded only in the lesson table (L lines 37–41). Base convention keeps rejected rows: 37 base rows have status `rejected` with reason and flip. The claims' target (822) adds none. This is a claims-level decision: either register the refusals as `rejected` rows (and move the target) or state in the claims why this round does not.
- **X18 — two same-page captures for D2.** E line 6 names `20251231111748` as the D2 same-page capture for recheck. E lines 4 and §8, the Gate (L line 20), and `ScoutDocS898` pair the live copy with `20260901045105` (byte-identical). R2 cell 1 lists both. Pick one for the recheck edge; the byte-identical one is the defensible pair.
- **X19 — plain-UA version string.** E line 8 and §8 line 111 say `curl/8.7.1` (from `ScribeEntryA/fetch-log.txt`). The committed-evidence probes used `curl/8.11.1` for D1 (`ScoutDocS897/evidence.txt:8`) and `curl/8.23.0` for D2 (`ScoutDocS898/evidence.txt:4`). Cite the version of the probe that the evidence file records (low).
- **X20 — tier split for D2.** R2 scope and tier cell gives tier A for the whole row; E line 13 grades the 88-term figure tier B and the 17-lexeme list tier A. The scope column carries no split. Either add the split to the row scope or drop it from E (low).

## Quote and locator checks (raw)

Commands and outputs are in `graph_check.out` (edges 9–10) and the inline probes below. The inline probes were run from the W1 stored texts and are not saved as separate files.

- D1 CJK spans (13 entries, including one `…` elision): every part found in `w1/stage/ScribeEntryA/d1-live.text` after whitespace folding. Output line: `located=13 unlocated=0`.
- D2 English spans (8): `d2-live.text` and `RevQualityFit-2/D2-onomastica.txt` both `8 of 8`.
- D2 page check: `pages = text.split('\f')`; the 88-term sentence, "among the names…", "standard given names…", "given names with lexemes denoting…" are on page 4 with running head `114`; "2,500 characters…" and "the 17 terms/characters listed…" on page 5 with head `115`; the §4 heading on page 6 with head `116`; "Six of these seventeen terms are absent" on page 11 with head `121`; "The frequency position of the other 9 terms is now lower" on page 12 with head `122`.
- D1 section map by character position in the whitespace-folded text: opening sentences at 240–252; §二 "南方地區華夏式姓名的使用是文化接觸的結果" at 635; §一 closing "普通民眾…單名、雙名並存" at 608; §四 items at 1466–1506; headings `一、` at 289, `二、` at 634, `三、` at 997, `四、` at 1456.
- Base registry: `grep -cE '^\| S[0-9]+ \|'` → 820; duplicates 0; `^\| S89[78] \|` → 0.
- Base README: footers at 755/798/819/830/834; partitions 95/41/32/32/29/24.

## Verified OK (summary)

- Two documents ↔ two lane ids ↔ two rows; each row used-by is the entry path (string match). S934 and S936 are duplicates of D2 and D1-adjacent W1 artifacts, not lane nodes (X17).
- Entry source lines: exactly one per adopted document; no legacy id; no S903.
- Quotes: all 13 CJK and 8 English spans locate verbatim in the stored texts.
- D2 locators (PDF p4/114, p5/115, p6/116, p11/121, p12/122) match the printed running heads.
- D1 locators match the section order and heading positions.
- D2 hashes and byte counts in E §8 equal `ScoutDocS898/evidence.txt`; CDX sizes equal `fetch-log.txt`.
- Base: 820 rows, S897/S898 unused, no duplicate ids; partition counts sum to 253; plan arithmetic 254 = 253 + 1 and 33+32+41+29+24+95 = 254.
- Outbound: all three couples targets and the §2, §6, §7 anchors exist at base; "~ancient" row at base line 54.

## Commands run (all read-only against the lane; `-C` explicit)

- `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse --show-toplevel` → `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
- `git -C <lane> show 211f9526…:corpus/SOURCES.md` and `…:corpus/README.md` → scratch copies (953 and 836 lines)
- `git -C <lane> show 211f9526…:corpus/knowledge/linguistics/naming-systems.md` for back-edge, anchors, `~ancient`
- `git -C <lane> cat-file -e 211f9526…:<path>` for couples targets, `corpus/CORPUS.md`, reports paths
- `git -C <lane> ls-tree --name-only 211f9526… corpus/knowledge/<d>/ | grep -c '\.md$'` per partition
- `python3 -B …/w2/stage/ConnDocsSources/graph_check.py > …/graph_check.out` → exit 0, `TOTAL 40 {'OK': 19, 'FAIL': 15, 'PENDING': 6}`
- inline `python3` probes for quote location, page map, and D1 section positions (outputs quoted above)

## Installs and cleanup

- Installs or updates: none. `pacman` was not run. `RULES.md` was read; no tool was needed.
- Writes: this report; `w2/stage/ConnDocsSources/graph_check.py`, `graph_check.out`. No lane git/jj/index writes. No fleet-root writes. No LOG.md, SCORECARD.md, SKILL.md, SHONEN.md, or corpus production file touched. No subagents, no background jobs.
- Scratch `/fast/scratch/hyaku/kotodama-r77/ConnDocsSources` deleted before yield.

## Checks for the main agent after landing

1. Re-run the checker's FAIL edges against the landed files (the script reads the drafts; repoint `W1` paths to landed `corpus/` and `reports/round-77/` paths).
2. Confirm the S897 and S898 evidence files reproduce E quotes and the 17-word window at PDF p4.
3. Confirm `corpus/README.md` `## linguistics/` reads `(33)` and the new footer is last; confirm the row body equals the entry's `- topic:` line.
