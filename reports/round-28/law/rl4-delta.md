# R28-D03 — the RL-4 fix, priced: the packet delta, the pin cascade, and the two records that still do not land

- **Seat:** R28-D03 (D axis, law-replay design 3 of 4), round 28, loop 3 build 4
  of 4. Claim **D** `register-law-replay` (`reports/round-28/claims.json`).
- **Date:** 2026-10-18 (measurements 20:0x–20:15Z). Baseline revision
  `69cecbc7dcf575a29f29660ecac470e05260fd86`; lane HEAD `69cecbc`.
- **Design authority:** `reports/round-28/law/design.md` §3.2 (the `mold-keeper`
  resolution); `reports/round-27/law/review.md` §5 (RL-4, the finding this file
  prices).
- **Write scope:** this file only; scratch under `.scratch/r28-law/`.
  `export TMPDIR=$PWD/.scratch` preceded every scratch-writing command. **This
  seat wrote no component, packet, pin, tool, or gate byte** — the fix it prices
  was landed by a sibling seat inside the measurement window, and this file
  records that fact rather than claiming the landing.
- **Canon:** NON-CANON engineering evidence. No real language, institution or
  script is described, cited or approximated.

**Verdict in one line.** The RL-4 fix **has landed** (`03-orthography.yml` and
`09-costumes.yml` gained `packet_keys` at 17:13Z, packet `86079a67…` →
`543d68a8…`), and it lands exactly the eight records round 27 named — but it
**leaves two sibling blocks deliberately component-only**, it does **not** move
the hold set (12/0/0 unchanged), and it leaves a **four-site pin cascade** the O
sweep still owes. The packet delta is `+2,286 bytes`, `+8` records, `+3` new
blocks, `−3` `skipped_keys` entries.

## 0. What RL-4 was, and what "fixed" means

Round 27's review named it:

> "**`03-orthography.yml` declares no top-level `packet_keys`**, so the assembler
> falls back to the `PACKET_KEYS` allowlist … **OR-01/OR-02/OR-03** (the
> `records` block) and **LI-01..LI-03** (the `literacy_institutions` block) are
> not packet records. … `09-costumes.yml`'s `enforcement` key is not in its
> `packet_keys`. … **EN-01/EN-02** … are **component-only** as well."
> — `reports/round-27/law/review.md` §5

"Fixed" therefore has two independently checkable halves, and this file measures
both:

1. **the components declare the keys** — a `packet_keys` list on each of the two
   files naming the blocks their records live in; and
2. **the records reach the packet as records** — each of the eight ids
   `OR-01..03`, `LI-01..03`, `EN-01..02` present in a list block whose rows are
   mappings carrying that `id`.

## 1. Half one — the declarations, measured

**Pre-fix**, reconstructed on a clean clone from `HEAD`'s component bytes:

```sh
$ git show HEAD:examples/culture-d4/components/03-orthography.yml | grep -c "^packet_keys:"
0
$ git show HEAD:examples/culture-d4/components/09-costumes.yml | grep "^packet_keys:"
packet_keys: [costumes, materials, cloth_sources, rank_rules, form_slots]
```

`03-orthography.yml` declares **none at all**; `09-costumes.yml` declares a list
that omits `enforcement`. The clone's re-assembly from those two bytes
reproduces the round-27 packet digest **exactly**, which is what makes the
pre-fix baseline trustworthy rather than reconstructed-by-argument:

```sh
$ cd .scratch/r28-law/pre && python3 tools/assemble-culture-d4.py >/dev/null
$ sha256sum examples/culture-d4/packet.d4.yml
86079a6708a0d360bedfed60306274c09ec4f4e76a5912b94a05f762d17caebc
```

**Post-fix** (landed by a sibling seat at 17:13Z, not by this one):

```yaml
# examples/culture-d4/components/03-orthography.yml:24
packet_keys: [orthography, records, literacy_institutions]

# examples/culture-d4/components/09-costumes.yml:22
packet_keys: [costumes, materials, cloth_sources, rank_rules, form_slots, enforcement]
```

| file | pre-fix `packet_keys` | post-fix | bytes |
|---|---|---|---|
| `03-orthography.yml` | **absent** | `[orthography, records, literacy_institutions]` | 14,035 → 14,989 |
| `09-costumes.yml` | `[costumes, materials, cloth_sources, rank_rules, form_slots]` | `+enforcement` | 12,047 → 12,535 |

**The declaration is deliberately narrow, and the sibling's own comment says
why** (`03-orthography.yml:13-23`): `signs`, `orthography_rules`,
`numeral_register`, `lexicon_requests` and `consistency_checks` stay
component-only because "no delivered record cites them by id, and widening the
packet surface is a separate decision". §3 measures the consequence of that
choice — it is the honest part of the fix and it is also where the residual gap
is.

## 2. Half two — the records, measured

**The id-level delta**, measured with `grep -c` over the pre-fix clone's packet
and the live packet:

| id | block | pre-fix hits | post-fix hits | reading |
|---|---|---|---|---|
| `OR-01` | `records` | 1 | 2 | was prose-only (in `ER-01`'s text), now also a record |
| `OR-02` | `records` | 2 | 3 | was prose-only, now also a record |
| `OR-03` | `records` | 2 | 3 | was prose-only, now also a record |
| `LI-01` | `literacy_institutions` | **0** | **1** | **was absent entirely** |
| `LI-02` | `literacy_institutions` | **0** | **1** | **was absent entirely** |
| `LI-03` | `literacy_institutions` | **0** | **1** | **was absent entirely** |
| `EN-01` | `enforcement` | **0** | **1** | **was absent entirely** |
| `EN-02` | `enforcement` | **0** | **1** | **was absent entirely** |

**The block-level delta**:

| block | pre-fix | post-fix |
|---|---|---|
| `records` | absent | 3 rows |
| `literacy_institutions` | absent | 3 rows |
| `enforcement` | absent | 2 rows |

**The `skipped_keys` ledger, which is the mechanism's own receipt**:

```
pre-fix keys: 78   post-fix keys: 75
keys dropped entirely: ['enforcement', 'literacy_institutions', 'records']
packet_keys: 10 files -> 11 files
```

Three keys left the ledger because the blocks they named now reach the packet;
one more file joined the `packet_keys` list (11 of 13 components now declare
their contribution; only `02-phonology.yml` and `01-brief.yml` do not, and both
are deliberately packet-owned or allowlist-served).

**The assembled packet delta**:

| | pre-fix | post-fix |
|---|---|---|
| `packet.d4.yml` | 96,555 B / `86079a67…` | 98,841 B / `543d68a8…` |
| `typed-labels.d4.yml` | 82,161 B / `88a94422…` | 82,161 B / `339bfd83…` |
| `packet.d4.typed.yml` | 102,914 B / `1c4b8808…` | 105,200 B / `15c81ec1…` |

**The projection's byte count is unchanged while its digest moves.** The
projection is a *derived* artifact whose `assembly.packet_sha256` pin names the
packet it was projected from; re-projecting against the new packet rewrites that
one line and nothing else. That is the whole of `339bfd83…`'s delta, and it is
the reason the pin cascade is four sites and not forty.

## 3. The residual gap — two records that still do not land

The fix's own scope comment leaves `signs` component-only. **This seat measured
what that costs**, and the answer is `RL-4`'s shape one level in:

```
$ grep -c '\bSG-\d{2}\b' examples/culture-d4/packet.d4.yml
0
```

`03-orthography.yml`'s `signs` block carries **20 sign records** (`SG-01..SG-20`,
each with `value`, `shape`, `name`, `era`, `origin`, `axis`, `evidence`), and
**not one reaches the packet**. The packet's `orthography` block carries
`signs: "20"` — a **count**, not the records. Measured:

```
orthography block: {'case': 'display-only', 'direction': '...', 'type': '...',
                    'signs': '20', 'scheme': 'D4-roman-1 ...', 'notes': '...'}
```

So the delivered tree's answer to "what are the 20 signs?" is a scalar. **This is
a deliberate scope decision by the sibling seat, and this file records it as a
decision with its cost rather than as an oversight:**

| block | reaches the packet? | why it was left out | what a reader loses |
|---|---|---|---|
| `signs` (20 rows) | **no** | "no delivered record cites them by id" | the sign inventory: 20 records of shape/origin/era become the scalar `20` |
| `orthography_rules` | **no** | same | the writing rules (`WR-*`) |
| `numeral_register` | **no** | same | the E0 count-stamp numeral system |
| `lexicon_requests` | **no** | same | the component's own owed-lexicon asks |
| `consistency_checks` | **no** | same | the component's self-declared checks |

**The `signs` case is the one worth naming**, because the round-27 law *cites
it*: `RGL-04`'s consequence is "a stamp form is inventory-checked exactly as a
plain form", and the sign inventory is the script's side of that. A leg
resolving `RGL-04` against the packet finds the scalar `20` and no records. That
is a real limit on the replay leg this round designs (`LD-*` in `design.md`), and
it is reported here because RL-4's fix is what exposed it.

## 4. The pin cascade, priced

The fix changes the packet digest, so every surface that pins a D4 packet digest
is stale until re-pinned. **Measured, not inferred** — the four sites, with the
digest each currently records:

| # | site | line | records | live | state |
|---|---|---|---|---|---|
| 1 | `tools/gates/typed-pipelines.json` | `:12` `packet.sha256` | `86079a67…` | `543d68a8…` | **stale** |
| 2 | `tools/gates/typed-pipelines.json` | `:20` `projection.sha256` | `88a94422…` | `339bfd83…` | **stale** |
| 3 | `examples/culture-d4/expected-holds.json` | `:3` `packet_sha256` | `86079a67…` | `543d68a8…` | **stale** |
| 4 | `examples/culture-d4/expected-holds.json` | `:4` `projection_sha256` | `88a94422…` | `339bfd83…` | **stale** |

Plus the **two derived artifacts the re-emit already moved** (so the cascade's
downstream half is done):

| # | site | records | state |
|---|---|---|---|
| 5 | `examples/culture-d4/typed-labels.d4.yml` `:9` | `543d68a8…` | **green** (sibling re-emitted) |
| 6 | `examples/culture-d4/packet.d4.typed.yml` `:2791-2792` | `543d68a8…` / `339bfd83…` | **green** (sibling re-emitted) |

**The typed gate's verdict at this stamp is the cascade, named precisely:**

```
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
ok   L3b-argot:
FAIL L1-profile: packet: pins 86079a6708a0, live 543d68a82640 (examples/culture-d4/packet.d4.yml);
                 projection: pins 88a94422b412, live 339bfd83bf66 (examples/culture-d4/typed-labels.d4.yml)
```

### 4.1 The re-emit chain, executed end to end on a clone

The fix's own recipe, run in order on a clean clone
(`.scratch/r28-law/full/`), with the digest at each step:

| step | command | result |
|---|---|---|
| 0 | `git show HEAD:…/03-orthography.yml > …` (restore pre-fix bytes) | `86079a67…` |
| 1 | add `packet_keys` to the two components | — |
| 2 | `python3 tools/assemble-culture-d4.py` | exit 0, `942af77d…` |
| 3 | `python3 tools/d2-typed-labels.py --packet … --emit …` | `d7af2c9f…` |
| 4 | re-point the projection's `assembly.packet_sha256` at the new packet | — |
| 5 | `python3 tools/assemble-d4-typed.py --packet … --projection … --emit …` | `6dbb64b4…` |
| 6 | `check-gate-battery.py`; argot gate; projector | **7 pass / 0 fail**; `violations=0 rule_holds=0`; `findings_total=12` |

**Step 4 is load-bearing and is the step that bites.** `assemble-d4-typed.py`
refuses without it, with a named exit-2 refusal:

```
$ python3 tools/assemble-d4-typed.py --packet … --projection … --emit …
FAIL projection_freshness: stale projection pin: projection records 86079a6708a0…,
     packet hashes 72b6450a9cbc…
assembly error: stale projection pin: …
```

So the chain is **assemble → project → re-pin the projection → re-emit the typed
packet → re-pin the two JSON surfaces**. A worker who runs steps 2–3 and stops
gets a green assembler and a refusing adapter; that is the failure mode this
table exists to prevent.

**The clone's digests differ from the live ones, and the reason is measured.**
The clone's `942af77d…` vs the live `543d68a8…` is **comment text**: the sibling
seat's patch also wrote explanatory `#` comments into the two component files,
and the assembler pins each component's **raw bytes**:

```
live  03-orthography.yml: 0f2ff45439fd7db3  bytes=14989
clone 03-orthography.yml: 26bded0ad70ed006  bytes=14094
```

The same `packet_keys` declarations with different comments produce different
packet digests. **This is worth stating plainly**: a worker reproducing the fix
must reproduce the *comments too*, or the pin cascade lands on a different digest
than the one already recorded in sites 5 and 6. The live digest is the one to
pin against.

## 5. What the fix does *not* change

| surface | measured | reading |
|---|---|---|
| the hold set | `expected-holds.json` `counts {hold: 12, note: 0, fail: 0}` — **unchanged** | the new blocks are not forms, so the six garment-form obligations still route to their twelve rows |
| the projector's findings | `findings_total=12`, `rank_rules_unresolved_items=0` — **unchanged** | the typed leg is inert to `records`/`literacy_institutions`/`enforcement` |
| the argot gate | `violations=0 rule_holds=0` — **unchanged**, but `records=183` (was 170 at round 27) | the register-scoped set is unchanged at 14; the record census grew by the 13 new rows |
| the battery | **7 pass / 0 fail / 0 unevaluable**, exit 0 | green |
| the eight records' own shape | all 8 land as `{id, …}` mappings in list blocks | the mechanism's own check (§2) passes |

**The one honest negative: the fix lands the records but no leg reads them.**
`grep -rl "OR-0\|LI-0\|EN-0" tools/*.py tools/gates/*.py` finds no consumer —
the records are now *present* in the packet and nothing *resolves* against them
yet. That is precisely what the replay leg this round designs would do
(`design.md` §1 resolution 1), and it is why `design.md` and this file are one
claim.

## 6. The delta, in one table

| | before | after | delta |
|---|---|---|---|
| `03-orthography.yml` | no `packet_keys` | `[orthography, records, literacy_institutions]` | +1 declaration |
| `09-costumes.yml` | `[…, form_slots]` | `[…, form_slots, enforcement]` | +1 key |
| `packet.d4.yml` | `86079a67…`, 96,555 B | `543d68a8…`, 98,841 B | **+2,286 B** |
| `typed-labels.d4.yml` | `88a94422…` | `339bfd83…` | pin line only |
| `packet.d4.typed.yml` | `1c4b8808…`, 102,914 B | `15c81ec1…`, 105,200 B | +2,286 B |
| packet blocks | — | `+records`, `+literacy_institutions`, `+enforcement` | **+3 blocks** |
| packet records | — | `OR-01..03`, `LI-01..03`, `EN-01..02` | **+8 records** |
| `assembly.skipped_keys` | 78 keys | 75 keys | **−3 keys** |
| hold set | 12/0/0 | 12/0/0 | **0** |
| projector findings | 12 | 12 | **0** |
| battery | 7/0/0 | 7/0/0 | **0** |
| stale pin sites | 0 | **4** | **+4 (the O sweep's debt)** |

## 7. Named limits

| id | limit | measured |
|---|---|---|
| **LR-1** | the fix leaves five sibling blocks component-only: `signs` (20 records), `orthography_rules`, `numeral_register`, `lexicon_requests`, `consistency_checks` | §3 |
| **LR-2** | the sign inventory is a **scalar** in the packet (`signs: "20"`), and the round-27 law cites it | §3 |
| **LR-3** | the fix's packet digest depends on the **comments** in the component files, not only on the declarations | §4.1 |
| **LR-4** | the projection must be re-pinned **between** projecting and re-emitting the typed packet, or the adapter refuses (exit 2) | §4.1 step 4 |
| **LR-5** | the four pin sites are **stale at this stamp**; the O sweep owes them | §4 |
| **LR-6** | no tool consumes `OR-*`/`LI-*`/`EN-*` yet: the records land and nothing resolves against them | §5 |
| **LR-7** | the fix was landed by a **sibling seat** at 17:13Z, inside this seat's measurement window; this file prices it and does not claim it | header |

## 8. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
# the pre-fix baseline, reconstructed and verified
git show HEAD:examples/culture-d4/components/03-orthography.yml | grep -c "^packet_keys:"
cd .scratch/r28-law/pre && python3 tools/assemble-culture-d4.py >/dev/null && sha256sum examples/culture-d4/packet.d4.yml
# the post-fix state
cd - && sha256sum examples/culture-d4/packet.d4.yml
for id in OR-01 OR-02 OR-03 LI-01 LI-02 LI-03 EN-01 EN-02; do
  printf "%s pre=%s post=%s\n" $id \
    "$(grep -c $id .scratch/r28-law/pre/examples/culture-d4/packet.d4.yml)" \
    "$(grep -c $id examples/culture-d4/packet.d4.yml)"; done
# the residual gap
grep -c '\bSG-\d{2}\b' examples/culture-d4/packet.d4.yml        # 0
grep -n "^packet_keys:" examples/culture-d4/components/*.yml
# the cascade
grep -n "86079a67\|88a94422" tools/gates/typed-pipelines.json examples/culture-d4/expected-holds.json
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml   # FAIL L1-profile
# the full chain, on a clone
cd .scratch/r28-law/full && python3 tools/assemble-culture-d4.py \
 && python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --emit examples/culture-d4/typed-labels.d4.yml \
 && python3 tools/assemble-d4-typed.py --packet examples/culture-d4/packet.d4.yml \
      --projection examples/culture-d4/typed-labels.d4.yml --emit examples/culture-d4/packet.d4.typed.yml
```

### Digests at measurement (`sha256sum`, 20:15Z 2026-10-18)

| artifact | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` (post-fix) | `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f` |
| pre-fix packet, reconstructed on the clone | `86079a6708a0d360bedfed60306274c09ec4f4e76a5912b94a05f762d17caebc` |
| `examples/culture-d4/components/03-orthography.yml` | `0f2ff45439fd7db3e9014bd1012bd917e42d042f457b8cef2bed2c9a791d4e1b` |
| `examples/culture-d4/components/09-costumes.yml` | `f61cc6845518d44f50e5179339a1a2fda2c5290efb52d6badb28cbec87768c23` |
| `examples/culture-d4/typed-labels.d4.yml` | `339bfd83bf66832479b5b8ffbbce708c8be15e13b08967fa7049b848661a3cf8` |
| `examples/culture-d4/packet.d4.typed.yml` | `15c81ec11b42efaa7d683dd9320bfc7cd9b5d1e812e042d99dbf8d8726ec5da6` |
| `examples/culture-d4/expected-holds.json` | `857417e949fb5cb9b265918b8982ca86e47a820d136ba7b009414d84aa4ec28f` |
| `tools/gates/typed-pipelines.json` | `69f250df363d70a2001840ab37f4f947e28244b4ac053a5a79d4a92860822f7a` |
| `tools/assemble-culture-d4.py` | `943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2` |
| `tools/assemble-d4-typed.py` | `92f5460bcc34ffbb43a771504d213d23aafd818b39c7017c823a363e99063fd0` |
