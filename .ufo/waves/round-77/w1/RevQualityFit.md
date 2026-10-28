# RevQualityFit-2 — QUALITY fit of the adopted entry (round 77, wave 1)

Seat: RevQualityFit-2 (leaf). Judged object: staged entry
`/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`
(read-only source tree) against lane `corpus/QUALITY.md` criteria 1–29 at base
`211f9526800906e0c585d878d265c37e5e090c15` (lane HEAD == base, verified below).
No staged file, registry, or claim was edited; all lane reads were read-only.

## 0. Base constants (draft COUNTS inputs re-derived)

- 253 knowledge .md at base — `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree -r --name-only 211f9526800906e0c585d878d265c37e5e090c15 -- corpus/knowledge | grep -c '\.md$'` → `253`. Draft's "253 → 254" ✓.
- 820 registry rows at base — `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 211f9526800906e0c585d878d265c37e5e090c15:corpus/SOURCES.md | grep -cE '^ {0,3}\| S[0-9]{3,} '` → `820`. Draft's "820 → 822" ✓ (820+2).
- lane HEAD — `git -C … rev-parse HEAD` → `211f9526800906e0c585d878d265c37e5e090c15` (worktree reads equal base).

## F1 (FATAL for the staged bytes as filed) — the retained "Superseded passage" block cites six staged ids that name DIFFERENT documents in the lane registry

The staged file instructs "Its cited rows stay cited, and its text is preserved below as the dated record" and carries staged ids S886, S888, S889, S890, S891, S896 in the second block. In the lane registry those ids are round-76/other-round rows for other documents:

| staged id (staged doc) | lane id's actual document |
|---|---|
| S886 (kotobank 苗字, 世界大百科事典) | Tzvetan Todorov, «Les catégories du récit littéraire», Communications 8 (lane `corpus/SOURCES.md` row 841) |
| S888 (NDL OpenSearch 日本人名大辞典) | 中国社会科学院大学《叙事学》课程大纲 PDF (row 843) |
| S889 (kotobank 日本人名大辞典+Plus) | 小方孝「物語生成の物語論…」Cognitive Studies 25(2) (row 844) |
| S890 (doi 10.34158/ONOMA.51/2016/8) | 村井源「物語構造の階層的記述方式の提案」情報知識学会誌 32(2) (row 845) |
| S891 (doi 10.5195/names.2021.2314) | Barthes, S/Z excerpt at unige.ch (row 846) |
| S896 (journal.kci.go.kr ART001409716) | 光明日报「农历编算有了国家标准…」(row 851) |

The DRAFT's frozen map covers only S897→S897 and S903→S898, and its row_set is exactly 2 rows (820→822). Keeping the retained block therefore (a) cites six lane rows for claims those rows do not support — QUALITY 1 provenance failure; (b) fails the round-76 REPOINTED-class check ("every inline S-id resolves to a frozen row; no campaign-namespace id cited as a lane row except the staged→lane substitutions in the frozen map; no unrelated staged id is preserved", `reports/round-76/accept-c.py:1758-1762`); (c) makes the entry cite six unopened/unregistered documents. **The lane rewrite must drop the superseded block** — the staged file itself licenses this ("Trim it if the later entry supersedes it outright") — and record the drop in the Gate, or the plan must grow to 8 rows (contradicting the frozen ONE-entry/2-row claim; that is the L1's call, not mine).

## F2 (DRAFT DATA CELL FALSE) — D1's "HTTP 403 wall both UAs" is contradicted; the wall is UA-gated the plain way

CLAIMS-DRAFT.md D1: "(live: HTTP 403 wall both UAs at L1 probe; Wayback capture 20240111092427 status 200 exists — ordinary means via capture)". Measured 2026-10-27 from this seat, plain requests only, `http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml`:

- `curl -sS -A "curl/8.x" -o /dev/null -w "HTTP %{http_code}, %{size_download} B\n"` → `HTTP 403, 162 B` (wall present)
- `curl -sS -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -o /dev/null -w …` → `HTTP 200, 143252 B` (wall absent, full page served)

QUALITY 22's own decision table: "a wall present under the plain UA and absent under the browser UA voids the reject and the source is re-opened by ordinary means". So: no wall-based reject of D1 is available, and the row's opening story should be **live page opened under the browser-shaped UA (plain request, `automation: none`) plus the same-page capture pair**, not "capture-only via 403". The Gate record must bind each UA to its own response in the QUALITY 22 line shape (`UA "…" -> HTTP 403, 162 B, wall present` / `UA "…" -> HTTP 200, 143252 B, wall absent`). CDX check of the draft's capture claim: `curl -sS "http://web.archive.org/cdx/search/cdx?url=lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml&output=json&limit=5"` → one row, `20240111092427`, status `200`, `text/html` ✓. D2 CDX: two captures `20251231111748` (426128 B) and `20260901045105` (406446 B), both `application/pdf`, status 200 ✓ — note the two D2 digests differ; the row must name the capture it actually quotes.

## F3 (per-criterion verdicts on the staged text)

1. **Provenance — PARTIAL FAIL.** Bullets carry their S-ids; but the "88 plant, flower and tree terms" figure is attributed INSIDE the opened paper to a second document: D2 §3 reads "According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees …" (pdftotext line 151), and the §3 frequency data comes from 《姓氏人名用字分析统计》 (Yuwen Chubanshe 1991, PRC 1982 census) plus a naming website. The entry line must carry the in-paper attribution (or the 2008 work must be opened and registered — outside the frozen 2-row plan). No `(to-verify)` laundering either way.
2. **Calibration — FAIL (missing).** No status clause anywhere. Kałużyńska's subcategories are one scholar's scheme built on the Xingshi statistics and internet data, and 魏斌's structure account is one study; the rewrite must name status with reason (QUALITY 2).
3. **Coupling — FAIL (dangling path).** `- couples:` names `culture-material/era-periodization-models.amend-2026-10-23.md`, which exists in the staged tree but NOT in the lane (lane holds only `era-periodization-models.md`; this round lands ONE entry). Rewrite must re-point couples to lane-existing paths (`linguistics/naming-systems.md`, `linguistics/toponymy-place-names.md`, `culture-material/era-periodization-models.md`).
4. **Usability — WEAK.** §N+2 gestures ("a name lexicon can be tabulated … checkable against a list") but no table, checklist or worked example exists in the text. The rewrite must land the actual artifact (natural: the 17-lexeme list as a typology table with lexeme class / frequency / cultural reading) — keeping S-ids out of table rows (criterion 15 TABLE-ID).
5. **Canon hygiene — PASS.** "it decides no culture's names" + explicit scope line.
6. **Tier scoping — see §F4.**
10. **Opened by ordinary means — entry-side N/A, draft-side defect F2** (the entry records no access means at all; the lane Gate must, per F2's UA-bound record).
12/16. **Recheck staleness — FAIL as carried.** Staged S897's recheck command (`curl -fsSL '<live cssn>' | grep -c '後起的文化習慣'` → 1, ran 2026-10-23) is no longer reproducible: the live URL answers 403 to the command's default UA (F2). Staged S903's recheck (`… -o /tmp/o.pdf && pdftotext … | grep -c 'Kałużyńska'` → 13) counts author-name occurrences only — presence, not scope — and hardcodes /tmp. The lane rows must re-derive scope-bound spans this round against named artifacts, with the cadence-only recheck cell and command+output in the Gate.
15. **Cited-lines clause scope — FAIL (measured).** `python3 -B tools/check-cited-lines.py <staged copy>` →
   ```
   MULTI-ID …:7 S897,S903
   MULTI-ID …:47 S886,S888,S889,S890,S891,S896
   MULTI-ID …:58 S888,S889
   CITED-LINES: 3 finding(s) in 1 file(s)
   exit=1
   ```
   (line 7 = the entry's own `recheck:` line "(S897 -> 1, S903 -> 13)"). One id per cited line in the rewrite.
18. **Row anchors resolvable — PARTIAL FAIL in staged S897.** The anchor cell names 「引言」 — `grep -c -o '引言'` on the served capture = **0**; the second phrase 華夏式姓名習慣 locates (count 1), and the structure claims locate near-verbatim (capture carries 「名的使用要早于姓，兩者組合是一種後起的文化習慣」 and 「春秋戰國以降…穩定的華夏式姓名習慣，即"姓（氏）+名"」). The lane row must anchor to spans present on the named artifact (e.g. 後起的文化習慣) and drop 引言. D2's anchors (§2; §3–§4) locate: §4 heading "4. LIST OF THE 17 MOST COMMON LEXEMES/CHARACTERS" (pdftotext line 211) ✓.
29. **Filed numbers — satisfied in this report** (every number above carries its command; unrun checks stated as unrun).

**Passing mechanically:** nine-field provenance header (source ×2, verified-at, recheck, ground, topic, gap filled, sources, couples, scope — `norm_label` maps "gap filled"→`gapfilled` = "gap-filled"; `reports/round-76/accept-c.py:243,295-296`); no placeholder values. **Word floor — PASS, derive, don't copy:** staged body under the counter rule (first `^## ` to EOF, headings removed) = **533 words** (`awk` over a scratch copy); first block alone = **352**; the round-77 base derives the floor as **208** (smallest = `culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md`; derivation loop over all 253 base files, command in receipts). The round-76 constant 478 is round-76's own base derivation and must NOT be frozen as round-77's gate.

**Leg-set note:** the draft's C leg list omits REPOINTED and CITEDLINES (round 76 carried both). Whatever freezes, criterion 15's lint binds independently, and dropping the REPOINTED function removes exactly the check that catches F1's collisions — the freeze should keep their functionality (COLLCHECK's by-document compare does not substitute for per-line id resolution).

**Draft wording defect (freeze-time):** the rejection of `naming-systems.amend-2026-10-24.md` reads "S934 is the same onomastica document as D2 — a document-level duplicate, refused (flip: it is a different document than D2)" — the flip cell as written contradicts the reason. State the flip as the considered-and-refuted alternative (e.g. "flip considered: a different document than D2 — refuted by <evidence>").

## F4 — Tier verdicts (criterion 6, claim-scoped)

- **S903 (Kałużyńska 2025, Onomastica LXIX) — tier A JUSTIFIED**, scope narrowed. The staged scope cell is right that this is the author's own classification, published open access in the field's own journal (Onomastica / IJPPan), and SOURCES.md tier A names "original paper". Verified on the opened artifact: §2 "CHINESE FEMALE GIVEN NAMES WITH LEXEMES DENOTING …" (line 97), §4 "LIST OF THE 17 MOST COMMON LEXEMES/CHARACTERS" (line 211) — the 17-list and the subcategory scheme are the paper's own. **But the 88-term count is NOT the 2025 paper's own finding** (F1-class attribution to Kałużyńska 2008 pp. 223, 232, with Xingshi-1991 + internet-site data): tier A holds for the paper's own classificatory statements; the 88 line must be worded as reported-by (or the 2008 work opened — not in the frozen plan). Live open: HTTP 200 (417093 B fetched this seat); captures 200.
- **S897 (魏斌〈單名與雙名…〉, cssn.cn) — tier B ADMISSIBLE and recommended, but the row's stated reason is the wrong axis.** The staged reason ("a scholarly article on the CASS's own site, not a peer-reviewed venue of onomastics") grades venue prestige, which is not the A/B axis; primary-for-scope is. The document is 魏斌's own study — primary for its own claims — so tier A would be available only for the version-of-record; what is opened is the CASS history-institute portal copy as served (no 参考文献 apparatus on the page: `grep -c -o '参考文献'` → 0; footnote marks [5][6][7] present), live URL UA-gated (F2). Tier B scoped to the portal-served copy, with the row naming which artifact it rests on, is the honest filing.

## F5 — Must-satisfy list for the lane rewrite before admission

1. Drop the superseded round-3 block (six colliding staged ids, F1); record the drop in the Gate.
2. One S-id per cited line (fix the line-7/47/58 classes, F3.15); renumber S903→lane S898 everywhere including prose mentions ("from S903" bullets).
3. Re-point `- couples:` to lane-existing paths (F3.3).
4. Carry the 2008 attribution on the 88-count line; keep S903's tier-A scope to the paper's own statements (F3.1, F4).
5. Add the calibration/status clause (F3.2).
6. Land a real usability table, S-id-free rows (F3.4).
7. Rows: live URL + same-page capture per row (QUALITY 18); D1 Gate record binds both UAs per QUALITY 22 with `automation: none` (F2); anchors anchored to spans present on the named artifact (F3.18).
8. Rechecks re-derived this round against named artifacts; cadence-only recheck cell in the row; no /tmp hardcode (F3.12).
9. Word floor holds post-drop (352 ≥ 208) — no filler needed, but no 478 constant either (§F3).

## Receipts

Copied to `.ufo/waves/round-77/w1/stage/RevQualityFit-2/`: `D1-cssn-20240111092427.html` (143457 B fetch), `D2-onomastica.txt` (pdftotext extraction of the live PDF, 417093 B fetch), `lint-staged.txt`, `fetch-log.txt` (exact curl commands + outputs). Scratch under `/fast/scratch/hyaku/kotodama-r77/RevQualityFit-2/` deleted after the copy.

**Unrun checks (reported as unrun):** no CDX probe of redirect/canonical slugs beyond the exact URLs (none needed — captures claimed and confirmed, not denied); no second fetch pass or retry budget exercised (single pass per URL, 2026-10-27); D2's §5 conclusions and the 17-item list contents were not transcribed item-by-item (L1's evidence captures will own the located quotes); the lane's round-77 counter does not exist yet, so no counter was run.
