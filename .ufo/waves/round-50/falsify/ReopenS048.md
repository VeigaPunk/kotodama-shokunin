# ReopenS048 — falsify seat

- Item attacked: SOURCES row **S048** (FAO 2001, *Pastoralism in the new millennium*, Introduction), its round-50 Gate bullet, and every `S048` citation in `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`.
- Landed commit read: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
- Verdict: **PARTIAL**. The row's URL, Gate quote, quote location, bibliographic identity, tier/scope, anchors and 8 of the entry's 9 substantive citation sentences hold exactly. One clause is an unscoped generalization that both the row's `teaches` field and entry `:152` assert beyond the source ("two to four species" as a general rule); one paraphrase ("refuted") is stronger than the source's wording but substantively supported.

## Method (no lane writes, no mutating git/jj, no clone needed)

```
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 1c779e4a:corpus/SOURCES.md            # row at line 77
git -C ... show 1c779e4a:corpus/lessons/round-50.md                                                # Gate bullet at line 33
git -C ... show 1c779e4a:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md          # S048 hits at 7,9,16,43,49,51,103,152,162,179
curl -sS -L -w 'HTTP %{http_code} final=%{url_effective} bytes=%{size_download} type=%{content_type}' https://www.fao.org/4/y2647e/y2647e02.htm
curl -sS -L https://www.fao.org/4/y2647e/y2647e00.htm                                               # cover/contents, bibliographic check
```

Live fetch this session: `HTTP 200 final=https://www.fao.org/4/y2647e/y2647e02.htm bytes=66283 type=text/html`.
Cover fetch: `HTTP 200 bytes=12996`; page shows `ANIMAL PRODUCTION AND HEALTH PAPER 150`, `ISBN 92-5-104673-5`, `© FAO 2001`, and a Contents list naming exactly `Classifying pastoral systems`, `Pastoral species`, `Pastoral enterprises`, `History and origins of pastoralism`, under `INTRODUCTION: PASTORAL SYSTEMS WORLDWIDE`. Chapter `<title>` is `Pastoralism in the new millennium`.

## What holds (observed)

1. **Row shape.** `SOURCES.md:77` has all 12 header fields populated (`awk -F'|' NR==77` → 13 splits incl. trailing empty; 808 bytes). `used-by` is the full path `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`, not truncated. `status=mined`, `opened=2026-10-21`, `recheck=365d`, `kind=docs`, `tier=B`.
2. **Gate quote, verbatim and located.** `lessons/round-50.md:33` records `§Classifying pastoral systems: "there is little or no impetus to herd animals"`. The live page contains that string exactly once, inside the paragraph under the `CLASSIFYING PASTORAL SYSTEMS` heading: "Where human population densities are very low, i.e. where hunting-gathering is relatively easy, there is little or no impetus to herd animals." (raw-HTML grep count 1; the phrase is contiguous in one text node, not reassembled across tags). Access date 2026-10-21 is today; page serves 200.
3. **Every anchor exists.** Page headings (uppercase runs): `OVERVIEW`, `CLASSIFYING PASTORAL SYSTEMS`, `PASTORAL SPECIES`, `PASTORAL ENTERPRISES`, `HISTORY AND ORIGINS OF PASTORALISM`, `SOURCES OF INFORMATION ON PASTORALISM`, `THE DISCOURSE OF PASTORALISM`. Row anchors map to real sections and subsections (`Nomadism`, `Transhumance`, `Agropastoralism`, `Enclosed systems and ranching` inside Pastoral enterprises).
4. **Bibliographic identity exact.** Series `Animal Production and Health Paper 150`, year 2001, chapter `Introduction` — all confirmed on the FAO cover/contents page, not just asserted by the lane.
5. **Tier/scope honest under `QUALITY.md:29` (criterion 6).** Criterion 6 bars over-claiming (abstracts/publisher blurbs as B). S048 is the full chapter, filed `B` with scope "FAO's comparative classification, species portfolio and history-of-the-idea of pastoral systems; institutional synthesis, not primary ethnography". That is an accurate `B` (expert survey/synthesis) and a scope that explicitly disclaims primary ethnography. If anything it is conservative, not inflated — no criterion-6 breach.
6. **Citation-by-citation support** (entry line → claim → what the page says):
   - `:16` "where hunting-gathering is easy, 'there is little or no impetus to herd animals'" — exact quote, same section. Supported.
   - `:43` "Any classification of this type must be treated as a simplification" — exact string once, first paragraph of `PASTORAL ENTERPRISES` (classification "by the degree of movement, from highly nomadic through transhumant to agropastoral"). Supported; the entry's extension of the caution to its own five-row table is a fair methodological use.
   - `:49` transhumant labour "herd splitting (S048)" — "A characteristic feature of transhumance is herd splitting". Supported.
   - `:51` enclosed/ranching "fenced, individually owned land (S048)" — "the land is individually owned and usually fenced". Supported; the unsourced "stored feed replaces movement" is correctly flagged `(to-verify)`.
   - `:103` "transhumance splits the herd (S048)" — same sentence as above. Supported.
   - `:7`, `:9` — bibliographic list entries only; accurate (title, year, URL, access date, tier/scope pointer).
   - `:162`, `:179` stage-ladder `R` — see caveat below; the substance (the hunting→herding→farming sequence is not the general order) is supported.
7. **Round-50 lesson's own claim** that S048/S049 quotes were re-fetched and matched under the named heading is true for S048.

## Finding — the one substantive defect: unscoped "two to four species"

- Source sentence (under `PASTORAL SPECIES`): "By contrast, **in Mongolia and the northern Sudan**, herders seem to manage between two and four species of roughly equal importance simultaneously." The same paragraph's contrast pole is single-species systems: "although horses, donkeys, camels, goats, cattle and dogs are kept by the nomads of Southwest Asia, sheep predominate".
- Table 1 (`Regional zonation of pastoral systems`) contradicts a 2–4 rule as a general count: Europe and North Africa = "Small ruminants" (one class), India = 5 named species, Central Asia = 5, Sub-Saharan Africa = 4, North America = 2, Andes = 3. So the page's own inventory spans 1–5 by region.
- Row `teaches` (`SOURCES.md:77` field 8) states it unscoped: "…herd splitting; herders manage two to four species; the evolutionary-stage reading is refuted…". That is a scope upgrade from a two-region observation to a property of herders.
- Entry `:152` reproduces it as a build rule: "| 2 | Species | two to four species and their shares (S048) | …". It also sits in tension with the entry's own `:67`/`:78`, which teach the five-species Mongolian "five snouts" set (S060). No other occurrence of "two to four" in the entry (`grep -n 'two to four'` → `:152` only).
- Severity: small but real. The number is right for the two regions named in the source; the missing scope is what makes the sentence unsupported, and the entry teaches it as a default cap.

## Caveat (not counted as a required fix): "refuted"

Entry `:162` and `:179` say "FAO reports the evolutionary-stage reading refuted". The page says the stage model belonged to older literature and that "the increase of archaeological data and a more careful reading of the historical sources, especially from Asia, have demonstrated a more complex story… In most parts of the world, Africa excepted, agriculture seems to have started earlier than pastoralism. Pastoralism develops from surplus…". FAO never uses "refuted", and the "Africa excepted" clause is dropped. Substantively the sequence is disconfirmed for most of the world and replaced by a surplus-origin account, so the `R` calibration stands; the wording attributes a stronger verdict than the text states. If the lane wants exactness, write "rejected as a general sequence — FAO reports a more complex story: in most parts of the world except Africa agriculture began earlier; pastoralism develops from surplus".

## Smallest fix (author-lane advice)

1. Entry (one line, the C claim's own land): change `:152` to
   `| 2 | Species | species mix and shares — single-species specialization, or two to four species of roughly equal importance (Mongolia, northern Sudan) (S048) | … |`
   This removes the unsupported default without touching byte-identical quotes.
2. Registry wording, only if the lane wants the row exact: SOURCES is append-only for `teaches`, so a correction is a new row opening `supersedes S048 —` with the same URL/tier/scope, the scoped species clause, and `used-by` naming the entry; log the old→new `status/recheck/used-by` (if any) in the next round lesson as the header requires. Repoint the entry's `:152` citation to the new id.
3. No change needed for the quote, location, anchors, tier or any other citation.

## Unresolved / not claimed

- FAO exposes no per-request access log; the 2026-10-21 access date rests on the lane record plus today's live 200 fetch.
- The "refuted" judgment is a wording call, not a factual contradiction; recorded as caveat, not a second fix.
- S048 does not itself supply the entry's "semi-nomadic" row or the enclosed "stored feed" clause; those are cited elsewhere or already flagged `(to-verify)`.

No tools installed; no clone created; no lane file, index, jj state or sibling artifact touched. Scratch fetches (`/tmp/fao_s048.html`, `/tmp/fao_s048.txt`, `/tmp/fao_cover.html`, `/tmp/entry50.md`, `/tmp/SOURCES50.md`) deleted after writing.
