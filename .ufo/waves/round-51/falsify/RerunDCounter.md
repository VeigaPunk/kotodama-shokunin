# RerunDCounter: claim D counter rerun (round 51, attempt 3, FALSIFY)

- Seat: KotodamaR51a3.RerunDCounter (leaf; read-only on the lane). Sandbox writes only under `/fast/scratch/hyaku/kotodama-r51a3-falsify/RerunDCounter/` (clone, plus `.runs/` trees). This file is the only lane file written.
- Item attacked: claim D (judged on depth): the counter `reports/round-51/boundary-count.py` run on every required tree, and the claim statement that the counter is meant to measure.
- Lane branch tip: `9feb69ec8ef3de00c2de41eea0286ad5031eab17`. Claim base: `bff83ba65bf9559af4d7567e81703059667a0005`. Declaration commit: `1f97472`. D commit: `35f0d49`.
- Date of checks: 2026-10-22 (about 09:50 to 10:10 UTC).

## Verdict: HOLDS-WITH-FIXES

- The printed value holds on every tree I built. The counter file has not changed since declaration. The declared falsifier ("any other printed value") does not trip.
- The printed 15 depends on one row that was already in base: `civilizations/` (tip entry line 43, base line 41). It has no `path:line` anchor, and it names a directory of 94 files, not one neighbour. The claim statement requires a `path:line` anchor and one neighbour for each row. Read literally, D fails by one row (strict count 14/14/14, exit 1). The L1 has to settle this rule before D is accepted (F1).
- Two smaller fixes are needed: D's own lead sentence overstates the table (F2), and one row-45 anchor does not support its cell (F3). The F3 fix was tested in the sandbox.
- Depth note: the counter measures row count and anchor resolution only. It cannot see whether a cell is supported. The depth problems I found (F1 to F3) are of that kind.

## (a) to (d): required measurements

Hashes: counter `fb1d5c89d2ed3ea32a699692901fa24fed28020f5a930fc7198e2b62f1b14cc2`; entry at base and at 1f97472 `16195696927b9c6cb1a96aed53d183097e2a39943503852f69656118dc6f3c32`; entry at 35f0d49 and tip `5c2e09d04652920ae5c8d2f64c175b871b5b98b3cf7a0327ccfe063390c019d0`.

| Req | Tree | Commit | Counter | Entry | Printed line | Exit |
|---|---|---|---|---|---|---|
| (a) | sandbox clone at branch tip | 9feb69e | fb1d5c89 | 5c2e09d0 | `rows=15 resolved=15 distinct=15` | 0 |
| (a) | D commit tree (git archive) | 35f0d49 | fb1d5c89 | 5c2e09d0 | `rows=15 resolved=15 distinct=15` | 0 |
| (b) | D-only tree: base plus 35f0d49 entry and counter | bff83ba + D lands | fb1d5c89 | 5c2e09d0 | `rows=15 resolved=15 distinct=15` | 0 |
| (c) | base as committed | bff83ba | ABSENT | 16195696 | `python3: can't open file ... [Errno 2] No such file or directory` | 2 |
| (c) | base plus declared counter (control) | bff83ba + counter from 1f97472 | fb1d5c89 | 16195696 | `rows=11 resolved=11 distinct=11` | 0 |
| ref | declaration tree (git archive) | 1f97472 | fb1d5c89 | 16195696 (equals base) | `rows=11 resolved=11 distinct=11` | 0 |
| ref | lane working copy, read-only run | tip | fb1d5c89 | 5c2e09d0 | `rows=15 resolved=15 distinct=15` | 0 |

- (c) The counter is not in the base commit. The expected 11/11/11 comes from the declaration tree, whose entry bytes equal base. It reproduces when the declared counter is copied into the base tree.
- (d) `git log -- reports/round-51/boundary-count.py` lists one commit, `1f97472` (status A). The blob `98d7131554899a92c7fd82054c056c6abe38459b` is the same at 1f97472, 35f0d49 and 9feb69e, and the lane working copy matches it. The counter was not edited after declaration. Commit time 06:22:52 -0300 (09:22:52Z) agrees with the claims.json re-declaration stamp (09:22Z) and the receipt re-run stamp (09:22:43Z).
- The counter is listed under D's `lands`, but it entered git in `1f97472`, not in D's commit. `35f0d49` changes only the entry (`git show --name-status 35f0d49`: `M corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`). The D-only tree therefore uses the counter as it stood at 35f0d49, which is the same blob.

## Controls and fix test (sandbox only)

A strict copy of the counter was made and two lines changed: `boundary-count.py:25` now requires a line number on the first file anchor (the other anchors already need one), and `:46-47` now returns None for directory anchors. Original and strict counts:

| Tree | Original counter | Strict copy |
|---|---|---|
| tip | 15/15/15, exit 0 | 15/14/14, exit 1 |
| D-only | 15/15/15, exit 0 | 15/14/14, exit 1 |
| base plus declared counter | 11/11/11, exit 0 | 11/10/10, exit 1 |
| tip plus row-45 fix (F3) | 15/15/15, exit 0 | 15/14/14, exit 1 |

## Findings

**F1, MEDIUM. The printed 15 relies on a directory anchor that the statement does not allow.**
- Evidence: tip entry `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:43` (row "`civilizations/` regional entries", base line 41, already present in base). The directory `corpus/knowledge/civilizations/` holds 94 `.md` files.
- The counter accepts directory anchors: `reports/round-51/boundary-count.py:11` (docstring, "`dir/` names an existing knowledge directory") and `:46-47` (the branch that returns the directory).
- The statement `reports/round-51/claims.json:18` says each row names "one distinct in-corpus neighbour by a backticked path:line anchor that resolves", and that "the existing 11 rows keep their neighbours". The required print is at `:25`.
- Analysis: with the existing neighbours fixed, all 15 rows can be path:line anchors only by re-anchoring row 43 to one file (which changes its neighbour set) or by adding a 16th row (which breaks "grows to 15"). The statement therefore cannot be met as written, so it has to be amended or the row has to change.
- Smallest fix (L1 decision; I did not edit anything): either (a) amend the statement at `claims.json:18` before acceptance to allow one directory anchor, for the regional row, which the counter docstring already documents; or (b) keep the statement, in which case D is FAILS as worded (14/14/14, exit 1). I recommend (a), recorded as an explicit declaration change.

**F2, LOW. D's own lead sentence overstates the table.**
- Evidence: the sentence D added at `entry:29` (diff hunk `@@ -28,0 +29,2 @@`) says "Each row names one neighbour and the line that shows what it owns" and "the body section named in the boundary cell develops it". Row 43 (`entry:43`) names no line. Eight of 15 rows (lines 33 to 38, 40 and 43) name no body section in their boundary cell.
- Smallest fix: reword line 29 to match the table. For example: "Each row names a neighbour by line, except the regional row, which names its directory. Where a boundary cell names a section, that section develops the seam."

**F3, LOW. The row-45 anchor does not support its full cell.**
- Evidence: `entry:45` says "the consistency rule that an animal taboo implies a rite, and the symbol grammar that enforces it". The anchored line `symbolism-synthesis-method.md:69` says only "An animal taboo implies a rite; write both or neither". The grammar is defined at `symbolism-synthesis-method.md:23` ("A symbolic grammar is the total system by which a culture maps...").
- Fix tested in sandbox copy `.runs/fix-row45`: anchor changed to `symbolism-synthesis-method.md:69,:23`. Diff shows only line 45 changed. Counter prints `rows=15 resolved=15 distinct=15`, exit 0. The count is unchanged because both anchors point to the same file. Not applied to the lane; the L1 should apply it.

**F4, MEDIUM (records; outside my counter scope, observed in the receipt). The dry-run rule is not met on the record.**
- Evidence: `reports/round-51/telemetry/declaration-dry-run.txt:17-18` and `:39-40`: `SEPARABILITY_INPUT_ERROR unit C lands 'corpus/knowledge/linguistics/sign-languages-manual-modality.md' ... exit 2`, in both declaration-tree runs (08:21:28Z and 09:22:43Z). `claims.json:54` (dry_run_rule) requires that "each must exit without an input error". `claims.json:11` requires exit 0.
- The failure is structural: unit C's land does not exist on the declaration tree, so this rule cannot pass there. At tip (sandbox run), `SEPARABILITY: 0 findings`, `SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=2`, exit 0.
- Smallest fix (records seat or L1): append a dated tip re-run to the receipt, and either scope dry_run_rule to lands that exist on the declaration tree or record the exception.

**F5, LOW (hygiene). An untracked bytecode file is in the lane.**
- Evidence: `reports/round-51/__pycache__/boundary-count.cpython-314.pyc`, mtime 2026-10-22 06:28:06 -0300, which is before this seat started. My runs used `python3 -B` and wrote nothing. I did not touch the file.
- Smallest fix: the L1 deletes it, or confirms it is excluded from the commit.

**F6, LOW (latent counter defects; code reading, not executed).**
- `boundary-count.py:39-40`: a top-level `corpus/knowledge/x.md` has `name == relpath`, so the same path is appended twice under one key, `len(hits) != 1`, and every anchor to it fails. No top-level `.md` exists at tip (count 0), so this is not exercised.
- `boundary-count.py:25`: the first `:N` is optional, so a bare `file.md` token resolves with no line. No current row uses a bare file token, so this is not exercised.
- Smallest fix: skip the duplicate key when `relpath == name`, and require the first `:N` (as in the strict copy).

**F7, INFO (provenance).** Git has no earlier version of the counter or of claims.json: their first commit is `1f97472`. Attempt-2 bytes therefore cannot be checked from git. "Re-declared unchanged" rests on claims.json and on the hash at 1f97472.

**F8, INFO (must-not-cite checks hold).**
- Added lines in D's diff (`git diff -U0 bff83ba 35f0d49`) contain no S-id of S071 or higher, no `sign-lang` or `manual-modality`, no `round-51`, and no `lesson`.
- Tip S-ids are S048 to S069, the same as base. Base S-ids of S071 or higher: 0.
- The only "lesson" hit is `entry:9` ("the round lesson's located quote"). It is identical at base line 9, so it is pre-existing and not D's.
- The D-only tree, which has no C-entry file, still resolves 15/15/15. So no row depends on the C entry.

**F9, INFO (anchor support spot-check, 5 of 15 rows).**
- `ritual-liminality.md:63` supports row 44. The calendrical row names the Vedic agnihotra milk oblation and the aśvamedha royal horse rite. Calling the horse rite a "herd product" is a stretch, for the content seats.
- `symbolism-synthesis-method.md:69` supports only the taboo-implies-rite clause (see F3).
- `celestial-symbolism-calendars.md:28` supports row 46 ("pastoralists on milky/river figures").
- `numerals-and-measures.md:101` supports row 47 (counting units, including "head of cattle").
- `sacred-kingship-mythic-charter.md:65` supports row 42 (king as shepherd, audited by omens and the gods' assembly).
- All four new rows are developed in the body: row 44 through `entry:148`, rows 45 and 46 through `entry:155` and `:156`, and row 47 through the seam sentence at `entry:93`. The shepherd-king row 42 aligns with `entry:154`.
- Not checked: support for the other 10 existing rows (content seats).

## Commands run (exit codes not echoed are marked; no error output)

Shorthand: `C` = `/fast/scratch/hyaku/kotodama-r51a3-falsify/RerunDCounter` (sandbox clone); `L` = `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (lane, read-only).

1. `read` claims.json, boundary-count.py and `~/.omp/agent/RULES.md`: read OK.
2. `git clone -q --shared $L $C`, then `realpath`: `CLONE_OK`; exit 0. A first attempt failed at the tool layer ("Service mode does not accept async or timeout"); no command ran.
3. `git -C $C rev-parse --abbrev-ref HEAD` gave `main`. `git -C $L rev-parse main` and `git -C $C rev-parse main` both gave `9feb69ec8ef3de00c2de41eea0286ad5031eab17`. `git log --oneline -n 14 main` listed 9feb69e, da31d3c, 35f0d49, 1f97472, 5ab3634, bff83ba and older commits. `python3 --version` gave `Python 3.14.8`. `rev-parse --verify` of bff83ba, 1f97472, 35f0d49, da31d3c and 9feb69e: all resolve. Exit not echoed.
4. `git show --no-patch` and `--name-status` for 1f97472, 35f0d49, da31d3c and 9feb69e, and `git diff --name-status bff83ba main`: 1f97472 adds five files including the counter; 35f0d49 modifies the entry only; da31d3c adds the C entry and changes README and SOURCES; 9feb69e changes QUALITY and adds the lesson. Exit not echoed.
5. `git cat-file -e`, `git rev-parse rev:path` and `git show rev:path | sha256sum` for the counter and entry at bff83ba, 1f97472, 35f0d49 and 9feb69e: values as in the table above. Exit not echoed.
6. `git log --format=... --name-status -- reports/round-51/boundary-count.py`: only `1f97472 ... A`. Exit not echoed.
7. `sha256sum` of the lane counter and entry, and `git show main:<path> | sha256sum`: all equal. `git -C $L diff --name-only main -- <paths> corpus`: no output. Its exit code was not captured because a `head` pipe followed it. Read-only `git diff` is on the operator's allowed list; it may refresh the index stat cache without changing content.
8. (a) at tip: `git diff --quiet HEAD -- corpus reports` gave "tracked tree clean". `python3 -B reports/round-51/boundary-count.py` gave `rows=15 resolved=15 distinct=15`; `exit=0`.
9. (a) at 35f0d49: `git archive 35f0d49 | tar -x -C $C/.runs/at-35f0d49`, then the counter: `rows=15 resolved=15 distinct=15`; `exit=0`.
10. Reference at 1f97472: `git archive 1f97472` into `.runs/at-1f97472`, then the counter: `rows=11 resolved=11 distinct=11`; `exit=0`.
11. (c) base as committed: `git archive bff83ba` into `.runs/base-bff83ba`. The counter file is absent (`counter ABSENT at base (as committed)`). Running it gave `python3: can't open file '.../reports/round-51/boundary-count.py': [Errno 2] No such file or directory`; `exit=2`.
12. (c) base plus declared counter: `git show 1f97472:reports/round-51/boundary-count.py` copied into `.runs/base-with-declared-counter`. sha256 fb1d5c89 for the counter and 16195696 for the entry. Counter: `rows=11 resolved=11 distinct=11`; `exit=0`.
13. (b) D-only: `git archive bff83ba` into `.runs/d-only`, then `git show 35f0d49:<entry>` and `git show 35f0d49:<counter>` written over it. sha256 fb1d5c89 and 5c2e09d0. `sign-language entry present in D-only tree? no`. Counter: `rows=15 resolved=15 distinct=15`; `exit=0`.
14. Lane, read-only: `sha256sum` gave fb1d5c89 for the counter. `find corpus/knowledge -name '*.md' | wc -l` gave 227. `python3 -B reports/round-51/boundary-count.py` (run in the lane) gave `rows=15 resolved=15 distinct=15`; `exit=0`. No files were written.
15. `grep` (`^(## |\|)`) on the tip entry: section 2 heading at line 27, table header at 31, separator at 32, data rows 33 to 47 (15 rows). Section headings follow at 49, 65, 79, 95, 107, 121, 133, 146, 160, 180, 186, 206 and 210. Exit n/a.
16. `git diff -U0 bff83ba 35f0d49 -- entry`: hunks `@@ -28,0 +29,2 @@`, `@@ -40 +42 @@`, `@@ -41,0 +44,4 @@` and `@@ -86,0 +93,2 @@`; `diff_exit=0`.
17. `grep -E` over the D-added lines for S-ids of S071 or higher (`S(0[7-9][0-9]|1[0-9][0-9])`), `sign-lang`, `manual-modality`, `round-51`, `lesson`: no output; grep exit 1.
18. `grep` of the tip entry for `sign-lang|manual-modality|round-51|lessons/|lesson`: one hit, line 9 (exit 0). `grep -nE 'lesson|round-5'` on base: the same line 9 (exit 0). Base S-ids of S071 or higher: 0.
19. S-ids cited, tip and base: S048 to S069 in both.
20. Top-level `.md` files in `corpus/knowledge`: sandbox 0, lane 0.
21. `read` of base section 2 (in `.runs/base-with-declared-counter`): 11 data rows at base lines 31 to 41. Row 41 is `civilizations/`. Row 40 (`sacred-kingship-mythic-charter.md:65`) keeps its anchor at tip line 42.
22. `read` of `reports/round-51/telemetry/declaration-dry-run.txt`: lines 1 to 21 (tree 5ab3634, 08:21:28Z): counter 11/11/11 exit 0; separability `SEPARABILITY_INPUT_ERROR` exit 2 (lines 17-18). Lines 23 to 43 (re-run 09:22:43Z): counter 11/11/11 exit 0; separability exit 2 (lines 39-40); `sources-census.sh validate kotodama` exit 0.
23. Strict copy: `diff` against the original counter shows lines 25 and 47 changed (exit 1). Runs: tip `rows=15 resolved=14 distinct=14`, exit 1; D-only `rows=15 resolved=14 distinct=14`, exit 1; base plus declared counter `rows=11 resolved=10 distinct=10`, exit 1.
24. Row-45 fix: `git archive main` into `.runs/fix-row45`, counter `rows=15 resolved=15 distinct=15`, `exit=0` (before edit). Edited entry line 45 in the copy to `symbolism-synthesis-method.md:69,:23`; `diff` against tip shows only line 45 changed (exit 1). Counter: `rows=15 resolved=15 distinct=15`, `exit=0`. Strict copy: `rows=15 resolved=14 distinct=14`, `exit=1`.
25. Five `read` calls on the anchored neighbour lines (listed under F9).
26. At tip: `python3 -B reports/round-51/claims-agree.py` gave `AGREE claims=['C', 'D']`; exit 0. `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json` gave `SEPARABILITY: 0 findings`; exit 0.
27. `find .../corpus/knowledge/civilizations -maxdepth 1 -name '*.md' | wc -l`: 94.
28. Lane `__pycache__` check: one directory, `reports/round-51/__pycache__`, containing `boundary-count.cpython-314.pyc` (06:28:06 -0300). Read-only `find` and `ls -ld`.
29. `_glob` of `.ufo/waves/round-51/*` and `.ufo/waves/round-51/falsify/*` (read-only): `RerunDCounter.md` did not yet exist, so there was no name clash.

Shell note: some bash outputs carried a notice that the session shell was busy and session variables were unavailable. Every command above set its own variables, so the results are unaffected.

## Source URLs opened

None. This seat makes no source claims. No URL was opened, so none is dated 2026-10-22.

## Tools and installs

None installed. Used the system `python3` (3.14.8, stdlib only) and `git`. No pacman transaction was run, and none was needed.

## Checks not run (for other seats or the L1)

- Support for the other 10 existing rows, and the prose of the whole D entry (content seats).
- C-claim checks: `reports/round-28/readme/sweep.py`, the S071 to S124 source rows, and the C entry content.
- The `sources-census.sh` validation at the fleet root (fleet-root script; not part of the D counter).
- Attempt-2 declaration bytes (not in git; see F7).

## Residual risk

- The printed count is correct, but the counter cannot see support, depth or redundancy. F1 is the decisive ambiguity: the statement and the counter disagree on row 43, and only the L1 can settle which rule governs.
- The strict copy is my reading of the statement. If the L1 keeps the declared counter as the authority, F1 becomes a wording fix only.
