# CriticClauseCO — QUALITY 11, claims C and O

## Scope and axes

Read-only instrument review; no admission, integration, canonical judgment, counter execution, fixture execution, or source fetching. Clause verdicts below assess instrument coverage, not whether a candidate passes. `MATCH` does not certify the required green/red controls.

- **Coverage (C):** the new footwear knowledge entry, its README index, and its owned SOURCES rows S652–S699.
- **Operability (O):** the new reusable `tools/check-cited-lines.py` CLI, not a new source-quality or blind-support score.

Read `claims.json` first; then QUALITY 7–14, both complete counters, the locator, source-access checker, README sweep, declaration receipt/manifest, and relevant round-60 evidence. Observed counter hashes match the assignment:

- C: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`
- O: `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`

Evidence references below are lane-relative paths and observed line numbers. All prospective PASS counterexamples are explicitly source-level inferences, **not control receipts**.

## 1. C statement: clause-by-clause verdict

Statement: `reports/round-61/claims.json:14`. Counter: `reports/round-61/accept-c.py` (C below).

| Clause | Mechanical leg / evidence | Clause verdict |
|---|---|---|
| Exact footwear entry exists | SET, C:119–123; ENTRY at 52 | MATCH: the added-path set must be exactly ENTRY. |
| It is the only added knowledge file | SET, C:119–123, using the 235-path base list | MATCH for file identities; additions and removals are checked separately, not count alone. Existing-file byte preservation is not stated or checked. |
| There are 236 knowledge files | SET, C:54,109–123 | MATCH; all walked files count, not only Markdown. |
| Entry is indexed in `corpus/README.md` | SWEEP, C:124–133 | MATCH: sweep exit is read; rows/files must be 236 and missing count zero. The sweep also compares index text to the entry's topic field; that is index consistency, not proof of subject matter. |
| At least 20 distinct cited rows | FLOOR plus RANGE, C:139,150–154 | MATCH for distinct cited identifiers with one valid registry row each. This is not a requirement for 20 distinct publications or new URLs within the new block. |
| Rows are new | RANGE reserves S652–S699; FRESH compares URLs with lower IDs | PARTIAL: new-ID ownership is the declared basis. The counter does not compare registry history with the frozen base or protect old rows from alteration. See finding C-FRESH. |
| Every cited ID is in S652–S699 | RANGE, C:151–153 | MATCH; also rejects duplicate cited-ID rows, malformed row widths, and recognized range notation. |
| Every row is opened 2026-10-23 | OPENED, C:157–158 | MATCH for the recorded opened cell. Actual ordinary opening/provenance is not established by a date string; ACCESS and live LOCATE are narrower additional checks. Treat historical opening truth as review evidence, not something OPENED proves. |
| Every row is mined | STATUS, C:155–156 | MATCH for the exact status cell. |
| Every row is used-by the entry | USEDBY, C:159–160 | MATCH: exact whole comma/semicolon-separated item, not substring. |
| Every cited line is a bullet | LINES, C:141,166–171 | MATCH to the counter's textual definition: optional whitespace followed by `- `. It is not a Markdown parser. |
| Every cited line carries exactly one S-id | LINES, C:168–170 | WEAKER STAND-IN: exactly one **distinct** ID, not exactly one occurrence. Repeating `(S652)` on the same line is accepted. Resolve the statement/docstring difference before data. |
| Every cited line shares at least three content words with its row's anchor | LINK, C:182–186 | MATCH to the declared operational definition: distinct normalized words of length at least four outside STOP. Not a test of entailment, scope, qualification, or relevant use of those words. |
| Every cited line copies at most 12 consecutive quote words | COPY, C:87–97,187–191 | MATCH to normalized longest-common-contiguous-word-run length. An entire 8–12-word quote can still be pasted; the numerical clause does not forbid that. |
| Every anchor quote carries a footwear-lexicon word | TOPIC, C:64–70,172–174 | MATCH as a lexical membership test only. It is a WEAKER STAND-IN if used to prove that the entry/quote is actually about footwear. See local `sole` counterexample below. |
| Every anchor quote is located live on a URL in its own source cell | LOCATE, C:172,193–204; locator:170–206 | MATCH to the locator's normalized occurrence rule and first quoted anchor span, with all cited IDs required. It is not proof that the line's added proposition is supported. Redirect provenance and ignored PDF child exit are defects below. |
| No cited row reuses a registry URL below S652 | FRESH, C:206–214 | MATCH against the parsed **current** registry under the frozen normalization. WEAK for the historical/base-registry interpretation: old rows are not pinned and duplicate lower-ID rows overwrite earlier ones in C's table. |

### C review-only and entry-rule boundaries

`claims.json:21` and C:38–40 correctly make wording support beyond shared words, craft usability, one-way links to partial owners, and lore handoff review-only. Those are not mechanically certified by LINK, TOPIC, or LOCATE.

The surface at `claims.json:12` additionally names **footwear as subject** and terms/status codes/rites/making. Those semantic coverage obligations need an explicit review-only clause and actual review; a lexicon hit does not discharge them. The same applies to **one clause per bullet**, as opposed to one distinct citation ID: LINES never counts clauses.

Binding entry rules not completely represented in the frozen statement/counter:

- Quote minimum eight normalized words: checked by locator:172–173.
- Quote maximum 25 words: **no check** in C or the locator.
- Verbatim page-body text: the locator deliberately normalizes punctuation, case, and hyphenation; HTML extraction includes text outside script/style, not specifically article body, and JSON extraction joins all string values (locator:56–71,96–141). Its PASS means normalized occurrence, not exact raw wording or body/provenance certification.
- No S-id in a heading/table: ordinary unprefixed headings/table rows fail LINES because they do not start `- `. The implementation does not inspect Markdown context; for example a bullet containing an ATX heading still meets its prefix test.
- A restatement, not a quote dump: COPY's numeric ceiling alone does not prove this, especially for an 8–12-word quote.

Smallest safe correction: retain exact lexical/count claims as such, explicitly list semantic subject, single-clause support, paraphrase, and quotation provenance as review-only, and enforce the missing objective 25-word bound before data if it remains a binding entry rule. Do not relabel lexical agreement as source support.

## 2. O statement and incorporated contract: clause-by-clause verdict

Statement: `claims.json:30`; incorporated contract: `reports/round-61/accept-o.py:7–16` (O below).

| Clause | Mechanical leg / evidence | Clause verdict |
|---|---|---|
| Tool exists at exact path | TOOL, O:149–156 | MATCH (`isfile`). |
| It passes its **own selftest of at least 10 cases** | TOOL, O:151–156 | WEAKER STAND-IN: exit zero and last line `selftest N/N`, N≥10. No cases, assertions, or exercised behavior are inspected. A fake footer is sufficient for this leg. |
| It does not load the counter | INDEP, O:157–159 | WEAKER STAND-IN: two source substring exclusions, not a dependency check. Obfuscated/composed imports can pass; an honest documentation reference can fail. |
| It is exercised on run-time random fixtures | GEN, O:147,160–169 | MATCH: fresh OS-entropy-seeded fixture tree and independent reference output. Seed/tree are not retained. Randomness is not itself completeness. |
| Directory arguments recurse over `.md` files only | GEN, O:127–140,162–169 | MATCH on generated nested Markdown plus one non-Markdown distractor. |
| Explicit file PATHs are read, including non-`.md` files | CLEAN/ERR use explicit Markdown files | PARTIAL: valid explicit Markdown is covered; valid explicit non-Markdown files are not. |
| PATH... supports multiple arguments | No invocation supplies multiple input paths | GAP: a tool ignoring every argument after the first can pass all listed invocations. |
| IDs match `\bS\d{3,}\b`, with distinct IDs sorted numerically | Reference O:47,63–68; GEN kinds O:101–123 | MATCH on generated examples, including repeated IDs, lookalikes, separators, and table IDs. Not exhaustive boundary coverage. |
| Two or more distinct IDs give MULTI-ID | GEN and REAL vs reference | MATCH for the tested finding set. |
| A leading-whitespace-stripped `|` line with an ID gives TABLE-ID; one line may give both findings | GEN includes table1/tablen; reference O:65–68 | MATCH for tested finding membership, including both kinds. |
| Findings print exactly in per-file line order | `parse`, O:80–90, builds a set | WEAKER STAND-IN: order and duplicate findings are discarded. Reversed or duplicated output can pass GEN and REAL. |
| Last summary has exact finding/file counts on random fixtures | GEN, O:166–167 | MATCH for the parsed summary, but duplicates before it are not counted. |
| Clean file gives no findings, exact summary, exit 0 | CLEAN, O:170–178 | MATCH for the generated clean Markdown file. |
| Missing path and invalid UTF-8 each give exit 2 and the diagnostic | ERR, O:179–185 | MATCH for these two inputs and return codes; marker is checked as a substring of stderr, not a full diagnostic-line grammar. |
| No PATH and an unreadable file also give exit 2 with CITED_LINES_ERROR | Contract O:14–16; no corresponding run | GAP: neither condition is exercised. |
| Base corpus gives exactly the contract's findings | REAL, O:186–200 | MATCH only as a finding set. Base R60 S612/S613 finding is specifically required; output ordering/duplicates are not checked. |
| Base corpus gives the contract's summary | REAL parses `summary` at O:195, then never checks it at 198–200 | GAP: arbitrary/wrong final summary can pass REAL. Its final line is even excluded from `bad` whether or not it matches SUMMARY. |
| Exits are exactly contract exits | GEN=1, CLEAN=0, ERR=2, REAL=1 explicitly checked | MATCH for exercised branches. Untested no-PATH/unreadable/multiple-PATH behavior remains unverified. |

## 3. Strong counterexamples and smallest safe corrections

These are **[INFERENCE: source-level witnesses, not executed receipts]**. Each preserves the stronger neighboring behavior rather than merely removing the claimed object.

### O-SELFTEST — false selftest provenance

**Counterexample:** otherwise correct lint behavior, but `--selftest` executes zero cases and prints `selftest 10/10`, exit 0. TOOL's only conditions all hold (O:151–156); GEN/CLEAN/ERR/REAL are unaffected. Thus O can mechanically PASS while its stated selftest clause is false.

**Axis:** operability. **Correction:** inspect the actual cases/assertions and show a targeted scanner mutation makes the tool's own selftest fail; independently exercise the promised case coverage. A printed count alone must not be recorded as ten tested cases.

### O-INDEP — substring authority is not independence

**Counterexample:** build the counter filename/path from string pieces and load it; neither forbidden contiguous substring need appear in the tool's source. Conversely, adding an explanatory comment naming `accept-o` makes INDEP fail without loading anything.

**Evidence:** O:157–159 reads only raw source text. **Axis:** operability, truthful provenance.

**Correction:** review executable dependencies and exercise the tool without the acceptance instrument available in its runtime tree. Keep documentation references separate from executable dependency evidence; do not claim the substring ban proves non-loading.

### O-EXACT — duplicate/order/REAL-summary holes

**Counterexample:** print every correct finding twice, retain the expected unique-count summary and contract exit. `parse` collapses duplicates, so GEN and REAL still see exactly `want`. Reversing findings within each file is likewise invisible. Separately, print correct REAL findings followed by `CITED-LINES: 0 finding(s) in 0 file(s)` only for the `corpus/knowledge` argument; REAL never validates that summary, while other invocations remain correct.

**Evidence:** O:80–90,166–167,193–200. **Axis:** operability.

**Correction:** compare ordered per-file finding sequences with multiplicity; require exactly one syntactically valid final summary in every successful scan and validate REAL's counts. Add deterministic invocations for multiple PATHs, valid direct non-Markdown input, no PATH, and unreadable input.

### C-ONE-ID — occurrence versus identity

**Counterexample:** from an otherwise passing C candidate, append another `(S652)` to a line already citing S652. FLOOR and RANGE use sets; LINES also uses a set; LINK/COPY strip all ID tokens. No neighboring leg needs to change, but the line carries two S-id occurrences.

**Evidence:** C:139,168–170,177,183. **Axis:** coverage/conformance.

**Correction:** if the frozen sentence really means one occurrence, count occurrences, not distinct values, and add a repeated-identical-ID near-miss. If it means one distinct row, state that explicitly before data and do not present it as a single-citation check.

### C-TOPIC — local proof that lexicon presence is not footwear coverage

The existing registry contains this 24-word quote in S265 (`corpus/SOURCES.md:294`):

> No institution has the authority over medicine masks, as they are the sole responsibility of the medicine societies and the Grand Council of Chiefs.

`sole` is in TOPIC_WORDS (C:66). Used as a row's first anchor quote, this is therefore TOPIC-positive although it concerns medicine-mask authority, not footwear. For example, a source-scoped paraphrase about medicine societies, responsibility and the Grand Council shares ample LINK words without changing the subject to footwear.

This is a **local TOPIC counterexample**, not a whole-C green fixture: reusing S265's old URL would separately fail FRESH. It establishes that TOPIC cannot prove the semantic subject even when the quotation is real.

**Axis:** coverage. **Correction:** explicitly review actual footwear subject and the promised terms/status/rites/making coverage. Keep TOPIC described only as lexicon membership; expanding a blacklist cannot turn it into entailment.

### C-FRESH — current registry is a mutable historical authority

**Counterexample:** copying a lower-ID row's source into a new ID while removing that URL from the old row defeats the historical-reuse check, because FRESH rebuilds `old` from the current C-owned SOURCES file. Also, C:145 overwrites table entries for duplicate old IDs; RANGE only demands uniqueness for cited new IDs, so an additional old-ID row can hide an earlier URL from C's FRESH table. The source-access parser does not enforce registry-ID uniqueness (`tools/check-source-access.py:47–58`).

**Evidence:** C:142–146,151–154,211–214. **Axis:** coverage/source freshness as a constraint, not an independently claimed freshness-axis gain.

**Correction:** compare against URLs from the frozen base registry and reject duplicate registry IDs. Preserve historical source rows rather than allowing a new landing to redefine which URLs were already present. Do not silently upgrade the claim into “20 distinct works”: that is not the declared counting unit.

### C-LOCATE — normalized occurrence and redirect provenance

**Counterexample:** an otherwise eligible quote longer than 25 words is not rejected by length anywhere; the locator only checks MIN_WORDS. An allowed original URL can also redirect to a refused host: `urlopen` follows redirects, but `url_refusal` is applied only to the original URL and `fetch` returns no final-response URL.

**Evidence:** locator:78–93,144,152–186. **Axes:** coverage, source provenance.

**Correction:** enforce the objective upper bound, retain/check final URL provenance, and review page-body/exact quotation separately from normalized occurrence. No network bypass was attempted here.

## 4. QUALITY 11: child statuses and control evidence

Two transitive status-reading defects are visible without running code:

1. **C / LOCATE / PDF:** locator:113–116 runs the PDF extractor, then returns `done.stdout` without reading `done.returncode`. A child that outputs a matching passage before failing can still feed a LOCATED result. Check the child exit before accepting extracted text. No PDF extraction or `uv` invocation was performed in this review.
2. **O / REAL:** O:188–190 executes `git archive ... | tar ...` with `shell=True` and no pipefail. `arch.returncode` is the shell pipeline's final command status, not a checked status for both tools. Separate the stages or explicitly collect both statuses. This violates QUALITY 11's no-hidden-child-status requirement even though many ordinary archive failures also make tar fail.

C's direct SWEEP and ACCESS subprocess exits are checked; O's tool subprocess exits are checked for all exercised branches. Those do not cure the two transitive gaps.

The committed `reports/round-61/telemetry/declaration-dry-run.txt` is an absent-land/base receipt: C FAIL/exit 1, O FAIL/exit 1, separability exit 2 at C's absent entry. It explicitly says later separability units are unevaluated. It is **not** a green control or one-near-miss-per-clause red control under QUALITY 11. `claims.json:41–44` lists broad control classes, not complete isolated clause controls (for example C's index, used-by, fixed-count file identity; O's exact summary/order and all error branches). The currently listed round-61 report directory contained no per-clause control builder/receipt beyond that declaration receipt at inspection time. Other seats' future receipts were not evaluated here.

Accordingly: mechanically mapped clauses remain **control-unverified by this review**, not “shown able to fail.” No CONTROL-MET/NONE-MET claim is made, because this assignment requested no runs and no fixture was scored.

## 5. Separability, labels, and identity

### Cross-claim read paths

No observed counter leg requires the other claim's landing:

- C SET/SWEEP/ACCESS traverse current knowledge/README/SOURCES, all C-owned or base paths; C never invokes `tools/check-cited-lines.py`.
- O TOOL/INDEP read its own tool; GEN/CLEAN/ERR read temporary fixtures; REAL reads `corpus/knowledge` **archived from 942abdf4**, not the live C footwear tree or C's registry rows. The temporary fixture IDs are strings, not registry lookups.
- `claims.json:23,38` and the separability manifest assign disjoint C/O lands. The actual new tool must still be reviewed for undeclared runtime imports and C-export references when it exists.

There are several explicitly named revisions: claims' round base and O's corpus BASE are `942abdf4`; manifest base/declaration instrument revision is `106df397`; assigned frozen review revision is `78ad4b17`. These are not automatically the same identity or a demonstrated regression. Receipts should retain their purposes rather than calling all three “base.” No historical tree comparison was performed here.

### Printed labels and exit statuses

On normal completion, both counters are internally consistent: each leg prints its Boolean, `verdict = all(...)`, final `ACCEPT-C-61`/`ACCEPT-O-61` label uses that verdict, and return is 0 for PASS or 1 for FAIL (C:215–219; O:201–205). No PASS/exit-1 or FAIL/exit-0 inversion was found.

Their documented input-error branches can exit 2 **before printing a final acceptance label**; O can do so after accumulating but not printing earlier leg results if archive setup fails. Preserve such a receipt as an input error, not a fabricated FAIL/PASS label.

The significant sentence/code mismatch is **semantic**, not the final Boolean wiring: O can say PASS without real selftests, independence, exact output order/multiplicity, or a correct REAL summary. C's “one S-id” versus “one distinct S-id” also differs, and lexical overlap must not be substituted for review-only support.

## 6. Anti-loop and whether the axes actually move

### C compared with rounds 58–60

The proposed entry changes area and does not re-enter the amulets entry; LINES blocks ordinary multi-distinct-ID lines and unprefixed table rows, and LOCATE reopens every cited anchor rather than relying on blind votes. These are real structural differences from the rejected packet shape.

They do **not** prove all R60-M6 failure modes are eliminated. `corpus/lessons/round-60-verifier-spotcheck.md:117–122,145` says the S612 packet joined **three lines (69,95,120)**, not merely a single multi-ID line. Multiple different clauses on one same-ID bullet, multiple bullets for one ID, or cited lead-ins can still be joined by an old packet builder; LINES has no clause parser. The same spot-check and `corpus/lessons/round-60.md:55–56` also document blind support missing overreach and registry teaches-cell problems. LINK/LOCATE do not repair those semantics.

**Smallest safe correction:** maintain actual one-clause/source-scoped bullets and review them against the quote; if packets return, build them from the scoped clause and pin judged bytes/IDs under QUALITY 14. Do not claim the new lint alone fixes multi-line packet assembly or unsupported teaches cells. This round does not declare blind packets, so QUALITY 14 is conditional, not an unperformed predicate leg.

O only tests its own tool. C deliberately does not invoke O (which also keeps the claims separable). Thus an O PASS is not evidence C was built with that tool, and the declaration correctly leaves next-packet use review-only. Avoiding blind support is an explicit measurement tradeoff, not by itself an instrument defect; it cannot be credited as improved discernment or proof of admission support.

### O versus an already-held rule

The requested recursive `MULTI` search was performed with the grep tool, not shell grep. At inspection it found only:

- `tools/check-gate-battery.py` — `re.MULTILINE`;
- `tools/d2-typed-labels.py` — `P-MULTI-DOC`;
- four historical/frozen copies of `d2-typed-labels.py` under `tools/gates/` — the same parser code.

No `MULTI-ID` or `TABLE-ID` lint existed in that result or the narrower rule search. Existing `tools/check-draft-ids.py:11–37` instead checks NEW tokens and dangling citation fragments; its selftest explicitly permits ID ranges (`:231–232`). `source-audit-inventory.py` is an uncertainty-marker inventory, not this cited-line rule.

The **prose rule/routed repair already exists** in R60-M6 (`corpus/lessons/round-60.md:56`), but a reusable CLI for arbitrary inputs is a distinct operability surface. Testing known base findings is a regression check, not alone new operability; GEN/CLEAN/ERR and a real selftest must establish the capability. This is not evidence that the lane already held an equivalent executable lint, nor permission to count the old rule twice as new knowledge coverage.

### Randomness: what is and is not established

GEN's set comparison avoids dependence on directory traversal order. Generated words contain lowercase letters only; IDs and separators match the stated regex; the clean lookalikes do not contain valid standalone IDs. **No source-level counterexample was found in which fixture randomness alone rejects a fully contract-conforming tool.** Do not report such an honest-tool failure without evidence.

What is established is non-reproducible fixture selection and incomplete mandatory separator coverage: separator choices are random (O:113–116), so a separator-specific mutant can survive a run that omits its failing separator. Keep run-time random variation, but retain the seed/tree in the receipt and include each required separator/boundary deterministically. This is a reliability correction, not grounds to weaken the frozen first-run kill rule after data.

## 7. Smallest safe disposition of the findings

Fixable before-data instrument defects: O fake-selftest acceptance, INDEP's proxy, output order/multiplicity and REAL summary omissions, missing CLI branches, hidden child statuses; C ID-occurrence ambiguity, missing quote upper bound, and historical-registry authority. Apply any instrument revision only under the declaration's pre-first-claimed-object-run rule and keep the forcing control receipt/hash.

Deliberate limits requiring honest scope rather than a proxy “fix”: lexical membership is not footwear subject; shared words/live quote location are not sentence entailment; 20 rows are not necessarily 20 works; a new lint is not new knowledge or a repaired packet pipeline; omission of blind support does not certify source support. These are matters for explicit review and the canonical assignment's judgment, not a critic's admission decision.

No tools installed or updated. No counter/test/runtime runs, background jobs, clones, or fixtures. Scratch directory created: `/fast/scratch/hyaku/kotodama-r61/CriticClauseCO/` (empty). The only lane write is this report, written once.
