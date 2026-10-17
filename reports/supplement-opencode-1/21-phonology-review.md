# 21 — Phonology review: why three A-NEUTRAL REVIEWs persist in component 02

- wave: `supplement-opencode-1` (not a numbered GLM round; no SHONEN assessment,
  no rank promotion — this file is author-side evidence only)
- reviewer: worker 21 (REVIEWER role, phonology scope)
- baseline revision: `fe34faaafbe0add59ff68827a0df6c5782a72404`
- assigned surface: `tools/gates/phonology-sanity-gate.py` and
  `examples/culture-d2/components/02-phonology.yml`
- entry under review: `examples/culture-d2/components/02-phonology.yml`,
  sha256 `23500df0f97a43c8800e3a678df6928f476254e56ff844fabe0c71829ecbb538`
  (baseline bytes; byte-identical to the working tree at review time, and the
  file was clean in `git status`/`git diff` at `fe34faa`)
- gate under test: `tools/gates/phonology-sanity-gate.py`, sha256
  `fb05c644cafb0855481beb5d8bc3f619ae688d8b12787e530f01543f85372655`
  (byte-identical to the gate hash recorded in
  `tools/gates/frozen/round-3/MANIFEST.tsv` — the gate has not changed since
  round 3, so no gate-side drift explains the residue)
- written: 2026-10-17 (UTC stamps in Appendix B)

## 1. Verdict

The three A-NEUTRAL REVIEW findings are **real, reproducible, and correctly
retained**. They are not a linguistic impossibility, not a gate bug, and not
evidence that the round-4 reanalysis failed. They persist because the kernel's
A-NEUTRAL check is a **membership test against the declared inventory**
(`rule["dst"] in phonemes`), while the round-4 reanalysis (AL-1, AL-2, AL-7
reclassified as morphophonemic stem alternations) lives in packet fields the
kernel never reads. A held-out in-memory pair reproduces the mechanism exactly:
the same rule string fires A-NEUTRAL when its output is a listed phoneme and is
silent when it is not, and adding the complete rev-1.1 reanalysis metadata
changes nothing (Appendix A, cases B–D).

The residue therefore has to be handed off, not argued away: the gate records
the prompt, the component records the human-readable reanalysis, and only a
reviewer (or an integrator/lore decision) can close the item. The component
says exactly this in `gate_run.interpretation` — which is a calibration
positive, and the reason this review keeps the findings visible rather than
scoring the gate clean.

## 2. Reproduction (observed, not quoted)

| Run | Input (sha256) | Result |
|---|---|---|
| gate on component bytes (CLI) | `23500df0…` | exit 1; exactly 3 findings, all `A-NEUTRAL`; stdout sha256 `1ce5f0cd…` |
| gate on baseline packet (CLI) | `d5fb4088…` (`examples/culture-d2/packet.d2.yml`) | exit 1; identical stdout, sha256 `1ce5f0cd…` |
| gate on the committed round-3 frozen input | `54be6319…` (`tools/gates/frozen/round-3/inputs/examples/culture-d2/packet.d2.yml`) | exit 1; identical stdout, sha256 `1ce5f0cd…` |
| committed frozen outputs, round 3 and round 4 | — | both sha256 `1ce5f0cd…`; `diff` between them is empty |

So `gate_run.actual` ("byte-for-byte the round-3 frozen `phonology-sanity-gate.out`",
component line 451) is **verified**, and I verified it from three distinct
inputs, including a true replay of the committed frozen input. The output
digest also matches `output_sha256` in
`tools/gates/frozen/round-3/MANIFEST.tsv`, and the gate digest matches its
`gate_sha256` entry.

The three findings (verbatim stdout):

```
FINDING A-NEUTRAL: REVIEW — notable_rules[1] 'n → m / _ p' neutralizes 'n' to the phoneme 'm': permitted, but the phonemic distinction in that same context still needs a contrast witness or a reanalysis (spec §5)
FINDING A-NEUTRAL: REVIEW — notable_rules[2] 'n → m / _ b' neutralizes 'n' to the phoneme 'm': permitted, but the phonemic distinction in that same context still needs a contrast witness or a reanalysis (spec §5)
FINDING A-NEUTRAL: REVIEW — notable_rules[7] 's → h / _ #' neutralizes 's' to the phoneme 'h': permitted, but the phonemic distinction in that same context still needs a contrast witness or a reanalysis (spec §5)
```

`parsed_check` (component line 453) also reproduces: 15 consonants, all
classified as IPA consonants by the gate module; vowels `a e i o u`; `tones: 0`;
`(C)V(C)` → onset 1, nucleus 1, coda 1; all nine rules parse to
source/output/environment. No `FAIL`, no `G-DATA`, no `T-C`, no `T-V`, no
`T-SYL`, no `P-*` finding in any run.

## 3. Mechanism — why reanalysis cannot silence A-NEUTRAL

**3.1 The condition is membership, not opposition.**
`tools/gates/phonology-sanity-gate.py:986-993` fires `A-NEUTRAL` only when

- `rule["dst"] in phonemes` — the output token is one of the tokens listed in
  `phonology.consonants` / `phonology.vowels`,
- `not src_class` — the rule's source is not spelled as a natural class, and
- `rule["dst"] != rule["src"]`.

`phonemes` is built at line 944 as `set(cons_raw) | set(vow_raw)` — the raw
declared inventory. There is no contrast test, no minimal-pair test, no
allophony-table lookup: the kernel cannot represent "this surface phone is an
allomorph, not a merger". (Also verified: the gate has no allowlist,
suppression, or exemption path — the only `allow`/`ignore` hits in the file are
prose inside finding messages.)

**3.2 The kernel's entire read surface is five phonology keys plus `names`.**
Confirmed by reading every read-site in the file:

- `packet.get("phonology")` — line 641
- `phonology.get("consonants")` / `("vowels")` — lines 646-647
- `phonology.get("tones")` — line 781
- `phonology.get("phonotactics")` — line 807
- `phonology.get("notable_rules")` — line 933
- `packet.get("names")` — line 1050

The rev-1.1 reanalysis is stored in `allophony[]` (`classification` line 152,
`morphological_trigger`, `alternation_witness_pair`, `neutralization` lines
159/169/203), `witnesses[]` (line 346), and `strata_note` (line 96) — **none of
which the kernel reads**. The `revision_notes` themselves say the nine finite
rule strings are unchanged (lines 2-4), and `strata_note` calls the gate-facing
strings "unchanged phonological projections, not encodings of the
morphological triggers". Persistence is therefore *by construction*, not an
oversight.

**3.3 The prompt is the spec's own unresolved-review clause.**
`corpus/knowledge/verification/phonology-sanity-gate.md:89`:
"Allophone neutralization into another phoneme's usual phone is permitted. A
phonemic distinction claimed in the SAME conditioning context still needs a
contrast witness or reanalysis." The kernel emits exactly that request. By the
spec's own verdict table (§1, line 12-14), an uncompleted reanalysis is
`REVIEW` — never `FAIL`. Calling the residue an error would misread the spec.

**3.4 The reanalysis is internally sound where a human can check it** (all
locators into the baseline component bytes):

- `P-3` (line 139) licenses coda set `{n, l, r, s}` — underlying coda `/m/` and
  coda `/h/` are excluded, so no same-context coda contrast `/n/:/m/` or
  `/s/:/h/` is claimed.
- The `/n/ : /m/` contrast is witnessed in onsets: `W-4` *nama* (line 361) and
  `W-5` *mata* (line 365).
- The alternating pairs exist: `W-23` *san* → [san] (line 439) against `W-3`
  *sanpa* → [sampa] / `W-6` *sanba* → [samba]; `W-11` *hus* → [ɸuh] against
  `W-1` *husa* → [ɸusa].
- `AL-1`/`AL-2`/`AL-7` `neutralization` fields (lines 159/169/203) state the
  reanalysis each finding asks for, and explicitly record that the A-NEUTRAL
  prompt stays visible rather than being suppressed.

So the component does what a reviewer would want; the kernel simply has no slot
for it. The gate's input contract (`spec §2`) is a finite segment kernel; `spec
§6`'s runnable kernel takes a different input object (inventory/phones/
qualities/legal/rules/examples/priors) that also has no reanalysis field.

**3.5 What would change the residue** (none of these is this reviewer's call):

1. Edit the inventory (drop `/m/` or `/h/`) — not warranted; both are needed by
   the design and are witnessed as onsets.
2. Rewrite the rule strings to surface-only spellings — changes the linguistic
   content of the projection, a design decision, not a fix.
3. Extend the kernel/spec to consume a reanalysis field — a spec-and-gate
   change owned by the gate's author, not a reviewer edit.
4. Accept and hand off the residue with its witnesses — what the component
   already does, and what this review recommends.

## 4. Held-out positive and negative in-memory packet test

Harness: `reports/supplement-opencode-1/scratch/21/an_audit.py` (stdlib only;
loads the baseline gate module from a verified scratch copy; never passes an
untrusted manifest, never touches the tree outside scratch). Observed run:

```
[A] baseline component: exit 1, 3 findings
    tally: {'A-NEUTRAL': 3}
[B] positive packet (m listed): exit 1 ids=[('A-NEUTRAL', 1)]
[C] negative packet (m NOT listed): exit 0 ids=[]
[D] reanalysis-carrying packet: exit 1 ids=[('A-NEUTRAL', 1)] identical_to_B=True
[E] class-source packet: exit 1 ids=[('A-CLASS', 1)] aneutral=False
[F] CLI baseline copy: exit 1 findings=3 ids=[('A-NEUTRAL', 3)]
[F2] CLI tampered copy (tones: 5): exit 1 ids=[('A-NEUTRAL', 3), ('T-TONE', 1)]
SCRATCH-HARNESS: all held-out checks passed
```

Test design (held out — neither packet is the gate's own fixture):

- **B, positive control**: a minimal in-memory packet whose inventory lists `m`
  and whose single rule is the exact string `n → m / _ p`. A-NEUTRAL fires on
  `notable_rules[1]`. This is the D2 condition in miniature.
- **C, negative control**: the *identical rule string*, with `m` absent from the
  inventory. A-NEUTRAL is silent (exit 0, no findings at all). This isolates the
  membership test as the single deciding factor: the persistence of the three
  findings depends on the component *listing* `/m/` and `/h/`, not on any
  linguistic merger.
- **D, reanalysis blindness**: packet B plus an `allophony:` block carrying the
  rev-1.1 AL-1 metadata verbatim in kind (`classification`,
  `morphological_trigger`, `alternation_witness_pair`, `neutralization`), plus
  `witnesses` and a `strata_note`. Output is identical to B. The kernel cannot
  consume the reanalysis even when it is spelled exactly as the component
  spells it.
- **E, second negative**: the same rule with a class-token source (`N → m / _ p`)
  produces `A-CLASS` and no A-NEUTRAL — confirming the `not src_class` guard, so
  a component cannot "fix" the prompt by class-spelling without changing the
  rule's meaning and triggering a different review.
- **F/F2, CLI sanity**: the gate CLI reproduces the component's three findings
  on a scratch copy of the baseline bytes, and a deliberate tamper
  (`tones: 0` → `tones: 5`) adds `T-TONE` — the run is reading this file's
  `phonology` block, not passing everything.

Interpretation: the residue is a property of the *finite projection + declared
inventory*, exactly as the component claims. It is resolvable only by a human
adjudication (or the spec work in §3.5), never by richer provenance inside the
component.

## 5. Source recheck (freshness)

Six audits; five rows carry directly retrieved public passages. Retrieval was
by `FetchURL` only (no shell network calls). `WebSearch` was quota-blocked at
review time (HTTP 403 from the search backend), so candidates were located by
following citations inside retrievable pages; blocked routes are recorded as
access limits, never as confirmation.

| id | claim (entry locator) | source | status | verdict |
|---|---|---|---|---|
| SR-1 | 15 consonants sit in the "moderately small" band (15-18), modal 19-25 noted and not chased (`follows: F-1`, line 21; series `C-1..C-6`) | wals.info/chapter/1 | full text retrieved | supported |
| SR-2 | 5 vowel qualities in the dispersion the corpus cites for five-vowel systems `/i e a o u/` (`V-1`, line 123) | wals.info/chapter/2 | full text retrieved | supported |
| SR-3 | the front-rounded implication is "not triggered rather than broken"; the corpus-carried hedge is "in most cases" (`V-1` line 123; gate `M-ROUND`) | wals.info/chapter/11 | full text retrieved | supported |
| SR-4 | AC-6's tonogenesis story: "an older coda voicing contrast was reanalysed as pitch on the preceding syllable", said to follow corpus §6 (Haudricourt 1954; Thurgood 2002) (`AC-6`, lines 237-239) — **language/era coupling audit** | local corpus §6 locator + tertiary summary (Wikipedia); scholarly full text not retrieved | partial (local + tertiary only) | unresolved |
| SR-5 | "mountains plus long-distance herding give whistled registers (Silbo Gomero, Kuskoey, Chinantec … Meyer 2008)"; the whistle encodes accent peak, syllable count, contour (`R-1` line 268; `ENV-1` line 321) — **language/ecology coupling audit** | UNESCO ICH entry for Silbo Gomero; Meyer 2008 full text not retrieved | institutional full text retrieved (instance-level) | supported (partial) |
| SR-6 | two-level accent, zero lexical tones, contour never stored; 2-level systems common, 5+ rare (`AC-1` line 221, `AC-5` line 235; gate `T-TONE`) | wals.info/chapter/13 | full text retrieved | supported |

Row notes:

- **SR-1** — WALS ch. 1 states the cut-offs verbatim: "the remainder divided
  into the categories small (from 6 to 14 consonants), moderately small (15-18),
  moderately large (26-33), and large (34 or more consonants)" and defines
  "average" as "22 ± 3" with modal value 22. The component's own count of 15 is
  verified locally (§2). The word "moderately small" and the 15-18 interval are
  exactly WALS's, so the entry's typological label is accurate.
- **SR-2** — WALS ch. 2: five-vowel inventories are the single most frequent
  ("188 or just over one-third"), and the chapter's own five-vowel exemplar is
  Spanish with `/i, e, a, o, u/`. Supports both the band placement and the
  dispersion example the corpus carries.
- **SR-3** — WALS ch. 11: "In most cases when any front rounded vowel occurs,
  the inventory of vowels has a front unrounded vowel of similar height, and
  also a back rounded vowel of similar height." This is the source of the hedge
  the gate's `M-ROUND` message repeats; the component's design (no front
  rounded vowels at all) means the prior is not triggered, which matches the
  retrieved wording.
- **SR-4 (coupling)** — this is the one audit that tests a language/era
  (diachrony) coupling rather than a bibliography fact, and it returns a
  **review note, not a confirmation**. The entry's own `follows` cites a model
  whose corpus wording is "loss of *laryngeal* codas reinterpreted as low/high
  pitch", while `AC-6` rewrites the trigger as a "*coda voicing* contrast" and
  places the pitch "on the preceding syllable". `AC-6`'s own continuation ("the
  ridge-locus list preserves the stems whose peak stood where a coda once
  stood") reads as pitch on the *host* syllable, so the phrase "preceding
  syllable" is at best ambiguous inside the file. A retrieved tertiary summary
  of coda-conditioned tonogenesis supports the *coda-loss* path and lists
  voicing among tonogenetic series, so this is **not** an impossibility claim —
  but the scholarly full texts that could settle the wording (Haudricourt's
  translation on HAL; Kingston's and Ratliff's tonogenesis chapters; Cambridge
  JIPA; PNAS) were all unreachable at review time (see access limits). Verdict
  `unresolved`, with the local wording mismatch routed to the component owner in
  §8. The component itself declares the D2 story invented (line 239, `CAL-5`),
  which bounds the damage: this is a citation-fit note, not a false claim about
  a real language.
- **SR-5 (coupling)** — the UNESCO ICH entry documents a real, large-community
  whistled language on a mountainous island, distinguishes whistles "according
  to pitch and whether they are interrupted or continuous", and notes school
  teaching since 1999 — the instance the entry's warrant rests on, and the
  pitch-encoding claim. What the UNESCO entry does **not** carry is the causal
  herding/mountain generalization for all three named communities (Silbo,
  Kuşköy, Chinantec); the Meyer 2008 JIPA article that the corpus cites could not
  be retrieved (PDF extraction unavailable; publisher landing page 429). The
  entry already scopes this ("design on a corpus-grounded coupling — flagged as
  a design stipulation wherever the detail exceeds the corpus"), so the audit
  lands as partial support, not as a defect.
- **SR-6** — WALS ch. 13 puts "simple tone system" (essentially a two-way
  contrast) at 132/527 (25.1%) against complex systems at 88/527 (16.7%), and
  gives Thai's five-tone system as an exemplar of the complex class. That
  supports the 2-level-common / 5+-rare framing the gate's `T-TONE` message and
  the component's two-level accent rely on.

## 6. Local cross-checks (not source rechecks)

- **OQ-1's reported conflict exists in the baseline bytes.** The component's
  `interface.open_conflict_reported` says 04-orthography assumes the script
  marks accent while 12-rank-rules and 14-kin-address say it does not. Baseline
  locators: `04-orthography.yml:125` ("if pitch accent is absent, delete glyph
  G-P01 and the OR-4 accent obligation"), `12-rank-rules.yml:489` ("writes what
  it cannot say: the script marks no pitch accent"), `14-kin-address.yml:198`
  ("the adapted script carries no accent marks until they are added"). The
  conflict report is accurate and correctly left open; owner 04-orthography.
- **Adjacency, not absorbed**: the wave baseline records naming-gate
  `PHON-INVENTORY: 10` and `PHON-CODA: 1`
  (`reports/supplement-opencode-1/claims.json`). Those come from
  `tools/gates/naming-collision-gate.py` (a different kernel with a different
  input contract — see its docstring table), not from the phonology gate. They
  are not counted in, or explained by, this review.
- **Observed, left for the operability owner**: `tools/gates/frozen/round-3/`
  carries an `inputs/` tree plus `MANIFEST.tsv` with pinned digests (verified:
  input `54be6319…`, gate `fb05c644…`, output `1ce5f0cd…` all match), while
  `tools/gates/frozen/round-4/` carries only five `.out` files with no inputs or
  manifest. Out of my scope; flagged for the frozen-replay worker.

## 7. Limits of this review

- I reviewed the **baseline bytes** of the component and the gate only. No
  later worker's edits are assumed to have landed, and I ran nothing that writes
  outside `reports/supplement-opencode-1/scratch/21/`.
- The gate's own selftest was not re-run (it writes
  `tools/gates/fixtures/phonology-sanity-gate.yml` and `.expected`, i.e. shared
  tree files). The committed fixture was not touched; the CLI, module-level
  `evaluate()`, and the frozen replays above are my evidence instead.
- `tools/gates/frozen/round-4/*.out` has no committed input snapshot, so the
  round-4 run cannot be independently replayed from its own artifacts; I
  established equality only through the digest-identical outputs.
- Access limits for source recheck (all recorded in Appendix B): Cambridge
  Core / doi.org HTTP 429; PNAS HTTP 403; HAL (both hostnames) blocked by
  Anubis; BASE search blocked; Semantic Scholar API HTTP 429; OpenAlex/DOAJ
  JSON endpoints not extractable by the fetch tool; DuckDuckGo captcha;
  `glossary.sil.org` returned a JS shell; PDF targets (ISCA archive, Kingston
  chapter) not text-extractable. No snippet, metadata hit, or blocked fetch was
  counted as confirmation, and no source or page number is invented here.
- No corpus erratum was appended: the wording mismatch in SR-4 is a
  citation-fit observation about a design drill component (not a corpus
  knowledge entry, and not my assigned write path). It is routed in §8.

## 8. Routed review notes (for the integrator / component owner — not absorbed)

1. **AC-6 citation fit (SR-4).** Reconcile `AC-6` (lines 237-239) with the model
   it cites: either say "laryngeal codas" (the corpus §6 wording) or state
   plainly that the voicing variant is the invented part; and clarify "pitch on
   the preceding syllable" against `AC-3`'s "the peak stood where a coda once
   stood". Owner: component 02 (D2 design drill), via the integrator.
2. **The three A-NEUTRAL REVIEWs should travel with the handoff**, with the
   AL-1/AL-2/AL-7 witnesses, as `REVIEW` items (spec §5), not be reported as a
   clean gate and not be "fixed" by editing the nine rule strings. This is the
   component's own position (`gate_run.interpretation`), now reproduced
   independently.
3. **Optional, gate-owner-facing:** if a future spec revision wants
   reanalysis-carrying packets to clear `A-NEUTRAL`, the kernel needs an
   explicit input field (e.g. a per-rule `reanalysis` reference checked against
   supplied witnesses). That is a spec/kernel change; nothing in this review
   authorizes it, and the current behaviour is correct for the current contract.

## Appendix A — commands actually executed and observed results

```
# baseline byte extraction (scratch copies), digests verified before use
git show fe34faa:tools/gates/phonology-sanity-gate.py        > scratch/21/gate-baseline.py            # fb05c644…
git show fe34faa:examples/culture-d2/components/02-phonology.yml > scratch/21/02-phonology.baseline.yml # 23500df0…
git show fe34faa:examples/culture-d2/packet.d2.yml           > scratch/21/packet.baseline.yml        # d5fb4088…

# CLI runs
python3 tools/gates/phonology-sanity-gate.py scratch/21/02-phonology.baseline.yml   # exit 1, 3 findings, sha 1ce5f0cd…
python3 tools/gates/phonology-sanity-gate.py scratch/21/packet.baseline.yml         # exit 1, 3 findings, sha 1ce5f0cd…
python3 tools/gates/phonology-sanity-gate.py tools/gates/frozen/round-3/inputs/examples/culture-d2/packet.d2.yml
                                                                                    # exit 1, identical output
diff <cli output> tools/gates/frozen/round-3/phonology-sanity-gate.out              # empty
diff tools/gates/frozen/round-3/phonology-sanity-gate.out tools/gates/frozen/round-4/phonology-sanity-gate.out  # empty
git diff fe34faa -- tools/gates/phonology-sanity-gate.py                            # empty (gate unchanged)

# held-out in-memory harness (positive/negative/reanalysis-blindness/class-source/CLI+tamper)
python3 reports/supplement-opencode-1/scratch/21/an_audit.py
# → "[A]..[F2] … SCRATCH-HARNESS: all held-out checks passed" (exit 0); full log in scratch/21/an_audit.out
```

Harness assertions (so a re-run fails loudly, not silently): each held-out case
asserts its exit code, its expected finding-id set, that the reanalysis-carrying
packet's output is identical to the positive control's, and that the tampered
CLI copy adds `T-TONE`.

## Appendix B — audit JSON (wave schema; embedded here because this worker's only assigned write path is this report)

```json
{
  "wave": "supplement-opencode-1",
  "baseline_revision": "fe34faaafbe0add59ff68827a0df6c5782a72404",
  "entry": "examples/culture-d2/components/02-phonology.yml",
  "entry_sha256_before": "23500df0f97a43c8800e3a678df6928f476254e56ff844fabe0c71829ecbb538",
  "checked_at_utc": "2026-10-17T15:45:48Z",
  "audits": [
    {
      "id": "SR-1",
      "claim": "15 consonants sit in the WALS 'moderately small' band (15-18); the modal 19-25 class is noted and deliberately not chased.",
      "entry_locator": "examples/culture-d2/components/02-phonology.yml:21 (follows F-1, decision_followed); inventory_record C-1..C-6",
      "source_url": "https://wals.info/chapter/1",
      "retrieval_status": "full text retrieved",
      "source_locator": "WALS Online, ch. 1 (Maddieson, Consonant Inventories), §1 categories paragraph",
      "source_excerpt": "the remainder divided into the categories small (from 6 to 14 consonants), moderately small (15-18), moderately large (26-33), and large (34 or more consonants)",
      "verdict": "supported",
      "basis": "Retrieved paragraph gives the band cut-offs verbatim and defines 'average' as 22 +/- 3 with modal value 22, i.e. the 19-25 band the entry names as modal; the entry's own inventory count of 15 was reproduced locally from the baseline bytes.",
      "access_limit": "none for this row"
    },
    {
      "id": "SR-2",
      "claim": "Five vowel qualities in the dispersion the corpus cites for five-vowel systems (/i e a o u/).",
      "entry_locator": "examples/culture-d2/components/02-phonology.yml:123 (inventory_record V-1)",
      "source_url": "https://wals.info/chapter/2",
      "retrieval_status": "full text retrieved",
      "source_locator": "WALS Online, ch. 2 (Maddieson, Vowel Quality Inventories), §2 values paragraph",
      "source_excerpt": "Considerably more languages have an inventory of five vowels than any other number — 188 or just over one-third. ... Spanish is thus counted as having five vowels ... i, e, a, o, u",
      "verdict": "supported",
      "basis": "The chapter both confirms five qualities as the most frequent count and itself uses the /i e a o u/ five-vowel dispersion the entry cites through corpus section 2.",
      "access_limit": "none for this row"
    },
    {
      "id": "SR-3",
      "claim": "No rounding contrast on the front vowels, so the front-rounded implication is not triggered rather than broken (hedged 'in most cases' in the corpus-carried prior).",
      "entry_locator": "examples/culture-d2/components/02-phonology.yml:123 (V-1) and 235 (AC-5); gate M-ROUND message in tools/gates/phonology-sanity-gate.py:867-872",
      "source_url": "https://wals.info/chapter/11",
      "retrieval_status": "full text retrieved",
      "source_locator": "WALS Online, ch. 11 (Maddieson, Front Rounded Vowels), §1 introduction",
      "source_excerpt": "In most cases when any front rounded vowel occurs, the inventory of vowels has a front unrounded vowel of similar height, and also a back rounded vowel of similar height.",
      "verdict": "supported",
      "basis": "The retrieved wording is the source of the 'in most cases' hedge; the entry's inventory contains no front rounded vowel, so the prior is simply not instantiated, matching the entry's claim.",
      "access_limit": "none for this row"
    },
    {
      "id": "SR-4",
      "claim": "AC-6: an older coda voicing contrast was reanalysed as pitch on the preceding syllable and the coda obstruents were lost; stated to follow corpus section 6 tonogenesis (Haudricourt 1954; Thurgood 2002). Language/era (diachrony) coupling audit.",
      "entry_locator": "examples/culture-d2/components/02-phonology.yml:237-239 (AC-6 rule + follows); the cited model at corpus/knowledge/linguistics/phonetics-phonology.md:181-182; the entry's own calibration CAL-5 at 02-phonology.yml:526",
      "source_url": "https://en.wikipedia.org/wiki/Tone_(linguistics)",
      "retrieval_status": "local cited model + tertiary summary retrieved; scholarly full text NOT retrieved",
      "source_locator": "local: corpus/knowledge/linguistics/phonetics-phonology.md section 6 ('Tonogenesis: loss of laryngeal codas reinterpreted as low/high pitch'); tertiary: Tone (linguistics), 'Triggers of tonogenesis' section",
      "source_excerpt": "local: 'Tonogenesis: loss of laryngeal codas reinterpreted as low/high pitch (Haudricourt 1954; Thurgood 2002)'; tertiary: 'final fricatives or other consonants may phonetically affect the pitch of preceding vowels'",
      "verdict": "unresolved",
      "basis": "The cited local model names laryngeal codas, while AC-6 names a coda voicing contrast and 'the preceding syllable'; the file's own AC-3 gloss ('the peak stood where a coda once stood') reads as pitch on the host syllable. Retrieved tertiary text supports the coda-loss path and does not make a voicing-coda trigger impossible, so this is a citation-fit/wording question, not a linguistic impossibility; it is routed to the component owner rather than resolved or absorbed.",
      "access_limit": "Haudricourt HAL translation (halshs-01678018, Anubis block), Cambridge JIPA and doi.org (HTTP 429), PNAS (HTTP 403), Semantic Scholar API (HTTP 429), DDG (captcha), PDF targets not text-extractable; no page numbers or quotes were invented."
    },
    {
      "id": "SR-5",
      "claim": "Mountains plus long-distance herding give whistled registers (Silbo Gomero, Kuskoey, Chinantec, via Meyer 2008); the register encodes accent-peak position, syllable count and phrase contour. Language/ecology coupling audit.",
      "entry_locator": "examples/culture-d2/components/02-phonology.yml:268-286 (R-1 grounding/encodes) and 321-324 (ENV-1)",
      "source_url": "https://ich.unesco.org/en/RL/silbo-gomero-whistled-language-of-la-gomera-canary-islands-spain-00172",
      "retrieval_status": "institutional full text retrieved (instance level)",
      "source_locator": "UNESCO Intangible Cultural Heritage, Silbo Gomero entry (inscribed 2009), description paragraph",
      "source_excerpt": "The whistled language of La Gomera Island in the Canaries, the Silbo Gomero, replicates the islanders' habitual language (Castilian Spanish) with whistling. ... The whistles can be distinguished according to pitch and whether they are interrupted or continuous.",
      "verdict": "supported",
      "basis": "Retrieved entry documents a real, community-wide whistled register on a mountainous island whose whistles encode pitch distinctions - the instance and the pitch-encoding the entry's warrant uses. The entry itself flags every detail beyond the corpus as a design stipulation, so the coupling is used at exactly the strength the retrieved source supports.",
      "access_limit": "UNESCO entry does not carry the causal mountain-herding generalization for all three named communities; Meyer 2008 (JIPA 38(1):69-94, doi:10.1017/S0025100308003277) full text not retrievable (landing 429 / PDF not extractable), so the three-language typology claim beyond Silbo remains uncorroborated in this pass."
    },
    {
      "id": "SR-6",
      "claim": "Two accent levels, zero lexical tones, contour never stored; the tone-structure prior '2-tone systems most common, 5+ rare' behind the T-TONE band.",
      "entry_locator": "examples/culture-d2/components/02-phonology.yml:221 (AC-1), 235-236 (AC-5), 259-262 (CX-NOTE); gate T-TONE message at tools/gates/phonology-sanity-gate.py:800-804",
      "source_url": "https://wals.info/chapter/13",
      "retrieval_status": "full text retrieved",
      "source_locator": "WALS Online, ch. 13 (Maddieson, Tone), §2 definition and distribution; §1 Thai five-tone example",
      "source_excerpt": "About a quarter of the languages (132, or 25.1%) have simple tone systems ... Less than a fifth (88, or 16.7%) have complex tone systems.",
      "verdict": "supported",
      "basis": "Simple tone systems (defined in the chapter as essentially a two-way high/low contrast) outnumber complex systems, and the chapter's five-tone Thai example belongs to the complex class - consistent with the 2-common/5+-rare framing; the entry's own tones: 0 with a culminative accent is a different system type (Hyman 2006, cited via the corpus) and is not contradicted by this chapter.",
      "access_limit": "none for this row"
    }
  ]
}
```

## Appendix C — file/hash ledger

| artifact | sha256 |
|---|---|
| `tools/gates/phonology-sanity-gate.py` (baseline) | `fb05c644cafb0855481beb5d8bc3f619ae688d8b12787e530f01543f85372655` |
| `examples/culture-d2/components/02-phonology.yml` (baseline entry) | `23500df0f97a43c8800e3a678df6928f476254e56ff844fabe0c71829ecbb538` |
| `examples/culture-d2/packet.d2.yml` (baseline) | `d5fb408871dcb985c2f9b134a26c6d64e8640a6f1f17ba1c6bb3c5db1d6dbd96` |
| `tools/gates/frozen/round-3/inputs/examples/culture-d2/packet.d2.yml` | `54be6319e4907d20c8239555e3f79fcb9bb6b36d102a30a6beabf34b146459f4` |
| gate stdout (all four runs above) | `1ce5f0cdabad1bda177245607226cb6bf643f2bfbbe2ddb0918c510749066dd2` |
| scratch harness log | `reports/supplement-opencode-1/scratch/21/an_audit.out` |

Scratch artifacts (temporary, wave-local): `reports/supplement-opencode-1/scratch/21/`
(`an_audit.py`, `an_audit.out`, `gate-baseline.py`, `02-phonology.baseline.yml`,
`packet.baseline.yml`, `cli-*.out`). Nothing outside this directory and this
report was written.
