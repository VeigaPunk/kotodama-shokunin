# Round 89 sibling-overlap scan (ConnectorSiblings, read-only)

Scope: /home/vgpnk/Projects/shokunin/*-shokunin except kotodama, working trees as on disk 2026-11-04 (no pinned sibling revs; .git/.jj/.ufo excluded).
Frozen config read: kotodama-shokunin/reports/round-89/claims.json, measure89.py (freeze 1cbd0efc, base 42816d25). Nothing amended.

## Scan commands (all rc 0)

- (1) `grep -rilE --exclude-dir=.git --exclude-dir=.ufo --exclude-dir=node_modules 'evidential|mirativ|epistemic modal|epistemic marking|WALS.{0,20}(77|78)|wals.info/chapter/7[78]' <sibling>` per sibling: 39 files in chousa, game-dev-3d, kaidoku, kama, kasegi, kengaku, lore, mori, souji; every hit inspected with `grep -rinoE '.{0,70}(...).{0,70}'`.
- `grep -rilE 'wals\.info' */corpus/SOURCES.md` → only kotodama-shokunin/corpus/SOURCES.md.
- (2) `grep -inE 'evidential|epistem|linguist|conlang|language|kotodama|canon|research method|source|recheck|prompt'` over lore/chousa/kotoba PROVINCE.md.
- (3) `ls */tools/*recheck* */tools/*fresh*`, `grep -rlE 'recheck' */tools --include=*.py`, head docstrings of candidate tools.

## (1) Evidentiality / epistemic modality / mirativity / WALS 77-78 content

Verdict for every sibling: **none**. All 39 hits use "evidential" as an English adjective ("evidential strength", "evidential status", "evidential maximum") about the lane's own evidence, never about the linguistic category. Representative anchors:

| path:line | text sense | verdict |
|---|---|---|
| chousa-shokunin/corpus/SOURCES.md:100 (S090) | "Structured Evidential Support" — Wikipedia grounding paper | none (citation support, not grammar) |
| chousa-shokunin/corpus/knowledge/claim-support-test-r37.md:22 | "support relation ... is evidential strength under supposition" | none |
| chousa-shokunin/corpus/README.md:1075 | same, index row | none |
| kengaku-shokunin/corpus/knowledge/instrument-registry-derivation.md:55 | "stronger evidential claim" | none |
| kasegi-shokunin/corpus/instruments/kill-rule-check.py:86,633-635 | verdict label `evidential`/`opaque` | none |
| kama-shokunin/SCORECARD.md:1522, corpus/lessons/round-28.md:33,54 | "evidential pre-freeze fixtures" | none |
| mori-shokunin/LOG.md:3022, corpus/lessons/round-60.md:123 | "zero-evidential entry" | none |
| lore-shokunin/reports/r2,r34,r71,r81 (e.g. r71-clause-scout.md:1) | "evidential boundaries" of pointers | none |
| game-dev-3d-shokunin/reports/round-102/adversary/F2.md:73 | "evidential residue" | none |
| souji census/*, kaidoku lessons round-54 | same adjective sense | none |

No sibling SOURCES row cites WALS chapters 77/78 (or wals.info at all), Aikhenvald, de Haan, DeLancey or any mirativity source. C's ground is uncovered fleet-wide. Kotodama's own base already holds scattered sub-bullets (civilizations/inca.md:36-37 Quechuan evidentials, "do not make evidentiality a biological truth detector"; china-qing.md:145 kaozheng "evidential research" is a homonym, not the grammar topic) and S002 (WALS CLDF dataset, SOURCES.md:31).

## (2) PROVINCE.md claims touching evidentiality

| path:line | claim | verdict | kotodama must |
|---|---|---|---|
| lore-shokunin/PROVINCE.md:9 | refuses canon without in-world citation | adjacent | keep C non-canon: evidential systems are design options, never a world's recorded grammar |
| lore-shokunin/PROVINCE.md:19; corpus/README.md:70,77,91 (CM-d) | lore owns **in-world source reliability grading** (partial: free-text `reliability_note`, "grading must model witness reliability as attributed claims, not canon truth") | **adjacent — nearest boundary** | refuse: C must not grade in-world witness/document reliability or map evidential markers to truth/reliability tiers in a bible; it may say an evidential grammar *supplies* attributable source-type tags that lore's CM-d could consume, and hand that off |
| lore-shokunin/PROVINCE.md:23,28 (CM-g) | kotodama packet intake uncovered; kotodama owns names/calendars, lore owns what lands on entities | adjacent | any worked evidential paradigm goes out only via synthesis/worldbible-integration-contract.md, not into a bible |
| chousa-shokunin/PROVINCE.md:3-8 | owns source hierarchy, claim-vs-source verification | adjacent | C's sourcing uses kotodama's own gates; do not author general rules about how researchers weigh "reported vs witnessed" evidence — that reads as chousa method |
| kotoba-shokunin/PROVINCE.md:3,69 | prompt/skill craft; lists kotodama as adjacent (lane-name collision only) | none | no prompt-hedging/"epistemic markers in LLM prompts" content in C |
| kotodama-shokunin/PROVINCE.md:13-20 | own refusals already cover canon, general research method, prompt craft | consistent | — |

No sibling PROVINCE.md claims evidentiality, epistemic modality or mirativity as a linguistic topic → **no conflict**.

## (3) Source re-verification / recheck-cadence tooling vs claim F

| path:line | what it does | verdict | relation to F |
|---|---|---|---|
| chousa-shokunin/corpus/knowledge/recheck-due-r26.md:1-3,9-28 | due-date model: "A due date schedules assessment, not truth"; NNd from **verified-at**; on-release = event, "no inferred calendar deadline"; command-only/invalid = unknown, "never silently current" | adjacent (method) | F's bounds already match the core point (re-verification ≠ re-certification). Kotodama's own auditor (tools/check-sources-recheck.py:4-10, round 82) computes NNd from **opened** and calls on-release "exempt; never due" — a divergent, lane-local rule on its own registry, not a conflict; cite chousa for the principle, don't re-derive it |
| chousa-shokunin/tools/research-gate.sh:35-36,675,685,3485-3572 | `verify-metadata --as-of` emits due=/freshness=, META_RECHECK_OVERDUE (entry-header level) | adjacent | entry-level (knowledge headers), F is registry-row level; no reuse needed this round |
| chousa-shokunin/corpus/knowledge/japanese-prisma-item-wording-r40.md:25; evidence-snapshot-coverage-r40.md:28 | an archived copy does not establish current revision; web.archive.org values unchecked for state | **adjacent — should reuse** | see flaw F-1 below |
| mori-shokunin/tools/mori-source-drift.py:1-10; mori-drift-recheck.py:1-10 | re-fetch every SOURCES row with a committed copy, classify copy vs today's body; separates vendor build churn from content drift | adjacent (closest analogue) | F re-locates a quote, it does not classify drift; mori's churn/content split is the ready precedent if F ever needs "still locatable but changed" disposition — reuse the concept, don't absorb the tool |
| kama-shokunin/tools/release-recheck.py:1-10 (+round44/45/46 audits) | re-verification ledger for `on-release` rows pinned to a GitHub commit (cited line ranges at pinned vs release) | adjacent | F excludes the 16 on-release rows; kama's method is the reusable route if kotodama later re-verifies them |
| kaidoku-shokunin/tools/round-78/surface-recheck.py; tameshi selfstate-freshness.py; tsukuroi check-freshness-r17.py, check-recheck-commands.py | re-derive recorded live values / figures / recheck command safety in their own records | none | different objects (host values, own figures) |
| chousa-shokunin/tools/assimilate-rows.py:51,63,502-507 | validates cited rows' recheck tokens (ISO, NNd, cadence) when assimilating | none | no duplicate of F |

No sibling owns kotodama's registry rows; F duplicates no sibling tool. Verdict: **no conflict**, two reuse points (chousa archive caveat, mori drift split).

## Cross-claim patterns F × C (from measure89.py, read-only)

1. **OTHERCELLS × APPENDONLY cell-set mismatch (kill hazard).** C allows base rows to change status/recheck/used-by (claims.json C predicate tail); F forbids any non-recheck change on the 16 population rows and any recheck change on non-population rows (measure89.py:189-197). So if C's new entry updates `used-by` of a population row (e.g. S009 CALS, the only conlang-feature census in the queue) or the recheck of any non-population row (e.g. S002 WALS CLDF), C passes and **F fails OTHERCELLS**. C may only touch `used-by`/`status` of non-population rows.
2. **Shared lesson file, loose disposition match.** Both legs read corpus/lessons/round-89.md. DISPOSED (measure89.py:185-186) accepts any line containing the id and the token LOCATED; BACKED takes `first_quote` of the first matching line (line 171-176). A C gate line that mentions a population id plus "LOCATED" (e.g. "cf. S009 ... LOCATED") could dispose that F row or feed it the wrong quote. Keep one id per line; C gate lines should name only S936-S941.
3. **Manifests are keyed by row id** (capture_check:129) and split across files (rechecks/manifest.json vs evidence/manifest.json) — no collision, but a C capture can never back an F row or vice versa; each WALS/CALS page needs its own capture per claim.
4. **New-id distinctness.** Base already has S002 (WALS CLDF repo). WALS chapter 77 / 78 pages as S936+ are distinct surfaces (chapter text vs dataset README) and are admissible new ids; citing S002 in C does not count toward NEWIDS.
5. **Tier floor.** C requires new ids at tier A/B; S009 CALS is tier C, so it cannot be a C anchor even though it is the queue row closest to C's subject.

## Flaws found (reported, not amended)

- **F-1 (freshness weakness in url_ok).** measure89.py:98-102 accepts `https://web.archive.org/web/<any timestamp>/<row url>`; capture_check (lines 140-141) checks only that `fetched_at` starts with 2026-11-04. A 2015 memento fetched today passes BACKED and the row's recheck advances on a years-old snapshot. The Contract says to use `/web/2026/`, but the counter does not enforce the memento year. Chousa already records that an archived copy does not establish the current revision (japanese-prisma-item-wording-r40.md:25). Proposed move for L1, not applied: disclose it in the F report and have the closure re-open check the memento timestamp of every archive-backed row (it should be ≥ 2026). Do not change the frozen counter.
- **F-2 (cadence semantics divergence).** kotodama check-sources-recheck.py:6-8 (NNd from opened, on-release exempt) vs chousa recheck-due-r26.md table (NNd from verified-at, on-release = event/unknown). It does not affect round 89's population, which was derived with kotodama's tool. Record it as adjacent method drift. It is not a defect in the claim.
