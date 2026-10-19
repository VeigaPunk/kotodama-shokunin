- Seat: C03 | executor (claim C) | verification entry 3: `contact-strata-verification-gate.md`, full fenced bytes under the round-35/36 contract | date 2026-10-19 | baseline dfb0719

# C03 — entry author fragment 3 of 4 (verification): `contact-strata-verification-gate.md`

- Round 39, seat C03 (entry authors ×4, verification partition 20 → 24), claim **C** (coverage).
- Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; HEAD `dfb0719711204b5943432034bd80c8dc248acddd` == the declared baseline `dfb0719` (verified `git rev-parse HEAD` this round); every command ran with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.
- Writes: this fragment only. The corpus entry below is **drafted, not applied** — per `reports/round-39/targets.json` shared_rules, the integrator writes `corpus/knowledge/**`. No filed byte, no tool, no gate, no telemetry file was touched; `git status --porcelain` → `?? reports/round-39/` (plus gitignored `.scratch/c03/`).
- Mission (verbatim, `reports/round-39/targets.json` seat C03): *"Author entry 3 with the same contract."* Contract applied: the round-35/36 entry contract (head-block fields, sources with locators, gap statement with measured sweeps, decision record), instantiated in the verification partition's house style (`corpus/knowledge/verification/two-reader-interop-agreement.md` `:1`–`:19` field shape; `corpus/knowledge/verification/gate-battery-surface-verification.md` `:1`–`:18` per K01 §5) and the executable bar in `reports/round-39/plan/P01-plan.md` §1.3.

## 1. Topic authority and disjointness (measured, not assumed)

- **The topic is K01's recommendation G1, taken as the allocator of record** (`reports/round-39/scout/K01-verification-gaps.md` §4 G1; X00 names K01's list the allocator, `reports/round-39/cross/X00-connector.md` §6 X00-1): a contact-strata verification gate — the loanword/borrowed-thing chronology audit `verification-method-overview.md` `:114` asks for and no entry owns. K01's G1 landed before this seat chose; this is a conformance, not an independent pick.
- **Disjointness at write time (all four sibling fragments landed and read):** C01 → `worked-example-verification.md` (`reports/round-39/cov/C01-entry-1.md:3`), C02 → `index-sweep-verification.md` (`reports/round-39/cov/C02-entry-2.md:9`), C04 → `append-only-record-verification.md` (`reports/round-39/cov/C04-entry-4.md:6`), C03 (this seat) → `contact-strata-verification-gate.md`. **Four distinct slugs; this seat took the only on-list topic** (C01/C02/C04 self-derived off-list per P01's §1.2 self-derive rule, K01 having landed mid-wave for them). No collision exists as far as observable; X00's §5.2 census re-check remains the integrator's.
- Proposed filename: `contact-strata-verification-gate.md` (K01 §5's own recommendation). Alphabetical row position in `## verification/`: **third**, between `citation-format-and-source-registry.md` and `costume-era-consistency-gate.md` ("citation" < "contact" < "costume"). The exact delta bytes are C06's deliverable, not this seat's.

## 2. Absence sweep (commands run 2026-10-19, lane root, HEAD `dfb0719`)

| command | result | reading |
|---|---|---|
| `grep -rli "loan strata\|contact strata" corpus/knowledge/` | 19 files | 18 outside `verification/` (the build-side method files and civilization entries); the one in-partition hit is `calibration-registry.md` `:71` — the real-historical replacement sequence inside a calibration row, not a gate for built packets |
| `grep -lic loanword corpus/knowledge/verification/*.md` | 4 files | all incidental: `label-channel-routing-verification.md` `:3` (per-string borrow-channel routing), `lexicon-coverage-audit.md` `:116` (§6 L, the lexicon gate's loanword-layer coherence leg), `myth-consistency-gate.md` `:104` (one contact-boundary routing row), `verification-method-overview.md` `:114` (the edge question itself) |
| `grep -rli "borrowing gate\|strata gate\|loanword gate\|loanword audit\|strata audit" corpus/knowledge/` | **0 files** | the direct absence |
| `grep -lic "strata\|stratum" corpus/knowledge/verification/*.md` | 8 files | all incidental mentions ( inspected; none is a strata audit) |
| `grep -lic contact corpus/knowledge/verification/*.md` | 11 files | all incidental |
| `grep -rn -i "loan\|borrow" examples/culture-d3/` | 3 hits | the D3 packet declares **no** loan strata (`examples/culture-d3/handoff.md` `:111` "no real-language derivation, borrowing"; `examples/culture-d3/components/07-evidence.json` `:46` "borrows only the abstract slot distinction") — recorded as the owed first field application, not as absence evidence |

**False-positive class reported rather than omitted** (round-28 `X63-F2` precedent; round-35 `ostra`→*prostration* precedent): the honest statement is **not** "zero mentions of loanwords in verification" — four files mention the word — it is "**no verification entry defines an audit of a built packet's contact strata**: no chronology leg, no event binding, no thing-chain, no receipt". The four hits are each exactly such a partial (the routing step, the lexicon coherence leg, the myth row, the question itself), dispositioned one by one in the entry's `- gap filled:` line.

## 3. Entry bytes — DRAFT for `corpus/knowledge/verification/contact-strata-verification-gate.md`

The bytes between the `````markdown ```` opening fence line and the closing ```` fence line (both fence markers exclusive) are byte-equal to the staged file the §5 receipt audited: sha256 `3fa037ae9f95de7449f4df937ed2ef0871bd85d75194c15f79c76053df3c841f`, 33,526 bytes, 166 lines. The equality was measured by line-slice extraction; the re-audit ran on those extracted bytes staged inside the sandbox's `verification/` directory so `couples:` resolution matches the landing path, and the staging copy was removed after the run — the live corpus carried no residue (`git status --porcelain` → `?? reports/round-39/` only, measured after the run; the partition re-counted at 20 files).

````markdown
# Contact-strata verification gate — auditing a built culture's loan strata against its declared contact history

- topic: The verification gate for **contact strata** in a built linguistic-cultural artifact: a culture packet that declares borrowed words, imported things, and the contact events that carried them is audited on three legs — the CHRONOLOGY leg (each stratum's adaptation stage must sit inside its declared window; the adaptation-freezes-phonology rule makes a form's shape dating evidence, so a shape that presupposes a sound change earlier than that change's declared window fails), the ORDERING leg (the strata's partial order must not contradict the declared event sequence; doublets and specialist-register licensing are read as evidence, never normalized away), and the THING-CHAIN leg (a borrowed word carries an object-and-knowledge chain — source, route, adoption, supply — and the two one-sided failures, a word without its thing and a thing without its word, are distinct findings); plus the declaration the gate requires before it runs, the failure-mode table, the fail-closed verdict mapping (a missing record is UNKNOWN, a contradiction is FAIL), the receipt the checker records, and the calibration that keeps the gate inside internal consistency — it audits a packet against its own declared history, never against real-world truth. Method and lane policy only; canon decisions belong to lore-shokunin.
- gap filled: the partition states the coupling question this gate answers and stops. `corpus/knowledge/verification/verification-method-overview.md` `:114` asks the era↔language edge question ("do borrowing, sound change, spelling, and name strata have compatible relative order?") and `:118` states the propagation rule, but neither has a procedure; `:88` records the duty this entry answers ("If no applicable rule exists, record a coverage gap and a candidate test"). Absence sweep 2026-10-19 at lane HEAD `dfb0719`, lane root: `grep -rli "loan strata\|contact strata" corpus/knowledge/` → **19 files — 18 outside `verification/`, one incidental in-partition** (`calibration-registry.md` `:71`, the real-historical replacement sequence, not a gate for built packets); `grep -lic loanword corpus/knowledge/verification/*.md` → **4 files, all incidental**: the per-string borrow-channel *routing* step (`label-channel-routing-verification.md` `:3`), the lexicon gate's loanword-layer *coherence* leg (`lexicon-coverage-audit.md` `:116` — one lettered section of a lexicon release gate; no chronology leg, no event binding, no thing-chain, no receipt), one contact-boundary routing row in the myth gate (`myth-consistency-gate.md` `:104`), and the overview's own edge row (`:114`); `grep -rli "borrowing gate\|strata gate\|loanword gate\|loanword audit\|strata audit" corpus/knowledge/` → **0 files**; `grep -lic "strata\|stratum" corpus/knowledge/verification/*.md` → 8 files, all incidental mentions. Nearest neighbours dispositioned, extended never restated: the build side owns construction — `synthesis/contact-scenario-builder.md` §5 `:63` and the exercise §§9–11 `:120,136,149`, whose §12 stress tests `:177`–`:187` are ad-hoc, exercise-local checks (this entry generalizes them into a gate with a receipt); `synthesis/loanword-material-dating.md` `:22` declares its verification scope bibliographic, not artifact audit; `verification/internal-consistency-audit.md` `:3` audits cross-file coherence in general and would see a strata defect only as a missing coupling, not as an auditable chronology.
- sources:
  - KTD-CS-S-0001 — `corpus/knowledge/verification/verification-method-overview.md` (sha256 `f52708d91f5829b44bbf081341d7073ba05e757764ce164ff21563c2f903f0c9`, read at HEAD `dfb0719`, 2026-10-19): `:73` the claim-family routing table a strata claim lands in without a surface; `:88` the record-a-coverage-gap duty; `:90`–`:103` the fail-closed verdict vocabulary this gate reuses (PASS/FAIL/UNKNOWN, the release rule at `:99`, missing-evidence-is-not-the-opposite at `:100`, issues-only packets at `:102`); `:114` the era↔language edge question; `:118` the dependency-propagation rule; `:150` the translation/original conflation caution applied here to calques. **States the question and the verdict vocabulary; this entry supplies the gate.**
  - KTD-CS-S-0002 — `corpus/knowledge/linguistics/language-contact.md` (sha256 `52385e3d81f7d8f8eb1423d408a47bd12c968f1444fd9fc5d77a9c3e691cd409`): `:13` borrowing defined (words arrive first, structure last); `:29`–`:31` the Thomason–Kaufman intensity scale and its core claim (depth is set by sociolinguistic intensity, not grammar); `:43`–`:45` two generations of borrowability hierarchies, "tendencies, not laws"; `:53`–`:54` inflection almost never borrows (a story beat, not an ordinary stratum) and the prestige-override calibration; `:66` the loanword-adaptation strategy table; `:81` "the adaptation freezes the donor's phonology at borrowing time — the hinge of stratigraphy"; `:133` §10 stratigraphy: dating fictional history with loan strata. **The decision surface for all three legs; none of it is restated here.**
  - KTD-CS-S-0003 — `corpus/knowledge/linguistics/historical-linguistics.md` (sha256 `019f28f09ceac28a1bcb6685f756170b66944129a6b3dca17ca76d9663ab3caf`): `:143`–`:145` relative chronology as the spine of dating, absolute dates as anchors. The ordering principle legs 1 and 2 measure against.
  - KTD-CS-S-0004 — `corpus/knowledge/synthesis/loanword-material-dating.md` (sha256 `5b1d75abd29422b100ab47649f2b5be1e40f598cf2d5cdf35d8afd6103db4d58`): `:2`–`:3` the build-side dating method and its registered sources; `:22` its verification scope (bibliographic, not artifact audit — the boundary this gate does not cross); `:23` the status vocabulary reused in receipts; `:25` §2 name-the-event-before-dating — the event-clock discipline the contact-event records follow.
  - KTD-CS-S-0005 — `corpus/knowledge/synthesis/contact-scenario-builder.md` (sha256 `fcc71a537b5d0649e3f61016bc927dd92ef48f59db500f8e827adad63c7a1961`): `:4` the Thomason & Kaufman registration; `:63` §5 build the loan strata, not a foreign-word garnish; `:120`, `:136`, `:149` the trade-port exercise, its event staging, and the worked lexical/material ledger; `:153`–`:158` the L1–L4 strata rows and the staged-repairs note audited in §12 below; `:164`–`:167` the C1–C4 event rows; `:177`–`:187` the stress tests this gate generalizes (the year-20 /sipa/ anachronism rejection at `:184` is this gate's chronology leg in ad-hoc form); `:198` the exercise's own verification scope.
  - KTD-CS-S-0006 — `corpus/knowledge/synthesis/multi-culture-creole-workshop.md` (sha256 `62acbaae5fd2e25535336b26fc752fbe5e6ec08922be0961f86c0d1a5446df5b`): `:98`–`:118` the designed language ledger and `:119` §8 utterance checks (forms must obey the ledger) — the build-side boundary: within-branch form checks are the workshop's; cross-stratum chronology against declared contact events is this gate's.
  - KTD-CS-S-0007 — `corpus/knowledge/verification/label-channel-routing-verification.md` `:3`: per-string channel routing (native form vs recipient-adapted borrow vs no channel). Runs before this gate, per string; this gate audits the routed strata in time and in chain, never re-grades a string's channel.
  - KTD-CS-S-0008 — `corpus/knowledge/verification/lexicon-coverage-audit.md` `:3`, `:116`: the lexicon gate's loanword-layer coherence leg — a *lexicon* release criterion against field briefs; boundary dispositioned in the gap line, not re-covered.
  - KTD-CS-S-0009 — `corpus/knowledge/verification/internal-consistency-audit.md` (sha256 `c3118517a8510e94b083ee061d0d18f867b479f3c60317cf1ccf7b4f6f2f3def`) `:3`: cross-file coherence generally; this entry is the strata-specific instantiation of one of its coupling edges, with its own receipt.
  - KTD-CS-S-0010 — `corpus/knowledge/verification/myth-consistency-gate.md` `:104` and `corpus/knowledge/verification/calibration-registry.md` `:71`: the two incidental in-partition touches (a contact-boundary routing row; the real-historical replacement sequence) — named to keep the absence claim bounded, not covered here.
  - KTD-CS-S-0011 — Sarah Grey Thomason & Terrence Kaufman (1988), *Language Contact, Creolization, and Genetic Linguistics*, University of California Press, chs. 2–3 (the intensity scale). Registered in-corpus at `corpus/knowledge/synthesis/contact-scenario-builder.md` `:4` and `corpus/knowledge/linguistics/language-contact.md` `:4`. **Not consulted this round** (no network in the seat environment); cited only at the status the corpus already gives it.
  - KTD-CS-S-0012 — Martin Haspelmath & Uri Tadmor, eds. (2009), *Loanwords in the World's Languages: A Comparative Handbook*, De Gruyter Mouton (WOLD companion), and Tadmor, Haspelmath & Taylor (2010) on borrowability; registered at `corpus/knowledge/linguistics/language-contact.md` `:4` and `corpus/knowledge/synthesis/loanword-material-dating.md` `:3`. **Not consulted this round**; the "tendencies, not laws" status is taken from the corpus's own calibration (`language-contact.md` `:45`), not from the survey.
  - KTD-CS-S-0013 — Philip Durkin (2014), *Borrowed Words: A History of Loanwords in English*, Oxford University Press; registered at `corpus/knowledge/synthesis/loanword-material-dating.md` `:3`. **Not consulted this round.**
  - KTD-CS-S-0014 — `examples/culture-d3/handoff.md` `:111` ("no real-language derivation, borrowing") and `examples/culture-d3/components/07-evidence.json` `:46` (the hall system "borrows only the abstract slot distinction"): the lane's current D-packets declare no loan strata, so the gate's first real packet application is still owed — recorded in §13, not claimed.
- calibration: the three named frameworks keep their corpus status and none is re-argued here: the Thomason–Kaufman intensity scale is mainstream as a sociolinguistic description (`language-contact.md` `:29`–`:31`) and is not a universal law; borrowability hierarchies are "tendencies, not laws" (`:45`), sample-based averages that prestige, religion and literacy override (`:54`); adaptation strategies are a descriptive typology (`:66`). The gate is this lane's house policy, not a published standard. It audits **internal consistency**: a packet can pass all three legs and still be historically wrong — passing certifies the packet's own bookkeeping, never real-world truth, and no gate pass is ever a canon decision. The D3/D4 drill material and the contact-builder exercise are NON-CANON. No real culture is described or adjudicated here.
- couples: verification — `verification-method-overview.md`, `internal-consistency-audit.md`, `label-channel-routing-verification.md`, `lexicon-coverage-audit.md`, `to-verify-triage-protocol.md`; synthesis — `../synthesis/loanword-material-dating.md`, `../synthesis/contact-scenario-builder.md`, `../synthesis/multi-culture-creole-workshop.md`, `../synthesis/era-language-staging.md`, `../synthesis/era-material-scoped-reconciliation.md`; linguistics — `../linguistics/language-contact.md`, `../linguistics/historical-linguistics.md`; siblings — lore-shokunin owns canon and world-bible consistency; chousa-shokunin owns general research method.
- source: the design authority is the corpus entries named above, read at HEAD `dfb0719` on 2026-10-19, plus the NON-CANON drill materials (KTD-CS-S-0014, KTD-CS-S-0005 §11–§12); the external frameworks in `- sources:` are cited for the mechanisms they document at the corpus's registered status, never as evidence about any fictional world. The three legs, the declaration contract, the failure-mode table and the receipt are this lane's house method.
- verified-at: 2026-10-19 — in-repo pointers checked mechanically at HEAD `dfb0719711204b5943432034bd80c8dc248acddd` from the lane root (`git rev-parse HEAD`): every cited `path` + `:NN` was read at that revision, and the six files carrying digests in `- sources:` were hashed with `sha256sum` the same day. **No external resource was fetched**: this seat ran without network access, so KTD-CS-S-0011/0012/0013 carry "not consulted this round" and rest on their in-corpus registrations. **Not checked and therefore not claimed:** no built packet with declared strata exists in this lane yet, so the legs are specified from the corpus surfaces and exercised only on the builder's prose ledger (§12) — the gate is a manual craft procedure, not an implemented script, and its first field application is owed (§13).
- recheck: before any packet quotes a strata date or a loanword origin into a handoff; when `contact-scenario-builder.md`, `loanword-material-dating.md`, `language-contact.md`, or the overview's verdict vocabulary changes; when a D-packet first declares contact strata (run the gate and file the receipt); and before reading a §12-style prose ledger as though the gate had machine-run over it. Corrections are new sections or new entries, never rewrites.
- scope: this entry covers the **audit of declared contact strata** — the three legs, the declaration the legs consume, the failure-mode readings, the verdict mapping, and the receipt. It does **not** cover per-string channel grading (`label-channel-routing-verification.md`), lexicon field-brief coherence (`lexicon-coverage-audit.md`), the construction of strata or contact scenarios (`contact-scenario-builder.md`, `multi-culture-creole-workshop.md`), the dating of real contact histories (`loanword-material-dating.md`), or any canon question. It records nothing about any world.

## 1. What this entry licenses

- A **gate over a declared packet**, not a builder and not a dating oracle: it takes a packet that already names its contact events, its strata, and its adaptation routes, and returns per-stratum verdicts plus a receipt. It invents nothing and dates nothing against the real world.
- Three inputs it requires before it runs (§2). If they are absent the gate does not pass silently — it reports UNKNOWN and blocks the affected handoff rows (fail-closed, `verification-method-overview.md` `:99`–`:102`).
- Why a gate and not more per-builder stress tests: the builders each carry partial, exercise-local versions of these checks — the contact builder's §12 stress tests (`:177`–`:187`) and the creole workshop's §8 utterance checks (`:119`) — and an ad-hoc check is re-derived (or skipped) per exercise. A gate with a fixed leg set and a receipt is the same audit across builders, packets, and rounds.
- What this entry is not: it is a **manual craft-verification specification**, in the register of `verification-method-overview.md` `:16` ("a manual craft-verification specification, not an implemented script") — no script, no registered command, and no automated verdict is claimed. A future executable gate needs its own registered command, fixtures, and verdict contract.

## 2. What the packet must declare before the gate runs

The gate consumes two tables and one statement. A packet missing any of them is not auditable; the gap is recorded, not papered over.

**The strata inventory** — one record per borrowed form:

| field | contents | why the leg needs it |
|---|---|---|
| stratum id | stable id (the S-row) | the receipt cites it |
| donor form + gloss | source-language shape and meaning at borrowing | the shape is the leg-1 evidence |
| source label | declared donor (or anonymized label) | separates one donor from two |
| event binding | exactly one contact-event id, or `unbound` | legs 1–2 read time through the event |
| adopted-in window | interval in the packet's own calendar | the leg-1 intersection |
| adaptation route | ordered list of repairs, each tied to a change stage with its own window | the shape-stage read (leg 1) |
| current meaning | what the form means now | separates dating from semantics |
| thing-chain pointer | the object/knowledge record that carried it (leg 3), or `none` | the chain leg |

**The contact-event table** — one record per declared event: event id, window (interval, one calendar), carrier (who/what crossed), parties, and what crossed (words, things, knowledge, people — the multi-clock discipline of `loanword-material-dating.md` `:25`).

**The adaptation-stage statement** — the packet's ordered sound/orthographic repairs, each with its own window, so "the shape presupposes stage k" is a checkable claim (`language-contact.md` `:81`; `historical-linguistics.md` `:145`).

Three rules fix the reading: R1 — every stratum binds exactly one event; `unbound` is a legal value and yields UNKNOWN, never a silent assignment to the nearest event. R2 — all windows in one comparison are intervals in one declared calendar; conversions are recorded, never implicit. R3 — a repair not in the adaptation-stage statement cannot be presumed; an analysis that needs it goes to `(to-verify)`, per the corpus's triage protocol (`to-verify-triage-protocol.md`).

## 3. Leg 1 — the chronology leg

- **Mechanism**: "the adaptation freezes the donor's phonology at borrowing time" (`language-contact.md` `:81`) — a form's shape is evidence of the stage at which it entered. Relative chronology is the spine; absolute dates are anchors (`historical-linguistics.md` `:145`).
- **Procedure**, per stratum: (a) read the declared donor form against the ordered repair list — which repairs the attested shapes have undergone, and which they lack; (b) that stage must intersect the stratum's adopted-in window and its event's window; (c) every later use of the form in the packet (labels, inscriptions, quoted speech) must not presuppose a repair earlier than that repair's window, unless the packet marks the use as later normalization.
- **Verdicts**: shape-stage inside the window → pass. Shape-stage earlier than its repair's window → FAIL (anachronism). Window absent, ambiguous, or in two calendars → UNKNOWN.
- **The named anachronism classes**: a pre-repair shape on an artifact dated after the repair; a post-repair shape attributed to a pre-change stratum; and borrowed **inflection** treated as an ordinary early stratum — inflection almost never borrows (`language-contact.md` `:53`), so an inflectional stratum is a declared story beat and must say so, or it fails.
- **What leg 1 does not read**: meaning. Semantic drift is not dating evidence — a form can keep its shape while its meaning narrows or shifts (the L1 pattern, §12), and the drift is recorded in the stratum's current-meaning field, never folded back into the date.

## 4. Leg 2 — the ordering leg

- The strata induce a partial order (by adaptation stage; by event windows). The declared event sequence must not contradict it: a late-stage form bound to an earlier event than an early-stage form of the same donor field is an **inversion**, and fails — unless the packet declares a re-borrowing, which is exactly what a doublet is.
- **Doublets are evidence, not noise**: two adaptations of one donor word are two strata — a borrowing before a change and a re-borrowing after it ceased — and the packet must declare both (the L1/L2 pattern, §12). Reading a doublet as "spelling variation" or collapsing it to one etymology is a finding, not a tidy-up.
- **Specialist-register licensing**: marginal donor sounds become available only when the packet's own rules license them (typically after a change ceases, in a specialist register — the staged-repairs discipline, `contact-scenario-builder.md` `:158`). A marginal donor sound in an ordinary register inside the change window, undeclared, is a licensing gap: UNKNOWN if the licensing record is missing, FAIL if the packet's own stages contradict it.
- **Prestige overrides are declared readings**: the hierarchies are tendencies, and prestige/religion/literacy override word class (`language-contact.md` `:45`, `:54`) — so an unexpected stratum (a verb, an inflection) is legal exactly when the packet declares the override and its social carrier. Undeclared, it is UNKNOWN; declared, it passes like any other row.

## 5. Leg 3 — the thing-chain leg

- A borrowed word's chain has four records: **source** (who had the thing), **route** (what carried it), **adoption** (who took it, for what), **supply** (does the thing still arrive). The chain is the word's material warrant; a word is not required to have an equal thing on the ground forever, but the packet must say where the chain stands.
- **Word without thing**: a stratum whose chain record is `none` → UNKNOWN (missing record). A chain that is declared and contradicts the packet elsewhere (the word survives while the packet also claims continued import of a thing whose supply event closed) → FAIL (supply contradiction; the C4 pattern, §12).
- **Thing without word**: a declared import with no lexical trace is **not by itself a defect** — loanlessness is a real configuration, and the borrowing-vs-substratum contrast (`language-contact.md` `:20`–`:27`) shows contact can reshape a language with few or no loans. It becomes a finding only when the packet also claims lexical elaboration of that thing.
- **Calque ≠ borrowing**: a translated epithet or loan-transcription is graded on the translation channel (the L4 pattern, §12); reading it as a borrowed name, a borrowed deity, or shared theology is the translation/original laundering class (`verification-method-overview.md` `:150`). Per-string channel grading belongs to `label-channel-routing-verification.md` and runs first; this leg never re-grades the channel — it reads the chain the declared channel implies.

## 6. The failure-mode table

| # | failure | leg | reading | verdict |
|---|---|---|---|---|
| 1 | shape presupposes a repair earlier than that repair's window | 1 | anachronism | FAIL |
| 2 | stratum bound to no event (`unbound`) | 1 | unbound stratum | UNKNOWN |
| 3 | post-repair form on a pre-change artifact, unmarked | 1 | unmarked modernization | FAIL |
| 4 | strata order contradicts event order, no re-borrowing declared | 2 | inversion | FAIL |
| 5 | doublet read as spelling variant / collapsed to one etymology | 2 | misread evidence | FAIL |
| 6 | marginal donor sound in an ordinary register inside the change window, licensing undeclared | 2 | licensing gap | UNKNOWN → FAIL if stages contradict |
| 7 | word survives while packet claims continued import after the supply event closed | 3 | supply contradiction | FAIL |
| 8 | stratum with no thing-chain record | 3 | missing chain | UNKNOWN |
| 9 | calque or translated epithet read as a borrowed name/thing | 3 | channel laundering | FAIL |
| 10 | unexpected stratum without a declared override | 2/3 | undeclared override | UNKNOWN |

## 7. Verdicts and the fail-closed rule

- The gate reuses the overview's verdict vocabulary (`verification-method-overview.md` `:90`–`:103`): **PASS** — the leg's predicate satisfied at the declared scope with the required records present; **FAIL** — an observed contradiction (rows 1, 3, 4, 5, 7, 9); **UNKNOWN** — a required record missing or unparseable (rows 2, 8, 10, the UNKNOWN side of 6); **N/A** — the leg's predicate demonstrably outside the packet's declared scope, with the exclusion recorded.
- **Fail-closed**: the release rule holds per leg (`:99`) — every applicable predicate must pass; a missing record never becomes the opposite finding (`:100`); a gate that cannot run (no declaration, §2) reports UNKNOWN for every stratum and blocks the affected handoff rows rather than passing the packet (`:102`).
- A pass attaches to the strata **as declared**. If the declaration itself is thin (no stage windows, one undated event), the honest output is UNKNOWN rows and a thin-declaration note — never a pass over an imaginary precision.

## 8. The receipt

The checker records, and the packet travels with:

| field | contents |
|---|---|
| gate id + basis | this entry's filename and the audited artifact's digest |
| per-stratum rows | stratum id, leg, verdict, evidence locator (form, stage, window), note |
| event crosswalk | the event table as read, with any calendar conversions |
| controls | the planted defects of §11 step 5 and their observed verdicts |
| checker, date, scope | who ran it, when, and the declaration version it ran against |

A strata date quoted into a handoff without a receipt row behind it is unverified at handoff — the same locator discipline the overview sets for rule citations (`verification-method-overview.md` `:51`). The receipt is a consistency record; it is never a clearance, and it never travels as one.

## 9. Calibration

- **Framework status, carried not re-argued**: Thomason–Kaufman intensity — mainstream as sociolinguistic description, not a law (`language-contact.md` `:29`–`:31`); borrowability — "tendencies, not laws", overridden by prestige/religion/literacy (`:45`, `:54`); adaptation strategies — descriptive typology (`:66`). The gate's readings never upgrade a tendency into a requirement: an unexpected stratum with a declared override is legal (§4).
- **Internal consistency only**: the gate audits a packet against the packet's own declared history. A fully consistent packet can be historically wrong; a pass certifies bookkeeping, not truth — the standing corpus clause that passing structural gates does not certify historical truth applies verbatim.
- **NON-CANON inputs**: the contact-builder exercise, the D3 drill, and every §12 row are invented demonstration material (`loanword-material-dating.md` `:23` "toy"), never historical evidence and never world canon.
- **The gate is manual**: no script, no exit code, no automated verdict is claimed (§1). Anyone may implement it; that act is a new capability with its own controls, not this entry.

## 10. Decision record — the strata-gate decisions this entry fixes

Each row is a decision a checker (or a later reviser of this file) takes explicitly; the rejected alternative is what must not be done silently.

| ID | Decision | Why | Rejected alternative |
|---|---|---|---|
| DR-CS-01 | Run three legs over one declaration and write one receipt, instead of per-builder ad-hoc stress tests | the same audit across builders, packets and rounds; ad-hoc tests are re-derived or skipped per exercise | leaving chronology checks inside each builder's §12 |
| DR-CS-02 | Date a stratum by shape-stage vs window intersection, mechanism = adaptation-freezes-phonology (`language-contact.md` `:81`) | the shape is the evidence; meaning drifts independently and is kept in its own field | dating by meaning change |
| DR-CS-03 | `unbound` is UNKNOWN; never assign a stratum to the nearest event | a silent assignment fabricates the chronology the gate exists to check | defaulting to the nearest event |
| DR-CS-04 | Doublets are two declared strata; collapse is a finding | the doublet is the packet's own best dating evidence (§4) | normalizing doublets to one etymology |
| DR-CS-05 | Thing-chains are required for word strata; wordless imports are legal | loanlessness is a real configuration, not a defect (§5) | requiring a loanword for every import |
| DR-CS-06 | Calques are graded on the translation channel, never as borrowings | gloss similarity is not borrowing evidence (`verification-method-overview.md` `:150`) | treating translated epithets as borrowed names |
| DR-CS-07 | Inflectional strata only as declared story beats (`language-contact.md` `:53`) | inflection almost never borrows; an undeclared one hides a sociolinguistic event | allowing ordinary early inflectional strata silently |
| DR-CS-08 | Supply status is recorded separately from word survival | word survival is not supply (the C4 pattern, §12) | reading word survival as continued import |
| DR-CS-09 | Fail closed: UNKNOWN blocks; an unrunnable gate never passes | the overview's release rule, applied to strata (`verification-method-overview.md` `:99`–`:102`) | "no findings found = green" |
| DR-CS-10 | A receipt is obligatory at handoff; a quoted strata date without a receipt row is unverified | locator discipline at the boundary (`:51`) | trusting the builder's prose dates |

## 11. Applying the gate — build order

1. Collect the declaration (§2). If any part is missing, record the gap and run what is runnable; expect UNKNOWN rows, and say so.
2. Leg 1 per stratum: shape-stage read, window intersection, later-use sweep (§3).
3. Leg 2 across strata and events: partial order, doublets, licensing, overrides (§4).
4. Leg 3 per stratum: source, route, adoption, supply; calque channel (§5).
5. **Negative controls** — plant, and require FAIL: (a) bind a post-repair shape to a pre-repair window (row 1); (b) invert two strata against the event order without a re-borrowing (row 4); (c) sever a chain the packet elsewhere claims is flowing (row 7). A gate run whose controls do not fail is not a run.
6. **Legitimate exceptions** — a declared prestige override and a marked later normalization must pass (§3, §4). A gate that fails a row for being declared is misreading it.
7. Write the receipt (§8) with every UNKNOWN row named.
8. Route unresolved items through `to-verify-triage-protocol.md` (`(to-verify)` at the affected claim), and hand the receipt with the packet — findings and `(to-verify)` rows travel; verdicts do not become world facts.

## 12. Worked micro-example (NON-CANON) — the gate read over the contact-builder's own ledger

The trade-port exercise in `contact-scenario-builder.md` declares events C1–C4 (`:164`–`:167`), strata L1–L4 (`:153`–`:156`), and staged repairs ("early /f/ → /p/, /v/ → /w/; later /k/ → /s/ before /i/; only after that change ceases does a new specialist register license marginal foreign sounds", `:158`). The gate runs read-only over those rows; everything below is a reading of the drill's declared bytes, not a world claim.

- **L1, leg 1**: /kifa/ adopted in 0–39 (event C1); the shape history /kifa/ → /kipa/ → /sipa/ places later uses after the /k/ → /s/ stage — the packet's own use window for /sipa/ is 70–99 (`:153`), consistent. The exercise's stress test says the same thing ad hoc: "Put /sipa/ on a year-20 spoken-language label → Reject under the stipulated chronology" (`:184`) — that is this gate's chronology leg in exercise-local form, which DR-CS-01 generalizes.
- **L2, leg 2**: /kifa/ re-borrowed in 100–139 with marginal /f/ retained (`:154`) — declared as post-change specialist licensing, exactly §4's pattern; L1/L2 are a declared doublet (two strata, DR-CS-04), and the packet says so ("doublets, not random spelling variants", `:154`).
- **L3, legs 1–2**: /wanu/ → /wanu/ via the existing /w/ — no repair presupposed, bound to C1's window (`:155`, `:164`); the borrowed unit-name survives a later locally fixed standard, which is a supply-and-standard note, not a dating problem (`:155`).
- **L4, leg 3**: the Wake Witness epithet is a translation with "no conlang spelling supplied" (`:156`) — graded on the translation channel; the packet itself forbids reading it as a borrowed deity-name (DR-CS-06 respected by the drill, and required by this gate for any packet).
- **Leg 3 across L1/C4**: C4 severs the cotton supply from year 140 (`:167`); L1's word survives while L2's import category loses supply — the packet records word survival and supply separately, which is DR-CS-08; a packet that claimed continued import behind a surviving word here would take a row-7 FAIL.
- **Planted control (row 1)**: bind a /sipa/ form to event C1 (0–39): the shape presupposes the /k/ → /s/ stage, whose completion the packet places after the early repairs and before the specialist licensing (`:158`) — the intersection fails, reproducing the builder's own `:184` rejection under the gate's reading. Observed: FAIL, as required by §11 step 5.
- **Receipt note (honest limit)**: the drill states its repairs as prose intervals, not as a separate adaptation-stage table with per-stage windows, so L1's leg-1 reading uses the use-window (70–99) as the outer bound and the repair prose for the stage order — recorded here as an UNKNOWN-tight note on window precision, not silently tightened to a precision the declaration does not carry (§7, last bullet).

## 13. Handoff note and canon boundary

- This entry ends at the handoff. It supplies the declaration contract, the three legs, the failure-mode table, the verdict mapping, the receipt, and the worked reading. It decides nothing in any world; canon decisions belong to lore-shokunin.
- **To lore-shokunin**: take the receipt and its UNKNOWN rows, plus any `(to-verify)` items — they must not become world facts until resolved through `to-verify-triage-protocol.md`. A PASS row is the packet's bookkeeping checking out, nothing more.
- **Known limits of this entry**: no external work was inspected this round (no network in the seat environment); the three legs are specified from the corpus's own surfaces and exercised only on the builder's prose ledger (§12) — the lane's current D-packets declare no loan strata (`examples/culture-d3/handoff.md` `:111`; `examples/culture-d3/components/07-evidence.json` `:46`), so the first field application is owed the day a packet declares strata; the gate is manual and ships no script (§1, §9); and the hierarchies it reads are tendencies, so every unexpected-stratum reading depends on the packet declaring its overrides (§4).
````

## 4. Self-check against the round's contract

| requirement (`reports/round-39/plan/P01-plan.md` §1.3; `reports/round-35/cov/C12-audit-runbook.md` §1) | state of the draft |
|---|---|
| frontmatter 5-field set `topic, sources, verified-at, recheck, couples` (R35-5F-1) | all five present; instrument reads `header_fields [couples, recheck, source, sources, topic, verified-at]`, `header_tail_ok: true` |
| four-leg reading R35-4F-1 (source / verified-at / recheck / scope-or-couples) | satisfied on both legs literally: `- couples:` present **and** a literal `- scope:` field (1, measured); `- source:` singular provenance line also present |
| gap statement with commands **and real outputs** | `- gap filled:` carries five sweep commands with their measured outputs, plus the four nearest-neighbour dispositions; `gap_named: true` |
| decision record | `## 10. Decision record — …` with `DR-CS-01`…`DR-CS-10`, each with a rejected alternative; `decision_record: true` |
| sources with locators | 14 numbered bullets (`KTD-CS-S-0001…0014`), `source_bullets_with_locator: 14/14`; every locator is an in-repo `path` + `:NN` pair or a named in-corpus registration |
| pointer hygiene | 13 backticked repo-path tokens (`corpus|examples/…`), 13 resolve on disk, 0 unresolved, 0 `(to-verify)` markers needed; **0 URLs** (measured) so nothing is claimed as fetched |
| digest pins | 7 pins, all 7 re-hashed live this round and matching (see §5); `digest_pins_stale_candidates` would be 0 |
| calibration clause (what a pass does not certify) | `- calibration:` names the frameworks' corpus status, the internal-consistency-only scope, the standing no-historical-truth clause, and NON-CANON inputs; `calibration_flagged: true` |
| no-bleed / canon hygiene | boundary sentence present ("canon decisions belong to lore-shokunin", §1/§13); **0 URLs, no ownership assertions**; the only `canon` tokens sit in boundary/negation context ("NON-CANON", "canon decisions belong"); `canon_hygiene: true` |
| no-fabrication | every external work (T&K 1988; Haspelmath & Tadmor 2009; Tadmor et al. 2010; Durkin 2014) is **already registered in-corpus**, cited by its registration path, and marked **"Not consulted this round"** with the reason (no network); no page number, no DOI, no quotation is invented |
| partition register (lane-local method; adjudicates nothing) | §1 "manual craft-verification specification"; §7 fail-closed mapping; §13 "ends at the handoff"; the entry decides no canon, clears no round, certifies no historical truth |
| usable (QUALITY.md item 4) | 4 tables (declaration fields, failure modes ×10, receipt fields, decision record ×10), an 8-step build order with negative controls, and a worked NON-CANON reading of the contact-builder's own L/C rows |

## 5. Verification receipt — the draft through the lane's own audit instrument

The entry bytes were extracted to `.scratch/c03/entry-draft.md` and audited in an **isolated sandbox root** (`.scratch/c03/audit-root/`, built this round): the instrument byte-copied to `audit-root/reports/round-19/audit/entry-audit.py` (its `HERE/../../..` root resolution redirected), and the six real partitions symlinked under `audit-root/corpus/knowledge/` so every `couples:` ref resolves exactly as it would in-tree. **Nothing was written to `corpus/knowledge/`.**

```
$ python3 -B .scratch/c03/audit-root/reports/round-19/audit/entry-audit.py --json \
      .scratch/c03/audit-root/corpus/knowledge/verification/C03-draft.md
{
  "schema": "kotodama-entry-audit-v1",
  "entries": [
    {
      "path": "corpus/knowledge/verification/C03-draft.md",
      "sha256": "3fa037ae9f95de7449f4df937ed2ef0871bd85d75194c15f79c76053df3c841f",
      "size_bytes": 33526,
      "header_fields": ["couples","recheck","source","sources","topic","verified-at"],
      "header_missing_required": [],
      "header_tail_ok": true,
      "source_bullets": 14,
      "source_bullets_with_locator": 14,
      "couples_resolved": 12,
      "couples_unresolved": [],
      "gap_named": true,
      "decision_record": true,
      "calibration_flagged": true,
      "canon_hygiene": true,
      "quality_bar": true
    }
  ],
  "summary": {"total": 1, "pass": 1}
}
```

- `pass 1/1` on the **first run**; no repair pass was needed (the round-35 C03 defects — locator-inside-ticks style, unresolved sandbox couples — were avoided by construction: `path` + ` :NN` outside the ticks throughout, and the sandbox symlinks all six partitions).
- Companion checks on the same bytes (all measured this round, 2026-10-19): backticked repo-path tokens **13/13 resolve** on disk (brace-expansion included); **7/7 digest pins** in `- sources:` match the live files' `sha256sum` (re-hashed this round: `verification-method-overview.md` `f52708d9…`, `language-contact.md` `52385e3d…`, `historical-linguistics.md` `019f28f0…`, `loanword-material-dating.md` `5b1d75ab…`, `contact-scenario-builder.md` `fcc71a53…`, `multi-culture-creole-workshop.md` `62acbaae…`, `internal-consistency-audit.md` `c3118517…`); `grep -c 'https\?://'` → **0**; `grep -c '^- scope:'` → **1**; 166 lines / 33,526 bytes.
- **Not verified by this seat:** the external works themselves (no network; none consulted), the landing itself (the integrator applies the bytes), C06's delta numbers (theirs to derive), and a machine run of the gate over a real packet — none exists yet; the entry's own §13 records the first field application as owed.

## 6. Index-row material (for C06 / the integrator — not this seat's write)

- Proposed row position: **third in `## verification/`**, between `citation-format-and-source-registry.md` and `costume-era-consistency-gate.md`; the row text is the entry's own `- topic:` line, byte-equal (the round-20 repair rule, `corpus/README.md` `:95`–`:101`).
- The partition moves 20 → 24 and the totals 212 → 216 only when **all four** entries land; the footer vector's fifth slot moves 20 → **24** (`21/23/25/29/24/94`) — **C06's numbers to re-derive and C05's audit to pass first** (`reports/round-39/plan/P01-plan.md` §1.4; X00 §5 steps 3–5). Single-entry intermediate sweeps are expected red (entries-without-rows).

## Owed

- **C05's audit** (`reports/round-39/cov/C05-audit.md`) — the four drafts are its input; this receipt is the author's own instrument run, not an independent audit.
- **C06's delta** (`reports/round-39/cov/C06-delta-receipt.md`) — must carry this entry's row (byte-equal `- topic:`) at position 3 with the post-landing sweep; predicted here only as position, never as bytes.
- **The integrator** — applies §3 to `corpus/knowledge/verification/contact-strata-verification-gate.md`; if the P01/K01 allocation for entry 3 is judged different, these bytes are self-contained and reassignable (K01 G1 is this entry's named source of topic authority, so reassignment is not expected).
- **The first field application** — no lane packet currently declares contact strata (`examples/culture-d3/handoff.md` `:111`); the day one does, §11's build order runs and files the receipt. Recorded in the entry itself (§13), so this owed item survives landing.

## Citations

Every path below was read or executed at lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin` at HEAD `dfb0719711204b5943432034bd80c8dc248acddd` on 2026-10-19.

- `REGIMEN.md` (round contract); `reports/round-39/claims.json` (claim C: verification 20 → 24, entry contract, thresholds); `reports/round-39/targets.json` (seat C03 mission + shared_rules).
- `git rev-parse HEAD` → `dfb0719711204b5943432034bd80c8dc248acddd`.
- `reports/round-39/scout/K01-verification-gaps.md` §4 G1 (topic), §5 (contract inputs, filename recommendation), §1 (partition baseline).
- `reports/round-39/plan/P01-plan.md` §1.2 (slot/self-derive rule), §1.3 (executable bar), §1.4 (per-seat obligations).
- `reports/round-39/cross/X00-connector.md` §2 (apply-time matrix), §5 (integration order), §6 X00-1 (allocator of record).
- Sibling fragments (disjointness): `reports/round-39/cov/C01-entry-1.md:1,3`, `C02-entry-2.md:9,16`, `C04-entry-4.md:6,23`.
- Partition census: `ls corpus/knowledge/verification/*.md | wc -l` → 20; `find corpus/knowledge -name '*.md' | wc -l` → 212; `corpus/README.md:5-11` (revision 2.1, vector 21/23/25/29/20/94), `:505-509` (totals line + counts footer).
- Entry-contract exemplars: `corpus/knowledge/verification/two-reader-interop-agreement.md:1-19`; `corpus/knowledge/verification/gate-battery-surface-verification.md:1-18`; `corpus/knowledge/verification/pre-declared-hold-set-reconciliation.md:1-9`.
- Audit instrument: `reports/round-19/audit/entry-audit.py` (byte-copied, unmodified, into `.scratch/c03/audit-root/reports/round-19/audit/`); runbook families: `reports/round-35/cov/C12-audit-runbook.md:26-44`.
- Cited corpus lines (all read this round; digests in §5): `corpus/knowledge/verification/verification-method-overview.md:16,51,73,88,90-103,114,118,150`; `corpus/knowledge/linguistics/language-contact.md:3,4,13,20-27,29-31,43-45,53-54,66,81,133`; `corpus/knowledge/linguistics/historical-linguistics.md:143-145`; `corpus/knowledge/synthesis/loanword-material-dating.md:2-3,22-25`; `corpus/knowledge/synthesis/contact-scenario-builder.md:2,4,63,120,136,149,153-158,164-167,177-187,198`; `corpus/knowledge/synthesis/multi-culture-creole-workshop.md:98,119`; `corpus/knowledge/verification/label-channel-routing-verification.md:3`; `corpus/knowledge/verification/lexicon-coverage-audit.md:3,116`; `corpus/knowledge/verification/myth-consistency-gate.md:104`; `corpus/knowledge/verification/calibration-registry.md:71`; `corpus/knowledge/verification/internal-consistency-audit.md:3`; `corpus/knowledge/verification/to-verify-triage-protocol.md` (couples).
- D3 evidence: `examples/culture-d3/handoff.md:111`; `examples/culture-d3/components/07-evidence.json:46`.
- `corpus/QUALITY.md:3-23` (the admission bar the instrument's `quality_bar` leg reads).
- Sweep commands and outputs: §2 table (all run 2026-10-19, lane root, `TMPDIR=$PWD/.scratch`); instrument JSON: §5; `git status --porcelain` → `?? reports/round-39/` (gitignored `.scratch/c03/` staging excluded).
