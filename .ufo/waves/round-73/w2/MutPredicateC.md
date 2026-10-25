# MutPredicateC — wave-2 FALSIFY (hyaku run 7) — claim C predicate vacuity

Seat: MutPredicateC (leaf; no delegation, no background jobs). Round 73, wave 2.
Attack surface: **claim C's predicate** — `reports/round-73/accept-c.py` r1
(sha256 `95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416`,
asserted identical to the bytes at lands) run as
`python3 -B reports/round-73/accept-c.py --root . --lands <lands>`.
Lands `0316b8883b4f8d44b8efd720140e7f52f734a102` (tree `9b10fa06a2d3756c8bacfc8fc7b2115921370d97`),
base `8841ad3b896a0227674fa0725b818c999118046f`, frozen claims.json blob
`7d28537d7004df5f7c2cc79b8d480edbc69d8ccc` (verified equal at freeze commit
af65165 and at lands; absent at base).

## Method

Fresh throwaway clone per the item template (outer git repo at the workdir,
lane clone inside, `git rev-parse --show-toplevel` of the outer dir verified
equal to the workdir before any commit; every junk commit used
`git -c user.name=mut -c user.email=mut@mut.invalid` **inside the clone
only**). Each junk landing is two commits on top of base: (A) artifacts
committed pre-data, (B) the registry append — satisfying SCRATCHMIRROR's
ordering honestly, so that only the *targeted* work is junked and every other
leg is exercised for real. The fleet census script was copied to
`$D/scripts/sources-census.sh` so the bare `--root .` command resolves
`fleet_root=dirname(lane)` exactly like a lane run; the real census script
(the round's own, unmodified) graded every landing. The counter ran from the
worktree checked out at the landed rev while `--lands` pointed at the junk
commit — graded bytes come only from the materialized lands tree (counter
header: `worktree graded: no`); this is the same invocation mode as the
filed do-nothing control `reports/round-73/telemetry/controls-c.txt`.

Harness sanity (mandatory before trusting any junk verdict):

```
$ python3 -B reports/round-73/accept-c.py --root . --lands 0316b8883b4f…   # P0a, real lands
LEG PASS ENTRIES … LEG PASS COLLCHECK
ACCEPT-C-73: PASS legs=11/11          exit=0

$ python3 -B reports/round-73/accept-c.py --root . --lands 8841ad3b896a…   # P0b, do-nothing
… LEG FAIL … LEG PASS CENSUS …
ACCEPT-C-73: FAIL legs=1/11           exit=1
```

P0a/P0b reproduce the filed receipts (`controls-c.txt`: FAIL legs=1/11, only
CENSUS green) byte-for-byte, so the harness is faithful. Builder + full log:
`/tmp/MutPredicateC/probe_build.py`, `/tmp/MutPredicateC/probe-run.log`,
evidence extractor `/tmp/MutPredicateC/extract.py`; clone retained at
`/tmp/MutPredicateC/probe` (outer toplevel `/tmp/MutPredicateC/probe`).

## Results (final run, all twelve)

| probe | junk (work skipped) | lands | verdict |
|---|---|---|---|
| P0a | none (real landed rev) | 0316b888… | PASS 11/11 (sanity) |
| P0b | everything (lands=base) | 8841ad3b… | FAIL 1/11 (matches controls-c.txt) |
| P1 | both entries = 9-field header + 561-word filler, zero quoted spans | 2c440ee85f3ce61da61cc4370a28e26a5c294c5f | **PASS 11/11 — SURVIVOR** |
| P2 | rows = staged-package bytes (S881,S882,S892,S893,S901) renumbered + mechanically normalized only | d030b62eaed3459aa30518d58bb7a5d90312c60f | **PASS 11/11 — SURVIVOR** |
| P3 | S880 anchor/Gate/evidence quote invented, forged window | 58ac7a02e4f477b1352cc8c9e098f1017aa8961a | **PASS 11/11 — SURVIVOR** |
| P4 | all five quotes invented, all evidence forged | 761c66fbb707e3ac56fd8fc08d461f8958c8b33e | **PASS 11/11 — SURVIVOR** |
| P5a | entry prose cites campaign id `(S894)` (uppercase) | 6b009ef18f8f81cc68960b2b2825103ad7872880 | FAIL 10/11 — caught |
| P5b | entry prose cites `(staged s894)` (lowercase) | a960e80670ea4ff6ddbcbff965678e62884d8f1e | **PASS 11/11 — SURVIVOR** |
| P6a | Gate refuse table deleted (no reject rows) | b3182edbdf6e6e9024097df50b2fa258681a8781 | FAIL 9/11 — caught |
| P6b | one fabricated reject row (nonexistent file, never-probed URL) | 93a20a75782bc86ce62b79c166797a721fb42a7b | **PASS 11/11 — SURVIVOR** |
| P7a | entries cite only S876/S880; S877–S879 rows `used-by: —` | a4127f0276b19aed1c6be930eceb9cd3be21434b | **PASS 11/11 — SURVIVOR** |
| P7b | only rows S876+S877 added AND claims.json **rewritten at lands** (row_set→S876,S877) | b88f66f69d2b1ea9aba4ef1770b377a4d20b95b6 | **PASS 11/11 — SURVIVOR** |

Answer to the item's explicit question: **ROWS does NOT demand all five rows
be cited.** P7a and P7b both pass.

## Findings

### F1 — BLOCKER: the counter reads its acceptance contract from the graded tree; a landing can rewrite the frozen claims.json and shrink its own test

`load_config()` (accept-c.py:432-… reads `(os.path.join(mat, CLAIMS),
"lands tree")` first, then falls back to the lane **worktree**) derives
`row_set`, `entries`, `rejects.*` and `ground.fragments` from
`reports/round-73/claims.json` **at `<lands>`**. Nothing pins those bytes to
the frozen blob. P7b committed a claims.json whose claim-C `row_set` is
`[{"id": "S876"}, {"id": "S877"}]` (blob at lands
`eb9a39e99a1eab419e0af09b96b577902f91cd4a` ≠ frozen `7d28537d…`), added only
rows S876–S877, stubbed the second entry — and the declared command printed:

```
$ python3 -B reports/round-73/accept-c.py --root . --lands b88f66f69d2b
# config source: lands tree: row_set, entries, rejects.refused_staged, rejects.refused_files, rejects.families, rejects.forbidden_ids, ground.fragments
# adopted rows: S876 S877
ACCEPT-C-73: PASS legs=11/11
```

The claim leg says (claims.json, claim C `legs[1]`): "the registry diff
base..<lands> adds exactly S876..S880 (contiguous)". At P7b's lands that leg
is **false** (two rows added) while the counter — the claim's declared
verifier — prints PASS. The rewrite also silently drops the staged-id pairing
(`row_staged`), loosening COLLCHECK further. The config-source flip is itself
a verdict hazard: P0b's receipt header reads `config source: lane worktree: …`
because base predates claims.json, so a pre-claims revision is graded under
whatever claims.json the grader happens to have checked out (the M5-class
worktree leak the Ca counter fixed in r2/r3; accept-c.py is still r1).

**Tightening:** in `main()`, after materializing, require
`sha256(mat/CLAIMS)` == the frozen digest (compile `7d28537d…`'s bytes-hash as
a constant, or compare `git rev-parse <lands>:reports/round-73/claims.json`
to the frozen blob id), and delete the worktree fallback — config comes from
the materialized tree only, else hard error.

### F2 — MAJOR: ROWS does not require the five mined rows to reach the entries

Leg wording (claim C `legs[1]`, tail): "used-by exactly the citing entries
whose source: lines cite it, union = both entries". That is a *union-of-both*
test, not a per-row test. P7a: entries keep one `source:` line each (S876,
S880); S877–S879 rows get `used-by: —`; everything else real:

```
$ python3 -B reports/round-73/accept-c.py --root . --lands a4127f0276b7
ACCEPT-C-73: PASS legs=11/11
```

Committed rows at that lands: `S877 used-by='—' S878 used-by='—' S879
used-by='—'`. Three of five "opened and mined" rows cite into no entry;
CENSUS treats mined-with-`—`-used-by as **W03, a warning that never fails the
lane** (sources-census.sh header: "warnings do not affect clean lanes").
**Tightening:** `leg_rows` must require `cited.get(sid)` non-empty for every
adopted row (`union` per-row coverage), i.e. each adopted row is a source of
at least one admitted entry.

### F3 — MAJOR: ENTRIES is satisfied by filler; no leg ever compares entry bodies with the captures

P1 replaced both entries with a nine-field header plus filler
(`body=561` words each, floor = 478 = `corpus/knowledge/culture-material/
heritage-taxonomy-models.amend-2026-10-24-r13.md`, the smallest of 245
knowledge files at base; `quoted_spans_in_body=0`):

```
$ python3 -B reports/round-73/accept-c.py --root . --lands 2c440ee85f3c
ACCEPT-C-73: PASS legs=11/11
```

ENTRIES checks field names, non-placeholder values and a word floor. ROWS/
REPOINTED read only the `source:` lines and id tokens. The mined prose — the
thing the claim actually admits — could be lorem ipsum. **Tightening:**
`leg_entries` must require each entry body to contain, per cited row, the
row's evidence quote as a QUOTE_RE span (≥1 quoted anchor per cited row),
so filler with zero quoted spans fails.

### F4 — MAJOR: the anchor↔Gate↔evidence quote triangle is self-referential; invented quotes and forged captures pass

P4 invented five nonsense quotes and forged all five evidence files:

```
# evidence S876 — claim C GATE (round 73) [P4 forged capture]        (committed)
fetch: GET https://ojs.unito.it/index.php/ricognizioni/article/view/7099
user-agent: Mozilla/5.0 (X11; …) Chrome/130.0 Safari/537.36
access-date: 2026-10-25
http-status: 200
bytes: 31337
sha256: c3a5607d063059331e5eb7c387297bc8e306ec2c91dae2c78a6e42046f8259a0
extract: junk probe; no fetch performed
quote-found-verbatim: yes
quote: purple penguins assemble seventeen telescopes beside the frozen harbor every quiet tuesday morning
```

```
$ python3 -B reports/round-73/accept-c.py --root . --lands 761c66fbb707
ACCEPT-C-73: PASS legs=11/11
```

`quote-found-verbatim: yes` is a self-attested field; `http-status`, `bytes`
and `sha256` are never re-derived; the only cross-checks run *between* the
three files the junk author also wrote (quote ⊆ anchor, quote ⊆ window, Gate
row carries quote). P3 shows the same on one row with everything else real.
The claim's kill_rule ("any cited source lacks … a committed evidence
capture") is therefore satisfiable by fabrication: a capture exists, is
committed, and is forged. **Tightening:** grade-time re-fetch with the
recorded UA comparing `sha256` (network failure = inconclusive, never pass),
or verify the quote against the independent Wayback capture URL already
present in each row's source cell with its digest committed; at minimum,
store the raw fetched bytes in-tree and recompute the digest and the
verbatim check from them instead of trusting the `quote-found-verbatim`
field.

### F5 — MAJOR: "no staged row appended as-is" is enforced by shape only; the staged capture date survives laundering inside the anchor cell

P2 copied the five staged rows (`/home/vgpnk/Projects/shokuknow/merge/
kotodama/SOURCES.append.md`, staged ids S881/S882/S892/S893/S901) verbatim,
then applied only the mechanical edits the leg checks for: renumber,
`opened 2026-10-23 → 2026-10-25`, recheck prose → `180d`, used-by appended,
escaped pipes trimmed. Evidence/Gate quotes were satisfied from the staged
**locator** cells (e.g. `"Abstract + Keywords (Constructed Languages,
Phonology,"` — a locating description, not page text). Result:

```
$ python3 -B reports/round-73/accept-c.py --root . --lands d030b62eaed3
ACCEPT-C-73: PASS legs=11/11
```

Committed S876 row at that lands: `opened='2026-10-25' status='mined'
recheck='180d'`, anchor cell = "Abstract + Keywords (Constructed Languages,
Phonology, Diachronic linguistics, Method-Oriented Teaching) — **article page
as served 2026-10-23**" — the staged package's capture date, two days before
the claimed round access date, rides in the anchor cell of a row swearing it
was opened 2026-10-25. The opened-date check launders rather than detects.
**Tightening:** `leg_rows` must scan every adopted row's cells for dated
capture stamps (`as served <date>`, `capture <timestamp>`) and require each
such date to equal ACCESS_DATE; and require the evidence quote to occur as a
QUOTE_RE-delimited *quotation* inside the anchor cell (not a bare substring
of locator prose).

### F6 — MINOR: the Gate reject side is count-shaped

P6a (probe as literally stated: no reject rows) is **caught**:
`LEG FAIL GATE — no reject row (want >=1)` plus REJECTS failing on the four
refused file names. But P6b replaces the six real refuse rows with one
fabricated row and names the refused files in prose:

```
| conlang-scholarship.amend-9999.md | S999 | status: junk probe HTTP 200; automation: none; reason: never probed, invented by this row | flip: none | https://example.org/junk-probe | refused |
$ python3 -B reports/round-73/accept-c.py --root . --lands 93a20a75782b
ACCEPT-C-73: PASS legs=11/11
```

GATE wants ">=1 reject; every reject row carries its probed URL, reason and
flip" — a row can *declare* a URL "probed" that nothing probed, naming a file
that does not exist. GATE never ties reject rows to
`rejects.refused_staged`/`refused_files`. **Tightening:** the Gate reject-row
set must enumerate exactly the claims.json refused set (bijection per id and
per refused file), not ">=1".

### F7 — MINOR: the campaign-id net is case-sensitive

P5a (uppercase `(S894)` in entry prose) is **caught**: `LEG FAIL REPOINTED —
corpus/knowledge/linguistics/conlang-scholarship.md:106 inline id S894 has no
registry row`. P5b (`(staged s894)`, line 106 of the same entry) passes:

```
$ python3 -B reports/round-73/accept-c.py --root . --lands a960e80670ea
ACCEPT-C-73: PASS legs=11/11
```

`TOKEN_RE = r"\bS\d{3,}\b"` (and check-cited-lines.py's SID) match only the
canonical uppercase form, so the REPOINTED promise "campaign ids appear
nowhere" is enforced only for exact-case tokens. **Tightening:** case-
insensitive token scan `(?i)\bs\d{3,}\b` in REPOINTED (and SID in
tools/check-cited-lines.py).

### Observations (not scored)

- guard-proof mirrors carry absolute symlinks (`mirror/SKILL.md`,
  `mirror-a3/SKILL.md`, mode 120000, target
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin/SKILL.md`): COLLCHECK's
  recursive read of `GUARD_DIR` follows them into **live lane worktree
  bytes**, in any clone, including the real grading runs. No verdict moved in
  these probes (P0a COLLCHECK PASS with the same bytes), but it is a
  worktree-read channel of the class QUALITY 19 bans.
- `tools/check-cited-lines.py` counts findings, never requires citations; a
  body with zero S-tokens prints `CITED-LINES: 0 finding(s) in 2 file(s)` and
  passes (subsumed by F3).

## Could NOT check

- Whether the **real** five landed quotes are on the real live pages — no
  live fetch was made by this seat (and the counter itself never fetches; see
  F4). Live/Wayback verification belongs to the reopen seats.
- `accept-ca.py` / claim Ca — outside this item.
- Census behavior on registry shapes other than the ones these probes
  produced (only P0–P7 shapes were exercised).
- Whether the selftest's 24 mutants cover any of F1–F7 — the mutants were
  not enumerated individually by this seat; the selftest receipt
  (`telemetry/selftest-r3.txt`) was not re-run here.

## Tooling

Nothing installed (no pacman, no new tools): python3 3.14, git 2.x and gawk
were already present; the census script was copied unmodified from the fleet.

## Restoration / bounds evidence

- Lane repo untouched except this report file: `git -C <lane> rev-parse HEAD`
  = `0316b8883b4f8d44b8efd720140e7f52f734a102` before and after; landed tree
  `9b10fa06a2d3756c8bacfc8fc7b2115921370d97`; `status --porcelain` shows only
  the wave-2 orchestration files and peers' reports (`?? .ufo/waves/round-73/
  build-w2.py`, `w2.ready`, `w2.ready.dispatched`, `w2/`) — no tracked file
  modified, no index change, no jj/git mutation by this seat.
- All junk commits live only in the throwaway clone `/tmp/MutPredicateC/
  probe/lane`; the outer dir `/tmp/MutPredicateC/probe` is itself a git repo
  whose toplevel was verified (`/tmp/MutPredicateC/probe`) before the first
  commit; the mut identity was used only there.
- Fleet root and shokuknow were only read (`scripts/sources-census.sh`,
  `merge/kotodama/SOURCES.append.md` — the latter read-only, no campaign
  tools run there).
