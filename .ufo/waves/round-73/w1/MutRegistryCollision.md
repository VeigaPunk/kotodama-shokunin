# MutRegistryCollision — mutation test of the CORPUS item-10 id-collision guard

Seat: `MutRegistryCollision` (kotodama round 73, hyaku run 7, leaf mutation-tester). Date: 2026-10-25.
Target invariant (claims.json claim C, COLLCHECK leg): *"collisions file (0-3-space-indent guard, proved on a planted indented collision first) has zero id tokens for the adopted ids"* — the guard is the pair `grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'` over the lane registry and the staged append, intersected with `comm -12` (dispatch wording to ExecRenumber; build artifact `.ufo/waves/round-73/assimilation/guard-proof/run-guard-proof.sh:12-13,95-97`).

## Instruments (the bounded behavioral detector, run identically on pristine / mutated / restored bytes)

```sh
GUARD='^ {0,3}\|[[:space:]]*S[0-9]{3,}'
grep -oE "$GUARD" "$REG"     | grep -oE 'S[0-9]+' | sort   # reg-ids
grep -oE "$GUARD" "$STAGED"  | grep -oE 'S[0-9]+' | sort   # staged-ids
comm -12 REGIDS STAGEDIDS                                 # collisions
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file <registry copy>
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh census   --file <registry copy>   # row count
```

Census comparisons ran twice: on the bare fixture (registry copy alone — pass 1) and in a corpus-mirror layout `M/corpus/SOURCES.md` with `cp -r` of the lane's 13M `corpus/` (pass 2), so used-by paths resolve. Fixture: `D=$(mktemp -d)` → `/tmp/tmp.zZVIBmw2As`, `git -C "$D" init -q` (no commits); registry copy = byte-identical `cp` of lane `corpus/SOURCES.md` (`cmp` verified), staged copy = `cp` of `/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md`. No tools were installed (bash/gawk/coreutils only). No downloads. All writes stayed in `/tmp/MutRegistryCollision/` and the fixture; the lane was touched only at the assigned report path.

## Baseline (pristine bytes)

- pristine registry sha256 `31a5739c83ad5737…824d8` (== lane bytes); staged sha256 `7fb4f488807e8364…3754`.
- Guard pair: reg-ids=799, staged-ids=132, collisions=17 — tokens `S859 S860 S861 S862 S863 S864 S865 S866 S867 S868 S869 S870 S871 S872 S873 S874 S875` (contiguous staged-namespace ids whose numbers coincide with unrelated lane documents). Reproduces the sibling receipt `assimilation/guard-proof/guard-proof.txt` §4 exactly (799/132/17; their col0 control also 17). Non-empty by design: the acceptance predicate is zero tokens for the **adopted** ids (S876+), not an empty file.
- Census on pristine: `rows=799`; validate findings are environment-only in my fixtures (bare: 729×E11 used-by missing — no `corpus/` on disk; mirror: 2×E11 `S859/S860 missing used-by SKILL.md` because the mirror lacks the lane-root `SKILL.md`). These constants are identical on every fixture, so the line-level codes below are the signal; the lane-environment exit 0 / 799 rows stands on the committed receipt `reports/round-73/telemetry/census-start.txt` and guard-proof §1.

## Mutation results — planted row `| S881 | Planted guard fixture (Enguehard 2022, ojs.unito.it article 7099) — … | paper | B | … | queued | 2026-10-25 | 90d | — |` inserted once inside `## Registry` (before `## Paths`, after the S875 row)

S881 is a staged id (staged S881 = the unito 7099 article), so the plant collides cross-file against `staged-ids` and not in-file (registry max is S875).

| mutant | planted bytes (lead-in) | guard pair (collisions / S881 token) | census `--file` reg copy (rows / findings) | verdict |
|---|---|---|---|---|
| m1 | `  \| S881 \|` 2 spaces | **18 / S881 present — killed** | rows 800 (row parsed); 0 E-findings, no E03 — census blind | caught by guard pair only |
| m2 | `   \| S881 \|` 3 spaces | **18 / S881 present — killed** | rows 800; 0 E-findings — blind | caught by guard pair only |
| m3 | `    \| S881 \|` 4 spaces | 17 / S881 absent — missed | rows **799** (line skipped as indented code); silent | **survives both** — by design |
| m4 | `\|S881\|` no spaces | **18 / S881 present — killed** | rows 800 (id parses via `trim($2)`); 0 E-findings — blind | caught by guard pair only |
| m5 | `\t\| S881 \|` tab | 17 / S881 absent — missed | rows **799** (skipped); silent | **survives both** — by design |
| m6 | `\| s881 \|` lowercase | 17 / S881 absent — missed | rows **800** (parsed); `E02 s881`; exit 1 | guard-missed; census catches it **as malformed, not as a duplicate** |

Census reg-copy semantics confirmed: `E03` never fires for any mutant here because the duplicate lives in the *other* file — `--file` validates one file (`seen[]` is per-run). In-file control (not a planted spec mutant, a sanity probe): two normalized S881 rows (column zero + 2-space) in one copy → `E03 S881 duplicate id`, exit 1. So census-E03 and the guard pair cover disjoint classes: in-file (post-adoption) vs registry×staged (pre-adoption). Claim C correctly requires both (COLLCHECK + SCRATCHMIRROR); dropping either reopens its class.

m3/m5 survival is the documented scope, not a guard defect: the census parser note (CORPUS.md, "Maintained parser note"; `sources-census.sh:40-42`) accepts 0–3 leading ASCII spaces, 4+ = indented code; a leading tab counts as 4 spaces under CommonMark. Both instruments agree with the markdown row notion; the plant is not a registry row. Recorded as the guard's scope statement: the pair protects exactly the rows the parser would count.

## Guard-pattern mutants (pattern swapped into the same pair, same fixtures)

| guard mutant | pattern | kills | survives on | verdict |
|---|---|---|---|---|
| column-zero-only (= the frozen CORPUS.md manual-census awk pattern) | `^\|[[:space:]]*S[0-9]{3,}` | m4 | **m1, m2** (17 collisions, S881 invisible) + m3/m5/m6 | SURVIVOR — this is exactly the drift item-10's `^ {0,3}` widening fixes; the frozen manual block still carries it (acknowledged by the maintained-parser note) |
| 0-1 spaces | `^ {0,1}\|[[:space:]]*S[0-9]{3,}` | m4 | **m1, m2** + m3/m5/m6 | SURVIVOR — under-indented bound |
| no `S` anchor | `^ {0,3}\|[[:space:]]*[0-9]{3,}` | nothing | **everything, including the baseline**: reg-ids=0, staged-ids=0, collisions=0 on all 7 fixtures | SURVIVOR — false-clean instrument; the `S` anchor is load-bearing |

## Staged-rows observation (measured, bears on claim C ROWS)

`awk -F'|'` NF histogram over the 132 staged rows: 7×13, 115×14, 9×15, 1×16 — 125/132 are E01 to the census parser (escaped `\|` inside recheck cells split as fields). Consequences, both exercised: (a) a naive concat fixture (registry + staged body under `## Registry`) yields 125×E01, 7×E09, 877×E11 and **zero E03** even though 17 ids collide — E01 rows `next` before the `seen[]` check, so census-E03 can never surface as-is staged duplicates; the guard pair is the only pre-adoption instrument. (b) This independently corroborates the ROWS leg "no row is the staged text appended as-is": normalization (de-escaping, renumber) is what makes the rows census-legal at all.

## Restoration evidence

After every mutant run the registry copy was restored from the pristine copy and hash-compared: pass 1 logged `RESTORED: reg.md == pristine (31a5739c83ad5737…)` for all six mutants; mutant-file sha256s recorded before restore (m1 `e2703321…`, m2 `30940726…`, m3 `ff83d774…`, m4 `c58630c9…`, m5 `2e0bd39c…`, m6 `1165f070…`). Pass 2 ended with `cmp`-verified mirror restoration (`mirror SOURCES.md restored == lane bytes`). Fixture kept at `/tmp/tmp.zZVIBmw2As` (tasking-declared scratch); raw logs `/tmp/MutRegistryCollision/results-final.txt` and `pass2.txt`.

## The exact guard command pair the L1 should run

```sh
A=/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-73/assimilation
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md | grep -oE 'S[0-9]+' | sort > "$A/reg-ids"
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' /home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md  | grep -oE 'S[0-9]+' | sort > "$A/staged-ids"
comm -12 "$A/reg-ids" "$A/staged-ids" > "$A/collisions"
```

Acceptance predicate (as claimed): `grep -E '^S(876|877|878|879|880)$' "$A/collisions"` is empty — the file itself is non-empty today by design (17 tokens, S859–S875). Pair it with `sources-census.sh validate --file` on the mirrored corpus (in-file E03 leg); neither substitutes for the other. Guard mutants that would silently survive: column-zero-only, 0-1-space, and any variant dropping the `S` anchor.

## Bounds

One mutant at a time; single planted row shape (well-formed 11 cells, so E01 cannot mask detection); m3/m5 verdicts are scope statements grounded in the documented parser rule and measured row counts, not defects found; census exit codes in my fixtures carry the constant environment noise described above — line-level codes are the reported signal. Verdict on the guard as written: **killed on its declared class** (0–3-space, column-optional, uppercase-S rows, cross-file), with the survivors tabled above.
