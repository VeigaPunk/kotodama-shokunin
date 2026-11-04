# SentinelScope — probe (Kotodama r84 w1)

Read-only adversarial probe of scope, file-I/O and append-only discipline. Lane
root is the repository containing this file; every path below is repo-relative
unless it names the fleet repo or a sibling lane. Nothing in the lane was
edited; the only writes are this file and `w1/SentinelScope.md`. Scratch was
used only under the sanctioned per-seat scratch dir and is removed at exit (see
§7).

## 0. Revision identity — four pins, not one

| artefact | revision it names | committed |
|---|---|---|
| the assignment I was dispatched with | `3ca2cf28…` (r0) | 2026-11-04T10:25:06-03:00 |
| `.ufo/waves/round-84/spec-v1.json`, `w1-dispatch.json`, `build-w1.py` | `7e6ee2f8…` (r2) | r2 committed 2026-11-04T10:31:06-03:00 |
| lane `HEAD` | `7e6ee2f8…` (r2) | same |
| wave dispatch marker `.ufo/waves/round-84/w1.ready.dispatched` | 12 agent ids | file mtime 10:28:24.641 |

Intermediate r1 = `e160a72e…` (10:28:17). The frozen config blob hashes:
`claims.json` `9849def4` (r0) → `de2282df` (r1) → `d75dac85` (r2).
The three counter `.py` files are byte-identical across r0..r2
(`git diff --stat 3ca2cf28 7e6ee2f8 -- 'reports/round-84/*.py'` is empty), so
the whole r1/r2 delta is frozen-config text.

## 1. Planned writes and containment

Claim `own_paths` at r0 and r2 are identical (verified with `git show` on both
blobs): D = entry + `corpus/SOURCES.md`; O = tool + `examples/sound-laws/` +
`SKILL.md`. Wave stage is `{WAVE}/stage/<Seat>/` for twelve seats plus
`stage/L1/`; round receipts are `{WAVE}/` and `reports/round-84/`.

Every planned path, resolved with `realpath`, is under the lane root:

- claim D: `corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md`,
  `corpus/SOURCES.md`;
- claim O: `tools/apply-sound-laws.py`, `examples/sound-laws/` (files
  `rules.json`, `proto-lexicon.tsv`, `expected.tsv`, `expected-trace.tsv`), `SKILL.md`;
- stage: `{WAVE}/stage/{ScoutGapWitch,ScoutSourcesWitch,ExecSoundLaws,ExecBeforeState,ExecRegistryRows,ScribeEntryWitch,ScribeRowsWitch,ConnectorOverlap,ReviewerEntry,CriticClaims,MutationTester,SentinelScope}/`;
- reports: `{WAVE}/SentinelScope.md`, `{WAVE}/SwarmRegistry`, `reports/round-84/counter-revisions.md`,
  `reports/round-84/telemetry/`.

Result: **23/23 resolved paths inside the lane; 0 escapes; no symlink on any ancestor**
(`.ufo`, `corpus`, `tools`, `examples` are ordinary directories). The only
sanctioned writes outside the lane are per-seat scratch dirs, which the host
guard requires to be cleaned. No seat prompt names a fleet or sibling path as a
write target: ConnectorOverlap's sibling scan and ScoutSourcesWitch's census
read are read-only; the census is invoked with `validate --file <mirror>`.

### Fleet repo

`git -C <fleet> status --porcelain` at probe close: 13 entries, **none**
matching `round-84`, `sound-law` or `witchcraft`. Nothing was deleted.

Files that *did* change on the fleet side during the wave window are all
non-r84 classes and are left in place:

- sibling-round reports: `.ufo/reports/round-87/mori.md` (mtime 10:31–10:33),
  `.ufo/reports/round-82/{mado,kama,tameshi}.md`;
- control-plane files: `.scratch/*` (goal/state/closure entries),
  `.scratch/run15-state.json`, `.ufo/l0-questions.md`;
- `after` (fleet root, untracked, dated 2026-11-03 20:05, pre-wave).

Attribution: no round-84 seat prompt names any of them, and no r84 path appears
in fleet porcelain. `scripts/hyaku/*` was modified at 10:20, before the wave.
The fleet repo is therefore **not clean globally** but carries **no
round-84-attributable write**.

MANIFEST.json (tracked, `aa66428a…`) is byte-identical to `HEAD:MANIFEST.json`
and clean in porcelain; its mtime advanced 10:24 → 10:33, i.e. the fleet control
plane rewrote it with identical bytes. `.ufo/state/` has a rewritten `state`
file (10:33) and growing control-plane logs; no round-84 artefact references
either as a write target (the only mentions are the bounds prohibition text).

## 2. Tool I/O surface — the staged tool, read and run

At probe time `{WAVE}/stage/ExecSoundLaws/apply-sound-laws.py` exists:
604 lines, 26296 bytes, sha256 `46c3dd6bbdf04a0d0b09947f556c2ef977729e3ba86b5702b1391d4219276602`;
imports only `json`, `os`, `re`, `sys`; no `tempfile`, no `subprocess`, no
network. Example files: `rules.json` `9a48a2c7…` (627 B), `proto-lexicon.tsv`
`192ef7e7…` (489 B), `expected.tsv` `241f0edf…` (196 B), `expected-trace.tsv`
`bf87cf87…` (487 B).

Observed invocations (cwd = a scratch dir, tool cited repo-relative):

- `python3 -B <tool> selftest` → `SELFTEST: PASS (36 checks)`, rc 0.
- `python3 -B <tool> --selftest` → same, rc 0 (both spellings accepted).
- `apply --rules in/rules.json --input in/proto-lexicon.tsv --out out/derived.tsv
  --trace out/trace.tsv` → `SOUNDLAWS: 16 words / 7 rules / 19 changes`, rc 0;
  `derived.tsv` byte-identical to `expected.tsv`; trace 19 lines; all 7 rule
  names occur (12 × `final-a-loss`, 1 each for the other six).
- Negative cases (all rc 2, `SOUNDLAW_ERROR: <label>: <detail>` on stderr, no
  traceback): missing rules (`rules-missing`), non-JSON (`rules-json`), top-level
  array (`rules-shape`), non-dict rule (`rules-shape`), empty `from`
  (`rule-from-empty`), missing `--out` (`usage`), `selftest extra` (`usage`).
- `--out` an existing directory, and `--trace` an existing directory, and a
  missing parent: rc 2 `SOUNDLAW_ERROR: io: …`, no traceback (the `OSError`
  catch covers these).

### Reads / writes

- Reads: exactly `--rules` (bytes, then JSON) and `--input` (bytes, UTF-8 then
  TSV). Nothing else — no env path, no include, no network.
- Writes: exactly `--out` always, `--trace` when given. `selftest` writes
  nothing (no tempfile in the source; verified by inspection and by the import
  set). This matches "no writes outside the paths the caller names".
- Path injection from file content: **none**. `from`/`to`/`pre`/`post`/`name`
  and the gloss are data; no field reaches `open()`. Rule names and glosses are
  echoed into the trace (see risk R7) but cannot name a path.

### Risks found (contract silence marked)

| # | risk | observed | forbidden by the frozen contract? | severity |
|---|---|---|---|---|
| R1 | `--out`/`--trace` may be absolute or `../` and escape the caller's cwd | allowed; `/dev/stdout` accepted, out in scratch accepted | no clause; guard only refuses `--out` equal to or inside the rules/input *directories* | Low (CLI caller is trusted) |
| R2 | `--trace` is unguarded: it may be the rules file or the input file | `--trace in/ii.tsv` rewrote the input 489→487 B, rc 0; `--trace in/rr2.json` rewrote rules 627→487 B, rc 0 | no; the seat prompt's guard names only `--out` | Medium (silent data loss) |
| R3 | `--out` == `--trace` | second write replaces the derived lexicon with the trace; summary still prints, rc 0 | no | Medium |
| R4 | `--out` is a symlink to a file elsewhere | target overwritten through the link, rc 0; realpath is used only for the guard comparison, not for the write | no | Low |
| R5 | existing directory / missing parent / unwritable path | rc 2, `SOUNDLAW_ERROR: io: …`, no traceback | input-error clause arguably does not cover output errors; behaviour is the safe one | none |
| R6 | the out-path guard is directory-level, not file-level | with rules+input in `in/`, `--out in/expected-regen.tsv` is refused (`output-path`); the committed example cannot be regenerated in place | no; the seat prompt asked for exactly this refusal | Medium (operability) |
| R7 | rule `name` with TAB/LF forges trace columns/lines | name `a\tb` → 6-column trace row; name `a\nb` → 22 changes become 44 trace lines while the summary says 22, rc 0 | no; but it breaks the tool's own trace invariant and the counter's `len(tl)==c` | Medium |
| R8 | gate row `--out /dev/stdout` (drafted in `stage/ExecRegistryRows/rows.md`) | with stdout redirected to a file, the tool opens the same file with `"w"`, truncating it: the captured log lost 3 of 16 lexicon lines and the summary was written over the first bytes (`grep -c SOUNDLAWS` = 1, at line 1) | no; but the row's write-scope cell calls it "read-only" | Medium |

`--out /dev/null` is safe (summary intact, rc 0) and is the smallest fix for R8.

## 3. Append-only proof for `corpus/SOURCES.md`

`corpus/SOURCES.md` is byte-identical at base and r2: blob
`169c338893c75d05de95a72b86f3707512b8f80b` for both. Registry at r2: **837**
rows under the 11-cell header (line 28); `S914`–`S917` absent (0 matches).

Declared in-place edits: **zero rows**. The round appends exactly four rows
(S914–S917) at the table tail; no prompt instructs editing an existing row.
Residual, stated: the entry is allowed to cite already-registered S-ids
(`stage/ScribeEntryWitch` brief), and no rule requires adding the new entry to
those rows' `used-by`; census E11 only checks that each `used-by` path exists.
If L1 chooses to extend an existing row's `used-by` for accuracy, that is cell
10 — outside the round's declared append-only intent — and my checker reports it
as `DIFF-EDIT`, not as a violation.

Checker (written in scratch; compacted source below, same logic — the tested file
printed the base/lands cell values truncated at 90 chars) compares base vs lands row-by-row:
it flags cell movement in cells 0..6, removal, reorder, mid-table insertion,
duplicate ids, and bad cell counts; cells 7..10 changes are informational.
Fixture results:

```
base vs r2 freeze      APPENDONLY: 837/837 rows / 0 new / 0 moved            rc 0
+ S914..S917 appended  APPENDONLY: 837/841 rows / 4 new / 0 moved            rc 0
teaches cell edited    CELL-MOVED S010 cell=6 … / 1 moved                    rc 1
two rows swapped       REORDER base=S004 lands=S005                          rc 1
row deleted            REMOVED S005 (base line 34) / REORDER …                rc 1
row inserted mid-table MID-INSERT S999 line=31 before base tail line=869     rc 1
duplicate id           DUPLICATE S002 + CELL-MOVED S002 …                     rc 1
used-by edited         DIFF-EDIT S006 cell=10 … / 0 moved                    rc 0
```

```python
#!/usr/bin/env python3
"""Append-only checker for corpus/SOURCES.md registry rows."""
import re, sys
ROW = re.compile(r"^[ ]{0,3}\| S[0-9]{3,} \|")
def rows(path):
    out = []
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            if ROW.match(line):
                out.append((n, [c.strip() for c in line.rstrip("\n").split("|")[1:-1]]))
    return out
def main(argv):
    if len(argv) != 3:
        print("usage: registry-appendonly.py BASE.md LANDS.md", file=sys.stderr); return 2
    try:
        base, lands = rows(argv[1]), rows(argv[2])
    except OSError as exc:
        print("APPENDONLY_ERROR: %s" % exc, file=sys.stderr); return 2
    for n, c in base + lands:
        if len(c) != 11: print("BAD-SHAPE line=%d cells=%d" % (n, len(c)))
    b_ids = [c[0] for _, c in base]; l_ids = [c[0] for _, c in lands]
    dups = sorted({i for i in l_ids if l_ids.count(i) > 1})
    for i in dups: print("DUPLICATE %s" % i)
    b_map = {c[0]: (n, c) for n, c in base}; l_map = {c[0]: (n, c) for n, c in lands}
    for i in b_ids:
        if i not in l_map: print("REMOVED %s (base line %d)" % (i, b_map[i][0]))
    survived = [x for x in l_ids if x in b_map]
    reordered = [k for k, (w, g) in enumerate(zip(b_ids, survived)) if w != g]
    if reordered:
        k = reordered[0]; print("REORDER base=%s lands=%s" % (b_ids[k], survived[k]))
    moved = 0
    for i in b_ids:
        if i not in l_map: continue
        bc, lc = b_map[i][1], l_map[i][1]
        for k in range(7):
            if bc[k] != lc[k]:
                moved += 1; print("CELL-MOVED %s cell=%d" % (i, k))
        for k in range(7, 11):
            if bc[k] != lc[k]: print("DIFF-EDIT %s cell=%d" % (i, k))
    base_tail = max((n for n, _ in base), default=0)
    mid = [c[0] for n, c in lands if c[0] not in b_map and n < base_tail]
    for i in mid: print("MID-INSERT %s" % i)
    print("APPENDONLY: %d base rows / %d lands rows / %d new / %d moved"
          % (len(b_ids), len(l_ids), len([i for i in l_ids if i not in b_map]), moved))
    missing = [i for i in b_ids if i not in l_map]
    return 1 if (moved or missing or dups or reordered or mid) else 0
if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

## 4. Immutability, provenance, secrets

- `PROVINCE.md` blob `313b182f251564b7997b06996b4f063370778f11` at base, at r2
  and at `HEAD`: **byte-identical**. PASS.
- `MANIFEST.json`: tracked, hash equals `HEAD` (`aa66428a…`), clean in
  porcelain; mtime rewritten in-wave with identical bytes by the control plane.
  No content mutation. `.ufo/state/` is fleet control-plane, rewritten in-wave,
  no r84 reference. No round-84 artefact names either as a write target.
- Sibling lanes: no `sound-laws` / `apply-sound-laws` / `witchcraft-sorcery`
  path in any sibling `*-shokunin` porcelain; the `reports/round-84` dirs in
  `audio-shokunin` and `game-dev-2d-shokunin` date from 2026-10-15 (their own
  rounds). No r84 write to a sibling repo.
- Credentials: `git grep` over `reports/round-84` at r0 and r2 for
  `BEGIN … PRIVATE KEY`, `AKIA…`, `gh[pousr]_…`, `xox[baprs]-`, `token=`,
  `password=`, `secret=`, and for home-directory credential dirs
  (`.ssh`, `.config`, `.aws`): **0 matches**. Working-tree round-84 dirs: 0 matches.
- Criterion 31: `python3 -B tools/check-cited-records.py --root . --from-round
  84 --bind-round 84` prints **`CITED-RECORDS: 0 empty / 6 scratch`, rc 1**.
  The six findings are in four pending telemetry receipts
  (`reports/round-84/telemetry/smoke-d-r0.txt`, `smoke-d.txt`,
  `smoke-o-r0.txt`, `smoke-o.txt`): each cites an absolute work-tree path under
  the fast scratch root. Committed round-84 bytes at r0/r2 are clean; the
  working-tree telemetry is not. If those receipts land as-is, criterion 31(ii)
  fails by the lane's own checker.
- Absolute paths also sit in `.ufo/waves/round-84/build-w1.py` and
  `spec-v1.json` (seat-scratch template and context). Criterion 31's checker
  does not scan `.ufo/waves/`, and round-82 landed the same class, but the wave
  bound still says no absolute scratch path in a committed receipt; land only
  the seat receipts, or normalise those lines, if the wave dir is committed whole.

## 5. Findings, severity, smallest remediation

- **F1 (High) — SEPARABLE makes the *first* claim red at a shared tip.**
  `separable()` takes `parent` = parent of the first commit touching the claim's
  unique own paths and compares the *other* claim's `foreign_paths` between
  `parent` and `--lands`. If both claims land in one commit, both counters fail
  (L1's own fixtures: `ACCEPT-D-84 FAIL legs=9/10`, `ACCEPT-O-84 FAIL 7/8`,
  `foreign_moved` = the other claim's paths, lands `6f3e45c6`). With two commits
  (D then O), D graded at the *tip* still fails, because O's paths move between
  base and the tip. Remedy (derived from the frozen formula, `[INFERENCE]` — no
  multi-commit fixture was run, the git-fixture bound): land **two commits**, and
  pin each verdict at its own claim commit — D at the D commit (`parent` = base,
  O's paths unchanged), O at the O commit (`parent` = D commit, D's paths
  unchanged). Any other shape is red by construction.
- **F2 (High) — the r2 freeze postdates dispatch, and two receipts say the
  opposite.** Dispatch marker 10:28:24 < r2 commit 10:31:06; the r2 section of
  `reports/round-84/counter-revisions.md` (working tree, 10:31:18) says
  "Pre-dispatch … the wave had not been dispatched", and the untracked lesson
  `corpus/lessons/round-84.md` (10:33:55) says "Claims frozen … before the wave
  was dispatched". Both are falsified by the marker file and by twelve live
  seats. The *substance* is intact (no claim artefact had landed at 10:31; the
  tool staged at 10:34; r1/r2 changed no counter code). Remedy: record r2 as a
  post-dispatch revision with its timestamp, and correct the lesson sentence to
  the actual sequence.
- **F3 (High) — the dispatched contract text is stale against the graded
  freeze.** The text names `## 2. The decision table` / `## 4. Attested
  anchors` and a `selftest`-only CLI; r1/r2 grade `## 2. Six design decisions` /
  `## 3. Attested anchors` (read from frozen config by `section_lines`) and the
  counter invokes `--selftest` (the tool accepts both — verified). A seat or
  landing that follows the dispatched text is red on SECTIONS/DECISIONS/ANCHORS
  while conforming to the text it was given. Remedy: grade only with r2, require
  the r1 headings in the landed entry, and keep the dual CLI spelling.
- **F4 (High) — criterion 31 is already red on pending telemetry.** See §4:
  `0 empty / 6 scratch`, rc 1. Remedy: rewrite those six citations to
  repo-relative or `<work>/tree/...` form before landing.
- **F5 (Medium) — the trace violates the r2 frozen semantics for
  length-changing rules, and the counter cannot see it.** r2's `semantics` says
  `index` is the matched position *before* the change and columns 4–5 are
  `word-before`/`word-after`; `derive_word` records `index = len(out)`
  (output-side) and the matched segment, not the word. Observed on `a a a`
  with `grow(a→a b)` then `mark(b→B)`: `grow` rows carry indices 0, 2, 4
  (matched positions were 0, 1, 2) and `before/after` = `a` / `a b`.
  `accept-o84` reads only field 2 and the line count. Remedy: record the
  input-side index and the full words, or narrow the frozen semantics to
  segments — one of the two, not both.
- **F6 (Medium) — `--trace` can destroy `--rules`/`--input`, and `--out ==
  --trace` corrupts both silently.** Observed (R2/R3). Remedy: run the same
  realpath refusal over `--trace`, plus `out != trace`; two lines.
- **F7 (Medium) — the out guard is directory-level and blocks in-place
  regeneration of the committed example.** Observed (R6). Remedy: refuse only
  equality with the rules/input *files* (already computed), not the directory.
- **F8 (Medium) — a rule name with TAB/LF forges the trace and the tool exits
  0.** Observed (R7), including 22 changes rendered as 44 lines. Remedy: refuse
  control characters in `name` with `SOUNDLAW_ERROR: rule-name-shape`.
- **F9 (Medium) — the drafted gate row's `--out /dev/stdout` corrupts its own
  captured stdout.** Observed (R8): 3 of 16 lines lost, summary written over the
  first bytes. Remedy: `--out /dev/null` (verified clean) or a scratch path
  outside the repo, and drop "read-only" from the write-scope cell or scope it to
  "no repo path is written".
- **F10 (Low) — symlink write-through is permitted** (R4); contract-silent.
- **F11 (Info) — fleet repo has no r84-attributable write** but is not globally
  clean (sibling rounds + control plane, §1). Nothing deleted.
- **F12 (Info) — in-wave lane writes that no seat owns:**
  `reports/round-84/counter-revisions.md` (M, 10:31:18),
  `corpus/lessons/round-84.md` (untracked, 10:33:55), `{WAVE}/**`,
  `reports/round-84/telemetry/**` — L1/orchestrator artefacts, inside the lane.
  The lesson's `## Gate` is still a placeholder; if it lands unfilled, criterion
  31(iii) fails.
- **F13 (Pass) — containment:** 23/23 resolved planned paths inside the lane; 0 escapes.
- **F14 (Pass, with residual) — append-only:** 0 declared in-place row edits;
  4 appended rows; checker proven on seven fixtures (§3).

## 6. Method limits

- The tool was read and executed as staged at 10:34–10:36; the landed bytes may
  differ. All tool claims above are about the staged sha256 in §2.
- No git fixture was created (the seat bound allows one only where the
  assignment asks); the two-commit SEPARABLE remedy is derived from the frozen
  formula, marked `[INFERENCE]`.
- Working-tree receipts are time-dependent; the criterion-31 count is a snapshot
  at probe close.
- The registry checker assumes the house row shape `| S…` with one leading
  space; the census grammar is looser (`\| *S`). The 837-row count agrees with
  the census.

## 7. Scratch

Scratch lived under the sanctioned per-seat scratch dir; it held the checker,
the seven SOURCES fixtures, and the tool test bed (fixtures, captures). Nothing
is cited from it; every receipt above is this file. The scratch tree was
removed before exit; nothing is left behind.
