# 23 CRITIC — myth gate: does a clean verdict prove role coverage?

- wave: supplement-opencode-1 (not a numbered GLM round; not counted as reserved number)
- model: opencode-go/deepseek-v4.1-flash
- baseline revision: fe34faaafbe0add59ff68827a0df6c5782a72404 (`kotodama-shokunin` HEAD at write time)
- baseline binding check: the committed packet bytes (`git show fe34faa:examples/culture-d2/packet.d2.yml`) hash to the same `d5fb4088…` as the worktree specimen and also run clean; the gate file itself is byte-identical between commit and worktree (sha256 `26d246e9…`, the same value pinned in `tools/gates/frozen/round-3/MANIFEST.tsv`), so the probes and the frozen replay measure the committed baseline artifacts even though sibling workers have since modified other worktree files (`06-pantheon.yml`, `07-myths-motifs.yml`, `assemble-d2.py`).
- specimen: `examples/culture-d2/packet.d2.yml`, sha256 `d5fb408871dcb985c2f9b134a26c6d64e8640a6f1f17ba1c6bb3c5db1d6dbd96`
- gate under test: `tools/gates/myth-consistency-gate.py` (spec: `corpus/knowledge/verification/myth-consistency-gate.md`)
- role/scope: critic; read-only over the packet and gate; no edits outside this report and `reports/supplement-opencode-1/scratch/23-myth-coverage/`

## 1. Verdict

**No.** A clean verdict proves the ledgers that were *submitted* are complete *columns* —
every record carries a status mark, a resolvable agent, a landscape-era key, a scoped exception —
and, per the spec, that nothing supplied asserts a rule it contradicts at the same scope. It does
not prove the ledger covers the culture's dependencies.

The decisive measurement: the baseline packet carries 23 `roles` records; deleting any one of
them — including the two that name an exclusive agent with substitutes denied — leaves the verdict
clean (exit 0, zero findings). Deleting **all** of them leaves the verdict clean, because an empty
`roles:` list is falsy and therefore takes the same branch as a missing key, where the `MC-P00`
"no role ledger" finding is suppressed. The same holds record-by-record for the whole ledger set:
23/23 role deletions, 10/10 symbol deletions, and 9/9 motif deletions each return a clean verdict.

The spec itself governs the limit (§3: "Start from the proposed society's dependencies and claims,
not a mandatory sky/earth/war/love roster… The rows above are prompts, not universal religious
needs", lines 49). The kernel implements the *conditional* half of §3 — "for every record the
designer submitted, is its mark honest?" — and nothing implements the *unconditional* half.
Coverage of the dependency space is a review judgment, not a mechanical one, and the design's
blank-slot thesis (`06-pantheon.yml`: "deliberate blank slots, not archetype completion") is only
checkable against a pinned dependency inventory that does not exist in the packet today.

## 2. Mechanism (why the blind spot exists)

`check_pantheon()` (`tools/gates/myth-consistency-gate.py:421`) opens with
`if not not_applicable and not roles:` (line 447) — a falsy `roles` value emits `MC-P00`. An empty
list is falsy, so an emptied ledger reads as "ledger absent" and is then *not* compared against the
pantheon's other records. Every later check in the function is per-record and conditional on the
record being present; the same shape holds for `check_motifs()` (per-motif) and `check_symbols()`
(per-entry). There is no oracle in the kernel for the spec's §3 prompt rows — no token list, no
required dependency set, no "n of m present" report. Deleting a record removes the only surface the
checks could act on, and nothing records what was deleted.

## 3. Counterexample matrix (actual command, observed result)

Commands (scratch scripts committed with this report):

```
python3 reports/supplement-opencode-1/scratch/23-myth-coverage/probe-role-coverage.py
python3 reports/supplement-opencode-1/scratch/23-myth-coverage/probe-drop-matrix.py
```

Observed (in-memory `gate.evaluate`, mutated deep copies; no file writes outside scratch):

| Probe | Stated result |
|---|---|
| baseline packet | findings `[]`, exit 0 |
| delete `storm-law-oath` (exclusive, no substitute) — 22 roles kept | `[]` |
| delete `salt-road-exchange` (exclusive, substitute denied) — 22 kept | `[]` |
| keep only `storm-law-oath` — 1 role | `[]` |
| keep only `sky-and-stars` — 1 role (`NON-DIVINE`) | `[]` |
| drop-one matrix, roles | 23 deletions, 23 clean verdicts, 0 noticed |
| drop-one matrix, symbols | 10 deletions, 10 clean verdicts, 0 noticed |
| drop-one matrix, motifs | 9 deletions, 9 clean verdicts, 0 noticed |
| `roles: []` (empty list) | `['MC-P00']` — but "no role ledger present", not a coverage finding |
| roles key absent (control) | `['MC-P00']` — identical wording; the two states are indistinguishable |

The gate does catch mutations on records that remain: a fabricated agent name (`Vantanu` for
`Kahatu`) emits `MC-P00` ("lists agent(s) absent from the pantheon"). So the blind spot is specific
to record *removal*, not to content checking — which is exactly what makes it dangerous: the
mutation that removes the evidence is the one that cannot be seen.

## 4. Frozen replay (does the clean verdict travel?)

The round-3 frozen baseline is re-executable and deterministic against the current gate:

```
python3 tools/gates/myth-consistency-gate.py \
  tools/gates/frozen/round-3/inputs/examples/culture-d2/packet.d2.yml
```

- observed: `exit 1`, one finding line — `MC-S00` under-normalized symbol keys: in the round-3
  snapshot packet the symbol records carry no `medium` key at all (frozen packet, `symbols:` line
  1258ff), so every key is incomplete; the re-checked predicate `"missing medium" in <output>` is
  true;
- recomputed output sha256 `ea56c2d3cd712864e55ff9a1fc3fc5cad1848b3999389cf33ace8bf76eb771cf`
  matches the recorded `output_sha256` in `tools/gates/frozen/round-3/MANIFEST.tsv` and the frozen
  `myth-consistency-gate.out` bytes — the gate grades the tree it is run on, and the replay is
  reproducible.

The round-4 frozen output (`tools/gates/frozen/round-4/myth-consistency-gate.out`) is a 0-byte
file; `wc -c` reports 0. A 0-byte file is consistent with a clean (exit 0) run but does not itself
pin the exit code, and the round-4 frozen directory carries no `MANIFEST.tsv`/inputs — so I record
the round-4 "myth gate clean" as *consistent with, not established by* the artifact. The baseline
worktree packet does run clean (`exit=0`, no output). The honest record: the round-3 snapshot was
dirty (1 finding) and the baseline packet is clean; the correction happened between snapshots, and
this critic does not claim which commit did it.

## 5. What a clean verdict legitimately proves

- Every submitted role record uses one of the five spec marks, has a resolvable agent or a declared
  non-divine mechanism, and (for `SHARED`) a jurisdiction note; `UNKNOWN` records carry a basis or
  evidence pointer. A record whose `basis` is elite-text-silence alone would emit `MC-P02`.
- Every submitted motif law with an `asserts_law: true` variant either has a consistent event or a
  bounded exception; every claimed index comparison carries checked entry + edition + witness.
- Every submitted symbol key is complete (5 fields) or reported; duplicate normalized keys with
  incompatible exclusive defaults are flagged (`MC-S01`).

That is a clean **column** result. It is compatible with the packet describing an arbitrarily
small slice of the culture, and compatible with the removal of any subset of its records.

## 6. Recommendation (design-side, not a patch to this kernel)

1. Pin a dependency inventory per culture revision in the packet (`dependencies:` list or the
   assembler's manifest) and have a future kernel report inventory-vs-ledger coverage as a HOLD,
   not a FAIL — the spec's rows are prompts, so "relevant" stays a review judgment.
2. Record every ledger deletion as an explicit state (`status: RETIRED` with basis) rather than by
   removing the record; a record that vanishes cannot be graded, and a record that stays can.
3. Keep the current kernel semantics: they are the right *conditional* checks; the missing half is
   the inventory. Adding a naive "all six rows must appear" gate would violate §3's own warning
   against imposing a universal pantheon — this lane explicitly does not require universal
   pantheons or unique symbols across all contexts.

## 7. Source rechecks (freshness axis, required round record)

Actual retrievals at 2026-10-17; search snippets and unretrieved pages are not counted as
confirmation. `retrieval_status` values: `retrieved-html`, `retrieved-binary-pdf-no-text`,
`blocked-429`.

| id | claim rechecked | entry locator | source_url | retrieval_status | source_locator | source_excerpt | verdict | basis / access_limit |
|---|---|---|---|---|---|---|---|---|
| KA-P01 | "**Uther (2024)**, revised and supplemented edition, The Kalevalaseura Foundation: [publisher's edition notice]" exists as cited | `corpus/knowledge/verification/myth-consistency-gate.md` §10 Uther bullet (lines 193–195; source list line 3) | https://www.folklorefellows.fi/ffc-284-286-2024-edition/ | retrieved-html | page heading + three part blocks | "FFC 284–286 (2024 edition) … Revised and Supplemented Edition, 2024 … The Kalevalaseura Foundation … Part I … Folklore Fellows' Communications 284" | supported | Full page text retrieved and read. The entry's disclaimer is kept: the notice verifies the revision and index purpose, **not** that any individual 2024 entry was consulted; the page lists part contents but not entry wording. |
| KA-P02D | Language/myth/era/dress coupling: the Greek-dress survey supplies the named garment terms used by the §7 reference packet (peplos: heavy wool, overfold *apoptygma*, shoulder pins; chiton: lighter, usually imported linen, girded) | same entry §7 "Costume/material signature" row (line 150) and §10 Met bullet (line 200) | https://www.metmuseum.org/essays/ancient-greek-dress | blocked-429 | — | — | unresolved | HTTP 429 (rate-limited) on 2026-10-17; no page text retrieved, so the cited passages cannot be confirmed this wave. Entry already marks the essay as consulted 2026-10-17 and says object-level evidence is still required per garment — that caveat is preserved. Recheck on a fresh pass. |
| KA-P03 | Turner 1973 *Science* 179: 1100–1105 is the page-level locus for the multivocality restatement behind §6 | same entry §6 (line 117) and §10 Turner (1973) bullet (line 201) | https://www.amherst.edu/system/files/media/1479/Symbols%2520in%2520African%2520Ritual_0.pdf | retrieved-binary-pdf-no-text | — | — | unresolved | The URL resolves but the response is raw PDF bytes; extracted text was not available, so the quoted restatement and page range were **not** re-confirmed. Recorded as unresolved, not as verified; page-level claims in the entry remain at their original status. |

No erratum is warranted: KA-P01 is supported as cited, and the two unresolved rows preserve the
entry's existing `(to-verify)`-style caveats rather than changing them. The rechecks tested a
bibliography fact (KA-P01) and a language/myth/era/dress coupling (KA-P02D), the latter resolving to
an access limit rather than a full-text confirmation — the correct outcome to record.

## 8. Limits of this critique

- The deletion probes are in-memory mutations of the baseline packet — they demonstrate what the
  kernel cannot see; they do not claim the D2 authors intended those records to be removable, and
  nothing here is a defect finding against the round-3/4 workers.
- "Coverage is not mechanically decidable" is a design consequence of the spec's own §3 stance;
  the drop matrix bounds the claim to *record removal*, and the fabricated-agent control shows the
  kernel is not blind to content.
- Freshness was limited by access: one retry of the Met essay was rate-limited, and the Turner PDF
  returned binary bytes. Neither outcome is treated as confirmation; both stay unresolved and
  should be re-attempted on a later pass.
