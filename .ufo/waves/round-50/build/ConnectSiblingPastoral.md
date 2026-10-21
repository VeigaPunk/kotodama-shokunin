# ConnectSiblingPastoral — round 50, claim C: sibling-lane ownership sweep and handoff boundary

Seat: `ChousaR27R2.ConnectSiblingPastoral-4` (leaf; no delegation, no background jobs). Lane: kotodama-shokunin, base `4ad26836552462d28a946ca3b067cab0b5ce3532`. Read-only over sibling lanes; no production file edited; no git/jj mutation; **no tool installed or updated** (nothing needed). Report is author-lane advice, not admission.

## Verdict

**No sibling lane under `/home/vgpnk/Projects/shokunin/*-shokunin` owns pastoralism, herding, husbandry, transhumance, or livestock — as a filename, a topic line, or a knowledge entry.** The fleet has **no history lane and no ecology lane**; the 20 sibling lanes are craft, records, and tooling lanes (domain lines below). The only cross-lane boundary kotodama must respect is therefore **function-based, not topic-based**: lore owns canon records, chousa owns research method, game-dev owns game mechanics. That boundary is already stated in kotodama's own contract; the new entry must cite it, not renegotiate it.

One first-order risk surfaced: lore's intake of kotodama packets is **unacknowledged and uncovered** (`CM-g`), so the new entry must hand off *without* claiming that lore will import anything.

## Evidence — the sweep (run this session at base 4ad2683, repo-only)

| Test | Command (abbreviated) | Result |
|---|---|---|
| Filenames, all sibling lanes | `find /home/vgpnk/Projects/shokunin/*-shokunin -path '*/.git' -prune -o -path '*/.ufo' -prune -o -type f \( -iname '*pastoral*' -o -iname '*herd*' -o -iname '*husband*' -o -iname '*transhuman*' -o -iname '*livestock*' -o -iname '*shepherd*' \) -print` | **0 files** |
| Find-expression control | same find on `lore-shokunin` for `-name 'README.md'` | 185 files — the expression/prune is live, so the 0 above is a real 0 |
| Topic owners, all sibling lanes | `grep -rniE --include='*.md' '^- topic:.*(pastoral\|herd\|husbandr\|transhuman\|livestock)' <20 lanes>` | **0 lines**, rc 1 |
| Body owners, word-boundary, all files | `grep -lIiE '\b(pastoral(ism)?\|transhumance\|agropastoral\|husbandry\|herding\|herder\|shepherd(ing)?\|nomad(ic\|ism)?\|livestock)\b'` over every file in the 20 lanes (excluding `.git`, `.jj`, `.ufo`, `node_modules`) | **1 file**, a false positive: `mado-shokunin/plans/round-5-record-draft.md:54` — the word "herder" is a script's self-label ("its herder self-labels 'round 5 / M5-2'"), not content |
| Adjacent-vocabulary sweep | `\b(pasture\|grazing\|cattle\|sheep\|goat\|camelid\|camel\|reindeer\|yak\|wool\|dairy)\b` over the same 20 lanes | Only false-positive classes: `chousa-shokunin` camel-**case** (`corpus/knowledge/scope-phrase-gap-r18.md:33`, `corpus/README.md:689`, `LOG.md:680`); `game-dev-3d-shokunin` collision-**grazing** (`corpus/fixtures/README.md:397,405`, `corpus/fixtures/shapecast3d_graze.gd:1,32`, `corpus/lessons/r42-graze-review.md:14`); `flock(2)`/`herdThreshold` in chousa/kagi/kumitate (syscall and throttle vocabulary). No husbandry content. |
| Kotodama-side register census | `find corpus/knowledge -iname '*pastoral*' -o -iname '*husband*' -o -iname '*herd*'` | 0 — consistent with `reports/round-50/claims.json` before-checks |

Sibling lanes swept (21 dirs, 20 excluding kotodama): audio, chousa, game-dev-2d, game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kengaku, kotoba, kumitate, lore, mado, mori, revenger, souji, tabi, tameshi, tsukuroi.

## Why no history/ecology lane exists — domain census (read-only)

- `lore-shokunin/PROVINCE.md:3` — "fictional-world records — entities (characters, places, factions, items), relations, timeline events — with consistency verification and sourced inspiration".
- `chousa-shokunin/PROVINCE.md:3` — "deep-research method … the reusable craft of source research".
- `tabi` browser/web craft (`PROVINCE.md:3`); `mori` fleet/host observability (`:3`); `kagi` secrets/vault (`:3`); `kotoba` prompt/skill craft (`:3`); `kengaku` LLM research/eval (`:3`); `mado` desktop/compositor (`:3`); `souji` repo hygiene (`:3`); `tameshi` verification fixtures (`:3`); `kumitate` orchestration/tooling (`:3`); `kake` web properties/publishing (`:3`); `kaidoku`/`revenger` reverse engineering (`:3`); `kasegi` bounty/security (`:3`); `kama` local model serving (`:3`); `audio` game audio (`:3`); `game-dev-2d`/`game-dev-3d` game production (`:3`); `tsukuroi` host operability (`:3`).
- `MANIFEST.json` roster (13 minted lanes) likewise names no history/ecology domain; the 21 directories are the authoritative present set.

Consequence: there is **no sibling knowledge path to cite, mirror, or avoid duplicating**. The entry's "coupled to another lane" language must point only at the lore/boundary contract, never at an invented sibling corpus entry.

## The real owners (function, not topic)

| Lane | What it owns (exact anchor) | Boundary kotodama must respect |
|---|---|---|
| **lore-shokunin** | world-bible records, relations, chronology, canon decisions, bible-wide consistency (`PROVINCE.md:3`); refuses "claiming canon without an in-world citation" and "silently resolving contradictions" (`PROVINCE.md:9`); writes only its own repo, sibling repos read-only (`PROVINCE.md:11`) | The entry supplies **reference method only**; which herds, breeds, routes, offices and words exist in-world is lore's. Handoff names recipient + open questions; no canon assertion. `PROVINCE.md:28` already maps kotodama's *owned surfaces* for lore (names/dates, naming, calendars) — pastoralism must join that map only as a supplied method, never as a lore surface. Identity check: the on-disk lane is `lore-shokunin/` but its remote repo is `shokunin-world-bible` (`git -C lore-shokunin remote -v` → `.../shokunin-world-bible.git`; `MANIFEST.json` roster `id: lore`); handoff prose should name the **lane**, and lore supplies its own bible/receipt paths (`worldbible-integration-contract.md:68`). |
| **lore-shokunin (intake state)** | `corpus/README.md:73` — "CM-g … intake of kotodama handoff packets \| **uncovered** \| none in lore knowledge or SKILL"; `:79` — "contract `kotodama-lore-adjacency` sits at unacknowledged digest 5f4c02bf… and lore holds zero durable-surface acknowledgement records"; `PROVINCE.md:19` — "CM-g kotodama packet intake stay `uncovered`" | **Activation is pending.** kotodama's contract says "Initial bilateral acknowledgement is **pending** until those records exist" (`corpus/knowledge/synthesis/worldbible-integration-contract.md:15`) and "an unbound research packet … cannot be imported as canon without a lore baseline and a new reviewed handoff" (`:69`). The new entry's handoff must say **pending/unacknowledged**, not "lore will import". |
| **chousa-shokunin** | general research method — question framing, source hierarchy, citation chaining, claim-vs-source verification (`PROVINCE.md:3`) | The entry applies the lane's own `QUALITY.md` / `SOURCES.md` discipline; it makes no research-method claim. Contract states this split at `worldbible-integration-contract.md:4` ("lore-shokunin owns canon, chousa owns general research method, integrator arbitrates contested scope"). |
| **game-dev-2d / game-dev-3d** | game production and mechanics verification (`PROVINCE.md:3`); game-dev-2d refuses "narrative canon (lore lane — contested scope is reported, not absorbed)" (`:10`) | Pastoralism as a *game system* (herd sim, breeding mechanics) is theirs; the entry is cultural-production reference method, not mechanics. lore `PROVINCE.md:9` confirms the split by refusing "game mechanics verification (game-dev-2d)". |

## Handoff boundary the entry must state (concrete)

1. **No sibling topic owner exists.** State the fleet sweep result once (0 filename/topic owners across 20 sibling lanes) and stop; do not cite a sibling "partial owner" that does not exist. Kotodama-internal partial owners are a different table (already handled by `CriticGapPremise.md`).
2. **Do not invent sibling paths or tools.** `worldbible-integration-contract.md:68` — "Do not invent a sibling path or tool and call it established." The handoff may name the contract (`kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md`), which lore itself points at (`lore-shokunin/PROVINCE.md:28`), nowhere else.
3. **Recipient + open questions, no canon assignment.** Use the established entry convention: `hunting-foraging-subsistence.md:205` ("Handoff: lore-shokunin owns which subsistence system exists in-world, who hunts and gathers, and which patches are sacred or owned"), `cartography-and-mapmaking.md:239`, `bathing-and-body-hygiene.md:141`, and the decision-row form at `agrarian-field-system-lexicon.md:162` (DR-AG-10: "Hand off as design instrument; no canon assignment … handoff names recipient and open questions"). For pastoralism the open questions are at minimum: species/breed choice, mobility regime, pasture tenure, herd ownership/transfer rules, and whether any real ethnographic case is being imported or only used as method.
4. **Mark intake as pending, not available.** Because lore's `CM-g` is uncovered (`lore-shokunin/corpus/README.md:73,79,94`; `PROVINCE.md:19`) and the contract's bilateral acknowledgement is pending (`worldbible-integration-contract.md:15`), the handoff line should say the packet is a *candidate* under an unacknowledged contract digest — never "lore will record/accept".
5. **No reciprocal edits.** C lands only `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` and `corpus/README.md` (`claims.json` C.lands). The partial-owner boundaries are therefore one-way citations; any edit to `agrarian-field-system-lexicon.md`, `semantic-fields-lexicon-building.md`, `animal-symbolism.md` or `transport-mobility-lexicon.md` would be a new claim, not part of C. This also keeps Ca's counterfactual trees clean (`tools/check-claim-separability.py` reads `lands`).
6. **Research-method and mechanics claims stay out.** Cite `QUALITY.md` criterion 6 for tiers; cite source-discipline entries for method; do not add a research-method rule (chousa) or a mechanics rule (game-dev).

## Prior-round records the claim should not ignore (calibration)

- `reports/round-35/plan/P01-c-plan.md:158` names `C02 pastoralism-husbandry-lexicon` with mentions/owners `23 / 0`, and `:203-224` already fixes the "Owns" list (herd species/product chains, transhumance and pasture law, breeding/castration vocabulary, fodder/wintering, herd disease, pastoral/settled interface, herd markers, herd counting) plus its extend-not-restate couples. This is the strongest prior art for §2 and §3 — reuse it, don't re-derive it.
- `reports/round-44/scout/K02-gap-scout.md:73` — Pastoralism/husbandry: filename 0, topic 0, prior status "**named** r35 CM-2", verdict "**carried — reject**". Round 50 is therefore **the first round deliberately reviving a carried gap**. The entry's gap line and the round lesson should record that revival (and why) so a future scout does not read r50 as a fresh discovery or as a contradiction of r44.
- `reports/round-35/cov/C02-entry-2.md:16` — the r35 "C02" draft is the **agrarian** entry (`# Agrarian Field-System Lexicon …`), not a pastoral draft, despite the plan's slot name. There is no pastoral draft in `reports/` to duplicate or resurrect; the new entry is genuinely new bytes.
- `reports/round-49/claims.json:30`'s sentence that adjacent registers own "pastoral" is stale (no owner then or now). Do not cite it as a prior owner; the peer `CriticGapPremise.md:52` already records this, and this sweep independently confirms it at fleet scale.

## Affected axes and the one bounded move

- **Coverage (primary):** an explicit sibling-boundary paragraph prevents the entry from either (a) claiming it is the first mention fleet-wide (false) or (b) inflating scope into a "pastoralism" blanket that duplicates six kotodama partial owners. The gain stays the comparative production-system register, which is genuinely unowned.
- **Operability (unchanged):** no tool, gate, or sibling path is touched; C's lands remain two paths, so Ca's static leg and O's sandboxes are unaffected.
- **Calibration (improved):** citing `r44:73` (carried), `lore CM-g` (unacknowledged), and the contract's pending-acknowledgement clause makes the handoff honest about what lore can actually do this round.

**Proposed move (bounded, one):** in the entry's §2/§15 handoff, add a three-sentence "sibling-lane boundary" block: (i) fleet sweep shows 0 sibling-lane owners of this register (no history/ecology lane exists; the only hits are false-positive vocabulary), so no sibling citation is owed; (ii) lore owns canon and its kotodama-packet intake is **unacknowledged/uncovered** (`CM-g`), so this is a candidate method handoff naming recipient and open questions, not an import; (iii) chousa owns research method and game-dev owns mechanics, so neither is claimed here. No new files, no reciprocal edits.

## Risks

- **Carried-gap tension:** r44 explicitly rejected this candidate as carried. A reader can read r50 as ignoring the registry. Mitigation is the explicit revival sentence above, not silence.
- **Handoff over-claim:** the tempting sentence "lore will record the herd" is exactly what `CM-g` forbids; the contract's pending acknowledgement (`:15`) and `:69` make an import claim unsupported.
- **False-owner inflation:** the fleet sweep's only textual hit is mado's "herder" self-label; if a future census greps without word boundaries it will manufacture an owner (the `sherd`→`herd` trap already recorded in `CriticGapPremise.md:15`). Use word-mode plus filename/topic modes, and keep the control count.
- **README placement:** with the current 27 culture-material files, `pastoralism-animal-husbandry.md` sorts between `music-instrument-lexicon.md` and `ritual-garments.md`; the index row must go there (filename order), not at the section end.

## Verification (what I ran, and what I did not)

Run this session: the four sweep commands and the control above; `sed`/`grep` reads of every cited `path:line`; lane domain lines; `MANIFEST.json` roster read (read-only). No external URL opened (repo evidence only), so no SOURCES tier is asserted here. Install record: none.

Unrun: I did not run the lane selftests, the README sweep, the new entry's anchors, or Ca/O gates — out of this seat's scope. I did not write or edit any production file, and I did not message peers (no coordination dependency found; the peer `ChousaR27R2.ScribeSec02Boundary-4` report already covers kotodama-internal partial owners with live anchors, which this report complements rather than replaces).
