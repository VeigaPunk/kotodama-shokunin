# Claim O guard contract — what accept-o.py grades

This is the compact schema the acceptance counter (`accept-o.py`, seat
ExecOCounter) assumes. It is specified **independently of the guard
implementation**; any `tools/ledger-token-guard.py` bytes at `<lands>` that
satisfy this contract pass. Behaviour is graded only — the counter never
parses the guard's source.

## CLI

```
python3 -B tools/ledger-token-guard.py --ledger PATH --repo PATH \
    --base HEX40 --work DIR [--emit PATH] [--selftest]
```

- `--ledger`, `--repo`, `--base`, `--work` are required for a grading run
  (missing → exit 2). `--base` must be a full 40-hex commit that exists in
  `--repo` (non-hex → exit 2).
- `--work` is an explicit scratch root; the guard must refuse (exit 2) rather
  than invent a temp dir when it cannot write scratch.
- `--selftest` builds its own tiny fixtures under `--work` and ignores the
  other grading flags.

## Ledger JSON grammar

```json
{
  "round": 79, "claim": "O", "base": "<40hex-or-{base}>",
  "pairs": [
    {"id": "A01", "disposition": "ANNOTATE",
     "stated_at": "LOG.md:1",
     "stated_text": "# fixture ledger-token guard observations",
     "stated_parse": "^# (.+)$",
     "observe_cmd": ["git", "-C", ".", "grep", "-c", "-E", "^#",
                     "{base}", "--", "LOG.md"],
     "parse": ":([0-9]+)$",
     "expected_after": "1",
     "observed_at_base": "2",
     "rederive": "git -C . grep -c -E '^#' {base} -- LOG.md"}
  ]
}
```

- `observe_cmd` is an **argv array** (never a shell string).
- The literal substring `{base}` anywhere in an element is replaced with the
  `--base` value before grammar checks and execution. After substitution the
  observation must be **pinned at `--base`**: at least one element equals
  `--base` or starts with `<base>:` (e.g. `git cat-file -s <base>:PATH`,
  `git grep ... <base> -- PATH`). An observation pinned at anything else —
  `HEAD`, a branch, another commit, the worktree — is a refusal.
- `argv[0]` must be `git` (no interpreters: python*, sh, bash, perl, node,
  ruby, …; no constant printers: echo, printf, true, yes). Any shell
  metacharacter (`| & ; < > ` $(` CR LF) in any element is a refusal.
- git subcommand must be read-only: one of `show grep cat-file ls-tree
  rev-parse log diff ls-files rev-list merge-base`.
- `parse` and `stated_parse` are regexes with exactly one capture group;
  observed token = `parse` searched in the observe stdout; stated token =
  `stated_parse` searched in `stated_text`.
- Per-observe timeout (≤ 60 s) and an output cap (≤ 1 MiB) are enforced.

## Exit codes and stable labels

- `0` — `LEDGER-GUARD-79: PASS pairs=N`
- `1` — `LEDGER-GUARD-79: FAIL pairs=N problems=M`, one line per problem:
  - `PAIR <id>: OBS_MISMATCH recorded='<r>' actual='<a>'` (recorded
    `observed_at_base` ≠ the re-run observation)
  - `PAIR <id>: NOT_RED token='<t>'` (stated token == observed token)
  - `PAIR <id>: <unobservable|unparseable …>` (observation failed)
- `2` — `LEDGER-GUARD-79: FAIL (refused: <why>)` for usage errors, unreadable
  ledgers, grammar violations and mutable/unpinned revisions. A refusal is
  never a pair verdict.

`--emit PATH` writes strict JSON the counter compares against its own
independent re-derivation (it does not trust guard stdout prose):

```json
{"verdict": "PASS|FAIL",
 "pairs": [{"id": "A01", "observed": "2", "stated": "fixture …",
            "status": "ok|obs-mismatch|not-red|…"}]}
```

`--selftest` must exit 0 and print one deterministic line starting with
`SELFTEST:` (the committed receipt `reports/round-79/telemetry/
selftest-guard.txt` carries that line under a `# guard sha256:` header).

## What the counter re-derives independently

For every fixture ledger the counter materializes the guarded-object repo
from committed fixture bytes in explicit scratch, then re-derives each pair:
stated token from `stated_parse`, `stated_text` equality against the named
blob line (`git show <base>:<path>`), and the observation by executing the
declared argv with `{base}` substituted. A guard whose `--emit` disagrees
with that re-derivation fails the leg even if its verdict line says PASS.
