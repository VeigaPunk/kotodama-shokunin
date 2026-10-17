# Review — component 12-rank-rules (culture D2)

- reviewer: round-4 REVIEW worker (round-3 missing review)
- target: `examples/culture-d2/components/12-rank-rules.yml`
- status: **FINDINGS — field-complete, not a clean legality handoff**
- canon: **NON-CANON** design drill; lore-shokunin owns canon decisions
- counts: **6 findings + 3 supporting flags**; 21 rule rows reviewed, plus 4 authority, 3 jurisdiction, 4 enforcement, and 5 sanction rows
- reviewed baseline: round-3 component at commit `c610e0abd8edf90d6c6d86ebebdc7a7cba8d4a0b`, SHA256 `2b88fbf68af0979a4189e97b92e675477b7f5466b31889139b28e49036f946fb`
- required reference: `corpus/knowledge/culture-material/sumptuary-law-rank-display.md`, full 110 lines; SHA256 `f4374402d87e71c55b3a3cb989d40aee7875043cb1bf04374228de3a709bad87`

## Scope and revision boundary

The component and reference were read in windows of at most 120 lines. Supporting checks used `corpus/knowledge/verification/costume-era-consistency-gate.md` §6, the existing costume gate's input contract, `tools/assemble-d2.py`, and `10-materials.yml:grade_ladder/measures` (lines 445–522).

A concurrent worker began revision 1.1 era normalization during review. Findings below identify records and fields rather than unstable line numbers. A read-only comparison with the fully read baseline passed after excluding `era`/`era_history` fields and accounting for one examined wording change: WR-09's `In the era-3 reform,` became `In the E2 reform,`. The compared policy blocks otherwise matched: `degree_slots`, `degree_gender_clause`, `wear_rules`, `speech_rules`, `touch_rules`, `authority`, `jurisdiction`, `enforcement`, `sanctions`, `loopholes`, and `black_market`. This confirms the findings' policy basis, **not** correctness or completion of the concurrent era edits.

- last comparison snapshot SHA256: `28696a5a70404984fbf1a453f66c9e7618e318ebf93f25bce461fdb7dfcd35a3` (a moving worktree snapshot, not a frozen full-component run)
- current policy-payload SHA256 after removing `era`/`era_history`: `66101f54791b97bde865df1df06834a9a53bfcafd23c7bdc058ddadf3d868ca2` (JSON, Unicode preserved, sorted keys, compact separators)
- era references below use the component's declared mapping: old `era-2` → E1, old `era-3` → E2. No founding date or final era-name reconciliation is inferred.

Only this review was written. The component, corpus, assembler, gates, and fixtures were not edited; no commit or LOG.md edit was made under the assignment's single-output write scope.

## Field and honesty checks that pass

All **9 wear + 6 speech + 6 touch = 21 rules** have nonempty `prescription`, `assay`, `authority`, `jurisdiction`, `era`, `enforcement_reality`, `sanction`, and `follows`: **168/168 field cells**, no duplicate rule IDs. This establishes completeness, not coherence or an executable legal verdict.

The institutional design is concrete: winter-moot checks, a mobile tally-warden, guild informers with conflicts of interest, and a fair court using testimony/registers rather than pretending cloth licenses police themselves. Most prescriptions have distinct practice accounts, including summer over-grading, selective prosecution, hidden linings, forged cords, and a dead-letter import ban. These are labeled fictional design, not observations about a real population. The calibration block rejects the rigid class pyramid and distinguishes legal grammar from lived gender order.

Reproducible field count, run from the repo root (existing stdlib subset reader; not a claim of full YAML conformance):

```bash
python3 -B - <<'PY'
from pathlib import Path
from runpy import run_path
p = Path('examples/culture-d2/components/12-rank-rules.yml')
d = run_path('tools/gates/costume-era-consistency-gate.py')['parse_packet'](p.read_text())
fields = ('prescription', 'assay', 'authority', 'jurisdiction', 'era', 'enforcement_reality', 'sanction', 'follows')
rules = [r for k in ('wear_rules', 'speech_rules', 'touch_rules') for r in d[k]]
missing = [(r['id'], f) for r in rules for f in fields if not r.get(f)]
print('wear/speech/touch:', *(len(d[k]) for k in ('wear_rules', 'speech_rules', 'touch_rules')))
print('rules/cells/missing:', len(rules), len(rules) * len(fields), len(missing))
print('authorities/jurisdictions/enforcers/sanctions:', *(len(d[k]) for k in ('authority', 'jurisdiction', 'enforcement', 'sanctions')))
print('rank_rules present:', 'rank_rules' in d)
assert not missing and len({r['id'] for r in rules}) == len(rules)
PY
```

Observed output: `wear/speech/touch: 9 6 6`; `rules/cells/missing: 21 168 0`; `authorities/jurisdictions/enforcers/sanctions: 4 3 4 5`; `rank_rules present: False`. Exit 0.

## Findings

### RR-01 — Import entitlements and retained prohibitions collide

**Prescription collision; exemption/version priority unresolved.** `DEG-6.rights` permits a treaty stranger's own lowland cloth, and WR-07 requires their fair coat; WR-02 says **none but a registered herd-master** may wear lowland-woven cloth. Thus a treaty stranger exercising the stated lowland-cloth entitlement at the fair has no explicit WR-02 exemption. WR-02's practice account then says strangers are prosecuted without distinguishing lawful treaty dress from impersonation under WR-07.

In E2, WR-09 permits any household's lowland cloth at the winter fair, but WR-02 remains an E1-onward ban and `BM-3.legal_floor` still says registered herd-masters only. WR-08's acknowledged dead-letter status describes practice, not repeal or an explicit legal priority. This is not a finding that widespread illegal wearing is impossible: the conflict is between statements of **lawful entitlement**.

- Basis: `sumptuary-law-rank-display.md` §2 (regulated person), §8.2/§8.5 (monopoly/exemption), §10.7 (enforcement mode); `costume-era-consistency-gate.md` §6.1/§6.4 (version and exemptions).
- Candidate repair: expressly preserve/exempt treaty strangers, state which clauses WR-09 supersedes and where/when, and era-scope BM-3's legal floor. Keep the fossil ban and actual violations visible if intended. Do not infer that permission to sell G3 felt also grants permission to wear it.
- Recheck: decide a treaty stranger's own cloth at the E1 fair and an ordinary household's cloth at the E2 winter fair without inventing an exemption.

### RR-02 — Jurisdiction alternates between legal reach and lawful location

**Scope gap, not a missing-field failure.** WR-02 prohibits cloth above the undefined `sell-line`, yet calls the rule `void at transit and high pasture`; this does not tell the reviewer whether upland wearing is illegal but unpoliced, or outside the ban altogether. SR-06 prohibits teaching outside the valley in storm season, but its jurisdiction says `valley, any season except the storm; camps, never`: the field excludes settings where the prohibition appears to operate.

Officer coverage also disagrees: JU-3 lists `wind-speakers only`, while EN-2 counts hems `at the camps` and has circuit-wide reach. WR-01 calls itself the only rule following households everywhere, although WR-03/WR-04/WR-05/WR-08 also name all-band reach.

- Basis: `sumptuary-law-rank-display.md` §2 (inspectorate must match its assay), §10.7; `costume-era-consistency-gate.md` §6.5 (venue and enforcement distinct from applicability).
- Candidate repair: distinguish legal territory/season, permitted acts, and officer presence; define the sell-line and reconcile JU-3 with the warden's itinerary. An intentional jurisdictional gap is acceptable when named as such.
- Recheck: an upland lowland-cloth wearer, a storm-season teacher at a camp, and a summer cord inspection each have a determinate legal scope and available forum/officer.

### RR-03 — A sale's mandatory touch violates the measure-touch rule

**Direct prescription collision in the same fair jurisdiction.** TR-04 says no household may use another's salt-measure, `nor touch the measure rather than the salt`. TR-06 opens a sale when the **seller touches the buyer's measure**. Both operate at the treaty fair from E1, and neither states a ceremonial-touch exception. DEG-6's own-measure entitlement does not authorize the seller's touch.

- Basis: `sumptuary-law-rank-display.md` §2/§10.7 (assay and tribunal); `costume-era-consistency-gate.md` §6.4 and its conflicting-authorities row (resolve exemptions/priority before asserting legality).
- Candidate repair: distinguish ritual touch from use/assay, specify an explicit witnessed-sale exception, or change the sale gesture. Preserve a deliberately contested gesture only by labeling the dispute and competing rulings.
- Recheck: an ordinary household buyer and seller can complete the two-touch sale without an unacknowledged breach or seizure under TR-04.

### RR-04 — Storm duration, overrides, and rescue duty need one reading

**Exception-scope gap.** WR-05 suspends mourning dress on storm law's **first day**, while TR-05 allows any available coat **while storm law holds**. JU-3 says storm law `supersedes all`; this is broader than TR-05's specific permissions and does not identify retained sacred-name or office restrictions. The words `speak plainly ... without rank formula` do not by themselves settle SR-01's storm-name taboo.

TR-05 also prescribes permissions (`may handle`, `take up`, `speak`) but penalizes **failure to lift**. The rescue duty and its relation to storm debt are not actually stated in that prescription. Social feeding-order punishment can be coherent, but should be identified as a customary duty/response rather than silently derived from permission.

- Basis: `sumptuary-law-rank-display.md` §8.5 and §10.7 (occasion exemptions and enforcement mode); `costume-era-consistency-gate.md` §6.1/§6.4/§6.5.
- Candidate repair: enumerate duration and overridden/retained restrictions; state the duty to rescue and who adjudicates refusal, or label it separately as customary practice. Do not assume emergency permission means blanket exemption from every taboo.
- Recheck: a mourning household on day two of a storm, a non-wind-speaker's storm-name utterance, and a refusal to rescue each receive an explicit legal/customary outcome.

### RR-05 — The felt-day assay has an institution but no reproducible mapping

**Assay gap.** WR-01 regulates G1–G3 by felt-days per bale and recomputes a household grade from ascents/bales. EN-3 instead assays by hand and eye. No felt-day-to-grade thresholds, ascent/bale-to-entitlement rule, or coat-to-certified-bale link is supplied in these fields. A recorded work input is not automatically a test of the coat being worn.

The bounded sibling check does not close this: `10-materials.yml:grade_ladder` supplies fiber/finish descriptions for G1–G3, while `measures:ME-02` supplies a felt-day **slot** that refers back to component 12. Those are useful design inputs, not a reproducible numeric conversion. The component's `calibration.design_flags` assertion that felt-days are reconciled should not be read as completing that assay.

- Basis: `sumptuary-law-rank-display.md` §2 craft rules 1–2 and §10.1–§10.2 (measurable surrogate; officer matched to assay).
- Candidate repair: choose whether the legal sign is a certified production record, a fiber/finish proxy, or both; specify the grade/entitlement decision and provenance check, including what cannot be detected. Do not import historical work rates to fill the gap.
- Recheck: given the same coat, bale record, and household ascent record, two inspectors can derive the same grade/entitlement or explicitly return unresolved.

### RR-06 — Some practice accounts are universal design assurances

**Calibration weakness, not a charge of fabricated history.** WR-05 says mourning is `observed hard` and `self-enforcing`; SR-06 is `kept strictly`; TR-05 is `the one rule no one evades`. The latter supplies a refusal sanction, yet no actual departure or adjudication scenario. A separate `enforcement_reality` key is good, but universal compliance language can still turn an ideal into apparent observed practice.

- Basis: `sumptuary-law-rank-display.md` §1/§9 (do not infer success or failure from legal form alone), §10.5 (design the leaks); `costume-era-consistency-gate.md` §6.5 (no enforcement evidence proves neither perfect compliance nor total failure).
- Candidate repair: identify these as deliberately idealized **DESIGN stipulations**, or qualify ordinary compliance and supply an authored exception, disputed account, or enforcement event. Do not invent prosecution statistics or real-world citations. No external evidence is required merely to stipulate fictional behavior honestly.
- Recheck: a reader can distinguish statute, institutional claim, customary norm, and authored practice, including whether `no one` is literal or rhetorical.

## Supporting flags

### RF-01 — Executable rank-rule coverage is explicitly absent

`python3 -B tools/gates/costume-era-consistency-gate.py examples/culture-d2/components/12-rank-rules.yml` returned **exit 2**, ``FINDING G-DATA: [could-not-evaluate] no `costumes` declared: nothing to review``. This is **not CLEAN** and is not an automated confirmation of RR-01–RR-06.

The gate's R checks read optional `rank_rules` records with structured authority, jurisdiction, eras, effect, property, ranks, and exemptions (`tools/gates/costume-era-consistency-gate.py:65–75`). This component has prose `wear_rules`/`speech_rules`/`touch_rules`, not that schema. `tools/assemble-d2.py:134–139` already declares that component 12 is not translated and R-checks are unevaluated. Silent costume/packet output must not clear these findings; any adapter and its scenario fixtures are integrator follow-up, not changes made by this reviewer.

`python3 -B tools/gates/costume-era-consistency-gate.py --selftest` returned **exit 0**, `10/10 checks passed; fixture exit 1 with 21 planted finding IDs`. That verifies the unchanged gate's fixture behavior only. The round-4 full gate battery was not run by this worker.

### RF-02 — Sanction and price schedules remain qualitative

WR-01 gives a hem to the informer; WR-02 gives half a coat's hem-value; TR-03 forfeits a bale and gives half its hem-value; SA-3 gives the garment's whole cut hem. Different offenses may legitimately have different awards, but the summary does not specify their relationship, residual recipient, or valuation. SA-2 says `set weight` without supplying the weight. Most `black_market.price_note` entries are gift/standing/seizure descriptions, not a paired legal/illegal price spread.

Basis: `sumptuary-law-rank-display.md` §6 (splits vary by statute), §10.4/§10.8. Do not flatten the variants into a single moiety or demand coin prices from a barter design. Label the handoff a qualitative incentive map, or supply per-offense awards, valuation units/ranges, and recipients before calling it an executable sanction/price schedule.

### RF-03 — Dependency status mixes delivery-time and current assertions

`depends_on[11-costumes].status` still says the sibling was not on disk at write time and needs verification; `garment_refs_note` and `open_checks` claim successful delivery reconciliation. These may be an honest historical sequence, but they are not clearly separated as past versus current status. Date/archive the old dependency note rather than implying both unresolved and closed states.

LEX-DEG surface forms and pitch-accent requests remain explicit open dependencies; this review does not certify their fulfillment or sibling-era consistency. Their `(to-verify)` markers are design handoff gaps, not newly verified historical claims.

## Disposition and limits

- **Presence:** PASS for the eight checked fields on all 21 rule rows; institutional tables are present and nonempty.
- **Substance:** retain RR-01–RR-06 and RF-01–RF-03. Two prescription collisions, three scope/assay gaps, and one calibration weakness prevent an unqualified clean handoff. These are manual review classifications, not fabricated gate finding IDs.
- **Practice honesty:** substantial positive separation of law from lived departures, with the specific universal-compliance caveat above. A declared breach is not itself a defect, and weak enforcement does not repeal a prohibition.
- **Verification:** field audit exit 0; unchanged costume self-test exit 0; direct component gate exit 2/could-not-evaluate. PyYAML was unavailable (`ModuleNotFoundError`); no dependency was installed, and counts used the repository's documented stdlib subset reader. No full YAML-conformance claim is made.
- **Source boundary:** corpus mechanisms and their internal citations were reviewed; no primary historical editions or new web citations were independently verified. Nothing here upgrades a comparator to verified historical fact or a D2 design to canon.
