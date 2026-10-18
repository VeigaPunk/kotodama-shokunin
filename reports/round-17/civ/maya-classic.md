# Round-17 C receipt — R17-C05 (maya fixer): the couples gap, dispositioned stale-fixed

- seat: R17-C05, claim C (coverage), round 17 (loop 2 of 3, build 1 of 4; 64w opencode-go/deepseek-v4.1-flash)
- assignment, verbatim: “C R17-C05 (maya fixer): the couples gap — add the sacbeob target or correct the transport-mobility-lexicon.md:20 pointer; reports/round-17/civ/maya-classic.md.”
- operator date 2026-10-18; all commands below ran 2026-10-18T09:16–09:22Z UTC (`date -u` → `2026-10-18T09:16:26Z`, `09:20:03Z`, `09:21:33Z`)
- writes of this seat: `corpus/knowledge/civilizations/maya-classic.md` (the fix) and this file. No other file written; no `git commit`/`push`; no LOG.md append (parent integrates)
- baseline: `reports/round-17/claims.json` declares `baseline_revision f30b6f8188937632bbedd0e7b29aeefff6f8b07b`; the wave is live, so the pre-edit bytes were pinned by hash, not by a clean worktree (`git status --porcelain -- corpus/` at 09:20Z already showed concurrent seats’ in-flight edits: `inuit.md`, `mongol.md`)
- scratch: `export TMPDIR=$PWD/.scratch` before every scratch write; raw copies in `.scratch/r17c05/` (`sacbe.html`, `IMH2020.pdf`, `IMH2020.txt`) — non-canon, not filed

## 1. Debt as received — the round-16 map’s reason trail

`reports/round-16/civ-map.json`, row `maya-classic.md` (entry 61):

```
"status": "stale-documented",
"verified_at": "2026-10-18",
"command": "in-repo verification battery per shard receipt: sha256sum + provenance-audit + couples-resolution (reports/round-16/civ/060-071.md)",
"reason": "couples pointer from transport-mobility-lexicon.md:20 names sacbeob with 0 hits in-entry (r16 C06 reproduction) [evidence: reports/round-16/civ/060-071.md]"
```

Trail, oldest first (all re-read this round):

- `reports/round-10/coverage/review-C08.md:182` — N2 weak couples pointer: “`couples` names `civilizations/maya-classic.md (sacbeob)`; that file has 0 hits for `sacb|coba|white road` — pointer is aspirational (file resolves). Couples-hygiene pass candidate.” An author-side recommendation, never an edit.
- `corpus/lessons/round-10.md:201` — N2 recorded as an observation of the round-10 review, explicitly not a filed defect against bytes.
- `reports/round-16/civ/060-071.md:88` (map row) and `:119` (machine-readable block) — reproduction: `grep -in 'sacbe\|causeway\|white road'` → no output; debt “couples-hygiene candidate, unfixed”.
- `reports/round-16/civ/map-audit.md:74` — the auditor re-ran the same sweep independently: **0 hits** while `transport-mobility-lexicon.md:20` names `civilizations/maya-classic.md (sacbeob)`; verdict “Reproduce.”

## 2. Pre-fix reproduction (2026-10-18T09:20:03Z)

```
sha256sum corpus/knowledge/civilizations/maya-classic.md
→ d3520973b3458df227cf687dd937b0822e75e23359189a2fb2d96c64eacc7055  (equals the r16 map row hash and the round-9 receipt hash `d3520973b3458df2` — the bytes the debt describes)

grep -inE 'sacbe|causeway|white road' corpus/knowledge/civilizations/maya-classic.md
→ exit 1, no output (0 hits — the r16 reproduction command, re-run)

sed -n '20p' corpus/knowledge/culture-material/transport-mobility-lexicon.md | grep -o 'civilizations/maya-classic.md (sacbeob)'
→ civilizations/maya-classic.md (sacbeob)   (pointer present)

sha256sum corpus/knowledge/culture-material/transport-mobility-lexicon.md
→ 86e5f9520e07e3ebb5d518183bb273d1ee8c22cca9c3ef1d35cf8fcef6d5aa70  (lexicon pre-state; unchanged after — §6)
```

## 3. Disposition — `stale-fixed`, branch “add the sacbeob target”

The pointer is not wrong about *which file* owns Maya road material; it is wrong only in that the named target did not exist. Two branches were offered; the pointer-correction branch was rejected because it would (a) delete a useful cross-reference instead of building it, and (b) require editing a round-10 artifact whose receipts are still live and would be invalidated for no gain — the lexicon’s couples text is recorded in `reports/round-10/validation.json:24` and its 15/15 URL sweep with per-URL sha16s in `reports/round-10/coverage/review-C08.md` §2 (including `Sacbe 94b6bdaf…`). Adding the target fixes the root cause and leaves the lexicon byte-identical.

## 4. Evidence (live accesses this round; quotes name location)

**a. `[S]` Sacbe — re-fetched live.** `GET https://en.wikipedia.org/wiki/Sacbe` → **HTTP 200, 178,576 bytes, sha256 `94b6bdafaae439ccc171e6e1f3fe458bbebb8a0954a547609d2d4c0c5c567e90`** — byte-identical to the copy the round-10 sweep recorded as sha16 `94b6bdaf` (`review-C08.md` §2), so the lexicon’s carried claims are content-verified live, not merely inherited. Verbatim article sentences used in §14:

- “A sacbe, plural sacbeob (Yucatec Maya: singular sakbej, plural sakbejo’ob), or ‘white road’, is a raised paved road built by the Maya civilization of pre-Columbian Mesoamerica.”
- “The 62-mile-long (100-kilometer) road connecting the ancient cities of Coba and Yaxuna was for decades the longest known to archaeologists [citation needed].”
- “a five-ton stoneroller resting atop the surface of the sacbe.”
- “Stone stelae and platforms were frequently added to the sacbeob to delineate the end of a sacbe, or the point of crossing for two sacbeob.”
- “sacbeob lead directly to cenotes, which serve both as important religious sites and sources of clean water.”
- “The term Beh refers to ‘the road of life’.” / “The present day and colonial Maya term for the Milky Way is also Sacbe.”
- “Without a profound reliance on beasts of burden to transport goods, it remains partially unclear why the Maya decided to expend so much labor constructing these impressive roads.”

**b. `[KH]` handbook — the entry’s own inspected source already carries the road word.** `GET https://www.mesoweb.com/resources/handbook/IMH2020.pdf` → **HTTP 200, 49,858,925 bytes, sha256 `2327b090ed3dfb0ef2b891786aef22a5612589253bdaf2a40b290604f9d238f2`**; `pdftotext -layout` → 8,330 lines. Thematic Dictionary page (printed **99/151**; PDF page 101) verbatim:

- `bih ~ bij` | `bi-hi` / `bi-ji` | `bih` / `bij` | n | “road” — “compare to sak-bih for lit. ‘white-road’ which is the Classic-period reflex of the causeways known as **sakbeob** in Yucatan.”
- `bihtuun` | `bi-TUN-ni` | `bih-tuun` | cn | “lit. ‘road-stone’ refers to plastered/paved surfaces and particular to the playing alleys of ballcourts”.

This matters for provenance: the linguistic side of the fix lands inside a source the entry already records as directly inspected — no new source class is imported for it; `[S]` is a tertiary relay used only for the road-object claims, at the same scope the lexicon already carries (`transport-mobility-lexicon.md:4,11`).

**c. In-corpus locators re-read:** `culture-material/transport-mobility-lexicon.md:4` (topic), `:11` (`[Sacbe]` source bullet), `:20` (couples), `:36` (§2 “Maya sacbeob” bullet), `:44` (route-institution table row).

## 5. Edits made (5, all in `corpus/knowledge/civilizations/maya-classic.md`; 198 → 208 lines)

1. `- sources:` — new `[S]` bullet at line 14 (live evidence, scope limit, non-substitute clause).
2. `- couples:` (line 15) — added `route/mobility — ../culture-material/transport-mobility-lexicon.md (sacbeob; …reciprocal pointer, closing the round-10 N2 gap)`.
3. `- verified-at:` (line 17) — new 2026-10-18 clause carrying the reason trail (`review-C08.md:182 → 060-071.md:88,119 → reports/round-17/civ/maya-classic.md`), pre-fix hash, and both live accesses; the 2026-10-17 round-8 pass text kept verbatim as the prior clause.
4. `- recheck:` (line 18) — added the §14 sacbeob figure recheck trigger.
5. New `## 14. Route layer: sacbeob — the white road (added in the round-17 couples fix)` at EOF (lines 201–208), **appended at EOF deliberately** so every pre-existing §-number and line locator in filed receipts keeps its meaning (Z15’s `§2 L32`, `§9 L140/143`, `§10 L151`, `§13 L193`; round-4 audit’s `:2–14/:16–21/:188–195`).

## 6. Post-fix verification (2026-10-18T09:21:33Z)

```
sha256sum corpus/knowledge/civilizations/maya-classic.md → d9608d842ccb97da3514032d41a323016dc65c0039ff6396d4f96b7678ce67b5
wc -l                                                   → 208
grep -inE 'sacbe|causeway|white road' <entry>            → 9 hit lines (was 0; exit 0)
python3 tools/gates/provenance-audit.py <entry>          → files=1 marks=5 mark-lines=5 findings=0 blocked=0, exit 0
                                                          (marks 4 → 5: the §14 limit marker, deliberate)
distinct URLs                                            → 10 (was 9; the `[S]` URL)
couples refs resolve                                     → 17/17, 0 missing (script, corrected base `corpus/knowledge/`)
```

Couples resolution, both directions: `maya-classic.md` now names `transport-mobility-lexicon.md` 6× (couples line, `[S]`, verified-at, §14 ×3) and `transport-mobility-lexicon.md:20` still names `civilizations/maya-classic.md (sacbeob)` — the pointer is now true.

No-harm sweeps:

- lexicon byte-identical: sha256 `86e5f9520e07e3ebb5d518183bb273d1ee8c22cca9c3ef1d35cf8fcef6d5aa70` before and after; absent from `git status`.
- frozen replay inputs: `find tools/gates/frozen -name maya-classic.md` → **0** (the frozen round-3 inputs copy `mesoamerica-primary-sources.md`, which this seat did not touch).
- writes sweep: `git status --porcelain -- corpus/` at 09:21Z → ` M inuit.md`, ` M maya-classic.md`, ` M mongol.md`, ` M rapa-nui.md`, ` M siam-thai.md`, `?? corpus/lessons/round-17.md`. The four non-maya entries are other seats’ targets per the r16 map (inuit = Dorais 2010 404-stable; mongol = `rubruck.html` hard-fail; rapa-nui & siam-thai = never-swept URL sets); `corpus/lessons/round-17.md` is another seat’s untracked scribe file. **This seat’s only corpus write is `maya-classic.md`.**

## 7. Limits / non-claims

- The entry’s other 9 cited URLs were **not** re-swept this round; no freshness claim is made about them (the 2026-10-17 sweep receipt stands as history). The two live accesses above are the ones the fix itself rests on.
- §14’s length/roller/labor figures are relayed (tertiary) and marked `(to-verify)` for site-level dates and construction estimates; no new linguistic claim is added; no real-world rights/clearance ruling is made anywhere — report only, everything here NON-CANON.
- `reports/round-16/civ-map.json` is a filed artifact and was not edited; the map scribe/parent should flip row 61 to `stale-fixed` with `new_sha256 d9608d84…` and `debt: closed`.
- `reports/round-17/run-validation.py` did not exist at this seat’s run time (other seats own it); this receipt is written to be machine-readable for it (block below).

## 8. Machine-readable block (map-scribe / validator input)

```json
{
  "shard": "C05",
  "round": 17,
  "claim": "C",
  "seat": "R17-C05",
  "checked_at_utc": "2026-10-18T09:21:33Z",
  "operator_date": "2026-10-18",
  "baseline_revision": "f30b6f8188937632bbedd0e7b29aeefff6f8b07b",
  "fragment": "reports/round-17/civ/maya-classic.md",
  "entries": [
    {
      "i": 61,
      "file": "corpus/knowledge/civilizations/maya-classic.md",
      "status": "stale-fixed",
      "old_sha256": "d3520973b3458df227cf687dd937b0822e75e23359189a2fb2d96c64eacc7055",
      "new_sha256": "d9608d842ccb97da3514032d41a323016dc65c0039ff6396d4f96b7678ce67b5",
      "receipts": ["reports/round-8/metadata/m04-civ-58-76.md", "reports/round-10/coverage/review-C08.md", "reports/round-16/civ/060-071.md", "reports/round-17/civ/maya-classic.md"],
      "debt": "closed: couples pointer culture-material/transport-mobility-lexicon.md:20 (sacbeob) now true — entry has 9 sacbe|causeway|white road hit lines, a reciprocal couples pointer, and §14; lexicon left byte-identical (86e5f952…)",
      "evidence": {
        "locator": "https://en.wikipedia.org/wiki/Sacbe (HTTP 200, 178576 bytes, sha256 94b6bdafaae439ccc171e6e1f3fe458bbebb8a0954a547609d2d4c0c5c567e90, 2026-10-18) + KH thematic dictionary p. 99/151 (PDF p. 101; handbook sha256 2327b090ed3dfb0ef2b891786aef22a5612589253bdaf2a40b290604f9d238f2)",
        "command": "grep -inE 'sacbe|causeway|white road' corpus/knowledge/civilizations/maya-classic.md"
      }
    }
  ],
  "other_corpus_writes_by_this_seat": 0
}
```

FILES: reports/round-17/civ/maya-classic.md | SUMMARY: maya-classic couples gap dispositioned stale-fixed by adding the sacbeob target (§14 + reciprocal couples pointer + [S]/KH live-verified sources; d3520973… → d9608d84…), lexicon untouched.
