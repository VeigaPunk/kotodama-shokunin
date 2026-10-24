# RevLoreHandoff — round 66, adjacency check on the scent entry's lore handoff

- seat: RevLoreHandoff (independent leaf, no subagent dispatch)
- judged on: adjacency, coverage · milestone r66-v2
- base: `94209e8f80969dbac48d56c5d0e2e623635b8616`; jj working copy `b94c22a4d5b0…`; lane tree read-only
- objects read: `corpus/knowledge/synthesis/worldbible-integration-contract.md` (sha256 `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`), the round-65 model `corpus/knowledge/culture-material/games-play-sport-contests.md` (§13 `:108`, §14 `:122`), the two richer handoff variants `fire-fuel-light.md:168`, `bathing-and-body-hygiene.md:138`, `reports/round-66/claims.json` claim C, `reports/round-66/accept-c.py`, `.ufo/waves/round-66/spec-v2.json` (all 64 items), `lore-shokunin/corpus/README.md`
- review kind: **prose/contract review — no LSP server answers Markdown**, so every check here is textual against cited line numbers; no semantic-server absence is claimed beyond that

## Verdict

**Not certifiable this run — and the instrument set does not protect the property under review.**

`corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` does not exist at review time (`find . -name '*scent*' -not -path './.git/*'` → empty; `ls corpus/knowledge/culture-material/` has 32 entries, none scent). So I cannot pass or fail the actual handoff text. What I *can* establish, and do below, is that **nothing in this wave forces the entry to have a handoff section at all**, that the section is not covered by any of the twelve frozen legs, and that four of the 24 row subjects collide with existing owners. The L1 should treat the template in §"Required handoff text" as a build obligation, not a suggestion.

## Findings

### HIGH-1 — No seat authors the entry, and the design seat's skeleton omits the handoff/adjacent sections

The 64-item spec contains row scouts (16), reject candidates (4), scribes (5: `ScribeEntrySpec`, `ScribeGateRows`, `ScribeLessonDraft`, `ScribeReadmePlan`, `ScribeS776Gate`), counters, reviewers, critics and mutators — **no item writes `scent-perfume-aromatics-codes.md`**. The one design seat asks only for content:

> `ScribeEntrySpec`: "Write … the exact entry skeleton for scent-perfume-aromatics-codes.md (<=16 H2, …), the RESTATE rules bullets must satisfy …, and the corpus/README.md edit recipe" (`.ufo/waves/round-66/spec-v2.json` item 17)

No handoff section, no adjacent-topics section, no required-non-decisions list. Meanwhile `accept-c.py:156` caps the entry at `h2 <= 16`, so a skeleton that spends all 16 H2 on scent classes leaves **zero slots** for the two sections the lane's own norm uses. If the L1 writes the entry straight from that spec, the default outcome is a register with no canon boundary, and every frozen leg still passes.

Norm evidence (32-file culture-material partition, `grep -ciE '^## .*(handoff|hand-off|canon boundary|adjacent|lore)'` per file): 21 entries carry exactly one such H2, the round-65 model carries two (§13, §14), and 10 carry none (textile-technology, sumptuary-law-rank-display, pastoralism, material-culture-inference-method, masks-masquerade, hunting-foraging, headgear, costume-semiotics, cartography, adornment-body-codes). Adjacency was scored **unchanged** in round 65 (`corpus/lessons/round-65-verifier-spotcheck.md:53,84`), so an entry without the sections is not a regression this round — but this round's declared axis for the scent register is adjacency, and the wave produces no adjacency artifact other than the entry itself.

### HIGH-2 — No frozen leg can catch a canon-claiming sentence

`grep -niE 'canon|handoff|hand-off|adjacen|lore|world.bible' reports/round-66/accept-c.py` matches only `FILE`'s docstring, `TOPIC`'s docstring and the `- topic:` handling — **no leg inspects canon wording or the presence of a handoff section**. The twelve legs are FILE/SET/ROWS/ONEID/RESTATE/HOSTS/LINK/APPEND/NOHARM/SWEEP/CAPTURE/TOPIC. `claims.json` is honest about this: claim C's `review_only` lists "lore handoff quality of the entry's handoff section". Consequence: an entry sentence such as "incense smoke carries prayer to the god" or "the culture anoints its dead" passes 12/12 legs and would still be a boundary breach of contract §3 (`:43-44`) and §6 (`:92-100`). This is not a counter defect — it is the exact gap my seat exists to close, and it will close only if the section is written.

### HIGH-3 — Seven of the 24 row subjects are living-tradition / attributed-belief material that §10 and §11 gate

Rows whose scout briefs name inscribed living traditions or contested efficacy: S777 (UNESCO ICH incense craft), S778 (kōdō), S779 (kyphi temple recipe), S784 (Grasse ICH), S785 (copal ritual use), S787 (puja fragrance), S792 (Aztec/Maya flower-scent codes), plus S791 (pomander / plague prophylaxis) and S782 (rosewater distillation, briefed as "Ibn Sina attribution calibration"). Two contract clauses bind the entry's payload, not just its tone:

- `:167` — "Rights, restricted cultural knowledge, or publication permission is unresolved → Operator … Hold restricted material; **a bibliography is not permission**."
- `:178` — "**Do not claim consultation or consent that did not occur**."
- `:43` — "Sacred doctrine is not automatically world-fact"; `:96-97` — an invented-and-accepted proposition and a well-attested-but-not-canonized one are orthogonal; "the temple teaches P" ≠ "P is true".
- `:180`-region (scholarly calibration) — a discredited claim must be named as a claim *with its critique* before export. S791 is the live test: miasma prophylaxis is a discredited mechanism, and the entry may describe it as an **attributed in-world belief**, never as a design fact about disease.

An entry that inserts an ICH-inscribed craft as colour, or that states incense "purifies" as world-fact, breaches the adjacency contract while passing every leg.

### MED-4 — Four rows have an existing owner; each needs an explicit one-way bullet, not a restatement

Measured against the owners' own text:

| Row | Subject | Existing owner (evidence) | Required treatment |
|---|---|---|---|
| S795 | incense clocks / timekeeping by burning | `timekeeping-instruments.md:26` — FIRE family, "incense sticks and seal-stamps (Bedini 1994) … **the consumable is the timekeeper**"; also `:86` survival bias | scent keeps the aromatic material and the burn-rate as a *material* property; resolution, failure modes and the variable-hour decision stay in that entry (§2 FIRE, §8) |
| S798 | alabastron / aryballos as perfume vessels | `vessel-container-lexicon.md:5` (owns the container side and "points there rather than restating it"), `:38` "**cosmetic/perfume** (Greek *alabastron*, *aryballos*; the kohl pot — see `adornment-body-codes.md`)" | one-way to the vessel entry for form/typology; note the owner's own routing to adornment, and claim neither |
| S799 | Edo kōdō games (jushukō/kumiko) | `games-play-sport-contests.md` owns game typology and rules (§§1–9), and its §13 already keeps "a game object in a tomb context as game evidence only" | scent keeps the aromatic discrimination kit; the game form, rules and contest structure stay with games |
| S780 / S796 | frankincense–myrrh trade; souk perfumers | `trade-economy-lexicon.md:5` region (owns measure→money→number ladder; 0 scent hits by design) | cite 0-exchange vocabulary; trade route and price are that entry's, not the scent register's |

Two more that a naive draft will restate: `fire-fuel-light.md:62` — "**what it smells like**" is already a fire-entry section heading (combustion odour belongs there); `ritual-garments.md:137` — sensory signature per garment including scent (wearer/occasion rules stay there).

### MED-5 — Reject-candidate S801 ("cosmetics in the ancient world") is not a free slot: the field is already owned

`adornment-body-codes.md:68` is literally "## 6. Cosmetics and their vocabulary", with kohl/lead-salt chemistry (`:71`), *cerussa*/*fucus* (`:72`), oshiroi/ohaguro/sindoor (`:73`). If S801 is admitted and its row's `used-by` names the **scent** entry, coverage is inflated into an owned field rather than extended. The admit-or-reject decision must cite `adornment-body-codes.md:68-73` as the reason — reject, or route the source to that entry (outside this round's NOHARM window). Same test for S802 (miasma/humoral theory — a belief system, myth-symbol/purity territory and §6 classification) and S804 (incense robes airing — `ritual-garments.md`).

### MED-6 — Contract identity: pending acknowledgement, and a stale digest still on disk

- Current bytes hash `5f4c02bfc4e6…` (measured above). A **stale pin `50c4c2f25a728…` is still in the tree**: `tools/gates/frozen/handoff-packet-check/r9-pre/packet.md:27`, `r18-post/packet.md:27`, `corpus/lessons/round-2-adjacency.md:88`. The digest question was left open (`corpus/lessons/round-15.md:57`), so **do not copy a digest from a fixture**.
- Bilateral read is **still pending**: contract `:15` "Initial bilateral acknowledgement is **pending** until those records exist"; `:209` "Bilateral reading and receipts remain required, not self-attested here". Lore's own tree agrees and is explicit: `lore-shokunin/corpus/README.md:73` "CM-g — intake of kotodama handoff packets | **uncovered** | … `git grep -l 'kotodama-lore-adjacency' -- corpus/knowledge SKILL.md` → exit 1 (**no acknowledgement record**)"; `:79` "lore holds **zero durable-surface acknowledgement records**"; `:94` "lore has no acknowledgement record and **no consumability gate**".
- Therefore the entry's handoff must (a) cite the contract **by path only**, exactly as the round-65 model does (`games…md:124`: `` `corpus/knowledge/synthesis/worldbible-integration-contract.md` ``) — no digest, no revision claim, unless the L1 pins `5f4c02bf`; and (b) never say lore has read, reviewed, accepted or imported anything. Writing "handoff accepted", "lore's receipt", or a `packet_id` would be a false stamp and would also imply envelope conformance (`:49-70`) that no entry-level prose can satisfy (`tools/gates/handoff-packet-check.py` is the packet gate; an entry note is not a packet).

### MED-7 — The handoff must live inside the entry: a separate file breaks two legs

`accept-c.py:287` NOHARM allows only `[ENTRY, GAMES_ENTRY]` under `corpus/knowledge`, and SWEEP (`:298`) asserts registry rows == corpus files with zero topic mismatches. A companion `.ufo`/`corpus` handoff file would trip NOHARM if under `corpus/knowledge`, and would need its own registry row + README index row if it were to survive SWEEP. So: one H2 handoff section + one H2 adjacent section **inside** the entry, inside the 16-H2 / 250-line budget.

### LOW-8 — Claim kind must travel in the payload, not be implied

Contract `:93-100` requires per-statement claim kind, evidence status or `(to-verify)`, workflow state and `Canon standing … otherwise `not canonized``. The scent register's bullets will mix real-world reference (S777–S800 as cited sources), designer interpretation (the fragrance-class groupings) and attributed belief (S779/S785/S787/S791). The handoff must say that the *cited rows* are the evidence boundary (the model's `:112` "Treat each bullet as scoped to its cited source") and that the grouping is designer metadata, not an emic category (`:87` gloss caution, and the etic/emic rule).

### LOW-9 — Reciprocity is out of reach this round (residual, not a defect)

One-way pointing is currently write-only: the scent entry will point at ten owners, and NOHARM forbids editing any of them, so no owner will point back. Record it in the lesson's residual list; do not simulate reciprocity.

## Required handoff text (build obligation for the L1)

Two H2 sections, modelled on the round-65 entry (§13/§14) and the fire entry's four-part shape (`fire-fuel-light.md:168-173`: Recipient / This entry supplies / What stays with lore / Known limits). Minimum content:

**Adjacent (one-way) section** — opening line must be the model's: *"This entry points to the following entries for adjacent scope. The pointing is one-way: they own their topic, and this entry does not restate or extend them."* Then one bullet per owner, each in the model's form "`path` owns X; this entry keeps Y as Z":

1. `culture-material/timekeeping-instruments.md` — FIRE timekeeping incl. incense clocks; S795 stays aromatic-material only.
2. `culture-material/vessel-container-lexicon.md` — container typology; S798 stays a use-context.
3. `culture-material/adornment-body-codes.md` — cosmetics vocabulary (§6); perfume ≠ cosmetic here.
4. `culture-material/games-play-sport-contests.md` — game typology; S799 stays the aromatic kit.
5. `culture-material/fire-fuel-light.md` — fuel, combustion and the smell of burning (§4); no fuel-odour modelling here.
6. `culture-material/ritual-garments.md` — garment sensory signature and wearer rules.
7. `culture-material/sumptuary-law-rank-display.md` — legal enforcement of display; who may wear/carry scent.
8. `culture-material/trade-economy-lexicon.md` — measure/money/exchange vocabulary; S780/S796 routes.
9. `culture-material/material-culture-inference-method.md` — residue/artifact inference ladder (S797/S798/S800).
10. `myth-symbol/plant-symbolism.md` and `myth-symbol/purity-pollution-boundary-systems.md` — resin/wood signs; smoke-as-purifier as belief, not mechanism (`:43`).

**Handoff section** — must contain, checkable as strings:

- recipient `lore-shokunin`, cited as owner of "the world bible and its consistency verification" under `corpus/knowledge/synthesis/worldbible-integration-contract.md`, *path only*; "contested scope goes to the integrator" (model `:124`).
- the model's canon disclaimer verbatim or equivalent: "**it makes no canon decision**" and "**Those are canon choices for lore-shokunin, recorded and verified in the world bible, not here.**"
- an explicit "Decisions this entry deliberately does not make" list, scent-specific — at minimum: (a) whether an offering is aliment, medium or gift, and which powers receive it; (b) whether scent has efficacy against disease or misfortune (S791) — attributed belief or discredited claim, never world-fact; (c) who may wear, carry or burn scent, and the enforcement (sumptuary); (d) whether a rite or game is sacred or secular (S779, S799); (e) dates and era bounds (S783, S794, S800); (f) whether an odour code is descriptive of practice or prescriptive (S788; contract `:44`); (g) botanical/zoological identity, substitution and trade routes (S780, S793, S796); (h) contested attributions, explicitly S782's Ibn Sina distillation attribution.
- an evidence-and-rights paragraph: each bullet scoped to its cited row; `(to-verify)` stays a backlog row, never promoted (fire/bathing handoff norm); the living-tradition rows carry the §11 filter and the `:167` operator route; **no consultation or consent is claimed**; the register is not permission to fictionalize an inscribed practice.
- a status line: this is a **draft handoff, bilateral read pending, no receipt**; nothing here is `canonized`. Do not name a packet, envelope or receipt.

## Verification recipe for the landed draft (run once, before commit)

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
E=corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md
grep -nE '^## .*(Handoff|handoff|Adjacent|adjacent|Canon boundary)' "$E"            # expect 2 sections
grep -c 'one-way' "$E"                                                              # expect >=1
grep -n 'worldbible-integration-contract' "$E"                                      # path, not a digest
grep -nE 'makes no canon decision|no canon decision' "$E"                            # expect 1
grep -niE 'canon(ized|ised)|accepted by lore|receipt|bilateral (read )?(done|complete|acknowledged)|has read|approved by lore' "$E"   # expect 0
grep -niE 'miasma|plague|prophyla|disinfect' "$E"                                    # each hit must be belief-classified
grep -nE 'S79[15]|S79[89]' "$E"                                                      # S795/S798/S799 bullets must defer to owner
grep -n 'consultation|consent|UNESCO|inscribed' "$E"                                 # rights filter present, no consent claim
python3 -B reports/round-66/accept-c.py --root .                                     # 12 legs, unaffected by prose
```

**Recipe calibrated on the accepted model** (`games-play-sport-contests.md` as the known-good input): sections=2, `one-way`=1, contract path at `:124`, "makes no canon decision"=1, false-stamp regex=**0 hits**. The recipe therefore discriminates on the property it claims to test and does not fire on the round-65 entry that the verifier already accepted (`round-65-verifier-spotcheck.md:84`, adjacency unchanged).

## Residual risk and verification gaps

- **Unverified (primary gap):** the handoff text itself. It does not exist; this report specifies what must be true, and gives the grep set that decides it. A later reader must re-run the recipe on the landed bytes — my PASS/FAIL on prose is impossible until then.
- **Axes honesty:** adjacency cannot be claimed as an improvement this round unless the entry lands both sections; the wave's other artifacts (rows, counters, separability) move coverage/operability only. Round-65 precedent scored adjacency unchanged (`round-65-verifier-spotcheck.md:84`) — do not let the L1 write "adjacency improved" off the row count.
- **Owner collisions are recorded, not resolved:** S795/S798/S799/S780/S796 remain dual-topic until the owner entries point back; NOHARM forbids touching them this round.
- **Digest split is pre-existing, not introduced here:** `5f4c02bf` (live bytes, examples, lore) vs `50c4c2f2` (frozen r9/r18 fixtures, round-2 lesson). Nothing in this round should re-pin any digest; if the L1 does, it must be `5f4c02bf`.
- **Not in my scope, flagged for the L1:** claim C's `RESTATE`/`ONEID` mechanics (`RevEntryDraft`, `MutEntry`), the rights/allowability of individual sources (`RevSourceSupport`), and whether S776's `used-by` should also name the scent entry (`ScribeS776Gate`).

## Tooling

No install or upgrade performed; no pacman transaction attempted (host-wide pause respected). Read-only review, `git` reads only, lane jj/Git index untouched.

---

# Delta — re-review after `stage/entry-spec.md` landed (08:36) and ScoutReject01's S801 verdict

`ScribeEntrySpec`'s output `.ufo/waves/round-66/stage/entry-spec.md` (28,757 B) now exists and **resolves HIGH-1 structurally**: it allocates `## 12. Adjacent topics` (`:210`) and `## 13. Handoff to the world bible` (`:232`), 13 H2 of a 16 ceiling, 137 assembled lines of a 250 cap, 24 bullet slots. So the sections are no longer at risk of being omitted — HIGH-1 is **closed** (my first pass ran at 08:29, seven minutes before the spec landed). What remains is the content of those two sections, reviewed below against the contract and the owners' measured text.

### HIGH-A — §12's owner list omits the three entries whose subjects are rows inside this register

Drafted §12 (`entry-spec.md:214-231`) names: bathing, cuisine, sumptuary, trade-economy, funerary, ritual-garments, material-culture-inference, music-instrument. Absent are the owners of three of the 24 rows and two adjacent registers:

| Missing owner | Owns (measured) | Row in this register that lands on it |
|---|---|---|
| `culture-material/timekeeping-instruments.md` | FIRE timekeeping family, "incense sticks and seal-stamps (Bedini 1994) … **the consumable is the timekeeper**" (`:26`), survival bias (`:86`) | **S795** incense clocks |
| `culture-material/vessel-container-lexicon.md` | container typology, incl. "**cosmetic/perfume** (Greek *alabastron*, *aryballos* …)" (`:38`) | **S798** perfume vessels |
| `culture-material/games-play-sport-contests.md` | game typology and rules (§§1–9); §13 already keeps "a game object in a tomb context as game evidence only" | **S799** kōdō games |
| `culture-material/adornment-body-codes.md` | "## 6. Cosmetics and their vocabulary" (`:68`), kohl/*cerussa*/*fucus*/oshiroi (`:71-73`) | S801 (if admitted), S790 scented gloves, S797 anointing |
| `culture-material/fire-fuel-light.md` | "## 4. Light: what burns, **what it smells like**, and who can afford it" (`:62`) | §5 incense smoke, §2 resins as fuel |

Without those bullets the entry writes S795/S798/S799 as if the register owned them, and no frozen leg objects (HIGH-2 stands). The model lists nine owners; ten here is in-norm.

### MED-B — §12 omits the lexicon-field owner while §1 is exactly a field brief

`corpus/knowledge/linguistics/semantic-fields-lexicon-building.md:3` owns "engineering a fictional lexicon by semantic field … field-by-field elaboration briefs". The entry's `## 1. What a smell term names` (`:88`) is such a brief. One bullet: that entry owns field engineering; this entry supplies the scent field's terms only. (The model points at a `linguistics/` sibling too, so the cross-partition edge has precedent.)

### MED-C — §13 is contract-clean but under-specified in four places

Verified present and correct: the model's two disclaimer sentences verbatim (`:234-236`, `:241`) — "makes no canon decision", "contested scope goes to the integrator", "Those are canon choices for lore-shokunin … not here". No false stamp anywhere in the spec (grep for canon-claim wording over the two sections: 0 hits).

Missing, each tied to a clause:

1. **Status line** — contract `:15` "Initial bilateral acknowledgement is **pending**"; `:209` "receipts remain required, not self-attested"; lore's own record: "uncovered … **no acknowledgement record** … **no consumability gate**" (`lore-shokunin/corpus/README.md:73,79,94`). One sentence: no acknowledgement or receipt exists, nothing here is `canonized`.
2. **Rights / no-consultation clause** — `:167` "Hold restricted material; a bibliography is not permission"; `:178` "Do not claim consultation or consent that did not occur". Six of the 24 rows are inscribed living traditions (S777, S778, S784, S785, S787, S792). The existing "sacred or therapeutic" clause answers belief, not permission.
3. **Known-limits bullet** — contract `:174-186` and the fire/bathing handoff norm (`fire-fuel-light.md:173`, `bathing-and-body-hygiene.md:141`). Name the weak row classes: ICH listing pages describe inscriptions, not craft technique; museum object pages describe objects, not use; a 1963 survey quoting Pliny is a compilation, not primary attestation (`:176`). §11 already says "treat each bullet as scoped to its cited source" — §13 should say which classes that costs.
4. **Non-decisions the list misses** — it covers sacred/therapeutic, authoritative rank scent, and compounding. Still absent: whether an odour code is **descriptive or prescriptive** (`:44`); **permission and enforcement** of wearing/carrying (the current clause names authority, not who may wear — `:44` "permitted wearers, objects, enforcement"); **era bounds and dates** (S783, S794, S800; contract §3 Era row, `:44`-region); **offering mechanics and addressee** (S779, S785, S787 — whether scent is aliment, medium or gift, and which powers receive it, `:43`); **contested attributions**, explicitly S782's Ibn Sina distillation brief ("attribution calibration"). Five clauses, one sentence each, still inside the line budget (137/250 used).

### S801 — ScoutReject01's ADMITTED verdict is mechanically invisible and conditionally acceptable

Measured: `NEW_IDS = [f"S{n}" for n in range(777, 801)]` (`accept-c.py:50`) — SET/ROWS/ONEID/RESTATE/HOSTS/LINK never read S801; APPEND only asserts `missing_old == 0` (`:277`), so any added row passes. The row file itself is well-formed (11 cells, `paper`∈KINDS `:55`, tier B, `mined`, `2026-10-24`, `used-by` = the scent entry, 14-digit capture `20250826123925`, quote present). RESTATE arithmetic on the drafted bullet, run through the counter's own helpers: `in-order-quote-words=4`, `teaches_cov=0.000`, `novel=10` → passes with margin.

Conditions under which I do not object (given to the scout directly): (i) the lesson declares S801 as an **extra row outside the claimed 24** — claim C's wording is "exactly 24 … S777-S800", and the statement's own "701 -> 725+" already contemplates extras; (ii) the entry cites it **exactly once** (no leg checks this — it is an L1 obligation); (iii) the bullet stays on the aromatic-materials/recipe side (incense, nitre, myrrh, frankincense, saffron, the resin seal for aroma retention) and does not carry cosmetics-as-body-code (kohl/lead/*cerussa*), shop institution or prices (adornment `:68-73`, trade-economy); (iv) §12 gains the `adornment-body-codes.md` and `vessel-container-lexicon.md` bullets. If the row is registered but the entry does not cite it, its `used-by` cell is false and nothing catches that — that is the disqualifying case. Also: the drafted bullet says "Pliny records…", but the row's evidence is Matthews 1963 *quoting* Pliny; naming the carrier ("Matthews quotes Pliny's cream of…") costs nothing — in-order quote words stay 4 — and satisfies `:176`'s primary-vs-compilation split.

**Final S801 bullet accepted** (ScoutReject01's revision, re-measured through the counter's helpers): *"Matthews (1963) quotes Pliny's cream of incense, nitre and myrrh — one aromatic recipe inside Rome's luxury cosmetics trade."* → `inq=4, cov=0.037, novel=10`, PASS (unchanged margin vs the draft). "cosmetics trade" is retained deliberately: it mirrors the row's own scope cell ("Roman cosmetics trade: perfumer's craft and priced luxuries"), so bullet and registry cell do not diverge — which makes the §12 `adornment-body-codes.md` bullet **mandatory, not advisory** (§12 currently lacks it, HIGH-A), and the existing `trade-economy-lexicon.md` bullet load-bearing for the "trade" half. Registered-but-uncited remains the disqualifier; no leg will notice either way.

### Updated residual risk

- The two sections are now written at spec level; the **entry bytes still do not exist**, so the recipe in §"Verification recipe" must run on the landed file.
- §12/§13 gaps above are invisible to all twelve legs; they can only be closed in prose before commit.
- Correction to my first pass, recorded for the audit trail: HIGH-1 (no handoff section in the skeleton) was an artifact of reviewing at 08:29; it is closed by `entry-spec.md:210,232`.
