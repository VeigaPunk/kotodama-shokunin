# ExecRunHygiene — wave 3 (falsify: scratch & hygiene)

Verdict: **BROKEN** on the attacked axis. The landed bytes and the graded claim-C counter are clean on scratch; the claim-Ca counter writes under `/tmp` unconditionally (D1), a non-runnable shadow copy of the claim-C counter sits at a `counters/` path (D3), and the claim's own reproduction string omits `--combined` so it prints 11/12, not the claimed 12/12 (D2, documentation-only — the landing itself reproduces 12/12 with the flag).

Axes walked: (A) scratch discipline / no-`/tmp`; (B) selftest cleanup; (C) fleet-root misroots; (D) landed diff surface (size, path surface).

Revisions exercised: base `f556d1049fe651d3d63975600b13acd9fb686f15`, freeze `5d0167464309d8133991b30f7d7a7011a6a0fd14`, claim Ca `012e8d3c8b92f47c734f735d58d118d574fe6a14`, claim C `4f5e3b2535c2c06c51627dc2736c40183847cae1`; round-74 lands `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`, round-74 freeze `00c408a0af2fa5ddf65af2224152ce258b26d896`.

## Method

Two throwaway clones under `/fast/scratch/hyaku/kotodama-r75/ExecRunHygiene/` (lane `--shared`, plus a `--shared` clone of the fleet repo used only as the read-only `--fleet-root` for legs that need one). Every counter ran with `-C`-explicit git against those clones; `strace -f -e trace=mkdir,mkdirat` on each run attributes every directory write to the process that made it. Nothing was written to the lane worktree, the fleet repo, `/tmp` (by me), or `/home/vgpnk/Projects/shokuknow`. No tool installs.

## D1 — HIGH — `accept-ca.py` writes under `/tmp` regardless of `--work`/`$HYAKU_SCRATCH`

Code path:
- `reports/round-75/accept-ca.py:2171-2175` — comment "clones live under /tmp … this counter's own clones and fixtures stay under --work" then `R74_TMPDIR = "/tmp"`; `:2182` `"TMPDIR": R74_TMPDIR` in the child env of `_run_r74_counter`; `:2272-2274` the RECEIPTS leg invokes the round-74 counter through it.
- `reports/round-74/accept-ca.py:1966` — `tmpdir = tempfile.mkdtemp(prefix="r74-ca-")` with **no `dir=`**, so the clone tree follows that `TMPDIR`. The round-74 counter's own receipt normaliser (`:101`) exists precisely because those clones are volatile `/tmp` paths.

Measured (real run, `--work` set, scratch root outside `/tmp`):

```
$ git -C <clone> checkout -q -B main 012e8d3c8b92f47c734f735d58d118d574fe6a14
$ HYAKU_SCRATCH=<S>/unused python3 -B reports/round-75/accept-ca.py --root . \
    --lands 012e8d3c8b92f47c734f735d58d118d574fe6a14 \
    --freeze 5d0167464309d8133991b30f7d7a7011a6a0fd14 \
    --fleet-root <S>/fleet-ro --work <S>/work-real        # strace -f mkdir,mkdirat
LEG PASS RECEIPTS
...
ACCEPT-CA-75: FAIL legs=11/12        # COMBINED only; see D2
```

`strace` record of that run: **121 `mkdir` calls under `/tmp`** — `70 /tmp/r74-ca-jxpeb2cp`, `47 /tmp/r73-ca-6eq71u5l`, `3 /tmp/r73-lands-3vbtrm2f`, `1 /tmp/r73-fleet-2s5rkf3n`; first line `mkdir("/tmp/r74-ca-jxpeb2cp", 0700) = 0`. Every other absolute `mkdir` in the run is under `<S>`; nothing touches the lane or the fleet clone. The child prints `clone=/tmp/r74-ca-jxpeb2cp/lands`, and the trees are removed on exit (no residue).

The shipped receipt already records this: `reports/round-75/telemetry/accept-ca-74-at-lands.txt:11` `# clone: /tmp/r74-ca-g9drlchf/lands`, `:12` base-clone, `:47` `clone=/tmp/r74-ca-g9drlchf/lands`. So the frozen evidence itself was produced with `/tmp` materialisation.

Contradiction: `reports/round-75/accept-ca.py:144` states "no path of this counter's own is hardcoded to /tmp." Line 2175 hardcodes exactly that.

Why wave 1/2 did not see it: the selftest's round-74 counter is a stub — `accept-ca.py:3090` writes `STUB_R74_CA` into the fixture. `strace` of the full selftest: **0** paths matching `/tmp`, **0** occurrences of `r74-ca-`; `SELFTEST: 154/154` green. The green selftest is structurally unable to detect D1.

Collateral: `/tmp` is world-visible and shared with sibling seats; during my runs another process's transient `/tmp/r74-ca-2294rjcv` existed alongside mine. Concurrent Ca evaluations therefore interleave in `/tmp` (unique names, so correctness holds, but the committed receipts publish machine-local `/tmp` paths and any `TMPDIR`-sensitive child sees a shared namespace).

Smallest disposition: make the child `TMPDIR` `os.path.join(work, "r74-tmp")` (the existing `RECEIPT_R74_TMP_RE` already strips `r74-ca-*` anywhere, so the normaliser needs no change), or have the leg substitute `<TMP>` into the child env; drop or qualify the `:144` sentence either way. Not applied — leaf seat.

## D1b — LOW — `accept-ca` also falls back to the system tempdir when no `--work`/`$HYAKU_SCRATCH`

`accept-ca.py:275` `root = tempfile.gettempdir()` in `scratch_dir()`; `:1166` and `:2221` set `TMPDIR` to `RUN_STATE["work"] or tempfile.gettempdir()`. Accept-c deliberately refuses that: `accept-c.py:6024-6027` bans `/tmp` (and `gettempdir()`) and `:6107-6112` refuses with exit 2 — verified:

```
$ python3 -B reports/round-75/accept-c.py --root . --lands 4f5e3b2… --freeze 5d01674… --work /tmp/ExecRunHygiene-probe
REFUSED: scratch root /tmp/ExecRunHygiene-probe is the system temporary directory (pass --work or set $HYAKU_SCRATCH; QUALITY 14)
ACCEPT-C-75: FAIL legs=0/13 (refused: …)      exit=2      # no directory created
```

The two counters should share one policy; as landed they do not. Live corroboration, same minute: a sibling seat's `accept-ca.py` (run without `--work`/`$HYAKU_SCRATCH`) materialises at `/tmp/r75-ca-2ixc3_qt/{lands,base}` (`pgrep -af accept-ca.py` shows `… ExecJunkRerun/…/repo/reports/round-75/accept-ca.py --root … --lands c82d2607… --freeze 5d01674…`); I did not create, inspect further, or remove that directory.

## D2 — MEDIUM — claim Ca's published command does not reproduce its own PASS line

`reports/round-75/claims.json:202` (`Ca.counter`) and `:175` (`Ca.after`) publish, without `--combined`:

```
python3 -B reports/round-75/accept-ca.py --root . --lands <lands> --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin
```

Run verbatim at Ca's landing it exits 1 (`LEG FAIL COMBINED — the explicit --combined revision is required`; `ACCEPT-CA-75: FAIL legs=11/12`), because the frozen COMBINED leg (`claims.json:213`) *requires* `--combined <combined-revision>` and `accept-ca.py:2550-2552` fails hard rather than skipping. Adding `--combined 4f5e3b2535c2c06c51627dc2736c40183847cae1` to the identical clone gives `LEG PASS` ×12 and `ACCEPT-CA-75: PASS legs=12/12`, exit 0 — so the landing holds; only the claim's reproduction sentence is wrong. The committed measurement receipt is honest: `reports/round-75/telemetry/measures-ca.txt:3` carries `--combined 4f5e3b2535c2c06c51627dc2736c40183847cae1`.

Impact: a grader executing the claim string records 11/12 and a red Ca, i.e. a false red on a landing that is green under the leg table.

## D3 — MEDIUM — a silent, non-runnable shadow "counter" is tracked at a counter path

`.ufo/waves/round-75/counters/accept-c.py` at `4f5e3b2` is blob `7147bc194ede…` — byte-identical to `.ufo/waves/round-75/w2/parts/part-a.py`: 515 lines, ending at `# --- PART B ---`, no `__main__`. Executed:

```
$ python3 -B .ufo/waves/round-75/counters/accept-c.py --selftest
exit=0            # no output at all
```

The graded counter is `reports/round-75/accept-c.py` (blob `1773b82a3a35…`, 6145 lines, mode 100755, named by `claims.json`). A reader or script that picks `counters/accept-c.py` because of its name gets exit 0 and no legs — a silent zero-grade. By contrast `.ufo/waves/round-75/counters/accept-ca.py` is identical to the graded Ca counter (`05a4196faac7…`), which is harmless, and `.ufo/waves/round-75/w2/stage/reports/round-75/accept-ca.py` is a stale pre-final copy (`4bc89223eccd…`, 166,264 B vs 166,430 B). The fragment should not carry a counter name in the landed tree.

## Non-findings (checked, clean)

1. **accept-c scratch (task item 2).** `HYAKU_SCRATCH=<fresh> python3 -B reports/round-75/accept-c.py --selftest` → exit 0, `SELFTEST: 85/85` (14.4 s; 32.9 s under strace), `CASE clean: PASS -- PASS 13/13`. `strace`: 40,601 `mkdir` calls, **all** inside `<HYAKU_SCRATCH>/kotodama-r75`; **0** under `/tmp`; `ls -d /tmp/r75-*` empty before and after (and before the whole session). After exit only the empty root `<HYAKU_SCRATCH>/kotodama-r75/counter` remains — that is the scratch root created by `_scratch_root` (`accept-c.py:6113-6116`), not a temp dir; no fixture, clone or selftest dirs survive. `--work /tmp/...` is refused before any write (see D1b). I did not run accept-c's 13-leg grading legs against real lands in this seat (only `--selftest` and the refusal probe).
2. **accept-ca selftest cleanup.** Exit 0, `SELFTEST OK: 154 checks across 39 scenarios reported-fail=0` / `SELFTEST: 154/154` (10.1 s; 34.4 s under strace); all writes under `<HYAKU_SCRATCH>/kotodama-r75`; the root is left empty. Its greenness does not cover D1 (stub child, above).
3. **Fleet-root misroots (task item 3).** `git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all` names exactly one path containing kotodama/round-75: `?? .ufo/waves/round-75/w1/RevEntryQuality.md` (14,330 B, mtime 2026-10-27 14:07). **Misroot:** it is a wave-1 seat report written into the fleet repo; the lane's own `.ufo/waves/round-75/w1/` holds 40+ sibling seat reports (Connector… through SentinelScope) but no `RevEntryQuality`, while rounds 72/73/74 each carry one in the lane (`.ufo/waves/round-7{2,3,4}/w1/RevEntryQuality.md`). It is untracked and not gitignored, so it can be committed into the fleet repo by accident; it is also absent from the lane's evidence. Left untouched. Other fleet dirt is unrelated to round 75 and untouched: `M .ufo/reports/round-58/chousa.md`, `?? .scratch/closure-mado-r50.json`, `?? .scratch/source-routing-queue.md`, `?? o.bin`, plus `?? .ufo/reports/round-78/kotoba.md` which appeared during the wave (concurrent seat activity).
4. **Landed diff surface (task item 4).** `git diff --numstat f556d10..4f5e3b2`: 295 paths (288 added, 7 modified), 63,011 insertions, 19 deletions. Largest changed blob `corpus/SOURCES.md` = 977,373 B — **no changed file over 1 MiB** (tree-wide at `4f5e3b2` the only blob >1 MiB is `reports/round-60/captures/pages/S637.txt`, 1,597,667 B, unchanged from base). Path surface: the 42 non-`.ufo` paths are all declared — `corpus/SOURCES.md`, `corpus/README.md`, `corpus/QUALITY.md`, the three `corpus/knowledge/myth-symbol/narrative-structure-frameworks*` entries, `corpus/lessons/round-75.md`, `reports/round-75/**` (both counters, ledger, claims, 3 R1EXEMPT fixtures, 9 evidence windows, 15 telemetry receipts), `reports/round-28/readme/sweep.py` (Ca `fixed_surfaces`, R74-M3), `SHONEN.md` and `SKILL.md`:701 (Ca; W2-F1 / `fixed_surfaces`), `SCORECARD.md` (Ca ANNOTATE leg, `claims.json:207` requires rows under `## Corrections — round 75`). The other 253 paths are `.ufo/waves/round-75/` workspace (w2 100, assimilation 68, w1 40, counters 29, root 16) — wave work products, not grading surface, except the D3 fragment. **No path outside the declared surface, no oversized blob.**
5. **Lane worktree state observed (not mine, untouched).** `M LOG.md`, `M corpus/lessons/round-75.md`, untracked `w3/*.md` reports and `w3.ready.dispatched`; `reports/round-75/__pycache__/accept-ca.cpython-314.pyc` is untracked/gitignored — no `__pycache__` is tracked at `4f5e3b2` (the only pycache-named tracked files are round-60 telemetry `.txt`).

## Risk summary

- D1 puts every seat that evaluates Ca outside its declared scratch and publishes a `/tmp` clone path in frozen evidence; under QUALITY 14 / prompt §7.4 that is a violation, and it makes side-by-side Ca runs share `/tmp`.
- D3 can yield a silent exit-0 "pass" from a path that looks authoritative.
- D2 makes the documented Ca reproduction look red while the landing is green.

## Suggested fixes (not applied; leaf seat)

1. `accept-ca.py`: derive the round-74 child's `TMPDIR` from `work` (e.g. `work/r74-tmp`) instead of `R74_TMPDIR="/tmp"`; the existing receipt normaliser already strips `r74-ca-*`. Fix or qualify `:144`.
2. `claims.json`: append `--combined 4f5e3b2535c2c06c51627dc2736c40183847cae1` to `Ca.counter` and the `Ca.after` sentence (or have the counter skip-and-report COMBINED when absent, matching the receipt).
3. Delete or rename `.ufo/waves/round-75/counters/accept-c.py` (it is `w2/parts/part-a.py`); refresh or drop `.ufo/waves/round-75/w2/stage/reports/round-75/accept-ca.py`.
4. Move `RevEntryQuality.md` into the lane's `.ufo/waves/round-75/w1/` (or delete it) — owner: the w1 seat / L1, not this seat.

No blockers. Installs: none. Seat scratch deleted after this report was written.
