# Round-65 verifier spot-check (kotodama, hyaku run 5)

author: hyaku closure (non-author integrator, @m_swe)
lane HEAD closed: `b70887be56e9c42521ce725b5799c22c1e01f320` (branch `main`);
closure prompt base: `f107e84924ff53d72b55d9aa1c0e60b41135089f`;
report: `.ufo/reports/round-65/kotodama.md` (fleet, committed by
`kotodama-shokunin <kotodama@shokunin.local>` in `9a8eed5918368d59c7e67f0a5c03fa6d90282029`).

## 1. Conformance

| check | command | observed |
|---|---|---|
| report committed by lane identity | `git -C $FLEET log --format='%an %ae %H' -- .ufo/reports/round-65/kotodama.md` | `kotodama-shokunin kotodama@shokunin.local 9a8eed59…` — PASS |
| SHONEN heading, one line per box | grep on committed report | 4 lines, all `[~]` asserted-with-pointer — PASS |
| cited commits exist + ancestor of branch | `git merge-base --is-ancestor <h> main` for f107e849, 17c32302, 3b1b5a67, 53a60275, 3e85a610, 29d0b0fc, b70887be | all 7 exist, all ancestors — PASS |
| no uncommitted round work / pushed | `jj-lane.sh state` | `ahead=0 behind=0 tracked=0 untracked=0 head=detached` — PASS |
| prompt carries template contract | re-read `.ufo/prompts/kotodama-round-65.md` | round-level items (mission binding, axis-move rule, L2 floor, commit-then-push, push scope, L0 channel) + five child-lane items present verbatim; L2 floor wording matches MISSION.md §L2 concurrency (≥8, one batched call) — PASS |

Status: **ok** (real report, not a marker).

Defects named (status-neutral):
1. **L2 floor unmet.** §3/MISSION require ≥8 *dispatched* L2 seats in one batched call; this attempt dispatched 0 (validated 64-seat v2 taskcall left prepared-but-unissued in `.ufo/waves/round-65/taskcall-prepared-unissued.json`; inherited `w1/` holds 54 `.md` seat artifacts, 10 named items with no report and no last-error text). Honestly reported, but the floor is a dispatch requirement, not a preparation one.
2. **Causal separability unverified.** `check-claim-separability.py` timed out at 600 s (`w1/RevSeparability.md`); lane disclosed it.
3. **Ca receipt-parent mismatch** — see claim Ca below; recorded by the lane as R65-M9.
4. **S753 source row durability** — the row's live URL 404s as PDF (returns HTML shell) and its committed Wayback capture `20250926172224` replays 404 today although CDX still lists `200 application/pdf` at that timestamp. Re-open failure, routed below.

## 2. Claim re-checks (all over committed bytes at `b70887be`, never re-executing lane gates)

### Claim C — coverage — verdict: **improved** (re-measured)

- Base census: `git ls-tree -r --name-only 17c32302… -- corpus/knowledge | grep -ciE '(^|[^a-z])(game|play|sport|contest|toy|mancala)([^a-z]|$)'` → **0** (matches report).
- Knowledge .md count: base 238 → tip 239 (`git ls-tree -r --name-only` on both revisions). culture-material dir: 32 files at tip — PASS.
- SOURCES rows: `git show 17c32302:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}\|'` → **675**; tip → **701** (+26 = S750–S775, verified ids present exactly once).
- Tier/status of S750–S775 re-derived: A=8, B=18, all `mined` — matches report.
- Gate evidence (§Gate standard, committed evidence verified, not executed): `reports/round-65/telemetry/final-measures-c.txt` — `ACCEPT-C-65: PASS`, exit 0, measured revision `3b1b5a67`, tree `e27ce372`, counter sha `398a362f`, 10/10 legs PASS including APPEND +26 and NOHARM (2-file knowledge diff).
- Semantic caveat: base `music-instrument-lexicon.md` does contain "musical contests" (verified: lines 3, 89–90 at base) and `transport-mobility-lexicon.md` does contain "Mesoamerican wheeled toys" (verified at base line 6) — the lane's disclosure of two partial-scope hits is accurate, and the new entry points one-way to the four partial owners (lines 113–120). Whole-register gap claim holds.

### Claim O — operability — verdict: **improved** (evidence-verified per §Gate standard)

- Committed evidence: `reports/round-65/telemetry/final-measures-o.txt` — `ACCEPT-O-65: PASS`, exit 0, measured at `3b1b5a67`, counter sha `1cc23758`, 26/26 legs incl. `FULL PASS exit=0 pass=23/23`, `MUT PASS mutants=10`, `MUTEX PASS` exact table, `FRAG PASS files=26/26, 0 findings`.
- Counter-honesty: the earlier same-bytes red run (`MUTEX` tracebacks on m10/m7/m8) is preserved in `accept-o-full-initial.txt`; the filtered diagnostic pass in `accept-o-debug-mutex.txt` is correctly *not* counted. Both kept — this is the disclosure discipline, not a hidden failure.
- Capability landed: `tools/check-row-fragments.py` exists at tip (12,505 bytes), enters SCORECARD `capabilities:` table with selftest + scan evidence pointer.
- Mutant fixture trees committed under `.ufo/waves/round-65/stage/mut-c/` — mutation evidence is durable, not session-scoped.

### Claim Ca — calibration — verdict: **unprovable** (claim's own predicate fails at tip)

- Committed evidence: `reports/round-65/telemetry/final-measures-ca.txt` (pre-records run at `3b1b5a67`): R1–R7, CRITERION, QUOTES all PASS — the underlying record repairs are real and present in the bytes (`final-measures-ca.txt` re-stamp to `8bab271c`+tree `0ec0e50e`; R3 path correction; claims.json R4 predicate byte-unchanged; QUALITY criterion 17).
- But the frozen `RECEIPTS` leg re-derives the lands revision: receipts stamp `3b1b5a67` while the post-record tip's immediate parent chain runs through `53a60275`/`29d0b0fc`. Committed `accept-ca-post-records-fail.txt` shows `RECEIPTS FAIL lands=53a60275` → `ACCEPT-CA-65: FAIL`, and the report records the tip rerun failing again with `lands=29d0b0fc`. The predicate `ACCEPT-CA-65: every leg PASS` never printed PASS — claim not verified as declared.
- This is a commit-ordering failure (prepared-wave evidence commit `53a60275` interposed between lands A and the records commit), not a falsified repair; no axis harm observed. Per fleet convention for a measured claim that fails its own counter: `unprovable`.

### Harm check

`git diff f107e849…b70887be -- SCORECARD.md` shows only the round-65 rows/corrections appended and the capabilities row added; no axis score lowered; `depth/freshness/adjacency` marked unchanged by the lane and nothing in the diff contradicts. Freshness pause (round-11 L0) continues.

## 3. Discernment spot-check (LEARNING.md — non-author re-open)

| item | gate decision | re-opened | verdict | reason |
|---|---|---|---|---|
| S754 (UNESCO tugging rituals, admit) | admit | wayback `20170513200455id_` | **agree** | Quote located verbatim: "Most variations include two teams, each of which pulls one end of a rope attempting to tug it from the other." Tier A (UNESCO listing itself) justified; teaches cell grounded. |
| S770 (Gutenberg, *Games and Songs of American Children*, admit) | admit | live `gutenberg.org/files/41727/41727-8.txt` | **agree** | Quote located verbatim (lines 199–200: "The games consist of two main divisions, which may be called descriptive, and singing or choral."). Tier B fit. |
| S771 (worldlacrosse.sport, admit) | admit | live 403 → capture `20260906151449id_` (the committed `20261014174845id_` 302s to it) | **agree, with caveat** | Quote found verbatim in page JSON-LD **after gzip decompression** — the capture is stored gzip-compressed, the class the lane itself documented in R65-M6. Quote and tier-B/interested-source caveat are right; raw-byte consumers cannot read it. |
| S753 (Penn Museum mancala, admit) | admit | live → HTML shell not PDF; capture `20250926172224id_`/`if_`/`im_` → **404** (CDX still lists 200 pdf) | **disagree on durability** | The row's evidence pointer does not resolve at closure (§Evidence standard: resolvable at closure time). Not a fabrication — CDX corroborates a capture existed — but the row needs a live-resolving anchor or alternate capture next round. |
| S765 first source (Remus PDF, edspace.american.edu) | replaced before admit (de facto reject) | row fragment `rows/ScoutRow08/row-S765.txt` VERIFY-L1 notes | **agree** | "No text layer, scanned images" is a correct reject reason for a quote-locator gate; replacement chain (Britannica → Wikisource 1911 EB) preserved the slot and located live. |
| ≤25-word quote rule, all 26 new rows | admit-time ground | script over `corpus/lessons/round-65.md` `## Gate` | **agree** | All 26 quotes 11–25 words. |
| Reject sample | — | SOURCES tip histogram: rejected=22 all pre-existing; `## Gate` names no reject rows | n/a | No `status=rejected` row was written this round; the S765 replacement chain (re-opened above) serves as the reject sample. Note for next round: write gate rejects as `rejected` rows so the spot-check has a first-class sample. |
| Source census | — | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` | exit **0**, `kotodama ok` | Same 28 pre-existing W04 duplicate-URL warnings; no new W04; matches committed `telemetry/census-end.txt`. |

## 4. Trend verdicts

- **expansion: improved** — one new admitted knowledge entry on ground the coverage map did not hold as a whole register; 26 mined rows S750–S775 each citing used-by; culture-material 31→32, corpus 238→239. Counts re-derived, not trusted.
- **quality: improved** — round-64 spot-check defects R1–R7 dispositioned and verified in committed receipts (all R-legs PASS); counters hardened (26 legs, mutation-exclusivity, exactness sweep, fragment checker); QUALITY criterion 17 added from the R1 lesson class; counter evidence honest (both red and green runs preserved).
- **discernment: improved** — this outside sample agrees with the gate on the resolvable admits and on the S765 reject cascade; the one disagreement (S753's unresolvable capture) is durability, not a content error, and is routed below.

## 5. Routed defects for next round

1. **R65-D1 (owned by kotodama):** repair S753's source cell — re-capture the Penn Museum PDF (or cite a live-resolving mirror/DOI); today neither the live URL nor the committed capture returns the quoted bytes.
2. **R65-D2 (owned by kotodama):** receipt sequencing — records commits must be direct children of the lands commit they receipt (criterion 17 already covers the leg; the process ordering is what failed). Consider making the receipt leg's expected lands hash the actual parent at run time.
3. **R65-D3 (owned by kotodama):** dispatch the L2 wave or record the refused/errored dispatch evidence — a prepared taskcall does not satisfy the ≥8 batched-seat floor; retain per-seat last-error text for dead seats.
4. **R65-D4 (owned by kotodama):** bound `check-claim-separability.py` so it returns a verdict inside a round, or replace it — a 600 s timeout leaves separability permanently unverified.

## 6. Round verdict

lanes.kotodama = **ok**; admitted = **false**; verdict = **rejected-honest-stop**.
Axis verdicts: coverage improved, operability improved, calibration unprovable, depth unchanged, freshness unchanged, adjacency unchanged.
SHONEN boxes: all four carry resolvable pointers and appear mechanically checkable by a non-author review — noted for the operator (promotion is operator-owned; this closure asserts no box).
