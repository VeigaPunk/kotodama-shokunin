# ExecPacketBuilder59 — claim C blind SUPPORT packet builder

Round 59 BUILD, lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, claim C (coverage, amulets /
talismans / apotropaic marks). Deliverable: the tool that turns the landed rows, the entry and the
planted file into the eight blind reviewer packets and `planted-key.json`, with a selftest, a
mutant, and a drift guard the L1 can re-run before the support task call.

- Script: `/fast/scratch/hyaku/kotodama-r59/ExecPacketBuilder59/build-packets.py` (668 lines,
  Python 3 stdlib only, `sys.dont_write_bytecode` set so it never writes `__pycache__` into the lane).
- Lane writes: **this report only.** No installs or updates (nothing needed); no `git`/`jj`.
- Inputs read: `reports/round-59/accept-c.py`, `reports/round-59/reopen-quote.py`,
  `corpus/SOURCES.md`, `corpus/knowledge/linguistics/toponymy-place-names.md` (dry-run entry only —
  claim C's rows S600–S659 and its entry do not exist yet and are untouched), plus scratch files
  under my own directory.

## 1. The contract it implements (read from accept-c's SUPPORT leg)

`accept-c.py` parses a seat packet with

```
PACKET_BLOCK = re.compile(r"^### (P\d{2})[ \t]*\n((?:(?!### ).*\n?)*)", re.M)
PACKET_FIELD = re.compile(r"^(quote|teaches|entry|url):[ \t]*(.*)$", re.M)
```

and binds `VERDICT Pnn ...` to a row only when the block's `quote`, `teaches` and `entry` — each
`.strip().strip('"')` then `locator.normalise()`d — equal that row's `proposition(sid)`:

```
(locator.normalise(row_target(cells)[1] or ""),           # first quoted span of SOURCES cells[6]
 locator.normalise(cells[7] if len(cells) > 7 else ""),   # the teaches cell
 locator.normalise(" ".join(cites)))                      # entry lines citing \bS###\b, ids removed
```

So the builder derives exactly those three values per row and prints them one per line: the quote is
`row_target`'s first quoted span (not the whole locator cell), the teaches cell is copied, and the
entry field is every line of the entry containing the id as a whole word, joined with one space,
`\bS\d{3,}\b` replaced by a space — the same substitution the counter performs. Whitespace is
collapsed only, which cannot change the comparison because `normalise` maps any run of non-word
characters to one space and casefolds. The block's `url` line carries every URL `row_target` finds in
cells[2], in order, space-separated (live URL first, then a Wayback capture of the same page when the
row lists one) — the counter does not compare it, but the reviewer needs it to open the page.

Block shape, exactly four lines after the heading and nothing else:

```
### P07
url: <every source URL of the row>
quote: "<anchor quote>"
teaches: <teaches cell>
entry: <citing entry lines, ids removed, one line>
```

## 2. Mechanics

- **Coverage.** Every id lands on exactly `--per-row` distinct seats, chosen each round from a
  seeded random seat permutation ordered by current real-row load, so loads stay balanced and ties
  are random. It refuses (`exit 2`, nothing written) when a seat would get no real row, when
  `--per-row` exceeds the seat count, or when the entry cites any id outside `--ids`.
- **Planted.** The planted list is seeded-shuffled and rotated across seats,
  `pool[(seat_index * k + step) % P]` for `k = --planted-per-seat`, so a seat's planted rows are
  distinct and the same planted row is spread over different seats. `--planted-per-seat > P` is
  refused.
- **Labels.** Each seat's items (reals + planted) are shuffled with a per-seat seed derived from the
  master seed, then labelled `P01..` in that order. No planted-first, no interleave, identical block
  shape. The build fails if every seat ends up with planted labels at the same positions (a
  positional tell); change `--seed`.
- **Blindness.** Planted field values carrying an S-id or the word `planted` are refused outright
  (the packet strips ids from real entries, so a planted entry with an id would not look like a real
  one and could hand the reviewer a real row's id). The rendered packet is then scanned for
  `(?i)\bs\d{3,}\b`, `planted`, `kind:`, `why-not-supported:` and every long extra field value of the
  planted file. Any hit means nothing is written. The packet preamble never prints a literal
  `VERDICT Pnn ...` example, so a reviewer copying it cannot manufacture a parseable verdict.
- **Round-trip.** Before writing, every block is re-parsed with accept-c's own `PACKET_BLOCK` /
  `PACKET_FIELD` and compared with the row's proposition; a planted block must match one of the input
  planted rows and no planted row may appear twice in a seat. `--check [DIR]` repeats all of that and
  also fails on any byte difference from a fresh render — the drift guard for a late entry edit.
- **Declared hash.** `--declared reports/round-59/planted-rows.sha256` refuses to build when the
  planted file does not hash to the already-committed sidecar (`bc7c7731…`), because the counter
  compares those two.
- **Key.** `planted-key.json` is `{"seats": {Seat: {"P01": "S6xx" | "PLANTED", …}}}` plus audit keys
  (`round`, `seed`, `per_row`, `planted_per_seat`, `sources_sha256`, `entry_sha256`,
  `planted_sha256`); accept-c reads only `.get("seats")`. The build prints its sha256 for
  `reports/round-59/planted-key.sha256`.

## 3. Runs (command, output, exit code)

Outputs and exit codes below are verbatim; a few long commands elide repeated scratch paths with
`...`, and two runs were captured through `tail` (noted at the block).

### 3.1 Selftest on synthetic input

```
$ cd /fast/scratch/hyaku/kotodama-r59/ExecPacketBuilder59 && timeout 300 python3 -B build-packets.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin --selftest
ok   coverage: clean
ok   blindness: clean
ok   roundtrip: clean
ok   shape: field_orders=1 planted_counts={'SupportA59': 2, 'SupportB59': 2, 'SupportC59': 2, 'SupportD59': 2}
ok   quote-wrap: doubled quote lines in []
ok   url-join: seats showing the two-URL row: 2 (per_row=2)
ok   planted-positions: distinct planted-position sets=3 of 4
ok   determinism: same seed, same bytes
ok   seed-sensitivity: different seed, different packets
SELFTEST PASS checks=9 blocks=22 reals=14 planted=8 roundtrip=14/14
exit=0
```

The selftest builds 7 synthetic rows (one carrying a live URL plus a `web.archive.org/...id_/`
capture), a synthetic entry (one line citing two ids plus one uncited line) and 4 planted blocks
carrying `kind` and `why-not-supported`, into a temp dir under the CWD, with 4 seats, `--per-row 2`,
`--planted-per-seat 2`. It asserts, through accept-c's regexes: every id on exactly 2 seats, every
seat 2 planted blocks and ≥1 real row, one field order (`url, quote, teaches, entry`), no doubled
`quote: ""`, the two-URL row on exactly 2 seats, planted labels not at identical positions, same seed
→ same bytes, different seed → different packets, and every block round-trips to the same normalised
proposition. Temp dir removed on exit (`ls selftest-*` → absent).

### 3.2 Mutant that leaks the id (must fail)

```
$ timeout 300 python3 -B build-packets.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin --selftest --mutant leak-id
ok   coverage: clean
FAIL blindness: SupportA59: packet carries the id 'S603'; SupportB59: packet carries the id 'S600'; SupportC59: packet carries the id 'S603'
FAIL roundtrip: SupportA59 P02: round-trip differs for S603; SupportA59 P04: round-trip differs for S604; SupportA59 P05: round-trip differs for S602
ok   shape: field_orders=1 planted_counts={'SupportA59': 2, 'SupportB59': 2, 'SupportC59': 2, 'SupportD59': 2}
ok   quote-wrap: doubled quote lines in []
ok   url-join: seats showing the two-URL row: 2 (per_row=2)
ok   planted-positions: distinct planted-position sets=3 of 4
ok   determinism: same seed, same bytes
ok   seed-sensitivity: different seed, different packets
SELFTEST FAIL
exit=1
```

The mutant appends ` (S600)`-style ids to each real block's `teaches` line; the blindness scan names
the offending id and the selftest exits 1. Second mutant (planted marker instead of id):

```
$ timeout 300 python3 -B build-packets.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin --selftest --mutant leak-planted
ok   coverage: clean
FAIL blindness: SupportA59: packet carries 'planted'; SupportB59: packet carries 'planted'; SupportC59: packet carries 'planted'
FAIL roundtrip: SupportA59 P01: planted block is not one of the planted rows; SupportA59 P02: round-trip differs for S603; SupportA59 P03: planted block is not one of the planted rows
ok   shape: field_orders=1 planted_counts={'SupportA59': 2, 'SupportB59': 2, 'SupportC59': 2, 'SupportD59': 2}
ok   quote-wrap: doubled quote lines in []
ok   url-join: seats showing the two-URL row: 2 (per_row=2)
ok   planted-positions: distinct planted-position sets=3 of 4
ok   determinism: same seed, same bytes
ok   seed-sensitivity: different seed, different packets
SELFTEST FAIL
exit=1
```

### 3.3 Real inputs, dry run (old rows S500–S543 + the round-58 toponymy entry as a stand-in)

44 real rows (13-cell rows, real URLs, real multi-line citations), 8 seats, `--per-row 2`,
`--planted-per-seat 3`, `--seed 59`, 6 scratch planted blocks:

```
$ IDS=$(python3 -c "print(','.join(f'S{n}' for n in range(500,544)))") && timeout 300 python3 -B build-packets.py \
    --root /home/vgpnk/Projects/shokunin/kotodama-shokunin \
    --entry corpus/knowledge/linguistics/toponymy-place-names.md \
    --ids "$IDS" --planted .../dryrun-planted.md \
    --seats SupportA59,SupportB59,SupportC59,SupportD59,SupportE59,SupportF59,SupportG59,SupportH59 \
    --per-row 2 --planted-per-seat 3 --seed 59 --out .../dryrun
seat SupportA59 blocks=14 reals=11 planted=3
seat SupportB59 blocks=14 reals=11 planted=3
seat SupportC59 blocks=14 reals=11 planted=3
seat SupportD59 blocks=14 reals=11 planted=3
seat SupportE59 blocks=14 reals=11 planted=3
seat SupportF59 blocks=14 reals=11 planted=3
seat SupportG59 blocks=14 reals=11 planted=3
seat SupportH59 blocks=14 reals=11 planted=3
coverage rows=44 seats=8 per_row=2 planted_per_seat=3 assignments=88 min_real_per_seat=11
blind ids=0 planted=0 kind=0 why=0 tokens=12
roundtrip blocks=112 reals=88 planted=24 roundtrip=88/88
planted-key.json sha256 f6387e731b0906559e78aa2ef0f3f51539214d567be30cbd54d4fa4fb354c513
sources sha256 22799e0afa5a44b9b4e15d690015deceed1a83f39103608aa11cad421e3492a5
entry sha256 a73ff4394476c852c939b4e355acdc28c9f23299ace8215b4bc45f5296f7959b
planted sha256 7a1e3edf16ac5d3cb2404b4d8f41aa68c3f083e24b977ccae665f431e1d80d73
wrote 9 files to /fast/scratch/hyaku/kotodama-r59/ExecPacketBuilder59/dryrun
PACKETBUILDER OK
exit=0
```

Check on the written directory:

```
$ ... same flags ... --check
seat SupportA59 blocks=14 reals=11 planted=3
... (8 seats identical to above) ...
coverage rows=44 seats=8 per_row=2 planted_per_seat=3 assignments=88 min_real_per_seat=11
blind ids=0 planted=0 kind=0 why=0 tokens=12
roundtrip blocks=112 reals=88 planted=24 roundtrip=88/88
planted-key.json sha256 f6387e731b0906559e78aa2ef0f3f51539214d567be30cbd54d4fa4fb354c513
CHECK PASS dir=/fast/scratch/hyaku/kotodama-r59/ExecPacketBuilder59/dryrun
exit=0
```

Independent count over the written packets: `grep -c 'VERDICT P'` → 0 in all eight packets (no
copyable verdict line), `grep -cE '\bS[0-9]{3}\b'` → 0 in all eight, `grep -c '^### '` → 14 in each.

### 3.4 Drift guard: one late edit to a cited entry line

`entry-drift.md` is a copy of the dry-run entry with `1960s` → `1950s` in the line citing S505 only
(output shown through `tail -6`):

```
$ ... --entry .../entry-drift.md ... --check
entry sha256 63f1ebc64b2b979194996a96427eebb1cdb5bcac2c763832d07fa7550760e9ec
...
PROBLEM packet-SupportA59.md: differs from a fresh build at line 21
PROBLEM packet-SupportH59.md: differs from a fresh build at line 87
PROBLEM planted-key.json: differs from a fresh build at line 2
CHECK FAIL dir=/fast/scratch/hyaku/kotodama-r59/ExecPacketBuilder59/dryrun
exit=1
```

Exactly the two seats holding S505 report the difference — the per-row coverage and the block
positions are the ones the counter will read. This is why packets must be built after the entry is
final and `--check` must run once more before dispatch.

### 3.5 Refusals (each exits 2 and writes nothing; `ls guard` → absent)

```
=== a: id with no row
$ --ids S500,S501,S999 --planted .../dryrun-planted.md --seats SupportA59,SupportB59 --per-row 1 --planted-per-seat 3
ERROR S999: no row in /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
exit=2
=== b: planted field carrying an id
$ --ids S500,S501 --planted .../bad-planted.md --seats SupportA59,SupportB59 --per-row 1 --planted-per-seat 3
ERROR /fast/scratch/hyaku/kotodama-r59/ExecPacketBuilder59/bad-planted.md PLANTED-4 teaches: carries an S-id; packets strip ids from real entries, so write the planted teaches without one
exit=2
=== c: per-row above the seat count
$ --ids S500,S501 --planted .../dryrun-planted.md --seats SupportA59,SupportB59 --per-row 3 --planted-per-seat 3
ERROR --per-row 3 must be 1..2 (the seat count)
exit=2
=== d: rows too few for seats
$ --ids S500,S501 --planted .../dryrun-planted.md --seats SupportA59,SupportB59,SupportC59 --per-row 1 --planted-per-seat 3
ERROR seat(s) with no real row: SupportC59; 2 rows at --per-row 1 cannot reach 3 seats
exit=2
=== e: id whose row the entry does not cite
$ --ids S500,S501,S560 --planted .../dryrun-planted.md --seats SupportA59,SupportB59 --per-row 1 --planted-per-seat 3
ERROR S560: no line of the entry cites it; the counter binds a verdict only to a cited row
exit=2
=== f: entry cites rows outside --ids
$ --ids S500 --planted .../dryrun-planted.md --seats SupportA59 --per-row 1 --planted-per-seat 3
ERROR the entry cites 43 row(s) outside --ids (S501, S502, S503, S504, S505, S506, S507, S508, ...); every cited row needs a packet or the counter finds no SUPPORTED verdict for it
exit=2
```

### 3.6 Declared planted hash

```
=== declared mismatch (the real committed sidecar names the L1's not-yet-written file)
$ ... --planted .../dryrun-planted.md --declared .../kotodama-shokunin/reports/round-59/planted-rows.sha256 ...
ERROR --declared /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/planted-rows.sha256 names bc7c77310a08, but /fast/scratch/hyaku/kotodama-r59/ExecPacketBuilder59/dryrun-planted.md hashes to 7a1e3edf16ac; the counter compares the sidecar with this file
exit=2
=== declared match (scratch sidecar for the same file; shown through tail -4)
$ ... --declared .../planted-dryrun.sha256 --seats SupportA59,SupportB59 --per-row 2 ...
wrote 3 files to /fast/scratch/hyaku/kotodama-r59/ExecPacketBuilder59/declared-ok
PACKETBUILDER OK
exit=0
```

### 3.7 Row-to-block correspondence (one real row, S505, unedited)

```
cells: 13  cells[2]=U.S. Geological Survey, 2015 (September 1), Old Name Officially Returns to Nation's Highest Peak — https://www.usgs.gov/news/featured-story/old-name-o…
cells[6]=§ An impasse with Congress and the Board: "the BGN adopted a policy in the 1960s that it would not consider geographic name issues that were the subject of pending congressional le…
cells[7]=From the 1960s the federal naming board refused to rule on any geographic name dispute while Congress had a bill pending about it.
entry lines citing it:
   - The US naming board adopted a policy in the 1960s that it would not consider geographic name issues that were the subject of pending congressional legislation (<id>). A legislature can freeze a renaming simply by keepi…
packet block P01:
url: https://www.usgs.gov/news/featured-story/old-name-officially-returns-nations-highest-peak
quote: "the BGN adopted a policy in the 1960s that it would not consider geographic name issues that were the subject of pending congressional legislation"
teaches: From the 1960s the federal naming board refused to rule on any geographic name dispute while Congress had a bill pending about it.
entry: - The US naming board adopted a policy in the 1960s that it would not consider geographic name issues that were the subject of pending congressional legislation ( ). A legislature can freeze a renaming simply by keeping a bill pending.
```

The `( )` is the counter's own substitution (`\bS\d{3,}\b` → space) and appears identically for
every block; `normalise` drops it. Nothing else in the block differs from the row.

## 4. Hand-off: the exact pre-dispatch sequence

After the rows S600–S659 and the entry have landed and `.ufo/waves/round-59/support/planted-rows.md`
is written (it must hash to `bc7c7731…`, the value `reports/round-59/planted-rows.sha256` already
declares), from the lane root:

```
python3 -B /fast/scratch/hyaku/kotodama-r59/ExecPacketBuilder59/build-packets.py \
  --root . --ids S600,S601,…  \                       # every id the entry cites; `--ids @file` works
  --planted .ufo/waves/round-59/support/planted-rows.md \
  --declared reports/round-59/planted-rows.sha256 \
  --out .ufo/waves/round-59/support \
  --seats SupportA59,SupportB59,SupportC59,SupportD59,SupportE59,SupportF59,SupportG59,SupportH59 \
  --per-row 2 --planted-per-seat 3 --seed 59

python3 -B /fast/scratch/hyaku/kotodama-r59/ExecPacketBuilder59/build-packets.py \
  --root . <same flags> --check .ufo/waves/round-59/support
```

Then write the printed `planted-key.json sha256` as the first token of
`reports/round-59/planted-key.sha256` (accept-c reads `.split()[0]`), add the eight
`packet-SupportX59.md` and `planted-key.json` paths to C's lands (they are already in
`claims.json` and `separability-manifest.json`), register the eight seats with
`agentId KotodamaR59.SupportX59`, and re-run `--check` after any later entry edit.

## 5. Risks and limits

- **Ordering.** The counter compares packets with the landed entry byte-derived, so any edit to a
  cited entry line after the build breaks every affected block's round-trip. `--check` is the one
  command that shows it; run it immediately before the support task call.
- **Planted content is the L1's, not the tool's.** The builder only guarantees shape, blindness and
  that planted blocks are the ones in the file. Whether a planted row is genuinely NOT-SUPPORTED is
  a property of its text; a planted row that happens to be true would fail the seat's qualification
  (`planted and all((p,"NOT-SUPPORTED")…)`), and the tool cannot detect that.
- **Planted fields must be id-free.** If the L1 drafts planted rows by copying real rows, the ids
  must be removed first; the builder refuses otherwise (guard b) because the packet strips ids from
  real entries and a planted id would both break the shape parity and could hand a reviewer a real
  row's id.
- **All seats need real rows.** With 8 seats and `--per-row 2`, at least 8 cited rows are needed
  (C targets ≥20 cited, so fine); otherwise it refuses rather than shipping a seat that can never
  qualify.
- **Randomised positions are checked, not guaranteed.** With very few blocks per seat the
  identical-position check can fire; change `--seed` (record which seed was used — it is in the key).
- **Not exercised here:** the full counter (SET/SWEEP/LOCATE/BOILER/TOPIC and SUPPORT against real
  reviewer reports) — that needs claim C's rows and entry, which do not exist yet. My run proves the
  packet contract against real 13-cell rows and accept-c's own regexes, not the network legs.

## 6. Hygiene

- Scratch only: `/fast/scratch/hyaku/kotodama-r59/ExecPacketBuilder59/{build-packets.py,
  dryrun-planted.md, bad-planted.md, entry-drift.md, entry-mini.md, planted-dryrun.sha256, dryrun/,
  declared-ok/}`. Selftest temp dirs are removed; refused runs create no `--out` directory.
- Lane writes: this report. `reports/round-59/__pycache__/{reopen-quote,rowcheck}.cpython-314.pyc`
  predate my first run (mtime 00:10:08 / 00:10:18, unchanged by my runs) — not mine, left alone.
- No tools installed or updated; no processes left running; no `git`/`jj` write commands.
