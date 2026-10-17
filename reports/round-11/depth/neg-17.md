# R11-D17 — negative: a translated label smuggled onto the sound channel (run receipts)

- round: 11 (loop 1 of 3, build round 4 of 4) · shard: **D17** (negative examples,
  claim D `d2-typed-pipeline`) · owner: L2 worker, kotodama-shokunin lane
- assignment (verbatim): "DEPTH R11-D17 (negative): smuggle a translated label
  onto the sound channel in a scratch packet; wiring must catch it;
  reports/round-11/depth/neg-17.md."
- date: 2026-10-17 (stamps UTC; local = UTC-3). Baseline revision
  `94ca098b8ab03be52ec80f6925538e5e2c0ed327` (`reports/round-11/claims.json:5`);
  working-tree HEAD at write time `e3ef171`.
- canon: NON-CANON engineering evidence. The fixtures are synthetic controls;
  nothing here is a culture design, a canon record, a handoff, or a claim about
  any real language or a real-world rights question.
- writes: **this file only** plus in-lane scratch under `.scratch/r11-d17/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command; `/tmp` is
  inode-exhausted on this host). No tool, gate, packet, component, baseline,
  manifest or earlier-round byte is edited by this seat; `reports/round-{8,9,10}/**`
  and `tools/gates/{frozen,expected}/**` are filed and read-only here. No commit,
  no push.
- **status: complete.** The wiring (`tools/typed-gate-flow.py`, the landed R11-D05
  adapter) was run over the live example and over all four smuggle fixtures; every
  fixture is caught (§4). The full matrix was run at **three** wiring revisions —
  `ae55e6fa…`, `a7e1224f…`, `5758e315…` — and every receipt came out
  **byte-identical** across all three (the peer was editing the tool while this
  shard ran; §6 has all pins). Tool sha256 at close: `5758e315…`.

## 1. The mechanism, and the smuggle

Claim D wires the round-8 typed-label projection into the D2 gate flow: translated
labels must never enter the sound channel, and the owed native forms must be
carried as named holds (`D2L-FORM-UNRESOLVED`, one per slot), replacing the ten
legacy `PHON-INVENTORY` FAILs. The design (`reports/round-11/depth/design.md`)
proposed two files and fixed my control in its §6 table, verbatim:

> **D17 — gloss smuggled onto the sound channel** | typed packet where a
> `typed_channel` record's gloss is left in its checked field (`garment`,
> `case`-equivalent of §1.3 experiment 1) | must be caught by **L2** | a typed-run
> finding line names an off-channel record (`PHON-INVENTORY` for `GAR-0N`) →
> channel violation, exit 1. (`design.md:392`)

The landed wiring is one tool, `tools/typed-gate-flow.py` (docstring: "R11-D05"),
whose adapter step marks every costume record whose typed label kind is
`translated-label` with `compare_only: true` in the *derived* typed packet (the
naming gate's own declared key-equivalence channel,
`naming-collision-gate.py:223`) and names the owed slot in `owed_form`
(e.g. `LEX-GAR-01`); the gate bundle is then run over the derived packet with five
checks that decide exit 0:

| check | question it answers |
|---|---|
| `sound-channel-clean` | no `PHON-*` artifact in the typed run names an off-channel record (the design's L2) |
| `differential-exact` | legacy findings − typed findings = exactly the off-record `PHON-INVENTORY` removals, nothing added |
| `owed-slots-crosscheck` | every declared `owed_form` has a named hold, and every hold names a declared slot |
| `hold-set-equal` | the full finding set equals the committed expected set (15 holds + 1 note, 0 fails) |
| `typed-packet-pinned` / `expected-*` | the derived artifacts byte-match the committed ones |

**Catch criterion.** A caught variant is one where the wired run does **not**
exit 0 with findings exactly equal to the expected hold set. The fixtures exercise
both surfaces of the sound channel — the typed channel (a gloss re-declared as a
supplied form, cases 17a/17b) and the field channel (the gloss left in/restored
to `costumes[].garment`, cases 17c/17d) — plus the wiring-level injection of the
same fault into the derived typed packet.

## 2. Fixtures and controls (scratch, byte-pinned)

All fixtures are byte-deterministic derivations of the live tree; hashes are
`sha256sum` of the file as run (2026-10-17T22:04–22:19Z). Source bytes:
`examples/culture-d2/packet.d2.yml` sha256
`e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643`.

### 2.1 Raw-packet fixtures (`--packet` input)

| id | fixture (`.scratch/r11-d17/…`) | sha256 | injected smuggle | control |
|---|---|---|---|---|
| **17a** | `packet-smuggle-17.yml` | `8cc436f5…cac4f04a` | hand-authored `typed_labels` entry: GAR-01's own English gloss declared `kind: native-form`, `status: supplied`, slot `LEX-GAR-01` — the translated label moved onto the checked channel | live packet |
| **17b** | `packet-smuggle-17b.yml` | `4a8f3432…d655762e` | same shape, text `sara mela` — inventory-clean, so only the slot debt betrays it (a smuggler who reads the phonology first) | live packet |
| **17c** | `packet-smuggle-17c.yml` | `9c9b1063…6d44bb7de` | routed view (ten `garment:` → `garment_gloss:`) **plus** GAR-01's gloss restored to `garment:` — the checked field refilled behind the routing (design-era shape) | `packet-routed-control.yml` `f049bbff…bdede20d` |
| (adjacent probe, D20's SC-1 direction) | `packet-compareonly-raw.yml` | `1ef7387b…9946525f` | `compare_only: true` inserted on the raw GAR-01 record — the mirror smuggle (a record smuggled *off* the channel by the raw author) | live packet |

### 2.2 The wiring-level fixtures (typed packet, `--typed-override` input)

| id | fixture | sha256 | injected smuggle |
|---|---|---|---|
| **17d** | `typed-tamper-17d.yml` | `835fef57…2e1d365a` | GAR-01's `compare_only: true` flipped to `false` in the derived typed packet — the translated label **forced back onto the sound channel** (single changed byte range, offset 92747; `owed_form: "LEX-GAR-01"` retained) |
| control | `derived-typed.yml` | `e8a83445…4e09bb` | the derivation itself — byte-identical to the committed `examples/culture-d2/packet.d2.typed.yml` (verified `cmp`, §4) |

The design-era `typedpacket-tamper.yml`/`typedpacket-ok.yml` pair (§3.3) is kept
as the design-shaped reproduction; the landed wiring's equivalent injection is
the `compare_only` flip above (the landed adapter routes by `compare_only`, not by
the design draft's `garment_gloss` rename — reported as an observation, §5).

## 3. Pre-wiring baseline (kept as the module-level evidence)

Tool pins at these runs: `tools/d2-typed-labels.py` sha256
`0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`;
`tools/gates/naming-collision-gate.py` `d9e4e8f4…`; Python 3.14.7.

### 3.1 Typed channel, case 17a — caught by the projector

```sh
python3 tools/d2-typed-labels.py --packet .scratch/r11-d17/packet-smuggle-17.yml --json   # exit 1
```

- live control: `stats {fail: 0, hold: 15, note: 1, labels: 58}` — the expected
  hold set, GAR-01 held (`run-control.json` sha256 `880d0e45…`).
- 17a: `stats {fail: 2, hold: 14, note: 1, labels: 59}`; the GAR-01 hold is gone
  and verbatim fail lines name the smuggled record (`run-smuggle.json` sha256
  `aeea1100…`; report text `run-smuggle.txt` sha256 `6db3856e…`):

```text
FINDING D2L-NATIVE: [fail] SMUGGLE-GAR-01 — supplied form 'winter valley coat (heavy felted wool; uncombed finish optional)' carries symbols outside the declared inventory: ['(', ')', ';', 'c', 'f', 'v', 'y']
```

(twice: the R4 pair rule and the record's own pass both fire). The declared
inventory is `bdghjklmnprstwʃ` + `aeiou`; the gloss's bytes fail it.

### 3.2 Typed channel, case 17b — the projector alone is silent

`stats {fail: 0, hold: 14, note: 1, labels: 59}` (`run-smuggle-17b.json`, sha256
`31cb9e43…`): zero fails, and GAR-01's owed-form hold is silently gone — the
smuggled costume-owned string cleared the 05-lexicon slot's debt
(`validate_labels` keys supplied forms on `(owner, label_id)` but never verifies
the form's owner is the slot's owner). The wiring must catch what the projector
misses; §4 shows it does.

### 3.3 Field channel, cases 17c/17d-design — the L2 signal, five-gate chain

Five culture gates over each fixture; the other four gates are byte-identical
across every run (`e3b0c442…` empty / `1ce5f0cd…` phonology):

| run | naming-gate findings | `PHON-INVENTORY` |
|---|---|---|
| routed control (17c control) | 7 | **0** |
| 17c (gloss restored to `garment`) | 8 | **1** — names `GAR-01` |
| `typedpacket-ok.yml` (17d-design control) | 7 | **0** |
| `typedpacket-tamper.yml` (gloss left in checked field) | 8 | **1** — names `GAR-01` |

The added line (`typedrun-tamper-naming.txt`, sha256 `8b0e8c16…`):

```text
FINDING PHON-INVENTORY: FAIL — name GAR-01 'winter valley coat (heavy felted wool; uncombed finish optional)': symbol /v/ at position 7 is not in the declared inventory …
```

Independent corroboration: the untampered typed run's naming-gate stdout sha256
`feb6488127f115f986bf7602c0b074ce911c951751e5e2c63e32e5d23bb52bd9` is byte-equal
to the design's own `.scratch/d01/allrouted-naming-collision-gate.out` hash
(`design.md:76`). Two seats, two procedures, same bytes.

## 4. Wired-pipeline re-run — all four variants caught

The matrix below was run at three wiring revisions (`ae55e6fa…`, `a7e1224f…`,
`5758e315…`; tool file was being edited by its owner between runs). **Every
receipt is byte-identical across the three revisions** — the sha256 shown per
receipt is the single hash all three runs produced (files `*-rev3.txt` are the
last-run copies). Python 3.14.7; lane root; `TMPDIR=$PWD/.scratch`.

### 4.1 Positive control and the wiring's own selftest

```sh
python3 tools/typed-gate-flow.py                 # exit 0; findings 16 (hold 15, note 1); 10/10 checks
python3 tools/typed-gate-flow.py --selftest      # exit 0; selftest: 14/14 checks passed
```

Positive run (`wiring-run-rev3.txt`, sha256 `204857cb…`; same bytes as
`wiring-run-rev2.txt` and `wiring-run3.txt`): all ten checks `ok`, including
`hold-set-equal`, `expected-pins`, `expected-delta-match`, `expected-verdicts-match`,
`expected-file-current`; `delta: 10 PHON artifact(s) retired, 0 added`; the banner
names the semantics (exit 0 = findings equal the frozen expected set). Selftest
(`wiring-selftest-rev3.txt`, sha256 `d423df1c…`), 14/14 including the wiring's own
smuggle / dropped-owed-form / laundered-hold / malformed controls.

### 4.2 17a — English gloss declared as a supplied native form

```sh
python3 tools/typed-gate-flow.py --packet .scratch/r11-d17/packet-smuggle-17.yml   # exit 1
```

`summary: 5/10 checks passed` (`wiring-17a-rev3.txt`, sha256 `8818e6cc…`);
failed checks:

- `owed-slots-crosscheck` — declared owed slots `[LEX-GAR-01…LEX-GAR-10]` vs
  holds `[GAR-02…GAR-10]` — **the LEX-GAR-01 debt is in the declaration and has
  no hold**: the catch names the smuggled slot exactly;
- `hold-set-equal` — observed 17 findings, expected 16 (the two `D2L-NATIVE`
  fails plus the lost hold);
- plus the three pin checks (`typed-packet-pinned`, `expected-pins`,
  `expected-file-current`) — the derived packet no longer byte-matches the
  committed one.

### 4.3 17b — inventory-clean laundered slot (the projector's blind spot)

```sh
python3 tools/typed-gate-flow.py --packet .scratch/r11-d17/packet-smuggle-17b.yml   # exit 1
```

`summary: 5/10 checks passed` (`wiring-17b-rev3.txt`, sha256 `a6401cdf…`): the
same `owed-slots-crosscheck` failure (LEX-GAR-01 owed, no hold) and
`hold-set-equal` (observed 15 findings, expected 16). **The wiring covers the
projector's silent case**: no fail is needed; the exact-set comparison and the
owed-slot cross-check both trip.

### 4.4 17d — the canonical injection: gloss forced back onto the sound channel

Shadow derivation (never writes lane paths):

```sh
python3 tools/typed-gate-flow.py --typed-packet .scratch/r11-d17/derived-typed.yml \
    --expected .scratch/r11-d17/derived-expected.json --emit
cmp .scratch/r11-d17/derived-typed.yml examples/culture-d2/packet.d2.typed.yml   # byte-identical
# single-line tamper: GAR-01's "compare_only: true" -> "compare_only: false" (byte offset 92747)
python3 tools/typed-gate-flow.py --typed-override .scratch/r11-d17/typed-tamper-17d.yml   # exit 1
```

`summary: 4/10 checks passed` (`wiring-17d-rev3.txt`, sha256 `c12a4f98…`); the
failures include the exact L2 signal the design requires:

```text
FAIL sound-channel-clean — PHON artifacts naming translated labels: ["naming-collision-gate.py: FINDING PHON-INVENTORY: FAIL — name GAR-01 'winter valley coat (heavy felted wool; uncombed finish optional)': symbol /v/ at position 7 is not in the declared inventory …"]
FAIL differential-exact — removed 9, off-records 10
```

plus the four expected-set checks (`expected-pins`, `expected-delta-match`,
`expected-verdicts-match`, `expected-file-current`) since the tampered typed
packet's sha differs. The channel violation is named by record (`GAR-01`) and by
gate (`naming-collision-gate.py`) — not a bare nonzero exit.

### 4.5 Adjacent probe (reported, not the D17 smuggle)

`packet-compareonly-raw.yml` (raw author marks a record `compare_only`):
`--packet` → exit 1, `differential-exact` FAIL (`removed 9, off-records 10`) —
the mirror direction is caught too (`wiring-compareonly-raw.txt`, sha256
`f56355f7…`, first-pass run). This is the control `design-review.md` §4
(DR-07/SC-1) asks for.

## 5. Dispositions, observations, limits

- **Verdict: all four D17 variants are caught by the wired flow**, with the same
  verdicts at all three observed wiring revisions. 17a/17b at the raw-packet
  input via `owed-slots-crosscheck` + `hold-set-equal` (17a additionally already
  at the projector, §3.1); 17d at the typed-packet injection via
  `sound-channel-clean` + `differential-exact`. The assignment's "wiring must
  catch it" is satisfied with named, record-addressed catches, not bare exits.
- **The projector's blind spot is closed in the flow, not in the projector.**
  17b is invisible to `d2-typed-labels.py` alone (§3.2) yet caught by the wiring
  (§4.3). No defect is filed against the wiring for this; the projector-level gap
  stays on record as D06's F-D06-1 class territory.
- **Observation O-D17-1 (for D05/D20, evidence, not a filed defect):** the wiring
  selftest's "smuggle control" injects its tamper as the `--typed-packet` pin
  target, not as the evaluated packet, so in that injection `sound-channel-clean`
  stays `ok` and the control passes on the pin check alone. Reproduced:
  `python3 tools/typed-gate-flow.py --typed-packet
  .scratch/r11-d17/typed-tamper-bin.yml` → exit 1 with `FAIL typed-packet-pinned`
  + `FAIL expected-file-current` but `ok sound-channel-clean`
  (`wiring-typedpacket-path-tamper.txt`, sha256 `78ad78fc…`). The real channel
  detection is exercised by `--typed-override` (§4.4); the selftest could assert
  the failing check id instead of a substring that also appears when the check
  passes.
- **Observation O-D17-2 (timing, not a defect):** at 22:12–22:13Z a mid-edit
  revision (`c0928a6d…`) was red — `expected-present` looked for
  `typed-gate.expected.json` while `typed-gate.expected.yml` was being written,
  and its selftest asserted an "owed-form holds" marker. The peer's later
  revisions closed it; the mid-flight run is not counted as evidence either way.
- **Mechanism note (report to the reviewers, not absorbed):** the landed adapter
  routes by `compare_only` marking inside the derived packet, while `design.md`
  §2.3/§6 describes a `garment_gloss` rename with a `typed_channel` table; and
  `design-review.md` DR-07 warns the `compare_only` skip is *silent* (no finding)
  when misused. The wiring compensates with `owed-slots-crosscheck`,
  `differential-exact` and `hold-set-equal` — measured here — but the mechanism
  delta and the DR-07 risk belong to the D20 reviewer and the D05 owner.
- **Limits.** Fixtures are scratch-only; no lane path was written by this shard.
  The fixtures' generation commands are in-tree reproducible (§6); the `--emit`
  scratch derivation is byte-identical to the committed typed packet at the
  tested revisions and will drift if D05/D06 re-emit — re-derive, never force the
  hash. The catch evidence is pinned to `5758e315…` and reproduced at `ae55e6fa…`
  and `a7e1224f…`; any later wiring edit is a re-read event. Canon status of the
  ten owed garment forms is lore's, not this lane's.
- Out of lane (report, never absorb): filed earlier-round artifacts modified in
  the worktree during this round (`reports/round-10/coverage/index-update-22.md`,
  `reports/round-{5,6,7,8,9}/validation.json`; `git status --short`) are other
  seats' writes; the orchestrator decides.

## 6. Reproduction and receipts

Generation (from the lane root, `TMPDIR=$PWD/.scratch`):

```sh
# 17a/17b: byte copy + a typed_labels block inserted before `costumes:`
#   (17a text: GAR-01's garment string; 17b text: "sara mela")
# 17c: ten `    garment: ` -> `    garment_gloss: ` renames, then GAR-01's garment line re-inserted
# 17d: --emit into scratch, then one byte run `compare_only: true` -> `compare_only: false` (first occurrence)
python3 tools/typed-gate-flow.py --typed-packet .scratch/r11-d17/derived-typed.yml \
    --expected .scratch/r11-d17/derived-expected.json --emit
```

Receipts (all `.scratch/r11-d17/`; `rev3.txt` copies are the last-run files, and
each hash below is the single value all three wiring revisions produced —
byte-identical receipts):

| receipt | sha256 |
|---|---|
| `run-control.json` (live projector) | `880d0e45…` |
| `run-smuggle.json` / `run-smuggle.txt` (17a projector) | `aeea1100…` / `6db3856e…` |
| `run-smuggle-17b.json` (17b projector) | `31cb9e43…` |
| chain `*-naming-collision-gate.txt` (routed control / 17c) | `feb64881…` / `8b0e8c16…` |
| `typedrun-ok-naming.txt` / `typedrun-tamper-naming.txt` | `feb64881…` / `8b0e8c16…` |
| `wiring-run-rev3.txt` (+ `-rev2`, `-run3`) — positive, 10/10 | `204857cb…` |
| `wiring-selftest-rev3.txt` (+ `-rev2`, `-selftest2`) — 14/14 | `d423df1c…` |
| `wiring-17a-rev3.txt` (+ rev2/rev1 twins) | `8818e6cc…` |
| `wiring-17b-rev3.txt` (+ rev2/rev1 twins) | `a6401cdf…` |
| `wiring-17d-rev3.txt` (+ rev2/rev1 twins) | `c12a4f98…` |
| `wiring-compareonly-raw.txt` | `f56355f7…` |
| `wiring-typedpacket-path-tamper.txt` | `78ad78fc…` |
| `typed-tamper-17d.yml` / `derived-typed.yml` | `835fef57…` / `e8a83445…` |
| hash-index files: `receipt-hashes.txt` / `typedpacket-hashes.txt` / `rev2-hashes.txt` / `rev3-hashes.txt` / `tool-sha.txt` | `61430db2…` / `7c4779d8…` / `50ec8842…` / `bf77ad69…` / `f685f0e2…` |
| wiring tool `tools/typed-gate-flow.py` (three observed revisions) | `5758e315…` (close) / `a7e1224f…` / `ae55e6fa…` |

Poll record: wiring files absent 22:07:28Z–22:10:36Z (`ls tools/ | grep -i typed`
→ only `d2-typed-labels.py`); `tools/typed-gate-flow.py` appeared 22:11:55Z;
revisions observed: `c0928a6d…` (mid-edit, red, 22:12–22:13Z), `ae55e6fa…`
(green, first full pass), `a7e1224f…` (green, second full pass), `5758e315…`
(green, third full pass 22:19Z; unchanged at close 22:19:00Z).

## 7. Sources

- `tools/typed-gate-flow.py` `5758e315…` / `a7e1224f…` / `ae55e6fa…` — mechanism,
  checks, selftest, CLI; `tools/d2-typed-labels.py` `0da0015f…` (`SOUND_KINDS`,
  `validate_labels`, `check_sound_form`); `tools/gates/naming-collision-gate.py`
  `d9e4e8f4…` (`:670` costume channel reading)
- `reports/round-11/depth/design.md` (§2.2 adapter, §3.1 L1–L4, §4 expected hold
  set, §6 D17 row `:392`); `reports/round-11/depth/design-review.md` (DR-07/SC-1)
- `reports/round-11/depth/shard-holds.md` (D06; TL-01 → `D2L-FORM-UNRESOLVED`,
  projector gaps F-D06-1/2); `reports/round-8/depth/skill-table-draft.md` (T1
  routing, §7 limits)
- `examples/culture-d2/packet.d2.yml` `e0f21509…`;
  `examples/culture-d2/packet.d2.typed.yml` `e8a83445…`;
  `examples/culture-d2/typed-gate.expected.json` `e962849a…`;
  `reports/round-11/claims.json`
- Scratch receipts as tabled above, `.scratch/r11-d17/**`
