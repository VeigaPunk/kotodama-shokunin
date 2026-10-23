# ReviewerEntry — round-64 wave 1, claim C entry review (review_only)

Reviewer: kotodama-r64.ReviewerEntry · 2026-10-23 · Axes judged: coverage, operability, calibration
Scope: `.ufo/waves/round-64/rows/ScribeEntrySkeleton/entry.md` (lane, unmodified) plus the mapped bullets. Four items: topic fit, lore handoff, one-way pointing, framing-vs-bullets overclaim.

## Inputs actually used (snapshot)

- Skeleton: `.ufo/waves/round-64/rows/ScribeEntrySkeleton/entry.md` (lines cited as `SK:n`).
- Canonical bullet text = each row's `BULLET` field in `.ufo/waves/round-64/rows/ScribeRowS*/row.txt`. `integrate-w2.py:192` renders bullets from `contributions[sid]["fields"]["BULLET"]`; `integrate-w2.py` never reads `stage/bullets.json` (grep over `.ufo/waves/round-64/` shows no reference to it in that file).
- `stage/bullets.json` reviewed too, because my dispatch named it — but it is **stale and unused** (finding F2), so framing verdicts below are keyed to the row.txt bullets that assembly actually ships.
- Boundary docs: `PROVINCE.md`, `corpus/knowledge/synthesis/worldbible-integration-contract.md` (exists; read in full), frozen counter `reports/round-64/accept-c.py` (leg docs, lines 16–48).

## Method (all mutation confined to scratch)

Copied the lane read-only into `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ReviewerEntry/lane` (`cp -a`). In the scratch copy only: added synthetic S723/S740 `row.txt` placeholders (SYNTHETIC, not sources — needed solely to get past the known missing-rows gate) and a synthetic `readme-row.txt` (also known missing). Then:

```text
$ python3 -B .ufo/waves/round-64/integrate-w2.py --root <scratch>/lane --rows-dir <scratch>/lane/.ufo/waves/round-64/rows --dry-run
INTEGRATE_ERROR generated entry would fail check-cited-lines.py at line 4: S718,S743   (exit=2)
```

After revising scratch skeleton SK:4 to the id-free wording the assembler's replace produces, in the same scratch copy:

```text
DRY-RUN root=... registry: append 32 rows ...; 643 -> 675 rows
entry: write corpus/knowledge/linguistics/language-socialization-and-acquisition.md with 26 mapped bullets
README: insert index row; linguistics header 29 -> 30; total/footer 237 -> 238
... real run: WROTE corpus/SOURCES.md, entry, README.md — ASSEMBLED registry_rows=675 entry_files=238 (exit=0)
$ python3 -B tools/check-cited-lines.py corpus/knowledge/linguistics/language-socialization-and-acquisition.md
CITED-LINES: 0 finding(s) in 1 file(s)   (exit=0)
```

The assembled scratch entry is at `<scratch>/lane/corpus/knowledge/linguistics/language-socialization-and-acquisition.md` (line pointers below cited as `ASM:n`). The lane repo itself was not modified by any of this; the only lane write is this report file.

## Verdicts on the four assigned items

### (1) Topic fit — PASS

- Entry is a sourced design reference for fictional language practices (SK:3, "not a universal developmental sequence"); it lives in `corpus/knowledge/linguistics/`, which `PROVINCE.md` §Owns lists as kotodama-owned.
- No canon content anywhere: no fictional entities, dates, or populations are asserted; every empirical line is a row-cited real-world claim; the §9 table (SK:53–59) is conditional design prompts, explicitly "not prescriptions" (SK:50). No game-mechanics, research-method, or rights content (PROVINCE §Refuses) appears.
- Evidence: full skeleton read; assembled entry `ASM:1–81` contains zero canon-standing language.

### (2) Final section's lore handoff — PASS

- `ASM:81` / SK:63: "it makes no canon decision. Lore-shokunin owns the world bible and its consistency verification under `corpus/knowledge/synthesis/worldbible-integration-contract.md`; contested scope goes to the integrator."
- Accurate against the contract: lore's ownership of bible-wide consistency verification matches contract §1; "contested scope goes to the integrator" matches contract §10 route and `PROVINCE.md` "Contested scope → report to the integrator, never absorb."
- It claims no packet, no acceptance, no acknowledgement state (contract §1's pending bilateral read is not misrepresented); nothing is "handed" — the entry only states the division of labor. No canon claimed.

### (3) One-way pointing — PASS

- The single outward reference is to lore's ownership via the lane-local contract path (the file exists and is kotodama-owned, so no sibling path is invented). Lore is pointed at, not restated: no canon entity, ruling, or bible content is repeated; no lore repo path is cited. The integrator is named as a role, without restating integrator rules.
- No reverse pointer claims lore's acknowledgment of this entry.

### (4) Framing prose vs bullets, per section — PASS with minor placement notes (F3)

Judged against the row.txt bullets as assembled (scratch proof above):

- §1 (SK:8–11; ASM:11): prose is instructional, no empirical assertion beyond S726's "linked to social membership". OK; section is thin (one bullet) but the heading's "is not" work is done by the prose's scope-limiting sentences, not by invented claims.
- §2 (SK:13–16; ASM:16–19): prose "compare documented registers by their features and interactional settings" — supported (S718/S729 IDS vs ADS rates in-sample; S719 IDS prosody attention; S724 child telegraphic output). No overclaim. Note S718 and S729 are the same study with near-duplicate bullets (F4), and S724 sits under a "talk to children" heading though it is child output — placement tension only, prose's "decide who speaks, which forms are available" covers it.
- §3 (SK:18–21; ASM:24–27): prose explicitly forbids deriving one topic from another ("Keep those topics distinct rather than deriving one from another") — exactly matches the bullets (babble S720, turn-taking S721, vocabulary S722, first words S723 pending). Anti-ladder framing is the strongest in the entry. S723 row still MISSING (known, inherited); assembly hard-fails until it lands (see F1 sequencing).
- §4 (SK:23–26; ASM:32–34): prose asks to "separate a correction episode from the conclusions a source permits about learning" — S725 is hedged ("may imitate"), matching its row's two-year-old recast scope. S743 (Japanese child-directed verb register) is a register fact, only weakly hooked by "how a response is framed" — placement tension (F3), not an overclaim.
- §5 (SK:28–31; ASM:39–42): prose demands "each practice attached to its source, language, setting, and stated limits" and "rather than... a single ladder" — the bullets are case-specific (Samoan S727, Kaluli S728, adoptive family S738, US classroom S742). No overclaim by the prose. Row-fidelity observations (L1 axis, not prose): S728's bullet states the Kaluli claim un-hedged where the row flags Frye as a secondary account of Schieffelin; S742's bullet drops the row's "one second-grade classroom" setting (F5).
- §6 (SK:33–36; ASM:47–50): prose "not as one uniform pathway... preserve source-specific terms and limits" — S731 is properly scoped ("in this sample"); S732 hedged ("sometimes"); S730 is definitional. S733 (ASL vocabulary growth) is not a bilingual/heritage case as bulleted — placement tension (F3).
- §7 (SK:38–41; ASM:55–57): prose "do not make one cited example stand for every speaker" — bullets are hedged ("may", "can", "plausible"). PASS cleanly.
- §8 (SK:43–46; ASM:62–64): prose covers "names, address forms, and honorific choices"; S741 is taboo words, not named in the prose but covered by "social index... distribution" — mild underlap only. S740 row MISSING (known).
- §9 (SK:48–59): zero bullets by design; prose marks the table "conditional design prompts, not prescriptions". Table rows are fictional design options, not empirical claims ("Correction is private or indirect" is a choice to offer a worldbuilder, not a sourced assertion). PASS.
- §10: see item (2). PASS.

## Findings by severity

### F1 — HIGH (operability; blocks assembly once the known gaps close): skeleton/assembler wording drift makes assembly fail deterministically

- `integrate-w2.py:168–172` replaces the exact string `Round-64 row citations S718–S743 in \`corpus/SOURCES.md\` supply the source claims; each claim is limited to its cited row.` — that string does not exist in the skeleton. SK:4 reads `- source: S718–S743 in \`corpus/SOURCES.md\` are the intended evidence anchors; each inserted claim must stay within its cited row.` The replace is a no-op, so the generated entry keeps two S-ids on line 4 and `integrate-w2.py:199–205` (mirroring the frozen counter's ONEID leg, accept-c.py:30–31) raises. Reproduced: `INTEGRATE_ERROR generated entry would fail check-cited-lines.py at line 4: S718,S743` (exit=2).
- Today this is masked by the earlier gate `missing contribution ids: S723, S740` (`integrate-w2.py:152–156`) and by the unwritten `readme-row.txt`; the line-4 failure fires next, after those two known repairs land. Dead attempt-1 left skeleton and assembler revised out of sync.
- Proposed pre-data revision (forcing control: the frozen ONEID leg — do not touch the counter): either change SK:4 to the id-free wording (exactly what I applied in scratch; then assembly, cited-lines check, and PLAN 643→675 all pass, outputs pasted above), or point the assembler's replace target at the actual SK:4 string. One-line, either side; owner's call. The "intended evidence anchors" wording is honest pre-data text — if kept, the assembler must strip it; if the entry is finalized post-data, the wording must become the id-free form anyway.

### F2 — MEDIUM (coverage; review-input integrity): `stage/bullets.json` is stale and is not an assembler input

- It holds only 19 of the 26 mapped ids; missing keys: S721, S723, S727, S733, S740, S741, S743 — even though S721/S727/S733/S741/S743 `row.txt` files exist with BULLET fields today. Four surviving keys have drifted from the canonical row.txt bullets:
  - S738: json "Expert guidance prioritized children's well-being and accommodated their needs linguistically during adoptive language socialization" vs row "Experts instructed parents not to introduce Polish immediately after meeting the children" — the json version generalizes one family's specific instruction into a broad claim; had it been assembled, §5 would overclaim its row.
  - S739: json flips direction ("teaches children to model culturally specific forms for addressing relatives") vs the row's parent→child evidence ("Parents can use various terms of address to children").
  - S742: json generalizes classroom → "a child's community-building practice" vs row's "shared classroom practice".
  - S719: mild rewording ("distinct attention cue" vs "helping caregivers attract a baby's attention").
- `integrate-w2.py` ignores it (bullets come from row.txt fields), but wave-2's separate plan builds a different assembler keyed to `{CACHE}/w2/bullets.json` (gen-w2.py:289) — same filename, different role. Anyone seeding the wave-2 json from this stale `stage/bullets.json` ships the S738/S739 overclaims and 7 holes.
- Smallest safe correction, owner's discretion: regenerate `stage/bullets.json` from current row.txt BULLET fields or delete it from the staging set, and say in dispatch that row.txt BULLET fields are canonical.

### F3 — LOW (coverage): three bullet-to-section placement tensions (no prose overclaim)

S743 (child-directed verb register) under §4 correction/metalinguistic awareness; S733 (ASL vocabulary acquisition) under §6 "more than one language"; S724 (child telegraphic output) under §2 "talk to children". The framing prose nowhere asserts what these bullets do not support, and accept-c's RESTATE leg checks bullets against their own row quotes, so nothing frozen depends on the placement. If the skeleton owner wants tighter fit, a pre-data remap or a one-clause prose acknowledgment suffices; not required for the claims to hold.

### F4 — LOW (coverage hygiene): S718 and S729 are the same study (Farran et al. 2016, PLOS ONE 11(3):e0151518) with near-duplicate bullets (ASM:16, ASM:19)

Assembled §2 presents duplicate support as two anchors. Row-level duplication is the registry reviewers' axis; flagged so it is a decision, not a surprise. (LOCATED captures differ: PMC vs PLOS — rows are individually verifiable.)

### F5 — LOW (calibration observation; L1/row-fidelity axis, recorded not judged here)

S728's bullet states the Kaluli elema claim without the row's secondary-account hedge (row: "Frye's secondary account of Schieffelin's report"); S742's bullet drops the row's single-classroom setting. Section §5's prose partially compensates ("Keep each practice attached to its source, language, setting, and stated limits"). The frozen RESTATE leg (≥3 in-order content words from the row quote) does not test hedges; flagging for L1 insertion review so the hedge loss is a conscious choice.

## Residual risk and verification gaps

- I did not run `reports/round-64/accept-c.py` itself (not my item; its legs ROWS/REJECTS/LIVE depend on the still-missing S723/S740 and real registry insertion). My assembly proof used synthetic S723/S740 placeholder rows — SYNTHETIC, not sources; they prove mechanics only, and the entry content verdicts for §3 and §8 rest on the 24 real bullets plus the known-missing status of S723/S740.
- I verified `worldbible-integration-contract.md` exists and read §1/§10 for the handoff wording; I did not audit the whole contract (out of scope).
- I did not re-verify row locators (LIVE leg owners own that); my quotes come from the row.txt VERIFY/CAPTURE/ACCESS fields as staged.
- F1's fix choice (skeleton line vs assembler replace target) is the owner's; both were validated only in the scratch copy.
- No tools were installed or upgraded for this review (nothing needed beyond repo python3); nothing to record under the tooling directive.

## Bottom line

Items (1), (2), (3): PASS. Item (4): PASS with placement notes. The entry text itself is clean of canon claims and of framing overclaims once assembled from row.txt bullets. The one actionable defect in my scope is F1 (deterministic assembly failure from the SK:4 / replace-target drift — one-line pre-data revision required, counter untouched), and F2 (stale, unused `stage/bullets.json` that my own dispatch pointed at — regenerate or delete to keep wave-2 seeds honest).
