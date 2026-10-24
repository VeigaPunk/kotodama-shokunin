# SentinelScope — round-66 scope guard + write-boundary audit (w1)

Seat: sentinel (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (jj-colocated),
base `94209e8f80969dbac48d56c5d0e2e623635b8616`. Inspected 2026-10-24T08:35–08:41 -03.
Read-only throughout: no git/jj writes, no staging, no counter runs, no subagent dispatch,
no tool installs (no pacman/uv/npm transaction ran; pacman paused as ruled).

## Verdict

- **No round-66 write fell outside the allowed roots.** Content-wise the lane diff vs base is
  exactly the declared O land plus the two round-66 untracked roots.
- **`tools/reopen-row.py` is byte-identical to base** (hash equal, 0-line diff).
- **The corpus/knowledge guard leg is currently vacuous, not passed**: the entry, the S776 row
  and the games-entry re-point have not landed yet, so "diff names only the new entry plus the
  games S776 re-point" cannot be judged. L1 must re-run that leg after integration.
- No misrooted kotodama round-66 seat note exists at the fleet root.
- The named hazards below are record/integration risks, not lane-state mutations.

## Scope-guard calls

| # | leg | command / evidence | result | verdict |
|---|---|---|---|---|
| 1 | `tools/reopen-row.py` unchanged | `git rev-parse BASE:tools/reopen-row.py` = `2894d2efdfa28cb0a89ed3723438c8bb48144bdf`; `git hash-object tools/reopen-row.py` = same; `git diff BASE -- tools/reopen-row.py \| wc -l` = `0` | identical | **PASS** |
| 2 | writes only `reports/round-66/`, `.ufo/waves/round-66/`, claim land paths | `git status --porcelain`: ` M tools/check-claim-separability.py`, `?? .ufo/waves/round-66/`, `?? reports/round-66/`; no `D` entries; `git diff --cached --name-only` empty | tool file is a declared O land (`claims.json` O `lands[0]`, `git diff --stat` +254/−39); everything else inside the two roots | **PASS** |
| 3 | corpus/knowledge diff names only new entry + games S776 re-point | `git diff --name-only BASE -- corpus/knowledge` → EMPTY; `git diff --name-only BASE -- corpus` → EMPTY; entry absent (`ls .../scent-perfume-aromatics-codes.md` ENOENT); `corpus/SOURCES.md` = 701 rows (== base) ending `S775`; games entry still `(S753)` at `:23` | nothing has landed yet | **PENDING / vacuous** |
| 4 | fleet-root misroot sweep | `git -C /home/vgpnk/Projects/shokunin status --porcelain` → 19 `M` + 11 `??`, none round-66; no `/home/vgpnk/Projects/shokunin/.ufo/waves/round-66`; fleet `.ufo/reports/round-66/` holds only other lanes' tracked reports (`audio.md`, `game-dev-2d.md`, `kotoba.md`, `revenger.md`) | no kotodama seat note misrooted | **PASS** |
| 5 | dispatch path resolution | `spec-v2.json`: 64 items, 64 unique names, names == `swarm-registry.json` members (64), `taskcall-v2.json counts.spawn=64`; every path token in prompts: 0 outside the lane, 0 fleet-root `.ufo` mentions; placeholder `…/w1/<SEAT>.md` is lane-absolute | structurally cannot misroot from the spec | **PASS** |
| 6 | frozen-before-data | `claims.json` 08:23, `accept-{c,o,ca}.py` 08:25, dispatch registry `createdAt` 08:29; dry-run/controls stamp `measured revision … 94209e8…`; stamped `counter sha256 (self)` == `sha256sum` of current counters (`0726b4b…`, `6817…`, `a4b93…`) | counters unchanged since their receipts | **PASS** |
| 7 | corpus/registry untouched by seats | `grep -c '^| S' corpus/SOURCES.md` = 701 (base 701); `find corpus/knowledge -name '*.md' \| wc -l` = 239; culture-material = 32 | base state | **PASS** |
| 8 | hidden/ignored/symlink writes | `ls .scratch` ENOENT; `git status --ignored` adds only pre-existing `__pycache__`/`run.log`; `find round-66 -type l` empty; no world-writable files; `git stash list`, `.git/*.lock` empty | no hidden writes | **PASS** |

Pre-existing fleet-root junk, named and **untouched** (all older than this wave, so not
misroots of r66): `write` (25 B, `agent://U100N079H334f935b`, 2026-10-21 — a misdirected
`write` argument from an earlier session, i.e. the class recurs), `bm.json`, `live.html`,
`live_s228.html`, `nama.html`, `s395.txt`, `tf_bavelas.html`, `unblob.log`, `wb2.html`,
`xc.xml`, `scripts/hyaku/*.bak-20261023T040735Z`, `?? .ufo/waves/round-41/`.

## Findings

### S-1 (MEDIUM, integration/process cleanup) — 130 MB embedded repo inside the report tree
`git add .ufo/waves/round-66` (or any blanket add of a REC land `.ufo/waves/round-66/w1/`) will
stage an **embedded-repository gitlink** plus 12,033 files of duplicated corpus/history.

Evidence:
- `du -sh .ufo/waves/round-66/w1/mut-entry-scratch` = **130M**; `find -type f | wc -l` = **12033**;
  breakdown `.git` 82M, `.jj` 16M, `corpus` 13M.
- `git status --porcelain -uall -- .ufo/waves/round-66/w1/mut-entry-scratch` collapses to one
  `??` line — git sees a single nested repo, i.e. an add becomes a gitlink, not content.
- `.ufo/waves/round-66/w1/mut-entry-scratch/.git/worktrees/*/gitdir` points at
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.scratch/ca02-wt-r34/.git` (absent),
  `/fast/scratch/hyaku/kotodama-r51-author/.git` (absent) and
  `/fast/scratch/hyaku/s3-ready66/kotodama-shokunin/.git` (present, mtime 2026-10-21).

Exploit path: L1 stages w1 recursively → record commit carries a broken submodule entry and
~130 MB of duplicated tree, or the add fails mid-run and the receipt/commit sequence slips.
Impact: record-commit integrity, repo size, slow subsequent git ops. Smallest remediation:
MutEntry moves/deletes its scratch tree before integration (e.g. `/tmp/mut-entry-r66`), or L1
stages w1 by explicit paths (`git add .ufo/waves/round-66/w1/<SEAT>.md …`) and never `-A`.

### S-2 (MEDIUM, calibration — fabrication surface) — D3's `>=8 seats` leg is a paper tiger
`accept-ca.py:148-155`:

```python
seat_paths = re.findall(r"(.ufo/waves/round-66/\S+\.md)", d3)
existing = [p for p in seat_paths if os.path.isfile(os.path.join(root, p))]
reported = len(seat_paths)
d3_ok = reported >= 8 and len(existing) >= 8 and len(existing) == reported \
        and re.search(r"(?i)(seat|report|status)", d3)
```

- It counts **occurrences**, not distinct seats: a path repeated twice increments both
  `reported` and `existing` by two, so 8 lines over 4 real files passes the floor.
- It never checks per-seat status or last-error text, although the claim requires
  "per-seat status and last-error text for dead seats"; the `(seat|report|status)` regex is
  satisfied by the seed's own header line `# report: each seat writes …`.
- The receipt is a Ca land, so trimming it to the surviving seats is sufficient to pass.
  Current seed names 65 expected files; only 27 `w1/*.md` exist at inspection — honest today,
  fragile at integration.

Smallest remediation: derive the required set from `swarm-registry.json` (`members`, 64),
require every member to appear once as `w1/<name>.md` with an explicit `status=live|dead`,
non-empty `last_error` for dead, and reject duplicates (`len(set(...)) == len(...)`).

### S-3 (MEDIUM, calibration — evidence binding) — D4 accepts an unbound free-text receipt
`accept-ca.py` D4 block accepts any text with `^SEPARABILITY: \d+ findings$`,
`acceptance_runs=\d+` and no `PARTIAL`. There is no tool sha256, argv, timestamp or lane
revision in the receipt, so a hand-written stub passes, and a run of a *pre-upgrade* tool
(which cannot emit a complete bounded verdict) is indistinguishable from the upgraded one.
D4's evidence is in fact produced by O's land, but the leg never reads the tool, so the
separation claim "Ca does not depend on O" holds only because the receipt is a Ca land.
Smallest remediation: require `tool_sha256: <sha of tools/check-claim-separability.py>` and
`argv: …` lines, verify the hash against the tool blob, and require `partial_runs=0`.

### S-4 (MEDIUM, records integrity) — D1's premise is inconsistent across the round's own records
Three committed-record sources give three different statuses for the same old capture
`20250926172224`:

| source | claim |
|---|---|
| `reports/round-66/claims.json` Ca statement | "committed capture 20250926172224 replays **404** although CDX lists 200 pdf" |
| `reports/round-66/telemetry/s753-recapture.txt:20-22` | `old_replay_status=**200** size=529795`, `/tmp/old-cap.bin: PDF document` |
| `.ufo/waves/round-66/w1/ScribeS776Gate.md:36,71-76` | `curl -L …20250926172224id_/…` → `**302**` → `20261024111013id_/…` → final `200 application/pdf`; "replays **404** here … that observation does not reproduce" |

The seat correctly disclosed the non-reproduction, but the frozen statement still asserts a
404 and the telemetry disposition garbles the distinction ("replays PDF not pdf"). The
substantive defect is real and is the R65-D1 class: the pinned replay is a **redirect stub**
(302 to the newest capture), not a pinned snapshot, so S776's fresh capture is justified — but
the record must say that, not "404". Additionally the artifact the receipt names,
`/tmp/old-cap.bin`, is now **0 bytes** (mtime 08:34, one minute *after* the receipt's 08:33),
so the old-capture evidence is not durable — the very defect class D1 exists to repair.
Impact: D1 can pass (`old_replay_status` is never read by the leg) while the lesson states a
premise that its own evidence contradicts, and the retained artifact cannot reproduce the
claimed bytes. Smallest remediation: in `corpus/lessons/round-66.md` state "pinned replay is a
302 redirect stub to the newest capture (200 PDF), 404 did not reproduce on 2026-10-24";
copy the old/new PDFs under `reports/round-66/telemetry/` with sha256 rather than naming
`/tmp`; have the D1 leg require the sha256 line.

### S-5 (LOW, controls) — O's do-nothing control is argued, not executed; O is green at dispatch
`controls-o.txt` has **no** `ACCEPT-O-66: PASS|FAIL` line (all other controls do:
`controls-c.txt`, `controls-ca.txt` each carry `ACCEPT-…-66: FAIL`), and it reasons from
`--help` option absence rather than running the counter on a base-bytes tool. The base tool
extraction is genuine (`/tmp/sep-base.py` sha256 `5764ea27…` == `git show BASE:tools/…`),
yet `dry-run-o.txt` already shows `ACCEPT-O-66: PASS` at 08:26, i.e. **before any seat ran** —
O's entire land is the tool itself, so the wave cannot falsify O except through the MUT legs.
Impact: a do-nothing wave would still show O green; the only falsifier is the four mutants.
Smallest remediation: add a mechanical base-bytes run to `controls-o.txt`
(`ACCEPT-O-66: FAIL failing=[SELFTEST,DIFF,OPTIONS,…]`) and state in `claims.json` that O's
acceptance is pre-satisfied at dispatch with the mutant legs as its falsifier.

### S-6 (LOW, lane-state) — a jj snapshot was written into the lane during the wave
`.jj/repo/op_heads/heads/dda1f34…` (mtime 08:32) and its op-store entry contain
`snapshot working copy` with args `jj log --no-graph -r @ -T 'commit_id ++ "\n"'`;
`.jj/working_copy/tree_state` was rewritten at 08:32. I ran no jj command, and the args match
an agent stamping the "measured revision (lane main)" line, so this is another agent's
read-looking `jj log` that auto-snapshotted the working copy mid-wave. No ref/commit changed
(`refs/heads/main` still `94209e8`, `git for-each-ref` clean; no staged entries), so impact is
metadata drift: the op now records a torn mid-wave tree that any later jj-based integration
builds on. Smallest remediation: stamp with `git rev-parse main` instead of jj; L1 confirms the
08:32 op is benign before any jj commit step. (`.git/index` mtime 08:32 carries no staged
content — `git diff --cached` empty — consistent with a stat refresh from read-only
`git status`, possibly this seat's own.)

### S-7 (INFO, hand to RevWaveEvidence) — seat-note trailer hygiene
27 `w1/*.md` exist; 16 have no `Report:` trailer (`ConnectorSiblings`, `ExecCounterSmokeC`,
`ExecSeparabilityReal`, `MutTool`, `RevBaseCensus`, `RevD1Anchor`, `RevD4Bound`,
`RevLoreHandoff`, `RevSourceSupport`, `RevWaveEvidence`, `ScoutGapScent`, `ScoutPartialOwners`,
`ScoutRow02`, `ScoutRow03`, `ScoutRow09`, `ScribeS776Gate`) and `ScribeEntrySpec.md` carries
two. This compounds S-2's D3 leg (a seat that never renders a trailer still counts as a seat).

## Dependencies recorded, not violations (absent at inspection)

- `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` — absent; C entry not
  landed (no draft under the wave dir either).
- Registry `S776` and `S777-S800` — absent; `corpus/SOURCES.md` ends at `S775` (701 rows).
- Games entry re-point `(S753)` → `(S776)` — not applied; `grep -c '(S753)'` = 1 at `:23`.
- `reports/round-66/separability-manifest.json`, `telemetry/final-measures-*.txt`,
  `telemetry/separability-real.txt`, `corpus/lessons/round-66.md` — absent; `corpus/QUALITY.md`
  unchanged (criterion 18 not added).
- `telemetry/seat-evidence.txt` is a **seed**: it names 65 expected reports; 27 exist.

These are the wave's pending build lands. Consequence for L1: re-run guard legs 3 (corpus
diff names) and 5 (only if seat reports move), plus the complete `git status` sweep, at the
integration tip — that is the only point at which the NOHARM names can be judged.

## Untrusted-data handling / secrets

`grep -rInE '(api[_-]?key|secret|passwd|password|BEGIN … PRIVATE KEY|ghp_|github_pat_|AKIA…)'`
over `reports/round-66` and `.ufo/waves/round-66` (excluding the scratch clone) produced only
historical wave prose and the literal `/etc/passwd` string inside the mutant fixtures'
negative tests. No credentials, no tokens, no private keys. No world-writable files; the
dispatch registry is mode 600.

## Report

Report: .ufo/waves/round-66/w1/SentinelScope.md
