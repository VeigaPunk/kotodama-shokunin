# examples/culture-d3 — D3 source-bounded culture drill (NON-CANON)

A deterministic, evidence-coupled culture assembly drill under profile
`kotodama-d3-evidence-coupling/1`. It builds a deliberately unbound research
packet (two fictional eras, 20 constructed lexemes, 6 constructed names,
7 utterances, 2 attributed beliefs, 2 audience-scoped symbols, 4 costumes —
one declared violation — 5 closed round-6 source bindings, 5 design-only
bridges) and checks it with a stdlib-only evidence-coupling guard.

**This is not canon, not a world-bible entry, and not accepted by
lore-shokunin.** The packet is `canon_status: NON-CANON`,
`handoff_status: prepared-not-accepted`; canon standing is lore's alone. No
real-language clearance, cultural permission, community consultation, or
ancient authenticity is claimed, performed, or granted anywhere in this
directory. Era coordinates E0/E1 are fixture-relative, not BCE/CE. All native
spellings are constructed and unscreened ASCII lowercase.

## Assembly status (scribe snapshot, round 7, 2026-10-17)

Baseline revision this directory was drafted against:
`30caac66a2a382f1c46ba31f0c3c93da62d0762c`.

Present (all digests measured from actual bytes):

| path | sha256 |
|---|---|
| `packet.json` | `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829` |
| `packet.gates.yml` | `306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425` |
| `components/04-language.json` | `fee4ad61a6aa9ca524c627a04ddbe61653a4058261aadf352f3b16a63b4dacfa` |
| `components/05-ritual.json` | `20ec0b1ffbc64a04fba2b031ddb3d8023c4610951382acdb85e2294c43320b2d` |
| `components/06-material.json` | `ba9866e37448b18e00710d490000ef662a07a41325109841a7d755f146d9eee7` |
| `components/07-evidence.json` | `1579aa84c3c924e91d4ea383b5bff1e1d75367a35ad0cbbd0533b9bc9725e8a3` |
| `controls.json` (3 positive / 16 domain / 4 malformed) | `f00ccf7aac931fb23719e4c3715f0e987c924fc79d7f9881236567d260d2ae70` |
| `expected.json` (parent-owned freeze manifest; 24 computational inputs; excludes docs) | `74496aa8aa7db2d7b2d69ecbd7a5a6acf3d4f565f600fd74bfeab5480adf5080` |
| `handoff.md` | documentation surface, outside the computational freeze; pinned by parent acceptance |
| `README.md` | documentation surface, outside the computational freeze; pinned by parent acceptance |
| `../..`/`tools/assemble-culture-d3.py` | `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014` |
| `../..`/`tools/check-evidence-coupling.py` | `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e` |
| `../..`/`tools/assemble-d2.py` (serializer dep, yaml_lines read-only) | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` |

The four component digests and the serializer digest are byte-identical to
the packet's own `assembly.source_sha256` / `assembly.serializer_sha256`
blocks. Closed evidence digests (ledger files, parent reconciliation,
contract) are pinned in `handoff.md` §artifact-manifest.

**Freeze, observed:** `expected.json` pins 24 computational input hashes with
predeclared `expected_exit: 0` / `finding_ids: []`, and the
packet-vs-frozen guard run is observed below at exit 0 / `findings: []`.
A freeze pins computational inputs only: it is **not** lore acceptance, not
canon, and not completion of the round arc; the final acceptance-runner
receipt remains pending and is not declared passed. `handoff.md`/`README.md`
are deliberately outside the freeze (no self-digest cycle); parent
acceptance pins their final hashes.

Provenance: the components, controls, both tools, the generated packet and
projection, and the freeze manifest were authored/assembled by this round's
tool workers and parent; this README records observed runs. The default
build is a normal, reproducible operation for anyone (see Reproduce).

## Reproduce

From the repository root. The default build is a normal, reproducible
operation: after intentional edits to any component, run
`python3 tools/assemble-culture-d3.py` — it deterministically writes exactly
the two derived outputs (`packet.json`, `packet.gates.yml`) and nothing
else. `--check` is the read-only drift check. Never hand-edit the generated
files; after any input change, re-run `--check` plus the guard/gates and
refresh the computational freeze (`expected.json`) only after that
re-verification — later input edits invalidate the existing snapshot before
any verdict.

```sh
python3 tools/assemble-culture-d3.py            # default build: writes exactly packet.json + packet.gates.yml
python3 tools/assemble-culture-d3.py --check    # read-only drift check (exit 0 equal / 1 drift / 2 error)
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json
python3 tools/check-evidence-coupling.py --selftest
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json
python3 tools/gates/naming-collision-gate.py examples/culture-d3/packet.gates.yml
python3 tools/gates/costume-era-consistency-gate.py examples/culture-d3/packet.gates.yml
python3 tools/gates/handoff-packet-check.py examples/culture-d3/handoff.md
```

Observed 2026-10-17 (this scribe, read-only runs; guard hash
`849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e`):

| command | exit | observed |
|---|---:|---|
| `assemble-culture-d3.py --check` | 0 | packet.json and packet.gates.yml byte-identical deterministic assembly |
| `check-evidence-coupling.py examples/culture-d3/packet.json` | 0 | `findings: []`, `counts.total: 0` |
| `check-evidence-coupling.py --selftest` | 0 | `selftest_passed: true`; positives 5/5 = controls.json's 3 positive cases (translated-label / place-change / belief-reword stay clean) + 2 CLI baselines (repo-cwd, foreign-cwd); domain 16/16 covering all 14 non-DATA diagnostics; malformed 4/4 (exit 2: invalid-json, invalid-utf8, wrong-root, missing-file); frozen 5/5 (good exit 0; tampered-digest / unknown-entry / bool-expected×2 exit 2 D3-SNAPSHOT) |
| `check-evidence-coupling.py packet.json --frozen expected.json` | 0 | `findings: []`, `counts.total: 0` against `expected.json` `74496aa8…f080` (24 computational input hashes verified before verdict; handoff/README excluded) |
| `naming-collision-gate.py packet.gates.yml` | 1 | exactly CROSS-HOLD ×2 (unresolved real-language sweep; no priority language/community named) + NAME-NEAR REVIEW (`E0` vs `E1`, recall-oriented); **no** phonology FAIL, **no** derivation FAIL |
| `costume-era-consistency-gate.py packet.gates.yml` | 1 | exactly one finding: R-01 [note] C03 declared RR1 violation kept visible; no R-02 |
| `handoff-packet-check.py handoff.md` | 0 | `fields=16/16 glossary-entries=20 findings=0` |
| acceptance runner | — | **pending** — final round receipt owed by the parent; not run by this scribe and not declared passed |

Digest verification of the closed evidence (real command, observed round 7;
matches `reports/round-7/baseline.json`):

```sh
sha256sum corpus/lessons/round-6-sources/05.json corpus/lessons/round-6-sources/03.json \
          corpus/lessons/round-6-sources/13.json corpus/lessons/round-6-sources/09.json \
          corpus/knowledge/synthesis/worldbible-integration-contract.md
# a00a5dc4… / adb22c9a… / 69504356… / 0dd2820d… / 50c4c2f2…
```

## Source bindings (closed; S01–S05)

Effective scopes/kinds follow the round-6 parent reconciliation rows (digest
`1b9b16710ae128185b5f1cdb339e4afd3dd09063b59974128271d23287892162`), not raw
worker whole labels. All files read-only; the guard re-verifies digests
(`D3-DIGEST`) and scope agreement (`D3-SCOPE`).

| id | ledger path | audit | effective scope | effective kind | source (closed binding) |
|---|---|---|---|---|---|
| S01 | corpus/lessons/round-6-sources/05.json | R6-05-A | partial-support | secondary-scholarly | UT Austin LRC, Hittite Online Lesson 2 — https://lrc.la.utexas.edu/eieol/hitol/20 |
| S02 | corpus/lessons/round-6-sources/03.json | R6-03-B | scoped-support | museum-object | Louvre E 12026 record — https://collections.louvre.fr/en/ark:/53355/cl010005890 |
| S03 | corpus/lessons/round-6-sources/13.json | R6-13-A | scoped-support | primary-text | Gobhila Gṛhya Sūtra II,8 (Oldenberg, SBE 30) via parent-pinned capture — https://web.archive.org/web/20231003011254/https://sacred-texts.com/hin/sbe30/sbe30020.htm |
| S04 | corpus/lessons/round-6-sources/13.json | R6-13-B | scoped-support | primary-text | Śatapatha-Brāhmaṇa III,2,1 (Eggeling, SBE 26) — https://www.wisdomlib.org/hinduism/book/satapatha-brahmana-english/d/doc63185.html |
| S05 | corpus/lessons/round-6-sources/09.json | R6-09-A | partial-support | secondary-scholarly | Stolper & Tavernier, ARTA 2007.001, printed p. 9 — http://www.achemenet.com/document/2007.001-Stolper-Tavernier.pdf |

Bridges (actual packet relations): BR01 S01→U01/U02 method-transfer; BR02
S02→C01/C02 method-transfer; BR03 S03→NR1 method-transfer; BR04 S04→O01/O04
analogy; BR05 S05→SY01/B01 method-transfer. All `asserted_scope: design-only`.

No source re-fetch happens from this directory; round-7 freshness re-fetches
belong to the assigned source scouts only.

## Expected holds (observed outcomes, not bugs to fix)

1. **CROSS-HOLD, naming legacy gate (exit 1)** — `screening.
   real_language_sweep_performed` is `false`; the projection's
   `cross_culture_review.unresolved` keeps `real-language sweep not
   performed`, and the second HOLD records that no priority
   language/community is named. Similarity stays a recorded review (the
   NAME-NEAR `E0`/`E1` pair is recall-oriented retrieval, not a confusion
   verdict), never disabled to buy green. No native phonotactic or
   derivation FAIL appears.
2. **Declared violation C03 (costume gate exit 1, R-01 only)** — RR1
   (Hall Wardens of the Two Benches, invented authority) prohibits
   plant-cloth on visitors at hall assembly; C03 intentionally violates it
   and stays visible. The new guard fails only a *false claim of lawful
   entitlement* (D3-RANK), never the honest declared violation.
3. **Not canonized** — the handoff envelope passes structurally
   (fields 16/16, glossary 20, findings 0) while remaining not canonized;
   no lore receipt exists and bilateral same-revision read is pending.
4. **Unresolved screening** — no real-language sweep has been performed; no
   clearance may be inferred or fabricated.
5. **Beliefs stay unresolved** — B01 (record-bound) and B02 (voice-bound)
   are attributed, disagreeing, `truth_status: unresolved` in-world
   accounts; promoting either to world-fact is exactly the D3-MYTH
   contradiction.

## Constraints

- Everything in this directory is NON-CANON design material. Never write
  canon standing, lore acceptance, world-bible import, or cultural-permission
  claims into any file here.
- Old D2 artifacts and the D1 handoff sample are read-only history; D3 does
  not replace or silently repair them.
- The assembler writes exactly two derived outputs (`packet.json`,
  `packet.gates.yml`) plus its script; `--check` is read-only (exit 0 equal
  / 1 drift / 2 error). The guard writes nothing at normal runs, follows no
  input-supplied paths outside the closed bindings, and makes no network
  requests.
- Components are hand-authored; the packet and projection are generated:
  never hand-edit `packet.json` or `packet.gates.yml`. After intentional
  component edits, rebuild with `python3 tools/assemble-culture-d3.py`
  (writes exactly those two derived outputs), re-run `--check` and the
  guard, and refresh the computational freeze (`expected.json`) only after
  that re-verification.
