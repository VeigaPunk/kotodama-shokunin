30. **A Ca ledger pair executes as an argv over committed bytes, and its statement sits where the ledger says** — adds to criteria 9, 11, 17, 19, 23, 26, 27 and 29.

Scope: every pair of a frozen claim-Ca `reports/round-<N>/ledger.json`, in both command fields — `observe_cmd` (the observation taken at the ledger's base revision) and `rederive` (the command a correction row re-runs at lands). The criterion binds the ledger blob at its freeze commit; a correction row that later cites a pair is criterion 27's object, not this one's.

(a) **argv, never command text.** Both command fields are argv arrays of non-empty strings. A field given as one shell string (the round-76 `rederive` shape) is refused, because a checker would have to re-tokenize it and every later limb would grade the tokenizer's guess instead of the pair. The executable is in the frozen read-only allowlist {git, grep, wc, sha256sum, ls, cat, head, tail, cut}; interpreters, shells and constant printers (python3, sh, perl, sed, awk, echo, printf, true) are refused in the executable position. A shell metacharacter (`|`, `&`, `;`, `<`, `>`, a backtick, `$(`, a newline) is refused in every element except a named grep pattern operand, which is data because the argv is never shell-parsed.

(b) **`git -C <repo>` leads, and the revision is in rev position.** A `git` command's elements 1–2 are `-C <repo>`, the repository the pair reads (the lane root, or the clone the counter materialized in its place); a `git` argv without them runs only from one working directory and is refused, and a `-C` naming a third repository is refused. A 40-hex revision is an operand *before* the `--` separator — never after it, never as a path, never inside a pattern — and resolves in that repository, so a dead pin is refused rather than observed as empty. Every `git` command naming committed bytes carries at least one revision operand; `<rev>:<path>` is a revision operand plus a path, not one opaque operand.

(c) **The pattern operand is named.** A grep / git-grep pattern is the argument of `-e`/`--regexp`, or the single first bare operand after the options. Only a named pattern operand may carry a metacharacter; a metacharacter anywhere else is refused. A pattern that has leaked into several operands is what a shell tokenizer produces from an unquoted space (`^window: chars=` becomes `^window:` and `chars=`), and the limb that catches it is (b)'s: the fragment is neither a revision nor a path.

(d) **The statement sits where the ledger says.** `stated_at` is `path:line` whose path is inside a frozen per-disposition allowlist — the append-only set for ANNOTATE, the mutable set for REPAIR — and `stated_text` is present on that line of the base tree, not merely somewhere in the file. A site outside the allowlist, a line past the file's end, or a text absent from its line refuses the ledger at build, before the freeze; none of the three is a land-time discovery.

(e) **The observation runs and returns the token.** At Ca-lands the counter executes each pair's exact `observe_cmd` as an argv — no shell, cwd = the clone it materialized — and requires `parse` to return `expected_after`. A non-zero exit, an empty match or a different token leaves the pair unannotated; a pair whose command could not run at the freeze cannot be closed by a correction row that quotes it.

Check (red-before, pre-dispatch) — one command over the ledger blob, printing one `RED <id> <CODE>: …` line per defect and one `PASS <id> …` line per clean pair, exiting 0 only when every pair is clean. It refuses (exit 2, no verdict line) when `--rev` is not a 40-hex commit, when the ledger is not committed at that revision, or when an allowlist is empty — an empty allowlist would pass every site:

```
python3 -B tools/check-ledger-pairs.py --repo <lane> --rev <freeze> \
    --ledger reports/round-<N>/ledger.json \
    --annotate-allow <the round's frozen append-only set, comma-separated> \
    --repair-allow <the round's frozen mutable set, comma-separated>
```

The two allowlists are the round's frozen sets, read from the freeze commit like every other constant
(criteria 25 and 26); round 76's were `LOG.md,SCORECARD.md,corpus/lessons/round-75.md,corpus/QUALITY.md`
for ANNOTATE and `corpus/README.md,SKILL.md,SHONEN.md` for REPAIR (`reports/round-76/claims.json:195-196`).

`--execute` adds limb (e): each pair's argv runs with cwd = `--work`, else `$HYAKU_SCRATCH`, else `$TMPDIR`, and the checker refuses when none is set rather than inventing a system temp dir.

Measured 2026-10-27 at lane base `211f9526800906e0c585d878d265c37e5e090c15` in `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (read-only; no lane byte was edited, no counter was edited). The checker's bytes are the round-77 stage draft `.ufo/waves/round-77/w1/stage/ScribeQuality30/check-ledger-pairs.py` (sha256 `db327b9f90a381a283da6c9f7fe0cbebf87c0200433cd06bda243ec47f1e127b`); it ships with this criterion at `tools/check-ledger-pairs.py`. The green fixture is `.ufo/waves/round-77/w1/stage/ScribeQuality30/fixture-gen.py` (sha256 `5245952344c9cd3bed101effbd711d4f124a051a800a9d3b70555d39946c5bb3`), which plants the same 20 pairs into the grammar and holds one defect per mutant; every mutant below is red against that fixture, which is green first in the same receipt (`LEDGER-PAIRS: PASS pairs=20/20`, exit 0), and the receipts are `stage/ScribeQuality30/receipt-fixture.txt`, `receipt-refusals.txt`, `receipt-execute-limb.txt`, `receipt-r76-ledger.txt`.

| target | exit | output |
|---|---|---|
| `reports/round-76/ledger.json` at lane base `211f952`, 20 pairs, the r76 frozen allowlists | 1 | `LEDGER-PAIRS: FAIL pairs=0/20 red=20 (NO-C=19, REDERIVE-STRING=20, STATED-AT-SET=1, STATED-TEXT-ABSENT=1)`; `RED L76-13 STATED-AT-SET: corpus/knowledge/myth-symbol/narrative-structure-frameworks.md is outside the frozen ANNOTATE allowlist […]`; `RED L76-19 STATED-TEXT-ABSENT: stated_text is not in corpus/lessons/round-75.md at base` |
| fixture `fc5dc79`: the same 20 pairs rewritten into the grammar | 0 | `LEDGER-PAIRS: PASS pairs=20/20` |
| mutant: L76-13's site back to the knowledge entry | 1 | `RED L76-13 STATED-AT-SET: …` (the fixture's one-line stand-in file adds `STATED-TEXT-ABSENT` for the same pair) |
| mutant: L76-19 stated_text `before=999` | 1 | `RED L76-19 STATED-TEXT-ABSENT: stated_text is not in corpus/lessons/round-75.md at base` |
| mutant: L76-19 `rederive` back to the r76 shell string | 1 | `RED L76-19 REDERIVE-STRING: rederive is str, not an argv list (a shell tokenizer would re-split it)` |
| mutant: `-C` dropped from L76-01 | 1 | ``RED L76-01 NO-C: git argv does not begin `git -C <repo>` (it only runs from one working directory)`` |
| mutant: L76-01's revision moved after `--` | 1 | ``RED L76-01 REV-POS: revision b988761fdc5b00cdf06e57194256fd74d9dc1848 sits after `--`, in the path position`` |
| mutant: `python3 -c print('present')` as L76-01's command | 1 | `RED L76-01 EXEC-NOT-ALLOWED: interpreter/constant-printer 'python3'` |
| mutant: L76-19's pattern split at its space (`^window:` + `chars=`) | 1 | `RED L76-19 UNRESOLVED: operand 'chars=' is neither a revision nor a path at base b988761` |
| mutant: revision `ffff…` (dead pin) | 1 | `RED L76-01 DEAD-PIN: revision ffffffffffffffffffffffffffffffffffffffff is not an object of the repository` |
| mutant: `observe_cmd` a shell string | 1 | `RED L76-01 SHELL-STRING: observe_cmd is a shell string, not an argv list` |
| empty `--annotate-allow` | 2 | `LEDGER-PAIRS: REFUSED (--annotate-allow and --repair-allow are required: an empty allowlist would pass every site)` |
| ledger absent at `--rev` | 2 | `LEDGER-PAIRS: REFUSED (no committed ledger at fc5dc79:reports/round-99/ledger.json)` |
| `--rev HEAD` | 2 | `LEDGER-PAIRS: REFUSED (--rev 'HEAD' is not a 40-hex commit)` |

The run limb, on a two-pair fixture ledger (`exec/ledger.json`, same fixture revision):

| target | exit | output |
|---|---|---|
| clean two-pair ledger, `--execute` | 0 | `LEDGER-PAIRS: PASS pairs=2/2` |
| mutant: `expected_after` says `line 4` | 1 | `RED X01 OBSERVE-MISMATCH: observed 'line 3' != expected 'line 4'` |
| mutant: command grep-matches nothing (exit 1) | 1 | `RED X01 EXEC-FAIL: exit=1` |
| `--execute` with no `--work`/`$HYAKU_SCRATCH`/`$TMPDIR` | 2 | `LEDGER-PAIRS: REFUSED (--execute needs --work, $HYAKU_SCRATCH or $TMPDIR; no system temp dir is invented)` |

The defect this criterion exists for, on the real bytes (receipts `receipt-exec.txt`, `receipt-exec2.txt`, `receipt-rederive-split.txt`, `receipt-parser-verdict.txt`):

| probe | exit | output |
|---|---|---|
| r76 `L76-01.observe_cmd` as recorded, run from a scratch cwd | 128 | `fatal: not a git repository (or any parent up to mount point /)` |
| the same argv with `git -C <lane>` first | 0 | `98c486bdb4650ba5b8e651d332910e8ee60ad121:reports/round-75/claims.json:227` |
| `L76-19.rederive`, tokenized by `shlex.split` (the round-76 counter's own tokenizer), run inside the lane | 128 | `fatal: unable to resolve revision: chars=` |
| the same three token lists under the round-76 H2 parser (`observe_problem(…, rederive=True)`) | — | `L76-19`: `git grep path operand 'chars=' does not exist in the clone`; `L76-20`/`L76-21`: `git grep path operand '98c486bd…' does not exist in the clone`; each pair's own `observe_cmd` → `None` (accepted) |
| `L76-19.rederive` as an argv with `-C` first and the pattern whole | 0 | `window: chars=4097 min=4096 pad=400 before=2020 after=2026` |
| round-76 H2 guard on `git -C <lane>` | — | `git -C '/home/vgpnk/Projects/shokunin/kotodama-shokunin' is refused (the counter fixes repo and cwd; only the --fleet-root may be named)` |

Three of the twenty round-76 pairs carry a `rederive` that tokenizes to a different argv than their own `observe_cmd` (L76-19, 8 → 9 tokens; L76-20 and L76-21, 9 → 10 each), and all three splits put a pattern fragment in the revision position; the same pairs' `observe_cmd` arrays pass the same parser unchanged (`pairs=20 rederive_tokenizes_to_same_argv=17 differ=3`, `receipt-rederive-split.txt`). The defect is the string field, not the argv.

Limits, stated: the checker grades shape and site, not truth — a pair can satisfy all five limbs and still observe the wrong artifact (criterion 27's ground), and limb (e) proves only that the command returns the token the ledger already claims. The positional parse is one parser: a pattern written as a second bare operand is read as a path, and a pair cannot override the parse by declaration; `--regexp=<pattern>` (the equals form) is not recognised and is refused as an unresolved operand. `-C` is compared by `realpath`, so a symlinked clone compares equal only where realpath agrees, while a worktree of the same repository at another path is refused on purpose (a pair names one repository). `rederive` may be omitted, and the counter derives it from `observe_cmd`; the limb refuses a string, never an absence. Fleet sites (`fleet:path:line`, an absolute fleet path, `stated_fleet`) are outside the checker, which binds lane sites only. Limb (e) needs a repository holding the ledger's base objects; a dead pin is reported, never repaired. A freeze blob rewritten outside the lane stays invisible (criterion 25's limit holds here). Two clauses of the same routed defect are out of scope and keep their owners: uncommitted telemetry receipts (criteria 17 and 23, plus the round's RECEIPTS leg) and the combined README exemption's line number (claim Ca's COMBINED leg). The round-76 counter's guard is the measured counterpart of limb (b): it refuses `git -C <lane>` and accepts the no-`-C` form, so a ledger written to this criterion needs that guard widened to its own repository, which is a counter revision and not a wording change (criterion 23's recorded-revision rule). Binds from round 77; the round-76 ledger stays red as recorded — it predates the rule — and no earlier ledger is retro-fitted.

Grounded in `corpus/lessons/round-76-verifier-spotcheck.md:123-125` (§5 item 3: "L76-13 stated_at outside the allowlist; L76-19/20/21 rederive strings unexecutable under the frozen argv parser (base revision / `chars=` treated as path operands)"), in the round-76 measured failure `reports/round-76/telemetry/measures-ca.txt` (`LEG FAIL LEDGER — L76-13 ANNOTATE stated_at path … is outside the frozen append-only allowlist; L76-19 stated_text is not found at the specified base lesson line.` and ``LEG FAIL ANNOTATE — three rows unannotated because L76-19/20/21 `rederive` commands are not executable under the frozen argv parser; L76-20/21 treat the base revision as a path operand and L76-19 treats `chars=` as a path operand.``), and in the r76 pair set `reports/round-76/ledger.json` (20 pairs; the 19 git pairs and the one `sha256sum` pair, all 20 carrying a shell-string `rederive`). Drafted by seat ScribeQuality30 in round 77.
