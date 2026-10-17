# V11 — metadata re-audit (round 9): `corpus/knowledge/verification/` (all 13 entries)

- Round-9 metadata re-audit, shard V11 (assignment: the verification partition, all 13 entries; fragment path `reports/round-9/metadata/v11-verification.md`).
- Date 2026-10-17; audit commands run in the window ~20:49Z–20:56Z (inline `date -u` receipts at 20:53:18Z and 20:53:40Z UTC). The locator sweep ran inside that window.
- Baselines: round-9 `claims.json` `baseline_revision` `e1694bad6ac96aca45a11ca5746582b275929355`; observed HEAD `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` ("round-9: declare claims F/O/D"). `git show --stat a7bb205` touches only `reports/round-9/{claims,targets}.json`, and `git diff --stat e1694ba..HEAD -- corpus/` is empty — the committed corpus at HEAD equals the declared baseline.
- Contract audited: round-9 `targets.json` field `metadata_verify` — "11 shards re-audit all 179 corpus/knowledge entries for complete source/verified-at/recheck frontmatter after round 8's sweep; fix stragglers in place; fragments under reports/round-9/metadata/ + 1 auditor shard" — plus fleet `CORPUS.md:17` ("Each `knowledge/` entry opens with `source:`, `verified-at:` and `recheck:`"). Gate neutrality re-confirmed against the gate source: `tools/gates/provenance-audit.py:75` `FIELD_NAMES = ("topic", "sources", "couples")`, `FIELD_RE` line 76 — the metadata trio is not read by the gate.
- Round-8 prior: `reports/round-8/metadata/m11-verification.md` — fields added to 10 of 13 files (3 already conformant), 137 cross-reference targets resolved, locator sweep 109 file–URL pairs / 104 unique URLs, gate `files=13 marks=72 … findings=0`, one Crossref-confirmed broken DOI repaired. This pass re-audits after that sweep.
- **Write scope: this fragment only. 0 entry files changed.** No straggler in this partition was fixable within this shard's write discipline (the one live class — body placement — belongs to the open fleet-text question, §10), and the 13 files are digest-pinned by the round-9 `r9-pre` gate baseline (§7), so any edit here would break a committed pin. No commit; no LOG.md write; no sibling repo or fleet file touched.

## Method and commands

Per file, in order: (1) line-anchored field census (`^- (source|sources):`, `^- verified-at:`, `^- recheck:`) with exactly-once / non-empty / no-placeholder checks; (2) straggler-class sweeps (dedicated field missing; singles-line bundled trio; `to-verify`/placeholder value); (3) sha256 digest equality against round-8's recorded after-state and against the round-9 `r9-pre` pin; (4) provenance gate re-run and `--selftest`; (5) frozen-input pin re-check; (6) `- couples:` cross-reference resolution; (7) fresh linked-locator reachability sweep over every http(s) locator; (8) falsification controls (planted defects in memory). Every count below carries its command and date.

## 1. Field census — 13/13 complete, exactly once, non-empty (pre = post)

Command: anchored regexes per file + `sha256sum` (inline Python, 2026-10-17). All three fields present in every file; no duplicate field line in any of the 13; no empty or placeholder value.

| # | file | source form | verified-at | recheck | first `##` | sha256 (16) |
|---|---|---|---|---|---|---|
| 1 | calibration-registry.md | plural `- sources:` @4 | 24 | 25 | 27 | `cf7cceee9008a9db` |
| 2 | citation-format-and-source-registry.md | singular `- source:` @15 | 16 | 17 | 13 | `6e27001de26ef302` |
| 3 | costume-era-consistency-gate.md | plural @3 | 5 | 6 | 8 | `455ad8701a703031` |
| 4 | gate-frozen-run-standard.md | plural @4 | 18 | 19 | 27 | `7eb2635bc72fb9a6` |
| 5 | internal-consistency-audit.md | plural @4 | 6 | 7 | 9 | `c3118517a8510e94` |
| 6 | lexicon-coverage-audit.md | plural @4 | 6 | 7 | 9 | `cbf4f7a0931270c4` |
| 7 | myth-consistency-gate.md | singular @9 | 10 | 11 | 6 | `4523b7a2747973be` |
| 8 | naming-collision-gate.md | plural @3 | 13 | 14 | 16 | `ddaaee83a9ef8f16` |
| 9 | phonology-sanity-gate.md | plural @4 | 6 | 7 | 9 | `de38547456a2b7e1` |
| 10 | provenance-audit-ledger-format.md | singular @9 | 10 | 11 | 6 | `dfa66d2af81b2789` |
| 11 | real-world-inspiration-boundaries.md | plural @3 | 5 | 6 | 8 | `dc66ed87559e533d` |
| 12 | to-verify-triage-protocol.md | plural @4 | 6 | 7 | 9 | `073a348b38c5d8b2` |
| 13 | verification-method-overview.md | plural @4 | 11 | 12 | 14 | `f52708d91f5829b4` |

All 13 `verified-at` values are dated 2026-10-17 and state their scope (round-8 metadata-pass wording). Every first-`##` line equals round-8's recorded after-value (calibration 27 · costume 8 · gate-frozen 27 · internal 9 · lexicon 9 · naming 16 · phonology 9 · real-world 8 · to-verify 9 · verification-method 14 · citation 13 · myth 6 · provenance 6), i.e. the +2/+1 shift round-8 disclosed is the still-current geometry — no further drift.

## 2. Straggler-class sweeps (three classes)

- (a) **Dedicated field missing** — none: the census above is 13/13 (under the lenient reading, `- source:` or `- sources:`).
- (b) **Singles-line bundled trio** (`^- source:.*verified-at:` on one line) — none in the partition. Corpus-wide sweep, 2026-10-17: exactly one residual, `corpus/knowledge/civilizations/burma.md:15` (a bundled restatement below the header bullets that already exist at lines 6–7) — not this shard; recorded as an open item by shard V01 (`reports/round-9/metadata/v01-civ-1-19.md` §"Open items", item 3) and left for the integrator.
- (c) **`to-verify`/placeholder as a trio value** — none. The one in-partition hit, `myth-consistency-gate.md:11`, is the token inside the recheck value's prose, not a placeholder: `- recheck: when the index edition, source translation, culture/era scope, pantheon inventory, or symbol grammar changes; check any `(to-verify)` claim before making it load-bearing.` A leading-token placeholder sweep (`^- verified-at:\s*[`*_]*\s*(to-verify|tbd|todo|unknown)\b`, case-insensitive) returns 0 files across all 179 entries (2026-10-17 — shard V01 dated the last three, in its own range, earlier in this wave).

## 3. Falsification controls (the checker was itself tested)

Five planted defects held in memory (nothing written), each run through the census checker (2026-10-17): field removed → flagged `no-rc`; bare `- verified-at: to-verify` → flagged; `to-verify — the entry body records no dated inspection` (the exact round-8/V01 straggler shape) → flagged; bundled single-line trio → flagged `bundled`; clean original → no flags, and the clean-tree control over the 13 real files → 0 flags. **The controls caught one real blind spot**: an earlier checker version keyed on exact placeholder values and let the `to-verify — reason` shape through; the final checker matches a bare or leading-token placeholder and passes all controls. (`placeholder-with-reason` and `bundled` control rows were initially mis-expected and the expectations corrected after diagnosis; final run: `CONTROLS ALL-PASS`.)

## 4. Digest stability vs round-8 — 13/13 byte-identical

`sha256sum` of each file now vs the after-values recorded in `reports/round-8/metadata/m11-verification.md` (JSON receipt): **13/13 SAME, 0 drift**. The round-8 edits persisted unchanged through the round-8→round-9 integration; nothing in this partition has been touched this round (`git status --porcelain -- corpus/knowledge/verification/` → empty at 20:53:40Z).

## 5. Provenance gate, before → after

`python3 tools/gates/provenance-audit.py corpus/knowledge/verification` (2026-10-17):

- after (20:53:40Z): `INFO scan: files=13 marks=72 mark-lines=72 findings=0 blocked=0` — exit 0
- before (start of wave, same command): identical numbers (72 marks); equals round-8's final measurement — shard delta **0 marks / 0 findings**.
- `python3 tools/gates/provenance-audit.py --selftest` → exit 0.
- Directory-context run (`corpus/knowledge`): `files=179 marks=619 mark-lines=613 findings=0 blocked=0` — matches the V12 auditor's pre-state figure; numbers may move while sibling round-9 shards edit other partitions.

## 6. Frozen pin — intact

`sha256sum tools/gates/frozen/round-3/inputs/corpus/knowledge/verification/gate-frozen-run-standard.md` → `7b3bdc80a12ba509aae5785a5039f4ba97c94641fe0a21520868883071dbbbde`, equal to the `input_sha256` in `tools/gates/frozen/round-3/MANIFEST.tsv` (row 8). The live file's digest (`7eb2635bc72fb9a6…`) differs from the frozen copy by design: the frozen run grades its snapshot, not the live tree.

## 7. `r9-pre` drift-pin cross-check (round-9 O-axis artifact covering this partition)

The round-9 gate-baseline work committed `tools/gates/frozen/provenance-audit/r9-pre/expected.json`, which pins snapshot inputs including **all 13 files of this partition**. Compared 2026-10-17: **13/13 live digests equal the pinned values** (same short16 values as the §1 table). Consequence recorded here: any future edit to these files must go through a baseline refresh; the zero-edit posture of this re-audit is therefore also the only posture that preserves the committed pin.

## 8. Cross-reference audit (`- couples:` resolution) — 127 concrete targets, 0 missing

Method (as round-8's, independently re-implemented): gate-`field_block` extraction of the `- couples:` field (single line here; no indented continuations, no duplicates), brace-union expansion `{a,b}.md` → `a.md b.md`, tokenize `[\w./-]+\.md`, resolve each token against the entry's directory → `corpus/knowledge/` → repo root → basename across `corpus/knowledge/**/*.md`.

Result: **127 concrete path refs, 0 missing** — counts per file: calibration 12 · citation-format 9 · costume-era 17 · gate-frozen 4 · lexicon-coverage 16 · myth-consistency 14 · naming-collision 12 · phonology-sanity 11 · provenance-ledger 8 · real-world 13 · to-verify-triage 11 (sum 127, identical to round-8's independently obtained 127). Non-token by design, not counted: `gate-frozen-run-standard.md`'s `*-gate.md` glob (tokenizes as `-gate.md`; excluded as the glob artifact round-8 also excluded) and `internal-consistency-audit.md`'s three directory references (`../linguistics/`, `../myth-symbol/`, `../culture-material/` — all exist) plus `verification-method-overview.md`'s 10 extension-less entry names (all resolve; same set round-8 listed).

## 9. Fresh linked-locator reachability sweep (round 9)

Command (2026-10-17, 10-thread pool): per-file unique `https?://` locators, trailing sentence punctuation stripped, each requested once with

```
curl -sS -o /dev/null -w '%{http_code}' -L --max-time 25 -A 'Mozilla/5.0 (X11; Linux x86_64)' <url>
```

Result: **109 file–URL pairs (104 unique URLs)** — identical pair/unique counts to round-8. Classification: 81 reachable (200/202/203), 25 blocked by remote servers (403/405/429), 2 unreachable from this environment (curl `000` connection timeout), 1 redirect-only (`301`; its target times out — see retries below).

| file | locators | reachable | blocked | unreachable | redirect-only | vs round-8 |
|---|---|---|---|---|---|---|
| calibration-registry.md | 8 | 4 | 4 | 0 | 0 | repaired-DOI row now 403 (was 404 removed by round-8's repair) |
| citation-format-and-source-registry.md | 7 | 7 | 0 | 0 | 0 | identical |
| costume-era-consistency-gate.md | 10 | 7 | 2 | 1 | 0 | identical (`library.lincoln.ac.uk` still times out) |
| gate-frozen-run-standard.md | 5 | 5 | 0 | 0 | 0 | identical |
| internal-consistency-audit.md | 13 | 10 | 2 | 1 | 0 | **delta**: the U-Tokyo PDF was 200 in round 8, now `000` (retry 502, below) |
| lexicon-coverage-audit.md | 6 | 5 | 1 | 0 | 0 | identical |
| myth-consistency-gate.md | 15 | 8 | 6 | 0 | 1 | **delta**: `limc-france.fr` was a timeout in round 8, now `301` (target still times out) |
| naming-collision-gate.md | 8 | 5 | 3 | 0 | 0 | identical |
| phonology-sanity-gate.md | 14 | 10 | 4 | 0 | 0 | identical |
| provenance-audit-ledger-format.md | 4 | 4 | 0 | 0 | 0 | identical |
| real-world-inspiration-boundaries.md | 9 | 8 | 1 | 0 | 0 | identical |
| to-verify-triage-protocol.md | 7 | 6 | 1 | 0 | 0 | identical |
| verification-method-overview.md | 3 | 2 | 1 | 0 | 0 | identical |

Non-2xx rows (28; all other rows returned 200/202/203):

| status | file | URL |
|---|---|---|
| 429 | calibration-registry | https://doi.org/10.1017/S0003598X00064310 |
| 403 | calibration-registry | https://doi.org/10.1086/200264 |
| 403 | calibration-registry | https://doi.org/10.1163/9789004513037 (round-8's repair; resolves, publisher bot-block) |
| 429 | calibration-registry | https://www.cambridge.org/core/journals/antiquity/issue/C1AFE95005862070C41E9629AE83A114 |
| 403 | costume-era | https://cameo.mfa.org/wiki/Spun_silk |
| 000 | costume-era | https://library.lincoln.ac.uk/items/202188 |
| 403 | costume-era | https://www.britannica.com/technology/spun-silk-yarn |
| 403 | internal-consistency | https://doi.org/10.1093/notesj/gjad106 |
| 403 | internal-consistency | https://doi.org/10.1136/bmj.b2680 |
| 000 | internal-consistency | https://repository.dl.itc.u-tokyo.ac.jp/record/27548/files/ggr031005.pdf |
| 403 | lexicon-coverage | https://doi.org/10.1075/ijcl.13.4.02gri |
| 403 | myth-consistency | https://brill.com/display/title/20123?language=en |
| 429 | myth-consistency | https://doi.org/10.1017/S0075426925100281 |
| 405 | myth-consistency | https://www.amherst.edu/system/files/media/1479/Symbols%2520in%2520African%2520Ritual_0.pdf |
| 429 | myth-consistency | https://www.cambridge.org/core/journals/journal-of-hellenic-studies/article/when-was-early-greece/AC78606D9821A8B1B65EAB8CEEE6FC6A |
| 403 | myth-consistency | https://www.cornellpress.cornell.edu/book/9780801491016/the-forest-of-symbols/ |
| 301 | myth-consistency | https://www.limc-france.fr/ |
| 429 | myth-consistency | https://www.metmuseum.org/essays/ancient-greek-dress |
| 429 | naming-collision | https://doi.org/10.1017/9780511807954 |
| 403 | naming-collision | https://doi.org/10.1093/oxfordhb/9780199656431.001.0001 |
| 403 | naming-collision | https://doi.org/10.1145/321796.321811 |
| 403 | phonology-sanity | https://doi.org/10.1051/aacus/2022044 |
| 403 | phonology-sanity | https://doi.org/10.1073/pnas.1417413112 |
| 403 | phonology-sanity | https://doi.org/10.1121/10.0002279 |
| 403 | phonology-sanity | https://doi.org/10.1126/science.aav3218 |
| 403 | real-world-inspiration | https://doi.org/10.1111/j.1468-2885.2006.00277.x |
| 403 | to-verify-triage | https://doi.org/10.1037/0022-0663.83.1.73 |
| 429 | verification-method | https://www.cambridge.org/core/books/uses-of-argument/26CF801BC12004587B66778297D5567C |

Round-8 comparison: the URL set is identical except one row changed **by round-8's own design** (the repaired DOI). Statuses are identical to round-8's published per-file table in every other row except the two deltas above. Serial retries for the two deltas (2026-10-17, same curl, max-time 25): U-Tokyo PDF → `502` on retry (first attempt `000`); `limc-france.fr` → `301` received, redirect target then times out (`curl: (28) … Connection timed out`, exit 28). Both are recorded as **documented access failures / upstream instability**, not dead links: 403/405/429 are server-side refusals to this client, `000`/timeouts are environment- or upstream-side reachability failures.

## 10. Corpus-wide context (snapshot of a live parallel round — not this shard's acceptance claim)

Measured 2026-10-17 20:53Z (sibling shards actively editing):

- **Lenient reading** (`- source:` or `- sources:`, plus `- verified-at:`, `- recheck:` anywhere): **179/179 conformant.** This is the reading round-8 M11/M07 established for this lane and the one this partition uses.
- **Literal fleet reading** ("opens with" a singular `- source:` + `verified-at:` + `recheck:` before the first `## `): 115/179; 64 nonconformant, in two classes: 61 files lack the singular `- source:` pointer (civilizations 19, culture-material 16, linguistics 16, verification 10) and 3 files carry the trio fully but below the first heading (this partition's `citation-format-and-source-registry.md` :16–17 below :13, `myth-consistency-gate.md` :10–11 below :6, `provenance-audit-ledger-format.md` :10–11 below :6). Those 3 are the only placement cases in this partition and are deliberately **not** moved here: round-8 M11 filed the `source:`/`sources:` fleet-text question with the integrator (`reports/supplement-opencode-1/28-corpus-contract.md` §6.2) and declined to decide it; this re-audit follows that reading (see also V08's identical posture). Sibling shards have taken both sides this round: V05 applied the literal reading **additively** (18 singular pointer lines added in civ 77–94), while V06's files already satisfy both readings and V08's keep the plural `- sources:` form — neither resolved the convention.
- The lenient count moved 178→179 during this wave because shard V04 split `civilizations/mali-songhai.md`'s bundled line into three fields (still below its first heading). In-flight worktree edits observed at 20:53Z: V01 (bali, byzantium, carthage), V04 (mali-songhai), V05 (18 files), V10 (era-periodization-models, material-culture-inference-method) — none in this partition.

## 11. Cross-shard status observed (20:53Z)

- Fragments landed: `audit.md` (V12 auditor), v01, v02, v03, v04, v05, v06, v07, v08, v10. Still missing at observation time: **v09 (myth-symbol)**; v11 = this file.
- Round 8's two orchestrator actions from M11 remain **open**: `reports/round-8/depth/design-spec.md:635` still pins `costume-era-consistency-gate.md` at `9a5982cf…a761aef` (current `455ad870…cd7a80b`) and `reports/round-8/depth/skill-table-draft.md:318` still pins `naming-collision-gate.md` at `60491bae…48b2b1d` (current `ddaaee83…5f768e9`). Re-checked 2026-10-17: no round-9 artifact has updated or superseded either pin.
- Round-8's disclosed citation-row shift (+2 lines below the inserted fields; 62 rows across 9 records) is **unchanged and still accurate** — this partition received no edits this round, so no new shifts were introduced. A round-9 scan for prefixed line locators into these files (`grep -rn 'verification/[a-z0-9-]*\.md:[0-9]' reports/round-9/`) → no hits.

## Limits

- Reachability is not content verification: the sweep re-requested locators and classified responses; it did not read the works behind them. Every `verified-at:` in this partition states the same limit.
- The fresh sweep ran on the same date as round-8's (2026-10-17); statuses are therefore expected to be near-identical, and the two deltas (U-Tokyo PDF, LIMC) are server-side/environment-side churn within hours, not content claims.
- 403/405/429 are remote-server refusals to this client (paywall/bot filter/rate limit), recorded as such, never as entry defects; `000`/timeout rows are environment- or upstream-side failures and are recorded with their retry outcomes.
- This is an apparatus audit — field presence, form, placement, digest stability, gate cleanliness, reference resolution, locator reachability — not claim-level verification of the entries' historical/linguistic content, and not a canon decision. No `(to-verify)` mark was added or removed; partition mark total 72 → 72.
- §10's corpus-wide counts are a snapshot of a live parallel round (siblings editing while measured); the auditor shard V12 owns the post-state headline count.

```json
{
  "schema": "kotodama-metadata-reaudit/1",
  "shard": "V11",
  "partition": "corpus/knowledge/verification",
  "date": "2026-10-17",
  "baseline_revision": "e1694bad6ac96aca45a11ca5746582b275929355",
  "worktree_head": "a7bb205d3aecdaa24d91c047c8719cd8689e4ddd",
  "files_audited": 13,
  "files_edited": 0,
  "field_census": {"complete_lenient": 13, "complete_strict_openblock": 10,
    "in_body_placement": ["citation-format-and-source-registry.md","myth-consistency-gate.md","provenance-audit-ledger-format.md"],
    "singles_line_bundled": 0, "placeholder_values": 0},
  "digest_stability": {"vs_round8_after_state": "13/13 SAME", "vs_r9pre_pin": "13/13 SAME"},
  "gate": {"command": "python3 tools/gates/provenance-audit.py corpus/knowledge/verification",
           "before": "files=13 marks=72 mark-lines=72 findings=0 blocked=0",
           "after":  "files=13 marks=72 mark-lines=72 findings=0 blocked=0", "exit": 0,
           "selftest_exit": 0},
  "frozen_pin": {"artifact": "tools/gates/frozen/round-3/inputs/corpus/knowledge/verification/gate-frozen-run-standard.md",
                 "sha256": "7b3bdc80a12ba509aae5785a5039f4ba97c94641fe0a21520868883071dbbbde", "manifest_match": true},
  "crossref": {"concrete_targets": 127, "missing": 0, "glob_artifacts": 1,
               "per_file": {"calibration-registry.md": 12, "citation-format-and-source-registry.md": 9, "costume-era-consistency-gate.md": 17, "gate-frozen-run-standard.md": 4, "lexicon-coverage-audit.md": 16, "myth-consistency-gate.md": 14, "naming-collision-gate.md": 12, "phonology-sanity-gate.md": 11, "provenance-audit-ledger-format.md": 8, "real-world-inspiration-boundaries.md": 13, "to-verify-triage-protocol.md": 11}},
  "locator_sweep": {"checked_at": "2026-10-17", "pairs": 109, "unique_urls": 104,
    "reachable": 81, "blocked_remote": 25, "unreachable_environment": 2, "redirect_only": 1,
    "deltas_vs_round8": [
      {"file": "internal-consistency-audit.md", "url": "https://repository.dl.itc.u-tokyo.ac.jp/record/27548/files/ggr031005.pdf", "round8": "reachable", "round9": "000 timeout; retry 502"},
      {"file": "myth-consistency-gate.md", "url": "https://www.limc-france.fr/", "round8": "unreachable (timeout)", "round9": "301 redirect; target times out (curl exit 28)"},
      {"file": "calibration-registry.md", "url": "https://doi.org/10.1163/9789004513037", "round8": "n/a (repair of a 404)", "round9": "403 publisher bot-block"}]},
  "falsification_controls": {"controls": 5, "result": "ALL-PASS",
    "caught_blind_spot": "exact-placeholder-only check missed the 'to-verify — reason' value shape; checker hardened to leading-token match"},
  "corpus_wide_context": {"measured_at": "2026-10-17T20:53Z", "files": 179,
    "lenient_conformant": 179, "strict_openblock_conformant": 115,
    "strict_nonconformant_classes": {"missing_singular_source": 61, "trio_in_body": 3},
    "live_edits_by_siblings": {"V01": ["bali.md","byzantium.md","carthage.md"], "V04": ["mali-songhai.md"], "V05": 18, "V10": ["era-periodization-models.md","material-culture-inference-method.md"]}},
  "open_items_for_integrator": [
    {"item": "stale digest pins in round-8 depth artifacts", "files": ["reports/round-8/depth/design-spec.md:635", "reports/round-8/depth/skill-table-draft.md:318"], "state": "still stale, re-checked 2026-10-17"},
    {"item": "source:/sources: fleet-text question", "status": "open (28-corpus-contract.md §6.2); two readings live in the round-9 tree"},
    {"item": "burma.md bundled in-body line 15", "status": "reported by V01, not this shard"}]
}
```
