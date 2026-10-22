# CriticCalibrationBank — round 55 falsify, claim C §14 (Calibration bank)

Seat: KotodamaR55.CriticCalibrationBank (critic, read-only leaf). Target: `corpus/knowledge/myth-symbol/monsters-hybrid-beings.md:167-178` at `eb0a331`. Codes checked against `corpus/knowledge/verification/calibration-registry.md:35-39` (lines confirmed: R 35, C 36, B 37, H 38, T 39). Scratch: `/fast/scratch/hyaku/kotodama-r55-falsify/CriticCalibrationBank/`. No tools installed or upgraded.

## Verdict

**DEFECT: 5 of the 8 bank items need a fix. Three of them get the wrong code or code strength (griffin, cryptids, yōkai). One gives no bound for its code (monere). One over-reads a clause (Pazuzu in "monster means evil").** The medieval item and the Cohen item are carried. The dragons item keeps its code, but one clause over-reads.

- **Griffin, `:172`.** "R as an origin" is premature saturation. The bank's only evidence against the thesis is one 2024 critique. That critique says the idea had "received little in the way of academic scrutiny", and it records a referee who disagreed with its conclusions. Its rejection also covers "influence", so the "C as influence" half has no cited support. The code that fits is C, with the weight of evidence stated. `animal-symbolism.md:109` ("attractive, contested") is the better-calibrated line. The routed item at `corpus/lessons/round-55.md:213` would spread the error into a second file and should be reversed.
- **Cryptids, `:176`.** The source is described at the wrong strength and over-read on content. The refereed undergraduate paper does not "argue that cryptozoology fails the demarcation test". On printed p. 6 it says "a case can be made to legitimize at least some parts". Its conclusion leaves the field "at best, a transitional field of research". "B as modern folklore" names no domain, and no cited row mentions folklore.
- **Monere, `:173`.** The derivation is carried, and the erratum at `divination-omen-systems.md:72` is present. But B is used without the named domain that B requires. Its stop rule, "State both, each attributed", is the C rule.
- **Yōkai, `:175`.** R against "ancient" is an overcorrection that the cited page itself contradicts. The Nichibunken glossary cites 下學集 and 太平記 for the older sense of 妖怪. Neither of the bank's two locators is backed by a quote in row S295.
- **"Monster means evil", `:177`.** "Pazuzu is largely amoral (S304)" has no locator. It also narrows a hedged sentence about supernatural beings in general into a statement about Pazuzu.

## Item lines

- **`:171`, dragons, code R — CARRIED (code), OVER-READ (one clause).** S351 is carried. Britannica, article body ¶1: "a large lizard- or serpent-like creature, conceived in some traditions as evil and in others as beneficent." (Wayback 20261007001308.) S338 does not say "English writers". Te Ara, A creature of many forms: "Others refer to them as dragons – many taniwha looked like reptiles, had wings and ate people." (Wayback 20260921201758.) Fix: "English writers have called taniwha dragons (S338, A creature of many forms)" → "Te Ara notes that others call taniwha dragons, since many looked like reptiles, had wings and ate people (S338, A creature of many forms)". The same over-read sits at `:113` in §9 and needs the same fix. "The count comes from the English label" is the designer's inference, not a sourced finding. It is acceptable under R as the general inference, but the build critic's guard against "some cultures have no dragons" (`.ufo/waves/round-55/build/CriticCalibrationMonsters.md:13`) was dropped.

- **`:172`, griffin, code "R as an origin, C as influence" — DEFECT (code over-reads S343; the "influence" half is unsupported).**
  - The sentence's quotes are carried. S343, Abstract: "An evaluation of the Protoceratops–griffin link, however, finds it uncompelling." S352, publisher's description ¶2: "sprang from tales first told by Scythian gold-miners". (The live Princeton page served a Cloudflare challenge, met and not passed. I read Wayback `20260729165509id_` instead; the row records a plain HTTP 200, which I did not reproduce.) The PDF's sha256 matches the row (`181be558…3f61`).
  - Counterexamples to R (registry `:35`, "Rejected/discredited") from the same PDF:
    - p. 2, Figure 1 caption: "This idea, first proposed in the early 1990s, has received little in the way of academic scrutiny, however."
    - p. 23, Acknowledgements: "An anonymous referee, through disagreeing with our conclusions, helped us to sharpen and refine our arguments."
    - p. 23, closing paragraph: "There is nothing inherently implausible with the idea that ancient peoples found dinosaur bones and incorporated them into mythology".
  - The authors describe the thesis as "widely promoted". One evaluation, published over a dissenting referee, is a strong C weighted against the thesis. It is not a field-level rejection.
  - Figure 1 caption, p. 2: the rejected claim is that fossils "inspired or influenced the mythology of the griffin". Witton and Hing reject influence as well as origin, and S352 states origin ("sprang from"). No cited row supports "influence" as the live alternative that "C as influence" implies.
  - Fix: "**R as an origin, C as influence — "griffins came from…"** … (S343, Abstract)." → "**C — "griffins came from *Protoceratops* fossils."** Princeton presents Mayor's thesis that the legend sprang from tales told by Scythian gold-miners (S352, publisher's description, ¶2); Witton and Hing (2024) find the link uncompelling and call it an "ex post facto geomyth" (S343, Abstract). The published evaluation weighs against the thesis; do not state it as the griffin's origin."
  - Routed-fix impact: reverse `corpus/lessons/round-55.md:213`. `animal-symbolism.md:109` "attractive, contested" stands, so two files would not carry two different codes for one proposition.

- **`:173`, monere, code B — DEFECT (code fits only once its domain is named; the stop rule given is C's).**
  - The derivation is carried. Lewis and Short (Perseus, HTTP 200, 133,864 bytes): "monstrum, i, n. moneo. I. Orig. belonging to relig. lang., a divine omen indicating misfortune". The Festus gloss inside the entry reads "quod moneat aliquid futurum".
  - Cicero is carried: L&S quotes Div. 1.93 as "quia ostendunt, portendunt, monstrant, praedicunt, ostenta, portenta, monstra, prodigia dicuntur".
  - The problem: registry `:37` requires B to carry "population, genre, period, task". The item names none of these. "State both, each attributed" restates C's rule at `:36`. The S286 tier note already gives the bound: "an attributed Roman antiquarian claim quoted from Festus, not a modern etymology".
  - Fix: "**B — "monster comes from *monere*, to warn."** Lewis and Short give that derivation (S286, sense I); Cicero ties…" → "**B, as Latin word history only — "monster comes from *monere*, to warn."** Lewis and Short head *monstrum* with *moneo* and quote Festus's "quod moneat aliquid futurum" (S286, sense I); Cicero instead ties *monstra* to *monstrant* (S287, 1.93). State both, each attributed; never use either to define what a taniwha, *yōkai* or *long* is."
  - Erratum check: `divination-omen-systems.md:72` carries the round-55 erratum as claimed.

- **`:174`, medieval belief, code C — CARRIED (one locator incomplete).**
  - Augustine (New Advent, HTTP 200), XVI.8 ¶2: "But we are not bound to believe all we hear of these monstrosities."
  - Isidore (LacusCurtius, HTTP 200), XI.3 §28: "alia hominum fabulosa portenta, quae non sunt, sed ficta in causis rerum interpretantur".
  - The "asserts some races" half is located at §12, not §28: "quaedam monstra sunt gentium, ut Gigantes, Cynocephali, Cyclopes". Fix: "(S289, XI.3 §28)" → "(S289, XI.3 §§12, 28)". This needs a §12 quote added to row S289.

- **`:175`, yōkai, code R — DEFECT (overcorrection; both locators lack a row quote).**
  - Nichibunken (HTTP 200, 30,166 bytes), Glossary 【妖怪】: "Something of strange appearance with unknowable or mysterious powers. 下學集、太平記." The same entry continues: "Today the term is used more broadly in popular culture".
  - "spanning from the late Edo period to the present" sits under "Development of the Database". It describes the database's collection window, not the history of the category.
  - "Ambiguous" is Komatsu's word as quoted by the page ("The word yōkai is an ambiguous term among both academics and lay-people"). `:23` attributes it correctly; `:175` writes "Nichibunken calls".
  - The S295 quote column holds neither the "ambiguous" sentence nor the late-Edo sentence.
  - The build critic coded this item "R for 'unchanged'; B for premodern attestations" and warned "do not call *yōkai* a modern invention" (`build/CriticCalibrationMonsters.md:17`). The landed item dropped that split.
  - Fix: → "**R for "unchanged", B for the word's premodern record — "*yōkai* are ancient and unchanged."** Nichibunken's glossary cites 下學集 and 太平記 for the older sense of 妖怪 and adds that "Today the term is used more broadly in popular culture" (S295, Glossary, 妖怪); the database's records run from the late Edo period to the present (S295, Development of the Database)." This needs those two quotes added to row S295.

- **`:176`, cryptids, code "R as zoology, B as modern folklore" — DEFECT (S354 over-read on content; B unbounded and unsourced).**
  - Strength: the SURG About page calls the journal "refereed", with "peer review by faculty with expertise in a similar subject area". It also says undergraduate journals "publish work that might not meet the requirements of mainstream academic journals". The paper's own head note says it was written "under the supervision of Professor Sofie Lachapelle, Department of History". "Refereed student study" is accurate. The row's Grounds and the lesson Gate line `round-55.md:138` say "The peer-reviewed article", which drops "undergraduate".
  - Content: printed p. 6, section "Cryptozoology as a Pseudoscience": "Using these factors, however, a case can be made to legitimize at least some parts of cryptozoology". Printed p. 9: "It may be beneficial to legitimize cryptozoology as a science". Printed p. 10: "at worst, a pseudo-science and, at best, a transitional field of research". "Argues that cryptozoology fails the demarcation test" over-reads all three passages.
  - What does carry R as zoology:
    - S354, printed p. 6, end of "Cryptozoology as a Discipline": "the consensus of the overall scientific community lean far more towards ridicule and the rejection of this discipline as a legitimate science". This is not in the row's quotes.
    - S343, p. 3: cryptozoology "today, it struggles for credibility among academics". This is in the bank's A-tier source, which the build critic used for this item. It is not in the row's quotes either.
  - The p. 8 clause (cryptozoologists separating themselves from paracryptozoology) is carried: "Cryptozoologists strongly dismiss the claims of paracryptozoologists".
  - S355, description ¶1 (Columbia, HTTP 200): "After examining the nature of science and pseudoscience and their relation to cryptozoology". "Testing science against pseudoscience" is a loose paraphrase.
  - Fix: → "**R as zoology, B as a modern belief subculture — cryptids.** A faculty-refereed undergraduate paper reports that scientific consensus leans toward rejecting cryptozoology as a legitimate science, yet leaves it "at best, a transitional field of research" (S354, printed pp. 6, 10), and records cryptozoologists separating hidden animals from frankly supernatural beings (S354, printed p. 8); Columbia University Press describes Loxton and Prothero's book as examining science and pseudoscience in cryptozoology, challenging the pseudoscience behind named cryptids, and analysing the subculture's persistent belief (S355, description, ¶¶1–2)." This needs the p. 6 consensus quote added to row S354, and the row's Grounds changed to "The refereed undergraduate article…".

- **`:177`, "monster means evil", code R — CARRIED (code), OVER-READ (Pazuzu clause, no locator).**
  - S295, Glossary 鬼: "Oni are not necessarily evil and can become a kami if worshipped". S338: "Others were kaitiaki, or protectors of iwi (tribes) and hapū (sub-tribes)." Both are carried.
  - The Met blog (Wayback `20171121161933id_`, HTTP 200), § beginning "To answer this question": "supernatural beings in ancient references seem to be presented as largely amoral". The sentence is hedged and about the category, as the row's own locator says ("on the category").
  - Fix: "Pazuzu is largely amoral (S304)" → "the Met's curator writes that ancient Near Eastern supernatural beings "seem to be presented as largely amoral", and Pazuzu served as a shield against Lamashtu (S304, § beginning "To answer this question")".

- **`:178`, Cohen, code H — CARRIED (one genre label wrong).** The S356 quotes for Theses I, III and V match the paraphrase. I did not re-open the Cohen PDF. S357 (nature.com, HTTP 200, 372,255 bytes) carries `citation_article_type" content="Comment"`, so "A 2020 survey" mislabels the genre. Fix: "A 2020 survey names" → "A 2020 comment introducing an interdisciplinary collection names". A further point for the monere item: S356 Thesis I gives "that which reveals," "that which warns", which fuses the two ancient derivations. The bank should not lean on Cohen for the etymology.

## Impacted axes

- **Calibration:** R overstated on the griffin and yōkai items; B unbounded on the monere and cryptid items.
- **Provenance:** locators lacking row quotes on the yōkai, medieval, cryptid and Pazuzu clauses.
- **Duplicate authority:** the bank conflicts with `animal-symbolism.md:109`, and the lesson routes that conflict the wrong way.

## Sources re-opened by ordinary means (12)

S343, S354 (plus the SURG About page and article page), S286, S352 (live page challenge met, not passed; Wayback used), S355, S295, S304 (Wayback), S338 (Wayback), S289, S353, S351 (Wayback), S357. No headless browser was used and no access control was routed around.

## Unrun checks

- S356: Cohen PDF not re-opened.
- S287: Perseus Cicero page not fetched directly; the 1.93 wording was seen only as Lewis and Short quote it.
- I did not run `tools/check-gate-quotes.py` or `accept-c.py` against the proposed replacement text.
- I did not check whether claim O's checker flags the bare "(S304)" with no locator.
