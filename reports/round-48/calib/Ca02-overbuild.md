# Ca02 — the r47 over-build defect class: queue-successor disposition

- Seat: **Ca02** | role executor | claim **Ca** (calibration) | round 48, loop 2, position 2
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19) == `reports/round-48/claims.json` `baseline_commit` (`a01405d`)
- Out path: `reports/round-48/calib/Ca02-overbuild.md` (this file only)
- Disposition: **one successor row, `r47-entry-overbuild-defect-class`, class `routed-with-owner`**, with the nine instance findings B1–B9 preserved inside it, a measured length record, and a proposed (not landed) entry-quality control. It edits no filed byte.

**One-line judgment.** The r47 cartography draft is a real topic drafted outside the house band — **790 assembled fenced lines** (51-line head + 739 body) against a live culture-material partition of 103–221 (median 149, max 221) — and nine blocking defects survived because the audits ran on per-seat fragments, never on the assembled bytes. The class is not "long entries"; it is **an out-of-band draft whose defect surface was never measured on the assembled artifact**. It needs a durable row, not another prose warning.

---

## 1. Class definition and boundary

**In class (`r47-entry-overbuild-defect-class`):**

1. The assembled **fenced entry body** materially exceeds the partition's live length discipline (here 3.6× the longest existing entry and 5.3× the median).
2. The excess is not a recorded exception: no audit, reviewer, or integrator ruling accepted the length.
3. Defects that a per-seat audit could not see — arithmetic, citation anchors, cross-section references, worked-example consistency, table completeness — are present in the assembled bytes.
4. The draft was correctly **not landed**; the count did not move (`reports/round-47/validation.json:9` → C `unchanged-blocked`, total 223).

**Out of class:** a long entry inside a declared band (C07's executable band is 100–260 lines, `reports/round-47/cov/C07-contract-audit.md:354`); a table-dense entry that passes its audits; a right-sized entry whose figures are all recomputed at landing. Length alone is a flag, not the defect — the class is **length plus an unmeasured defect surface**.

**Why the class needs a row rather than a gate claim this round.** The r48 freshness gate guards *topic ownership* (the r48 C claim is FRESH because cartography is unowned); it does not inspect entry quality. No durable length-or-quality control exists in `tools/`: `grep -rln 'partition band\|length in partition' tools/` returns no file, and the only checker of record is the r47 C07 fragment's inline `warn(...)` at `reports/round-47/cov/C07-contract-audit.md:354`. That checker did fire — `FAIL length in partition band: 854 lines` on the pre-trim assembly, `reports/round-47/cov/C11-scribe.md:67-78` — but as a fragment, not as a gate. So the class is open with an owner, not fixed.

---

## 2. Measurements (this seat, at `a01405d`)

All commands from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19. Fence extraction reads each fenced block's body only: it drops the opening and closing fence lines and any prose outside the fences.

| What | Command / method | Output |
|---|---|---|
| corpus total | `find corpus/knowledge -name '*.md' \| wc -l` | `223` |
| culture-material | `ls corpus/knowledge/culture-material/*.md \| wc -l` | `25` |
| partition band | `wc -l` over the 25 files | min **103**, median **149**, max **221**, mean 150.2 |
| r47 entry, by fragment | fence extraction | C04 head **51**, C01 §§1–4 **201**, C02 §§5–9 **361**, C03 §§10–15 **177** |
| assembled | sum | **790 lines**, 20,123 words, 127,942 chars, 15 H2, **240** table rows, 51 `(to-verify)` |
| body only (head excluded) | 790 − 51 | **739 lines**, 17,601 words, 106,997 chars |
| ratios | 790 / 221; 790 / 149 | **3.6×** the longest; **5.3×** the median |
| body-based ratios | 739 / 221; 739 / 149 | 3.3×; 5.0× |

The 739/17,601/106,997 body figure reproduces R03 exactly (`reports/round-47/review/R03-c-content.md:96`) and reconciles with R01's assembly table (`reports/round-47/review/R01-review.md:88-92`: 790 = 51 head + 739 body). The two ratio pairs are not a contradiction; they use different numerators, and both are far outside band. This seat measured them rather than carrying either.

Fragment digests pin the bytes measured (they match the r47 R03 §1 read):

```
cfb42955617373479a41d881fb6fd83f7df907aa7f563f51de95493d9ec8c44d  reports/round-47/cov/C01-entry-a.md
5f5683a72ea06d4e929d694a7eb03a067ebc7adc00cdb5ea6d72f489797779af  reports/round-47/cov/C02-entry-b.md
4b699e06537115274807b64fbc5947cefc889348e5b4434b14a8ddb661eee3e5  reports/round-47/cov/C03-entry-c.md
cb5a7489676de47e146e5055e07be9c8fa9d2df624c8872b0d438efcd67b68b0  reports/round-47/cov/C04-entry-header.md
```

**Trimming did not cure it.** The pre-trim assembly was 854 lines and failed C07's length leg (`reports/round-47/cov/C11-scribe.md:67-78`); C02 was then trimmed 424 → 361 body lines, moving the assembly to 790 — still 3.6× the partition max (`reports/round-47/review/R01-review.md:92`). The lesson is that a 20% trim is not a right-sizing; the target must be set before drafting.

---

## 3. The nine instance findings, re-verified live

Each row states the filed defect, the live check this seat ran, and the rule the r48 right-sized draft must satisfy. The fixes are the r48 draft's obligations, not edits to r47 bytes.

| ID | Filed bytes | Live check (this seat) | r48 obligation |
|---|---|---|---|
| **B1** arithmetic | `reports/round-47/cov/C02-entry-b.md:98` says 0.2 mm at 1:50,000 with a survey closing at 200 m "asserts ten times the available precision" | `0.2 mm × 50,000 = 10,000 mm = 10 m`; `200 m / 10 m = 20`. The text's own quantities give **20×**, not 10× | Recompute every ratio at drafting; either 100 m or "twenty times" |
| **B2** unreproducible count | `reports/round-47/cov/C04-entry-header.md:115` claims `grep -rli 'cartograph'` → "2 files / 3 lines", and names `cosmology-cosmography.md:71` as a hit | `grep -rn 'cartograph' corpus/knowledge/ \| wc -l` → **2**; the hits are `cosmology-cosmography.md:102` and `mesoamerica-primary-sources.md:58`. `:71` does not contain the token | A gap line states the command it actually ran and a count that command can produce |
| **B3** false accusation | `reports/round-47/cov/C02-entry-b.md:36` and `:501` say C01's quote "a map is an archive of coups" is "not in the file" and order it replaced with "renamings" | `grep -n 'archive of coups' corpus/knowledge/linguistics/naming-systems.md` → `70:… Every renaming is datable; a map is an archive of coups.` The quote is verbatim; C03's `:219` "renamings" is the paraphrase | Never "correct" a source before grepping it; a reviewer's accusation is itself a citation claim |
| **B4** mis-anchored ladder | `reports/round-47/cov/C02-entry-b.md:248` cites `craft-artisan-lexicon.md:44` as the workshop ladder; the audit row `:421` certifies ":44 workshop ladder table … real" | `sed -n '44p'` → the **Steel (Japan)** material row; the ladder header is `:54`, the seven systems `:56-63`, the design rule `:65` | Re-read the anchored line, not the section; an audit row that repeats the body's anchor verifies nothing |
| **B5** wrong section refs | `reports/round-47/cov/C03-entry-c.md:79` says "the typology in §1–3"; `:184` says "the typology in §2" | The eight-form typology is C01 **§4.1** (`reports/round-47/cov/C01-entry-a.md:238`); §2 is the five-condition register test (`:109`) | Resolve every `§` pointer against the assembled heading map after assembly, not per fragment |
| **B6** wrong section ref | `reports/round-47/cov/C01-entry-a.md:298` says "Provenance/charter (§9)" | `reports/round-47/cov/C02-entry-b.md:278` = `## 8. Provenance and charter`; `:347` = `## 9. The container-name fossil` | Same rule as B5 |
| **B7** worked-example inconsistency | `reports/round-47/cov/C03-entry-c.md:123` "re-survey after any storm that breaches a dike"; `:137` "not due until the levy year turns … after every breach, not every levy year"; `:150` table row "after a dike breach, per levy year" | Three incompatible statements; C14 already failed it — `reports/round-47/cov/C14-example.md:11` (F-1 blocking), and `grep -c 'DR-CT-'` over §11 = **0** (F-2, `:123`) | One update rule stated once, with rule ids in the example; re-run the example audit on the assembled section |
| **B8** overstated ownership | `reports/round-47/cov/C01-entry-a.md:90` and `reports/round-47/cov/C04-entry-header.md:115` claim the corpus "owns no made map", citing only `cosmology-cosmography.md:71`/`:102` | `corpus/knowledge/myth-symbol/cosmology-cosmography.md:27` defines cosmography as "how the world is drawn (maps), named, walked, and built" — a competing sentence the draft never dispositions | State the boundary against `:27` in one sentence: cosmography owns the world-drawn content; this entry owns the surveyed, projected, reproduced sheet |
| **B9** incomplete per-form table | `reports/round-47/cov/C03-entry-c.md:95-103` is titled "Minimum credible build per form" with **5** rows | C01 §4.1 lists **eight** forms (`reports/round-47/cov/C01-entry-a.md:238-249`); celestial/star chart, thematic, and lienzo are absent from the table | Either cover all eight or retitle "five common forms"; the table's row count is checkable against the typology's |

R03's verdict stands (`reports/round-47/review/R03-c-content.md:188-196`); this seat independently reproduced each live check above rather than citing the review. The r47 record also carries the class verdict: `reports/round-47/validation.json:9` — "790 lines vs live partition max 221 with 9 blocking defects … Not landing-ready".

---

## 4. Successor row (fenced, integrator-applied)

**Apply path:** `reports/round-48/calib/queue-successor-r48.json` (new file; never an in-place edit). **Parent:** `reports/round-40/op/defect-queue-v2.json`, pinned at `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907` (this seat's `sha256sum`; 38 rows; `git status --porcelain` on it → empty). **Predecessor successor:** `reports/round-47/calib/queue-successor-r47.json`, sha256 `9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58`, 3 rows — this seat grepped its `rows[]` ids and found **no over-build row**, so this is a new row, not a duplicate.

```json
{
 "schema": "kotodama-defect-queue-successor-v1",
 "round": 48,
 "date": "2026-10-19",
 "loop": 2,
 "artifact": "defect-queue-v2 successor delta - the r47 over-build defect class (Ca02)",
 "parent": "reports/round-40/op/defect-queue-v2.json",
 "parent_sha256_at_assembly": "dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907",
 "parent_bytes_edited": false,
 "predecessor_successor": {
  "path": "reports/round-47/calib/queue-successor-r47.json",
  "sha256": "9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58",
  "rows": 3,
  "over_build_row_present": false
 },
 "baseline_commit": "a01405d",
 "class_vocabulary": {
  "routed-with-owner": "No fix is claimed; the finding has a named owner and a next touch.",
  "recorded": "The measured fact or correction is recorded; filed bytes are immutable or no action is owed.",
  "fixed-with-evidence": "A landed artifact plus a pasted measured output closes the finding.",
  "could-not-recover": "The evidence the finding depends on cannot be recovered; a named reason and owner are recorded.",
  "v2_mapping": "routed-with-owner -> carried-with-owner (owner + next_touch); recorded -> carried-with-owner with next_touch 'none - recorded'; fixed-with-evidence -> fixed-with-evidence; could-not-recover -> carried-with-owner with the named reason."
 },
 "rows": [
  {
   "id": "r47-entry-overbuild-defect-class",
   "origin": "r47 C (cartography entry) non-landing. Instance review: reports/round-47/review/R03-c-content.md:188-196 (B1-B9) and :96 (739-line body); assembly arithmetic: reports/round-47/review/R01-review.md:88-92 (790 = 51 head + 739 body); round verdict: reports/round-47/validation.json:9; the pre-trim length FAIL: reports/round-47/cov/C11-scribe.md:67-78. Dedupe aliases: 'r47-C-overbuild', '790-line cartography draft', 'R03-B1..B9' (instance findings, not separate rows), 'over-built entry pattern'.",
   "class": "routed-with-owner",
   "v2_class_equivalent": "carried-with-owner",
   "owner": "r48 C drafter (right-sized redraft) + r48 integrator (entry-quality acceptance); future entry-drafting rounds inherit the pre-apply checklist. Not owned by the README editor or by the freshness-gate owner.",
   "reason": "The r47 cartography entry was a genuine, fresh topic drafted outside the partition's length discipline: 790 assembled fenced lines (51 head + 201 + 361 + 177) against a live culture-material band of 103-221 lines, median 149, max 221 (wc -l on the 25 files at a01405d) - 3.6x the longest and 5.3x the median. The body-only measure is 739 lines / 17,601 words / 106,997 chars / 240 table rows, reproducing R03 :96 and reconciling with R01 :92. Nine blocking defects (B1-B9) then survived to assembly because each seat audited its own fragment and no audit ran on the assembled bytes: a wrong ratio (200 m vs 10 m ground = 20x, text says ten times, C02-entry-b.md:98); a count its own command cannot produce (C04-entry-header.md:115 '2 files / 3 lines' vs grep -rn 'cartograph' = 2); a false source-accusation against a verbatim quote (C02-entry-b.md:36,:501 vs naming-systems.md:70); a mis-anchored workshop ladder certified by its own audit row (C02-entry-b.md:248,:421 vs craft-artisan-lexicon.md:44,:54-65); two wrong section pointers (C03-entry-c.md:79,:184; C01-entry-a.md:298); a worked example with three incompatible update rules (C03-entry-c.md:123,:137,:150; C14-example.md:11 FAIL F-1, and DR-CT- count in section 11 = 0, F-2); an ownership claim that never answers cosmography's competing definition at cosmology-cosmography.md:27; and a 'per form' table covering 5 of the 8 forms (C03-entry-c.md:95-103 vs C01-entry-a.md:238-249). Trimming the assembly from 854 to 790 did not bring it into band, so the failure is design-time, not a late edit. The topic remains fresh and unowned at a01405d; the defect is entry quality, not coverage.",
   "next_touch": "r48 C: land ONE right-sized entry (target inside the live 103-221 band; the round's stated tolerance is <=~250 lines) measured by fence extraction on the assembled body, with every B1-B9 shape checked on the assembled bytes before apply: ratios recomputed, every path:line re-read, every section pointer resolved against the assembled heading map, one update rule in the worked example, the form table's row count equal to the typology's, and the cosmography :27 boundary stated. Reclass only after the r48 landing measurements are pasted into a NEW closing row (see reclass_gates); never edit the r47 fragments.",
   "evidence": "reports/round-47/review/R03-c-content.md:96,188-196 (sha256 7e3e0880cfc7610b5d066bdf09c713a22038121b84cabb12c4fb8f968e8f238e); reports/round-47/review/R01-review.md:88-92 (sha256 196328de7de3ea19cce8f689bef140bbaa13f8b77b0be987253a702c23fe235c); reports/round-47/validation.json:9 (sha256 17f8f1d4498f5c0f89ac51989e2c42d91b3275a692b988f02b88c56d6942d166); reports/round-47/cov/C11-scribe.md:67-78 (sha256 4637ab1018327348902a3d78767ec0b224335d74740fa7a3abe5bc1748f4d97c); reports/round-47/cov/C01-entry-a.md (cfb42955617373479a41d881fb6fd83f7df907aa7f563f51de95493d9ec8c44d); reports/round-47/cov/C02-entry-b.md (5f5683a72ea06d4e929d694a7eb03a067ebc7adc00cdb5ea6d72f489797779af); reports/round-47/cov/C03-entry-c.md (4b699e06537115274807b64fbc5947cefc889348e5b4434b14a8ddb661eee3e5); reports/round-47/cov/C04-entry-header.md (cb5a7489676de47e146e5055e07be9c8fa9d2df624c8872b0d438efcd67b68b0); corpus/knowledge/myth-symbol/cosmology-cosmography.md:27 (165f292b95852459842900a091c6a40e1cd39b209b8fe2d84e62ecad6266ed2e); corpus/knowledge/linguistics/naming-systems.md:70 (d972a1d65e7a8fba34f44e1cd57019c175a8ed24671ef95f3e0ea3d1ed9ffb3d); corpus/knowledge/culture-material/craft-artisan-lexicon.md:44,54-65 (fd678d82fcc5134f5c5c0a65b15106b35cabe67bfd935d45df4fa16524f30288); parent pin reports/round-40/op/defect-queue-v2.json (dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907).",
   "verification": "Commands run by this seat at a01405d on 2026-10-19: (1) find corpus/knowledge -name '*.md' | wc -l -> 223; (2) ls corpus/knowledge/culture-material/*.md | wc -l -> 25; (3) wc -l over the 25 -> min 103, median 149, max 221, mean 150.2; (4) fence extraction -> 51 + 201 + 361 + 177 = 790 lines, 20,123 words, 240 table rows, 15 H2; sections-only 739 / 17,601 / 106,997; (5) grep -n 'ten times the available precision' reports/round-47/cov/C02-entry-b.md -> :98; (6) grep -rn 'cartograph' corpus/knowledge/ | wc -l -> 2 (cosmology-cosmography.md:102, mesoamerica-primary-sources.md:58); (7) grep -n 'archive of coups' corpus/knowledge/linguistics/naming-systems.md -> :70 (verbatim); (8) sed -n '44p;54p;65p' corpus/knowledge/culture-material/craft-artisan-lexicon.md -> steel row, ladder header, design rule; (9) sed -n '79p;184p;123p;137p;150p' reports/round-47/cov/C03-entry-c.md -> the quoted strings; (10) awk 'NR>=107 && NR<=152' ... | grep -c 'DR-CT-' -> 0; (11) sed -n '27p' corpus/knowledge/myth-symbol/cosmology-cosmography.md -> 'how the world is drawn (maps)'; (12) grep -c '^| ' over C03:92-104 -> 7 lines (header, separator, 5 form rows); (13) sha256sum of the four fragments -> the four digests above; (14) sha256sum reports/round-40/op/defect-queue-v2.json -> dfc9265d...; git status --porcelain on it -> empty; (15) sha256sum reports/round-47/calib/queue-successor-r47.json -> 9508b6aa...; parse of its rows -> 3 ids, no over-build row.",
   "incidence": {
    "verified": [
     {"round": 47, "claim": "C", "artifact": "cartography draft", "assembled_lines": 790, "body_lines": 739, "partition_max": 221, "defects": 9}
    ],
    "indicative_to_verify": [
     {"round": 42, "artifact": "reports/round-42/cov/C01-entry-1.md", "fragment_file_lines": 538, "note": "whole-fragment wc -l, not an assembled entry body; the draft was routed as a spare after a collision, so no entry-body measure is filed"},
     {"round": 44, "artifact": "reports/round-44/cov/C01-entry-draft.md", "fragment_file_lines": 485, "note": "whole-fragment wc -l; drafted a carried topic and did not land"}
    ],
    "excluded": "A long entry inside a declared band (C07 executable band 100-260, reports/round-47/cov/C07-contract-audit.md:354) or a table-dense entry whose audits ran on assembled bytes is not this class."
   },
   "findings": [
    {"id": "B1", "class": "routed-with-owner", "owner": "r48 C drafter", "evidence": "reports/round-47/cov/C02-entry-b.md:98; arithmetic 0.2 mm x 50,000 = 10 m, 200 m / 10 m = 20", "next_touch": "recompute every scale/precision ratio at drafting; write 20x or change 200 m to 100 m"},
    {"id": "B2", "class": "routed-with-owner", "owner": "r48 C drafter", "evidence": "reports/round-47/cov/C04-entry-header.md:115; grep -rn 'cartograph' corpus/knowledge/ | wc -l = 2 (cosmology-cosmography.md:102, mesoamerica-primary-sources.md:58)", "next_touch": "state the exact command and a count that command can produce; do not count :71 as a token hit"},
    {"id": "B3", "class": "routed-with-owner", "owner": "r48 C drafter + reviewer", "evidence": "reports/round-47/cov/C02-entry-b.md:36,:501; corpus/knowledge/linguistics/naming-systems.md:70 contains 'a map is an archive of coups' verbatim", "next_touch": "drop the correction; treat a claimed absence as a citation claim requiring a grep"},
    {"id": "B4", "class": "routed-with-owner", "owner": "r48 C drafter + audit author", "evidence": "reports/round-47/cov/C02-entry-b.md:248,:421; corpus/knowledge/culture-material/craft-artisan-lexicon.md:44 is the Steel (Japan) row; ladder at :54-65", "next_touch": "re-read the anchored line; an audit row repeating the body anchor is not verification"},
    {"id": "B5", "class": "routed-with-owner", "owner": "r48 C integrator", "evidence": "reports/round-47/cov/C03-entry-c.md:79,:184; typology is C01 section 4.1 (reports/round-47/cov/C01-entry-a.md:238)", "next_touch": "resolve all section pointers after assembly, against the assembled heading map"},
    {"id": "B6", "class": "routed-with-owner", "owner": "r48 C integrator", "evidence": "reports/round-47/cov/C01-entry-a.md:298; C02-entry-b.md:278 = section 8 provenance/charter, :347 = section 9 container-name fossil", "next_touch": "same as B5"},
    {"id": "B7", "class": "routed-with-owner", "owner": "r48 C drafter + example auditor", "evidence": "reports/round-47/cov/C03-entry-c.md:123,:137,:150; reports/round-47/cov/C14-example.md:11 (F-1 FAIL) and :123 (F-2); DR-CT- count in section 11 = 0", "next_touch": "one update rule stated once; name rule ids in the example; re-run the example audit on assembled bytes"},
    {"id": "B8", "class": "routed-with-owner", "owner": "r48 C drafter", "evidence": "reports/round-47/cov/C01-entry-a.md:90, C04-entry-header.md:115; corpus/knowledge/myth-symbol/cosmology-cosmography.md:27 defines cosmography as 'how the world is drawn (maps)'", "next_touch": "state the boundary against :27 in one sentence; keep the :71/:102 disclaimers as supporting evidence"},
    {"id": "B9", "class": "routed-with-owner", "owner": "r48 C drafter", "evidence": "reports/round-47/cov/C03-entry-c.md:95-103 (5 form rows) vs reports/round-47/cov/C01-entry-a.md:238-249 (8 forms)", "next_touch": "cover all eight forms or retitle 'five common forms'"}
   ],
   "proposed_control": {
    "status": "proposed - not landed; no durable entry-quality control exists at a01405d (grep -rln 'partition band|length in partition' tools/ -> no match; the only checker is inline at reports/round-47/cov/C07-contract-audit.md:354). Ca05 owns the README heading control; this is entry quality and is a different object.",
    "check": "Before any corpus entry apply: (a) extract the assembled fenced body and assert its line count is inside the target band (culture-material: 103-221 live, <=250 round tolerance) and that the count is measured on assembled bytes, not fragment files; (b) run the nine-shape checklist (B1 arithmetic recompute, B2 command/count reproducibility, B3 quote-presence grep, B4 anchored-line re-read, B5/B6 section-pointer resolution, B7 single-rule example, B8 boundary-vs-competing-definition, B9 table-completeness vs typology); (c) require one named non-author to review the assembled bytes after the fixes, not the pre-fix fragments.",
    "owner": "integrator (apply-time acceptance); the check is a candidate gate extension for the next build round - this row does not claim it landed."
   },
   "reclass_gates": [
    "G1 landed bytes: corpus/knowledge/culture-material/cartography-and-mapmaking.md exists at the landing commit; the landed file's line count is inside the declared band (<=250, target 103-221) and is pasted from wc -l on the landed path.",
    "G2 arithmetic: every scale/precision/date ratio in the landed entry is recomputed in a filed verifier fragment; B1's 10 m / 200 m shape does not recur.",
    "G3 citations: every in-corpus path:line in the landed entry resolves to the described content, re-read at the landing commit; B2/B4 shapes do not recur; the naming-systems.md:70 quote is exact.",
    "G4 structure: every section pointer resolves against the landed heading map (B5/B6); the worked example states one update rule and names its rule ids (B7); the form table's row count equals the typology's (B9); the cosmography :27 boundary is stated (B8).",
    "G5 independent read: a non-author review of the assembled landed bytes records B1-B9 as absent, with commands.",
    "G6 filing: a NEW closing row (fixed-with-evidence) carries G1-G5's pasted outputs; this row is never edited in place."
   ],
   "class_boundary": "This row dispositions ENTRY QUALITY for one instance and the pattern it exposes. It does not absorb: the r43/r44 stale-premises class (reports/round-47/calib/queue-successor-r47.json row r43-stale-premises), the resolver soft-wrap edge (same successor, r44-resolver-hyphen-after-blank), or the MANIFEST dual-schema row. If r48 Ca06 mints a combined process-defect row covering both build quality and stale premises, this row is the canonical entry-quality member and must be cited, not duplicated; the integrator picks one canonical id and records the other as an alias. No census double-count.",
   "sources_not_consulted": "No external bibliographic source was checked (no network at seat time). This row makes no claim about any external work; the r47 draft's Tier B shelf remains (to-verify) and is outside this disposition."
  }
 ],
 "application_gates": [
  "A1 parent pin: sha256sum reports/round-40/op/defect-queue-v2.json == dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907 and git status --porcelain on it is empty.",
  "A2 parse: the fenced JSON parses; schema == kotodama-defect-queue-successor-v1; round == 48; baseline_commit == a01405d; rows length == 1; findings length == 9; every rows[].class in the declared vocabulary; no empty id/class/owner/reason/next_touch/evidence/verification.",
  "A3 anchors: re-run the live checks named in verification items 5-12; all must reproduce before the row is filed.",
  "A4 immutability: apply as a new file reports/round-48/calib/queue-successor-r48.json; do not edit the parent or the r47 successor (sha 9508b6aa...); no corpus byte is touched by this row.",
  "A5 reclass discipline: G1-G6 only; a fixed claim without pasted measurements is inadmissible, and this row is never flipped in place."
 ],
 "census_note": "Records, not a merged live count: parent 38 rows + r47 successor 3 rows + this row 1 = 42 filed successor-line rows if all three artifacts are read together. The parent is the pinned baseline; successors are append-only deltas and must not be summed into the parent in place."
}
```

---

## 5. Dedupe and boundary (who else touches this)

| Other artifact | Relationship | Handling |
|---|---|---|
| `reports/round-47/calib/queue-successor-r47.json` (3 rows) | Predecessor; rows are stale-premises, resolver edge, MANIFEST schemas | This row does not restate any of them; it is appended as a fourth successor-line record |
| r48 **Ca06** (combined process-defect row for build quality + stale premises) | Overlapping class | One canonical id. If Ca06 mints a combined row, cite `r47-entry-overbuild-defect-class` as its entry-quality member; do not count two rows for one class |
| r48 **Ca05** (README heading-count control) | Adjacent but different object | Ca05 asserts one H1 in `corpus/README.md`; this row asserts entry length/quality. Neither substitutes for the other |
| r48 **Ca01** (README dup-heading removal) | Calibration surface, not entry quality | No overlap; the README duplicate H1 is a live index defect, while this row is about draft discipline |
| r48 **C** (right-sized redraft) | The reclass path | G1-G6; this row stays `routed-with-owner` until the landed measurements exist |

---

## 6. What I did not verify

- **The nine fixes.** I verified the nine *defects* exist; I did not author or test their repairs. B7's fix in particular requires a re-run of the C14 example audit, which this seat did not run.
- **r42/r44 over-build incidence.** The 538- and 485-line figures in `incidence.indicative_to_verify` are whole-fragment `wc -l`, not assembled entry bodies. They are marked to-verify and are not counted in the verified incidence.
- **Any external bibliographic claim.** No network; the r47 Tier B shelf stays `(to-verify)` and is outside this row.
- **The r48 C draft.** At my write cut `reports/round-48/cov/` held C02, C04 and M01 fragments only; no entry body existed to measure, so no right-sized-length claim is made for r48 here.
- **The README fix and heading control.** Other seats (Ca01/Ca03/Ca05); I did not touch or verify them.

---

## 7. Commands and write-surface statement

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ wc -l corpus/knowledge/culture-material/*.md | sort -n
min 103 / median 149 / max 221 (25 files; mean 150.2)
$ python3 (fence extraction over C04/C01/C02/C03)
790 lines (51 head + 201 + 361 + 177); 20,123 words; 240 table rows; 15 H2
body only: 739 lines / 17,601 words / 106,997 chars
$ grep -n 'ten times the available precision' reports/round-47/cov/C02-entry-b.md
98: ...
$ grep -rn 'cartograph' corpus/knowledge/ | wc -l
2
$ grep -n 'archive of coups' corpus/knowledge/linguistics/naming-systems.md
70: ... a map is an archive of coups.
$ sed -n '44p;54p;65p' corpus/knowledge/culture-material/craft-artisan-lexicon.md
:44 Steel (Japan) ... ; :54 ladder header ; :65 design rule
$ sed -n '79p;184p;123p;137p;150p' reports/round-47/cov/C03-entry-c.md
the quoted typology refs and update-rule lines
$ awk 'NR>=107 && NR<=152' reports/round-47/cov/C03-entry-c.md | grep -c 'DR-CT-'
0
$ sed -n '27p' corpus/knowledge/myth-symbol/cosmology-cosmography.md
... Cosmography = the projected, inhabited version: how the world is drawn (maps), ...
$ sha256sum reports/round-40/op/defect-queue-v2.json
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907
$ sha256sum reports/round-47/calib/queue-successor-r47.json
9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58
$ grep -rln 'partition band\|length in partition' tools/
(no output)
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223; 0 missing; 0 topic_mismatch; totals_line 223; footer 25/26/25/29/24/94; exit 0
```

**Write surface:** this file only — `reports/round-48/calib/Ca02-overbuild.md`. No `corpus/**`, `tools/**`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged; no git mutation, install, or network; no `reports/round-*/run-validation.py` executed in-tree. The successor JSON is a **fenced draft**; the integrator writes `reports/round-48/calib/queue-successor-r48.json`.
