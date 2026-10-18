# R25-D11 — argot-derivation leg, execution 1: the replay over D4's stated inputs

- **Seat:** R25-D11 (argot execution 1 of 4), round 25, loop 3 build 1 of 4
  (`devin/deepseek-v4-1-flash-high`), claim **D** `argot-derivation-check`
  (`reports/round-25/claims.json:20-27`).
- **Date:** 2026-10-18. Baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`;
  working-tree HEAD at write time `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- **Write scope:** this file only. Scratch under `.scratch/r25-d11/`
  (`TMPDIR=$PWD/.scratch` preceded every scratch write). No tool, gate, packet,
  component or earlier-round byte touched; no commit, no push.
- **Canon:** NON-CANON engineering evidence. No real language, institution,
  script or argot is described, cited or approximated.

## 1. What the leg is

The claim's discipline is the SKILL's derivation-replay rule
(`SKILL.md:189-217`, "a typed derivation is replayable only when … the replay
names every input") applied to D4: **machine-readable `pattern`/`output` pairs
replayed against stated inputs; a form the stated rules do not yield is a
violation.**

D4's delivered replay surface is `morphology.derivation_rules`
(`examples/culture-d4/packet.d4.yml:205-226`) — three rules, each with a
machine-readable `pattern` and `output`:

| rule | kind | pattern | output |
|---|---|---|---|
| `CX-01` | compound | `^(?P<a>.+)\+(?P<b>.+)$` | `{a}{b}` |
| `CX-02` | suffix | `^(?P<stem>.+)$` | `{stem}ar` |
| `CX-03` | suffix | `^(?P<stem>.+)$` | `{stem}en` |

The rule set is declared replayable **by the packet itself**:
`derivation_note` (`:226`) states "the three rules replay the four derived or
compound records in this file and the eight names in 05-naming". That is the
pre-registered expectation; this leg measures it.

The records that carry a stated derivation are:

- **lexicon, route `derived`/`compound`** — `L-45` `tikmes` (CX-01, bases
  `tik`+`mes`), `L-46` `mesar` (CX-02, base `mes`), `L-47` `kalen` (CX-03,
  base `kal`), `L-48` `haitun` (CX-01, bases `hai`+`tun`)
  (`examples/culture-d4/packet.d4.yml:765,783,799,815`);
- **names with a `formation` record** — `NM-01`…`NM-08`, each carrying
  `formation{stem, bases, rule, expected}` (`:1938-2104`).

## 2. Command and result

```
export TMPDIR=$PWD/.scratch
python3 .scratch/r25-d11/argot-replay.py examples/culture-d4/packet.d4.yml
```

Harness `sha256 4934f17d0cfed1b5248d45aca18dab6b129d42ce709981b76ed70f5f7853673d`
(scratch, this seat). It reads the packet with the gate's own subset reader
(`tools/gates/naming-collision-gate.py:488 load_yaml`, sha256
`d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d`), resolves
each record's construction name to its rule id via the `constructions` block
(`:995-1040`), applies the rule's `pattern` to the record's stated stem
(`+`-joined bases for a compound rule, the single base for a suffix rule), and
compares `output.format(**groups)` against the delivered form.

**Result (2026-10-18T17:29Z): 12 rows replayed, 0 violations.**

```
ok   L-45 | tikmes | derived | CX-01 | tikmes | ok
ok   L-46 | mesar  | derived | CX-02 | mesar  | ok
ok   L-47 | kalen  | derived | CX-03 | kalen  | ok
ok   L-48 | haitun | derived | CX-01 | haitun | ok
ok   NM-01 | tumhai | name | CX-01 | tumhai | ok
ok   NM-02 | kalker | name | CX-01 | kalker | ok
ok   NM-03 | samren | name | CX-01 | samren | ok
ok   NM-04 | mestum | name | CX-01 | mestum | ok
ok   NM-05 | haitik | name | CX-01 | haitik | ok
ok   NM-06 | meslun | name | CX-01 | meslun | ok
ok   NM-07 | kalnes | name | CX-01 | kalnes | ok
ok   NM-08 | salwer | name | CX-01 | salwer | ok
```

The declared replay surface (4 + 8 = 12) is exactly the replayed surface: the
`derivation_note`'s pre-registered count is confirmed by measurement, not
inherited from the note.

## 3. Independent corroboration

The gate's own Gate C leg (`tools/gates/naming-collision-gate.py:1346-1523`)
carries the same replay for names, and it agrees:

```
python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml
→ exit 1, 0 lines matching DERIV (all findings are 7 NAME-NEAR REVIEW +
  6 PHON-INVENTORY FAIL on the garment glosses + 1 CROSS-HOLD = 14 lines)
```

Zero `DERIV-*` lines over the source packet (measured 2026-10-18T17:29Z,
receipt `.scratch/r25-d11/g-src.out`, 14 lines, `grep -c DERIV` → 0). The
replay half of Gate C is clean on D4; the gate's red comes from its other legs.

## 4. Limits

- The leg replays the **stated** derivation only. It cannot detect a record
  whose stated rule is *not* the rule the language actually used — only that
  the stated rule reproduces the stated form. A rule set that is wrong but
  self-consistent passes; that is the replay discipline's known bound, not a
  defect introduced here.
- The register-scoped half of the round-17 forecast (the argot itself) is
  absent from the delivered packet; see `execution-3.md` for the named delta.
- Readings bind to the digests above; a later edit to the packet or the gate is
  a re-read event.
