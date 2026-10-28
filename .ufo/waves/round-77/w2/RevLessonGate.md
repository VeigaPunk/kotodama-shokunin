# RevLessonGate — wave-2 falsifier review, round 77

Seat scope: review the lesson draft `## Gate` (`.ufo/waves/round-77/w1/drafts/corpus/lessons/round-77.md`, lines 9–49) and the staged S897/S898 evidence. Confirm per row: exact URL, access date, ≤25-word quote, locator, D2 p.4/114, per-UA response; confirm a non-author spot-check plan exists covering ≥1 admit and ≥1 reject. Report corrections. Per assignment, the spot-check plan was confirmed to exist — no spot-check was performed and none is claimed.

## Assignment checklist — results

| check | result |
|---|---|
| S897 row: exact URL | OK — live `http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml` + same-page capture `…/20240111092427id_/…` identical to claims D1 and to `w1/stage/ScoutDocS897/evidence.txt:2-3`. |
| S897 row: date | OK — `2026-10-27`. Fetches ran `2026-10-28T01:26–01:31Z` = `22:26–22:31` local `-03` on 10-27; convention consistent. |
| S897 row: quote ≤25w | **L1-FILL in the row** — fill is staged, verified: `名的使用要早于姓，兩者組合是一種後起的文化習慣` (23 chars; `wc -w`=1, segmented ≈11 — ≤25 either way), verbatim in the 143457-byte capture (`SentinelSources/receipts/s897-capture-quote.txt:9-13`, grep count 1). |
| S897 row: locator | **L1-FILL in the row** — staged: `article lead (unnumbered introduction, ¶2–4), before heading 一、單名與雙名; quote = lead ¶2 sentence 3` (`ScoutDocS897/evidence.txt:30`). Verified in the stored window: the quote is the third `。`-terminated sentence of lead ¶2 (the `「人之有名，以相紀別」` epigraph ends `，`); footnote markers `[5]`/`[6]` flank as recorded. |
| S897 row: per-UA response | OK — plain `curl` UA → `403 text/html 162` WAF page; browser `Mozilla/5.0 … Chrome/130.0` UA → `200 text/html 143252`. Consistent across three independent records: lesson receipt-05 (`stage/ScribeLesson/receipt-05-probes.txt:3-4`), `ScoutDocS897/evidence.txt:8-9` (UA `curl/8.11.1`, 403 ×2 sha256 `1d08335e…`), `SentinelSources/receipts/s897-live-probe.txt:2-12` (UA `curl/8.23.0`, 403/200 each ×2). No both-UA-blocked claim. |
| S898 row: exact URL | OK — live `https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/` + same-document capture `20260901045105id_`; byte-identity corroborated by sha256 `5d1bfa5a5f01bee6…` (417093 B) for both in `ScoutDocS898/evidence.txt:7,9` and `w2/stage/ExecCapEvidence/S898-candidate.txt:69,83`. |
| S898 row: date | OK — `2026-10-27`. |
| S898 row: quote ≤25w | OK on count — `wc -w` of the stored quote = 17 words / 111 chars (measured in scratch). Verbatim 5-word gate quote `there were altogether 88 terms` is also present. |
| S898 row: locator = D2 p.4/114 | **Confirmed independently.** `ScribeMistakes/d2-locator-sweep.txt:10-23`: `altogether 88` hits = 1 on PDF p.4, 0 on all other 12 pages; `p4.txt:1` = journal label `114`. Stored D2 text (`RevQualityFit-2/D2-onomastica.txt:151`) places the sentence as §3 ¶1 sentence 2 — matches the row's `journal p. 114 / PDF p. 4` and supersedes the 22:33 claims' p.115/PDF p.5. |
| S898 row: per-UA response | OK — single-UA record, no wall: `challenge: none` (`ScoutDocS898/evidence.txt:25-26`). QUALITY 22's binding field governs wall/refusal records only; D2 needed none. |
| Spot-check plan ≥1 admit | **Present** — `round-77.md:49`: admit side vs `reports/round-77/evidence/S897.txt`/`S898.txt`, URL+quote+locator in stored window, explicit note the D2 window must reach PDF p.4. |
| Spot-check plan ≥1 reject | **Present and real** — reject side vs S934: staged row names Słon «Names and the named: gender…Poland», Onomastica 68 (`/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md:82`) while its own capture `20251231111748id_/…/574/763/` serves Kałużyńska LXIX 2025 (546440 B, sha256 `1b4c60f2…` — `ScoutDocS898/evidence.txt:10`). The misdescription is verified, so the plan checks a live target. |
| Spot-check not claimed performed | OK — `round-77.md:49` is `L1-FILL — required before this Gate is closed`; plan only. |

## Findings (corrections)

**F1 (medium) — spot-check plan names the wrong round/file.** `round-77.md:49` assigns the check to a "round-78 verifier" recording into `corpus/lessons/round-78-verifier-spotcheck.md`, yet marks it "required before this Gate is closed." Base convention (`git show 211f9526:corpus/lessons/`, files `round-49-`…`round-76-verifier-spotcheck.md`): `round-N-verifier-spotcheck.md` is authored by round N's non-author closure and contains round N's check — round 76's file embeds the wave-2 RevLessonGate check *within* round 76 (`corpus/lessons/round-76-verifier-spotcheck.md`, author "hyaku closure (non-author integrator)"; check restated in `round-76.md:23`). Under that convention the record belongs at `corpus/lessons/round-77-verifier-spotcheck.md` by round 77's own non-author verifier. As written, either the gate waits for a future round (gate never closes) or the record lands misfiled under round 78. Correct actor/file to round-77, or drop "required before this Gate is closed" if a cross-round check was intended.

**F2 (medium) — S898 quote cell is the folded span; staged artifacts disagree on the convention.** The row's quote is the 17-word sentence `"According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees"`. In the PDF text it folds across a line break (`…88 terms\ndenoting…`), so it is **not verbatim-contiguous**: the claims themselves say "folded across a PDF line break, not claimed verbatim" and name `there were altogether 88 terms` as the "(verbatim, 5 words)" gate quote. The staged evidence files now carry two different shapes: `ScoutDocS898/evidence.txt:12` calls the 17-word span `quote-found-verbatim: yes / matched=verbatim` (contradicts the fold), `ExecAdaptCapture/dryrun/S898-P4.txt:17,51` calls the same span `quote-found-verbatim: no / matched=folded`, and `w2/stage/ExecCapEvidence/S898-candidate.txt` resolves it the claims' way — `quote:` = the 5-word verbatim span, the 17-word sentence demoted to `anchor-quote`. The Gate row is silent on the distinction ("stored … and located" admits folded matches, so the row is defensible, but the committed `S898.txt` and this row must settle one shape). Correction: carry the 5-word verbatim span as the row quote with the 17-word sentence as named anchor (the w2 candidate's shape), or record `matched=folded` explicitly.

**F3 (low) — `ScoutDocS898/evidence.txt` header metrics describe the superseded quote.** `quote-words: 10`, `quote-chars: 65` (line 13-14) while `quote:` (line 42) holds the 17-word/111-char sentence (measured: `wc -w`→17, `wc -m`→111; 10w/65c matches the dropped tail `there were altogether 88 terms denoting plants, flowers and trees`). Also `access-date: 2026-10-28` (line 32) conflicts with the round's local-date convention: its own `fetched: 2026-10-28T01:26:13Z` = `22:26 -03` on 10-27, and every sibling artifact (lesson, ScoutDocS897, both capture candidates) uses `access-date: 2026-10-27`. Both corrections belong in the committed `reports/round-77/evidence/S898.txt`.

**F4 (low) — provenance of the byte-identity claim.** `receipt-05-probes.txt:9-12` records only status/bytes for D2 (417093 / 546440 / 417093); the "this seat re-derived `cmp` silent and one sha256 for both" step lives in `ScribeLesson.md` G6, not in the receipt the row cites as "full receipt". Support is elsewhere (`ScoutDocS898` identical live/wayback sha256 lines; `S898-candidate.txt` response-bind lines) — cite it, or add the cmp/sha256 lines to the receipt.

**F5 (low) — unattributed detail in the per-UA record.** Row note "(nginx `403 Forbidden`; status and size only, body not retained)": receipt-05 retains status+size only, so the `nginx` banner identification cannot come from it — it is ScoutDocS897's observation (`evidence.txt:8`, "162-byte nginx '403 Forbidden' page"). Cite the scout record for the banner, or the parenthetical misattributes.

**F6 (informational) — per-UA binding complete where required, preamble overpromises.** The only wall case (D1 live) is fully bound both ways (see checklist). Capture and D2 lines carry no UA token in receipt-05 — QUALITY 22 binds UAs only for wall/CAPTCHA/refusal records, so nothing is required; but the preamble "each User-Agent bound to the response that request received" is broader than the stored record. Cosmetic: record the fetch UA per line or narrow the sentence.

**F7 (informational) — S897 `quote-words: 1`.** Whitespace-counted; a segmented count is ≈11. ≤25 either way — no defect — but the committed `S897.txt` should name the counting convention since the Gate cap is word-based.

## Consistency confirmed during review

- `ls reports/round-77` → `telemetry` only; lane tip = base `211f9526…`. The draft's "evidence absent / counters absent" cells are accurate.
- Staged tiers match the verdict cells: `SOURCES.append.md:45` S897→B, `:51` S903→A.
- `corpus/QUALITY.md` at base: criterion 10 (opened by ordinary means — lesson's reason for not re-fetching S897), 22 (UA binding on refusal records), 29 criteria total (lesson M11's `30` slot is free) — all as cited.
- README footer stack: `Total knowledge entries:` at lines 755/798/819/830/834 (lesson says five blocks); line 824 names `round-28/readme/sweep.py` first-block parsing — as cited.
- D2 captures not interchangeable (informational, `ScribeLesson.md` F9): `20251231111748id_` = 546440 B / `1b4c60f2…` vs `20260901045105id_` = 417093 B / `5d1bfa5a…`; only the latter is byte-identical to live — the row correctly names only `20260901045105id_` as the byte-identical capture.

## Residual risk / verification gaps

- S897's quote/locator cells are still L1-FILL; the landing can still drift from the verified staged values — the L1 should copy the ScoutDocS897 strings verbatim.
- F2's convention decision (5-word quote + 17-word anchor vs 17-word folded quote) is open; whichever lands must be identical in the Gate row and `S898.txt` or EVIDENCE/GATE self-contradicts.
- The spot-check plan is required-but-unexecuted by design; its record-file name (F1) decides where the check lands.
- `lsp` device unused: no language server applies to this artifact review; checks were `grep`/`git show`/byte counts over the named files — all outputs above.

## Commands run (outputs quoted inline)

- `find .ufo/waves/round-77 -type f` — file inventory.
- `git -C <lane> show 211f9526…:corpus/QUALITY.md | grep -nE '^(10|18|22)\.'` — criteria 10/18/22.
- `git -C <lane> show 211f9526…:corpus/lessons/round-76-verifier-spotcheck.md | head -40`; `ls-tree --name-only …:corpus/lessons/ | grep verifier` — convention (F1).
- `git -C <lane> show 211f9526…:corpus/README.md | grep -n 'Total knowledge entries'` → 755/798/819/830/834.
- `grep -n 'altogether 88' …/RevQualityFit-2/D2-onomastica.txt` → `:151`; `sed -n '140,160p'` — §3 ¶1 sentence 2, journal p.114.
- `wc -w`/`-m` on the 17-word quote → 17 / 111; `wc -m` on the CJK quote → 23.
- `grep -n S934 /home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md` → `:82` (Słon row vs Kałużyńska capture).
- `ls reports/round-77` → `telemetry`; `git status --porcelain` → `??` only; `git log -1` → base.

No installs; no fleet/sibling mutation; scratch `/fast/scratch/hyaku/kotodama-r77/RevLessonGate` used only for the word-count check and deleted.
