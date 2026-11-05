# ExecAdjacency94 — Claim A (adjacency), round 94 w1

## Status
Repoint edits done in a scratch clone at base e7fa8eaf. The frozen A1 counter still prints 2 dangling after the repoint. Cause: the frozen counter filters out any link target whose path contains "greet" (predispatch.py line 33: `targets = [t for t in LINK.findall(text) if "greet" not in t]`), so the correct target `linguistics/greeting-leave-taking-formulae.md` can never count. I did not edit the counter. A scratch-only diagnostic copy with that filter removed prints `A1 dangling-greeting-pointers 0`. L1 decision needed on the counter. Adjacency edits are complete; the gate is not met.

## Clone and base verification
- `git clone --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin <scratch>/work && git checkout --detach e7fa8eafb7c5d9edd706f860cfc023e6c99b1ab2`
- `git -C <work> rev-parse HEAD` → `e7fa8eafb7c5d9edd706f860cfc023e6c99b1ab2`; `rev-parse --show-toplevel` → the scratch work dir.

## A1 before and after
Command: `python3 -B <scratch>/predispatch.py --root <work>` (copy of reports/round-94/predispatch.py), rc=0.
- Before: `A1 dangling-greeting-pointers 2 :: corpus/knowledge/culture-material/adornment-body-codes.md:5 corpus/knowledge/culture-material/costume-semiotics.md:143`
- After (same command): `A1 dangling-greeting-pointers 2 :: corpus/knowledge/culture-material/adornment-body-codes.md:5 corpus/knowledge/culture-material/costume-semiotics.md:143`
- After, diagnostic copy (`sed` removed only the `if "greet" not in t` filter, scratch-only): `A1 dangling-greeting-pointers 0 ::`

Full after-run output (rc=0) is in `stage/ExecAdjacency94/predispatch-after-full.txt`. The other lines (C1 entry-present 0, C2 888 / S964, O0 sha 9799a96c…, CENSUS rc=0, INDEX rc=0) are unchanged from base.

## Changed lines (one per file)
- adornment-body-codes.md:5 (couples). Before: `linguistics/politeness-taboo-euphemism.md (greeting formulae, touch taboos, "paint" as moral slur)`. After: `linguistics/politeness-taboo-euphemism.md (touch taboos, "paint" as moral slur); linguistics/greeting-leave-taking-formulae.md (greeting formulae)`. The touch-taboo and paint-slur claims stay with their owner. Only the greeting claim moves to the greeting file. This is a split, not a drop. Judgment call: the greeting target is a new couple target on this line. Revert the split if the L1 prefers a strict single-path swap.
- costume-semiotics.md:143. Before: `- → linguistics/linguistic-anthropology.md: dress as communicative practice alongside greeting formulae and address systems.` After: `- → linguistics/linguistic-anthropology.md: dress as communicative practice alongside address systems; → linguistics/greeting-leave-taking-formulae.md: dress as communicative practice alongside greeting formulae.`

## Scope and patch
- `git -C <work> diff --numstat`: `1 1 corpus/knowledge/culture-material/adornment-body-codes.md` and `1 1 corpus/knowledge/culture-material/costume-semiotics.md`. Two files, two changed lines.
- Patch: `stage/ExecAdjacency94/adjacency.patch`, 2 `diff --git` headers (`grep -c '^diff --git'`), 2 hunks (`grep -c '^@@'`).
- Patch sha256: `3719edcf5d0d02486e21e015de073c1a2e53d79dac6eda7e071505460d6ced49` (`sha256sum`). Written to `stage/ExecAdjacency94/DONE`.
- `stage/ExecAdjacency94/before-after.txt` holds the A1 before/after, numstat, and changed lines.
- Not measured: no other gates were run (per assignment, the main agent runs gates).

## Recommendation for L1
Either (a) amend the frozen counter's line 33 to stop excluding greet-named targets (counter defect: it rejects the one target the A1 pointer is supposed to use), or (b) accept the repoint on the editorial merits and record A1 as 2 with this cause. I did not do either; the counter and claims.json are frozen for seats.

## Tooling
None installed. No pacman, sysctl, or host changes.

## Scratch
Scratch dir `/fast/scratch/hyaku/kotodama-r94/ExecAdjacency94/` removed at the end of the run (trap set).
