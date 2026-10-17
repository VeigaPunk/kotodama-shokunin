# M11 — metadata audit: `corpus/knowledge/verification/` (all 13 entries)

- Round 8 metadata sweep, shard M11 (assignment: `corpus/knowledge/verification/`, all 13 entries; fragment path `reports/round-8/metadata/m11-verification.md`).
- Protocol source: `reports/round-8/targets.json` field `metadata_sweep` — "audit corpus/knowledge/\* frontmatter (source/verified-at/recheck) … Fixes applied in place on own-lane files only; per-file fragment under reports/round-8/metadata/."
- Date: 2026-10-17 (all commands run 2026-10-17, ≈17:10–20:30 UTC; the locator sweep ran ≈17:15–17:20 UTC).
- Baseline revision: `e7ca0fa` (round-8 `baseline_revision`); worktree HEAD `cf338a7` ("round-8: declare claims F/O/D + operator regimen bookkeeping"); `git diff HEAD -- corpus/` is empty for the pre-edit tree, so `git show HEAD:<file>` is the valid before-state. Pre-edit digests equal the `reports/supplement-opencode-1/inventory-after.json` records (spot-checked for all 13; full list below).
- Contract audited: fleet `CORPUS.md:17` — "Each `knowledge/` entry opens with `source:`, `verified-at:` and `recheck:`" (quoted in `reports/supplement-opencode-1/28-corpus-contract.md` §1). Lane gate `tools/gates/provenance-audit.py` reads only `topic|sources|couples` (`FIELD_NAMES`, line 72) and does not test the metadata trio, so the added fields are gate-neutral. **Source leg:** the existing `- sources:` header field (bibliography or pointer to the entry's bibliography section) is the source metadata; it is present in all 13. No separate `- source:` pointer line was added — same reading as shard M07 (`m07-synth-13-24.md` §Protocol). The fleet-text question is already filed with the integrator in `28-corpus-contract.md` §6.2 and is not decided here.
- Write scope: the 13 entry files listed below plus this fragment. No sibling repo, fleet file, frozen artifact, or other shard's report was touched; no commit made.

## Protocol applied

Per file, audited in this order:

1. header-block presence of `- topic:` / `- sources:` / `- couples:` (the provenance-audit gate fields);
2. the metadata trio `source` / `verified-at` / `recheck` — presence, location (header block vs in-body), and whether the value can cite a check this pass actually performed;
3. cross-reference resolution of every `couples:` path (brace expansion; exact path first, then basename across `corpus/knowledge/**/*.md`);
4. **fresh linked-locator reachability sweep** — every `http(s)` locator in the entry re-requested on 2026-10-17 (see §3); this is the check the new `verified-at:` values cite;
5. fixes applied in place; `tools/gates/provenance-audit.py` re-run before/after; frozen-baseline pin re-checked.

Fix shape (shard-standard, matching M01–M09): two header bullets `- verified-at: …` and `- recheck: …` inserted **directly after the `- couples:` line**; for `gate-frozen-run-standard.md`, which already carries `- verified-at:` at the end of its header block, only `- recheck:` was added there. No date, source, or scope was invented: each `verified-at:` states exactly what this pass checked (header fields, cross-reference resolution, locator reachability) and what it did not (the cited works themselves). Nothing else was edited except one verified locator repair (§3, calibration-registry).

## Evidence (commands + outputs)

### 1. Field presence before → after

Command: `for f in corpus/knowledge/verification/*.md; do grep -c '^- verified-at:' $f; grep -c '^- recheck:' $f; done` (anchored, line-start; 2026-10-17).

| state | files with `- verified-at:` | files with `- recheck:` |
|---|---|---|
| before (HEAD) | 4 / 13 (`citation-format-and-source-registry`, `gate-frozen-run-standard`, `myth-consistency-gate`, `provenance-audit-ledger-format`) | 3 / 13 (same set minus `gate-frozen-run-standard`) |
| after (worktree) | **13 / 13** | **13 / 13** |

Case variant found and handled: `real-world-inspiration-boundaries.md:15` carried `- Verified-at:` (capital V) with the recheck trigger embedded in the same sentence; the line is retained **verbatim** (prior-text preservation) and the operative fields were added to the header. `naming-collision-gate.md` carried only a §1 prose line ("Verification date: 2026-10-17.") — prose is not a field; header fields added.

### 2. Cross-reference audit (negative claim; sweep named)

Sweep: Python brace-expanded resolver over each `- couples:` value (2026-10-17). Tokens `[\w./-]+\.md` after `{a,b}.md` expansion; resolved exactly against the entry's directory and against `corpus/knowledge/`, then by basename across `corpus/knowledge/**/*.md`.

Result: **137 concrete targets checked, 0 missing** — 127 path refs (calibration 12 · citation-format 9 · costume 17 · gate-frozen 4 · lexicon 16 · myth 14 · naming 12 · phonology 11 · provenance 8 · real-world 13 · to-verify 11) plus 10 extension-less entry names in `verification-method-overview.md` (all resolve: historical-linguistics, naming-systems, writing-systems, comparative-frameworks, symbolism-synthesis-method, color-symbolism, era-periodization-models, textile-technology, costume-semiotics, material-culture-inference-method). Non-concrete by design, not counted: `gate-frozen-run-standard.md` names a `*-gate.md` glob; `internal-consistency-audit.md` names three directories (`../linguistics/`, `../myth-symbol/`, `../culture-material/`) — all exist.

### 3. Linked-locator reachability sweep (the fresh check the new fields cite)

Command (2026-10-17): per-file unique `https?://` locators, trailing sentence punctuation stripped, each requested once with

```
curl -sS -o /dev/null -w '%{http_code}' -L --max-time 25 -A 'Mozilla/5.0 (X11; Linux x86_64)' <url>
```

**109 file–URL pairs (104 unique URLs); 82 reachable (200/202/203), 24 blocked by remote servers (403/429/405), 2 unreachable from this environment (connection timeout), 1 broken (404).**

Per-file counts:

| file | locators | reachable | blocked | unreachable | broken |
|---|---|---|---|---|---|
| calibration-registry.md | 8 | 4 | 3 | 0 | 1 |
| citation-format-and-source-registry.md | 7 | 7 | 0 | 0 | 0 |
| costume-era-consistency-gate.md | 10 | 7 | 2 | 1 | 0 |
| gate-frozen-run-standard.md | 5 | 5 | 0 | 0 | 0 |
| internal-consistency-audit.md | 13 | 11 | 2 | 0 | 0 |
| lexicon-coverage-audit.md | 6 | 5 | 1 | 0 | 0 |
| myth-consistency-gate.md | 15 | 8 | 6 | 1 | 0 |
| naming-collision-gate.md | 8 | 5 | 3 | 0 | 0 |
| phonology-sanity-gate.md | 14 | 10 | 4 | 0 | 0 |
| provenance-audit-ledger-format.md | 4 | 4 | 0 | 0 | 0 |
| real-world-inspiration-boundaries.md | 9 | 8 | 1 | 0 | 0 |
| to-verify-triage-protocol.md | 7 | 6 | 1 | 0 | 0 |
| verification-method-overview.md | 3 | 2 | 1 | 0 | 0 |

Non-2xx rows (27) with status: calibration — `10.1017/S0003598X00064310` 429, `10.1086/200264` 403, Cambridge Antiquity issue page 429, `10.1163/9789084513837` **404**; costume — `cameo.mfa.org/wiki/Spun_silk` 403, `britannica.com/technology/spun-silk-yarn` 403, `library.lincoln.ac.uk/items/202188` timeout; internal-consistency — `10.1093/notesj/gjad106` 403, `10.1136/bmj.b2680` 403; lexicon — `10.1075/ijcl.13.4.02gri` 403; myth — `brill.com/display/title/20123` 403, `10.1017/S0075426925100281` 429, Amherst PDF 405, Cambridge JHS article 429, Cornell UP book page 403, Met essay 429, `limc-france.fr` timeout; naming — `10.1017/9780511807954` 429, `10.1093/oxfordhb/9780199656431.001.0001` 403, `10.1145/321796.321811` 403; phonology — `10.1051/aacus/2022044` 403, `10.1073/pnas.1417413112` 403, `10.1121/10.0002279` 403, `10.1126/science.aav3218` 403; real-world — `10.1111/j.1468-2885.2006.00277.x` 403; to-verify — `10.1037/0022-0663.83.1.73` 403; verification-method — Cambridge *Uses of Argument* page 429.

Two first-pass artifacts were re-checked and corrected: phonology-sanity-gate's eight "404" rows were extraction artifacts (trailing `,`/`;` captured in the URL); on retry four resolve 200 and four return 403; to-verify's DOI likewise returned 403 on retry. The classification above is the corrected one. 403/429/405 are server-side blocks (paywall/bot filter/rate limit) to this client, **not** dead links; the timeouts (Lincoln library catalogue, `limc-france.fr`) are environment-side reachability failures, recorded as such, not as broken locators.

**Locator repair (only content change besides the field additions):** `calibration-registry.md` line 22 cited `[doi:10.1163/9789084513837](https://doi.org/10.1163/9789084513837)` for Debourse, *Of Priests and Kings* (Brill 2022). That DOI does not resolve: `curl -L https://doi.org/10.1163/9789084513837` → 404 and `https://api.crossref.org/works/10.1163/9789084513837` → 404 "Resource not found" (2026-10-17). Crossref bibliographic query returned the registered record `10.1163/9789004513037` (title "Of Priests and Kings: The Babylonian New Year Festival in the Last Age of Cuneiform Culture", author Debourse, issued 2022-02-10); the replacement resolves (`https://doi.org/10.1163/9789004513037` → `brill.com/view/title/59777`, HTTP 403 to this client = publisher bot-block after successful resolution). Both occurrences on the line were corrected; the old value is preserved here as the audit trail.

### 4. Provenance gate, before and after

`python3 tools/gates/provenance-audit.py corpus/knowledge/verification` (2026-10-17):

- after: `INFO scan: files=13 marks=72 mark-lines=72 findings=0 blocked=0` — exit 0
- before (mark total recomputed from HEAD with `git show HEAD:<file> | grep -oic 'to-verify'`, summed): **72** — no triage-inventory delta from this shard. No added line contains the marker token (deliberately: the gate counts it case-insensitively).

### 5. Frozen baseline pin unaffected

`tools/gates/frozen/round-3/inputs/corpus/knowledge/verification/gate-frozen-run-standard.md` is a **copy**; its digest `7b3bdc80a12ba509aae5785a5039f4ba97c94641fe0a21520868883071dbbbde` still equals the `input_sha256` pinned in `tools/gates/frozen/round-3/MANIFEST.tsv` (2026-10-17). The live file's edit changes the live digest only — the frozen run keeps grading its snapshot, exactly as `gate-frozen-run-standard.md` requires.

### 6. Diff shape

`git diff --numstat corpus/knowledge/verification/` (2026-10-17):

```
3	1	calibration-registry.md            (2 field lines + DOI repair: 1 changed line)
2	0	costume-era-consistency-gate.md
1	0	gate-frozen-run-standard.md        (recheck only; verified-at pre-existed)
2	0	internal-consistency-audit.md
2	0	lexicon-coverage-audit.md
2	0	naming-collision-gate.md
2	0	phonology-sanity-gate.md
2	0	real-world-inspiration-boundaries.md
2	0	to-verify-triage-protocol.md
2	0	verification-method-overview.md
```

`citation-format-and-source-registry.md`, `myth-consistency-gate.md`, `provenance-audit-ledger-format.md`: conformant before this pass (both fields present in §1), **not edited**. `git diff --check`: clean.

### 7. Citation-drift disclosure (required by this shard's file set)

The inserted lines shift every line below the insertion point. Delta: **+2** for the 9 files that gained two lines; **+1** for `gate-frozen-run-standard.md`; the 3 unedited files are unchanged. First `## ` heading, before → after: calibration 25→27 · costume 6→8 · gate-frozen 26→27 · internal 7→9 · lexicon 7→9 · naming 14→16 · phonology 7→9 · real-world 6→8 · to-verify 7→9 · verification-method 12→14; citation-format 13→13 · myth 6→6 · provenance 6→6.

Recorded `file:line` citations into these entries that now resolve **two lines later** (line +2; sweep: regex `verification/<name>.md:NN` over `corpus/lessons/**` and `reports/**`, 2026-10-17) — **62 rows across 9 records**:

| record | rows | target entries |
|---|---|---|
| `corpus/lessons/round-1-triage/V3.md` | 26 | real-world 5 · to-verify 12 · verification-method 9 |
| `corpus/lessons/round-2-triage/V01.md` | 9 | calibration 9 |
| `corpus/lessons/round-2-triage/V03.md` | 8 | costume 8 |
| `corpus/lessons/round-2-triage/V05.md` | 2 | lexicon 2 |
| `corpus/lessons/round-2-triage/V07.md` | 4 | naming 4 |
| `corpus/lessons/round-4-audit/civ-85-92.md` | 1 | to-verify 1 |
| `reports/supplement-opencode-1/21-phonology-review.md` | 1 | phonology 1 |
| `reports/round-8/depth/design-spec.md` | 9 | costume 9 |
| `reports/round-8/depth/skill-table-draft.md` | 2 | naming 2 |

Before this pass, the round-1/round-2 citations were text-exact against HEAD (spot-checked: 8 rows matched their quoted wording; 60/60 rows naming a section fell inside that section) — so this shift is real and is disclosed rather than silent. Two consequences need **orchestrator** action, both in concurrent round-8 D-shard artifacts (not this shard's write scope):

- `reports/round-8/depth/design-spec.md` pins `costume-era-consistency-gate.md` at digest `9a5982cf…a761aef` (line 635) and cites nine of its lines; new digest `455ad870…cd7a80b`, lines +2.
- `reports/round-8/depth/skill-table-draft.md` pins `naming-collision-gate.md` at digest `60491bae…48b2b1d` (line 318) and cites two of its lines; new digest `ddaaee83…5f768e9`, lines +2.

The round-1/2/4 triage records are historical; their rows quote the target wording, so the +2 offset is recoverable from this table. Round-8 artifact check (2026-10-17): `grep -rn 'verification/[a-z0-9-]*\.md:[0-9]' reports/round-8/` → no hits, i.e. no prefixed line locator into these files exists anywhere in round 8; the only round-8 line references are the eleven bare-name rows above (`design-spec.md` ×9, `skill-table-draft.md` ×2). The only other round-8 mention is path-level: `reports/round-8/operability/neg-controls/neg-05/neg-05-report.md:217` routes a one-line subset-policy note for `phonology-sanity-gate.md` to the parent — that note is not part of this metadata pass and was not absorbed here.

## Per-file result

Digests short16, `git show HEAD:<file> | sha256sum` → `sha256sum <file>` (2026-10-17). "fields before" = header-block `verified-at`/`recheck`.

| # | file | fields before | action | digest before → after | heading shift |
|---|---|---|---|---|---|
| 1 | calibration-registry.md | — | +2 lines; broken DOI repaired | `cb285870a5b339f2` → `cf7cceee9008a9db` | +2 |
| 2 | citation-format-and-source-registry.md | both (§1) | none (conformant) | `6e27001de26ef302` → `6e27001de26ef302` | 0 |
| 3 | costume-era-consistency-gate.md | — | +2 lines | `9a5982cf2aee742c` → `455ad8701a703031` | +2 |
| 4 | gate-frozen-run-standard.md | verified-at | +1 line (recheck) | `31f589f536a7b763` → `7eb2635bc72fb9a6` | +1 |
| 5 | internal-consistency-audit.md | — | +2 lines | `bcee67a41d7539fe` → `c3118517a8510e94` | +2 |
| 6 | lexicon-coverage-audit.md | — | +2 lines | `5c7e9b42d52ac4c6` → `cbf4f7a0931270c4` | +2 |
| 7 | myth-consistency-gate.md | both (§1) | none (conformant) | `4523b7a2747973be` → `4523b7a2747973be` | 0 |
| 8 | naming-collision-gate.md | — | +2 lines | `60491baec7b1aa91` → `ddaaee83a9ef8f16` | +2 |
| 9 | phonology-sanity-gate.md | — | +2 lines | `ee8ed1bb6bbef72b` → `de38547456a2b7e1` | +2 |
| 10 | provenance-audit-ledger-format.md | both (§1) | none (conformant) | `dfa66d2af81b2789` → `dfa66d2af81b2789` | 0 |
| 11 | real-world-inspiration-boundaries.md | verified-at (in-body, capital-V; recheck embedded) | +2 header lines; in-body line kept verbatim | `183cd7ad7c828b60` → `dc66ed87559e533d` | +2 |
| 12 | to-verify-triage-protocol.md | — | +2 lines | `c4508e50bc1a3b2b` → `073a348b38c5d8b2` | +2 |
| 13 | verification-method-overview.md | — | +2 lines | `2a14558b2add2069` → `f52708d91f5829b4` | +2 |

## Limits and boundary notes

- Reachability is not content verification. The sweep re-requested locators and classified responses; it did not read the books, articles, or catalogue records behind them. Every new `verified-at:` says so ("cited books not re-inspected" / "sources not re-inspected" / "no uninspected passage is quoted").
- 403/429/405 responses are remote-server refusals to this client and are **not** recorded as entry defects; the two timeouts are environment-side. Only the one Crossref-confirmed non-resolving DOI was treated as a defect and repaired.
- No tradition-specific, historical, or linguistic claim was asserted, altered, or cleared by this pass; no `(to-verify)` mark was removed (mark totals 72 → 72). No canon decision; no sibling repo or fleet file written.
- The `recheck:` triggers paraphrase each entry's own limits text (e.g. calibration-registry's §13 recheck practice, naming-collision's rerun rule, to-verify's handoff cadence); none introduces a new obligation.
- Lane-wide mark counts will still move because of concurrent shards editing other partitions (cf. `m01-civ-1-19.md` §Evidence note); this shard's own delta is 0.
- Fleet `CORPUS.md`'s `source:`-leg question stays with the integrator (`28-corpus-contract.md` §6.2); this fragment records the lane reading (header `- sources:` satisfies the leg) and does not edit fleet text.
- Re-verification commands for any future round: the four commands in §1, §2, §3, §4 above; a recount returning different numbers means this fragment is stale, not that the contract changed silently.

```json
{
  "schema": "kotodama-metadata-sweep/1",
  "shard": "M11",
  "partition": "corpus/knowledge/verification",
  "date": "2026-10-17",
  "baseline_revision": "e7ca0faeb6680fa9891b907be628d9db578c28f4",
  "worktree_head": "cf338a7",
  "files_audited": 13,
  "files_edited": 10,
  "fields_added": {"verified-at": 9, "recheck": 10},
  "conformant_before": ["citation-format-and-source-registry.md", "myth-consistency-gate.md", "provenance-audit-ledger-format.md"],
  "crossref_audit": {"concrete_targets": 137, "missing": 0, "glob_tokens": 1, "directory_refs": 3},
  "locator_sweep": {"checked_at": "2026-10-17", "file_url_pairs": 109, "unique_urls": 104,
    "reachable": 82, "blocked_remote": 24, "unreachable_environment": 2, "broken": 1,
    "repaired": [{"file": "calibration-registry.md", "line": 22, "old": "10.1163/9789084513837", "new": "10.1163/9789004513037", "evidence": "doi.org 404 + Crossref 404; replacement from api.crossref.org bibliographic query"}]},
  "gate": {"command": "python3 tools/gates/provenance-audit.py corpus/knowledge/verification", "before_marks": 72, "after_marks": 72, "findings": 0, "exit": 0},
  "frozen_pin_check": {"artifact": "tools/gates/frozen/round-3/inputs/corpus/knowledge/verification/gate-frozen-run-standard.md", "sha256": "7b3bdc80a12ba509aae5785a5039f4ba97c94641fe0a21520868883071dbbbde", "manifest_match": true},
  "line_shift": {"delta_two": ["calibration-registry.md","costume-era-consistency-gate.md","internal-consistency-audit.md","lexicon-coverage-audit.md","naming-collision-gate.md","phonology-sanity-gate.md","real-world-inspiration-boundaries.md","to-verify-triage-protocol.md","verification-method-overview.md"], "delta_one": ["gate-frozen-run-standard.md"],
    "affected_citation_rows": 62,
    "affected_records": {"corpus/lessons/round-1-triage/V3.md": 26, "corpus/lessons/round-2-triage/V01.md": 9, "corpus/lessons/round-2-triage/V03.md": 8, "corpus/lessons/round-2-triage/V05.md": 2, "corpus/lessons/round-2-triage/V07.md": 4, "corpus/lessons/round-4-audit/civ-85-92.md": 1, "reports/supplement-opencode-1/21-phonology-review.md": 1, "reports/round-8/depth/design-spec.md": 9, "reports/round-8/depth/skill-table-draft.md": 2}},
  "orchestrator_actions": [
    {"file": "reports/round-8/depth/design-spec.md", "issue": "digest pin + 9 line refs into costume-era-consistency-gate.md now stale", "old_sha256_16": "9a5982cf2aee742c", "new_sha256_16": "455ad8701a703031"},
    {"file": "reports/round-8/depth/skill-table-draft.md", "issue": "digest pin + 2 line refs into naming-collision-gate.md now stale", "old_sha256_16": "60491baec7b1aa91", "new_sha256_16": "ddaaee83a9ef8f16"}
  ],
  "files": [
    {"path": "corpus/knowledge/verification/calibration-registry.md", "before": "cb285870a5b339f20927428e5a28692d202bb29851a4ccb7dac638806cf1a26f", "after": "cf7cceee9008a9db768d074671f490e4e99feb59ed4e10fb21fa0b72a4e0454c", "added": ["verified-at", "recheck"], "locators": {"total": 8, "reachable": 4, "blocked": 3, "unreachable": 0, "broken": 1}},
    {"path": "corpus/knowledge/verification/citation-format-and-source-registry.md", "before": "6e27001de26ef30255b6dcd9ecdd3c91ca1095aebb8882f1b084abbd04c9d040", "after": "6e27001de26ef30255b6dcd9ecdd3c91ca1095aebb8882f1b084abbd04c9d040", "added": [], "locators": {"total": 7, "reachable": 7, "blocked": 0, "unreachable": 0, "broken": 0}},
    {"path": "corpus/knowledge/verification/costume-era-consistency-gate.md", "before": "9a5982cf2aee742ce702ccbffdec717889a3d6c987d9e32628ecd9c0aa761aef", "after": "455ad8701a703031ca63e1d118a1af396f06aebf65c762ae9d53490d2cd7a80b", "added": ["verified-at", "recheck"], "locators": {"total": 10, "reachable": 7, "blocked": 2, "unreachable": 1, "broken": 0}},
    {"path": "corpus/knowledge/verification/gate-frozen-run-standard.md", "before": "31f589f536a7b763f172302bcd61f91e526405b9ffb4435bd699b3396c482ad8", "after": "7eb2635bc72fb9a6ba19f0a565c15d7d03c0d6aaf62df46cc1413354b5626bb6", "added": ["recheck"], "locators": {"total": 5, "reachable": 5, "blocked": 0, "unreachable": 0, "broken": 0}},
    {"path": "corpus/knowledge/verification/internal-consistency-audit.md", "before": "bcee67a41d7539fe30af852033f7ec859d7880eaa7bfca78c9297191ddc3ebad", "after": "c3118517a8510e94b083ee061d0d18f867b479f3c60317cf1ccf7b4f6f2f3def", "added": ["verified-at", "recheck"], "locators": {"total": 13, "reachable": 11, "blocked": 2, "unreachable": 0, "broken": 0}},
    {"path": "corpus/knowledge/verification/lexicon-coverage-audit.md", "before": "5c7e9b42d52ac4c67431221d819b11af4ccf9b3d0782e7e82bb95ad8793ee570", "after": "cbf4f7a0931270c49fdcf5d665bd2cc0823cb26e6278f4c5bf5e575a5f38f9b8", "added": ["verified-at", "recheck"], "locators": {"total": 6, "reachable": 5, "blocked": 1, "unreachable": 0, "broken": 0}},
    {"path": "corpus/knowledge/verification/myth-consistency-gate.md", "before": "4523b7a2747973beeab00eb97b113e12a8cbfbba6a169ea7d56b3d037c995daf", "after": "4523b7a2747973beeab00eb97b113e12a8cbfbba6a169ea7d56b3d037c995daf", "added": [], "locators": {"total": 15, "reachable": 8, "blocked": 6, "unreachable": 1, "broken": 0}},
    {"path": "corpus/knowledge/verification/naming-collision-gate.md", "before": "60491baec7b1aa916432cf1e27cebac0d3ac3a093d57c6cbec997ecfc48b2b1d", "after": "ddaaee83a9ef8f16d179f49e24bb9b722617e32495b1def325ddc384b5f768e9", "added": ["verified-at", "recheck"], "locators": {"total": 8, "reachable": 5, "blocked": 3, "unreachable": 0, "broken": 0}},
    {"path": "corpus/knowledge/verification/phonology-sanity-gate.md", "before": "ee8ed1bb6bbef72bebbe4b3d6036abcd2a85505cf3eb8a2367f75a1a6d24f6a5", "after": "de38547456a2b7e1fd774669da29c39957f1fe7df2d75a8d47b3d77ebd44e333", "added": ["verified-at", "recheck"], "locators": {"total": 14, "reachable": 10, "blocked": 4, "unreachable": 0, "broken": 0}},
    {"path": "corpus/knowledge/verification/provenance-audit-ledger-format.md", "before": "dfa66d2af81b2789ad58b710cc577278f331a6cbda6d6c648d8bbf25613501f4", "after": "dfa66d2af81b2789ad58b710cc577278f331a6cbda6d6c648d8bbf25613501f4", "added": [], "locators": {"total": 4, "reachable": 4, "blocked": 0, "unreachable": 0, "broken": 0}},
    {"path": "corpus/knowledge/verification/real-world-inspiration-boundaries.md", "before": "183cd7ad7c828b60d8088b85dc989fb92c8c6818cd6a7b9b0b13c9b946a6b354", "after": "dc66ed87559e533d026dd2e9a3efb1b999d39bd4e2f5f7e575f751a275e5858f", "added": ["verified-at", "recheck"], "locators": {"total": 9, "reachable": 8, "blocked": 1, "unreachable": 0, "broken": 0}},
    {"path": "corpus/knowledge/verification/to-verify-triage-protocol.md", "before": "c4508e50bc1a3b2b066706702ba628842751f540a68495155d74e1e3ecff127e", "after": "073a348b38c5d8b27cef8f109afed06ff592da00f2eb91252657ab857e32fb13", "added": ["verified-at", "recheck"], "locators": {"total": 7, "reachable": 6, "blocked": 1, "unreachable": 0, "broken": 0}},
    {"path": "corpus/knowledge/verification/verification-method-overview.md", "before": "2a14558b2add20695edb81a512157f8081438ec23da11d49ee82e6683f1c32c6", "after": "f52708d91f5829b44bbf081341d7073ba05e757764ce164ff21563c2f903f0c9", "added": ["verified-at", "recheck"], "locators": {"total": 3, "reachable": 2, "blocked": 1, "unreachable": 0, "broken": 0}}
  ]
}
```
