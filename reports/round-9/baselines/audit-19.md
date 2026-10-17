# R9-O19 — auditor: no gate source file changed behavior in round 9

- **Seat:** R9-O19 (auditor). **Lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  **Date:** 2026-10-17, local clock UTC-03:00; audit window opens 17:48:49 and closes at the
  write-time re-check recorded in §7.
- **Role limits:** this seat executes and measures; it decides no admission, promotes no claim,
  and certifies no canon or source content. Its only write is this file. Fragments written by
  other seats are cited as *their* evidence, never absorbed as mine.
- **Revision binding:** `HEAD = a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (round-9 declaration),
  declared `baseline_revision = e1694bad6ac96aca45a11ca5746582b275929355` (= `HEAD~1`, round-8
  admit). Measured window diff `git diff --stat e1694ba HEAD` →
  `reports/round-9/claims.json` (34 +) and `reports/round-9/targets.json` (125 +), 159 insertions,
  0 deletions. So the graded artifact tree is identical at the declared revision and at HEAD, and
  every gate byte named below is the same byte under both.
- **Question this file answers:** did any of the seven structural gate sources
  (`tools/gates/*.py`) change *behavior* in the round-9 window, and if so, is the change
  documented? Assignment text: `git diff tools/gates/*.py must be empty except documented
  exceptions`.

## 1. Verdict

**No gate source file changed bytes or behavior in the window audited.** All seven gate scripts
are byte-identical to the declared baseline revision at three independent samples, and every
behavioral probe I ran (7 selftests, plus a 21-probe error-path vector) produced identical results
at the first and second samples. **Documented exceptions for gate sources: none — zero.**

The only tracked file under `tools/` that the round has touched is the *runner*
`tools/check-gate-battery.py`, which claim O explicitly authorizes
(`reports/round-9/claims.json` O `after_required`: "no gate behavior changes without a documented
reason in the fragment"; `reports/round-9/targets.json` R9-O15: "WITHOUT changing gate behavior").
Its gate-execution path is unchanged (§5). It was still being written inside my window, so my
verdict binds the gate tree, **not** the runner's final bytes.

## 2. Content identity of the gate tree

| scope | command | observed |
|---|---|---|
| declared → HEAD | `git diff --stat e1694ba HEAD -- tools/gates/` | empty |
| declared → worktree | `git diff --stat e1694ba -- tools/gates/` | empty |
| HEAD → worktree | `git diff --stat -- tools/gates/` | empty |
| status classes | `git status --porcelain -uall -- tools/gates/ \| awk '{print $1}' \| sort \| uniq -c` | `17:52` → `9 ??`; write-time re-check `17:52:45` → `33 ??`; in both sweeps and every sweep between, **0 modified, 0 deleted** — only other seats' baseline data was landing |
| per-file digests | `for f in $(git ls-tree -r e1694ba --name-only -- tools/gates/); do [ "$(git rev-parse e1694ba:$f)" = "$(git hash-object $f)" ] ...` | 61/61 `MATCH`, `fail=0` |
| fixture subtree | `git diff --stat e1694ba -- tools/gates/fixtures/`; `git status --porcelain -uall -- tools/gates/fixtures/` | both empty (21 fixture files unchanged, none added) |
| counts | `git ls-files tools/gates/ \| wc -l`; `ls tools/gates/*.py \| wc -l`; `find tools/gates/fixtures -type f \| wc -l` | 61 tracked; 7 gate scripts; 21 fixtures (= the battery's 7 + 21 = 28 hashed paths) |

**The untracked additions are data, not gate code.** The nine files below are the complete set at
the 17:52 sweep (sha256 of each, `git status` + `sha256sum`, 2026-10-17); the set grew to 33 files
by the 17:52:45 re-check as other seats landed more baselines, and the *tracked-file* diff stayed
empty throughout — additions only, never an edit to an existing gate or fixture byte:

```
644b5734485e2186896dc5a4a48d0b7a53babeea7dde645aa64d53c6410a2348  tools/gates/expected/costume-era-consistency-gate/r9-pre/expected.json
89e4d25060933842caff0d3cd4d3c85644967effb64ffd6069c3b825912584c1  tools/gates/expected/costume-era-consistency-gate/r9-pre/freeze.txt
36d92113d0cb8e04687c36694b507e93f25ca08c04003d75b7b537de65c1ea0e  tools/gates/expected/costume-era-consistency-gate/r9-pre/packet.yml
2763614ff26959e6b7fa7d96471e8d5e9e93616e37d47e3f0bec99b5caa62cde  tools/gates/expected/phonology-sanity-gate/r9-pre/expected.json
e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643  tools/gates/expected/phonology-sanity-gate/r9-pre/packet.yml
4d392240e61c63cc2146d05bb1e354c0b75cd33d9603e7ea33a428a83c0c2f25  tools/gates/frozen/lexicon-coverage-audit/r9-pre/digests.sha256
0fad58ba70d545328d015990de5184bdd371e575810eb7e79c96bcc7c8a4ff9c  tools/gates/frozen/lexicon-coverage-audit/r9-pre/expected.json
4909a6b49b838e96c8ca00bf049b832dc55332243342b59222e42a4d56a6d788  tools/gates/frozen/lexicon-coverage-audit/r9-pre/freeze.txt
a1b8ed7c3548ace7a631b6b2752673f6a65a44896caecef170e373d67ec59187  tools/gates/frozen/lexicon-coverage-audit/r9-pre/packet.yml
```

### 2.1 The mtime anomaly, resolved (recorded because it looks like churn and is not)

Five gate scripts and `tools/gates/fixtures/phonology-sanity-gate.yml` carry mtimes/ctimes of
2026-10-17 17:15–17:26 (`stat -c 'mtime=%y ctime=%z'`), i.e. *after* the round-8 declaration
`cf338a7` (17:10:35) and *before* the round-8 admit commit `e1694ba` (17:44:17) — inside the
**round-8** window, not round 9 (which opens at `a7bb205`, 17:46:36). Their content is
byte-identical to the bytes that commit carries (`git rev-parse e1694ba:<path>` = `git hash-object`
= current `sha256`). Attribution: the round-8 gate repairs, committed in `e1694ba`
(`git show --stat e1694ba -- tools/gates/` → 6 gate scripts, 596 insertions, 73 deletions;
`handoff-packet-check.py` was not among them). No round-9 writer touched gate bytes.

## 3. Behavior, sampled twice (T1 17:48–17:50, T2 17:51)

### 3.1 Selftests

`python3 tools/gates/<gate>.py --selftest`, run in the live tree, stdout captured:

| gate | T1 exit | T2 exit | stdout sha256 (T1 = T2) | verdict |
|---|---|---|---|---|
| costume-era-consistency-gate | 0 | 0 | `0c2ed631fb5809ade6cbd52185cbe86f677f3278c8c40e61c5389fc191aca00b` | byte-identical across samples |
| handoff-packet-check | 0 | 0 | `be1ef058b2cfc67a564003917fd39125121755ae66960bd9ea5feb04c0c7ef2f` | byte-identical across samples |
| lexicon-coverage-audit | 0 | 0 | `fd731b1423443238cb5c1fc75dfd350244cc611295c9713b129252b251478658` | byte-identical |
| myth-consistency-gate | 0 | 0 | `80e7d9dc86a29cf56591cfa0cf5bd8fab82a84d4b9d67f03200f1bd689c5aa53` | byte-identical |
| naming-collision-gate | 0 | 0 | `d3566a9cad69f956fd7a4274cb80ad4b95a92bb63a9cf689e45338d05ca5c7da` | byte-identical |
| phonology-sanity-gate | 0 | 0 | `3e9a1209afa352902922a64df1d0bf7a48c25cf09126aa62b70855bd3b447843` | byte-identical |
| provenance-audit | 0 | 0 | `972306c1269a79149f2588d80579602357cb2f140a2ae4c37691eab0523c04b1` | byte-identical |

Comparison at the sample level was `cmp` (byte compare), not digest-only: all seven reported
`vs_T1=BYTE-IDENTICAL`.

**Cross-round stability where a pre-round-9 pin exists.** Five of the seven selftest outputs are
byte-identical to the committed round-3 frozen artifacts under `tools/gates/frozen/round-3/selftests/`
(costume `0c2ed631…`, lexicon `fd731b14…`, naming `d3566a9c…`, provenance `972306c1…`, matching
`sha256sum` of those files). Two differ from their round-3 frozen copy in the summary line only:

```
myth:        … fixture and expected rewritten under tools/gates/fixtures/     (round-3)
       →     … fixture and expected verified against the embedded constants  (now)
phonology:   … 26 control cases passed   (round-3)  →  … 29 control cases passed  (now)
```

These are **round-8** changes, not round-9: `tools/gates/frozen/round-3/MANIFEST.tsv` records
`gate_sha256 26d246e9…` (myth) and `fb05c644…` (phonology) against today's `5368b135…` and
`d5fe087f…`, and the round-8 admit diff above is where those bytes changed. Round-9 added no
further drift: T1 = T2 for both.

### 3.2 Error-path vector (behavior beyond the selftest)

Each gate was fed three unusable inputs — malformed YAML (`bad.yml`), empty file, missing path —
and each run must read could-not-evaluate (exit 2), never a silent pass:

```
T1 and T2, identical:  7 gates × {bad.yml, empty.yml, nosuch.yml} → "2 2 2"  (21/21 exit 2)
```

### 3.3 Behavior on the live D2 packet (input digests recorded, so attribution is exact)

`examples/culture-d2/packet.d2.yml` = `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643`,
unchanged between `e1694ba` and the worktree (`git diff --stat e1694ba -- <packet>` empty). Fixture
entries, 2026-10-17: phonology exit 1 / 3 `FINDING` lines / stdout `1ce5f0cd…` (identical to the
round-3 frozen output — the packet changed since round 3, so this is a *coincidence-free* match at
3 findings, not a pin); lexicon exit 0 / empty stdout; myth exit 0; costume exit 0; naming exit 1 /
17 lines / `ebc8850d…`; provenance over two corpus files exit 0. **Comparisons against round-3
frozen entry outputs for myth/costume/naming are confounded by input drift** (round-3 pins input
`54be6319e4907d20…`, live input `e0f21509…`) and are therefore *not* used as round-9 evidence here;
they are recorded so no one else reads them as drift.

## 4. Additions under `tools/gates/` are inert to gate behavior

Two independent lines:

1. **Static:** no gate reads `expected/` or `frozen/`, and no gate globs its own tree — the only
   glob-like call anywhere in the seven scripts is `provenance-audit.py:344`
   (`found = sorted(p for p in path.rglob("*.md") …)`), which walks a *user-supplied* CLI path.
   Fixture/expected paths are built from a literal `fixtures/` component plus a fixed filename
   (`costume-era-consistency-gate.py:140`, `handoff-packet-check.py:688-689`,
   `lexicon-coverage-audit.py:126-127`, `myth-consistency-gate.py:104`, `naming-collision-gate.py:1787-1788`,
   `phonology-sanity-gate.py:118-119`, `provenance-audit.py:107-108`). `grep -n "'frozen'\|expected/\|frozen/" tools/gates/*.py`
   → no match.
2. **Dynamic:** I copied `tools/gates/` to `/dev/shm/r9o19/min/gates`, **deleted** this round's
   added `expected/` and `frozen/` directories from the copy, and ran all seven selftests there.
   After normalizing the tree root in the outputs, all seven are identical to the live runs:
   `costume IDENTICAL, handoff IDENTICAL, lexicon IDENTICAL, myth IDENTICAL, naming IDENTICAL,
   phonology IDENTICAL, provenance IDENTICAL` (exit 0 each). The round's additions demonstrably do
   not participate in gate behavior.

## 5. The runner changed; its gate-execution path did not

Claim O authorizes extending `tools/check-gate-battery.py`. Revision timeline measured in this
window (`sha256sum` + `stat -c %y`):

| revision | at | size | state |
|---|---|---|---|
| `077f68e488d56c633c98a0d95a24581389ed655b52e0fb553c3dec5f5ffe9b67` | ≤17:50:0x | 19508 | round-8 bytes (equal to the round-8 audit pin `reports/round-8/operability/audit.md:20`) |
| `6fff02dfe752050bb64f83387e79533b061bfa68d18f52c48b572130cfdf724d` | 17:50:49 | 22498 | extension docstring + constants only (no baseline code path yet) |
| `50f576c5f3300d6df53a683d305ce3a099987f48a87dbb936742cfc0493bc8bc` | 17:51:30 | 38850 | baseline check implemented (`inspect_baselines`, `verify_baseline_spec`, `combined_exit`) |
| `c954135edfeba6d2199fb9e5360837c0630594e798317334312e293ae6c7b3d0` | 17:51:46 | 39222 | baseline check present; still being written |
| `9ad0ef9516852c0f…` | 17:52:36 | — | a further revision, observed by the continuity poller (one-minute `sha256sum` samples) after my last direct hash; the runner did **not** settle inside my window |

What I verified on the gate side of that file:

- `GATE_NAMES` (line 92) is the same seven names; the child launch is still
  `[sys.executable, str(mirror / name), "--selftest"]` with `shell=False` (line 720), the mirror is
  still built by `shutil.copy2` + `copytree` of the same paths (703–704), and `battery_paths` still
  means *7 scripts + fixtures tree only* (line 159, `28` hashed paths). No gate is modified or
  executed differently by the new code — its docstring states the check "reads bytes only", and the
  code I read matches that (baseline inspection compares digests; it never re-runs a gate).
- **Full battery, pre-extension revision** (`TMPDIR=/dev/shm python3 tools/check-gate-battery.py`):
  exit 0; `summary {battery_exit: 0, fail: 0, pass: 7, unevaluable: 0}`;
  `originals {added: 0, deleted: 0, modified: 0, preserved: true, files_hashed_before: 28, files_hashed_after: 28}`;
  `findings []`; report sha256 `5651b47a0810817d1a24b8e9303eb0be3038c886a4b026e672ee298f6c946f05`.
- **Runner selftest, both revisions:** `python3 tools/check-gate-battery.py --selftest` → exit 0,
  stdout sha256 `03f14e3d2d16fd7b0203631b8031a84e216fed1568e55ba257ad1596e96569cf` — byte-identical
  *before* and *after* the extension, and equal to the values pinned by round 5
  (`reports/round-5/validation.json:236`) and round 8 (`reports/round-8/operability/audit.md:92`;
  `reports/round-8/operability/battery-rerun.json`). The extension disturbed no existing behavior
  surface of the runner.
- **Independent tamper/could-not-evaluate drill** on a copy (`/dev/shm/r9o19/drill/tools/`, the
  extended runner run against a copy of the gates tree): untampered copy with 3 baselines present
  → **exit 2**, `baselines.summary {baselines_found: 3, pinned: 3, unevaluable: 0, gates_covered:
  [costume, lexicon, phonology], gates_uncovered: [handoff, myth, naming, provenance]}` with four
  `BASELINE-GATE-UNCOVERED` findings — an incomplete baseline set is never a green pass. After
  appending one byte to the costume snapshot's `packet.yml` → **exit 2**,
  `readings {pinned: 2, snapshot_tampered: 1}`, finding `BASELINE-TAMPERED` with detail
  `packet.yml: digest 887e1d544a0f25fe… does not match the pin 36d92113d0cb8e04…`. This is
  adjacent support for claim O's tamper clause measured by an auditor, not the O18/O20 baseline
  re-run mandate, and it binds only revision `50f576c5`.

## 6. Documented exceptions and contested scope

- **Gate sources: no exceptions are needed, because there are no changes.** Nothing in the round
  required a "gate behavior change with a documented reason".
- **Runner change is documented and authorized**, but its owning fragment
  (`reports/round-9/baselines/registry.md:146`) self-declares the row *pending* and says it "must
  be re-measured after O15 lands" — at my close the file was still changing, so **no verdict here
  binds the runner's delivered bytes**. The parent should treat the runner rows of the O claim as
  unsettled until quiescence and re-run the counting command then.
- **Baseline-root divergence (reported, not absorbed).** The extended runner discovers baselines
  only under `tools/gates/{expected,frozen}` (`BASELINE_ROOTS`, line 114). Baselines are landing in
  three roots: `tools/gates/expected/<gate>/r9-pre/`, `tools/gates/frozen/<gate>/r9-pre/`, and
  `reports/round-9/baselines/<gate>/` (seen this window: naming, myth, handoff, phonology). The
  default roots cannot see the `reports/` root, so "7/7 gates carry a committed baseline" is
  currently unreachable through the runner without an orchestrator decision on the root list
  (the registry raises the same item, `reports/round-9/baselines/registry.md:204-214,230-233`).
  Ownership of that decision is the orchestrator's; I record the conflict and the measurement.
- **The added-data set was not quiescent during the audit.** The handoff baseline directory was
  present at `tools/gates/frozen/handoff-packet-check/r9-pre/` at 17:49:36, absent at my 17:52
  `find` (its files then living under `reports/round-9/baselines/handoff-packet-check/`), and
  present again at the 17:52:36 continuity sample — all three observed, each by its own command.
  No gate byte moved at any point; the *placement* of round-9 data did.
- **`/tmp` is inode-exhausted** (`df -i /tmp` → `tmpfs 1048576 1048576 0 100% /tmp`;
  `mkdir /tmp/r9o19` → `No space left on device`, while `df -h /tmp` showed 8.5G free). Any
  temp-dir-dependent run — including the battery's mirror, which uses `tempfile` unless `TMPDIR`
  is overridden — fails without redirection. All my scratch lived in `/dev/shm/r9o19/`. Two other
  seats measured the same condition independently (`reports/round-9/baselines/phonology-sanity-gate/rerun.md`;
  `reports/round-9/baselines/registry.md:16-18`).

## 7. Limits

- Window-bounded: the verdict binds 2026-10-17 17:48:49 – write time, and the gate-tree hashes in
  §2/§3. The tree was live; re-sweep after quiescence (the assignment's own precondition).
- Byte identity plus sampled behavior is strong evidence of unchanged behavior, but it is not a
  proof that no writer rewrote a gate with identical bytes — the battery's own documented caveat.
  The mtime evidence in §2.1 is consistent with exactly that class of event during the round-8
  window and shows no round-9 occurrence.
- I did not re-run the baselines' verdict replay or re-derive their digests (O18/O20 scope). My
  drills bind one runner revision as stated.
- No claim here about D3, freshness, metadata or canon; other seats own those.

## 8. Receipts (commands, 2026-10-17, lane root)

```
git diff --stat e1694ba HEAD -- tools/gates/                     # empty
git diff --stat e1694ba -- tools/gates/                          # empty
git diff --stat -- tools/gates/                                  # empty
git status --porcelain -uall -- tools/gates/ | awk '{print $1}' | sort | uniq -c   # 9 ?? at 17:52; 33 ?? at 17:52:45
for f in $(git ls-tree -r e1694ba --name-only -- tools/gates/); do compare blob vs hash-object; done  # 61 MATCH, fail=0
python3 tools/gates/<gate>.py --selftest      # 7 gates, exit 0 at T1 and T2, stdout cmp-identical
python3 tools/gates/<gate>.py {bad.yml,empty.yml,nosuch.yml}   # 21/21 exit 2 at T1 and T2
TMPDIR=/dev/shm python3 tools/check-gate-battery.py            # exit 0, pass 7, preserved true (round-8 bytes)
TMPDIR=/dev/shm python3 tools/check-gate-battery.py --selftest # exit 0, stdout 03f14e3d… (both revisions)
<extended battery on copied tree, untampered>                  # exit 2, gates_uncovered ×4
<extended battery on copied tree, one tampered byte>           # exit 2, BASELINE-TAMPERED (snapshot_tampered)
df -i /tmp                                                     # 1048576 1048576 0 100% /tmp
```

**Write-time re-check, 2026-10-17T17:52:45-03:00** (run immediately before this file's last edit):
the three diff scopes above were re-run and are still empty, per-file blob comparison against
`e1694ba` reports `blob mismatches at write time: 0`, the gate-tree status is additions-only
(`33 ??`, no `M`, no `D`), and the fixture subtree is still untouched. The audit verdict holds at
the close of my window; anything a later writer lands is outside it.

This fragment is uncommitted at handoff (the orchestrator integrates once per round). Its sha256
at the 17:52:45 measurement snapshot, before the three accuracy edits that followed (full digests
for three gates, the untracked-count growth, this section), was
`d81574c039b5871493e782ac4b4e178028ca5b8e131dd1fbbe049bfaca0af8f2`; the parent should re-derive
the delivered-digest with `sha256sum reports/round-9/baselines/audit-19.md` rather than trust a
self-reported hash.
