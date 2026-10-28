# W2 seat report — RevLessonGate (round 76 kotodama, falsification)

Seat: RevLessonGate-2 · Date: 2026-10-27 · Scope: round-76.md **Gate** and **refused-package** tables vs the frozen C claim contract and the final C counter. Review only; no edits to claims, counters, lane files, or reports.

## Method and revisions

All reads are committed bytes, never the mutable worktree:

- Frozen contract: `git show df0f0309d61e5485bb17035d3f8791b1e6a11d40:reports/round-76/claims.json` (status "FINAL … frozen before landings", `frozen: 2026-10-27`).
- Final lesson / counter / evidence / registry: revision `722e69ff6361aadf148cb46acbf6ac8fd147f59a` (C landing). `reports/round-76/claims.json` and `reports/round-76/accept-c.py` are byte-identical between `df0f030` and `722e69f` (`git diff` empty), so freeze == lands for FROZENCFG purposes.
- Base for before-state: `98c486bdb4650ba5b8e651d332910e8ee60ad121`. Ca landing `a43ed807ea38b5fc5a7875a839d576cea73aba7c` touches only SCORECARD.md/SKILL.md (out of this seat's tables).
- Counter behavior was read statically (`accept-c.py`); the counter was **not executed** (wave rule: no tests/builds). Quote folding = NFKC + whitespace-run→single-space, per the counter's own rule (`accept-c.py:307-308`, `2554`).
- No tool installs or upgrades were needed or performed; pacman untouched. Scratch used: `/fast/scratch/hyaku/kotodama-r76/RevLessonGate/` (removed before yield).

## Gate admit table (round-76.md:9-13 @722e69f) — row-by-row

| check | S894 (line 11) | S895 (line 12) | S896 (line 13) |
|---|---|---|---|
| URL vs frozen `row_set` | live `https://www.digital.archives.go.jp/search` + capture `20260422145052id_` — match | live `newGbInfo?hcno=E107EA…` + capture `20260424031027id_` — match; contract adds "showGb is a 302 alias to this record" | live `news.gmw.cn/2017-05/23/content_24559485.htm` — match; **capture `20170523024955id_` is NOT in the frozen row_set** (see F3) |
| URL vs landed registry | `corpus/SOURCES.md:849` identical carriers — match | `:850` identical carriers — match | `:851` identical carriers — match |
| Access date | 2026-10-27 = frozen `access_date` — pass | same — pass | same — pass |
| Quote caps | 「元号名称 開始西暦年 令和 2019」 4 tokens / 18 chars — pass (≤25/≤80) | 「标准号：GB/T 33661-2017」 2 / 19 — pass | 「首次明确了农历的编排规则、计算模型和精度等」 1 / 21 — pass |
| Quote == registry anchor (folded) | pass (anchor cell 6 `:849`) | pass (`:850`) | pass (`:851`) |
| Quote in committed window | verbatim + folded, `evidence/S894.txt` | verbatim + folded (fullwidth `：` folds to `:`), `evidence/S895.txt` | verbatim + folded, `evidence/S896.txt` |
| window-sha256 recomputed | `86428e0a…` match (9059 B) | `882d1f9a…` match (1445 B) | `3b0fc54b…` match (4005 B) |
| window-scope rule | excerpt 4103 ≥ 4096 — legal | whole-document 664 = `visible-chars:` < 4096 — legal | whole-document 1487 = `visible-chars:` < 4096 — legal |
| Locator | 「元号選択 → 和暦元号 table, header and first row」 — **verified in window** (modal/tab/header/first row present) | 「标准信息表, 标准号 field」 — **DISCREPANCY, see F1** | 「article paragraph 4」 — **verified**: quote is the 4th `<p>` of the article (`w1/stage/ExecCensusRows/window/S897-news.gmw.cn-2017-05-23.html`) |
| Verdict | admitted (tier A) = registry tier cell `A` | admitted (tier A) = `A` | admitted (tier B) = `B` (census A+2/B+1 at `round-76.md:77`) |

Gate shape vs GATE leg (`accept-c.py:2352-2466`): ≥1 admit + ≥1 reject present; every reject row carries probed URL + reason + flip; quote cell binds to the row anchor. No structural defect.

## Gate reject table (round-76.md:15-19) and refused-package families (:25-35)

1. **showGb online alias** (line 17) — probed URL = frozen candidate b's document; reason is receipt-backed: `w1/stage/ExecCensusRows/validate-receipt-draft.txt:18` records `http=302 transfer=0` for the showGb route and `:27-28` the 302 headers; `w1/ExecCensusRows.md:77` records `Location: …/newGbInfo?…&refer=outter`; the followed window (`S896-openstd.showGb-followed-2026-10-27.html`) is the same record (title `国家标准|GB/T 33661-2017`, 标准号 field present). The stated presence of 「标准号：GB/T 33661-2017」 in `evidence/S895.txt` is true. Flip condition present. Verdict `refused` matches contract `candidates[b].admitted=false`. **But see F2** — the machine-readable by-document binding fails.
2. **duplicate archive table** (line 18) — probed URL = S894's live URL; reason mirrors contract `rejects.refused_files_pending_triage` ("archive era table is not a second uncovered ground"); S894 evidence does carry the quote. Verdict/flip consistent.
3. **drafter interpretation** (line 19) — probed URL = candidate d's document; quote 「取其中最先出现的一个不包含中气的农历月为农历闰月」 is present in the cited window (`S895-xingzuobaike.com-2026-10-27.html`, inside a numbered clause `<p>(4)…`). Verdict/flip consistent with `candidates[d]`. **But see F4** on the reason wording.
4. **Triage paragraph** (line 21): 1 adopted / 9 path-present / 30 refused, sums to 40 and equals frozen `rejects.counts {1,9,30,40}`; the six non-candidate families ×11/9/1/3/1/2 = 27 match the frozen `counts_note`.
5. **Families table** (:27-35): rows sum 1+1+1+11+9+1+3+1+2 = 30 = refused (REJECTS leg reconciliation satisfied); every row carries reason + flip. Family files exist and are distinct: `naming-systems.*` ×11 and a separate `era-periodization-models.amend-2026-10-23.md` (distinct from candidate c's `-23b.md`) verified in `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/` (40 `.md` files total, matching `counts_note`).
6. **Quarantine** (:41-63): 21 rows; every prior verdict matches `reports/round-71/telemetry/quarantine-verdicts.md` (register tally PRESENT 10 / REFUSED 7 / UNVERIFIABLE 4 = 21), matching line 39.

## Findings

**F1 · Medium — S895 Gate locator cites a label the evidence window does not contain.** `round-76.md:12` locator "标准信息表, 标准号 field". The S895 window is the whole visible text (664 chars) and contains no `标准信息表` string — only the site banner `全国标准信息公共服务平台`. The landed registry anchor (`SOURCES.md:850`, cell 6) itself says "record page, 标准号 field", and the evidence receipt's own `locator:` field (`evidence/S895.txt` line 30) says "archived registry record, 标准号 field row". The lane's own w1 receipt (`w1-results.json` → ScoutDocS896 output) lists the "标准信息表 label" among the statements the staged entry must drop/hedge. The C landing rewrote the Gate table but kept the stale locator. The GATE leg cannot catch it — `_leg_gate_locator` (`accept-c.py:2309-2319`) only checks the cell is non-empty, non-URL text.

**F2 · Medium — the refusal narrative is true, but the frozen map cannot bind it; COLLCHECK fails on exactly this row.** The frozen map (`df0f030:.ufo/waves/round-76/assimilation/id-renumber-map.json`, `assignments[3]`) records `S938 → S895` with `normalized_document_url = openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296`, while the landed S895 row cell (`SOURCES.md:850`) carries the alias only as prose ("showGb?type=online redirects here by HTTP 302") — never the full showGb URL. The frozen COLLCHECK therefore reports "map record S938 -> S895 names a document the row does not" (`telemetry/controls-c.txt`, COLLCHECK block), and no landing that keeps this row cell can pass it. The lesson's Collision-guard sentence "resolved by document, not arithmetic: … S932/S938→S895" (`round-76.md:69`) is imprecise for S938: the resolution is by redirect-alias, not by document URL. The failure is honestly disclosed at `round-76.md:89` (ROWS/COLLCHECK named, no softening) — no false green in the Gate table itself, but the table's clean "refused" presentation plus the "resolved by document" sentence overstate what the frozen configuration can bind.

**F3 · Low — S896's capture carrier is outside the frozen row_set and never fetched in any committed round-76 receipt.** The frozen `row_set` S896 document names only the live URL (unlike S894/S895, whose captures are in the frozen text); the capture `20170523024955id_` appears only in the landed row and Gate table. No `reports/round-76/evidence/` receipt fetches it (`evidence/S896.txt` is live-only). The w1 receipts that did measure the capture (`w1/ScoutDocS898.md:64-65,139`; `w1/RevQualityFit.md:152,261`) used the **http://**-embedded form (`…id_/http://news.gmw.cn/…`), while the Gate/registry rows write the **https://**-embedded form. The lane normalizer folds scheme-only changes (`w1/ScoutCDXPositive.md:12`), so this is citation precision, not fabrication.

**F4 · Low — refusal-reason wording drift on the drafter-interpretation row.** `round-76.md:19` says the page "does not contain normative clause text" (presence claim), but the window it cites visibly contains numbered clause text — including the quoted span itself (`<p>(4)若从某个农历十一月开始…置闰规则为:取其中最先出现的一个不包含中气的农历月为农历闰月。</p>`). The frozen contract's wording is provenance-flavored and accurate ("a tier-C drafter interpretation, not the standard's clause text", backed by `w1/ScoutDocS895.md`: "Page has no 原文 section: it is the drafter's 解读 summary"). Verdict unaffected; the paraphrase is falsifiable by the seat's own cited window.

**F5 · Info — stale comment inside the frozen counter.** `accept-c.py` `leg_rejects` section-1 comment reads "3 adopted / 6 path-present / 31 refused (40)", contradicting the frozen counts 1/9/30 the code actually reads from `cfg`. Comment only; no behavior.

**F6 · Info — no final-counter-over-lands receipt is committed.** `round-76.md:89` calls "the final C counter receipt" the authority, but the C landing commits (`788bd56`, `722e69f`) add no counter output over `--lands 722e69f`; the only committed counter outputs are the pre-data do-nothing controls (`telemetry/controls-c.txt`, measured at freeze). The final outcome is nonetheless determined by frozen bytes: ROWS fails regardless of the table because the two non-row SOURCES.md lines added between base and freeze persist at lands (`SOURCES.md:854` "- calendar-standard design — S896 → S895 → S894: …", `:902` "**State-standard calendar compilation (round 76).**…"; absent at base) and the frozen R1 check is a line-multiset diff (`accept-c.py` ROWS R1) — exactly the M3-recorded parser/append interaction; COLLCHECK fails per F2. The lesson's "failed as declared" record is faithful to the frozen predicates.

## Verdict

The Gate and refused-package tables are faithful to the frozen C contract in every checked dimension except F1–F4: all URLs, access dates, quote texts/caps, evidence digests, tiers, verdict strings, refusal reasons (except F4's wording), flips, triage arithmetic, family counts, and the quarantine slice verify against committed bytes at `df0f030`/`722e69f`. No false green was found in the tables. The substantive defects are: the unsupported S895 locator label (F1), the frozen map/row alias binding that makes the recorded COLLCHECK failure unavoidable (F2), the S896 capture carrier asserted beyond frozen contract text and committed receipts (F3), and the falsifiable presence-flavored refusal wording (F4).

## Residual risk and verification gaps

- The counter was not executed (wave rule); leg outcomes at lands are derived from static reading of frozen `accept-c.py` plus committed receipts, not a fresh run. F6 records that no committed lands-receipt exists to compare against.
- CITEDLINES / INDEX / ENTRIES / GROUND / CENSUS leg values are outside this seat's tables and were not audited.
- The `9 path-present at base` count is taken from the frozen `counts_note` and verified only arithmetically (40 staged files on disk; per-file base-presence not re-derived).
- Wayback captures were not re-fetched (read-only wave); capture claims rest on committed w1/evidence receipts.
