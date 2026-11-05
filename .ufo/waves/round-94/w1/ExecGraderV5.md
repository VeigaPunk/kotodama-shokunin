# ExecGraderV5 — round 94 wave 1 (grader v5 candidate), 2026-11-05

Result: grader v5 candidate produced from a detached clone at e7fa8eafb7c5d9edd706f860cfc023e6c99b1ab2
(HEAD verified before editing). Only `tools/check-advance-evidence.py` in the clone was edited; the lane
repo, corpus, reports and frozen files untouched; no git/jj mutations anywhere.

## Deliverables (stage dir)

- `.ufo/waves/round-94/w1/stage/ExecGraderV5/check-advance-evidence.py` — candidate, sha256
  `7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff` (v4 base
  `9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7` verified in-clone before editing).
- `selftest.txt` — full selftest output; `diff.txt` — unified diff vs base v4;
  `changes.md` — per-class ledger with line numbers, diagnostics, test names; `DONE` — candidate sha.

## N and stability

- Selftest: `python3 -B <clone>/tools/check-advance-evidence.py --selftest --work <scratch>/st` →
  `SELFTEST PASS 126/126`, rc 0, exactly 126 `  ok ` lines, 0 `  BAD` (114 base checks kept + 12 new:
  A1, B1, G1, H1, I1, J1, K1, script-strip, comment-strip, unescape, dispo-any-casei, baserows-drop-cell8).
- Stability: 4 concurrent runs on separate `--work` dirs → 4× `SELFTEST PASS 126/126` rc 0, outputs
  byte-identical (md5 unique count 1).

## Diffstat and class summary

- diffstat: 1 file changed, 163 insertions(+), 9 deletions(-) in `tools/check-advance-evidence.py`.
- A1 `VERDICT-NONASCII` rc 2; B1 `VERDICT-SOFTHYPHEN` rc 2; G1 span-surface rule (number stripped for
  span, hits rule frozen) `LEG TOPIC FAIL` rc 1; H1 `MANIFEST-ROW-TYPE` rc 2 (entry + advance);
  I1 `LEG NEWIDS/BASEROWS FAIL` `registry row has N cells < 11` rc 1; J1 dash folding → correct-direction
  flip `LEG APPENDONLY FAIL` rc 1, v4 false flip text gone; K1 `VERDICT-LOWERCASE` rc 2 (anchored
  lowercase untouched). Details: stage `changes.md`.

## Mutation kills (each mutant applied to a scratch copy, selftest run)

- script-strip-off → FAIL 125/126 rc 1; comment-strip-off → FAIL 125/126 rc 1 (pin uses a comment with
  an inner `>` so the tag stripper cannot cover); unescape-off → FAIL 125/126 rc 1; dispo-any-casei →
  FAIL 124/126 rc 1; baserows-drop-cell8 → FAIL 125/126 rc 1. killed 5/5, survived 0.
- The five mutation-target source lines are byte-identical to v4, so textual mutant patterns still apply.

## Regression (frozen battery93 grade set, run in scratch)

- v4 (git archive of e7fa8eaf) vs v5: all 26 cases identical rc and named outcome
  (`G0 rc=0 CLEAN`, `A5a rc=0 CLEAN`, `A6g rc=2 refused-unnamed` with its frozen message, `A4a/A4b
  refused on TOPIC`); per-case diff empty. Commands: `R93_ROOT=<v4tree|v5clone> R93_WORK=<scratch>
  python3 -B <tree>/reports/round-93/battery93.py`.
- Positive controls: `positive advance` rc 0, `positive entry` rc 0, direct G0-style fixture
  rc 0 `ENTRY-EVIDENCE: PASS legs=9/9`.
- Per-class receipts (CriticClaims93 recipe inputs through the CLI): A1/B1/J1/K1 rc 2 named tokens,
  G1/H1-leg/I1/J1 rc 1 named legs, control rc 0 — captured in this seat's scratch log before deletion.

## Behavior notes and risks

- A1/B1/J1/K1 refuse via the frozen `Refused` path: rc 2, stderr `ADVANCE-EVIDENCE_ERROR: ...`,
  no traceback; G1/I1/J1 stay named-leg rc 1 refusals. H1 is additionally guarded in advance mode and
  I1 in BASEROWS (outside the CriticClaims recipes; battery93 verified unaffected).
- K1 changes v4's "lowercase prose stays clean" for UNANCHORED id+located lesson lines only (now rc 2
  refusal); battery93 A5a/A5b/A5c (line-start anchored) verified unchanged. Real-lane lessons with
  mid-sentence `S<id> ... located` prose would now refuse — this is the routed intent (claims O).
- Tooling record: no installs or upgrades performed (none needed); no pacman transactions (guard active);
  no sysctl changes; disk-guard status checked once (/fast/scratch 49% use). Scratch
  `/fast/scratch/hyaku/kotodama-r94/ExecGraderV5` (clone, mutants, batteries, receipts) deleted after
  this report.
