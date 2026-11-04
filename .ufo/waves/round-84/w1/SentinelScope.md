# SentinelScope — round-84 w1 report (scope, file-I/O, append-only)

Seat: SentinelScope (leaf, read-only). Full evidence and receipts:
`.ufo/waves/round-84/w1/stage/SentinelScope/probe.md`. No lane file other than
these two was written; no fix was applied.

**Verdict.** Containment is clean (23/23 planned paths inside the lane, no
escape, no sibling/fleet write attributable to a round-84 seat), the registry
plan is append-only (0 in-place row edits, 4 appended, checker proven), but the
round is carrying **four high-severity calibration defects** that will change
what the counters say: a shared-tip landing reds SEPARABLE, a post-dispatch r2
freeze is logged as pre-dispatch, the dispatched contract text is stale against
the graded constants, and criterion 31 is already red on pending telemetry.

## 1. Scope enumeration and containment

Frozen `own_paths` are identical at r0 `3ca2cf28` and r2 `7e6ee2f8`:
D = `corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md`,
`corpus/SOURCES.md`; O = `tools/apply-sound-laws.py`, `examples/sound-laws/`,
`SKILL.md`. The wave stage is `{WAVE}/stage/<Seat>/` (twelve seats + `stage/L1/`);
round receipts are `{WAVE}/SentinelScope.md` and `reports/round-84/`.

All 23 resolved planned paths (claims + example files + stage + reports) are
under the lane root; 0 escapes; no symlinked ancestor. The only sanctioned
outside-lane writes are per-seat scratch dirs. No seat prompt names a fleet or
sibling path as a write target.

Fleet repo: `git -C <fleet> status --porcelain` = 13 entries, **none matching
round-84 / sound-law / witchcraft**. Files that changed in the wave window are
sibling-round reports (`.ufo/reports/round-87/mori.md`,
`.ufo/reports/round-82/{mado,kama,tameshi}.md`) and control-plane files
(`.scratch/*`, `.ufo/l0-questions.md`) — none named by an r84 prompt, none
deleted. `MANIFEST.json` is tracked and byte-identical to `HEAD`
(`aa66428a…`) though its mtime was rewritten in-wave; `.ufo/state/` is
control-plane and rewritten in-wave; no r84 artefact references either for write.

## 2. Tool file-I/O surface (staged tool, sha256 `46c3dd6b…`, 604 lines)

Reads only `--rules` and `--input`; writes only `--out` (always) and `--trace`
(when given); `selftest` writes nothing (imports json/os/re/sys only, no
tempfile). No rule or input field reaches `open()`: **no path injection**.
Contract-forbidden behaviour: none of the findings below; all are silence in the
frozen contract, and the safe ones (missing/absent/unwritable/directory path)
already exit 2 with a `SOUNDLAW_ERROR:` label and no traceback.

- **Escapes:** `--out`/`--trace` accept absolute and `../` paths (e.g.
  `/dev/stdout`, scratch); the only guard refuses `--out` equal to or inside the
  rules/input *directories*. Contract silent.
- **Symlink:** write-through is followed; realpath is used for the guard
  comparison only, so a symlink onto the rules file is refused, any other target
  is overwritten.
- **Existing directory:** `SOUNDLAW_ERROR: io: Is a directory`, rc 2 — for both
  `--out` and `--trace`.
- **Weakest defects (verified by execution):** `--trace` may be the rules or
  input file and destroys it (489→487 B / 627→487 B, rc 0); `--out` == `--trace`
  silently leaves the trace in place of the lexicon (rc 0); a rule `name`
  containing TAB/LF forges trace columns/lines (22 changes → 44 lines, rc 0);
  the out guard is directory-level so `--out <dir-of-rules>/expected-regen.tsv`
  is refused; and the drafted gate row's `--out /dev/stdout` truncates the
  caller's redirected stdout (captured log lost 3 of 16 lines and the summary was
  written over the first bytes). `--out /dev/null` is clean and is the smallest
  fix for the gate row.

## 3. Registry append-only

`corpus/SOURCES.md` blob is `169c3388…` at both base and r2: 837 rows, S914–S917
absent. The round intends **zero in-place edits**; it appends exactly four rows
at the tail. An independent checker (source in probe.md §3) passes base-vs-r2
and an append fixture (841 rows, 0 moved) and reds cell movement (0..6),
reorder, removal, mid-table insert and duplicate ids; cells 7..10 changes are
reported as `DIFF-EDIT`. Residual: the entry may cite existing S-ids and no rule
requires extending their `used-by`; if L1 does extend one, that is a cell-10
edit outside the declared append-only intent.

## 4. Immutability, manifest/state, secrets

`PROVINCE.md` blob `313b182f…` is byte-identical at base, r2 and `HEAD`. No r84
artefact mutates `MANIFEST.json` or `.ufo/state/`; no sibling repo has an r84
path. Credential sweep over committed r0/r2 receipts and working-tree round-84
dirs: 0 matches for private keys, cloud/API token shapes, `token=`/`password=`/
`secret=`, or home credential dirs.

**Criterion 31 is red now:** `tools/check-cited-records.py --root . --from-round
84 --bind-round 84` → `CITED-RECORDS: 0 empty / 6 scratch`, rc 1. The six
findings live in `reports/round-84/telemetry/{smoke-d-r0,smoke-d,smoke-o-r0,smoke-o}.txt`,
each citing an absolute work-tree path under the fast scratch root. Committed
round-84 bytes are clean; those pending receipts are not.

## 5. Findings, severity, smallest remediation

| # | sev | finding | smallest remediation |
|---|---|---|---|
| F1 | High | SEPARABLE reds the first claim at a shared tip: if both claims land in one commit, both fail (L1 fixtures: D 9/10, O 7/8, `foreign_moved` = the other claim's paths); with two commits, the first claim still fails if graded at the tip | land two commits and pin each verdict at its own claim commit (D at the D commit, O at the O commit); derived from the frozen `separable()` formula — no multi-commit fixture was run |
| F2 | High | r2 `7e6ee2f8` committed 10:31:06, after dispatch 10:28:24, but `counter-revisions.md` and `corpus/lessons/round-84.md` say "pre-dispatch"/"before the wave was dispatched" | record r2 as post-dispatch with its timestamp; correct the lesson sentence. Substance intact: no claim artefact had landed, no counter code changed r0→r2 |
| F3 | High | the dispatched contract text names `## 2. The decision table`/`## 4. Attested anchors` and a `selftest`-only CLI; r1/r2 grade `## 2. Six design decisions`/`## 3. Attested anchors` and invoke `--selftest` | grade only with r2; require the r1 headings in the landed entry; keep the tool's dual CLI spelling (it already accepts both — verified) |
| F4 | High | criterion 31 already red: `0 empty / 6 scratch`, rc 1, from four pending telemetry receipts | rewrite the six citations to repo-relative or `<work>/tree/...` before landing |
| F5 | Med | trace violates the r2 `semantics` for length-changing rules (index 0,2,4 where matched positions were 0,1,2; before/after are the segment, not the word); ungraded by accept-o84 | record input-side index + full words, or narrow the frozen semantics to segments |
| F6 | Med | `--trace` can be the rules/input file (destroys it); `--out == --trace` corrupts both, rc 0 | apply the realpath refusal to `--trace` and forbid `out == trace` |
| F7 | Med | directory-level out guard refuses in-place regeneration of the committed example | refuse equality with the rules/input files only |
| F8 | Med | rule `name` with TAB/LF forges/splits trace rows while exiting 0 | refuse control characters in `name` |
| F9 | Med | drafted gate row uses `--out /dev/stdout`, which truncates redirected stdout and loses the summary | use `--out /dev/null`; qualify the "read-only" write-scope cell |
| F10 | Low | symlink write-through permitted | none required; state it in the gate row |
| F11 | Info | fleet repo not globally clean (sibling rounds + control plane), but no r84-attributable write; nothing deleted | none |
| F12 | Info | in-wave lane writes no seat owns: `reports/round-84/counter-revisions.md`, `corpus/lessons/round-84.md`, `{WAVE}/**`, `reports/round-84/telemetry/**`; the lesson's `## Gate` is a placeholder | fill the Gate before landing, else criterion 31(iii) fails |
| F13 | Pass | containment: 23/23 planned paths inside lane, 0 escapes | — |
| F14 | Pass | append-only: 0 in-place row edits, 4 appended, checker proven | run the checker on the real SOURCES before landing |

## 6. Limits

Tool claims describe the staged bytes at 10:34–10:36, not the future landed
bytes. F1's remedy is derived from the frozen `separable()`/`claim_span` code and
marked as inference (no git fixture was created; the seat bound permits one only
where the assignment asks). The criterion-31 count and fleet porcelain are
snapshots at probe close. Scratch was removed; nothing left behind.
