# MutPath — round-79 W1: blob path traversal, absolute path, colon/option ambiguity

Seat: MutPath (mutation-tester). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `44f76d456c1b326a71ffdb381590af825cbf11be`. Read-only against the lane. Stage: `.ufo/waves/round-79/w1/stage/MutPath/`. No subagents. No shared edits.

## 0. Result

- Traversal and absolute `<rev>:<path>` operands are refused, both by git (rc 128) and by the committed round-74 guard (K2, K3, K26). Those are not the risk.
- The risk is everything around them. The committed observe guard the O design would inherit accepts **20 of its 30 refusal fixtures** (MATCH 12, GAP 20, REVIEW 3 of 35). The findings cluster in six classes: option pass-through (write and code execution), mutable reads (index, named refs, multi-rev), false zero observations, worktree reads including a symlink escape, non-blob objects, and replace refs.
- The O guard is base-absent (CLAIMS-DRAFT). These results are measured against the committed precedent `reports/round-74/accept-ca.py` (H2 guard) and against git itself. They are red-before evidence for O, not a verdict on O.

## 1. Inputs read

- `~/.omp/agent/RULES.md`; `.ufo/waves/round-79/CLAIMS-DRAFT.md` (O and Ca; "counters grade git-show committed bytes, never moving worktree", line 6); `corpus/QUALITY.md` criteria 9, 17, 19, 23, 25, 28 (criterion 19: evaluation "over committed bytes read from it (`git show <lands>:<path>`)", never a moving worktree).
- `.ufo/waves/round-79/w1/spec.json` (MutPath entry, line 120-124).
- `reports/round-78/telemetry/census-end.txt` (S884 row used for the Ca fixture; not my item, read for path shapes only).
- Committed bytes: `git show 44f76d4:reports/round-74/accept-ca.py` (blob `bb69fb04f5971a8d5c2d9da7b4a3f9afc65d9b12`, sha256 `8052f1e2…a8470f`). Relevant regions: `_inside_clone` 576-581, `_exists_in` 584-589, `_resolve_in` 592-594, `_git_rev_problem` 608-617, `_mutable_ref` 620-626, `_pathspec_ok` 629-634, `_git_problem` 637-672, `_git_grep_problem` 675-719, `_grep_problem` 751-783, `observe_problem` 798-818, allowlists 166-176, `run_observe` 838-866 (env 841-850; zero mapping 860-864).
- Lane: `git cat-file -t 4b255745…^{commit}` = commit (the round-78 pin); `refs/replace` empty at base; no `corpus/knowledge` `.md` deeper than one partition directory (253 files at base).

## 2. Findings (ranked)

**F1 — HIGH — option pass-through allows write and code execution.** `_git_problem` and `_git_grep_problem` skip every token that starts with `-` (accept-ca.py:655-657, 683-693). The global-option refusal (641-643) is an exact-token tuple match, so `--git-dir=…` and attached `-C…`/`-c…` pass.
- `git show --output=<file> <rev>:<path>` writes a file: a blob read created an empty file, and a commit show wrote 1890 bytes (git-level receipts **F1**, **F1b**). Guard: K7 ACCEPT (static).
- `git grep --open-files-in-pager=<cmd>` and `-O<cmd>` **execute `<cmd>`** in the no-revision worktree form. The marker file gained `ran corpus/SOURCES.md` for each (receipts **F2b**, **F2c**; the F2 rev form is refused by git, rc 128). Guard: K8, K9 ACCEPT (static; not re-executed here).
- Attached/`=` global options: K25 `--git-dir=…`, K31 `-C/etc`, K32 `-ccore.pager=…`, K33 `--exec-path=…` all ACCEPT (static). K24 (`-C` as a separate token) is refused.
- Fix: a per-subcommand option allowlist. Match `=` and attached short forms. Refuse `-C`, `-c`, `-O`, `--output`, `--open-files-in-pager`, `--git-dir`, `--work-tree`, `--exec-path`, `--namespace` in every form.

**F2 — HIGH — mutable reads are accepted.** Shows that the guard is not a committed-bytes reader.
- Empty rev `:path` reads the **index** (git **D3**, **D4**, **D13**): guard K4, K17 ACCEPT with observed `staged`.
- Named refs in `show` are accepted (`main:path`, K6 observed `changed`). `_mutable_ref` (620-626) is consulted only by grep and diff. Git-level **A5** shows `HEAD:path` moves per commit.
- `HEAD` is allowed on purpose by `REV_NAMES` (605). K5 is graded GAP against the draft's "refuses mutable revisions"; the design choice needs an explicit decision.
- Two revision operands (`grep -c X <C1> HEAD -- p`, git **E17**) are accepted (K19). The regex reads one capture group; the second observation is silently ignored.
- The generic operand loop (655-671) returns `None` for any non-hex name (`_git_rev_problem` 616-617), so only grep checks names.

**F3 — HIGH — rc 1 becomes a zero, and the path set is not checked against the revision.** `run_observe` maps empty stdout with rc 1 to the observation `"0"` for `git grep -c` (860-864). Git gives rc 1 for a missing or unmatched pathspec with no message (git **E8**, **E16**), so rc alone cannot tell absent from zero. Existence is checked against the worktree of the clone, not the tree at the revision (`_exists_in` 584-589, `os.path.exists`), and every `:`-prefixed or glob token is exempt (`_pathspec_ok` 629-634).
- K11 `:/etc/passwd` → observed `0`.
- K12 `corpus/nothing/*.md` → observed `0`.
- K13 `corpus/worktree-only.md` (exists only in the clone worktree, absent at C1) → observed `0`. This is a false zero, and it reproduces the lands-versus-base confusion that criterion 19 forbids.
- Fix: check each path set against `git ls-tree -r --name-only <rev> -- <path>` (committed tree). Refuse magic and glob tokens unless the counter freezes them as literal lists. Treat rc 1 as zero only when the expanded set is non-empty at the revision. Anything else is an error.

**F4 — HIGH — worktree reads and a symlink escape.** `cat`, `head`, `tail`, `grep`, `wc`, `sha256sum`, `ls`, `cut` are on `OBSERVE_ALLOW` (166-167), and `_grep_problem` reads the clone worktree.
- K21 `cat corpus/SOURCES.md` → observed `worktree`. K22 `grep -c S001 corpus/SOURCES.md` → observed `1`. Both break "committed bytes, never moving worktree" (CLAIMS-DRAFT line 6).
- K34: a worktree symlink `corpus/link-ext` pointing to a file **outside** the repo. `_inside_clone` (576-581) is lexical `normpath`, and `os.path.exists` follows the link. Observed `1`, which is a count from `$SCR/work2/outside-secret.txt`. This is a path-traversal escape through the worktree.
- Fix: drop the worktree-reading binaries from the committed-bytes channel. If any stays, use `realpath` containment and refuse symlinks.

**F5 — MEDIUM — non-blob objects are accepted.** `git show <rev>:<tree>` exits 0 with a listing (git **B14**, **B18**; guard K29 ACCEPT, observed `tree …/inner.md`). The gitlink case is rc 128 (**B16**). `git show <rev>` with a path and no colon prints the HEAD commit and its diff (**C8**, **D8**), which is not blob content. `cat-file blob` on a tree is rc 128 (**B15**).
- Fix: require `git cat-file -t <rev>:<path>` == `blob`, then read with `git cat-file blob`, never `git show`.

**F6 — MEDIUM — replace refs change committed bytes.** With a `refs/replace` entry in the clone, `git show` and `cat-file blob` return the replacement (git **H1**, **H2**, observed `S999`). `grep` honours it too (**H4**, rc 1 for S001). `--no-replace-objects` restores the bytes (**H3**). `run_observe` does not set `GIT_NO_REPLACE_OBJECTS`, and it does not set `GIT_CONFIG_GLOBAL` (841-850), so user global config leaks in. The lane has no replace refs at base (**L4**). Whether `git clone` transfers `refs/replace` was not tested.
- Fix: set `GIT_NO_REPLACE_OBJECTS=1` and `GIT_CONFIG_GLOBAL=/dev/null` in the run environment, and refuse when `git for-each-ref refs/replace` is non-empty.

**F7 — LOW-MEDIUM — the traversal fix holds, but only by accident.** `rev:../x`, `rev:/x`, `corpus/../x`, `rev:corpus//x` and trailing slashes are all refused by git (**B1–B7**, **C1–C3**, **E12**, **E13**). The guard catches the plain forms through `cat-file -e` (K2, K3, K26, K27). A magic-prefixed traversal, `:../../etc/passwd` (K35), is accepted statically because of the `:` exemption, and git then fails closed (rc 128 → `None`, not a zero). Fix: refuse `..`, leading `/` and empty segments in every path form, magic included.
- `git -C corpus show <rev>:../corpus/SOURCES.md` succeeds (**B9**), so `..` is relative to the working directory. The guard is safe only while `-C` is refused in every form (F1).

**F8 — LOW — ambiguity facts the fixture must pin (not defects in themselves).**
- Colon in a legal filename works at a revision (**D1**, **D10**; K15 ACCEPT). A splitter that cuts at the first colon breaks it (**D5**: `cat-file -e corpus/a:b.md` → rc 128, "invalid object name 'corpus/a'"). Rule: `(hex40):(path)` split on the first colon only, with a non-empty 40-hex rev.
- A 40-hex branch named like the commit does not shadow it (**F8**, **F9**: the object wins, with a stderr warning). A stderr warning must not be read as failure.
- git accepts uppercase 40-hex (**F6**) and 7-char short revs (**F7**). The guard should refuse both by regex. `re.match(r"[0-9a-f]{40}$")` accepts `C1\n` (PY block in r2), while git rejects the newline (**F5**). Use `re.fullmatch`.
- Plain pathspec wildcards cross `/` (**E4**, **E6**: `corpus/knowledge/*/*.md` and `corpus/*.md` recurse). `:(glob)` does not (**E5**). The round-74 ledger rederives `git diff --shortstat … -- 'corpus/knowledge/*/*.md'` at `reports/round-74/ledger.json:292-293`, with a "one level deep" comment. That comment does not describe git's recursion. The lane has no such nested file at base (census 0), so there is no numeric effect today.

**F9 — INFO — textconv does not apply to these readers.** `git show <rev>:path`, `--no-textconv` and `cat-file blob` return identical raw bytes with `diff.tc.textconv` set and `*.md diff=tc` committed (**G1–G3**). Not probed: `git diff --shortstat` and `git grep --textconv`.

## 3. Fixture table (red-before for the O guard)

Each argv runs through the committed guard's `observe_problem(argv, clone)` and, if accepted, `run_observe`. Receipt `receipts/committed-h2-probe-raw-r4.txt`; expected verdicts are mine. "static" means the static guard's verdict; "observed" means the dynamic value.

| id | argv (abridged; `C1` = pinned rev) | expect | committed guard | grade |
|---|---|---|---|---|
| K1 | `show C1:corpus/SOURCES.md` | ACCEPT | ACCEPT, committed bytes | MATCH |
| K2 | `show C1:../SOURCES.md` | REFUSE | REFUSE | MATCH |
| K3 | `show C1:/etc/passwd` | REFUSE | REFUSE | MATCH |
| K4 | `show :corpus/SOURCES.md` | REFUSE | ACCEPT, observed `staged` (index) | GAP |
| K5 | `show HEAD:corpus/SOURCES.md` | REFUSE | ACCEPT, observed `changed` | GAP (design) |
| K6 | `show main:corpus/SOURCES.md` | REFUSE | ACCEPT, observed `changed` | GAP |
| K7 | `show --output=W/k7 C1:…` | REFUSE | ACCEPT (static) | GAP |
| K8 | `grep --open-files-in-pager=W/pager.sh -c S001 -- corpus/SOURCES.md` | REFUSE | ACCEPT (static); executes (F2b) | GAP |
| K9 | `grep -OW/pager.sh -c S001 -- corpus/SOURCES.md` | REFUSE | ACCEPT (static); executes (F2c) | GAP |
| K10 | `grep -c S001 C1 -- :!corpus/SOURCES.md` | REVIEW | ACCEPT, 5 lines | REVIEW |
| K11 | `grep -c S001 C1 -- :/etc/passwd` | REFUSE | ACCEPT, observed `0` | GAP |
| K12 | `grep -c S001 C1 -- corpus/nothing/*.md` | REFUSE | ACCEPT, observed `0` | GAP |
| K13 | `grep -c S001 C1 -- corpus/worktree-only.md` | REFUSE | ACCEPT, observed `0` (false zero) | GAP |
| K14 | `grep -c S001 C1 -- corpus/nope.md` | REFUSE | REFUSE | MATCH |
| K15 | `show C1:corpus/a:b.md` | ACCEPT | ACCEPT | MATCH |
| K16 | `show C1:corpus/a:b.md:x` | REFUSE | REFUSE | MATCH |
| K17 | `show :corpus/a:b.md` | REFUSE | ACCEPT, observed index | GAP |
| K18 | `grep -c S001 "" -- corpus/SOURCES.md` | REFUSE | REFUSE | MATCH |
| K19 | `grep -c S001 C1 HEAD -- corpus/SOURCES.md` | REFUSE | ACCEPT, two lines | GAP |
| K20 | `grep -c S001 main -- corpus/SOURCES.md` | REFUSE | REFUSE | MATCH |
| K21 | `cat corpus/SOURCES.md` | REFUSE | ACCEPT, observed `worktree` | GAP |
| K22 | `grep -c S001 corpus/SOURCES.md` | REFUSE | ACCEPT, observed `1` | GAP |
| K23 | `show "C1\n:corpus/SOURCES.md"` | REFUSE | REFUSE | MATCH |
| K24 | `-C /etc show C1:…` | REFUSE | REFUSE | MATCH |
| K25 | `--git-dir=/etc/x/.git show C1:…` | REFUSE | ACCEPT (static); git rc 128 | GAP |
| K26 | `cat-file -e C1:../../etc/passwd` | REFUSE | REFUSE | MATCH |
| K27 | `show C1:corpus/SOURCES.md/` | REFUSE | REFUSE | MATCH |
| K28 | `show C1:corpus/link-abs` | REVIEW | ACCEPT, observed `/etc/passwd` (link text) | REVIEW |
| K29 | `show C1:corpus/sub` | REFUSE | ACCEPT, observed tree listing | GAP |
| K30 | `grep -c S001 C1 -- corpus/*.md` | REVIEW | ACCEPT, recursive set | REVIEW |
| K31 | `-C/etc show C1:…` | REFUSE | ACCEPT (static) | GAP |
| K32 | `-ccore.pager=W/pager.sh show C1:…` | REFUSE | ACCEPT (static) | GAP |
| K33 | `--exec-path=W show C1:…` | REFUSE | ACCEPT (static) | GAP |
| K34 | `grep -c SECRET corpus/link-ext` (worktree symlink → outside file) | REFUSE | ACCEPT, observed `1` | GAP |
| K35 | `grep -c S001 C1 -- :../../etc/passwd` | REFUSE | ACCEPT (static); git rc 128 | GAP (fails closed) |

Totals: MATCH 12, GAP 20, REVIEW 3 (35 cases). Eight GAPs are static acceptances that are either never executed here (K7–K9, K31–K33) or fail closed at run time (K25, K35, rc 128). The other twelve GAPs (K4, K5, K6, K11, K12, K13, K17, K19, K21, K22, K29, K34) produce an accepted observation, several of them wrong or unsafe.

Fixture repository (git-level, `receipts/mutpath-probe-raw.txt` and `-r2.txt`; about 90 probes): the committed-blob baseline (A1–A5), traversal (B1–B21), absolute (C1–C8), colon and index (D1–D13), pathspec (E1–E18), options and exec (F1–F9, F1b, F2b, F2c), textconv (G1–G3), replace (H1–H5), lane read-only (L1–L6). `mutpath_probe.py` asserts the fixture toplevel before every write and refuses any `--work` outside the MutPath scratch root.

## 4. Recommendation for O (for L1 integration)

These are rules a new guard can be tested against, not an implementation:
1. Rev operand: `re.fullmatch(r"([0-9a-f]{40}):(.+)")` on the whole token. The rev must be a 40-hex lowercase, and `HEAD`, named refs, empty rev and a second rev operand are refused (F2).
2. Path operand: no leading `/`, no `..`, no empty segment, no trailing `/`, no magic prefix. For a blob read, `cat-file -t` must say `blob`, then `cat-file blob` with `GIT_NO_REPLACE_OBJECTS=1` (F5, F6, F7).
3. Pathspecs: refuse magic and glob tokens unless frozen literal. Check existence against `git ls-tree -r --name-only <rev>` (F3).
4. Options: per-subcommand allowlist, prefix-matched on `=` and attached short forms. Refuse the list in F1.
5. Binaries: drop `cat`, `head`, `tail`, `grep`, `wc`, `sha256sum`, `ls`, `cut` from the committed-bytes channel, or require realpath containment with symlinks refused (F4).
6. Zero: `rc 1` is a zero observation only when the expanded path set is non-empty at the revision and the output is empty. `rc ≥ 2` is an error. Never map `rc 1` to zero for an unchecked path (F3).
7. Acceptance: the 35 fixtures above are red-before. Each REFUSE must be refused, each ACCEPT accepted, graded by `git show`/`cat-file` of committed bytes at the pinned revision (QUALITY 19, 23).

## 5. Limits and unrun checks

- Not implemented or tested: the O guard (base-absent), and any change to the round-74 counter. Results are red-before evidence.
- Static-only cases were never executed (K7–K9, K31–K33). Their execution evidence is the git-level F1, F1b, F2b and F2c receipts.
- Not probed: `git diff --shortstat` with a pathspec and textconv; `GIT_*` environment injection beyond the replace and global-config cases; core.quotePath; Unicode normalization; a clone's transfer of `refs/replace`.
- K5 (`HEAD`) is a design question, graded GAP against the draft's wording, not a defect in the code's intent.
- The receipts were produced by a driver that writes the fixture, so the fixture is reproducible from `REPRODUCE.txt`, not an independent observation of a lane.

## 6. Tools, lane access, scratch

- Installs or updates: **none**. git 2.56.0 (`/usr/bin/git`) and python3 3.14.8 (system) were used as found.
- Lane access was read-only: `git cat-file`, `show`, `ls-tree`, `for-each-ref`, `rev-parse`, and `status --porcelain` (which may refresh the index stat cache, with no content change). Lane HEAD stayed `44f76d4`. The status count was 2 before and after.
- All writes: the stage directory and this report. Fixture repos, clones and the guard copy lived under `/fast/scratch/hyaku/kotodama-r79/MutPath/`, and that directory is removed after the receipts are copied. No commit, push or jj mutation anywhere. No `~/.local/bin` or PATH change. No `task` or subagent dispatch.

Report: .ufo/waves/round-79/w1/MutPath.md (relative to /home/vgpnk/Projects/shokunin/kotodama-shokunin)
