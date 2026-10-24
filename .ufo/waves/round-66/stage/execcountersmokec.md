# Counter smoke — ACCEPT-C-66 (`accept-c.py`), round 66

Seat: ExecCounterSmokeC (build, operability). Time-boxed leaf; counters NOT edited.

## Environment

- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
- lane revision (HEAD, detached) = `main` = `94209e8f80969dbac48d56c5d0e2e623635b8616` (base)
- counter sha256 (self-reported and independently verified with `sha256sum`):
  `0726b4bc99eefe05a81c92cb6fd1bb3819a041b68679466aa6278350c19dda86`
- Python: system `python3`; no new tools installed (nothing needed; pacman guard untouched)
- corpus entry absent, registry at 701 rows, `corpus/README.md` 239 files — pre-data state

## Run 1 — the claim command

`python3 -B reports/round-66/accept-c.py --root .` → **exit 1**, wall **0.088 s**
(output byte-identical to the frozen receipt `reports/round-66/telemetry/dry-run-c.txt`;
two consecutive runs byte-identical → deterministic)

| leg | verdict | detail (verbatim) |
|---|---|---|
| FILE | FAIL | `unreadable: [Errno 2] No such file or directory: '.../corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md'` |
| SET | FAIL | `missing=['S777' … 'S800'] non-unique=['S777' … 'S800']` (all 24 in both lists) |
| ROWS | PASS | `bad=[] n=0` |
| ONEID | FAIL | `bad=['S777:citations=0', … 'S782:citations=0']` (6 shown of 24) |
| RESTATE | FAIL | `bad=['S777:bullets=0', … 'S780:bullets=0']` (4 shown of 24) |
| HOSTS | FAIL | `hosts=0` |
| LINK | PASS | `bad=[]` |
| APPEND | PASS | `missing_old=0 appended=0` |
| NOHARM | PASS | `diff=[] allowed=['corpus/knowledge/culture-material/games-play-sport-contests.md', 'corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md']` |
| SWEEP | PASS | `exit=0 readme_sha256 0c04517bcd485feb64b283d934db2037552f5d771449374a5a36f9cb3b26d3e7` |
| CAPTURE | FAIL | `bad=['S777:absent', … 'S784:absent']` (8 shown of 24) |
| TOPIC | FAIL | `entry topic text appears verbatim in the README row` |
| — | — | `ACCEPT-C-66: FAIL` |

PASS of the pre-data control: the do-nothing tree FAILS exactly as `controls-c.txt` declares,
and the output matches the frozen dry-run receipt byte-for-byte. No leg crashed on this path.
No side effects: `git status --short` unchanged; no `__pycache__` (`-B`); no writes outside stdio.

## Run 2 — `--help`

`python3 -B reports/round-66/accept-c.py --help` → **exit 0**, prints
`usage: accept-c.py [-h] [--root ROOT]` and the option list. No crash. Missing-`--help` risk does not apply.

## Other exit paths probed

- `--root /nonexistent-lane-root` → prints FILE FAIL line, then `ACCEPT_C_INPUT_ERROR registry: …` on stderr, **exit 2**, no `ACCEPT-C-66:` verdict line.
- `--bogus` → argparse usage, **exit 2**.
- run from `/tmp` with absolute `--root` → same legs, **exit 1**, but header prints
  `# measured revision (lane main): unresolvable` (defect D3 below).

## Defects, crashes, ambiguities (path:line + minimal fix)

### D1 (HIGH, crash) `reports/round-66/accept-c.py:236` — `KeyError` when a cited id has no row
`row_line = reg_by_id[sid][0]` is reached whenever the entry cites `(S777)` exactly once
(`RESTATE` bullets == 1) even if the registry has no S777 row. Uncaught traceback, exit 1,
**no `ACCEPT-C-66:` verdict line** — a partial landing (entry written before registry rows)
crashes the instrument instead of printing an honest FAIL. Reproduced in a shared fixture clone:
```
Traceback (most recent call last):
  File ".../reports/round-66/accept-c.py", line 332, in <module>
    sys.exit(main())
  File ".../reports/round-66/accept-c.py", line 236, in main
    row_line = reg_by_id[sid][0]
KeyError: 'S777'
EXIT=1
```
Minimal fix (2 lines, at the top of the `for sid in NEW_IDS:` RESTATE loop):
```python
if sid not in reg_by_id:
    restate_bad.append(f"{sid}:no-row"); continue
```

### D2 (HIGH, bypass) `accept-c.py:281-286` — NOHARM measures committed `BASE..main`, not the lands
The wave's lands live in the worktree while the counter runs. `git diff BASE main -- corpus/knowledge`
ignores uncommitted changes entirely, so any corpus/knowledge damage is invisible. Reproduced in a
shared clone: deleting `corpus/knowledge/culture-material/calendar-festival-systems.md` (worktree)
gives `git status` ` D …`, committed diff count 0, and the counter still prints
`NOHARM PASS diff=[]`. Compounded by D3/ref state: HEAD is **detached** and the jj bookmark/git branch
`main` sits at base (`jj bookmark list → main: 94209e8f`), so if the L1 integrates on a detached
HEAD or a bookmark that does not move `main`, NOHARM stays vacuous even after the commit.
With APPEND covering only registry rows, **no leg observes corpus/knowledge in the worktree**.
Minimal fix: add the worktree+tip comparison, e.g. in the NOHARM leg
```python
wt = subprocess.run(["git","-C",root,"status","--porcelain","--","corpus/knowledge"], ...)
paths = diff + [p[3:] for p in wt.stdout.splitlines()]
```
and resolve the tip from `HEAD` (falling back to `main`) instead of hardcoding `main`.

### D3 (HIGH, receipt integrity) `accept-c.py:137` — `git rev-parse main` ignores `--root`
`subprocess.run(["git","rev-parse","main"], …)` has no `-C root`/`cwd=root`, so the printed
`# measured revision (lane main)` describes the **caller's** repository, not `--root`. From `/tmp` with a
valid absolute `--root` it prints `unresolvable` while the lane is intact; from any other repo it would
print that repo's `main`. That header is the counter's self-evidence of what was measured.
Minimal fix: `["git","-C",root,"rev-parse","HEAD"]` (or `main` with `-C root`, plus a HEAD fallback).

### D4 (MED, false-FAIL) `accept-c.py:319-321` — TOPIC takes the first line mentioning the filename
`row = next(l for l in rtext.splitlines() if ENTRY.split("/")[-1] in l)` picks the **revision-prose**
line, not the index bullet, as soon as the routine README revision block (pattern at
`corpus/README.md:3-10`) mentions the new filename above the sorted index row. Demonstrated with
identical README text in two orders: index bullet first → `TOPIC PASS`; prose first (the normal
pattern) → `TOPIC FAIL`, even though the index bullet carries the topic text verbatim
(`corpus/README.md:390` shows the games entry's correct bullet vs. prose mention at `corpus/README.md:4`).
This leg will FAIL a correctly landed round-66 entry unless the prose is contorted.
Minimal fix: match the index bullet instead of the first mention:
```python
row = next((l for l in rtext.splitlines() if l.strip().startswith(f"- `{ENTRY.split('/')[-1]}`")), "")
```
(or `any(...)` over all mentioning lines, which still passes the defensive check).

### D5 (MED, false-PASS) `accept-c.py:155` + `:321` — empty `- topic:` passes both legs
FILE only tests `l.startswith("- topic:")`; TOPIC tests `"" in row`, which is true for any README line
mentioning the filename. Reproduced in the fixture: entry with a bare `- topic:` line →
`FILE PASS … topic=True` and `TOPIC PASS`. An entry with no topic text can satisfy the frozen predicate.
Minimal fix: `topic_text = tline[len("- topic:"):].strip()`; require `len(topic_text) >= 20` in FILE
and `topic_text in row` in TOPIC.

### D6 (MED, threshold inflation) `accept-c.py:251-257` vs docstring `:19` — HOSTS not normalized
The leg says ">=10 distinct normalized hosts" but counts raw `urllib.parse.urlparse(u).netloc.lower()`,
so `www.example.org` and `example.org` count twice (`norm_url` would collapse them:
`https://www.example.org/a/ → example.org`). 5 real hosts × with/without `www` reaches 10.
Minimal fix: `hosts.add(urllib.parse.urlparse(norm_url(u)).netloc)`.

### D7 (MED, documented bypass) `accept-c.py:104-105` vs docstring `:21` — LINK is NOT scheme/query-insensitive
The docstring promises "scheme/www/query-insensitive", but `norm_url` keeps scheme and query
(probe: `http://example.org/a`, `https://example.org/a`, `https://example.org/a?utm_source=x` all
distinct). http↔https and tracking-query duplicates therefore pass LINK.
Minimal fix: drop scheme (or force `https`) and strip/sort the query in the normalized identity, or
correct the docstring and the claim text — but then the leg's stated intent is unmet.

### D8 (MED, bypass) `accept-c.py:108-113` — LINK checks only the first live URL per row
`row_urls` returns `live[0]`. 233 of 701 base registry rows carry 2+ URLs (e.g. S061, S069, S142,
S143, S151), so a new row reusing a base row's **second** URL is invisible to LINK.
Minimal fix: build/compare a set of all live URLs per row (skip only web.archive.org captures).

### D9 (MED, invisible duplicates) `accept-c.py:272-280` — APPEND is set-based
Exactly duplicating a base row is reported as `appended=0` and passes: reproduced by appending a copy
of the `S001` row to the fixture registry → `APPEND PASS missing_old=0 appended=0`, no other leg
counts rows, so registry row inflation by duplication is undetectable.
Minimal fix: compare `collections.Counter` multisets and require
`sum(tip.values()) - sum(base.values()) == len(new rows)`.

### D10 (LOW, misleading evidence) `accept-c.py:189-190` — missing ids reported as "non-unique"
`dup = [sid for sid in NEW_IDS if len(reg_by_id.get(sid, [])) != 1]` puts every *missing* id into
`non-unique`, so the base dry-run's two lists are identical and suggest duplicate rows where there are none.
Minimal fix: `> 1`.

### D11 (LOW, false-FAIL trap) `accept-c.py:78-79` — pipe inside an anchor quote breaks the row
`cells()` splits on `|`; a legitimate anchor quote containing `|` yields `ROWS FAIL bad=['S777:cells=12']`
(reproduced). Minimal fix: constrain scribe anchors to no `|`, or split on unescaped pipes.

### D12 (LOW, weak evidence line) `accept-c.py:297` — SWEEP detail prints only sweep's last line
`readme_sha256 …` is shown, while the leg actually requires `totals_ok True` (present two lines earlier
in sweep's stdout). Minimal fix: print the `totals_line … totals_ok …` line in the detail.

### D13 (LOW, output contract) `accept-c.py:166-171` — input-error path emits a stray `FILE FAIL` then exit 2
On `--root /nonexistent-lane-root` the run prints `FILE FAIL …` before `ACCEPT_C_INPUT_ERROR registry`
and returns 2 with no `ACCEPT-C-66:` line, contrary to the docstring's "output ends ACCEPT-C-66".
Documented exit 2, so acceptable; note only.

### D14 (LOW, shape ambiguity) `accept-c.py:217-245` — "cited exactly once"/"each cited bullet" are not bullet-scoped
ONEID counts `(S###)` anywhere in the entry (HTML comments, tables, the topic line all count), and
RESTATE's `entry_bullets` matches any line containing `(S###)`, not markdown bullets. No harm
demonstrated; the leg names promise a shape the implementation does not enforce.

### D15 (LOW, scope) `accept-c.py:51` — `ROW_RE` is not table-scoped
`^\|\s*(S\d+)\s*\|` matches rows in any section of `corpus/SOURCES.md`
(`## Registry`:26, `## Paths`:733, `## Search log`:768, `## Leads (unopened)`:780). A properly shaped
row placed outside `## Registry` still satisfies SET/ROWS/CAPTURE.
Minimal fix: parse rows only between the `## Registry` header and the next `##` header.

### D16 (hygiene) `accept-c.py:178` — `base_ids` computed and never used (dead).

## Bookkeeping note for the L1

The counters are untracked draft files; the frozen identity is the sha above. D1 (crash), D2 (worktree
blind NOHARM), D3 (wrong repo in the revision header), D4 (TOPIC first-match) and D5 (empty topic)
change what the frozen predicate can honestly certify. D2/D4 in particular can make ACCEPT-C-66
unmet after a correct landing and can also be satisfied without certifying the claim. If they are
fixed, re-freeze with fresh `controls-c.txt`/`dry-run-c.txt` receipts before data legs are trusted;
workarounds (prose line containing the full topic text, committing before the run) hide the defects
rather than repairing them and should be stated in the acceptance receipt.

## Evidence retained

- `reports/round-66/telemetry/dry-run-c.txt` (pre-existing) == `stage/evidence/accept-c-base-run.txt` (this run, exit 1)
- Reproductions: shared clone (`git clone --shared file://$PWD`) under a scratch dir, now removed;
  commands: create entry citing `(S777)` with no row → KeyError at :236; delete a corpus/knowledge file
  → NOHARM PASS; swap README prose/bullet order → TOPIC PASS/FAIL; blank `- topic:` → TOPIC PASS;
  append duplicate `S001` row → APPEND appended=0; append a row with `|` in the anchor → ROWS cells=12;
  `norm_url` probe via `importlib` module load.
