# R10-C20 — Reviewer of worker C10's verification-partition entry (author-side review)

- reviewer scope: `reports/round-10/coverage/review-C10.md` only. No corpus, ledger, bookkeeping, canon, or promotion edits. Author-side review evidence only; not an admission decision and not independent promotion verification.
- assignment: `reports/round-10/targets.json` → `R10-C11..C20` ("Ten reviewers: one per authored entry (poll for it, max 20 min): verify frontmatter completeness, source resolvability (re-run the cited command or open the cited path/URL), no filler, no duplication of an existing entry; verdict `reports/round-10/coverage/review-<id>.md`").
- C10 is the second verification-partition author (`R10-C01..C10`: linguistics ×3 — C01–C03; myth-symbol ×3 — C04–C06; culture-material ×2 — C07–C08; verification ×2 — C09–C10). Expected outputs: fragment `reports/round-10/coverage/C10.md` naming one new `corpus/knowledge/verification/<slug>.md` entry, per `targets.json` ("read corpus/README.md known-gaps + the partition's existing entries + round-8/9 receipts; pick ONE distinct gap (derive filename slug from the gap; on collision append -b); write corpus/knowledge/<partition>/<slug>.md with full frontmatter and a decision-record section").
- round-10 declared baseline revision: `9dc18ec1339bffd6f81e74f1a5742464ef578749` (`reports/round-10/claims.json`); working tree at review open: `e3a1ec9` ("round-10: availability attempt 3 — opencode-go-5 dry; keys 3/4/5 unprovisioned, retrying key 1").
- date: 2026-10-17. Poll window opened 21:26Z (background poll, 55 s cadence, 20-min cap → ≈21:46Z). All times UTC.

## 0. Review status

At review open (21:26:00Z–21:28:45Z) `reports/round-10/coverage/` held only `review-C08.md` (sibling reviewer C18, landed 21:28:32Z): **C10's fragment and C10's entry have not landed** and are not yet inspectable. The wave is nevertheless live — observed in the same window: `corpus/README.md` modified, `reports/round-10/drift/` created, `reports/round-10/findings-tracker.json` created, `git status` dirty — so sibling C/F/O shards are working. Per the assignment this review polls up to 20 minutes; the landed-bytes review (or the unreviewed-absent verdict) is appended below as §2.

Round-10 context (from `git log` and `reports/round-10/availability-attempt-*.json`): attempts 1–3 all returned HTTP 402 "Insufficient account funds" on opencode-go keys 3/4/5 with zero workers launched ("all 64 workers failed at launch, no work performed"); attempt 4 retries key 1 within the sanctioned provider. A late or absent C10 is a scheduling/availability fact, not evidence about worker quality, and this review does not predict it.

## 1. Pre-landing method (checks prepared, no entry to apply them to yet)

The four mandated checks, with their exact instruments, frozen here so the landed review is a mechanical application:

1. **Frontmatter completeness** — criterion (round-9 V11 reading for this partition, the one all 13 verification files use): `- topic:`, `- sources:` (or `- source:`), `- couples:`, `- verified-at:`, `- recheck:` each present exactly once, non-empty, no placeholder value; `verified-at` dated with its inspected scope; every `couples` reference resolving to a real file. Instruments: `.scratch/c20-apparatus.py` (anchored regex census, digest, heading list, placeholder sweep, locator extraction), the round-9 V11 §7 cross-reference expansion pattern, and `python3 tools/gates/provenance-audit.py <newfile>`.
2. **Source resolvability** — re-run each cited command and open each cited path/URL, including round-8/9 receipts cited by path (allowed as sources by `claims.json` C: "round-8/9 receipts and existing corpus cross-references count as sources when cited by path"). Instruments: `.scratch/c20-dupcheck.py` (path-reference resolution against the repo root) plus a `curl` reachability sweep with recorded HTTP status and retry. Non-resolving items: verdict `to-verify`, never silently passed.
3. **No filler** — the entry must name the gap it fills; the gap must be real (not already covered by an existing entry or by `corpus/README.md`'s known-gaps being satisfied) and the entry must deliver on it (per `corpus/QUALITY.md`: provenance, calibration, coupling, usability, canon hygiene — decision tables/typologies/checklists, no essays).
4. **No duplication** — compare the new entry's slug, title, and topic against the committed baseline of all 179 entries. Instruments: `.scratch/all-paths-r10c20.txt` (179 paths, captured 21:28:45Z) and `.scratch/c20-dupcheck.py` (slug-collision check + topic similarity ranking; corpus-wide duplicate slugs currently: none).

Baseline facts recorded at open (evidence for the no-duplication and gap checks):

- `find corpus/knowledge -name '*.md' | wc -l` → `179` (21:28:45Z, tree `e3a1ec9`); `find corpus/knowledge/verification -name '*.md' | wc -l` → `13`.
- verification partition at open: calibration-registry, citation-format-and-source-registry, costume-era-consistency-gate, gate-frozen-run-standard, internal-consistency-audit, lexicon-coverage-audit, myth-consistency-gate, naming-collision-gate, phonology-sanity-gate, provenance-audit-ledger-format, real-world-inspiration-boundaries, to-verify-triage-protocol, verification-method-overview.
- README known-gaps at open (`corpus/README.md`, revision 1.2) that a verification entry could plausibly target: the fleet's complete `source`/`verified-at`/`recheck` header conformance (older topic/sources/couples profile only), D2 typed-label/rank/era reconciliation, D3 round-7 acceptance pendency, strict historical path whitelists in earlier acceptance scripts, cultural permission / real-language name screening / lore receipt / independent promotion review.

## 2. Landed review — C10's entry

### 2.0 Artifact, revision, and an identification correction

- Reviewed artifact: `corpus/knowledge/verification/header-conformance-readings.md` — 160 lines, 21,829 bytes, sha256 `d627eba3b99f56933b6eae2ab1339013be57da30a5e5608b4d75ddb7f36feb90`, mtime 2026-10-17 18:31:46 −03 (= 21:31:46Z). Digest re-checked at 21:32Z, 21:35:47Z and 21:36:04Z: **unchanged** — no mid-review churn on this file. The digest equals the one C10's fragment claims post-edit (21:32Z), so the reviewed bytes are the delivered bytes.
- C10's fragment `reports/round-10/coverage/C10.md` landed in the same window and names this entry and the gap it fills; it is consistent with what the entry does.
- **Identification correction (for the parent):** sibling C09's entry (`corpus/knowledge/verification/verification-independence-anti-circularity.md`) landed ≈1 minute before C10's, and this reviewer initially ran the full battery on it before C10's fragment fixed the attribution. Two locator observations from that run belong to **C09's** entry, not C10's, and are handed to reviewer C19's scope: (a) its `verified-at` cites the `circularity` hit at `myth-symbol/hero-journey-variants.md:37`, but the swept token is at line 121 (line 37 carries the related "circular method"); (b) its C6 row cites `SCORECARD.md:117`, which was the round-8 line and is now stale (`## Planned` is at line 160; the string occurs in the Planned section at line 181). Neither observation is charged to C10's entry below.

### 2.1 Frontmatter completeness — PASS

Census (`.scratch/c20-apparatus.py`, 2026-10-17): `- topic:` @3, `- sources:` @4, `- couples:` @5, `- verified-at:` @6, `- recheck:` @7, first `## ` heading @9 — each field exactly once, all inside the opening block, no placeholder values. Lane gate on the file: `python3 tools/gates/provenance-audit.py corpus/knowledge/verification/header-conformance-readings.md` → `files=1 marks=5 mark-lines=4 findings=0 blocked=0`, exit 0 — byte-equal to the numbers C10's fragment reports (§3.1).

- No singular `- source:` line: the entry is deliberately reading-B conformant (documented in the entry §3/§9 and consistent with the lane shard protocol — `reports/round-8/metadata/m07-synth-13-24.md:32` "`- sources:` as the source leg"; `reports/round-8/metadata/m11-verification.md:157` "this fragment records the lane reading (header `- sources:` satisfies the leg)"). Reading A counts this file as missing the source leg, which is the entry's own thesis, not a defect.
- `verified-at` is dated, names the measurement window and revision, and explicitly states what was **not** checked ("no entry's sources were re-inspected, no URL was re-fetched, and the fleet ruling question was not adjudicated"). `recheck` carries four concrete triggers (handoff counts, the §3 command, `FIELD_NAMES` changes, `CORPUS.md` amendment, integrator ruling). Both satisfy the round-8/9 shard fix-shape.

### 2.2 Source resolvability — PASS (every cited item re-run or opened)

| cited item | my check (2026-10-17) | result |
|---|---|---|
| fleet `CORPUS.md:17` | read directly | exact: "Each `knowledge/` entry opens with `source:`, `verified-at:` and `recheck:`;" |
| `corpus/QUALITY.md` items 1–3 | read | provenance/calibration/coupling — as claimed |
| `tools/gates/provenance-audit.py:75` | read | `FIELD_NAMES = ("topic", "sources", "couples")` — exact |
| gate-blindness demo on `to-verify-triage-protocol.md` | re-ran | exit 0, `files=1 marks=13 mark-lines=13 findings=0 blocked=0` — byte-equal to the entry's quoted output |
| `reports/round-9/metadata/audit.md` | read | three-reading table exact: A 83→64, B 4→3, C 0→0; B-remainder names the same three files with the same geometry (trio 15–17/9–11/9–11, first heading 13/6/6) |
| `reports/round-8/metadata/m07-…` / `m11-…` | read | protocol statements present at :32 / :157 |
| `reports/supplement-opencode-1/28-corpus-contract.md` §2/§6/§7 | read | sections exist; §6.2 quote exact ("The integrator either amends CORPUS.md's sentence to a profile-inherits-its-gate rule or declares the lane non-conformant"); §6.3 quote exact ("a placeholder date is a fabricated verification"); §6.5 recount-staleness statement exact |
| `tools/gates/frozen/provenance-audit/r9-pre/expected.json` | re-hashed | **20/20 pinned digests match live bytes; 20/20 baseline-local snapshot copies match** |
| `corpus/README.md` rev 1.2 known-gaps | read | the quoted gap sentence is present |
| all 10 in-repo path references | resolved | 10/10 exist (list in §1 instrument output) |
| external URLs | — | none cited; the entry claims no external source beyond the fleet sentence and in-repo receipts, and the file carries 0 URLs — consistent |

### 2.3 No filler — PASS

The gap is named and real: `corpus/README.md` known-gaps' header-conformance sentence, unanswered by any of the 13 pre-existing verification entries (none measures the header contract; `citation-format-and-source-registry.md` covers in-entry citation syntax, `provenance-audit-ledger-format.md` covers claim-level ledgers, `gate-frozen-run-standard.md` covers freeze mechanics — the entry cites each and says it does not restate them). The entry delivers the contract it promises: vocabulary (§2), three named readings with a reproduction command (§3), count-statement schema with six mandatory fields (§4), reading registry + context table (§5), the digest-pin constraint and its three stragglers (§6), repair discipline (§7), can/cannot table (§8), **decision-record section with DR-1..DR-5** (§9, satisfying the round-10 "decision-record section" requirement), escalation state (§10), handoff reading (§11), limits (§12). Tables and schemas throughout; no essay padding.

### 2.4 No duplication — PASS

- Slug `header-conformance-readings` — no collision anywhere in `corpus/knowledge/` (corpus-wide duplicate slugs: none).
- Highest topic similarity 0.254 (`synthesis/source-discipline-calibration.md`), next 0.241 — no near-duplicate; content spot-checks against the three closest verification entries found no restatement.
- The entry's numbers are measurement results on the corpus's own apparatus; no existing entry contains the three-reading definition set or the count schema.

### 2.5 Live-claim re-verification (the entry's own numbers, independently re-run)

| claim (entry) | my re-run | verdict |
|---|---|---|
| §3 command reproduces the counts; pre-landing 64/179, post-landing 66/181 | same command, four re-runs: `files=183 missing_any=68` (observed between 21:32:45Z and 21:34:57Z; exact stamp not printed); 21:36:04Z: `files=187 A=69 B=3 C=0`; 21:37:07Z: `files=188 A=70` | reproduces in kind — the rise is exactly the reading arithmetic the entry documents (each new B-conformant entry adds 1/1 to A and total); B and C held |
| B-remainder = exactly the three named stragglers | B missing = 3, the identical three files, at both measurements | exact |
| C = 0 | C missing = 0 | exact |
| per-partition A-breakdown | civilizations 19/94, myth-symbol 0/16, synthesis 0/24 unchanged; culture-material/linguistics/verification each +1/+1 for the newly landed B-conformant entries | consistent with the entry's pre-landing 19/94 · 16/16 · 16/16 · 13/13 · 0/16 · 0/24 |
| "no file under `corpus/knowledge/` newer than the round-10 wave start" at its 21:29Z measurement | mtime sweep: earliest new file 21:31:46Z | consistent |
| stragglers' digests match the `r9-pre` pin | 20/20 match (live and snapshot) | exact |

### 2.6 Findings

- **F-1 (minor, non-blocking, evidence presentation):** the §3 command is labelled "the round-9 auditor's, run verbatim", but the printed command is a 436-char variant of the audit's 485-char command — the audit's trailing clause `;[print('MISSING',p,','.join(d)) for p,d in miss]` is omitted (`reports/round-9/metadata/audit.md:31` vs entry line 49). The `files=/missing_any=` output line is unaffected and the entry's cited count matches the audit's close line exactly, so **no number moves**; but under the entry's own standard (reproducible, exactly-stamped counting commands) the word "verbatim" should be dropped or the clause restored. Owner: author/integrator; the reviewer does not edit the entry.
- **Notes, not defects:** (a) the §3 output sha256 `5464c9b0…` is not re-verifiable after the tree moved — by design, and the entry says so; I verified reproducibility in kind, not that hash. (b) `corpus/README.md` still shows `## verification/ (13)` and no new slugs at 21:36Z — the index-row update is C21/C22's task; a round-integration item, not a C10 defect. (c) `reports/round-10/run-validation.py` now exists (X03's); I did **not** run it, because it writes `reports/round-10/validation.json`, outside this review's write scope. (d) The entry was authored inside a live wave; its numbers are revision-stamped and its own recheck trigger is the §3 command — correct posture, no action.

### 2.7 Limits of this review and verdict

- Author-side review evidence only; not an admission decision and not independent promotion verification.
- I verified the entry's apparatus and its internal-receipt claims as listed above. I did not re-inspect any entry's sources, did not re-fetch any URL (none cited), did not adjudicate the fleet-text question (the entry explicitly does not either), and did not re-run the round-10 acceptance runner (write scope).
- Every count above carries its UTC time and the tree it was measured on (`e3a1ec9435787328ac9f828f96cb6390e4916b8f`, dirty from concurrent shards, `corpus/knowledge/` growing 179→187 across the check window).
- **Verdict: PASS** on the four mandated checks (frontmatter complete, sources resolvable, no filler, no duplication), with one minor finding (F-1) recorded for disposition by the author/integrator.
