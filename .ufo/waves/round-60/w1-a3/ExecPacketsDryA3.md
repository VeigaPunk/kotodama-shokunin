NONE-MET

# ExecPacketsDryA3 — instrument dry run: support packets + one honest seat (round 60, attempt 3, wave 1)

Scope: the packet builder `reports/round-60/build-packets.py` and the seat leg of `ACCEPT-D-60` at
revision 5 (`14e6413820d482913f723432b62d566967ccd1a6`, counter sha256
`b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`, equal to the declared sha), run in a
sandbox clone with `/fast/scratch/hyaku/kotodama-r60a3/L1/build.patch` applied. No data seat work, no
judgement of any quote, no lane write except this report. No tool installs.

## A. Instrument check (packets built from the candidate entry)

Build: `cd <clone> && python3 -B reports/round-60/build-packets.py planted-rows.copy.md <outdir>`
(seed = byte copy of `/fast/scratch/hyaku/kotodama-r60a3/support/planted-rows.md`, sha256
`1a082ff0bb8abaf87dfb0536f0e7383202ffd719d6b5771943bdd2bc3b518682`, equal to the counter's frozen
`PLANTED_ROWS_SHA256`). Two independent builds (different `os.urandom` shuffle seeds) gave the same invariants.

stdout, build 1: `cited=47 planted_rows=16 seats=24 planted_per_seat_min=2` (exit 0)
stdout, build 2: `cited=47 planted_rows=16 seats=24 planted_per_seat_min=2` (exit 0)

Independent checker (`check-packets.py`, imports `accept-d.py`'s own `PACKET_BLOCK/PACKET_FIELD/URL_TOKEN/
page_of/row_target` and `reopen-quote.page_of`; full output in `check-out.txt`):

```
entry_sha256=0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0
key_entry_sha256=0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0 equal=True
cited_ids=47 planted_rows=16 planted_rows_sha=1a082ff0bb8abaf87dfb0536f0e7383202ffd719d6b5771943bdd2bc3b518682
planted_rows_sha_is_frozen=True
real_ids_in_packets=47 exactly_cited=True
real_ids_not_exactly_3_seats=none
planted_seats=24 min_planted_per_seat=2 seats_below_2=none
planted_block_total=48 expected=48
packets=24 blocks_total=189 entry_sha_lines_bad=none
block_problems=none
fidelity_problems_vs_counter_proposition=none
packet_bytes_per_seat={"SupportA60": 5210, "SupportB60": 5575, "SupportC60": 6180, "SupportD60": 5575, "SupportE60": 5351, "SupportF60": 5351, "SupportG60": 5575, "SupportH60": 5693, "SupportI60": 5210, "SupportJ60": 4952, "SupportK60": 4952, "SupportL60": 4952, "SupportM60": 6180, "SupportN60": 5139, "SupportO60": 5139, "SupportP60": 5139, "SupportQ60": 5210, "SupportR60": 5522, "SupportS60": 5351, "SupportT60": 6180, "SupportU60": 5693, "SupportV60": 5522, "SupportW60": 5693, "SupportX60": 5522}
planted_per_seat={"SupportA60": 2, "SupportB60": 2, "SupportC60": 2, "SupportD60": 2, "SupportE60": 2, "SupportF60": 2, "SupportG60": 2, "SupportH60": 2, "SupportI60": 2, "SupportJ60": 2, "SupportK60": 2, "SupportL60": 2, "SupportM60": 2, "SupportN60": 2, "SupportO60": 2, "SupportP60": 2, "SupportQ60": 2, "SupportR60": 2, "SupportS60": 2, "SupportT60": 2, "SupportU60": 2, "SupportV60": 2, "SupportW60": 2, "SupportX60": 2}
blocks_per_seat={"SupportA60": 8, "SupportB60": 8, "SupportC60": 8, "SupportD60": 8, "SupportE60": 8, "SupportF60": 8, "SupportG60": 8, "SupportH60": 8, "SupportI60": 8, "SupportJ60": 7, "SupportK60": 7, "SupportL60": 7, "SupportM60": 8, "SupportN60": 8, "SupportO60": 8, "SupportP60": 8, "SupportQ60": 8, "SupportR60": 8, "SupportS60": 8, "SupportT60": 8, "SupportU60": 8, "SupportV60": 8, "SupportW60": 8, "SupportX60": 8}
```

Per demanded item:
1. **47 ids x exactly 3 distinct seats** — PASS. `real_ids_not_exactly_3_seats=none`; the 47 ids in the packets
   are exactly the 47 ids the candidate entry cites.
2. **every seat >= 2 PLANTED** — PASS. All 24 seats carry exactly 2 planted blocks (48 = 16x3 slots, 2 full
   cycles of 24); `seats_below_2=none`.
3. **`entry_sha256: <hex>` in every packet** — PASS. 24/24; value equals sha256 of the entry bytes
   (`0073da7e...`), which is also byte-identical to the L1's `candidate-entry.md` (`diff -q` clean).
4. **every block's url field yields >= 1 URL under accept-d.py's URL_TOKEN and page_of matches the row** —
   PASS over all 189 blocks / 300 URL tokens in each build. For real ids, `page_of(urls[0]) ==
   page_of(row_urls[0])` and every other listed URL is on that same page; for planted blocks,
   `page_of(urls[0])` equals the seed row's page and no URL is refused by `url_refusal`. Additionally all
   300 URL tokens per build are recognised by `names_page` against their row's page, so a seat curling any
   listed URL can satisfy the FETCHED gate.
5. **packet sizes** — 4,952–6,180 bytes per seat (table above); 189 blocks total; labels contiguous P01..Pnn
   in every packet.
6. Extra fidelity check: for every real block, the packet's (quote, teaches-without-`supersedes`, entry-with-
   S-ids-removed) equals the counter's own `proposition(sid)` under `normalise` — 0 mismatches in both builds.
   Without this, SUPPORTED verdicts would silently never count.

## B. Honest-shaped fake transcript for one seat, SESSIONS-only probe

Fixture (`build-probe.py`): root = the patched tree + `reports/round-60/captures/` from the L1 build dir +
`.ufo/waves/round-60/support/{planted-rows.md, planted-key.json, packet-SupportA60.md, SupportA60.md,
registry.json, transcripts/KotodamaR60A3.SupportA60.jsonl}` + the two sha files, with a synthetic key whose
`entry_sha256` is the entry's. Transcript: one `session_init` whose `task` is the packet byte-for-byte, 11
`bash` `curl` calls (every URL of every block) with `cwd /tmp/SupportA60`, and one `write` of the report to
`/kotodama-shokunin/.ufo/waves/round-60/w1-a3/SupportA60.md` with verdicts (planted -> NOT-SUPPORTED, real ->
SUPPORTED). Session file is a byte copy of the committed transcript.

Probe diff (the ONLY change in each probe counter):

```
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/ExecPacketsDryA3/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # PROBE: SESSIONS only
```

**Answer: yes.** Under the probe the seat is `SupportA60:Q2` (qualified, 2 planted) with **no `/sees:`**, and
its 6 real blocks count `good=1` each (so the FETCHED + proposition + qualified gates all fire for it). Under
the frozen counter the same fixture is `X2/sees:session-files=0` — a sandbox session file cannot vouch for a
real seat, which is the intended behaviour, and the only difference is the SESSIONS constant.

Full stdout, frozen counter (`b6389454...`), root = probe-root, `python3 -B probe-root/reports/round-60/accept-d.py --root probe-root`, exit 1:

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```

Full stdout, probe counter (`40e331bf6be4745715b004ffedbd0dd13e2e8cd0d092a9d3d02e40755a7d1aeb`), same root, exit 1:

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=1', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=1', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=1', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=1', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=1', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=1', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=['SupportA60'] seats=['SupportA60:Q2']
ACCEPT-D-60: FAIL
```

SUPPORT still FAILs only because 23 of 24 seats are absent (each id needs 2 good seats); that is the expected
shape of a one-seat fixture, not an instrument fault.

## C. Seat-leg gate mutations (same fixture, one input changed each)

- B `no-fetch` (every curl call removed; seat still Q2): all `good=0` — the FETCHED gate is live at id level.
- C `planted-supported` (both planted verdicts flipped): `qualified=[]`, `SupportA60:X2` — the planted gate
  refuses the seat, and its real verdicts stop counting.
- D `report-rewrite` (one verdict appended to the committed report after the write): `X2/sees:report-not-its-
  own-write`, and the appended `S622 NOT-SUPPORTED` is counted as dissent (`S622:NOT/SupportA60`).
- E `roster-24` (registry lists all 24 seats, only SupportA60's files exist): seat stays Q2 under the rev-5
  probe and under the working-tree rev-6 snapshot probe (`0aad90bf...`), no `/sees:`, 23 seats `missing`.

Full stdout, B (`40e331bf...`, exit 1):

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=['SupportA60'] seats=['SupportA60:Q2']
ACCEPT-D-60: FAIL
```

Full stdout, C (`40e331bf...`, exit 1):

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2']
ACCEPT-D-60: FAIL
```

Full stdout, D (`40e331bf...`, exit 1):

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S622:NOT/SupportA60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:report-not-its-own-write']
ACCEPT-D-60: FAIL
```

Full stdout, E under the working-tree rev-6 snapshot probe (`1404786f1ca4a72665f8dfc1c0b4c3e59375ef9ee67aa52b7cda2533b8e5160d`,
SESSIONS-only change on `0aad90bf...`; uncommitted snapshot, see D), exit 1:

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=1', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=1', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=1', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=1', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=1', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=1', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=['SupportA60'] seats=['SupportA60:Q2', 'SupportB60:missing', 'SupportC60:missing', 'SupportD60:missing', 'SupportE60:missing', 'SupportF60:missing', 'SupportG60:missing', 'SupportH60:missing', 'SupportI60:missing', 'SupportJ60:missing', 'SupportK60:missing', 'SupportL60:missing', 'SupportM60:missing', 'SupportN60:missing', 'SupportO60:missing', 'SupportP60:missing', 'SupportQ60:missing', 'SupportR60:missing', 'SupportS60:missing', 'SupportT60:missing', 'SupportU60:missing', 'SupportV60:missing', 'SupportW60:missing', 'SupportX60:missing']
ACCEPT-D-60: FAIL
```

## D. Reference runs on the inherited build (build attack, mechanical legs only)

Base (committed rev-5 entry/SOURCES, no captures, no support dir), frozen counter `b6389454...`, exit 1 —
reproduces the declared `before` exactly:

```
SET FAIL cited=43 want=47 missing=['S648', 'S649', 'S650', 'S651'] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=0 base_line=False', 'S649:lines=0 base_line=False', 'S650:lines=0 base_line=False', 'S651:lines=0 base_line=False']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=0 registry=None', 'S649:rows=0 registry=None', 'S650:rows=0 registry=None', 'S651:rows=0 registry=None']
PINNED FAIL bad=['manifest:FileNotFoundError', 'S648:no-row-or-manifest', 'S649:no-row-or-manifest', 'S650:no-row-or-manifest', 'S651:no-row-or-manifest']
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
```

Candidate build (`build.patch` applied + the L1's `captures/` copied to `reports/round-60/captures/`; no support
dir yet), frozen counter `b6389454...`, exit 1:

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
```

So the inherited build's mechanical legs all pass against the committed captures (SET, LINES, OLDWORD, ROWS,
PINNED), and JUDGED passes as soon as a key naming `0073da7e...` exists (probe-root run above). JUDGED in a
lane run must fail until the L1 commits `planted-key.json` + `planted-key.sha256`, and it will fail again if
any byte of the entry changes after the packet build.

## D2. Re-check at the lane's new HEAD `1cd9db7` (revisions 6-7, now committed)

The lane advanced while this dry run was in flight: `b9faed9` committed revisions 6-7 (counter sha now
`45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59`; adds an EVIDENCE leg: a SUPPORTED verdict
counts only with a straight-quoted >=10-word page span that locates in `reports/round-60/captures/pages/<sid>.txt`
and not in the packet block) and `1cd9db7` committed the claim-D build (entry sha `36bd628b6af6a9e6...`, SOURCES
`641115af...`, captures incl. `pages/`). I re-ran the whole instrument against that HEAD:

- `build-packets.py` is unchanged (`ff69e9bc...`). Rebuilt from the committed entry: `cited=47 planted_rows=16
  seats=24 planted_per_seat_min=2` (exit 0). Checker output in full:

```
entry_sha256=36bd628b6af6a9e62e2cbeb2a51f32032e8f5837705f25f25c9aceaca6f770e2
key_entry_sha256=36bd628b6af6a9e62e2cbeb2a51f32032e8f5837705f25f25c9aceaca6f770e2 equal=True
cited_ids=47 planted_rows=16 planted_rows_sha=1a082ff0bb8abaf87dfb0536f0e7383202ffd719d6b5771943bdd2bc3b518682
planted_rows_sha_is_frozen=True
real_ids_in_packets=47 exactly_cited=True
real_ids_not_exactly_3_seats=none
planted_seats=24 min_planted_per_seat=2 seats_below_2=none
planted_block_total=48 expected=48
packets=24 blocks_total=189 entry_sha_lines_bad=none
block_problems=none
fidelity_problems_vs_counter_proposition=none
packet_bytes_per_seat={"SupportA60": 5567, "SupportB60": 4946, "SupportC60": 6237, "SupportD60": 5098, "SupportE60": 6237, "SupportF60": 5567, "SupportG60": 4946, "SupportH60": 5370, "SupportI60": 5370, "SupportJ60": 5370, "SupportK60": 5575, "SupportL60": 5707, "SupportM60": 5297, "SupportN60": 5575, "SupportO60": 5567, "SupportP60": 5575, "SupportQ60": 5297, "SupportR60": 6237, "SupportS60": 5707, "SupportT60": 5098, "SupportU60": 5297, "SupportV60": 5707, "SupportW60": 4946, "SupportX60": 5098}
planted_per_seat={"SupportA60": 2, "SupportB60": 2, "SupportC60": 2, "SupportD60": 2, "SupportE60": 2, "SupportF60": 2, "SupportG60": 2, "SupportH60": 2, "SupportI60": 2, "SupportJ60": 2, "SupportK60": 2, "SupportL60": 2, "SupportM60": 2, "SupportN60": 2, "SupportO60": 2, "SupportP60": 2, "SupportQ60": 2, "SupportR60": 2, "SupportS60": 2, "SupportT60": 2, "SupportU60": 2, "SupportV60": 2, "SupportW60": 2, "SupportX60": 2}
blocks_per_seat={"SupportA60": 8, "SupportB60": 7, "SupportC60": 8, "SupportD60": 8, "SupportE60": 8, "SupportF60": 8, "SupportG60": 7, "SupportH60": 8, "SupportI60": 8, "SupportJ60": 8, "SupportK60": 8, "SupportL60": 8, "SupportM60": 8, "SupportN60": 8, "SupportO60": 8, "SupportP60": 8, "SupportQ60": 8, "SupportR60": 8, "SupportS60": 8, "SupportT60": 8, "SupportU60": 8, "SupportV60": 8, "SupportW60": 7, "SupportX60": 8}
```
- Honest seat fixture rebuilt for this HEAD (24-member registry, `packets-v7`, evidence spans): probe counter
  `79da84bf17f6a87b699f5a9bdbd5ecf8794163c3d997d58ce3db55676c062216` (SESSIONS only), seat `SupportA60:Q2`,
  no `/sees:`, and the 6 real blocks it was given each count `good=1` — so the rev-7 EVIDENCE gate is
  satisfiable and the seat leg is operable end-to-end at the current HEAD.
- Without the quoted span (plain `VERDICT Pnn SUPPORTED` lines, same fixture) the seat is still `Q2` but every
  `good=0`: the EVIDENCE gate is live. The a3 support prompt in `.ufo/waves/round-60/gen-support-a3.py` already
  demands exactly `VERDICT P01 SUPPORTED — "<one sentence of at least 10 words ... in straight double quotes>"`
  and says a SUPPORTED line without it does not count, so prompt and counter agree.

Full stdout, new-HEAD honest fixture, frozen counter `45ce3ef4...`, `--root probe-root`, exit 1:

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:missing', 'SupportC60:missing', 'SupportD60:missing', 'SupportE60:missing', 'SupportF60:missing', 'SupportG60:missing', 'SupportH60:missing', 'SupportI60:missing', 'SupportJ60:missing', 'SupportK60:missing', 'SupportL60:missing', 'SupportM60:missing', 'SupportN60:missing', 'SupportO60:missing', 'SupportP60:missing', 'SupportQ60:missing', 'SupportR60:missing', 'SupportS60:missing', 'SupportT60:missing', 'SupportU60:missing', 'SupportV60:missing', 'SupportW60:missing', 'SupportX60:missing']
ACCEPT-D-60: FAIL
```

Full stdout, same fixture under the SESSIONS-only probe `79da84bf...`, exit 1:

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=1', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=1', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=1', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=1', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=1', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=1', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=['SupportA60'] seats=['SupportA60:Q2', 'SupportB60:missing', 'SupportC60:missing', 'SupportD60:missing', 'SupportE60:missing', 'SupportF60:missing', 'SupportG60:missing', 'SupportH60:missing', 'SupportI60:missing', 'SupportJ60:missing', 'SupportK60:missing', 'SupportL60:missing', 'SupportM60:missing', 'SupportN60:missing', 'SupportO60:missing', 'SupportP60:missing', 'SupportQ60:missing', 'SupportR60:missing', 'SupportS60:missing', 'SupportT60:missing', 'SupportU60:missing', 'SupportV60:missing', 'SupportW60:missing', 'SupportX60:missing']
ACCEPT-D-60: FAIL
```

(The 6 `good=1` ids here are the blocks that landed on SupportA60 in the `packets-v7` shuffle; their evidence
sentences were machine-picked from the pinned page text for the fixture and are NOT support judgements.)

## E. Receipts

```
RECEIPT ExecPacketsDryA3/base-do-nothing counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,LINES,ROWS,PINNED,JUDGED,SUPPORT
RECEIPT ExecPacketsDryA3/candidate-build-with-captures counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT ExecPacketsDryA3/dry-seat-honest-frozen counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SUPPORT
RECEIPT ExecPacketsDryA3/dry-seat-honest-probe counter-sha256=40e331bf6be4745715b004ffedbd0dd13e2e8cd0d092a9d3d02e40755a7d1aeb rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT
RECEIPT ExecPacketsDryA3/dry-seat-24roster-probe counter-sha256=40e331bf6be4745715b004ffedbd0dd13e2e8cd0d092a9d3d02e40755a7d1aeb rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT
RECEIPT ExecPacketsDryA3/rev6snapshot-24roster-probe counter-sha256=1404786f1ca4a72665f8dfc1c0b4c3e59375ef9ee67aa52b7cda2533b8e5160d rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=n/a exit=1 probe=FAIL stopped-by=SUPPORT
RECEIPT ExecPacketsDryA3/head1cd9db7-dry-seat-frozen counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7 frozen=FAIL exit=1 probe=n/a stopped-by=SUPPORT
RECEIPT ExecPacketsDryA3/head1cd9db7-dry-seat-probe counter-sha256=79da84bf17f6a87b699f5a9bdbd5ecf8794163c3d997d58ce3db55676c062216 rev=1cd9db7 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT
```

(`rev6snapshot-*` is the then-uncommitted working-tree counter `0aad90bf...` snapshotted at 04:12:08 local,
SESSIONS line only changed; it was superseded by committed rev 7 `45ce3ef4...`. The `head1cd9db7-*` receipts
are scored at the lane's current HEAD, counter `45ce3ef4...` + a SESSIONS-only probe; `rev=` there names the
HEAD commit I checked out, and `JUDGED`/`SET`/`LINES`/`OLDWORD`/`ROWS`/`PINNED` all PASS in that run.)

`CONTROL-MET` check: no fixture — including every probe above — reaches `ACCEPT-D-60: PASS`, so this report is
`NONE-MET`. None of my fixtures skips the claimed work (the only omissions are the 23 absent seats and, in B,
the fetches), and none of them is a claim for PASS.

## F. Lane state observed (not mine to change)

The lane moved twice while this dry run was in flight. It is now at HEAD `1cd9db7` ("claim D build ..."): after
`b9faed9` committed revisions 6-7 (`reports/round-60/accept-d.py` sha256
`45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59`, `revision_note_6` and `_7` present; rev 7
adds EVIDENCE) and `1cd9db7` committed the entry (`36bd628b...`) with SOURCES `641115af...` and the captures
(including `captures/pages/`). `freeze_note` is still empty, so the freeze commit has not been named yet.

Consequence for every receipt above that names `rev=14e6413...`: those were scored, as instructed, against the
revision-5 counter `b6389454...` and the then-uncommitted candidate entry `0073da7e...`; they are valid for that
object only. The entry I first tested is **not** the entry now in the lane — 19 base lines were narrowed between
them — so packets must be built from the frozen commit, not from the earlier candidate. Section D2 re-ran the
packet build and the seat leg at `1cd9db7` (`45ce3ef4...`, entry `36bd628b...`) and both hold.

Working tree at report time (read-only `GIT_OPTIONAL_LOCKS=0 git status --porcelain`): `M LOG.md`, `M SCORECARD.md`,
`M corpus/QUALITY.md`, `M corpus/lessons/round-59.md`, plus untracked wave/build files and the new
`corpus/lessons/round-60.md` — records and wave-1 work by other seats, not mine. I made no lane change except
this report.

## G. Files changed, artifacts

Lane: only `.ufo/waves/round-60/w1-a3/ExecPacketsDryA3.md` (this report). No lane edits, no git/jj writes, no
processes left running.

Sandbox `/fast/scratch/hyaku/kotodama-r60a3/ExecPacketsDryA3/`:
`clone/` (sandbox clone, now at `1cd9db7`), `packets/`, `packets2/` (rev-5-entry packet builds + keys),
`packets-v7/` (packet build from the committed entry `36bd628b`), `probe-root/` (one-seat fixture at `1cd9db7`),
`sessions/2026/1023/KotodamaR60A3/KotodamaR60A3.SupportA60.jsonl`, `check-packets.py`, `check-out.txt`,
`build-probe.py`, `mutate-seat.py`, `frozen-counter.py` (sha `b6389454...`), `probe-counter.py` (sha `40e331bf...`),
`rev6-snapshot.py` (sha `0aad90bf...`), `probe-root/reports/round-60/accept-d.py` (sha `45ce3ef4...`),
`probe-root/reports/round-60/accept-d-probe.py` (sha `79da84bf...`), `planted-rows.copy.md`, `run-base.txt`,
`run-candidate.txt`, `run-frozen.txt`, `run-probe.txt`, `run-probe-rev6.txt`, `run-v7-{frozen,probe}.txt`,
`run-mut-{A-honest,B-nofetch,C-planted-supported,D-report-rewrite,E-roster24}.txt`. Mutation roots and
`base-root` were deleted after their stdout was captured.

## H. Risks

1. **Build packets from the frozen commit only**: the entry changed between rev 5's candidate (`0073da7e...`) and
   the committed build (`36bd628b...`), and packets embed `entry_sha256`. Any packet build made before
   `freeze_note` is named is dead if the entry moves again.
2. **Randomised builder**: `build-packets.py` shuffles with `os.urandom`, so packets and the key are not
   reproducible. Build once from the frozen entry, commit `planted-rows.sha256`/`planted-key.sha256`, and never
   rebuild after the support call. A byte change to the entry afterwards breaks JUDGED by design.
3. **min-2 planted is emergent, not enforced**: it holds because the frozen seed has exactly 16 planted rows
   (16x3 slots = 2 cycles of 24). Any regeneration of `planted-rows.md` also breaks the frozen
   `PLANTED_ROWS_SHA256` check, so the frozen file must stay.
4. **Exactly 3 seats per id = no slack in the id-level minimum**: `MIN_SEATS_PER_ID=2`, so one dead/voided
   seat of the three is tolerated, two are not. Seat loss is the main failure mode for the support wave.
5. **Registry shape (rev 6+)**: the support dir's `registry.json` must list exactly the 24 frozen seats, once
   each, `role: reviewer`, `agentId: KotodamaR60A3.<Name>`; otherwise SUPPORT fails with `roster` even if every
   verdict is clean.
6. **EVIDENCE line format (rev 7)**: a SUPPORTED verdict counts only with a straight-quoted >=10-word span that
   locates in `captures/pages/<sid>.txt` and is not the packet quote. The a3 support prompt
   (`gen-support-a3.py`) already requires that line; a seat that paraphrases, uses curly quotes, or omits the
   span silently loses its SUPPORTED verdicts (my plain-verdict fixture: `Q2`, `good=0`). The gate does not
   distinguish body text from page chrome — a header/navigation sentence of >=10 words satisfies it (my fixture's
   machine-picked spans were mostly chrome), so this leg guards "did not read the page", not "quoted the right
   sentence".
7. **Captures must be committed with the entry**: they now are at `1cd9db7` (`manifest.json` + `pages/`); a lane
   run without them fails PINNED `manifest:FileNotFoundError`.
8. **Packet text is a task payload**: each packet is 4.9–6.2 KB and must be embedded byte-for-byte in the
   seat's `session_init` task (`bound`), along with `entry_sha256: 36bd628b...`.
9. No claims about quote/page content or support verdicts are made here; the 47 ids remain unjudged. The
   evidence sentences in my fixture were machine-picked to satisfy the EVIDENCE leg, not to support anything.

Blockers: none for this dry run.
