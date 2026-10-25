# ExecSelftestAll — the counters' claims about themselves (round 73, wave 2 FALSIFY)

Seat: ExecSelftestAll. Leaf: no delegation, no background jobs, no `task` spawns, no labrat used.
Item: run both selftests in a throwaway clone, read the selftest code, list every scenario/mutant and
its mapped leg, find legs no scenario or mutant makes fail, and write the smallest scratch mutation
that shows each one can fail.

Base `8841ad3b896a0227674fa0725b818c999118046f`, lands `0316b8883b4f8d44b8efd720140e7f52f734a102`.

Clone provenance:

```
$ D=$(mktemp -d) && git -C "$D" init -q && git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane" \
    && git -C "$D/lane" checkout -q --detach 0316b8883b4f8d44b8efd720140e7f52f734a102
$ git -C "$D" rev-parse --show-toplevel
/tmp/tmp.vwgSyNL6vE
$ git -C "$D/lane" rev-parse HEAD
0316b8883b4f8d44b8efd720140e7f52f734a102
```

`D=/tmp/tmp.vwgSyNL6vE`. Every `git` call in this seat names `-C /tmp/tmp.vwgSyNL6vE/lane`; the only
commits are scratch commits inside that clone, made with `-c user.name=selftest -c user.email=selftest@local`,
and the clone is reset to `0316b888` after every probe (`git -C /tmp/tmp.vwgSyNL6vE/lane rev-parse HEAD`
= `0316b8883b4f8d44b8efd720140e7f52f734a102` at the end). Probe scripts and scratch ledgers live in
`/tmp/ExecSelftestAll/`. No tool installed or upgraded (nothing was needed; `python3` and `git` sufficed).
No live fetch was made, so QUALITY 21/22 UA records do not apply to this seat. The lane write is this file only.
The lane advanced past the claim's lands while this seat ran (`0316b888` → `2d1cd91` → `c1b5b476`, wave-2
orchestrator commits) and `c1b5b47` committed an in-progress copy of this report, so `git status` shows
`.ufo/waves/round-73/w2/ExecSelftestAll.md` modified; I made no commit and no other tracked file changed under
my hand. **Everything graded below is graded at `0316b888`**, the revision the frozen claim names.

---

## 0. Both selftests reproduce

```
$ cd /tmp/tmp.vwgSyNL6vE/lane && python3 -B reports/round-73/accept-c.py --selftest; echo "EXIT=$?"
SELFTEST: 29/29
EXIT=0

$ cd /tmp/tmp.vwgSyNL6vE/lane && python3 -B reports/round-73/accept-ca.py --selftest; echo "EXIT=$?"
… (10 scenario blocks) …
SELFTEST OK: 10 scenarios — do-nothing control (BASEMISMATCH found=2, REPAIR/ANNOTATE/NOSTUB FAIL),
clean landing 9/9, stub-row control (ANNOTATE+NOSTUB FAIL), append-only removal FAIL,
in-place-outside-footer FAIL, shell-string argv FAIL, min-pairs gate FAIL, authorized SKILL.md registry
append 9/9, CLI exit 2 on a bad --lands
EXIT=0
```

Both match the receipts the assignment names (`SELFTEST: 29/29`; `SELFTEST OK: 10 scenarios`).

Real counters at lands, for the baseline the probes are measured against:

```
$ python3 -B reports/round-73/accept-c.py --root . --lands 0316b888… --fleet-root /home/vgpnk/Projects/shokunin
ACCEPT-C-73: PASS legs=11/11
$ python3 -B reports/round-73/accept-ca.py --root . --lands 0316b888… --fleet-root /home/vgpnk/Projects/shokunin
ACCEPT-CA-73: PASS legs=9/9
```

Reproduction caveat (not a defect, disclosed by the counter itself): claim C's declared command carries
no `--fleet-root`, so run from the throwaway clone it prints

```
LEG FAIL CENSUS
     census script not found: /tmp/tmp.vwgSyNL6vE/scripts/sources-census.sh
ACCEPT-C-73: FAIL legs=10/11
```

— the census leg resolves `os.path.dirname(root)`, which is the fleet root only when the lane is graded
in place. Every probe below therefore passes `--fleet-root /home/vgpnk/Projects/shokunin` (read-only use of
`scripts/sources-census.sh`; the counter symlinks the materialized tree into a temp fleet root and writes there only).

---

## 1. Inventory — every selftest check and the leg it is mapped to

### 1.1 `accept-c.py --selftest` = 29 checks (`total = 5 + len(MUTANTS)`, `:1676`)

The five non-mutant checks (`run_selftest`, `:1603-1658`):

| # | check | assertion |
|---|---|---|
| 1 | `r73st-clean` fixture | `"ACCEPT-C-73: PASS legs=11/11"` in stdout **and** `# evaluated revision: <lands>` in the header |
| 2 | do-nothing control (same fixture, `--lands base`) | `"ACCEPT-C-73: FAIL"` present |
| 3 | missing `--lands` | exit 2 **and** `--lands` in stderr |
| 4 | `r73st-claims` (claims.json drives row_set/entries) | PASS 11/11 **and** `# config source: lands tree: row_set, entries` |
| 5 | `r73st-claims-narrow` (row_set minus S880) | `LEG FAIL ROWS` present **and** final FAIL |

The 24 mutants (`MUTANTS` `:1425-1450` / `EXPECTED_FAIL` `:1452-1479`), each built as its own fixture and each asserted
only as `"ACCEPT-C-73: FAIL"` **and** `"LEG FAIL <EXPECTED_FAIL[name]>"` (`:1670-1675`):

| mutant | mapped leg |
|---|---|
| drop_entry | ENTRIES |
| staged_as_is | ROWS |
| usedby_empty | ROWS |
| row_gap | ROWS |
| repoint_url | REPOINTED |
| campaign_id | REPOINTED |
| gate_quote | GATE |
| gate_reject_no_url | GATE |
| gate_no_admit | GATE |
| no_rejects | REJECTS |
| family_missing | REJECTS |
| ground_zero | GROUND |
| receipt_no_exit | SCRATCHMIRROR |
| receipt_in_append | SCRATCHMIRROR |
| collisions | COLLCHECK |
| guard_missing | COLLCHECK |
| map_missing | COLLCHECK |
| multi_id_line | CITEDLINES |
| census_fail | CENSUS |
| junk_rows | ENTRIES |
| evidence_missing | EVIDENCE |
| evidence_notfound | EVIDENCE |
| anchor_no_quote | ROWS |
| placeholder_header | ENTRIES |

So all 11 legs have at least one mutant. The uncovered surface is **inside** the legs (§2.1).

### 1.2 `accept-ca.py --selftest` = 10 scenario blocks (7 dump a full leg table, 1 prints only a title, 2 are silent)

| # | scenario (comment tag) | asserted |
|---|---|---|
| 1 | do-nothing control, `lands = ledger commit` | exit 1; LEDGER PASS; BASEMISMATCH PASS; REPAIR FAIL; ANNOTATE FAIL; NOSTUB FAIL; APPENDONLY PASS; SEPARABLE PASS; STAMP PASS; `found=2` in text. **TRACKED is not asserted** (it is red in that run) |
| 2 | clean landing | exit 0 (which requires `passed==total and total==9`); 8 named legs PASS (**TRACKED not named**) |
| 3 | stub-row control | exit 1; STAMP PASS; REPAIR PASS; ANNOTATE FAIL; NOSTUB FAIL |
| 4 | append-only removal (`LOG.md`) | exit 1; STAMP PASS; APPENDONLY FAIL |
| 5 | in-place edit outside the footer | exit 1; STAMP PASS; APPENDONLY FAIL |
| 6 | shell-string `observe_cmd` | exit 1; LEDGER FAIL |
| 7 | min-pairs gate (silent — no `print`, `:1231-1235`) | exit 1; LEDGER FAIL; BASEMISMATCH FAIL |
| 8 | authorized in-place registry append | exit 0; 9 legs PASS; `in-place=['SKILL.md(registry)']` in text |
| 9 | worktree-only ledger (7b, `:1301-1325`) | exit 1; LEDGER FAIL |
| 10 | CLI input errors (silent) | bad `--lands` → 2; missing ledger → 1 **and** `LEG FAIL LEDGER`; frozen base absent → 2 |

Legs with **no negative scenario**: SEPARABLE, TRACKED, STAMP (§2.2). The declared REPAIR path
(`statement_after`) is also never exercised (§4.2).

---

## 2. Uncovered legs — smallest scratch mutation for each, run

### 2.1 Claim C: sub-clauses no mutant touches

Method: one minimal edit to the landed tree, committed inside the clone, graded with
`--lands <that commit> --fleet-root /home/vgpnk/Projects/shokunin`, then reset. Table is the run output
(script `/tmp/ExecSelftestAll/probe_c.py`, 21 probes, 45 s):

```
probe                    verdict   legs that FAIL                 detail of the leg under test
entry_body_floor         FAIL      ENTRIES                        … body has 7 words (floor 478 = the smallest knowledg
entry_missing_couples    FAIL      ENTRIES                        … header missing: couples
gate_access_date         FAIL      GATE                           S876 row access date missing 2026-10-25
gate_locator_blank       PASS      -                          <<< declared clause, not enforced
evidence_no_fetch        PASS      -                          <<< declared clause, not enforced
evidence_status_403      FAIL      EVIDENCE                       S876 http-status '403' (want 200)
evidence_ua_curl         FAIL      EVIDENCE                       S876 user-agent not recorded as a browser-shaped UA
evidence_sha_short       FAIL      EVIDENCE                       S876 sha256 line not a 64-hex digest
evidence_quote_window    FAIL      EVIDENCE                       S876 quote absent from its own context window
evidence_access_date     FAIL      EVIDENCE                       S876 access-date '2026-10-24'
rows_extra_usedby        FAIL      ROWS                           S876 used-by=['…conlang-methodology.md', '…conlang-scholarship.m
rows_escaped_pipe_only   FAIL      ROWS,CENSUS                    S876 opened='x' … S876 status='mined \' (want mined)
collcheck_regid          FAIL      COLLCHECK                      S876 present in reg-ids (id not free)
collcheck_map_identity   FAIL      COLLCHECK                      map keeps id S876 (arithmetic, not a re-point)
collcheck_map_old_absent FAIL      COLLCHECK                      map old id S999 absent from staged-ids
collcheck_map_drop       FAIL      ROWS,COLLCHECK                 (JSON left invalid by the probe — see note)
collcheck_stale_map      FAIL      COLLCHECK                      stale round-71 map changed base..lands (…)
mirror_no_file           PASS      -                          <<< probe artifact: receipt has two "--file" (see 2.1.2)
mirror_missing_row       FAIL      SCRATCHMIRROR                  receipt does not carry S880
rejects_no_flip          FAIL      GATE,REJECTS                   reject reason+flip columns not recorded in Gate
ground_rowcount          FAIL      GROUND                         receipt names a 798-row registry; base holds 799
```

Round 2 (`/tmp/ExecSelftestAll/probe_c2.py`) isolates the rest:

```
mirror_no_file_all         FAIL      SCRATCHMIRROR      receipt does not show census validate --file
mirror_exit_prose          PASS      -                  <<< declared clause, not enforced
ground_frag_leak           PASS      -                  <<< declared clause, not enforced
collcheck_map_drop_valid   FAIL      COLLCHECK          map records no old->new for S879
guard_receipt_deleted      PASS      -                  <<< the guard-proof receipt is never read
guard_adopted_id           FAIL      COLLCHECK          guard proof …/mirror-a3/corpus/SOURCES.md plants an adopted id S876
base_stray (separate base) FAIL      GROUND             base tree already holds conlang-scholarship files: ['…/conlang-scholarship-old.md']
lands==base (control)      FAIL      all but CENSUS     ACCEPT-C-73: FAIL legs=1/11   (claim's control line, reproduced)
```

Every one of those probes shows the clause is live and falsifiable — except the four marked `<<<`, which are
the subject of §3. Notes on two rows: `collcheck_map_drop` broke the JSON (my edit left a trailing comma), so its
COLLCHECK failure was "not a JSON object"; `collcheck_map_drop_valid` re-ran it correctly and isolated the
`map records no old->new for S879` branch. `mirror_no_file` replaced only the first of two `--file` occurrences;
`mirror_no_file_all` replaced both. `rows_escaped_pipe_only` cannot isolate the escaped-pipe branch: `str.split("|")`
splits on `\|` too, so any pipe shifts the cell indices and the opened/status checks fire first — the escaped-pipe
clause is redundant with them, not independently testable.

`lands == base` reproduces the claim's do-nothing control exactly: `ACCEPT-C-73: FAIL legs=1/11`, only CENSUS green.

### 2.2 Claim Ca: three legs no scenario makes fail

```
separable_sid            FAIL      SEPARABLE,STAMP    scanned=[… 'reports/round-73/telemetry/controls-ca-r2.txt' …
tracked_delete           FAIL      TRACKED,STAMP      paths=2 problems=['.ufo/waves/round-72/w1/ScoutMergeScan.md absent or empty at lands']
stamp_main_at_base       FAIL      STAMP              problems=['measured 8841ad3b896a0227674fa0725b818c999118046f != lands 0316b8883b4f8d44b8efd720140e7f52f734a102']
```

(`separable_sid` = `S876` appended to `reports/round-73/telemetry/controls-ca.txt`; `tracked_delete` = the
must_track file deleted at lands; `stamp_main_at_base` = `git branch -f main 8841ad3b` in the clone. STAMP is
collateral in the first two only because my scratch commit moves `HEAD` past `main`.)

All three legs can fail. So they are not vacuous — they are simply untested by `--selftest`, and STAMP is
mostly tautological by construction: `header = {"stamped": lands, "evaluated": clone["head"], "tree": …,
"sha": sha256_file(__file__)}` (`:902-905`) are all derived from the same `--lands` inside the same run, so the
only genuinely external inputs are `measured` (`git rev-parse main`) and `RUN_STATE["outside_clone"]`.

---

## 3. BLOCKER / MAJOR — clauses the legs declare and the counters do not check

### 3.1 BLOCKER — C `COLLCHECK`: "a 4-space one not found" exists nowhere

The frozen leg (`reports/round-73/claims.json`, claim C, leg COLLCHECK):

> "reg-ids/collisions files hold no adopted id; **guard-proof shows a planted 1-3-space-indented collision
> found and a 4-space one not found**; the regenerated map maps old->new for every adopted id and the
> round-71 map is byte-identical base..<lands>"

The counter's whole indent-guard implementation is:

```
$ sed -n '141p;1036,1056p' reports/round-73/accept-c.py
INDENTED_ROW_RE = re.compile(r"^ {1,3}\|\s*(S\d{3,})\s*\|", re.M)
    # 0-3-space-indent guard: a planted indented collision was detected.
    guard = None
    if os.path.isdir(os.path.join(mat, GUARD_DIR)):
        for rel in tree_files(mat, GUARD_DIR):
            …
            planted = INDENTED_ROW_RE.findall(text)
            if planted and re.search(r"(?i)collision", text) and \
                    re.search(r"(?i)exit\s*[=:]?\s*1|\bfail|\bdetected|non-?empty|SURVIVED|killed", text):
                guard = (rel, planted)
                break
```

There is no 4-space condition, no negative control, and no exit-status read anywhere in the file
(`grep -n 'space\|indent\|INDENTED' reports/round-73/accept-c.py` returns only those lines plus the fixture text).
And the named artifact does not hold one either:

```
$ grep -rnE '^ {4}\| S[0-9]{3,} \|' .ufo/waves/round-73/assimilation/guard-proof/ ; echo "exit=$?"
exit=1
$ grep -rniE '4 ?spaces|four-space' .ufo/waves/round-73/assimilation/guard-proof/
(no output)
```

`guard-proof/guard-proof.txt` tests exactly one plant, at 2 spaces ("fixture A2 — same copy + PLANTED
INDENTED row (2 spaces)"), with the column-zero control at 17 collisions. So half of the frozen COLLCHECK leg
is false of the artifact the leg names, and the counter cannot see that it is false.

Worse, the "found" half is not read from the proof at all. The guard is satisfied by the first file under
`guard-proof/` that has *any* 1-3-space-indented row and *any* occurrence of `collision` plus one of
`fail|detected|exit 1|…` — and that file is a 783-row registry mirror whose prose happens to contain the word
"fail":

```
$ python3 - <<'EOF'   # replicate the counter's loop over tree_files(GUARD_DIR)
…
FIRST MATCH: .ufo/waves/round-73/assimilation/guard-proof/mirror-a3/corpus/SOURCES.md planted= ['S881']
EOF
$ grep -n 'fail' .ufo/waves/round-73/assimilation/guard-proof/mirror-a3/corpus/SOURCES.md | head -1
50:| S021 | DK and Hatzel 2026, … frontier models converge on a mean generic narrative; negative prompting and temperature scaling fail | queued | …
$ python3 -c "… re.finditer(r'(?i)collision', mirror-a3/SOURCES.md) …"   # the file's only 'collision'
'pus/knowledge/verification/phonology-sanity-gate.md, corpus/knowledge/verification/naming-collision-gate.md, corpus/knowledge/civilizations/newar-nepal.md |'
```

Both tokens the guard check demands are incidental registry prose in a 783-row mirror copy
(`grep -cE '^ {0,3}\| S[0-9]{3,} \|' mirror-a3/corpus/SOURCES.md` = `783`; `grep -ci collision` = `1`, and that
one is a knowledge-file path in S002's used-by cell) — not a guard-proof statement.

Deleting the proof receipt leaves the leg green:

```
guard_receipt_deleted      PASS      -     <<< (rm .ufo/waves/round-73/assimilation/guard-proof/guard-proof.txt → 11/11)
```

Severity BLOCKER on the item's definition ("a claim leg is wrong"): COLLCHECK as frozen is not satisfied at
`0316b888`, yet the counter prints `PASS legs=11/11`. Mitigation a grader may weigh: the 4-space fact *is*
recorded in the round, in the wave-1 mutation report (`MutRegistryCollision.md` m3: "4 spaces … 17 / S881 absent
— missed … survives both — by design"), so the round knows the answer; what is missing is the artifact the leg
names and any instrument that would notice its absence. A grader reading "guard-proof" loosely as "the round's
guard proof" would call this MAJOR instead of BLOCKER; I read it as the counter's own `GUARD_DIR`, which is the
only thing the leg can mean to an executable counter.

**State of play (post-lands, recorded so nobody re-litigates the revision):** while this seat was
writing, the lane advanced past the claim's lands to `c1b5b476`, and commit `2d1cd91` added
`.ufo/waves/round-73/assimilation/guard-proof/four-space-control.txt`, whose first line says it was
"appended after wave-2 ExecSelftestAll 3.1". The counters themselves are unchanged after lands:

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin log --oneline 0316b888..HEAD -- reports/round-73/accept-c.py reports/round-73/accept-ca.py
(no output)
$ sha256sum reports/round-73/accept-c.py      # at HEAD
95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416
```

The new file is a three-line narrative (`reg-ids with 4-space plant (guard): 804`, `collision detected for
S881: 0`) with no command and no output pasted, and the counter still reads only a 1-3-space plant plus a
marker token, so the instrument gap in this section is unchanged at HEAD. It also does not close the
`guard_receipt_deleted` hole: the guard is still satisfied by the mirror copy.

### 3.2 MAJOR — C `EVIDENCE`: "with fetch line" is never checked

Leg text: "reports/round-73/evidence/<id>.txt exists per adopted row at <lands> **with fetch line**, a
browser-shaped UA, HTTP 200, a 64-hex sha256, quote-found-verbatim yes, …". The leg body (`:783-817`) checks
`access-date`, `http-status`, `sha256`, `user-agent`, `quote-found-verbatim`, the quote and its window — and
never looks for a `fetch` key:

```
$ grep -n 'fetch' reports/round-73/accept-c.py
784:    """Leg EVIDENCE: a committed capture per adopted row — fetch line (UA, status 200,
1254:source: S876 — https://fixture.example/a — §1 abstract — fetched 2026-10-25
…
1520:                body = ("# evidence %s\nfetch: GET https://fixture.example/%s\n"
```

The only `fetch:` in the file is the one the selftest **writes** into its own fixture (`:1520`); no code path
reads a `fetch` key.

Probe — delete the `fetch:` line from `reports/round-73/evidence/S876.txt` and commit:

```
$ head -3 reports/round-73/evidence/S876.txt      # after the mutation
# evidence S876 — claim C GATE (round 73)
user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36
access-date: 2026-10-25
$ python3 -B reports/round-73/accept-c.py --root . --lands <scratch> --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS EVIDENCE
ACCEPT-C-73: PASS legs=11/11
```

The claim is *true of the data* (all five files carry exactly one `fetch:` line —
`for f in reports/round-73/evidence/S87*.txt reports/round-73/evidence/S880.txt; do grep -c '^fetch: ' $f; done`
→ `1 1 1 1 1`), so this is an instrument gap, not a false claim.

Related, same leg: the UA test is `ev.get("user-agent","").startswith("Mozilla/5.0")` (`:803`), so
`Mozilla/5.0 (compatible; curl/8.7.1)` would pass — "browser-shaped" is only a prefix test.

### 3.3 MAJOR — C `GATE`: "non-empty locator cell" is vacuous

```
$ sed -n '758,760p' reports/round-73/accept-c.py
        cells = [c for c in row_cells(row_line) if c]
        if len(cells) < 5:
            bad.append("%s row lacks a locator cell" % sid)
```

The Gate table has six columns; blanking one leaves five non-empty cells, so the check cannot fire. Probe —
blank the S876 locator cell (`| Abstract paragraph under the Abstract heading (page-source line 267) |` → `|  |`):

```
non-empty cells: 5
| S876 — https://ojs.unito.it/index.php/ricognizioni/article/view/7099 (paper, Enguehard 2022) | 2026-10-25 | "the construction of languages by studen…
LEG PASS GATE
ACCEPT-C-73: PASS legs=11/11
```

The landed Gate rows do carry locators, so the claim is true of the data; the clause is unfalsifiable as coded.

### 3.4 MAJOR — C `ROWS`: "cadence-only recheck cell" accepts a date

```
$ grep -n 'RECHECK_RE =' reports/round-73/accept-c.py
147:RECHECK_RE = re.compile(r"^(?:\d+d|\d{4}-\d{2}-\d{2}|[a-z][a-z-]*)$")
```

Probe — replace S876's recheck cell `180d` with the date `2026-10-23` (the as-is tell the leg exists to catch):

```
$ git show HEAD:corpus/SOURCES.md | grep '^| S876 |' | …   # cells after the mutation
10 '2026-10-23'
LEG PASS ROWS
ACCEPT-C-73: PASS legs=11/11
```

The landed rows carry `180d`, so the data is fine; the instrument accepts the class it claims to reject.

### 3.5 MAJOR — C `SCRATCHMIRROR`: "exit 0" and "carrying the five rows" are prose substrings

```
$ sed -n '965,970p' reports/round-73/accept-c.py
    if "--file" not in receipt:
        bad.append("receipt does not show census validate --file")
    if re.search(r"(?i)(?:exit|rc)\s*[=:]?\s*0", receipt) is None:
        bad.append("receipt does not show exit 0")
    missing = [sid for sid in cfg["rows"] if sid not in receipt]
```

Probe — change the run's own `exit=0` to `exit=2` in the command block:

```
mirror_exit_prose          PASS      -    <<< still 11/11
```

because the receipt's later prose line `census validate --file exit 0 (see above).` matches. The receipt itself
says the ids it is graded on were appended after the first grading:

```
$ sed -n '/## ids carried/p' .ufo/waves/round-73/assimilation/validate-receipt.txt
## ids carried (appended 2026-10-25 after the landed data was first graded; the mirror run above inserted exactly these five rows)
```

So the leg's "on the mirrored corpus carrying the five rows" is verified as "the strings S876…S880 occur
somewhere in the file" — including in a block the file admits was written later. The same pattern is in
`GROUND`: `gap-sweep.txt:67` says the literal-fragment section was "appended 2026-10-25 after the landed data was
first graded", and the counter's per-fragment zero check reads it. Both are disclosed (lesson R73-M6), so I
rate them MAJOR rather than BLOCKER: the repair is admitted, but the counter cannot distinguish pre-data
evidence from post-hoc prose, which is the only thing this leg exists to do.

### 3.6 MAJOR — C `GROUND`: the per-fragment zero leaks to its neighbours

```
$ sed -n '876,884p' reports/round-73/accept-c.py
        for frag in cfg["ground_fragments"]:
            idxs = [i for i, line in enumerate(lines) if frag in line]
            …
            for i in idxs:
                window = "\n".join(lines[i:i + 3])
                if re.search(r"\b0\b", lines[i]) or re.search(r"\b0\b", window):
                    zero = True
```

Probe — set the `ojs.unito.it` line to 3 rows (leaving the next two lines at 0):

```
ground_frag_leak           PASS      -    <<< 11/11
```

The landed receipt has all five at 0, so the data is fine; the instrument's "a 0 for each fragment" is
"a 0 within three lines of each fragment".

### 3.7 MAJOR — a stale, buggy duplicate of the Ca counter is committed, at the path the landed counter's own USAGE names

```
$ sha256sum reports/round-73/accept-ca.py .ufo/waves/round-73/counters/accept-ca.py
222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89  reports/round-73/accept-ca.py
f8ebb5d849c9113d2d227494be0ec1403c746dd9124a505da0373e608bb97865  .ufo/waves/round-73/counters/accept-ca.py
```

`f8ebb5d8…` is r1 — the revision `counter-revisions.md` says "silently read the WORKTREE ledger". And the
landed r3 file's own docstring USAGE block points at it:

```
$ sed -n '/^USAGE/,/^"""/p' reports/round-73/accept-ca.py
USAGE

  python3 -B .ufo/waves/round-73/counters/accept-ca.py --root . \
      --lands <40hex> --fleet-root /home/vgpnk/Projects/shokunin
  python3 -B .ufo/waves/round-73/counters/accept-ca.py --selftest
"""
```

Run it at lands:

```
$ python3 -B .ufo/waves/round-73/counters/accept-ca.py --root . --lands 0316b888… --fleet-root /home/vgpnk/Projects/shokunin
# ledger: reports/round-73/ledger.json source=worktree-uncommitted sha256=c912401dd511d712567d8a704a690bf02fa4a8253a628b8e67ab9473798356b9
     NOTE ledger read from the moving worktree (not committed at lands)
…
ACCEPT-CA-73: PASS legs=9/9
```

So the landed tree contains a counter that prints PASS 9/9 while grading worktree bytes — the exact defect
F2/r2/r3 fixed and the frozen LEDGER leg forbids ("committed at <lands>'s ancestry"). `counter-revisions.md`
does not mention that the `.ufo` copy exists or is stale. (The claim-C copies are byte-identical:
`reports/round-73/accept-c.py` and `.ufo/waves/round-73/counters/accept-c.py` are both `95aee881…`.)

---

## 4. Passing for the wrong reason

### 4.1 C: a mutant is accepted if its mapped leg is *among* the failures

The assertion is only (`:1670-1675`):

```
        if "ACCEPT-C-73: FAIL" not in out:
            failures.append(...)
        elif "LEG FAIL %s" % wanted not in out:
            failures.append(...)
```

No assertion that the other ten legs pass, and none that the mapped leg fails for the named reason. Measured
over all 24 mutants (`/tmp/ExecSelftestAll/mutant_matrix.py`, using the counter's own `build_fixture`):

```
mutants whose mapped leg is the ONLY failure: 17
mutants with collateral failures: 7
total mutants: 24

mutant             mapped        legs that FAIL
drop_entry         ENTRIES       ENTRIES,ROWS,REPOINTED,CITEDLINES
row_gap            ROWS          ROWS,REPOINTED
repoint_url        REPOINTED     ROWS,REPOINTED,GATE
gate_quote         GATE          GATE,EVIDENCE
no_rejects         REJECTS       GATE,REJECTS
map_missing        COLLCHECK     ROWS,COLLCHECK
junk_rows          ENTRIES       ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,SCRATCHMIRROR,COLLCHECK
```

The clearest wrong-reason case is `junk_rows`: the mutant is named for junk rows, is mapped to **ENTRIES**, and
its ENTRIES detail is `corpus/knowledge/linguistics/conlang-scholarship.md missing` — it fails because the
fixture has no entries at all, not because a row is junk. The ROWS junk-row predicate is never the thing that
makes it fail; the selftest would accept a counter whose ROWS leg ignored junk rows entirely (the clean fixture
is what keeps ROWS honest, not this mutant).

### 4.2 Ca: the selftest exercises the REPAIR *fallback*, never the declared path

The frozen REPAIR leg: "every REPAIR pair's **statement re-read at <lands>** (last occurrence) equals the truth
observed at <lands> and differs from the base statement". All three real REPAIR pairs use it:

```
$ python3 -c "…for p in ledger['pairs']: print(p['id'], json.dumps(p.get('statement_after'))[:60])"
L04 REPAIR {"path": "SHONEN.md", "parse": ":(\\d+)` \\(Error patterns\\)"}
L05 REPAIR {"path": "SHONEN.md", "parse": ":(\\d+)` \\(Checklist\\)"}
L08 REPAIR {"path": "SKILL.md", "parse": "(?s).*\\| (accept-[a-z]+-\\d+) \\|"}
```

but `statement_after` appears in the selftest **nowhere** — neither `SELFTEST_LEDGER_PAIRS` (P1/P2/P3) nor the
scratch ledgers carry the key:

```
$ grep -n 'statement_after' reports/round-73/accept-ca.py
519:def statement_after(pair, clone_path):
520:    """Re-read the statement side at the clone: …
523:    spec = pair.get("statement_after")
547:            "stmt_after": statement_after(pair, lands_clone["path"]),
```

So every `REPAIR PASS` in the selftest comes from the weaker branch at `:593`,
`if norm(obs) == norm(pair.get("expected_after")):` — i.e. the ledger's own declared expectation, not the
statement bytes. The declared branch does work (probe: revert `SHONEN.md` `:505` → `:468`):

```
LEG FAIL REPAIR
     green=['L05', 'L08'] red=["L04(statement-after='468' truth='505' stated-at-base='468')"]
```

— it is simply never tested. This is the strongest "passes for the wrong reason" in the pair: the selftest's
"clean landing 9/9" advertises the REPAIR leg while exercising a code path the frozen leg does not describe.

### 4.3 Ca: ANNOTATE and NOSTUB pass vacuously at zero annotate pairs (disclosed)

```
$ python3 - <<'EOF'  # one-pair ledger: L04 only, statement_after removed, --min-pairs 1
…
one_pair_ledger          FAIL      APPENDONLY     annotate-pairs=0 (vacuous)
   NOSTUB   : annotate-pairs=0 (vacuous)
   REPAIR   : green=['L04'] red=[]
EOF
```

Both legs report PASS with no correction row in existence, and the same run shows the `expected_after`
fallback turning a REPAIR green with no statement read. The counter's docstring states both holes
("A ledger with zero ANNOTATE pairs makes ANNOTATE and NOSTUB vacuous; the receipt prints
`annotate-pairs=0 (vacuous)`"), and under the declared command the hole is not reachable — `--min-pairs`
defaults to 8 and the ledger has exactly 8 pairs, so dropping any pair reds LEDGER and BASEMISMATCH. MINOR,
recorded because the leg text does not carry the caveat.

---

## 5. The counters' descriptions of themselves are stale

1. `accept-c.py:21` — `Legs (10):` and the list that follows enumerates ten legs, **omitting EVIDENCE**, while
   the file runs eleven (`run_legs`, `:1105-1129`). `grep -n '^  EVIDENCE' reports/round-73/accept-c.py`
   → no output. The leg missing from the self-description is exactly the one with the unimplemented `fetch`
   clause (§3.2).
2. `accept-ca.py:45` — `LEGS (8, fixed at freeze)`; the file runs nine. TRACKED (the leg added for defect R1)
   is absent from the docstring's leg list, present only in code (`:817-830`).
3. `claims.json` claim Ca, `do_nothing_control` — "FAILS (ACCEPT-CA-73: FAIL legs=5/9; red: REPAIR, ANNOTATE,
   NOSTUB, TRACKED; green and unmoved: LEDGER, BASEMISMATCH, APPENDONLY, SEPARABLE, STAMP)". The committed r3
   control reads otherwise:

   ```
   $ grep -E '^ACCEPT' reports/round-73/telemetry/controls-ca.txt reports/round-73/telemetry/controls-ca-r3.txt
   controls-ca.txt:ACCEPT-CA-73: FAIL legs=5/9
   controls-ca-r3.txt:ACCEPT-CA-73: FAIL legs=4/9
   ```
   and `controls-ca-r3.txt` says in its own header "STAMP is red here only because lane main has moved past base
   (measured != lands)". So the claim's sentence is the r1 result: r3 is one leg redder (STAMP) than the claim
   says. With the *declared* command (`--ledger` omitted) it is starker still — r3 refuses the default ledger
   path in the worktree, so my run at `lands == base` is `ACCEPT-CA-73: FAIL legs=1/9` (LEDGER, BASEMISMATCH,
   REPAIR, ANNOTATE, NOSTUB, APPENDONLY, TRACKED, STAMP red; SEPARABLE green). The control's purpose
   (do-nothing must fail) survives all three readings; the claim's five-green colouring is not reproducible
   from the command the claim itself declares.
4. `claims.json` claim Ca — "the min-pairs gate (SELFTEST OK: **9 scenarios**, reports/round-73/telemetry/selftest.txt)";
   the landed counter prints `SELFTEST OK: 10 scenarios`. `selftest.txt` is the r1 receipt (sha `f8ebb5d8…`).
5. `accept-ca.py:1332` — the summary claims "10 scenarios" but enumerates **nine**, and the one it omits is
   scenario 7b ("worktree-only ledger"), the scenario r3 was written to add. The comment numbering skips 8
   (`# ---- 7.`, `# ---- 9.`, `# ---- 7b.`, `# ---- 8.`).
6. `reports/round-73/telemetry/selftest-r3.txt` is truncated mid-word:

   ```
   $ cat -A selftest-r3.txt | sed -n '6p' | cut -c1-200
   SELFTEST OK: 10 scenarios M-bM-^@M-^T do-nothing control (BASEMISMATCH found=2, REPAIR/ANNOTATE/NOSTUB FAIL), clean landing 9/9, stub-row control (ANNOTATE+NOSTUB FAIL), append-only removal FAIL, in-p
   ```
   The committed r3 receipt therefore does not carry the full line its counter prints, and stops before the
   scenarios 7b/8/9 it is supposed to evidence.
7. C's do-nothing control reads its configuration from the **lane worktree** (`# config source: lane worktree:
   row_set, entries, rejects.refused_staged, …` in `controls-c.txt`), because `claims.json` does not exist at
   base. The header discloses it, but the control's row set is then unpinned — a different worktree grades a
   different control. (The graded run reads `# config source: lands tree: …`, correctly.)
8. C's CENSUS leg is stubbed in the selftest (`CENSUS_STUB_OK = "#!/bin/sh\nprintf 'kotodama\\tok\\tstub\\n'"`,
   `:1394`), so `--selftest` cannot detect an interface drift in the real `sources-census.sh`. (I did run the
   real one at lands: `exit=0 last-line=kotodama	ok	…/corpus/SOURCES.md`.)

---

## 6. Severity summary

| # | severity | finding |
|---|---|---|
| 3.1 | **BLOCKER** | C `COLLCHECK`'s "a 4-space one not found" is absent from the counter and from `guard-proof/`; the "found" half is satisfied by an incidental `fail` in a registry mirror, so deleting `guard-proof.txt` still gives 11/11. Frozen leg false at lands, counter prints PASS |
| 3.7 | **MAJOR** | a stale r1 copy of the Ca counter is committed at `.ufo/waves/round-73/counters/accept-ca.py` — the path the landed counter's USAGE block names — and prints `PASS legs=9/9` while grading worktree bytes |
| 4.2 | **MAJOR** | the Ca selftest never exercises the declared REPAIR path (`statement_after`); all its REPAIR greens come from the `expected_after` fallback |
| 3.2 | **MAJOR** | C `EVIDENCE`'s "with fetch line" is not checked (deleting the line → 11/11); UA test is a `Mozilla/5.0` prefix |
| 3.3 | **MAJOR** | C `GATE`'s "non-empty locator cell" is vacuous (blanking it → 11/11) |
| 3.4 | **MAJOR** | C `ROWS`'s "cadence-only recheck cell" accepts a bare date (→ 11/11) |
| 3.5 | **MAJOR** | C `SCRATCHMIRROR`'s "exit 0" and "carrying the five rows" are prose substrings; the receipt admits the ids block was appended after the first grading |
| 3.6 | **MAJOR** | C `GROUND`'s per-fragment zero leaks to the neighbouring two lines |
| 4.1 | MINOR | the C selftest accepts a mutant when the mapped leg is merely among the failures (7/24 have collateral); `junk_rows` fails ENTRIES because entries are missing, not because rows are junk |
| 2.2 | MINOR | Ca `SEPARABLE`, `TRACKED`, `STAMP` have no negative scenario (all three proven falsifiable); STAMP is largely self-derived |
| 4.3 | MINOR | Ca `ANNOTATE`/`NOSTUB` pass vacuously at zero annotate pairs (disclosed; unreachable under the declared command) |
| 5.1-5.8 | MINOR | stale self-descriptions: `Legs (10)`/`LEGS (8)`, the claim's r1 control colouring (4 vs 5 reds, STAMP), "9 scenarios" vs 10, the summary enumerating 9 and omitting 7b, the truncated `selftest-r3.txt`, the worktree-read control config, the stubbed CENSUS |

What is **not** broken, measured: every one of the 11 C legs and 9 Ca legs is implemented and can fail (probes
above); `lands == base` fails on both counters (C: `legs=1/11` with only CENSUS green — exactly the claim's
control line; Ca: `legs=1/9` under the declared command, `legs=4/9` with the r3 receipt's explicit `--ledger`);
the C fixture's ENTRIES body floor is live (`body has 7 words (floor 478 …)`), the nine-field header is live,
`opened 2026-10-25` and the access date are live, `used-by` is live, the map old→new and the stale-map byte
identity are live, `reg-ids` and the guard's adopted-id clause are live, the base-stray ground is live, and the
Ca `statement_after`, `SEPARABLE`, `TRACKED` and `STAMP` legs all fail when they should.

---

## 7. What I could NOT check

- **Any live source.** No URL was fetched by this seat: the evidence files' `fetch`/`user-agent`/`http-status`/
  `bytes`/`sha256`/`quote-found-verbatim` values were taken as recorded bytes, not re-measured. Whether the
  five captures are real, current, or UA-gated as recorded is outside this item and needs a QUALITY 21/22
  record I did not make.
- **The wave-1 m3 (4-space) measurement.** I verified that `guard-proof/` holds no 4-space probe and that the
  counter has no such check; I did not re-run `MutRegistryCollision`'s scratch fixture, so I take its m3 row
  ("4 spaces … survives both — by design") as that seat's claim, not mine.
- **The fleet side of Ca `APPENDONLY`.** I ran the counter (which pins `fleet_pin 80d8c9b576d4` and compares the
  round-72 report blob) but did not independently diff the fleet repo's history.
- **The real census script's semantics.** The selftest stubs it; I ran the real one at lands (exit 0) but did not
  audit `scripts/sources-census.sh` for what "ok" covers.
- **The three dead wave-1 seats** (`ConnectorSiblings`, `ScribeMistakes`, `ExecScratchMirror`) and their missing
  reports — outside my item; I did not read the 34 w1 reports for consistency with the counters.
- **Whether `--selftest` leaves temp dirs behind on failure** — not exercised (both selftests exit 0; the code
  `shutil.rmtree`s its fixtures at the end of `run_selftest`/`selftest`).
