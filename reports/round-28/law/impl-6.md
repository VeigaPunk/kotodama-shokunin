# R28-D10 — the named holds, the defects left standing, and the probe mistake this seat made

- **Seat:** R28-D10 (D axis, law-replay implementation 6 of 8). Round 28, loop 3
  build 4 of 4, claim **D** `register-law-replay`. Integrator: `impl-1.md`.
- **Date:** 2026-10-18. Baseline `6c0ac448…`; lane HEAD `69cecbc`.
- **Write scope:** this file only; scratch under `.scratch/r28-d/`.
- **Canon:** NON-CANON engineering evidence. This file adjudicates nothing.

## 1. The hold set, revised honestly

`examples/culture-d4/expected-holds.json` — **12 holds / 0 notes / 0 fails**,
unchanged from round 22. The revision note names the round-28 landing and the
RL-4 fix; `supersedes_pins` gains three `r27_*` keys.

**The counts are unchanged because nothing in this claim creates or closes a
form obligation.** The RL-4 fix lands eight *institutional* records (OR/LI/EN),
not forms; the law rows are not forms; the replay leg adds no row. The six
garment-form obligations still route to their twelve record/slot rows. A hold set
whose counts moved here would be a signal that something was absorbed rather than
reported.

**What was NOT done to the hold set**, named because each would have been a
silent laundering:

- no hold was downgraded to a note to make a count look better;
- no hold was deleted;
- the `projector_sha256` pin was **not** changed — the projector did not move, and
  re-pinning it "to be safe" would hide a real drift later;
- the round-26 pins were not overwritten; they stay under their own keys.

## 2. The findings left standing, each with its owner

The replay leg reports four findings on the clean packet. They are defects of a
**filed** artifact, so they are reported, never repaired here:

| class | row | token | why it is a finding | owner |
|---|---|---|---|---|
| `D4L-LAW-DANGLING` | `RGL-01` | `QREG-05` | the design row the law claims to implement is not a packet record | `13-register-law.yml`'s owner |
| `D4L-LAW-DANGLING` | `RGL-01` | `QREG-07` | same | same |
| `D4L-LAW-DANGLING` | `RGL-02` | `QREG-06` | same | same |
| `D4L-LAW-DANGLING` | `RGL-03` | `QREG-08` | same | same |

The design seat measured the same four independently and named the same owner
(`reports/round-28/law/design.md` §3.1, §6). Two acceptable dispositions are on
record there: land `QREG-05..08` as `registers` records, or drop the `design_row`
field and let `cite` carry the reference (the `cite` paths all resolve — 13 of
13, `design.md` §3.6). **Both rewrite a filed round-27 file**, so neither is this
seat's move.

A second class-fit question is recorded there too: `RGL-04`/`RGL-05` are
constraint rows (sound-channel, dating) sitting in a speech-act block, so the
design's reference probe reports two `CONSEQUENCE` findings. This seat's leg
**scopes the consequence resolution by the row's own `force: none`** and reports
0 — the design's §6 owner table offers exactly that as one of the two acceptable
dispositions. Recorded as a deliberate difference, not a disagreement.

## 3. The defects this seat found in its own work

**One, and it changed the implementation.** The first `none`-resolution read the
literal `none` by token membership, which let a value append garbage to it and
pass:

```
'none but wibble'  -> []     # the hole
```

The selftest caught it; `NON_FORCE_RE` now requires a separator after the head
word; the probe fires. Recorded in `impl-2.md` §3 and `impl-3.md` §5.

## 4. A probe mistake this seat made, and corrected

Worth recording because it is exactly the class of error a control exists to
catch. The seat-side probe that tampers a **law row's** `register`/`axis` fields
initially anchored on the string `register_law:` — which also occurs in the
packet's `contract.record_fields` block, **earlier in the file**. The first
`register: "stamp"` match after that anchor was therefore a **lexicon** row
(`L-56 kit`), not a law row:

```
$ … probe (wrong anchor)
register    added_classes=[] lines=0        # the tamper landed on a lexicon record
$ … probe (anchored on '\nregister_law:\n')
register    added_classes=['D4L-LAW-REGISTER'] lines=1   # fires
```

The correction is the anchor, and the lesson is the one the design's §1 states:
a tamper is only a control if it lands on the thing under test. The round
runner's own `tamper_law_text` anchors on the first `^\s*force:`/`^\s*speaker:`/
`^\s*consequence:` line — which, measured, is a law row for all three fields,
because `force` occurs nowhere else in the packet and `speaker`/`consequence`
occur first in the `register_law` block. Verified:

```
$ grep -n '^ *force:' examples/culture-d4/packet.d4.yml | head -3
2722:    force: "directive-binding for the charge; …"      # RGL-01
2738:    force: "commissive-binding refused"               # RGL-02
2754:    force: "directive-binding, not-rollable"          # RGL-03
```

So the runner's three tampers do land on law rows, and its measured +1 deltas are
real.

## 5. The eight record ids, and what each is

For a reader who wants to check RL-4 without re-deriving it:

| block | ids | what they are |
|---|---|---|
| `records` | `OR-01`, `OR-02`, `OR-03` | the three script stages: the count-stamp tally (E0), the extended stamp hand (E1), the league hand (E2) |
| `literacy_institutions` | `LI-01`, `LI-02`, `LI-03` | the stamp-house, the mold-keeper's license, the furnace roll |
| `enforcement` | `EN-01`, `EN-02` | the council's fine, the stamp-holder's refusal to mark |

`OR-02` is the one the law cites (`RGL-01`'s `mold-keeper (OR-02, component-only)`)
and `EN-01`/`EN-02` are the delivered tree's **only two enforcement mechanisms** —
round 27's review called their invisibility the same class as round 26's RD-1.
Both now ride the packet as records.

## 6. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
python3 -c "import json;d=json.load(open('examples/culture-d4/expected-holds.json'));print(d['counts'], len(d['holds']), sorted(d['supersedes_pins']))"
grep -n '^ *force:' examples/culture-d4/packet.d4.yml | head -3
python3 -c "import runpy;n=runpy.run_path('tools/gates/naming-collision-gate.py');p=n['load_yaml'](open('examples/culture-d4/packet.d4.yml').read());print([(k,[r['id'] for r in p[k]]) for k in ('records','literacy_institutions','enforcement')])"
```
