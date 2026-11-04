# ScoutSurface read-only receipts

Axes: operability, historical attribution accuracy, boundedness. No executable checker, battery, selftest, build, lint, or formatter was run.

1. `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin cat-file -e 83846a22ee1e9da7aa52ac505ccebf4455169247:tools/check-attestation-packet.py`
   Observed exit 128; stderr: `fatal: path 'tools/check-attestation-packet.py' does not exist in '83846a22ee1e9da7aa52ac505ccebf4455169247'`.
2. Opened immutable bodies with `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 2a3b5643899c3520867ae930593cafef6ef19cad:reports/round-87/claims.json` and same revision `:reports/round-87/measure87.py`; both returned bodies successfully. No measurement was executed.
3. Opened immutable inherited checker with `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 83846a22ee1e9da7aa52ac505ccebf4455169247:.ufo/waves/round-86/w1/stage/ExecCraftLedger/check-craft.py`; returned full body. Compared against read-tool numbered working body (192 lines); observed relevant definitions and branches identical in the displayed bodies.
4. Glob, hidden included and gitignore disabled: lane `**/considerthese*` and `**/ConsiderThese*` returned no files. Fleet direct-child `*considerthese*` returned none and explicit fleet `considerthese/**` reported missing. This is scoped filesystem-pattern absence, not global tool/package absence.
5. Lane structure walk found `tools/check-cited-records.py`, many existing specialized checkers, and r86 `ExecCraftLedger/check-craft.py`. Targeted source search found r87 frozen `measure87.py` constants PACKET and TOOL and claims CLI references. At observation time glob found no production `tools/*attestation*` and no stage `ExecAuditor/*`; stage directories observed included ExecDomainTrial, ReviewerAuditor, ExecControls, ConnectorScope, ScoutSurface, CriticCounter. Concurrent staging may change.
6. `read xd://lsp` returned `No such tool: xd://lsp`. No semantic server device was available; source matching is literal fallback, not semantic-reference proof.

No installs/updates, source registry additions, external adoptions, Git mutations, or production writes. No external shokuknow menu was needed.
