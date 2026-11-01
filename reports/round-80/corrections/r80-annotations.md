# Round-80 append-only annotations — three wording defects in filed round-79 bytes

Routed by the round-79 non-author verifier spot-check (`corpus/lessons/round-79-verifier-spotcheck.md` §6 item 4): "Minor annotation defects (fix next time the files are touched; do not rewrite filed bytes)." None of the three filed artifacts is rewritten; this record and the `## Corrections — round 80` section appended to `corpus/lessons/round-79.md` are the fix. Each defect is bound below to the filed blob and a re-runnable verification.

## (a) `reports/round-79/claims.json` claim O `before` — "is empty" misstatement

- Filed bytes: blob `d6a75532fd2c5363ecf41fdafc9d15d393c2c171` (unchanged at HEAD, `git ls-tree HEAD -- reports/round-79/claims.json`), the frozen round-79 config; never edited.
- Defect: claim O `before` says "`git ls-tree 44f76d4 tools/` is empty". The directory has 27 entries at that commit; only the guard path is absent.
- Verification:
  - `git ls-tree 44f76d456c1b326a71ffdb381590af825cbf11be tools/ | wc -l` → 27
  - `git cat-file -e 44f76d456c1b326a71ffdb381590af825cbf11be:tools/ledger-token-guard.py` → rc 128 (`fatal: path 'tools/ledger-token-guard.py' exists on disk, but not in '44f76d45...'` — the worktree file is the round-80 revision; at the named commit the path does not exist)
  - `git show HEAD:reports/round-79/claims.json | grep -o "git ls-tree 44f76d4 tools/ is empty"` → the string is present, so the filed defect is real and stays as filed.
- Correction: read the claim's `before` as "no `tools/ledger-token-guard.py` at base" (as the SCORECARD round-79 row already words it); the parenthetical's "is empty" is false of the directory and true only of the guard path.

## (b) `corpus/lessons/round-79.md` Gate — the "(20 words)" miscount

- Filed bytes: the quote spans lesson lines 49–50 at HEAD; the "(20 words)" annotation is on line 50.
- Defect: whitespace-split count of the located quote is 16, not 20 (≤ 25 either way, so the Gate's rule held; the annotation number is wrong).
- Verification: `git show HEAD:corpus/lessons/round-79.md | sed -n '49,50p' | tr '\n' ' ' | grep -oE 'This guard.*observe. object' | wc -w` → 16.
- Correction: the S897 located quote is 16 words by whitespace split.

## (c) SOURCES row S897 anchor command — `python3 -B` is the old host's spelling

- Filed bytes: the S897 row at `corpus/SOURCES.md` (line 852 at HEAD) anchors the command `python3 -B tools/ledger-token-guard.py --selftest --work <scratch>`.
- Defect: this Windows host has no working `python3` alias (the Store stub answers "Python was not found"); the working spelling is `python -B`, which is what the round-79 run-14 receipts and report already use.
- Verification: `git show HEAD:corpus/SOURCES.md | grep -o "python3 -B tools/ledger-token-guard.py --selftest"` → present; `python --version` → Python 3.13.15; `python3 --version` → the Store stub message.
- Disposition: no superseding row is filed. The row's tier, teaches and anchor quote are unaffected; only the interpreter spelling is host-dated, the round-79 report's host note already covers it, and the registry's append-only rule reserves in-place cell changes for `status`/`recheck`/`used-by`. A superseding row would spend a registry id to restate the same source. Future rows opened on this host spell the command `python -B` (see S898–S900 anchor records, which carry no command).
