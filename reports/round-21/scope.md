# Round 21 — Scope watch (SCRIBE X02)

- **Axes:** scope integrity (protected surface unchanged); province fidelity (live lane still matches its declared boundaries); evidence limits (distinguish verified bytes from ignored or unobservable state).
- **Assignment:** fleet root clean; filed rounds 8–20 untouched; `PROVINCE.md` accurate.
- **Date:** 2026-10-18, from `date -I` in the observation commands below.
- **Role limits:** read-only scope audit. This seat wrote only this report, did not run a historical validator, did not edit or repair filed artifacts, and made no commit or push.

## Verdict

**PASS for the tracked filed surface and lane-local province checks; fleet root clean.** The round-21 declared baseline is `35b6797b42d48bec52e1e3ddba1f3afc9bb85046`, and the observed lane HEAD is `8115eaaeb57c9dce157fe291337cb52dd914c6cf`; `git merge-base --is-ancestor` returned yes (all three observations from commands run 2026-10-18). The change from baseline to HEAD is limited to the new round-21 declaration files `reports/round-21/claims.json` and `reports/round-21/targets.json`; the protected filed surface has no tracked diff.

The lane and fleet-root status checks each returned only their branch/upstream header and no changed or untracked file rows (commands run 2026-10-18). Branches being ahead of their upstreams is not worktree dirt. The fleet-root check was read-only.

## Filed-round integrity

For the filed surface `reports/round-{8..20}`:

- `git diff --name-status 35b6797b42d48bec52e1e3ddba1f3afc9bb85046 HEAD -- reports/round-{8..20}` returned empty, and the same baseline-to-worktree diff returned empty (both commands run 2026-10-18).
- `git status --porcelain=v1 --untracked-files=all -- reports/round-{8..20}` returned empty (command run 2026-10-18).
- `git ls-files reports/round-{8..20} | wc -l` returned **973 tracked paths** (command run 2026-10-18).

**Verification boundary:** `git ls-files --others --ignored --exclude-standard reports/round-{8..20}` listed **17 ignored paths** on 2026-10-18: Python bytecode caches and run logs. They have no Git baseline and are excluded from the tracked-byte comparison; this audit does not claim their byte identity. No historical validator was run by this seat. The round-20 scope record (`reports/round-20/scope.md`, read 2026-10-18) also documents a prior transient rewrite/restoration involving the round-9 receipt; the current clean comparison verifies its present tracked bytes against the declared baseline, not the absence of that historical event.

## Province fidelity

- `PROVINCE.md` is unchanged between the declared baseline and HEAD (`git diff --name-status 35b6797b42d48bec52e1e3ddba1f3afc9bb85046 HEAD -- PROVINCE.md`, run 2026-10-18). Its current SHA-256 is `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` (`sha256sum PROVINCE.md`, run 2026-10-18), matching the prior round-20 scope/adjacency records read for this audit.
- `ls -1 corpus/knowledge` returned the six declared owned partitions—`civilizations`, `culture-material`, `linguistics`, `myth-symbol`, `synthesis`, and `verification`—on 2026-10-18. The adjacent `corpus/knowledge/synthesis/worldbible-integration-contract.md` exists (`test -f`, 2026-10-18); its SHA-256 is `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` (`sha256sum`, 2026-10-18), unchanged between baseline and HEAD.
- The contract identifies lore as owner of canon and the world bible, reserves general research method to chousa, and restricts each lane to its own authorized surfaces (`corpus/knowledge/synthesis/worldbible-integration-contract.md`, §§1 and 3, read 2026-10-18). Round-20 scope and adjacency records reviewed here place that round's work under the existing owned-tools/gates, non-canon examples, and reports clauses; no province expansion or contradictory local scope was found.

This is a lane-local structural and documentary check, not a certification of canon, rights, source truth, or sibling-repository behavior. In particular, this seat cannot prove the negative that no out-of-lane write ever occurred; contested or out-of-province work remains routed, never absorbed.

## Commands and evidence date

All commands below were run on 2026-10-18; `export TMPDIR=$PWD/.scratch` was set before the command batches. No scratch files were written.

- `git status --short --branch --untracked-files=all`
- `git -C /home/vgpnk/Projects/shokunin status --short --branch --untracked-files=all`
- `git rev-parse HEAD`; `git rev-parse 35b6797b42d48bec52e1e3ddba1f3afc9bb85046`; `git merge-base --is-ancestor 35b6797b42d48bec52e1e3ddba1f3afc9bb85046 HEAD`
- `git diff --name-status 35b6797b42d48bec52e1e3ddba1f3afc9bb85046 HEAD -- reports/round-{8..20}`
- `git diff --name-status 35b6797b42d48bec52e1e3ddba1f3afc9bb85046 -- reports/round-{8..20}`
- `git status --porcelain=v1 --untracked-files=all -- reports/round-{8..20}`; `git ls-files reports/round-{8..20} | wc -l`; `git ls-files --others --ignored --exclude-standard reports/round-{8..20}`
- `git diff --name-status 35b6797b42d48bec52e1e3ddba1f3afc9bb85046 HEAD -- PROVINCE.md corpus/knowledge/synthesis/worldbible-integration-contract.md`; `sha256sum PROVINCE.md corpus/knowledge/synthesis/worldbible-integration-contract.md`
- `ls -1 corpus/knowledge`; `test -f corpus/knowledge/synthesis/worldbible-integration-contract.md`

## Compliance

Only `reports/round-21/scope.md` was written by this seat. Filed rounds 8–20 were not written; no validator was executed; no sibling or fleet file was changed; no commit or push was made. Historical transient findings are preserved as findings, not silently patched.
