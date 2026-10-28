# ScoutRejectSet — round 77 wave 2

Scope: audit the rejected `S933`/`S934`/`S936` rows (staged `naming-systems.amend-2026-10-24.md`) and the `…-r10.md` candidate grounds. Verify each reason+flip is evidence-based; confirm live-unavailable is not the reject reason. Sources: staged rows in `/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md` (lines 81–84, 87–92), the two candidate files, W1 seat outputs under `.ufo/waves/round-77/w1/`, `CLAIMS-DRAFT.md`, and my own fetches of the three captures plus the live originals (scratch `/fast/scratch/hyaku/kotodama-r77/ScoutRejectSet`, deleted after this report).

## Verdicts per item

### S934 — REFUSE ground VERIFIED (misdescribed duplicate of D2)

- Staged row (SOURCES.append.md:82) describes `Słon, M., «Names and the named: gender, femininity and given names in Poland», Onomastica 68` and claims "the live article path no longer serves this text; the archived capture does", citing `web.archive.org/web/20251231111748id_/…/download/574/763/`.
- My fetch: `curl -sSL …20251231111748id_/…/574/763/` → `HTTP 200 546440B`, PDF. `pdftotext -f 1 -l 1` → `https://doi.org/10.17651/ONOMAST.69.7`, `Onomastica LXIX, 2025`, `IRENA KAŁUŻYŃSKA`, `FLOWERS, PLANTS, AND TREES IN FEMALE NAMING IN CHINA`. Grep of full text: `słon|slon` → 0 hits; `kałuż|kaluz` → 16 hits. Line 151 carries the D2 anchor sentence `According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms`.
- Live original: `curl -sSL …/download/574/763/` → `HTTP 200 417093B`, same Kałużyńska title page. `pdfinfo` → 13 pages both; sha256 differ (`1b4c60f2…` capture vs `5d1bfa5a…` live) — different encodings of the same document (consistent with ScribeLesson F9: only capture `20260901045105id_` is byte-identical).
- Verdict: the row's document cell misdescribes its own capture, and the capture is the D2 document — the refuse ground "misdescribed duplicate of D2" is evidence-based and correct. The flip ("reopen only if a staged row's document and its capture agree on a document D2 does not already hold", lessons Gate row) is the right falsifiable flip.

### S936 — REFUSE ground evidence-based, and understated

- Staged row (:84) describes the reference list in «三维铸牢中华民族共同体意识» (中央民族大学学报 47(1), 2020) and claims "the live repository file no longer serves this text", citing `web.archive.org/web/20251010013419id_/…/omu.repo.nii.ac.jp/record/4358/files/2014000035.pdf`.
- My fetch: capture → `HTTP 200 562907B`, PDF. `pdftotext -f 1 -l 2` → `名前から見る古代貴族の家族観`, author 潘蕾, 大阪府立大学人文学会 人文学論集, DOI 10.24729/00004351 — NOT the 2020 中央民族大学学报 article the row names. References section (line 498 `参考文献`) does contain line 556 `・納日碧力戈『姓名』中央民族大学出版社、2000` plus 完顔紹元 and 何暁明 entries — so the bibliography-bridge *payload* exists as claimed.
- Live original: `curl -sSL https://omu.repo.nii.ac.jp/record/4358/files/2014000035.pdf` → `HTTP 200 564692B`, same 潘蕾 document. The row's "live … no longer serves" note is false.
- Verdict: "excess bibliography bridge" is supported (the row sells a reference-list block, not this claim's ground), but the stronger defects the draft does not name are also confirmed: (a) the row misdescribes its carrier article, (b) the document is the same URL/artifact as held-23c's S918 — a document-level duplicate. Refusal stands; the record should name the misdescription+duplicate, not only scope.

### S933 — correctly NOT a refuse ground; its own "live gone" note is false

- Staged row (:81) claims "the live CN page no longer carries this text; the archived capture does", but the cited capture is the **EN** page `20220630094933id_/…/xlkxjz/EN/10.3724/SP.J.1042.2021.01067`.
- My fetch: EN capture → `HTTP 200 160156B`, `<title>Psychological and behavioral effects of personal names in real world: Evidence and theories</title>`, DOI `SP.J.1042.2021.01067` — correct document. **Live CN page** `curl -sSL https://journal.psych.ac.cn/xlkxjz/CN/10.3724/SP.J.1042.2021.01067` → `HTTP 200 169549B`, `<title>姓名对个体心理与行为的实际影响：证据和理论</title>`, title string ×5, `摘要` ×6 — the live CN page DOES carry the text today.
- Document identity: same DOI/document as staged S875 (cited only by the `amendments/` anchor file) and live-carried by r13/r14's S966 (CN page) / S969 (CN PDF) — confirmed via their staged rows (:114, :117).
- Verdict: the draft's rule "S933 archived rather than live, so route alone is not a refusal" is the correct standard, and the final refusal is grounded on S934+S936 instead — **live-unavailable is not the reject reason in the current bytes**. Additionally the row's withdrawal claim is contradicted by the live CN page, so "live text gone" must never re-enter the record as a reason (it is also factually wrong, not merely insufficient).

### r10 (`naming-systems.amend-2026-10-24-r10.md`) — HOLD disposition correct; one stated ground is unevidenced

- File read in full: cites staged S939 (sciscanpub 《译道》 2023 issue PDF, tier B), S940 (docin upload record, self-declared tier C), S941 (NDL catalogue, tier A), S943 (Waseda UP 目次, tier B), S944 (CiNii record, tier B). Ground: round-9 CANNOT-ANSWER §5, original/venue chase for 姓名についての人類学的研究 — verified distinct from claim C's structure+lexeme-inventory ground.
- "Tier-C weight" ground: evidence-based — S940's own row declares `community | C` for a docin upload record; SentinelSources independently classifies it tier C.
- **"Pending S899/S900 quarantine resolution" ground: NOT evidence-based.** S899/S900 are staged chinawriter.com.cn interview rows (SOURCES.append.md:47–48) cited only by `culture-material/worldbuilding-setting-practice.amend-2026-10-23.md` — a different theme's file. Zero hits for `S899|S900` in `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`, in every `naming-systems*.md`, and in all r77 wave artifacts outside restatements. No quarantine ruling on S899/S900 exists, and no naming file cites them. The dependency as stated is mistaken; the hold survives on "distinct ground; reopen as its own amendment" alone. ScoutHeldEntries already flagged existence unverified; this seat verifies the IDs resolve to unrelated worldbuilding rows.

## Mistaken dispositions / record defects found

1. **`report-skeleton.md:21` re-injects the banned reason.** `w1/stage/ScribeReport/report-skeleton.md` instructs the Gate to record `naming-systems.amend-2026-10-24.md` rejects as "(S933 live text gone; S934 document-level duplicate of D2; S936 bibliography-bridge)". "S933 live text gone" is both the forbidden live-unavailable route and factually false (live CN page 200, article title present — this seat's fetch). If L1 copies it, live-unavailable re-enters the reason set. Must be struck; the file's refusal needs no S933 leg.
2. **`claims-C.skeleton.json` mislabels the held r10 file.** `w1/stage/ExecAdaptC/claims-C.skeleton.json` `rejects.refused_files` = `[10-24.md, 10-24-r10.md]`, while the draft and lessons Gate disposition r10 as **held** — contradicting the W1 lesson "keep held apart from refused". No leg reads `cfg["refused_files"]` (verified: parsed at accept-c.py:827–833, stored at :915, consumed by no leg function), so it is dead config, but the frozen record would still mislabel a held file refused.
3. **Skeleton `refused_staged_not_appended` mixes refused and held ids without distinction** ([S933,S934,S936] + [S939–S944] + S942). S942 is cited only by the `amendments/` anchor file, not by any of the 11 triaged naming files (`grep -rln S942 …/merge/kotodama/knowledge` → SOURCES.append.md only; citer = `amendments/corpus/knowledge/linguistics/naming-systems.md`). Listing is defensible id-wise (staged, not appended) but the REJECTS leg will force all nine into Gate reject rows, so held r10 ids will sit in a "refused" set — the Gate rows must word them as held.
4. **Report-skeleton repeats the unevidenced dependency** for r10 ("tier-C upload record pending S899/S900 resolution") — same finding as the per-item audit.

## Standards check

- Live-unavailable is **not** the reject reason in the current CLAIMS-DRAFT/lessons-Gate disposition for the refused file; it survives only in the stale report-skeleton line (defect 1) and inside the staged rows' own (false) withdrawal notes, which are staged data, not the lane's stated reason.
- Refuse of 10-24: evidence-based (verified above); hold of r10 and the nine siblings: evidence-based on distinct-ground, with the S899/S900 dependency to be corrected or dropped.
- ScoutHeldEntries's "10-24 REFUSE per DRAFT" agrees with the draft's refused/held split; the only divergence is the skeleton's refused_files list (defect 2).

## Commands run (raw outputs above)

```
curl -sSL -o s934.pdf …/20251231111748id_/…/574/763/  → HTTP 200 546440B; PDF 13pp; pdftotext p1 → Kałużyńska Onomastica LXIX; Słon hits 0
curl -sSL …/download/574/763/ → HTTP 200 417093B; same title page
curl -sSL -o s936.pdf …/20251010013419id_/…/2014000035.pdf → HTTP 200 562907B; pdftotext → 潘蕾《名前から見る古代貴族の家族観》; ref list line 556 納日碧力戈『姓名』2000
curl -sSL https://omu.repo.nii.ac.jp/record/4358/files/2014000035.pdf → HTTP 200 564692B; same doc
curl -sSL …/20220630094933id_/…/EN/10.3724/SP.J.1042.2021.01067 → HTTP 200 160156B; EN article page, correct doc
curl -sSL https://journal.psych.ac.cn/xlkxjz/CN/10.3724/SP.J.1042.2021.01067 → HTTP 200 169549B; <title>姓名对个体心理与行为的实际影响：证据和理论</title>
grep -rln 'S899\|S900' merge/kotodama/knowledge → worldbuilding-setting-practice.amend-2026-10-23.md only
grep -n 'S899\|S900' absent-defect-register.md → no hits
```

No installs; pacman untouched. Lane repo unmodified (scratch dir deleted).
