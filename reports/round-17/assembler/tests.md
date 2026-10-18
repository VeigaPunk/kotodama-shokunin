# R17-D21..D24 — `tools/assemble-culture-d4.py` test record (O claim)

- round: 17 (operator loop 2 of 3, build round 1 of 4) · seats **R17-D21..D24**
  (O-assembler, single writer) · claim **O `assemble-culture-d4`**.
- date: 2026-10-18 (all commands below run on this date; outputs captured
  verbatim). Reference revision `9b49a4a` (round-17 declare); baseline
  `f30b6f8188937632bbedd0e7b29aeefff6f8b07b`.
- canon: NON-CANON engineering evidence; no canon, clearance, rights or
  promotion claim. Writes: this fragment plus the tool and
  `reports/round-17/assembler/impl.md`; scratch under `.scratch/r17-o/`
  (`TMPDIR=$PWD/.scratch` exported before every scratch-writing command).
- companion: `reports/round-17/assembler/impl.md` (contract and decisions).

## 0. Verdict

1. `python3 tools/assemble-culture-d4.py --selftest` → **exit 0, 81/81 checks
   passed** (2026-10-18T09:37:54Z; §3.1). The summary line carries the four
   control tokens the round-17 runner token-grades
   (`reports/round-17/run-validation.py:972-980`: `positive|clean`, `tamper`,
   `malformed`, `missing`) and the `N/M checks passed` count.
2. The selftest drives the **same CLI** the runner grades, over a fixture
   component tree inside one temporary directory; no file outside that
   directory is touched (the temp root is under `.scratch/` via `TMPDIR`).
3. The **delivered tree** is green: the integrator landed
   `examples/culture-d4/` (brief.md + 12 components + packet.d4.yml) during this
   seat's window, `--check` exits 0 on it, two in-place regenerations are
   byte-identical to the delivered bytes (sha256 `39c2d56a…`, 80,509 bytes),
   and the round-17 counting command's no-write run reports **claim O
   passed=true** (selftest tokens all true, 81/81, d2/d3 regressions green).
   Receipts in §3.5; the mirror probe history is in §3.3.
4. What this record does **not** vouch for: the D4 design content, the hold
   set, the typed projection/adapter/gate, or any real-world claim. Claim D is
   still blocked on other seats' artifacts plus one NON-CANON scan hit in the
   landed brief (F-O-6, impl.md §4).

## 1. What the selftest is

`--selftest` copies this tool, `tools/assemble-d2.py` (serializer) and
`tools/gates/costume-era-consistency-gate.py` (reader) into a temporary
directory, writes a 12-file fixture component tree under
`examples/culture-d4/components/` inside that directory, and drives the real
CLI (`subprocess`, `sys.executable`) through every control below. The fixture
tree mirrors the round-17 registry shape (01-brief, 02-phonology,
03-morphosyntax, 04-ledger-script, 05-lexicon, 06-register-contract,
07-oaths-sayings, 08-symbols-tokens, 09-eras-calendar, 10-measures-materials,
11-costumes, 12-ranks-names) with one block-scalar prose line carrying a colon
(the F-O-1 shim control). No gate is executed by this selftest (the D4 gates
are other seats' tools); the reader and serializer are executed read-only.

## 2. Control inventory (81 checks)

| class | controls | checks |
|---|---|---|
| positive | CLI exit 0, packet written, second run exit 0, deterministic bytes | 4 |
| `--check` clean | exit 0, byte-identical report | 2 |
| packet structure | profile keys, packet-owned name/canon, NON-CANON, all fixture blocks carried, metadata never merged | 5 |
| assembly pins | source digests recorded + match files, skipped keys, block-scalar shim recorded, elided prose never a packet block, generator, self-pin, reader/serializer pins, no host path, NON-CANON notes | 9 |
| tamper | mutation applied, `--check` exit 1, difference named, restore green | 4 |
| missing output | `--check` exit 1, default run regenerates | 2 |
| fail-closed negatives (11 classes × 4: exit 2, message names the defect, no traceback, no output written) | malformed component; root not a mapping; missing required block; empty block; wrong value type; empty required block; record not a mapping; duplicate record IDs; component collision; missing field; too few components | 44 |
| missing component file | exit 2, count message, fail closed | 3 |
| serializer absent | exit 2, fail closed | 2 |
| reader absent | exit 2, fail closed | 2 |
| restore | fixture tree assembles again, `--check` green | 2 |
| **total** | | **81** |

## 3. Receipts

### 3.1 Selftest — exit 0, 81/81

Command (2026-10-18T09:37:54Z, cwd = lane root, `TMPDIR=$PWD/.scratch`):

```
$ python3 tools/assemble-culture-d4.py --selftest
selftest: 81/81 checks passed — positive assemble/--check/determinism, tamper drift, malformed, missing-component and missing-output controls, plus collision, duplicate-id, wrong-type, empty-block, missing-field, too-few-files and serializer/reader-absent fail-closed controls; no file outside the temporary directory touched
EXIT=0
```

Tool pin at that run: `sha256sum tools/assemble-culture-d4.py` →
`61e04320cee18f7f45e01e3439ccc0424edabb1db140b088b3142458671eb2db` (802 lines;
the docstring edit recorded in this file's §3.3 history re-pins the tool to
`03a0754eec5565aad76598be53de4ba26e0199c81a30814ec88e87e31951f466`, 806 lines,
selftest re-run green at 2026-10-18T09:43:39Z). A later edit re-pins both; the
receipt above is the read-time pin (impl.md §6).

### 3.2 `--check` on the lane tree (pre-delivery)

Command (2026-10-18, cwd = lane root):

```
$ python3 tools/assemble-culture-d4.py --check
assembly error: components directory not found: examples/culture-d4/components
EXIT=2
```

This is the correct fail-closed state before the integrator lands the D4 tree
(`reports/round-17/scope.md:90-92` records the tree as expected-absent at
check time; F-O-3 in impl.md §4).

### 3.3 Mirror probe over the staged real components

The staged fragments live under `reports/round-17/d4/components/` (the
integrator copies them into `examples/culture-d4/components/`; the file header
of `01-brief.yml` states this). Probe (`.scratch/r17-o/mirror-probe.sh`,
2026-10-18): mirror the tool + reader + serializer into a scratch tree, copy
every staged component, pad to 12 files with stubs that declare no packet keys,
then run the real CLI:

```
staged components copied: 5
assembly error: missing required block 'eras': no component declares it
ASSEMBLE_EXIT=2
```

Reading: all five staged files (01-brief, 02-phonology, 03-orthography,
04-lexicon, 05-naming) parsed and merged; the only failure is the required
`eras` block, whose component (08-eras in the staged registry) had not landed.

Re-run at 09:39Z with 7 staged components (08-eras, 09-costumes added): build 1
and build 2 both exit 0, the two builds are byte-identical (`DETERMINISTIC=yes`),
`--check` exits 0 ("packet.d4.yml: byte-identical deterministic assembly",
58,458 bytes), and the five culture gates over the mirror packet all exit 1
with no stderr (naming 15 findings, phonology-sanity 1, costume-era 7,
lexicon-coverage 1, myth-consistency 3 — all in the runner's {0,1} range).

Re-run at 09:41Z with 9 staged components (06-myth, 07-symbolism added):
`BUILD1_EXIT=2` — `07-symbolism.yml: YAML subset parse error: duplicate key
'evidence' in flow mapping` (the file's line 47 declares `evidence` twice in
one flow mapping: the quoted self-sweep string and `evidence: design-choice`).
This is a defect in the staged component, not in the assembler: the reader
(the lane's stdlib subset) refuses duplicate keys by design, and this tool
fails closed with the file and key named. Disposition is the component seat's
or the integrator's — this seat does not edit another seat's file (F-O-5 in
impl.md §4).

Re-run at 09:43Z with **all 12 staged components** (the 07-symbolism duplicate
was corrected by its own seat; the probe no longer needs filler stubs):

```
staged components copied: 12
BUILD1_EXIT=0
BUILD2_EXIT=0
DETERMINISTIC=yes
packet.d4.yml: byte-identical deterministic assembly
CHECK_EXIT=0
80509 .scratch/r17-o/mirror/examples/culture-d4/packet.d4.yml
gate naming-collision-gate: exit=1 findings=16 err=
gate phonology-sanity-gate: exit=1 findings=1 err=
gate costume-era-consistency-gate: exit=1 findings=7 err=
gate lexicon-coverage-audit: exit=1 findings=1 err=
gate myth-consistency-gate: exit=0 findings=0 err=
```

Mirror packet verification (2026-10-18T09:44Z): parses under the costume gate
reader; 32 top-level keys (name, canon, assembly + 29 merged blocks:
calendar, cloth_sources, constructions, contact, contract, costumes,
cross_culture_review, era_dates, era_records, eras, festivals, form_slots,
layers, lexicon, materials, motifs, named_eras, names, narratives, orthography,
pantheon, phonology, provenance, rank_rules, rites, roles, routes,
source_era_dates, symbols); `assembly.source_sha256` carries all 12 component
digests and every one re-verifies against the file bytes; `assembler_sha256`
matches the tool; 75 metadata keys recorded under `skipped_keys`; 29 block
scalars elided across all 12 files; packet sha256 prefix `39c2d56a…`, 80,509
bytes. The delivered-tree `--check` receipt replaces this section at
settlement (§3.5).

### 3.4 Runner requirement mapping

`reports/round-17/run-validation.py:955-980` (claim O) runs `--check` and
`--selftest`, requires exit 0 for both, and token-grades the selftest stdout.
This tool's selftest stdout contains `positive`, `tamper`, `malformed`,
`missing` and `81/81 checks passed` — both acceptance branches of the token
check are satisfied. The D-claim determinism leg (`:557-565`) runs the same
`--check` and requires exit 0.

### 3.5 Delivered-tree receipt

The integrator landed `examples/culture-d4/` (brief.md + 12 components +
packet.d4.yml) during this seat's window; the receipts below were taken on the
delivered tree (2026-10-18T09:45Z, cwd = lane root, `TMPDIR=$PWD/.scratch`):

```
$ python3 tools/assemble-culture-d4.py --check
packet.d4.yml: byte-identical deterministic assembly
CHECK_EXIT=0

$ cp examples/culture-d4/packet.d4.yml .scratch/r17-o/packet.gen0.yml
$ python3 tools/assemble-culture-d4.py      # run 1: "Wrote … (80509 bytes)"
$ python3 tools/assemble-culture-d4.py      # run 2: "Wrote … (80509 bytes)"
$ cmp .scratch/r17-o/packet.gen0.yml examples/culture-d4/packet.d4.yml
GEN0==GEN2: yes   GEN1==GEN2: yes
$ sha256sum examples/culture-d4/packet.d4.yml
39c2d56a2ac357e2e8baf06eae94dc6c6c07740d39f4e85ee69ed1723c565038
```

Both in-place regenerations are byte-identical to the delivered bytes (the
R9-D02 determinism idiom); the delivered `assembly.assembler_sha256` equals the
current tool digest `03a0754e…`, so the packet was built by this tool revision.

The round-17 counting command, run in its no-write mode
(`python3 reports/round-17/run-validation.py --check`, 2026-10-18), reports
**claim O passed=true** with `--check` exit 0, `--selftest` exit 0, selftest
tokens all true, count 81/81, assembler sha256 `03a0754e…`, and all five d2/d3
regression legs green. The same run reports claim C passed and claim D failing
on other seats' pending artifacts (typed packet, projection, expected holds,
round-17 frozen manifest) plus one NON-CANON scan hit in the landed
`examples/culture-d4/brief.md` (F-O-6 in impl.md §4 — a refusal sentence whose
substring "accepted by lore" matches the runner's clearance pattern).

## 4. Not covered

- The typed derivation (projection, adapter, typed packet, hold set) and the
  round-17 frozen manifest — other seats' tools; this tool only exposes
  `assemble()` for the adapter's identity leg (`typed-support-1.md` §5.2 B4).
  Their absence is the current D-claim blocker (measured, §3.5).
- The five culture gates over the delivered packet are run by the runner's D5
  leg; the mirror probe ran them over the mirror packet (all exits in {0,1}).
- Real-world clearance, canon, or design-truth questions — out of province.

## 5. Limits

- A green selftest is a fixture-level control result; it does not certify the
  delivered components' design quality, only that the assembler fails closed
  on the classes it tests and reproduces its output deterministically.
- Digests are read-time pins; a later mismatch means the file changed after
  the read, never that the earlier read was wrong.
