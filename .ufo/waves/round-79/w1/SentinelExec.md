# SentinelExec — round-79 W1 — read-only observation execution grammar

Seat: SentinelExec (sentinel). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Base: `44f76d456c1b326a71ffdb381590af825cbf11be`.
Stage (draft production files, L1 integrates): `.ufo/waves/round-79/w1/stage/SentinelExec/`
Scope: refuse shells, subcommands, config hooks, external diff and effects; exact safe git syntax. Draft + committed files read; no integration, no shared-file edits, no git mutation in the lane.

## 1. Verdict

The committed round-73 observe guard (`reports/round-73/accept-ca.py` at base, sha256 `222d4dd6…b89`) **cannot be the basis of the O guard as written**. Its admission rule is `argv[0]` basename in `{git, grep, find, wc, ls, cat, sha256sum, stat, python3}`; it never screens `git` subcommands, flags, `-C`/`--git-dir`/`-c`, revisions, paths, or the environment's config. Every exercised escape below was admitted by the committed `argv_problem` and then executed by the committed `run_observe`.

A closed replacement is drafted (`stage/SentinelExec/observe_grammar.py`, spec `OBSERVE-GRAMMAR.md`). On the probe set it refuses every escape, admits the pinned read forms, and its environment scrub alone neutralises the operator-config drivers. It is a **draft**: no counter, ledger or selftest was built or run against it, and nothing here claims an implementation check passed.

## 2. Evidence — committed guard (exercised)

Probe: `stage/SentinelExec/probe_observe.py`, raw `probe-observe-v2-raw.txt`, records `probe-observe-v2-results.jsonl`. Each case runs once through the committed `argv_problem` and `run_observe` (module imported unmodified from base bytes). Fixtures: a lane-shaped repo, an "other" repo holding a sentinel, and a hostile HOME whose `core.pager`, `diff.external`, `diff.evil.textconv` and `core.hooksPath` each write a marker.

| case | argv | committed `argv_problem` | effect observed |
|---|---|---|---|
| C00 | materialize (clone + checkout), host HOME config | — | `post-checkout` hook from `core.hooksPath` **executed** |
| C01 | `git cat-file -p HEAD:a.txt` | admitted | mutable revision read |
| C04 | `git grep -O needle -- a.txt` | admitted | HOME `core.pager` **executed** |
| C05 | `git -c core.pager=… grep -O …` | admitted | argv `-c` accepted; pager executed (same script as HOME config, so the marker does not attribute the source — the admission is the finding) |
| C06 | `git diff REV1..REV2 -- a.txt` | admitted | HOME `diff.external` **executed** |
| C06b | `git diff --no-ext-diff REV1..REV2` | admitted | HOME textconv driver **executed** (twice) |
| C08 | `git -C <other> cat-file -p …:secret.txt` | admitted | read **outside the clone** |
| C09 | `git --git-dir <other>/.git cat-file …` | admitted | read **outside the clone** |
| C10 | `find . -maxdepth 0 -fprint <outside>` | admitted | file **written outside the clone** |
| C11 | `cat <outside>/secret.txt` | admitted | absolute read outside the clone |
| C12 | `python3 -c "print(245)"` | refused | — |
| C12b | `python3 -c "import pathlib;print(245)"` | admitted | constant printer prints `245` (the decoy token `pathlib` passes the regex) |
| C13 | `python3 -c "import subprocess;subprocess.run(['sh','-c',…])"` | admitted | shell escape **executed** |
| C14 | `git cat-file -p 7d8755d:a.txt` | admitted | 7-hex (mutable prefix) read |
| C15 | `git -C <other> update-ref -d refs/heads/victim` | admitted | outside repo branch **deleted** (fixture only) |
| C16/17 | `git ls-files --others --exclude-standard` | admitted | worktree-only file observed (clone-local) |
| C18 | `git ls-tree -r --name-only <40hex> -- a.txt` | admitted | control: pinned form, correct |

Controls: `C03` (`git cat-file blob <40hex>:path`) and `C18` admitted and correct; `C07` (`git diff --no-ext-diff --no-textconv …`) ran clean with zero markers; `textconv-control-raw.txt` shows `git show --textconv` fires the driver while default `git show` does not (so C02's "no marker" is real behaviour, not wiring error).

Verified dead code: `RUN_STATE["outside_clone"]` is set only when `run_observe(..., cwd_is_clone=False)` is called; the sole call site (accept-ca.py:373) uses the default `True`. The STAMP check at :855 ("an observe_cmd ran outside the clone") therefore cannot fire.

Committed round-73 ledger (`reports/round-73/ledger.json`, 8 pairs) shape: L01–L03 and L07–L08 are `python3 -c` (three of them `subprocess.run(['git', …])` inside python, which the escape C13 uses); L04–L06 are worktree `grep`. The committed ledger contains no `git -C`. The round-73 wave draft (`.ufo/waves/round-73/w1/drafts/ledger-draft.json`) uses `git -C <absolute lane>` and `git ls-files --others` (worktree-only); both are refused by the draft grammar.

## 3. Evidence — draft grammar (probe of the draft; not an implementation check)

`probe-draft-raw.txt` (31 cases, **0 mismatches** against declared expectations), `edge-draft-raw.txt` (15 shape edges). Final file bytes are the ones probed (see `SHA256SUMS`).

Exact admitted forms (`<40hex>` = lowercase full commit id; `<path>` = relative, no `..`, no leading `-`, no `:`, no control characters):

```
git cat-file -p|-s|-t <40hex>[:<path>]
git cat-file blob <40hex>:<path>
git ls-tree -r --name-only <40hex> -- <path>
git grep [each of -n -c -l -o -h -H -E -F -i -w -x at most once] <pattern> <40hex> -- <path>
git rev-parse --verify --quiet <40hex>^{tree|commit}
git rev-list --count <40hex>
```

Refused before any process starts: `argv[0] != git`; any global option as argv[1] (`-c -C --git-dir --work-tree --exec-path --paginate --namespace --config-env`); subcommands outside the table (`show diff log checkout clean update-ref ls-files …`); flags outside the per-form whitelist (`-O`, `--open-files-in-pager`, `--textconv`, `--ext-diff`, `--output`); non-40-hex revisions (`HEAD`, branch/ref names, 7-hex, uppercase, `^{tree}` on a symbolic name); unsafe paths; repeated flags; wrong positional arity; grep patterns starting with `-`.

Scrubbed environment (replaces the environment; does not extend it): `GIT_CONFIG_GLOBAL=/dev/null`, `GIT_CONFIG_NOSYSTEM=1`, `HOME` and `XDG_CONFIG_HOME` → empty scratch, `GIT_PAGER=cat`, `PAGER=cat`, `GIT_TERMINAL_PROMPT=0`, `GIT_OPTIONAL_LOCKS=0`. Requires git ≥ 2.32 (fail closed).

Environment-only control (`E01–E03` vs `H01–H03` in `probe-draft-raw.txt`): with the scrub and a hostile HOME, raw `git diff` (ext-diff on), `git diff --no-ext-diff`, and `git grep -O` produce no markers; the same three without the scrub fire the external diff, the textconv driver and the pager. Under the scrub, `materialize` fires no hook (`MATERIALIZE_MARKERS []`).

## 4. Findings for L1 (ranked)

1. **HIGH — argv admission by basename only; `git` unrestricted.** `-C`, `--git-dir` reach outside the clone (C08, C09); `update-ref -d` mutates an outside repo (C15, executed on fixture). Fix: closed grammar (`observe_grammar.py`), `cwd` = clone only, no `-C`/`--git-dir`.
2. **HIGH — `python3 -c` admitted with decoy tokens.** `pathlib|open(|subprocess|os.` in the code string is a token gate, not a semantic one: C12b prints a literal, C13 spawns `sh`. Fix: no python in the observe grammar; migrate the three subprocess pairs and the two glob/json pairs (§5).
3. **HIGH — operator config executes in observation and materialization.** `run_observe` keeps the parent's `HOME` and sets only `GIT_CONFIG_NOSYSTEM`, so the pager (C04), `diff.external` (C06), textconv (C06b), and `core.hooksPath` (C00, in `materialize`, which uses `os.environ` unscrubbed) all execute. Fix: scrubbed env (§3); `materialize` must also run under it.
4. **HIGH — `find -fprint` and absolute `cat` reach outside the clone** (C10, C11). Fix: no `find`/`cat`/`ls`/`grep` on the worktree.
5. **MEDIUM — mutable and short revisions admitted** (C01 `HEAD`, C14 `7d8755d`). The clone's HEAD is pinned by STAMP, but the observation's own revision is not. Fix: 40-hex only.
6. **MEDIUM — worktree-only observation** (C16/17, `ls-files --others`). The clone is a fresh checkout, so this reads the clone's untracked files, which the round-73 ledger draft used. Fix: refuse `ls-files`.
7. **LOW (dead code) — `outside_clone` check unreachable** (accept-ca.py:343, :373, :855). Fix: remove the dead check in the O counter rather than keep a check that cannot fire; the grammar's cwd/argv screen replaces it.
8. **LOW — counter's own `git diff` legs** (accept-ca.py:260, :272, :283) run against the lane with unscrubbed `os.environ`. Same command shape as C06/C06b, which executed the drivers; the three exact call sites were **not** run in isolation. [INFERENCE for those three lines.] Fix: same scrub, or `--no-ext-diff --no-textconv` on each.
9. **INFO — `git show` default does not textconv** (C02 vs the `--textconv` control). Not a risk for the grammar; `show` is refused anyway.
10. **INFO — selftest env vs observe env differ.** `SELFTEST_ENV` sets `GIT_CONFIG_GLOBAL=/dev/null` (accept-ca.py:994); `run_observe` does not. The selftest does not exercise the observe path's config exposure.

## 5. What L1 must decide (not decided by this seat)

- **Migration of the committed round-73 pairs.** L04–L06 map 1:1 to `git grep -n -E … <40hex> -- SKILL.md`. L01–L03 need `git ls-tree -r --name-only <40hex> -- corpus/knowledge` plus a **count parse mode**, which the draft does not implement (observed = number of stdout lines matching `parse`). L07 (claims.json) maps to `git cat-file -p <40hex>:…` plus grep. **L08 (`max` over round numbers) is not expressible** in the closed grammar: either a pinned constant with a count, or a pinned tool under QUALITY 28.
- **Count mode and aggregation** must be frozen in the claim text before any O ledger freezes.
- **Ledger-level checks** (`observed_at_base` equals a fresh observation; `stated_token` differs from the actual observation) belong to the O counter, not the grammar. Not implemented here.
- **Version floors.** Probed on git 2.56.0 only. The `GIT_CONFIG_GLOBAL` floor (2.32) is stated, not probed on older git. SHA-256 repositories fail closed (64-hex refused).
- **Bounds.** 1 MiB stdout cap (refuse, not truncate) and 120 s timeout are stated defaults.

## 6. Tool and channel record

- No install, no update, no pacman, no host service change. The seat used the system `git` 2.56.0 (`/usr/bin/git`, pre-existing) and system `python3` (stdlib only). Nothing written to `~/.local/bin` or any PATH directory.
- No `task`/delegation. No build, lint or test run; the probes are the only executions, and their raw output is preserved in stage.

## 7. Mutations and writes (all disclosed)

- **Lane:** read-only. `git status --porcelain` shows only the pre-existing untracked round-79 directories. No tracked file, index or ref written.
- **Fixtures:** `git init` in `/fast/scratch/hyaku/kotodama-r79/SentinelExec/probe/{lane,other}` with root verified (`rev-parse --show-toplevel`) before use. Mutations there: fixture commits, a `victim` branch deleted by C15 (intended). The scratch directory is removed after the receipts are copied to stage (`commands.txt` step 7).
- **Stage:** my own report and `stage/SentinelExec/` only.
- **Process deviation disclosed:** several in-place patches to my own draft files (`observe_grammar.py` ×4, `probe_draft_grammar.py` ×1) used scripted string replacement instead of the `edit` tool; each was re-verified by rerunning the probe, and the staged bytes are the bytes the final probes ran against. One `edit` to `OBSERVE-GRAMMAR.md` was mis-targeted: it overwrote the C06 row and duplicated C02. Both were repaired with explicit ranges and the final table was re-read (C01–C16, C18 present once each).
- **Probe v1 superseded:** the first driver had a quoting defect (C06 inconclusive) and double execution on executed cases. Its output is kept as `probe-observe-v1-SUPERSEDED-raw.txt`; its driver file was overwritten by v2 and is not preserved.

## 8. Limits of this seat's evidence

- Every "admitted/refused" statement is a probe of the committed `argv_problem` or of the draft `check_argv`, on the fixtures in §2–3. The draft has not been wired into a counter, a ledger or a selftest.
- "Constant printer" closure is claimed only for the argv forms the grammar admits (git plumbing has no literal-print form). A git-derived value that happens to be constant is a data fact, not a printer, and the O counter's own two-revision check is the control for it.
- No peer was consulted or waited on (leaf seat; no task or delegation).

## 9. Files

Stage (`.ufo/waves/round-79/w1/stage/SentinelExec/`): `observe_grammar.py` (draft grammar + scrubbed run + materialize), `OBSERVE-GRAMMAR.md` (spec), `probe_observe.py`, `probe_draft_grammar.py`, `edge_draft.py` (drivers), `probe-observe-v2-raw.txt` + `probe-observe-v2-results.jsonl`, `probe-observe-v1-SUPERSEDED-raw.txt`, `probe-draft-raw.txt` + `probe-draft-results.jsonl`, `edge-draft-raw.txt`, `textconv-control-raw.txt`, `commands.txt`, `SHA256SUMS`.
