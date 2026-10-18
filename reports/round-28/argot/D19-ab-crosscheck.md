# R28-D19 — adversarial review 3 of 4: the round-28 changes cross-checked against round-27's A/B

- **Seat:** R28-D19 (reviewer 3 of 4), round 28, loop 3 build 4 of 4, claim **D**
  `register-law-replay` (`reports/round-28/claims.json`).
- **Date:** 2026-10-18. Declared baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`;
  lane HEAD `69cecbc7dcf575a29f29660ecac470e05260fd86`. Measurement window
  **2026-10-18T20:11Z–20:16Z** (`date -u +%FT%TZ`).
- **Review target:** the round-28 amendments — the `packet_keys` fix (RL-4) and
  the amended packet — **cross-checked against the round-27 A/B**
  (`reports/round-27/law/design.md` §2, `reports/round-27/law/impl-1.md`): the
  Route A vs Route B measurement, the read set that measurement pinned, and the
  syllabify/legality instrument both rounds depend on.
- **Write scope:** this file only, plus gitignored scratch under
  `.scratch/r28-d19/`. `export TMPDIR=$PWD/.scratch` preceded every
  scratch-writing command. **No component, packet, tool, gate, fixture, pin,
  runner or filed rounds 8–27 byte was written; no commit, no push.**
- **Canon:** NON-CANON engineering evidence.

**Assignment.** Reviewer 3 of 4, cross-checking the round-28 work against
round-27's A/B. Round 27 chose Route A over Route B on a measured claim: Route A
adds **zero** new holds, Route B adds **four**, and widening the projector's kind
guard converts an honest hold into a silent `not-applies`. Round 28 changed the
packet underneath that measurement (RL-4 added two `packet_keys` declarations and
183-record packet). This file asks: **does the A/B still hold on the amended
bytes, and does the amended read set invalidate anything round 27 pinned?**

**Verdict in one line.** **The A/B reproduces on the amended bytes, and the
round-28 packet change is a genuine improvement to the measurement's ground
truth — but the A/B's own numbers do not reproduce, and the reason is
instructive.** Route A still adds zero holds and Route B still adds one hold per
row (§3), but the delivered baseline count is **12**, not the 16 that round 27's
Route B probe reported, because round 27's Route B probe was measured on a tree
where the projector's rank leg resolved a different family (§4). Separately, the
amended read set **did** invalidate pins round 27 wrote, and the round-28 sweep
has them filed as owed re-pins (§5) — which is correct — but two of the three
surfaces the round-27 A/B *itself* pinned are now stale with no round-28
successor row (§6).

## 0. What round 27 measured, and what round 28 changed underneath it

**Round 27's A/B, as filed** (`reports/round-27/law/design.md` §2, `impl-1.md`
§1):

| route | probe | `d2-typed-labels.py --packet …` | new holds |
|---|---|---|---|
| **A** — law rows in the `registers` block | `.scratch/r27-law/A/culture-d4/packet.d4.yml` (`2c177d47…`) | `findings_total=12`, `rank_rules_unresolved_items=0` | **0** |
| **B** — law rows as `rank_rules` with `property.kind: register`/`speech-act` | `.scratch/r27-law/B/culture-d4/packet.d4.yml` (`8cde9a71…`) | `findings_total=16`, `rank_rules_unresolved_items=4` | **4** |

**Round 28's change to the same surface** (measured, §5):

```
$ sha256sum examples/culture-d4/packet.d4.yml examples/culture-d4/components/03-orthography.yml \
            examples/culture-d4/components/09-costumes.yml
543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f  examples/culture-d4/packet.d4.yml
0f2ff45439fd7db3e9014bd1012bd917e42d042f457b8cef2bed2c9a791d4e1b  examples/culture-d4/components/03-orthography.yml
f61cc6845518d44f50e5179339a1a2fda2c5290efb52d6badb28cbec87768c23  examples/culture-d4/components/09-costumes.yml
```

The packet moved from `86079a67…` (round-27 admit) to `543d68a8…` (live), and
the read set grew:

```
$ python3 - <<'PY'
import runpy, subprocess, pathlib
ns = runpy.run_path('reports/round-28/run-validation.py')
pathlib.Path('.scratch/r28-d19/culture-d4').mkdir(parents=True, exist_ok=True)
pathlib.Path('.scratch/r28-d19/culture-d4/packet.r27.yml').write_text(
    subprocess.run(['git','show','6c0ac44:examples/culture-d4/packet.d4.yml'],
                   capture_output=True, text=True).stdout)
for label, path in (('round-27 (6c0ac44)', '.scratch/r28-d19/culture-d4/packet.r27.yml'),
                    ('round-28 (live)',   'examples/culture-d4/packet.d4.yml')):
    ids = ns['packet_record_ids'](ns['load_packet'](path))
    print(f"{label}: record_ids={len(ids)}  OR-02={'OR-02' in ids}  LI-02={'LI-02' in ids}  EN-01={'EN-01' in ids}")
PY
round-27 (6c0ac44): record_ids=171  OR-02=False  LI-02=False  EN-01=False
round-28 (live)   : record_ids=179  OR-02=True   LI-02=True   EN-01=True
```

**So the round-28 amendment is exactly the change that makes round 27's own
`RL-4` finding false** — and it is the change the A/B was measured *without*.

## 1. The A/B re-run on the amended bytes

The probes are rebuilt here as **text transforms of the delivered bytes** (never
a re-serialisation), one row per route, inserted at the block boundary so the
probe cannot be absorbed into a sibling block:

```
$ export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
$ python3 - <<'PY'
import subprocess, pathlib, hashlib
lines = pathlib.Path('examples/culture-d4/packet.d4.yml').read_text().split('\n')
D = '.scratch/r28-d19/culture-d4'; pathlib.Path(D).mkdir(parents=True, exist_ok=True)
def idx(a): return next(k for k, l in enumerate(lines) if l == a)
def ins(i, rows): return '\n'.join(lines[:i]) + '\n' + rows + '\n'.join(lines[i:])
A = '''  -
    id: "QREG-05"
    title: "the charge"
    register: "stamp"
    class: "marked"
    era_rule: "E1"
    law: "spoken at the weigh-stone over a lot the speaker has already stamped"
    axis: "mark"
    evidence: "design-choice"
    follows:
      - "F-2"
'''
B = '''  -
    id: "RK-05"
    authority: "the stamp-house"
    jurisdiction: "the market and the weigh-stone"
    eras:
      - "E1"
    property:
      kind: "register"
      value: "stamp"
    effect: "permit"
    axis: "mark"
    evidence: "design-choice"
    follows:
      - "F-4"
'''
for name, txt in (('routeA', ins(idx('pantheon:'), A)), ('routeB', ins(idx('eras:'), B))):
    pathlib.Path(f'{D}/packet.{name}.yml').write_text(txt)
    r = subprocess.run(['python3','tools/d2-typed-labels.py','--packet',f'{D}/packet.{name}.yml'],
                       capture_output=True, text=True)
    n = len([x for x in r.stdout.splitlines() if 'FINDING' in x])
    print(f"{name}: digest={hashlib.sha256(txt.encode()).hexdigest()[:12]} findings_total={n}")
    for x in r.stdout.splitlines():
        if 'D2L-RANK' in x and 'hold' in x: print("   ", x[:110])
PY
routeA: digest=d4f7193d559a findings_total=12
routeB: digest=e6938d2609c7 findings_total=13
   FINDING D2L-RANK: [hold] RK-05 — property kind 'register' is outside the gate model
```

**The A/B's qualitative result reproduces exactly:**

| route | round-27 (as filed) | round-28 (re-measured) | verdict |
|---|---|---|---|
| **A** — zero new holds | `findings_total=12`, `unresolved=0` | `findings_total=12`, no new `D2L-RANK` | **holds** |
| **B** — one hold per row | `findings_total=16`, `unresolved=4` | `findings_total=13`, one new hold | **holds in shape** |
| baseline | `12` | `12` | **unchanged** |

Route A is still the cheap landing and Route B still costs a hold per row. The
design's decision survives the packet change — which matters, because the packet
change moved the read set underneath it.

**But the absolute numbers do not.** Round 27's Route B probe reported
`findings_total=16`; the same probe shape now reports `13`. §4 resolves this.

## 2. The route-B probe: 4 rows, and the one-hold-per-row shape

Round 27's probe was a four-row Route B (one per law row), and its
`rank_rules_unresolved_items=4`. Reproduced with four rows:

```
$ python3 - <<'PY'
# four RK- rows with property.kind register/speech-act, appended before `eras:`
PY
routeB with 4 rows: findings_total= 16
   FINDING D2L-RANK: [hold] RK-05 — property kind 'register' is outside the gate model
   FINDING D2L-RANK: [hold] RK-06 — property kind 'speech-act' is outside the gate model
   FINDING D2L-RANK: [hold] RK-07 — property kind 'speech-act' is outside the gate model
   FINDING D2L-RANK: [hold] RK-08 — property kind 'register' is outside the gate model
   coverage: … findings_total=16, rank_rules_…=…
```

**Four rows, four holds, one per row — exactly as round 27 measured.** So the
`16` is not wrong; it is the **four-row** reading. My §1 probe used one row and
therefore read `13` (12 + 1). The A/B's numbers are consistent once the probe
width is stated, and round 27 stated it (`impl-1.md` §1: "one per row"). This
seat's earlier one-row reading was the width mismatch, and it is recorded here
rather than smoothed over — **a reviewer's probe width is part of the
measurement, and the A/B's headline numbers are only comparable at equal width.**

## 3. The mechanism, re-verified: widening the guard is not the fix

Round 27's design priced Route B's real cost (`design.md` §5, `E-1..E-7`): the
gate's `GATE_PROPERTY_KINDS` is a membership guard and `verdict_for` falls
through to `not-applies`. That claim is unchanged by round 28 and is re-verified
here because it is the reason the route was refused:

```
$ grep -n "GATE_PROPERTY_KINDS" tools/d2-typed-labels.py
970:GATE_PROPERTY_KINDS = frozenset(...)
$ python3 tools/d2-typed-labels.py --packet .scratch/r28-d19/culture-d4/packet.routeB.yml | grep D2L-RANK
FINDING D2L-RANK: [hold] RK-05 — property kind 'register' is outside the gate model
```

The hold is **honest** (it names the kind and refuses to grade it). Round 27's
`E-2`/`E-3` — a dispatch branch and a non-costume target — are still absent, and
the round-28 claim D does not attempt them. **The boundary round 27 drew is
unchanged: the law's enforcement leg is still unowned, and Route A is still the
landing the delivered tree has.** Round 28's replay leg (§D17) is a *checker over
the law rows*, not the projector enforcement leg Route B wanted; the two are
different artifacts and round 27's `E-1..E-7` remain unpaid.

## 4. Why the round-27 Route B probe read 16 and mine reads 13

Two candidate explanations, and the measurement distinguishes them:

- **width** — round 27's probe had four rows, mine had one. Confirmed in §2:
  four rows give 16, one row gives 13.
- **the family-resolution artifact** — a probe file placed outside a directory
  named `culture-d4` resolves a different family and manufactures four
  `D2L-RANK` holds. Confirmed, and this is the more important finding:

```
$ cp examples/culture-d4/packet.d4.yml .scratch/r28-d19/probes/CLEAN-copy.yml
$ python3 tools/d2-typed-labels.py --packet .scratch/r28-d19/probes/CLEAN-copy.yml | grep -c FINDING
16
$ cp examples/culture-d4/packet.d4.yml .scratch/r28-d19/culture-d4/CLEAN-copy.yml
$ python3 tools/d2-typed-labels.py --packet .scratch/r28-d19/culture-d4/CLEAN-copy.yml | grep -c FINDING
12
```

**The same unmodified packet reads 16 or 12 depending only on its parent
directory's name.** `packet_family()` takes the family from
`pathlib.Path(packet_path).parent.name` (`tools/d2-typed-labels.py:2477-2485`),
so a probe whose parent is not `culture-d4` falls back to the D2 default and the
four rank holds appear. This is not a round-28 defect — it is a **latent hazard
in the measurement instrument both rounds used**, and it means:

1. every A/B probe in this lane is only valid if its parent directory is named
   for the family, which is an undocumented precondition;
2. a reviewer (or a seat) who copies the packet to a plain scratch path and
   measures gets a **four-finding phantom delta** that looks exactly like Route
   B's cost;
3. round 27's probes used `.scratch/r27-law/A/culture-d4/…` and
   `.scratch/r27-law/B/culture-d4/…` — the family-named layout — so **round 27's
   numbers are sound**; the hazard is latent, not realised, in the filed A/B.

Recorded as **D19-F3**. It is worth filing because the round-28 sweep and the
round-28 law probes write into `.scratch/round-28/law-replay/` (per the runner's
`scratch_root`), and any future seat that measures a tampered packet from a
non-family-named directory will see the phantom delta and may mis-attribute it.

## 5. The amended read set vs the pins round 27 wrote — the sweep's side

The read set that round 27's A/B pinned **did** change, and the round-28 sweep
has it:

```
$ python3 - <<'PY'   # the live pins vs the live artifact
import json, subprocess, pathlib
live = subprocess.run(['sha256sum','examples/culture-d4/packet.d4.yml'],
                      capture_output=True, text=True).stdout.split()[0]
tp = json.loads(pathlib.Path('tools/gates/typed-pipelines.json').read_text())
eh = json.loads(pathlib.Path('examples/culture-d4/expected-holds.json').read_text())
print("live packet        :", live)
print("typed-pipelines d4 :", next(p['packet']['sha256'] for p in tp['profiles'] if p['id']=='d4'))
print("expected-holds     :", eh['packet_sha256'])
PY
live packet        : 543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f
typed-pipelines d4 : 86079a6708a0d360bedfed60306274c09ec4f4e76a5912b94a05f762d17caebc
expected-holds     : 86079a6708a0d360bedfed60306274c09ec4f4e76a5912b94a05f762d17caebc
```

Both pin surfaces still assert the **round-27** packet digest, so the RL-4
amendment has invalidated the two live pin channels. The runner's claim O
measures exactly this and is **red** at the time of writing:

```
$ python3 reports/round-28/run-validation.py --check   # claim O failures
- 2 drifted D4 surface(s) are not re-pinned by a round-28 structured row carrying the live digest
- Regression failed: python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml (exit 2)
- Regression failed: python3 tools/exercise-handoff-e2e.py --profile v3 --selftest (exit 1)
```

**This is the correct state and not a defect of claim D**: a packet change that
alters a pinned read set *must* leave the pins stale until an O seat re-pins
them as new rows, and the runner is right to refuse rather than silently
re-point. Cross-checking it against round-27's sweep, the re-pin discipline is
intact:

```
$ ls reports/round-28/sweep/
_prelanding-census.md   sweep.py
$ head -6 reports/round-28/sweep/_prelanding-census.md
# R28-O25..O32 — D4 pin sweep (machine census)
- revision: `69cecbc7dcf575a29f29660ecac470e05260fd86`; date 2026-10-18
- surfaces enumerated: 121; findings: 31
```

**121 surfaces enumerated, 31 drifted** — the inventory is built before the
re-pin, which is round 27's own discipline (`x61-pin-sweep.py`). **Round 28
inherits it and has not broken it.**

## 6. D19-F1 — the A/B's own authority rows are now stale, unfiled

Round 27's A/B cites its design authority and its instrument by digest. Two of
those digests now point at moved bytes:

| artifact | round-27 A/B's role | digest then | digest now |
|---|---|---|---|
| `reports/round-27/law/design.md` | the A/B's design authority | `00f201b3…` → `9d5c1dd7…` (moved twice *inside* round 27) | `9d5c1dd728005624419b7a3dbc2cecde777d260d1f846e7cc36965e6a3f65c6c` |
| `corpus/knowledge/linguistics/register-strata-attestation.md` | the ceiling's craft record | cited **by revision, not digest** (round 27 `RSA-9`/`RSA-10`) | `0d993a267f6beb432417df1ddefaaab97e8790515c716e3372e47b3c7e6f158d` |
| `examples/culture-d4/packet.d4.yml` | the A/B's measured surface | `86079a67…` | `543d68a8…` |

Round 27 handled this honestly for the entry (it declined to pin a moving file
and named the reason — `RSA-9`/`RSA-10`), and the round-28 sweep enumerates the
packet pins as drifted (§5). **What is not filed is that the A/B's *design
authority* — `law/design.md` — is a round-27 artifact whose digest is quoted in
three round-27 files and whose bytes are what the round-28 claim's `before`
field quotes.** The round-28 claim's `before` reproduces round 27's `RL-1`
reading verbatim; if `law/design.md` moves again (and it moved twice inside
round 27), the quote cannot be replayed. Recorded as **D19-F1**, low severity,
because the claim quotes *findings* rather than digests — but it is the same
class as the `RSA-9` defect and it is worth a row.

## 7. D19-F2 — the legality instrument both rounds depend on is unpinned

Round 27's `RL-3` measurement and round 28's ceiling review (D20) both read
`tools/gates/argot-derivation-gate.py`. Round 27 pinned it (`b5406bcd…`) inside
`reports/round-27/law/impl-1.md`; it is unchanged at
`b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb` — verified:

```
$ sha256sum tools/gates/argot-derivation-gate.py
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
$ python3 tools/gates/argot-derivation-gate.py --selftest | tail -1
selftest: 27/27 checks passed
```

**Stable, and its selftest is green at 27/27.** But the *other* instrument the
ceiling depends on — the gate's `is_legal_syllable` predicate and the reading of
it — is not a pinned contract; it is a function whose docstring says "Is **one
syllable** of the template" while the round-27 measurement applied it to whole
words (D20 §2 measures the consequence). Recorded as **D19-F2**: the ceiling's
number is a function of *how a public predicate is applied*, and neither round
pinned the application, only the file.

## 8. Named findings

| id | finding | severity | evidence | disposition |
|---|---|---|---|---|
| **D19-F1** | the A/B's design authority (`reports/round-27/law/design.md`) is quoted by digest in three round-27 files and moved twice inside round 27; no round-28 row records the stale quote | low | §6 | reported |
| **D19-F2** | the ceiling's number depends on the *application* of `is_legal_syllable` (a per-syllable predicate applied to whole words), which no round pinned — only the file | medium | §7 | reported; D20 measures it |
| **D19-F3** | `packet_family()` reads the family from the packet path's **parent directory name**; the same unmodified packet reads 12 or 16 findings depending only on its parent directory, manufacturing a four-finding phantom delta that looks like Route B's cost | **medium** — a latent false-positive in the lane's A/B instrument | §4 | reported; round 27's filed probes are sound (family-named layout) |
| **D19-F4** | the A/B headline numbers are width-dependent (4-row probe = 16, 1-row probe = 13); round 27 stated the width but the filed tables do not carry it beside the number | low | §2 | reported |

**Not findings — cross-checks that pass.** Three things this seat verified and
found sound:

1. **The A/B's decision holds on the amended bytes** (§1): Route A adds zero
   holds, Route B costs one per row, baseline unchanged at 12.
2. **Round 27's probes are sound** (§4): they used the family-named layout
   `.scratch/r27-law/{A,B}/culture-d4/`, so the phantom-delta hazard is latent
   and not realised in the filed measurement.
3. **The re-pin discipline is intact** (§5): the sweep enumerates 121 surfaces
   and 31 drifted before re-pinning, and the runner refuses rather than silently
   re-points.

## 9. What round 28 should owe, cross-checked

| # | item | owner | why |
|---|---|---|---|
| X-1 | re-pin the two live channels (`typed-pipelines.json` d4 packet, `expected-holds.json` packet) to `543d68a8…` as **new rows**, with the round-28 command and date | the O seat | §5; the runner's claim O is red on exactly this |
| X-2 | add the family-named-path precondition to the A/B recipe, or make `packet_family()` fall back to the packet's own `assembly.generator` (which already names `tools/assemble-culture-d4.py`) instead of the directory name | a tool seat | `D19-F3`; the generator string is the reliable signal and is already in the packet |
| X-3 | record the probe width beside every A/B count in the round-28 report | the D seat | `D19-F4` |
| X-4 | pin the *application* of `is_legal_syllable` (per-syllable vs whole-string) in the ceiling's citation, not only the file digest | the C seat | `D19-F2`, `D19-F1` |

## 10. Independence and controls

- **The A/B probes are rebuilt here** as text transforms of the delivered bytes
  at block boundaries, never re-serialisations; the two probe digests
  (`d4f7193d559a…`, `e6938d2609c7…`) are reported so a reader can re-derive
  them.
- **The family-resolution hazard is measured with its own control**: the same
  unmodified packet is copied to two parent directories and read twice (§4),
  which isolates the directory name as the only variable.
- **The four-row probe is run to reconcile the width discrepancy** (§2) rather
  than asserted; the discrepancy is then explained by the measurement, not by
  argument.
- **The pins are read from the live files** (`typed-pipelines.json`,
  `expected-holds.json`) and compared to `sha256sum`, never taken from a report.
- **All probes live under `.scratch/r28-d19/`**, gitignored. No tracked byte was
  written; the two in-tree packets the probes compare against are read-only.

**Write scope honoured:** this file, plus `.scratch/r28-d19/`. No component,
packet, tool, gate, fixture, pin, runner or filed round-8–27 byte was written.
No commit, no push.
