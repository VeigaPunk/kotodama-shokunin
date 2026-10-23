# CtlCLineScam — claim C entry-line pre-data controls (round 63, wave 1)

Seat: `kotodama-r63-w1-CtlCLineScam` (mutation-tester / control). Leaf; no subagents, no installs.

Counter under test (unmodified, byte-identical to the freeze):
`reports/round-63/accept-c.py` sha256 `3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca`
at rev `80d53ffde7788299b69dbb0bd0436b2b7ddddb95` (clone HEAD `68c92c4` = freeze + labelled PROBE
fixture commit; `git diff --name-only 65b393e HEAD -- corpus/knowledge` =
`corpus/knowledge/culture-material/headgear-head-covering-codes.md` only).

No counter edit was made. Only the claimed object (entry, registry rows, README index) was
fabricated inside the scratch clone `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-CtlCLineScam/clone`.

## Probe fixture (clearly labelled; not a claim-C data submission)

The point of the fixture is that it carries no headgear substance at all, yet every offline leg and
the live leg pass:

- Registry: 24 rows S694-S717 appended to `corpus/SOURCES.md` (619 -> 643), tier `B`, status
  `mined`, opened `2026-10-23`, recheck `180d`, used-by the new entry. Each source cell is
  `Probe fixture page S###, Example Domain, n.d. — https://example.com/#s### ; capture https://web.archive.org/web/20200101000000id_/https://example.com/#s###`
  (fragment variants keep each URL unique, so LINK sees one hit each). S695's anchor quote is the
  full 25-word contiguous span of the example.com body; the other rows carry the 11-word span
  `This domain is for use in documentation examples without needing permission`.
- Entry `corpus/knowledge/culture-material/headgear-head-covering-codes.md` with the file-leg head
  block (`- topic: headgear as rank, ritual and identity code (probe fixture for entry-line controls)`,
  one H1, one H2) and exactly one variable probe line.
- README index: `## culture-material/ (30)` -> `(31)`, one index row carrying the exact topic text,
  `Total knowledge entries: 236` -> `237`, footer `(total 236 files; directory totals
  29/29/30/29/24/95)` -> `(total 237 files; directory totals 29/29/31/29/24/95)`.
- The clone's local `main` was moved to the probe commit so the NOHARM leg
  (`git diff <base> main -- corpus/knowledge`) sees the entry. This is a fixture construction, not a
  counter edit.

## RECEIPT lines

```
RECEIPT kotodama-r63-w1-CtlCLineScam/c1_gold counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none
RECEIPT kotodama-r63-w1-CtlCLineScam/c2_multiid counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=ONEID
RECEIPT kotodama-r63-w1-CtlCLineScam/c3_idonly counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=RESTATE
RECEIPT kotodama-r63-w1-CtlCLineScam/c4_quotedump counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=RESTATE
RECEIPT kotodama-r63-w1-CtlCLineScam/c5_content4 counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=RESTATE
RECEIPT kotodama-r63-w1-CtlCLineScam/c6_inorder2 counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=RESTATE
RECEIPT kotodama-r63-w1-CtlCLineScam/c7_copy13 counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=RESTATE
RECEIPT kotodama-r63-w1-CtlCLineScam/c8_defect counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none
RECEIPT kotodama-r63-w1-CtlCLineScam/c9_tablerow counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=ONEID,RESTATE
RECEIPT kotodama-r63-w1-CtlCLineScam/c10_defect_after counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=RESTATE
RECEIPT kotodama-r63-w1-CtlCLineScam/c11_copy12 counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none
RECEIPT kotodama-r63-w1-CtlCLineScam/c12_quote11 counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none
RECEIPT kotodama-r63-w1-CtlCLineScam/c13_floor counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none
```

## Case lines and full stdout (verbatim, every run)

Each run rewrote only the one probe line under `## 1. Probe lines`; everything else was fixed.

### c1_gold — `- domain documentation examples without needing (S694)` (5 content words, 5 in order, longest copy run 4)

```
FILE PASS exists lines=11 h1=1 h2=1 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=1 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=1
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: PASS
exit=0
```

### c2_multiid — `- domain documentation examples without needing (S694) (S695)`

```
FILE PASS exists lines=11 h1=1 h2=1 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID FAIL bad=["line10:ids=['S694', 'S695']"] cited_lines=0 cited_lines_tool=exit1 clean=False
RESTATE PASS bad=[] lines=0
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: FAIL
exit=1
```

### c3_idonly — `- (S694)` (id-only bullet)

```
FILE PASS exists lines=11 h1=1 h2=1 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=1 cited_lines_tool=exit0 clean=True
RESTATE FAIL bad=['line10:S694:content=0'] lines=1
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: FAIL
exit=1
```

### c4_quotedump — the verbatim 25-word quote as the clause, `(S695)`

Clause: `This domain is for use in documentation examples without needing permission This is not a service; avoid relying on it for testing and monitoring purposes`

```
FILE PASS exists lines=11 h1=1 h2=1 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=1 cited_lines_tool=exit0 clean=True
RESTATE FAIL bad=['line10:S695:copy_run=25'] lines=1
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: FAIL
exit=1
```

### c5_content4 — `- domain documentation examples without (S694)`

```
FILE PASS exists lines=11 h1=1 h2=1 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=1 cited_lines_tool=exit0 clean=True
RESTATE FAIL bad=['line10:S694:content=4'] lines=1
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: FAIL
exit=1
```

### c6_inorder2 — `- documentation zebra domain examples yonder stone (S694)`

```
FILE PASS exists lines=11 h1=1 h2=1 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=1 cited_lines_tool=exit0 clean=True
RESTATE FAIL bad=['line10:S694:in_order=2'] lines=1
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: FAIL
exit=1
```

### c7_copy13 — 13-or-more consecutive copied words, `- domain is for use in documentation examples without needing permission this is not a service (S695)` (measured copy run 15)

```
FILE PASS exists lines=11 h1=1 h2=1 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=1 cited_lines_tool=exit0 clean=True
RESTATE FAIL bad=['line10:S695:copy_run=15'] lines=1
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: FAIL
exit=1
```

### c8_defect — unresolved defect mark before the terminal id: `- domain documentation examples without needing permission (to-verify) (S694)`

```
FILE PASS exists lines=11 h1=1 h2=1 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=1 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=1
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: PASS
exit=0
```

### c9_tablerow — a table row carrying S-ids: `| probe note | S694 |`

```
FILE PASS exists lines=11 h1=1 h2=1 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID FAIL bad=[] cited_lines=1 cited_lines_tool=exit1 clean=False
RESTATE FAIL bad=['line10:shape'] lines=1
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: FAIL
exit=1
```

### c10_defect_after — `- domain documentation examples without needing permission (S694) (to-verify)` (mark after the id)

```
FILE PASS exists lines=11 h1=1 h2=1 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=1 cited_lines_tool=exit0 clean=True
RESTATE FAIL bad=['line10:shape'] lines=1
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: FAIL
exit=1
```

### c11_copy12 — 12-word verbatim run plus one non-quote filler: `- domain is for use in documentation examples without needing permission this zebra (S695)`

```
FILE PASS exists lines=11 h1=1 h2=1 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=1 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=1
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: PASS
exit=0
```

### c12_quote11 — the entire 11-word anchor quote pasted as the clause: `- This domain is for use in documentation examples without needing permission (S694)`

```
FILE PASS exists lines=11 h1=1 h2=1 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=1 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=1
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: PASS
exit=0
```

### c13_floor — cheapest compliant clause found: `- domain documentation examples alpha beta (S694)` (5 content words, only 3 in quote order, longest copy run 2)

```
FILE PASS exists lines=11 h1=1 h2=1 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=1 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=1
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: PASS
exit=0
```

## Shape -> stopping leg (measured)

| probe line shape | stopping leg | measured detail |
|---|---|---|
| two ids on one cited line | ONEID | `ids=['S694','S695']`, check-cited-lines MULTI-ID (exit1) |
| id-only bullet `- (S###)` | RESTATE | `content=0` (ONEID passes: one id, no lint finding) |
| whole 25-word quote as clause | RESTATE | `copy_run=25` |
| 4 content words | RESTATE | `content=4` |
| 2 content words in quote order | RESTATE | `in_order=2` |
| 13+ consecutive copied words | RESTATE | `copy_run=15` (line as written) |
| defect mark `(to-verify)` BEFORE the terminal id | none | ONEID PASS, RESTATE PASS, **whole counter PASS exit 0** |
| defect mark AFTER the terminal id | RESTATE | `shape` (regex requires the line to end in ` (S###)`) |
| table row carrying an S-id | ONEID (+RESTATE) | check-cited-lines TABLE-ID (exit1); RESTATE `shape` |

Boundary measurements:
- copied run of exactly 12 words plus one filler passes RESTATE (c11, whole counter PASS);
- the entire 11-word anchor quote pasted as the clause passes RESTATE (c12, whole counter PASS);
  the `copy_run > 12` rule only stops quotes longer than 12 words, and the row quote floor is 8;
- cheapest passing clause: 5 content words, 3 of them in the quote in order, longest copy run 2 (c13).

## Verdicts

```
VERDICT multi-id lines: NONE-MET (c2 stopped by ONEID, check-cited-lines MULTI-ID; no cheaper shape reaches PASS)
VERDICT id-only bullets: NONE-MET (c3 stopped by RESTATE content=0)
VERDICT 25-word quote-dump lines: NONE-MET (c4 stopped by RESTATE copy_run=25)
VERDICT 4-content-word clauses: NONE-MET (c5 stopped by RESTATE content=4)
VERDICT 2-in-order-word clauses: NONE-MET (c6 stopped by RESTATE in_order=2)
VERDICT 13+ consecutive copied words: NONE-MET (c7 stopped by RESTATE copy_run=15)
VERDICT defect-mark lines: CONTROL-MET — fixture c8 `- domain documentation examples without needing permission (to-verify) (S694)` gets ACCEPT-C-63: PASS, exit 0; the mark sits inside group(1) of the RESTATE shape regex and neither leg reads it. Smallest counter change: in tools/check-cited-lines.py add one defect-marker finding (or in RESTATE reject a clause matching `\((?:to-verify|unverified|todo|fixme|tbd|draft)\b`), e.g. `DEFECT = re.compile(r"\((?:to-verify|unverified|todo|fixme|tbd|draft)\b", re.I)` and append a finding when it matches.
VERDICT table rows carrying S-ids: NONE-MET (c9 stopped by ONEID TABLE-ID and RESTATE shape)
VERDICT whole-quote dump at or below 12 words: CONTROL-MET — fixture c12 pastes the entire 11-word anchor quote as the clause and gets PASS, exit 0 (c11 shows the same at exactly 12 copied words plus one filler). Smallest counter change: reject a clause whose longest copied run is >= 8 (the quote-word floor), or reject when the clause's content-word sequence is a contiguous sub-span of the quote, i.e. lower the `best > 12` threshold to `best >= MIN_QUOTE_WORDS`.
VERDICT cheapest passing line: c13 `domain documentation examples alpha beta (S694)` — 5 content words, 3 in order, copy run 2; PASS exit 0. The machine floor of RESTATE is that weak by construction; no cheaper line exists that satisfies content>=5 and in_order>=3.
VERDICT cheap whole-counter fixture: CONTROL-MET — the entire frozen counter (all nine legs, ACCEPT-C-63: PASS, exit 0) is satisfied by 24 registry rows pointing at `https://example.com/#sNNN` whose anchor quotes are example.com boilerplate and whose entry line is example.com words; no headgear page, capture or subject appears. Smallest counter change: in the LIVE leg, run the base locator once per URL and require `LOCATED` for the capture URL as well as the live URL (the row rule says BOTH; `--row` stops at the first LOCATED, here the live URL, so the fabricated `web.archive.org/web/20200101000000id_/...` captures are never fetched). A one-line host check refusing placeholder/reserved documentation hosts would also stop this exact fixture.
```

## Restoration and integrity evidence

- Counter bytes never changed: `accept-c.py` sha256
  `3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca` before and after every run,
  equal to the frozen hash in the round-63 tasking and claims.json surface.
- Probe line rewrites were confined to the entry working file; after the last run the working bytes
  were restored to the committed probe-gold state:
  before restore `e4eca002d0d89546e24f27b6a2802e086719f435bd604de6188d2dea6117e271`,
  after `git checkout --` `62f2cb4d663be88b0d9695d61a9b0e8f103b4ced72c08c9fc0376769610975a1`;
  `git status --porcelain` = 0 lines (clean working tree).
- All fixture files live only under
  `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-CtlCLineScam/` (clone, builder scripts,
  `runs/*.txt` full outputs). The lane worktree `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
  and the fleet repo were not written; no sibling's sources were touched.
- Installs: none. Sandbox git used only inside the scratch clone (`git add/commit`, `git branch -f
  main`, `git checkout --`); no git/jj write in the lane or fleet repos.
