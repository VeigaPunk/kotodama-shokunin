# RevScorecardCorrections — kotodama round 74, WAVE 2 (falsify), hyaku run 7

PASS/FAIL is not mine to emit. The assigned object: the claim-Ca landing
`5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3` — `SCORECARD.md` `## Corrections — round 74`
(section :1436, rows :1442-1453), the `SKILL.md` line-594 repair and the three appended
gate rows (:705, :706, :707) — plus claim C's counter run through its own gate row.

- Lane repo (read-only git; every graded run inside a throwaway clone): `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
- Base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; operative freeze `00c408a0af2fa5ddf65af2224152ce258b26d896`; claim-Ca lands `5e4796c0…`; claim-C lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`; lane main at dispatch `1d7add3` (telemetry/LOG/SCORECARD/report-side only after the freeze; `SCORECARD.md`/`SKILL.md` unchanged after `5e4796c0`).
- Frozen claims/ledger read at the freeze (`claims.json`, `ledger.json`), never from the graded tree.
- No tool installed or upgraded; pacman not run. No network fetch, so no UA is recorded.
- Seat-hygiene disclosure: my first write of this report resolved the relative `Report:`
  path against the workspace root and created
  `/home/vgpnk/Projects/shokunin/.ufo/waves/round-74/w2/RevScorecardCorrections.md`
  (fleet root) instead of the lane. Corrected at 23:19 by `mv` to the assigned path and
  `rmdir` of the two directories the write created; the fleet path is gone
  (`ls: cannot access '/home/vgpnk/Projects/shokunin/.ufo/waves/round-74'`), and the only
  untracked entry left under the fleet's `.ufo/waves/` is a pre-existing `round-30/` that I
  did not touch. This report exists only at
  `kotodama-shokunin/.ufo/waves/round-74/w2/RevScorecardCorrections.md` (no other file under
  either tree was written by this seat).

**Verdict summary.** The 12 correction rows themselves are honest: every re-derivation
command returns the stated new token, every old token is verbatim at its `stated_at`
line in the base tree, the corrections section is append-only, and the Ca counter
prints `ACCEPT-CA-74: PASS legs=11/11` at its lands. Nine defects survive in the
landing's own record: the two round-74 gate rows carry four factual defects — a stale
counter sha256/selftest count (F1), a misdescribed refusal contract (F2), a documented CLI
that cannot reach PASS in a clone (F3), and a miscount of the observe allowlist (F4); the
frozen ledger and the lesson contradict the landed disposition of LC-01 (F5); the ANNOTATE
leg does not do what its sentence says (F6, **demonstrated with a passing junk landing**);
one note-row premise is anachronistic (F7); the round-70 registry-count invariant is only
true under a kind filter (F8); and the RECEIPTS leg was observed to be non-deterministic (F9).

---

## Findings

### F1 — HIGH — `accept-ca-74` gate row states a counter sha256 and a selftest result that no shipped byte produces; the receipt it names says otherwise

`SKILL.md:706`, selftest cell:

> `… --selftest` — measured at counter sha256 `76d00b88325f…`: exit 0, `SELFTEST OK: 138 checks across 37 scenarios reported-fail=0`; receipt `reports/round-74/telemetry/selftest-ca.txt`

Evidence (cwd lane):

```
$ git log --all --format=%H -- reports/round-74/accept-ca.py    # then sha256 per rev
00c408a 8052f1e25c366a18ccb28e1c47931fd1cdd91db042153fdda570fd9f0fa8470f
11dae66 8052f1e25c366a18ccb28e1c47931fd1cdd91db042153fdda570fd9f0fa8470f
08bb555 26dd04a4971e6dcee4bd7a021ef9f876a93a0ea2c2f27943ff60539c11c0fe53
3595c91 26dd04a4… b1ad644 26dd04a4… ab0994b 26dd04a4…
703571c dd755893f72cb8e93b8c53577188ad3b868bd3367c76b0ab789e19227ca520ec
d0f86d6 dd755893… de93d91 dd755893… f8cf250 dd755893…
```

No committed revision of the counter hashes to `76d00b88…` (the string survives only in
wave-1 drafts — `.ufo/waves/round-74/drafts/skill-gates-rows.md:11,132,143` and
`ScribeSkillGates.md:165,177`, where the seat itself wrote *"the current bytes are
`2ddebefcb1de…`. Re-run the selftest at freeze and file `selftest-ca.txt` from those
bytes if they differ."*). At the landed bytes:

```
$ sha256sum reports/round-74/accept-ca.py
8052f1e25c366a18ccb28e1c47931fd1cdd91db042153fdda570fd9f0fa8470f  reports/round-74/accept-ca.py
$ python3 -B reports/round-74/accept-ca.py --selftest | tail -1; echo EXIT=$?
SELFTEST OK: 179 checks across 41 scenarios reported-fail=0: do-nothing, clean, …
EXIT=0
$ python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0… --freeze 00c408a… --fleet-root … | head -1
# counter sha256 (self): 8052f1e25c366a18ccb28e1c47931fd1cdd91db042153fdda570fd9f0fa8470f
```

`reports/round-74/telemetry/selftest-ca.txt` (the receipt the row names) ends
`SELFTEST OK: 179 checks across 41 scenarios reported-fail=0` — the row's own receipt
contradicts its stated numbers. The row also fails the round's own lesson, which records
the correct figures: `corpus/lessons/round-74.md:175` (R74-M8) says `179 checks across 41
scenarios`.

Proposed fix: replace the sentence with `measured at counter sha256 8052f1e25c36…: exit 0,
SELFTEST OK: 179 checks across 41 scenarios reported-fail=0` (receipt `selftest-ca.txt`).
The stale `76d00b88…` belongs in the wave-1 draft, not in the gate registry.

### F2 — MEDIUM — both round-74 gate rows misdescribe the refusal contract: the verdict line is not printed for the input-error class

`SKILL.md:705`:

> A refused run prints `ACCEPT-C-74: FAIL legs=0/13 (refused: …)` and exits 2: missing, malformed or tree-absent `--lands` or `--freeze`; `--root` without `.git`; `lands` equal to the frozen base; unreadable frozen `claims.json`; … LEGCOUNT; … a materialization failure.

`SKILL.md:706`:

> Refusals print `ACCEPT-CA-74: FAIL legs=0/11 (REFUSED: …)` and exit 2: missing or malformed `--lands` or `--freeze`; missing or non-directory `--fleet-root`; an absent revision; `lands` equal to the frozen base; an unreadable frozen `ledger.json` or `claims.json`; or … LEGCOUNT.

Only the `refuse()/_refuse()` class prints that line. Every input-error class prints an
`ERROR:` line on stderr and exits 2 with **no verdict line at all** (measured, cwd clone):

```
$ python3 -B reports/round-74/accept-c.py --root . --lands nothex --freeze 00c408a…
ERROR: --lands must be a 40-hex commit (the worktree is never graded, QUALITY 19)
EXIT=2
$ python3 -B reports/round-74/accept-c.py --root . --lands 1111…1111 --freeze 00c408a…
ERROR: --lands revision not found: 1111111111111111111111111111111111111111
EXIT=2
$ python3 -B reports/round-74/accept-c.py --root . --lands f7104cbc… --freeze 00c408a…
REFUSED: lands f7104cbce186 is the frozen claim base f7104cbce186 (the do-nothing control: no data landed)
ACCEPT-C-74: FAIL legs=0/13 (refused: lands f7104cbce186 is the frozen claim base f7104cbce186 (the do-nothing control: no data landed))
EXIT=2
$ python3 -B reports/round-74/accept-ca.py --root . --lands nothex --freeze 00c408a… --fleet-root /home/vgpnk/Projects/shokunin
ERROR: --lands must be 40 hex
EXIT=2
$ … --fleet-root /nonexistent-xyz
ERROR: --fleet-root /nonexistent-xyz is not a directory
EXIT=2
$ … --lands 1111…1111
ERROR: --lands 1111111111111111111111111111111111111111 is not a commit in …/lane
EXIT=2
$ … --freeze f7104cbc…            # unreadable frozen assets
ERROR: claims file reports/round-74/claims.json is not committed at --freeze f7104cbc…
EXIT=2
```

Source agrees: `accept-c.py:1902` prints the `(refused: …)` verdict only from `refuse()`
(called at :1945, :1947 lands==base, :1952 no-legs, :1954 LEGCOUNT); every other exit 2 is
`print("ERROR: …", file=sys.stderr); return 2` (:1927, :1931, :1937, :1941, :1961, :1981).
`accept-ca.py:1926` likewise, called from :1954, :1964, :2046 only; its input-error exits
are :1941 (`--lands`), :1945 (`--freeze`), :1950 (unreadable frozen assets), :1962 (frozen
base unresolved), :1970/:1974 (materialization), and :2831/:2837/:2841 in `main()`.

Consequence for a seat: the documented misuse produces no `ACCEPT-…: FAIL` line to grep,
so a harness keying on the verdict line reads *nothing* where the row promised `FAIL`.

Proposed fix: split the sentence into the two real classes —
*input errors* (missing/malformed/absent `--lands`/`--freeze`; `--root` without `.git`;
non-directory `--fleet-root`; unreadable frozen assets; materialization failure) print
`ERROR: …` on stderr, exit 2, no verdict line; *refusals* (`lands` == frozen base;
frozen leg-table mismatch, LEGCOUNT; for Ca additionally `freeze == lands` with every
leg green) print `ACCEPT-…: FAIL legs=0/N (REFUSED|refused: …)` and exit 2.

### F3 — MEDIUM — `accept-c-74`'s documented CLI cannot reach `PASS` outside the fleet-sibling layout; the row omits `--fleet-root`

`SKILL.md:705` documents `python3 -B reports/round-74/accept-c.py --root . --lands <40-hex> --freeze <40-hex>`
and asserts the output ends `ACCEPT-C-74: PASS legs=13/13` (exit 0). Measured in a
throwaway clone at the C lands (cwd clone, local `main` = lands):

```
$ python3 -B reports/round-74/accept-c.py --root . --lands c4bf61a8… --freeze 00c408a…
LEG FAIL CENSUS
     census script not found: /tmp/<clone>/scripts/sources-census.sh
ACCEPT-C-74: FAIL legs=12/13
$ python3 -B reports/round-74/accept-c.py --root . --lands c4bf61a8… --freeze 00c408a… --fleet-root /home/vgpnk/Projects/shokunin
ACCEPT-C-74: PASS legs=13/13
```

The counter resolves the census script as `<fleet-root>/scripts/sources-census.sh`
(`accept-c.py:1447-1450`) and defaults `fleet_root` to `dirname(root)` (`:1962`); it
accepts an explicit `--fleet-root` (`:1916`). Inside the lane worktree the default
happens to resolve; in any materialized clone it does not. The assignment's own canonical
counter form carries `--fleet-root /home/vgpnk/Projects/shokunin`; the gate row and the
claim's `counter` field do not.

This is precisely the defect the same landing annotates for round 73: `SKILL.md:707`
correction (2) — *"`accept-c-73` reaches `PASS legs=11/11` at its lands only when the
census script is named"*.

Proposed fix: document the C row's CLI as
`… --freeze <40-hex> --fleet-root /home/vgpnk/Projects/shokunin` and add one clause:
"the census script is resolved as `<fleet-root>/scripts/sources-census.sh` (default: the
lane's parent directory), so a run in a bare clone reads `FAIL legs=12/13` with CENSUS red".

### F4 — MEDIUM — "the ten allowlisted observe executables" — there are nine

`SKILL.md:706`, config cell: `…; the ten allowlisted observe executables; …`

```
$ sed -n '166,167p' reports/round-74/accept-ca.py
OBSERVE_ALLOW = ("git", "grep", "wc", "sha256sum", "ls", "cat", "head", "tail",
                 "cut")
```

Nine entries. The frozen ledger's own grammar R2 names the same nine:
`{git, grep, wc, sha256sum, ls, cat, head, tail, cut}`. Proposed fix: "the nine allowlisted
observe executables".

### F5 — MEDIUM — LC-01's disposition is contradicted by the frozen ledger, the lesson and the landed tree; a known-false line survives

Row `SCORECARD.md:1442` annotates LC-01 `412 → 804` (SHONEN.md:6). The pair's disposition
is `ANNOTATE`, and the landing left the line as filed. But the same frozen ledger tells
the opposite story, and so does the lesson:

```
$ python3 -c "import json;d=json.load(open('reports/round-74/ledger.json'));print([r['id'] for r in d['repair_edits']]);print(d['pairs'][0]['disposition']);print([r['id'] for r in d['annotate_rows']])"
['LC-01', 'LC-09']
ANNOTATE
['LC-02', 'LC-03', 'LC-06', 'LC-07', 'LC-08', 'LC-11', 'LC-12', 'LC-15', 'LC-16', 'LC-17', 'LC-18']
$ python3 -c "import json;d=json.load(open('reports/round-74/ledger.json'));print([s for s in d['inplace_spans']['required_for_this_ledger'] if 'SHONEN' in s][0][:90])"
SHONEN.md: add to the in-place path set with an explicit box-1 span (the `asserted:` line at :6). LC-01 rewrites that line
$ python3 -c "import json;d=json.load(open('reports/round-74/ledger.json'));print([p for p in d['pairs'] if p['id']=='LC-01'][0]['why'][:120])"
SHONEN box 1 is the only statement of registry size … The repair prepends the dated current figure with its own receipt
$ git diff f7104cbce186bc2e1522abf0cfd619cc834628bb main -- SHONEN.md    # empty
$ git show 5e4796c0…:SHONEN.md | sed -n '6p' | cut -c1-160
  asserted: `SKILL.md:20` (Decision table), `:505` (Error patterns), `:564` (Checklist); sources registered in `corpus/SOURCES.md` (412 rows after round 56 …
```

`corpus/lessons/round-74.md:199-200` also calls it *"a REPAIR, since SHONEN is not
append-only"*. So three artefacts (ledger `repair_edits`, ledger `inplace_spans`, lesson)
declare a repair; the pair's grading disposition, `annotate_rows`, the SCORECARD row and
the tree all treat it as an annotation, and SHONEN.md:6 still reads `412 rows` against 804.

The contradiction is not cosmetic: the counter's APPENDONLY derives the allowed in-place
lines from REPAIR pairs only (`accept-ca.py:1375-1391`; the land run prints
`repair-stated_at={'SKILL.md': [594]}`). If the L1 had executed the ledger's own LC-01
`repair_edits` instruction, APPENDONLY would have failed with
`SHONEN.md: changed lines outside REPAIR stated_at lines [6]`.

Proposed fix: delete the LC-01 entry from `repair_edits` and the SHONEN.md line from
`inplace_spans.required_for_this_ledger` (or list LC-01 as REPAIR and land the edit in
both SHONEN.md and the REPAIR set), and align `corpus/lessons/round-74.md:199` with
whichever decision holds. No claim leg changes either way; the record just stops
contradicting itself.

### F6 — HIGH — the ANNOTATE leg does not re-run the row's re-derivation command; a correction row whose printed command is dead passes `ACCEPT-CA-74: PASS legs=11/11`

Frozen leg (claims.json, Ca → ANNOTATE): *"… and the row's re-derivation command is
re-run by the counter and returns the observed token"*. The `SCORECARD.md:1438` intro
restates it: *"each row carries id, old token, new token and the re-derivation command,
which the counter re-runs."*

The implementation never parses or executes the row's command text. `leg_annotate`
(`accept-ca.py:1303-1342`) requires only that the row *contains* the stated and observed
tokens as substrings, then runs the **ledger pair's** `observe_cmd`/`rederive_cmd`
(`rederive_argv(pair)`); `leg_nostub` (`:1492-1507`) requires only that the ledger's
`rederive` string occurs in the row (`cmd not in nr → lacks "rederive-cmd"`).

Three mutation runs in a throwaway clone at lands `5e4796c0` (each: edit the LC-11 row,
commit, `git branch -f main <mutant>`, run the frozen counter):

| mutant | row cell as landed vs mutated | shell run of the printed cell | counter |
|---|---|---|---|
| M1 `84cd52b5…` | real command replaced by `git grep -c -E 'NO-SUCH-TOKEN' … -- corpus/SOURCES.md` | rc=1, no output | `LEG PASS ANNOTATE` / `LEG FAIL NOSTUB` → `FAIL legs=10/11` |
| M2 `3c94fb45…` | bogus command **+ ` ; ` + the ledger command** | prints the token (second command) | `LEG PASS ANNOTATE` / `LEG PASS NOSTUB` → `FAIL 10/11` on RECEIPTS twice, then `PASS 11/11` (F9) |
| M3 `8268849f…` | `git grep -c -E 'NO-SUCH-TOKEN' … -- corpus/SOURCES.md  # <ledger command>` | **rc=1, no output** (the real command is commented out) | `LEG PASS ANNOTATE` / `LEG PASS NOSTUB` / `LEG PASS RECEIPTS` → `ACCEPT-CA-74: PASS legs=11/11` |

M3 is the falsification: a correction row that, exactly as printed, returns nothing at all
passes the whole counter, including the leg whose sentence says that command is re-run and
returns the observed token. A junk landing of the round-73 class (R74-M3, *"junk landings
pass"*) is still passing inside the record that claims to close it.

Scope note: the 12 landed rows are honest — I ran every printed command and every one
returns its stated new token (see "Attacks that failed" A1). The defect is the predicate,
not the data.

Proposed fix: in `leg_annotate`, take the row's fourth cell, run it through the same H2
guard used for observe argv (`observe_problem`), execute it in the lands clone, and require
its stdout to parse to the observed token; reject any cell containing a shell metacharacter
(`#`, `;`, `|`, `&`, `$(`, backtick) — the ledger's own R2 already forbids them in argv.
Cheaper alternative that is still honest: reword the leg and the SCORECARD intro to "the
row names the ledger's re-derivation command verbatim (substring) and the counter re-runs
the ledger argv", so the predicate matches the code.

### F7 — LOW — `SKILL.md:707` correction (3) explains a measurement-time state as if it were the landing state

Row text: *"… the documented form reads `FAIL legs=8/9` (STAMP) because lane `main` is
`f7104cb…`."* At the measurement (`ExecReceiptRerun73.md`, receipt
`.ufo/waves/round-74/w1/receipts/measures-ca73-at-lands.txt:9,24,150`) lane `main` was
`f7104cb…`; at the landing `5e4796c0` (one commit after the operative freeze, whose parent is
`00c408a…`) lane `main` was `00c408a…`, and today it is `1d7add3…`. The row's other two
corrections hold (see A8).
Proposed fix: "… because lane `main` was `f7104cb…` at that read (it must now be passed as
`--main <lands>`)".

### F8 — LOW — the round-70 registry invariant survives only under a `kind` filter; a naive row count now reads 46 vs 45, and three rows print two-line commands

Round-70's invariant (`corpus/lessons/round-70.md:22`): *"the landed table has exactly 36
rows matching the 36 enumerated counter files"*.

```
$ awk -F'|' '/^\| accept-[a-z]+-[0-9][0-9]/{print $2}' SKILL.md | wc -l        # naive count
46
$ find reports -name 'accept-*.py' | wc -l
45
# filtered on the kind cell == gate:
gate rows: 45 counter files: 45
rows without a counter file: []   counter files without a row: []   duplicate row ids: []
(at base: 43 naive rows == 43 files)
```

The invariant holds (bijective) when rows are filtered on `| gate |`, because the third
appended row is `| accept-c-73 / accept-ca-73 correction | note | …` — its first cell
starts with an accept id, so any check that counts table rows by first cell now reads 46
against 45 files. Separately, rows LC-15/LC-17/LC-18 (`SCORECARD.md:1450,1452,1453`) print
commands that return **two** lines (the historical revision and the pinned base, e.g.
`…:corpus/SOURCES.md:724` then `…:corpus/SOURCES.md:804`); the row's "new token" is only
selectable through the ledger's `parse` (keyed on the revision literal), which the row does
not say.

Proposed fix: give the note row a first cell that is not an accept id (e.g. `note-73`), or
extend the invariant check to the `kind` cell explicitly; and add "read the line for the
named revision" to the three two-line rows.

### F9 — MEDIUM — the RECEIPTS leg was observed non-deterministic (same command, same revision, FAIL twice then PASS), and its failure detail discards the re-run's stderr

Three consecutive runs of the identical frozen counter command at the same lands
(`3c94fb45…`, my in-clone mutant M2 — but the leg re-runs round-73 artefacts only, so the
mutant is not the cause):

```
run A: ACCEPT-CA-74: FAIL legs=10/11        (ANNOTATE and NOSTUB both PASS)
run B (same command, immediately after): LEG FAIL RECEIPTS
     rev=2d1cd9140d3a receipts=['accept-c-73=50c60bb67f16', 'accept-ca-73=864c94192854']
     problems=['accept-ca-73 re-run exit=2 (want 0)', "accept-ca-73 re-run did not print 'ACCEPT-CA-73: PASS legs=9/9'",
               'reports/round-74/telemetry/accept-ca-73-at-lands.txt: committed stdout differs from the re-run (55544779204d vs e3b0c44298fc)']
ACCEPT-CA-74: FAIL legs=10/11
run C (same command, next): LEG PASS RECEIPTS → ACCEPT-CA-74: PASS legs=11/11
$ # identical direct re-run of the round-73 counter, in a clone of the same source:
$ python3 -B reports/round-73/accept-ca.py --root . --lands 2d1cd914… --main 2d1cd914… --fleet-root /home/vgpnk/Projects/shokunin
ACCEPT-CA-73: PASS legs=9/9    EXIT=0
```

`e3b0c44298fc…` is the sha256 of empty bytes: the re-executed `accept-ca-73` wrote nothing
to stdout and exited 2, i.e. it failed on an input/materialization path before grading. The
round-73 counter's own materialisation prints `ERROR: clone of … failed` / `ERROR: checkout
… failed` / `ERROR: clone HEAD … != …` and returns 2 (`reports/round-73/accept-ca.py:297-308`
at `2d1cd914`) — exactly this signature, i.e. a transient `git clone`/checkout failure
inside the re-run. The leg captures stderr (`_run_r73_counter`, `accept-ca.py:1738-1743`)
but never reports it, so the receipt cannot say why. This can only produce a false FAIL,
never a false PASS, but it makes a red RECEIPTS line unadjudicable. Cause not identified;
my own environment had no concurrent counter run.

Proposed fix: put `proc.stderr[-200:]` into the problem string, and retry the
materialization/re-run once before grading.

---

## Attacks that failed (the landing survived)

**A1 — every correction row's re-derivation command returns its stated new token.**
Run as printed, cwd lane; the token is the one the ledger's `parse` selects:

| id | command (as printed in `SCORECARD.md:1442-1453`) | raw output |
|---|---|---|
| LC-01 | `git grep -c -E '^. S[0-9]{3}' f7104cbc… -- corpus/SOURCES.md` | `f7104cbc…:corpus/SOURCES.md:804` → **804** |
| LC-02/03 | `git grep -h -o -E 'SELFTEST OK. [0-9]+ scenarios' f7104cbc… -- reports/round-73/telemetry/selftest-r3.txt` | `SELFTEST OK: 10 scenarios` → **10** |
| LC-06/07 | `git diff --shortstat 4b825dc6… f7104cbc… -- 'corpus/knowledge/*/*.md'` | ` 247 files changed, 43426 insertions(+)` → **247** |
| LC-08 | `git diff --shortstat 4b825dc6… f7104cbc… -- 'corpus/knowledge/linguistics/*.md'` | ` 32 files changed, 5689 insertions(+)` → **32** |
| LC-11 | `git grep -h -o -E 'decompress.*23443.*[0-9]+ bytes' f7104cbc… -- .ufo/waves/round-73/w2/ScoutReopenS879.md` | `decompress -> 23443 -> 97656 bytes` → **97656** |
| LC-12 | `git grep -h -o -E 'HAS two status-200 Wayback captures' f7104cbc… -- corpus/lessons/round-73.md` | `HAS two status-200 Wayback captures` → **two** |
| LC-15 | `git grep -c -E '^. S[0-9]{3}' 65fe857… f7104cbc… -- corpus/SOURCES.md` | `65fe857…:…:724` + `f7104cbc…:…:804` → **724** (F8 notes the two lines) |
| LC-16 | `git grep -h -o -E 'wall (present) \("Client Challenge"\)' f7104cbc… -- corpus/lessons/round-73.md` | `wall present ("Client Challenge")` → **present** (ERE grouping; an escaped `\(present\)` would not match — my first run used escaped parens and returned rc=1; the row's form is correct) |
| LC-17 | `git grep -c -E '^. S[0-9]{3}' c5f0992… f7104cbc… -- corpus/SOURCES.md` | `…:728` + `…:804` → **728** |
| LC-18 | `git grep -c -E '^. S[0-9]{3}' 94209e8… f7104cbc… -- corpus/SOURCES.md` | `…:701` + `…:804` → **701** |

**A2 — every old token is verbatim at its `stated_at` line in the base tree.**
`git show f7104cbc…:<path> | sed -n '<line>p'` for SHONEN.md:6 (`412 rows after round 56`),
LOG.md:4297 (`Ca 9 scenarios`), corpus/README.md:732 (`Total knowledge entries: 243.`),
:736 (`(total 243 files; …)`), :344 (`## linguistics/ (30)`), lessons/round-73.md:38
(`(20261025222414, 23443 B)`), :138 (`are reachable and span-present`),
reports/round-73/claims.json:11 (`no Wayback capture of the same page`), README.md:28
(`registry moved 752 → 776 rows.`), :36 (`registry moved 753 → 776 rows.`).
The fleet half of LC-03: `git -C /home/vgpnk/Projects/shokunin show dad39efd…:.ufo/reports/round-73/kotodama.md | sed -n '10p'`
prints `selftests (C 29/29; Ca 9 scenarios)`, and `… show HEAD:… | sha256sum` =
`000bab3a36648498b67b78ea3d7db3f2e8dd17a3ad762aa528d95ef169132bdd` — the pinned bytes.

**A3 — append-only holds.**
`git diff f7104cbc… main -- SCORECARD.md LOG.md | grep '^-[^-]'` → no output (rc=1); the
same over the seven-file protected set (LOG, SCORECARD, lessons/round-74/73/72,
reports/round-73/claims.json, ledger.json) → no output. At lands the counter reports
`protected-removed=0` over the same set (base..lands). All eleven non-LC-09 `stated_at`
lines are byte-identical between base and lands (LC-09 is the one intended in-place repair).

**A4 — the Ca counter passes at its lands.** In my clone with local `main` = lands:
`ACCEPT-CA-74: PASS legs=11/11` (exit 0), `stamped=evaluated=measured=5e4796c0cb6a`,
`PAIR … stated/observed_base/observed_lands` matching each row's old/new token, `LEG PASS
ANNOTATE rows=14 annotate-pairs=12`, `LEG PASS NOSTUB`, `LEG PASS APPENDONLY`,
`LEG PASS SEPARABLE`, `LEG PASS TRACKED`, `LEG PASS RECEIPTS`, `LEG PASS FROZENCFG`,
`LEG PASS STAMP`. (`rows=14` in the ANNOTATE detail is `correction_rows`' list: the 12 data
rows plus the section's intro paragraph and the table header line; the separator and blanks
are skipped, and `row_starts_with_id` keeps only rows whose first cell is exactly the pair id.)

**A5 — the C counter passes at its lands with the canonical form.** `--fleet-root` given:
`ACCEPT-C-74: PASS legs=13/13`. (The flagless form is F3.)

**A6 — the SKILL.md:594 repair is exact and minimal.**
`git diff f7104cbc… 5e4796c0… -- SKILL.md` shows one replaced line and three inserted rows
and nothing else: `- … 94 entries: 92 earlier-civilization` →
`+ … 95 entries: 93 earlier-civilization`; lines 592-596 at lands read
`- \`corpus/knowledge/civilizations/\` — 95 entries: 93 earlier-civilization` /
`  bases plus two source maps (\`africa-primary-sources.md\`,` /
`  \`mesoamerica-primary-sources.md\`), each`. Honest: base holds 95 files in that
directory (`git ls-tree f7104cbc… corpus/knowledge/civilizations/ | wc -l` = 95) and
exactly two of them are the named primary-source maps, so 93 base files is right.

**A7 — the row/ledger command binding does catch a wrong command** (it is just weaker than
the leg says): mutant M1 → `LEG FAIL NOSTUB`, `ACCEPT-CA-74: FAIL legs=10/11`.

**A8 — the round-73 correction note's three facts hold.**
(1) `git show af65165:reports/round-73/accept-ca.py | sha256sum` =
`f8ebb5d8…` and its `telemetry/selftest.txt` prints `SELFTEST OK: 9 scenarios`; r3 =
`222d4dd6…` (`git show 2d1cd914…:reports/round-73/accept-ca.py`) and `selftest-r3.txt`
prints `SELFTEST OK: 10 scenarios` after the `ERROR: base 8841ad3b… is not a commit …`
line, with exit 0 (the round-74 counter's own CLI-error scenario shows the same
`ERROR`-before-`SELFTEST OK` shape, which supports reading it as control output).
(2) `measures-c73-at-lands.txt:46,88`: `FAIL legs=10/11` for the flagless form, `PASS
legs=11/11` with `--fleet-root`; the r73 counter resolves `script = census_sh or
os.environ["KOTODAMA_CENSUS_SH"] or <fleet_root>/scripts/…` — one branch, so
`--census-sh` is the same code path as claimed. (3) `measures-ca73-at-lands.txt:58,117`:
`FAIL legs=8/9` documented form, `PASS legs=9/9` only with `--main 2d1cd914…`; the r73
`--main` feeds the `measured` header and STAMP only.

---

## Residual risk and verification gaps

- F6 is a predicate gap, not bad data: all 12 landed rows are correct (A1). The claim's
  kill rule (*"any correction row … whose re-derivation command does not return the
  observed token"*) is therefore not triggered by the landing, but the leg cannot enforce it.
- F9's cause is unidentified (transient `git`/materialization failure inside the re-executed
  round-73 Ca counter, most likely). One false-FAIL window remains open in the RECEIPTS leg.
- I did not re-run the round-73 selftests from source to reproduce the `ERROR … is not a
  commit` control line; I verified it from the two committed receipts and the analogous
  round-74 CLI-error scenario (A8.1). No network was used, so no fetch-hygiene ruling is due.
- Token selection for LC-15/LC-17/LC-18 rests on the ledger's `parse`; I verified the
  selection, not the row's ability to convey it (F8).
