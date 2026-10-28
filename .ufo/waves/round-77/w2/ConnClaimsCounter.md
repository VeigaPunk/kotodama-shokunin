# ConnClaimsCounter — round 77 wave 2 (connector, leaf, attack-only)

Seat: ConnClaimsCounter · Lane: kotodama-shokunin · Base: 211f9526800906e0c585d878d265c37e5e090c15
Assignment: connect every clause in claim C and claim Ca frozen after/kill rules to its counter leg; table clause → leg → red fixture/receipt; identify clauses promised but not checked (especially `required_sections` and all entry source ids).
Stage: `.ufo/waves/round-77/w2/stage/ConnClaimsCounter/` (receipts, probe drivers, counter copies, sha256 list).

## 0. Verdict in brief

1. **The frozen C and Ca contracts are mostly wired to a real leg with a red fixture.** Re-run here: C selftest `37/37` (exit 0); Ca selftest `199/199 across 51 scenarios` (exit 0); real 11-pair ledger `LEDGER-CHECK-77: PASS pairs=11` at base.
2. **Several promised checks are absent or defeated.** The most serious, each reproduced by a probe (§5):
   - **C — the counter executes lands-supplied code for CITEDLINES** (`tools/check-cited-lines.py` at lands, unpinned by FROZENCFG). Replacing the tool with a stub makes a two-source-ID line green (`cited-stub`: 13/13).
   - **C — "query-aware record keys" in COLLCHECK is not implemented.** `norm_url` drops the query; a source cell naming `…/docs/alpha?id=2` for a row frozen as `…/docs/alpha` passes all 13 legs (`query-other-record`: 13/13).
   - **C — the `refused_files` clause is never graded.** Frozen `rejects.refused_files` names 2 of the 10 non-adopted staged files; the clean fixture does not name its declared file in the Gate and still grades 13/13.
   - **C — "each new factual line carrying exactly one source ID"** is enforced only for lines with ≥2 IDs; zero-ID factual lines pass (`zero-id`: 13/13).
   - **C — a capitalised `Source:` line naming a wrong document passes all legs** (`caps-source-wrong-doc`: 13/13); `EVIDENCE` accepts a wrong `fetch:` line whenever `url:` names the frozen document (`ev-wrong-doc`: 13/13).
   - **Ca — the observe/rederive validator accepts a mutable branch in the revision slot, no `--` before paths, and option-driven program execution.** `git grep --open-files-in-pager=<cmd>` is accepted and the counter's own executor runs `<cmd>` (marker file created). `git diff --output=<path>` is accepted and writes outside the clone. The three promised routed defects (`--`, immutable 40-hex revision, and the no-executable-side-effect intent of the argv rule) therefore have no enforcing leg.
3. **Non-blocking but real:** duplicate physical registry row lines pass `ROWS` (it counts distinct IDs); only the real `sources-census.sh` (E04) catches them, and the selftest runs a stub census. Frozen `row_set` accepts duplicate documents and one staged ID mapped to two lanes.
4. Counters examined: the **W1 staged** files (`w1/stage/ExecAdaptC/accept-c.py`, sha256 `5ac63e0d…826dca4`; `w1/stage/ExecAdaptCa/accept-ca.py`, sha256 `ac2bc93d…91b2e`). No L1 install exists yet (`reports/round-77/` holds only `telemetry/`). If L1 installs a different file, §1–§2 must be re-run against it.

## 1. Inputs and method

- Claim text: `.ufo/waves/round-77/CLAIMS-DRAFT.md` (38 lines). C after-state line 21, C kill rule line 23; Ca frozen legs/routed defects line 29, ANNOTATE/REPAIR/command line 31, Ca kill rule line 33. Full lines were read with Python (the display tool truncates long lines; no literal `…` exists in the draft).
- C frozen-config skeleton: `w1/stage/ExecAdaptC/claims-C.skeleton.json` (the only frozen-config draft; **no Ca skeleton exists** in W1).
- Leg code read end-to-end: `accept-c.py` LEGS table (lines 2381–2394), leg functions 1181–2266, `load_frozen_config` 743–933, `main` LEGCOUNT 3240–3256; `accept-ca.py` LEG_SPECS 333–426, `_git_problem`/`_git_grep_problem`/`observe_problem` 1124–1385, `run_observe` 1432.
- Selftest case lists read from `_ST_CASES` (C) and the Ca `selftest()` scenario calls.
- "Red fixture" means a scenario in the counter's own selftest that is graded red for that leg. Where none exists, I drove a probe (§5) in scratch; probes are labelled.

Commands run (scratch under `/fast/scratch/hyaku/kotodama-r77/ConnClaimsCounter/`):

```
python3 -B <scratch>/c/accept-c.py --selftest                 # exit 0; "SELFTEST: 37/37"
python3 -B <scratch>/ca/accept-ca.py --selftest               # exit 0; "SELFTEST OK: 199 checks across 51 scenarios reported-fail=0"
python3 -B accept-ca.py --ledger-check <W1 probe-real-ledger.json> --root /home/vgpnk/Projects/shokunin/kotodama-shokunin --base 211f9526800906e0c585d878d265c37e5e090c15 --work <scratch>/ca/lc
                                                              # exit 0; "LEDGER-CHECK-77: PASS pairs=11"
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin status --porcelain   # afterwards: only "?? .ufo/waves/round-77/" and "?? reports/round-77/" (pre-existing); HEAD 211f9526…
```

Probe drivers: `stage/ConnClaimsCounter/probe_c.py` (C fixtures built by the counter's own `_st_build`, one landing commit per mutation, graded by `_st_run`), `stage/ConnClaimsCounter/probe_ca.py` (direct `observe_problem` / `run_observe` on a fixture clone). Fixture toplevel asserted before every commit.

## 2. Claim C — clause → leg → red receipt

Legs (13, `LEGS` order = frozen `legs[]` in `w1/stage/ExecAdaptC/claims-C.skeleton.json`, identical): ENTRIES, ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS, SCRATCHMIRROR, COLLCHECK, FROZENCFG, INDEX.

Status key: **OK** = red selftest case and green control; **OK-probe** = enforced in code and red in a probe, no selftest case; **PARTIAL** = some sub-clause unenforced; **MISS** = promised, not enforced (probe or code-read).

### 2.1 After-state (line 21)

| Clause (C after-state) | Leg | Red fixture / receipt | Status |
|---|---|---|---|
| ACCEPT-C-77 PASS at C-lands | verdict = all 13 | `clean` → `PASS legs=13/13`; `lands-eq-freeze` → `FAIL legs=3/13`; `lands-eq-base` → refused exit 2 | OK |
| exactly one new admitted entry, 253→254 knowledge files | ENTRIES (added == frozen entries; `knowledge_before+n`) | `counts-extra-knowledge` → {ENTRIES,INDEX}; `entry-missing` → 6 legs | OK |
| registry 820→822 rows; S897/S898 mined, used-by the entry only | ROWS (new IDs == row_set; count; status; used-by == admitting entries) | `row-extra`, `row-usedby-extra` → ROWS; `pre-row-edit` → ROWS | PARTIAL — duplicate physical row line passes ROWS (probe `dupline`: 13/13, 2 physical `\| S005 \|` lines). Only real CENSUS catches it (`census-dupline.tsv`: `E04 S005 duplicate url`, exit 1). Selftest CENSUS is a stub (`_st_census_stub`). |
| two opened same-page URL+archive pairs | ROWS (`opened == access_date`; live and capture same document key) | none in selftest; probe `row-opened-other` → ROWS FAIL | OK-probe. "opened" is self-declared; no evidence cross-check on the date. |
| committed evidence quote windows | EVIDENCE (window-sha/bytes re-derive; excerpt ≥4096 chars or whole-document visible-chars; Gate quote inside window) | `evidence-window-sha`, `evidence-stamp-wrong` → EVIDENCE; J2 `gate-quote-absent` → {EVIDENCE,GATE} | OK (see §6 item 8 for self-attestation) |
| Gate: URL/date/≤25-word located quote per new row; ≥1 admit, ≥1 reject | GATE (admit row per lane ID: quote_ok, access date, frozen document key, evidence path); REJECTS (≥1 reject row) | J2 → GATE; `rejects-empty` → REJECTS | PARTIAL — no red fixture for GATE URL/date/evidence-path mismatch; "≤25 tokens" is whitespace tokens, so a CJK quote counts as one token and the ≤80-character cap is the operative limit. |
| README index/footer update | INDEX (one index row per entry, verbatim topic; heading counts; last footer total/vector; older footers byte-identical; no unexplained README line) | `index-footer` → INDEX | PARTIAL — a second index row for an existing knowledge file passes (probe `readme-dup-old`: 13/13). |
| end census exit 0 | CENSUS (`scripts/sources-census.sh validate --file --today`; exit 0; no E-code) | `census-red` (stub exit 1) → CENSUS. Real script on the duplicate fixture exits 1 (E04) — §5.3 | OK (selftest uses a stub; real-script behaviour shown by probe only) |
| counter preserves 13 lineage legs; exactly one INDEX | LEGCOUNT refusal in `main` (`theirs != ours` or duplicate) | `legcount-duplicate` → refused exit 2, names INDEX | PARTIAL — reorder/extra/missing have no C fixture (code path only at `accept-c.py:3247-3256`) |
| ROWS scope = S-row lines only; Paths/Search-log checked by INDEX, never row-diff | ROWS (`ROW_RE`); INDEX (`required_sections`) | `index-required-section` → {INDEX} only, ROWS green; my re-run: included in 37/37 | OK |
| COLLCHECK normalizes same document identity incl. **query-aware record keys** and Wayback originals | COLLCHECK + `_doc_url_key` (`accept-c.py:420-445`, `norm_url` 222) | Wayback: `collcheck-archive-identity` green. Alias: `collcheck-alias`, `collcheck-map-alias`, `collcheck-prose-only` red. **Query: MISS** — probe `docid`: `_doc_url_key(…?id=1)==_doc_url_key(…?id=2)` = True; leg-level probe `query-other-record`: S004 source cell `…/docs/alpha?id=2` → **13/13 PASS** | MISS (query-aware) |
| LEGCOUNT compares distinct ordered names and refuses duplicates | main LEGCOUNT | `legcount-duplicate` | OK for duplicates; order PARTIAL (see above) |

### 2.2 Kill rule (line 23)

| Kill clause | Leg(s) | Red fixture / receipt | Status |
|---|---|---|---|
| any leg false → claim fails | verdict | `clean` vs any red case; exit 1 on any FAIL | OK |
| do-nothing landing passing | all data legs | `lands-eq-freeze` → FAIL 3/13 (only CENSUS, SCRATCHMIRROR, FROZENCFG green); `lands-eq-base` refused | OK |
| wrong source | ROWS (opened, same-document capture); GATE (frozen document in admit row); EVIDENCE (fetch/url doc, http 200, challenge, access-date); REPOINTED (source line names the row's document) | `src-wrong-doc` → REPOINTED (probe); `ev-http403`, `ev-challenge`, `ev-access-other` → EVIDENCE (probe); `row-opened-other` → ROWS (probe). **Escapes:** `ev-wrong-doc` 13/13, `caps-source-wrong-doc` 13/13 (§6 items 7) | PARTIAL / MISS |
| unopened source | EVIDENCE (`http-status`, `challenge`), ROWS (`opened`) | probes above → red. No selftest case. `ev-sha-zeroed` (body digest replaced with zeros) → **13/13** — body digest is shape-checked only (§6 item 8) | OK-probe / PARTIAL |
| wrong quote | GATE + EVIDENCE | `gate-quote-absent` (J2) → {EVIDENCE, GATE} | OK |
| duplicate document map | COLLCHECK; `_cfg_row_set` | none. Config probe `dup-document-two-lanes` ACCEPTED (§5.10) | MISS (config level) |
| missing document map | COLLCHECK (map optional) | `rowset-only-map-absent` → **13/13** (map absent is legal by design, SCHEMA-NOTE "Absent is legal") | MISS as written — the kill rule says "missing" fails; the counter treats an absent map as legal. Either the rule or the counter must change. |
| changed pre-existing row outside rule-2 cells | ROWS | `pre-row-edit` → ROWS; `pre-row-rule2-cell` green | OK (removal and reorder of pre-existing rows: code only) |
| non-admitted `used-by` | ROWS (used-by == admitting entries) | `row-usedby-extra` → ROWS | OK |
| either source outside claim scope | ROWS (new IDs == row_set); REPOINTED (inline ID must resolve to a lane or base row; staged/campaign IDs refused) | `row-extra` → ROWS; `body-staged-id` and `body-unresolved-id` → REPOINTED (probe) | OK (REPOINTED inline-ID cases have no selftest case) |

### 2.3 Claim-body clauses that the after/kill rules rely on

| Clause (draft line) | Leg | Status |
|---|---|---|
| Adopt ONE entry; remove legacy S886/S888/S889/S890/S891/S896 (line 12) | REPOINTED (`removed_ids`) | OK — `repointed-legacy-id` (S886 kept in body); legacy on a `source:` line → refused by code (`accept-c.py:1288`) |
| each new factual line carries exactly one source ID (line 12) | CITEDLINES (committed tool at lands) | **MISS** — zero-ID lines pass (probe `zero-id` 13/13). Two-ID lines red (`cited-two-id` → CITEDLINES). The tool itself is lands-controlled (`cited-stub` 13/13). |
| refused staged IDs S933,S934,S936,S939–S944 not appended; refused files by exact filename in the Gate (line 19) | REJECTS (`refused_staged`, derived from `refused_staged_text`) | IDs: OK (refused ID as lane row → code `accept-c.py:2100-2104`; no fixture). **Files: MISS** — `cfg["refused_files"]` is loaded (`accept-c.py:827-833`, `915`) and read by no leg; the clean fixture declares `naming-systems.amend-2026-10-24.md` in `rejects.refused_files`, does not name it in the Gate, and is 13/13 (`stage/ConnClaimsCounter/refused-files-and-terms-unread.txt`; clean control 13/13 in `probe_c.out`). |
| `ground.sweeps` absent at base, present in entry (line 10) | GROUND | `ground-before-present`, `ground-after-missing` → GROUND. OK. |
| `ground.terms` 單名/雙名 (skeleton) | none | **MISS** — `cfg["terms"]` is loaded (`accept-c.py:816`, `912`) and no leg reads it (receipt in `refused-files-and-terms-unread.txt`). |
| "no Chinese-language system-level account" (line 10) | none (GROUND checks URL-string sweeps only) | Not gradeable by the counter; the claim's negative absence rests on the W1/W2 sweeps, not on a leg. Informational. |
| START and END census receipts (line 37) | CENSUS (`census_start.rows` substring "820") | PARTIAL — `str(820) in text` substring test; `census-start` exit-line check present (`accept-c.py:2159-2184`). |

## 3. Entry source IDs and `required_sections` (the named focus)

### 3.1 Entry source-ID rules and their checks

| Rule | Check | Red receipt | Status |
|---|---|---|---|
| one ID per `source:` line | REPOINTED (`len(ids)!=1`, `accept-c.py:1288` region) | `src-multi-id` → REPOINTED+CITEDLINES (probe) | OK-probe |
| source line URL names the row's document | REPOINTED (intersection of `_doc_url_key`) | `src-wrong-doc` → REPOINTED (probe); `repointed-source-no-url` (selftest) | OK |
| legacy IDs absent from entry (source line and body) | REPOINTED (`removed_ids`) | `repointed-legacy-id` | OK |
| campaign/staged IDs not cited as lane rows | REPOINTED (`staged` universe) | `body-staged-id` → REPOINTED (probe) | OK-probe |
| every inline ID resolves to lane or base row | REPOINTED | `body-unresolved-id` → REPOINTED (probe) | OK-probe |
| every lane row cited by the entry (no orphan) | ROWS (`cited.get(sid)` empty → orphan) | `orphan-lane-row` → ROWS (probe) | OK-probe |
| cited IDs `mined` and present at lands | ENTRIES | code only (`accept-c.py:1387-1399`) | OK-code (no fixture) |
| `source:` line recognition: `Source:` (capital) and `**source:**` forms | REPOINTED/ENTRIES/ROWS via `source_field_lines` (`accept-c.py:1040-1043`, regex `^[-*\s]*source:`, case-sensitive) | `**source:**` recognised (probe §5.5). **`Source:` (capital) not recognised** — `caps-source-wrong-doc` → 13/13 | MISS |
| "exactly one source ID per factual line" | CITEDLINES (tool) | `cited-two-id` red; `zero-id` green (MISS); `cited-stub` green (tool unpinned) | MISS (zero-ID) / PARTIAL |

### 3.2 `required_sections` — what is checked, and what is not

- Checked: INDEX loops `cfg["required_sections"]` (`accept-c.py:1882-1906`); each record's `pattern` must hit ≥`min` lines of `path` (default: every admitted entry when `path` is empty). Red receipt: `index-required-section` → {INDEX} only, ROWS green (selftest; re-run in §1).
- Loader refuses empty/absent lists and non-compiling patterns (`_cfg_required_sections`, `accept-c.py:549-585`).
- Not checked / weak:
  1. **Only one negative case exists** (drop the appended lines). No fixture for wrong-file, path-less record, `min>1`, or a pattern that matches a line that is not appended (pre-existing text would satisfy a pin).
  2. **Non-vacuity at base is verified** (`stage/ConnClaimsCounter/probe_required_sections_base.out`): both pins return **0 hits** at base `corpus/SOURCES.md`. So neither pin is trivially satisfied by existing text.
  3. **Satisfiability is not yet shown.** No draft of the `## Paths` bullet or the round-77 `## Search log` entry exists in the W1 drafts: `w1/drafts/` has no `corpus/SOURCES.md`, and the pins match no line in the three drafts that mention S897 (entry, lesson, scorecard section). The pins are literal regexes the writer must hit exactly (`^- [^\n]*S897[^\n]*S898`; `(?i)^\*\*[^*]*naming-system[^*]*\(round 77\)`). The second pin requires the hyphenated word `naming-system` inside the bold title, which is not the form of the base search-log headings (e.g. `**State-standard calendar compilation (round 76).**`). The pins must be fixed to the literal text before freeze (SCHEMA-NOTE open choice 1).
  4. **Line-bound patterns vs wrapped base entries.** Base `## Paths` entries wrap across lines (`probe_required_sections_base.out`, base lines 857–858: `- Typology evidence chain — S001 → S002 → S003 → S004: name the languoid in` / `  Glottolog first …`). The Paths pin needs S897 and S898 on one physical line. A wrapped Paths entry fails INDEX even when the content is right.
  5. The Search-log pin does not check the searched-set count or the Gate linkage; that is CritFrontier's ground, but the counter cannot see it.

## 4. Claim Ca — clause → leg → red receipt

Legs (12): LEDGER, BASEMISMATCH, REPAIR, ANNOTATE, APPENDONLY, R1EXEMPT, NOSTUB, SEPARABLE, COMBINED, RECEIPTS, FROZENCFG, STAMP. (Order note: the draft line 29 lists `RECEIPTS, COMBINED`; the counter's `--emit-legs` order is `COMBINED, RECEIPTS`. Same set; freeze must take the counter order. Draft text should be fixed.)

| Clause (draft lines 29–33) | Leg | Red receipt (Ca selftest scenario, unless noted) | Status |
|---|---|---|---|
| ≥10 unique pairs; frozen at freeze in `reports/round-77/ledger.json` | LEDGER (`min_pairs`, `duplicate id`); FROZENCFG | `min-pairs` (LEDGER, BASEMISMATCH); `worktree-only-ledger`; `config-edit-ledger` | OK. "unique" = unique `id` only; two pairs with identical `stated_at`+token under different IDs both count (code, `accept-ca.py:1785-1795`). |
| candidate W1 pairs are data to verify | LEDGER, BASEMISMATCH | `fabricated-base-observation`; `green-pair`; `stated-line-mismatch` | OK |
| 12-leg lineage set; ordered list equals `legs[]`; reject duplicates | main: `frozen_names != list(REQUIRED_LEGS)` (`accept-ca.py:2899`) | `legcount` (11 names) → refused; `legorder` (swap) → refused. Duplicate: implicit (equality against a unique table), no duplicate fixture | OK (duplicate implicit) |
| `stated_at` in exact disposition-specific allowlists | LEDGER (`classify_stated_at`, `_allow_for`) | `stated-at-out-of-allowlist`; `annotate-on-mutable`; `repair-not-mutable`; `protected-in-place`; `unnamed-in-place` (APPENDONLY) | OK |
| `stated_text` present at named base line | LEDGER / BASEMISMATCH | `stated-text-absent`; `stated-line-mismatch` | OK |
| observe/rederive: validated argv | LEDGER → `observe_problem` (`accept-ca.py:1353`) | `shell-string`, `interpreter`, `constant-printer`, `out-of-clone`, `dead-pin`, `no-c-form`, `bare-assign`, `escaped-pipe`, `rederive-backtick`, `no-rederive` | OK for these |
| — `git -C <lane>` first | `_git_problem` (`args[0] != "-C"`) | `no-c-form`; probe: no `-C` → REFUSED | OK |
| — immutable 40-hex revision in revision position | `_git_rev_problem` only checks 40-hex existence; any other token in a rev slot is accepted | `dead-pin` covers a non-existent 40-hex only. Probe `probe_ca.out`/`probe_ca2.out`: `git -C <clone> log -1 main -- LOG.md` **ACCEPTED**; `log -1 no-such-branch -- LOG.md` **ACCEPTED**; `show main:LOG.md` **ACCEPTED**; `show HEAD~0:LOG.md` **ACCEPTED** | **MISS** |
| — `--` before repo-relative paths | `_git_problem`/`_git_grep_problem` skip `--` (`a == "--": continue`); never required | probe `probe_ca.out`: `git -C <clone> log -1 <40hex> LOG.md` **ACCEPTED** | **MISS** |
| — no bare `name=value` operands | `BARE_ASSIGN_RE` in git/grep/diff operands | `bare-assign` | OK |
| validated argv is what executes (no option that runs a program or writes outside the clone) | option loops are inert: `_git_problem` (`accept-ca.py:1155-1158`), `_git_grep_problem` (`1184-1187`), `_git_diff_problem` (`1232-1234`) | **MISS, confirmed by execution.** `observe_problem(['git','-C',clone,'grep','--open-files-in-pager=touch <marker>','-e','A01','LOG.md'])` → None (accepted); `run_observe` → `('', 'exit=0')` and the marker file **exists** (`probe_ca_pager.out`). `git diff --output=<path> <40hex> -- LOG.md` accepted; `run_observe` writes the file outside the clone (`probe_ca_diffout2.out`) | **MISS** — arbitrary program execution from a "validated" argv |
| `REPAIR` post-state observed at lands | REPAIR | `expected-after-mismatch`; `repair-no-statement`; `shadow-repair` | OK |
| ANNOTATE rows under `## Corrections — round 77` with pair id, old token, observed token, per-pair command | ANNOTATE; NOSTUB | `annotate-other-token`; `stub-rows`; `no-rederive` | OK |
| REPAIR touches only {README, SKILL, SHONEN}; only on proven base mismatch | REPAIR (`REPAIR_MUTABLE`); BASEMISMATCH | `repair-not-mutable`; `annotate-on-mutable` | OK |
| removed append-only line → red | APPENDONLY | `append-only-removal` | OK |
| R1: rule-2 cell edits exempt; teaches-cell edits red | R1EXEMPT; APPENDONLY | `r1-rule2-exempt`, `r1-teaches-red`, `r1-mixed-red` | OK |
| committed receipt blobs at freeze | RECEIPTS | `uncommitted-receipt`; `fixtures-absent` | OK |
| COMBINED README exemption carries path+line | COMBINED | `readme-exemption-no-line`; `combined-missing-entry`; `combined-required` | OK |
| no C-added path/S-ID in Ca read set | SEPARABLE | `separable-lane-row`; `separable-family` | OK |
| stamp: stamped == evaluated == measured == lands | STAMP | `stamp-measured` | OK |
| frozen config from `git show <freeze>`; freeze on first-parent chain | FROZENCFG | `freeze-off-first-parent`; `config-edit-claims` | OK |
| NOSTUB (no placeholder tokens) | NOSTUB | `stub-rows` | OK |
| PASS 12/12 required | verdict | `do-nothing` → exit 1 with REPAIR/ANNOTATE/NOSTUB red; `clean` → 12/12 | OK |
| real 11-pair ledger | LEDGER | `ledger-check-real.out`: `LEDGER-CHECK-77: PASS pairs=11` | OK (pairs D01–D10 use a 40-hex base; D11 is a bare `grep` on `corpus/README.md`; §4.1) |

### 4.1 Observation on the real ledger
The real ledger passes the validator, but only because its commands use the strict form. Probe-real-ledger D01–D10: `['git','-C','.','grep','-c','-E','^#','211f…','--','LOG.md']`. D11: `['grep','-o','-E','Total knowledge entries: [0-9]+','corpus/README.md']`. The defects in §4 therefore have no current effect on the 11 candidate pairs; they are latent escapes in the validator that a future or altered ledger would exercise.

## 5. Probe receipts

All probes: scratch fixtures under `/fast/scratch/hyaku/kotodama-r77/ConnClaimsCounter/probe/`; raw output copied to the stage directory.

### 5.1 Control and CITEDLINES (`probe_c.out`)
```
== control: exit=0 verdict=ACCEPT-C-77: PASS legs=13/13
== dupline: exit=0 verdict=ACCEPT-C-77: PASS legs=13/13      (physical S005 lines at lands: 2)
== cited-two-id: exit=1 verdict=ACCEPT-C-77: FAIL legs=12/13  failing: ['CITEDLINES']
== cited-stub: exit=0 verdict=ACCEPT-C-77: PASS legs=13/13
== zero-id: exit=0 verdict=ACCEPT-C-77: PASS legs=13/13
```
`cited-stub` replaces `tools/check-cited-lines.py` in the landing commit with a stub that prints `CITED-LINES: 0 finding(s)`; the entry keeps the two-ID line. `zero-id` appends an uncited factual sentence to the entry.

### 5.2 Query-keyed identity (`probe_c.out`, `probe_c_query.out`)
```
_doc_url_key('https://example.org/record?id=1')=('example.org', '/record')
_doc_url_key('https://example.org/record?id=2')=('example.org', '/record')  equal=True
_doc_url_key('https://example.org/docs/alpha?view=print')=('example.org', '/docs/alpha')  equal=True
== query-other-record: exit=0 verdict=ACCEPT-C-77: PASS legs=13/13
S004 row at lands: | S004 | … live https://example.org/docs/alpha?id=2 ; same page captured … at https://web.archive.org/…/docs/alpha?id=2 …
```

### 5.3 Duplicate physical row, real census (`census-control.tsv`, `census-dupline.tsv`)
```
control : physical S005 lines = 1 ; sources-census.sh validate → exit=0, "file ok …"
dupline : physical S005 lines = 2 ; sources-census.sh validate → exit=1, "file E04 S005 duplicate url example.org/docs/beta within scope fixture scope"
```
ROWS counts `parse_rows` dict keys (`accept-c.py:308-314`, `leg_rows` `len(lands_rows) != want_rows`), so the second line is invisible to it.

### 5.4 Evidence (`probe_c_evidence.out`)
```
ev-http403       EVIDENCE=FAIL  (failing: ['EVIDENCE'])
ev-challenge     EVIDENCE=FAIL
ev-wrong-doc     PASS legs=13/13      <- fetch: names gamma, url: still names alpha
ev-sha-zeroed    PASS legs=13/13      <- sha256 body digest replaced with 0*64
ev-access-other  EVIDENCE=FAIL
row-opened-other ROWS=FAIL            (S004 opened 2026-10-20 vs access date)
```
Cause for `ev-wrong-doc`: `_evidence_doc_keys` (`accept-c.py:992-1000`) is a union over `fetch`, `url` and `final-url`; any one naming the frozen document passes. Cause for `ev-sha-zeroed`: the body `sha256:` is only shape-checked (`accept-c.py:1935-1936`, `re.fullmatch(r"[0-9a-f]{64}", digest)`); only the window digest is re-derived.

### 5.5 Source lines (`probe_c_source.out`, plus parser output in `probe_c.out`)
```
src-multi-id         REPOINTED=FAIL CITEDLINES=FAIL  (11/13)
src-wrong-doc        REPOINTED=FAIL
body-staged-id       REPOINTED=FAIL
body-unresolved-id   REPOINTED=FAIL
orphan-lane-row      ROWS=FAIL
caps-source-wrong-doc PASS legs=13/13   <- "Source: S005 — https://wrong.example/other"
source_field_lines(mixed-case text) = ['S897 — https://example.org/docs/alpha ; lane row S897', '** S898 — https://example.org/docs/beta']
```
The regex `^[-*\s]*source:` (`accept-c.py:1040-1043`) is case-sensitive; the capital-S line is not returned.

### 5.6 README (`probe_c_readme.out`)
```
readme-dup-old PASS legs=13/13    <- second index row `- \`sample.md\`` for an existing base knowledge file
```
INDEX exempts any added README row whose file name is in the base knowledge tree (`accept-c.py:1863-1864`).

### 5.7 Required-section pins at base (`probe_required_sections_base.out`)
```
base hits for '^- [^\n]*S897[^\n]*S898' = 0
base hits for '(?i)^\*\*[^*]*naming-system[^*]*\(round 77\)' = 0
```

### 5.8 Ca validator (`probe_ca.out`, `probe_ca2.out`)
```
control: -C, 40-hex rev, --, path                           ACCEPTED
no `--` before repo-relative path (log -1 <40hex> LOG.md)   ACCEPTED
mutable branch name in rev slot (log -1 master -- LOG.md)   ACCEPTED   (master does not exist in fixture)
mutable branch name in rev slot (show master:LOG.md)        REFUSED: does not resolve   (fixture has no master)
HEAD~0 relative rev in rev slot (show HEAD~0:LOG.md)        ACCEPTED
no -C (control)                                             REFUSED   (round-76 form)
-- probe_ca2 (fixture branch 'main') --
show main:LOG.md                                            ACCEPTED
log -1 main -- LOG.md                                       ACCEPTED
log -1 no-such-branch -- LOG.md                             ACCEPTED
```

### 5.9 Option-driven execution (`probe_ca_pager.out`, `probe_ca_diffout2.out`)
```
pager probe argv: ['grep', '--open-files-in-pager=touch <scratch>/pwned-marker', '-e', ...]
observe_problem -> None
run_observe -> ('', 'exit=0')
marker created by counter executor: True
```
```
observe_problem(diff --output, 40-hex rev) -> None
run_observe -> ('', 'exit=0')
file written outside clone: True
```
Note: `run_observe` itself does not re-validate. The validator is the gate: `pair_problems` calls `observe_problem` at `accept-ca.py:1626` before executing; the validator accepts both forms, so the gate is open.

### 5.10 Row-set config (`probe_c_rowset.out`)
```
dup-document-two-lanes       -> ACCEPTED  [('S897', ['S897'], 'http://lishisuo.cssn.cn/x.shtml'), ('S898', ['S903'], 'http://lishisuo.cssn.cn/x.shtml')]
one-staged-id-two-lanes      -> ACCEPTED  [('S897', ['S903'], …), ('S898', ['S903'], …)]
control-distinct             -> ACCEPTED
```
`_cfg_row_set` refuses only a repeated lane ID (`accept-c.py:522-546`).

## 6. Promised but not checked — consolidated list

Ranked by consequence. "Promised" = in the frozen clause text (line cited).

| # | Clause (line) | Gap | Evidence | Severity |
|---|---|---|---|---|
| 1 | Ca: validated argv, no executable side effects (29) | Option-driven program execution (`git grep --open-files-in-pager`) and file write (`git diff --output`) pass the validator and run through `run_observe` | §5.9 | High |
| 2 | C: CITEDLINES tool is the per-line citation contract (line 12, via tool) | Tool is lands-controlled, FROZENCFG does not pin it; counter executes lands Python (`accept-c.py:1579`) | §5.1 `cited-stub` | High |
| 3 | C: COLLCHECK "query-aware record keys" (21) | Query dropped by `norm_url`; distinct records on one path are one document | §5.2 | High |
| 4 | Ca: immutable 40-hex in rev position; `--` before paths (29) | Not enforced (`log`, `show`, `grep` accept names, `HEAD~0`, no `--`) | §5.8 | High |
| 5 | C: refused files by exact filename in the Gate (19) and frozen `rejects.refused_files` | Loaded, never graded; frozen list has 2 of the 10 named non-adopted files (8 missing: `…23b`, `…23c`, `…24-r11` … `…24-r16`) | `refused-files-and-terms-unread.txt` (clean fixture 13/13 without the file) | High |
| 6 | C: each new factual line exactly one source ID (line 12) | Zero-ID lines pass; tool only flags ≥2 | §5.1 `zero-id` | Medium |
| 7 | C: entry source IDs — `source:` line names the row's document | Capital `Source:` line not parsed; `EVIDENCE` fetch check is an OR over fetch/url/final-url | §5.4, §5.5 | Medium |
| 8 | C: unopened source (21/23) | Body digest shape-only; no selftest for challenge/http/fetch/opened; evidence self-attests | §5.4 | Medium |
| 9 | C: ROWS 820→822 registry rows | Duplicate physical row passes ROWS; only real CENSUS catches it; selftest CENSUS is a stub | §5.3 | Medium |
| 10 | C: duplicate / missing document map (23) | Duplicate documents and one staged ID → two lanes accepted at config; absent map is legal (kill rule says missing fails) | §5.10, §2.2 | Medium |
| 11 | C: `required_sections` (draft line 21: "checked by INDEX"; SCHEMA-NOTE) | Only the drop case is red; no drafted text; line-bound pin vs wrapped Paths entries; search-log pin needs the literal hyphenated word | §3.2, §5.7 | Medium |
| 12 | Ca: ≥10 unique pairs (29) | Uniqueness by `id` only | §4 row 1 | Low |
| 13 | C: `ground.terms` 單名/雙名 (skeleton) | Declared, never graded | `refused-files-and-terms-unread.txt` | Low |
| 14 | C: README footers/index (21) | Extra index row for an existing file passes INDEX | §5.6 | Low |
| 15 | C: FROZENCFG (21) | Does not pin the counter, CITEDLINES tool, census script, or the staged-ids file; only `claims.json` bytes | `accept-c.py:1181-1256` | Medium (ties to #2) |
| 16 | C/Ca: LEGCOUNT reorder/extra/missing (21, 29) | No C fixture for reorder/extra/missing (Ca has legcount/legorder; duplicate implicit) | §2.1 | Low |
| 17 | C: census-start receipt rows (37) | Substring `"820" in text` | `accept-c.py:2159-2184` | Low |
| 18 | Draft line 29 Ca leg order | `RECEIPTS, COMBINED` vs counter `COMBINED, RECEIPTS` | `--emit-legs` | Low (fix text before freeze) |
| 19 | C body line 10: "no Chinese-language system-level account" | Not a leg; GROUND greps URL strings | §2.3 | Informational |

## 7. Fix directions (scoped; not applied — my assignment is attack-only)

- #1: validator must allowlist git subcommand options per subcommand and refuse anything else (`--open-files-in-pager`, `-O`, `--output`, `--exec*`, `--ext-diff`, `-c`); execute with `GIT_PAGER=cat`, `PAGER=cat`, `GIT_EXTERNAL_DIFF` unset.
- #2: pin the CITEDLINES tool blob in FROZENCFG (or copy it from `<freeze>`); never execute a file from the graded tree.
- #3: keep the query in the document key (or list query-keyed hosts explicitly); add a red fixture `query-other-record`.
- #4: require a 40-hex revision in every revision slot of `log`/`show`/`grep`/`diff`/`ls-tree`; require `--` before the first path operand; add red fixtures for each.
- #5: grade `refused_files` (each named file must occur in the Gate reject table); freeze the full 10-file list; add a red fixture.
- #6: count ID-less factual lines in the CITEDLINES contract, or state in the claim text that "exactly one" means "at most one".
- #7: match `source:` case-insensitively and per line; require `fetch:` (not an OR over three fields) to name the document; add `Source:` and `fetch` red fixtures.
- #8: recompute the body digest from the stored body; add red fixtures for `challenge`, `http-status`, `fetch`, `opened`.
- #9: make ROWS count physical row lines and refuse duplicates; run the real census in a selftest or a red fixture.
- #10: refuse duplicate documents and duplicate staged-to-lane mappings in `_cfg_row_set`/`_map_pairs`; state whether a missing map fails (kill rule) or is legal (SCHEMA-NOTE) and align the two.
- #11: pin the two `required_sections` regexes to the literal appended text after drafting; add wrong-file and path-less fixtures.
- #15: extend FROZENCFG to the tool and census script blob digests.

## 8. Installs, writes, scratch

- Installs / updates: **none**. Python 3 stdlib only. `/home/vgpnk/.omp/agent/RULES.md` read (tooling directive); no package or tool installed.
- Writes: this report; `.ufo/waves/round-77/w2/stage/ConnClaimsCounter/` (probe drivers, probe outputs, selftest re-runs, census outputs, ledger-check output, counter copies, `counter-sha256.txt`, `receipts-sha256.txt`, `base-SOURCES.md`, `refused-files-and-terms-unread.txt`). Nothing under `reports/**`, `corpus/**`, `LOG.md`, `SCORECARD.md`, `SKILL.md`, `SHONEN.md`, the fleet root, `scripts/`, `.ufo/state`, sibling lanes, lane git/index/jj, or `~/.local/bin`.
- Lane git state after my runs: HEAD `211f9526…`; `git status --porcelain` shows only the pre-existing `?? .ufo/waves/round-77/` and `?? reports/round-77/`.
- Scratch: `/fast/scratch/hyaku/kotodama-r77/ConnClaimsCounter/` (fixtures, counter copies, probe work dirs). Deleted before yield.
- Unrun / limits: no L1-installed `reports/round-77/accept-*.py` or frozen `claims.json`/`ledger.json` exists, so all runs used W1 staged counters and skeleton-shaped configs built by each counter's own fixture builder; the real `--fleet-root` census was run only on fixture registries; the real round-77 freeze, lands and evidence captures do not exist and were not run.
