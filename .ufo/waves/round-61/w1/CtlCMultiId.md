# CtlCMultiId — claim C multi-id/table pre-data control

- Seat: KotodamaR61.CtlCMultiId; leaf mutation probe only.
- Frozen revision: `78ad4b176695e9fcd490ab607cb8218e2ce62738`.
- Completed: 2026-10-23T09:46:05Z.
- Scope: only this assigned C line-shape probe; no O score, integration, shipping, runtime invocation, or lane corpus edits.

## Axes

1. Coverage: discriminate the claimed one-row-per-bullet and no-range invariants (LINES/RANGE).
2. Reproducibility: exact frozen counter, FLOOR-only probe, full stdout/exit receipts, before/mutant/after hashes.
3. No harm/access: isolated scratch mutations, ordinary public GETs, exact restoration; no sibling source changes.

## Result

**CONTROL-MET (FLOOR-only probe):** `(S652; S 653)` and `(S652; Ｓ653)` retain two human-readable source references on a bullet but pass every probe leg. These are coverage findings for noncanonical citation spelling, not permission to amend the frozen contract. The counter scans raw text with `\bS\d{3,}\b` before locator normalization; neither spelling is a second recognized S-id.

**No frozen PASS was observed.** The two-row pristine fixture, every variant, and every restored fixture fail the frozen FLOOR=20 leg. Thus no mutant is called killed under the frozen predicate: its baseline fails, so frozen kill attribution is inconclusive. The FLOOR=2 probe baseline passes and every post-mutation restoration passes; probe results are 11 killed negative variants, 2 surviving hidden-id variants, and 1 valid single-bracket positive control.

Canonical two-id bullets, tables, headings, paragraphs, bracket pairs, commas, slashes, raw ids in URL fragments, and footnote markers are rejected. Both full and abbreviated en-dash ranges are rejected by RANGE. A single `[S652]` per bullet is accepted as expected.

## Fixture and ordinary-access evidence

- Scratch clone: `/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/clone`. Clone and checkout used the assigned commands with GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE unset.
- Fixtures: `/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/fixtures`; pristine entry `pristine.md`, named variants `<case>.md`, and shared support `README.md` / `SOURCES.md`.
- Counter/receipts: `/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py` and `/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/evidence`. All files are below 5 MB.
- Only new knowledge file was the assigned entry. The index row, culture-material count, total, and live footer were adjusted in scratch; 235 original entries and the frozen base list were retained. Two new mined rows S652/S653 use the assigned entry as used-by, opened 2026-10-23.
- An exact URL search of the frozen registry returned no matches for either new URL. Every counter run independently printed LOCATE PASS for both rows and FRESH PASS; all other non-target legs passed except frozen FLOOR.

Sources (body text read by ordinary means; independent frozen locator returned the following complete stdout):

1. [V&A, Shoes collection](https://www.vam.ac.uk/collections/shoes): anchor `collection of shoes, with around 2,000 pairs spanning more than 3,000 years of history from different cultures around the globe.`

```text
LOCATED https://www.vam.ac.uk/collections/shoes
```

2. [V&A, A history of shoes – timeline](https://www.vam.ac.uk/articles/a-history-of-shoes): anchor `showing chronological progression of shoe height, heel shape and materials, from Roman sandals to sculpted stilettos and the classic wellington boot.`

```text
LOCATED https://www.vam.ac.uk/articles/a-history-of-shoes
```

Both anchors are 8–25 normalized words, carry a footwear word, and the entry uses short restatements rather than a quote dump. The complete pristine fixture follows.

```markdown
# Footwear citation control

- topic: footwear citation control
- status: scratch control

- The collection covers more than 3,000 years of shoes from different cultures. (S652)
- The timeline charts shoe height, materials and heel shape from Roman sandals to sculpted stilettos and the classic wellington boot. (S653)
```

## Counter identity and permitted probe diff

- Frozen counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- Probe counter SHA-256: `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`.
- No TOTAL/base-list/locator/other counter change was made. The original counter file itself was never changed.

```diff
--- clone/reports/round-61/accept-c.py
+++ accept-c-floor-2.py
@@ -54,7 +54,7 @@
 TOTAL = 236
 FIRST_SID = 652
 LAST_SID = 699
-FLOOR = 20
+FLOOR = 2
 LOCATOR = "reports/round-61/reopen-quote.py"
 SHARE = 1.0
 OPENED = "2026-10-23"
```

## Per-item mutant, expected detector, observed result, verdict

| Case | Expected target | Probe result | Probe verdict |
|---|---|---|---|
| `two-ids` | LINES (plus LINK/COPY no-row) | FAIL, exit 1; failed: LINES,LINK,COPY | killed |
| `table-row` | LINES | FAIL, exit 1; failed: LINES | killed |
| `heading` | LINES | FAIL, exit 1; failed: LINES | killed |
| `paragraph` | LINES | FAIL, exit 1; failed: LINES | killed |
| `bracket-single` | PASS: one canonical id per bullet remains valid | PASS, exit 0; failed: none | valid-positive-control |
| `bracket-multi` | LINES (plus LINK/COPY no-row) | FAIL, exit 1; failed: LINES,LINK,COPY | killed |
| `comma` | LINES (plus LINK/COPY no-row) | FAIL, exit 1; failed: LINES,LINK,COPY | killed |
| `slash` | LINES (plus LINK/COPY no-row) | FAIL, exit 1; failed: LINES,LINK,COPY | killed |
| `range-en-dash` | RANGE and LINES (plus LINK/COPY no-row) | FAIL, exit 1; failed: RANGE,LINES,LINK,COPY | killed |
| `range-abbreviated` | RANGE; LINES may pass | FAIL, exit 1; failed: RANGE | killed |
| `hidden-space` | LINES would reject a recognized second reference; literal SID regex is expected to miss S 653 | PASS, exit 0; failed: none | survived |
| `hidden-fullwidth` | LINES would reject a normalized second reference; literal SID regex is expected to miss Ｓ653 | PASS, exit 0; failed: none | survived |
| `url-id` | LINES: raw URL text still exposes the second canonical id | FAIL, exit 1; failed: LINES,LINK,COPY | killed |
| `footnote-marker` | LINES: raw footnote text still exposes the second canonical id | FAIL, exit 1; failed: LINES,LINK,COPY | killed |

Each case starts with the same pristine entry bytes. The initial pristine score is the first baseline; each fully scored restoration is the next case's baseline. Frozen and probe runs for a given byte state were independent foreground subprocesses joined together; mutations on the shared scratch entry were serialized. The same two bounded commands were used throughout. The fixture was restored in a finally block before the next case.

Per-case control verdicts (negative-control meaning, not a round judgment):

```text
NONE-MET CtlCMultiId/two-ids fixture=/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/fixtures/two-ids.md rejected-by-FLOOR-only-probe
NONE-MET CtlCMultiId/table-row fixture=/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/fixtures/table-row.md rejected-by-FLOOR-only-probe
NONE-MET CtlCMultiId/heading fixture=/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/fixtures/heading.md rejected-by-FLOOR-only-probe
NONE-MET CtlCMultiId/paragraph fixture=/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/fixtures/paragraph.md rejected-by-FLOOR-only-probe
NONE-MET CtlCMultiId/bracket-single fixture=/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/fixtures/bracket-single.md valid-positive-control-not-a-miss
NONE-MET CtlCMultiId/bracket-multi fixture=/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/fixtures/bracket-multi.md rejected-by-FLOOR-only-probe
NONE-MET CtlCMultiId/comma fixture=/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/fixtures/comma.md rejected-by-FLOOR-only-probe
NONE-MET CtlCMultiId/slash fixture=/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/fixtures/slash.md rejected-by-FLOOR-only-probe
NONE-MET CtlCMultiId/range-en-dash fixture=/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/fixtures/range-en-dash.md rejected-by-FLOOR-only-probe
NONE-MET CtlCMultiId/range-abbreviated fixture=/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/fixtures/range-abbreviated.md rejected-by-FLOOR-only-probe
CONTROL-MET CtlCMultiId/hidden-space fixture=/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/fixtures/hidden-space.md FLOOR-only-probe; frozen-FLOOR-failed
CONTROL-MET CtlCMultiId/hidden-fullwidth fixture=/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/fixtures/hidden-fullwidth.md FLOOR-only-probe; frozen-FLOOR-failed
NONE-MET CtlCMultiId/url-id fixture=/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/fixtures/url-id.md rejected-by-FLOOR-only-probe
NONE-MET CtlCMultiId/footnote-marker fixture=/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/fixtures/footnote-marker.md rejected-by-FLOOR-only-probe
CONTROL-MET C-multi-id/table fixture=hidden-space.md,hidden-fullwidth.md mode=FLOOR-only-probe
```

## Receipt lines

`counter-sha256` and `exit` identify the frozen run; the added probe fields identify its paired probe run. `stopped-by` lists every frozen FAIL leg. Restored cases are included, not silently omitted.

```text
RECEIPT CtlCMultiId/pristine counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/two-ids counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LINES,LINK,COPY probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=1 probe-stopped-by=LINES,LINK,COPY
RECEIPT CtlCMultiId/two-ids-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/table-row counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LINES probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=1 probe-stopped-by=LINES
RECEIPT CtlCMultiId/table-row-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/heading counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LINES probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=1 probe-stopped-by=LINES
RECEIPT CtlCMultiId/heading-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/paragraph counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LINES probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=1 probe-stopped-by=LINES
RECEIPT CtlCMultiId/paragraph-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/bracket-single counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/bracket-single-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/bracket-multi counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LINES,LINK,COPY probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=1 probe-stopped-by=LINES,LINK,COPY
RECEIPT CtlCMultiId/bracket-multi-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/comma counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LINES,LINK,COPY probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=1 probe-stopped-by=LINES,LINK,COPY
RECEIPT CtlCMultiId/comma-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/slash counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LINES,LINK,COPY probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=1 probe-stopped-by=LINES,LINK,COPY
RECEIPT CtlCMultiId/slash-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/range-en-dash counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,RANGE,LINES,LINK,COPY probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=1 probe-stopped-by=RANGE,LINES,LINK,COPY
RECEIPT CtlCMultiId/range-en-dash-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/range-abbreviated counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,RANGE probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=1 probe-stopped-by=RANGE
RECEIPT CtlCMultiId/range-abbreviated-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/hidden-space counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/hidden-space-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/hidden-fullwidth counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/hidden-fullwidth-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/url-id counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LINES,LINK,COPY probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=1 probe-stopped-by=LINES,LINK,COPY
RECEIPT CtlCMultiId/url-id-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
RECEIPT CtlCMultiId/footnote-marker counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LINES,LINK,COPY probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=1 probe-stopped-by=LINES,LINK,COPY
RECEIPT CtlCMultiId/footnote-marker-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-counter-sha256=d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c probe-exit=0 probe-stopped-by=none
```

## Exact mutation/restoration hashes

Every mutation's pristine-before and restored-after entry SHA-256 is `e54c3bfa04282ed5a0090ca9a3a1b2699bf05807ffa76d0223ea219b6428a211`. Every corresponding restored probe returned PASS/0. The per-case mutated hashes are:

| Case | Mutant SHA-256 |
|---|---|
| `two-ids` | `f8eefd55c9774b1142b490f2d34dabfa040484aecf5e7135d30726877410d184` |
| `table-row` | `96ebc842aa6288f96fe0a00fc17e01cfc26e5691cb5682fe96ea7374fa2da757` |
| `heading` | `d71c537b432464fa6b1ecb9dea225ceb300ff3c5cb22b3f5c58641e752b2ec00` |
| `paragraph` | `3e71af20641f2e910e02b5e394469631c56304934fa6fdef51d232393cd32a73` |
| `bracket-single` | `493fe98b110d6133832043b3d890d83f9a79fc5c335dac14e6c89841419d743d` |
| `bracket-multi` | `88f10a3302e62fe25a3413d45801c71e75a2e08f574e8d7b816005a5477196fd` |
| `comma` | `52ed88644a5b90a5f78173a491b01cadb89b2e1392d0b40122e036411da7ede4` |
| `slash` | `f66988db7d15e89aac9817d3ff546dc5598d26db235582122863c9fcd1489911` |
| `range-en-dash` | `066b32cfe1c18dafbc964df97599a9220cbd6712e41db6680c2ba443c8f2391c` |
| `range-abbreviated` | `084091d13a8fc4cac0726889b3087543a029b17c19929518693617257a7d7a09` |
| `hidden-space` | `32c2f581040b925bca65775fe1dbd06649c8d1d0c8c5e50d5d27b8c64c7148f3` |
| `hidden-fullwidth` | `c02f5d24e79eb45fae327e24a8f5b24e2eea060a9229cb58d2552b45a78899c2` |
| `url-id` | `9d3e9247b55adaae325e815e9457cbc61ff724e2831eb969fad42a2b2ae20c25` |
| `footnote-marker` | `f11c451d095d5da61d2dac3f6e385ba18ef8d28ea3121117bac86e802327bb11` |

After all 14 probes, the added scratch entry was removed (absent both before fixture construction and at final cleanup), and original clone index/registry bytes were restored. Exact byte comparisons and SHA-256 evidence:

| Original file | Before SHA-256 | After SHA-256 | Exact bytes |
|---|---|---|---|
| `corpus/README.md` | `a7fc403cf0f2908581926515d70c5b358afb504ac132bde3e1a0987e5870352c` | `a7fc403cf0f2908581926515d70c5b358afb504ac132bde3e1a0987e5870352c` | True |
| `corpus/SOURCES.md` | `641115af3777359d9b42cce28a249f7ce6807df601e543b4f5a867c74d7af485` | `641115af3777359d9b42cce28a249f7ce6807df601e543b4f5a867c74d7af485` | True |
| `reports/round-61/accept-c.py` | `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10` | `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10` | True |

Detailed immutable evidence: `/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/evidence/restoration.json`, `/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/evidence/manifest.json`, `/fast/scratch/hyaku/kotodama-r61/CtlCMultiId/evidence/runs.json`. Fixture support files and all entry variants remain outside the clone for replay. All 58 counter subprocesses returned 0/1, emitted no stderr, and were joined; no process timed out or background service was started. All launched process trees have completed. No tool installs or updates were needed.

## Every run: full stdout and exit code

No stdout lines are abbreviated. Every run used cwd equal to the scratch clone. Its counter SHA-256 is given with each invocation.

### pristine

Entry SHA-256: `e54c3bfa04282ed5a0090ca9a3a1b2699bf05807ffa76d0223ea219b6428a211`.

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:43Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:43Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### two-ids

Entry SHA-256: `f8eefd55c9774b1142b490f2d34dabfa040484aecf5e7135d30726877410d184`.

First bullet changes `(S652)` to `(S652 S653)`; the second bullet remains unchanged.

```markdown
# Footwear citation control

- topic: footwear citation control
- status: scratch control

- The collection covers more than 3,000 years of shoes from different cultures. (S652 S653)
- The timeline charts shoe height, materials and heel shape from Roman sandals to sculpted stilettos and the classic wellington boot. (S653)
```

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652,S653']
TOPIC PASS rows=2 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652,S653']
TOPIC PASS rows=2 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### two-ids-restored

Entry SHA-256: `e54c3bfa04282ed5a0090ca9a3a1b2699bf05807ffa76d0223ea219b6428a211`.

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### table-row

Entry SHA-256: `96ebc842aa6288f96fe0a00fc17e01cfc26e5691cb5682fe96ea7374fa2da757`.

The first cited clause becomes a Markdown table row, with a header and delimiter row.

```markdown
# Footwear citation control

- topic: footwear citation control
- status: scratch control

| Note | Citation |
|---|---|
| The collection covers more than 3,000 years of shoes from different cultures. | S652 |
- The timeline charts shoe height, materials and heel shape from Roman sandals to sculpted stilettos and the classic wellington boot. (S653)
```

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['8:S652']
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['8:S652']
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### table-row-restored

Entry SHA-256: `e54c3bfa04282ed5a0090ca9a3a1b2699bf05807ffa76d0223ea219b6428a211`.

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### heading

Entry SHA-256: `d71c537b432464fa6b1ecb9dea225ceb300ff3c5cb22b3f5c58641e752b2ec00`.

The first cited clause changes from `- ` to `## `.

```markdown
# Footwear citation control

- topic: footwear citation control
- status: scratch control

## The collection covers more than 3,000 years of shoes from different cultures. (S652)
- The timeline charts shoe height, materials and heel shape from Roman sandals to sculpted stilettos and the classic wellington boot. (S653)
```

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652']
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652']
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### heading-restored

Entry SHA-256: `e54c3bfa04282ed5a0090ca9a3a1b2699bf05807ffa76d0223ea219b6428a211`.

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### paragraph

Entry SHA-256: `3e71af20641f2e910e02b5e394469631c56304934fa6fdef51d232393cd32a73`.

The first cited clause loses its bullet prefix.

```markdown
# Footwear citation control

- topic: footwear citation control
- status: scratch control

The collection covers more than 3,000 years of shoes from different cultures. (S652)
- The timeline charts shoe height, materials and heel shape from Roman sandals to sculpted stilettos and the classic wellington boot. (S653)
```

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652']
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652']
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### paragraph-restored

Entry SHA-256: `e54c3bfa04282ed5a0090ca9a3a1b2699bf05807ffa76d0223ea219b6428a211`.

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### bracket-single

Entry SHA-256: `493fe98b110d6133832043b3d890d83f9a79fc5c335dac14e6c89841419d743d`.

Both citations change from parentheses to `[S652]` / `[S653]`; this is a valid positive control, not a multi-id defect.

```markdown
# Footwear citation control

- topic: footwear citation control
- status: scratch control

- The collection covers more than 3,000 years of shoes from different cultures. [S652]
- The timeline charts shoe height, materials and heel shape from Roman sandals to sculpted stilettos and the classic wellington boot. [S653]
```

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### bracket-single-restored

Entry SHA-256: `e54c3bfa04282ed5a0090ca9a3a1b2699bf05807ffa76d0223ea219b6428a211`.

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### bracket-multi

Entry SHA-256: `88f10a3302e62fe25a3413d45801c71e75a2e08f574e8d7b816005a5477196fd`.

The first cited clause carries `[S652] [S653]`.

```markdown
# Footwear citation control

- topic: footwear citation control
- status: scratch control

- The collection covers more than 3,000 years of shoes from different cultures. [S652] [S653]
- The timeline charts shoe height, materials and heel shape from Roman sandals to sculpted stilettos and the classic wellington boot. (S653)
```

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652,S653']
TOPIC PASS rows=2 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652,S653']
TOPIC PASS rows=2 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### bracket-multi-restored

Entry SHA-256: `e54c3bfa04282ed5a0090ca9a3a1b2699bf05807ffa76d0223ea219b6428a211`.

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### comma

Entry SHA-256: `52ed88644a5b90a5f78173a491b01cadb89b2e1392d0b40122e036411da7ede4`.

The first cited clause carries `S652,S653`.

```markdown
# Footwear citation control

- topic: footwear citation control
- status: scratch control

- The collection covers more than 3,000 years of shoes from different cultures. (S652,S653)
- The timeline charts shoe height, materials and heel shape from Roman sandals to sculpted stilettos and the classic wellington boot. (S653)
```

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652,S653']
TOPIC PASS rows=2 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652,S653']
TOPIC PASS rows=2 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### comma-restored

Entry SHA-256: `e54c3bfa04282ed5a0090ca9a3a1b2699bf05807ffa76d0223ea219b6428a211`.

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### slash

Entry SHA-256: `f66988db7d15e89aac9817d3ff546dc5598d26db235582122863c9fcd1489911`.

The first cited clause carries `S652/S653`.

```markdown
# Footwear citation control

- topic: footwear citation control
- status: scratch control

- The collection covers more than 3,000 years of shoes from different cultures. (S652/S653)
- The timeline charts shoe height, materials and heel shape from Roman sandals to sculpted stilettos and the classic wellington boot. (S653)
```

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652,S653']
TOPIC PASS rows=2 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652,S653']
TOPIC PASS rows=2 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### slash-restored

Entry SHA-256: `e54c3bfa04282ed5a0090ca9a3a1b2699bf05807ffa76d0223ea219b6428a211`.

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### range-en-dash

Entry SHA-256: `066b32cfe1c18dafbc964df97599a9220cbd6712e41db6680c2ba443c8f2391c`.

The first cited clause carries `S652–S653`.

```markdown
# Footwear citation control

- topic: footwear citation control
- status: scratch control

- The collection covers more than 3,000 years of shoes from different cultures. (S652–S653)
- The timeline charts shoe height, materials and heel shape from Roman sandals to sculpted stilettos and the classic wellington boot. (S653)
```

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE FAIL bad=[] range_notation=['S652–S653']
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652,S653']
TOPIC PASS rows=2 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE FAIL bad=[] range_notation=['S652–S653']
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652,S653']
TOPIC PASS rows=2 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### range-en-dash-restored

Entry SHA-256: `e54c3bfa04282ed5a0090ca9a3a1b2699bf05807ffa76d0223ea219b6428a211`.

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### range-abbreviated

Entry SHA-256: `084091d13a8fc4cac0726889b3087543a029b17c19929518693617257a7d7a09`.

The first cited clause carries `S652–653`; this isolates RANGE because the second endpoint is not a complete S-id token.

```markdown
# Footwear citation control

- topic: footwear citation control
- status: scratch control

- The collection covers more than 3,000 years of shoes from different cultures. (S652–653)
- The timeline charts shoe height, materials and heel shape from Roman sandals to sculpted stilettos and the classic wellington boot. (S653)
```

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE FAIL bad=[] range_notation=['S652–653']
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE FAIL bad=[] range_notation=['S652–653']
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### range-abbreviated-restored

Entry SHA-256: `e54c3bfa04282ed5a0090ca9a3a1b2699bf05807ffa76d0223ea219b6428a211`.

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### hidden-space

Entry SHA-256: `32c2f581040b925bca65775fe1dbd06649c8d1d0c8c5e50d5d27b8c64c7148f3`.

The first cited clause carries `(S652; S 653)`; a separate legitimate S653 bullet preserves the two-row floor.

```markdown
# Footwear citation control

- topic: footwear citation control
- status: scratch control

- The collection covers more than 3,000 years of shoes from different cultures. (S652; S 653)
- The timeline charts shoe height, materials and heel shape from Roman sandals to sculpted stilettos and the classic wellington boot. (S653)
```

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### hidden-space-restored

Entry SHA-256: `e54c3bfa04282ed5a0090ca9a3a1b2699bf05807ffa76d0223ea219b6428a211`.

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### hidden-fullwidth

Entry SHA-256: `c02f5d24e79eb45fae327e24a8f5b24e2eea060a9229cb58d2552b45a78899c2`.

The first cited clause carries `(S652; Ｓ653)` (U+FF33 FULLWIDTH LATIN CAPITAL LETTER S); the separate S653 bullet is unchanged.

```markdown
# Footwear citation control

- topic: footwear citation control
- status: scratch control

- The collection covers more than 3,000 years of shoes from different cultures. (S652; Ｓ653)
- The timeline charts shoe height, materials and heel shape from Roman sandals to sculpted stilettos and the classic wellington boot. (S653)
```

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### hidden-fullwidth-restored

Entry SHA-256: `e54c3bfa04282ed5a0090ca9a3a1b2699bf05807ffa76d0223ea219b6428a211`.

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### url-id

Entry SHA-256: `9d3e9247b55adaae325e815e9457cbc61ff724e2831eb969fad42a2b2ae20c25`.

The first cited clause includes S652 and a link whose URL fragment is `#S653`.

```markdown
# Footwear citation control

- topic: footwear citation control
- status: scratch control

- The collection covers more than 3,000 years of shoes from different cultures. (S652; [timeline](https://www.vam.ac.uk/articles/a-history-of-shoes#S653))
- The timeline charts shoe height, materials and heel shape from Roman sandals to sculpted stilettos and the classic wellington boot. (S653)
```

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652,S653']
TOPIC PASS rows=2 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652,S653']
TOPIC PASS rows=2 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### url-id-restored

Entry SHA-256: `e54c3bfa04282ed5a0090ca9a3a1b2699bf05807ffa76d0223ea219b6428a211`.

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### footnote-marker

Entry SHA-256: `f11c451d095d5da61d2dac3f6e385ba18ef8d28ea3121117bac86e802327bb11`.

The first cited clause carries `(S652)[^S653]`.

```markdown
# Footwear citation control

- topic: footwear citation control
- status: scratch control

- The collection covers more than 3,000 years of shoes from different cultures. (S652)[^S653]
- The timeline charts shoe height, materials and heel shape from Roman sandals to sculpted stilettos and the classic wellington boot. (S653)
```

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652,S653']
TOPIC PASS rows=2 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=2 bad=['6:S652,S653']
TOPIC PASS rows=2 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### footnote-marker-restored

Entry SHA-256: `e54c3bfa04282ed5a0090ca9a3a1b2699bf05807ffa76d0223ea219b6428a211`.

**frozen** — counter SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`

```text
$ timeout 900 python3 -B reports/round-61/accept-c.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

**probe** — counter SHA-256 `d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`

```text
$ timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCMultiId/accept-c-floor-2.py
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

