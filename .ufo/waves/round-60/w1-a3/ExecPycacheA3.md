HOLDS

CONTROL-MET: NONE-MET — this seat scored no fixture that skips the claimed work; routed defect 4 is an operability audit of bytecode pollution, not a control fixture, so no PASS was manufactured or observed.

# ExecPycacheA3 — routed defect 4: `__pycache__` / `*.pyc` audit (round 60, attempt 3, wave 1)

Seat: KotodamaR60A3.ExecPycacheA3 (executor, leaf). Audited 2026-10-23, ~06:58Z–07:08Z. Python 3.14.8. No installs or updates. No LSP call was needed (no symbol operation); grep/read/stat only.

Clone: `/fast/scratch/hyaku/kotodama-r60a3/ExecPycacheA3/clone` at `14e6413820d482913f723432b62d566967ccd1a6`; counter `reports/round-60/accept-d.py` sha256 `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc` (matches the declaration). Every process capped with `timeout`; `python3 -B` throughout; no git/jj write; no lane file created, edited or deleted except this report.

## 1. Inventory

### Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (find run at audit start, read-only)

Exactly one cache, one file:

```
/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-60/__pycache__
/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-60/__pycache__/reopen-quote.cpython-314.pyc
```

| item | value |
|---|---|
| size | 16456 bytes |
| mtime | `2026-10-23 02:38:52.041763542 -0300` = **2026-10-23T05:38:52.0418Z** |
| birth | same instant (created, not copied) |
| header (first 16 bytes) | `2b 0e 0d 0a 00 00 00 00 4b e8 da 6a 19 25 00 00` |
| header fields | magic CPython 3.14, flags 0x0 (timestamp invalidation), source mtime 1792731211 = 2026-10-23T04:53:31Z, source size 9497 |
| tracked? | no — `git -C clone ls-files 'reports/round-60/__pycache__*'` prints nothing at rev 5; `.gitignore:4:__pycache__/` matches (`git check-ignore -v` exit 0) |

**Likely writer (mechanism proven, single script not unique).** The filename is the bytecode-cache name for `reports/round-60/reopen-quote.py`; the header's source stamp equals that file's lane mtime (`2026-10-23 01:53:31 -0300` = 04:53:31Z) and its 9497-byte size exactly. It is written by any CPython 3.14 process that `exec_module`s that locator without `-B`/`PYTHONDONTWRITEBYTECODE`. Lane instruments that do exactly this:

- `reports/round-60/accept-d.py:129-132` (`load_locator`, `--root`-based)
- `reports/round-60/build-packets.py:35-37`
- `reports/round-60/make-planted.py:48-50`

Path-length model (measured, not assumed): a pyc from this source is `16376 + len(absolute source path)` bytes under this interpreter. Control measurements: an 85-char path produced 16461; an 87-char path produced 16463. The lane file is 16456 ⇒ source path length 80 = `len("/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-60/reopen-quote.py")` = 80 exactly. So the compile target was the lane locator **by absolute path**; an out-of-lane script loading it by absolute path would land its cache in the lane just the same. Timing (05:38:52Z) is 99 s after the last capture fetch in `captures/manifest.json` (05:37:13Z) and 26 s before `build-packets.py`'s current mtime (05:39:18Z), inside attempt 2's window (attempt 1 died 05:25:25Z; attempt 2 died 06:19:06Z). The counter run that scores a revision is the likeliest single writer; `build-packets.py`/`make-planted.py` fit the same window and the artifact cannot separate them.

Removal: another seat removed this directory at **07:04:21Z** during my audit; lane telemetry `reports/round-60/telemetry/pycache-removed-a3.txt` records the same file (16456 bytes, 02:38:52 -0300) and "removed ... at 2026-10-23T07:04:21Z". I deleted nothing. Re-list at 07:07:01Z: lane count 0.

### Scratch `/fast/scratch/hyaku/kotodama-r60a3` (as of 07:07:01Z)

One cache, one file:

```
/fast/scratch/hyaku/kotodama-r60a3/AuditA3R16/__pycache__/reopen-quote.cpython-314.pyc
```

| item | value |
|---|---|
| size | 16437 bytes |
| mtime | `2026-10-23 04:06:33.030364152 -0300` = **2026-10-23T07:06:33Z** |
| header | `2b 0e 0d 0a 00 00 00 00 6a 07 db 6a 19 25 00 00` (source size 9497) |
| writer | an unguarded import of that seat's **local** copy `AuditA3R16/reopen-quote.py` (byte-identical to the lane locator, sha256 `64e78c74…`); path length 61 + 16376 = 16437 matches, and no importer `.py` exists in that directory, so the load was an ephemeral `python3 -c`/heredoc without `-B` |

Outside the lane, so no lane effect; same unguarded-import pattern.

## 2. Demonstration — the documented counter run writes no cache

Clone cleaned of any cache first. **Before:** `count_before=0`.

```
$ PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B clone/reports/round-60/accept-d.py --root clone
SET FAIL cited=43 want=47 missing=['S648', 'S649', 'S650', 'S651'] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=0 base_line=False', 'S649:lines=0 base_line=False', 'S650:lines=0 base_line=False', 'S651:lines=0 base_line=False']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=0 registry=None', 'S649:rows=0 registry=None', 'S650:rows=0 registry=None', 'S651:rows=0 registry=None']
PINNED FAIL bad=['manifest:FileNotFoundError', 'S648:no-row-or-manifest', 'S649:no-row-or-manifest', 'S650:no-row-or-manifest', 'S651:no-row-or-manifest']
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```

**After:** `count_after=0`. No `__pycache__`, no `*.pyc` anywhere in the clone.

Guard matrix (each run from a clean clone; stdout files byte-identical, sha256 `695a731ac01d0a32a3932a32676e644db29b7fd1317e8b127ce60e6f586185ad` for all four, so the guard changes nothing in the verdict):

| variant | command | exit | pyc after |
|---|---|---|---|
| V1 documented | `PYTHONDONTWRITEBYTECODE=1 python3 -B … --root clone` | 1 | 0 |
| V2 `-B` only | `python3 -B … --root clone` | 1 | 0 |
| V3 env only | `PYTHONDONTWRITEBYTECODE=1 python3 … --root clone` | 1 | 0 |
| V0 unguarded control | `python3 … --root clone` | 1 | 1 (`clone/reports/round-60/__pycache__/reopen-quote.cpython-314.pyc`, 16463 bytes, source stamp = clone locator mtime) |

V0 reproduces the lane artifact's name, magic, flags and 9497-byte source stamp; it was removed again in my sandbox after the measurement.

RECEIPT ExecPycacheA3/pycache-documented-run counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,LINES,ROWS,PINNED,JUDGED,SUPPORT

(No probe was run: this defect is not a control fixture and no leg after PROVENANCE needed exercising. OLDWORD was the only PASS leg. Frozen FAIL is the expected claim-base result at rev 5, not a defect of the counter.)

## 3. Verdict on the check

`HOLDS`: with `PYTHONDONTWRITEBYTECODE=1 python3 -B`, the counter at rev 5 leaves the clone with zero `__pycache__`/`*.pyc` (0 → 0), and either guard alone suffices. The unguarded form demonstrably writes the exact artifact found in the lane, which is thus attributable to an unguarded run of a lane importer (absolute lane locator path, source stamp 04:53:31Z / 9497 bytes), not to the documented invocation.

## 4. Risks / residual notes

1. Recurrence is one keystroke away: any run of `accept-d.py`, `build-packets.py`, `make-planted.py` — or any sandbox script that loads `reports/round-60/reopen-quote.py` by absolute path — without a guard recreates `reports/round-60/__pycache__` **inside the lane**. It is gitignored and untracked, so it cannot enter the judged object (entry/SOURCES/captures untouched by it), but a "clean tree" claim or a transcript-vs-tree byte comparison can misfire while it exists.
2. Stale-bytecode hazard: a timestamp-invalidated cache is reused only when source mtime **and** size both match. Not observed here (the locator's lane mtime is 04:53:31Z, 9497 bytes; every other copy differs in mtime), and the lane cache no longer exists.
3. The `AuditA3R16` cache is outside the lane and needs no action from me; noted so the L1 can sweep scratch if it wants a uniform receipt.
4. The lane already carries a removal receipt (`reports/round-60/telemetry/pycache-removed-a3.txt`, 07:04:21Z); my audit adds provenance (writer class, exact source stamp/path) and the guard matrix, and made no lane change.

Blockers: none.
