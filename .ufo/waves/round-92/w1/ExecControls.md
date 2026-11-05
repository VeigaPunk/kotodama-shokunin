# ExecControls: frozen-counter controls at 066b9728fc64e78735769c4740d05c1000d31a3b

Judged on: operability. Milestone: r92-v1.
Stage: .ufo/waves/round-92/w1/stage/ExecControls/ (controls-summary.txt, receipts, stderr/stdout captures).

## Measured (rc and leg names)

| # | Command (claim, lands, freeze) | rc | Result |
|---|---|---|---|
| 1 | O, lands=freeze | 0 | PASS legs=8/8. Brief expected rc 1 with TOOL and MUTATION failing: did not occur. |
| 2 | C, lands=freeze | 1 | FAIL legs=2/4 failed=ENTRY,APPENDONLY. ENTRY failed as expected; APPENDONLY also failed (0 qualifying new ids, entry absent from README). |
| 3 | O, lands=base 21350361 | 2 | Refused: "--lands equals the frozen base; a do-nothing landing cannot pass". As expected. |
| 4 | C, lands=freeze, run twice | 1, 1 | Same work dir: receipts byte-identical (cmp). Different work dirs: differ only in the `observed=` work-dir path on line 7. |
| 5 | C, lands=freeze, freeze=base | 2 | Refused, but not for "not an ancestor": base is an ancestor of the freeze; the refusal is the claims.json read at base. |
| 6 (extra) | C, lands=freeze, freeze=lane main 66b3ae93 | 2 | Refused: "--freeze 66b3ae93fe44 is not an ancestor of --lands 066b9728fc64". This is the true ancestor refusal. |

Full commands, receipts and sha256 values: stage controls-summary.txt.

## Findings

1. **O's do-nothing control is not a null at the freeze.** The freeze already contains the pinned v3 tool (`tools/check-advance-evidence.py` sha 905be2fe…, equal to `O.tool_sha256`), the 60-mutant receipt, and the pinned mutants.py. At lands = freeze, O passes all 8 legs. A landing that adds nothing beyond the freeze would pass O. The claim text says the TOOL leg fails at base; I confirmed base tool sha 88597a66… (`git show 21350361…:tools/check-advance-evidence.py | sha256sum`), so the failure is real at base, but the counter cannot grade base (refused by design). Route to L1: the O claim's control cannot discriminate freeze from lands. Not changed by me; frozen files are read-only for this seat.
2. C's do-nothing control fails as intended: ENTRY absent (`git cat-file -e 066b97…:corpus/knowledge/linguistics/ideophones-mimetics.md` → no). APPENDONLY also fails, which the brief did not predict.
3. The C freeze-not-ancestor control with freeze=base does not exercise the ancestor check. Use a non-ancestor freeze (case 6) to exercise it.
4. Determinism: C receipts are byte-identical across runs in the same work dir. Receipts embed the work-dir path, so they are not portable across work dirs. The receipt also embeds lane main at run time (66b3ae93…).

## Could not measure

- O at base: the counter refuses lands = base by design, so the O TOOL/MUTATION failure at base is established only by the base tool sha, not by a counter receipt.

## Tooling

No installs. Used python3 3.14.8 (existing), git read-only, sha256sum, cmp, diff, cp.

## Cleanup

Scratch /fast/scratch/hyaku/kotodama-r92/ExecControls removed after the receipts were copied to stage. No writes to production files, no git mutations, no sysctl changes, no subagents.
