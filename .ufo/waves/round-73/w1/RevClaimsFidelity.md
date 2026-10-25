# RevClaimsFidelity — w1 attack on reports/round-73/claims.json (DRAFT-v0)

Seat: RevClaimsFidelity (leaf, kotodama round 73 / hyaku run 7). Date: 2026-10-25.
Attacked: `reports/round-73/claims.json` (base `8841ad3b896a0227674fa0725b818c999118046f`, = lane HEAD at review time) against fleet `AXES.md`, `LEARNING.md`, `CORPUS.md`, prompt §9 (`/home/vgpnk/Projects/shokunin/.ufo/prompts/kotodama-round-73.md:417-439`), lane `corpus/QUALITY.md` (1–21 at base; no item 22), and the staged package `/home/vgpnk/Projects/shokuknow/merge/kotodama/` (READ-ONLY).

## Verified before-values (all re-run at base; committed bytes via `git show`/`git ls-tree`)

| Claim | Before clause | Result NOW |
|---|---|---|
| C | `find corpus/knowledge -iname '*conlang-scholarship*'` = 0 | 0 ✓ |
| C | registry = 799 rows, 0 rows naming ojs.unito.it / philol.msu.ru / journals.rudn.ru / cyberleninka.ru/article/n/klassifikatsii / sanders.phonologist.org | 799 ✓ (last id S875 ✓); host sweep over ALL cells = 0 ✓ (stronger than the source-cell claim) |
| C | conlang-methodology.md sources are craft manuals + typological datasets, no research venue | ✓ (Rosenfelder/Peterson/Okrent/Higley; WALS/PHOIBLE/APiCS/Comrie/Croft…) — but see F7 |
| Ca R1 | `git ls-files --others --exclude-standard .ufo/waves/round-72` lists exactly ScoutMergeScan.md, ScribeLesson.md | ✓ in the live worktree; both absent from the base tree — but see F2 |
| Ca R2 | SCORECARD:1401 asserts `ACCEPT-CA-72 PASS legs=12/12`; `reports/round-72/telemetry/measures-ca.txt:29` reads `FAIL legs=12/12` | ✓ live mismatch; the restamp receipt is `ACCEPT-CA-71: PASS` (round-71 counter at 64da9e14), so no committed ACCEPT-CA-72 PASS exists — R2 is honestly open |
| Ca R3 | SKILL.md §Gates registry has no accept-ca-70..72 / accept-c-70..72 rows | ✓ (rows stop at accept-*-69, SKILL.md:674–695) — but see F4 |
| Ca R4 | README:732 `Total knowledge entries: 243` vs count = 245 | ✓ (245 `.md` files at base) |
| frontier | census `validate --root /home/vgpnk/Projects/shokunin kotodama` exit 0, 799 rows | ✓ exit 0, `ok` line (W04 duplicate-URL warnings are informational) |
| axes_note | SCORECARD header quote; freshness pause | ✓ verbatim at SCORECARD:13–15 ("defining a calibrated numeric rubric remains an explicit protocol-conformance gap. Freshness is historically the lowest non-retired axis"); pause re-affirmed per round ("Pause in force") — see F8 for the path |
| C REPOINTED | staged S728/S769/S806 really are campaign ids naming unrelated lane docs, and the staged theme cites them | ✓ lane S728 = Qaqet corrective input, S769 = Opie, S806 = Ayurveda; staged cites: S728 in conlang-scholarship.md:11, S769 in amend-23c:14, S806 in amend-24:42 — the leg is well-founded |

Routed-defect fidelity: Ca's R1–R3 match `corpus/lessons/round-72-verifier-spotcheck.md` :14/:65–67 verbatim in substance ✓. (g) waiver honesty: "No stagnation-nudge waiver is claimed" is correct — the nudge's preconditions are not met, and the freshness pause is an open operator L0 (`kotodama | round-11`: "Freshness axis-move claims are paused until ruled"), honestly disclosed. (f) axis-by-surface: C = coverage (new ground, `find` = 0 is the unmoved-showing command); Ca = calibration (countable self-assessment vs state) — both correctly named.

# Findings

## F1 — BLOCKER (C): the claim's pass/fail hinges on an unfrozen reachability ruling, and its own admitted entries cite the row it may refuse
Staged `conlang-scholarship.amend-2026-10-23.md` (one of the two ENTRIES) cites staged **S894 three times** (Sowers-Wills, DOI 10.1017/cnj.2024.21); full pair citation set = S728, S881, S882, S892, S893, S894, S901. The REJECTS leg refuses "staged S894/S910 **if** their payload stays unreachable by ordinary means", and the kill rule fails the claim if "any admitted entry cites a … unreachable row". So one scout ruling either (i) kills C without any executor fault, or (ii) forces S894 into the ROWS set ("one per source the two entries cite") — which the TENTATIVE 5-row map (S881/S882/S892/S893/S901 → S876–S880) does not contain; while an unreachable ruling forces an undeclared edit (dropping three S894-dependent clauses from the adopted entry). This violates QUALITY 13 (a live-fetch treatment must be declared before data — archived capture listed in the row, or a bounded allowance with its own control — "frozen and never relaxed after data"); "if … stays unreachable" is neither. It also leaves the ROWS count open against the entry citation set.
**Fix (exact wording):** replace the REJECTS parenthetical with: "staged S869 (conference-paper clause, quarantine class); staged S894 and S910 have their disposition frozen at freeze by the wave-1 scout receipt: either reachable under the recorded fetch (URL, UA, date) and re-pointed into the ROWS set, or unreachable under the frozen QUALITY 13/16 treatment (a named same-page archived capture listed in the row, or a bounded retry allowance with paired control), in which case each S894/S910-dependent clause in the admitted entries is dropped at adoption and the lesson records each drop old→new. C's verdict must not depend on a ruling made after freeze."

## F2 — MAJOR (Ca): R1's observe_cmd is worktree-only — unreproducible in the materialized clone the STAMP leg requires
`git ls-files --others` reads the working tree, not committed bytes. A closure materializing base in a fresh clone (STAMP leg, QUALITY 19) observes **zero** untracked files, so the R1 pair cannot be re-derived and BASEMISMATCH's count drops. This re-introduces the exact QUALITY 20 class ("worktree-only") that round-72's routed defects name.
**Fix:** restate R1 as a committed-bytes property: "(R1) the two round-72 w1 seat reports are absent from the base tree (`git cat-file -e 8841ad3b…:.ufo/waves/round-72/w1/ScoutMergeScan.md` and `…/ScribeLesson.md` each fail; the worktree-only observation `git ls-files --others` listed them, recorded once as history)"; REPAIR becomes "R1 both paths present at <lands> (`git cat-file -e <lands>:<path>` succeeds twice)". Add to LEDGER: "every observe_cmd reads committed bytes only (`git show`/`git ls-tree` at a revision), per QUALITY 19".

## F3 — MAJOR (Ca↔C): the README-count pair breaks separability in the C-landed order
Ca's ledger recomputes `find corpus/knowledge -type f -name '*.md' | wc -l` at <lands>. Claim C adds two knowledge files (245→247). If the ledger freezes `expected_after` as the base value 245, Ca fails whenever C lands; if it freezes 247, Ca fails when C does not land. Ca's SEPARABLE leg covers only the Ca→C direction ("no Ca-added line cites an S-id >= S876…"); the C→Ca direction is unhandled — violates AXES "each verifiable without the others having landed" and QUALITY 7.
**Fix:** declare the pair's after-state as an invariant, not a constant: "README count corrected by an appended dated line whose number equals the value `find corpus/knowledge -type f -name '*.md' | wc -l` prints at <lands> (invariant under claim C landing 0 or 2 files)"; add to SEPARABLE: "…and the README pair's check is invariant under C's two added knowledge files".

## F4 — MAJOR (Ca): R3 repair as worded forces registry rows for two gates whose counters do not exist
`reports/round-70/` at base holds telemetry receipts only (measures-*.txt, controls-*.txt at 453676a2); no `accept-c.py`/`accept-ca.py` for round 70 is tracked, and git shows no deletion history — the counter bytes were never committed and are unrecoverable from sha256. REPAIR requires "SKILL.md registry rows exist for each named gate" (accept-ca-70..72 / accept-c-70..72 = six gates), which either registers dead commands (AXES operability: "commands that exist") or forces an undeclared counter reconstruction. The routed fix itself says "add round-72 rows (and backfill or explain 70/71)".
**Fix:** "R3 SKILL.md registry rows exist for the gates whose counters are tracked at base (accept-c-71, accept-ca-71, accept-c-72, accept-ca-72); the round-70 pair carries a ledger disposition `explain` (receipts exist at 453676a2; counter bytes never committed) unless a reconstructed counter is committed as a declared land before the rows."

## F5 — MAJOR (C): the not-adopted enumeration omits the rest of the conlang theme itself
REJECTS names only "the remaining naming-systems / calendar / era / verification staged families" as not adopted. The package's own MERGE-REPORT lists, unadopted and unnamed: `conlang-scholarship.amend-2026-10-23b.md` (S909/S910), `-23c.md` (S915), `conlang-scholarship.amend-2026-10-24.md` (S929/S930), `conlang-methodology.amend-2026-10-24.md`, and a proposed amendment to the lane's existing `conlang-methodology.md` ("target already exists in the lane"). The universal "remaining … families" does not enumerate its set (§9 bullet 2; CORPUS "a negative claim carries its sweep").
**Fix:** "…and every staged file of the package not admitted by ENTRIES is named not-adopted in the lesson with a one-line reason, enumerated at freeze, including: conlang-scholarship.amend-2026-10-23b.md, -23c.md, -2026-10-24.md, conlang-methodology.amend-2026-10-24.md, and the conlang-methodology.md round-1 amendment proposal, plus the naming-systems / calendar / era / verification families."

## F6 — MAJOR (C kill rule / REJECTS): "quarantine-REFUSED" is an undefined token across three namespaces
`SOURCES.append.md` contains no REFUSED/quarantine marker (grep = 0). The round-72 quarantine artifact (`.ufo/waves/round-72/assimilation/quarantine-slice`) lists **register** ids S776–S835 with labels `payload-absent` / backticked — a different namespace from staged-package ids (S869, S894, S910). The kill rule's set is not machine-enumerable as worded, and the assignment's own warning ("THREE namespaces: join by URL/document only") is violated by the wording.
**Fix:** "…cites a staged row refused for quarantine in the round-73 scout verdict receipt (staged namespace) or listed in .ufo/waves/round-72/assimilation/quarantine-slice (register namespace); every id in the lesson names its namespace".

## F7 — MINOR (C before): "only conlang craft owner" carries no command and is falsified by a naive sweep
Base holds two conlang knowledge files (`linguistics/conlang-methodology.md`, `synthesis/conlang-blueprint-template.md`). The clause is true in substance (the template is a fill-in template; neither cites a research venue) but is not command-re-derivable (§9 bullet 1; CORPUS "a negative claim carries its sweep").
**Fix:** append: "`find corpus/knowledge -iname '*conlang*' | wc -l` = 2 (linguistics/conlang-methodology.md — the sole craft-method owner; synthesis/conlang-blueprint-template.md — a fill-in template); `grep -icE 'unito|msu\.ru|rudn|cyberleninka|phonologist'` over both = 0."

## F8 — MINOR (axes_note): the L0 citation path does not exist in the lane tree
`.ufo/l0-questions.md:47` resolves only at the **fleet root** (`/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:47`, the `kotodama | round-11` row — verified, content correct); the lane has no such file, and every other path in claims.json is lane-relative.
**Fix:** cite "/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:47 (fleet root; no such file in the lane)".

## F9 — MINOR (Ca APPENDONLY): one command cannot cover two repos
"git diff --numstat base..<lands> shows zero removed lines in LOG.md, … and the round-72 fleet report (fleet git)" — the fleet report is not in the lane repo, so the single command cannot show it.
**Fix:** split: "…zero removed lines in LOG.md, SCORECARD.md, corpus/lessons/round-72.md, corpus/lessons/round-71.md (lane git); and, in the fleet repo, zero removed lines in the round-72 fleet report (fleet git)."

## F10 — MINOR (C COLLCHECK): two artifacts unnamed
The regenerated renumber map's path and the planted-collision proof's receipt path are unstated ("superseded by a regenerated map … filed bytes untouched" is ambiguous about where the new map lives).
**Fix:** "…superseded by .ufo/waves/round-73/assimilation/id-renumber-map.json regenerated from S876 (old→new recorded; .ufo/waves/round-71/assimilation/id-renumber-map.json bytes untouched), with the planted indented-collision failure receipt at .ufo/waves/round-73/assimilation/collcheck/ committed before data."

## F11 — MINOR (Ca BASEMISMATCH): the ">= 8 pairs" floor is asserted pre-sweep
Only four pairs are evidenced (R1, R2, R3, README). If the wave-1 sweep finds fewer than 8, the claim cannot freeze as written.
**Fix:** "…>= 8 pairs, the floor justified at freeze by the wave-1 sweep receipt enumerating the pairs; a shortfall lowers the floor in this file before freeze, never after data."

## F12 — VERIFICATION GAP (both claims; not a defect): declared pre-data artifacts do not exist yet
`reports/round-73/` is empty at base: no accept-c.py, accept-ca.py, ledger.json, telemetry/gap-sweep.txt, telemetry/census-start.txt, and no do-nothing/junk-row/stub control receipts. Check (d) — predicate sentence == counter leg == receipt label — is therefore unverifiable; the declared labels (ACCEPT-C-73 / ACCEPT-CA-73) are at least identical between each `after` and `counter` string. QUALITY 9 requires every declared command in a two-way-checked pre-dispatch receipt; the claims' "receipts committed before dispatch of wave 2" matches that but is unexercised.

# Residual risk and verification gaps

- The TENTATIVE 5-row map does not close the pair's citation set (see F1); the frozen row set must enumerate: the five mapped documents + the S728-cited document (re-pointed or its clause dropped) + S894 (per its frozen disposition) — every decision old→new in the lesson.
- GATE leg hard-codes access date 2026-10-25 (leg + kill rule): acceptable only if the wave lands same-day; safer to declare "the round's declared access date" once at freeze.
- Census `validate` exits 0 now, but the C CENSUS leg says "at the registry bytes of <lands>" — the closure must run it against materialized <lands> (or the mirror `validate --file` path the SCRATCHMIRROR leg already provides), not the moving worktree.
- Do-nothing controls (e): as declared, junk rows fail ENTRIES/ROWS, base lands fail REPAIR legs, stub rows fail NOSTUB — structurally sound, but unproven until the counter exists (F12). Per §9 these receipts must land before data, and I could not score them.
- Waiver reasoning (g) is honest (quotes verbatim, pause real and operator-owned); residual risk only if the operator rules the L0 pause does not excuse the lowest-axis obligation.
- Out-of-scope note: an IRC flag from R50ReopenRowS105 (round-50 spans.tsv offsets) arrived and was retracted by its author before I acted; no round-73 claim touches it.

Tooling record: no tools installed or upgraded (none needed); all work via read-only git (`git show`/`ls-tree`/`grep`/`ls-files`), `sources-census.sh validate` (read-only; output scratch at /tmp/RevClaimsFidelity-census.{out,err}), and reads of the read-only staged tree. No writes outside this report file.
