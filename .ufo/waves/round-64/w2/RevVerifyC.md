# RevVerifyC — independent verification of `reports/round-64/accept-c.py` (claims C, pre-data revisions)

Scratch: `/home/vgpnk/.cache/hyaku/kotodama-r64-w2/RevVerifyC/` (clone of the lane at
`097c21d`, every control in its own `git clone --shared` copy; lane untouched, no
commit, no index change, no pacman). Tools installed: none. LSP: **unavailable** —
no `lsp` device/server is surfaced (`xd://lsp` → "No such tool … Mounted devices:
ast_edit, debug"), so caller/definition checks were direct source inspection plus
executed controls, not semantic queries; this is recorded as a tooling gap, not used
as proof of absence.

Axes judged: coverage, operability, calibration.

## 0. Counter bytes I verified (sha256, full)

| label | sha256 | where |
|---|---|---|
| rev1 | `4df7b32b430282c81970acf9b6565c6ef96e598038f82ca843a2cace2de08a68` | working tree at wave-2 start (= CriticRevC's frozen snapshot) |
| rev3 (transient) | `073e9716188251773c14c90b26f524454191c1cbf2b41793bfe5b3d4826fd23e` | observed live 2026-10-23 ~23:54 (CriticReceipts' "2A2E") |
| rev3b (current) | `979050ce21fa01758c075745b08bf3ecf7d6e73baad543a1df83f666ecc5de2b` | current working tree; **uncommitted** (`git status` = ` M`) |

`diff rev3 rev3b` is exactly the 2-line move of `row = reg_by_id.get(...)` above its
first use (line 293 before 297). Saved as `accept-c-rev1.py`, `accept-c-rev3.py`,
`accept-c-rev3b.py` in scratch.

Real-lane snapshot also measured (read-only, `python3 -B`):
`corpus/SOURCES.md b92b95818b94…`, `corpus/README.md c131ffd99196…`,
`entry 31f2c307506c…` (81 lines), counter `979050ce…`.

## 1. Control matrix (each line pasted from `results/`)

### 1a. do-nothing (base corpus state) — must FAIL FILE/ROWS/APPEND (+REJECTS/ONEID/NOHARM/SWEEP/LIVE)

rev1 (`4df7b32b`):

```
FILE FAIL unreadable: ... No such file or directory: .../language-socialization-and-acquisition.md
ROWS FAIL bad=['S718:rows=0', ...] checked=26
REJECTS FAIL bad=['S744:rows=0', ...] checked=6
ONEID FAIL bad=[] marks=[] cited_lines=0 cited_lines_tool=exit2 clean=False
RESTATE PASS bad=[] lines=0
HOSTS PASS bad=[]
LINK PASS bad=[]
APPEND FAIL missing_base_lines=0 s687_queued=False base=643 measured=643 +32=False
NOHARM FAIL diff=[]
SWEEP FAIL exit=0 topic_row=False
LIVE FAIL subset=[...] bad=['S718:no_row', ...]
ACCEPT-C-64: FAIL
EXIT=1
```

rev3b (`979050ce`) — identical vector, ONEID now also lists
`citations_exactly_once=False missing=[S718 … S743]`:

```
FILE FAIL …  ROWS FAIL …  REJECTS FAIL …  ONEID FAIL … citations_exactly_once=False missing=[all 26] duplicates=[]
RESTATE PASS bad=[] lines=0   HOSTS PASS   LINK PASS
APPEND FAIL …  NOHARM FAIL diff=[]  SWEEP FAIL exit=0 topic_row=False  LIVE FAIL …
ACCEPT-C-64: FAIL
EXIT=1
```

**PASS (control holds).** This reproduces `telemetry/dry-run-c.txt`
(sha `ff9e65f3…`) leg-for-leg, with the rev3 ONEID detail added. RESTATE/HOSTS/LINK
pass vacuously at `lines=0` — expected, recorded.

### 1b. stub entry + copied rows — must FAIL ROWS + RESTATE

Fixture: 26 lines copied from base `S009` remapped to S718–S743 (tier C, status
queued, `opened 2026-10-19`, no capture, no quote), sourceless stub bullets.

rev1 (`4df7b32b`):

```
FILE PASS  ROWS FAIL bad=['S718:tier=C','S718:status=queued','S718:opened=2026-10-19','S718:recheck=90d','S718:usedby=—','S718:quote_words=0','S718:no_capture', ...]
REJECTS FAIL bad=['S744:rows=0', ...]  ONEID PASS bad=[] … cited_lines=26
RESTATE FAIL bad=['line10:S718:in_order=0', …] lines=26
HOSTS PASS  LINK FAIL bad=['S718:registry_hits=27', …]
APPEND FAIL … measured=669  NOHARM FAIL diff=[]  SWEEP FAIL exit=1
```

rev3b (`979050ce`): same ROWS/REJECTS/RESTATE/LINK/APPEND leg outcomes (`RESTATE
FAIL … in_order=0 … lines=26`); run reached SWEEP then LIVE exceeded my 60 s cap
(fixture's copied `cals.info` URL), so no `ACCEPT-C-64` line was printed for this
fixture. ROWS + RESTATE failure is verified; it fails RESTATE through
`in_order`, **not** through `teaches_copy` or `no_novel_content_word` (the stub
clauses share no quote words but add only novel words).

rev3 transient (`073e9716`) — **violated the declared signature**: it printed
`ROWS FAIL`, then died in RESTATE before any RESTATE verdict (see Finding 1).

The rev3 citation guard is not this fixture's discriminator; its negatives are
§1d below.

### 1c. 26 teaches-copied bullets — must FAIL rev2 RESTATE

Fixture: valid staged rows S718–S743 + S744–S749, S687 flipped, bullets = each
row's `teaches` cell verbatim.

rev3b (`979050ce`) — **PASS (control holds for exact copies)**:

```
ROWS PASS  REJECTS PASS  ONEID PASS citations_exactly_once=True
RESTATE FAIL bad=['line10:S718:teaches_copy','line10:S718:in_order=0',
 'line11:S719:teaches_copy', … ] lines=26
APPEND PASS … base=643 measured=675 +32=True
LIVE PASS subset=['S718','S723','S728','S733','S738','S743'] bad=[]
ACCEPT-C-64: FAIL
EXIT=1
```

Replica of the same guard (same functions, same rows): **26/26 flagged**
`teaches_copy`; on a 3-copy subset only S729/S730/S739 are flagged.

rev1 (`4df7b32b`) — **control absent**: the same fixture gave
`RESTATE PASS bad=[] lines=26`; a replica of rev1's RESTATE shows **5/26**
teaches-copied bullets passing lexically (S723, S729, S730, S739, S740); the leg
only failed overall through incidental `in_order` on the other 21. This is the
CriticClaims false negative, independently reproduced.

**Escape from the rev3b guard (Finding 2):** `teaches cell + " Indeed."`
(`tree-teachesplus3`) gives

```
RESTATE FAIL bad=['line21:S729:in_order=1'] lines=26
```

i.e. S730 and S739 pass RESTATE while carrying the row's teaches narration plus a
tail; replica of the guard flags **0/26** on that fixture.

### 1d. citation coverage — entry citing zero / 25-of-26 / duplicates must FAIL rev3

rev3b (`979050ce`):

```
tree-cite0 : ONEID FAIL bad=[] marks=[] cited_lines=0 cited_lines_tool=exit0 clean=True
             citations_exactly_once=False missing=[S718 … S743] duplicates=[]
tree-cite25: ONEID FAIL … cited_lines=25 citations_exactly_once=False missing=['S741'] duplicates=[]
tree-dup   : ONEID FAIL … cited_lines=26 citations_exactly_once=False missing=['S719'] duplicates=['S718']
```

**PASS.** Rev1 on the same fixtures printed `ONEID PASS cited_lines=0` /
`cited_lines=25` / duplicate-citation PASS, and `RESTATE PASS lines=0` for the
zero-citation entry — the D1 vacuity, independently reproduced.

### 1e. all-26-cited with one beyond-quote bullet — must FAIL RESTATE

rev3b (`tree-beyond`; S735 bullet = six quote words + "holds in every community
and every classroom studied."):

```
ONEID PASS citations_exactly_once=True
RESTATE PASS bad=[] lines=26
```

**FAIL (requirement unmet).** No leg checks support: the clause asserts beyond the
quote and is accepted. `claims.json` declares "sentence support" **review-only**,
so requirement (c) conflicts with the frozen claim's own scope; I record the
conflict rather than call the leg individually broken.

### 1f. faithful land — satisfiability / no over-rejection

Synthetic full land (26 faithful staged bullets + skeleton head, 32 rows, S687
flip, README row and 237→238 / 29→30 / footer bump, committed, `main` = land
commit), rev3b:

```
FILE PASS exists lines=89 h1=1 h2=10 h3=0 topic=True
ROWS PASS  REJECTS PASS  ONEID PASS citations_exactly_once=True
RESTATE PASS bad=[] lines=26
HOSTS PASS  LINK PASS  APPEND PASS base=643 measured=675 +32=True
NOHARM PASS diff=['corpus/knowledge/linguistics/language-socialization-and-acquisition.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=[...] bad=[]
ACCEPT-C-64: PASS
EXIT=0
```

So rev3b is satisfiable and the new guards do not reject faithful bullets. (Same
fixture on the committed rev0 counter: `ACCEPT-C-64: FAIL`, REJECTS rejects
`queued` rows.)

### 1g. real (uncommitted) land, read-only at the snapshot in §0

```
FILE PASS … ROWS PASS … REJECTS PASS … ONEID PASS citations_exactly_once=True
RESTATE PASS bad=[] lines=26 … APPEND PASS base=643 measured=675 +32=True
NOHARM FAIL diff=[]
SWEEP PASS exit=0 topic_row=True  LIVE PASS subset=[...] bad=[]
ACCEPT-C-64: FAIL
EXIT=1
```

11/12 legs pass on the real bytes; NOHARM is the only failure because the land is
not reachable from `main` (Finding 4). The measurement must bind `main` to the
measured commit (or the counter must measure the tree) or claim C can never print
PASS even on a correct land.

## 2. Findings

### BLOCKER (existed in `073e9716`; repaired in `979050ce`; must be captured in the stamped revision)

**F1 — RESTATE used `row` before assignment; any citation-bearing entry crashed the counter.**
In `073e9716`, `teaches = cells(row)[6]` was at line 296 and `row =
reg_by_id.get(sid, …)` at line 300. First well-shaped cited line raises
`UnboundLocalError`; exit 1 with a traceback and no leg/verdict line (contrary to
the docstring's exit contract). Pasted from `results/rev3-tree-teaches.txt`:

```
Traceback (most recent call last):
  File ".../accept-c.py", line 457, in <module>
    sys.exit(main())
  File ".../accept-c.py", line 296, in main
    teaches = cells(row)[6] if row else None
UnboundLocalError: cannot access local variable 'row' where it is not associated with a value
EXIT=1
```

Reproduced on every citation-bearing fixture (teaches, teaches3, cite25, omit,
beyond, dup) and on the stub fixture after `ROWS FAIL` — so rev3 could not print
`RESTATE FAIL` for the declared stub control, and could never print
`ACCEPT-C-64: PASS`. `RevCounters.md` records that no post-edit run was made;
this is the consequence. Current bytes `979050ce` move the lookup to line 293 and
I verified all controls above run without the exception.

### HIGH

**F2 — the rev2 teaches guard is exact byte equality and is trivially escapable.**
`accept-c.py:297-299` (`979050ce`): `teaches = cells(row)[6]`; `clause == teaches`.
Evidence: `tree-teachesplus3` (`teaches cell + " Indeed."` for S729/S730/S739)
prints `RESTATE FAIL bad=['line21:S729:in_order=1'] lines=26` — S730/S739 pass;
the guard replica flags 0/26 on that fixture while flagging 26/26 on exact copies.
A tail word, a case change, or typographic substitution (the guard does not NFKC/
casefold, unlike `norm_words`) defeats it. The forcing control (CriticClaims §)
asked for normalized equality; the implementation compares stripped bytes only.

**F3 — a beyond-quote bullet passes RESTATE (required control (c) unmet).**
`tree-beyond`: `RESTATE PASS bad=[] lines=26` with the S735 clause
"The teacher, through her questions and holds in every community and every
classroom studied." The leg is lexical (quote overlap/order, novelty, copy run);
neither rev2 nor rev3 adds a support check. `claims.json` lists "sentence support"
as review-only, so this is a scope conflict the L1 must resolve explicitly; it is
not satisfiable by moving the row lookup or by normalization alone.

### MEDIUM (inherited, unchanged by rev2/rev3)

**F4 — NOHARM measures refs, not the measured tree.** `accept-c.py:383` runs
`git -C root diff --name-only BASE main -- corpus/knowledge` and requires exactly
`[ENTRY]`. Consequences reproduced twice: (i) the real land in §1g is complete on
disk yet `NOHARM FAIL diff=[]` because `main` is at `097c21d` and HEAD is detached
(`git symbolic-ref` → detached); (ii) uncommitted harm to another knowledge file
is invisible (ReviewerCounterC D2). Fix direction already recorded: diff `BASE`
against the working tree plus `git ls-files --others --exclude-standard`.

**F5 — REJECTS docstring promises a live URL; the leg never reads a URL.**
`accept-c.py:239-252` checks 11 cells, `rejected|queued`, and the
`REJECTED:`/`QUEUED-CANDIDATE: … ; flip:` cell. A URL-less disposition row passes
(both rev1 and rev3b). Doc/code drift, unchanged.

**F6 — APPEND's S687 exception tolerates any single-row rewrite.**
`accept-c.py:373-378`: any one missing base line beginning `| S687 ` is tolerated
and, separately, *some* S687 row must carry `cs[7]=='queued'`; the cells are never
compared, so the anchor/source/scope can be silently rewritten while APPEND passes
(ReviewerCounterC D3; static, unchanged).

### LOW

- `LOCATOR_SHA256 = None` (`:84`) is resolved from `BASE` each run (`:416`); the
  comment says "then hard-code it (rev 3)" but no literal pin exists. The effective
  invariant (working-copy bytes == base bytes) is the intended one; the comment
  overstates it.
- Dead line `it = iter(range(len(qset_seq)))` (`:307`).
- The docstring's leg text for ONEID/RESTATE was not updated to describe revisions
  2–3 (only the separate "Revision history" block does).

### Calibration / evidence fidelity

- `claims.json` controls C names `reports/round-64/telemetry/controls-c.txt` —
  **absent on disk**. The only C telemetry is `dry-run-c.txt` (mtime 19:35,
  sha `ff9e65f3…`), which predates revisions 2/3 and lacks
  `citations_exactly_once/missing/duplicates`; it cannot serve as a rev3 receipt.
- The docstring says the frozen predicate sentence appears "in every receipt"; no
  file in `reports/round-64/telemetry/` contains it (`grep` empty).
- `RevCounters.md` itself states no post-revision counter/control run was made. My
  §1 controls are the first executed evidence for rev2/rev3 and should be committed
  with the stamped revision; the L1 owns that stamp.
- Current `979050ce` is **uncommitted** (` M reports/round-64/accept-c.py`), so no
  revision stamp binds the bytes I verified.

## 3. Frozen predicate verification

`claims.json` predicate (single line):
`ACCEPT-C-64: every leg of reports/round-64/accept-c.py prints PASS.`

Docstring text (lines 55–57) wraps the same sentence across three lines
(`… prints` / `PASS.`). Joined and whitespace-normalized, both strings are
identical (`EQUAL_AFTER_UNWRAP: True`); the literal single-line substring does not
occur in the docstring because of the wrap. No word or punctuation difference.

## 4. Residual risk / verification gaps

- The transient `073e9716` defect was found by execution; I did not patch the lane
  counter, and I did not run 073e9716 against the real land.
- My full green (§1f) is a synthetic fixture; §1g is a real but uncommitted
  snapshot (`entry 31f2c30…`, `SOURCES b92b958…`, `README c131ffd…`). LIVE passed
  on this host in ~7 s; the six-row subset is still network-dependent.
- F2/F3 remain open on the current bytes: exact-copy narration passes when a tail
  word is appended, and a beyond-quote assertion passes RESTATE. Closing either
  needs a counter revision (normalization + a support rule or an explicit
  narrowing of the requirement), not a fixture tweak.
- Fixtures and all raw outputs: `/home/vgpnk/.cache/hyaku/kotodama-r64-w2/RevVerifyC/`
  (`build.py`, `run*.sh`, `results/*.txt`, four counter snapshots).

Report: `.ufo/waves/round-64/w2/RevVerifyC.md`
