# CtlCCopiedRows — round 61 wave 1 pre-data controls

## Result

**Item 1: CONTROL-MET.** Copied S623 material with `?ref=x` or a changed `#fragment` passes every frozen leg when repeated under twenty new ids S652–S671. Both twenty-row mutants printed `ACCEPT-C-61: PASS`, exit 0. The one-row versions also pass the permitted FLOOR-only probe.

**Item 2: NONE-MET.** OPENED rejects 2026-10-22; STATUS rejects queued; USEDBY rejects another entry and longer paths containing ENTRY; RANGE rejects split rows of 14 or 12 cells and duplicate S652 ids. Every metadata mutant failed the expected leg under both counters.

FRESH misses three requested spellings: query, fragment, and `m.` host. The mobile-host fixture does **not** pass end-to-end: LOCATE fails. Plain URL reuse, HTTP/HTTPS, `www.` normalization, and a Wayback-wrapper spelling are caught by FRESH.

No counter, lane source, or integration contract was changed. These are detector-coverage findings, not an admission judgment.

## Axes and scope

- Primary axis: coverage of copied-row and stale-row controls.
- Supporting axes: detector discrimination, exact restoration/no harm, bounded execution.
- Isolated clone: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- Revision: `78ad4b176695e9fcd490ab607cb8218e2ce62738`.
- Claims were read before setup or scoring. Only the assigned C controls were exercised; no delegation, background jobs, git/jj writes in the lane, tool installs, PDF helpers, headless access, or access-control bypasses were used.
- Fixtures used ordinary live GETs through the frozen locator. No detector output was mocked or patched. At most four fixture workers ran concurrently; every detector process had a 180-second timeout and process-group cleanup.

## Frozen counter and allowed probe

- Frozen SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- One-row probe SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- Only `FLOOR = 20` becomes `FLOOR = 1`; TOTAL and the base list remain unchanged.
- Probe file: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py`.

```diff
--- frozen/accept-c.py
+++ probe-floor-1.py
@@ -54,7 +54,7 @@
 TOTAL = 236
 FIRST_SID = 652
 LAST_SID = 699
-FLOOR = 20
+FLOOR = 1
 LOCATOR = "reports/round-61/reopen-quote.py"
 SHARE = 1.0
 OPENED = "2026-10-23"
```

The twenty-row FLOOR-to-fixture-size probe is byte-identical to the frozen counter (`FLOOR` is already 20): empty diff, SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`. Its separately recorded second run is labeled `probe`; no other constant was changed.

## Fixture construction and interpretation

- Original rows S623 and S650 already name `https://footwearresearchnetwork.org/articles/concealed-shoes-revealed` below S652. Exact-copy cases renumber a row to S652 and set mined, opened 2026-10-23, and the exact entry used-by item. URL-variant cases retain S623’s anchor and use a short, non-verbatim bullet with shared quote words.
- S650’s inherited anchor lacks a footwear word, and its copy also fails TOPIC and LINK. It is included as requested, not presented as an isolated TOPIC-positive FRESH escape.
- The existing source URL already lacks `www.`. Consequently `www-dropped` is byte-identical to the exact canonical case; the additional `www-added` case checks the opposite equivalent spelling.
- The Wayback test rewrites the source URL to the syntactically valid `https://web.archive.org/web/20260608000000id_/https://footwearresearchnetwork.org/articles/concealed-shoes-revealed`. It is a constructed wrapper test, not a claim that this timestamp is an available capture; LOCATE failed.
- Metadata fixtures keep an otherwise mechanically passing row with the nine-word body anchor `shoes are always highly worn, often patched and repaired` and the bullet `The shoes are described as worn and repaired, with patches.`. Each changes only the named cell/shape/id multiplicity. Their pristine source URL has `#fragment`, deliberately using the observed FRESH escape to isolate metadata guards; this baseline is not represented as newly researched material.
- Cell counts follow the frozen parser: `line.split("|")` normally has 13 cells, including the two empty boundary cells (11 logical table cells). The malformed cases have split lengths 14 and 12, respectively.
- Twenty-row confirmations repeat the same copied S623 nine-word anchor and paraphrase under ids S652–S671, with the same query or fragment URL in each new source cell. They add no new source research. The two twenty-row specimens satisfy the frozen numerical floor without changing it.
- Every fixture has exactly the added ENTRY and a matching README index/count/footer. Existing knowledge files, reports and tools are read-only symlinks into this seat’s pristine clone. Only fixture SOURCES bytes change during each mutation.
- One-row frozen pristine baselines fail FLOOR. Thus those frozen mutation comparisons are **inconclusive as whole-predicate kill tests**; they are never counted as frozen kills. Their FLOOR=1 pristine and restored probes pass, permitting conditional probe kills/survivals. The twenty-row pristine and restored baselines pass frozen and probe.
- A FRESH miss for `m.` is syntactic only: the locator failed to locate that host. No working mobile alias or full-predicate escape is claimed.

## Case receipts and verdicts

`stopped-by` below lists all failing frozen legs. Probe exit codes and full individual outputs are included in the appendix.

```text
RECEIPT CtlCCopiedRows/copy-S650-exact counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,TOPIC,LINK,FRESH
RECEIPT CtlCCopiedRows/copy-S623-exact counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,FRESH
RECEIPT CtlCCopiedRows/copy-S623-wayback counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LOCATE,FRESH
RECEIPT CtlCCopiedRows/copy-S623-http counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,FRESH
RECEIPT CtlCCopiedRows/copy-S623-www-added counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,FRESH
RECEIPT CtlCCopiedRows/copy-S623-www-dropped counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,FRESH
RECEIPT CtlCCopiedRows/copy-S623-query counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR
RECEIPT CtlCCopiedRows/copy-S623-fragment counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR
RECEIPT CtlCCopiedRows/copy-S623-mobile counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LOCATE
RECEIPT CtlCCopiedRows/opened-yesterday counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,OPENED
RECEIPT CtlCCopiedRows/status-queued counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,STATUS
RECEIPT CtlCCopiedRows/usedby-other-entry counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,USEDBY
RECEIPT CtlCCopiedRows/usedby-longer-suffix counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,USEDBY
RECEIPT CtlCCopiedRows/usedby-longer-prefix counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,USEDBY
RECEIPT CtlCCopiedRows/cells-14 counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,RANGE,ACCESS,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCCopiedRows/cells-12 counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,RANGE,ACCESS,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCCopiedRows/duplicate-row-id counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,RANGE,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCCopiedRows/copy-S623-query-full20 counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=PASS stopped-by=none
RECEIPT CtlCCopiedRows/copy-S623-fragment-full20 counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=PASS stopped-by=none
```

| Case | Expected detector | Measured target / mutation verdict | Control |
|---|---|---|---|
| copy-S650-exact | FRESH FAIL | FAIL; killed by FRESH under FLOOR=1 probe; frozen comparison inconclusive | NONE-MET |
| copy-S623-exact | FRESH FAIL | FAIL; killed by FRESH under FLOOR=1 probe; frozen comparison inconclusive | NONE-MET |
| copy-S623-wayback | FRESH FAIL | FAIL; killed by FRESH under FLOOR=1 probe; frozen comparison inconclusive | NONE-MET |
| copy-S623-http | FRESH FAIL | FAIL; killed by FRESH under FLOOR=1 probe; frozen comparison inconclusive | NONE-MET |
| copy-S623-www-added | FRESH FAIL | FAIL; killed by FRESH under FLOOR=1 probe; frozen comparison inconclusive | NONE-MET |
| copy-S623-www-dropped | FRESH FAIL | FAIL; killed by FRESH under FLOOR=1 probe; frozen comparison inconclusive | NONE-MET |
| copy-S623-query | FRESH FAIL | PASS; survived FLOOR=1 probe; frozen comparison inconclusive | CONTROL-MET |
| copy-S623-fragment | FRESH FAIL | PASS; survived FLOOR=1 probe; frozen comparison inconclusive | CONTROL-MET |
| copy-S623-mobile | FRESH FAIL | PASS; FRESH survived; probe killed by LOCATE; frozen comparison inconclusive | NONE-MET |
| opened-yesterday | OPENED FAIL | FAIL; killed by OPENED under FLOOR=1 probe; frozen comparison inconclusive | NONE-MET |
| status-queued | STATUS FAIL | FAIL; killed by STATUS under FLOOR=1 probe; frozen comparison inconclusive | NONE-MET |
| usedby-other-entry | USEDBY FAIL | FAIL; killed by USEDBY under FLOOR=1 probe; frozen comparison inconclusive | NONE-MET |
| usedby-longer-suffix | USEDBY FAIL | FAIL; killed by USEDBY under FLOOR=1 probe; frozen comparison inconclusive | NONE-MET |
| usedby-longer-prefix | USEDBY FAIL | FAIL; killed by USEDBY under FLOOR=1 probe; frozen comparison inconclusive | NONE-MET |
| cells-14 | RANGE FAIL | FAIL; killed by RANGE under FLOOR=1 probe; frozen comparison inconclusive | NONE-MET |
| cells-12 | RANGE FAIL | FAIL; killed by RANGE under FLOOR=1 probe; frozen comparison inconclusive | NONE-MET |
| duplicate-row-id | RANGE FAIL | FAIL; killed by RANGE under FLOOR=1 probe; frozen comparison inconclusive | NONE-MET |
| copy-S623-query-full20 | FRESH FAIL | PASS; survived frozen + probe | CONTROL-MET |
| copy-S623-fragment-full20 | FRESH FAIL | PASS; survived frozen + probe | CONTROL-MET |

```text
CONTROL-MET item-1-copied-rows fixtures=/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/snapshots/copy-S623-query-full20-mutated-SOURCES.md,/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/snapshots/copy-S623-fragment-full20-mutated-SOURCES.md frozen=PASS exit=0 (also query/fragment one-row FLOOR=1 probes PASS)
NONE-MET item-2-stale-and-malformed-rows fixtures=/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/opened-yesterday,/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/status-queued,/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/usedby-other-entry,/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/usedby-longer-suffix,/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/usedby-longer-prefix,/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/cells-14,/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/cells-12,/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/duplicate-row-id
```

## Exact restoration evidence

All 19 mutated fixture registries were restored byte-for-byte in `finally` blocks; every restored FLOOR probe passed. The twenty-row restorations also passed the frozen counter. The shared pristine baselines are content-addressed and reused only where their before hashes match the case. Each case’s original and mutated registry snapshots are retained below the scratch `snapshots/` directory; fixture roots named below are currently restored. Replay the retained mutated SOURCES snapshot with the corresponding unchanged entry and README to reproduce a mutant.

| Case | Before SHA-256 | Mutated SHA-256 | Restored SHA-256 |
|---|---|---|---|
| copy-S650-exact | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` | `bd1fb42fe72603b402c9d9097475d5666aad092ae469ad56624390fbaedff2e6` | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` |
| copy-S623-exact | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` | `d30ba6c87311610241ce5aac8f9ba20039ab747d568ad8a27ea90b10d02cbee2` | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` |
| copy-S623-wayback | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` | `8a69bf52d864cf55264660587ab68a16b38e51b3c7b30d2be8a1aeaaccb90899` | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` |
| copy-S623-http | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` | `f4e938fb3bfe27caf54bc53e3dcbc870fcf556ffb0cb4c13d916710542081868` | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` |
| copy-S623-www-added | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` | `36787414ab31ef555903722bf29d07b340bed21189ca1e6163a63f17174e1e5a` | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` |
| copy-S623-www-dropped | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` | `d30ba6c87311610241ce5aac8f9ba20039ab747d568ad8a27ea90b10d02cbee2` | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` |
| copy-S623-query | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` | `901e44f1f073a749c86899da5bfb30fa7332d5268730f136708fe215ffbf95d0` | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` |
| copy-S623-fragment | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` | `3e077bd0fdbec36fc1c205b2d166568365a51475fef9381cdb07012a09a0e4e8` | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` |
| copy-S623-mobile | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` | `8db9467cc08c1bc7e83d1dc6d2fd16d97f4d70398d7bde13008d9000af82e811` | `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6` |
| opened-yesterday | `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a` | `4d2ef038733e2cfb0313ebf9487426b608eeb2b1c287e48dbe5d690d4efc69f6` | `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a` |
| status-queued | `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a` | `f5edf3f06ef25c2c5033ce15f907a2967cee7381f609bd0868558aef6f6f3684` | `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a` |
| usedby-other-entry | `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a` | `6ada3cc770faf9b51386b1c2cda80954081a537abd25b6093cfded9dba248b24` | `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a` |
| usedby-longer-suffix | `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a` | `dfa1dd9384b90f64e65abccd16d2da06b398a4efb4de764917db62b2a1040b15` | `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a` |
| usedby-longer-prefix | `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a` | `ddc98bd3c50228fec8a6a30744f9104802d241d6226ca2d292b1c9adfeb5e452` | `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a` |
| cells-14 | `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a` | `008a7e4e20ee8577735809f57882747c870d5a035f66e7c9b64f985a4f537ed7` | `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a` |
| cells-12 | `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a` | `51e4ae34c37b421e935b0def569059f47c47f26aeade45755265bbca3e8f9450` | `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a` |
| duplicate-row-id | `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a` | `6db2f761adbc97f7c7e28969a3f548b25dc47c0bc6f08ba6ec39493227bac66c` | `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a` |
| copy-S623-query-full20 | `551f59ad09e27a7762cd1a094bca971d53faab920084900ab0e216827ebe6291` | `00a6285dcecb1f32785a92dbc8620570f29bcc65b48371ed1101c5815bbd0cce` | `551f59ad09e27a7762cd1a094bca971d53faab920084900ab0e216827ebe6291` |
| copy-S623-fragment-full20 | `551f59ad09e27a7762cd1a094bca971d53faab920084900ab0e216827ebe6291` | `ad7c98ede743f4cf41a19deb9a58762139114e8514d8a2b9c982770c432d5e6b` | `551f59ad09e27a7762cd1a094bca971d53faab920084900ab0e216827ebe6291` |

- Clone SOURCES before/after: `641115af3777359d9b42cce28a249f7ce6807df601e543b4f5a867c74d7af485` / `641115af3777359d9b42cce28a249f7ce6807df601e543b4f5a867c74d7af485`.
- Clone README before/after: `a7fc403cf0f2908581926515d70c5b358afb504ac132bde3e1a0987e5870352c` / `a7fc403cf0f2908581926515d70c5b358afb504ac132bde3e1a0987e5870352c`.
- Frozen counter before/after: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10` / `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- Both harnesses report `PROCESS_GROUPS_REMAINING []`; every started detector group was killed/cleaned after capture. No process remains running from this assignment.
- Maximum retained non-clone artifact observed: 796800 bytes, below the 5 MB write cap. No tools were installed or updated.

## Artifact paths

- Main data and per-run captures: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/evidence.json`, `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/results.json`, `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/results/`.
- Twenty-row data: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/full-floor-evidence.json`, `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/full-floor-runs.json`.
- Generated data fixtures/restored roots: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/<case>/`.
- Exact original/mutant registry snapshots: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/snapshots/<case>-{pristine,mutated}-SOURCES.md`.
- Bounded harnesses: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/run-controls.py`, `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/run-full-floor.py`.
- No files other than this requested report were written in the lane or fleet repository.

## Full counter stdout and exits — every run

The following is the complete captured stdout of all 82 detector executions, including pristine, mutated and restored runs. Each run names its exact counter hash, argv, cwd, source hash and exit. Counter stderr was empty unless explicitly included. Parent counter output is preserved exactly, including any detail shortening performed internally by the counter itself.

### Run 1: copied-pristine / pristine / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copied-pristine`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 2: copied-pristine / pristine / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copied-pristine`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 3: metadata-pristine / pristine / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/metadata-pristine`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 4: metadata-pristine / pristine / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/metadata-pristine`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 5: full20-pristine / pristine / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `551f59ad09e27a7762cd1a094bca971d53faab920084900ab0e216827ebe6291`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/full20-pristine`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:48Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 6: full20-pristine / pristine / probe

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `551f59ad09e27a7762cd1a094bca971d53faab920084900ab0e216827ebe6291`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/full20-pristine`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:48Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 7: copy-S650-exact / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `bd1fb42fe72603b402c9d9097475d5666aad092ae469ad56624390fbaedff2e6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S650-exact`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC FAIL rows=1 bad=['S652']
LINK FAIL min=3 bad=['6:1']
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH FAIL rows_reusing_registry_urls=['S652']
ACCEPT-C-61: FAIL
exit=1
```

### Run 8: copy-S650-exact / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `bd1fb42fe72603b402c9d9097475d5666aad092ae469ad56624390fbaedff2e6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S650-exact`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC FAIL rows=1 bad=['S652']
LINK FAIL min=3 bad=['6:1']
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH FAIL rows_reusing_registry_urls=['S652']
ACCEPT-C-61: FAIL
exit=1
```

### Run 9: copy-S650-exact / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S650-exact`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 10: copy-S650-exact / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S650-exact`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 11: copy-S623-exact / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `d30ba6c87311610241ce5aac8f9ba20039ab747d568ad8a27ea90b10d02cbee2`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-exact`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH FAIL rows_reusing_registry_urls=['S652']
ACCEPT-C-61: FAIL
exit=1
```

### Run 12: copy-S623-exact / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `d30ba6c87311610241ce5aac8f9ba20039ab747d568ad8a27ea90b10d02cbee2`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-exact`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH FAIL rows_reusing_registry_urls=['S652']
ACCEPT-C-61: FAIL
exit=1
```

### Run 13: copy-S623-exact / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-exact`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 14: copy-S623-exact / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-exact`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 15: copy-S623-wayback / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `8a69bf52d864cf55264660587ab68a16b38e51b3c7b30d2be8a1aeaaccb90899`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-wayback`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://web.archive.org/web/20260608000000id_/https://footwearresearchnetwork.org/articles/concealed-shoes-revealed HTTPError']
FRESH FAIL rows_reusing_registry_urls=['S652']
ACCEPT-C-61: FAIL
exit=1
```

### Run 16: copy-S623-wayback / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `8a69bf52d864cf55264660587ab68a16b38e51b3c7b30d2be8a1aeaaccb90899`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-wayback`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://web.archive.org/web/20260608000000id_/https://footwearresearchnetwork.org/articles/concealed-shoes-revealed HTTPError']
FRESH FAIL rows_reusing_registry_urls=['S652']
ACCEPT-C-61: FAIL
exit=1
```

### Run 17: copy-S623-wayback / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-wayback`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 18: copy-S623-wayback / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-wayback`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 19: copy-S623-http / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `f4e938fb3bfe27caf54bc53e3dcbc870fcf556ffb0cb4c13d916710542081868`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-http`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH FAIL rows_reusing_registry_urls=['S652']
ACCEPT-C-61: FAIL
exit=1
```

### Run 20: copy-S623-http / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `f4e938fb3bfe27caf54bc53e3dcbc870fcf556ffb0cb4c13d916710542081868`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-http`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH FAIL rows_reusing_registry_urls=['S652']
ACCEPT-C-61: FAIL
exit=1
```

### Run 21: copy-S623-http / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-http`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 22: copy-S623-http / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-http`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 23: copy-S623-www-added / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `36787414ab31ef555903722bf29d07b340bed21189ca1e6163a63f17174e1e5a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-www-added`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH FAIL rows_reusing_registry_urls=['S652']
ACCEPT-C-61: FAIL
exit=1
```

### Run 24: copy-S623-www-added / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `36787414ab31ef555903722bf29d07b340bed21189ca1e6163a63f17174e1e5a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-www-added`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH FAIL rows_reusing_registry_urls=['S652']
ACCEPT-C-61: FAIL
exit=1
```

### Run 25: copy-S623-www-added / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-www-added`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 26: copy-S623-www-added / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-www-added`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 27: copy-S623-www-dropped / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `d30ba6c87311610241ce5aac8f9ba20039ab747d568ad8a27ea90b10d02cbee2`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-www-dropped`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH FAIL rows_reusing_registry_urls=['S652']
ACCEPT-C-61: FAIL
exit=1
```

### Run 28: copy-S623-www-dropped / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `d30ba6c87311610241ce5aac8f9ba20039ab747d568ad8a27ea90b10d02cbee2`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-www-dropped`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH FAIL rows_reusing_registry_urls=['S652']
ACCEPT-C-61: FAIL
exit=1
```

### Run 29: copy-S623-www-dropped / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-www-dropped`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 30: copy-S623-www-dropped / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-www-dropped`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 31: copy-S623-query / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `901e44f1f073a749c86899da5bfb30fa7332d5268730f136708fe215ffbf95d0`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-query`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 32: copy-S623-query / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `901e44f1f073a749c86899da5bfb30fa7332d5268730f136708fe215ffbf95d0`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-query`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 33: copy-S623-query / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-query`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 34: copy-S623-query / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-query`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 35: copy-S623-fragment / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `3e077bd0fdbec36fc1c205b2d166568365a51475fef9381cdb07012a09a0e4e8`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-fragment`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 36: copy-S623-fragment / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `3e077bd0fdbec36fc1c205b2d166568365a51475fef9381cdb07012a09a0e4e8`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-fragment`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 37: copy-S623-fragment / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-fragment`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 38: copy-S623-fragment / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-fragment`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 39: copy-S623-mobile / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `8db9467cc08c1bc7e83d1dc6d2fd16d97f4d70398d7bde13008d9000af82e811`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-mobile`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://m.footwearresearchnetwork.org/articles/concealed-shoes-revealed URLError']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 40: copy-S623-mobile / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `8db9467cc08c1bc7e83d1dc6d2fd16d97f4d70398d7bde13008d9000af82e811`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-mobile`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://m.footwearresearchnetwork.org/articles/concealed-shoes-revealed URLError']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 41: copy-S623-mobile / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-mobile`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 42: copy-S623-mobile / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `04f7cd1436f817bf868ccf8da507eba502c8eb2392ae42cdfda96384fc112ba6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-mobile`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 43: opened-yesterday / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `4d2ef038733e2cfb0313ebf9487426b608eeb2b1c287e48dbe5d690d4efc69f6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/opened-yesterday`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED FAIL bad=['S652:2026-10-22']
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 44: opened-yesterday / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `4d2ef038733e2cfb0313ebf9487426b608eeb2b1c287e48dbe5d690d4efc69f6`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/opened-yesterday`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED FAIL bad=['S652:2026-10-22']
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 45: opened-yesterday / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/opened-yesterday`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 46: opened-yesterday / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/opened-yesterday`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 47: status-queued / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `f5edf3f06ef25c2c5033ce15f907a2967cee7381f609bd0868558aef6f6f3684`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/status-queued`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS FAIL bad=['S652:queued']
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 48: status-queued / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `f5edf3f06ef25c2c5033ce15f907a2967cee7381f609bd0868558aef6f6f3684`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/status-queued`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS FAIL bad=['S652:queued']
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 49: status-queued / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/status-queued`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 50: status-queued / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/status-queued`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 51: usedby-other-entry / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `6ada3cc770faf9b51386b1c2cda80954081a537abd25b6093cfded9dba248b24`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/usedby-other-entry`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY FAIL bad=['S652']
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 52: usedby-other-entry / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `6ada3cc770faf9b51386b1c2cda80954081a537abd25b6093cfded9dba248b24`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/usedby-other-entry`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY FAIL bad=['S652']
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 53: usedby-other-entry / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/usedby-other-entry`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 54: usedby-other-entry / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/usedby-other-entry`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 55: usedby-longer-suffix / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `dfa1dd9384b90f64e65abccd16d2da06b398a4efb4de764917db62b2a1040b15`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/usedby-longer-suffix`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY FAIL bad=['S652']
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 56: usedby-longer-suffix / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `dfa1dd9384b90f64e65abccd16d2da06b398a4efb4de764917db62b2a1040b15`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/usedby-longer-suffix`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY FAIL bad=['S652']
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 57: usedby-longer-suffix / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/usedby-longer-suffix`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 58: usedby-longer-suffix / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/usedby-longer-suffix`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 59: usedby-longer-prefix / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `ddc98bd3c50228fec8a6a30744f9104802d241d6226ca2d292b1c9adfeb5e452`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/usedby-longer-prefix`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY FAIL bad=['S652']
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 60: usedby-longer-prefix / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `ddc98bd3c50228fec8a6a30744f9104802d241d6226ca2d292b1c9adfeb5e452`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/usedby-longer-prefix`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY FAIL bad=['S652']
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 61: usedby-longer-prefix / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/usedby-longer-prefix`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 62: usedby-longer-prefix / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/usedby-longer-prefix`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 63: cells-14 / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `008a7e4e20ee8577735809f57882747c870d5a035f66e7c9b64f985a4f537ed7`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/cells-14`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE FAIL bad=['S652'] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS FAIL exit=2 ?
LINES PASS cited_lines=1 bad=[]
TOPIC FAIL rows=0 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 64: cells-14 / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `008a7e4e20ee8577735809f57882747c870d5a035f66e7c9b64f985a4f537ed7`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/cells-14`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE FAIL bad=['S652'] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS FAIL exit=2 ?
LINES PASS cited_lines=1 bad=[]
TOPIC FAIL rows=0 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 65: cells-14 / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/cells-14`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 66: cells-14 / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/cells-14`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 67: cells-12 / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `51e4ae34c37b421e935b0def569059f47c47f26aeade45755265bbca3e8f9450`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/cells-12`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE FAIL bad=['S652'] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS FAIL exit=2 ?
LINES PASS cited_lines=1 bad=[]
TOPIC FAIL rows=0 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 68: cells-12 / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `51e4ae34c37b421e935b0def569059f47c47f26aeade45755265bbca3e8f9450`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/cells-12`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE FAIL bad=['S652'] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS FAIL exit=2 ?
LINES PASS cited_lines=1 bad=[]
TOPIC FAIL rows=0 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 69: cells-12 / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/cells-12`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 70: cells-12 / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/cells-12`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 71: duplicate-row-id / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `6db2f761adbc97f7c7e28969a3f548b25dc47c0bc6f08ba6ec39493227bac66c`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/duplicate-row-id`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE FAIL bad=['S652'] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC FAIL rows=0 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 72: duplicate-row-id / mutated / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `6db2f761adbc97f7c7e28969a3f548b25dc47c0bc6f08ba6ec39493227bac66c`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/duplicate-row-id`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE FAIL bad=['S652'] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC FAIL rows=0 bad=[]
LINK FAIL min=3 bad=['6:no-row']
COPY FAIL max=12 bad=['6:no-row']
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 73: duplicate-row-id / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/duplicate-row-id`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Run 74: duplicate-row-id / restored / probe

- Counter SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`.
- SOURCES SHA-256: `6a703f7dda5481dbd609be933405e61e829a69fe63d02e0acfbda09b18d8127a`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/probe-floor-1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/duplicate-row-id`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 75: copy-S623-query-full20 / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `00a6285dcecb1f32785a92dbc8620570f29bcc65b48371ed1101c5815bbd0cce`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-query-full20`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:48Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 76: copy-S623-query-full20 / mutated / probe

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `00a6285dcecb1f32785a92dbc8620570f29bcc65b48371ed1101c5815bbd0cce`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-query-full20`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:48Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 77: copy-S623-query-full20 / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `551f59ad09e27a7762cd1a094bca971d53faab920084900ab0e216827ebe6291`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-query-full20`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:48Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 78: copy-S623-query-full20 / restored / probe

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `551f59ad09e27a7762cd1a094bca971d53faab920084900ab0e216827ebe6291`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-query-full20`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:48Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 79: copy-S623-fragment-full20 / mutated / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `ad7c98ede743f4cf41a19deb9a58762139114e8514d8a2b9c982770c432d5e6b`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-fragment-full20`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:48Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 80: copy-S623-fragment-full20 / mutated / probe

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `ad7c98ede743f4cf41a19deb9a58762139114e8514d8a2b9c982770c432d5e6b`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-fragment-full20`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:48Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 81: copy-S623-fragment-full20 / restored / frozen

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `551f59ad09e27a7762cd1a094bca971d53faab920084900ab0e216827ebe6291`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-fragment-full20`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:48Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Run 82: copy-S623-fragment-full20 / restored / probe

- Counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- SOURCES SHA-256: `551f59ad09e27a7762cd1a094bca971d53faab920084900ab0e216827ebe6291`.
- cwd: `/fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone`.
- argv: `timeout --kill-after=5 180 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCCopiedRows/fixtures/copy-S623-fragment-full20`.

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=20 bad=[]
TOPIC PASS rows=20 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=20 cited=20 need=20 at=2026-10-23T09:48Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

