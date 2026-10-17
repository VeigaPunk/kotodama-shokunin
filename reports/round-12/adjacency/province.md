# Round-12 adjacency — province accuracy audit

## Finding

No province-related scope drift was found in the reviewed round-8 typed-label work, round-9 D3 acceptance work, round-10 corpus additions, or round-11 typed pipeline and handoff exercise. `PROVINCE.md` remains accurate; no correction draft is recommended.

The controlling text is `PROVINCE.md:9-14`: Kotodama owns its linguistic-cultural craft and records, lane-local gates, source-check records, examples and reports, while the verification/civilization partitions do not confer ownership of general research method, fleet protocol, historical-truth certification or lore canon. The adjacent-contract and write-boundary clauses at `PROVINCE.md:22-31` reserve lore decisions and require contested scope to be reported rather than absorbed.

## Comparison with the new work

- **Round 8 — typed labels:** `reports/round-8/claims.json:26-31` scopes D2 to a typed-label schema, reconciliation and adapter. The design record keeps this as a non-canon D2 drill and explicitly excludes canon decisions (`reports/round-8/depth/design-spec.md:4-6,64-69,546-558,680-682`). This is lane-local language/culture modeling and tooling, not an expansion into lore decisions or game mechanics.
- **Round 9 — D3 acceptance:** `reports/round-9/claims.json:26-31` covers deterministic assembly and evidence coupling for the D3 drill. The capability draft says the row is a computational capability only—not lore acceptance, real-language clearance or a universal culture validator—and retains unresolved findings (`reports/round-9/d3/capability-draft.md:23-34,239-251`). This fits the lane's own systems, gates and non-canon examples.
- **Round 10 — corpus entries:** the C declaration is for sourced knowledge entries in Kotodama’s linguistic, myth-symbol, culture-material and verification corpus (`reports/round-10/claims.json:11-15`). The entries inspected were `linguistics/{numerals-and-measures,language-shift-obsolescence-revival,sound-symbolism}.md`, `myth-symbol/{direction-symbolism,plant-symbolism,divination-omen-systems}.md`, `culture-material/{transport-mobility-lexicon,vessel-container-lexicon}.md`, and `verification/{verification-independence-anti-circularity,header-conformance-readings}.md`.
  - The language, symbolism and material-culture entries supply domain reference and craft methods, preserve uncertainty where stated, and route world-specific decisions to lore; they do not make canon, rights or game-mechanics rulings.
  - `verification-independence-anti-circularity.md:15,31,151,157` expressly limits its rules to lane-local engineering evidence and disclaims a general verification standard or canon authority.
  - `header-conformance-readings.md:11,32,97-102,141,145` is the boundary-sensitive item: it measures this corpus’s header readings and reports an open fleet-contract question. It explicitly blocks a fleet-level conformance ruling pending the integrator, says the lane does not amend or reinterpret the fleet sentence, and leaves the question open. Its lane-operative reading is local measurement guidance, not ownership of fleet protocol. This distinction is consistent with the existing province wording.

  Current-tree presence check for the named additions: **10/10 present**, read-only command from the Kotodama root at **2026-10-17T22:49:37Z** (the timestamp was emitted by `date -u '+AUDIT_UTC=%Y-%m-%dT%H:%M:%SZ'` immediately before this command):

  ```sh
  export TMPDIR=$PWD/.scratch
  python3 -c 'from pathlib import Path; p=["corpus/knowledge/linguistics/numerals-and-measures.md","corpus/knowledge/linguistics/language-shift-obsolescence-revival.md","corpus/knowledge/linguistics/sound-symbolism.md","corpus/knowledge/myth-symbol/direction-symbolism.md","corpus/knowledge/myth-symbol/plant-symbolism.md","corpus/knowledge/myth-symbol/divination-omen-systems.md","corpus/knowledge/culture-material/transport-mobility-lexicon.md","corpus/knowledge/culture-material/vessel-container-lexicon.md","corpus/knowledge/verification/verification-independence-anti-circularity.md","corpus/knowledge/verification/header-conformance-readings.md"]; [print(("PRESENT " if Path(x).is_file() else "MISSING ")+x) for x in p]; print("PRESENT_COUNT=%d/%d"%(sum(Path(x).is_file() for x in p),len(p)))'
  ```

- **Round 11 — typed pipeline and handoff:** the final D2 integration record identifies the landed adapter and gate as lane tooling, marks the evidence non-canon, and says holds remain open debt (`reports/round-11/depth/integration.md:9-22,27-36,74-95,273-275`). It records that the earlier `typed-gate-flow.py` prototype and its expected file were retired in conformance, rather than leaving that preliminary implementation as the delivered interface (`integration.md:17-19,50-63`). The handoff exercise builds a packet from live D2/D3 artifacts, tests it through the lane’s contract gate on an isolated copy, requires a non-canon marker, and disclaims canon decision and lore acceptance (`reports/round-11/handoff/impl.md:20-30,233-243`). This exercises the adjacent interface; it does not claim lore’s authority.

## Baseline and verification limits

`PROVINCE.md` was read directly and compared with the declared R12 baseline. `git diff --quiet a3f6fcef2d92a1099581140c81d4264e9a4e2aa3 -- PROVINCE.md` returned empty at **2026-10-17T22:49:19Z**; this confirms unchanged bytes, not accuracy by itself. The scope conclusion above comes from comparing the province clauses with the declarations and actual artifacts.

This was a static scope audit. I did not rerun the historical pipeline or handoff tests, and did not invoke any `reports/round-*/run-validation.py` runner. Historical receipts are cited only as documentation, not represented as current reruns.
