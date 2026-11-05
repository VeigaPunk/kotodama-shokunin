# MutationTester95 — round-95 independent mutation re-run of the v6 candidate

Seat: MutationTester95 (leaf, no subagents). Stage: `.ufo/waves/round-95/w1/stage/MutationTester95/`.
Scratch used and deleted: `/fast/scratch/hyaku/kotodama-r95/MutationTester95/`.

## Result

`MUTATION-INDEPENDENT: MATCH`

- My independent full run over the 95-mutant manifest: `MUTATION-SCORE: 95/95 killed, 0 survived, 0 broken-pattern`, driver rc=0, on the v6 candidate sha256 `f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec` (CLEAN-FIRST selftest rc=0, `SELFTEST PASS 134/134`).
- Per-mutant lines: byte-for-byte identical to `../ExecMutants95/stage/mutation-score.txt` — all 95 graded `MUTANT`-body lines, the graded `MUTATION-SCORE` trailer, all 95 stub-control lines and the stub `MUTATION-SCORE: 0/95 killed, 0 survived, 95 broken-pattern` (197/197 behavioral lines, 0 divergences; `scratch/diff-verdict.txt` in my scratch recorded it before deletion, the same evidence is reconstructible by `diff` of the two stage files).
- The only full-file deltas are the two `COMMAND:` lines (each seat's own stage/scratch paths) and the stub-control `TOOL sha256=` line (my stub bytes `e3436a40…` vs theirs `7023cc1d…`; both stubs score identically). Recorded as data; not behavioral divergence.

## Inputs and provenance (sha256, command, rc)

- `mutants95.py` copied from `../ExecMutants95/stage/`, sha256 `ff450980dec9e79b3315db276a985ac97df0f950964d751e4416b44c9f3ecf96` == `../ExecMutants95/DONE` (verified with `sha256sum`, rc 0).
- `v6-candidate.py` copied from `../ExecGraderV6/stage/`, sha256 `f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec` == `../ExecGraderV6/DONE`, and != v5 `7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff` (O0 holds). Observation recorded: ExecGraderV6's stage carried v5-sha bytes named `v6-candidate.py` before its DONE (15:15Z state); I used only the DONE-stamped bytes.
- Full run: `python3 -B mutants95.py --tool v6-candidate.py --work /fast/scratch/hyaku/kotodama-r95/MutationTester95/run` from my stage dir; driver rc=0; receipt `run/mutation95-score.txt` (98 lines: TOOL sha, CLEAN-FIRST, 95 mutant lines, MUTATION-SCORE).
- Stub control: independent stub tool (`print("SELFTEST PASS 134/134")`), `python3 -B mutants95.py --tool stub-tool.py --work run-stub`; rc=1, all 95 BROKEN-PATTERN matches=0, `MUTATION-SCORE: 0/95 killed, 0 survived, 95 broken-pattern` — the driver cannot score kills off the tool's own patterns.

## Hand probes (manifest unamended; fresh copies; kill direction = mutant selftest rc != 0)

1. head-qualify-off by hand: `return len(h.lstrip('#').split()) >= 2` → `return True` (12-space indent, count=1, exactly-once as the manifest requires). Mutant selftest rc=1, `SELFTEST FAIL 133/134` — the new head-qualify pin (`single-token headings anchor no phrase (head-qualify pin)`) fires. KILLED.
2. cd1-refusal-off (my own second probe, not the manifest's `combining-refuse-off`): both `raise Refused(f'line {n}: verdict token carries a combining mark (VERDICT-COMBINE)')` sites → `pass` (count=2, replace-all). Mutant selftest rc=1, `SELFTEST FAIL 133/134` — the `round-95 CD1` pin fires. KILLED. (The manifest's own narrower `combining-refuse-off` — NFKD-recovery branch only — also killed in my full run, matches=1.)
3. Clean candidate selftest: rc=0, `SELFTEST PASS 134/134` (>= floor 134), matching `../ExecGraderV6/selftest.txt` head and my CLEAN-FIRST receipt.

## Kill highlights relevant to claim O3

- `head-qualify-off` KILLED (matches=1, exactly-once) — the round-94 survivor is closed by the new selftest pin.
- `dispo-fallback-off` KILLED (matches=1 on the refreshed 8-space-indent pattern) — the round-94 broken-pattern is closed.
- All seven new refusal removals KILLED, matches=1 exactly-once: `combining-refuse-off`, `lrm-refuse-off`, `tab-refuse-off`, `id-lookalike-refuse-off`, `num1-anchor-off`, `rm1-anchor-off`, `num2-anchor-off`.
- Manifest totals 95 = 88 carried + 7 new (stub line count and `MUTATION-SCORE x/95` both confirm); semantics field present per entry (82 replace-all round-93-lineage + 6 exactly-once carried + 7 exactly-once new).

## Dependencies, tooling, bounds

- Waited on `../ExecMutants95/DONE` and `../ExecGraderV6/DONE` with bounded 45x60s loops (one full window expired before ExecMutants95 landed; a second bounded window caught it; no BLOCKED fired).
- Tooling installed or upgraded: none. No pacman, no sysctl, no git/jj mutations; read-only `git show` of the base rev only.
- Reads only: claims.json, predispatch.py, round-94 lesson (L1 integration record item 3), CriticO94.md recipes, mutants94.py/mutation-score.txt (format reference), ExecGraderV6 stage receipts. Tasking-pointer note: the cited round-94 lesson "## Mistakes R94-M5" does not exist in `corpus/lessons/round-94.md` (mistakes R94-M1..M3 only); the mutation-leg substance it pointed at is in the L1 integration record item 3, which I used. No frozen file was read for amendment, none amended.
- Scratch deleted before yield (`rm -rf /fast/scratch/hyaku/kotodama-r95/MutationTester95`). Stage keeps: mutants95.py, v6-candidate.py, mutation-score-independent.txt, hand-probes.txt, verdict.txt, DONE.

## Stage files

- `stage/mutants95.py`, `stage/v6-candidate.py` — provenance-verified copies.
- `stage/mutation-score-independent.txt` — my assembled score (graded + COMMAND/RC + stub + COMMAND/RC, mirroring the sibling shape, 202 lines).
- `stage/hand-probes.txt` — clean + two hand-probe receipts.
- `stage/verdict.txt` — `MUTATION-INDEPENDENT: MATCH` with details.
- `stage/DONE` — sha256 of verdict.txt.
