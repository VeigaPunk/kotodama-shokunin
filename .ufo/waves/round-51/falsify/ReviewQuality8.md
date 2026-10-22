# ReviewQuality8: QUALITY criterion 8 and its round-51 application

- Seat: KotodamaR51a3.ReviewQuality8 (leaf reviewer, round 51 attempt 3, falsify wave)
- Date: 2026-10-22
- Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin (branch main). Read-only for this seat.
- Commits: claim base bff83ba; declaration and dry-run receipt 1f97472 (06:22:52 -0300); claim D 35f0d49; claim C da31d3c; records 9feb69e (06:44:39 -0300, which landed criterion 8 and the round-51 lesson).
- Item attacked: `corpus/QUALITY.md:33` (criterion 8), applied to `reports/round-51/claims.json` and `reports/round-51/separability-manifest.json` against `reports/round-51/telemetry/declaration-dry-run.txt`.
- Basis tags used below: **replayed** = run by this seat in a private clone; **read** = text or code read at the cited line; **inferred** = marked as inference.

## Verdict: FAILS

Criterion 8 as landed does not hold, and round 51 does not meet it.

1. **Grounding: partial.** The round-50 record supports the consequence: the frozen check ran on the wrong file and exited 2. It does not support the dry-run rule, the absent-land exemption, or the clause "fails the declaration, not the round". Those were written in round 51. R51-M1 and criterion 8 cite each other.
2. **Checkability: not as claimed.** The closure checks one direction only (receipt to declaration), so it cannot see a declared command the receipt omits. Exit code 1 means three different things here, and the criterion gives no way to tell them apart. No tool under `tools/` reads the receipt (searched; see F6).
3. **Application: two declared acceptance commands were never dry-run on their exact input** (`separability-manifest.json:13-17` and `:30-35`). The lesson's statement that every round-51 counting and acceptance command was dry-run (`corpus/lessons/round-51.md:100`, and the debt-1 cell at `:16`) is false.
4. **What holds:** the counting and separability commands in the receipt match their declarations. The receipt was committed with the declaration (1f97472) and has no later commit. The six replayed exit codes reproduce. Every declared command passes after landing. The defect is the missing pre-dispatch run and the rule's wording, not a wrong command.

Calibration: criterion 8 is a process rule, not a proposition about the world, so no code from `corpus/knowledge/verification/calibration-registry.md:35-39` applies.

## Commands run and results

Clone: `/fast/scratch/hyaku/kotodama-r51a3-falsify/ReviewQuality8` (`git clone --shared`; detached checkouts 1f97472, 9feb69e, bff83ba; realpath checked, no symlink).

| # | cwd | Command | Exit | Output |
|---|---|---|---|---|
| 1 | lane | `git log` and `git show --stat` for 1f97472, 35f0d49, da31d3c, 9feb69e; `git log --` on the receipt, claims and manifest | 0 | 1f97472 has 5 files (+286); 9feb69e has `corpus/QUALITY.md` (+2) and `corpus/lessons/round-51.md` (+111); receipt history is 1f97472 only |
| 2 | lane | `git show <rev>:<path> \| sha256sum` (claims at HEAD and 1f97472; manifest and receipt at 1f97472); `git diff --stat 1f97472 HEAD -- reports/round-51 tools corpus/QUALITY.md` | 0 | claims d991616c…, same at HEAD; manifest 8eabed41…; receipt 1f1a27fc…; diff shows only `corpus/QUALITY.md` (+2) |
| 3 | clone | `test ! -e` then `git clone --shared`, `realpath`, `git checkout --detach 1f97472`, parent, presence and status checks | 0 | realpath is the clone path; 1f97472 parent is 5ab3634 (the receipt's tree); absent at 1f97472: `corpus/lessons/round-51.md` and the sign-language entry; status empty |
| 4 | clone | Replay at 1f97472 of each declared argv, exactly as stored in the committed JSON (see the inventory table) | see table | see table |
| 5 | clone | `git checkout --detach 9feb69e`; `git diff --stat 1f97472 9feb69e -- <declaration files>` | 0 | empty diff: the declaration files did not change |
| 6 | clone | Replay at 9feb69e of the same argvs | see table | see table |
| 7 | lane (cwd error, disclosed) | `git checkout --detach bff83ba` in the clone, then `find` and `grep -rliP` run in the lane by mistake | 0 | results discarded: lane results include the landed sign-language entry. Read-only; nothing written |
| 8 | clone | `find corpus/knowledge` with the C gap-evidence name patterns; `grep -rliP` with the C gap-evidence topic pattern; `find corpus/knowledge -name '*.md'` piped to `wc -l` | 0 / 1 / 0 | find: 0 files; grep: no matches (grep exits 1 on no match); knowledge markdown count 226; sign-language entry absent at bff83ba |
| 9 | lane, read-only | `git --no-pager diff --stat bff83ba 5ab3634` | 0 | 2 files: `reports/round-51/calibration/oracle.json` (309 lines), `ruler.py` (263 lines); 572 insertions |
| 10 | search, read-only | Receipt readers in `tools/`, `reports/round-51/`, `reports/round-28/`; round-51 strings in `tools/`; dry-run wording in round-50 records (word-boundary pattern) | n/a | only `claims.json:54` and the receipt name the receipt; only hit in `tools/` is a fixture in `tools/harness/receipt_guard_adoption.py:1028-1135`; no round-50 match |
| 11 | lane, read-only | `realpath` and existence of `.ufo/waves/round-51/falsify` | 0 | exists; realpath unchanged |

Replay results (exact declared argv; cwd = clone):

| Declared command | At 1f97472 (declaration commit) | At 9feb69e (records commit) |
|---|---|---|
| separability (`claims.json:10`) | exit 2, "unit C lands ... absent from the worktree" | exit 0, "SEPARABILITY: 0 findings", 3 units, acceptance_runs=2 |
| claims-agree (`claims.json:12`) | exit 0, "AGREE claims=['C', 'D']" | exit 0, same |
| D counting (`claims.json:23`) | exit 0, "rows=11 resolved=11 distinct=11" | exit 0, "rows=15 resolved=15 distinct=15" |
| C counting (`claims.json:40`), find piped to wc -l | exit 0, "226" | exit 0, "227" |
| C after-required sweep (`claims.json:42`) | exit 0, footer total 226, footer_ok True | exit 0, footer total 227, linguistics 26, footer_ok True |
| D acceptance (`separability-manifest.json:13-17`) | exit 1, no output (value is 11, not 15) | exit 0 |
| C acceptance (`separability-manifest.json:30-35`), whole argv | exit 1, no output (count test fails at 226; S-id leg never reached) | exit 0, "C_SID_UNRESOLVED 0 []" |
| C S-id snippet run alone (argv element 4 as `python3 -c`) | exit 1, FileNotFoundError at `open(p)` on the absent entry | not run alone; the whole C argv above printed "C_SID_UNRESOLVED 0 []" |
| Historical control (receipt `:19-21`, undeclared) | exit 2, "manifest is missing base, schema" | not run |

## Declared-command inventory

Every command string or argv in `claims.json` and `separability-manifest.json`, compared with the receipt.

| # | Declared command (location) | Receipt entry | Dry-run status |
|---|---|---|---|
| 1 | Separability argv (`claims.json:10`) | `:16-18` and `:38-40`, exit 2 at unit C | Dry-run on exact input. Stops at the first absent land (F4). |
| 2 | `claims-agree.py` (`claims.json:12`) | `:13-15` and `:35-37`, exit 0 | Dry-run. |
| 3 | D counting (`claims.json:23`) | `:2-4` and `:24-26`, rows=11 | Dry-run. Matches `before` (`claims.json:24`). |
| 4 | C counting (`claims.json:40`) | `:5-7` and `:27-29`, 226 | Dry-run. |
| 5 | C sweep (`claims.json:42`) | `:8-12` and `:30-34`, annotated "(tail 3)" | Run. The annotation hides whether exit 0 belongs to sweep or to a pipe (F10). |
| 6 | D acceptance (`separability-manifest.json:13-17`) | none | **Not dry-run** (F2). |
| 7 | C acceptance (`separability-manifest.json:30-35`) | none verbatim. Parts appear only as rows 4 and 5. | **Not dry-run** (F2). The source-ID leg never ran before landing (F5). |
| 8 | C gap evidence, find (`claims.json:34`) | none | Not in receipt. Passes at base: 0 files (F9). |
| 9 | C gap evidence, grep -P (`claims.json:34`) | none | Not in receipt. Passes at base: no matches (F9). |
| 10 | C gap evidence, sibling-lane grep (`claims.json:34`) | none | **Unrun** by this seat (outside lane bounds) (F9). |
| 11 | base_note git diff (`claims.json:8`) | none | Matches prose: 2 files, 572 insertions (F9). |
| 12 | Receipt control (`:19-21`) | undeclared | Undeclared, exit 2 with a non-absent message (F10). |
| 13 | Receipt sources-census line (`:41-43`) | undeclared | Undeclared. Not re-run by this seat (fleet script). |

The records unit (REC, `separability-manifest.json:37-52`) has no acceptance argv and no command.

Declared commands not dry-run on their exact input: **rows 6 and 7** (two of the round's acceptance argvs).

## Findings

Ordered by severity. Each finding gives the pointer, the evidence, the basis tag, and the smallest fix.

**F1 (high): the closure checks one direction only.**
- Pointer: `corpus/QUALITY.md:33`, "each command in the dry-run receipt matches its declaration verbatim and exits 0 or stops only at an absent land".
- Evidence: it checks receipt to declaration. Nothing requires each declared argv to appear in the receipt. The receipt has no entry for `separability-manifest.json:13-17` or `:30-35`. The seat's own draft had the missing direction (`.ufo/waves/round-51/build/ScribeQualityCriterion.md:22`, "For every counting/acceptance/separability command declared ... verify a receipt entry whose argv matches verbatim"); the landed text dropped it. Even with the control and census lines excluded, the closure as written does not flag the two omitted acceptance argvs. Basis: read, replayed.
- Smallest fix: add to `QUALITY.md:33`: "and every declared counting or acceptance argv in claims.json and the separability manifest has a receipt entry whose argv matches verbatim".

**F2 (high): round 51 does not meet criterion 8. Two declared acceptance commands were never dry-run.**
- Pointers: `separability-manifest.json:13-17` (D acceptance) and `:30-35` (C acceptance). The lesson claims otherwise at `corpus/lessons/round-51.md:100` ("every round-51 counting and acceptance command was run on its declared input before wave 1") and `:16` ("every declared command was dry-run before dispatch").
- Evidence: `declaration-dry-run.txt` has no entry for either. Replayed pre-landing, both exit 1 with no output (values 11 and 226). Replayed post-landing, both exit 0. The "shown able to fail" control (receipt `:19-21`) shows only that the checker rejects a wrong manifest. It does not show that these argvs ran. Basis: replayed.
- Smallest fix: correct the two lesson cells to say these argvs were not dry-run. Add a receipt block with the pre-landing results (exit 1, values 11 and 226, labelled as expected before landing) and a post-landing block (exit 0, values 15 and 227, 0 unresolved).

**F3 (high): the exit rule cannot be met by the round's acceptance commands.**
- Pointer: `corpus/QUALITY.md:33` ("exits 0 or stops only at an absent land"), applied to "every declared counting or acceptance command".
- Evidence: the acceptance argvs check the post-landing state. Before landing they exit 1 for a value reason (F2), and the criterion allows neither exit 1 nor a value reason. Exit 1 has three meanings here: a value mismatch (D and C acceptance), an absent file (FileNotFoundError in the source-ID snippet), and a real source-ID finding (the snippet's own `sys.exit(1)`). The criterion gives no stderr rule that separates them. Basis: replayed.
- Smallest fix: split the rule. Counting argvs exit 0 on the declaration tree. Acceptance argvs run before landing with no input-shape error and may fail only with an absent-land message or with their before-value printed. Acceptance argvs must exit 0 in a post-landing receipt. A closure classifies by stderr text, not by exit code.

**F4 (medium): the separability dry run covers only units before the first absent land.**
- Pointers: `tools/check-claim-separability.py:672-680` (order: parse, load units, novelty, static, overlap, acceptance); `:451-458` (an absent land raises at once); `:683-706` (acceptance runs). Receipt `:16-18` and `:38-40` report only unit C. `separability-manifest.json:37-52`: unit REC also has an absent land (`corpus/lessons/round-51.md`, absent at 1f97472) and it was never reported.
- Evidence: the replay at 1f97472 stops at unit C. No novelty, static, overlap or acceptance check ran. The full run at 9feb69e reports 0 findings and 2 acceptance runs. The lesson's "stops only at the not-yet-landed C entry" (`corpus/lessons/round-51.md:100`) overstates: the dry run proved parse and loads up to C. Criterion 7's pre-dispatch run (`QUALITY.md:31`) is the same checker and has the same limit. Basis: replayed, read.
- Smallest fix: state in criterion 8 that an absent-land exit proves parse and loads only, and require a post-landing receipt of the separability command. Correct `round-51.md:100`.

**F5 (medium): the absent-land exemption lets a dry run stop before the command's own logic.**
- Pointer: `separability-manifest.json:34`. The source-ID snippet's first statement is `e=open(p).read()`, and `p` is the entry that does not exist before landing.
- Evidence: the pre-landing replay stops at `open(p)`, so the used-by check (index 11 of the SOURCES table; header at `corpus/SOURCES.md:28`, used-by is the eleventh column) never ran before landing. After landing it runs and reports 0 unresolved. Basis: replayed.
- Smallest fix: run the snippet before landing in the private clone against a stand-in entry, or name the post-landing receipt as this check's only evidence.

**F6 (medium): "checkable from committed bytes" is not implemented, and the receipt is only partly identifiable.**
- (a) No reader. A search of `tools/` finds no reader of `declaration-dry-run.txt` or of round-51 artifacts. The one round-51 string is a test fixture (`tools/harness/receipt_guard_adoption.py:1028-1135`). Basis: read.
- (b) No identity. The receipt has no input hashes and no argv records. I found no generator for it under `tools/` or `reports/round-51/`. Block 2 (`:23`, 09:22:43Z) ran on tree 5ab3634, which is the parent of 1f97472 (verified). The declaration commit was made 9 seconds later (09:22:52Z), so block 2 is attributable with high confidence (inferred). Block 1 (`:1`, 08:21:28Z) predates `claims.json:5` declared_at 08:31Z and cannot be tied to committed bytes.
- (c) Exit codes are text. The six replayed exits match the receipt in both blocks. A closure reading committed bytes can read the exit codes, not verify them.
- Smallest fix: either write the closure as a script that compares argvs in both directions, classifies errors by stderr text, and checks input hashes; or reword the sentence to "a reviewer reads the receipt by hand". Record a sha256 of claims.json and the manifest in each receipt block.

**F7 (medium): grounding is partial and circular.**
- (a) The round-50 Decision (`corpus/lessons/round-50-verifier-spotcheck.md:5-11`), Pins (`:13-23`) and `reports/round-50/telemetry/final-conformance.json:29-39` establish the consequence: the frozen exit-0 check ran on `reports/round-50/claims.json`, exited 2, and a substitute cannot satisfy it.
- (b) A word-boundary search of `round-50-verifier-spotcheck.md` and `round-50.md` finds no "dry run", "before dispatch" or "pre-freeze". Routed debt 1 (`:93-94`) asks for "compatible own-round manifest inputs", not a dry run.
- (c) R51-M1 (`corpus/lessons/round-51.md:100`) names "now QUALITY criterion 8" as its capture. Criterion 8 names R51-M1 as its grounding. Each cites the other.
- (d) Criterion 8 cites the Decision for the exact message "SEPARABILITY_INPUT_ERROR manifest is missing base, schema". That message is in Pins (`:22-23`) and in `final-conformance.json`, not in the Decision.
- Smallest fix: cite Pins and `final-conformance.json` for the message. Remove "Grounded in the round-50 Decision" from the dry-run clause. State the dry-run rule as a round-51 decision grounded in R51-M1 alone, and drop the circular capture.

**F8 (medium): the round's own declared rule is narrower and stricter than criterion 8.**
- Pointer: `reports/round-51/claims.json:54` (`dry_run_rule`): counting and separability commands only, "each must exit without an input error".
- Evidence: acceptance argvs are outside it. The separability exit 2 (receipt `:16-18`, `:38-40`) fails its literal words, and criterion 8 relaxes that for absent lands. The declaration was not amended to match. Basis: read.
- Smallest fix: add a note to the R51-M1 row that `claims.json:54` is narrower than criterion 8 and omits acceptance. Do not edit the landed declaration.

**F9 (low): "declared counting or acceptance command" is undefined.**
- Pointers: `claims.json:34` (C gap evidence: find, grep, and a sibling-lane grep) and `:8` (base_note git diff). Neither is a `counting_command` field.
- Evidence: the find, grep and base diff pass at base (0 files; no matches; 2 files, 572 insertions). The sibling-lane grep is unrun (outside lane bounds). Basis: replayed.
- Smallest fix: define the term in criterion 8 as "every command named as the source of a before or after value, in any field".

**F10 (low): receipt presentation defeats the literal check.**
- Pointers: `declaration-dry-run.txt:8` and `:30` ("(tail 3)" hides whether exit 0 belongs to sweep or to a pipe); `:19-21` (historical control: undeclared, exit 2 with a non-absent message); `:41-43` (sources-census: undeclared).
- Smallest fix: put the control and census lines in a labelled block outside the verbatim check. Run the sweep without a pipe and record its exit code.

**F11 (low, out of scope for criterion 8; for the separability reviewer).**
- Pointer: `separability-manifest.json:37-52` (unit REC). It lists `claims.json` and `claims-agree.py`, which 1f97472 landed, and `SCORECARD.md`, `LOG.md`, `SHONEN.md`, `corpus/lessons/README.md`, which 9feb69e did not change. The commit that lands those four is not identified in the record. Basis: read, git show --stat.

## Answers to the three questions

1. **Grounded in a lesson (the spot-check Decision and R51-M1)?** Partly. The Decision and Pins ground the consequence (exit 2, substitute cannot satisfy the frozen condition). Nothing in the round-50 record grounds the pre-dispatch dry run or the absent-land exemption (F7). R51-M1 grounds the rule only by citing criterion 8 as its capture, and its own fix claim is false (F2).
2. **Checkable from committed bytes, as it claims?** No, not as written. The declarations and receipt are committed together and the receipt is unchanged since (holds). But the closure checks one direction only (F1), no tool implements it (F6a), exit 1 cannot be classified by exit code (F3), and block 1 cannot be tied to committed bytes (F6b).
3. **Round 51: declared commands not dry-run on their exact input?** Two: `separability-manifest.json:13-17` (D acceptance) and `:30-35` (C acceptance, including its source-ID leg). All counting and separability commands in `claims.json` were dry-run (rows 1 to 5 in the inventory).

## Residual risk and verification gaps

- Block 1 of the receipt (08:21:28Z) has no input identity. If it ran on different declaration bytes, its six exit codes would describe a different declaration. The replays of the committed declaration show the same codes, so the risk is low, but it is unverified.
- Post-landing replays ran at commit 9feb69e. The lane head may have moved since; I used commit hashes throughout.
- Two checks are unrun: the fleet census script (receipt `:41-43`) and the sibling-lane grep (`claims.json:34`). Both read outside the lane, and neither changes the verdict on criterion 8.
- The held prior-attempt material (`reports/round-51/calibration/`, `/fast/scratch/hyaku/kotodama-r51-*`, `kotodama51-*`) was not read, per bounds.
- Attempt 1 and attempt 2 declarations are not in committed history apart from 1f97472. I did not inspect them.
- The checker's own `--selftest` was not run. Its ordering claims come from code reading (`check-claim-separability.py:672-706`) and are confirmed by the observed replay behaviour.

## Unrun checks

- `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate` (receipt `:41-43`): fleet script, outside lane bounds.
- Sibling-lane topic grep (`claims.json:34`): outside lane bounds.
- `python3 -B tools/check-claim-separability.py --selftest`: not needed for the verdict.
- `tools/gates/provenance-audit.py`: not in criterion 8's scope.

## Tooling and bounds

- Installs or updates: none. Tools used: git (read-only), system python3 (stdlib, the declared commands), sha256sum, find, grep, sh. No pacman, no uv, no npm, no jj.
- One private clone was created at `/fast/scratch/hyaku/kotodama-r51a3-falsify/ReviewQuality8` (detached checkouts 1f97472, 9feb69e, bff83ba). Realpath was checked. Nothing was written to the lane apart from this report.
- One disclosed mistake: at step 7 of the command table, a read-only `find` and `grep` ran in the lane because of a wrong cwd. Their output was discarded and the base-state results were re-run in the clone (step 8).

## Sources opened

None. This item has no source rows and no URLs were opened.

## Suggested closure sentence (for the L1 to decide; not applied)

"A closure reads committed bytes only. Every counting argv in claims.json and every acceptance argv in the separability manifest must appear verbatim in the dry-run receipt, and every receipt argv must match a declared argv verbatim or sit in a labelled control block. A counting argv exits 0 on the declaration tree. An acceptance argv exits 0 in a post-landing receipt; before landing it may stop only at an absent land or print its before-value, and the closure classifies stderr text, not exit codes, to tell these apart."
