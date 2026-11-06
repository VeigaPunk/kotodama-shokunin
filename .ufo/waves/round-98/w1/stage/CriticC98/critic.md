# CriticC98 — falsification attempt on claim C (toasts and drinking-speech formulae), kotodama round 98

Seat: CriticC98 (critic; edit-nothing-in-lane). Frozen inputs read first: `reports/round-98/claims.json` and `reports/round-98/predispatch.py` (580 lines, all C-legs read); controls `predispatch-base.txt` (PREDISPATCH-98: FAIL legs=5/15), `controls/forgery-summary.txt` (6 fixtures). Base `bcf664aa089ddbd1fac85772ed22a38d1b454d23`; freeze commit `db88f107`. Dependencies waited on (bounded loop, 60 s x N, exit when both exist, rc 0): `.ufo/waves/round-98/w1/stage/ScribeEntry98/DONE` (sha `0724a044…d4cf`) and `.ufo/waves/round-98/w1/stage/ExecRegistry98/DONE` (sha `72a1c504…9582b`). No frozen file touched; the only lane bytes written by this seat are this stage, the wave Report, and DONE.

Axes (godspeed): A1 base ownership, A2 duplicate authority / overlap, A3 citation integrity, A4 source support, A5 verdict.

## Leg 1 — is the surface truly unowned at base by content? YES.

Command (rc=0): `git -C <lane> grep -n -i -E 'toast|wassail|bragaf|libation|symposi|tamada|loving cup' bcf664aa… -- corpus/knowledge` → 11 hit-lines. Per-token file counts at base over `corpus/knowledge` (rc=0): toast=0, wassail=0, bragaf=0, toastmaster=0, health-drink=0, tamada=0, `loving cup`=0; libation=4 files; symposi=4 files. Whole-tree toast-family sweep (toast|wassail|bragaf|toastmaster|health-drink|drinking oath|toast formula|toast sequence, rc=0): only `.ufo/waves/*` artifacts and `reports/round-{86,90,96}/evidence/S{925,949,976}.*` capture bytes — no corpus knowledge file, no SOURCES row text.

Every substantive hit inspected (file:line at base):
- `ainu.md:109` — `ikupasuy` libation stick + `tuki` cup in a prayer-communication implement table cell. Implement sense; not drinking speech.
- `funerary-material-culture.md:8` — reference-layer mention of *patera* for libation (vessel side).
- `vessel-container-lexicon.md:5, :36, :38` — libation dish (*phiale*, *patera*), SERVING job row, ritual extensions. Container side.
- `death-afterlife-eschatology.md:41, :100` — libations inside the ancestor-offering economy (kispu, Parentalia, Ghost Festival). Dead-offering sense.
- `furniture-interior-lexicon.md:52` — "the dining couch belonged to the symposium" (seating history).
- `inca.md:187`, `japan-edo.md:27`, `ritual-garments.md:12` — the token matched is "Symposium" inside "Textile Society of America Symposium Proceedings" citations. Bibliographic false positives.

No base file teaches drinking-speech formulae as a section; none owns a frozen phrase in a topic line or heading (counter C8 guard: owners=0 on base, measured `predispatch-base.txt` LEG C8 PASS files scanned=269 other owners=0). **The new entry is expansion into an empty surface, not duplicate authority.** Prose nit (F3, frozen-claims side, unfixable): the `C.before` parenthetical lists libation at "ainu.md:109, funerary-material-culture.md, vessel-container-lexicon.md:5 and :36" but misses `vessel-container-lexicon.md:38` and `death-afterlife-eschatology.md:41/:100`; the operative sentence ("4 files, prose or table cells only") is correct and my count agrees (4 files).

Adjacent-risk check at base (are the neighbors already teaching this?): oath entry has no feast/drink/cup section (its "health" hits are self-imprecation targets, :109); duelling entry names "a drink" only as a release-rule example (:182) and owns the boast formula (§6); guest-right entry teaches the shared cup as bond-opening marker and seal (topic line :3, table :33-:34, checklist :98) — property boundary the entry must and does respect.

## Leg 2 — overlap with adjacent owners: 19 shared 8-grams total; no duplicate authority.

Method: word-level, case-folded 8-grams (`[a-z0-9']+` tokens), independent script `overlap8.py` (scratch, deleted after; one path-resolution bug fixed and rerun). Owners = the ten files named in `stage/ConnectorOverlap98/overlap.md` §3 (9 assigned + death-afterlife-eschatology.md), all exist (rc=0). Entry: 8,211 8-grams.

| owner | shared 8-gram occurrences | distinct |
|---|---|---|
| linguistics/verbal-duelling-ritual-insult.md | 11 | 11 |
| linguistics/oath-blessing-curse-formulae.md | 6 | 6 |
| linguistics/petitionary-and-votive-formulae.md | 2 | 2 |
| vessel / cuisine / guest-right / greeting / calendar / ritual-liminality / death-afterlife | 0 | 0 |
| **total** | **19** | |

Top three spans (word-level): 11 w "performative verb witness invocation assertion sanction clause self imprecation uptake and" — the deliberate six-slot cross-reference of the oath entry's own list (couples line + §6.1, pointer not restatement); 9 w "the rules above make these failures checkable because each" — stock frame sentence also opening duelling §10; 8 w "verified at 2026 11 05 recheck 180d topic" — head-matter boilerplate every entry shares. Scale reference: CriticC97 measured 294 shared 8-grams on the r97 entry, repaired to 35. 19 < 35, and the largest span is terminology pointed at, not teaching copied. Cosmetic stock-prose reuse (9 w/8 w spans) noted, no boundary crossed. **Pass.**

## Leg 3 — citation integrity: all clean.

Independent recount `citecheck.py` (own implementation, not counter bytes; rc=0): rows_total=929, highest=S1005, qualifying=11 (S994–S1004: id>S993, tier A|B, status mined, opened 2026-11-05, used-by exactly the entry path); S1005 correctly not qualifying (supersede row, used-by `corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md`, implements r97 routed defect 1; `s992.md` documents the S992 in-place edit — status mined→queued, used-by →—, fixed cells 0-6/8 identical — the rule-2-legal edit; old→new logging rides rows.md/s992.md until the L1 lands the round lesson). Entry cites all 11 qualifying ids, zero uncited. rows.md ids vs entry-cited ids: rows.md minus qualifying = {S1005, S992, S993} (supersede row + context mentions), qualifying minus rows.md = ∅ — consistent. Manifest binding: 0 failures — all 17 captures exist with matching sha256, every quote 1..25 words, ws-collapsed quote count exactly 1 in its named quote_capture, quote present in the row's anchor cell. Census read-only: `bash scripts/sources-census.sh validate --file corpus/SOURCES.md` → rc=0, final `ok` (W01 tier-C-mined ×5 and W04 duplicate-URL ×28 findings are pre-existing base rows, not this round's). **Pass.**

## Leg 4 — source support: 49 probes, all resolved; 2 minor defects, 0 fatal.

Probe script over the named captures (ws-collapsed containment + count; rc=1 driven by 3 probe misses, each resolved below). Every quoted string the entry attributes to a source was checked, plus paraphrase keys:

- S994 goblet order (entry §5/§6.1/§8): grounded at capture :2487-2494 ("And first Odin's goblet was emptied for victory and power to his king; thereafter, Niord's and Freyja's goblets for peace and a good season. Then it was the custom of many to empty the brage-goblet…; and then the guests emptied a goblet to the memory of departed friends, called the remembrance goblet") + endnote :2509 ("The brage-goblet, over which vows were made"). All counts verified.
- S995: Old Norse anchor count=1; `bragafull` ×2 in capture.
- S996: anchor count=1; no-compulsion passage :1196-1200 ("It was agreed that drinking was not to be the order of the day, but that they were all to drink only so much as they pleased… there is to be no compulsion").
- S997: "Quite right (said Callias), and we will pledge you." count=1; "push the cups round", "charioteers", "quickening" each count=1.
- S998: "the pledge-cup to the Good Deity" count=1; "a taste of the unmixed wine should be served round" count=1; "tyrant" ×52, "Good Deity" ×10 (§4 sentences faithful).
- S999: all five entry sentences grounded in the scholarly body :55-70 ("two men are present, one of them is selected to be tamada… knowledgeable, witty, and articulate, but also a good drinker"; "No wine is to be consumed unless a toast… after which he – and only he – drinks"; "the other guests, one after the other… on the same theme"; "The order of toasts, especially in the opening phase of… follows a quite rigid sequence"; "single draught… only the tamada is obliged"). The paper's Text A–D specimen section (:1109-1147, including fictional "X people" Text D) is NOT cited anywhere in the entry — no fiction-within-source contamination.
- S1000: anchor count=1. S1001: anchor count=1; "before everyone simultaneously drinks" count=1; choreography sentence faithful to :393 ("standing to toast… around a table, touching glasses (or merely lifting them) and making eye contact (or gazing into space) before everyone simultaneously drinks"). S1002: "offered to drink your health" count=1; "Your answer to her must be 'Drinc heil'" count=1. S1003: anchor count=1; vessel placement faithful to :21915-21919 ("the chief of the district… had the vessel of liquor placed between the room (on the east), and the door…, host and guests sharing it between them"). S1004: anchor count=1; "no man must drink a toast if it went against his principles" count=1; "manliness" count=1.

Uncited-and-unmarked claims: none found. The grading apparatus is applied consistently — "(design, not sourced)" on every proposal (slot list §2, tables §3/§5/§6.2/§8, rules §7, procedure §9, failures §10, checklist §11), "(inference)" plus a 7-item §13 ledger for readings beyond sources, registry ids on every recorded-practice sentence. The one corpus-internal reference (`civilizations/ainu.md`) matches base ainu.md:109 exactly.

**F1 (defect, minor).** S994's `teaches` cell ends "Oceanic and other cups besides Odin's, Njord's and Freyja's." The Odin/Niord/Freyja enumeration is grounded (:2487-2489), but the word "Oceanic" occurs in no capture: `grep -r -l 'Oceanic' reports/round-98/evidence` → NONE; S994.txt `ceanic`=0, `okenn`=0, `bragafull`=0 (that capture says "brage-goblet"). One ungrounded token in a fixed cell. Not caught by any leg (C7 binds quote↔anchor; census checks shape). Smallest safe correction: superseding row per CORPUS rule 2 (teaches is not in-place-mutable), same capture, or an L1 landing-ruling of it as a drafting slip.
**F2 (defect, minor).** Entry §8 grounding list quotes S996 as "they were all to drink only as much as they pleased", but capture :1197 reads "they were all to drink only **so much** as they pleased" — one-word divergence inside quotation marks (the §7 body paraphrase is faithful). Not caught by C7 (the manifest quote for S996 is the other, verbatim-count-1 string). Smallest safe correction: one-word fix in the entry's §8 line, or drop the quotation marks.

## Verdict

**Claim C survives falsification.** Base ownership clean (leg 1); duplicate-authority overlap 19 8-grams against a 35 precedent threshold (leg 2); citation integrity, manifest binding and census clean (leg 3); every cited sentence supported, tagging discipline consistent (leg 4). Counter legs C1-C8 pass on the landed tree (independently re-derived C2/C6/C7 equivalents; C1/C3/C5/C8 confirmed in ExecRegistry98's counter run `counter.txt`); C9 is ReviewerC98's non-author re-open leg and that seat was still running at my check — outside this seat's falsification scope. F1 and F2 are real, small, ledger-worthy defects for the round lesson; neither flips a leg. No tooling installed (pacman pause respected); scratch dir deleted before yield.
