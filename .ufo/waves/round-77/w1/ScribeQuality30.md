# ScribeQuality30 — QUALITY criterion 30 draft ("ledger pairs execute")

Seat: `ScribeQuality30`, round 77 (hyaku run 10), wave 1, leaf.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `211f9526800906e0c585d878d265c37e5e090c15`
(the lane worktree is at that commit: `git -C … rev-parse --short HEAD` → `211f952`).
DRAFT claims read, never edited: `.ufo/waves/round-77/CLAIMS-DRAFT.md`.
Scratch `/fast/scratch/hyaku/kotodama-r77/ScribeQuality30/` created and deleted at the end; every
receipt below was copied into the wave stage directory first.

## 1. Behaviour

Proposed `corpus/QUALITY.md` criterion **30**, in the file's own numbered style (title, "adds to
criteria …" line, lettered limbs, `Check (red-before, pre-dispatch)` block, measured table, `Limits,
stated`, `Grounded in`), at `.ufo/waves/round-77/w1/drafts/quality-30.md` (73 lines, 12 924 B, sha256 `a2cfedf6a63e2abb8c883cd0a450c44360e07f00ab6b2ca6af7720e33a4ab330`). No lane
byte was edited; `corpus/QUALITY.md` was read only.

The criterion binds **both** command fields of every frozen Ca ledger pair (`observe_cmd` *and*
`rederive`) to five limbs: (a) argv arrays, never shell strings, executable in the frozen allowlist
{git, grep, wc, sha256sum, ls, cat, head, tail, cut}; (b) `git -C <repo>` leading, revision in rev
position (before `--`, never a path, resolvable — dead pins refused), at least one revision operand;
(c) the grep pattern operand named (`-e`/`--regexp` or the single first bare operand), metacharacters
admitted only there; (d) `stated_at` = `path:line` inside a frozen per-disposition allowlist with
`stated_text` present *on that line* of the base tree; (e) at Ca-lands the exact argv runs and `parse`
returns `expected_after`. It ships a checker, `tools/check-ledger-pairs.py`, whose stage draft is the
artifact measured here.

Two things the criterion deliberately does **not** take from the same routed defect: uncommitted
telemetry receipts (criteria 17/23 + the round's RECEIPTS leg) and the combined README exemption's
line number (claim Ca's COMBINED leg) — both named in Limits.

## 2. Measured evidence

All runs are read-only against the lane; the fixture lives in scratch and is rebuilt by the generator.
Receipts: `.ufo/waves/round-77/w1/stage/ScribeQuality30/receipt-*.txt`, `fixture-build.txt`.
Checker sha256 `db327b9f90a381a283da6c9f7fe0cbebf87c0200433cd06bda243ec47f1e127b`, generator sha256
`5245952344c9cd3bed101effbd711d4f124a051a800a9d3b70555d39946c5bb3` (`SHA256SUMS` in the stage dir).

**The round-76 ledger, at the lane base.** `python3 -B …/check-ledger-pairs.py --repo <lane> --rev
211f952… --ledger reports/round-76/ledger.json --annotate-allow
LOG.md,SCORECARD.md,corpus/lessons/round-75.md,corpus/QUALITY.md --repair-allow
corpus/README.md,SKILL.md,SHONEN.md` exits **1** and prints:

```
LEDGER-PAIRS: FAIL pairs=0/20 red=20 (NO-C=19, REDERIVE-STRING=20, STATED-AT-SET=1, STATED-TEXT-ABSENT=1)
```

with `RED L76-13 STATED-AT-SET: corpus/knowledge/myth-symbol/narrative-structure-frameworks.md is
outside the frozen ANNOTATE allowlist [...]` and `RED L76-19 STATED-TEXT-ABSENT: stated_text is not
in corpus/lessons/round-75.md at base` — the two findings `reports/round-76/telemetry/measures-ca.txt`
records as `LEG FAIL LEDGER` (`receipt-r76-ledger.txt`: 41 `RED` lines, a summary line, an `exit=1`
line and the command line). The 19 `NO-C` hits are the 19 git
pairs; the twentieth pair is `sha256sum` (`reports/round-76/ledger.json`, 20 pairs
`python3 -c "len(pairs)"` → 20).

**Green first, then one defect per mutant** (fixture `fc5dc79`, base `b988761`; the same 20 pairs
rewritten into the grammar): `LEDGER-PAIRS: PASS pairs=20/20`, exit 0. Then, each a full ledger copy
with one edit — `STATED-AT-SET`, `STATED-TEXT-ABSENT`, `REDERIVE-STRING`, `NO-C`, `REV-POS`,
`EXEC-NOT-ALLOWED`, `UNRESOLVED` (`chars=` from a split pattern), `DEAD-PIN`, `SHELL-STRING` — each
exits 1 printing exactly its named `RED` line, and the three bad-input shapes (`--rev HEAD`, ledger
absent at `--rev`, empty allowlist) refuse with exit 2 and no verdict line
(`receipt-fixture.txt`, `receipt-refusals.txt`). The run limb is measured on a two-pair ledger: green
`PASS pairs=2/2` exit 0; `OBSERVE-MISMATCH: observed 'line 3' != expected 'line 4'` and `EXEC-FAIL:
exit=1` for its two mutants; `--execute` with no `--work`/`$HYAKU_SCRATCH`/`$TMPDIR` refuses exit 2
(`receipt-execute-limb.txt`).

**The routed defect, reproduced on real bytes.** `python3 -c` over `reports/round-76/ledger.json` with
`shlex.split` (the tokenizer `reports/round-76/accept-ca.py:rederive_argv` uses) prints
`pairs=20 rederive_tokenizes_to_same_argv=17 differ=3`; the three are L76-19 (8 → 9 tokens) and
L76-20/L76-21 (9 → 10 each). Executed inside the lane, L76-19's token list exits 128
`fatal: unable to resolve revision: chars=` and L76-20/L76-21's exit 128
`fatal: unable to resolve revision: [0-9a-f]{8}`. Under the round-76 H2 parser the same token lists
are refused as `git grep path operand 'chars=' does not exist in the clone` (L76-19) and
`git grep path operand '98c486bd…' does not exist in the clone` (L76-20/21) — the spot-check's "base
revision / `chars=` treated as path operands", verbatim — while those same pairs' `observe_cmd`
arrays return `None` (accepted). The defect is the string field, not the argv
(`receipt-rederive-split.txt`, `receipt-l76-20-exec.txt`, `receipt-parser-verdict.txt`).

**`-C` is load-bearing.** L76-01's recorded `observe_cmd`, run from a scratch cwd, exits 128
`fatal: not a git repository (or any parent up to mount point /)`; the same argv with `git -C <lane>`
first exits 0 printing `98c486bdb4650ba5b8e651d332910e8ee60ad121:reports/round-75/claims.json:227`
(`receipt-exec.txt`).

## 3. Findings for the L1

1. **The r77 LEDGER leg text in `CLAIMS-DRAFT.md` is narrower than the criterion.** The draft names
   the allowlist, rev position and pattern operands but not `git -C` nor the `stated_at` allowlist +
   `stated_text`-on-the-line limb, both of which the r76 closure's §5 item 3 names. If criterion 30
   lands as drafted, the r77 LEDGER leg must carry all five limbs or the criterion and the frozen
   claim diverge (criterion 9's two-way agreement, applied to a claim rather than a receipt).
2. **A ledger written to limb (b) breaks the copied r76 guard.** Measured:
   `mod.observe_problem(['git','-C',<lane>, …], <lane>)` →
   `git -C '<lane>' is refused (the counter fixes repo and cwd; only the --fleet-root may be named)`,
   while the no-`-C` form returns `None`. ExecAdaptCa's brief already requires the `-C` form, so the
   adapted guard must admit its own repository/clone and keep refusing every other `-C`; this is a
   counter revision, recordable under criterion 23 (`receipt-exec2.txt`).
3. **`rederive` must be an argv or absent.** All 20 r76 pairs carry a shell-string `rederive`; a
   round-77 ledger that copies that field shape fails criterion 30's limb (a) on 20/20 pairs even
   if every `observe_cmd` is perfect. Deriving `rederive` from `observe_cmd` (the counter's own
   fallback) satisfies the criterion; a string does not.
4. **The statement-site limb is line-scoped.** `stated_text` must sit on the `stated_at` line, not
   merely in the file — measured: a mutant carrying text present elsewhere in
   `corpus/lessons/round-75.md` is red (`STATED-TEXT-ABSENT` names the path, not the line). A r77
   ledger built against a whole-file reading will pass its author's check and fail this one.
5. **No round-77 ledger exists yet**, so criterion 30's application to round 77 is unmeasured:
   `git -C <lane> cat-file -e HEAD:reports/round-77/ledger.json` → `fatal: path
   'reports/round-77/ledger.json' does not exist in 'HEAD'`; `git ls-tree --name-only HEAD
   reports/round-77/` prints nothing; `git status --porcelain` shows `?? reports/round-77/` and
   `?? .ufo/waves/round-77/`. The pre-freeze red-before on the real r77 ledger is the L1's to run.

## 4. Gates (not done, by design)

- Did not edit `corpus/QUALITY.md`, `SCORECARD.md`, `LOG.md`, `SHONEN.md`, `SKILL.md`, `corpus/**`,
  `reports/round-76/**`, `reports/round-77/**`, the fleet repo, `scripts/`, `templates/`, `.ufo/state`,
  `.ufo/watchdog.log`, or `/home/vgpnk/Projects/shokuknow/**`.
- No git/jj mutation in the lane (no add/commit/checkout/stash/reset/switch/pull/push). The only git
  commands run were read-only (`show`, `cat-file`, `ls-tree`, `grep`, `rev-parse`, `status`).
- No subagent, no background job, no planning, no model routing, no pacman, no tool installed.
- The only repo writes are this report, `w1/drafts/quality-30.md`, and
  `.ufo/waves/round-77/w1/stage/ScribeQuality30/**` (stage artifacts below). The fixture git repo
  lives in scratch; before its commits
  `git -C "$D" rev-parse --show-toplevel` was asserted equal to `$D` (`fixture-gen.py` line
  `assert os.path.realpath(top) == os.path.realpath(dest)`), and its identity is scoped to the
  fixture (`-c user.name=quality30-fixture -c user.email=quality30@fixture.invalid`).

## 5. Out of scope

- The other two clauses of the same routed defect (uncommitted receipts, combined line number) — owned
  by criteria 17/23, the round's RECEIPTS leg and claim Ca's COMBINED leg; named in the draft's Limits.
- `corpus/QUALITY.md` numbering/ordering beyond "criterion 30 appends after 29" — the L1 installs at
  the freeze.
- Any judgment on whether the proposed criterion is the right *form* of the rule (that is the wave-2
  attack's job); this seat supplies text, check, fixture and measurements.

## 6. Artifacts

| path (relative to the lane) | content |
|---|---|
| `.ufo/waves/round-77/w1/drafts/quality-30.md` | the criterion draft, 73 lines / 12 924 B, sha256 `a2cfedf6…` |
| `.ufo/waves/round-77/w1/stage/ScribeQuality30/check-ledger-pairs.py` | proposed `tools/check-ledger-pairs.py`, sha256 `db327b9f…` |
| `.ufo/waves/round-77/w1/stage/ScribeQuality30/fixture-gen.py` | fixture + mutant generator, sha256 `5245952…` |
| `.ufo/waves/round-77/w1/stage/ScribeQuality30/exec-limb.py`, `exec-limb2.py` | real-bytes executability probes |
| `.ufo/waves/round-77/w1/stage/ScribeQuality30/receipt-r76-ledger.txt` | r76 ledger, 20/20 red, per-code counts |
| `.ufo/waves/round-77/w1/stage/ScribeQuality30/receipt-fixture.txt` | green 20/20 then nine single-defect mutants |
| `.ufo/waves/round-77/w1/stage/ScribeQuality30/receipt-execute-limb.txt` | run limb: green, mismatch, exit-1, refusal |
| `.ufo/waves/round-77/w1/stage/ScribeQuality30/receipt-refusals.txt` | `--rev`, absent-ledger, empty-allowlist refusals |
| `.ufo/waves/round-77/w1/stage/ScribeQuality30/receipt-exec.txt`, `receipt-exec2.txt` | `-C` before/after; r76 guard on `git -C` |
| `.ufo/waves/round-77/w1/stage/ScribeQuality30/receipt-rederive-split.txt`, `receipt-l76-20-exec.txt`, `receipt-parser-verdict.txt` | rederive token divergence and both failure surfaces |
| `.ufo/waves/round-77/w1/stage/ScribeQuality30/fixture-build.txt`, `SHA256SUMS` | fixture commits and artifact digests |

Scratch `/fast/scratch/hyaku/kotodama-r77/ScribeQuality30/` deleted after the receipts were copied;
`/fast/scratch/hyaku/kotodama-r77/` itself untouched.
