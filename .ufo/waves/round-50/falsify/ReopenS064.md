# ReopenS064 — falsify seat

- Item attacked: SOURCES row **S064** (ETCSL, *The debate between Sheep and Grain*, composition 5.3.2), its round-50 Gate bullet, and every `S064` citation in `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`.
- Landed commit read: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`); all lane bytes via `git show <commit>:<path>`, never the working tree.
- Verdict: **PARTIAL**. URL route, capture identity, composition number, verbatim quote, quote range, tier/scope and both entry citation sentences hold exactly. One anchor descriptor is factually wrong: `lines 130–142 (Grain's third speech)` — 130–142 is the closing paragraph of Grain's **second** speech (the one announced at 116); Grain's third speech is 169–179. The error is metadata-only: it never reaches the knowledge entry.

## Method (read-only; no lane writes, no clone, no mutating git/jj)

```
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 1c779e4a:corpus/SOURCES.md            # row at :93, preamble at :9-11
git -C ... show 1c779e4a:corpus/lessons/round-50.md                                               # Gate bullet at :49
git -C ... show 1c779e4a:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md         # hits at :7 (shelf), :139, :140
git -C ... show 1c779e4a:corpus/QUALITY.md                                                        # criterion 6 at :29
curl -sS -o /dev/null -w '%{http_code}' --max-time 30 https://etcsl.orinst.ox.ac.uk/section5/tr532.htm
curl -sS -o /dev/null -w '%{http_code}' --max-time 15 http://etcsl.orinst.ox.ac.uk/section5/tr532.htm
curl -sS -L 'https://web.archive.org/web/20260605210113id_/https://etcsl.orinst.ox.ac.uk/section5/tr532.htm' | gunzip | sha256sum
curl -sS 'https://web.archive.org/cdx/search/cdx?url=etcsl.orinst.ox.ac.uk/section5/tr532.htm&output=json&from=2026&to=2026'
curl -sS -L 'https://web.archive.org/web/2026/https://etcsl.orinst.ox.ac.uk/catlist.htm'          # 5.3.2 numbering
curl -sS -L 'https://web.archive.org/web/2026/https://etcsl.orinst.ox.ac.uk/catalogue/catalogue5.htm'
```

## What holds (observed)

1. **Row shape.** `corpus/SOURCES.md:93` carries all 11 registry columns (`id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by`), `kind=dataset`, `tier=A`, `status=mined`, `opened=2026-10-21`, `recheck=365d`, `used-by=corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`. `dataset` is one of the seven kinds in the registry; the build seat recorded the alternative (`book`) and the reason (`.ufo/waves/round-50/build/SrcDumuzi.md`).
2. **Access route is exactly as filed.** Live host still times out from this seat: `https` → `curl: (28) Connection timed out after 30000 milliseconds`, code `000`; `http` → timeout after 15 s, code `000`. DNS resolves (`getent hosts` → `163.1.185.89 orin-hutton.orient.ox.ac.uk`), so the row's “host timed out” is a connection failure, not a name-resolution one. Archive reads at tier A are this round's own convention where the live host is unavailable (S052 tier A via mirror; S062 tier A via Wayback CAPTCHA).
3. **Capture exists and matches the seat's record.** CDX for the URL: `20260218064807 200 47QTFUXVUTJROVDRR6OKADGZU2IEWYFE 6000` and `20260605210113 200 47QTFUXVUTJROVDRR6OKADGZU2IEWYFE 6000` — the named 20260605210113 capture is real, HTTP 200, and byte-stable against the 2026-02-18 capture. The `id_` fetch is a gzip body that decompresses to **12,767 bytes, sha256 `97817899b6fdd7f5a567157b9b497ba2fbb2bef77c29ca3be0684551d43fd5f2`**, exactly the size/digest claimed in `.ufo/waves/round-50/build/SrcDumuzi.md`. The page is the publisher's own Oxford page (`<title>The debate between Sheep and Grain: translation`; revision history ends `7.ix.2001 … substantive content of file not changed`).
4. **Gate quote is verbatim and correctly located.** `corpus/lessons/round-50.md:49` records `lines 130–142: "Every night your count is made and your tally-stick put into the ground"`. In the capture the paragraph anchor is `<a name="para15" href="c532.htm#line130"><sup>130-142</sup></a>"Every night your count is made and your tally-stick put into the ground, so your herdsman can tell people …`. Machine check on the collapsed text: `quote found verbatim: True | words: 13` (≤25). The quoted clause is contiguous in one paragraph, not reassembled across tags.
5. **Composition number is correct.** ETCSL's own `catlist.htm` lists `5.3.2 The debate between Sheep and Grain: composite text | translation | bibliography (26.v.2000)`; `catalogue/catalogue5.htm` repeats `5.3.2 The debate between Sheep and Grain`. The URL path `section5/tr532.htm` matches.
6. **Tier/scope honest under `corpus/QUALITY.md:29` (criterion 6).** Criterion 6 reserves tier A for “sources primary or authoritative for the exact scope” and bars publisher blurbs/abstracts from A. S064's scope is exactly “the composition's own wording on herding and farming — an emic literary representation, not a description of pastoral practice”: ETCSL is the authoritative scholarly edition/translation for *what the composition says*, and the row explicitly refuses practice claims. No tier inflation; the narrowest possible scope is filed.
7. **Both entry citations are supported** (`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`):
   - `:139` `the farmer taunts the herder: "Every night your count is made and your tally-stick put into the ground" (S064)` — quote exact (see 4). The taunt is Grain's, addressed to Sheep; the poem's preceding block (123–129) supplies the economic personae: “when I am standing in the furrow in the field, my farmer chases away your herdsman with his cudgel.” Supported.
   - `:139` design check `the count is a literary fact before it is a ritual one` — the entry's own analytic caution, not a source assertion; consistent with the row's “emic literary representation”.
   - `:140` `the Sumerian disputation sets Sheep against Grain as rival sisters (S064)` — supported: `71` “Sister, I am your better”; `92` “My sister”; `65–70` “they started a quarrel … began a debate”; `180–191` Enki: “Sheep and Grain should be sisters! … But of the two, Grain shall be the greater”; `192–193` “Dispute spoken between Sheep and Grain: Sheep is left behind and Grain comes forward”.
   - `:140` design check `a theological ranking, not evidence of practice` — supported by Enki's verdict (180–191) and consistent with the row's scope.
   - `:7` shelf entry `S064 ETCSL *Debate between Sheep and Grain*` — bibliographic, accurate.
   No other `S064` occurrence exists in the entry (`git grep` at the commit: `:7`, `:139`, `:140`).
8. **Status bookkeeping consistent.** The row is `mined` with the entry as `used-by`, matching `corpus/lessons/round-50.md` “Status and used-by change log” (new rows S048–S069 enter `mined` with that `used-by`). No in-place field contradicts the lesson.

## Finding — the anchor's speech ordinal is wrong (only defect)

`corpus/SOURCES.md:93`, anchor column:

```
lines 130–142 (Grain's third speech); lines 180–191
```

The capture's speech structure (paragraph anchors from the `id_` bytes):

| anchor | line | range | speech intro |
|---|---|---|---|
| para8 | 71 | 71-82 | “Grain called out to Sheep” — Grain #1 |
| para10 | 92 | 92-101 | “Thereupon Sheep answered Grain” — Sheep #1 |
| para13 | 116 | 116-122 | “Again Grain addressed Sheep” — Grain #2 |
| para14 | 123 | 123-129 | *(continuation of Grain #2)* |
| para15 | 130 | 130-142 | *(closing paragraph of Grain #2; contains the quote)* |
| para16 | 143 | 143-155 | “Again Sheep answered Grain” — Sheep #2 |
| para18 | 169 | 169-179 | “Then Grain was hurt in her pride … Grain answered Sheep” — **Grain #3** |
| para19 | 180 | 180-191 | Enki's verdict |

So 130–142 is the closing paragraph of Grain's **second** speech; Grain's third speech begins at 169. The label is wrong under every plausible count (Grain's own speeches: 71, 116, 169; third speech in the poem: Sheep at 92). Provenance: the same phrase appears in the build seat's candidate row and quote list (`.ufo/waves/round-50/build/SrcDumuzi.md:39,75`) and was copied into the registry; it does **not** appear in the knowledge entry (`git grep 'third speech'` at the commit: only the seat report and `SOURCES.md:93`).

Severity: small but real. The quote, range and lesson Gate are correct, and no downstream claim repeats the ordinal; the row's `teaches` (count, rival sisters, theological ranking) is unaffected. The row is a citation pointer, and its annotation misidentifies the quoted speech.

## Caveat (not counted as a required fix): “the farmer taunts the herder”

The literal speaker in 130–142 is Grain — the deified grain, not a human farmer — addressing Sheep. The entry's gloss compresses the disputation's two economic personae into “farmer”/“herder”, which the poem itself supports at 123–129 (“my farmer chases away your herdsman”). Substantively supported; if exactness were demanded, “Grain taunts Sheep” would be tighter, but the entry's economic gloss is the point of the row and needs no change.

## Smallest fix (author-lane advice)

1. Correct the anchor annotation to:

   `lines 130–142 (closing paragraph of Grain's second speech; Grain's third speech is 169–179); lines 180–191`

   or, minimally, drop the ordinal: `lines 130–142; lines 180–191`.
2. Mechanism: `corpus/SOURCES.md:9-11` is append-only — only `status`, `recheck` and `used-by` change in place, and a correction is a new row whose `teaches` opens `supersedes S0NN —`. Following the round-49 precedent (S034/S038/S039 → S044–S046), file the correction as **S070** with `teaches` opening `supersedes S064 — anchor corrected: 130–142 is the closing paragraph of Grain's second speech (Grain's third is 169–179)`, same URL/tier/scope, and keep S064 untouched. If the registrar rules an anchor annotation non-substantive, a one-line erratum in the next round lesson's Gate is the lighter path; an in-place edit of `:93` would violate the preamble.
3. No change to the knowledge entry: both `S064` sentences and the quote are supported, and the entry never repeats the ordinal.

## Unresolved / not claimed

- Build-time live reachability cannot be re-proven retroactively; today's timeout on both schemes, the seat's recorded `curl (28)` output, the real CDX 200 capture and the matching decompressed sha256 corroborate the filed access route.
- The capture proves the 2026 text; it cannot prove what the Oxford host served to the build seat on 2026-10-21 beyond the stable digest chain (2022 → 2026 captures share `47QTFUXVUTJROVDRR6OKADGZU2IEWYFE`).
- `kind=dataset` for a literary translation is a taxonomy choice within the seven allowed values, not a criterion-6 tier issue; noted, not challenged.
- No installs, no clone, no background jobs. Temp captures under `/tmp` deleted after this report; no lane file, git index, jj state or sibling artifact touched.
