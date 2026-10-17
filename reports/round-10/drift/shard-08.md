# R10-F08 — Drift shard 08: `SKILL.md` lines 141–160

- worker: FRESHNESS R10-F08 (drift shard 08); deliverable: this file only. Author-side receipt, **not an independent promotion verifier** (F19 re-runs a sample independently).
- date: 2026-10-17 (run window ~18:25–18:29 local, -03:00). Lane: `kotodama-shokunin`.
- revisions: declared round-10 baseline `9dc18ec1339bffd6f81e74f1a5742464ef578749`; live HEAD at run time `e3a1ec9435787328ac9f828f96cb6390e4916b8f` (HEAD differs only by the three round-10 availability-attempt commits). `SKILL.md` is **unchanged** between baseline and worktree: sha256 `2bce468db89be47db7009cce1537538e574c3897da1a6097302dc56c0351df1b` (C17; `git show 9dc18ec:SKILL.md` gives the same). Sibling workers were mid-wave (`corpus/README.md` and round-10 dirs dirty); nothing in this shard reads those surfaces.
- source region: `SKILL.md:141-160`, sha256 `eae1ae547454e035de205b93f8e65081b64a732a6fe6869b7113829345a15b00` — identical at `9dc18ec` and in the worktree (C11, C16).
- environment: `TMPDIR=$PWD/.scratch`; no `/tmp` writes. No web citations exist in this line range, so no access attempt was required (stated, not skipped).

## 1. What lines 141–160 contain, and the runnable set

| Lines | Content |
|---|---|
| 141–142 | tail of the `corpus/knowledge/verification/` partition description (gate specifications, citation/provenance formats, calibration registry, to-verify triage, real-world-inspiration boundaries) |
| 143–145 | `corpus/knowledge/civilizations/` — the count claim "92 earlier-civilization bases, each coupling … language, writing, myth, symbols, era model, costume, and naming, with provenance cautions" |
| 147–153 | "Using the evidence" prose: appended-errata instruction; `corpus/lessons/supplement-opencode-1/sources/` description ("supported, contradicted and unresolved claims with passage and access limits"); two aphorisms (catalogue record ≠ unread contents; disappearing uncertainty marker ≠ verified claim) |
| 155–160 | evidence-table header + rows 1–4, citing `reports/supplement-opencode-1/{21,22,04,23,24}-*.md` |

The range contains **no literal shell commands and no URLs**. The runnable set is therefore the derived checks below: the count claim, the two path/partition claims, the sources-dir field census, the errata instruction, and the four table rows' cited paths and subject matter.

## 2. Receipts (all commands re-run 2026-10-17; output sha256 = sha256 of captured stdout)

| # | Command (as run, from lane root) | Exit | Output sha256 | Output |
|---|---|---|---|---|
| C1 | `ls corpus/knowledge/civilizations/*.md \| wc -l` | 0 | `e3d6c4d4599e00882384ca981ee287ed961fa5f3828e2adb5e9ea890ab0d0525` | `94` |
| C2 | `git ls-tree -r 9dc18ec -- corpus/knowledge/civilizations/ \| wc -l` | 0 | `e3d6c4d4599e00882384ca981ee287ed961fa5f3828e2adb5e9ea890ab0d0525` | `94` (same at baseline) |
| C3 | `head -1 corpus/knowledge/civilizations/*.md \| grep -ic 'primary sources'` | 0 | `d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35` | `2` |
| C4 | `grep -l '^- couples:.*naming' corpus/knowledge/civilizations/*.md \| wc -l` | 0 | `8241649609f88ccd2a0a5b233a07a538ec313ff6adf695aa44a969dbca39f67d` | `92` |
| C5 | `ls corpus/knowledge/verification/ \| wc -l` | 0 | `3fdba35f04dc8c462986c992bcf875546257113072a909c162f7e470e581e278` | `13` |
| C6 | `ls corpus/lessons/supplement-opencode-1/sources/*.json \| wc -l` | 0 | `e629fa6598d732768f7c726b4b621285f9c3b85303900aa912017db7617d8bdb` | `15` |
| C7 | `for f in 21-phonology-review.md 22-label-representation.md 04-name-correction.md 23-myth-coverage.md 24-costume-coverage.md; do test -f reports/supplement-opencode-1/$f && echo OK \|\| echo MISSING; done \| sort \| uniq -c` | 0 | `aa714bdea613f3c80c4877122917866aec2e03fb2f921ac4d38f59aa36b0cc2b` | `5 OK` (no MISSING) |
| C8 | `grep -ril errata corpus/knowledge/ \| wc -l` | 0 | `e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683` | `6` (all under `linguistics/`) |
| C9 | `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge \| python3 -c "…collections.Counter(f['path'].split('/')[0])…"` | 0 | `fb50d18941127a64664e50483600a7883002dbfd23e6fe13a6c044d443fe7248` | `{'civilizations': 94, 'culture-material': 16, 'linguistics': 16, 'myth-symbol': 16, 'synthesis': 24, 'verification': 13}` |
| C10 | audit census over `sources/*.json` (verdicts + missing fields) | 0 | `d071d209643870b9cf52ca562f75d70c3ff03959de406cd6bd7989fabac1eaa9` | `161 {'supported': 130, 'unresolved': 21, 'contradicted': 10} no_excerpt 10 no_locator 4 no_access_limit 0` |
| C11 | `sed -n '141,160p' SKILL.md \| sha256sum` | 0 | — | `eae1ae547454e035de205b93f8e65081b64a732a6fe6869b7113829345a15b00` |
| C12 | row-subject greps: `grep -c 'A-NEUTRAL' 21-…; grep -c 'native_form' 22-…; grep -c 'coda' 04-…; grep -c 'ledger' 23-…; grep -c 'ledger' 24-…` | 0 | `fbe69f0d10d9946dc4a72b9c2ae8feae80bbd24e7fc60232405a1a7c02e37f93` | `21 / 12 / 16 / 7 / 8` |
| C13 | `grep -ril 'provenance caution' corpus/knowledge/civilizations/ \| wc -l` | 0 | `8241649609f88ccd2a0a5b233a07a538ec313ff6adf695aa44a969dbca39f67d` | `92` (set ≠ C4's set, see §3.2) |
| C14 | files lacking `naming` in `- couples:` | 0 | `35f3eb0057dc97b97acbb706113ea7f7f1eebc327cb51f663771101d1602ed98` | exactly the two `*-primary-sources.md` files |
| C15 | `for key in linguistics myth-symbol culture-material; do …; done` | 0 | `21393eec87ab740f191f199dbf04d8e21e0f7558d3a228bab6fd1792e7fecabd` | `linguistics=94 myth-symbol=94 culture-material=94` |
| C16 | `git show 9dc18ec:SKILL.md \| sed -n '141,160p' \| sha256sum` | 0 | — | `eae1ae54…` (region unchanged since baseline) |
| C17 | `sha256sum SKILL.md` | 0 | — | `2bce468d…` (worktree = baseline) |

Cited-file pins (sha256, full): `21-phonology-review.md` `469732f3…b775f089383a87`, `22-label-representation.md` `5493b3f7…26bc88bdeacb3364`, `04-name-correction.md` `7f82bdda…771c246e6596833a`, `23-myth-coverage.md` `8decec42…7e2ea3a0db987c792`, `24-costume-coverage.md` `6e774ff3…fdcdf36e130d56d`.

## 3. Item verdicts

### 3.1 Lines 141–142 — verification partition description → **current**
`corpus/knowledge/verification/` holds 13 files (C5) and every described category is present: gate specifications (`costume-era-consistency-gate.md`, `myth-consistency-gate.md`, `naming-collision-gate.md`, `phonology-sanity-gate.md`, `gate-frozen-run-standard.md`), citation/provenance formats (`citation-format-and-source-registry.md`, `provenance-audit-ledger-format.md`), calibration registry (`calibration-registry.md`), to-verify triage (`to-verify-triage-protocol.md`), real-world-inspiration boundaries (`real-world-inspiration-boundaries.md`); plus `internal-consistency-audit.md`, `lexicon-coverage-audit.md`, `verification-method-overview.md`. No command is cited here; no drift surface beyond the listing.

### 3.2 Lines 143–145 — "92 earlier-civilization bases" → **current** (92 = 94 files − 2 source maps)
The directory holds **94** `.md` files at baseline and today (C1, C2, C9), not 92 — but the lane's established reading is "92 bases plus two source maps", recorded at `SCORECARD.md:31` (`civilization partition remains 92 bases + two source maps, not 94 verified civilizations`), `LOG.md:2431`, `reports/round-5/kotodama.md:73`, and `reports/supplement-opencode-1/kotodama.md:111-112`. Independent discriminators re-run now:
- C3: the two files whose first line carries "primary sources" are exactly `africa-primary-sources.md` and `mesoamerica-primary-sources.md`; both self-describe as bounded source maps, "not a continent-wide cultural profile" / "a reference map for the four Mesoamerican bases … never fictional canon".
- C4/C14: exactly 92 files list `naming` among their `- couples:` targets; the only two that do not are those same two maps. (C15: all 94 list `linguistics`/`myth-symbol`/`culture-material` — the maps couple to method partitions, not to a naming system.)
- C13: 92 files carry the phrase "provenance caution" — a *different* 92-set: `taino.md` uses the variant heading "Provenance, standard editions, and cautions" (false negative) while `mesoamerica-primary-sources.md` mentions "provenance cautions" in its topic line (false positive). Count coincidence only; the C4 discriminator is the reliable one.
- C9 corroborates the partition census 16/16/16/24/13/94 against the SCORECARD counting command.

Verdict: **current**, no fix required. Reader note for the ledger: `SKILL.md:143` does not carry the "plus two source maps" qualifier that SCORECARD has, so a file count of the directory reads 94. That is a clarity question, not staleness; any clarifying phrase is a SKILL.md edit outside this shard's write scope (flag for F15–F18/F14 if wanted).

### 3.3 Line 149 — "Read each entry's appended errata" → **current** (instruction, conditionally exercised)
Errata exist in exactly 6 knowledge entries, all in `corpus/knowledge/linguistics/`: `phonetics-phonology.md`, `sociolinguistics-registers.md`, `semantic-fields-lexicon-building.md`, `color-terminology.md`, `orality-formulaic-language.md`, `kinship-terminology.md` (C8). In each, the errata section is the **last** heading (e.g. `phonetics-phonology.md` last heading at line 314 of 325; `color-terminology.md` at 114 of 116), i.e. genuinely appended, dated 2026-10-17, with preserved original bytes and audit-record pointers. No civilization-partition entry carries an errata section — no append was made there, so the instruction is simply unexercised for those 94 entries; it is not falsified.

### 3.4 Lines 150–151 — `sources/` "records supported, contradicted and unresolved claims with passage and access limits" → **current with note**
C6+C10 over the 15 JSON files: **161** audit rows, verdict vocabulary exactly `supported` 130 / `unresolved` 21 / `contradicted` 10 — the three named statuses are the whole vocabulary. `access_limit` is present on **161/161** rows. `source_excerpt` (the passage) is absent on 10 rows and `source_locator` on 4 — **all of them `unresolved`**, and each carries a `retrieval_status` naming the block (`blocked_http_429`, `blocked_http_403`, `blocked_bot_verification…`, etc.) with the access limit stating what was and was not retrieved (e.g. `meso-13` Cambridge Core 429; `meso-14` ScienceDirect 403). So "with passage and access limits" holds for every row where a passage was retrievable; blocked rows record the access limit and no passage by construction. The prose is accurate as written; the note is for readers counting excerpts.

### 3.5 Lines 152–153 — the two aphorisms → **non-executable, no drift surface**
"A catalogue record establishes catalogue metadata, not the unread book's contents" and "A disappearing uncertainty marker is not a verified claim" are principles with no command and no count. They are instantiated by the `access_limit`/`retrieval_status` fields verified in §3.4 (161/161) and by the to-verify discipline in the verification partition; recorded here as checked-by-instantiation, nothing to re-run.

### 3.6 Lines 155–160 — table rows 1–4 → **current**
C7: all five cited paths exist. C12: each row's subject matter is present in its cited file — `A-NEUTRAL` in `21-phonology-review.md` (21 hits), garment-label/`native_form` representation in `22-label-representation.md` (12), the coda-rule repair in `04-name-correction.md` (16), and ledger-coverage critiques in `23-myth-coverage.md` (7) and `24-costume-coverage.md` (8). This is subject-matter presence at file level, not a full re-read of the cited reports (limit in §5).

## 4. Stale dispositions

- **stale-fixed: 0. stale-documented: 0. current: 5 items (3.1–3.6).**
- Two current-with-note items, neither requiring a fix: the 92-vs-94 reader note (§3.2) and the excerpt-less unresolved rows (§3.4). Neither is a stale claim, so nothing was fixed or documented-as-stale.
- No file in this shard's range was edited: the deliverable is this receipt only.

## 5. Limits and handoff

- Author-side run; F19 should independently re-run C1, C3, C4, C8, C9, C10 (and optionally C7) from the lane root — each is cheap and deterministic; C9/C10 depend on `tools/source-audit-inventory.py` and the `sources/*.json` files, both at the pinned revisions above.
- Content checks are subject-matter greps, not full re-reads; the cited reports' internal claims were audited by their own rounds (`reports/round-9/freshness/`), not re-adjudicated here.
- For the F14 ledger: this shard contributes no stale items; the C9 partition census and C10 audit census are the reusable pins, and the §3.2 discriminator (92 = 94 − 2 maps) should be carried into the ledger note so the 94-file count is never mistaken for drift.
