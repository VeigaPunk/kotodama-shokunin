# R11-D10 — test differential: the ten GAR translated labels leave the `PHON-INVENTORY` class

- seat: **R11-D10** (test shard, legacy-vs-typed differential), round 11 (loop 1 of 3, build round 4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D10 (test differential): legacy-vs-typed differential — prove the ten GAR translated labels no longer produce PHON-INVENTORY artifacts; reports/round-11/depth/test-differential.md."
- writes: **this file only** (plus in-lane scratch under `.scratch/r11-d10/`). No tool, gate, packet, projection, baseline, manifest or earlier-round byte was edited; no commit, no push. `reports/round-{8,9,10}/**` were read only.
- canon: NON-CANON engineering evidence. Nothing here admits a round, a capability or a canon fact; no culture, canon or rights claim is made.
- clock: all stamps UTC (`date -u +%FT%TZ`); local time is UTC-03:00.
- lane revision: `git rev-parse HEAD` → `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7` with the round-11 landing uncommitted (sibling seats wrote `tools/**` and `examples/**` while this shard ran — every pin below names its artifact and the stamp it was read).
- **tested revision of the wiring** (the subject of every assertion below): `tools/typed-gate-flow.py` sha256 `5758e315593bb818dbf38c3c3ed7f79eb9ea555955331fadab4b50b2faa92075`, as read 22:18Z; the full assertion set was run against it (`.scratch/r11-d10/differential.json`) and against the earlier revision `ae55e6fa…` (22:13–22:15Z; `.scratch/r11-d10/differential-ae55e6fa.json`) — identical differential outputs on both (the legacy/typed/control stdout digests in §2–§5 are equal across the two runs). The seat revised the tool four times during this shard; the revision watch is §7.6.
- environment: Python 3.14.7, Linux, `export TMPDIR=$PWD/.scratch` before every scratch-writing command; `/tmp` unused. All runs are in isolated mirrors; no lane file is written by any leg.

## 0. Verdict

**The differential holds, with controls.** Over `examples/culture-d2`, the legacy gate flow emits exactly ten `PHON-INVENTORY` FAIL lines, one per `GAR-01..GAR-10`; the typed flow emits **zero**, and the two finding streams differ by exactly those ten lines and nothing else. The ten records are not silenced: each is carried as a named `D2L-FORM-UNRESOLVED` hold, the sound channel still fires on a planted violation on a checked class, and the differential is exactly the wiring (un-marking one record restores its `PHON-INVENTORY` line).

| # | assertion (measured, 22:13–22:18Z; final run on revision `5758e315…`) | result | receipt |
|---|---|---|---|
| A1 | legacy naming run emits exactly 10 `PHON-INVENTORY` lines, all `GAR-01..10` | **pass** | §2.1 |
| A2 | typed run emits zero `PHON-INVENTORY` lines naming a routed record | **pass** | §3.2 |
| A3 | typed naming stream == legacy stream **minus exactly those ten lines** (line-level multiset; 0 added) | **pass** | §4.1 |
| A4 | the ten named `D2L-FORM-UNRESOLVED` holds are present (projector and flow agree, one per owed slot) | **pass** | §3.3 |
| A5 | control: planted out-of-inventory symbol on a checked class (NM-01) still FAILs in the typed run | **pass** | §5.1 |
| A6 | control: un-marking `GAR-01` restores its `PHON-INVENTORY` line — the differential is the wiring | **pass** | §5.2 |
| A7 | flow e2e (`python3 tools/typed-gate-flow.py`) exit 0, 10/10 checks | **pass** (tested revision) | §3.1 |
| A8 | determinism: two adapter builds byte-identical; e2e stdout identical across two runs | **pass** | §6 |
| A9 | the other four culture gates read byte-identical over both packets | **pass** | §4.2 |

## 1. What is proven, and what is not

The claim under test (`reports/round-11/claims.json`, claim D): the ten translated costume
labels "never enter the sound channel and owed native forms are carried as named holds (not
PHON artifacts)". This shard tests the **differential** leg only:

- proven: for `examples/culture-d2`, the typed flow over the typed packet produces no
  `PHON-INVENTORY` line naming any of the ten labels, while the legacy flow produces ten; the
  difference between the two finding streams is exactly those ten lines; the ten records come
  back as named holds; the channel is live (control A5) and the differential is the channel
  marking, not a global silencing (control A6).
- not proven here: that any owed form is *resolved* (they stay owed by design — the holds are
  the point), any canon/culture content, the D3 path, the battery, or other shards' legs. The
  hold-set equality to the committed expected set is the flow's own check (§3.1) and other
  shards' assignment; this shard independently reproduces only the ten-label differential.
- method note: the flow's own `differential-exact` check is **quoted, not trusted** — this
  shard re-runs the five gates itself and computes the line-level multiset difference in the
  mirror (§4, receipts).

### 1.1 The artifact class being removed

The class is the round-4 representation artifact: `tools/gates/frozen/round-4/naming-collision-gate.out`
(sha256 `4d70252bdf7745dea76af07b41a94560b5789ff278cdbb5af4bf6924688bb19e`, re-read 22:15Z)
carries 10 `PHON-INVENTORY` lines and **10 of 10 name English `GAR-*` garment labels**
(`grep -c "PHON-INVENTORY"` → 10; `… | grep -c "GAR-"` → 10, same stamp). The diagnosis is on
record (`examples/culture-d2/ASSEMBLY.md:94`: "the naming gate treats costume garment labels as
entity names and tries to pronounce the supplied English descriptions as D2"; `SKILL.md:42`:
"grading a gloss against native phonotactics manufactures representation artifacts — 10/10 of
the frozen round-4 `PHON-INVENTORY` class are this").

## 2. Legacy side (measured)

### 2.1 Live legacy run

```sh
# 2026-10-17 22:06Z and again 22:13Z, lane root, TMPDIR=$PWD/.scratch
python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml
# exit 1; 17 finding lines: 6 NAME-NEAR + 10 PHON-INVENTORY (GAR-01..GAR-10) + 1 CROSS-HOLD
# stdout sha256 ebc8850d08ec1b7e32616cbca9092ba66f3b6f148a61515a033e6bed6fa66f4b
```

Gate sha256 `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d`
(unchanged all shard; matches `reports/round-8/depth/review-22.md` §2 pre-change digest).
Output sha matches the round-10 drift ledger's recorded row (`reports/round-10/drift/shard-05.md`
row 8, `ebc8850d08ec…`), so this is the same legacy reading the ledger pinned.

### 2.2 Per-label legacy findings (and the frozen class they reproduce)

The live run's ten lines and the frozen round-4 file's ten lines are identical per label in
symbol **and** position (checked programmatically at 22:15Z; `legacy == frozen_r4` for all ten):

| record | legacy live (and frozen round-4): symbol / position | typed disposition (named hold) |
|---|---|---|
| GAR-01 | `/v/` at position 7 | `D2L-FORM-UNRESOLVED` hold — `label_id LEX-GAR-01 has no supplied native/borrowed form` |
| GAR-02 | `/-/` at position 5 | `D2L-FORM-UNRESOLVED` hold — `LEX-GAR-02 …` |
| GAR-03 | `/c/` at position 8 | `D2L-FORM-UNRESOLVED` hold — `LEX-GAR-03 …` |
| GAR-04 | `/-/` at position 8 | `D2L-FORM-UNRESOLVED` hold — `LEX-GAR-04 …` |
| GAR-05 | `/-/` at position 5 | `D2L-FORM-UNRESOLVED` hold — `LEX-GAR-05 …` |
| GAR-06 | `/'/` at position 9 | `D2L-FORM-UNRESOLVED` hold — `LEX-GAR-06 …` |
| GAR-07 | `/c/` at position 9 | `D2L-FORM-UNRESOLVED` hold — `LEX-GAR-07 …` |
| GAR-08 | `/c/` at position 5 | `D2L-FORM-UNRESOLVED` hold — `LEX-GAR-08 …` |
| GAR-09 | `/-/` at position 10 | `D2L-FORM-UNRESOLVED` hold — `LEX-GAR-09 …` |
| GAR-10 | `/(/` at position 12 | `D2L-FORM-UNRESOLVED` hold — `LEX-GAR-10 …` |

(The symbols are exactly the non-inventory characters of the English glosses — `v`, hyphens,
`c`, apostrophe, `(` — i.e. the artifact class; the gate's own inventory is
`{p,t,k,b,d,g,m,n,s,ʃ,r,l,j,w,h}` / `{a,e,i,o,u}`.)

The typed-disposition column names the hold as the flow renders it at the tested revision
(`where` = the owed slot `LEX-GAR-0x`, with the record `GAR-0x` carried in the finding's
`record` field); the projector renders the same holds with `where` = `GAR-0x` (§3.3).

## 3. Typed side (measured)

### 3.1 The flow end-to-end (tested revision `5758e315…`)

```sh
# 2026-10-17 22:18:31Z, lane root, TMPDIR=$PWD/.scratch
python3 tools/typed-gate-flow.py            # exit 0
# stdout sha256 204857cbb84d49cf39b51272651451609fa9a5ad29f4befdc712b07067d1f181
# header lines: packet e0f21509…; typed packet e8a83445…;
#   "sound channel: off=GAR-01,GAR-02,…,GAR-10 on=0 untyped=none"
#   ten "FINDING D2L-FORM-UNRESOLVED: [hold] LEX-GAR-0x (GAR-0x) — label_id LEX-GAR-0x …" lines
#     (quoted: "FINDING D2L-FORM-UNRESOLVED: [hold] LEX-GAR-01 (GAR-01) — label_id
#      LEX-GAR-01 has no supplied native/borrowed form")
# tail: "findings: 16 (hold 15, note 1)"; "summary: 10/10 checks passed"
python3 tools/typed-gate-flow.py --json     # exit 0; stdout sha256 121e8c8ca62d7572bfdcd817f469e4cdae711e4b798964744cd6a7f0eeb69f8b
```

The 10/10 checks: `typed-packet-pinned`, `no-untyped-records`, `sound-channel-clean`,
`differential-exact`, `owed-slots-crosscheck`, `hold-set-equal`, `expected-pins`,
`expected-delta-match`, `expected-verdicts-match`, `expected-file-current`.

### 3.2 The typed packet and the mechanism, as measured

`examples/culture-d2/packet.d2.typed.yml` sha256
`e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb` (read 22:14Z; identical to
this shard's own adapter build, §6). Each of the ten GAR records keeps its `garment` gloss and
gains three fields (10/10 measured; e.g. `packet.d2.typed.yml:1882-1884`):

```yaml
    typed_label_kind: "translated-label"
    compare_only: true
    owed_form: "LEX-GAR-01"
```

The gate skips `compare_only` records from its sound checks at
`tools/gates/naming-collision-gate.py:1154-1155` (also `:1045`, `:1090`, `:1121`), which is the
documented "mechanism-fixture record: key-equivalence checks only" channel (`:93`). The typed
naming run over the typed packet:

```sh
python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.typed.yml
# exit 1; 7 finding lines: 6 NAME-NEAR + 1 CROSS-HOLD; zero PHON-INVENTORY
# stdout sha256 feb6488127f115f986bf7602c0b074ce911c951751e5e2c63e32e5d23bb52bd9
```

### 3.3 The holds (no silent pass)

`python3 tools/typed-gate-flow.py --json` findings census (22:18Z), holds 15 + note 1, fail 0:

- `D2L-FORM-UNRESOLVED` hold ×10, `where` = `LEX-GAR-01..LEX-GAR-10` with `record` = `GAR-01..GAR-10`
  (this is the ten-label exchange; the plain output renders each as `LEX-GAR-01 (GAR-01)`);
- `D2L-NATIVE` hold ×2 at `L-15`, `L-16` (pre-existing, carried unchanged);
- `D2L-RANK` hold ×3 at `TR-04#a|TR-06#a`, `WR-02#g|WR-09#g`, `WR-08#g|WR-09#g`;
- `D2L-RANK` **note** ×1 at `SR-01#a|SR-01#b` (present, not counted as a hold).

The census equals `reports/round-11/depth/design.md` §4.2/§4.3 in ids, wheres and severities for
the non-GAR rows; for the ten GAR rows the flow now addresses the owed slot (`where: LEX-GAR-0x`,
`record: GAR-0x`) where the design table lists `where: GAR-0x` — the committed expected file
`examples/culture-d2/typed-gate.expected.json` (sha256
`7ed597317b32b238d880af0a602fcbfa1ffd92608008879f049db9fd02aa03aa`, read 22:18Z) pins the slot
rendering, and the flow's own `hold-set-equal` passes against it. The projector agrees
independently: `python3 tools/d2-typed-labels.py --json` (lane, 22:13Z) holds
`D2L-FORM-UNRESOLVED` at exactly `GAR-01..GAR-10` (its `where` = record id), and
`python3 tools/d2-typed-labels.py --check` now exits 0 — the projection was re-pinned in-wave to
sha256 `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`, byte-equal to
`design.md` §5.1's prediction. `python3 tools/assemble-d2.py --check` exits 0.

## 4. The differential, computed independently

All legs in an isolated mirror (`.scratch/r11-d10/iso`, `tools/` + `examples/culture-d2/`
byte copies; the legacy input's sha was re-verified inside the mirror:
`packet.d2.yml` = `e0f21509…`, same as the lane). The five culture gates were run over the
legacy packet and over the typed packet; the finding **lines** were compared as multisets.

### 4.1 The exact exchange

- removed: **10 lines, all `PHON-INVENTORY`, naming exactly `GAR-01..GAR-10`**;
- added: **0 lines**;
- typed-run `PHON-INVENTORY` naming a routed record: **none**.

So the channel differential is exactly the ten-line exchange; nothing else moved. (The typed
naming stdout's sha `feb6488127f1…` is identical to the sha `design.md` §1.3 measured for its
all-routed field-rename experiment — the two channel mechanisms are output-indistinguishable on
this differential; see §7.1.)

### 4.2 The other four gates

| gate | legacy findings | typed findings | stdout sha256 (both runs) |
|---|---|---|---|
| costume-era-consistency-gate | 0 | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty) |
| lexicon-coverage-audit | 0 | 0 | `e3b0c442…` (empty) |
| myth-consistency-gate | 0 | 0 | `e3b0c442…` (empty) |
| phonology-sanity-gate | 3 | 3 | `1ce5f0cdabad1bda177245607226cb6bf643f2bfbbe2ddb0918c510749066dd2` |
| naming-collision-gate | 17 | 7 | legacy `ebc8850d…` / typed `feb6488127…` |

## 5. Controls

### 5.1 A5 — the sound channel is live (planted violation on a checked class)

In the mirror, `examples/culture-d2/components/13-naming.yml` NM-01's name `sunel` was replaced
by `qvorhen`; the packet and projection were regenerated (`assemble-d2.py`, then the flow's
`--emit`) and the naming gate was run over the typed packet (22:13Z):

```
FINDING PHON-INVENTORY: FAIL — name NM-01 'qvorhen': symbol /q/ at position 1 is not in the
declared inventory (consonants {p, t, k, b, d, g, m, n, s, ʃ, r, l, j, w, h}, vowels {a, e, i, o, u})
FINDING DERIV-REPLAY: FAIL — name NM-01 'qvorhen': declared chain 'UP-COMPOUND' applied to 'su+nel' …
```

- typed-run `PHON-INVENTORY` count: **1** (the planted NM-01), with `GAR-*`: **0**;
- the same planted line is present in the legacy run (which then has 11 `PHON-INVENTORY`:
  10 GAR + 1 NM-01), so the plant is genuine and visible in both channels;
- receipts: `control-typed-naming.out` sha256 `8ba8601bd5bf…`, `control-legacy-naming.out`
  sha256 `b9e19ae15bda…` (mirror, 22:13Z; the final harness run at 22:18Z reproduced the same
  two digests).

Conclusion: the typed flow's zero-GAR result is a **channel** result, not a disabled gate —
a genuine violation on a checked class still fails the typed run.

### 5.2 A6 — the differential is the wiring (smuggled gloss caught)

`compare_only: true` was removed from `GAR-01`'s record in the typed packet (nothing else
changed); the naming gate over the tampered typed packet emits its `PHON-INVENTORY` again:

```
FINDING PHON-INVENTORY: FAIL — name GAR-01 'winter valley coat (heavy felted wool; uncombed finish
optional)': symbol /v/ at position 7 is not in the declared inventory …
```

receipt `smuggled-typed-naming.out` sha256 `8b0e8c16ed32…` (22:13Z). So any record that keeps
its gloss on the checked channel re-fires; the ten-line removal is exactly the off-channel
marking, and D17's fault class is detectable by the same tool this differential uses.

### 5.3 Note — the flow on the planted tree (scope of its own verdict)

With the NM-01 plant in place, `typed-gate-flow.py --emit` exits **0** and its own 10/10 checks
pass; the planted `PHON-INVENTORY`/`DERIV-REPLAY` lines sit in the *retained* legacy stream
("delta: 10 PHON artifact(s) retired, 0 added, retained lines identical"), and `--emit`
re-derives the committed expected file to the observed state. This is consistent with a
differential flow whose verdict scope is the hold set + channel differential; recorded here
because the expected-file semantics matter to the battery/reviewer shards, not as a defect claim.

## 6. Determinism

| leg | receipt |
|---|---|
| two adapter builds (mirror `--emit` twice) | typed packet sha256 `e8a83445…` both times; equals the lane's committed typed packet |
| two e2e runs (`--json`, lane) | stdout sha256 `121e8c8ca62d7572bfdcd817f469e4cdae711e4b798964744cd6a7f0eeb69f8b` both times; exit 0 both |
| e2e plain output | sha256 `204857cbb84d49cf39b51272651451609fa9a5ad29f4befdc712b07067d1f181`, exit 0 |
| same three legs on the earlier revision `ae55e6fa…` | typed packet `e8a83445…`; `--json` `8732066f408b…` twice; plain `d236e8e2bae6…` — i.e. the emitted artifacts are revision-identical even though the flow's own stdout changed with its check wording |

## 7. Limits, honesty notes, and observations

1. **Mechanism divergence (reported, not adjudicated).** The tested flow routes the ten records
   off the sound channel by marking them `compare_only: true` **in the derived gate packet**
   (§3.2). `reports/round-11/depth/design.md` §2.1/§2.3 instead specifies a new adapter
   `tools/assemble-d2-typed.py` that **moves** the checked field to `garment_gloss` with a
   `typed_channel` table — that file had not landed at this shard's read (D03 delivers it as a
   fragment, `.scratch/D03/assemble-d2-typed.py` sha `95ac9d05…`). Round-8 language is explicit
   that `compare_only` is "**not** a licensed exemption channel for typed labels"
   (`reports/round-8/depth/design-spec.md` §1.3 R3; `ASSEMBLY.md:94`). Reviewers already hold
   this seam: `design-review.md` DR-07 and SC-1 (silent-channel risk; proposes a packet-input
   control), `shard-assembler.md` §"both shapes remove the ten lines, so the L2 differential
   cannot separate them". **This shard's differential deliberately does not separate the two
   mechanisms either** — measured, both yield the same typed naming sha `feb6488127…`. Which
   shape is licensed is D20/D21/D22 + integrator territory; reported here, never absorbed.
2. **Read against a moving tree.** Sibling seats wrote `tools/**` during this shard. Every
   assertion above is against the revision named in the header; a later re-read is a new
   measurement. Re-run commands: §Receipts.
3. **Detail-string nit (fixed by the tested revision).** On the revisions read at 22:12–22:13Z,
   the flow's `typed-packet-pinned` check printed "derived typed packet differs from …" in both
   the failing (no pinned file) and passing (pinned, byte-equal) states — the `ok` flag was
   correct, the detail text stale. The tested revision `5758e315…` carries an empty detail on
   that check (22:18Z); recorded as a resolved observation.
4. **Line-level comparison.** A3 is a multiset comparison of finding **lines** (the design's own
   L2 form). It proves the exchange set; it does not interpret severities (the flow's L3 does,
   and its 10/10 includes it).
5. **Scope.** Five culture gates over two packet files; `examples/culture-d2` only; no D3, no
   battery, no canon. Scratch only under `.scratch/r11-d10/`; no lane file written by this seat.
6. **Revision watch (this shard saw four revisions of the flow).** Measured states:
   | revision (sha256, first read) | e2e state |
   |---|---|
   | `ae55e6fa…` (22:13Z) | exit 0, 10/10; tested revision of the first assertion run |
   | `d1712055…` (22:16:20Z) | exit 1, `7/10 checks passed — owed-slots-crosscheck; hold-set-equal; expected-file-current` ("declared owed slots ['LEX-GAR-01', …] vs holds ['LEX-GAR-01', …]"; "observed 16 findings, expected 16") — the D05 seat mid-edit, reworking the hold checks/rendering |
   | `a7e1224f…` (22:17Z) | exit 0, 10/10 (hold rendering now `LEX-GAR-0x` + `record: GAR-0x`) |
   | `5758e315…` (22:18Z) | exit 0, 10/10 — **the tested revision** of every final receipt above |
   The transient red is quoted so the integrator can attribute it; the differential itself was
   emitted identically by every revision observed ("delta: 10 PHON artifact(s) retired, 0 added,
   retained lines identical"). The integrator should still re-run the one-line e2e on the final
   revision before the claim is counted (and re-run §Receipts' commands if the tool changes
   again).

## 8. Adjacent observations (reported, never absorbed)

- **Filed earlier-round artifacts modified in the working tree during this wave** (`git status --porcelain`, 22:16Z, mtimes 19:01–19:05 local): `reports/round-5/validation.json`,
  `reports/round-6/validation.json`, `reports/round-6/checkpoint-validation.json`,
  `reports/round-7/validation.json`, `reports/round-8/validation.json`,
  `reports/round-9/validation.json`, `reports/round-10/coverage/index-update-22.md`. This seat
  did not write them; they look like ledger commands re-run "1:1" whose outputs live inside the
  repo. Round 10 recorded the same defect class once; the integrator should verify or revert
  before commit.
- `reports/round-11/depth/frozen-records.md` + `tools/gates/frozen/round-11/MANIFEST.tsv`
  (sha `4ddb911c…`) landed during this shard; not exercised here (D11/D12/D23 territory).

## Receipts

```sh
# 2026-10-17, lane root /home/vgpnk/Projects/shokunin/kotodama-shokunin, TMPDIR=$PWD/.scratch
# stamps as noted; all artifact pins re-read at 22:18Z

# artifact pins (sha256, 22:18Z)
tools/typed-gate-flow.py          5758e315593bb818dbf38c3c3ed7f79eb9ea555955331fadab4b50b2faa92075   # tested revision
tools/gates/naming-collision-gate.py d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
tools/d2-typed-labels.py          0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802
tools/assemble-d2.py              8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d
examples/culture-d2/packet.d2.yml          e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643
examples/culture-d2/packet.d2.typed.yml    e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb
examples/culture-d2/typed-labels.d2.yml    a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43
examples/culture-d2/typed-gate.expected.json 7ed597317b32b238d880af0a602fcbfa1ffd92608008879f049db9fd02aa03aa
tools/gates/frozen/round-4/naming-collision-gate.out 4d70252bdf7745dea76af07b41a94560b5789ff278cdbb5af4bf6924688bb19e
# (the expected file read e962849a… at 22:14Z, before the flow's rendering change; both reads named)

# legacy and typed naming runs (mirror; 22:13Z and 22:18Z — identical across the two runs)
python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml          # exit 1, sha ebc8850d08ec…
python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.typed.yml    # exit 1, sha feb6488127f1…

# flow (lane; 22:18Z, tested revision 5758e315…)
python3 tools/typed-gate-flow.py           # exit 0, 10/10 checks, sha 204857cbb84d49cf39b51272651451609fa9a5ad29f4befdc712b07067d1f181
python3 tools/typed-gate-flow.py --json    # exit 0, sha 121e8c8ca62d7572bfdcd817f469e4cdae711e4b798964744cd6a7f0eeb69f8b (twice identical)

# supporting checks (lane; 22:18Z)
python3 tools/d2-typed-labels.py --check   # exit 0 (projection re-pinned)
python3 tools/assemble-d2.py --check       # exit 0, "byte-identical deterministic assembly"

# scratch harness (all assertions + controls, mirrors): .scratch/r11-d10/
python3 .scratch/r11-d10/differential.py   # ALL PASS, verdict JSON in .scratch/r11-d10/differential.json
                                           # earlier revision run preserved as differential-ae55e6fa.json
```

Reproduction sketch (any reviewer, in an isolated copy):

```sh
mkdir -p /tmp-free-mirror && cd /tmp-free-mirror
cp -r "$LANE/tools" . && mkdir examples && cp -r "$LANE/examples/culture-d2" examples/
export TMPDIR=$PWD/.scratch
python3 tools/typed-gate-flow.py --emit
python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml > legacy.out
python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.typed.yml > typed.out
python3 - <<'PY'
from collections import Counter
l = [x for x in open("legacy.out") if x.startswith("FINDING ")]
t = [x for x in open("typed.out") if x.startswith("FINDING ")]
removed, added = Counter(l) - Counter(t), Counter(t) - Counter(l)
print("removed", len(list(removed.elements())), "added", len(list(added.elements())))
PY
# → removed 10 (all PHON-INVENTORY naming GAR-01..10), added 0
```
