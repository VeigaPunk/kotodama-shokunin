# Round-12 adjacency — A11–A12 consolidated ledger and handoff verdict

- Date: 2026-10-17.
- Scope: consolidate the R8–R12 adjacency record; check the landed R12 adjacency receipts against the cited artifacts and the R10 corpus additions.
- Method boundary: this is a source-boundary and handoff-envelope review, not a new audit of historical scholarship. R8–R11 adjacency statements are treated as prior reports, not as independent proof. No external historical sources were re-opened.

## Verdict

**REJECT — transfer is not proven and this packet is not an accepted handoff.** This verdict concerns the handoff only; it does not change any round-admission verdict or decide canon.

Reasons:

1. The required R12 A01–A04 new-entry audit receipts did not land by the bounded wait (through 2026-10-17T19:55:40-03:00). The final read-only inventory at 19:57:23-03:00 listed only `contract.md` and `province.md` in `reports/round-12/adjacency/`. The target assignment requires A01–A04 to cover all R10 entries and R11/R12 changes (`reports/round-12/targets.json:53-57`). This scribe independently inspected the ten R10 entries below, but that does not manufacture or stand in for the missing assigned receipts.
2. The R11 packet is explicitly an unbound, NON-CANON exercise with no lore brief, bible baseline, or receipt surface; it says `prepared-not-accepted` and bilateral reading is pending (`reports/round-11/handoff/packet.md:1-6,12-18,141-145`). Contract §1 requires both lanes to record their read before transfer, and §4 requires uncertainty in each claim ledger and typed, applicable, justified coupling edges (`corpus/knowledge/synthesis/worldbible-integration-contract.md:11-19,53-70`). The R12 contract audit independently found the uncertainty dimension absent and D2 coupling represented only as an aggregate edge (`reports/round-12/adjacency/contract.md`, “§4 field comparison,” especially lines 27-32). The shape gate does not close those findings.
3. A09–A10 found no province drift and recommends no Province correction (`reports/round-12/adjacency/province.md:3-7,9-25`); that is a positive boundary finding, not a lore receipt or transfer authorization (`reports/round-12/adjacency/contract.md:44-48`).

No canon assignment, real-world rights/permission ruling, or game-mechanics content was observed in the sources reviewed. That is a content-boundary observation only—not an acceptance, clearance, or permission ruling.

## R12 receipt ledger

| Assignment | Receipt state | Independent disposition |
|---|---|---|
| A01–A04 | **Missing at cutoff.** Assignment: `reports/round-12/targets.json:53-57`. | Not proven. The required new-entry receipt set is absent; the source-level check below is separately identified as this scribe’s work. |
| A05–A08 | **Landed:** `reports/round-12/adjacency/contract.md:1-6`. | Boundary conclusion is consistent with direct inspection: packet is an unbound exercise, not a canon or rights ruling. Contract conformance is **not** clean: missing claim uncertainty and aggregate D2 edge are confirmed against packet and contract. Bilateral acknowledgment remains pending. |
| A09–A10 | **Landed:** `reports/round-12/adjacency/province.md:1-7,9-31`, assigned in `reports/round-12/targets.json:63-65`. | Province remains accurate for the reviewed work; no correction proposed. Its own limits say this is a static audit and historical receipts were not rerun (`province.md:27-31`). |
| A11–A12 | This consolidated ledger. | **REJECT** the handoff on the evidence above. |

Receipt inventory command, run 2026-10-17T19:57:23-03:00:

```sh
python3 -c 'from pathlib import Path; p=Path("reports/round-12/adjacency"); print("\n".join(sorted(x.name for x in p.iterdir() if x.is_file())))'
```

Output: `contract.md`, `province.md`.

## Round ledger: prior assertions versus checked evidence

- **R8 — typed-label design and corpus metadata.** The prior X04 report recorded its own boundary/province pass and documented a contract metadata-header change plus an unresolved digest/acknowledgment question (`reports/round-8/adjacency.md:17-25,90-103,131-153`). Treat those as the R8 report’s findings, not a new independent audit. The R8 design spec itself marks the work NON-CANON and excludes canon decisions (`reports/round-8/depth/design-spec.md:1-14,64-69`). The latest R12 contract receipt still records the bilateral/L0 question as open in the latest available evidence (`reports/round-12/adjacency/contract.md:38-42`).
- **R9 — D3 acceptance work.** The prior X03 report recorded a boundary pass but also found a Kotodama-authored V09 fragment written into the parent repository (`reports/round-9/adjacency.md:18-26,191-214`). R10 X02 later reported that fragment relocated in-lane and the parent stray removed (`reports/round-10/adjacency.md:145-156`); these are historical reports, not a fresh process-attribution check. The D3 capability source describes a computational capability only—not lore acceptance, real-language clearance, cultural permission, or a universal validator—and says the packet is NON-CANON (`reports/round-9/d3/capability-draft.md:23-34`).
- **R10 — ten new corpus entries.** The previous X02 adjacency report claimed no canon assertion and Province accuracy at its stamped snapshot (`reports/round-10/adjacency.md:18-28,30-47,102-127`); it is not the missing A01–A04 receipt. The R10 admit commit’s file list was independently checked with `git show --format='%H %cI %s' --name-status 94ca098 -- corpus/knowledge` at 2026-10-17T19:49:12-03:00; it adds exactly the ten paths listed below. A direct boundary review of each path found no source making a world-canon assignment, a real-world rights ruling, or a game-dev mechanic. The targeted locators are listed in “R10 source check.”
- **R11 — typed pipeline and handoff exercise.** The prior X02 report called the boundary clean “so far” and described its seat-run gate result (`reports/round-11/adjacency.md:95-115,132-139`); that does not establish contract conformance or lore acceptance. The actual packet is expressly unbound and prepared-not-accepted (`reports/round-11/handoff/packet.md:1-6,12-18,141-145`). R12’s A05–A08 receipt identifies the claim-ledger and D2 edge gaps (`reports/round-12/adjacency/contract.md:13-32`), which this review confirms against packet `claim_ledger`/`coupling_edges` (`packet.md:75-103`) and contract §4 (`worldbible-integration-contract.md:63-66`). Separately, R12’s defect sweep records that the R11 craft round remains **REJECTED** on its F threshold; that round verdict is not the handoff verdict here (`reports/round-12/defects/sweep-r11.md:5,23-25,39-42`).
- **R12 — consolidation.** A05–A08 and A09–A10 landed; A01–A04 did not by the cutoff/inventory above. The R12 declaration assigns A11–A12 to the ledger/verdict (`reports/round-12/targets.json:67-69`). At 2026-10-17T19:57:23-03:00, both `git diff --name-status a3f6fcef2d92a1099581140c81d4264e9a4e2aa3..HEAD -- corpus/knowledge PROVINCE.md` and `git diff --name-status a3f6fcef2d92a1099581140c81d4264e9a4e2aa3 -- corpus/knowledge PROVINCE.md` returned no paths: no observed changes to `corpus/knowledge` or `PROVINCE.md` relative to the R12 baseline. `corpus/lessons/round-12.md:1-7,11-18,36-42` is a bounded survey: its 22:57:01Z listing found only the contract/province adjacency receipts and says A was not demonstrated because the entry-level bleed ledger was missing. This snapshot corroborates the receipt gap, but is not an A01–A04 receipt or a final round-admission verdict; it predates this A11–A12 file. The sibling-cleanliness caveat remains: `reports/round-12/scope.md:3-5,11-17` explicitly does not claim all siblings clean and does not attribute the active Lore worktree to Kotodama.

## R10 source check: boundary locators

The R10 additions were confirmed present as **10/10** by the read-only Python presence check reproduced from `reports/round-12/adjacency/province.md:18-23`, rerun at **2026-10-17T19:51:20-03:00**. The source boundary review is not an external fact-check.

- `corpus/knowledge/culture-material/transport-mobility-lexicon.md:20,22,122-129` — transport examples include historical bans and permits, but its handoff reserves routes and fictional ride permissions for lore and calls the entry a design instrument, not verified transport history. No real-world rights decision is made.
- `corpus/knowledge/culture-material/vessel-container-lexicon.md:25,169,174` — explicitly reference/method only; the worked example is NON-CANON and the handoff says unresolved items must not be promoted to world-fact.
- `corpus/knowledge/linguistics/language-shift-obsolescence-revival.md:167-184` — design decisions and handoff distinguish staging from world truth; real-world rights/attribution questions are routed out rather than decided here.
- `corpus/knowledge/linguistics/numerals-and-measures.md:170,199-207` — worked example is NON-CANON; method/reference material is handed to lore, which decides a given world’s system.
- `corpus/knowledge/linguistics/sound-symbolism.md:150-155` — method/reference only; real-world sacred/restricted-use rulings are explicitly out of province.
- `corpus/knowledge/myth-symbol/direction-symbolism.md:190-202` — fictional canon choices belong to lore; real-world sacred-practice permissions are explicitly not ruled on here.
- `corpus/knowledge/myth-symbol/divination-omen-systems.md:48,159-161,180,207,211,218` — no canon or predictive-truth claim; worked example is NON-CANON; restricted living-practice detail is bounded and canon adoption is lore’s. “Unplayable” at §12 is a design/narrative failure mode, not a videogame mechanic.
- `corpus/knowledge/myth-symbol/plant-symbolism.md:164-175,193-196` — the worked fixture is explicitly non-canon; the entry supplies reference/method and leaves naming, era, and canon decisions to lore.
- `corpus/knowledge/verification/header-conformance-readings.md:11,131,145,152` — the entry measures the corpus’s own provenance apparatus, says it certifies no historical or world-bible claim, and leaves fleet-level conformance to the integrator.
- `corpus/knowledge/verification/verification-independence-anti-circularity.md:31,151-159` — lane-local engineering discipline only; it claims neither a general research/verification standard nor canon authority.

Keyword-like terms are not themselves bleed: `numerals-and-measures.md:37` uses “mechanical consequences” for a linguistic system’s downstream effects; `divination-omen-systems.md:95-109,207` uses “rules,” “procedure,” and “unplayable” for the operation of a fictional divination institution. They are not game-dev mechanics. Historical laws, bans, and permit systems are described as reference examples, not as current legal or permission rulings; the contract expressly assigns real-world rights/permission decisions outside this lane (`corpus/knowledge/synthesis/worldbible-integration-contract.md:36-47`).

## Reproduced measurements

- **R10 additions:** `git show --format='%H %cI %s' --name-status 94ca098 -- corpus/knowledge`, 2026-10-17T19:49:12-03:00 → ten added paths (enumerated above).
- **R10 path presence:** Python presence command at `reports/round-12/adjacency/province.md:20-23`, rerun 2026-10-17T19:51:20-03:00 → `PRESENT_COUNT=10/10`.
- **Handoff shape only:** `export TMPDIR=$PWD/.scratch; python3 tools/gates/handoff-packet-check.py reports/round-11/handoff/packet.md`, rerun 2026-10-17T19:49:12-03:00 → exit 0, `fields=16/16 glossary-entries=20 findings=0`. This confirms shape/gate output only, not semantic contract conformance or acceptance; the same limitation is stated by the R12 contract receipt (`contract.md:7-10,15-32`).
- **Manifest digests:** the read-only inline Python checker and exact command are in `reports/round-12/adjacency/contract.md`, “Independent measurements,” item 3 (line 11). Re-run 2026-10-17T19:49:47-03:00 → `21 21 0` (file-backed rows, matching digests, mismatches). This verifies file digests, not record-count semantics.
- **Corpus/Province baseline:** the two `git diff --name-status` commands recorded in the R12 row above, 2026-10-17T19:57:23-03:00 → empty output.

## Conditions for a future ACCEPT

1. File the assigned A01–A04 source-specific receipts with resolvable source locators and findings; do not treat this report’s direct check or the old R8–R11 adjacency reports as substitutes.
2. Keep this packet classified as a successful non-canon exercise, not a transfer. Before a real transfer, close the claim-ledger uncertainty and coupling-edge findings, settle/freeze the exact packet bytes, record bilateral contract acknowledgment, and obtain the lore-owned receipt/disposition required by the contract (`reports/round-12/adjacency/contract.md:44-48`; `worldbible-integration-contract.md:11-19,53-70,92-106`).
3. No PROVINCE edit is indicated by the reviewed evidence (`reports/round-12/adjacency/province.md:3-7,27-31`).
