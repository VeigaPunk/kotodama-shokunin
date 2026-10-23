HOLDS

# Criterion 14 — scoped falsification

Axes: **calibration** (the assigned axis). Object identity, provenance, replayability and consistency are the evidence dimensions; no other axis is scored here. This is a critique, not admission or adjudication.

Scope: newest QUALITY addition at frozen declaration commit `47f27bd0cb0bea219f21cd731c2eb0fe71f7f626`. Read-only source and committed-receipt review; no Python program, acceptance counter, selftest or judging runtime was executed by this seat. No tool installs, sandbox files or background jobs. The read-only git commands below all completed under `timeout`.

## Findings against the four requested questions

1. **Testable from committed bytes: yes, with the original key as the input.** `corpus/QUALITY.md:45` names the key, entry revision, command, retained output and distinct exit meanings. `tools/check-judged-object.py:253-266` loads the key and reads the entry from a git blob at the requested revision; `:296,321-322` compare the full SHA-256 and choose the result. No live source is required. The frozen declaration additionally commits the key commitment: `reports/round-60/planted-key.sha256:1` is `15ad8e2fae46285c85997ccdeba211e4b72a65a4a7b2de1d09e4362a59ca396a`; `claims.json:56` says the freeze precedes data and the key was built from entry build `1cd9db7c`. I did not open the current packets/key or data-seat material. Current-round closure compliance is therefore not asserted.

2. **Names a check shown able to fail: yes, not merely an input error.** `reports/round-60/telemetry/judged-object-r59.txt:2-16` records the named checker on real round-59 bytes. It prints `JUDGED_OBJECT: FAIL`, `exit=1`, 47 judged ids versus 43 landed ids, and the exact four missing ids. The wave-one review independently reports the same result at `.ufo/waves/round-60/w1-a3/ReviewJudgedToolA3.md:36-69`. These are committed observations by those authors, not reruns by me. The receipt also distinguishes a missing-key control (exit 2) from a measured mismatch.

3. **Would catch round 59's actual narrowing: yes.** The original key hash is `556ddb27c7e8066ab5b13bb4b1c1f58be118daa13651c1d030574561a10dcf19`; landed revision `d45985b2` hashes to `4e1bef48db9cbab07bb218f3b586ff2cc2e5f3b9e923f5ccb603c0afcc9e9d3d`. The receipt names `S602 S616 S623 S643` as narrowed. `corpus/lessons/round-59-verifier-spotcheck.md:93-108` independently describes the failed 47-row object, original key commitment before the review call, then seven deleted lines. The original entry need not itself exist as a committed blob for a mismatch against its previously committed digest to be measurable. The criterion also says to record that mismatch as a miss, rather than salvage the claim by deletion.

4. **No contradiction with the earlier criteria found.** Criterion 9 concerns declaration/receipt agreement; 14 adds object identity rather than replacing the receipt check. Criterion 11's requirement for a genuinely failing check is supported here by the historical mismatch receipt; it should not be confused with proving every clause of the round's acceptance predicate. Criterion 12's insistence on output for measurable rejection grounds is reinforced by retaining full output and the exit code. Criterion 13 freezes fetch treatment, whereas this identity check is offline. Claim-scoped source correction under criterion 6 remains possible under a new pre-data freeze; it does not authorize changing the already-judged object to turn its miss into a pass. Keeping corrected product while recording a missed claim is also consistent with the round-59 spot-check (`:115-117,188`).

## Strongest local counterexample, and why it does not falsify the literal criterion

The wave-one reviewer already supplies the strongest concrete counterexample to an overbroad interpretation: pair the **narrowed landed 43-row entry** with a newly constructed key whose digest is that landed entry's digest. The checker prints `JUDGED_OBJECT: PASS`, exit 0 (`ReviewJudgedToolA3.md:71-92`). This proves the command alone does not establish that its key was the key used before verdicts. It does not prove criterion 14 permits the operation: criterion 14 explicitly forbids re-keying rejected rows to make a narrowed object pass, and the round-60 declaration supplies a pre-data key commitment.

A second static limitation is equally important for calibration: `check-judged-object.py:268-294` computes id-set differences, but `:296,321-322` base the result only on digest equality. The tool also does not compare reviewer rosters. Thus a key with an inconsistent id list, or a changed reviewer roster with unchanged entry bytes, is not excluded by this checksum result alone. [INFERENCE from source; not an executed fixture.] These cases would violate the criterion's recorded-id/frozen-reviewer obligations; they are not evidence that the literal criterion allows them. Do not report the auxiliary checker as a complete mechanical verifier of all of criterion 14.

## Impact and smallest safe correction

No demonstrated regression on the assigned calibration axis. The byte-identity safeguard is real, has a historical negative control, and catches the cited incident. Rejecting all byte changes, including innocuous edits, is the explicit identity tradeoff of a frozen judged object, not a newly discovered defect.

Smallest safe clarification, if the criterion is revised later: **use the original pre-data key verified against its committed commitment, and separately verify the frozen reviewer roster; state that this command checks entry-byte identity only.** If id-set consistency is advertised as mechanically enforced, make a mismatched/missing required id set fail rather than remain diagnostic. No such change was made here. A checksum PASS with a replacement key is not sufficient closure evidence.

## Historical failure receipt (complete; evidence read, not executed here)

Source: `reports/round-60/telemetry/judged-object-r59.txt:1-22`.

```text
# R60-M1 fix shown able to fail on round 59's own bytes (2026-10-23T05:44:55Z), lane read-only
$ python3 -B tools/check-judged-object.py --key .ufo/waves/round-59/support/planted-key.json --repo . --rev d45985b2 --entry corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md
JUDGED_KEY: .ufo/waves/round-59/support/planted-key.json
JUDGED_REPO: .
JUDGED_REV: d45985b2
JUDGED_ENTRY: corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md
JUDGED_SHA256_KEY: 556ddb27c7e8066ab5b13bb4b1c1f58be118daa13651c1d030574561a10dcf19
JUDGED_SHA256_AT_REV: 4e1bef48db9cbab07bb218f3b586ff2cc2e5f3b9e923f5ccb603c0afcc9e9d3d
JUDGED_ID_SOURCE: key.seats
JUDGED_IDS_COUNT_JUDGED: 47
JUDGED_IDS_COUNT_AT_REV: 43
JUDGED_NARROWED_IDS: S602 S616 S623 S643
JUDGED_WIDENED_IDS: (none)
JUDGED_NOTE: the entry at d45985b2 is not the judged object; the judged object was changed after it was judged
JUDGED_OBJECT: FAIL
exit=1
$ python3 -B tools/check-judged-object.py --selftest
selftest ok unchanged-entry -> PASS
selftest ok one-word-changed -> FAIL
selftest ok row-line-removed -> FAIL with S602 listed
selftest ok missing-key -> exit 2
exit=0
```

## All commands executed by this seat, with complete output

The remaining evidence was obtained with file-read and targeted-search tools. No command output was trimmed. The long line in command 2 was retrieved from the tool's complete output artifact before inclusion here.

### 1. Locate the newest frozen criterion

```text
$ timeout 30s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin log -3 --format='%H %s' 47f27bd0cb0bea219f21cd731c2eb0fe71f7f626 -- corpus/QUALITY.md
47f27bd0cb0bea219f21cd731c2eb0fe71f7f626 round-60: FREEZE (claim D, before any data seat) — freeze_note; packet-key hash (key built from the 1cd9db7c entry, kept outside the lane until the support wave settles); revision-9 residual re-score receipts (NONE-MET); records: SCORECARD and LOG round-59 corrections, round-59 errata, QUALITY criterion 14, round-60 lesson (pre-data parts)
7d19bd1f534d7f68b3cb94ac68d879cc87219493 round-59: records — lesson (intake, Gate S600-S647, errata, R59-M1..M5), QUALITY criterion 13, SCORECARD, LOG, final measures, build wave reports
e27c8a67a6adadecdfda84a56f5e0da2fbed5b9c round-58: records — lesson, QUALITY criterion 12, superseding/registered rows S564-S576, heraldry :41 re-sourced to S575
```

### 2. Read the exact criterion addition at freeze

```text
$ timeout 30s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show --format=fuller --no-ext-diff --no-renames 47f27bd0cb0bea219f21cd731c2eb0fe71f7f626 -- corpus/QUALITY.md
commit 47f27bd0cb0bea219f21cd731c2eb0fe71f7f626
Author:     kotodama-shokunin <kotodama@shokunin.local>
AuthorDate: Fri Oct 23 04:42:11 2026 -0300
Commit:     kotodama-shokunin <kotodama@shokunin.local>
CommitDate: Fri Oct 23 04:50:34 2026 -0300

    round-60: FREEZE (claim D, before any data seat) — freeze_note; packet-key hash (key built from the 1cd9db7c entry, kept outside the lane until the support wave settles); revision-9 residual re-score receipts (NONE-MET); records: SCORECARD and LOG round-59 corrections, round-59 errata, QUALITY criterion 14, round-60 lesson (pre-data parts)

diff --git a/corpus/QUALITY.md b/corpus/QUALITY.md
index 96b5be6..4e408c9 100644
--- a/corpus/QUALITY.md
+++ b/corpus/QUALITY.md
@@ -41,3 +41,5 @@ support for an admitted claim.
 12. **Re-test stated rejection grounds** — a reject or not-registered reason that names a tool, gives a measurable result (a word count, a locator failure, an HTTP error) or asserts a source property a tool can check names the re-test tool and carries its verbatim output in the lesson's Gate line. Without that output the reason is unverified and cannot justify the decision. Grounded in the round-56 koon1244 reason ("no quotable passage", contradicted by quotable JSON fields) and the round-57 CODH reason ("below the 8-word minimum", contradicted by four quotes that each locate) (`corpus/lessons/round-57-verifier-spotcheck.md` §3 and §5 item 1); drafted by seat ScribeQualityC12 (`.ufo/waves/round-58/build/ScribeQualityC12.md`).
 
 13. **Unreachable live sources are handled before data** — a predicate with a live-fetch leg declares before data how an unreachable page is treated: list an archived capture of that same page in the row, or define a bounded allowance for that fetch class with its own control; the treatment is frozen and never relaxed after data. Grounded in `corpus/lessons/round-58-verifier-spotcheck.md` §5 item 5 (S510/S511 returned HTTP 403 and the no-slack predicate failed on those fetches); round 59's FETCH-59 (`reports/round-59/rowcheck.py`) is the first application. Drafted by seat ScribeErrataQuality59.
+
+14. **The judged object stays frozen through adjudication** — when blind packets are built, the packet key records the exact entry-byte sha256 and the judged id set; at closure, compare that key with the entry at the measured revision with `python3 -B tools/check-judged-object.py --key <packet-key.json> --repo <repo> --rev <measured revision>` and keep its full output and exit code (exit 1 is a measured mismatch, exit 2 an input error). If the bytes differ, record a miss; never delete, reword, re-key or re-score rejected rows so that a narrowed object passes, and never drop or add a reviewer after the verdicts. Shown able to fail: it prints `JUDGED_OBJECT: FAIL` on round 59's own bytes (`reports/round-60/telemetry/judged-object-r59.txt`; re-run by ReviewJudgedToolA3, `.ufo/waves/round-60/w1-a3/ReviewJudgedToolA3.md`). Grounded in the round-59 post-verdict narrowing (`corpus/lessons/round-59-verifier-spotcheck.md` §2 and §5 item 1); drafted by seat ScribeRecordsA3.
```

### 3. Locate committed checker and receipt provenance

```text
$ timeout 30s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin log -2 --format='%H %s' 47f27bd0cb0bea219f21cd731c2eb0fe71f7f626 -- tools/check-judged-object.py reports/round-60/telemetry/judged-object-r59.txt .ufo/waves/round-60/w1-a3/ReviewJudgedToolA3.md
b9faed93ea70c6ba136ce802ef45952b26283106 round-60: revisions 6-7 (attempt 3, before any data seat) — exact 24-seat roster and dissent scan over every frozen seat (CtlNarrowA3); CONFINED false voids fixed (dry runs); EVIDENCE: SUPPORTED counts only with >=10 words of the pinned page text not in the packet (CtlKeyedLabelA3); 47 pinned page texts; wave-1 pre-data control receipts and build audits (scored at 14e64138)
f39e5ea28401051ad791ea334315ddbd0b683ef2 round-60: revision 4 (pre-data, from control-wave receipts at 35de1f9c) — fetch-like calls only; new line carries its quote; no copied rejected teaches; LINES ignores id-only edits; 24 support seats x3; tools/check-judged-object.py (R60-M1 fix) with its round-59 FAIL receipt
```

Tool metadata accompanying command 3 (not git stdout):

```text
Ran in a temporary shell while the session shell is busy with another command: session variables and functions were unavailable, and nothing set here persists.
```

### 4. Establish that the read working files equal their frozen committed versions

```text
$ timeout 30s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin diff --exit-code --no-ext-diff 47f27bd0cb0bea219f21cd731c2eb0fe71f7f626 -- corpus/QUALITY.md tools/check-judged-object.py reports/round-60/telemetry/judged-object-r59.txt .ufo/waves/round-60/w1-a3/ReviewJudgedToolA3.md corpus/lessons/round-59-verifier-spotcheck.md reports/round-60/planted-key.sha256 reports/round-60/claims.json
```

Output: none (the tool returned `(no output)`).
