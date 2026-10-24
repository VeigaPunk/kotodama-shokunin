# Counter smoke — reports/round-66/accept-ca.py (seat ExecCounterSmokeCa)

Measured object: `reports/round-66/accept-ca.py`, self sha256
`a4b93bf750e997b3ed6185dc3bcf242b460f14068a3c492490fc721879775c11`, at lane main
`94209e8f80969dbac48d56c5d0e2e623635b8616` (base). No counter bytes were edited.

## 1. Required runs (verbatim outcome)

`python3 -B reports/round-66/accept-ca.py --root .` from the lane root, first run:

```
# counter sha256 (self): a4b93bf750e997b3ed6185dc3bcf242b460f14068a3c492490fc721879775c11
# measured revision (lane main): 94209e8f80969dbac48d56c5d0e2e623635b8616
D1 FAIL bad=['live_status', 'quote', 'capture_ts', 's776', 's776_citations=0', 's753_citations=1']
D2 FAIL bad=['reports/round-66/telemetry/final-measures-c.txt:absent', 'reports/round-66/telemetry/final-measures-o.txt:absent', 'reports/round-66/telemetry/final-measures-ca.txt:absent']
D3 FAIL named=65 existing=0 min=8
D4 FAIL complete verdict + run count, no partial
CRITERION FAIL QUALITY criterion 18 names anchor resolvability
QUOTES FAIL exit=2 gate_ids=0 clean=True
ACCEPT-CA-66: FAIL
EXIT=1
```

Re-run after sibling seats wrote drafts (same revision, D3 detail moved):

```
D1 FAIL bad=['quote', 's776_citations=0', 's753_citations=1']
D3 FAIL named=65 existing=7 min=8
... D2/D4/CRITERION/QUOTES unchanged ...
ACCEPT-CA-66: FAIL   EXIT=1
```

`python3 -B reports/round-66/accept-ca.py --help` does **not** crash; exit 0:

```
usage: accept-ca.py [-h] [--root ROOT]
options:
  -h, --help   show this help message and exit
  --root ROOT
```

`python3 -B reports/round-66/accept-ca.py --root /nonexistent` **crashes** (see CS-01).

## 2. Defects, crashes, ambiguities

Each item: path:line → behaviour → minimal fix. "Demonstrated" means a synthetic root under
`/tmp` (no lane bytes touched) reproduced the behaviour; the repro recipe is in §3.

### Crashes / input contract

- **CS-01 crash on unusable `--root`** — `reports/round-66/accept-ca.py:171`
  (`subprocess.run([...], cwd=root)`). `--root /nonexistent` raises
  `FileNotFoundError: [Errno 2] No such file or directory: '/nonexistent'` as an uncaught
  traceback from `main()`, exit 1. Minimal fix: after `root = os.path.abspath(...)` (:76) add
  `if not os.path.isdir(root): print("ACCEPT-CA-66: INPUT_ERROR root"); return 2`; or wrap the
  QUOTES subprocess in `try/except FileNotFoundError` and fail the leg.
- **CS-02 documented exit 2 is never returned** — docstring :34 ("exit 0/1, or 2 on unusable
  input") vs `:184 return 0 if verdict else 1`. All three receipts absent still yields exit 1,
  indistinguishable from a measured predicate failure. `corpus/QUALITY.md:45` (criterion 14)
  requires the 1-vs-2 split for tools of this class. Minimal fix: if every path in `RECEIPTS`
  is absent (or the root is not a git repo), print `ACCEPT-CA-66: INPUT_ERROR` and `return 2`.
- **CS-03 header revision resolves against the process CWD, not `--root`** —
  `:78 mv = subprocess.run(["git", "rev-parse", "main"], ...)` omits `-C root`, while `git_out`
  (:68) correctly uses it. Demonstrated: run from `/tmp` → header prints `unresolvable`; run
  from `/home/vgpnk/Projects/shokunin` → header prints `5695abbee4fb729de6d76a538c9788eaf0531223`
  (the outer repo's `main`) while the lane main is `94209e8…`; both with `--root` pointing at the
  lane. A receipt measured from the wrong cwd is stamped with the wrong revision. Minimal fix:
  `["git", "-C", root, "rev-parse", "main"]`.

### D2 — receipt sequencing (`:108-143`)

- **CS-04 worktree bytes, not carrier bytes** — `:108-113` reads the receipt with `read(root, rpath)`
  and `:135` hashes `read(root, counter_path)`, i.e. the *worktree*, while the docstring (:15-17)
  says the tree and counter sha "resolve against the stamped revision". Demonstrated in
  `/tmp/ca-d2`: commit A (counters), commit B (three **empty** receipt files, parent A), then
  write correct receipt text into the worktree only → `D2 PASS bad=[]` while
  `git show HEAD:reports/round-66/telemetry/final-measures-c.txt` is 0 bytes and
  `git status` shows all three receipts modified-uncommitted. This is the stale-receipt / false
  stamp bypass class. Minimal fix: read the receipt with `git show {carrier}:{rpath}` and the
  counter with `git show {stamped}:{counter_path}` (hash those bytes), or at minimum require
  `git diff --quiet HEAD -- {rpath}` before trusting the worktree.
- **CS-05 vacuous tree line when `rev-parse` fails** — `:130-133`. On failure `tree == ""`, and
  `f"tree: {tree}" not in rtext` becomes `"tree: " not in rtext`, which is a substring of any
  `tree: <anything>` line. It cannot flip FAIL→PASS by itself (the parent check at :124-129 fails
  in the same case) but it suppresses the true cause. Minimal fix:
  `if not tree or f"tree: {tree}" not in rtext: d2_bad.append(...)`.
- **CS-06 parent-equality is a sequencing trap and `main` is not guaranteed to carry receipts** —
  `:121-129` requires the carrier commit's parent to equal the stamped revision. Only one commit
  can be the child of a given revision, so the three receipts either share one receipt-only
  commit stamped at its parent, or must be committed in a chain with a re-measure between each.
  Any commit landing between measurement and integration permanently fails D2. In this lane
  `git rev-parse --abbrev-ref HEAD` is `HEAD` (jj-colocated, detached) and
  `git ls-tree -r main reports/round-66` is empty (0 files): if the L1 integrates via jj without
  moving the git `main` ref, `git log -1 main -- <receipt>` returns nothing and D2 can never
  pass. Minimal fix: measure at integrated revision R and commit the three receipts in one
  commit whose parent is R, moving `main` to it; or relax the leg to
  `git merge-base --is-ancestor {stamped} {carrier}` plus counter blob at `{stamped}`, and state
  in the receipt which ref carries it.

### D3 — dispatch evidence (`:145-155`)

- **CS-07 empty report files and a keyword-only status check pass** — `:146-152`. Demonstrated in
  `/tmp/ca-d3`: eight **zero-byte** files under `.ufo/waves/round-66/w1/` plus a receipt whose only
  status evidence is the seed comment `# seat status: added at integration` →
  `D3 PASS named=8 existing=8 min=8`. `re.search(r"(?i)(seat|report|status)", d3)` (:152) is
  satisfied by the receipt's own header, and the docstring's "per-seat status line; dead seats
  carry a last-error line" (:18-20) is never checked. Minimal fix: require a line shape
  `^(\.ufo/\S+\.md) +(done|partial|dead|no-output)$`, require `last-error:` for non-`done`, and
  require each existing file to be non-trivial (≥200 bytes or carry a `Report:` trailer).
- **CS-08 `len(existing) == reported` contradicts the dead-seat allowance** — `:150-151`. Every
  named path must exist, so one seat that dies without writing a report fails the leg forever,
  even with 8+ good reports — while :18-20 explicitly anticipates dead seats. Minimal fix:
  `len(existing) >= 8` and treat a named-but-absent path as acceptable only when the receipt
  carries its `last-error:` line.
- **CS-09 unescaped dot in the path regex** — `:146 r"(.ufo/waves/round-66/\S+\.md)"`. The leading
  `.` matches any character, so `xufo/waves/round-66/Foo.md` is harvested as `.ufo/...` and then
  fails the file check. Minimal fix: `r"(\.ufo/waves/round-66/[^\s]+\.md)"`.

### D4 — separability bound (`:157-161`)

- **CS-10 a run that never ran passes** — `:158-160`. Demonstrated in `/tmp/ca-d3` with
  `SEPARABILITY: 0 findings` + `acceptance_runs=0 (static-only; partial coverage)` →
  `D4 PASS`. `"PARTIAL" not in d4` is case-sensitive and blind to the tool's own
  `static-only` / `skipped` shapes (`tools/check-claim-separability.py:50` prints
  `SEPARABILITY_PARTIAL`; `:765` prints `SEPARABILITY_UNRESOLVED ... acceptance skipped
  (static-only)`), and `acceptance_runs=\d+` accepts 0. Minimal fix: require
  `acceptance_runs=[1-9]\d*`, reject `(?i)partial|static-only|skipped|UNRESOLVED|UNEVALUATED`,
  and require the receipt to embed the tool's raw stdout block.
- **CS-11 `acceptance_runs=` is hand-typed, not tool-derived** — `grep -n acceptance_runs
  tools/check-claim-separability.py` is empty; the tool reports runs only through its
  `SEPARABILITY`/`SEPARABILITY_PARTIAL` lines. The wrapper receipt therefore carries a number no
  instrument produces — a fabrication surface. Minimal fix: have the tool (or the runner that
  invokes it) emit `acceptance_runs=<n>` derived from its own run counter, and have D4 compare
  that line to the tool's verdict block.
- **CS-12 exact-phrase verdict regex** — `:158 ^SEPARABILITY: \d+ findings$`. Matches today's tool
  wording (`:53` of the tool), but any singular/format change silently fails. Minimal fix:
  `^SEPARABILITY: \d+ finding(?:s)?$`.

### CRITERION — QUALITY criterion 18 (`:163-169`)

- **CS-13 900-character window can false-FAIL a house-style criterion** — `:169`. Demonstrated in
  `/tmp/ca-d3`: `18. … <940 chars filler> anchor resolv` → `CRITERION FAIL`; the same words near
  the start → `PASS`. Criterion 17 (`corpus/QUALITY.md:55`) is longer than 900 characters, so a
  criterion 18 written in the same style can fail on word position alone. Minimal fix: read to
  the next `^\d+\. ` or `^## ` boundary instead of `m.start() + 900`.
- **CS-14 regex matches any `18. ` line anywhere** — `:168 r"(?m)^\s*18\.\s"`. Demonstrated PASS
  with a two-line stub `17. …` / `18. **Durability** — a row anchor must resolv`. Minimal fix:
  restrict the scan to the criteria block (consecutive `^\d+\. ` entries) and require the
  predecessor `^\s*17\.\s` to be present before it.

### QUOTES — lesson Gate (`:170-180`)

- **CS-15 the 25 ids are counted anywhere in the lesson, not in the Gate** — `:174-177`.
  Demonstrated in `/tmp/ca-d3`: a lesson whose `## Gate` holds only `- S001 — https://example.com/x`
  (check-gate-quotes exits 0, `GATE_QUOTES: 0 findings`) and whose **body** line lists S776…S800
  → `QUOTES PASS exit=0 gate_ids=25 clean=True`, contradicting the docstring's "its Gate names
  the round's ids" (:25-26). Minimal fix: slice the lesson from `^##\s+Gate\b` to the next `^##\s`
  and run the id scan on that slice.
- **CS-16 `re.findall` returns the capture group, not the id** — `:174`. `gate_ids` holds suffixes
  (`"776"`, `"800"`), not `S###` ids; the `>= 25` threshold only works because the alternation
  enumerates 25 suffixes. Fragile and opaque in the detail line. Minimal fix:
  `r"\bS(?:77[6-9]|7[89]\d|800)\b"` (non-capturing) and count full matches.
- **CS-17 line-count filler** — `:176 len(lesson_text.splitlines()) > 10`. A stub satisfies it;
  it does not check the Gate/Grounds shape the claim assumes. Minimal fix: require at least as
  many Gate rows as the round's ids, or drop the term.

### D1 — S753 durability (`:89-106`)

- **CS-18 live status check is vacuous** — `:92 if "200" not in d1 or "application/pdf" not in d1`.
  Demonstrated in `/tmp/ca-d3`: receipt whose live line is `status=404`, whose only `200` is
  `response_bytes=200`, and whose `application/pdf` appears in `Accept: application/pdf`
  (a request header) → `D1 FAIL bad=['quote']` only, i.e. `live_status` PASSED. Minimal fix:
  `re.search(r"(?m)^(?:live_)?status=200\b", d1)` and
  `re.search(r"(?m)^content-type=application/pdf\b", d1)`.
- **CS-19 capture timestamp checked by substring only** — `:96-97`. Nothing ties
  `20261024111013` to the `replay_status=200 content-type=application/pdf` line. Minimal fix:
  require one line carrying both, e.g. `re.search(r"(?m)^.*20261024111013.*\b200\b.*application/pdf", d1)`
  (or the receipt's labelled replay line).
- **CS-20 citation regexes are parenthesized-form only** — `:100-101`. A games entry reading
  "supersedes S753" (bare) would pass the "S753 zero" check while still naming S753, and a
  multi-id citation `(S776, S777)` counts as zero and fails. Freeze the intended form explicitly:
  minimal fix `len(re.findall(r"\bS753\b", games)) == 0` and
  `len(re.findall(r"\(S776\)", games)) == 1` (or the corpus one-id-per-line rule from
  `corpus/QUALITY.md:47`, criterion 15).

### Receipt-content findings (owner: the S753 receipt seat, not the counter)

- **CS-21 receipt quote presence changed under the counter run** — the 08:33 draft of
  `telemetry/s753-recapture.txt` contained 0 occurrences of
  `Versions of mancala are traditionally played across Africa and Asia` (`grep -cF` → 0), so D1
  failed `quote`; the 08:35 rewrite adds it at :25 (`grep -cF` → 1) and D1's `quote` sub-check now
  passes. No counter defect; recorded because the counter's quote check is exact-substring and the
  receipt is the only carrier of it. Minimal fix (receipt): keep the verbatim quote line stable
  once the final receipt is measured.
- **CS-22 receipt's old-capture claim is not supported by its own lines** — the 08:35 receipt
  prints `old_capture status=000` (:8) and `old_replay_status=200 size=529795` (:21), then asserts
  at :26 "committed capture 20250926172224 replays 200 application/pdf TODAY". Peer re-probe
  (RevengerIntent, w1/RevengerIntent.md F3/F4; attributed, not re-run by this seat) reports that
  the 200 at :21 is a 302 redirect into the *fresh* capture, that the exact
  `20250926172224id_` request answers 302, and that the CDX old record length is negative
  (`-8498789105` = broken record). Read against that, :26 attributes the fresh capture's bytes to
  the old capture. D1's substring checks cannot see this. Minimal fix (receipt): state the 302 and
  the broken CDX record at :21/:26 instead of "replays 200 application/pdf", and add
  `sha256(live) == sha256(fresh_capture) = cb6ff9b8ef73c176782b12c7b4cada9be63de54feac248069eb009f17e538632`
  as the byte-exactness line — note D1 has no sha/redirect leg, so this line is record-only and only
  a reviewer can hold the receipt to it.
- **CS-23 D1 does not verify the receipt's URL** — `:89-106` never checks that the recapture
  receipt concerns S753's live URL (`penn.museum/.../sowing-seeds.pdf`). Any PDF receipt with the
  right substrings passes. Minimal fix: require the S753 URL string in `d1`.
- **CS-24 live measurement is non-deterministic during the wave** — the same counter run twice at
  the same revision changed D1/D3 details (D3 `named=65 existing=0` → `existing=7`; the D1 receipt
  appeared between runs at 08:33). Receipts must be measured after the tree is quiescent, and a
  receipt over a moving worktree must say so (criterion 17,
  `corpus/QUALITY.md:55`). Minimal fix (process, not code): measure the final receipts after the
  last data commit, on a clean worktree (`git status --porcelain` empty for the read paths).

### Cross-counter constraint

- **CS-25 fixes to accept-ca.py invalidate its own receipts** — `final-measures-ca.txt` must carry
  `counter sha256 (self)` of accept-ca.py, and D2 hashes the same file (:135). If any CS fix above
  lands, all three `final-measures-*.txt` must be re-measured at the revision carrying the final
  bytes, and D2 must be re-derived. The L1 owns this ordering; no fix here was applied.

## 3. Repro recipes (synthetic, no lane bytes touched)

- `/tmp/ca-d2` — git repo, counters copied; commit A, commit B with empty receipts (parent A);
  stamped receipts written to the worktree only → `D2 PASS` with 0-byte committed blobs (CS-04).
- `/tmp/ca-d3` — 8 empty seat files + seed-style receipt → `D3 PASS` (CS-07); receipt
  `SEPARABILITY: 0 findings` + `acceptance_runs=0 (static-only; partial coverage)` → `D4 PASS`
  (CS-10); Gate naming only S001 + body listing S776–S800 → `QUOTES PASS` (CS-15); `18.` with
  `anchor resolv` beyond 940 chars → `CRITERION FAIL`, near the start → `PASS` (CS-13); receipt
  `status=404 … response_bytes=200 … Accept: application/pdf` → `live_status` passes (CS-18).
- `/tmp` (cwd) with `--root <lane>` → header `measured revision … unresolvable` (CS-03);
  `/home/vgpnk/Projects/shokunin` as cwd → header prints the outer repo's `5695abb…` (CS-03).

## 4. What is sound

- `--help` exits 0 and documents `--root`; no argparse crash.
- Missing receipts/lesson degrade to FAIL lines, not tracebacks (except CS-01's `cwd`).
- D2's parent/tree/counter-sha shape matches docstring and criterion 17's intent; the defects are
  byte-source (CS-04) and boundary (CS-05/06) issues, not a wrong model.
- D4's rejection of `SEPARABILITY_PARTIAL` is directionally correct (the tool's token does contain
  the literal `PARTIAL`), but it is not sufficient (CS-10/11/12).
