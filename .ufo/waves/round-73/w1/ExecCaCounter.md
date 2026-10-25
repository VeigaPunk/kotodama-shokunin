# ExecCaCounter — claim-Ca counter draft (round 73, wave 1)

Seat: ExecCaCounter (leaf). Assignment: adapt `reports/round-72/accept-ca.py` into a
ledger-driven counter for the eight frozen legs of claim **Ca** in
`reports/round-73/claims.json` (DRAFT-v0, not edited), exercise it with `--selftest` and
with a 2-pair fixture ledger at `--lands` = base, and report the leg table, the
predicate ambiguities and the fixtures.

## 1. What exists now

| path (relative to the lane) | sha256 | size |
|---|---|---|
| `.ufo/waves/round-73/counters/accept-ca.py` | `8785c6c87dbab3d158f497acd8d586de91f9e4013f2c0a5eba677a33f05b56e0` | 1294 lines |
| `.ufo/waves/round-73/counters/fixture/ledger.json` | `225d8a39e7f1e260b2ddc139b34776e53fcdbed18b774569eb49fc9b6f5628ea` | 40 lines, 2 pairs |

Nothing else was written. `.ufo/waves/round-73/counters/accept-c.py` in the same directory
is a sibling seat's claim-C counter, not mine. Lane git state is unchanged
(`git status --porcelain` shows the same four untracked entries as at seat start:
the two round-72 w1 files plus `.ufo/waves/round-73/` and `reports/round-73/`); no clone,
worktree add, index write, commit or fetch touched the lane.

Design: every graded byte is read from `git show <lands>:<path>` or from a clone
materialized at `--lands` (`git clone --no-checkout` + `checkout --detach`, HEAD and tree
re-derived). The ledger is data: the counter holds no pair set, so freezing the ledger at
freeze does not touch the counter. Per-pair observations run **once** per revision
(`evaluate_pairs`) and every leg consumes that single evidence table; the receipt prints a
`PAIR` line per pair (stated token, observed at base, observed at lands, expected_after).

```
python3 -B .ufo/waves/round-73/counters/accept-ca.py --root . --lands <40hex> \
    --fleet-root /home/vgpnk/Projects/shokunin [--ledger <path>] [--min-pairs N] [--main main]
python3 -B .ufo/waves/round-73/counters/accept-ca.py --selftest
```
Exit 0 all 8 legs pass · 1 any leg fails · 2 input error (bad `--lands`, base absent from
the repo, unreadable ledger, clone/checkout failure, `--selftest` failure).

## 2. Leg table (8 legs, the claim's `legs=<n>/<n>`)

| leg | reads | passes when | planted failure exercised |
|---|---|---|---|
| **LEDGER** | `--lands:reports/round-73/ledger.json` (a worktree read is disclosed and only allowed for an explicit `--ledger`) | round 73, claim `Ca`, `base` == the counter's base, `pairs >= --min-pairs`, unique ids, `disposition ∈ {REPAIR, ANNOTATE}`, `observe_cmd` is a non-empty argv list with no shell interpreter/pipeline/substitution, `parse` compiles with >=1 capture group, `expected_after` non-empty, `stated_at` = `path:line` resolvable at lands, `stated_text` found in that file at lands, stated token anchored in `stated_text` | shell-string `observe_cmd` → `problems=['P1: observe_cmd is not a non-empty argv list']`; 2 pairs under the default 8 → `pairs=2 < min-pairs=8`; ledger absent → `ledger unreadable at reports/round-73/ledger.json and in the worktree` |
| **BASEMISMATCH** | the same ledger, evaluated in a clone at **base** | `>= --min-pairs` pairs whose stated token differs from the observed token at base, and no pair unobservable there | do-nothing control: `found=2 min=2 ids=['P1','P2']`; under default 8: `found=2 min=8` → FAIL |
| **REPAIR** | clone at lands | every `REPAIR` pair observes `expected_after` | `red=["P1(observed='ACCEPT-CA-72: FAIL' expected='PASS')"]`; green case `green=['P1']` |
| **ANNOTATE** | `SCORECARD.md` at lands, section `## Corrections — round 73` | every `ANNOTATE` pair has a row naming id + stated token + observed token at lands; prints `unannotated=` | no section → `no '## Corrections — round 73' section; annotate-pairs=1`; stub row → `unannotated=1 ["P2(stated='entries: 1' observed='2')"]` |
| **APPENDONLY** | `git diff --numstat base..lands` over `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-72.md`, `corpus/lessons/round-71.md`; the fleet round-72 report at the ledger's `fleet_pin`; `-U0` hunks of `SKILL.md` / `corpus/README.md` / `README.md` | zero removed lines everywhere, fleet report blob identical to `fleet_pin` with zero removed lines, in-place hunks only inside `SKILL.md` `## Gates and probes` or a README footer, and every in-place file named by a ledger `stated_at` | removed `LOG.md` line → `lane-removed=2 0\t2\tLOG.md\n4\t0\tSCORECARD.md`; README head rewrite → `corpus/README.md hunk(s) outside footer: ['@@-1,+1']`; authorized registry append → `in-place=['SKILL.md(registry)']` PASS |
| **NOSTUB** | the same rows | each row also carries the re-derivation command (`rederive`, default `shlex.join(observe_cmd)`) and no placeholder token | stub row → `stubs=['P2:stated-token,rederive-cmd']` |
| **SEPARABLE** | the bytes the Ca legs *read*: ledger text, corrections rows naming a pair id, `reports/round-73/telemetry/*ca*` | no `S<id> >= 876` token and no claim-C path; ledger `observe_cmd`/`expected_after`/`parse`/`rederive`/token fields name no claim-C path | not plantable in the fixture repo without editing the counter; scan-set evidence: `scanned=['ledger','corrections-rows','reports/round-73/telemetry/measures-ca.txt']` |
| **STAMP** | the receipt header + the clone | `# counter sha256 (self):`, `# stamped revision:`, `# evaluated revision:`, `# measured revision (lane main):`, `# tree:` all present (grammar of `tools/check-receipt-seq.py`), stamped == evaluated == measured == `--lands`, tree == `git rev-parse <lands>^{tree}`, counter sha == sha256 of the running file, clone HEAD/tree == lands, no `observe_cmd` ran outside the clone | measured != lands (a branch commit under a stale `main`) → `problems=['measured … != lands …']` |

Header shape, verified against the real tool's regexes (not a paraphrase): I loaded
`tools/check-receipt-seq.py` and applied its `STAMPED_RE`, `EVAL_RE`, `MEASURED_RE`,
`TREE_RE`, `SHA_RE` to the fixture receipt — all five matched
(`stamped/evaluated/measured = 8841ad3b…`, `tree = 17c286f5…`, counter sha as above).

## 3. Ledger schema as implemented (superset of the frozen pair shape)

Frozen pair shape (claims.json): `{id, stated_at, stated_text, observe_cmd, expected_after,
disposition}`. The counter accepts that and adds, all optional except the two noted:
`parse` (capture regex over `observe_cmd` stdout), `stated_token` / `stated_parse`
(how the stated token is taken from `stated_text`), `rederive` (human re-derivation command
for the NOSTUB row), and the ledger-level `fleet_pin` (required by APPENDONLY) plus
`round` / `claim` / `base` (required). `observe_cmd` is executed as an argv list with
`cwd` inside the clone, a sanitized environment and a 120 s timeout; a shell interpreter as
`argv[0]`, or `|`, `&&`, `$(` or a backtick in any element, is a LEDGER failure. A nonzero
exit is not by itself unobservable (the token comes from stdout); unobservable =
missing binary, timeout, OS error, or empty stdout with a nonzero exit.

## 4. Predicate ambiguities found (the frozen text does not decide these)

1. **"mismatch pair" at base is undefined.** I formalize it as *stated token ≠ observed
   token at base*, i.e. the self-assessment disagrees with the repo state. It is therefore
   disposition-independent: an ANNOTATE pair is a mismatch at base **and** at lands, and is
   closed by its correction row, not by a repo change. The alternative reading (mismatch =
   `observed != expected_after`) would make every ANNOTATE pair invisible to BASEMISMATCH
   and cannot reach `>= 8` if the ledger annotates rather than repairs. **Ledger owners
   should be told which reading is graded before freeze.**
2. **The frozen pair shape names no "stated token"**, yet ANNOTATE and NOSTUB require one.
   The counter derives it (explicit `stated_token`, else `stated_parse` over
   `stated_text`, else `stated_text`) and **requires it to be anchored in `stated_text`**.
   Consequence for the ledger: an omission-class defect such as R3 (registry rows missing)
   has no sentence asserting its absence, so its pair must anchor on a stated line — e.g.
   `stated_at SKILL.md:<last accept row>`, `stated_text` that row, `stated_token` the last
   accept row's number — not on the absence itself. If the ledger instead wants the
   literal "rows for accept-ca-70..72" as the stated token, the anchor check will reject it
   and the frozen text will need a pre-data correction.
3. **A materialized clone is blind to untracked state — this bites R1 directly.** R1's
   "before" observation is `git ls-files --others --exclude-standard .ufo/waves/round-72`
   (two files). Inside a clone that command is **0 at every revision** (measured:
   clone at base → `0`; live worktree → `2`), so a REPAIR pair encoded that way would read
   green at base and would never count as a mismatch. The gradable predicate is the
   tracked count: `git ls-files <the two paths> | wc -l` (measured at base → `0`, which is
   the honest base observation). The counter emits a NOTE when an `observe_cmd` contains
   `--others`, but the ledger must not use it.
4. **APPENDONLY names no fleet revision.** "the round-72 fleet report (fleet git)" is
   graded against a ledger-level `fleet_pin` (40 hex); without it the leg fails closed.
   For this round the pin is the report's last-touching commit
   `80d8c9b576d45d3c390e1e8edc6c149cfb698483` (fleet HEAD at seat time `9f4bfc49`).
5. **"README footer" and "README" are ambiguous.** The lane-root `README.md` is 14 lines
   and carries **no** `Total knowledge entries` line; the statement R3 cites
   (`Total knowledge entries: 243.`) is `corpus/README.md:732`, whose own footer block
   says "Counts checked 2026-10-25 … (total 243 files; directory totals 30/29/36/29/24/95)"
   while `find corpus/knowledge -type f -name '*.md' | wc -l` = **245** — so the stale
   number is repeated twice inside that footer. The counter authorizes in-place hunks from
   the last `^Total knowledge entries:` line or the last `^## ` heading to EOF (so
   `corpus/README.md` → line 732+, root `README.md` → line 10+), and names that file in
   its detail line so the freeze can see which README the claim means.
6. **`--min-pairs` and the worktree ledger read are control knobs.** `--min-pairs`
   (default 8) exists so a 2-pair fixture can exercise BASEMISMATCH before the real ledger
   is frozen; `--ledger` pointing at an uncommitted path is the only way to read a
   pre-freeze fixture. Both are disclosed in the receipt (`# min-pairs:`, `# ledger: …
   source=worktree-uncommitted`), and the graded run must use the defaults.
7. **ANNOTATE and NOSTUB are vacuous with zero ANNOTATE pairs** (an all-REPAIR ledger).
   The receipt prints `annotate-pairs=0 (vacuous)`; the frozen do-nothing control
   ("stub-row control … FAIL") presumes at least one ANNOTATE pair, so the ledger should
   carry one.
8. **`measured == lands` is gated**, per QUALITY 19's `stamped == evaluated == measured`.
   A run at an older lands than the lane's `main` prints STAMP FAIL — the counter must be
   run before `main` advances past the stamped commit (or with `--main` naming the ref that
   is at lands).
9. **The claim's own `after` string omits `--fleet-root`** (`reports/round-73/accept-ca.py
   --root . --lands <lands>`) while its `counter` line includes it. The counter requires
   `--fleet-root` (this seat's instruction) and fails with exit 2 without it; the frozen
   `after`/`counter` strings should be made to agree at freeze.
10. **R2's sub-clause "a committed receipt carrying a PASS stamp at the stamped revision for
    REPORTCORR+REPORTLAST"** is delegated to the ledger's `observe_cmd` (the counter grades
    only `observed == expected_after`). A shell-free encoding that works in a clone, e.g.
    `["grep","-l","ACCEPT-CA-72: PASS","reports/round-73/telemetry/measures-ca.txt"]` with
    `parse "^(.*)$"` and `expected_after` = that path, keeps the "receipt exists at lands
    and reads PASS" meaning without a pipe. Whatever the ledger picks, the "at the stamped
    revision" part is only checkable through the receipt's own header (STAMP), not through
    this pair.
11. **SEPARABLE's scan set is a choice.** I scan the bytes the Ca legs read (ledger,
    corrections rows that name a pair id, `*ca*` telemetry) and the added in-place lines of
    `SKILL.md`/`corpus/README.md`/`README.md`, but **not** the counter source (it must name
    the claim-C paths it tests for, so a self-scan is incoherent) and **not** `LOG.md`
    (a round-73 LOG entry legitimately describes claim C). At `lands == base` the leg is
    vacuous (empty diff) — the real test is at the lands commit.

## 5. Fixtures

### 5.1 On-disk 2-pair fixture (`.ufo/waves/round-73/counters/fixture/ledger.json`)

Built verbatim from committed bytes at base (`git show 8841ad3:…`), so `stated_text` is
byte-exact; `base = 8841ad3…`, `fleet_pin = 80d8c9b5…`.

| pair | stated_at | stated token | observe_cmd (argv) | parse | expected_after | disposition |
|---|---|---|---|---|---|---|
| `F-R2` | `SCORECARD.md:1401` | `ACCEPT-CA-72 PASS legs=12/12` | `grep -ho 'ACCEPT-CA-72: [A-Z]*' reports/round-72/telemetry/measures-ca.txt` | `ACCEPT-CA-72: (PASS)` | `PASS` | REPAIR |
| `F-R3README` | `corpus/README.md:732` | `entries: 243` | `python3 -c "…rglob('*.md')"` | `^(\d+)$` | `245` | ANNOTATE |

### 5.2 Embedded selftest fixtures (no files; synthetic lane + fleet repos under /tmp)

Nine scenarios, each asserting the exact leg states and the exit code:

1. do-nothing control (lands = ledger commit) → `ACCEPT-CA-73: FAIL legs=5/8`,
   `BASEMISMATCH found=2 min=2`, REPAIR/ANNOTATE/NOSTUB FAIL, APPENDONLY/SEPARABLE/STAMP PASS;
2. clean landing (PASS receipt + corrections row) → `ACCEPT-CA-73: PASS legs=8/8`;
3. stub-row control (row names only the id) → ANNOTATE + NOSTUB FAIL, `legs=6/8`;
4. append-only removal (`LOG.md` line deleted) → `lane-removed=2`, APPENDONLY FAIL, `legs=7/8`;
5. in-place edit outside the footer (`corpus/README.md` head rewritten) → APPENDONLY FAIL, `legs=7/8`;
6. shell-string `observe_cmd` → LEDGER FAIL (`problems=['P1: observe_cmd is not a non-empty argv list']`), `legs=5/8`;
7. the same clean landing under the default `--min-pairs 8` → LEDGER + BASEMISMATCH FAIL;
8. authorized `SKILL.md` registry append + a pair naming `SKILL.md` → `PASS legs=8/8`,
   `in-place=['SKILL.md(registry)']`;
9. CLI input errors → bad `--lands` exit 2, frozen base absent from the repo exit 2,
   unreadable ledger exit 1 with `LEG FAIL LEDGER`.

## 6. Exercised evidence (commands and observed output)

```
$ python3 -B .ufo/waves/round-73/counters/accept-ca.py --selftest
SELFTEST OK: 9 scenarios — do-nothing control (BASEMISMATCH found=2, REPAIR/ANNOTATE/NOSTUB FAIL),
clean landing 8/8, stub-row control (ANNOTATE+NOSTUB FAIL), append-only removal FAIL,
in-place-outside-footer FAIL, shell-string argv FAIL, min-pairs gate FAIL,
authorized SKILL.md registry append 8/8, CLI exit 2 on a bad --lands
exit 0
```

Draft run at lands = base with the fixture ledger (`--min-pairs 2`):

```
$ python3 -B .ufo/waves/round-73/counters/accept-ca.py --root . \
    --lands 8841ad3b896a0227674fa0725b818c999118046f \
    --fleet-root /home/vgpnk/Projects/shokunin \
    --ledger .ufo/waves/round-73/counters/fixture/ledger.json --min-pairs 2
# counter sha256 (self): 8785c6c87dbab3d158f497acd8d586de91f9e4013f2c0a5eba677a33f05b56e0
# stamped revision: 8841ad3b896a0227674fa0725b818c999118046f
# evaluated revision: 8841ad3b896a0227674fa0725b818c999118046f
# measured revision (lane main): 8841ad3b896a0227674fa0725b818c999118046f
# tree: 17c286f5503426a6063a2279c3862fbf3a74c261
# min-pairs: 2
# clone: /tmp/r73-ca-qarwkozn/lands head=8841ad3b…      (base-clone: reused)
# ledger: .ufo/waves/round-73/counters/fixture/ledger.json source=worktree-uncommitted sha256=225d8a39…
LEG PASS LEDGER          pairs=2 min=2
PAIR F-R2 disposition=REPAIR stated_at=SCORECARD.md:1401 stated='ACCEPT-CA-72 PASS legs=12/12'
     observed_base='ACCEPT-CA-72: FAIL' observed_lands='ACCEPT-CA-72: FAIL' expected_after='PASS'
PAIR F-R3README disposition=ANNOTATE stated_at=corpus/README.md:732 stated='entries: 243'
     observed_base='245' observed_lands='245' expected_after='245'
LEG PASS BASEMISMATCH    found=2 min=2 ids=['F-R2', 'F-R3README'] parse-miss=['F-R2']
LEG FAIL REPAIR          green=[] red=["F-R2(observed='ACCEPT-CA-72: FAIL' expected='PASS')"]
LEG FAIL ANNOTATE        no '## Corrections — round 73' section; annotate-pairs=1
LEG FAIL NOSTUB          minimum-shape=id+stated+observed+rederive stubs=['F-R3README:no-row']
LEG PASS APPENDONLY      lane-removed=0 fleet-pin=80d8c9b576d4 blob=ea256ae7f9d7 in-place=none
LEG PASS SEPARABLE       scanned=['ledger'] problems=[]
LEG PASS STAMP           stamped=evaluated=measured=8841ad3b896a tree=17c286f55034 counter=8785c6c87dba
ACCEPT-CA-73: FAIL legs=5/8      exit 1
```

Both mismatches are found at base, which is the do-nothing control's required behaviour;
REPAIR/ANNOTATE/NOSTUB fail because base carries no repair and no corrections section.
The two further controls:

```
$ … --ledger .ufo/…/fixture/ledger.json              (default --min-pairs 8)
LEG FAIL LEDGER          pairs=2 min=8 problems=1 ['pairs=2 < min-pairs=8']
LEG FAIL BASEMISMATCH    found=2 min=8 …
ACCEPT-CA-73: FAIL legs=3/8      exit 1

$ … (no --ledger; reports/round-73/ledger.json absent at base)
# ledger: reports/round-73/ledger.json source=absent sha256=none
LEG FAIL LEDGER          ledger unreadable at reports/round-73/ledger.json and in the worktree
ACCEPT-CA-73: FAIL legs=2/8      exit 1
```

Clone-blindness probe (evidence for ambiguity 3):

```
$ git -C "$D/clone" ls-files --others --exclude-standard .ufo/waves/round-72 | wc -l
0
$ git -C "$D/clone" ls-files .ufo/waves/round-72/w1/ScoutMergeScan.md .ufo/waves/round-72/w1/ScribeLesson.md | wc -l
0
$ git -C <lane> ls-files --others --exclude-standard .ufo/waves/round-72 | wc -l
2
```

(`$D` = `mktemp -d`; the clone was made with `git -C "$D" clone --no-checkout <lane>
"$D/clone"` and checked out detached at base, then removed.)

Also exercised: `python3 -m py_compile` clean; `--lands` without `--fleet-root` → exit 2;
`--fleet-root` without `--lands` → exit 2; `--help` lists the six flags.

## 7. Hand-off notes for main

- **Freeze-time wiring**: the claim's `counter`/`after` strings name
  `reports/round-73/accept-ca.py`. Copying this draft there changes the `# counter:` path
  line and nothing else in the stamp; the STAMP leg re-hashes the *running* file, so the
  receipt must be produced by the copy that will live at `reports/round-73/accept-ca.py`
  (and re-run after any edit — a receipt whose sha does not match the counter fails STAMP).
- **Before freeze**, the two ambiguities that change the ledger's shape must be settled:
  the mismatch formalization (1) and the stated-token anchor rule (2). The R1 pair must use
  the tracked-count predicate (3), and the ledger needs a `fleet_pin` (4).
- **Checks main should run** (this seat ran none of them at a real lands, because no lands
  exists yet): at the frozen lands, the graded invocation above with the default
  `--min-pairs 8` and the default ledger path, then
  `python3 -B tools/check-receipt-seq.py --root <lane> --lands <lands> <receipt> <counter>`
  (expect 0; this seat only verified the header grammar against that tool's regexes), and
  the do-nothing control receipt committed pre-data.
- **Risks**: (a) a ledger whose `observe_cmd` cannot run in a clone (untracked predicates,
  `sh -c`, pipes) fails BASEMISMATCH closed — this is intended but will look like a counter
  bug to the ledger author; (b) the `--min-pairs`/`--ledger` knobs are disclosed but must
  not appear in the graded receipt; (c) STAMP's `measured == lands` gate will fail a rerun
  after `main` advances.
- **Tooling**: no installs or upgrades were needed or made (no pacman, no uv, no fetch). No
  network access was used, so no User-Agent is recorded and no source was ruled unreachable.
