# RevAppendOnly — round 72, w1 — APPENDONLY check design + trial (claim Ca leg 10)

Seat: L1Kotodama72.RevAppendOnly (leaf; no delegation, no installs — git/awk/coreutils only; pacman untouched per host pause).
Scope: design and trial the leg-10 check, attack the coverage of its file set. Frozen claims: `reports/round-72/claims.json` (read first; leg 10 = `Ca.legs[9]` APPENDONLY).

## The check (exact commands)

Frozen-literal leg under test:

```
git diff -U0 b60c7b1..<lands> -- LOG.md corpus/lessons/round-71.md corpus/QUALITY.md
```

Accept iff zero content `-` lines. In unified diff the only `-` lines that are not content are the per-file removal headers `--- a/<path>` (default `a/`/`b/` prefixes; these three files are tracked at base, so no `--- /dev/null` header is possible). Counter used (scripts at `/tmp/RevAppendOnly/check.sh`):

```
git diff -U0 "$BASE..$LANDS" -- LOG.md corpus/lessons/round-71.md corpus/QUALITY.md \
  | awk '/^--- [ab]\//{next} /^-/{c++} END{print c+0}'          # content '-' lines
git diff --numstat --no-renames "$BASE..$LANDS" -- <same paths> \
  | awk '{s+=$2} END{print s+0}'                                 # independent deletions crosscheck
```

Header-discrimination rule: exclude exactly `^--- a/` and `^--- b/`; count every other `^-` line. numstat deletions is authoritative on disagreement — it has no header-ambiguity class at all (a removed filed line shaped `--- a/…` is indistinguishable from a header in the patch form; numstat resolves it).

## Results

1. Trivial (lane repo, HEAD == b60c7b1), `b60c7b1..b60c7b1`: empty diff → `content-minus=0`, `numstat-deletions=0` → **ACCEPT, exit 0**.
2. Fixture, pure appends (repo v1 `/tmp/RevAppendOnly/repo`, base = exact `git show b60c7b1:` bytes of the three files; appended a round-72 block to each): `6f16e6d5` → **ACCEPT** (`content-minus=0 numstat-deletions=0`). Reproduced on fixture v2 with a planted `--- `-prefixed filed line at base: `4a2985fb` → **ACCEPT**.
3. Fixture, one line edited in place (v1: QUALITY.md title `admission bar`→`admission gate`; v2 rerun `428f6761`): diff shows `-# corpus/QUALITY.md — the admission bar` → **REJECT** (`content-minus=1 numstat-deletions=1`, exit 1).

Check accepts pure appends and rejects a single in-place rewrite, as required.

## Findings by severity

**HIGH — shipped draft counter's APPENDONLY filter has a false-negative class.**
`/.ufo/waves/round-72/counters/accept-ca.py` leg 10 counts `line.startswith("-") and not line.startswith("---")`. Any removed filed line whose text begins with `--` (diff line begins `---`) is silently excluded. Demonstrated (fixture v2, `05a2597e`, only removals are two filed lines):

```
--- a/LOG.md
---include='*.md' | awk -F: '{s+=$2} END {print s}'` = 1258 provenance   <- filed byte removed
--- a/corpus/QUALITY.md
--- a/corpus/lessons/round-71.md
---- provisional note filed at base                                       <- filed byte removed
```

Precise filter: `removed-count=2` → REJECT. Draft filter: `removed-count=0` → **PASS (false negative)**. numstat deletions=2 → REJECT. Real exposure: LOG.md at base contains ≥3 filed lines beginning with `--` (`:45`, `:960`, `:2436`); deleting any of them in place passes the draft leg today. Fix: exclude only `^--- a/`/`^--- b/`, or make numstat-deletions==0 (with `--no-renames`) the leg's acceptance condition and keep the patch grep as readable diagnostics.

**HIGH — coverage: `reports/round-71/telemetry/measures-ca.txt` is touched by the corrections non-additively and no leg constrains it.**
CASTAMP at lands requires `"f706aacd"` present and regex `1ce25fb9.{0,120}64da9e14` (re.S) **absent** from the receipt. The stale pairing is a filed byte at base, so the fix MUST delete/rewrite it — a non-append edit of a filed record, in a file leg 10 does not monitor. Consequences: (a) "append-only corrections" is not literally true of the whole Ca landing; (b) the receipt edit's blast radius is unconstrained (arbitrary rewrites inside measures-ca.txt pass all 12 legs); (c) naively adding the receipt to leg 10's path set makes CASTAMP and APPENDONLY jointly unsatisfiable. Note the corpus's own convention (QUALITY criterion 17): receipt re-stamps preserve original bytes **below a marker** and append the corrected stamp — the CASTAMP leg as implemented (regex absence over the whole file) forbids exactly that preservation and forces byte removal, contradicting criterion 17. Fix direction: CASTAMP should require original bytes preserved under a marker plus an appended superseding stamp (marker-scoped regex), after which the receipt can safely join leg 10's path set with marker-scoped originals excepted.

**MEDIUM — coverage: the seven `.ufo/waves/round-71/w2/` files the landing must commit are outside leg 10 (by design), and the sibling W2FILES tuple is wrong.**
At base: 2 tracked-modified (`Filler30.md`, `RevReceipts.md`) + 5 untracked (`CritTrends.md`, `Filler28.md`, `Filler36.md`, `RevCounterCa.md`, `RevEntry.md`) — committing them lands rewritten bytes for the two modified files, unmonitored by leg 10 (acceptable: they are not kill-rule "filed bytes"). But the counter's `W2` tuple = {RevReceipts, RevCounterCa, RevSeparability, CritGaming2, RevRows, RevCausality, Filler33}; five of those (`RevSeparability`, `CritGaming2`, `RevRows`, `RevCausality`, `Filler33`) are already tracked-clean at b60c7b1, so W2FILES is vacuously true at base, while the actually-uncommitted `CritTrends`/`Filler28`/`Filler36`/`RevEntry`/`Filler30` are absent from the tuple. W2FILES needs the claims' real seven (the 2 modified + 5 untracked).

**MEDIUM — coverage: the filed round-71 fleet report is unverifiable by any lane leg.**
Kill rule protects `.ufo/reports/round-71/kotodama.md` `:57`/`:61` bytes; REPORTCORR correctly writes corrections into a NEW round-72 report. But that file lives in the fleet root (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-71/kotodama.md`), outside the lane worktree — leg 10's lane git diff cannot cover it even in principle. The fleet root is a git repo (toplevel confirmed), so a fleet-side `git diff`/hash-pin leg can verify byte-identity; none of the 12 legs does. Rewrite of `:57`/`:61` would violate the kill rule invisibly.

**LOW — rename evasion in the literal leg.** Default rename detection means `git mv` of a covered file yields a `similarity index`/`rename from/to` diff with zero `-` content lines — leg 10 passes while the file leaves its path. Mitigated by QUAL20/21/LOGCORR blob reads failing independently; harden with `--no-renames` regardless (numstat crosscheck here already carries it).

**LOW — frozen counter path not yet materialized.** Claims name `reports/round-72/accept-ca.py`; `reports/round-72/` currently holds only `claims.json` + `telemetry/`. The draft lives at `.ufo/waves/round-72/counters/accept-ca.py`. Until copied in, the claims' counter command fails on file-not-found.

## Residual risk / verification gaps

- My precise patch filter still has one intrinsic ambiguity class (removed filed line shaped exactly `--- a/<covered path>`); the numstat-deletions counter has none — treat numstat==0 as authoritative.
- Trials exercise synthetic lands only; no real `<lands>` exists yet (HEAD == base). The leg must be re-run at the real lands; expected ACCEPT with the hardened filter.
- I did not execute the full draft counter end-to-end (adjacent, not assigned): note `blob(lands, "corpus/id-renumber-map.json")` raises at any lands lacking that new file → whole-counter exit 2 instead of per-leg reporting.
- LOG.md/lesson/QUALITY covered paths were fixture-copied as exact base bytes (`git show b60c7b1:`); the lane worktree QUALITY.md is dirty (criterion 20) but leg 10 compares commits only — unaffected.
- Tooling installed: none.

## Hand-off checks for main

1. Patch draft leg 10 to the precise filter or numstat-deletions==0 (with `--no-renames`), re-run my three fixture cases (scripts: `/tmp/RevAppendOnly/{setup.sh,setup2.sh,check.sh}`).
2. Resolve the CASTAMP vs criterion-17 marker-preservation contradiction before lands; then decide whether measures-ca.txt joins leg 10's set.
3. Fix the W2 tuple to the claims' seven actually-uncommitted files; add a fleet-side byte-identity leg for the round-71 fleet report; materialize `reports/round-72/accept-ca.py`.
