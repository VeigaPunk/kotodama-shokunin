# RevRegistryFinal — registry integration attack (round 65, claim C)

Seat: `kotodama-r65.RevRegistryFinal` (revenger, leaf). Date 2026-10-24.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `17c32302`.
Instrument under test: `reports/round-65/accept-c.py` sha256 `ad5540fe…9365d8`
(460 lines, docstring "revision 2" — the file changed during this seat's window from
a 448-line revision 1; every finding below was re-verified against the rev2 sha and
rev2 line numbers). Base registry: 802 lines, 675 rows (`| S001 |`…`| S749 |`),
table lines 26–704, then `## Paths` (706), `## Search log` (741),
`## Leads (unopened)` (753); file ends at 802 inside the Leads bullet list.

Method: imported the frozen module (`importlib`) and replicated the ROWS / LINK /
APPEND bodies verbatim from `accept-c.py:204-264` (ROWS), `:370-379` (LINK),
`:381-388` (APPEND), reusing the module's own `ROW_RE` (:82), `URL_RE` (:83),
`CAPTURE_RE` (:85), `cells` (:114), `norm_url` (:126). Control: on the unmutated
base registry the replica returns `APPEND missing=0 base=675 measured=675 +26=False`
— byte-identical to the real instrument's line in `telemetry/dry-run-c.txt`
(`sha256 36fdc328…67d7`), so the replica is calibrated to the real tool. A
synthetic 26-row fixture (S750–S775, 11 cells, tier A, mined, 2026-10-24, 180d,
used-by the entry, 9-word quote, same-page capture) passes ROWS+LINK+APPEND
unmutated; every mutation below was applied to that clean post-state. All
mutations were made in memory; nothing in the lane was written except this file.

## Direct answers to the three assigned questions

### Q1. Appended row duplicating a base id with one cell changed — does APPEND catch a base teaches cell edited?

**Caught (Y), but only through whole-line identity + the +26 count — ROWS itself
never checks base-id uniqueness.**

| case | mutation | ROWS | LINK | APPEND | proof |
|---|---|---|---|---|---|
| Q1a | base S100 `teaches` cell edited in place | PASS | PASS | **FAIL** | `missing=1 base=675 measured=701` |
| Q1b | base S100 line re-appended with only `teaches` changed (base line intact) | PASS | PASS | **FAIL** | `missing=0 base=675 measured=702` (+26=False) |
| Q1c | the Q1b duplicate re-appended *instead of* new row S775 | **FAIL** | PASS | PASS | `S775:rows=0` (ROWS' "each new id exactly once" catches it) |

Mechanism: `reg_multiset` is keyed on the whole line (`accept-c.py:382-385`), so a
changed base line is a missing line; `count_ok` (`:386`) forbids a 27th appended
row. Both directions therefore fail closed. Residual: the guard is *shape*-sensitive
— see M4, where the same duplicate in a shape `ROW_RE` misses passes every leg.

### Q2. Appended row reusing a base URL under a new id — LINK checks only new rows?

**Partly.** LINK scans every `ROW_RE` line (`:374 hits = sum(1 for line in reg_lines
if url in line)`), so *exact* reuse is caught by the hit count, but its identity is
raw substring, and `norm_url`/`norm_seen` (`:252-256`) are applied only among the 26
new rows — the 675 base rows are never normalized or seeded into `norm_seen`.

| case | new S750 live URL | ROWS | LINK | APPEND | proof |
|---|---|---|---|---|---|
| Q2a | exact base URL `https://en.wikipedia.org/wiki/List_of_headgear` (S749) | PASS | **FAIL** | PASS | `S750:registry_hits=2` |
| Q2b | base URL + `?utm_source=x` | PASS | PASS | PASS | norms equal, base line lacks the query string → `hits=1` |
| Q2c | `www.` twin of the base URL | PASS | PASS | PASS | `norm_url` strips `www.` only for the new row |
| Q2d | base URL + trailing `/` | PASS | PASS | PASS | trailing slash stripped in `norm_url`, not in the raw base line |
| Q2e | `http://` twin of the base URL | PASS | PASS | PASS | `norm_url` keeps the scheme → different norm, different substring |
| Q2f | base URL + `#section-2` | PASS | PASS | PASS | fragment ignored by `norm_url`; absent from the base line |

Q2b–Q2f all pass **every registry leg**: a row can re-cite an already-registered
source under a new id while the claim counts "exactly 26 new sources". The same
failure holds against non-row text: `https://pulotu.com/about`, which appears once
as a *Leads (unopened)* bullet, is accepted as S750's live source with all three
legs PASS (LINK only scans `ROW_RE` lines).

### Q3. New row whose capture normalizes equal but points at a different page

**Not caught (N).** `norm_url` drops query and fragment (`:126-146`), and ROWS
compares `norm_url(cap.group(2)) != norm_url(urls[0])` (`:259`):

| case | live | capture original | ROWS | proof |
|---|---|---|---|---|
| Q3a | `https://shop.test.invalid/product?id=1001` | `…/product?id=9999` (a different product) | PASS | query ignored |
| Q3b | `https://ref.test.invalid/doc` | `…/doc#part-9` (a different section) | PASS | fragment ignored |

So a row can claim "archived same-page capture" for a page it does not have, which
is exactly the evidence the LIVE leg is supposed to lean on for 6 of 26 rows.

## Additional integration errors that pass a leg but corrupt the registry

### HIGH-1 — table membership and position are never checked; the default `>>` integration lands the 26 rows in `## Leads (unopened)`

APPEND counts `ROW_RE` lines anywhere in the file (`:209-210`, `:386`). The base
registry's table ends at line 704; 98 non-table lines follow. Appending the 26 rows
at EOF (the natural `>> corpus/SOURCES.md`) puts them after `## Leads (unopened)`,
where the file itself says "A lead is not evidence and never a row".

Proof: post-state = working-tree registry + `\n` + the 26 fixture rows at EOF
(lines 803-828) → `ROWS PASS LINK PASS APPEND PASS missing=0 measured=701`. No leg
checks that a new row sits inside the `## Registry` table (lines 26-704), that the
26 rows are contiguous, or that ids ascend. Descending id order also passes all
three legs; mid-table insertion is only caught when it *duplicates* a row
(`S750:rows=2`), not because of position.
`[INFERENCE]` the appended lines render as paragraph text under GFM because the
`## Paths` heading closes the table; I did not run a renderer.

### HIGH-2 — non-row lines are entirely unguarded by APPEND

APPEND only compares lines matching `ROW_RE`. Everything else in the 802-line file
— the `| id | source | … |` header, the `|---|…---|` delimiter, the tier legend,
the "Append-only" rule, `## Paths`, `## Search log`, `## Leads` — can be rewritten
or deleted with no leg noticing:

- deleting the delimiter row `|---|---|---|---|---|---|---|---|---|---|---|` (present
  exactly once) leaves the whole 675-row registry not rendering as a table →
  `ROWS PASS LINK PASS APPEND PASS measured=701`;
- rewriting `**A** — primary or` → `**A** — convenient or` and
  `Append-only: only` → `Mutate freely: only` → all three legs PASS.

This matters because the tier semantics ROWS relies on ("A/B"), and the append-only
contract itself, live in exactly those unguarded lines.

### MEDIUM-3 — phantom rows: a base-id duplicate with a changed `teaches` cell passes every leg

`ROW_RE = r"^\|\s*(S\d+)\s*\|"` (:82) is anchored at column 0 with an uppercase `S`.
A line that renders as a registry row but misses the regex is invisible to
`reg_lines`, `base_lines`, `reg_by_id` and LINK's scan:

| case | appended line | ROWS | LINK | APPEND |
|---|---|---|---|---|
| M3a | ` \| S100 \| … \| PHANTOM teaches overwrite for S100 \| … \|` (one leading space, base id, one cell changed) | PASS | PASS | PASS `measured=701` |
| M3b | `\| s750 \| Phantom Source — https://phantom.test.invalid/fake \| …` (lowercase id) | PASS | PASS | PASS `measured=701` |

M3a is the Q1b corruption in a shape the counter cannot see: the base row is
duplicated and its `teaches` silently overwritten in the rendered registry, with
`missing=0` and the count still 701. `[INFERENCE]` GFM allows up to three leading
spaces before a table row, so M3a renders inside the table.

### MEDIUM-4 — used-by is a substring test

`:239 if ENTRY not in usedby` accepts:
- `…games-play-sport-contests.md, corpus/knowledge/linguistics/naming-systems.md`
  (rows claiming support for an unrelated existing entry) → ROWS PASS;
- `…games-play-sport-contests.md.bak` (a path that is not the entry) → ROWS PASS.
The claim's "used-by the entry" is not verified as an exact cell value.

### MEDIUM-5 — tier inflation the instrument can see and does not check

`:231` accepts any `A|B`. The registry legend (unguarded, see HIGH-2) states
"`community` is never A"; a new row with `kind = community` and `tier = A` passes
ROWS. Similarly `kind` and `scope` are never validated.

### MEDIUM-6 — only `urls[0]` is constrained inside a source cell

`:251 live_urls[sid] = urls[0]`. A source cell
`<clean-live> ; mirror https://en.wikipedia.org/wiki/List_of_headgear ; capture <cap>`
passes ROWS and LINK and carries a second, unregistered URL that duplicates base row
S749's source — the same "one row, two sources" ambiguity Q2 exploits, without even
changing the live URL.

### MEDIUM-7 — `norm_url` aborts the counter on a malformed port

`:138 port = parts.port` is outside the `try` that only wraps `urlsplit`. `ROWS`
calls `norm_url` at `:252` and `:259` with row-controlled text:

```
norm_url("https://x.test.invalid:99999/p") -> ValueError: Port out of range 0-65535
norm_url("https://x.test.invalid:abc/p")   -> ValueError: Port could not be cast …
```

An uncaught exception aborts the script before any leg line and before
`ACCEPT-C-65:` is printed (`return 0 if verdict else 1`, `:456`). That fails closed
on the exit code but produces no receipt-able leg verdict, and a crafted row can
deny the counter its stamp rather than earn a FAIL.

### LOW-8 — HOSTS host extraction is bypassable

`:364 host = re.sub(r"^https?://","",url).split("/")[0].lower().split(":")[0]`
takes everything before the first `:`, so `https://user:pass@example.org/p` yields
host `user` and PASSES HOSTS, while `urlsplit` hostname is `example.org`. Reserved /
fake hosts also pass unmodified: `*.test.invalid`, `src750.example`, `localhost`,
`127.0.0.1:8080`. The leg is literal to the claim ("no placeholder hosts") but is not
a fabricated-anchor gate.

### LOW-9 — false-fail brittleness (over-strict, not a bypass)

- live URL wrapped in parentheses: `URL_RE` captures `https://…/page)` and
  `norm_url` strips only trailing `.,;'` → spurious
  `S750:capture_mismatch` (`ROWS FAIL`);
- an escaped pipe in any cell (`… \| pipe`) → `cells=12` → `S750:cells=12` FAIL;
- a new live URL that is a prefix of a base URL (`https://en.wikipedia.org/wiki`)
  → `registry_hits=3` FAIL, because LINK matches substrings across all row lines.

### LOW-10 — receipts

- `telemetry/controls-c.txt` control 2 ends `ACCEPT-C-65: FAIL` followed by
  `exit=0`; the tool returns 1 on a failed verdict (`:456`), and
  `telemetry/dry-run-c.txt` correctly records `exit=1`. The control receipts' exit
  stamps are therefore not the tool's exit status (stale/false stamp in the forcing
  controls; the ACCEPT-C-65 line itself is consistent with the output).
- controls-c.txt shows `LINK PASS bad=[]` in the only fixture exercising the URL
  twin: the twin was caught by ROWS `norm_dup`, so **no control forces LINK at all**,
  and none forces the base-row boundary that Q2b–Q2f exploit.
- `dry-run-c.txt` records `SWEEP FAIL exit=0` (sweep exited 0; the leg failed only on
  the README topic row) — correct, but it shows the leg detail mixes two causes under
  one word.

## Positive checks (no finding)

- Base registry is internally clean: 0 duplicate ids, 0 duplicate lines, 0 rows
  without a URL in the source cell, max id S749 (no pre-existing S750–S775 collision).
- Working-tree registry equals base at review time (675/675 rows).
- Exact base-line edits and exact 27th-row appends are caught (Q1a/Q1b), and exact
  base-URL reuse is caught (Q2a).

## Residual risk and verification gaps

1. My ROWS/LINK/APPEND are a faithful re-implementation of inline code, not the
   executed legs; calibration is the base-state line matching `dry-run-c.txt`
   exactly plus the clean-fixture control. The real instrument was not run end-to-end
   by this seat (LIVE needs network; the entry file was still absent at review time,
   so LINK's `url in text` branch and NOHARM's `git diff BASE main` were not
   exercised — at review `main == HEAD == 17c32302`, so NOHARM can only pass once the
   L1 commits the entry; NOHARM also reads commits only, so a post-commit working-tree
   edit to another `corpus/knowledge` file is invisible to it while every other leg
   reads the working tree).
2. HIGH-1's rendering claim and M3a's in-table rendering are `[INFERENCE]` from GFM
   rules; no renderer was run.
3. HIGH-1, HIGH-2, M3, M4, M5, M6, LOW-8 are all invisible to the frozen predicate as
   written, so they cannot be "fixed by a rerun": they are gaps in the counter's
   scope, not flaky results. If the L1 wants the claim to mean what it says, the
   cheapest closures are: require each new row's index to be inside the
   `## Registry` section and the 26 rows to be the file's last 26 row lines; seed
   `norm_seen` with the normalized base-row URLs; compare base-URL identity against
   the whole file (including Leads); require `used-by` to equal the entry cell
   exactly; and guard `norm_url` so a malformed port is a leg FAIL, not a traceback.
4. No tool installs were needed for this seat (no package manager was run).
