# Filler28 — variant 27 (sentinel): frozen claim-C counting command re-run at lane HEAD in a fresh clone

Seat: `L1Kotodama71.Filler28`, role sentinel, leaf (no spawns). Read-only on the lane; all
mutation probes ran inside a throwaway clone. Findings only.

Measured revision: **`cb772004f813851f5846e63f8d46d6e2ba81e236`** (lane `main` tip at
08:44–08:47; tree `0909cb0737069bb59f478e99642734c66b89952f`), then **re-verified at
`e7e7e2693b66fa67103d986374b618790ce40203`** (tip at 08:52; tree
`2c94402366a669977305bd058b7e72a6f81b4294`) — see §9. The lane tip moved four times during this
seat (see §6), so every result below is pinned to a revision.

---

## 1. Fresh clone

```
$ git clone --no-hardlinks -q /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/f28-clone.x2YuAM/lane
$ cd /tmp/f28-clone.x2YuAM/lane && git checkout -q cb772004f813851f5846e63f8d46d6e2ba81e236
$ git rev-parse HEAD; git rev-parse 'HEAD^{tree}'; git status --porcelain | wc -l
cb772004f813851f5846e63f8d46d6e2ba81e236
0909cb0737069bb59f478e99642734c66b89952f
0
```

Clean worktree, no lane files touched, no `.jj` state carried over.

## 2. Frozen counting command (claim C) — verbatim, at lane HEAD

Command taken byte-for-byte from `reports/round-71/claims.json` → `claims[0].counting_command`
(extracted programmatically, not retyped):

```
find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l; find corpus/knowledge -type f -name '*.md' | wc -l; grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md; python3 -B tools/check-cited-lines.py corpus/knowledge/culture-material/dance-performance-movement-codes.md; test -f corpus/knowledge/culture-material/dance-performance-movement-codes.md
```

Exact output and exit code:

```
36
243
797
CITED-LINES: 0 finding(s) in 1 file(s)
EXIT=0
```

Per-segment exits (same segments, run individually): `cm-files=0`, `corpus-md=0`,
`registry-rows=0`, `check-cited-lines=0`, `entry-exists=0`.

**Verdict: PASS.** Against the frozen target (`culture-material=36`, `corpus=243`,
`registry >= 784+12 = 796`, entry exists, `check-cited-lines` exit 0): every leg holds, and
797 = 784 + 13 rows exactly.

Replication: identical output/exit at three revisions of the lane, so the numbers are stable
across the later commits (claim-C surfaces untouched between them —
`git diff --stat 14c88d9b HEAD -- corpus/ reports/round-71/accept-c.py reports/round-71/claims.json`
is empty):

| revision | tree | frozen-command output | exit |
|---|---|---|---|
| `050a65a2` (jj `@` at start, == `14c88d9b` tree) | `2a9f2ab5` | 36 / 243 / 797 / 0 findings | 0 |
| `ccadb598` | `f1a71950` | 36 / 243 / 797 / 0 findings | 0 |
| `cb772004` | `0909cb07` | 36 / 243 / 797 / 0 findings | 0 |

## 3. Committed counter `reports/round-71/accept-c.py` — same clone, same revision

```
$ python3 -B reports/round-71/accept-c.py --root .
LEG PASS ENTRY        corpus/knowledge/culture-material/dance-performance-movement-codes.md
LEG PASS COUNTS       culture-material=36 corpus=243 (want 36/243)
LEG PASS CITED        distinct S-ids cited=13 (want >=12)
LEG PASS ROWS         missing=[] not-mined=[] usedby-missing=[]
LEG PASS USEDBY-PATHS missing-paths=[]
LEG PASS CITED-LINES  exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
LEG PASS SWEEP        filename-owners=[…dance-performance-movement-codes.md] topic-owners=[…:20:…]
ACCEPT-C-71: PASS
EXIT=0
```

Counter bytes are the stamped ones: `sha256sum reports/round-71/accept-c.py` =
`1df995c2207c50f37f8e1b5187fa7b0cd0e985e54c7667c662105293628d5db4`, equal to the
`# counter sha256 (self):` line of `reports/round-71/telemetry/measures-c.txt`.

Independent re-derivation of the row facts at HEAD (not the counter's own parse):

```
$ awk -F'|' '$2 ~ /^ *S8(6[1-9]|7[0-3]) *$/ {…}' corpus/SOURCES.md
S861|mined|2026-10-25 … S873|mined|2026-10-25        (13/13 rows: status mined, opened 2026-10-25)
$ grep -oE 'S[0-9]{3,}' …/dance-performance-movement-codes.md | sort -u
S861 … S873                                           (exactly 13, no older id smuggled in)
$ grep -oE '^\s{0,3}\|\s*S[0-9]{3,}\s*\|' corpus/SOURCES.md | tr -d ' |' | sort | uniq -d
(empty)                                               (no duplicate row ids)
$ grep -n 'gap filled' …/dance-performance-movement-codes.md
19:- gap filled: … `find corpus/knowledge/culture-material -maxdepth 1 -type f -name '*danc*'` prints nothing, and `grep -rniE '^- topic:.*\b(danc|choreograph|movement culture|performance)\b' …` prints nothing (the unbound variant false-matches "avoidance" …)
$ grep -oE 'S8(6[1-9]|7[0-3])' corpus/lessons/round-71.md | sort -u
S861 … S873                                           (Gate table lists all 13)
```

## 4. Is the PASS non-vacuous? Mutation probes (clone only, reverted each time)

| probe | mutation | declared command | counter `accept-c.py` | discriminating? |
|---|---|---|---|---|
| P1 | S861 used-by → `corpus/knowledge/culture-material/GONE.md` | — | `LEG FAIL ROWS`, `LEG FAIL USEDBY-PATHS`, `ACCEPT-C-71: FAIL`, exit 1 | **yes** |
| P2 | S862 status `mined` → `open` | — | `LEG FAIL ROWS`, FAIL, exit 1 | **yes** |
| P6 | entry file removed | 35 / 242 / 797, `CITED_LINES_ERROR no such file or directory`, exit 1 | `LEG FAIL ENTRY`, `LEG FAIL COUNTS`, FAIL, exit 1 | **yes** |

So the ENTRY / COUNTS / ROWS / USEDBY-PATHS legs genuinely bite. The following probes show
what the counter does **not** bite.

## 5. Findings

### F1 — MODERATE: no registry-count leg; the claim's registry target is unenforced

The frozen target contains `registry >= 784 + 12`. `accept-c.py` has no leg on the registry row
count at all (its ROWS leg only asks that each cited id exist). Demonstrated:

```
# delete two uncited rows S001, S002
$ grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md
795                                   # < 796 → frozen target violated
$ python3 -B reports/round-71/accept-c.py --root .
ACCEPT-C-71: PASS                     # exit 0
```

At HEAD the fact holds (797 ≥ 796), so this is a *counter-coverage* defect, not a false PASS
today; the counter cannot fail the leg the claim declares.

Smallest remediation: add a leg asserting `len(rows) >= 796` (or `>= base_rows + len(cited)`),
so the declared target is the instrument's own predicate.

### F2 — MODERATE: "S ids opened this round" is not implemented

`accept-c.py` parses the row's `status` and `used-by` cells only (no reference to the `opened`
column; `grep -nE 'opened|cells\[9\]' accept-c.py` → docstring line 9 only). Demonstrated:

```
# S861 opened 2026-10-25 -> 2025-01-01
$ python3 -B reports/round-71/accept-c.py --root .
ACCEPT-C-71: PASS   (exit 0)
```

The claim text and the frozen predicate both say "S ids opened this round"; a row opened in a
prior round passes. At HEAD all 13 rows carry `opened=2026-10-25` (verified in §3), so the fact
holds — the *leg* is missing. Smallest remediation: require `opened == <round date>` for every
cited id.

### F3 — LOW (latent): the counter's COUNTS leg is not the declared command

Declared: `find … -maxdepth 1 -type f | wc -l` (all files) and a recursive
`find corpus/knowledge -type f -name '*.md' | wc -l`. Counter: `os.listdir(…)/*.md` at one
level, and a one-level sum over partition dirs. Demonstrated divergence:

```
$ : > corpus/knowledge/culture-material/.probe-note
$ find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l
37                                    # declared command: target 36 → mismatch
$ python3 -B reports/round-71/accept-c.py --root .
ACCEPT-C-71: PASS                     # exit 0
```

At HEAD the two agree (`36` files == `36` `.md`; no nested dirs under `corpus/knowledge`,
verified with `find corpus/knowledge -mindepth 2 -type d`), so this is latent. Smallest
remediation: make the counter shell out to the declared `find | wc -l` (or replicate it exactly,
including non-`.md` files and recursion).

### F4 — LOW/MODERATE: `--lands` is optional and ungraded; the counter emits none of the 17/19 header

QUALITY 19 says "every round counter takes a **required** lands revision (`--lands <40hex>`) and
never grades whatever worktree it happens to sit in". `accept-c.py` declares
`--lands, default=None, help="lands revision (printed, not graded)"`, defaults `--root` to `.`,
and prints no header line:

```
$ python3 -B reports/round-71/accept-c.py --root . --lands 0000000000000000000000000000000000000000 | tail -1
ACCEPT-C-71: PASS        # exit 0 — bogus revision accepted
$ python3 -B reports/round-71/accept-c.py --root . | grep -cE '^# (counter sha256|stamped revision|…)'
0                        # counter emits no 17/19 header line
```

The receipt's six header lines are therefore hand-authored text around the run, not counter
output — nothing in the counter ties the printed verdict to a revision. Smallest remediation:
require `--lands`, resolve `--root` from it (clone or `git show`), and emit the header block from
the counter so the receipt is machine-produced.

### F5 — MODERATE, now CLOSED: claim C's receipt was absent from the tree at `ccadb598`

Observed at `ccadb598` (08:41:59), in the fresh clone:

```
$ git ls-tree --name-only HEAD reports/round-71/telemetry/
census-end.txt census-start.txt controls-c.txt controls-ca.txt controls-d.txt
measures-ca.txt measures-d.txt quarantine-verdicts.md      # measures-c.txt NOT present
$ git show HEAD:reports/round-71/telemetry/measures-c.txt ; echo EXIT=$?
EXIT=128
$ python3 -B tools/check-receipt-seq.py --lands 8c203bd9dd45b42c4b45ecb3afc1b07a23575dbd reports/round-71/telemetry/measures-c.txt
SEQ-… FAIL unreadable
RECEIPT-SEQ: FAIL        # exit 1
```

The receipt existed in the lane worktree (`stat`: mtime 08:35:30) *before* both commits
(`14c88d9b` 08:40:45, `ccadb598` 08:41:59), i.e. it was left out of the tree, not merely
younger than them. Closed by `c21213a` ("commit C receipt (measures-c.txt) …", 08:43:29): at
`cb772004` the receipt is tracked and default-mode `check-receipt-seq` prints
`SEQ PASS stamped=8c203bd9 evaluated=8c203bd9 measured=8c203bd9 equal=True`,
`TREE PASS recorded=ffb5c549 actual=ffb5c549`, `RECEIPT-SEQ: PASS`, exit 0.

### F6 — MODERATE, CLOSED at `7179d6d6`: `--topo` failed on claim C's receipt at `cb772004`; Ca/D passed

QUALITY 19: "Carrier-parentage — the commit that carries a receipt has the stamped revision as
its parent … graded after the records commit with `--topo`". At HEAD:

```
$ python3 -B tools/check-receipt-seq.py --topo reports/round-71/telemetry/measures-c.txt
SEQ-…  PASS stamped=8c203bd9 evaluated=8c203bd9 measured=8c203bd9 equal=True
TREE-… PASS recorded=ffb5c549 actual=ffb5c549
TOPO-… FAIL carrier=c21213ab parent=ccadb598 stamped=8c203bd9
RECEIPT-SEQ: FAIL        # exit 1

$ python3 -B tools/check-receipt-seq.py --topo reports/round-71/telemetry/measures-ca.txt reports/round-71/telemetry/measures-d.txt
TOPO-… measures-ca.txt PASS carrier=3764c2df parent=1d1b4325 stamped=1d1b4325
TOPO-… measures-d.txt  PASS carrier=3764c2df parent=1d1b4325 stamped=1d1b4325
RECEIPT-SEQ: PASS        # exit 0
```

Ca/D were filed in a direct child of their stamped revision; C was filed four commits late
(first-parent chain, `git log --first-parent --format='%h %s' 8c203bd9..cb77200 | tac`:
`8c203bd9 → 1d1b432 → 3764c2d → 14c88d9b → ccadb598 → c21213a → 2166e45 → cb77200`), so its
carrier parent is `ccadb598`, not the stamp. Note the `--lands` mode is structurally
unsatisfiable for any post-records receipt and fails `unreadable` for all three (verified:
`--lands 1d1b4325` on Ca/D → `FAIL unreadable`, exit 1), so `--topo` is the operative leg.

Per QUALITY 19's own limit clause, carrier-parentage "is cited by no frozen predicate", so this
does **not** change claim C's predicate verdict (§2/§3 PASS); it is a criterion-19 telemetry
defect that the lane's own checker grades exit 1 at tip.

Smallest remediation (history is now past `8c203bd9`, so a parent-of-stamp commit is no longer
constructible): re-stamp at the tip whose bytes were actually re-measured — I already produced
that run (§2: 36/243/797, exit 0, tree `0909cb07`) — file it as a new receipt in a child of the
tip, and record the old receipt's carrier-parentage failure in the lesson's correction table
rather than editing the old bytes.

**Closed in the lane at `7179d6d6`** ("re-stamp C/Ca receipts at final HEAD (hardened counters)"):
the C receipt now stamps `64da9e14` (tree `ff803f43`) and its carrier `7179d6d6` has
`64da9e14` as parent. Re-verified at `e7e7e26` (§9): `TOPO PASS carrier=7179d6d6 parent=64da9e14
stamped=64da9e14`, `RECEIPT-SEQ: PASS`, exit 0, for C, Ca and D alike.

### F7 — LOW, OPEN: round-71 lesson "Mistakes" table is structurally broken

At `cb772004` (`corpus/lessons/round-71.md`), and unchanged at `e7e7e26` (orphan now line 62,
blank separators now 51/54/56/58/60/63):

- line 49 is a truncated row: `| attribution |` (class only; evidence/captured-by/fix/state empty);
- lines 50, 52, 54, 56 are separated by blank lines, splitting the table into five one-row tables
  (the file's own Gate table, lines 10–22, is contiguous — so this is not the file's convention);
- line 57 is an orphaned fragment with no leading pipe:
  ` round-70 receipts stamped "measured at lane 6cb51a4+landed edits" while the after-state first exists at acc2d614 (V70-2) | QUALITY criterion 19 | …`

No lane checker flags it: `python3 -B tools/check-gate-quotes.py corpus/lessons/round-71.md` →
`GATE_QUOTES: 0 findings`, exit 0 (the lesson itself records at line 50 that the checker only
parses bullet rows). Smallest remediation: close line 49 into a full row, delete the blank
separators, prefix line 57 with `| ` and give it a class cell.

## 6. Lane tip moved during measurement (context, not a defect)

`14c88d9b` (seat start, jj `@` = `050a65a2`) → `ccadb598` 08:41:59 → `cb772004` 08:46-ish.
`check-receipt-seq.py` reported `head=cb772004 moved_past=True` while the clone's `main` ref still
pointed at `14c88d9b`; the `--topo` run required fast-forwarding the clone's local `main`
(`git branch -f main cb772004`, temp clone only) so that `git log -1 main -- <receipt>` resolves
the real carrier. Any clone-based verifier must do the same, otherwise `--topo` answers
`no_carrier` for a receipt that exists.

## 7. Not verified by this seat (other surfaces)

- Live/Wayback re-opening of the 13 row URLs and verbatim quote presence (RevRows / ScoutReopen
  surfaces).
- Verbatim quote match between each row and the lesson Gate cell (RevGate surface) — I only
  confirmed all 13 ids appear in the Gate table.
- The receipt's extra claims not printed by the counter: `README sweep exit=0 (rows 243 files
  243, header_drift {})`, `census exit=0 (W04=28 same as base)`, `registry=797` — these are
  hand-added lines; `accept-c.py` prints none of them (see F1/F4).
- Claims Ca and D counters beyond the `--topo` contrast in F6.

## 8. Tooling

No installs, no upgrades, no `pacman` use. Only `git`, `python3` (3.14), `bash`, coreutils in
throwaway clones under `/tmp/f28-clone.x2YuAM` and `/tmp/f28b.65kMTW`; the lane was read-only
(`jj st` untracked set unchanged by this seat).

## 9. Final re-verification at `e7e7e269` (lane tip at 08:52, after the re-stamp)

Second fresh clone (`git clone --no-hardlinks` of the lane, `git checkout e7e7e26`, clean,
tree `2c94402366a669977305bd058b7e72a6f81b4294`; local `main` fast-forwarded to the clone HEAD
so `--topo` resolves the real carrier).

Frozen claim-C counting command — **unchanged result**:

```
$ bash -c "<claims[0].counting_command, verbatim>"
36
243
797
CITED-LINES: 0 finding(s) in 1 file(s)
EXIT=0
```

Counter (hardened bytes, `sha256 80b4ca093a1d1c8436c7e5ff8a0fdb4be7f01a6517ac9dfec35cf05577650ed8`):
all seven legs PASS, `ACCEPT-C-71: PASS`, exit 0. The "hardened counters" commit changed exactly
one line of `accept-c.py` versus `cb772004` (the module docstring's sweep sentence:
`git diff cb772004..HEAD -- reports/round-71/accept-c.py` → 1 line), which is why the counter sha
and therefore the receipt had to be re-stamped.

Receipts at `e7e7e26` — all green, F5/F6 confirmed closed:

```
$ python3 -B tools/check-receipt-seq.py --topo measures-c.txt measures-ca.txt measures-d.txt
SEQ-… measures-c.txt  PASS stamped=64da9e14 evaluated=64da9e14 measured=64da9e14 equal=True
SEQ-… measures-ca.txt PASS stamped=64da9e14 …
SEQ-… measures-d.txt  PASS stamped=1d1b4325 …
TREE-… measures-c.txt PASS recorded=ff803f43 actual=ff803f43
TOPO-… measures-c.txt PASS carrier=7179d6d6 parent=64da9e14 stamped=64da9e14
TOPO-… measures-ca.txt PASS carrier=7179d6d6 parent=64da9e14 stamped=64da9e14
TOPO-… measures-d.txt  PASS carrier=3764c2df parent=1d1b4325 stamped=1d1b4325
RECEIPT-SEQ: PASS        # exit 0
$ python3 -B tools/check-receipt-seq.py measures-c.txt reports/round-71/accept-c.py
SHA-… measures-c.txt PASS reports/round-71/accept-c.py recorded=80b4ca09 actual=80b4ca09
RECEIPT-SEQ: PASS        # exit 0
```

Findings re-probed against the hardened counter — **F1, F2, F3, F4 persist unchanged**:

| probe at `e7e7e26` | declared result | hardened counter |
|---|---|---|
| delete uncited rows S001, S002 (registry 795 < 796) | target violated | `ACCEPT-C-71: PASS`, exit 0 |
| S861 `opened` → 2025-01-01 | "opened this round" violated | `ACCEPT-C-71: PASS`, exit 0 |
| extra non-`.md` file in culture-material (declared `find` prints 37 ≠ 36) | target violated | `ACCEPT-C-71: PASS`, exit 0 |
| `--lands` omitted / `--lands 000…0` | QUALITY 19 requires it | both PASS, exit 0; 0 header lines emitted |

F7 persists at `e7e7e26` too (`corpus/lessons/round-71.md` lines 49, 51–63: truncated
`| attribution |` row, blank-separated rows, orphan fragment at line 62 without a leading pipe;
`check-gate-quotes.py` still `0 findings`, exit 0).

**Bottom line for variant 27:** the one frozen claim-C counting command re-runs green at lane
HEAD in a fresh clone (`36 / 243 / 797`, `CITED-LINES: 0 findings`, exit 0), the committed
counter agrees (`ACCEPT-C-71: PASS`, 7/7 legs, exit 0), the receipt is now tracked, sha-pinned
and carrier-parented correctly; the surviving defects are counter-coverage (F1–F4) and a lesson
table integrity break (F7), none of which changes the claim-C predicate verdict.
