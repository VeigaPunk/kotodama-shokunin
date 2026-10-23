VERDICT: ALL-FAIL

GREEN: PASS

## Measured revision and detector

Final matrix: `1a07344e77ea34c3e6b3c38a838c7c35654522be`, following the parent’s revision notices. The frozen instruments were never edited. Every run used `timeout 1200 python3 -B reports/round-58/accept-c.py` from the sandbox root. No lane corpus, lane index, jj state or sibling files were written.

[Honest green stdout](MutLegIsolation58/green-final/stdout.txt): exit **0**, all **14** legs PASS, final line `ACCEPT-C-58: PASS`. [Exact green fixture](MutLegIsolation58/green-final/fixture.patch), [untracked entry](MutLegIsolation58/green-final/untracked/corpus/knowledge/linguistics/toponymy-place-names.md), and [row/quote specification](MutLegIsolation58/final-fixture-data.json). This fixture is control evidence only; it never enters the lane corpus or claim data.

## Per-leg mutations

Each variant starts from the honest green bytes and changes one defect. Expected failing-leg sets were recorded before scoring in [mutation-plan.json](MutLegIsolation58/mutation-plan.json). All actual sets matched. Each mutated run printed `ACCEPT-C-58: FAIL` and exited **1**; after each mutation the exact green bytes were restored and the same frozen detector printed PASS, exit **0**.

| Mutation | Fixture patch and full output | Failing legs | Exit |
|---|---|---|---|
| SET-extra-file-final | [fixture](MutLegIsolation58/SET-extra-file-final/fixture.patch), [stdout](MutLegIsolation58/SET-extra-file-final/stdout.txt) | SET | 1 |
| SWEEP-drop-index | [fixture](MutLegIsolation58/SWEEP-drop-index/fixture.patch), [stdout](MutLegIsolation58/SWEEP-drop-index/stdout.txt) | SWEEP | 1 |
| FLOOR-19-ids | [fixture](MutLegIsolation58/FLOOR-19-ids/fixture.patch), [stdout](MutLegIsolation58/FLOOR-19-ids/stdout.txt) | FLOOR | 1 |
| RANGE-S499 | [fixture](MutLegIsolation58/RANGE-S499/fixture.patch), [stdout](MutLegIsolation58/RANGE-S499/stdout.txt) | RANGE, FRESH | 1 |
| RANGE-S560 | [fixture](MutLegIsolation58/RANGE-S560/fixture.patch), [stdout](MutLegIsolation58/RANGE-S560/stdout.txt) | RANGE | 1 |
| RANGE-duplicate | [fixture](MutLegIsolation58/RANGE-duplicate/fixture.patch), [stdout](MutLegIsolation58/RANGE-duplicate/stdout.txt) | RANGE | 1 |
| RANGE-notation-final | [fixture](MutLegIsolation58/RANGE-notation-final/fixture.patch), [stdout](MutLegIsolation58/RANGE-notation-final/stdout.txt) | RANGE | 1 |
| STATUS-queued | [fixture](MutLegIsolation58/STATUS-queued/fixture.patch), [stdout](MutLegIsolation58/STATUS-queued/stdout.txt) | STATUS | 1 |
| TIER-C | [fixture](MutLegIsolation58/TIER-C/fixture.patch), [stdout](MutLegIsolation58/TIER-C/stdout.txt) | TIER | 1 |
| USEDBY-missing | [fixture](MutLegIsolation58/USEDBY-missing/fixture.patch), [stdout](MutLegIsolation58/USEDBY-missing/stdout.txt) | USEDBY | 1 |
| ACCESS-headless | [fixture](MutLegIsolation58/ACCESS-headless/fixture.patch), [stdout](MutLegIsolation58/ACCESS-headless/stdout.txt) | ACCESS | 1 |
| LOCATE-invented | [fixture](MutLegIsolation58/LOCATE-invented/fixture.patch), [stdout](MutLegIsolation58/LOCATE-invented/stdout.txt) | LOCATE, BOILER, TOPIC | 1 |
| BOILER-footer | [fixture](MutLegIsolation58/BOILER-footer/fixture.patch), [stdout](MutLegIsolation58/BOILER-footer/stdout.txt) | BOILER, RELEVANCE, TOPIC | 1 |
| RELEVANCE-no-stems | [fixture](MutLegIsolation58/RELEVANCE-no-stems/fixture.patch), [stdout](MutLegIsolation58/RELEVANCE-no-stems/stdout.txt) | RELEVANCE | 1 |
| TOPIC-offtopic | [fixture](MutLegIsolation58/TOPIC-offtopic/fixture.patch), [stdout](MutLegIsolation58/TOPIC-offtopic/stdout.txt) | RELEVANCE, TOPIC | 1 |
| FRESH-old-url | [fixture](MutLegIsolation58/FRESH-old-url/fixture.patch), [stdout](MutLegIsolation58/FRESH-old-url/stdout.txt) | FRESH | 1 |
| DISTINCT-shared-url | [fixture](MutLegIsolation58/DISTINCT-shared-url/fixture.patch), [stdout](MutLegIsolation58/DISTINCT-shared-url/stdout.txt) | DISTINCT | 1 |

**Final matrix verdict: 17 killed, 0 survived, 0 inconclusive.** SET adds a non-Markdown second file so it isolates SET without changing the README sweep’s Markdown inventory. FLOOR removes S500’s citations while retaining other rows on that host. ACCESS records a fictitious prohibited-method marker only; no browser or bypass was actually used. FRESH adds S001’s already-registered URL to one source cell while retaining its first, valid source. DISTINCT adds another cited row’s URL without changing the first URL, quote or host floor.

### Coupled failures; not hidden as independent isolation

- **RANGE/S499 also fails FRESH:** the renamed row is below S500 and therefore puts its own URL into the legacy set. S560, duplicate-row and range-notation variants fail RANGE alone.
- **Invented quote:** LOCATE fails, and BOILER/TOPIC also fail because both require a located URL. Its original relevant stems remain, so RELEVANCE still passes.
- **Footer quote:** the real sentence is on both the source page and root; BOILER fails. Replacing the quote also breaks its semantic binding and naming window, so RELEVANCE/TOPIC fail.
- **Off-topic quote:** real source-page prose, “On this page you can find an attempt to summarise the main aspects involved.”, is not on the root. LOCATE and BOILER pass; RELEVANCE and TOPIC fail.

These dependency sets are the observed limits of single-field isolation, not amended predicates or suppressed failures.

## What honest green required

The final fixture has one short worldbuilding entry, its matching README topic row, the linguistics section count **29**, total/footer **234**, and **20** honest S500–S519 rows: **20 distinct URLs, 20 distinct quotes, 10 hosts, 12 tier-A and 8 tier-B rows**. All quotes were opened by ordinary urllib GET and state their scoped teaching; teaches cells and entry lines are paraphrases. [Source GET receipts](MutLegIsolation58/source-get-evidence.json) record HTTP status, content hashes, quotes and root checks.

Sources span SNSBI, the Scottish Place-Name Society, USGS, GOV.UK/PCGN, UNGEGN, Edward Relph’s Placeness site, Names journal, Nottingham’s EPNS pages, Ordnance Survey and OX Magazine. Catalogue/journal pointers are explicitly scoped to the existence or remit of the resource, not unread arguments. Institutional tier A is scoped to its own statements. The entry includes linguistic inheritance, layered river/city names, evidence uncertainty, naming authority, survey coverage and a non-canon lore handoff.

Practical instrument constraints encountered, preserved rather than patched around in the instrument:

- The original d4a5ea31 fixture with three Wikipedia pages plus USGS passed the original twelve-leg counter ([stdout](MutLegIsolation58/green/stdout.txt)). Parent revisions then required distinct URLs/ten hosts, A/B tiers, sentence-shaped teaches and stricter topic/boiler checks, so a new honest fixture was built.
- At c42121f4, that original fixture failed TOPIC and DISTINCT ([receipt](MutLegIsolation58/revised-initial/result.json)); that is a baseline failure, not a killed mutant.
- The revised BOILER rule rejects genuine lead sentences repeated in meta descriptions. The final fixture uses qualifying body passages, and the actual full-text PDF for the Names article, rather than pretending its abstract metadata passes.
- The locator rejects legitimate quotes containing three words also present in the URL path, e.g. “on geographic names”; initial final-revision build attempts consequently failed LOCATE/BOILER/TOPIC ([receipt](MutLegIsolation58/final-green/result.json)). A later attempt exposed a six-word copied run in S508’s teaches ([receipt](MutLegIsolation58/final-green-corrected/result.json)). Both were corrected in the fixture, before the successful baseline and mutation matrix.
- One EOF insertion preflight failed before applying any mutation. Its restoration run passed; [interruption receipt](MutLegIsolation58/harness-interruption.json) records the error. The corrected, measured variant is RANGE-notation-final.

The early original-counter SET probe also failed SET alone ([stdout](MutLegIsolation58/SET-extra-file/stdout.txt), exit 1). Its exact original fixture and instrument bytes were reconstituted in a separate owned sandbox at d4a5ea31 and the original detector passed ([restored stdout](MutLegIsolation58/original-restored/stdout.txt), [hash receipt](MutLegIsolation58/original-restored/result.json)); it is separate from the final 17-variant matrix.

## Restoration evidence

[mutation-results.json](MutLegIsolation58/mutation-results.json) contains each final-matrix mutant’s full before hashes, actual failing legs, exit/verdict, and restored hashes. Every final-matrix run directory also retains full stdout/stderr, exit data, `fixture.patch`, the untracked entry, and copies of the three fixture files. Each final-matrix `<mutation>-restored/result.json` records the restoration detector run. [Consolidated restoration evidence](MutLegIsolation58/restoration-evidence.json): **17/17 restored counters PASS; 17/17 complete input/instrument manifests equal the green manifest; final sandbox equals green; extra mutant file absent.**

Fixture SHA-256 before the first mutation and after every restoration:

| File | Before = after |
|---|---|
| `corpus/README.md` | `fedc4e048f7363b8286f4ff736e048cdc9f287f15409977c48a32648ffe61108` |
| `corpus/SOURCES.md` | `b0029657ec9a89164b7386d726dc5365a74b96c05fe9978dd242d3bb2f1c8d67` |
| `corpus/knowledge/linguistics/toponymy-place-names.md` | `e594b26f00fd9837c36bd5a5ab0f41a07e257de317209ad4edfd93a105a4b899` |

Frozen counter SHA-256: `162009260b60db8e5f02094ccf3dba71a94c714f01e61fd6a199f1badc2b3534`. Rowcheck: `796f4004eb6cc133a4d04091ccb5be870cab8090d45cfc2c9d70226f4001863e`. Full instrument hashes are in every result receipt. All bounded counter processes exited; no service or background process was left running.

## Cheapest variant not buildable

A **LOCATE-only** invented-quote mutant is not buildable under this frozen detector without changing instruments: an unlocated quote necessarily also fails BOILER and TOPIC. The measured minimal mutation demonstrates that exact three-leg dependency. No claim is made that all fourteen legs are pairwise independent.

## Installs

No system upgrades or permanent tool installations. Existing **uv 0.13.0** supplied the isolated **pypdf 5.4.0** environment via `uv run --no-project --quiet --with pypdf==5.4.0` (PyPI package channel), required by the frozen locator to read the Names PDF; the version was observed. No pacman transaction, headless browser, captcha solving or paywall/login bypass.

Report: .ufo/waves/round-58/control/MutLegIsolation58.md
