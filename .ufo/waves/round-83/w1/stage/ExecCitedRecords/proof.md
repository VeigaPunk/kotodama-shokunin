# ExecCitedRecords — proof for check-cited-records.py (kotodama round 83, w1)

Seat deliverable: an independent implementation of the QUALITY-criterion-31
checker at

    .ufo/waves/round-83/w1/stage/ExecCitedRecords/check-cited-records.py

written to the seat spec's frozen contract. Per the L1's standing instruction
this round, the lane path `tools/check-cited-records.py` was NOT written by
this seat (the L1 installed a working checker first; comparison below).

Method: the frozen claims/counters commit `21277b0` was materialized read-only
with `git archive 21277b089e3c64c247bb4e0fcb033abfdfa1e668 | tar -x` into the
seat scratch root; no lane or fleet byte was touched by any proof command.

Masking: criterion 31 binds this round, so no absolute scratch path appears
below. Every flagged scratch path is rendered as `<ABS-SCRATCH-n>`; the
unmasked bytes are committed at the cited documents of the frozen commit and
regenerate from the commands in "Reproduce".

## Frozen contract implemented

- CLI: `--root DIR` (default `.`), `--from-round N` (default 83),
  `--bind-round N` (default 83), `--json`, `--selftest`.
- Documents for round k (k >= --from-round): `reports/round-<k>/**/*.md` and
  `corpus/lessons/round-<k>*.md` (leading digit run is k; round-8 vs round-83
  cannot mix).
- EMPTY leg: backticked tokens matching
  `(reports|corpus|tools|\.ufo)/[A-Za-z0-9_./-]+\.(md|txt|json|py|tsv|yml)`
  that resolve under --root to a regular file of size 0 -> `EMPTY <path> <doc>`.
  Unresolved tokens, tokens escaping --root, non-files: not findings.
- SCRATCH leg: for k >= --bind-round, absolute paths matching
  `^/(tmp|var/tmp|fast/scratch)/` (boundary lookbehind so the match cannot be
  preceded by a path character; trailing sentence dots trimmed) ->
  `SCRATCH <path> <doc>`.
- Output: finding lines then exactly one
  `CITED-RECORDS: <empty> empty / <scratch> scratch` line; exit 0 iff both 0,
  1 on findings, 2 with `CITED-RECORDS-ERROR <msg>` on could-not-evaluate;
  no traceback ever.
- `--json`: `{"empty": [{"path","doc"}...], "scratch": [...], "documents": N}`
  on one line; exit codes unchanged.
- `--selftest`: 15 checks over fixtures in a TMPDIR-honouring temp dir.

## Run A — frozen tree, `--from-round 82 --bind-round 82`

Command: `python3 check-cited-records.py --root <frozen checkout of 21277b0>
--from-round 82 --bind-round 82`

Output (verbatim; scratch shapes masked as `<ABS-SCRATCH-n>`):

```
EMPTY reports/round-82/counter-revisions.md corpus/lessons/round-82-verifier-spotcheck.md
EMPTY reports/round-82/counter-revisions.md corpus/lessons/round-82.md
SCRATCH <ABS-SCRATCH-1> corpus/lessons/round-82-verifier-spotcheck.md
SCRATCH <ABS-SCRATCH-2> corpus/lessons/round-82-verifier-spotcheck.md
CITED-RECORDS: 2 empty / 2 scratch
exit=1
```

- `<ABS-SCRATCH-1>` is the fast-scratch shape root: the document cites it
  ellipsis-masked (`corpus/lessons/round-82-verifier-spotcheck.md` line 233 at
  21277b0); the reported path ends at the shape root because the frozen tail
  class stops at the ellipsis.
- `<ABS-SCRATCH-2>` is the tmp shape root, likewise ellipsis-masked (same
  document, line 64). The seat text calls these "the two /fast/scratch/
  receipts"; on the frozen bytes the two in-scope scratch citations are one
  fast-scratch shape and one tmp shape — both are flagged, and both are the
  defect the round-82 spot-check §6 names.
- `reports/round-82/counter-revisions.md` is 0 bytes at 21277b0
  (`git cat-file -s 21277b089e3c64c247bb4e0fcb033abfdfa1e668:reports/round-82/counter-revisions.md`
  = 0) and is cited inside backticks by `corpus/round-82.md` line 12 and by
  `corpus/lessons/round-82-verifier-spotcheck.md` lines 207-208; one finding
  per citing document, deduplicated per (path, doc) as the contract requires.

## Run B — same tree, default binding (`--from-round 83 --bind-round 83`)

Command: `python3 check-cited-records.py --root <frozen checkout of 21277b0>`

```
CITED-RECORDS: 0 empty / 0 scratch
exit=0
```

`--json` on the same run: `{"empty": [], "scratch": [], "documents": 1}`.
One round-83 document exists at the freeze — `reports/round-83/counter-revisions.md`,
landed by the frozen counter's own r2 revision; it carries no scratch path and
cites no empty record, so the green is a true 0/0 over one document, not a
vacuous scan (the seat text's "none exist yet" predates that r2 record). That
the green is substantive was falsified positively below.

## Falsification (planted round-83 documents, default binding)

A scratch copy of the frozen tree gained: `reports/round-83/planted-zero.md`
(0 bytes, cited in backticks by a planted `corpus/lessons/round-83.md`), a
tmp-shape receipt path in that lesson's prose, and `reports/round-83/uncited-zero.md`
(0 bytes, mentioned WITHOUT backticks so it is not a citation).

First attempt at this fixture backticked the uncited file's own path in the
lesson prose; the checker correctly flagged it (any backticked matching token
is a citation — the fixture, not the tool, was wrong). Fixture corrected;
rerun:

```
EMPTY reports/round-83/planted-zero.md corpus/lessons/round-83.md
SCRATCH <ABS-SCRATCH-3> corpus/lessons/round-83.md
CITED-RECORDS: 1 empty / 1 scratch
exit=1
```

Both planted defects caught; the uncited zero-byte file not counted. Run B's
frozen-tree green is therefore a measured sensitivity, not a blind spot.

## Independent reverse cross-check

A separate diagnostic (different code path: substring containment inside
backticked spans instead of regex token extraction) enumerated, over the same
frozen tree and document floor: 4 documents, 125 zero-byte files in the whole
tree. Reverse-empty findings: exactly the 2 (path, doc) pairs of Run A.
Reverse-scratch findings: exactly the 2 pairs of Run A. Nothing missed,
nothing invented.

## Selftest

`TMPDIR=<seat scratch> python3 check-cited-records.py --selftest`:

```
ok 1 - clean tree is green
ok 2 - empty cited record is caught
ok 3 - nonempty cited record is accepted
ok 4 - scratch path inside the bind window is caught
ok 5 - same scratch path in an older round is ignored
ok 6 - unresolved cited token is ignored
ok 7 - zero-byte file that is not cited is not counted
ok 8 - json output has the exact contract shape
ok 9 - absent root exits 2 with an error line
ok 10 - no traceback on any code path
ok 11 - exactly one summary line per non-error run
ok 12 - same empty record in two documents yields two findings
ok 13 - citation outside the four roots is ignored
ok 14 - citation escaping the root is ignored
ok 15 - all three scratch shapes are caught
SELFTEST: PASS (15 checks)
exit=0
```

`py_compile` is clean (bytecode directed at the seat scratch). Stdlib only;
no repository import (no counterlib). Selftest output prints no absolute
paths (fixture root masked in any failure detail), and its fixtures are
removed after the run.

## Comparison against the installed `tools/check-cited-records.py`

The installed checker (read after the L1's notice) was run on the same frozen
checkout, same bindings:

| probe (frozen 21277b0) | this seat's stage tool | installed tool |
|---|---|---|
| `--from-round 82 --bind-round 82` | `2 empty / 2 scratch`, exit 1 | `2 empty / 9 scratch`, exit 1 |
| default binding | `0 empty / 0 scratch`, exit 0 (1 document) | `0 empty / 2 scratch`, exit 1 |
| `--selftest` | `SELFTEST: PASS (15 checks)` | `SELFTEST: PASS (12 checks)` |

Line formats are byte-identical (`EMPTY <path> <doc>`, `SCRATCH <path> <doc>`,
`CITED-RECORDS: <e> empty / <s> scratch`); both carry the source markers the
frozen counter's CHECKER leg greps for; both clear the 10-check floor.

Observable differences, all traced to two design choices:

1. Document set. The seat spec froze `reports/round-<k>/**/*.md`; the
   installed tool also admits `*.txt` under the same round directories. On
   the frozen tree that widens the scratch leg by 7: the round-82 telemetry
   files `controls-d.txt`, `controls-o.txt`, `junk-d.txt`, `junk-o.txt`
   (fixture-tree paths) and `quality30-probe.txt` (a capture path), plus the
   round-83 telemetry files `smoke-d.txt`, `smoke-o.txt` — the last two are
   also why its default-binding run is RED on the frozen tree (it scans the
   frozen counters' own smoke receipts, which cite the L1's materialization
   tree). Those are genuine criterion-31 violations in the frozen telemetry;
   the wider net catches verbatim the two probes the round-82 spot-check §6
   named. At lands the frozen C counter's CHECKER leg materializes only the
   listed blobs plus round-83 `*.md` documents — no `.txt` anywhere — so the
   difference is unobservable to the grader; both implementations print
   `CITED-RECORDS: 0 empty / 0 scratch`, exit 0 there.
2. Rendering details. The installed tool's scratch tail class admits the
   ellipsis character, so it reports e.g. the full ellipsis-masked citation
   where this seat's tool reports the bare shape root (frozen tail class
   `[A-Za-z0-9_./-]*`); its citation regex adds a boundary lookbehind the
   frozen pattern does not state; its round-number parse is looser
   (`round[-_]?(\d+)` anywhere) where this tool keys on exact directory and
   file prefixes. None of these diverge on any committed byte in scope.

Both are consistent with the frozen CHECKER leg; the choice between them —
`.md`-only per the seat contract, or `.md`+`.txt` per the wider hygiene net —
is the L1's. This seat made no write to the lane tool path.

## Reproduce

```
git -C <lane> archive 21277b089e3c64c247bb4e0fcb033abfdfa1e668 | tar -x -C <scratch>
python3 .ufo/waves/round-83/w1/stage/ExecCitedRecords/check-cited-records.py \
    --root <scratch> --from-round 82 --bind-round 82     # 2 empty / 2 scratch, exit 1
python3 .ufo/waves/round-83/w1/stage/ExecCitedRecords/check-cited-records.py \
    --root <scratch>                                     # 0 empty / 0 scratch, exit 0
TMPDIR=<scratch> python3 .ufo/waves/round-83/w1/stage/ExecCitedRecords/check-cited-records.py --selftest
```

No absolute scratch path appears in this receipt; the seat scratch root was
removed at exit, nothing left behind.
