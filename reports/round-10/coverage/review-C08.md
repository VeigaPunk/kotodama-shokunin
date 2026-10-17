# R10-C18 — Reviewer of worker C08's culture-material entry (author-side review)

- reviewer scope: `reports/round-10/coverage/review-C08.md` only. No corpus, ledger, bookkeeping, canon, or promotion edits. Author-side review evidence only; not an admission decision and not independent promotion verification.
- assignment: `reports/round-10/targets.json` → `R10-C11..C20` ("Ten reviewers: one per authored entry (poll for it, max 20 min): verify frontmatter completeness, source resolvability (re-run the cited command or open the cited path/URL), no filler, no duplication of an existing entry; verdict `reports/round-10/coverage/review-<id>.md`").
- **Reassignment record:** this review was originally filed as `review-C07.md` under the seat label R10-C17. It reviewed `transport-mobility-lexicon.md` on the assumption that C07 was the first culture-material author to land. That assumption was wrong: `reports/round-10/coverage/C08.md` (filed 18:28) names `transport-mobility-lexicon.md` as **C08's** entry, and `reports/round-10/coverage/C07.md` names `vessel-container-lexicon.md` as C07's. The artifact, evidence, commands and findings below are unchanged from the filed bytes — only the seat label is corrected. The genuine C07 review is `review-C07.md` (rewritten 18:4xZ).
- C08 is the second culture-material author (`R10-C01..C10` seat split: linguistics ×3 = C01–C03, myth-symbol ×3 = C04–C06, culture-material ×2 = C07–C08, verification ×2 = C09–C10).
- date: 2026-10-17 (all times UTC). Tree at review: `e3a1ec9435787328ac9f828f96cb6390e4916b8f`, dirty from concurrent shards. Review window ≈21:26–21:37Z.
- baseline: round-10 declared revision `9dc18ec1339bffd6f81e74f1a5742464ef578749` (`reports/round-10/claims.json`).

## 0. Review status — LANDED, reviewed

C08's fragment was already on disk (18:28 local) when this review opened; the entry landed at 18:32 local: `corpus/knowledge/culture-material/` went 16 → 17 files, the new file being `transport-mobility-lexicon.md` (mtime 18:32 local = 21:32Z). The artifact reviewed is the **bytes on disk**, which are what the C claim counts.

**Artifact under review:** `corpus/knowledge/culture-material/transport-mobility-lexicon.md` — 128 lines, 39,383 bytes, sha256 `36a7370ff49cda98030cc978c059c23fbc32d86eec690bcf0caa5555d66ad272` (21:31Z, unchanged through 21:36Z). Title: "Transport and Mobility Lexicon — Roads, Vehicles, Draft, Watercraft, and the Words That Travel With Them".

**Verdict summary: 3 of 4 mandated checks pass clean; 1 defect found (source resolvability, one mislinked URL).** The defect is a citation-path error, not a content error — the cited fact is correct and independently confirmed. No evidence of fabrication, filler, or duplication.

| mandated check | verdict |
|---|---|
| frontmatter completeness | **pass** |
| source resolvability | **defect — 1 mislinked URL** (see §2.4); 12/14 URLs 200, 2 blocked by bot wall but confirmed via Wayback |
| no filler (gap named, real, delivered) | **pass** |
| no duplication of an existing entry | **pass** |

## 1. Check 1 — frontmatter completeness: PASS

House profile = the five fields every committed entry carries, each exactly once in the head block (text before first `## `). Instrument: `.scratch/c17-frontmatter-check.py`.

- `- topic:` L3 count=1; `- sources:` L4 count=1 with 14 nested sub-bullets L5–L18; `- couples:` L19 count=1; `- verified-at:` L20 count=1, dated and scope-bearing; `- recheck:` L21 count=1, names concrete triggers. Head block = L1–22; first `## ` at L23. **No missing, duplicated, or placeholder field.**
- **Method note (recorded because my first pass produced a false positive):** my initial regex treated `- sources:` as EMPTY. That was the instrument's bug, not the entry's. The `- sources:` + indented `  - <source>` sub-bullet form is the house pattern — `grep -rln '^- sources:$' corpus/knowledge/ | wc -l` → **72** committed entries use it. The instrument was corrected to count nested sub-bullets before reporting EMPTY. A reviewer using a naive line-value check would file this same false finding.
- Required **decision-record section** present: `## 10. Decision record` L111, table `DR-TR-01..07` L113–121, each row carrying decision / trigger / evidence / status. `## 11. Handoff note (non-canon)` L123 closes at the handoff per `corpus/QUALITY.md` §5.
- Lane gate: `python3 tools/gates/provenance-audit.py corpus/knowledge/culture-material/transport-mobility-lexicon.md` — see §5 for the recorded run.

## 2. Check 2 — source resolvability: DEFECT (1 of 14 URLs mislinked)

### 2.1 In-corpus path:line citations — all 9 resolve to the cited content

`corpus/knowledge/culture-material/material-culture-inference-method.md:67` (transport row, "state logistics; military reach") and `:92` (substrate inventory naming transport); `culture-material/trade-economy-lexicon.md:103` (caravan lingua franca), `:131` ("who eats the loss if the ship sinks, the caravan robs"), `:145` (instrument named after the carrying object), `:136` (bottomry/respondentia — cited in §6); `civilizations/polynesia-navigation.md:23` (waka cognate set), `:37` (WAKA.A row), `:53` (Thompson's star houses), `:60` (horizon houses row); `linguistics/language-contact.md:56-62` (WOLD section incl. ≈24% mean borrowing rate); `synthesis/loanword-material-dating.md:43-57` (strata procedure + diagnostic table). Every cited line was opened and matches the use made of it. **No misattributed line reference.**

### 2.2 Live URL access (2026-10-17, `curl -L --max-time 20`, recorded verbatim)

```
200  https://en.wikipedia.org/wiki/Wheel
200  https://en.wikipedia.org/wiki/Royal_Road
200  https://en.wikipedia.org/wiki/Cursus_publicus
200  https://en.wikipedia.org/wiki/Inca_road_system
200  https://en.wikipedia.org/wiki/Queshuachaca
200  https://en.wikipedia.org/wiki/Sacbe
200  https://en.wikipedia.org/wiki/Horse_collar
200  https://en.wikipedia.org/wiki/Stirrup
200  https://en.wikipedia.org/wiki/Rickshaw
200  https://en.wikipedia.org/wiki/All_roads_lead_to_Rome
200  https://en.wiktionary.org/wiki/Kutsche
200  https://www.newworldencyclopedia.org/entry/Junk_(ship)
403  https://www.etymonline.com/word/canoe
403  https://www.merriam-webster.com/dictionary/coachable
```

The two 403s are a Cloudflare interstitial (`<title>Just a moment...</title>`), not dead links — the same 403 is returned for the unambiguously-correct `.../dictionary/coach`, so 403 is **not** evidence about either URL's correctness. Both were instead resolved through the Wayback Machine (§2.4).

### 2.3 Claim-level verification against fetched article text (the entry's load-bearing numbers)

Article source text was fetched via `https://en.wikipedia.org/w/index.php?title=<X>&action=raw` into `.scratch/c17-src/` and grepped. Every figure below was found in the cited article, **not** taken on the entry's word:

| entry claim | article text found | verdict |
|---|---|---|
| Royal Road 1,677 miles / 2,699 km | "me 1677 miles, primarily as a post road" (2,699 km is the article's own conversion) | confirmed |
| 111 posting stations | "It included one hundred and eleven posting stations maintained with a supply of fresh horses" | confirmed |
| Sintashta spoked wheels c. 2000 BCE, Krivoye Lake | "earliest known examples of wooden spoked wheels are from the Sintashta culture, dating to c. 2000 BCE (Krivoye Lake)" | confirmed |
| Ljubljana Marshes wheel 3340–3030 BCE | "3340–3030 BCE" (Stare Gmajne) | confirmed |
| Mesoamerican wheeled toys c. 1500 BCE | "small wheeled artifacts, identified as children's toys ... approximately 1500" | confirmed |
| Q'eswachaka 28 m, ichu grass, annual June renewal | infobox `length = {{convert|28|m}}`; "renewing the bridge annually, during the second week of June" | confirmed |
| Q'eswachaka UNESCO ICH 2013 ref. 00594; R.S. 1112/INC-2009 | infobox ICH `ID = 00594`, `Year = 2013`; `Resolución Directoral Nº 1112/INC-2009` | confirmed |
| 2021 collapse; 2025 vandalism, rebuilt | "the bridge collapsed in March 2021 ... rebuilt"; 2025 *atentado* press release | confirmed |
| Coba–Yaxuna sacbe ~100 km + five-ton roller | "62 mi-long road connecting ... Coba and Yaxuna"; "almost 100 km to the west"; "a five-ton stone roller resting atop the surface" | confirmed |
| Dunhuang cave 257 mural 477–499 CE (Needham 1986) | "earliest legitimate depiction ... cave 257 ... Northern Wei dynasty ... dated to 477–499 AD" | confirmed |
| Qhapaq Ñan 40,000 km, range 23,000–60,000 km | "about 40,000 km long in total"; "from 23,000 km ... to 40,000 km ... to 60,000 km" | confirmed |
| Pertinax news reached Egypt in 63 days (193 CE) | "took over sixty-three days to reach Egypt, being announced on March 6 in Alexandria" | confirmed |
| stirrup: Bachrach 13 in 704 eighth-century German burials | "Out of 704 eighth century male burials excavated in Germany" (Bachrach) | confirmed |
| rickshaw first English use 1879; replaced kago/norimono by 1872 | "first known use of the term in English was in 1879"; "By 1872, they replaced the kago and norimono ... about 40,000 rickshaws in service" | confirmed |
| rickshaw independently invented c. 1869 after lifting of a Tokugawa ban on wheeled vehicles | "independently invented in Japan circa 1869 ... after the lifting of a ban on wheeled vehicles from the Tokugawa period" | confirmed |
| White 1964 vs Bullough 1970 / Bachrach 1970 on the stirrup | "Bullough, D. A. (1970) ... Bachrach, Bernard S. (1970), 'Charles Martel, Mounted Shock Combat'" | confirmed |

The one figure the entry attributes to a *secondary* source rather than the article — the llama load of ~30 kg at 20 km/day (Nielsen 2000; D'Altroy 2002) — was not located verbatim in the fetched article text; the entry's own §5 attributes it to those studies and `verified-at` already flags the tertiary-relay limit. Noted, not scored as a defect.

### 2.4 The defect: one URL points at a different headword than its text claims

**L80** reads `([Merriam-Webster](https://www.merriam-webster.com/dictionary/coachable), [Wiktionary *Kutsche*](https://en.wiktionary.org/wiki/Kutsche))` — the link text says **coach**, the URL resolves to the headword **coachable**.

- `/dictionary/coachable` is a *distinct* Merriam-Webster headword, not a redirect to `coach`: the Wayback CDX index lists separately-archived snapshots of `merriam-webster.com/dictionary/coachable` (2009–2015, HTTP 200), while `.../dictionary/coach` is its own page.
- The archived `coach` page carries the fact the entry actually cites: `First Known Use` → **1556**, and the etymology chain through French *coche* ← German *kotsche* ← Hungarian *kocsi (szekér)* "of Kocs". The archived `coachable` page does not carry it.
- So: **the cited fact is correct and the citation is verifiable — at the wrong URL.** This is a resolvability defect under the assignment's own test ("open the cited path/URL"), not a fabrication, and not a factual error.

**Severity: low.** It misdirects a rechecker to a page that does not support the claim; the correct page does. Recorded as a finding against C07's entry rather than silently passed, per the round rule that non-resolving items are never silently passed. The entry's *other* citation for the same sentence (Wiktionary *Kutsche*) resolves 200 and carries the same chain.

## 3. Check 3 — no filler: PASS

- **The gap is named and real.** The entry's subject — transport/mobility as a material-culture system with its own lexicon — appears in the committed corpus only as a single row in `material-culture-inference-method.md:67` ("transport & draft animals | state logistics; military reach") and one word in the `:92` substrate inventory. No committed entry owns it: the nearest neighbours (`trade-economy-lexicon.md` = market/measure/money words; `architecture-settlement-lexicon.md` = built environment; `warrior-material-culture.md` = the saddle as military kit) each explicitly leave carriage and its vocabulary elsewhere, and the entry says so at L19 in its `couples` line.
- **It delivers** the gap it names: four-layer frame (§1), route-institution table with maintenance clauses (§2), bridges-as-institutions (§3), wheel capacity-chain (§4), draft/harness/stirrup (§5), watercraft (§6), vehicle-loan chains (§7), design decision table (§8), calibration shelf (§9), decision record (§10).
- **`corpus/QUALITY.md` bar, item by item:** provenance — every claim carries a source (verified in §2.3); calibration — §9 flags all seven contested/discredited readings with their disputants and a "safe use"; coupling — 30+ named couplings in `couples` L19, plus `corpus companion` column in §8; usability — five tables + checklist, no essays; canon hygiene — §11 explicitly hands off and states "no canon assignment", DR-TR-07 records the lane rule.
- **`to-verify` discipline holds.** 3 markers: the `verified-at` limits sentence (L20), the §7 carried-items list (L85: vinaigrette precedent, rival rickshaw inventors, *chuán* derivation, steppe-migration framing, harness quantities), and DR-TR-06 (L120). The unverified Edo post-road row is explicitly quarantined at L46 ("included as a design slot, not a sourced claim ... did not re-verify Edo post-road details this round"). Nothing unverifiable is laundered into assertion.

## 4. Check 4 — no duplication: PASS

- **Slug collision:** none. `transport-mobility-lexicon.md` was absent from the 179-slug baseline (`.scratch/baseline-slugs.txt`); no `-b` suffix needed.
- **Topic overlap:** highest Jaccard against any of the 179 committed entries is **J=0.045** (`era-periodization-models.md`), then 0.038 / 0.036 / 0.035 (`.scratch/c17-dup-check.py`). No near-duplicate.
- **Content overlap:** §6 defers to `polynesia-navigation.md` rather than restating it ("Cite that file rather than restating it"), and §7's loan chains are new corpus content, not a restatement of `loanword-material-dating.md` (which is cited for method, not copied).
- **Baseline integrity:** the other 16 culture-material files carry mtimes 17:22–17:50 local, all pre-round-10; only the new file is 18:32. No existing entry was edited by C07.

## 5. Evidence — commands run

```sh
# frontmatter census (head block, nested-sub-bullet aware)
python3 .scratch/c17-frontmatter-check.py corpus/knowledge/culture-material/transport-mobility-lexicon.md
# -> all five fields count=1; topic/couples/verified-at/recheck non-empty;
#    sources = 14 nested sub-bullets; first '## ' at L23; VERDICT_FRONTMATTER: complete

# house-pattern control for the nested form
grep -rln '^- sources:$' corpus/knowledge/ | wc -l      # -> 72

# duplication
python3 .scratch/c17-dup-check.py corpus/knowledge/culture-material/transport-mobility-lexicon.md
# -> top J=0.045; slug collisions: none

# live URLs
for u in <14 cited URLs>; do curl -s -o /dev/null -w '%{http_code}' -L --max-time 20 -A 'Mozilla/5.0' "$u"; done
# -> 12x200, 2x403 (Cloudflare interstitial; also 403 for the correct URL)

# article text for claim-level checks
curl -s -L 'https://en.wikipedia.org/w/index.php?title=<X>&action=raw' -o .scratch/c17-src/<X>.txt

# corpus totals at review
find corpus/knowledge -name '*.md' | wc -l          # -> 187
ls corpus/knowledge/culture-material/*.md | wc -l   # -> 17
```

## 6. Findings

| # | finding | severity | status |
|---|---|---|---|
| R10C18-F1 | L80 cites the Merriam-Webster **coach** entry but links `/dictionary/coachable`, a distinct MW headword that does not carry the cited 1556 first-use. Cited fact verified correct on the archived `coach` page; the URL alone is wrong. | low | **open — reported to parent**; this seat holds no corpus write |

## 7. Limits of this review

- Author-side review, not independent promotion verification (lane rule, `AGENTS.md`). This seat verified sources against the *same tertiary surfaces the author cites*; it did not read the underlying scholarly works (Needham 1986, Hyslop 1984, D'Altroy 2002, White 1964, Bullough 1970, Bachrach 1970, Law 1980, Brownrigg 2022). Agreement here means "the entry faithfully reports its cited tertiary sources", not "the history is settled".
- No C07 fragment existed to compare against; the review is of the artifact, and cannot check the author's own claims about what they did or where they wrote.
- The 403-blocked URLs were resolved only through the Wayback Machine (archived snapshots), not live pages.
- `.scratch/` is shared by all live workers; instruments are `c17-`-prefixed (the prefix records the instrument's origin, not a claim about the seat).

FILES: reports/round-10/coverage/review-C08.md

---

## 8. Second independent pass — appended by the seat dispatched as R10-C18 (this run, 2026-10-17 21:26–21:46Z)

**Collision record (read before integrating).** The review above was authored by the seat self-labeled R10-C17 (its reassignment record at line 5; `review-C07.md` carries the fuller correction record). That seat first reviewed `transport-mobility-lexicon.md` believing it was C07's entry, then re-filed those bytes here and rewrote `review-C07.md` for the vessel entry. This run was independently dispatched to review C08's entry at this same path and opened 21:26Z. The bytes above are preserved unmodified; this section adds only this run's independent checks. Both passes reviewed the same artifact: sha256 `36a7370ff49cda98030cc978c059c23fbc32d86eec690bcf0caa5555d66ad272`, unchanged 21:31Z → 21:40Z.

**Material addition — the round's own acceptance checker fails this entry's gap check.** Both passes agree the gap is real and delivered; they diverge on one machine-readable point the review above did not test:

- `grep -c -i 'gap' corpus/knowledge/culture-material/transport-mobility-lexicon.md` → **0** (exit 1). The entry never names its gap in-file (the gap statement lives in `C08.md` §1 and now the README row L81, not in the entry).
- `entry_checks('corpus/knowledge/culture-material/transport-mobility-lexicon.md')` — imported read-only from `reports/round-10/run-validation.py` (the script itself writes `validation.json`, outside this seat's write scope) — returns `missing_frontmatter: []`, `decision_record: True`, `locators: 6`, **`gap: False`**.
- `measure_c()` lines 435–436 append `f"{relative}: no named gap (filler risk)"` for every entry with `gap=False`, and `main()` sets `passed = all(result["passed"] …)`. **Consequence: with the current bytes, `python3 reports/round-10/run-validation.py` reports a C-claim failure naming this file.**
- So §3 above ("The gap is named and real") is true of the fragment and README row but not of the entry bytes the declared checker reads. Recommended disposition (parent/fixer; this seat holds no corpus write): add a one-line in-file gap statement (inline `Gap filled: …` clause or a "gap" heading, e.g. on §1). No content change needed.

**Correction to §2.3's llama note.** The review above records the llama load as "not located verbatim in the fetched article text". It **is** on the cited page, in the Trade section of Wikipedia *Inca road system* (fetched 2026-10-17, sha16 `e191acf0914e184a`): "Llamas of the Q'ara race (short-haired variety), which are used also in contemporary caravans, can carry about 30 kilograms (66 lb) for a distance of 20 kilometres (12 mi) per day, when necessary they can carry up to 45 kilograms (99 lb) for short trips." The entry's "~30 kg at 20 km/day, up to 45 kg short trips" matches verbatim. A `grep '30 kg'` returns 0 because the page spells the units out — the same units-artifact that produced this run's first false negative, recorded so later recheckers do not repeat it.

**Finding R10C18-F1 (M-W `/coachable`) — independently confirmed, one live-behavior note.** CDX index: `/dictionary/coachable` and `/dictionary/coach` are distinct archived URL keys (both status 200, snapshots 2009–2015). The 2010-04-11 archived `/coachable` snapshot (`.scratch/r10c18/wb-coachable.html`, 52,112 B) contains "coachable" ×39 and **zero** hits for `1556`, `Kocs`, `kocsi` — it does not carry the cited chain; the live `/coach` page does (FetchURL 2026-10-17: "Middle English *coche* … from Hungarian *kocsi* (*szekér*), literally, wagon from *Kocs*, Hungary"; "First Known Use Noun 1556"). Note: this run's live FetchURL of the cited `/coachable` URL returned coach-entry content — consistent with a redirect added since the archive era; the archived evidence still shows the cited URL historically served a different headword. The finding stands at severity low; fix is to cite `/dictionary/coach`.

**Source the review above did not resolve: HandWiki.** The entry names the "HandWiki Djong entry" without a URL. Resolved this run: `https://handwiki.org/wiki/Engineering:Djong` (curl code 000 — connection failure in this environment, two attempts; FetchURL retrieved it 2026-10-17). Page supports the contested-derivation claim: Chinese-origin claim "rejected" by Pelliot and Mahdi, Old Javanese *jong* derivation, Portuguese *junco*; `Manguin` ×5 (refs 1980/1993). Locator wording imprecise (see N3).

**Independent re-runs matching the review above (three of four verdicts agree).**

- Frontmatter: one `topic`/`sources`/`couples`/`verified-at`/`recheck`, all in head block L1–22 (first `## ` L23), no placeholders; `verified-at` dated + scope-bearing; 31 couples refs + 35 whole-file refs, 0 missing; `synthesis/worldbible-integration-contract.md` and `civilizations/japan-edo.md` exist.
- Provenance gate: `python3 tools/gates/provenance-audit.py <entry>` → `files=1 marks=3 mark-lines=3 findings=0 blocked=0`, exit 0.
- In-repo citations: all 10 line references verify by `sed -n` (list in this run's §2.2 notes; matches §2.1 above).
- URL sweep (curl browser-UA; sha16 recorded in `.scratch/r10c18/`): Wheel `0e04b55f…`, Royal Road `2532e8d1…`, Cursus publicus `9575ceff…`, Inca road system `e191acf0…`, Queshuachaca `3dd5e1bf…`, Sacbe `94b6bdaf…`, Horse collar `d2a79c85…`, Stirrup `7044e8a0…`, Rickshaw `9a85a2a5…`, All roads lead to Rome `ad35d917…`, Wiktionary Kutsche `acb697d0…`, NWE Junk `b92d2716…` — all 200 and carrying the quoted anchors (e.g. Stirrup: "Out of 704 eighth century male burials … only 13 had stirrups"; Cursus: "took over sixty-three days to reach Egypt"); Etymonline canoe and M-W via FetchURL (curl 403 bot-wall); HandWiki via FetchURL. **15/15 cited sources resolve.**
- Duplication: baseline `git ls-tree 9dc18ec…` → 16 files, `grep -i 'transport\|mobil\|road\|vehicle'` → empty (exit 1); corpus-wide slug sweep → only the new file + `sogdian-silk-road.md` (different scope, cited by the entry); C07's `vessel-container-lexicon.md` landed during this run — distinct slug, mutual coupling, no `-b` needed; partition now 18 files.
- Fragment numbers: `C08.md` §4's provenance/couples results reproduced exactly; its inventory total (182→183) is a moving-total concurrency fact (this run: 184 at 21:36Z).

**Observations not in the review above.**

- **N2 weak couples pointer:** `couples` names `civilizations/maya-classic.md (sacbeob)`; that file has 0 hits for `sacb|coba|white road` — pointer is aspirational (file resolves). Couples-hygiene pass candidate.
- **N3 Manguin locator:** "Manguin cited in the HandWiki Djong entry" is true (×5; refs 1980/1993) but his presence there concerns tonnage, not the etymology dispute (the page attributes the rejection to Pelliot/Mahdi). Locator imprecise; claim supported.
- **N4 README:** rows for both new culture-material entries are present (`corpus/README.md` L81–82); heading-count/total reconciliation is C21/C22/C23–C26 scope.
- **N7 counts:** `corpus/knowledge` = 184 files at 21:36Z; culture-material 18; verification 15; coverage dir 21 fragments — moving under parallel workers.

**Out-of-seat observation (surfaced by the shared checker; routed, not absorbed).** `myth-symbol/plant-symbolism.md` (C06's entry) returns `gap=False` **and** `locators=0` from `entry_checks` → two `measure_c` failures ("no named gap (filler risk)"; "no retrievable locator"). For the parent and C16's review.

**Limits of this second pass.** Author-side only: no corpus edit, no admission, no promotion verification; the gap-clause fix is recommended, not applied (write scope = this fragment). `run-validation.py` was imported read-only, not executed. Every verdict is against the bytes at sha256 `36a7370f…` (21:31–21:40Z); if the entry is edited later, this pass covers only that revision.

FILES: reports/round-10/coverage/review-C08.md | SUMMARY: second independent pass agrees with the filed review on frontmatter/sources/duplication and adds one material finding — the entry carries no in-file gap clause, so the round's own acceptance checker (entry_checks gap=False) will fail the C claim on this file until a one-line fix lands; plus llama figures confirmed verbatim on the cited page, HandWiki source resolved, M-W finding independently confirmed.
