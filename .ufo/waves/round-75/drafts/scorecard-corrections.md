# SCORECARD `## Corrections — round 75` — draft rows for the ANNOTATE pairs

Seat ScribeQuality (leaf, wave 1), lane base `f556d1049fe651d3d63975600b13acd9fb686f15`, 2026-10-27.
Source: `reports/round-75/ledger.json` (DRAFT, unfrozen — never edited by this seat). The ledger holds
11 pairs; the five `ANNOTATE` pairs are L75-05, L75-06, L75-08, L75-09, L75-10 and those are the rows
below. The six `REPAIR` pairs carry no row here (L75-01/02/03/04/07/11 are closed by their statements at
`<lands>`).

## Contract these rows must satisfy (round-74 counter, `reports/round-74/accept-ca.py`, inherited by round 75)

| leg | what it does with a row | evidence |
|---|---|---|
| `ANNOTATE` | reads the section between `## Corrections — round <frozen round>` and the next `^## `; `row_starts_with_id` takes the **first cell**; requires `token_in(row, stated_token)` **and** `token_in(row, observed_token)`; then **re-runs the pair's own `rederive`** (`shlex.split` → argv) with cwd in the lane clone at `<lands>` and requires that output to contain the observed token | `:1290-1345`, `:297-330` |
| `NOSTUB` | requires `norm(rederive)` to appear **verbatim (whitespace-normalized) inside the row** plus both tokens, and refuses a `rederive` outside the observe allowlist (`git grep wc sha256sum ls cat head tail cut`), any shell metacharacter (`\| & ; < > \` $(`), and any `git -C`/`git -c`/`--git-dir` (`GIT_GLOBAL_OPTS`) | `:1470-1512`, `:175-176`, `:603-604` |
| count pairs | an `ANNOTATE` pair with a **numeric** `expected_after` must name the frozen **base** revision in its `observe_cmd` | `:1310-1317` |
| `LEDGER` | the pair's `parse` must compile **and carry a capture group** | `:1034-1046` |

`token_in` is boundary-matched (`(?<![0-9A-Za-z_])TOKEN(?![0-9A-Za-z_])`, `:269`), so a token cell must
hold the ledger's own token, never a paraphrase: the observed token is whatever the pair's `parse`
extracts from `observe_cmd`, and each row's `new token` cell below is exactly that string.

## Text to append (after the file's last line; append-only — no base line is touched)

```markdown
## Corrections — round 75

Append-only record (hyaku run 10, L1 KotodamaR75). Claim Ca ledger `reports/round-75/ledger.json`,
frozen with `reports/round-75/claims.json`. Counter: `python3 -B reports/round-75/accept-ca.py --root .
--lands <lands> --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin`. The filed lines named
below stand as filed; each row carries id, old token, new token and the re-derivation command, which the
counter re-runs.

| id | old token | new token | re-derivation command |
|---|---|---|---|
| L75-05 | was absent from the page it was bound to | 1 | git grep -c '非凡特性来自最初造物主' f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-74/evidence/S883.txt |
| L75-06 | was the Sowers-Wills clause, absent from this page | 1 | git grep -c '这个我肯定考虑过' f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-74/evidence/S884.txt |
| L75-08 | see the closing line below | 1 | git grep -c 'see the closing line below' 3a7401609325341eb3fe0efd42d0eec29d06be3c -- .ufo/reports/round-74/kotodama.md |
| L75-09 | FAIL | FAI | git grep -h -o -E 'min-pairs gate [A-Z]+' f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-73/telemetry/selftest-r3.txt |
| L75-10 | 43 of 44 | 44 | git diff --shortstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 f556d1049fe651d3d63975600b13acd9fb686f15 -- ':(glob).ufo/waves/round-74/w2/*.md' |

Notes. L75-05 and L75-06 record the round-74 closure's routed defect R2: the two lesson reject rows
(:37, :38) say the staged rows' spans were absent from the pages they name, while each own anchor occurs
once in that page's round-74 capture; the correction carries the presence count. L75-08 records routed
defect R3 / closure step-1 defect D1: the filed fleet report promises a closing line carrying the pushed
lane hash and no closing line carries one (the report's tail is the stale-lane/misroot lines; its only
40-hex values are the lane's base, freeze and lands). L75-09 records the truncated round-73 selftest
receipt: its sixth line ends `min-pairs gate FAI`, with the next line `SELFTEST OK: 10 scenarios` as the
authoritative scenario count. L75-10 records the historical-as-filed wave-2 count: `43 of 44` at filing,
44 report files at the frozen base (`git ls-tree` on `.ufo/waves/round-74/w2/` lists 44 `.md` files;
the three `drafts/*.md` files are outside that directory's own listing).
```

## Per-row verification (executed read-only in a fresh `--shared` clone of the lane at base)

Each `re-derivation command` was run with cwd inside
`/fast/scratch/hyaku/kotodama-r75/ScribeQuality/lane-clone` — the same context the `ANNOTATE` leg uses.

| id | command output | observed token found | notes |
|---|---|---|---|
| L75-05 | `f556d10…:reports/round-74/evidence/S883.txt:1` | `1` | `git grep -c` on the pair's own URL capture; matches the ledger `rederive` verbatim |
| L75-06 | `f556d10…:reports/round-74/evidence/S884.txt:1` | `1` | as above; matches the ledger `rederive` verbatim |
| L75-08 | `3a74016…:.ufo/reports/round-74/kotodama.md:1` (run in the **fleet** repo) | `1` | **needs the ledger fix below**: the drafted `rederive` begins `git -C /home/vgpnk/Projects/shokunin`, which the guard refuses |
| L75-09 | `min-pairs gate FAI` | `FAI` | **needs the ledger fix below**: the drafted `rederive` is a pipeline and prints `son` |
| L75-10 | ` 44 files changed, 13810 insertions(+)` | `44` | **needs the ledger fix below**: drafted `observe_cmd`/`parse`/`rederive` replaced |

## Blocking ledger fixes (pre-freeze; this seat cannot edit `ledger.json`)

The three `rederive` strings below are the only thing standing between these rows and a passing
`ANNOTATE`: the leg re-runs the **pair's** `rederive`, and `NOSTUB` requires the row's fourth cell to
equal that string modulo whitespace. If the freeze keeps the drafted text, the rows above must be
rewritten to it — and then `ANNOTATE` fails, for the reasons measured.

| pair | drafted (fails) | why measured | replacement |
|---|---|---|---|
| L75-08 | `git -C /home/vgpnk/Projects/shokunin grep -c 'see the closing line below' 3a7401609325341eb3fe0efd42d0eec29d06be3c -- .ufo/reports/round-74/kotodama.md` | `git -C` is in `GIT_GLOBAL_OPTS` → `observe_problem` returns "git option '-C' is refused (the counter fixes repo and cwd)" (`:642-643`); without a fleet root the 40-hex is a dead pin in the lane clone (measured: `git cat-file -e 3a74016…` exits 1 there) | `git grep -c 'see the closing line below' 3a7401609325341eb3fe0efd42d0eec29d06be3c -- .ufo/reports/round-74/kotodama.md`, run against `--fleet-root` |
| L75-09 | `git show f556d10…:reports/round-73/telemetry/selftest-r3.txt \| tail -c 4` | the `\|` is a shell metacharacter (`SHELL_META`, `:175`) → refused as an argv element; and as a shell it prints `son` (the file's last four bytes), not `FAI` | `git grep -h -o -E 'min-pairs gate [A-Z]+' f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-73/telemetry/selftest-r3.txt` |
| L75-10 | `ls .ufo/waves/round-74/w2 \| grep -c '\.md$'` | same `\|` refusal; `ls` cannot return a count, and the drafted `parse` (`\.md$`) has **no capture group** → `LEDGER` refuses the pair outright (`:1034-1046`) | `git diff --shortstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 f556d1049fe651d3d63975600b13acd9fb686f15 -- ':(glob).ufo/waves/round-74/w2/*.md'` |

Companion field changes for L75-10 (the observation itself is wrong today, not just its re-run):
`observe_cmd` = `["git","diff","--shortstat","4b825dc642cb6eb9a060e54bf8d69288fbee4904","f556d1049fe651d3d63975600b13acd9fb686f15","--",":(glob).ufo/waves/round-74/w2/*.md"]`,
`parse` = `([0-9]+) files? changed`, `expected_after` = `"44"` (unchanged). Without `:(glob)` the
pathspec's `*` also matches `w2/drafts/*.md` and the count is **47** (measured); `_pathspec_ok`
accepts the `:(glob)` prefixed operand (`:629-634`) and `_git_rev_problem` exempts the empty tree
(`:608-612`), so the guard passes and the count is 44 at both base and `<lands>`.

For L75-08 the pair also needs the round-74 fleet grammar (`stated_fleet: {path, pin, line, sha256}`,
resolved with `git -C <fleet> show <pin>:<path>`, `:1073-1110`) instead of an absolute `stated_at`, and
the observation must run with the fleet root: `stated_fleet.path` = `.ufo/reports/round-74/kotodama.md`,
`pin` = `3a7401609325341eb3fe0efd42d0eec29d06be3c`, `line` = 20, `sha256` =
`354273bc972d8b86a012a8aac024618d5defa73e72ea1eae5a960fdf64f84107` (measured: 45 lines; line 20 =
"LOG.md round-74 entry … Lane pushed hash: see the closing line below"). One further catch: `ANNOTATE`'s
count-pair rule requires a numeric `expected_after` to pin the **base** revision in `observe_cmd`, and
L75-08's rev is the fleet pin — so either the round-75 counter accepts `ledger.fleet_pin` as the pin for
a `stated_fleet` pair, or `expected_after` for L75-08 must be non-numeric. That is a counter/ledger
decision, not a row decision: the row carries `1` either way.

## Position and safety

- The section is **appended** at the end of `SCORECARD.md`; the claim-Ca `APPENDONLY` leg protects
  `SCORECARD.md` against removed lines only, so an appended section passes and no base byte moves.
- No row begins with a pair id in the `Notes.` paragraph (a second leading-id line would be read as a
  second candidate row by `row_starts_with_id`), and no cell contains an unescaped `|`.
- The five rows name no claim-C id (S885–S892) and no claim-C path, satisfying `SEPARABLE`.
