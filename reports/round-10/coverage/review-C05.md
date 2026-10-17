# R10-C15 — Reviewer of worker C05's myth-symbol entry (author-side review)

- reviewer scope: `reports/round-10/coverage/review-C05.md` only. No corpus, ledger, bookkeeping, canon, or promotion edits. Author-side review evidence only; not an admission decision and not independent promotion verification.
- assignment: `reports/round-10/targets.json` → `R10-C11..C20` ("Ten reviewers: one per authored entry (poll for it, max 20 min): verify frontmatter completeness, source resolvability (re-run the cited command or open the cited path/URL), no filler, no duplication of an existing entry; verdict `reports/round-10/coverage/review-<id>.md`").
- C05 is the second myth-symbol author (`R10-C01..C10` seat split: linguistics ×3 = C01–C03; myth-symbol ×3 = C04–C06; culture-material ×2 = C07–C08; verification ×2 = C09–C10). Expected outputs: fragment `reports/round-10/coverage/C05.md` naming one new `corpus/knowledge/myth-symbol/<slug>.md` entry, per `targets.json` ("read corpus/README.md known-gaps + the partition's existing entries + round-8/9 receipts; pick ONE distinct gap (derive filename slug from the gap; on collision append -b); write corpus/knowledge/<partition>/<slug>.md with full frontmatter and a decision-record section").
- round-10 declared baseline revision: `9dc18ec1339bffd6f81e74f1a5742464ef578749` (`reports/round-10/claims.json`); worktree HEAD at review open: `e3a1ec9435787328ac9f828f96cb6390e4916b8f` ("round-10: availability attempt 3 — opencode-go-5 dry; keys 3/4/5 unprovisioned, retrying key 1"). `git diff --name-only 9dc18ec1339bffd6f81e74f1a5742464ef578749 -- corpus/knowledge` is empty at review open, so the committed corpus equals the declared baseline.
- date: 2026-10-17. Poll window opened 18:26:37 local (UTC-03:00; 21:26:37Z), background poller 60 s cadence, 20 min cap → 18:46:37 local, watching both `reports/round-10/coverage/C05.md` and `corpus/knowledge/myth-symbol/` for a 17th file, so a landed entry is caught even if its fragment is late.

## 0. Review status

At review open (18:26:37–18:31:51 local) `reports/round-10/coverage/` held no C05 fragment, and `corpus/knowledge/myth-symbol/` still held exactly its 16 committed files (mtimes 17:25–17:26, pre-round-10): C05's entry is **not yet inspectable**. The wave is nevertheless live — observed in the same window: sibling reviewer files `review-C01.md`, `review-C04.md`, `review-C06.md`, `review-C08.md`, `review-C10.md`, `audit-unchanged.md`, `audit-ling-verif.md`; `reports/round-10/drift/shard-01/02/04/06/07/08/09/10/14.md`; `reports/round-10/findings-tracker.json`; and `corpus/README.md` modified — so sibling C/F/O shards are working. Per the assignment this review polled up to 20 minutes (closing 18:46:37 local); the landed-bytes review is §3. C05's entry landed at 18:38 local as `corpus/knowledge/myth-symbol/divination-omen-systems.md` (revised by the author at 18:41:20; current sha256 `6666e7db…`), and C05's fragment landed at 18:42 local — attribution fragment-confirmed (§3.1).

Round-10 context (from `git log` and `reports/round-10/availability-attempt-*.json`): attempts 1–3 returned HTTP 402 "Insufficient account funds" on opencode-go keys 3/4/5 with zero workers launched ("all workers failed at launch, no work performed"); attempt 4 retries key 1 within the sanctioned provider (this run). A late or absent C05 is a scheduling/availability fact, not evidence about worker quality, and this review does not predict it.

## 1. Pre-landing method (checks prepared, no entry to apply them to yet)

The four mandated checks, with their exact instruments, frozen here so the landed review is a mechanical application:

1. **Frontmatter completeness** — criterion: the house profile all 16 committed myth-symbol files use (`topic` / `sources` / `couples` / `source` / `verified-at` / `recheck`; round-8 metadata sweep added the `source`/`verified-at`/`recheck` trio, re-audited by round-9 V09), each present exactly once in the head block (text before the first `## ` heading), in field order, non-empty, `verified-at` dated and scope-bearing, every `couples` reference resolving to a real file. Instruments: `.scratch/c15-field-census.py` (validated against `trickster.md`: 6/6 fields exactly once, head-block, order OK, conforming=true) plus `python3 tools/gates/provenance-audit.py <newfile>`.
2. **Source resolvability** — open each cited repo path and check it exists and supports the cited use; re-run each cited runnable command and record exit + output; give every cited URL a documented access attempt; round-8/9 receipts cited by path count as sources per `claims.json` C ("round-8/9 receipts and existing corpus cross-references count as sources when cited by path"). Instrument: `.scratch/entry-check.sh` (path/URL extraction) plus direct `ls` / `python3` / fetch. Bibliographic citations (author + year, no path/URL) are checked for identification specificity, not full-text retrieval — note no committed myth-symbol entry cites a URL (`grep -ho 'https\?://[^ )>]*' corpus/knowledge/myth-symbol/*.md | wc -l` → 0). Non-resolving items: verdict `to-verify`, never silently passed.
3. **No filler + decision-record presence** — the entry must name the gap it fills; the gap must be real (a myth-symbol topic absent from the 16 committed entries and not already satisfied by `corpus/README.md` known-gaps) and the entry must deliver on it per `corpus/QUALITY.md` (provenance, calibration, coupling, usability, canon hygiene). `targets.json` additionally requires "a decision-record section": no committed myth-symbol entry carries a literal decision-record heading (`grep -rn -i "decision record\|decision-record" corpus/knowledge/myth-symbol/` → 0 hits, 18:29 local), so this is a round-10 addition the entry must actually deliver; absence is a finding against the C claim, not a style note.
4. **No duplication** — compare the new entry's slug, title, and topic against the committed baseline of all 179 entries and specifically against the 16 myth-symbol entries; 8-gram body-shingle Jaccard screen via `.scratch/c15-shingle.py` (validated against `trickster.md`: max Jaccard 0.0027, i.e. the screen discriminates; a real near-duplicate would rank near the top). A near-duplicate of any existing entry is a finding; a slug collision without the `-b` suffix is a naming defect.

Baseline facts recorded at open (evidence for checks 1, 3, 4):

- `find corpus/knowledge -name '*.md' | wc -l` → `179`; `ls corpus/knowledge/myth-symbol/ | wc -l` → `16` (18:28 local, HEAD `e3a1ec9`); all 179 titles captured to `.scratch/all-titles-r10c15.txt` (179 lines).
- `python3 tools/gates/provenance-audit.py corpus/knowledge/myth-symbol/` → `INFO scan: files=16 marks=9 mark-lines=9 findings=0 blocked=0`, exit 0 (18:28 local) — post-landing re-run compares against this line.
- `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → `"files": 179` (18:28 local).
- `corpus/README.md` at open: `## myth-symbol/ (16)` heading with exactly 16 index rows (script, 18:28 local); `## Known gaps (frontier)` at L213+ names lane-wide gaps (round-5/6/7 residuals, D2/D3 status, gate/parser debts, cultural-permission/name-screening/lore-receipt/independent-promotion limits). A C05 gap must be a *partition* gap (a real myth-symbol topic absent from the 16), not merely an evidence-state note.
- myth-symbol slugs at open: `animal-symbolism`, `celestial-symbolism-calendars`, `color-symbolism`, `comparative-frameworks`, `cosmology-cosmography`, `creation-myths-taxonomy`, `flood-traditions`, `hero-journey-variants`, `motif-index-usage`, `myth-folktale-genres`, `myth-ritual-theories`, `number-symbolism`, `pantheon-archetypes`, `ritual-liminality`, `symbolism-synthesis-method`, `trickster`.
- Per-file `sha256sum corpus/knowledge/myth-symbol/*.md` captured to `.scratch/c15-myth-sha.txt` (16 lines; aggregate `sha256sum` of that list = `9a8b3168da463cf2af876b33124d926fbd3eae272d55f7ef4b93e2389904c512`, 18:32 local) so a post-landing change to an existing file is distinguishable from the new file. This aggregate matches reviewer C16's independent capture (`reports/round-10/coverage/review-C06.md` §1, 21:28:37Z) — the partition was identical under both captures.
- `git status --short` at open showed the shared live edits of sibling shards (` M corpus/README.md`, ` M reports/round-9/validation.json`, untracked `reports/round-10/coverage/`, `reports/round-10/drift/`, `reports/round-10/findings-tracker.json`) — observed read-only, not this seat's writes, not dispositioned here.

## 2. Observations outside this seat (reported, not dispositioned)

Recorded read-only for the parent, since the reviewer seat owns no bookkeeping write:

- The worktree at open carries live sibling edits to shared files (`corpus/README.md` one-row rewrite of `africa-primary-sources.md`; `reports/round-9/validation.json` modified). Round-10's F targets say "never rewrite filed report bytes — corrections are new entries"; whether the `reports/round-9/validation.json` modification is an authorised F-seat regeneration or an unlogged overwrite is the parent's call, not this seat's.
- Reviewer siblings C14/C16/C18/C10 filed pre-landing reports with their poll windows still open; their landed verdicts (or absence verdicts) are theirs to append.

## 3. Landed review

Appended 2026-10-17 ≈18:42 local (UTC-03:00; ≈21:42Z). All commands below run from the lane root on the live tree.

### 3.1 What landed, and attribution

- **Entry (reviewed), revision 2 = current bytes:** `corpus/knowledge/myth-symbol/divination-omen-systems.md` — 48,358 bytes, 218 lines, mtime 18:41:20 local, sha256 `6666e7dbd5cc5a4bd9833b3e842843854af8ef7b365396c6d1737aac8cbf2ba4` (captured 18:42 local). Revision 1 was 48,135 bytes, sha256 `30d7ccc641d413631a3eb1a5eb15a05957dd5c0072df6d80a10726306df09dde` (captured 18:39 local); the author revised the file at 18:41:20 — the `../../verification/…` refs of F-1 are corrected in revision 2 (verified: `grep -c '\.\./\.\./verification'` → 0). Untracked new file (matches the runner's `discover_new_entries` set).
- **Attribution — fragment-confirmed.** Fragment `reports/round-10/coverage/C05.md` landed 18:42 local (11,892 bytes) and states: "seat: **R10-C05** (round 10 …) Deliverable: one new `corpus/knowledge/myth-symbol/<slug>.md` + this fragment"; "**File**: `corpus/knowledge/myth-symbol/divination-omen-systems.md`". Sibling attribution also stands independently (C04 = `direction-symbolism.md`, C06 = `plant-symbolism.md`, each claimed by its own fragment). The fragment's own after-state digest line cites the same revision-2 sha256 `6666e7db…`.
- **Fragment:** landed 18:42 local, read in full for this section. Its self-reported counts were cross-checked where independently reproducible (below); its remaining self-report is author-side evidence, not re-verified by this seat.

### 3.2 Poll receipts

- Poller 1 (`bash-vcxcbn0n`): 18:26:37–18:36:37 local, 60 s cadence (harness 600 s cap); ticks 18:26:37…18:33:37 all `frag=none new_myth=none`; tick 18:34:37 caught `direction-symbolism.md` + `plant-symbolism.md` (the two sibling myth entries). No C05 fragment in any tick.
- Poller 2 (`bash-q0lqmqgn`): 45 s cadence; 18:36:53 `frag=none new_myth=none`; **18:37:38 `frag=none new_myth=divination-omen-systems.md`** (first sighting); 18:38:23–18:41:23 unchanged; **18:42:08 `frag=yes`** → poller exit `LANDED: C05.md + divination-omen-systems.md`.
- Direct checks 18:40–18:41:17: `ls reports/round-10/coverage/C05.md` → absent (pre-landing); 18:42:08 → present. Poll window closed early by the landing condition at 18:42:08 local (cap would have been 18:46:37).

### 3.3 Mechanical checks (the round's own acceptance runner)

Instrument: `.scratch/c15-runner-check.py` imports `reports/round-10/run-validation.py` (sha256 prefix `23d6dc09002fe18c`, captured 18:41 local) and calls its `entry_checks()` on the entry — the exact function the C-claim acceptance runs (`run-validation.py:349-373`; failure strings at `:432-442`).

```
python3 .scratch/c15-runner-check.py corpus/knowledge/myth-symbol/divination-omen-systems.md
```

Result on **both revisions** (rev 1 at 18:39, rev 2 at 18:42) — **all four runner checks pass**:

| runner check | result |
|---|---|
| `missing_frontmatter` (topic, sources, verified-at, recheck, couples; non-empty) | `[]` |
| `gap` (named gap: clause or heading) | `true` |
| `decision_record` (heading matching `decision[- ]record` + body) | `true` — `## 10. Decision record`, DR-DIV-01…10 |
| `locators` (existing `corpus/|tools/|reports/|examples/` path or URL) | 17 existing repo paths |

Supporting instruments on rev 2: field census (`.scratch/c15-field-census.py`) → all six house fields exactly once, head-block (ends at first heading L30), in order, non-empty, `verified-at` dated and scope-bearing → `conforming=true`. Provenance gate on the file: `python3 tools/gates/provenance-audit.py corpus/knowledge/myth-symbol/divination-omen-systems.md` → `files=1 marks=0 mark-lines=0 findings=0 blocked=0`, exit 0 (same on rev 1). Full-partition gate: at 18:37 local (18 files) `files=18 marks=22 mark-lines=22 findings=0 blocked=0`; at 18:42 local (19 files, post-revision) `files=19 marks=20 mark-lines=20 findings=0 blocked=0` — exit 0 both times; baseline 16/9/9/0/0; no finding introduced by this entry. (The 22→20 movement is sibling revisions, not this entry: the file's own count is 0 marks in both revisions.)

### 3.4 Source resolvability

- **Repo paths (rev 2).** Refcheck sweep: **0 unresolved** among the file's local path tokens — every `corpus/…`-anchored path, every sibling-relative (`./`, `../`) path, and all three cited round-8/9 receipts resolve. Revision 1 carried **five broken refs** `../../verification/…` (L25, L28, L159, L178, L216) resolving to non-existent `corpus/verification/`; **the author corrected them in revision 2** (finding F-1, now resolved — see §3.7).
- **Round-8/9 receipts cited by path** (count as sources per `claims.json` C): `reports/round-8/metadata/m09-myth.md`, `reports/round-9/metadata/v09-myth.md`, `corpus/lessons/round-4-audit/myth-symbol.md` — all three exist (checked, both revisions).
- **URLs.** No URL is cited (`https?://` token count 0); the entry's own `verified-at` states this and says no link check was owed — consistent, nothing to access.
- **Quoted text verified.** The entry quotes the gate rule "Do not expose restricted ritual knowledge to fill a table. Mark an access boundary and choose a less extractive comparison." and cites `myth-consistency-gate.md §2` — found verbatim at `corpus/knowledge/verification/myth-consistency-gate.md:34`, inside §2 "Minimum review packet" (heading L20, next heading L36). Citation accurate.
- **Before-state claims independently re-verified.** The entry's quoted pre-write measurements all reproduce: partition count 16 (my 18:28 capture: 16); gate `files=16 marks=9 mark-lines=9 findings=0 blocked=0` (my independent 18:28 run: identical line); aggregate `sha256sum corpus/knowledge/myth-symbol/*.md | sha256sum` → `9a8b3168da463cf2af876b33124d926fbd3eae272d55f7ef4b93e2389904c512` (my independent 18:32 capture: identical; also identical to reviewer C16's capture in `review-C06.md` §1). The entry's §1 gap sweeps re-run: `grep -l "^- topic:.*divination" corpus/knowledge/myth-symbol/*.md | wc -l` → 1 (only the new entry; 0 before, as claimed); `grep -rc "divination"` → `celestial-symbolism-calendars.md:2`, `motif-index-usage.md:1` (as claimed), plus the new entry 31; `grep -rl "divination" corpus/knowledge/civilizations/ | wc -l` → 14 (as claimed).

### 3.5 No filler — the gap is real and delivered

- The entry names its gap in the topic line and §1: the partition owns symbol *registers* and the *narrative* side, but no entry owned the **reading technologies** (question → technique → closed sign space → licensed reader → prescription). Independent check confirms the gap was real at authoring time: no myth-symbol topic named divination; the corpus carried divination only as scattered data (14 civilization files) and two passing mentions in the partition.
- The entry delivers on the gap rather than restating neighbours: §2 core frame, §3 fourteen-family technique typology with real exemplars, §4 interpretive engine, §5 institutions/licence, §6 omen archives, §7 the word-omen channel (the lane's namesake ground), §8 boundary table, §9 worked design example, §12 build order and failure modes — decision tables and a build protocol, not an essay (`QUALITY.md` item 4).
- Calibration (`QUALITY.md` item 2): §11 flags contested/discredited items with reasons — Delphic vapours (contested), "oracles always ambiguous" (pop simplification, Fontenrose), Dodds' dream evolutionism, the Azande closed-system reading, rune-casting as a modern esoteric construction, geomancy origin (contested), "proto-science" distortion, the 2012 phenomenon as a modern movement, panbabylonian astral religion (discredited), the shaman catch-all, Whorf/Lévy-Bruhl framing (discredited).
- Canon hygiene (`QUALITY.md` item 5): §8 boundary, §9 explicitly "NON-CANON — a design exercise", DR-DIV-10 ("no canon, no admission claim"), §13 handoff to lore-shokunin — no canon decision made.
- Provenance (`QUALITY.md` item 1): bibliographic citations are identification-specific (author + title + year/venue); the entry's own "Limits" paragraph (L218) states no work was retrieved in full and no ritual detail was extracted from living traditions; 0 `to-verify` marks with the reason recorded as DR-DIV-07. Calibration honesty verified: no marker inflation, no launder.

### 3.6 No duplication

- Slug/title/topic vs the committed corpus and the other round-10 entries at check time: no collision, no near-duplicate topic.
- 8-gram body-shingle Jaccard (`.scratch/c15-shingle.py`, re-run on rev 2) — max `0.0012` (`verification/myth-consistency-gate.md`, legitimately cross-referenced), next `0.0008` (`trickster.md`, `ritual-liminality.md`). Calibration: reviewer C13 measured the committed corpus's highest pair at `0.0119`; the two sibling round-10 myth entries screen at `0.0055`/`0.0016`; the author's own screen reports max `0.00135`. No reuse signal — no duplication.
- Boundary work: §8 separates it from `celestial-symbolism-calendars.md` §7 (eclipse/sky omens), direction codes, tale indexes, ritual grammar, name magic; DR-DIV-03 records the exclusion decision.

### 3.7 Verdict

**PASS on all four mandated checks** (frontmatter completeness; source resolvability — clean in current bytes; no filler — real, named, delivered gap; no duplication) on revision 2 (`6666e7db…`), with the following findings and notes for the parent:

- **F-1 (minor; FIXED by the author in revision 2 — kept as history):** revision 1 carried five broken relative references `../../verification/…` (L25 couples, L28 recheck, L159 §8, L178 DR-DIV-08, L216 §13) resolving to non-existent `corpus/verification/`. Revision 2 replaces them with the correct `../verification/…` form (`grep -c '\.\./\.\./verification'` → 0; refcheck sweep → 0 unresolved). No action owed; no previously green check regressed (runner checks re-run on rev 2 still pass).
- **N-1 (resolved):** attribution to seat C05 is fragment-confirmed (`C05.md` names the file; fragment landed 18:42 local).
- **N-2 (resolved):** `corpus/README.md` now carries `## myth-symbol/ (19)` with a `divination-omen-systems.md` index row (line 52) and the footer reads `Total knowledge entries: 189.` (verified 18:42 local) — the C21/C22 index update landed.
- No admission, promotion, merge, or canon decision is made or implied here; the entry stays as filed for parent reconciliation.

### 3.8 Reviewer verification footprint

Reads: the entry (rev 1 in full; rev 2 re-checked field-by-field for the changed bytes), fragment `C05.md` (all sections), fragments `C04.md`/`C06.md`/`C07.md` headers, `run-validation.py` (C section), `myth-consistency-gate.md` §2, `corpus/QUALITY.md`, `reports/round-8/metadata/m09-myth.md`, `reports/round-9/metadata/v09-myth.md`, `corpus/lessons/round-4-audit/myth-symbol.md`, `corpus/README.md` (myth-symbol section + footer). Commands: runner import check (both revisions); field census (both revisions); provenance gate (file, both revisions; partition, two timepoints); refcheck sweep (both revisions); shingle screen (both revisions); gap-sweep re-runs; hash/stat captures. No corpus byte, ledger, or sibling file was edited; no commit; this file (plus uniquely named scratch under `.scratch/`) is the only write.

## 4. Limits of this review

- §0–§2 are retained as history (state at review open, 18:26–18:32 local); §3 is the operative landed review of 18:42–18:43 local against entry revision 2, sha256 `6666e7dbd5cc5a4bd9833b3e842843854af8ef7b365396c6d1737aac8cbf2ba4` (revision 1 was `30d7ccc6…`). If the entry is edited after that hash, §3's anchors must be re-verified before reuse.
- Bibliographic sources were checked for identification specificity, not full-text retrieval (the entry itself says the same); no URL was cited, so no access attempt was owed. The reviewer did not re-retrieve any cited book or article.
- No live gate selftests run beyond the provenance gate on the file and partition; no corpus bytes, ledgers, or shared bookkeeping touched; only this assigned file written (plus uniquely named scratch under `.scratch/`).
- C05's fragment landed only at 18:42 local (after the poll close); it was read in full for §3.1, and its self-reported counts were verified only where independently reproducible — and the reproducible ones all held (§3.4). The rest of its self-report is author-side evidence, not re-verified by this seat.
- Author-side review only; parent owns integration, judgment, and publication.
