VERDICT: ALL-FAIL

| mutant | killing fixture | original verdict | mutant verdict |
|---|---|---|---|
| F01-drop-relevance-a ([diff](MutRowcheck58/mutants/F01-drop-relevance-a.patch), [receipt](MutRowcheck58/mutants/F01-drop-relevance-a.json)) | [patch](MutRowcheck58/fixtures/edec-rel-a/fixture.patch) `edec-rel-a` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| F02-drop-relevance-b ([diff](MutRowcheck58/mutants/F02-drop-relevance-b.patch), [receipt](MutRowcheck58/mutants/F02-drop-relevance-b.json)) | [patch](MutRowcheck58/fixtures/edec-rel-b/fixture.patch) `edec-rel-b` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| F03-drop-relevance-c ([diff](MutRowcheck58/mutants/F03-drop-relevance-c.patch), [receipt](MutRowcheck58/mutants/F03-drop-relevance-c.json)) | [patch](MutRowcheck58/fixtures/edec-rel-c/fixture.patch) `edec-rel-c` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| F04-drop-relevance-d ([diff](MutRowcheck58/mutants/F04-drop-relevance-d.patch), [receipt](MutRowcheck58/mutants/F04-drop-relevance-d.json)) | [patch](MutRowcheck58/fixtures/edec-rel-d/fixture.patch) `edec-rel-d` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| F05-copy-run-99 ([diff](MutRowcheck58/mutants/F05-copy-run-99.patch), [receipt](MutRowcheck58/mutants/F05-copy-run-99.json)) | [patch](MutRowcheck58/fixtures/edec-copy-six/fixture.patch) `edec-copy-six` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| F06-boiler-always-true ([diff](MutRowcheck58/mutants/F06-boiler-always-true.patch), [receipt](MutRowcheck58/mutants/F06-boiler-always-true.json)) | [patch](MutRowcheck58/fixtures/edec-boiler/fixture.patch) `edec-boiler` | BOILER FAIL; D=0 | BOILER PASS; D=1; **killed** |
| F07-page-hits-zero ([diff](MutRowcheck58/mutants/F07-page-hits-zero.patch), [receipt](MutRowcheck58/mutants/F07-page-hits-zero.json)) | [patch](MutRowcheck58/fixtures/edec-page-hits/fixture.patch) `edec-page-hits` | TOPIC FAIL; D=0 | TOPIC FAIL; D=0; **survived** |
| F08-window-fifty ([diff](MutRowcheck58/mutants/F08-window-fifty.patch), [receipt](MutRowcheck58/mutants/F08-window-fifty.json)) | [patch](MutRowcheck58/fixtures/edec-window/fixture.patch) `edec-window` | TOPIC FAIL; D=0 | TOPIC PASS; D=1; **killed** |
| F09-stems-ignore-stop ([diff](MutRowcheck58/mutants/F09-stems-ignore-stop.patch), [receipt](MutRowcheck58/mutants/F09-stems-ignore-stop.json)) | [patch](MutRowcheck58/fixtures/edec-stem-stop/fixture.patch) `edec-stem-stop` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| F10-stems-min-three ([diff](MutRowcheck58/mutants/F10-stems-min-three.patch), [receipt](MutRowcheck58/mutants/F10-stems-min-three.json)) | [patch](MutRowcheck58/fixtures/edec-stem-short/fixture.patch) `edec-stem-short` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| F11-stems-no-singular ([diff](MutRowcheck58/mutants/F11-stems-no-singular.patch), [receipt](MutRowcheck58/mutants/F11-stems-no-singular.json)) | [patch](MutRowcheck58/fixtures/edec-stem-plural/fixture.patch) `edec-stem-plural` | RELEVANCE PASS; D=0 | RELEVANCE FAIL; D=1; **killed** |
| F12-stems-width-four ([diff](MutRowcheck58/mutants/F12-stems-width-four.patch), [receipt](MutRowcheck58/mutants/F12-stems-width-four.json)) | [patch](MutRowcheck58/fixtures/edec-stem-width/fixture.patch) `edec-stem-width` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| F13-topic-seq-no-singular ([diff](MutRowcheck58/mutants/F13-topic-seq-no-singular.patch), [receipt](MutRowcheck58/mutants/F13-topic-seq-no-singular.json)) | [patch](MutRowcheck58/fixtures/edec-seq-plural/fixture.patch) `edec-seq-plural` | TOPIC PASS; D=0 | TOPIC FAIL; D=1; **killed** |
| F14-page-terms-zero ([diff](MutRowcheck58/mutants/F14-page-terms-zero.patch), [receipt](MutRowcheck58/mutants/F14-page-terms-zero.json)) | [patch](MutRowcheck58/fixtures/edec-page-terms/fixture.patch) `edec-page-terms` | TOPIC FAIL; D=0 | TOPIC PASS; D=1; **killed** |
| F15-quote-function-zero ([diff](MutRowcheck58/mutants/F15-quote-function-zero.patch), [receipt](MutRowcheck58/mutants/F15-quote-function-zero.json)) | [patch](MutRowcheck58/fixtures/edec-function-floor/fixture.patch) `edec-function-floor` | TOPIC FAIL; D=0 | TOPIC PASS; D=1; **killed** |
| F16-teaches-words-zero ([diff](MutRowcheck58/mutants/F16-teaches-words-zero.patch), [receipt](MutRowcheck58/mutants/F16-teaches-words-zero.json)) | [patch](MutRowcheck58/fixtures/edec-teaches-floor/fixture.patch) `edec-teaches-floor` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| L01-page-hits-zero-independent ([diff](MutRowcheck58/mutants/L01-page-hits-zero-independent.patch), [receipt](MutRowcheck58/mutants/L01-page-hits-zero-independent.json)) | [patch](MutRowcheck58/fixtures/latest-page-floor/fixture.patch) `latest-page-floor` | TOPIC FAIL; D=0 | TOPIC PASS; D=1; **killed** |
| L02-labels-empty ([diff](MutRowcheck58/mutants/L02-labels-empty.patch), [receipt](MutRowcheck58/mutants/L02-labels-empty.json)) | [patch](MutRowcheck58/fixtures/latest-labels-id/fixture.patch) `latest-labels-id` | BOILER FAIL; D=0 | BOILER PASS; D=1; **killed** |
| L03-min-hosts-one ([diff](MutRowcheck58/mutants/L03-min-hosts-one.patch), [receipt](MutRowcheck58/mutants/L03-min-hosts-one.json)) | [patch](MutRowcheck58/fixtures/latest-one-host/fixture.patch) `latest-one-host` | DISTINCT FAIL; D=0 | DISTINCT PASS; D=1; **killed** |
| L04-distinct-always-true ([diff](MutRowcheck58/mutants/L04-distinct-always-true.patch), [receipt](MutRowcheck58/mutants/L04-distinct-always-true.json)) | [patch](MutRowcheck58/fixtures/latest-duplicate/fixture.patch) `latest-duplicate` | DISTINCT FAIL; D=0 | DISTINCT PASS; D=1; **killed** |
| L05-locate-slack-80 ([diff](MutRowcheck58/mutants/L05-locate-slack-80.patch), [receipt](MutRowcheck58/mutants/L05-locate-slack-80.json)) | [patch](MutRowcheck58/fixtures/latest-locate-slack/fixture.patch) `latest-locate-slack` | LOCATE FAIL; D=0 | LOCATE PASS; D=1; **killed** |
| L06-omit-topic-loop ([diff](MutRowcheck58/mutants/L06-omit-topic-loop.patch), [receipt](MutRowcheck58/mutants/L06-omit-topic-loop.json)) | [patch](MutRowcheck58/fixtures/latest-omit-topic/fixture.patch) `latest-omit-topic` | TOPIC FAIL; D=0 | TOPIC MISSING; D=1; **killed** |
| L07-tier-always-true ([diff](MutRowcheck58/mutants/L07-tier-always-true.patch), [receipt](MutRowcheck58/mutants/L07-tier-always-true.json)) | [patch](MutRowcheck58/fixtures/latest-tier/fixture.patch) `latest-tier` | TIER FAIL; D=0 | TIER PASS; D=1; **killed** |

## Scope and detector semantics

- F01–F16 measured `edecdc904953cc8a76a4e0d644bd544af775d1e3`; L01–L07 measured `1a07344e77ea34c3e6b3c38a838c7c35654522be`. Results are revision-labelled, not extrapolated across freezes. The earlier d4a5 generation is retained below. c421 baselines were superseded before any c421 mutant was scored.
- Axes: fault sensitivity, live-page concreteness, minimality, exact restoration.
- `D` is the bounded behavioral detector exit, **not** the counter exit: D=0 means the expected original decision was observed. A negative fixture correctly failing its target leg is a passing baseline detector. A kill requires pristine D=0, mutant D=1 with an actual changed observation, restored D=0. No failed baseline is counted as a kill.
- Row probes call the frozen `check_row` on one real source row and print every row leg. One row is sufficient because these rules have no cross-row state. Positive stem fixtures deliberately expose false rejection; other fixtures expose false acceptance. This is focused guard sensitivity, not an aggregate ACCEPT-C kill.
- Counter probes execute the real bounded `python3 -B reports/round-58/accept-c.py` in the clone. One row suffices for host/TIER/leg-presence checks; two are minimal for duplicate detection; five (4 located, 1 invented absent quote) are minimal for an 80% ceiling versus strict LOCATE equality. FLOOR remains intentionally red. A missing TOPIC output kills the loop-omission mutant even though other independent legs keep the aggregate red.
- Source GETs were ordinary urllib GETs, with no browser, CAPTCHA solving, login or bypass. [Access receipts](MutRowcheck58/access-final.json) record statuses and response SHA-256s. Fresh URL candidates were checked against the frozen registry.

## Survivors and discriminating witnesses

- **F07-page-hits-zero survived** the Huck Finn fixture: quote_hits=1, page_hits=2, page_terms=0; PAGE_TERMS still rejected it after PAGE_HITS became 0. This is a masking/coverage finding for that concrete fixture, not permission to weaken the contract.
- L01 kills the analogous PAGE_HITS mutation on the later 1a07344e freeze with the real Crossref title “Toponymy and Geopolitics: The Political Use — and Misuse — of Geographical Names”: quote_hits=2, distinct function_words=3, page_hits=2, page_terms=2. Only the page-hit threshold rejects it. [Original output](MutRowcheck58/runs/latest-baseline.latest-page-floor.pristine.stdout), [mutant output](MutRowcheck58/runs/L01-page-hits-zero-independent.latest-page-floor.mutated.stdout).
- F05 uses exactly one six-word copied run, “Toponym is the general term for”, rather than relying only on a fully copied quote.
- F08 uses the real sentence “The generic identifies the kind of place denoted by the name, while the specific distinguishes the place from others in the same class.” The nearest relevant name/place distance is 4: WINDOW=3 rejects; WINDOW=50 accepts.
- F14 uses Moby Dick’s real Berlin Gazette sentence: page_hits=3, page_terms=0. F15 uses the actual Wikipedia contents fragment “2 Toponymic typology 3 Toponymic structure 4 History 5 Toponomastics”: zero function words.
- L02 uses a real long article heading through `https://en.wikipedia.org/?curid=750096`; the ordinary fetched heading is located, root-clear, and rejected specifically as title/h1/meta. Empty LABELS accepts it.

## Full original counter runs

| variant | fixture path | failing legs | exit |
|---|---|---|---|
| latest-one-host | [fixture.patch](MutRowcheck58/fixtures/latest-one-host/fixture.patch), [stdout](MutRowcheck58/runs/latest-baseline.latest-one-host.pristine.counter.stdout) | FLOOR, DISTINCT | 1 |
| latest-duplicate | [fixture.patch](MutRowcheck58/fixtures/latest-duplicate/fixture.patch), [stdout](MutRowcheck58/runs/latest-baseline.latest-duplicate.pristine.counter.stdout) | FLOOR, DISTINCT | 1 |
| latest-locate-slack | [fixture.patch](MutRowcheck58/fixtures/latest-locate-slack/fixture.patch), [stdout](MutRowcheck58/runs/latest-baseline.latest-locate-slack.pristine.counter.stdout) | FLOOR, LOCATE, BOILER, TOPIC, DISTINCT | 1 |
| latest-omit-topic | [fixture.patch](MutRowcheck58/fixtures/latest-omit-topic/fixture.patch), [stdout](MutRowcheck58/runs/latest-baseline.latest-omit-topic.pristine.counter.stdout) | FLOOR, RELEVANCE, TOPIC, DISTINCT | 1 |
| latest-tier | [fixture.patch](MutRowcheck58/fixtures/latest-tier/fixture.patch), [stdout](MutRowcheck58/runs/latest-baseline.latest-tier.pristine.counter.stdout) | FLOOR, TIER, DISTINCT | 1 |

Every listed original full counter run printed `ACCEPT-C-58: FAIL` and exited 1. No fixture was observed passing the original counter. Mutated counter runs also remain aggregate FAIL because the minimal fixtures retain independent red legs; their target leg decisions change as shown above.

## Cheapest variant not built

The initial long-title Wikipedia slug fixture could not be used as a located BOILER baseline: the unchanged locator rejected its URL as `url-reflects-quote` ([actual baseline](MutRowcheck58/runs/latest-baseline.latest-labels.pristine.stdout), D=2/inconclusive). The same real article was then opened using its real `curid`, producing the valid L02 fixture. No named mutant was left without a concrete probe. An all-green aggregate one-page/one-row variant was not constructed: FLOOR requires 20 ids and DISTINCT requires unique URLs/quotes across 10 hosts; the justified minimal fixtures cannot meet those independent legs by construction.

## Restoration and reproducibility

- All changes were contained in `/fast/scratch/hyaku/kotodama-r58/MutRowcheck58/clone`; lane writes are this report and its sibling evidence directory only. No lane/fleet Git or jj writes occurred.
- Each linked mutant receipt gives before, mutated and restored SHA-256s, the three actual detector exits, and all stdout paths. Every completed mutant restored byte-identically, including the surviving probe.
- Final 1a07344e rowcheck SHA-256, before=after: `796f4004eb6cc133a4d04091ccb5be870cab8090d45cfc2c9d70226f4001863e`.
- Final accept-c SHA-256, before=after: `162009260b60db8e5f02094ccf3dba71a94c714f01e61fd6a199f1badc2b3534`.
- edec rowcheck SHA-256 used by F probes: `a10f83739c72d1acd6380f217435dfbc97b726df06a4bac8e26f64c54d051aa5`; its counter hash is the same final counter hash above.
- [Final restoration receipt](MutRowcheck58/restoration.json), [all mutant receipts](MutRowcheck58/mutants.json), [all command/exit/hash records](MutRowcheck58/runs.json), [detector source](MutRowcheck58/mutation_probe.py). Per-run `*.stdout`/`*.stderr` are the full wrapper streams; `*.counter.stdout`/`*.counter.exit` preserve the exact counter stream and its exit separately.
- Every process was timeout-bounded and synchronously reaped. No services/background jobs or other runtimes were invoked. Original corpus README/SOURCES bytes were also restored; the temporary entry was removed. Reproducible fixture bytes remain in the evidence directory.

## Historical d4a5 generation

These thirteen earlier probes completed before the parent supplied the revised freezes. They are retained as measured history, not evidence for a later freeze.

| mutant | killing fixture | original verdict | mutant verdict |
|---|---|---|---|
| M01-drop-relevance-a ([diff](MutRowcheck58/mutants/M01-drop-relevance-a.patch), [receipt](MutRowcheck58/mutants/M01-drop-relevance-a.json)) | [patch](MutRowcheck58/fixtures/rel-a/fixture.patch) `rel-a` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| M02-drop-relevance-b ([diff](MutRowcheck58/mutants/M02-drop-relevance-b.patch), [receipt](MutRowcheck58/mutants/M02-drop-relevance-b.json)) | [patch](MutRowcheck58/fixtures/rel-b/fixture.patch) `rel-b` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| M03-drop-relevance-c ([diff](MutRowcheck58/mutants/M03-drop-relevance-c.patch), [receipt](MutRowcheck58/mutants/M03-drop-relevance-c.json)) | [patch](MutRowcheck58/fixtures/rel-c/fixture.patch) `rel-c` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| M04-drop-relevance-d ([diff](MutRowcheck58/mutants/M04-drop-relevance-d.patch), [receipt](MutRowcheck58/mutants/M04-drop-relevance-d.json)) | [patch](MutRowcheck58/fixtures/rel-d/fixture.patch) `rel-d` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| M05-copy-run-99 ([diff](MutRowcheck58/mutants/M05-copy-run-99.patch), [receipt](MutRowcheck58/mutants/M05-copy-run-99.json)) | [patch](MutRowcheck58/fixtures/rel-b/fixture.patch) `rel-b` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| M06-boiler-always-true ([diff](MutRowcheck58/mutants/M06-boiler-always-true.patch), [receipt](MutRowcheck58/mutants/M06-boiler-always-true.json)) | [patch](MutRowcheck58/fixtures/boiler/fixture.patch) `boiler` | BOILER FAIL; D=0 | BOILER PASS; D=1; **killed** |
| M07-page-hits-zero ([diff](MutRowcheck58/mutants/M07-page-hits-zero.patch), [receipt](MutRowcheck58/mutants/M07-page-hits-zero.json)) | [patch](MutRowcheck58/fixtures/page-hits/fixture.patch) `page-hits` | TOPIC FAIL; D=0 | TOPIC PASS; D=1; **killed** |
| M08-window-fifty ([diff](MutRowcheck58/mutants/M08-window-fifty.patch), [receipt](MutRowcheck58/mutants/M08-window-fifty.json)) | [patch](MutRowcheck58/fixtures/window/fixture.patch) `window` | TOPIC FAIL; D=0 | TOPIC PASS; D=1; **killed** |
| M09-stems-ignore-stop ([diff](MutRowcheck58/mutants/M09-stems-ignore-stop.patch), [receipt](MutRowcheck58/mutants/M09-stems-ignore-stop.json)) | [patch](MutRowcheck58/fixtures/stem-stop/fixture.patch) `stem-stop` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| M10-stems-min-three ([diff](MutRowcheck58/mutants/M10-stems-min-three.patch), [receipt](MutRowcheck58/mutants/M10-stems-min-three.json)) | [patch](MutRowcheck58/fixtures/stem-short/fixture.patch) `stem-short` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| M11-stems-no-singular ([diff](MutRowcheck58/mutants/M11-stems-no-singular.patch), [receipt](MutRowcheck58/mutants/M11-stems-no-singular.json)) | [patch](MutRowcheck58/fixtures/stem-plural/fixture.patch) `stem-plural` | RELEVANCE PASS; D=0 | RELEVANCE FAIL; D=1; **killed** |
| M12-stems-width-four ([diff](MutRowcheck58/mutants/M12-stems-width-four.patch), [receipt](MutRowcheck58/mutants/M12-stems-width-four.json)) | [patch](MutRowcheck58/fixtures/stem-width/fixture.patch) `stem-width` | RELEVANCE FAIL; D=0 | RELEVANCE PASS; D=1; **killed** |
| M13-topic-seq-no-singular ([diff](MutRowcheck58/mutants/M13-topic-seq-no-singular.patch), [receipt](MutRowcheck58/mutants/M13-topic-seq-no-singular.json)) | [patch](MutRowcheck58/fixtures/seq-plural/fixture.patch) `seq-plural` | TOPIC PASS; D=0 | TOPIC FAIL; D=1; **killed** |

## Installs

None. Python and Git already available; no package transaction or update was performed.

Report: .ufo/waves/round-58/control/MutRowcheck58.md
