# Handoff-e2e exercise — field map from live D2/D3 artifacts to the §4 envelope (R11-O01)

- topic: The design of `tools/exercise-handoff-e2e.py` — which live D2/D3
  artifact bytes supply each of the handoff contract's 16 envelope fields, how
  the rendered packet is judged by `tools/gates/handoff-packet-check.py`, and
  what the exercise must assert that the gate cannot. O02–O05 implement from
  this map; it is a spec, not a transcript of a render.
- sources: `corpus/knowledge/synthesis/worldbible-integration-contract.md`
  (§4 fields :53–67, §6 claim kinds :94–106, §8 :124–136, §9 :138–157);
  `tools/gates/handoff-packet-check.py` (``FIELD_NAMES`` :122–139, placeholders
  :144–160, finding ids :49–70, `_mentions` :201–204, `collect_fields`
  :274–314, `check_glossary` :388–444, scan line :591);
  `examples/culture-d3/packet.json` (keys `lexicon`…`bridges`, `assembly`,
  `screening`, `scope_notes`); `examples/culture-d3/expected.json`;
  `examples/culture-d3/handoff.md` (the committed reference packet, read as
  documentation only); `examples/culture-d2/packet.d2.yml` (:1–2, :3319–3345);
  `examples/culture-d2/typed-labels.d2.yml` (keys `coverage`, `findings`,
  `typed_labels.labels`, `rank_rules`, `era_material_reconciliation`);
  `tools/check-gate-battery.py` (:114, :387–394, :597–650);
  `reports/round-11/claims.json` (claim O), `reports/round-11/targets.json`
  (R11-O01…O18).
- couples: `reports/round-8/depth/skill-table-draft.md` §7 (the D2 typed-label
  limit this exercise reads, never re-opens); `reports/round-11/depth/design.md`
  (claim D owns D2 wiring and the expected hold set — this document cites D2
  only as read-only input bytes); `examples/culture-d3/README.md` (D3 reproduce
  commands and observed runs).
- taken-from: contract §4's field table, the gate's own recognition code, and
  the D3 committed packet's shape; no new contract terms are invented here.
- verified-at: 2026-10-17 — all 21 read-set digests measured with `sha256sum`;
  a scratch prototype (`.scratch/proto-handoff-e2e.py`, not a deliverable)
  rendered a packet and the gate scanned it `fields=16/16
  glossary-entries=20 findings=0`, exit 0, byte-identical across two runs
  (sha256 `a7defa9531dc5fa33465c6271f23e1148f5b50055dfc8398e18afe1eb224a0e1`,
  139 lines); 11 control probes measured, two of them the recognition hazards
  of §4 (the rest in §9).
- recheck: on any change to the read set, the gate, or the contract; before the
  §8 baseline is first pinned and before any re-pin; before the first real
  packet leaves the lane.

## 0. Scope of this design

The O claim (`reports/round-11/claims.json`) asks for a runnable exercise that
assembles a handoff packet from **live** D2/D3 artifacts and validates it
through the envelope gate in an isolated copy, with 16/16 fields, 20/20
glossary entries, a committed baseline and a selftest. This document fixes:

- the exact read set (§2) and what is deliberately excluded;
- the field-by-field source map and render form (§3);
- the recognition hazards that silently change what the gate reads (§4);
- the glossary payload rule (§5) and the cross-reference assertions (§6);
- two live discrepancies the exercise must measure around rather than copy (§7);
- the baseline path, shape and tamper controls (§8, §9), and the exercise's own
  CLI/exit-code surface (§10) so `reports/round-11/run-validation.py` (X03) can
  call it.

Out of province, reported not absorbed: canon decisions and any canon
standing (lore-shokunin), real-world rights/permission rulings (operator),
game mechanics, general research method (chousa). The exercise emits
`not canonized` and never a producer-side canon certification (gate
`HO-CANON-MARKER`/`HO-CANON-CLAIM`, contract §6/§8.7/§11; measured in §9).

## 1. The judged interface (as it actually behaves)

Observed target: `python3 tools/gates/handoff-packet-check.py <packet.md>`
exits 0 and prints `INFO scan: fields=16/16 glossary-entries=20 findings=0`.

Two measured gaps the exercise must close on its own side:

1. **Entry count is not enforced.** A packet missing one of the 20 glossary
   rows still exits 0 (probe `drop L20`, §9): the gate counts rows it sees, it
   does not know how many there should be. The exercise asserts the row count
   and the entry-id set against the live lexicon.
2. **Digest presence is checked, digest equality is not.** `DIGEST_RE`
   (gate :164–167) only requires *a* hex digest to appear in
   `contract_ref`/`artifact_manifest`; nothing compares it to bytes. The
   committed `examples/culture-d3/handoff.md` passes while pinning two stale
   digests (§7). The exercise re-measures every digest from bytes and asserts
   equality; that is the point of the exercise, not a gate change.

## 2. Read set (live, read-only; digests measured 2026-10-17)

| path | role | sha256 |
|---|---|---|
| `corpus/knowledge/synthesis/worldbible-integration-contract.md` | pinned contract (§1/§4 authority) | `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` |
| `examples/culture-d3/packet.json` | D3 payload source (lexicon, names, utterances, beliefs, symbols, materials, objects, costumes, rank rule, references, bridges, assembly, screening) | `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829` |
| `examples/culture-d3/packet.gates.yml` | D3 legacy projection (native forms only) | `306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425` |
| `examples/culture-d3/controls.json` | guard control expectations | `f00ccf7aac931fb23719e4c3715f0e987c924fc79d7f9881236567d260d2ae70` |
| `examples/culture-d3/expected.json` | D3 freeze manifest (24 computational input hashes; docs excluded) | `562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc` |
| `examples/culture-d3/components/04-language.json` | D3 component (phonology, lexicon, names, sound_changes, utterances) | `fee4ad61a6aa9ca524c627a04ddbe61653a4058261aadf352f3b16a63b4dacfa` |
| `examples/culture-d3/components/05-ritual.json` | D3 component (beliefs, speech_rules, symbols, naming_rule) | `20ec0b1ffbc64a04fba2b031ddb3d8023c4610951382acdb85e2294c43320b2d` |
| `examples/culture-d3/components/06-material.json` | D3 component (eras, materials, objects, costumes, rank_rules) | `ba9866e37448b18e00710d490000ef662a07a41325109841a7d755f146d9eee7` |
| `examples/culture-d3/components/07-evidence.json` | D3 component (references, bridges, canon_status, handoff_status, scope_notes, screening) | `1579aa84c3c924e91d4ea383b5bff1e1d75367a35ad0cbbd0533b9bc9725e8a3` |
| `examples/culture-d2/packet.d2.yml` | D2 merged gate packet (read-only input bytes) | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` |
| `examples/culture-d2/typed-labels.d2.yml` | D2 typed-label/reconciliation/rank projection (JSON-formatted) | `e70ba1477dbeb830061db6fd12516b7d902587bddae173f55a3650015d380b2f` |
| `corpus/lessons/round-6-sources/05.json` | closed ledger R6-05-A (S01) | `a00a5dc4c872de14970899f6736007039c2cda10824f9731d2436bdd519afbdb` |
| `corpus/lessons/round-6-sources/03.json` | closed ledger R6-03-B (S02) | `adb22c9a5f3acee621103c7b9dddeeb1eedba22d9e1d92081e37825b80560cea` |
| `corpus/lessons/round-6-sources/13.json` | closed ledgers R6-13-A / R6-13-B (S03, S04) | `695043562e7e0caeda6693384baca060009c9e3feb2c108f5e8ea6bfc282d71a` |
| `corpus/lessons/round-6-sources/09.json` | closed ledger R6-09-A (S05) | `0dd2820d1e837b9ab5e503d21f1a891d367d873c9335f9dad80bef3c2da6ac94` |
| `reports/round-6/parent-reconciliation.json` | effective round-6 scope/kind authority | `1b9b16710ae128185b5f1cdb339e4afd3dd09063b59974128271d23287892162` |
| `tools/gates/handoff-packet-check.py` | this run's judge | `e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575` |
| `tools/assemble-culture-d3.py` | D3 assembler (dependency pin) | `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014` |
| `tools/assemble-d2.py` | yaml serializer dependency (read-only) | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` |
| `tools/d2-typed-labels.py` | D2 typed-label projection generator | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` |
| `tools/check-evidence-coupling.py` | D3 evidence-coupling guard | `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e` |

Deliberately **excluded**: `examples/culture-d3/handoff.md` and the directory
`README.md`. They are documentation surfaces outside the computational freeze
(`examples/culture-d3/expected.json` `limits`: "Handoff/README and round
acceptance receipts are external presentation evidence checked separately"),
and they currently carry stale digests (§7). The exercise reads no prose packet;
it re-renders one from the bytes above. The exercise never reads `/tmp` scratch
and never writes inside `examples/**` or `corpus/**`.

## 3. The 16-field map

Form column: **T** = first-cell table row, **H** = `## <exact field name>`
section heading whose body is the value. Heading names must use the exact
underscore field name (§4a).

| # | field | form | live source | derivation rule | gate consequence |
|---|---|---|---|---|---|
| 1 | `packet_id` | T | — | constant `kotodama.handoff.d2d3-e2e` | supplied |
| 2 | `packet_version` | T | — | `1.0.0`, bumped when the renderer or read set changes; carries "pure function of the pinned read set; no wall-clock content" | supplied; no timestamp may enter the packet |
| 3 | `contract_ref` | T | contract bytes | `kotodama-lore-adjacency 1.0.0, contract digest sha256:<sha256(contract bytes)>` measured this run | `HO-CONTRACT-REF` needs revision + digest: both present |
| 4 | `producer` | T | — | `kotodama-shokunin (round-11 handoff-e2e exercise; generative craft and design records only)` | supplied |
| 5 | `recipient` | T | — | `lore-shokunin (canon, world-bible entities, chronology, bible-wide consistency)` | supplied |
| 6 | `request_ref` | T | — | `none — no lore brief exists; assembled as a deliberately unbound research drill (contract §4)` | supplied |
| 7 | `baseline_bible_ref` | T | — | `none — deliberately unbound research packet; cannot be imported as canon without a lore baseline and a new reviewed handoff (contract §4)` | needs `unbound`+`research` proximity or `unbound` in the value (`HO-BASELINE` is document-wide, §4c) |
| 8 | `artifact_manifest` | H | read-set digests + live JSON lengths | table `artifact_id \| path \| role \| sha256 \| records`; one row per read-set file + one inline-glossary row (§5) | needs ≥1 hex digest (`HO-MANIFEST-DIGEST` satisfied); rows with `artifact_id` are never read as a glossary payload |
| 9 | `subject_refs` | T | D3 `packet.json` (`beliefs`, `rank_rules`, `scope_notes`); D2 `packet.d2.yml` (:1, lexicon `L-04 las`, `PAN-01 Halatu`, `era_records ER-01`) | 8 namespaced candidates, all unresolved: `cand:kotodama.d3.{language-variety,record-keeper-office,voice-of-the-record-office,hall-assembly-institution}` + `cand:kotodama.d2.{culture,pasture-lineage-institution,archaic-sky-holder,open-grazing-era}`; each names its witness record; never a guessed lore ID | supplied; free text, no gate check — the assertion is the exercise's (§6) |
| 10 | `scope` | T | live counts | one line: D2 drill + D3 drill, eras E0/E1, 20 lexemes, 6 names, 7 utterances, 2 beliefs, 2 symbols, 4 costumes (one declared violation), 5 bridges, D2 read-only inputs, "no real place", ASCII-lowercase note; counts computed from `packet.json` lengths | supplied; **no heading may contain the token `scope`** (§4b) |
| 11 | `dependency_manifest` | H | digests + `packet.json` rules | bullets: profile `kotodama-handoff-e2e/1`; assembler/serializer/typed-label generator/gate/freeze-manifest digests; SC1, AV1, NR1, RR1 one-liners from live records; "no floating `latest`" | `HO-DEP-FLOAT` scans for the literal `latest`: never write it unnegated |
| 12 | `claim_ledger` | H | `packet.json` (`sound_changes[0]`, `speech_rules[0]`, `naming_rule`, `rank_rules[0]`, `symbols[0..1]`, `beliefs[0..1]`, `scope_notes[0]`, `references[0..4]`, `screening`) + D2 `typed-labels.d2.yml` (`coverage`, `era_material_reconciliation.summary`) | table `claim_id \| kind \| evidence_status \| summary`: CL01–CL05 generative rules, CL06 attributed belief (B01/B02, `truth_status: unresolved`), CL07 designer interpretation, CL08–CL12 real-world references (scope/kind/audit/locator from live records), CL13 screening statement; D2-CL01 typed-label channel (58 labels; 46/10/2 by kind; 10 holds), D2-CL02 normalization residuals (13 unresolved, 3 quarantine, 4 conflicts, 10 reconciliations) | free text; kind vocabulary from contract §6 (§6.3 below) |
| 13 | `coupling_edges` | H | `packet.json` `bridges[]` | table `bridge \| source \| relation \| target_ids \| mechanism \| limits`, rows BR01–BR05 verbatim from live records (`relation`, `target_ids`, `mechanism`, `limits`, `asserted_scope` recorded) | free text; the heading **must** be `## coupling_edges` (§4a) |
| 14 | `requested_decisions` | H | live record classes | RD-01…RD-08 (lexicon+names / beliefs / symbols / eras / costumes+rank / names+screening / bridges / transfer surface) generated with the live record IDs in the text, `accept` always meaning "retain as non-canon candidate material"; RD-D2-01/RD-D2-02 for the D2 typed-label channel and its retained holds | free text; no canon wording |
| 15 | `validation` | H | actual run observations | observed rows only, with captured exits and the scan line: digest re-measure (21 files), gate exit 0 + scan, D2 read-only facts (58 typed labels, 16 findings, 15 hold/fail, 9 `R-MAT-BRIDGE-MISSING`), plus the §6 assertions actually run | heading `## validation` is a field; its body must describe runs, not intentions |
| 16 | `open_questions` | H | live unresolved keys | OQ-E2E-01 real-language sweep unperformed (`screening.status=unresolved`); OQ-E2E-02 no lore receipt/baseline/bilateral read; OQ-E2E-03 the §7 digest drift (kotodama-owned, non-blocking); OQ-E2E-04 D2 rank/material holds open (blocking for any D2 rank/material claim) | free text; each names a responsible lane and blocking status (§4) |

Two supporting forms, both required by the gate and measured: the level-1
heading `# Handoff packet — … (deliberately unbound research packet; not
canonized)` (without a level-1 heading the gate returns `HO-DATA`, exit 2) and
the line `- canon_standing: not canonized — lore disposition required
(lore-shokunin owns canon)` (`HO-CANON-MARKER`).

## 4. Field-recognition hazards (measured, not theoretical)

- **(a) Hyphenated headings supply nothing.** `_mentions` (gate :201–204) does
  a boundary-checked literal match; underscores matter. Probe: replacing
  `## coupling_edges` with `## coupling-edges` produced `HO-MISSING` (exit 1).
  All seven heading-form fields therefore use the exact `## field_name` text.
- **(b) A heading containing a field-name token hijacks that field.** Heading
  candidates are collected before table candidates and the first
  non-placeholder candidate wins (`collect_fields` :274–314). Probe: inserting
  `## scope-notes` made the `scope` value the new heading's body (reported
  `where: section heading line 109`) instead of the `| scope |` row; exit
  stayed 0, so only an inspection catches it. Do not emit any heading whose
  text contains `scope`, `validation`, `open_questions`, etc., unless that
  body is the intended value. (The committed D3 handoff.md already behaves
  this way for `scope` — its `## scope-notes` body is what the gate reads.)
- **(c) `HO-BASELINE` is document-wide.** A bare `baseline_bible_ref: none` is
  only reviewed when the words `unbound` and `research` do not appear within 60
  characters of each other anywhere in the packet (gate :507–521). Probe: a
  bare `| baseline_bible_ref | none |` row still exited 0 because the
  `request_ref` row carries "unbound research". Keep the §3 wording; if the
  request_ref wording ever changes, re-check this pair.
- **(d) Placeholder vocabulary.** Values in the gate's `PLACEHOLDERS` set
  (:144–160) — including `unknown`, `(to-verify)`, `n/a`, `-` — count as
  blank. An honest unknown must be a sentence ("unknown — no in-world account
  drafted"), and the glossary's `status: unknown` is valid *inside an
  etymology cell*, never as a whole field value.
- **(e) Canon-claim regex traps.** Avoid affirmative canon verbs near `canon`
  on one line (`certif|establish|grant|award … canon`, "this packet is canon",
  `canon_standing: canonized …`). The marker line and negatives like "never
  canonized" are safe (`_affirmative`, gate :321–355).
- **(f) Manifest rows and glossary rows are different tables.** A table with an
  `artifact_id` column is never a glossary payload; the manifest's inline
  glossary row must contain the word `inline` so no `INFO glossary-external`
  line claims the profile is unchecked.

## 5. Glossary payload: 20/20

One inline table, header `| entry_id | E0 form | E1 form | gloss (packet) |
etymology |`, exactly 20 rows, one per `packet.json` `lexicon[]` record in
source order. Row rule:

- `entry_id` = `lexicon[].id` (asserts the L01…L20 set, §1 gap 1);
- E0/E1 forms = `lexicon[].forms.E0` / `.E1` (E1 differs from E0 only under SC1);
- gloss = `lexicon[].gloss` verbatim;
- etymology = `status: <lexicon[].status> — E0 *<E0> → E1 <E1> (<changed by SC1|unchanged into E1>); available_from <era>`.

All 20 live statuses are `constructed` (measured), which is inside the
licensed vocabulary `attested/reconstructed/constructed/contested/unknown`
(glossary-registry-format.md §4, consumed by the gate :174). The exercise
asserts: 20 rows, ids `L01…L20`, statuses equal the live lexicon's status set,
and every etymology cell non-placeholder. A manifest row
`| A-GLOSS | §glossary payload (inline, this packet) | … | sha256:<packet.json
digest> | 20 |` identifies the payload's source bytes — the packet is never
self-digested (a self-reference cannot be a fixed point).

## 6. Cross-reference assertions (contract side, run by the exercise)

1. **Three-way field agreement (§4).** Parse the contract §4 table
   (`worldbible-integration-contract.md:53–67`), split the field-name cells on
   `,` (row 1 yields `packet_id` and `packet_version`; row 3 yields
   `producer`/`recipient`/`request_ref`; row 12 yields
   `validation`/`open_questions`), and assert the resulting 16-name set equals
   the gate's `FIELD_NAMES` tuple and the set the rendered packet supplies.
2. **Contract digest equality (§1).** `contract_ref`'s digest equals the sha256
   of the contract bytes measured in the same run (would be `5f4c02bf…` at the
   §2 measurement; never hard-coded).
3. **Claim kinds (§6).** Every `claim_ledger` row's kind token is drawn from
   the contract's five kinds (real-world reference; generative rule; candidate
   world-fact; attributed in-world belief; designer interpretation) or the
   screening-statement note; the D2 rows are labeled "derived projection
   (author-side)" in the evidence column so they cannot be read as world claims.
4. **No floating versions (§9).** `dependency_manifest` contains no unnegated
   `latest`, and every dependency names an exact digest or version pin.
5. **Candidates stay unresolved (§4).** Every `subject_refs` token starts
   `cand:`; none matches a lore entity id pattern; the text says "unresolved".
6. **Manifest digests equal bytes.** Every manifest row's digest equals the
   sha256 of the named file, measured in-run (this is the assertion the gate
   cannot make, §1 gap 2).

## 7. Live discrepancies this design reports (not repairs)

Measured 2026-10-17; all three are documentation-side, none blocks the
exercise, and the exercise re-measures rather than propagating them:

1. `examples/culture-d3/handoff.md:27` and `:74` pin contract digest
   `sha256:50c4c2f2…`; current contract bytes measure `sha256:5f4c02bf…`.
   `examples/culture-d3/expected.json` already pins `5f4c02bf…`, so the freeze
   manifest is current and the handoff prose is stale.
2. `examples/culture-d3/handoff.md:242` and `examples/culture-d3/README.md`
   cite `expected.json` as `sha256:74496aa8…`; current bytes measure
   `562b76cb…` (the manifest's own inputs still measure as pinned — the file
   was re-pinned after the documentation pass).
3. `examples/culture-d2/packet.d2.yml` measures `e0f21509…`;
   `examples/culture-d2/ASSEMBLY.md:16` records `54be6319…` and its own
   :129–135 supplement says the text describes the round-3 snapshot, not the
   current packet. Historical record; read-only here.

These are kotodama-owned documentation drift; they are recorded in the packet's
`open_questions` (OQ-E2E-03) and handed to the parent. Repairing
`handoff.md`/`README.md` prose is outside this design's file set.

## 8. Baseline, tamper control, and where it must not live

- **Path:** commit `reports/round-11/handoff/expected.json` (default), with
  `--baseline PATH` overriding so a later round can re-home it without touching
  the renderer.
- **Do not commit it under `tools/gates/expected/**` or
  `tools/gates/frozen/**`.** `tools/check-gate-battery.py` reads *every*
  `expected.json` under those roots as a gate baseline (`BASELINE_ROOTS` :114;
  discovery :388–395; validation :597, finding `BASELINE-GATE-UNCOVERED`); a
  baseline that names no gate from the seven-name `GATE_NAMES` tuple
  (:92–100) is a could-not-evaluate finding —
  the battery exits 2. The exercise is not a gate.
- **Shape** (freeze-manifest discipline, cf. `examples/culture-d3/expected.json`
  and `corpus/knowledge/verification/gate-frozen-run-standard.md` §4/§6):

```json
{
  "profile": "kotodama-handoff-e2e/1",
  "packet_id": "kotodama.handoff.d2d3-e2e",
  "packet_version": "1.0.0",
  "expected_exit": 0,
  "expected_finding_ids": [],
  "expected_scan": {"fields": "16/16", "glossary_entries": 20, "findings": 0},
  "packet_sha256": "<rendered packet digest>",
  "glossary_entry_ids": ["L01", "…", "L20"],
  "inputs": {"<repo-relative path>": "<sha256>", "…": "…"},
  "declared_expectation": "exit 0 / findings [] fixed before implementation; hashes measured from bytes, never generated from a printed verdict",
  "limits": "pins computational inputs only; not lore acceptance, not canon, not completion of the round arc; documentation surfaces excluded"
}
```

- The baseline pins bytes, so any renderer or read-set change is a PATCH that
  re-runs the gate first and records the reason — never a silent re-pin. The
  exercise's own script is not self-pinned (no self-digest cycle), but the gate
  script is pinned.
- **Tamper controls (in `--selftest`):** baseline digest edited inside an
  isolated copy → exit 2 with `E2E-BASELINE`, never a pass; a read-set file
  edited inside an isolated `--root` copy → exit 1 with `E2E-DIGEST`; a gate
  whose observed scan disagrees with `expected_scan` → exit 1 with `E2E-SCAN`.
- **Measured addendum (2026-10-17, this design pass, read-only):** during the
  round a sibling exercise baseline appeared at
  `tools/gates/expected/handoff-exercise/r11/expected.json`; running the
  battery's own `inspect_baselines` over the default roots then reported
  `BASELINE-GATE-UNKNOWN` plus `BASELINE-EXTERNAL-INPUT` ×5 for it (file still
  being written at the time, so counts are illustrative of the mechanism, not
  of its final contents). A default `python3 tools/check-gate-battery.py` run
  already reports `BASELINE-GATE-UNCOVERED` ×2 because the naming-collision and
  myth-consistency baselines live at `reports/round-9/baselines/`; the battery
  states `--baselines-root` "is not a way to silence a committed baseline"
  (:76). Placing the exercise baseline under a default root therefore cannot be
  neutralized by flags; `reports/round-11/handoff/expected.json` (or another
  non-gate root) keeps the exercise invisible to the battery by construction.
  This is reported for the O02–O05 owner and the parent to adjudicate; the
  design does not edit their file.

## 9. Selftest control matrix (positive + malformed; gate behavior measured, exercise-side rows designed)

Positive control, measured on the scratch prototype: exit 0, scan
`fields=16/16 glossary-entries=20 findings=0`, packet sha256
`a7defa9531dc5fa33465c6271f23e1148f5b50055dfc8398e18afe1eb224a0e1` reproduced
byte-identically on a second run.

| control | mutation of the rendered packet | expected | measured (proto) |
|---|---|---|---|
| malformed-01 | drop the `request_ref` row | exit 1, `HO-MISSING` | exit 1, `HO-MISSING` |
| malformed-02 | blank the `scope` value (`-`) | exit 1, `HO-EMPTY` | exit 1, `HO-EMPTY` |
| malformed-03 | write an unnegated `latest` into `dependency_manifest` | exit 1, `HO-DEP-FLOAT` | exit 1, `HO-DEP-FLOAT` |
| malformed-04 | remove every `not canonized` marker | exit 1, `HO-CANON-MARKER` | exit 1, `HO-CANON-MARKER` |
| malformed-05 | add `canon_standing: canonized by lore` | exit 1, `HO-CANON-CLAIM` | exit 1, `HO-CANON-CLAIM` |
| malformed-06 | set one etymology `status: invented` | exit 1, `HO-GLOSS-ETYM` | exit 1, `HO-GLOSS-ETYM` |
| malformed-07 | drop one glossary row | gate exits 0 — the **exercise** must fail it | gate exit 0 (gap §1.1); exercise assertion required |
| malformed-08 | hyphenate `## coupling_edges` | exit 1, `HO-MISSING` | exit 1, `HO-MISSING` |
| hazard probe | insert a `## scope-notes` heading | no gate finding; exercise must not emit it | exit 0, `scope` hijacked (§4b) |
| isolation probe | run from a foreign working directory | identical result | required in `--selftest` (foreign-cwd run) |
| preservation probe | snapshot the 21 read-set digests before/after | unchanged | required in `--selftest` |

## 10. Exercise interface (for O02–O05 and `run-validation.py`)

```
python3 tools/exercise-handoff-e2e.py                 # assemble -> gate -> baseline compare
python3 tools/exercise-handoff-e2e.py --selftest      # control matrix (§9)
python3 tools/exercise-handoff-e2e.py --root DIR      # alternate repo root (tamper controls, foreign-cwd)
python3 tools/exercise-handoff-e2e.py --baseline PATH # baseline override
python3 tools/exercise-handoff-e2e.py --keep          # keep the isolated packet dir
python3 tools/exercise-handoff-e2e.py --json          # one receipt document on stdout
```

- Exit codes: 0 clean (packet assembled, digests equal, gate exit 0, scan and
  baseline match); 1 mismatch/findings (`E2E-DIGEST`, `E2E-GATE`, `E2E-SCAN`,
  `E2E-COUNT`); 2 could-not-evaluate (`E2E-ARTIFACT` missing/unreadable,
  `E2E-BASELINE` absent/tampered, `E2E-DATA` malformed, I/O error) — stable
  messages, no traceback.
- Writes go only to a fresh directory under `TMPDIR` (the lane rule:
  `export TMPDIR=$PWD/.scratch`); the live read set is never touched, no
  network, stdlib only, no third-party YAML (the D2 packet is read as bytes and
  its `assembly.source_sha256` block is cited, not re-parsed; the
  JSON-formatted `typed-labels.d2.yml` is loaded with `json`).
- One stable summary line for `run-validation.py`, e.g.
  `handoff-e2e: exit=0 fields=16/16 glossary=20/20 findings=0 packet_sha256=<…>`.

## 11. Ordering, risks, open items

- **Ordering:** if claim D's wiring lands and changes `packet.d2.yml`,
  `typed-labels.d2.yml` bytes or the D2 tool digests, the baseline must be
  re-rendered and re-pinned **after** the D2 side stops moving (single
  integrator, one writer on `tools/exercise-handoff-e2e.py`); the packet's D2
  rows and `validation` numbers are computed from those bytes.
- **This file's footprint:** this design wrote only
  `reports/round-11/handoff/design.md` plus scratch files under `.scratch/`
  (prototype and rendered packet — not deliverables, excluded by `.gitignore`).
  Filed round-8/9/10 artifacts were read, never edited.
- **Open, non-blocking:** the §7 documentation drifts; whether the exercise
  should also carry D2's `D2L-FORM-UNRESOLVED` hold list verbatim into
  `validation` (currently counts + ids only) is left to the implementers with
  the constraint that the D2 hold set itself is claim D's deliverable.
- **Unverified here (`to-verify` for the implementers):** that the exercise's
  selftest can run with `TMPDIR` unset without failing on the exhausted `/tmp`
  inode table — the lane rule requires the redirect; do not rely on defaults.

## 12. Design evidence (commands and observed results, 2026-10-17)

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/proto-handoff-e2e.py
# --- gate exit: 0
# INFO scan: fields=16/16 glossary-entries=20 findings=0
# packet_id … table row line 11 … open_questions … section heading line 109

sha256sum .scratch/handoff-e2e/packet.md   # a7defa95… (139 lines), identical on a second run
```

Control probes ran the gate module in-process over mutated copies of the
rendered packet; the table in §9 records the observed ids and exits. Digests in
§2 were measured with `sha256sum` over the named paths at the same date. Counts
carry their command: 20 lexemes, 6 names, 7 utterances, 2 beliefs, 2 symbols,
3 materials, 4 objects, 4 costumes, 1 rank rule, 5 references, 5 bridges, 2
eras (`packet.json` list lengths); 58 labels / 46/10/2 by kind / 16 findings /
10 holds / 9 `R-MAT-BRIDGE-MISSING` (`typed-labels.d2.yml` `coverage` and
`era_material_reconciliation.summary`).
