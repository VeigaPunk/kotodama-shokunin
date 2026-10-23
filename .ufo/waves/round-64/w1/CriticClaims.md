# CriticClaims — C control falsification

Axes: **coverage** (new admitted language-socialization knowledge), **operability** (the counter distinguishes real work from copied/stub content), **calibration** (receipts describe exactly what was exercised). This is counterexample evidence, not a claim/round judgment or admission.

## Result and smallest safe correction

**The declared cheap control is reproduced. The stronger teaches-copy requirement is falsified.** A sourceless, quote-dump stub plus copied registry rows fails ROWS for tier/status/absent quote and RESTATE for `no_novel_content_word`, while FILE/ONEID/SWEEP pass. The base do-nothing run matches every leg and detail of `reports/round-64/telemetry/dry-run-c.txt`, after substituting the root pathname.

However, an entire 26-bullet set copied verbatim from registry `teaches` cells can print `RESTATE PASS bad=[] lines=26`. This is **not** a whole ACCEPT-C bypass: that fixture still fails LINK and NOHARM. A separate three-bullet fixture using unchanged current S729/S730/S739 rows also prints RESTATE PASS and LINK PASS with all three teaches cells copied verbatim; its other rows are deliberately absent. These two results isolate a RESTATE false negative rather than claiming the incomplete or duplicate-source fixture is admissible.

Smallest safe correction to propose, **not apply**: through the authorized frozen-counter/pre-data revision process, add a RESTATE failure when the normalized entry clause equals its row's normalized teaches cell (`teaches_copy`). Preserve all existing quote overlap/order, novelty, copied-run, row and other legs. The forcing negatives are the 26-copy fixture below and the current S729/S730/S739 verbatim teaches lines; both must RESTATE-fail. Pair them with non-copied, faithfully supported original bullets as a positive control. The proposed revision/positive pair has **not** been run. Do not retrofit a weaker predicate or present the existing PASS as proof of novel entry content.

Cause: `accept-c.py:275-300` compares the clause with `anchor_quote(cells(row)[5])`; it never reads cell 6 (`teaches`) for RESTATE. In the 26-copy escape, the quote is `a woman's semicircular jewelled headdress for formal occasions`; the copied teaches cell is `Collins defines a tiara as a woman's semicircular jewelled headdress for formal occasions`. Its supposedly novel content words are `collins`, `defines`, `tiara`, all already present in teaches. The mixed 26-source control fails only because two clauses have insufficient in-order quote overlap, **not** because teaches copying is recognized.

Impacted axes: coverage evidence is weaker than claimed (row narration is not new admitted entry content); counter operability misses the required negative; calibration is harmed if either generic lexical PASS or a negative for an unrelated reason is described as an anti-teaches-copy success. This is a fixable proof defect, not a justified axis trade, saturation signal, production-tool repair, or a verdict from this critic. The canonical judge retains judgment.

## Isolation, provenance and exact commands

Scratch root: `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/CriticClaims/` (abbreviated `$S` below). Base corpus extracted with `git -C "$S/base" archive ff30a205c8d23b35f1ac533740121a955a9fda96 | tar -x -C "$S/base"` after a read-only-source `git clone --shared --no-checkout --no-hardlinks` into scratch. Only the scratch clone's main ref was set to that base; `git -C "$S/base" rev-parse main` printed `ff30a205c8d23b35f1ac533740121a955a9fda96`. Fixture `.git` pointers target that scratch clone, never lane git state. NOHARM therefore correctly reports `diff=[]` for these uncommitted scratch additions; no scratch commit was manufactured to green it.

All five runs invoke the **full, unchanged** frozen counter as `python3 -B reports/round-64/accept-c.py --root .`, with cwd printed in each receipt. The runner captures stdout/stderr/exit without changing the predicate, subprocess results, sleeps or fetch behavior. The pinned base citation checker, README sweep and LIVE locator were copied unchanged. Counter SHA-256 in the lane snapshot and each fixture: `4df7b32b430282c81970acf9b6565c6ef96e598038f82ca843a2cace2de08a68`. Each fixture's `fixture.json` records input digests and mappings. Later lane edits are outside this frozen snapshot.

Preparation/execution commands (cwd `$S`):

```sh
python3 -B prepare-controls.py stub
python3 -B run-control.py base
python3 -B run-control.py stub-copy
python3 -B prepare-controls.py reused-teaches
python3 -B prepare-controls.py teaches-escape
python3 -B run-control.py reused-teaches
python3 -B run-control.py teaches-escape
python3 -B prepare-current-teaches.py
python3 -B run-control.py current-teaches-escape
```

`prepare-controls.py`, `prepare-current-teaches.py` and `run-control.py` are retained in scratch as reproduction artifacts, not lane implementation files. All fixtures copy the base corpus, add the target filename, and update the real README row/header/total/footer consistently. Nothing mocks SWEEP. The stub has no provenance trio and only one verbatim quote bullet. Duplicate or partial fixture rows are deliberate negative controls, never represented as real round openings/admitted facts.

### 1. Do-nothing control and original receipt

The original receipt begins `measured-revision ff30a205c8d23b35f1ac533740121a955a9fda96 (lane base; claim C lands absent)`. Its content does contain all six requested failures: FILE/ROWS/APPEND/NOHARM/SWEEP/LIVE; it additionally fails REJECTS and ONEID. RESTATE/HOSTS/LINK pass. My comparison printed `DO_NOTHING_RECEIPT_VECTOR_MATCH True` and `DO_NOTHING_ALL_LEG_DETAILS_MATCH_EXCEPT_ROOT True`. The original receipt SHA-256 read before testing was `ff9e65f3e0c19b3a2829340a6f48f0c7a6709e5e454ebd489d0384bf68efc072`.

```text
cwd /home/vgpnk/.cache/hyaku/kotodama-r64-w1/CriticClaims/base
$ python3 -B reports/round-64/accept-c.py --root .
FILE FAIL unreadable: [Errno 2] No such file or directory: '/home/vgpnk/.cache/hyaku/kotodama-r64-w1/CriticClaims/base/corpus/knowledge/linguistics/language-socialization-and-acquisition.md'
ROWS FAIL bad=['S718:rows=0', 'S719:rows=0', 'S720:rows=0', 'S721:rows=0', 'S722:rows=0', 'S723:rows=0', 'S724:rows=0', 'S725:rows=0'] checked=26
REJECTS FAIL bad=['S744:rows=0', 'S745:rows=0', 'S746:rows=0', 'S747:rows=0', 'S748:rows=0', 'S749:rows=0'] checked=6
ONEID FAIL bad=[] marks=[] cited_lines=0 cited_lines_tool=exit2 clean=False
RESTATE PASS bad=[] lines=0
HOSTS PASS bad=[]
LINK PASS bad=[]
APPEND FAIL missing_base_lines=0 s687_queued=False base=643 measured=643 +32=False
NOHARM FAIL diff=[]
SWEEP FAIL exit=0 topic_row=False
LIVE FAIL subset=['S718', 'S723', 'S728', 'S733', 'S738', 'S743'] bad=['S718:no_row', 'S723:no_row', 'S728:no_row', 'S733:no_row', 'S738:no_row', 'S743:no_row']
ACCEPT-C-64: FAIL
exit=1
```

### 2. Declared sourceless stub plus copied rows

Mapping: S719 copies base S178; the other 25 IDs copy base S009, changing only their IDs. The entry dumps S178's quoted sentence under S719 without a source/provenance header. Thus ROWS visibly catches tier C, queued status and zero quote words; RESTATE catches no novel content and a 14-word copy run. FILE/ONEID/SWEEP are the real frozen legs, not modeled stand-ins.

```text
cwd /home/vgpnk/.cache/hyaku/kotodama-r64-w1/CriticClaims/stub-copy
$ python3 -B reports/round-64/accept-c.py --root .
FILE PASS exists lines=6 h1=1 h2=0 h3=0 topic=True
ROWS FAIL bad=['S718:tier=C', 'S718:status=queued', 'S718:opened=2026-10-19', 'S718:recheck=90d', 'S718:usedby=—', 'S718:quote_words=0', 'S718:no_capture', 'S719:tier=C'] checked=26
REJECTS FAIL bad=['S744:rows=0', 'S745:rows=0', 'S746:rows=0', 'S747:rows=0', 'S748:rows=0', 'S749:rows=0'] checked=6
ONEID PASS bad=[] marks=[] cited_lines=1 cited_lines_tool=exit0 clean=True
RESTATE FAIL bad=['line6:S719:no_novel_content_word', 'line6:S719:copy_run=14'] lines=1
HOSTS PASS bad=[]
LINK FAIL bad=['S718:registry_hits=26', 'S719:registry_hits=2', 'S720:registry_hits=26', 'S721:registry_hits=26', 'S722:registry_hits=26', 'S723:registry_hits=26']
APPEND FAIL missing_base_lines=0 s687_queued=False base=643 measured=669 +32=False
NOHARM FAIL diff=[]
SWEEP PASS exit=0 topic_row=True
LIVE FAIL subset=['S718', 'S723', 'S728', 'S733', 'S738', 'S743'] bad=['S718:NOT_LOCATED no quote', 'S723:NOT_LOCATED no quote', 'S728:NOT_LOCATED no quote', 'S733:NOT_LOCATED no quote', 'S738:NOT_LOCATED no quote', 'S743:NOT_LOCATED no quote']
ACCEPT-C-64: FAIL
exit=1
```

### 3. Mixed 26-row verbatim-teaches set

S692–S717 at the base are remapped in order to S718–S743; only id and used-by are changed. Every entry clause equals its copied row's teaches cell byte-for-byte. Six inherited disposition rows supply REJECTS; S687's status/used-by are changed to queued/— in scratch. RESTATE fails only S722 (copied S696) and S735 (copied S709), both `in_order`, not teaches-copy novelty. ROWS separately notices S692's absent capture. This is the requested set-level RESTATE failure, but it does not establish the intended discriminator.

```text
cwd /home/vgpnk/.cache/hyaku/kotodama-r64-w1/CriticClaims/reused-teaches
$ python3 -B reports/round-64/accept-c.py --root .
FILE PASS exists lines=31 h1=1 h2=0 h3=0 topic=True
ROWS FAIL bad=['S718:no_capture'] checked=26
REJECTS PASS bad=[] checked=6
ONEID PASS bad=[] marks=[] cited_lines=26 cited_lines_tool=exit0 clean=True
RESTATE FAIL bad=['line10:S722:in_order=2', 'line23:S735:in_order=1'] lines=26
HOSTS PASS bad=[]
LINK FAIL bad=['S718:registry_hits=2', 'S719:registry_hits=2', 'S720:registry_hits=2', 'S721:registry_hits=2', 'S722:registry_hits=2', 'S723:registry_hits=2']
APPEND PASS missing_base_lines=0 s687_queued=True base=643 measured=675 +32=True
NOHARM FAIL diff=[]
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S718', 'S723', 'S728', 'S733', 'S738', 'S743'] bad=[]
ACCEPT-C-64: FAIL
exit=1
```

### 4. Stronger 26-bullet counterexample

All 26 new IDs copy base S710 (only id/used-by changed); all 26 entry clauses copy its teaches cell verbatim. Source cell, quote, tier, status, date and recheck are unchanged. Six inherited disposition rows and the queued S687 edit are as above. ROWS/REJECTS/ONEID/RESTATE/APPEND/SWEEP/**LIVE** pass; LINK rejects duplicate URLs and NOHARM compares the unchanged scratch main ref. The observed RESTATE PASS contradicts “teaches text is not novel entry content.” Neither the duplicate URL failure nor a snapshot/ref mismatch repairs that lexical blind spot.

```text
cwd /home/vgpnk/.cache/hyaku/kotodama-r64-w1/CriticClaims/teaches-escape
$ python3 -B reports/round-64/accept-c.py --root .
FILE PASS exists lines=31 h1=1 h2=0 h3=0 topic=True
ROWS PASS bad=[] checked=26
REJECTS PASS bad=[] checked=6
ONEID PASS bad=[] marks=[] cited_lines=26 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=26
HOSTS PASS bad=[]
LINK FAIL bad=['S718:registry_hits=27', 'S719:registry_hits=27', 'S720:registry_hits=27', 'S721:registry_hits=27', 'S722:registry_hits=27', 'S723:registry_hits=27']
APPEND PASS missing_base_lines=0 s687_queued=True base=643 measured=675 +32=True
NOHARM FAIL diff=[]
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S718', 'S723', 'S728', 'S733', 'S738', 'S743'] bad=[]
ACCEPT-C-64: FAIL
exit=1
```

### 5. Same miss on the actual current row vocabulary

This deliberately partial fixture appends only the unchanged current contribution rows S729/S730/S739 and copies each teaches cell verbatim into a bullet. No new URL/quote/tier/status is invented; other new rows are absent, so LIVE performs no source fetch. These are the exact copied clauses:

```text
- Helps worldbuilders portray Lebanese mothers using more infant-directed speech per minute than the study's American comparison mothers. (S729)
- Helps learners distinguish children’s simultaneous acquisition of two languages from birth from later sequential second-language learning. (S730)
- Helps worldbuilders model how caregivers vary terms of address across situations as children learn community language practices. (S739)
```

```text
cwd /home/vgpnk/.cache/hyaku/kotodama-r64-w1/CriticClaims/current-teaches-escape
$ python3 -B reports/round-64/accept-c.py --root .
FILE PASS exists lines=8 h1=1 h2=0 h3=0 topic=True
ROWS FAIL bad=['S718:rows=0', 'S719:rows=0', 'S720:rows=0', 'S721:rows=0', 'S722:rows=0', 'S723:rows=0', 'S724:rows=0', 'S725:rows=0'] checked=26
REJECTS FAIL bad=['S744:rows=0', 'S745:rows=0', 'S746:rows=0', 'S747:rows=0', 'S748:rows=0', 'S749:rows=0'] checked=6
ONEID PASS bad=[] marks=[] cited_lines=3 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=3
HOSTS PASS bad=[]
LINK PASS bad=[]
APPEND FAIL missing_base_lines=0 s687_queued=False base=643 measured=646 +32=False
NOHARM FAIL diff=[]
SWEEP PASS exit=0 topic_row=True
LIVE FAIL subset=['S718', 'S723', 'S728', 'S733', 'S738', 'S743'] bad=['S718:no_row', 'S723:no_row', 'S728:no_row', 'S733:no_row', 'S738:no_row', 'S743:no_row']
ACCEPT-C-64: FAIL
exit=1
```

## Inherited defects and limits

The initial inherited artifact tree still lacked `rows/ScribeRowS723/row.txt` and `rows/ScribeRowS740/row.txt` when inspected; the glob returned those paths missing. The entry skeleton directory contained `entry.md` but no `readme-row.txt`. Its line 4 still uses the two-ID range S718–S743, so carrying that line into a finished entry unchanged would violate ONEID **[INFERENCE from the frozen regex, not a skeleton check run here]**. The staged rows/teaches were not treated as a complete final entry. I did not rerun the inherited 30/32 claim or claim it is a new verified tally. Six reused disposition rows passed the frozen REJECTS shape check in the two full 32-row controls; that does not attest their source access, truth or outside admission.

No final real-entry acceptance, source-authority/support review, independent admission, claim O/Ca check, judge, fleet operation, other runtime, commit, or lane index/jj/ref mutation was performed. No frozen counter was edited. Only this assigned report was written in the lane; all fixture work is under the allowed scratch root. **Tools installed/updated: none.**

Report: .ufo/waves/round-64/w1/CriticClaims.md

## Addendum — completed actual 26-row teaches control

After the initial report, both missing row owners supplied S723/S740 and I read their finalized contribution files. Their inherited absence above is a historical observation, not a remaining control prerequisite. I then tested the exact completed S718–S743 contribution set: every entry clause copies its row's teaches cell verbatim, while all 32 contribution ROW lines are copied into the fixture and S687 is queued in scratch. No replacement rows or invented teaches are used in this sixth run.

Commands (cwd `$S`):

```sh
python3 -B prepare-controls.py teaches
python3 -B run-control.py teaches-all
```

Observed full output:

```text
cwd /home/vgpnk/.cache/hyaku/kotodama-r64-w1/CriticClaims/teaches-all
$ python3 -B reports/round-64/accept-c.py --root .
FILE PASS exists lines=31 h1=1 h2=0 h3=0 topic=True
ROWS PASS bad=[] checked=26
REJECTS PASS bad=[] checked=6
ONEID PASS bad=[] marks=[] cited_lines=26 cited_lines_tool=exit0 clean=True
RESTATE FAIL bad=['line6:S718:in_order=0', 'line7:S719:in_order=2', 'line8:S720:in_order=1', 'line9:S721:in_order=1', 'line10:S722:in_order=1', 'line12:S724:in_order=2', 'line13:S725:in_order=1', 'line14:S726:in_order=0'] lines=26
HOSTS PASS bad=[]
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 s687_queued=True base=643 measured=675 +32=True
NOHARM FAIL diff=[]
SWEEP PASS exit=0 topic_row=True
LIVE FAIL subset=['S718', 'S723', 'S728', 'S733', 'S738', 'S743'] bad=['S718:NOT_LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC4794163', 'S733:NOT_LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709']
ACCEPT-C-64: FAIL
exit=1
```

Receipt: `$S/teaches-all.txt`; input digests and source contribution snapshots: `$S/teaches-all/fixture.json`. Entry SHA-256: `6d78fa00775a37b4d0a067af9f0d4c26864c11cfd6bf10f7fe43f8dc166d0a24`. This satisfies the requested full actual-set RESTATE failure, but does not erase the three actual verbatim clauses that independently pass RESTATE, nor turn its quote-overlap failures into a teaches-copy guard. LIVE also failed the frozen budget for S718/S733 in this run; this is not a passing final-entry acceptance measurement.

Tool/dependency addendum: this sixth run exercised the pinned locator's PDF branch, which provisioned **pypdf 5.4.0** via `uv run --no-project --quiet --with pypdf==5.4.0` for PDF text extraction, under `$S/uv-cache/`. Its installed METADATA explicitly reports `Name: pypdf`, `Version: 5.4.0`; the environment records uv 0.13.0 and the already-existing managed CPython 3.15.0. No system transaction, global tool upgrade or new interpreter installation was performed. The earlier “none” statement applies to the first five runs; this dependency provisioning is now recorded explicitly.

Report: .ufo/waves/round-64/w1/CriticClaims.md
