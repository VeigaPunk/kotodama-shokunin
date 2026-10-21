# ReviewSourcesContract — round-50 frontier (SOURCES contract)

- Seat: ChousaR27R2.ReviewSourcesContract-4 · leaf reviewer · read-only · no subagents, no background jobs.
- Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin · base 4ad26836552462d28a946ca3b067cab0b5ce3532 · working tree read 2026-10-21. No git or jj command was run. Only this file was written.
- External URLs opened by this seat: none. No SOURCES row was written or verified here.
- Axes: coverage · operability · calibration.
- Where each requested item sits: grammar §1 · values §2 · used-by and status §3 · lesson `## Gate` §4 · census commands and results §5 · next free id §6 · r49 rows §7. Findings §8, moves §9, candidate mistakes §10, limits §11.

## 0. Answer summary

- **Next free id: S048.** Registry S001–S047 is contiguous with no duplicates (census 5). No `S048`+ text exists in `corpus/`, `tools/` or `reports/`. Two scout drafts already claim S048 for different sources (§6). L1 must assign.
- **Census is green on the lane tree** (7 of 7 commands, §5). All 47 Gate bullets carry an ISO access date and a quote of at most 25 words.
- **If the new entry cites only S048+ rows, zero r49 rows change `used-by`.** No r49 row has pastoral, herding, livestock, steppe or transhumance scope. Conditional candidates are in §7.
- **P0 (F1):** as written, Ca cannot detect the defect it exists to detect. C.lands omits the registry, the Gate and the lesson index, and the frontier is not in the manifest. Once mined rows name the C entry, the r49 reverse leg fails too (no mined row names it yet).
- **P0 (F3):** claims.json has no `exports`, `tree` or `acceptance`. "Exits 0 on claims.json" would therefore be vacuous.
- **P1 (F2):** the r49 runner is round-locked (`opened` must equal 2026-10-19; lesson = round-49.md). Run on round-50 rows it goes red or checks the wrong file.
- **P1 (F14):** both S048 drafts support identity or object scope only. Neither carries a herding-management content claim.

## 1. Row grammar — 11 columns

Header (`corpus/SOURCES.md:28`) and separator (`:29`), verbatim:

```
| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
```

Each row has 12 pipes, 11 cells, and awk `NF==13` (census 2). Cell rules (`CORPUS.md:89–108`):

1. **id**: `S` plus 3 or more digits. Next unused, never reused, no `|` in any cell.
2. **source**: title — canonical URL or DOI (repo path or command for `own-work`).
3. **kind**: see §2.
4. **tier**: A, B or C, scoped to `scope`. `community` is never A. No NATO or GRADE labels.
5. **scope**: the claim or topic the tier applies to.
6. **anchor**: exact section, heading, page or line, plus a revision (version, commit or publication date). Never a bare homepage.
7. **teaches**: one grounded learner benefit. Rejected rows read `REJECTED: <reason>; flip: <what would change the verdict>`. A correction row opens `supersedes S0NN —`.
8. **status**: see §2.
9. **opened**: ISO date the row's author opened the source.
10. **recheck**: ISO date or cadence. The contract's examples are `90d`, `180d`, `on-release`. The registry also uses `365d` (`round-49.md:89`).
11. **used-by**: comma-separated repo-relative paths, or `—`.

Shape example: `corpus/SOURCES.md:71` (S042).

## 2. Allowed values

| column | allowed | enforced by census today |
|---|---|---|
| kind | spec · docs · paper · code · tool · dataset · talk · book · community · own-work | yes (census 6) |
| tier | A · B · C; `community` never A | yes (census 6, tier-inflation) |
| status | queued · mined · rejected | yes (census 6) |
| opened | ISO date | no. Checked by hand: 47/47 pass |
| recheck | ISO date or cadence | no. Checked by hand: 47/47 pass |
| teaches, rejected rows | starts `REJECTED:` | no. S047 fails (F5) |
| used-by | paths, or `—` | paths exist only (census 7) |

Status meanings (`CORPUS.md:103–104`, `SOURCES.md:19–21`): `queued` = opened, worth mining. `mined` = cited by at least one path in `used-by`. `rejected` = kept with reason and flip; a rejection is evidence of taste.

Observed: 22 queued, 20 mined, 5 rejected. Every queued and rejected row has `used-by` `—`. Every mined row has at least one path.

## 3. used-by and status rules

- **Path rule.** Mined rows' paths must exist (census 7 checks existence only).
- **Citation rule, as written.** `used-by` is "repo-relative paths of the knowledge entries or lessons citing the row" (`CORPUS.md:107–108`).
- **Practice.** `used-by` lists knowledge entries only. Lessons cite every row through their Gate: S044 appears at `round-49.md:79` and `:308`, with `used-by` `—`. A literal reading would make each row mined by its own Gate line. Treat the reading as knowledge-only and state it in the round-50 Gate (F11).
- **Citation test, not checked.** The r49 integrator's class lesson says: "a substring hit on a site name is not a citation of the row's scope — a mined row's `used-by` must cite the catalogue/dataset/work the row scopes" (`round-49.md:99–100`). The census does not check this. It is manual.
- **Id test, not checked.** Eight of 20 mined rows have `used-by` paths containing zero occurrences of their S-id: S001, S002, S003, S007, S008, S013, S016, S018. Their paths cite the source by name: Glottolog, WALS/PHOIBLE/Rosenfelder, TMI, ATU, D-PLACE, da Silva/Tehrani (F6). The twelve S031–S042 rows are cited by id from `hunting-foraging-subsistence.md`.
- **Post-landing change rule.** Only `status`, `recheck` and `used-by` change in place. Each change is logged old→new in the round lesson (`CORPUS.md:116–117`; precedent `round-49.md:84–113`). Tier, anchor and teaches changes need a superseding row (`QUALITY.md:29`; `CORPUS.md:117–118`).
- **Correction rule.** A correction is a new row whose teaches opens `supersedes S0NN —`. Examples: S044→S034, S045→S038, S046→S039, S047→S029 (`SOURCES.md:73–76`).

## 4. Lesson `## Gate` format

- **Heading and extent.** `## Gate` (`reports/round-49/run-validation.py:215`, regex `^## Gate[ \t]*$`). The section runs to the next `^## ` heading. `###` subsections are allowed. r49 uses `### Post-review supersession rows — opened 2026-10-19` (`round-49.md:77`).
- **Lead paragraph.** Names the opening seat, the date and the quote rule (`round-49.md:20–25`).
- **One bullet per new row.** r49 form (`round-49.md:29`):

  `- S0NN — <canonical URL or DOI> — accessed <YYYY-MM-DD> — <section/page/para>: "<verbatim quote, ≤25 words>". Grounds <what the row supports>.`

  Corrections add `; supersedes S0NN at tier B` (`round-49.md:79`).
- **What the runner checks.** Only that each registry id starts a line `- S0NN ` inside the section (`run-validation.py:210–221`). It does not check the access date, quote length, verbatim status or tier.
- **What I measured on the r49 section.** 47 of 47 bullets carry `accessed 20YY-MM-DD`. Quotes are at most 25 words: the maxima are S006 and S043 at 25, and S032 at 24.
- **Template drift.** `build/ScribeLesson.md:53` wraps URL and quote in backticks and appends `Tier: <A|B|C> per QUALITY criterion 6`. That is not the r49 form. Use the r49 form; tiers live in the registry (M11).
- **Companion sections.** A lesson that mines mistakes also carries `## Mistakes`: rows of class · evidence pointer · captured-by · fix (`CORPUS.md:171–178`). Class vocabulary: vacuous, survivor, stale-premise, reference-drift, number-drift, scope, attribution, landing, provider.
- **Index.** `corpus/lessons/README.md` needs one row per lesson file. A lesson that lands after its stamp adds a row (`:301–304`). No round-50 row exists yet (F8).

## 5. Census commands (verbatim, `CORPUS.md:134–147`) and results today

```sh
# rows (spacing-tolerant)
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
# malformed rows — 11 columns means NF=13; must print 0
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
# tier histogram
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
# status histogram
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
# duplicate ids — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | sort | uniq -d
# enum violations and tier inflation — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; gsub(/[[:space:]]/,"",i); gsub(/[[:space:]]/,"",k); gsub(/[[:space:]]/,"",t); gsub(/[[:space:]]/,"",s); if (t !~ /^[ABC]$/) print "tier", i, t; if (s !~ /^(queued|mined|rejected)$/) print "status", i, s; if (k !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/) print "kind", i, k; if (t=="A" && k=="community") print "tier-inflation", i}' corpus/SOURCES.md
# mined rows whose used-by paths do not exist — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {s=$9; gsub(/[[:space:]]/,"",s); if (s=="mined") {n=split($12, a, /[,;]/); for (j=1;j<=n;j++) {p=a[j]; gsub(/^[[:space:]]+|[[:space:]]+$/,"",p); if (p!="" && p!="—") print p}}}' corpus/SOURCES.md | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
```

| # | check | result today | pass rule |
|---|---|---|---|
| 1 | rows | 47 | ≥ 1 |
| 2 | malformed (NF≠13) | 0 | 0 |
| 3 | tier histogram | A=34 B=6 C=7 | — |
| 4 | status histogram | mined=20 queued=22 rejected=5 | rejected ≥ 1 (runner) |
| 5 | duplicate ids | empty | empty |
| 6 | enum / tier inflation | empty | empty |
| 7 | mined `used-by` paths missing | empty | empty |

Also: knowledge entries 225, culture-material 27. Both match `claims.json:16`. The census was tested only on a synthetic table (`CORPUS.md:131`). I ran it on the working tree and did not compare against base 4ad2683.

## 6. Next free id

- **S048.** Evidence: registry ids are S001–S047, 47 unique values, so contiguous (census 5 empty). `grep S048` over `corpus/`, `tools/` and `reports/` returns nothing.
- **Collision.** Two drafts already claim S048 for different sources:
  - `.ufo/waves/round-50/build/SrcDysonHudson.md:44`: Dyson-Hudson & Dyson-Hudson 1980, "Nomadic Pastoralism", *Annual Review of Anthropology* 9:15–61. Kind paper, tier A, scope identity only. The row says it "carries no content claims".
  - `.ufo/waves/round-50/build/SrcUnescoGer.md:11–16`: UNESCO ICH element 00872, Mongol ger. Kind docs, tier A. Scope excludes "pastoral ecology, herd management or transhumance". Its own text says "`status: mined` and `used-by` are correct only once claim C's entry text actually cites it".
- Two more scouts (FAO pastoralism, Bedouin) appear on the peer roster but have no draft on disk. I did not review them.
- **Rule.** Ids are never reused (`CORPUS.md:89`). Precedent: r49 renumbered fragment ids contiguously at merge (`round-49.md:21–24`). L1 assigns S048+ at merge; drafts use temporary ids (M2).

## 7. r49 rows whose `used-by` would change if the new entry cites them

- **Default (entry cites only S048+ rows, as the design requires): none change.**
- **Conditional, if the entry cites an r49 row.** Each row below is scope-adjacent only. None has pastoral scope. Each change must be logged old→new in round-50.md.

| row | status now | used-by now | fit for a pastoralism entry | change if cited |
|---|---|---|---|---|
| S007 D-PLACE 2026, root dataset | mined | `linguistics/kinship-terminology.md` | dataset-level only. A pastoral variable needs its own opened row, as S042 shows | used-by += entry path; stays mined |
| S023 Cliopatria 2025, polity dataset | queued | — | the ≥5000 km² and ≥50-year polity threshold (`round-49.md:52`) excludes many mobile polities. Caveat needed | queued → mined; used-by = entry path |
| S040 Binford 1980, mapping-on / logistics | mined | `culture-material/hunting-foraging-subsistence.md` | hunter-gatherer settlement frame. Transfer to herders must be argued, not sourced | used-by += entry path |
| S044 Kelly 2013 (tier B) | queued | — | foraging spectrum; forager scope | queued → mined |
| S046 Stephens & Krebs 1987 (tier B) | queued | — | optimal foraging models; use for grazing is an argument, not the source's claim | queued → mined |
| S001 Glottolog | mined | `naming-systems.md`, `zapotec-mixtec.md`, `moche.md` | languoid identity for named groups only | used-by += entry path |

- **Do not cite.**
  - S042: EA001 gathering dependence. A pastoral dependence claim needs its own EA-variable row, which would be S048+.
  - S028, S029, S030, S043, S047: rejected, so not evidence.
  - S034, S038, S039: superseded by S044–S046 at tier B. Cite the superseder.
  - S009, S011: tier C. Lead only, never sole support.
- **Pending residual, not caused by the new entry.** `hunting-foraging-subsistence.md` still cites S034 (lines 18, 20, 96, 104, 116, 187, 189), S038 (18, 20, 185, 197) and S039 (18, 20, 188). S044–S046 are queued with `used-by` `—`. Repointing would change `used-by` for S034, S038, S039 (mined → queued where no citer remains) and for S044–S046 (queued → mined), all logged (F7, M8).

## 8. Findings (ordered by severity)

**F1 — P0 · calibration · separability.** `claims.json:18`: C.lands = [entry, `corpus/README.md`]. `:17`: every cited S-id must resolve to a SOURCES row whose `used-by` names the entry. `:10`: "C's entry cites SOURCES rows opened by the frontier step (not a claim)".
- The frontier is not in the manifest, so Ca's pairwise check never sees C→frontier.
- The r49 S-without-C leg (`run-validation.py:301–305`, `:322–324`) fails whenever a mined row's `used-by` names the C entry. The registry then depends on C while C depends on the registry, so the pair is inseparable under the checker's own semantics.
- This is the r49 REJECTED-HONEST-STOP (`corpus/lessons/round-49-verifier-spotcheck.md:17`) reintroduced under a new label.
- The only exit-0 design under the shared contract is to fold the frontier into C: `corpus/SOURCES.md`, `corpus/lessons/round-50.md` and the lessons index row (M1). O and Ca land disjoint paths (`claims.json:37`, `:51`), so folding does not couple them to C.

**F2 — P1 · operability.** `run-validation.py:49` LESSON = `round-49.md`. `:209` `opened_ok` requires every opened cell to equal `2026-10-19`. `:233–236` `s_ok` includes `opened_ok` and the round-49 lesson check. Run on round-50 rows, the S leg reports red, or it validates the wrong file. Fix with a parameterized round-50 census (M3). Do not edit the round-49 runner.

**F3 — P0 · calibration · Ca input.** claims.json top-level keys: round, campaign, coordinator, declared_at_utc, baseline_commit, axes_in_play, lowest_axis_reasoning, freshness_pause_in_force, separability_contract, claims, non_goals. Grep for `exports`, `tree` or `acceptance`: 0 hits. The shared contract requires per-claim `exports` and a `tree` commit. The lane workflow produces patches under `.ufo/waves/round-50/patches/<NAME>.patch`, not per-claim commits. With no exports the checker finds no dependency, so "exits 0" is vacuous. Fix: a `kotodama-separability-manifest-v1` file with exports and per-claim trees built from scratch clones. The checker should exit 2 when a claim has no exports (M5).

**F4 — P1 · calibration · before-check.** `claims.json:21` declares `"mode": "word"` with targets {pastoralism, pastoral, herding, husbandry, transhumance, livestock}. `:22` evidence_command is `grep -rniE '^- topic:.*(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/`, a substring match with a different list.
- It returns `corpus/knowledge/culture-material/writing-media-surface-economy.md:3`, matched inside "sherd" (the topic lists "sherd, wall, pot, body").
- A word-mode grep over the topic lines returns nothing. The claim "no topic owner" holds. The literal evidence contradicts `expect: true`.
- Fix: rebuild evidence_command from the spec list with word boundaries (M4).

**F5 — P2 · grammar.** `SOURCES.md:76` (S047): status rejected, teaches opens "supersedes S029 —" rather than `REJECTED:`. Rejected rows read `REJECTED:` (`CORPUS.md:101–102`). Corrections open `supersedes` (`:117–118`). The contract has no form for a rejected correction. Neither rule is census-checked. The contract is frozen (`CORPUS.md:66–68`). Record the exception in round-50.md and propose contract v2 wording (M6). Do not edit S047 (append-only).

**F6 — P1 · calibration, latent.** Eight of 20 mined rows have zero S-id occurrences in their `used-by` paths (§3). The name-based links are real:
- `naming-systems.md`: Glottolog ×2
- `conlang-methodology.md`: WALS/PHOIBLE/Rosenfelder ×14
- `phonology-sanity-gate.md`: PHOIBLE ×4
- `comparative-frameworks.md`: TMI ×3
- `myth-consistency-gate.md`: TMI ×7, ATU ×10
- `kinship-terminology.md`: D-PLACE ×1
- `myth-folktale-genres.md`: da Silva/Tehrani ×4
- `zapotec-mixtec.md` and `moche.md`: Glottolog ×1 each

The census cannot tell a citation from a name hit. The r49 class lesson makes the test manual. A blocking S-id check would turn eight legacy rows red through no fault of C, so do not make it blocking in r50 (M7).

**F7 — P1 · calibration, r49 residual, outside r50 claims.** The superseded tier-A rows S034, S038 and S039 are still cited (§7). S044–S046 are never cited, although `round-49.md:79–81` and QUALITY criterion 6 (`QUALITY.md:29`) make them the tier-B citations for publisher-level claims. Line 188 grades S039 as B, so the grade was applied but the id was not repointed. This edits an admitted r49 entry, so it is outside any r50 claim. Log it as a residual and a mined mistake, and decide separately (M8).

**F8 — P1 · operability.** `corpus/lessons/README.md` has no round-50 row. A lesson landing after its stamp adds a row (`:301–304`). The index audit `reports/round-25/audit/c31-lessons-index-audit.py` enumerates lesson files. It was not run. Add the row in the same change that lands round-50.md (in M1).

**F9 — P2 · reference drift.** `SOURCES.md:8` says the round lesson's Gate covers "S001–S043". The registry has S001–S047, and `round-49.md` covers all 47 (bullets at `:29–75` and `:79–82`). `round-49.md:20` has the same stale range. Do not edit the filed lesson; corrections are new files (`round-49-verifier-spotcheck.md:3`). Fix the SOURCES.md header in the r50 change and note the correction in round-50.md (M9).

**F10 — P2 · operability.** The seven census commands do not check:
- REJECTED prefix (F5 shows the gap)
- `supersedes` target existence
- `used-by` ↔ citation (F6)
- Gate quote length and access date (the runner checks ids only)
- anchor is not a bare homepage (S006 and S028 use "home page" blocks)
- recheck format (`365d` is in use)

The rows I checked by hand pass the ISO-date, recheck and quote-length tests today. Add these as a non-blocking sidecar (M7).

**F11 — P2 · contract ambiguity.** `used-by` "knowledge entries or lessons" (`CORPUS.md:107–108`) versus practice (knowledge only). The literal reading makes a Gate line self-mine its row. State the reading in the round-50 Gate (M11).

**F12 — P2 · template drift.** `build/ScribeLesson.md:53` uses backticks and a Tier suffix that are not in the r49 form (M11).

**F13 — P1 · entry contract (C).** `CORPUS.md:163–165` says a new knowledge entry "opens with its provenance trio" (`source:`, `verified-at:`, `recheck:`). The r49 model entry and `run-validation.py:51–52` (HEAD_FIELDS) place them after topic, gap filled, sources and couples (`hunting-foraging-subsistence.md:3–5`, `:19–23`). `claims.json:15` requires an "8-field head in order". L1 must pick one order and record the conflict in round-50.md. The runner's HEAD_FIELDS order is the one the r49 runner measures.

**F14 — P1 · coverage gate.** Both S048 drafts are identity or object scope (`SrcDysonHudson.md:44`, `SrcUnescoGer.md:16`). QUALITY criterion 1 (`QUALITY.md:5–8`) requires a checkable source for each factual claim. The entry's herding-management content therefore needs at least one opened content-scope row, tier A for its exact scope or else B, before any pastoral-practice claim is admitted (M12). The FAO and Bedouin drafts are not on disk and were not reviewed.

## 9. Moves (kept only if they improve an axis and harm none)

| move | fixes | axis effect | harm and mitigation |
|---|---|---|---|
| **M1.** Fold `corpus/SOURCES.md`, `corpus/lessons/round-50.md` and the `corpus/lessons/README.md` index row into C.lands | F1, F8 | calibration +, operability + (one unit), coverage 0 | Ca can no longer report the C↔registry coupling. State that in the verdict. C's citations are then verified by the Gate runner and census. O and Ca stay disjoint |
| **M2.** L1 assigns S048+ contiguously at merge. Scouts use temporary ids. No seat writes S048 into the lane | §6 | operability +, coverage 0 | none |
| **M3.** Write a round-50 census runner with lesson path and opened date as parameters. Leave the round-49 runner untouched | F2 | operability + | none |
| **M4.** Rebuild the before-check evidence_command from the spec list, word-boundary | F4 | calibration + | verdict unchanged |
| **M5.** Separate `kotodama-separability-manifest-v1` with exports and per-claim trees. Checker exits 2 on zero exports | F3 | calibration + | none |
| **M6.** Log the S047 exception in round-50.md. Propose contract v2 wording `supersedes S0NN — REJECTED: …; flip: …` | F5 | calibration + | none. Do not edit S047 |
| **M7.** Non-blocking sidecar: `used-by` ↔ canonical URL/DOI (not S-id), REJECTED prefix, supersedes target, quote ≤25 words. Report only, not in sweep | F6, F10 | operability +, calibration + | none if non-blocking. Blocking would redden eight legacy rows, so do not make it blocking in r50 |
| **M8.** Repoint the hunting entry from S034/S038/S039 to S044–S046 as a separate logged change, with `used-by` updates | F7 | calibration + | scope creep if folded into C. Touches an admitted r49 entry, so keep it out of C |
| **M9.** Fix `SOURCES.md:8` in the r50 SOURCES edit. Note the correction in round-50.md | F9 | operability + | none. Do not edit the filed round-49 lesson |
| **M10.** Add the round-50.md row to the lessons index | F8 | operability + | none (included in M1) |
| **M11.** Gate in r49 form. Treat `used-by` as knowledge-only and state the reading in the Gate | F11, F12 | calibration + | none |
| **M12.** Frontier opens at least one content-scope row for herding management before C admits any pastoral-practice claim | F14 | coverage + | more frontier work, not a narrowing |

## 10. Candidate `## Mistakes` rows for corpus/lessons/round-50.md

| class | evidence | captured-by | fix |
|---|---|---|---|
| landing | `claims.json:10, :17–18`: frontier outside manifest; C.lands lacks SOURCES.md | none (Ca has no frontier leg) | M1 |
| vacuous | `claims.json:17` "exits 0" with no exports (grep = 0) | none | M5 |
| scope | `claims.json:21–22`: evidence_command differs from spec mode and list; "sherd" hit | none | M4 |
| attribution | `hunting-foraging-subsistence.md:18, 20, 185, 187, 188, 197` cite superseded S034/S038/S039; S044–S046 `used-by` `—` | QUALITY criterion 6 (no check) | M8 (logged) |
| reference-drift | `SOURCES.md:8` and `round-49.md:20` say S001–S043 | none | M9 |

## 11. Unrun checks and limits

- No external URL was opened. The S048 drafts' quotes and URLs are unchecked by me.
- Not run:
  - `tools/check-claim-separability.py`: absent (confirmed).
  - `reports/round-49/run-validation.py`: round-locked (F2). Not run, to keep the lane read-only.
  - `scripts/sources-census.sh` at the fleet root: exists, maintained CLI, accepts 0–3 leading spaces (`CORPUS.md:150–155`). Not run.
  - `reports/round-25/audit/c31-lessons-index-audit.py`: not run.
  - `reports/round-28/readme/sweep.py`: present, not run.
  - `reports/round-50/jj-colocation-probe.py`: O claim, outside the frontier.
- Before-state checks, which I did run: 225 knowledge entries; 27 culture-material; no pastoral, husband, herd or transhum filename; no separability tool; QUALITY has criteria 1–6 only; no topic owner in word mode.
- Anchors: the rule "never a bare homepage" is not checked by census. I did not sample it.

## 12. Tooling

No installs or updates. Used GNU awk 5.4.1 and grep as shipped. No pacman, uv, npm or cargo action.
