# 24 — Baseline assembler and costume gate: rank-rule / material-ledger coverage

- wave: `supplement-opencode-1` (not a numbered GLM round; no promotion consequence)
- baseline revision: `fe34faaafbe0add59ff68827a0df6c5782a72404` (repo HEAD at read time; worktree was clean apart from the untracked `reports/` this wave creates)
- scope worked: `tools/assemble-d2.py` (baseline assembler) and `tools/gates/costume-era-consistency-gate.py` (the costume gate), read at the baseline revision; the assembled packet `examples/culture-d2/packet.d2.yml` was read, never written
- assigned write: this file only; scratch evidence under `reports/supplement-opencode-1/scratch/24-costume-coverage/`
- author-side evidence: no `SHONEN.md` box is checked here and nothing in this report promotes a rank

## 1. Method and commands actually run

| # | command | observed result |
|---|---|---|
| 1 | `python3 tools/assemble-d2.py --check` | `packet.d2.yml: byte-identical deterministic assembly`, exit 0 (no write) |
| 2 | `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d2/packet.d2.yml` | no output, exit 0 |
| 3 | `sha256sum examples/culture-d2/packet.d2.yml` | `d5fb408871dcb985c2f9b134a26c6d64e8640a6f1f17ba1c6bb3c5db1d6dbd96` — identical to the wave's baseline pin `baseline.d2_packet_sha256` in `reports/supplement-opencode-1/claims.json` |
| 4 | `python3 tools/gates/costume-era-consistency-gate.py --selftest` | `self-test: 10/10 checks passed; fixture exit 1 with 21 planted finding IDs`, exit 0 |
| 5 | `python3 reports/supplement-opencode-1/scratch/24-costume-coverage/run-contrast.py` | 9/9 cases matched expected exit code and finding IDs (full output: `scratch/24-costume-coverage/contrast.out`) |
| 6 | `python3 reports/supplement-opencode-1/scratch/24-costume-coverage/d2-coverage-census.py` | census + reachability guards (full output: `scratch/24-costume-coverage/census.out`) |
| 7 | `git status --porcelain`, `git diff --stat` | clean except untracked `reports/`; no live component modified |

Command 4 has a side effect that must be on the record: `selftest()` (gate lines 1452–1457) does `os.makedirs(FIXTURE_DIR)` and then **writes** `tools/gates/fixtures/costume-era-consistency-gate.{yml,expected}` in the live tree. After I ran it, both files hashed byte-identically to `git show fe34faa:<path>` (`36d92113…` / `4b0724f9…`) and the worktree stayed clean — the write is a no-op only while the script's in-file `FIXTURE` constant and the committed fixture agree. A selftest that rewrites the committed fixture can silently re-bless a drifted fixture; fleet gate standard requires isolated fixtures with no live-tree write. Recording, not fixing (the gate is not my write scope).

The round-3 frozen costume run (`tools/gates/frozen/round-3/costume-era-consistency-gate.out`, 10 × `G-ERA [hold]`) shows the gate does go red on this packet lineage; the round-4 frozen run (`tools/gates/frozen/round-4/costume-era-consistency-gate.out`, 0 bytes) is the green one. Note for the operability owner: `frozen/round-4/` carries `.out` files only — no `MANIFEST.tsv`, no `inputs/`, so that green is not digest-pinned where it sits (round-3's manifest pins input `54be6319…`, an older packet than HEAD's `d5fb4088…`).

## 2. What the green run does and does not cover

The gate's 21 finding IDs are all implemented and all are exercised by the committed fixture (command 4), so the question is only which of them the *assembled D2 packet* can reach. Reachability below is read off the gate's own guards (`evaluate()`, lines 593–1010) and the packet's keys (census output), not off the gate's silence.

| finding ID | D2 status | reason |
|---|---|---|
| G-ERA | reached (10 rows) | every row declares an era in `eras` |
| MAT-01 | reached, not fired | no row names a `VAGUE_MATERIALS` entry without composition |
| MAT-02 | reached (10 rows) | reject branch live: 2 ledger entries carry `excluded_eras` (both `E0`-excluded, both worn in `E1`) |
| MAT-03 | reached (10 rows) | 7 `local-production`, 3 `import` rows all matched to their routes |
| MAT-04 | reached (2 rows) | `dye: hearth-dark` on `GAR-02`, `GAR-05` |
| MAT-05 | **unreached — adapter** | needs packet `supply` (quantified demand + route outputs). Assembler emits no `supply` key; component 10 declares prose `supply_state` only, so no quantities exist to adapt yet |
| MAT-06 | **unreached — adapter + component** | needs a reuse/heirloom/stock claim: no row declares one, and 10's declared `reuse` route (`smith-scale`, MAT-19, flagged in its `reuse_rule`) never enters the packet ledger |
| MAT-07 | reached (5 rows) | 5 rows carry `closures` |
| EAR-01 | reached | availability `no-era` path live |
| EAR-04 | **unreached — adapter** | needs `rank_rules`; key absent |
| E-01 | **unreached — adapter ×2** | needs costume `processes` (0 rows) *and* `era_dates`: the assembler deliberately renames 09's non-CE block to `source_era_dates` (assembler normalizations, line 132), and the gate reads only `era_dates` |
| T-01 | reached (1 row) | `GAR-01` body felt panel 1.7 m seamless vs 1.9 m felt table → no finding |
| T-02 | **unreached — component** | no row carries `features`/`fit` |
| T-03 | **unreached — adapter** | needs `rejection_rules`; key absent |
| R-01…R-06 | **unreached — adapter** | need `rank_rules`; key absent (see §3) |
| R-03 (badge branch) | **unreached — component** | badge branch is independent of `rank_rules`, but no row carries `badge`/`badge_office` |
| R-07 | **unreached — adapter** | rule-level prereq loop; key absent |
| G-DATA | n/a | well-formed packet |

Counted plainly: 10 of the 21 IDs could not run on the D2 packet because the assembler does not emit the block they read — R-01…R-07, EAR-04, MAT-05, T-03 (and E-01, which is doubly blocked: no `processes` row and the renamed `era_dates`); two more could not run because no costume row carries the optional field (T-02; R-03's badge branch); and MAT-06 because no row claims reuse while component 10's reuse route was left un-unioned. The green run is a statement about ~10 costume rows against 9 ledger entries — not about the D2 law, not about the era model.

**A green gate is not historical authenticity.** Command 2's exit 0 means "no contradiction inside the checks that ran". It does not mean the costume system is right, dated, or lawful; the rank-rule dimension — the one that makes a wardrobe a *social* system — is exactly the part that did not run.

## 3. Rank-rule checks: unreached because the law is not translated

The gate reads rank rules only from `rank_rules` (`normalise_rules`, lines 462–492; documented at lines 65–75: `rules`, `claims` "are tolerated and not read"). The assembler's `take()` set (lines 84–108) never touches `examples/culture-d2/components/12-rank-rules.yml`, and its own `assembly.unresolved` says so (line 138): *"12 prose rank rules are not translated into executable rank_rules; R-checks are unevaluated"*. The omission is a missing **translation**, not a lost copy: 12's rule records carry `id, sign_axis, prescription, assay, authority, jurisdiction, era, era_history, enforcement_reality, sanction, follows, garment_refs, precedent_via_corpus` — no `effect`, no `property: {kind, value}`, no `wearer_ranks`. The components do carry the coupling by id (`11-costumes` rows carry `rule_edges: ["WR-01","WR-06",…]`; 12 carries `garment_refs` with `appears_in`); no block on either side, or in the packet, is what the gate reads.

Two consequences are worth separating:

1. **Silence by absence** — with no `rank_rules`, R-01…R-06, R-07 and EAR-04 cannot fire. A rank-rule conflict like "a herd-master wears what only the lineage head may wear" cannot be expressed in the packet at all.
2. **Silence by value form** — even a mechanical export of 12's rules would not couple to 11's rows. `wearer_rank` and `rite` values are prose (e.g. `GAR-01.wearer_rank`: "any adult of a pasture-holding lineage, at the low pole (…)"); the R block matches `key(wearer) == key(w)` against rule tokens, so a rule scoped to `herd-master` simply skips the row (`continue`, line 904–906) instead of raising R-06. Unmatched scope reads as "rule does not apply", never as "cannot resolve".

### The minimal lawful/violation contrast (scratch, no live component touched)

Same packet four times; only the rank-rule plumbing changes (files in `scratch/24-costume-coverage/`):

| packet | difference | exit | finding |
|---|---|---|---|
| `rank-lawful.yml` | rule `WR-1` prohibits `felt` for `herd-master`; wearer is `wind-speaker` | 0 | none — control: the check ran and found the rule inapplicable |
| `rank-violation.yml` | same rule, wearer `herd-master`, `claimed_status: lawful` | 1 | `R-02 [reject] … applicable prohibition WR-1 (Valley Moot) covers felt, and the packet claims unqualified lawful entitlement with no exemption on record` |
| `rank-omitted.yml` | the violation row with `rank_rules` deleted (the D2 shape) | 0 | none |
| `rank-prose-wearer.yml` | the violation row with `wearer_rank` in 11's prose form | 0 | none |

The pair is lawful-versus-violation on identical costume data; the third row is the D2 green reproduced minimally, and the fourth shows the second-order gap. Material-ledger controls run the same way: `ledger-cover.yml` (route `eras: [E0]`, costume `E0`) → exit 0; `ledger-miss.yml` (route `eras: [E1]`) → exit 1 `EAR-01 [hold]`; `ledger-rename.yml` — the same miss written with a route key the gate does not read (`era_scope`) → exit 0, a vacuous pass. That last one is a generic hazard of splicing any unadapted block: component 10's `materials` routes do use the gate's `eras` key (all 29 routes verified), but its bulk rows use `era_scope` and live outside `materials` by its own `gates_interface` note.

## 4. Material ledger: what the missing union costs

- The packet ledger is 11's 9 records (`wool, felt, pack-ox down, leather, horn, lowland plant-thread cloth, lowland cord, silk, hearth-dark`). Component 10 supplies 22 `MAT-*` records plus 6 bulks, and its `gates_interface.splice_blocks` states a packet "can splice … `materials:` … from this file unchanged". The assembler's `assembly.unresolved` (line 139) records that it did not: *"10 material inventory is not unioned into 11 costume-facing routes; silk/down slot conflicts remain"*.
- **Not a mechanical copy.** Two of 11's nine entries carry `maps_to: null` with "REPORT, do not merge" (`CMAT-03` pack-ox down; `CMAT-08` silk — 10 has no silk record, and its luxury import is `lowland-broadcloth` on a different era mapping). And the era vocabularies collide: 10's `interface_facts.era_slots_assumed: [E1…E4]` are slot ids ("shelter / road / assembly / script") that its own note says must be mapped to 09's names, while 09/11/12 use canonical `E0…E3`. An unadapted union would inject 10's `E1` exclusions (e.g. `MAT-05` `excluded_eras: [E1]`) as canonical `E1` — a reject-grade claim about the wrong era. The union is a design act with an open question attached, not a merge script.
- **Reject-grade inventory left on the table.** 10 declares `excluded_eras` on 12 records and its `closed_inventory_rule` says such a hit "is a real contradiction (reject), not a missing datum". In the packet, only 2 ledger entries carry `excluded_eras`; the reject severity of MAT-02/04/07 is therefore largely unexercised for D2, and one of the defects the R-dimension should catch (a later-era good claimed early) is precisely what 10's excluded-eras table was built to make decidable.
- **MAT-05 has nothing to read.** The gate's strongest contradiction test (minimum demand > maximum feasible supply, lines 985–1010) needs quantities; 10 offers `supply_state` prose and 6 bulk records with `measure_note`, and no component declares demand or route outputs. The omission is honest, but the quantitative dimension of the spec is untested for D2.

## 5. Limits of this review

- Static guard reading plus CLI runs; I did not enumerate the gate's internal states by mutation testing for every ID (the fixture is the positive control for all 21).
- I did not verify the assembler's `reader_sha256`/`source_sha256` pins against a re-run of every source file; only the packet digest was checked (command 3).
- I did not evaluate the other four gate outputs in the round-4 frozen directory, nor the naming-gate failures visible there (`NAME-NEAR`, `PHON-INVENTORY` on `GAR-*` garment glosses) — those belong to other lanes' scopes; they are worth a look because the same packet that is costume-clean is name-dirty.
- Nothing was changed in any live component; the scratch packets and scripts are the only new files besides this report.
- **Concurrency caveat.** All measurements above were taken while the worktree matched `fe34faa`. Other workers in this wave have since begun editing `tools/assemble-d2.py` (adding a selftest per the operability claim), `corpus/` entries and `examples/culture-d2/components/06-pantheon.yml` / `07-myths-motifs.yml`. The surfaces this review measured are still at baseline digests — `packet.d2.yml` `d5fb4088…`, gate `29a9361c…` (the same gate hash round-3's frozen manifest pins), fixtures `36d92113…`/`4b0724f9…` — but every assembler line number cited here is the baseline file's, and re-running commands 1/5/6 after the assembler change lands may read a different script.

## 6. Source recheck (role duty) — retrieved audits

Two concrete claims were rechecked against actually retrieved public sources; one test exercises language/rank/dress/era coupling, the other era/material/dress coupling. Search snippets, blocked fetches and metadata are not counted as confirmation. JSON blocks below are the assigned record; the parent folds them into the wave's `sources/` aggregate (no unassigned path was written).

```json
{
  "wave": "supplement-opencode-1",
  "baseline_revision": "fe34faaafbe0add59ff68827a0df6c5782a72404",
  "entry": "corpus/knowledge/verification/costume-era-consistency-gate.md",
  "entry_sha256_before": "9a5982cf2aee742ce702ccbffdec717889a3d6c987d9e32628ecd9c0aa761aef",
  "checked_at_utc": "2026-10-17T15:42:59Z",
  "audits": [
    {
      "id": "24-A1-CG-S",
      "claim": "[S] Perkin synthesized mauveine in 1856 and opened the factory in 1857 — the anchor the gate uses for 'mauveine' and the entry's worked check that a specified 1840 mauveine route rejects",
      "entry_locator": "§1 source key [S] (line 14); §11 worked check 'Perkin's commercially supplied mauveine in 1840' (line 187)",
      "source_url": "https://www.sciencehistory.org/education/scientific-biographies/william-henry-perkin/",
      "retrieval_status": "retrieved (full page text, 2026-10-17)",
      "source_locator": "body, section 'A Happy Accident: Mauve'",
      "source_excerpt": "In 1856 ... 18-year-old William Henry Perkin (1838-1907) synthesized mauve, or aniline purple - the first commercialized synthetic dyestuff ... In 1857 he opened his factory at Greenford Green, not far from London.",
      "verdict": "supported",
      "basis": "Retrieved page states both dates the entry attributes to [S]; the gate's PROCESS_ANCHORS text (1856 synthesis / 1857 factory) matches.",
      "access_limit": "Institutional author with no publication year, as the entry itself notes; no independent second source for the factory year was retrieved in this pass."
    },
    {
      "id": "24-A2-CG-L",
      "claim": "[L] the apparel proclamation is Greenwich, 15 June 1574; it exempts 'a servant ... wearing any cognizance of his master' beside henchmen, heralds, pursuivants at arms and apparel given by the Queen; it distinguishes fabric, garment placement, degree, income and service, and adapts Henrician/Marian statutes",
      "entry_locator": "§1 source key [L] (line 11); §6 closing paragraph (line 118); §10 rows 'Symbolic system' and 'Era model' (lines 170-171)",
      "source_url": "https://www.elizabethan.org/sumptuary/who-wears-what.html",
      "retrieval_status": "retrieved (full transcription text, 2026-10-17)",
      "source_locator": "header line; preamble; note following the men's clauses",
      "source_excerpt": "[Greenwich, 15 June 1574, 16 Elizabeth I] ... the meaning of this order is not to prohibit a servant from wearing any cognizance of his master, or henchmen, heralds, pursuivants at arms",
      "verdict": "supported",
      "basis": "Retrieved text carries the date/place header and the cognizance exemption with henchmen/heralds/pursuivants; it also names income thresholds (100 pounds, 300 marks, subsidy book), garment placements and the Henrician/Marian moderation clause, matching the entry's coupling and rank-rule readings; the exemption names no badge device, matching the entry's absence claim over this document.",
      "access_limit": "The retrieval is a third-party transcription; the printed Hughes & Larkin pagination anchors (II.381/384/386) rest on Bolland 2011 / Cotter 2021 / Kirtio 2011 and were NOT re-verified here - those page anchors stay unresolved."
    },
    {
      "id": "24-A3-CG-B",
      "claim": "[B] 'Spun silk is made from short lengths obtained from damaged cocoons or broken off during processing, twisted together to make yarn' — the corroboration the T-03 false-positive guard rests on",
      "entry_locator": "§1 source key [B] (line 16); §5 row 'Reeled silk' (line 83); §11 worked check (line 183)",
      "source_url": "https://www.britannica.com/technology/spun-silk-yarn (live: HTTP 403, 2026-10-17); retrieved via https://web.archive.org/web/2024/https://www.britannica.com/technology/spun-silk-yarn",
      "retrieval_status": "live page blocked (HTTP 403); full article text retrieved from an Internet Archive snapshot of the same URL (snapshot year 2024; exact capture timestamp not exposed by the fetch tool)",
      "source_locator": "article body, 'sericulture' inset",
      "source_excerpt": "Spun silk is made from short lengths obtained from damaged cocoons or broken off during processing, twisted together to make yarn.",
      "verdict": "supported",
      "basis": "The archived article states the discontinuous-fibre definition verbatim as quoted; it also classifies silk yarn thickness by denier, not by reeling, so 'silk is never spun' remains a false rejection rule.",
      "access_limit": "Confirmation is by archived copy, not the live page; the snapshot's exact date is not resolvable with the tools used, so the citation should read 'archived copy, 2024 capture year'."
    }
  ]
}
```

```json
{
  "wave": "supplement-opencode-1",
  "baseline_revision": "fe34faaafbe0add59ff68827a0df6c5782a72404",
  "entry": "corpus/knowledge/culture-material/dress-through-eras.md",
  "entry_sha256_before": "3b24cb4c9c8747f3cc0dd9d59d9226c3078281ed014873039cd23bea0ac32ea7",
  "checked_at_utc": "2026-10-17T15:42:59Z",
  "audits": [
    {
      "id": "24-A4-DTE-SILK",
      "claim": "'silkworm eggs smuggled to Byzantium c. 552 ends the Chinese-Persian monopoly (Procopius, Wars 8.17)' — the era/material/dress chronometer (same anchor as the gate's c. 552 silk-reeling entry)",
      "entry_locator": "§3 'Silk as chronometer' (line 37); also corpus/knowledge/culture-material/textile-technology.md line 21, §3",
      "source_url": "https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Procopius/Wars/8C*.html",
      "retrieval_status": "retrieved (full chapter text, Dewing/Loeb translation, 2026-10-17)",
      "source_locator": "Wars VIII.17.1-7 (Loeb pages 227-231); context anchor VIII.15.12 (page 211)",
      "source_excerpt": "At about this time certain monks, coming from India ... they then once more went to Serinda and brought back the eggs to Byzantium",
      "verdict": "supported",
      "basis": "The passage supports the episode (monks from India, country of Serinda, eggs brought to Byzantium, silk produced in Roman territory from then on) and its citation to Wars 8.17; the corpus's c. 552 sits in the right narrative position because VIII.15.12 dates the surrounding truce to Justinian's 25th regnal year. Two words in the claim are not in the retrieved text: 'smuggled' (the narrative is an imperial negotiation; no concealment is described) and 'Chinese' (the passage names Serinda and the Persians, not China).",
      "access_limit": "Dewing's English (LacusCurtius) read; the Greek text and the scholarship behind the c. 552 convention were not retrieved, so the framing words above stay open."
    },
    {
      "id": "24-A5-DTE-SILK-YEAR",
      "claim": "the absolute date 'c. 552' is attributable to Procopius, Wars 8.17",
      "entry_locator": "§3 (line 37); gate anchor table 'byzantine-silk-reeling: 552' in tools/gates/costume-era-consistency-gate.py line 520",
      "source_url": "https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Procopius/Wars/8C*.html",
      "retrieval_status": "retrieved (same chapter)",
      "source_locator": "Wars VIII.17.1 ('At about this time'); VIII.15.12 (25th regnal year)",
      "source_excerpt": "At about this time certain monks, coming from India",
      "verdict": "unresolved",
      "basis": "VIII.17 states no year; the chapter carries only 'at about this time'. The 552 figure depends on converting VIII.15.12's 25th regnal year of Justinian and on later scholarship, neither settled by the retrieved text. The event is supported; the date's attribution to the source is not.",
      "access_limit": "No source for the dating convention was retrieved in this pass; the corpus date should keep its uncertainty rather than be read as quoted from Procopius."
    }
  ]
}
```

Errata: none appended. The only corrections this review supports are (a) the framing words in the silk chronometer claim (§6, 24-A4/A5) and (b) the coverage readings in §2–§4; both are reported here rather than written into corpus files, since no corpus path is in this worker's write scope.
