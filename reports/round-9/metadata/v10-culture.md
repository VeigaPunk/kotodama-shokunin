# V10 — culture-material frontmatter re-audit (round 9)

- worker: V10 (metadata shard — "culture-material all"; deliverable `reports/round-9/metadata/v10-culture.md`)
- partition: `corpus/knowledge/culture-material/` — all 16 entries
- mandate: `reports/round-9/targets.json` → `metadata_verify` ("11 shards re-audit all 179 corpus/knowledge entries for complete source/verified-at/recheck frontmatter after round 8's sweep; fix stragglers in place; fragments under reports/round-9/metadata/ + 1 auditor shard")
- date: 2026-10-17; re-audit run window 20:49–20:53Z (all timestamps from `date -u`)
- baseline: `e1694bad6ac96aca45a11ca5746582b275929355` (claims.json/targets.json); working tree opened at `a7bb205`; this shard's two in-place fixes are left uncommitted for the orchestrator's once-per-round commit
- completeness criterion used: exactly one standalone `- sources:` (or block form), one `- verified-at:` and one `- recheck:` line, in the entry's head block (text before the first `## ` heading); `verified-at` dated and scope-bearing; every `couples` reference resolving — the format round-8's M10 sweep established and the one all 16 partition files use
- scope note: §1–§4, §6–§8 cover only this shard's 16 files. §5 records a full-corpus snapshot taken as a courtesy for the other shards and the auditor; it is a snapshot of a live parallel round, not a fix report.

## 1. Result at round-9 open (before-state)

All 16 files carried the full field set at open — nothing to repair for completeness. Two residual classes from round 8 remained fixable inside the partition; both were fixed (§2).

- Every file: exactly one `- sources:` (one line or an indented block), one `- verified-at:`, one `- recheck:`; all `verified-at` dated 2026-10-17 and scope-bearing; zero duplicate or misplaced field lines.
- Hash drift check: all 16 sha256-first-16 values matched round-8 M10's documented after-state (`reports/round-8/metadata/m10-culture.md` §2) at open — no byte changed between the round-8 sweep and this re-audit.
- Couples integrity: the round-8 verification script (embedded verbatim in §6.A) returned `ALL_OK 16 files` at open and again after this shard's edits; 0 dangling references (the pattern's per-file unique refs sum to 206 across the partition).
- Structural spot-checks: no stray `---` YAML fences; every file's first-line title intact; every `sources` block substantive (min 2,104 chars `textile-technology.md`, max 6,733 `material-culture-inference-method.md`).

## 2. Changes landed by this shard (2 files; all others untouched)

Neither change rewrites content; both replace a weaker receipt with the receipt this round actually obtained, under the round-8 discipline of stating exactly what was checked and at what access level.

### 2.1 `material-culture-inference-method.md` — Sauvet & Wlodarczyk 2008 residual resolved

- Before: `sha256[:16]` `80d1b049aab73b25`; `verified-at` tail read "Sauvet & Wlodarczyk 2008 (Rock Art Research 25(2)) is not Crossref-indexed — to-verify."; recheck demanded "without an independent index hit".
- Receipt: OpenAlex record `W2196576233` — "Towards a Formal Grammar of the European Palaeolithic Cave Art", *Rock Art Research* 25(2), first page 165, 2008, DOI `10.69978/rar.v25i2.30`, authors Georges Sauvet & André Włodarczyk (fetched 2026-10-17; full record §3 R1). A Crossref bibliographic query still returns no direct record (§3 R2) — the OpenAlex hit is the independent index.
- After: `sha256[:16]` `7cc44399f81ab210`. `verified-at` now: "Sauvet & Wlodarczyk 2008 resolved by the round-9 re-audit: OpenAlex record W2196576233 (Rock Art Research 25(2), first page 165, 2008, DOI 10.69978/rar.v25i2.30; fetched 2026-10-17), while a Crossref query still returns no direct record." Recheck now scopes the remaining limit: "beyond the index-confirmed record (OpenAlex, 2026-10-17 — pages past 165 not inspected)". The inline bibliography (line 14) and body mention (line 107) are unchanged — they already read `25(2):165–172`; the last page was not independently confirmed, and the receipt says so.

### 2.2 `era-periodization-models.md` — Korean era-law legs re-checked

- Before: `sha256[:16]` `bf6b7985ce51bdda`; `verified-at` tail read "Korean-law legs not re-fetched."
- Receipt: ko.wikisource full text of 연호에 관한 법률 (fetched 2026-10-17) shows: main text "대한민국의 공용(公用) 연호(年號)는 서력기원(西曆紀元)으로 한다"; 부칙 `<제775호, 1961.12.2.>` — "①본법은 단기 4295년 1월 1일부터 시행한다. ②법률 제4호 연호에관한법률은 이를 폐지한다. ③…단기연대에서 2333년을 감하여 이를 서력연대로 간주한다." (§3 R3). The sources-line claims (법률 제775호 1961; 서력기원 from 1 January 1962; repealing the 1948 law) are supported; the 1948 promulgation date of 법률 제4호 was not independently re-dated this pass and the receipt says so.
- After: `sha256[:16]` `889198a64f1b07ba`. `verified-at` now carries the ko.wikisource receipt, the law.go.kr access failure (JS shell, no extractable text — §3 R4), and the un-re-dated 1948 date.
- Round-8's deferred items in this file are untouched: the raw `symbol (…)` / `era (…)` aliases in the `couples` line (line 16) remain, per §4.2.

### 2.3 Decision: no re-stamps on the other 14 files

The other 14 files were already complete and byte-clean against the round-8 handoff; adding a round-9 "re-audited" clause to each `verified-at` line was considered and rejected as churn with no evidence content (the re-audit result for them is exactly this fragment + §1's drift check). Their `verified-at` access-level statements therefore remain round-8 statements, and this fragment is the round-9 audit of record for them.

## 3. Fresh retrieval receipts (2026-10-17)

Each receipt names the exact URL/command, access date, and support scope. Machine note: `/tmp` showed transient exhaustion during this window (a redirect capture to `/tmp/gate_out` failed with "No space left on device"; two `curl -o /tmp/...` attempts errored with `curl: (23) client returned ERROR on write`); a re-check at 20:50Z showed `/tmp` 6.7G/16G used (8.5G free), so the condition was transient contention from the parallel round. All receipts below were re-taken via stdout pipes, no temp files.

- **R1 — Sauvet & Wlodarczyk 2008, positive.** `https://api.openalex.org/works?search=Towards%20a%20Formal%20Grammar%20of%20the%20European%20Palaeolithic%20Cave%20Art` → top hit exact; then `https://api.openalex.org/works/doi:10.69978/rar.v25i2.30` → title, 2008, *Rock Art Research*, vol 25, issue 2, first_page 165, DOI, authors Sauvet/Włodarczyk, ID W2196576233. Scope: index record only; article content not read.
- **R2 — Sauvet, Crossref negative control.** `https://api.crossref.org/works?query.bibliographic=Sauvet+Wlodarczyk+formal+grammar+European+Palaeolithic+cave+art&rows=3` → no matching record (unrelated Creswell Crags items). Scope: "not Crossref-indexed" remains true; recorded in the file.
- **R3 — 연호에 관한 법률, positive.** `https://ko.wikisource.org/wiki/연호에_관한_법률` (HTTP 200), text extracted: main text + 부칙 제775호 (1961.12.2, effective 단기 4295년 1월 1일 = 1962-01-01; repeals 법률 제4호; 단기→서력 −2333 conversion rule). Scope: statute text as republished on Wikisource; provenance of the transcription itself not audited.
- **R4 — law.go.kr, documented access failure.** `https://www.law.go.kr/LSW/lsSc.do?...query=연호에 관한 법률` (HTTP 200) returns only the JS application shell — no law text extractable by plain fetch. Fallback: R3.
- **R5 — Wiktionary "tattoo" (re-verify, `adornment-body-codes.md`).** `https://en.wiktionary.org/wiki/tattoo` (HTTP 200; grep hits: Polynesian ×11, Samoan ×10, tatau ×14). Scope: donor-chain leg re-confirmed at page level.
- **R6 — mechon-mamre Exodus 28 (re-verify, `ritual-garments.md`).** `https://mechon-mamre.org/p/pt/pt0228.htm` (HTTP 200; breastplate ×11, ephod ×12). Scope: prescription text re-confirmed.
- **R7 — ja.wikisource 元号法 (re-verify, `era-periodization-models.md`).** `https://ja.wikisource.org/wiki/元号法` (HTTP 200; 元号は、政令で定める ×1, 皇位の継承 ×1, 昭和五十四年六月十二日 ×7, 法律第四十三号 ×5). Scope: the four checked strings re-confirmed.
- **R8 — Crossref Ogilvie (re-verify, `craft-artisan-lexicon.md`).** `https://api.crossref.org/works/10.1257/jep.28.4.169` → "The Economics of Guilds", *Journal of Economic Perspectives*, 2014-11-01.
- **R9 — Crossref Alesina/Giuliano/Nunn (re-verify, `material-culture-inference-method.md`).** `https://api.crossref.org/works/10.1093/qje/qjt005` → "On the Origins of Gender Roles: Women and the Plough", *QJE*, 2013-05-01.
- **R10 — Wikipedia sample (re-verify).** `https://en.wikipedia.org/wiki/Sumptuary_law` (hits "1363" ×2; `sumptuary-law-rank-display.md`); `https://en.wikipedia.org/wiki/Uma-jirushi` (hits uma-jirushi ×7; `warrior-material-culture.md`).
- **R11 — drift check (no retrieval).** sha256[:16] of all 16 files compared to `reports/round-8/metadata/m10-culture.md` §2 after-state: 16/16 match at open.

## 4. Audit observations (no edit applied; recorded for the orchestrator/auditor)

### 4.1 `to-verify` inventory of the partition after this round

`python3 tools/source-audit-inventory.py --json --summary --baseline round9-v10` (read-only; filter `culture-material/`), raw occurrences (markers = parenthesized `(to-verify)` form):

| file | raw lines | raw occurrences | markers |
|---|---|---|---|
| cuisine-food-lexicon.md | 2 | 2 | 0 |
| dress-through-eras.md | 1 | 1 | 1 |
| ritual-garments.md | 3 | 3 | 2 |
| all other 13 files | 0 | 0 | 0 |

`material-culture-inference-method.md` fell 1 → 0 in this round (the Sauvet resolution, §2.1). The three files above carry the same round-8-or-earlier residuals (Brazil purple-mourning association; "gates of hell" sobriquet; Thai palette record) — none resolvable from the sources already used, none newly hidden.

### 4.2 Raw `couples` aliases carried (round-8 §4.3 deferred class)

Unchanged this round, as the mapping is a multi-target editorial choice (not a metadata fix): `calendar-festival-systems.md` line 19 (`symbolism (…cycle arithmetic…)`, `symbol (luck systems riding on weekdays)`); `cuisine-food-lexicon.md` line 20 (`symbol (bread-and-salt covenant symbolism; coin-in-cake)`); `era-periodization-models.md` line 16 (`symbol (number symbolism, decline-to-renewal axis, gold-as-first-metal)`, `era (this entry is the era-system core)`). Still flagged for the lane's couples-hygiene pass; `to-verify` in effect.

### 4.3 Receipt convention note

The partition contains 0 raw `https://` strings (`grep -rno 'https\?://' corpus/knowledge/culture-material/ | wc -l` → `0`): `verified-at` receipts name venues, DOIs, and law numbers in prose rather than URLs. Every venue named is resolvable (this round re-resolved several, §3), and round-8 §7 declared this format (access level stated; DOI where one exists). No edit applied; noted because a future consistency pass may prefer URL-bearing receipts.

## 5. Full-corpus snapshot (courtesy; other shards' scope — not fixed here)

Criterion as in §1 head block, plus a whole-file standalone-line count, run at 20:49Z and re-run at 20:52Z (live parallel round):

- **20:52Z:** standalone `- verified-at:`/`- recheck:` lines: 178/179; within head block (before first `## `): 174/179.
- **MISSING standalone (1):** `civilizations/amazigh-berber.md` carries **two** pairs (lines 6–7 and 20–21) — a duplicate-field defect visible at snapshot time; its shard/auditor should keep the canonical pair and drop the other. (At 20:49Z it was not yet flagged in my sweep; it appeared during the parallel edits.)
- **Layout variants (4; standalone fields present, placed after the first `## ` heading):** `civilizations/mali-songhai.md` (first `## ` line 7; va line 15, rc line 16 — at HEAD the fields were inline inside one source bullet; split into standalone lines by its round-9 worker during this window), and `verification/{citation-format-and-source-registry,myth-consistency-gate,provenance-audit-ledger-format}.md` (va/rc after their first section heading in the committed tree).
- **20:49Z contrast:** the same sweep then showed 175/179 head-block-complete and reported the 4 files above as flag candidates; this is why the fragment distinguishes *field presence* (whole-file) from *head-block placement* (round-8 format).
- Concurrency evidence: `git status --short corpus/knowledge/` at 20:51Z listed 22 modified `civilizations/*` files in the working tree — the snapshot is mid-flight and may differ again by integration time.

## 6. Verification commands (re-runnable verbatim)

**A — partition completeness, couples, structure** (round-8 M10 §5 script, unchanged):

```
cd kotodama-shokunin && python3 - <<'PY'
import os,re
d='corpus/knowledge/culture-material'
pat=re.compile(r'\b((?:linguistics|myth-symbol|culture-material|synthesis|verification|civilizations)/[a-z0-9-]+(?:\.md)?)')
ok=True
for name in sorted(os.listdir(d)):
    t=open(os.path.join(d,name),encoding='utf-8').read()
    va=len(re.findall(r'^- verified-at:',t,re.M)); rc=len(re.findall(r'^- recheck:',t,re.M))
    m=re.search(r'^- couples:(.*?)(?=\n## )',t,re.M|re.S); body=m.group(1) if m else ''
    miss=[r for r in set(pat.findall(body)) if not os.path.exists('corpus/knowledge/'+(r if r.endswith('.md') else r+'.md'))]
    if va!=1 or rc!=1 or miss: ok=False; print('FAIL',name,va,rc,miss)
print('ALL_OK' if ok else 'FAIL', len(os.listdir(d)), 'files')
PY
```

Observed 2026-10-17 (before and after this shard's edits): `ALL_OK 16 files`.

**B — full-corpus field snapshot** (standalone vs head-block):

```
cd kotodama-shokunin && python3 - <<'PY'
import os
root='corpus/knowledge'; total=whole=head=0; bad=[]; layout=[]
for part in sorted(os.listdir(root)):
    d=os.path.join(root,part)
    if not os.path.isdir(d): continue
    for name in sorted(os.listdir(d)):
        if not name.endswith('.md'): continue
        total+=1; t=open(os.path.join(d,name),encoding='utf-8').read(); lines=t.splitlines()
        va=[i for i,l in enumerate(lines,1) if l.startswith('- verified-at:')]
        rc=[i for i,l in enumerate(lines,1) if l.startswith('- recheck:')]
        he=next((i for i,l in enumerate(lines,1) if l.startswith('## ')),len(lines)+1)
        if len(va)==1 and len(rc)==1: whole+=1
        else: bad.append(f"{part}/{name} va={va} rc={rc}")
        if len(va)==1 and len(rc)==1 and va[0]<he and rc[0]<he: head+=1
        elif len(va)==1 and len(rc)==1: layout.append(f"{part}/{name} first-## line {he}, va {va[0]}, rc {rc[0]}")
print(f"standalone {whole}/{total}; head-block {head}/{total}")
for b in bad: print("MISSING:",b)
for l in layout: print("LAYOUT:",l)
PY
```

Observed 2026-10-17 20:52Z: `standalone 178/179; head-block 174/179` + `MISSING: civilizations/amazigh-berber.md va=[6, 20] rc=[7, 21]` + the 4 layout lines of §5.

**C — to-verify inventory (partition):**

```
python3 tools/source-audit-inventory.py --json --summary --baseline round9-v10
```

(read-only; numbers of §4.1 filtered to `culture-material/`.)

## 7. Lane-tool regression after the edits

All 7 structural gates re-run in the edited tree, `--selftest`, exit codes observed 2026-10-17 20:52Z:

| gate | selftest result (final line) | exit |
|---|---|---|
| tools/gates/costume-era-consistency-gate.py | "self-test: 10/10 checks passed; fixture exit 1 with 21 planted finding IDs" (expected fixture path printed) | 0 |
| tools/gates/handoff-packet-check.py | "selftest: OK — fixture findings 11 across 9 ids" | 0 |
| tools/gates/lexicon-coverage-audit.py | "selftest: 14/14 checks passed" | 0 |
| tools/gates/myth-consistency-gate.py | "selftest: OK — fixture exit 1; planted IDs present …; clean control exit 0" | 0 |
| tools/gates/naming-collision-gate.py | "selftest: OK — fixture findings 12 across 11 ids" | 0 |
| tools/gates/phonology-sanity-gate.py | "fixture exit 1; 15/15 planted finding IDs present; 29 control cases passed" | 0 |
| tools/gates/provenance-audit.py | "SELFTEST OK: 7 fixture file(s), planted IDs missing-topic, missing-sources, …" | 0 |

`tools/check-gate-battery.py` and `tools/check-craft-exercise.py` are the O-shard's round-9 instruments and are not re-run here; this shard's edits touch only two `corpus/knowledge/culture-material/*.md` metadata lines, which no gate reads.

## 8. Handoff notes

- Write scope respected: only `corpus/knowledge/culture-material/material-culture-inference-method.md` and `.../era-periodization-models.md` were edited, plus this fragment. No other partition, tool, or bookkeeping file was touched; no git operations performed (rules: orchestrator integrates and commits once per round).
- Both edits are receipt upgrades, not content rewrites; each states its own access level and the remaining limit (pages past 165 not inspected; 1948 promulgation not re-dated; law.go.kr unreadable via plain fetch).
- Round-9 F/O/D shards are unaffected: the edits change no gate input, no packet pin, and no claim file. If the orchestrator wants LOG.md integration, this fragment + `git diff` of the two files are the complete record.
- For the auditor shard: §5's `amazigh-berber.md` duplicate pair (lines 6–7 and 20–21 at 20:52Z) is outside this shard's write scope and was observed mid-flight — re-check at integration time before acting.

FILES: reports/round-9/metadata/v10-culture.md | SUMMARY: culture-material re-audit green (16/16 complete, 0 drift, 0 dangling couples), 2 residual upgrades landed (Sauvet via OpenAlex; Korean era-law legs via ko.wikisource), 7 gates exit 0; full-corpus snapshot flags 1 duplicate pair in amazigh-berber.md + 4 layout-variant files for other shards.
