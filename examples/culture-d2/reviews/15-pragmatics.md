# Review — component 15-pragmatics (culture D2)

- reviewer: round-4 REVIEW worker (missing round-3 review)
- date: 2026-10-17
- target: `examples/culture-d2/components/15-pragmatics.yml`
- canon: not canonized (D2 design drill); canon decisions remain lore-shokunin's
- verdict: **NOT CLEAN — 8 open manual findings (5 HIGH, 3 MEDIUM).** The three politeness axes are distinguished conceptually, but the honorific implementation and lexicon-backed ladders are not integrated. These are review findings, not invented executable-gate finding IDs.
- scope: this review only; no component, corpus, gate, or log was edited.

## Reviewed evidence

SHA-256 fingerprints of the primary inputs (working-tree bytes, not a claim about a committed revision):

- `components/15-pragmatics.yml`: 509 lines; `48484788bb69808d7d688951e87347107617a4b6572de0215e86d3f09cc323fd`.
- `components/05-lexicon.yml`, final recheck: 849 lines; `9bdcb8d895be0592047260361c4c12493569e7d38318b3508a5bde314d87abdf`.
- `corpus/knowledge/linguistics/politeness-taboo-euphemism.md`: 133 lines; `7fe13a118539dc467d48c99473439b04e268eca9b0e3552139ab8db5b7f22b80`.

The lexicon owner prepended 22 lines of name-only repair support during verification. `git diff -- examples/culture-d2/components/05-lexicon.yml` showed that the 40-record lexicon body was unchanged; the embedded probe and standard gate were re-run successfully. The original 827-line input had SHA-256 `fdd48f4e197dd87081e26e6d2334f3f35f022584dcaf7b8b62756ba1162b3e46`. Lexicon line references below describe that inspected body: add 22 for the final 849-line revision. All ID, form, and ladder measurements remain unchanged.

Here and below, `components/` means `examples/culture-d2/components/`. Sibling records were checked directly, not inferred from their older reviews. Concurrent round-4 edits were observed, so sibling record IDs are the governing pointers; line numbers describe the inspected versions:

- `03-morphosyntax.yml`: M-17, SYN-07..SYN-13, SYN-29 (SYN-29 at line 255 in the 346-line revision).
- `14-kin-address.yml`: PH1..PH3, A01..A04, A08..A12, R01 (436-line file).
- `12-rank-rules.yml`: SR-01..SR-05, JU-1..JU-3 (698-line revision; JU-2 at lines 486–492).
- `01-brief.yml`: CP-07/CP-11/CP-12, contract namespaces, RG-03/RG-04.

The unchanged standard command was run from this repo:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 tools/gates/lexicon-coverage-audit.py examples/culture-d2/components/05-lexicon.yml
```

Observed result: **exit 0, no findings printed**. This grades the lexicon's declared design, not inbound references from pragmatics; it does not discharge any finding below. The full round-close battery was not run by this review worker.

## Lexicon-link measurements

A read-only probe used the shipped gate's `load_packet(text)` parser. Observed: 40 lexicon records; 23 distinct lexeme handles anywhere in pragmatics, **0 exact matches** to current lexicon IDs; 32 explicitly qualified citation occurrences naming 15 distinct handles, also **0 exact matches**. All 15 qualified handles have same-number `L-` candidates, but no alias is declared in the reviewed component. The dependency list contains 22 handles and omits the used `L11`.

The six ladder rows were checked individually:

| Ladder row | Delivered `term_id` | Exact resolution |
|---|---|---|
| TB-1 R1 | `pending 05-lexicon delivery` | UNRESOLVED |
| TB-1 R2 | `pending 05-lexicon delivery` | UNRESOLVED |
| TB-1 R3 | `pending 05-lexicon delivery` | UNRESOLVED |
| TB-3 D1 | `05-lexicon:L32 toksa` | UNRESOLVED; candidate `L-32 tolsa` |
| TB-3 D2 | `pending 05-lexicon delivery` | UNRESOLVED |
| TB-3 D3 | `pending 05-lexicon delivery` | UNRESOLVED |

Thus **5 placeholder flags across 6 rows; 0/6 exact links**. D1 has a real same-number lexical candidate; that is not permission to silently alias it. No replacement forms were invented by this reviewer.

Reproduction, from the repo root (prints measurements, not a new gate verdict):

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from pathlib import Path
import hashlib, re, runpy
load = runpy.run_path('tools/gates/lexicon-coverage-audit.py')['load_packet']
p = Path('examples/culture-d2/components/15-pragmatics.yml')
l = Path('examples/culture-d2/components/05-lexicon.yml')
c = Path('corpus/knowledge/linguistics/politeness-taboo-euphemism.md')
for path in (p, l, c):
    raw = path.read_bytes()
    print(path, len(raw.splitlines()), hashlib.sha256(raw).hexdigest())
text = p.read_text()
prag, lex = load(text), load(l.read_text())
ids = {row['id']: row for row in lex['lexicon']}
handles = set(re.findall(r'\bL-?\d{2}\b', text))
qualified = re.findall(r'05-lexicon:(L-?\d{2})', text)
deps = next(d['ids'] for d in prag['deps'] if d['component'] == '05-lexicon')
print('records / handles / exact:', len(ids), len(handles), len(handles & ids.keys()))
print('qualified occurrences / distinct:', len(qualified), len(set(qualified)))
print('dependency handles / used-but-undeclared:', len(deps), sorted(set(qualified) - set(deps)))
for tab in prag['taboo_ladders']:
    for rung in tab.get('live_rungs', []):
        print(tab['id'], rung['rung'], rung['term_id'], 'stage=', rung.get('stage'))
seen = set()
for m in re.finditer(r'\b(L-?\d{2})\s+([^\s;,)"\']+)(?=\s*["\'])', text):
    handle, echo = m.groups()
    candidate = 'L-' + handle.removeprefix('L-').removeprefix('L')
    if candidate in ids and echo != ids[candidate]['term']:
        seen.add((handle, echo, candidate, ids[candidate]['term']))
print('stale quoted forms:', len(seen), sorted(seen))
PY
```

## Open findings

### PG-01 — HIGH — stale lexicon namespace and forms

`15-pragmatics.yml:32–35,142,162,202,214–219,268–273,305` cites `L01`..`L37` handles, whereas `05-lexicon.yml:13,208–758` defines `L-01`..`L-40`. None of the 23 distinct handles resolves literally. This is not merely punctuation: eight echoed forms differ from their same-number candidates: `im → ir`, `sirra → sinra`, `tal → tas`, `kat → kas`, `pert → per`, `kól → palkor`, `hurim → hurir`, `toksa → tolsa`. The death fossil also names the old base `tok` rather than current `tol` (`05`, L-14).

Basis: `01-brief.yml` RG-03/RG-04; `politeness-taboo-euphemism.md` §6 steps 2/4 (build and record the grammar/lexicon). Require an explicit owner-approved ID/form reconciliation, including the missing L-11 dependency. Same-number candidates are evidence for repair, not an automatic mapping.

### PG-02 — HIGH — five live rungs have no lexical record IDs

TB-1 R1–R3 and TB-3 D2–D3 (`15-pragmatics.yml:243–246,269–272`) still say `pending 05-lexicon delivery`, although the 40-record lexicon is delivered. They specify English glosses and users, not lexeme bindings. D1's candidate is the existing fossil L-32, not a newly delivered live rung. SC-4/SC-5 and the handoff (`:342–353,502`) therefore exercise named placeholders, not a resolved ladder lexicon.

Basis: `politeness-taboo-euphemism.md` §6 step 4 explicitly requires ladders recorded in the lexicon with era tags; `01-brief.yml` RG-04. Preserve all five as UNRESOLVED until the lexicon owner supplies or explicitly declines their records; neither counting glosses as headwords nor substituting unrelated existing IDs closes this finding.

### PG-03 — MEDIUM — four-strata completeness is not supported

TB-1 calls `hur` a fossilized replacement (`15-pragmatics.yml:242`), but the current L-09 is a native root with `etymology: underived` (`05-lexicon.yml:317–328`), with no recorded replacement history. Its owner SR-01 calls for the valley's grandfather-name (`12-rank-rules.yml:309–319`); no binding establishes that this is `hur`. By contrast, L-32 explicitly records the death circumlocution and its lost suffix (`05:627–641`).

The shared minced oath in TB-1/TB-4 (`15:247–248,280–283`) is described as a reduced two-syllable formula but has no form or lexical ID. L-32's **sanction** mentions a storm formula; it does not deliver the reduced oath, and the cited **sense_note** describes the fossil instead. TB-6 and the handoff (`:303–314,502`) overstate two complete four-stratum packages. Sharing an oath between two taboos is not itself a defect; its undelivered realization and history are.

Basis: `politeness-taboo-euphemism.md` §5 closing rule: fossilized euphemism, live ladder, minced oath, legal/liturgical fossil of visibly different ages **per deep taboo**. Keep the missing lexical/history bindings explicit; the existing legal citation lists do not fill the other strata.

### PG-04 — HIGH — required referent honorifics have no adopted morphology

AX-2/PR-01/PR-02 (`15-pragmatics.yml:113–120,139–157`) request exalt/descend affixes; SA-1 requires descend for a valid claim (`:185–189`). Yet the delivered morphology's SYN-29 explicitly states that no grammatical honorific system is designed in the core (`03-morphosyntax.yml:255`), and M-17 (`03:211`) has no honorific slot. No form, slot-order rule, or M-/SYN- dependency discharges this mismatch. TV-2 admits the request is unresolved (`15:461–466`); that honesty does not make the mandatory act executable. SPC-1's claim that every third-person clause encodes the height relation also lacks an explicit default/neutral selection rule for referents outside PR-01/PR-02's licensing cases.

Basis: `politeness-taboo-euphemism.md` §2 (separate addressee/referent mechanisms; construction kit), §6 step 2; `01-brief.yml` RG-03/RG-04. Obtain an explicit cross-owner decision and stable grammar IDs before treating referent-marked testimony as implemented; this review does not choose or rewrite either owner's system.

### PG-05 — MEDIUM — addressee and bystander pitch rules have no priority

AX-1 and SA-1 void wrong-direction calls (`15-pragmatics.yml:102–112,189`), and SA-4 requires an up-call even to an equal (`:231`). The referenced owner simultaneously requires all-low realization for an avoidance-triggering bystander (14 A09, PH3, R01) and during storm speech (14 A03). These are at `14-kin-address.yml:39–44,159–175,192–195,208–237`. No priority says whether licensed flattening preserves an up-call's grammatical direction or voids it. SA-3 adds a market suspension (`15:217`) without saying how it interacts with the audience trigger.

Basis: `politeness-taboo-euphemism.md` §2 (independent addressee/referent/bystander axes) and §6 step 6 (stress-test eavesdroppers). A useful unresolved case is an affine entering during a junior's formal address: require one explicit outcome under the combined rules, not three separately plausible descriptions.

### PG-06 — HIGH — bystander answerability changes its trigger and scope

PR-03 defines answerability by venue and gives camp/above-line/storm-season speech an unanswerable status (`15-pragmatics.yml:158–168`). SA-1 instead says spectators' presence makes it answerable (`:183`), and SC-1 says a bystander makes the pass oath answerable without establishing a hearing venue (`:317–320`). It is unclear whether audience presence overrides location, season, or both.

The attribution to 12 SR-03 is also broader than the owner: SR-03 concerns the dead-name offense and its valley enforcement, not blanket immunity for all speech (`12-rank-rules.yml:331–341`). JU-3 still has spoken law and storm law at the high pasture (`12:493–499`).

Basis: `politeness-taboo-euphemism.md` §3 (taboo × sanction institution), §6 steps 3/6. Separate audience-conditioned register, quotation/transmission, and legal jurisdiction; state their combined result without generalizing one taboo's exemption to every act.

### PG-07 — HIGH — the hearing's cited altitude band has no court

SA-1 locates the fair court at the pass and explicitly cites band JU-2 (`15-pragmatics.yml:180–189`); SA-3 and SC-4 rely on that venue for answerability. The owner says JU-2 has a tally-warden and **no court**, with the scripted register left in the valley (`12-rank-rules.yml:486–492`), whereas JU-1 lists the fair court (`12:479–485`). This makes the same act's authorized venue contradictory, independently of whether a bystander is present.

Basis: `politeness-taboo-euphemism.md` §6 step 6 (hearing/market/oath stress tests), plus the ownership explicitly declared in `15` deps and `01-brief.yml` RG-03/RG-04. Route the venue conflict to the rank/assembly owners; this reviewer does not relocate either court.

### PG-08 — MEDIUM — rung-based dating exceeds the recorded chronology

All six rung rows lack `stage`/`era_tag` bindings (`15-pragmatics.yml:243–246,269–272`). Their `age` values are relative or functional: current youth usage, mourning usage, and a still-active fossil. TB-6 nevertheless dates D3/R3 texts to “this generation” (`:309`), while EC-2 places both candidates' entry in E1 (`:397–405`) without tying that era to the present generation. The death rows also differ by speaker/occasion, not just replacement date; coexisting registers cannot alone establish a document's date.

EC-2/EC-3/TV-4 retain `Nalne/Pertne` as lexicon-derived era names (`:399,408,474`), but the current lexicon offers `Kolne/Perne` only as candidates (`05-lexicon.yml:76–80,821`); 09 owns the actual seams. TV-4 correctly leaves the binding open.

Basis: `politeness-taboo-euphemism.md` §4–§5 and §6 step 4 (age-layered ladders and lexical era tags); `01-brief.yml` CP-07. Require per-rung introduction/continued-use information mapped to owned era IDs before claiming dating precision. This is a missing design chronology, not a demand for invented real-world dates.

## Checks that are sound within this review's scope

- AX-1/AX-2/AX-3 distinguish speaker→addressee, speaker→referent, speaker→bystander; AX-4 is a logic mix, not a fourth Comrie axis. The owner split is explicit. Conceptual separation does not resolve PG-04..PG-07.
- The discernment/volitional/licensed-impoliteness mix is labeled design-choice; PR-01 explicitly distinguishes own-side versus other-camp honorification. These follow the corpus §1–§2 recipe rather than claiming universal psychology.
- TB-5 supplies six taboo domains with owners and sanctions, within §6 step 3's 5–8-domain recipe. Its light-domain omissions are declared, not hidden.
- CAL-1..CAL-3 and the non-canon/handoff boundary preserve the corpus's cautions about universal face, Frazer as folk-model only, and the treadmill not proving reform futile (§7–§8).

## Limits and disposition

This is a review of a fictional design against repo evidence, not verification of the corpus bibliography or a real-language attestation claim. No external citation was invented. The prior 05-lexicon review describes an older revision; its measurements were not reused. The standard lexicon gate was left unchanged, and its clean result must not erase these manual findings. All eight remain open for owner/integrator disposition; none was silently fixed. Re-run the link probe and collision scenes after any owner revision. The integrator can append the required lane log entry; this worker's explicit path restriction excludes `LOG.md`.
