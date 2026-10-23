# CtlCUrlReuse — pre-data URL controls for claim C (ACCEPT-C-63)

Seat: control (Ctl*), leaf. Round 63, hyaku run 5, 2026-10-23 UTC.
Lane repo (read-only for this seat): /home/vgpnk/Projects/shokunin/kotodama-shokunin
rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95, round base 65b393ef3a4d82bd693cc21b7f96a1231417d522.
Sandbox clone: /fast/scratch/hyaku/kotodama-r63/CtlCUrlReuse/clone
(fixture builder /fast/scratch/hyaku/kotodama-r63/CtlCUrlReuse/build.py; raw logs run_*.txt).
Counter run: reports/round-63/accept-c.py, sha256
`3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca`
(equals the claim's declared hash; hashed before the first run and again after the last, unchanged).
The counter was **never edited**; no PROBE copy was needed. Every fixture is a sandbox-clone commit
on local branch `main`; the lane and the fleet repo were not written.

## Method

The claimed object (new entry + rows S694–S717) is being authored concurrently by the scribes, so
the pristine object does not exist at the freeze. I built a claim-C-shaped baseline fixture in the
sandbox clone — the new entry file (1 h1, 3 h2, 39 lines, `- topic:`), the 24 rows S694–S717
appended after S693, and the README index/count/footer moved 236→237, culture-material 30→31 —
and confirmed the frozen counter reads **ACCEPT-C-63: PASS, exit 0** on it. Each control case then
changes exactly one URL property in row S695 (or S695+S696) and re-runs the identical counter.

For the six LIVE ids (S694 S698 S702 S706 S710 S714) the fixture rows use real pages whose quotes
were verified with the frozen base locator `reports/round-61/reopen-quote.py` before any fixture run
(all six LOCATED: Mitre, Biretta, Coif, Shako, Pileus (hat), Tudor bonnet — Wikipedia). The other
18 rows use synthetic `https://example.org/headgear/s69N` URLs, which no leg fetches. This is a
counter control, not claim-C substance; the fixture must not be read as proposed registry data.

Command per case: `cd clone && timeout 900 python3 -B reports/round-63/accept-c.py --root .`

## Full stdout and exit codes

### baseline (no defect; head b14e658fbe2238f3f83476fae9af317aeac97bed)

```
FILE PASS exists lines=39 h1=1 h2=3 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: PASS
exit=0
```

### v1_reuse — S695 live URL is S693's registry URL verbatim (head a296e1dcc2dc75e5bd7a74bad94d336a20d05ab4)

Defect: `... - https://www.dictionary.com/browse/talaria ; capture .../id_/https://www.dictionary.com/browse/talaria`

```
FILE PASS exists lines=39 h1=1 h2=3 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK FAIL bad=['S695:registry_hits=2']
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: FAIL
exit=1
```

### v2_query — S695 live URL is S693's URL + `?ref=headgear` (head a25c1443401f2909e83d618a8a66e4de44b8d837)

Defect: `... - https://www.dictionary.com/browse/talaria?ref=headgear ; capture .../id_/https://www.dictionary.com/browse/talaria?ref=headgear`

```
FILE PASS exists lines=39 h1=1 h2=3 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: PASS
exit=0
```

### v2b_fragment — S695 live URL is S693's URL + `#sense-2` (head 1b977006cf1b1c432f4634c770f123d57805df8e)

Defect: `... - https://www.dictionary.com/browse/talaria#sense-2 ; capture .../id_/https://www.dictionary.com/browse/talaria#sense-2`

```
FILE PASS exists lines=39 h1=1 h2=3 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: PASS
exit=0
```

### v3_capture_other — S695 capture embeds a DIFFERENT original URL (head eed6bdbf867f49d9b20896dc677369a1ae4d19d3)

Defect: live `https://example.org/headgear/s695`; capture `https://web.archive.org/web/20261023000000id_/https://other.example.org/not-the-page`

```
FILE PASS exists lines=39 h1=1 h2=3 h3=0 topic=True
ROWS FAIL bad=['S695:capture_original_mismatch'] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: FAIL
exit=1
```

### v3b_capture_semicolon — same, but a `;` truncates the compared original (head c94db189a87db9278f28451b96f57a0dbb4d83cd)

Defect: capture `https://web.archive.org/web/20261023000000id_/https://example.org/headgear/s695;https://other.example.org/not-the-page`
(`CAPTURE_RE`'s lazy `(.+?)\s*(?:;|\||$)` stops at the `;`, so the compared original equals the live URL while the listed capture carries a second URL.)

```
FILE PASS exists lines=39 h1=1 h2=3 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: PASS
exit=0
```

### v4_share — S695 and S696 share one literal URL (head 3f63e13791e8c6d0c0d2b32712592e9ec87e4dfa)

Defect: both rows `... - https://shared.example.org/headgear-page ; capture ...`

```
FILE PASS exists lines=39 h1=1 h2=3 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK FAIL bad=['S695:registry_hits=2', 'S696:registry_hits=2']
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: FAIL
exit=1
```

### v4b_share_scheme — S695/S696 share one page across an https/http scheme swap (head b9fd0db3c16a583209ecb07b39fc4ddb1774e990)

Defect: S695 `https://shared.example.org/headgear-page`, S696 `http://shared.example.org/headgear-page`

```
FILE PASS exists lines=39 h1=1 h2=3 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: PASS
exit=0
```

### v5_fake_capture — S695 capture id is `1` (no existence check) (head ac17dd5c9f02ee2e7e8a3c647f918b0812e0e2d5)

Defect: capture `https://web.archive.org/web/1id_/https://example.org/headgear/s695`

```
FILE PASS exists lines=39 h1=1 h2=3 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: PASS
exit=0
```

### restored freeze — clone reset to 80d53ff, clean tree, counter re-run

```
FILE FAIL unreadable: [Errno 2] No such file or directory: '/fast/scratch/hyaku/kotodama-r63/CtlCUrlReuse/clone/corpus/knowledge/culture-material/headgear-head-covering-codes.md'
ROWS FAIL bad=['S694:rows=0', 'S695:rows=0', 'S696:rows=0', 'S697:rows=0', 'S698:rows=0', 'S699:rows=0', 'S700:rows=0', 'S701:rows=0'] checked=24
ONEID FAIL bad=[] cited_lines=0 cited_lines_tool=exit2 clean=False
RESTATE PASS bad=[] lines=0
LINK PASS bad=[]
APPEND FAIL missing_base_lines=0 base=619 measured=619 +24=False
NOHARM FAIL diff=[]
SWEEP FAIL exit=0 topic_row=False
LIVE FAIL subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=['S694:no_row', 'S698:no_row', 'S702:no_row', 'S706:no_row', 'S710:no_row', 'S714:no_row']
ACCEPT-C-63: FAIL
exit=1
```

(`frozen=PASS` in the receipts below means the baseline claim-C-shaped fixture passes the frozen
counter, i.e. the case's deviation is the only variable; `frozen=FAIL` on the restored-freeze case
is the declared pre-data state where the claimed object does not exist yet.)

## Receipts

```
RECEIPT CtlCUrlReuse/baseline counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlCUrlReuse/v1_reuse counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=1 stopped-by=LINK
RECEIPT CtlCUrlReuse/v2_query counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlCUrlReuse/v2b_fragment counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlCUrlReuse/v3_capture_other counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=1 stopped-by=ROWS
RECEIPT CtlCUrlReuse/v3b_capture_semicolon counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlCUrlReuse/v4_share counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=1 stopped-by=LINK
RECEIPT CtlCUrlReuse/v4b_share_scheme counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlCUrlReuse/v5_fake_capture counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlCUrlReuse/restored_freeze counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=FILE,ROWS,ONEID,APPEND,NOHARM,SWEEP,LIVE
```

## Verdicts on the four requested controls

1. **New row reusing an existing registry URL (S693 dictionary.com) — NONE-MET.**
   LINK stops it: `S695:registry_hits=2`, exit 1. The check is literal string containment over
   every `| S### |` line; the base row plus the new row make 2 hits. (Caveat under item 2: the
   stop is exact-string only.)
2. **New row whose live URL differs only in query/fragment from an existing one — CONTROL-MET.**
   Both `v2_query` (`?ref=headgear`) and `v2b_fragment` (`#sense-2`) get a full
   `ACCEPT-C-63: PASS`, exit 0. LINK counts occurrences of the *new* URL string only; it never
   compares a new URL to the base rows' URLs. A base URL carrying a query/fragment variant is
   exactly the registry reuse the claim forbids, and it passes.
   *Smallest counter change that stops it:* add a normalised base-URL set and one membership check:
   `norm(u) = re.sub(r"^https?://(www\.)?", "", u.lower()).split("#")[0].split("?")[0].rstrip("/")`,
   `base_norm = {norm(u) for line in base_lines for u in URL_RE.findall(line)}`; in LINK,
   `if norm(url) in base_norm: link_bad.append(f"{sid}:url_reused_from_base")`.
3. **New row whose capture embeds a DIFFERENT original URL (same-page check bypass) — CONTROL-MET
   (via the separator).** The literal swap is stopped by ROWS (`S695:capture_original_mismatch`,
   exit 1), but `v3b_capture_semicolon` passes the full counter: `CAPTURE_RE`'s lazy
   `(.+?)\s*(?:;|\||$)` truncates the compared original at the first `;`, so
   `...id_/<live URL>;<other URL>` compares equal while the listed capture carries a second URL
   that no leg examines. LINK never looks at capture URLs at all. `v5_fake_capture`
   (`web/1id_/<live URL>`) also passes: the timestamp pattern `(\d+|[a-z]+)` accepts any digits,
   so capture existence/plausibility is unchecked for all 24 rows.
   *Smallest counter change that stops it:* anchor the capture to the cell end and forbid a second
   URL in the compared original — `CAPTURE_RE = re.compile(r"web\.archive\.org/web/(\d{14})id_/([^\s;|]+)\s*$", re.I)`
   — then compare `group(2)` to the live URL exactly. Existence still needs a fetch (only the 6
   LIVE rows are ever opened, and only when the live URL fails).
4. **Two new rows sharing one URL — NONE-MET for a literal share; CONTROL-MET for a variant share.**
   `v4_share` fails LINK for both rows (`registry_hits=2`), but `v4b_share_scheme`
   (`https://` vs `http://` on the same host/path) passes the full counter because neither string
   is a substring of the other, so each new URL scores `hits=1`. The same hole exists for `www.`
   prefixes, explicit default ports and percent-encoded paths.
   *Smallest counter change that stops it:* the same `norm()` as item 2, applied within NEW_IDS —
   count distinct normalised live URLs and fail a duplicate (`len({norm(u) for u in live_urls.values()}) != len(live_urls)`),
   and/or require `hits == 1` over normalised forms of all row URLs.

## Cross-cutting coverage note for the L1/closure

LINK is a per-new-URL, line-substring occurrence count. It therefore (a) cannot see URL identity
across normalisation (scheme, `www.`, default port, query, fragment, encoding), (b) ignores capture
URLs and any second URL in the source cell, and (c) cannot see a base row's URL being reused when
the new spelling is not a superstring of the base spelling. ROWS' capture check is exact-string
after `rstrip(".;,')")` and truncation at `;`/`|`, and it never verifies that a capture exists.
None of this was exercised by the frozen counter on the baseline: the baseline passed every leg.

## Restoration evidence

- Fixture clones: `/fast/scratch/hyaku/kotodama-r63/CtlCUrlReuse/clone`, sandbox git only.
- After the last fixture run the clone was reset: `git checkout -q -B main 80d53ffe…` + `git clean -fdq`
  → `HEAD=80d53ffde7788299b69dbb0bd0436b2b7ddddb95`, `git status --porcelain | wc -l` = 0.
- Counter hash before first run and after last run:
  `3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca` (unchanged; no edits).
- The lane repo and the fleet repo received no writes from this seat except this report file.
- Fixture commits (sandbox only): baseline b14e658, v1 a296e1d, v2 a25c144, v2b 1b97700, v3 eed6bdb,
  v3b c94db18, v4 3f63e13, v4b b9fd0db, v5 ac17dd5. Raw full logs: `run_<case>.txt` beside the builder.
- No tools installed this run (nothing needed; no pacman used).
