# R28-D08 — RL-4: the `packet_keys` declarations and the records that reach the packet

- **Seat:** R28-D08 (D axis, law-replay implementation 4 of 8). Round 28, loop 3
  build 4 of 4, claim **D** `register-law-replay`. Integrator: `impl-1.md`.
- **Date:** 2026-10-18. Baseline `6c0ac448…`; lane HEAD `69cecbc`.
- **Files written:** `examples/culture-d4/components/03-orthography.yml`,
  `examples/culture-d4/components/09-costumes.yml`.
- **Write scope:** this file only; scratch under `.scratch/r28-d/`.
- **Canon:** NON-CANON engineering evidence.

## 0. The gap, in round 27's words

> "**`03-orthography.yml` declares no top-level `packet_keys`**, so the assembler
> falls back to the `PACKET_KEYS` allowlist … **OR-01/OR-02/OR-03** (the
> `records` block) and **LI-01..LI-03** (the `literacy_institutions` block) are
> not packet records. … `09-costumes.yml`'s `enforcement` key is not in its
> `packet_keys`. … **EN-01/EN-02** … are **component-only** as well."
> — `reports/round-27/law/review.md` §5 (RL-4)

The assembler's rule is exact (`tools/assemble-culture-d4.py:258-264`): a
component's own top-level `packet_keys` list, **when declared**, fixes that file's
packet contribution exactly; otherwise the `PACKET_KEYS` allowlist applies and
everything else is recorded under `assembly.skipped_keys`. So a block can be legal
in the component and invisible to every gate that reads the packet.

## 1. The two declarations, and the reasoning recorded with each

Both edits are one line plus a comment explaining the choice, so a reader can
disagree with the *scope* rather than reconstruct it.

**`03-orthography.yml`:**

```yaml
packet_keys: [orthography, records, literacy_institutions]
```

**`09-costumes.yml`:**

```yaml
packet_keys: [costumes, materials, cloth_sources, rank_rules, form_slots, enforcement]
```

## 2. What was deliberately left component-only

Widening the packet surface is a decision, not a side effect, so the exclusions
are named rather than implied:

| file | block | left out because |
|---|---|---|
| `03-orthography.yml` | `signs`, `orthography_rules`, `numeral_register` | no delivered record cites them by id; adding them widens the packet surface with no consumer |
| `03-orthography.yml` | `lexicon_requests`, `consistency_checks` | component-side bookkeeping, not packet content |
| `09-costumes.yml` | `legibility`, `rank_rules_note` | prose notes; `rank_rules` itself already rides |

`orthography` stays declared (it was the allowlist's one hit for that file) and
`costumes`/`materials`/`cloth_sources`/`rank_rules`/`form_slots` stay declared on
09. The change is therefore **purely additive at two addresses**.

## 3. The records now reach the packet, measured

```
$ export TMPDIR=$PWD/.scratch
$ python3 - <<'PY'
… records                 skipped=None  in_packet=True
… literacy_institutions   skipped=None  in_packet=True
… enforcement             skipped=None  in_packet=True
… signs                   skipped=['examples/culture-d4/components/03-orthography.yml']  in_packet=False
OR ids in packet: ['OR-01', 'OR-02', 'OR-03']
LI ids in packet: ['LI-01', 'LI-02', 'LI-03']
EN ids in packet: ['EN-01', 'EN-02']
PY
```

The round runner's own RL-4 measurement, read back from the receipt:

```
"record_locations": {"EN-01": "enforcement", "EN-02": "enforcement",
                     "LI-01": "literacy_institutions", …, "OR-01": "records", …}
"records_absent": []
"still_skipped": {}
```

**Eight of eight ids ride a list block whose rows are mappings carrying that
`id`** — not prose cross-references. That is the second half of RL-4's definition
("the records must be present in the packet **as records**"), and the runner
measures it that way on purpose.

## 4. Why this fix and the replay leg land together

The replay leg's **speaker** resolution resolves agent ids against delivered
records. `RGL-01`'s `speaker` carries `mold-keeper (OR-02, component-only)`, and
round 27 measured `OR-02` as absent from the packet.

So the two halves of this claim are **not independent**:

- before the RL-4 fix, a speaker resolution over `OR-02` would have reported a
  defect **caused by the packet's own blindness** — the id is legal in the
  component and simply never arrived;
- after it, `OR-02` is a packet record, the resolution reads true
  (`speaker_tokens=3`, `speaker_failures=0`), and it fires on a genuinely
  unresolvable id such as `(ZZ-99)`.

This is recorded because it changes what the fix *means*: RL-4 was filed as a
citation-hygiene defect, and closing it is what makes the law's speaker clause
checkable at all. The gate could not have been written honestly before it.

## 5. The blast radius, and what it did *not* move

The fix moves the packet, so it moves every artifact generated from it. What it
did **not** move is the important half:

| surface | moved? | measured |
|---|---|---|
| `packet.d4.yml` | yes | `86079a67…` → `543d68a8…` (98,841 bytes, +8 records, +3 blocks) |
| `typed-labels.d4.yml`, `packet.d4.typed.yml` | yes (regenerated) | see `impl-5.md` |
| the hold set's **counts** | **no** | 12 holds / 0 notes / 0 fails, unchanged from round 22 |
| `tools/d2-typed-labels.py` | **no** | unchanged; the standalone leg touches no projector byte |
| `tools/gates/typed-pipeline-gate.py` | **no** | unchanged, and still GREEN in the filed round-26 manifests |
| the argot derivation leg | **no** | `violations=0 rule_holds=0` before and after |
| the four sibling culture gates | **no** | naming 14, phonology 1, myth 0, costume 0 — identical before and after |

The hold set's counts are unchanged **because a law row is not a form**: the six
garment-form obligations still route to their twelve record/slot rows, and the
register stratum owes no form slot. The pins moved; the obligations did not.

## 6. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
grep -n "packet_keys" examples/culture-d4/components/03-orthography.yml examples/culture-d4/components/09-costumes.yml
python3 -c "import runpy;n=runpy.run_path('tools/gates/naming-collision-gate.py');p=n['load_yaml'](open('examples/culture-d4/packet.d4.yml').read());print({k:[r['id'] for r in p[k]] for k in ('records','literacy_institutions','enforcement')});print({k:v for k,v in p['assembly']['skipped_keys'].items() if any('orthography' in x or 'costumes' in x for x in v)})"
python3 reports/round-28/run-validation.py --check | python3 -c "import json,sys;print(json.load(sys.stdin)['claims']['D']['measurement']['rl4'])"
sha256sum examples/culture-d4/components/03-orthography.yml examples/culture-d4/components/09-costumes.yml
```
