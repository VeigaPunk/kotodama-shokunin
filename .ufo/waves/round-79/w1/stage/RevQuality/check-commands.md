# Concrete check/fixture commands — round 79 O and Ca (seat RevQuality)

All commands are read-only against committed bytes; run from the lane root or with `-C`.
Scratch for any materialized clone: /fast/scratch/hyaku/kotodama-r79/<seat> only.

## 1. Re-derive Ca's filed mismatch=1 (QUALITY 29; run, output in probe-receipt-registry-mismatch.txt)

```
git show 44f76d456c1b326a71ffdb381590af825cbf11be:reports/round-78/telemetry/census-end.txt \
| grep -E '^kotodama W01 S[0-9]+ tierC mined used-by=' > /tmp/r79-receipt-w01.txt
git show 44f76d456c1b326a71ffdb381590af825cbf11be:corpus/SOURCES.md \
| awk -F'|' '/^\| S[0-9]+ /{gsub(/ /,"",$2); gsub(/ /,"",$12); print $2" "$12}' > /tmp/r79-registry-usedby.txt
# expect exactly one W01 token that differs from the registry cell:
#   S884  receipt=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md
#         registry=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
```

(The seat probe count-mismatch.py in this stage does both revisions; raw output preserved.)

## 2. Bind the original receipt digest for the correction (QUALITY 17/29)

```
git rev-parse 44f76d45:reports/round-78/telemetry/census-end.txt
# 62eb55b77f44bf47c283c98c5645dd7141e98495   (same blob at 4b255745 — unchanged by the spot-check commit)
git show 44f76d45:reports/round-78/telemetry/census-end.txt | sha256sum
# 05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867
```

## 3. Append-only / changed-receipt control (QUALITY 25 J6; the "changed receipt must fail" clause)

```
git diff --numstat 44f76d456c1b326a71ffdb381590af825cbf11be..<lands> -- \
  reports/round-78/telemetry/census-end.txt reports/round-78/telemetry/census-start.txt
# expected: empty (zero removed, zero added). Any line change fails APPENDONLY.
```

## 4. Counter shape one-liners (criteria 25/26, unchanged from the criteria)

```
# 25-shape: --freeze present, git show <rev>:<path> present, no graded-root claims.json join
sh -c 'grep -q -- --freeze "$1" && grep -qE "\"show\", *\"%s:%s\"" "$1" && ! grep -qE "os\.path\.join\((mat|root|clone|treework)[^)]*CLAIMS" "$1"' _ reports/round-79/accept-ca.py
sh -c 'grep -q -- --freeze "$1" && grep -qE "\"show\", *\"%s:%s\"" "$1" && ! grep -qE "os\.path\.join\((mat|root|clone|treework)[^)]*CLAIMS" "$1"' _ reports/round-79/accept-o.py

# 28-shape: no repository tool executed from a graded materialization without a 64-hex pin
sh -c 'comm -23 <(grep -oE "os\.path\.join\((mat|root|clone|treework)[^)]*\"" "$1" | grep -oE "\"[^\"]+\"" | tr -d "\"" | grep -E "\.(py|sh)$" | sort -u) <(grep -oE "\"[^\"]+\": *\"[0-9a-f]{64}\"" "$1" | sed "s/\": *\".*//" | tr -d "\"" | sort -u)' _ reports/round-79/accept-o.py
# must print nothing — accept-o must pin tools/ledger-token-guard.py per criterion 28.
```

## 5. Selftest receipts (criterion 23 + round-75 addendum)

```
head -2 reports/round-79/telemetry/selftest-ca.txt | grep -q 'clean -> exit=0'
head -2 reports/round-79/telemetry/selftest-o.txt  | grep -q 'clean -> exit=0'
# and both counters run at the FREEZE commit (receipts present, landing absent), exit != 0.
```

## 6. Do-nothing / junk receipt legs (criteria 25b, 11; draft kill rules)

Expected red legs, to be asserted by the committed junk receipts:
- Ca do-nothing (lands == base 44f76d45): correction absent → the correction leg red;
  mismatch re-derivation still 1.
- Ca lying correction: row whose old/actual tokens ≠ the measured strings in §1–§2 → ANNOTATE-class red.
- Ca wrong revision: row naming a revision whose bytes do not carry the stated tokens → red.
- Ca changed receipt (§3) → APPENDONLY red.
- Ca correction citing O's guard fixtures or S897 → SEPARABLE red.
- O constant-printer observe_cmd (J4/J4b) → guard refusal leg red.
- O observed_at_base ≠ re-run actual → red (R78-M1's exact class; corpus/lessons/round-78.md R78-M1).
- O stated_token == actual observation → red (the do-nothing pair class).

## 7. Guard fixture bounds the draft names (O clauses)

- immutable base read-only grammar: no shells/interpreters/worktree reads in observe argv
  (allowlist in the lineage: git, grep, wc, sha256sum, ls, cat, head, tail, cut — round-77
  ExecAdaptCa accept-ca.py LEDGER leg is the existing implementation to mirror);
- exact observed token validation; stated==actual rejection;
- clean/error exit 0/1/2 with stable labels;
- timeout + output caps on every observation; explicit --work scratch.
