# R20-D20 — interop: independent-reader agreement over the v3 handoff packet

- seat: R20-D20 (interop), lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- date: 2026-10-18. Baseline revision `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d`
  (round-19 admit); observed HEAD `122086bce0aa577bec221bb2d37eedf20f4f3ed2`
  ("round-20: declare claims D/O/C"). Readings stamped UTC.
- purpose: the round-19 coverage gap `two-reader-interop-agreement`
  (`reports/round-19/gaps.md`, slug `two-reader-interop-agreement`) applied to
  the v3 handoff surface — **two independent readers of one artifact must
  agree; a divergence is dispositioned, never averaged**. This file records the
  reader set, the agreement controls, and the disposition rule.
- role limits: executes and measures only. Writes: **this file** plus the
  seat's other assigned round-20 fragments and gitignored scratch under
  `.scratch/r20-d17/` (`TMPDIR=$PWD/.scratch` exported for every
  scratch-writing command). No commit, no push, no filed round-8..19 byte
  touched.
- canon: NON-CANON engineering evidence. Reader agreement is a computational
  fact about bytes; it is not canon, acceptance, or a lore receipt.

## 0. Verdict at this stamp

**Reader agreement holds on every surface measured so far; the v3 packet
itself was not rendered yet (13:10Z), so the v3 legs are pending.** The reader
set was controlled on the v2 build05 twins (the v3 packet's own base) and on
the 37 D4 link specs the design files (`claims-map.md`). Two shared
digest-drift findings were produced independently by two different readers and
agree — the strongest form of agreement evidence this surface offers (two
readers, same finding, same subjects).

## 1. The reader set

| reader | surface | what it reads | implementation |
|---|---|---|---|
| R1 | markdown | own parser of the packet tables; resolves `path#selector` under the published v2-design §3.1 grammar | this seat, `.scratch/r20-d17/auditlib.py` (independent code, no harness imports) |
| R2 | machine twin | claim uncertainty census + grammar findings | `tools/harness/packet_uncertainty.py` |
| R3 | machine twin | claim-to-record links + edge targets, digest re-measurement | `tools/harness/packet_links.py` |
| R4 | markdown | 16-field envelope, glossary count, canon/baseline traps | `tools/gates/handoff-packet-check.py` |
| R5 | receipt | the v3 exercise's own scan line and census (pending; exercise mid-rewrite at this stamp) | `tools/exercise-handoff-e2e.py` |
| R6 | twin pair | markdown vs machine twin agreement (cross-serialization) | R1 over md vs R2/R3 over the twin |

## 2. Control A — the v2 build05 twins (15 claims, statuses 8/5/2)

Command: `python3 .scratch/r20-d17/interop.py readers reports/round-15/handoff/packet-v2-05.md reports/round-15/handoff/packet-v2-05.yml` (measured 2026-10-18T13:09Z; `TMPDIR=$PWD/.scratch`).

| reader | reading | agreement |
|---|---|---|
| R1 | 15 claims, `{supported 8, partial 5, unresolved 2}`; links 50/50 resolved; basis locators 23/23; 2 findings (manifest digest drifts) | baseline |
| R2 | exit 0, `claims=15 findings=0` (`--require-oq`) | claims agree 15=15; zero findings (R2 does not digest-check manifest rows) |
| R3 | exit 1, `links_checked=50 resolved=50`, 2 findings — `M-DIGEST-MISMATCH [tools/d2-typed-labels.py]`, `M-DIGEST-MISMATCH [tools/harness/packet_links.py]` | links agree 50=50; **the two findings are the same two R1 reports** (`A-20`, `A-25`), independently derived |
| R4 | exit 0, `fields=16/16 glossary-entries=20 findings=0` | shape agrees |
| R6 | md (R1) vs twin (R2/R3): same claim count, same status census, same link count | twin agreement holds |

**Disposition of the two shared findings** (they are digest drift, not packet
defects, and both readers agree): `tools/harness/packet_links.py` moved in
round 16 (`f81bc9f7…` → `66d854cc…`; round-16 `verify.md` §5(e), the documented
self-pin interaction), and `tools/d2-typed-labels.py` is being rewritten by
the round-20 O seat (`0da0015f…` → `76536a92…` at the stamp). Both are
recorded supersessions with successor pins owed; the v2 packet bytes
themselves are unchanged (§`regression-v2.md`).

## 3. Control B — the D4 link specs before the packet exists

Source: the 37 unique `path#selector` specs extracted from
`reports/round-20/handoff/claims-map.md` (§1 link lines), measured
2026-10-18T13:0xZ.

| reader | command | reading |
|---|---|---|
| R1 | `python3 .scratch/r20-d17/auditlib.py` resolution pass over the spec list | 37/37 resolve, 0 dangling |
| R3 | `python3 tools/harness/packet_links.py --links "<37 specs>" --repo-root . --json` | exit 0, `links_checked=37 resolved=37 findings=0` |
| negative control | `… --links "examples/culture-d4/packet.d4.yml#ER-99,examples/culture-d4/typed-labels.d4.yml#no_such_block,examples/culture-d4/expected-holds.json#counts"` | exit 1: 2 × `L-TOKEN-MISSING`, third spec ok — the resolvers discriminate |

R1 and R3 agree spec-for-spec on the proposed D4 witnesses.

## 4. The v3 packet — build 16 vs the exercise surface (measured 13:14–13:17Z)

`reports/round-20/handoff/packet-v3-16.md`, sha256
`9f37c08af9bd56fce668ccb42bd34351d21e650c49e27898ff7736a70dfdd730` (builds
14–16 are content-identical apart from the build key and stamps; the initial
build-13 render and its repaired re-render are recorded in `audit-v3.md` §3).
The freeze seat then landed the exercise's machine twin `twin.json`
(sha `b3e2bad7…`) and baseline `expected.json` (13:15:37–13:15:45Z), and the
exercise runs exit 0 (`fields=16/16 glossary=20/20 findings=0 links=61/61
packet_sha256=6de822f4…`).

| reader | reading | agreement |
|---|---|---|
| R1 (markdown, own parser, packet-v3-16) | 27 claims `{supported 16, partial 7, unresolved 4}`; basis locators 46/46; links 92/92; edges 94; manifest 56/56; 0 findings | baseline A |
| R4 (markdown, gate, packet-v3-16) | exit 0, `fields=16/16 glossary-entries=20 findings=0` | shape agrees |
| R6 (v2-subset equality, packet-v2-05 vs packet-v3-16) | 15/15 carried rows equal on all five comparable fields | agrees |
| R1 (markdown, own parser, `packet.md` — the exercise's filed assembly, sha `6de822f4…`) | 24 claims `{supported 14, partial 7, unresolved 3}`; basis locators 47/47; links 61/61; edges 48; manifest 42/42; 0 findings | baseline B — internally clean, but a **different census** from baseline A |
| R2 (twin, uncertainty) | exit 0, **`claims=24`**, findings=[] | agrees with B; **DISAGREES with A (24 ≠ 27)** |
| R3 (twin, links) | exit 0, `links_checked=61 resolved=61`, findings=[] | agrees with B and with R1-over-`packet.md`; **DISAGREES with A (61 ≠ 92)** |
| R5 (exercise receipt) | exit 0, `links=61/61`, packet sha `6de822f4…`; baseline `counts {claims 24, d4_claims 9, edges 48}` | agrees with B |

Note on R1's reader upgrade (recorded for reproducibility): the exercise's
`packet.md` uses the artifact-id selector form (`A-11#coverage.typed_labels`)
and its `typed-labels.*.yml` files are JSON bytes under a `.yml` suffix. This
seat's reader was extended to resolve artifact ids through the manifest index
and to JSON-resolve any JSON-parseable artifact regardless of suffix; after the
upgrade R1-over-`packet.md` reads 47/47 basis locators and 61/61 links, 0
findings — i.e. the upgrade closed a reader gap, not a packet defect. The same
reader still reads packet-v2-05 at 23/23 + 50/50 and packet-v3-16 at 46/46 +
92/92.

### The divergence, precisely (F-INT-1, major)

- Two filed "v3 packets" carry **different D4 claim sets**. The packet seat's
  render (`packet-v3-13…16.md`, built from the round-20 design and
  `claims-map.md`) carries **12 D4 claims** `D4-CL01…D4-CL12` (27 total); the
  exercise's filed assembly (`packet.md`, sha `6de822f4…`, frozen in
  `expected.json` with its twin `twin.json`) carries **9** `D4-CL01…D4-CL09`
  (24 total). The exercise tool's own source defines exactly nine D4 rows
  (`tools/exercise-handoff-e2e.py` :1073–1226; its header line 31 says "the
  nine new D4 claim rows"), while the design, `claims-map.md` and the packet
  seat's render all carry twelve.
- The packet seat's validation row declares `claims=27 findings=0` and
  `links=102 resolved=102`; the filed twin measures 24 claims / 61 links / 48
  edges. The packet's own control therefore measured a twin that is not the
  filed one (its build script's twin, not the exercise's).
- Every reader is green **on its own surface** — the gate reads the packet
  markdown (16/16 + 20/20 on both filed packets), the harness reads the twin
  (24 claims, 0 findings), the exercise compares against its own baseline
  (exit 0). Nothing in the round cross-reads the two surfaces, which is exactly
  the interop gap this seat exists to close.
- Disposition per §5 rule 1 (**census disagreement**): the round's v3 surface
  is **not settled**; both readings are named, neither is averaged, and the
  divergence is routed to the packet seat + impl seat + integrator with the
  design's 12-claim set as the declared expectation (`design.md` §2,
  `claims-map.md` §1, `uncertainty-plan.md` census `27 / 15 / 7 / 5`).
- Secondary defect found while measuring: the exercise's `--keep DIR` flag is
  parsed (`:3263`) but never passed to the run — a dead CLI surface.

When the surfaces are reconciled, the same command set re-runs:

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/r20-d17/interop.py readers reports/round-20/handoff/packet-v3-*.md reports/round-20/handoff/twin.json
python3 tools/harness/packet_uncertainty.py --packet reports/round-20/handoff/twin.json --require-oq --json
python3 tools/harness/packet_links.py --packet reports/round-20/handoff/twin.json --json
python3 tools/exercise-handoff-e2e.py --quiet
```

## 5. Divergence disposition rule (declared before the v3 readings)

1. **Census disagreement** (claims, status histogram): the markdown surface and
   the twin disagree → the packet is not frozen; the divergence is routed to
   the packet seat with both readings named.
2. **Link disagreement** (a spec one reader resolves and another does not): the
   stricter reading wins until resolved; the spec is re-run through both
   readers and the resolver's own negative control (§3) proves the checker
   discriminates.
3. **Digest disagreement**: live bytes are re-measured twice; if stable, the
   pin is the drift and the re-pin discipline applies (new row, recorded
   reason).
4. No reader's reading is averaged with another's, and no reader's zero
   findings is treated as the other's evidence.

## 6. Limits

- Readers R2/R3 judge the machine twin; R1/R4 judge the markdown. Agreement
  between them is also a serialization-agreement check (R6), not an
  independent re-derivation of the packet's claims.
- R1 is this seat's code; its own positive/negative controls are recorded in
  `audit-v3.md` §Controls (build05 known-good, round-11 v1 known-reject).
- All readings are computational; none is a canon, source-freshness, or rights
  verdict.
