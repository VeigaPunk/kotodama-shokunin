# Observation execution grammar — SentinelExec (round-79 W1)

Status: DRAFT for L1 integration. Not frozen. Not a verified implementation of the O counter.
Evidence = raw probe receipts in this directory (see `commands.txt`, `SHA256SUMS`).
Base for the observed committed guard: `44f76d456c1b326a71ffdb381590af825cbf11be`,
`reports/round-73/accept-ca.py` (sha256 `222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89`).

## 1. What the committed guard admits (exercised, not inferred)

`argv_problem` (accept-ca.py:313-337) checks only `argv[0]`'s basename against
`{git, grep, find, wc, ls, cat, sha256sum, stat, python3}`, rejects the shell list and four
shell constructs, and for `python3` requires `-c` plus one of `pathlib|open(|subprocess|os.`
and no quoted-literal `print`. `run_observe` (340-365) passes `cwd=clone` and a fresh env
that keeps the parent's `HOME` and `PATH`.

| id | argv (abbrev.) | committed verdict | observed effect (fixture, `probe-observe-v2-raw.txt`) |
|---|---|---|---|
| C01 | `git cat-file -p HEAD:a.txt` | admitted | mutable revision read |
| C04 | `git grep -O needle -- a.txt` | admitted | HOME `core.pager` executed (marker) |
| C05 | `git -c core.pager=… grep -O …` | admitted | argv `-c` accepted; pager script executed (same script as the HOME config, so the marker does not attribute the source; the argv acceptance is the finding) |
| C06 | `git diff REV1..REV2 -- a.txt` | admitted | HOME `diff.external` executed |
| C06b | `git diff --no-ext-diff REV1..REV2` | admitted | HOME `diff.evil.textconv` executed (x2) |
| C02 | `git show REV:a.txt` (attr `diff=evil`) | admitted | no textconv by default; `--textconv` control fires (`textconv-control-raw.txt`) |
| C08 | `git -C <other> cat-file -p OTHER:secret.txt` | admitted | read outside clone |
| C09 | `git --git-dir <other>/.git cat-file …` | admitted | read outside clone |
| C10 | `find . -maxdepth 0 -fprint <outside>` | admitted | file written outside clone |
| C11 | `cat <outside>/secret.txt` | admitted | absolute read outside clone |
| C12b | `python3 -c "import pathlib;print(245)"` | admitted | constant printer prints 245 |
| C13 | `python3 -c "import subprocess;subprocess.run(['sh','-c',…])"` | admitted | shell escape executed |
| C14 | `git cat-file -p 7d8755d:a.txt` | admitted | 7-hex (mutable prefix) read |
| C15 | `git -C <other> update-ref -d refs/heads/victim` | admitted | outside repo branch deleted (fixture) |
| C16 | `git ls-files --others --exclude-standard` | admitted | worktree-only file observed |
| C00 | materialize (clone + checkout) | — | HOME `core.hooksPath` post-checkout executed |
| C12 | `python3 -c "print(245)"` (no decoy token) | refused | the decoy token is the only thing that separates C12 from C12b |

## 2. Draft closed grammar (`observe_grammar.py`)

Every observation is `git` plus one of five plumbing forms. No other binary. No global options.

| form | exact argv shape | notes |
|---|---|---|
| cat-file | `git cat-file -p\|-s\|-t <40hex>[:<path>]` or `git cat-file blob <40hex>:<path>` | no `--textconv`/`--filters` |
| ls-tree | `git ls-tree -r --name-only <40hex> -- <path>` | tree listing at a pinned commit |
| grep | `git grep [flags] <pattern> <40hex> -- <path>` | flags ⊆ `-n -c -l -o -h -H -E -F -i -w -x`, each at most once; pattern must not start with `-` |
| rev-parse | `git rev-parse --verify --quiet <40hex>^{tree\|commit}` | |
| rev-list | `git rev-list --count <40hex>` | |

Refused at `check_argv` (before any process starts): `argv[0] != "git"`; subcommand outside the
table (this refuses `-c`, `-C`, `--git-dir`, `--work-tree`, `--exec-path`, `--paginate`,
`--namespace`, `--config-env` and every `show`, `diff`, `log`, `checkout`, `clean`, `update-ref`,
`ls-files`); any flag outside the per-form whitelist (refuses `-O`, `--open-files-in-pager`,
`--textconv`, `--ext-diff`, `--output`); revisions that are not lowercase 40-hex (refuses
`HEAD`, branch and ref names, abbreviations, uppercase hex, `^{tree}` on a symbolic name);
paths that are absolute, start with `-`, contain `..`, `:`, or any control character; repeated
flags; wrong positional shape.

Verified verdicts: `probe-draft-raw.txt` (31 cases, 0 mismatches against declared expectations),
`edge-draft-raw.txt` (15 shape edge cases; the newline-in-path gap E6 was found and closed in
this round and the probe rerun on the final file).

## 3. Scrubbed environment (`scrubbed_env`)

Replaces the environment (does not extend it): `GIT_CONFIG_GLOBAL=/dev/null` and
`GIT_CONFIG_NOSYSTEM=1` remove the operator's global config (pager, diff.external, textconv,
core.hooksPath, fsmonitor); `HOME` and `XDG_CONFIG_HOME` point at an empty scratch dir;
`GIT_PAGER=cat`, `PAGER=cat`, `GIT_TERMINAL_PROMPT=0`, `GIT_OPTIONAL_LOCKS=0`. Parent `GIT_DIR`,
`GIT_WORK_TREE` and `GIT_CONFIG*` are not inherited. Requires git >= 2.32 (fail closed otherwise).

Controls (`probe-draft-raw.txt`): with the scrubbed env and a hostile HOME, raw `git diff`
(ext-diff on), `git diff --no-ext-diff` and `git grep -O` produce no markers (E01-E03).
The same three under the hostile HOME without the scrub fire the external diff, the textconv
driver (twice) and the pager (H01-H03). The config-off defence therefore works alone, without
relying on the grammar refusing `diff`/`grep -O`. `materialize` under the scrubbed env fires no
hook (`MATERIALIZE_MARKERS []`), while the committed `materialize` fires `post-checkout` (C00).

## 4. Required changes to reach the grammar (migration, not a silent tightening)

The committed round-73 ledger (`reports/round-73/ledger.json` at base, 8 pairs) uses forms the
draft refuses. Each needs a rewrite before any O ledger is frozen:

| pair | committed observe_cmd shape | closed-grammar replacement | gap |
|---|---|---|---|
| L01-L03 | `python3 -c "…subprocess.run(['git','ls-tree',…]) …len(...)"` | `git ls-tree -r --name-only <40hex> -- corpus/knowledge` + a **count** parse | needs a count mode (see §5) |
| L04-L06 | `grep -n -E '^## Error patterns$' SKILL.md` | `git grep -n -E '^## Error patterns$' <40hex> -- SKILL.md` | none |
| L07 | `python3 -c "…json.load(open(...reports/round-72/claims.json))…"` | `git cat-file -p <40hex>:reports/round-72/claims.json` + grep for the id line | needs the id list as a count/grep, not json |
| L08 | `python3 -c "…pathlib.Path('reports').glob('round-*/accept-*.py')…max…"` | not expressible: `max` over round numbers | needs either a pinned constant with a count of matching paths, or a pinned tool under QUALITY 28 |

## 5. Gaps the grammar does not close (stated, not hidden)

- **Count mode is not in the draft.** `observe_grammar.py` returns stdout only. The ledger
  convention "observed = number of stdout lines matching `parse`" must be specified and frozen
  before L01-L03 and the README-count pairs can be expressed. Not implemented here.
- **No `max`/aggregation.** L08 is not expressible without a pinned tool (QUALITY 28) or
  constant pinning. L1 decides.
- **Parse regex** (`re.search` on stdout) is still a text match; it cannot distinguish a
  derived value from a literal line that happens to match. The O counter's own checks are the
  control: `observed_at_base` must equal a fresh observation, and `stated_token` must differ.
- **Revision width.** Only 40-hex (SHA-1) revisions are admitted. A SHA-256 repository fails
  closed.
- **Git version.** Probed on git 2.56.0 only. The `GIT_CONFIG_GLOBAL` floor (2.32) is stated, not
  probed on an older git.
- **Output bounds.** 1 MiB stdout cap and 120 s timeout are stated defaults; the cap refuses,
  it does not truncate.
- **Pattern beginning with `-`** cannot be expressed in the grep form (refused). Intentional.
- **Tree listing via cat-file -p `<rev>:<dir>`** is admitted and prints the tree; this is
  read-only and harmless, noted for completeness.

## 6. Residual defects in the committed counter (same class, found while probing)

- **Dead outside-clone check.** `run_observe` sets `RUN_STATE["outside_clone"]` only when
  `cwd_is_clone=False`; the single call site (accept-ca.py:373) uses the default `True`. The
  STAMP-leg check at :855 therefore cannot fire. Verified by `grep -n run_observe(`.
- **Counter materialize and legs run operator config.** `materialize` (292-310) and the counter's
  own `git diff` calls at :260, :272, :283 inherit `os.environ`, so the HOME config (hooks,
  diff.external, textconv) executes during grading. The materialize hook was executed (C00); the
  diff calls share the command shape of C06/C06b, which executed the driver. The exact :260/:272/:283
  calls were not run in isolation. [INFERENCE for those three call sites.]
- **`--selftest` env** (accept-ca.py:994-999) does set `GIT_CONFIG_GLOBAL=/dev/null`, but the
  observe path (`run_observe`, :344-353) does not. The selftest and the observe path therefore
  run under different config.
