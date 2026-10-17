# R10-C11 — Reviewer of worker C01's linguistics entry (author-side review)

- reviewer scope: `reports/round-10/coverage/review-C01.md` only. No corpus, ledger, bookkeeping, canon, or promotion edits. Author-side review evidence only; not an admission decision and not independent promotion verification.
- assignment: `reports/round-10/targets.json` → `R10-C11..C20` ("Ten reviewers: one per authored entry (poll for it, max 20 min): verify frontmatter completeness, source resolvability (re-run the cited command or open the cited path/URL), no filler, no duplication of an existing entry; verdict `reports/round-10/coverage/review-<id>.md`").
- C01 is the first linguistics-partition author (`R10-C01..C10` seat split: linguistics ×3 = C01–C03, myth-symbol ×3 = C04–C06, culture-material ×2 = C07–C08, verification ×2 = C09–C10). Expected outputs: fragment `reports/round-10/coverage/C01.md` naming one new `corpus/knowledge/linguistics/<slug>.md` entry, per `targets.json` ("read corpus/README.md known-gaps + the partition's existing entries + round-8/9 receipts; pick ONE distinct gap (derive filename slug from the gap; on collision append -b); write corpus/knowledge/<partition>/<slug>.md with full frontmatter and a decision-record section").
- round-10 declared baseline revision: `9dc18ec1339bffd6f81e74f1a5742464ef578749` (`reports/round-10/claims.json`); worktree HEAD at review open: `e3a1ec9435787328ac9f828f96cb6390e4916b8f` ("round-10: availability attempt 3 — opencode-go-5 dry; keys 3/4/5 unprovisioned, retrying key 1").
- date: 2026-10-17. Poll window opened 21:27:07Z (background poll `bash-1ajy2mm9`, 60 s cadence, 20-min cap → ≈21:47Z) watching two surfaces: `reports/round-10/coverage/C01.md` and `corpus/knowledge/linguistics/` for a 17th file, so a landed entry is caught even if its fragment is late. All times UTC.

## 0. Review status

At review open (21:27:07Z) `reports/round-10/coverage/` was empty and `corpus/knowledge/linguistics/` still held exactly its 16 committed files (all mtimes 17:18, pre-round-10): C01's entry is **not yet inspectable**. The wave is nevertheless live — observed in the same window: sibling reviewer files `review-C04.md`, `review-C08.md`, `review-C10.md`, auditor file `audit-unchanged.md`, `reports/round-10/drift/shard-07.md`, `reports/round-10/findings-tracker.json`, and `corpus/README.md` modified — so sibling C/F/O shards are working. Per the assignment this review polls up to 20 minutes; the landed-bytes review is appended below as §3 (the entry landed 21:35:52Z and its author fragment 21:39:47Z; see §3's poll receipt).

Round-10 context (from `git log` and `reports/round-10/availability-attempt-*.json`): attempts 1–3 returned HTTP 402 "Insufficient account funds" on opencode-go keys 3/4/5 with zero workers launched ("all 64 workers failed at launch, no work performed"); attempt 4 retries key 1 within the sanctioned provider (this run). A late or absent C01 is a scheduling/availability fact, not evidence about worker quality, and this review does not predict it.

## 1. Pre-landing method (checks prepared, no entry to apply them to yet)

The four mandated checks, with their exact instruments, frozen here so the landed review is a mechanical application:

1. **Frontmatter completeness** — criterion: the house profile all 16 committed linguistics files use, `- topic:` / `- sources:` / `- verified-at:` / `- recheck:` / `- couples:` (round-8 M08 sweep added the last two to all 16; the round-10 claim names the `source`/`verified-at`/`recheck` triple). Each present exactly once in the head block (text before the first `## ` heading), non-empty, no placeholder value (`none`, `n/a`, `tbd`, `todo`, `unknown`, `-`, `(to-verify)`); `verified-at` dated and scope-bearing; every `couples` reference resolving to a real file. Instruments: `.scratch/c11-check-c01.py` (header-block field extraction replicating the gate's `FIELD_RE` + indented-continuation reading, placeholder sweep, heading list, cited-path/URL/command extraction) and `python3 tools/gates/provenance-audit.py <newfile>` (same gate that reads the live corpus; baseline reading on the 16 at open: `files=16 marks=29 mark-lines=29 findings=0 blocked=0`, 21:27Z).
2. **Source resolvability** — open each cited repo path and check it exists and supports the cited use; re-run each cited runnable command and record exit + output; give every cited URL a documented access attempt (fetch with recorded result); round-8/9 receipts cited by path count as sources per `claims.json` C ("round-8/9 receipts and existing corpus cross-references count as sources when cited by path"). Bibliographic citations (author + year, no repo path/URL) are checked for identification specificity (author, title/venue, year present; locator where the entry makes a page/line-specific claim), not full-text retrieval. Non-resolving items: verdict `to-verify`, never silently passed.
3. **Decision-record presence** — `targets.json` requires the entry to carry "a decision-record section". Criterion: at least one headed section or labeled block that records decisions taken (what was chosen and why, with the rejected alternative or the limit). No committed linguistics entry currently carries a literal "decision record" heading (`grep -rn -i "decision record\|decision-record" corpus/knowledge/linguistics/` → 0 hits, 21:27Z), so this is a round-10 addition the entry must actually deliver; absence is a finding against the C claim, not a style note.
4. **No duplication** — compare the new entry's slug, title, and topic against the committed baseline of all 179 entries (`git ls-tree -r HEAD --name-only corpus/knowledge` → 179 files; captured `.scratch/head-knowledge-files.txt`) and specifically against the 16 linguistics entries (title/topic map captured `.scratch/c11-ling-topics.tsv`); topic token-overlap ranking + an n-gram body-shingle screen to catch text reuse. A near-duplicate of any existing entry is a finding; a slug collision without the `-b` suffix is a naming defect.

Baseline facts recorded at open (evidence for checks 1, 3 and 4):

- `git ls-tree -r HEAD --name-only corpus/knowledge | grep -c '\.md$'` → `179`; `.../corpus/knowledge/linguistics` → `16` (21:29Z, HEAD `e3a1ec9`).
- Per-file `sha256sum corpus/knowledge/linguistics/*.md` captured to `.scratch/c11-ling-baseline.tsv` (16 lines) so any post-landing change to an existing file is distinguishable from the new file; full-hash spot check: `color-terminology.md` `7ee9f7e4…5992`, `conlang-methodology.md` `272329f7…77ea`, `historical-linguistics.md` `019f28f0…3caf` (21:30Z) — matching the round-8 M08 after-state hashes, i.e. no pre-round-10 drift in this partition.
- `corpus/README.md` at open: `## linguistics/ (16)` index with the 16 rows; `## Known gaps (frontier)` at L213 names lane-wide gaps (fleet header conformance for older entries; D2 typed labels; D3 acceptance; strict historical path whitelists; cultural permission / real-language name screening / lore receipt / independent promotion review). A C01 gap must be a *partition* gap (a real linguistic topic absent from the 16), not merely an evidence-state note.

## 2. Observations outside this seat (reported, not dispositioned)

Recorded read-only for the parent; this seat owns no bookkeeping write:

- Worktree carries `M corpus/README.md`: the `civilizations/africa-primary-sources.md` index row was rewritten (expanded description). No C01–C10 target partition covers civilizations; whether this is an authorised index-updater act or an out-of-seat edit is the parent's call.
- Worktree carries `M reports/round-5/validation.json` (rewritten; its F and O sections now read `passed:false` with error strings) and `M reports/round-9/validation.json` (two `stdout_sha256` values and one `git_status` block changed). These are rewrites of *filed* receipt bytes; round-10's F targets state "never rewrite filed report bytes — corrections are new entries". Whether these are authorised re-runs or an unlogged overwrite is the parent's call.
- `.scratch/` is shared by all live workers (sibling files present, e.g. `review-C02-skeleton.md`, `poll-ling-verif.sh`, `entry-index.json`); this seat names all its scratch files `c11-*` to avoid collisions.

## 3. Landed-bytes review — C01's entry

**Poll receipt.** Window 21:27:07Z–21:47Z cap; entry first seen 21:35:52Z (a 17th file in the partition, found by an mtime watcher after an earlier watcher bug: the first poll's scratch baseline was renamed mid-run, its greps failed, and it false-fired at 21:30:20Z — corrected within minutes; no review decision rests on it). Author fragment `reports/round-10/coverage/C01.md` landed 21:39:47Z. The entry's `verified-at` cites that fragment as its URL-receipt location, which fixed its authorship to this seat (C03's `numerals-and-measures.md` and C02's `sound-symbolism.md` are siblings' artifacts).

**Anchor revision.** `corpus/knowledge/linguistics/language-shift-obsolescence-revival.md`, sha256 `89d2a225dd709a7947c4f9d967ffd6ce858f784bfef10f581b11a863dc6c8315`, 184 lines / 39,676 bytes, mtime 21:38:48Z; re-hashed stable at 21:40:43Z. All checks below run against these bytes; a later edit invalidates the anchors.

**Churn record (informational).** The entry was edited twice inside the review window: `289a1956…` (21:36:11Z) → `a37178a4…` (21:38:13Z; cross-reference correction `sociolinguistics-registers.md` §2 → §3) → `89d2a225…` (21:38:48Z; couples refinement `culture-material` → `culture-material/craft-artisan-lexicon`). All three revisions passed the same checks; the verdict binds to `89d2a225…`. Mid-review churn is itself a re-verification trigger for the parent's integration step.

### 3.1 Frontmatter completeness — PASS

Header block = lines 1–31 (text before the first `## `). All five house-profile fields present, non-empty, no placeholders: `topic` (554 ch), `sources` (8,471 ch, 22 entries incl. two lane receipts and five corpus cross-references), `verified-at` (992 ch, dated 2026-10-17 with its inspected scope and its exclusions), `recheck` (456 ch, use-triggers + re-run rule), `couples` (1,458 ch). The round-10 `- gap filled:` field is also present (554-char `topic` + gap field both name the gap). Instrument: `.scratch/c11-check-c01.py` (gate-equivalent header reading) + `python3 tools/gates/provenance-audit.py <entry>` → `INFO scan: files=1 marks=24 mark-lines=23 findings=0 blocked=0`, exit 0 (the 24 `to-verify` marks are inventory, not findings). Acceptance-runner-aligned reading (`reports/round-10/run-validation.py` §C `C_FRONTMATTER_FIELDS`): `topic=ok sources=ok verified-at=ok recheck=ok couples=ok`.

### 3.2 Source resolvability — PASS (all cited surfaces opened)

| Cited surface | Access by this reviewer (2026-10-17) | What was checked |
|---|---|---|
| Wikisource, Atlas of the World's Languages in Danger (3rd ed.) introduction | fetched OK | Degree definitions Safe (5) → Extinct (0) match the entry's quotations verbatim; the "objections to the term 'extinct'… the bald term 'extinct' does not reflect the true situation for some languages" passage is present as quoted |
| Avalon Project, Palestine Mandate | fetched OK | Art. 22 reads "English, Arabic and Hebrew shall be the official languages of Palestine" — verbatim match |
| GOV.WALES cabinet handbook §4 | fetched OK | 538,300 / 17.8% aged 3+; −1.2 points / −23,700 vs 2011's ~562,000 / 19.0%; APS 862,700 / 28.0% (year to 31 Mar 2024) — all figures match; the entry's "differ by ~60%" and "~26–28%" readings are consistent with the page |
| Te Ara, "Te reo Māori" | fetched OK | WAI 11 lodged 1984 / four-week hearing / 1986 report; Māori Language Act 1987; first kōhanga reo Pukeatua 1982; 1972 petition 30,000+; 2013 census 125,352 Māori speakers / 148,395 total (3.7%); 38.8% of 65+ vs 16.6% under 15; T. B. Strong 1930 quote with the *Maori and education*, 1931, p. 193 citation; Education Ordinance 1847; Benton surveys + Hui Whakatauira 1979–80; Te Ataarangi — all match |
| `reports/round-8/freshness/R8-F01-receipt.md` | opened | Contains exactly the quoted passages: Jagersma 2010 pp. 1, 6 ("…language of scholarship and cult…"); Rubio 2006 p. 50 ("…as was the case of Latin in some academic and clerical circles well into the twentieth century"); Michalowski 2006 p. 164 ("There is agreement on one thing only: the spoken language died in antiquity. The date of this death has been variously estimated") |
| `reports/round-9/freshness/audit.md` | opened | Documents client-dependent bot-walls (Anubis interstitial; DataDome; UA-sensitivity) as the entry's §5.6 claims |
| `reports/round-10/coverage/C01.md` | landed 21:39:47Z; read | Carries the session's retrieval table with access outcomes (unesdoc 403 recorded, not worked around) and re-runnable gap sweeps; its sweep lines reproduce against the live tree (below) |
| `couples:` targets (14 named, incl. `culture-material/craft-artisan-lexicon` after the 21:38:48Z edit) | all 14 exist | 0 missing |
| In-prose corpus cross-references (language-contact §2, sociolinguistics-registers §3, era-language-staging §6, real-world-inspiration-boundaries §7, orality-formulaic-language) | opened | Section locators correct: §2 "The master asymmetry", §3 "Diglossia", §6 "Diglossia cycles", §7 "Consulting-source guidance — authority is specific, not demographic" |

Non-resolving items: none at review close. Book-length works cited without page-level inspection are the entry's own `(to-verify)` marks (24) and were not re-fetched by this seat.

### 3.3 Decision-record presence — PASS

`## 8. Decision record: staging a death, a dormancy, or a revival` (L165) with DR-1…DR-10, each row: decision point / options / recorded choice / reason-evidence / residual. Acceptance-runner regex (`^#{2,4}[^\n]*decision[- ]record[^\n]*\n+\s*(\S[^\n]*)`) matches. The gap is named in the frontmatter `- gap filled:` field and in §1 ("The gap this entry fills" content inside the header; §1 opens the body).

### 3.4 No filler / gap is real — PASS

Independent sweeps on the live tree (2026-10-17, this seat): `grep -rln "GIDS\|EGIDS" corpus/knowledge/` → only the new entry; `grep -rln "obsolescen" corpus/knowledge/` → only the new entry; `grep -rln "revitaliz" corpus/knowledge/linguistics/` → only the new entry; `grep -rln "Fishman" corpus/knowledge/` → the three pre-existing files the entry itself names (sociolinguistics-registers, linguistic-anthropology, era-language-staging — all Fishman 1967 diglossia) plus the new entry. The nearest neighbours are cross-referenced for scope-splitting, not restated. The entry delivers usable craft: base mechanism ladder, three diagnostic frameworks, a calibrated case table, revival-mechanics ranking, a debunk shelf, a scene-visible staging ladder, the decision record, and a handoff list.

### 3.5 No duplication — PASS

Slug `language-shift-obsolescence-revival` absent from the committed 179-entry baseline; topic token-overlap vs the 16 existing linguistics entries max 0.031 (linguistic-anthropology); body-shingle screen (8-gram) vs all 179 committed entries: exactly one shared shingle (j=0.0001, with `verification/gate-frozen-run-standard.md`) — no text reuse. Distinct from sibling round-10 linguistics entries (`numerals-and-measures`, `sound-symbolism`).

### 3.6 Findings and observations

- **P1 (resolved):** the entry cited `reports/round-10/coverage/C01.md` before that fragment existed (first harness reading, 21:36Z). The fragment landed 21:39:47Z and the pointer now resolves; closed at review close.
- **O1 (minor, non-blocking):** §1 bullet 2 carries an illustrative "badly documented with 200,000 speakers (many signed and minority languages)" — the one figure in the entry with neither a citation nor a `(to-verify)` mark (every other figure is cited; 24 marks elsewhere). Recommend naming an example or marking it at the next touch.
- **O2 (informational):** three revisions within three minutes of landing (see churn record) — re-verification trigger, not a defect.
- **O3 (out-of-seat, repeated from §2):** `M corpus/README.md`, `M reports/round-5/validation.json`, `M reports/round-9/validation.json` remain the parent's adjudication.

## 4. Verdict

**PASS — author-side review only.** C01's entry meets all four mandated checks against anchor `89d2a225…`: frontmatter complete (5/5 fields + gap field; gate exit 0), sources resolvable (4/4 URLs fetched and content-checked by this seat, 2/2 lane receipts opened with quotes located, 1/1 author fragment landed and read, 14/14 couples resolve), decision record present (`## 8`, DR-1–DR-10), no duplication (slug new; shingle overlap ≤1; topic Jaccard ≤0.031). One minor provenance nit (O1) and one resolved pending-locator item (P1); no blocking condition. This seat decides no admission, promotion, or canon.

## 5. Limits

- URL checks were direct fetches by this seat; the entry's search-engine result pages live in `C01.md` and were not re-driven, and the entry's "read in full" claims were spot-verified against what the fetches returned, not exhaustively diffed.
- Book locators marked `(to-verify)` in the entry (Fishman, Dorian, Schmidt, Mufwene, Hinton, etc.) were not re-fetched; the marks stand as the entry states them.
- The pre-authoring sweep state can only be corroborated post-landing; I re-ran the sweeps on the live tree and reconciled every delta against the entry's own file.
- Mid-review churn (O2) means the anchor hash is load-bearing: if the entry is edited after 21:40:43Z, re-run `.scratch/c11-check-c01.py` before reusing this verdict.
- This seat wrote only this file; no corpus, ledger, gate, or bookkeeping bytes were touched; no commit.
