# Round 76 — kotodama: calendar-standard record and archival era table

Round 76 declares C (coverage) and Ca (calibration). Base `98c486bdb4650ba5b8e651d332910e8ee60ad121`; frozen configuration is in `reports/round-76/claims.json`. C targets one selected knowledge entry and three new, opened source documents. Ca counts twenty ledger pairs. The C counter is frozen in `reports/round-76/accept-c.py`; the Ca counter is `reports/round-76/accept-ca.py`.

## Gate

Access date: 2026-10-27. Evidence windows are committed as `reports/round-76/evidence/S894.txt`, `S895.txt`, and `S896.txt`; each contains the fetched body digest, request metadata, the located quote, and a stored window.

| source | access date | quote (≤25 tokens, ≤80 characters) | locator | evidence | verdict |
|---|---|---|---|---|---|
| candidate a — S894, National Archives of Japan, https://www.digital.archives.go.jp/search; same-page capture https://web.archive.org/web/20260422145052id_/https://www.digital.archives.go.jp/search | 2026-10-27 | 「元号名称 開始西暦年 令和 2019」 | 元号選択 → 和暦元号 table, header and first row | `reports/round-76/evidence/S894.txt` | admitted (tier A); re-open live and capture; if the table no longer locates, row becomes unverifiable |
| candidate a — S895, National standards registry record https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296; same record capture https://web.archive.org/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296 | 2026-10-27 | 「标准号：GB/T 33661-2017」 | record page, 标准号 field | `reports/round-76/evidence/S895.txt` | admitted (tier A); re-open record/capture; if identity fields disappear, row becomes unverifiable |
| candidate a — S896, Guangming Daily report https://news.gmw.cn/2017-05/23/content_24559485.htm; same-page capture https://web.archive.org/web/20170523024955id_/https://news.gmw.cn/2017-05/23/content_24559485.htm | 2026-10-27 | 「首次明确了农历的编排规则、计算模型和精度等」 | article paragraph 4 | `reports/round-76/evidence/S896.txt` | admitted (tier B); re-open article/capture; if the report no longer locates, row becomes unverifiable |

| item | probed URL | reason | flip | verdict |
|---|---|---|---|---|
| showGb online alias | https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296 | `w1/stage/ExecCensusRows/window/S896-openstd.showGb-followed-2026-10-27.html` follows HTTP 302 to the same `newGbInfo` record; the registry quote 「标准号：GB/T 33661-2017」 is present in `reports/round-76/evidence/S895.txt`; no distinct document is served | reopen only if the route serves a distinct source document, not the same record | refused |
| duplicate archive table | https://www.digital.archives.go.jp/search | `reports/round-76/evidence/S894.txt` carries 「元号名称 開始西暦年 令和 2019」; this is the same archive page adopted as S894, not a second uncovered document | reopen only if a distinct page supplies new uncovered era ground | refused |
| drafter interpretation | https://www.xingzuobaike.com/huangli/wannianli/d165803.html | the staged reproduction page locates 「取其中最先出现的一个不包含中气的农历月为农历闰月」 but presents a drafter's interpretation, not the standard's own normative clause text; `w1/stage/ExecCensusRows/window/S895-xingzuobaike.com-2026-10-27.html` | reopen only with an A/B carrier for the claimed rule and a narrower entry | refused |

### Non-author spot-check

Reviewer `RevLessonGate` (wave 2, non-author) spot-checked the S894 admit and the showGb-alias refusal against the committed evidence and redirect capture (`.ufo/waves/round-76/w2/RevLessonGate.md:17-35`). **Agree** on S894: the URL, quote, and locator resolve in the committed window. **Agree** on the showGb refusal: the probed URL returns HTTP 302 to the already-cited `newGbInfo` record, so no second source row is warranted. The reviewer also **disagreed** with the original S895 locator phrase `标准信息表` because that label was absent from the 664-character window; the Gate and evidence locator now use `record page, 标准号 field`, which names the visible field instead.
Triage measured 2026-10-27: 40 staged knowledge files — `find /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge -type f -name '*.md' | wc -l` → 40; 9 path-present at base — the per-file base path sweep in `.ufo/waves/round-76/w1/ExecAdaptC.md:216` reports `same=0 diff=9 absent=31`; 30 refused = 40−1 adopted−9 path-present. The frozen counts are 1 adopted / 9 path-present / 30 refused (1+9+30=40). Candidate a is the sole adopted entry; the 27 non-candidate refusals are naming-systems ×11, verification amendments ×9, era-periodization ×1, conlang-scholarship ×3, conlang-methodology ×1, and narrative-structure amendments ×2; these are outside this entry's calendar-standard/era-table scope. Flip only when a separate, lane-scope source-grounded gap is declared. Candidates b/c/d were refused for the reasons above. No row was appended unless cited by the admitted entry. Candidate a's staged citations to campaign ids were re-pointed by document to S894/S895/S896; no campaign id is used as a lane citation.

### Refused package families

| family | files | reason | flip |
|---|---:|---|---|
| candidate b | 1 | `showGb?type=online` redirects to the already-cited `newGbInfo` record; it is an alias, not a second document | reopen only if the route serves a distinct source document |
| candidate c | 1 | the era table is the same archive page already adopted as S894; no second uncovered document | reopen only if a distinct page supplies new uncovered era ground |
| candidate d | 1 | the drafter page reproduces an interpretation, not the standard's own normative clause text | reopen only with an A/B carrier for the claimed rule and a narrower entry |
| candidate family: naming-systems | 11 | these entries concern naming systems, not calendar compilation or an era-name table | review only under a separately declared naming-systems gap |
| candidate family: verification amendments | 9 | these files are verification material, outside this knowledge entry's topic | review only under a separately declared verification gap |
| candidate family: era-periodization-models | 1 | this is outside the entry's new ground; the selected archive table is the only adopted era record | review only if a new, opened era-periodization source fills an uncovered claim |
| candidate family: conlang-scholarship amendments | 3 | scholarship on constructed-language practice is unrelated to the calendar source set | review only under a separately declared conlang-scholarship gap |
| candidate family: conlang-methodology | 1 | methodology material does not support this calendar entry | review only under a separately declared conlang-methodology gap |
| candidate family: narrative-structure-frameworks amendments | 2 | narrative-theory content is off-topic for the calendar/era entry | review only under a separately declared narrative-theory gap |

## Quarantine

The standing kotodama slice was re-derived read-only on 2026-10-27 from `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` with the §6 item-10 `awk -F'|'` selector (exact command in `.ufo/waves/round-76/w1/ScoutQuarantine.md:6`); `wc -l .ufo/waves/round-76/w1/stage/ScoutQuarantine/quarantine-slice` → 21 and every line contains an S-id (`grep -cvE 'S[0-9]+'` → 0). Standing verdict histogram command in `ScoutQuarantine.md:12-14` re-derived PRESENT 10 / REFUSED 7 / UNVERIFIABLE 4 from `reports/round-71/telemetry/quarantine-verdicts.md`; the register remains read-only. By document, five current lane rows overlap slice documents: three pre-existing round-75 bridges (S883/S816, S884/S817, S893/S787) and two new round-76 rows (S894/S825 and S895/S776). The two PRESENT documents were re-opened with new located quotes and appended as new rows; no register verdict or existing lane row was edited. The initial ID-only sweep did not establish document disjointness.

| slice id | prior verdict | round-76 disposition |
|---|---|---|
| S776 | PRESENT | same document as new S895; re-opened with the registry field quote; prior verdict unchanged |
| S778 | PRESENT | carried, not touched |
| S779 | REFUSED | carried, not touched |
| S786 | REFUSED | carried, not touched |
| S787 | REFUSED | same document as pre-existing S893 (round 75); prior verdict unchanged |
| S791 | UNVERIFIABLE | carried, not touched |
| S792 | REFUSED | carried, not touched |
| S795 | PRESENT | carried, not touched |
| S796 | PRESENT | carried, not touched |
| S804 | PRESENT | carried, not touched |
| S814 | REFUSED | carried, not touched |
| S816 | REFUSED | same document as pre-existing S883 (round 75); prior verdict unchanged |
| S817 | REFUSED | same document as pre-existing S884 (round 75); prior verdict unchanged |
| S820 | PRESENT | carried, not touched |
| S823 | PRESENT | carried, not touched |
| S824 | PRESENT | carried, not touched |
| S825 | PRESENT | same document as new S894; re-opened with the archive-table quote; prior verdict unchanged |
| S827 | PRESENT | carried, not touched |
| S807` | UNVERIFIABLE | carried, not touched; trailing backtick is a register-cell artifact |
| S812` | UNVERIFIABLE | carried, not touched; trailing backtick is a register-cell artifact |
| S835` | UNVERIFIABLE | carried, not touched; trailing backtick is a register-cell artifact |

The slice register itself remains read-only; every verdict above was carried unchanged. The two PRESENT documents now have new S894/S895 rows with newly located quotes and no old row replacement. The three REFUSED overlaps already had S883/S884/S893 lane rows from round 75; they remain refused and were not adopted in this entry. The other 16 slice documents do not match this round's source documents. The W1 ID-only conclusion in `.ufo/waves/round-76/w1/ScoutQuarantine.md` was too broad; the W2 document-level comparison is `.ufo/waves/round-76/w2/ScoutQuarantineStatus.md:3-19`.

## Collision guard

At base on 2026-10-27, `wc -l .ufo/waves/round-76/assimilation/reg-ids .ufo/waves/round-76/assimilation/staged-ids .ufo/waves/round-76/assimilation/collisions` → 817/132/35. SHA-256: `reg-ids` `97eef07a858487225118d5c2d18ceb919b8c9549a3768b9adee6a3a321dbd3a7`; `staged-ids` `bab11d7d0ee0d84795b1ff80274fe371670fff73a477c747b2fd3cad4c25ddad`; `collisions` `be203dd8b02cde5fcea89a04e882daa3f525200b8a801e324ad73cde2ebbaf47`. The 35-id collision set is S859–S893; the separate post-adoption numeric-overlap map resolves staged S908/S935→S894, S932/S938→S895, S937→S896. A 1–3-space plant `S897` was found by the whitespace-tolerant extractor (`assimilation/guard-proof/planted-1space-proof.txt`, output includes S897); the 4-space plant was not found (`planted-4space-proof.txt`, grep exit 1). The guard fixtures are committed under `.ufo/waves/round-76/assimilation/guard-proof/`.

## Normalization

Rows S894–S896 are sequential, each was opened 2026-10-27, status `mined`, recheck `180d`, 11 cells, no escaped pipes, and one distinct document per row. The staged rows were transformed to the CORPUS.md schema; used-by points only to the adopted calendar amendment. Same-document live/capture carriers remain in one source cell; the showGb route is recorded as a redirect, not a second source row. The scratch mirror receipt is `.ufo/waves/round-76/assimilation/validate-receipt.txt` (validate and census exit 0; 820 rows, tiers A493/B311/C16; mined725/queued58/rejected37). Existing cross-scope duplicate-URL and tier-C warnings are listed in that receipt; no new S894–S896 row warning appeared.

## Census

Start validation: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → exit 0; raw output is `reports/round-76/telemetry/census-start.txt`. Base counts were re-derived from the frozen `98c486bdb4650ba5b8e651d332910e8ee60ad121:corpus/SOURCES.md` blob with the commands recorded verbatim in `reports/round-76/telemetry/census-start-counts.txt`: 817 rows, A491/B310/C16, mined722/queued58/rejected37, exit 0. End validation used the same `validate --root` command → exit 0, raw output `reports/round-76/telemetry/census-end.txt`. End counts were measured on the lane root with `sources-census.sh census --root /home/vgpnk/Projects/shokunin kotodama` → 820 rows, A493/B311/C16, mined725/queued58/rejected37, exit 0 (`census-end-counts.txt`). The manual seven table-shape and histogram checks on the 820-row mirror are in `.ufo/waves/round-76/assimilation/validate-receipt.txt`; pre-existing W04 duplicate-URL and W01 tier/status warnings remain, with no new S894-S896 census error.

Final close recheck at lane tip `21ef98c131dae5cc7a6b6b3387a4a2d56cc74962` (2026-10-27): `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` exited 0, followed by `sources-census.sh census --root /home/vgpnk/Projects/shokunin kotodama` exiting 0 with 820 rows, tiers A493/B311/C16 and statuses mined725/queued58/rejected37; complete output is `reports/round-76/telemetry/census-final-root.txt`.

## Mistakes

| id | class | evidence pointer | captured-by | fix / demonstrated failure |
|---|---|---|---|---|
| R76-M1 | attribution: a number read from a staged copy or probe is filed as though measured from a different committed artifact | `.ufo/waves/round-76/w1/RevengerMistakes.md` §2; `.ufo/waves/round-76/w1/stage/RevengerMistakes/recurrence.txt` | QUALITY criterion 29 (new) | A red check against the round-75 lesson at base found six number mismatches; the repaired fixture returned clean for those same six cells. The rule requires each numeric assertion to name its artifact/revision and be re-derived from that artifact. |
| R76-M2 | scope: frozen C leg names did not match the implemented leg table (duplicated INDEX, omitted SCRATCHMIRROR) | `.ufo/waves/round-76/w1/stage/L1/freeze-control-legcount-redbefore.txt`; `.ufo/waves/round-76/w1/stage/L1/pre-data-counter-repair.txt` | QUALITY criterion 26 (frozen leg list / LEGCOUNT) | Counter leg implementation repaired to match the already-frozen 13-leg list before data; selftest 89/89. Predicate/config bytes were not changed. |
| R76-M3 | scope: frozen ROWS compares the full registry diff but the declared row set only names S894-S896; the required Paths/Search-log lines are additional non-row changes | `reports/round-76/telemetry/controls-c.txt`; W2 `.ufo/waves/round-76/w2/CritRowDiff.md` and `ConnCounterPatterns.md` (they disagree on whether this exceeds the claim text) | none (no target-reachability control distinguished a frozen target made impossible by non-row changes) | Claim C remains failed as declared; a future freeze must either include the required section edits in its target or explicitly scope ROWS to source rows. No predicate changed. |
| R76-M4 | scope: three evidence files passed frozen EVIDENCE but lacked 17 producer-required anchor-binding headers | `.ufo/waves/round-76/w2/ExecEvidenceAudit.md`; `reports/round-76/telemetry/capture-evidence-recapture.txt` | none (the frozen EVIDENCE contract did not require the round-76 producer-only headers) | Re-captured S894-S896 through the frozen producer; each run printed `VERIFY OK` and `CAPTURE OK` with anchors bound. This strengthens provenance without changing frozen claims or the counter. |
| R76-M5 | scope: a pre-close seat was instructed to review a report that cannot be written until WAVE-DONE | `.ufo/waves/round-76/w2/ScribeReportCheck.md:11-16`; `.ufo/waves/round-76/w2/spec.json` | none (the wave prompt did not treat report absence before closure as a terminal result) | ScribeReportCheck returned NOT REVIEWABLE because the report was absent before close. Future waves should make report review post-close or accept “report absent pre-close” as a completed observation; this round's report is filed only after WAVE-DONE. |

## Routed to round 77

C failed as measured at `cb4f6c6a550b3233f3c12a266e72dee6f4bc126b`: `ACCEPT-C-76: FAIL legs=11/13`, with only ROWS and COLLCHECK red; GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS and INDEX pass. W2 reviewers disagreed whether ROWS over-reads or the frozen claim failed to account for required Paths/Search-log lines; both the frozen counter result and the disagreement are recorded in `w2/CritRowDiff.md` and `w2/ConnCounterPatterns.md`. COLLCHECK rejects S938→S895 because the frozen map carries the full `showGb` URL while the immutable S895 source cell only mentions that alias in prose. The W2 S895 locator finding was corrected, the evidence files were regenerated with the frozen producer, and the non-author spot-check is recorded above; W2 also noted that the S896 capture carrier is not in the frozen row set or the evidence file, although the live source is. Ca failed as measured at `a43ed807ea38b5fc5a7875a839d576cea73aba7c`: `ACCEPT-CA-76: FAIL legs=5/12`; LEDGER, REPAIR, ANNOTATE, NOSTUB, R1EXEMPT, SEPARABLE, and COMBINED are red; BASEMISMATCH, APPENDONLY, RECEIPTS, FROZENCFG, and STAMP pass. LEDGER specifically rejects L76-13 (stated-at path outside the frozen append-only allowlist) and L76-19 (stated text not found at the specified lesson line); additional ledger command-grammar and README-owned-inplace failures are in `reports/round-76/telemetry/measures-ca.txt`. Claims and ledger were not edited after freeze. The scorecard's post-measurement summary is an outcome record, not a changed predicate. Route counter/ledger defects to round 77 with new frozen claims and controls.
Final remeasurement after W2 integration and full count/scope reconciliation was run at `b40113eb3961bce44fba6b066ce6a656f0e16fec`: `ACCEPT-C-76: FAIL legs=11/13`, with the same two red legs (ROWS and COLLCHECK). Its committed receipt is `reports/round-76/telemetry/measures-c-final-c7.txt`.

## Sources & frontier

`corpus/SOURCES.md` at base `98c486bdb4650ba5b8e651d332910e8ee60ad121`: 817 rows; at the C7 data commit `b40113eb3961bce44fba6b066ce6a656f0e16fec`: 820 rows (A +2, B +1, C unchanged). The source-table diff command `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin diff --numstat 98c486bdb4650ba5b8e651d332910e8ee60ad121 b40113eb3961bce44fba6b066ce6a656f0e16fec -- corpus/SOURCES.md` prints `8 0`; W2's row-by-row check found no pre-existing row changed (`.ufo/waves/round-76/w2/ExecMapAudit.md:220-221`). The escaped-pipe sweep `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show b40113eb3961bce44fba6b066ce6a656f0e16fec:corpus/SOURCES.md | grep -E '^ {0,3}\| S(894|895|896) \|' | grep -F '\|'` prints nothing, exit 1. Frontier rows: S894 National Archives era instrument, S895 official GB/T registry record, S896 Guangming Daily report; their new statuses are mined/180d, used-by the one admitted entry. Final lane-tip census at `21ef98c131dae5cc7a6b6b3387a4a2d56cc74962` re-ran both `validate` and `census` modes with exit 0; `census-final-root.txt` records 820 rows/A493/B311/C16/mined725/queued58/rejected37. The round prompt §2b requires start/end validation; `CORPUS.md` supplies the seven manual census commands but does not impose a post-landing census. Base/end count receipts are above. `test -d /home/vgpnk/Projects/shokunin/kotodama-shokunin/considerthese` prints `absent`, exit 1; no still-unimplemented proposal was available.
