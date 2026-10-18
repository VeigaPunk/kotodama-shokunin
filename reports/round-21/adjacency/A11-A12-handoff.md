# Round 21 adjacency — A11–A12 consolidated ledger and handoff verdict

- **Date:** 2026-10-18. **Scope:** Round 19/20 entry fragments, the ten new Round 19 corpus entries, all D4 artifact files, handoff v3, and `PROVINCE.md`.
- **Method:** source-boundary review, not external historical research, legal review, community consultation, canon adjudication, or a general quality audit. No Round 8–20 validator or Round 20/21 runner was invoked. No filed-round file was changed.

## Verdict

**ADJACENCY EXCEPTION — one D2-to-D4 fixture-boundary bleed is now explicitly filed; `unfiled_bleed=0`.** This is an intra-lane cross-culture contamination in the D4 typed-label projection, not a canon assignment, real-world rights/permission ruling, or game-mechanics claim. `PROVINCE.md` remains accurate for Kotodama's remit; no correction is proposed.

**Handoff v3 remains `prepared-not-accepted`.** Its computational envelope, uncertainty census, links, and deterministic projection checks pass, but the packet is deliberately unbound: no lore brief, baseline bible, or receipt surface exists, and bilateral acknowledgment of contract revision 1.0.0 is pending. A green shape/reproducibility check is not lore acceptance, canon, truth, or clearance.

## Dated inventory

At **2026-10-18T14:01:10Z**, the explicit `pathlib.Path.is_file()` inventory command recorded in `ledger.json` returned:

- Round 19 author fragments: **10/10**; reviewer fragments: **10/10**.
- Round 20 entry fragments: **4/4**.
- New Round 19 corpus entries: **10/10**.
- `examples/culture-d4/` regular files: **19**.

The ledger lists every counted path. The ten corpus entries are lane methods/workflows (verification and synthesis); the entry-level review found no canon promotion, real-world rights ruling, or gameplay mechanics. The Round 20 entry fragments are operational evidence and do not certify packet claims.

## D4 fixture-boundary finding

`examples/culture-d4/typed-labels.d4.yml` is not merely labeled with a stale D2 name. It contains D2 rank-rule data: the metadata identifies a D2 design projection at lines 28 and 329; its `rank_rules` block cites `examples/culture-d2/components/12-rank-rules.yml` and carries D2 ranks, statutes, garment materials, and dress-law content. The current generator hard-codes that D2 source and normalized rank rules (`tools/d2-typed-labels.py:925-1104`). D4's own component declares four RK records (`examples/culture-d4/components/09-costumes.yml:133-138`), while the projection says `rank_rules_component: 21`.

The numeric comparison and source-reference count were independently measured at **2026-10-18T14:05:45Z** with the Python command in `ledger.json` → `checks` → “D4 projection source/count comparison”: **D4 RK records=4; projection rank_rules_component=21; D2 rank-source references=24**. The D4-specific deterministic check at **14:01:09Z** (`python3 tools/gates/d4-typed-labels-check-gate.py`) returned exit 0 and “byte-identical deterministic projection.” That confirms reproducibility, not D4 isolation; the D4 brief explicitly bans D2 imports (`examples/culture-d4/components/01-brief.yml:61-67,111-121`).

The handoff already acknowledges that the D4 projection re-carries D2 normalization residuals (`reports/round-20/handoff/packet.md`, D4-CL09), so the issue is not wholly undisclosed. This ledger files the adjacency disposition and routes it to the Round 21 O/D4 projector owner; this A-seat does not repair the projection. The existing A01–A04 boundary receipt remains sound for canon/rights/game-mechanics categories, but its broad D4 pass did not catch this distinct intra-lane fixture contamination (`reports/round-21/adjacency/entries.md:56-62`).

## Round 19/20 and D4 boundary disposition

- The ten Round 19 corpus entries are in-province lane methods or verification workflows. Their individual paths and scope evidence are in `ledger.json` → `entries`.
- The inventoried Round 19/20 report fragments are non-canon engineering records. Reviewer notes on broken `couples` pointers (`review-C11.md`, `review-C16.md`), a superseded battery measurement/false absence sweep (`review-C14.md`), and false lexical absence sweeps (`review-C17.md`, `review-C20.md`) are listed as non-scope observations, not as bleed. Their current operational disposition was not independently re-run here.
- The D4 brief, components, packets, assembly record, README, and hold file otherwise keep canon with lore and disclaim real-world rights/permission/clearance claims. Fictional furnace rights and garment rules are in-world design, not rulings about real people or law.

## Handoff and Province checks

All commands below ran with `TMPDIR=$PWD/.scratch` and `PYTHONDONTWRITEBYTECODE=1` where scratch-writing behavior could apply.

- **2026-10-18T13:49:39Z** — `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0; **16/16** fields, **20/20** glossary entries, **0** findings, **105/105** links, **27** claims with status census **16/7/4**, v2 subset equal, alias leg landed.
- **2026-10-18T13:49:41Z** — `python3 tools/exercise-handoff-e2e.py --profile v3 --selftest` → exit 0; positive run plus **28** controls.
- **2026-10-18T13:56:40Z** — `python3 tools/gates/handoff-packet-check.py reports/round-20/handoff/packet.md` → exit 0, fields **16/16**, glossary entries **20**, findings **0**.
- **2026-10-18T13:56:40Z** — `python3 tools/harness/packet_uncertainty.py --packet reports/round-20/handoff/twin.json --require-oq --json` → **27** claims, no findings.
- **2026-10-18T13:56:40Z** — `python3 tools/harness/packet_links.py --packet reports/round-20/handoff/twin.json --json` → **105/105** links resolved, no findings.
- **2026-10-18T13:50:00Z** — `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → exit 0, **19/19** legs passed; holds remain design debt.
- **2026-10-18T14:05:45Z** — `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` → byte-identical deterministic projection. This does not negate the fixture-boundary finding above.
- **2026-10-18T14:05:45Z** — `git diff --quiet -- PROVINCE.md` exited 0; `git rev-parse HEAD:PROVINCE.md` → `313b182f251564b7997b06996b4f063370778f11`; the working-file digest was `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`. The contract digest was `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`. `git status --porcelain reports/round-{8..20}` returned empty output.

The handoff packet itself says contract **1.0.0**'s bilateral same-revision read is pending and declares `request_ref: none`, `baseline_bible_ref: none`, and no lore brief, baseline bible, or receipt surface (`reports/round-20/handoff/packet.md:1-16`). Contract §1 and §4 require both-lane acknowledgment and keep an unbound packet from canon import without a lore baseline and a new reviewed handoff (`corpus/knowledge/synthesis/worldbible-integration-contract.md:11-18,49-70`). Therefore the computational pass and the transfer decision remain separate.

## Filed artifacts

`reports/round-21/adjacency/ledger.json` contains the per-path inventory, scope/bleed flags, dated command results, and finding A21-D4-XF-01. At **2026-10-18T14:10:20Z**, the ledger's “Round 21 path and bleed census” command returned **53** unique paths, **1** filed bleed, and **0** unfiled bleed (10 corpus entries, 24 report-fragment rows, 19 D4 artifacts). It joins bleed rows to their filed finding IDs; this does **not** mean no bleed was found.

FILES: reports/round-21/adjacency/ledger.json, reports/round-21/adjacency/A11-A12-handoff.md | SUMMARY: D4 typed-label projection contains a filed D2→D4 fixture bleed; zero unfiled bleed, PROVINCE accurate, handoff remains prepared-not-accepted.
