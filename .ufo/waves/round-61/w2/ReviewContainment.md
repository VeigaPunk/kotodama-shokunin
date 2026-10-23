# Round 61 WAVE 2 — containment & misroot sweep (ReviewContainment)

Scope: read-only containment check of the fleet repo, the lane repo (kotodama-shokunin), and /fast/scratch/hyaku/kotodama-r61, per wave-2 dispatch. Nothing deleted, nothing mutated. Measured 2026-10-23, during live wave-2 execution.

## Fleet repo /home/vgpnk/Projects/shokunin

`git status --porcelain` untracked inventory (16 paths):
`.omp/mcp.json`, `.ufo/state/kotoba.report-baseline`, `.ufo/state/kotodama.report-baseline`, `.ufo/state/revenger.report-baseline`, `.ufo/waves/round-58/`, `AGENTS.md`, `bm.json`, `live_s228.html`, `nama.html`, `s395.txt`, `scripts/hyaku/__pycache__/`, `scripts/hyaku/append-closure.py.bak-20261023T040735Z`, `scripts/hyaku/fleet-commit.sh.bak-20261023T040735Z`, `tf_bavelas.html`, `wb2.html`, `write`.
Tracked modifications: 11 × `.ufo/state/*.report-baseline` (lane baselines) + `.ufo/watchdog.log` — normal fleet state files, untouched by this sweep.

**Misroot content check: NO misroot found.** Case-insensitive scan (`kotodama|round[-. ]?61|R61`) over every untracked fleet path above returned zero matches. No untracked fleet file names kotodama round 61 by content, and none does by name (nearest are `round-58/`, `kotodama.report-baseline` — neither mentions round 61).

**Dispatch-example correction:** the cited example `/home/vgpnk/Projects/shokunin/.ufo/waves/round-61/w1/ScribeSrc01.md` does not exist — there is no `round-61/` directory under the fleet's `.ufo/waves/` at all. The real `ScribeSrc01.md` (7.6 KB) is correctly rooted in the lane repo at `kotodama-shokunin/.ufo/waves/round-61/w1/`. The example was stale/wrong-root, not an actual leak. Flag for the round report: any lesson text citing a fleet-root round-61 leak should cite the lane path or nothing.

## Lane repo /home/vgpnk/Projects/shokunin/kotodama-shokunin (measured revision efbee29)

At sweep start, `status --porcelain` showed 4 modified tracked files and 8 untracked wave-1 paths:
- Modified: `LOG.md` (+9), `SCORECARD.md` (+26), `corpus/QUALITY.md` (+2), `reports/round-61/separability-manifest.json` (+20/−6) — per `diff --stat`, 51 insertions / 6 deletions total.
- Untracked: `.ufo/waves/round-61/{gen-w2.py, w2-spec.json}`, `w1/{ScribeSrc01,ScribeSrc08,ScribeSrc09}.md`, `corpus/lessons/round-61.md`, `reports/round-61/telemetry/final-measures.txt`.

**Transient state observed:** within minutes the L1 committed all of the above — a follow-up `status --porcelain` returns only `?? .ufo/waves/round-61/w2/` (this wave's in-flight row reports + `swarm-registry.json`), and `diff HEAD` on `separability-manifest.json` is now empty. Two `git diff` invocations on the manifest returned no output *after* the initial +20/−6 diffstat, i.e. the working tree was actively mutated during the sweep window by the L1's commit. **Finding (low):** lane tracked-file dirt during wave 2 is live round activity, not a misroot; but the manifest flip-flop means any wave-2 seat that read the manifest mid-sweep may have seen pre- or post-commit content. Wave-1 measures were taken on frozen counters, so verdicts are unaffected.

Wave-1 lane outputs are all correctly rooted under `.ufo/waves/round-61/` and the round-61 report/telemetry paths. No lane file is misrooted.

## Scratch /fast/scratch/hyaku/kotodama-r61

- Size: **6.2 G** at first measure; **6.4 G** on a re-measure minutes later (live growth — wave-2 control/mutation seats still writing).
- Top consumers (`du -h --max-depth=1`, sorted): CtlCDoNothing 738M, CtlCJunkLines 671M, CtlCOffTopic 554M, CtlCHonestHtml 554M, CtlCFabricated 435M, w2 324M, MutCounterC 324M, CtlCCopiedRows 234M, KotodamaR61.CtlCHonestPdf 199M, CtlCEchoUrls 198M, KotodamaR61.CtlOHonest 193M, ExecLintTool 193M, CtlCMultiId 187M, then a band of 185M dirs (MutCounterO, L1, CtlOSelftest, CtlOParsing, CtlOKeyed, CtlODoNothing, CtlCSourceless, CtlCQuoteDump, CtlCNoReader); KotodamaR61.ScribeSrc09 and CriticClauseCO are 0.
- Processes: `ps -eo pid,etimes,args | grep kotodama-r61` showed only the sweep's own `du` (etimes 0). A full `/proc/*/cwd` readlink scan found **zero live processes with cwd under /fast/scratch/hyaku/kotodama-r61**. Containment of running state: clean.

## Verdict

No seat misroot into the fleet repo (by name or content); the dispatch's example misroot path does not exist. Lane is correctly rooted and, apart from the expected in-flight `w2/` output dir, clean at commit efbee29+. Scratch is large (6.2→6.4 G live) but process-free. Nothing deleted.

## Residual risk / verification gaps

- Content scan used the text grep tool; binary untracked artifacts (`scripts/hyaku/__pycache__/*.pyc`) were covered by the tool's scan but a string embedded solely in binary form would not surface as a text match.
- The `write` file at fleet root (odd name, zero content matches) was left unexamined beyond the content scan — not round-61 related on evidence available.
- Lane state moved under me (L1 committed mid-sweep); the +20/−6 manifest diff was observed only as a diffstat, never content-read before it resolved to HEAD.
- Tooling directive: no tools installed or updated for this sweep (none needed).
