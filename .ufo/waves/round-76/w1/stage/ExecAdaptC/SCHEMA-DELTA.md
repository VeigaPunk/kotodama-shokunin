# Claim-C schema deltas — round 76 (ACCEPT-C-76)

Counter: `.ufo/waves/round-76/w1/stage/ExecAdaptC/accept-c.py` (6686 lines,
sha256 `9db9305d5b4a7a8df8e9173e521e34ed40ef52b7680631dd2039e14a5142dd12`).
Draft claim document: `claim-C.json` (same directory), loadable as
`reports/round-76/claims.json` once claim Ca's object is added at the freeze.

The frozen claims.json is the contract. Every constant the counter uses is
read with `git show <freeze>:reports/round-76/claims.json` (QUALITY 25/26/28);
nothing is parsed out of prose that the freeze could leave ambiguous.

## 1. Why the schema has to change

Round 75's claim C was an EXACT-SET claim: `entries[]` was the three admitted
paths, `row_set[]` was the nine rows, and the ENTRIES/ROWS legs compared the
landed tree against those lists one-for-one. Round 76's claim C is a
THRESHOLD claim: four candidate paths, `n >= 2` admitted, and `k` registry
rows where k is *derived* from the documents the admitted entries cite. An
exact-set counter would either grade a two-candidate landing as a missing
entry or accept a row that no admitted entry cites.

## 2. New / changed keys (claims[id="C"])

| key | shape | required | reading |
|---|---|---|---|
| `candidates[]` | `{"path", "admitted": bool, "cites": [S-id], "documents": [url]}` | yes | the four candidate entry paths; `admitted` is a REQUIRED boolean (the freeze is the only authority on the admission set) |
| `min_admitted` | int >= 1 | yes | the floor; a freeze that admits fewer refuses (exit 2) |
| `entries[]` | paths | optional | when present it must be EXACTLY the admitted candidate paths, else the loader refuses; the counter's `cfg["entries"]` is the admitted subset |
| `rows_before` | int >= 1 | yes | the base registry row count (817); ROWS grades base == declared and lands == declared + k |
| `knowledge_before` | int >= 1 | yes | the base `corpus/knowledge` .md count (252); ENTRIES grades base == declared and lands == declared + n |
| `row_set[]` | unchanged (`id`/`staged`/`document`) | yes | one row per NEW document; ROWS now also derives k from the entries and requires the row set to cover exactly the cited new documents |
| `reused_rows[]` | unchanged | yes (may be `[]`) | rows the round re-opens; round 76 freezes none (S892/S885 are cited as already-held rows, not re-opened) |
| `requoted[]` | `{"staged", "lane"}` | optional (`[]`) | replaces round 75's hard-coded `S870 -> S893`: each staged id whose document is re-opened is observable only when an admitted entry cites its lane id |
| `ground.sweeps[]` | `{"pattern", "candidate", "scope"}` | yes | the before/after ground probe (D10 below) |
| `ground.receipt` | repo path | optional | the gap-sweep receipt; graded only when declared (declared here) |
| `ground.fragments[]` | strings | yes | documents the base registry must not name (re-derived at base) |
| `ground.terms[]` | strings | optional | round 76 freezes none; an absent list is not a frozen-constant failure (the sweeps are the coverage surface) |
| `rejects.counts` | `{adopted, path_present, refused, total_staged_files}` | optional | `adopted` must equal `len(entries)`; the lesson must state the same triple summing to the total |
| `map.path` / `map.sha256` | unchanged | yes | the by-document map, hash-pinned |
| `legs[]`, `access_date`, `base`, `owned_inplace` | unchanged | `legs[]`, `base` yes | LEGCOUNT and the receipt |

`CLAIM_KEYS` is now
`("candidates", "min_admitted", "rows_before", "knowledge_before", "row_set",
"ground", "rejects")` — `entries` is the optional cross-check.

## 3. Leg-by-leg effect (13 legs kept, none added or dropped)

| leg | round-75 behaviour | round-76 behaviour |
|---|---|---|
| ENTRIES | exact frozen entry list, shape/length gate | + `n >= min_admitted`; a NON-admitted candidate path present at lands is a FAIL; knowledge tree must hold `knowledge_before + n` .md files; base must hold exactly `knowledge_before` |
| ROWS | exact frozen row set, used-by, quote-in-anchor | + `rows_before` -> `rows_before + k`; k = distinct DOCUMENTS the admitted entries cite that the base registry did not hold (document key space, never raw+doc); one row per document (no two added rows on one document, no row re-adding a base-held document); no admitted entry may be supported only by tier-C rows |
| REPOINTED | forbidden = staged ids not adopted; staged `S870` must be replaced | same by-document join; a citation resolves to a frozen lane id OR a row the claim base held (the draft cites already-held S892/S885); campaign-namespace ids never resolve as themselves; the `requoted[]` records replace the S870/S893 hard-code |
| GATE | unchanged | unchanged (rows + reused; access date 2026-10-27) |
| EVIDENCE | unchanged | unchanged |
| REJECTS | unchanged | unchanged (triage counts now 4/9/27 frozen in the claim) |
| GROUND | gap-sweep receipt + fragment absence at base | + `ground.sweeps[]`: before absent at base UNCONDITIONALLY over the declared scope; after present in >=1 landed knowledge entry ONLY when the gating candidate is admitted; receipt graded only when declared |
| CITEDLINES / CENSUS / SCRATCHMIRROR / COLLCHECK | unchanged | unchanged, except COLLCHECK accepts the round-76 map's `staged_url_cell_urls` / `normalized_document_url` as well as round 75's `url` |
| FROZENCFG | compares the frozen constants | + candidates/admitted flags, `min_admitted`, `rows_before`, `knowledge_before`, `ground.sweeps`, `ground.receipt`, `requoted`, admitted-count-vs-floor |
| INDEX | myth-symbol rows, frozen vector `32/32/40/29/24/95` | partition derived from the admitted entry paths; EVERY partition heading graded against its live .md count; the footer vector graded against the LIVE per-partition counts (a frozen vector cannot follow n); total == live total |

## 4. Refusals (exit 2, FAIL printed) added by the loader

- `candidates` absent/not a list, a non-object item, a repeated or non-relative path;
- `admitted` missing or not boolean;
- `min_admitted` not an integer >= 1, or the frozen admitted count below it;
- `entries[]` present but not exactly the admitted subset;
- `rows_before` / `knowledge_before` absent or not positive integers;
- `ground.sweeps` empty, a pattern that does not compile as an `-E`
  expression, a gating candidate that is not a frozen candidate, a
  non-relative scope;
- `ground.receipt` non-relative;
- a `requoted` record without two S-ids.

## 5. Draft findings (frozen text vs measured base)

1. **The draft's before-command scope is wrong.** The draft says
   `git grep -l -E 'GB/T 33661' 98c486b -- corpus` and the
   `digital\.archives\.go\.jp` twin "each print nothing (exit 1)". Measured:
   both DO match at base — `GB/T 33661` in `corpus/lessons/round-68.md` and
   `corpus/lessons/round-69.md`, `digital\.archives\.go\.jp` in
   `corpus/lessons/round-68.md`. Scoped to `corpus/knowledge` both print
   nothing (exit 1). The draft claim therefore freezes
   `scope = "corpus/knowledge"`; the before/after sentence must say so.
2. **The by-document map carries no `url` field.** The round-76 map
   (`assimilation/id-renumber-map.json`) stores `normalized_document_url` +
   `staged_url_cell_urls`; round 75's COLLCHECK expected `url`. The counter
   now reads both, and `staged_url_cell_urls[0]` (a full URL) wins over the
   scheme-less normalized form.
3. **`map.sha256` is pinned to the current staged bytes**
   (`13372a06…e70130fc`). If `ScoutIdMap` rewrites the map, the L1 must
   re-pin at the freeze and commit exactly those bytes at `map.path`.

## 6. Selftest

`python3 -B accept-c.py --selftest` -> `SELFTEST: 94/94` (receipt
`selftest-receipt.txt` in this directory). 94 cases: the positive fixture
(PASS 13/13), the two do-nothing controls, the two missing-argument errors, a
no-data landing, the mutant-table coverage case, and 87 mutants — at least one
per leg (87 over 13/13 legs), and at least one per
NEW limb: `candidate_refused_written`, `candidate_extra_admitted`,
`row_duplicate_document`, `row_document_at_base`, `tier_c_only_support`,
`requote_uncited`, `ground_before_present`, `ground_after_missing`,
`index_heading_other`.
