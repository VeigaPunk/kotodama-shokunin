# C16 — topic-line verification (non-author)

- Seat: `C16` | role: verifier | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:6` (`baseline_commit: "a01405d"`)
- Out path: `reports/round-48/cov/C16-topic.md` (this file)
- Non-author statement: I drafted neither the r44 seed nor either head block; I edited no fragment. Every number below was recomputed in this seat, and the commands are reproduced in §8.

**One-line judgment.** The `- topic:` line is **byte-equal to the r44 seed at three points in time** (seed `K02:227`, r47 draft `C04:114`, r48 draft `C02:114`; 766 chars, sha256 `bc7274f4…`), passes the live sweep's own `topic_of` and row parsers, and reads as a **register/method** entry rather than a generic map-file: it promises a production chain, a question-fixed typology, decision surfaces, a build order and a calibration bank, and promises no historical narrative. **Two non-blocking observations** (F1 digest convention; F2 the literal "register" slot is named one field below, in `- gap filled:`), plus **one landing condition** (F3: the right-sized r48 body did not exist at my cut, so every promised element must be re-checked against the assembled entry before apply). No blocking defect in the topic line.

---

## 1. What exists at my write cut

`reports/round-48/` held only seat fragments; there was **no assembled r48 entry body** when I measured (`find reports/round-48 -type f`, §8). The head block was filed as `reports/round-48/cov/C02-header.md` (263 lines), so the verification targets are:

| Artifact | What it is | Line | Bytes |
|---|---|---|---|
| `reports/round-44/scout/K02-gap-scout.md` | the seed (`§4.2`, fenced `text`, single physical line) | `:227` | 766 topic chars |
| `reports/round-47/cov/C04-entry-header.md` | r47 head block, never landed (total still 223) | `:114` | 766 chars, identical |
| `reports/round-48/cov/C02-header.md` | r48 head block, fenced at `:111`, topic at `:114` | `:114` | 766 chars, identical |

The live tree is still **223 files / culture-material 25** (`find`/`ls`, §8), so both head blocks are drafts; the target path `corpus/knowledge/culture-material/cartography-and-mapmaking.md` is absent and the topic-owner probe is 0 lines.

---

## 2. Byte-equality — measured, not carried

The seed's topic text and both drafted topic texts are the same bytes. I extracted the text after `- topic:` from each source and hashed it, and separately hashed the **whole physical line**:

| Comparison | Result |
|---|---|
| seed `K02:227` == r47 `C04:114` (stripped topic) | **True**, 766 chars, sha256 `bc7274f411cc6977032ab2754ebff19def4a1f5240fe5882624fc76e744f4495` |
| seed `K02:227` == r48 `C02:114` (stripped topic) | **True**, same 766 chars and sha256 |
| whole-line bytes (`- topic: …`) seed == r47 == r48 | **True**, sha256 `a42926b1d0fe5ac5d608bb4ebd8e16873b3ed2f43a74c34392f0e4d5632496f8` (no trailing newline) |
| whole line **with** `\n` | sha256 `9424fb81c22fe8c9a468d75aa291e1b5943a268b8699320915de52d7bda3459a` |
| tabs / trailing whitespace in the topic text | none (`'\t' in s` False; `s == s.rstrip()` True) |
| physical lines the field occupies | **1** (so the README row is a single line and `ROW_RE` can match it) |

The r48 header states the seed-line digest as `9424fb81…` at `reports/round-48/cov/C02-header.md:109`. That value **reproduces exactly** if "the line" means the line including its newline terminator; the naked-line digest is `a42926b1…` and the topic-text digest is `bc7274f4…`. The filed value is therefore true under a stated convention, not a fabricated hash. See F1 for the wording recommendation.

---

## 3. Does the topic line read as a register, not a map-file?

### 3.1 Five register tests against the topic text

| Test | Evidence in the topic line | Verdict |
|---|---|---|
| Names a **production system** with stages and institutions, not an object list | "the survey → projection → drawing → reproduction chain that makes a map authoritative" | pass |
| Carries a **typology fixed by function**, not by era or region | "the map-form typology (itinerary/strip, cadastral, chorographic, portolan, celestial, cosmographic, thematic, and the cartographic history/lienzo)" — eight forms, question-driven; the body states the rule at `reports/round-47/cov/C01-entry-a.md:236` | pass |
| Names **decision surfaces** an author can act on | "projection and scale as claims about what matters"; "the symbol grammar (orientation, compass rose, scale bar, legend, boundary, blank)"; "the reproduction economics (manuscript, woodblock, copperplate, the atlas)" | pass |
| Ends in a **build instrument**, not a survey | "a build order, a decision record, a NON-CANON worked example" | pass |
| Carries a **calibration posture** (what not to ship as settled) | "a calibration bank (the neutral-map claim, the flat-earth myth, portolan accuracy, the primitive-map fallacy, map = territory)" | pass |
| **Negative test:** a generic map-file would promise history/description | the topic promises no chronology, no "history of cartography", no region survey | pass |

For comparison, the corpus's register precedent uses the same shape: `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:5` ("the lithic register … the mineral slot the register family lacks … Covers: … a build protocol; a NON-CANON worked fixture … a calibration bank"). The cartography topic has the same skeleton minus the literal word "register".

### 3.2 The register **slot** question — where the slot is named

The mission asks that the line "name the register slot it fills (lapidary-adjacent named slot for cartography)". Read literally, the topic line names the **object class and its method** ("the map as an instrument and a claim for fictional cultures"), not the slot. The slot is named **one field below**, in the same head block:

- `reports/round-48/cov/C02-header.md:115` (and r47 `C04:115`): "the corpus owns the world-picture, the sacred route, the orientation code and the built plan, **and owns no made map** … This entry owns the surveyed, projected, reproduced sheet as production."
- r47 body `reports/round-47/cov/C01-entry-a.md:109`: "## 2. What makes a map a register — the five-condition test".

The **lapidary analogy holds only in part**, and the difference is worth recording rather than smoothing over:

| | lithic register (landed r42) | cartography (this claim) |
|---|---|---|
| Where the missing component is named | positively, in the partition's method file: "bestiary + **lapidary** + numerology + heraldic code" (`corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:29`) | negatively, by disclaimer: "T-O diagrams are symbolic, **not survey maps**" (`corpus/knowledge/myth-symbol/cosmology-cosmography.md:71`) and "**not cartographic**" (`:102`) |
| Competing definition that must be dispositioned | none | `corpus/knowledge/myth-symbol/cosmology-cosmography.md:27`: cosmography is "how the world is drawn (**maps**), named, walked, and built" |
| The topic line itself | says "the lithic register … the mineral slot the register family lacks" | does **not** use the word "register" or "slot" |

So: the corpus **names the slot by exclusion**, not by a method-file charter, and the r48 head block handles the weaker charter honestly — `- gap filled:` now dispositions `:27` and quotes `:71`/`:102` (verified live, §8). That is the correct treatment; it is just not the lapidary's positive-naming shape. I do **not** recommend forcing the word "register" into the topic (see F2): the amendment would break the byte-equality the round has measured since r44, and the slot is already named in the head block.

---

## 4. Topic-promise ledger — what the line obliges the right-sized entry to contain

The topic is not decoration: it is the claim the README row repeats to every reader. I traced each promise to the r47 body (the only body bytes that exist) and marked the r48 risk. **This ledger is the binding check for the assembled draft.**

| # | Promise in the topic text | r47 body anchor (verified live) | r48 landing condition |
|---|---|---|---|
| 1 | survey → projection → drawing → reproduction chain | `reports/round-47/cov/C02-entry-b.md:41` (§5, seven links); the topic compresses 7 links to 4 stages without contradicting them (select/measure/control/reduce = survey; project; symbolize = drawing; reproduce) | the right-sized cut must keep the chain table, not only name it |
| 2 | map-form typology, eight named forms | `reports/round-47/cov/C01-entry-a.md:238-249` — counted **8** form rows (`grep -c '^| \*\*'` → 8) | all eight forms must survive; R03 **B9** (the minimum-build table covers 5 of 8) must not be inherited as if it were the typology |
| 3 | projection and scale as claims about what matters | `reports/round-47/cov/C01-entry-a.md:171-177` (projection table), `:184-187` (scale = three numbers) | keep both; a cut that leaves only the mechanism prose hollows the promise |
| 4 | symbol grammar: orientation, compass rose, scale bar, legend, boundary, blank | orientation §3.4 at `C01:189` (compass trap `:197`); symbolization §3.5 at `C01:200`, legend `:202-207`, boundary line `:204`; the suppressed blank at `C01:163` (§3.1) | each of the six items must remain readable as a lever, not merely mentioned |
| 5 | reproduction economics: manuscript, woodblock, copperplate, atlas | `reports/round-47/cov/C02-entry-b.md:149` (§6 cost/scarcity/prestige), `:218` (§7 trade); "woodblock" and "copperplate" both present in C02 | keep §6/§7's cost ladder; the four media must be named |
| 6 | the map's silences | `C01:163` (suppressed class), `C02:34` (silences distributed in §3.1/§5.5), `C03:84` (blank policy: unknown/withheld/not-applicable) | keep the three-way blank distinction — it is the operational form of the promise |
| 7 | use as a legal/territorial instrument | `C01:214` ("the treaty map, the cadastral register, the tithe map, the boundary map … the deposited copy is the legal object"); `C02:299` (which map is performative) | keep at least the deposited-copy rule |
| 8 | build order | `reports/round-47/cov/C03-entry-c.md:73` (§10, nine steps, artifact per step) | keep the step→artifact column; steps without outputs are decoration |
| 9 | decision record | `C03:189` (§13, `DR-CT-01..12`) | keep stable ids; note R03 **B7/F-2**: the worked example does not cite the DR rows |
| 10 | NON-CANON worked example | `C03:107` (§11, one lagoon, two maps) | **R03 B7 must be fixed first**: the update rule is stated three incompatible ways (`C03:123`, `:137`, `:150`); one rule, stated once |
| 11 | calibration bank, five named readings | `C03:154` (§12): row 1 neutral-map, row 2 flat-earth, row 3 portolan accuracy, row 4 primitive-map/indigenous, row 5 map = territory — all present | keep the five; the bank has 14 rows, so the cut may compress, not delete these five |

**Result:** 11/11 promises have a live anchor in the r47 bytes. Nothing in the topic is unsupported *in the r47 draft*; the risk is that the right-sized r48 cut silently drops an element the topic still promises. F3 records that as a landing condition rather than a passed check.

---

## 5. README-row mechanics — the guard works

The sweep does not compare prose; it compares the entry's own `- topic:` field to the README row text after normalizing line continuations (`reports/round-28/readme/sweep.py:60-61`, `:74-80`) and reports a mismatch when they differ (`:139-146`). I exercised those functions directly on a scratch pair (no in-tree writes):

```
topic_of(temp entry) == seed topic            -> True
README row chars                              -> 766  (row prefix adds 35)
parsed row text == topic_of(entry)            -> True
control: delete "and a claim for fictional cultures" from the row
  -> mismatch detected                        -> True
```

The full README row for this topic is therefore **801 chars**, sha256 `2ff3050862ed6b8487e8bbb69e6e214eaa6936731570ad74e01a429ffd6d9e2c` (`- \`cartography-and-mapmaking.md\` — ` + topic text). The topic is one physical line, so no continuation-joining subtlety applies. C09's 766-char/`bc7274f4…` pin is the right thing to pin; the 801-char row digest is what the staged sweep should see.

---

## 6. Findings

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| **F1** | P3 (wording) | `reports/round-48/cov/C02-header.md:109` calls `9424fb81…` "sha256 of the seed line". That digest is the line **plus its `\n`**; the naked line is `a42926b1…` and the topic text is `bc7274f4…`. The value is true, the convention is unstated. | No byte change required. In the landing wire, state "line including terminator"; the README-row generator should pin the **topic text** digest `bc7274f4…` (as C09 already does), because that is what the sweep compares. |
| **F2** | P3 (non-blocking) | The topic line does not literally say "register" or name the slot; the slot is named at `C02:115` (`- gap filled:`) and `C01:109` (body §2). A literal reading of my mission's "names the register slot" is therefore only partly met by the topic field itself. | **Do not amend.** An amendment (prepending "the cartographic register: ") makes the topic 793 chars and the row 828 chars, breaks the seed byte-equality measured since r44/r47, and forces C09's row and every staged-sweep prediction to be regenerated. The slot is named in the head block one field below; that is visible and sufficient. Recorded so the integrator decides with the cost stated. |
| **F3** | P2 (landing condition) | No assembled r48 body existed at my cut (only the head block and an example fragment). The topic is an 11-promise contract (§4); byte-equality with the seed proves the *text*, not that the right-sized body keeps what the text promises. | Before apply: re-run the §4 ledger against the assembled entry; any missing promise means either restore it or (only if the integrator accepts the cost) revise the topic **and regenerate the README row**. The sweep cannot catch this class — it checks row↔topic equality, not topic↔body coverage. |
| **F4** | P3 (consistency) | The topic's four-stage chain ("survey → projection → drawing → reproduction") compresses the body's seven-link chain (`C02:41-55`: select → measure → control → reduce → project → symbolize → reproduce). | Consistent as a summary; the mapping is stated in §4 row 1. No change. |
| **F5** | P2 (inherited body risk) | Two promises are currently supported by defective bytes: "NON-CANON worked example" (R03 **B7**: three incompatible update rules at `C03:123`, `:137`, `:150`) and the eight-form promise (R03 **B9**: minimum-build table covers 5/8). | The r48 body must fix B7/B9 or the topic promise reads stronger than the entry delivers. This is a content obligation on C01/C03/C14, not a topic-line defect. |
| **F6** | P3 (h1 consistency) | r48's H1 changed from r47's "the map as an instrument and a claim" to "the map as an argument about space" (`reports/round-48/cov/C02-header.md:112`), matching the seed's master claim (§4.3). H1 is not byte-bound to anything. | No conflict with the topic; both name the same spine. No change. |

No finding touches the filed seed or r47 bytes; nothing was written outside this out path.

---

## 7. Verdict

- **Byte-equality to the r44 seed intent: PASS** — 766 chars, sha256 `bc7274f4…`, identical at `K02:227`, `C04:114` and `C02:114`; one physical line; the sweep's normalization yields the same text.
- **README-row equality mechanics: PASS** — the 801-char row parses to the topic text; a one-clause deletion is detected as a mismatch.
- **Register character (system/method, not generic map-file): PASS** — five-of-five register tests, and the negative test (no history/region narrative) holds.
- **"Names the register slot" in the topic field itself: PARTIAL** — the object class is named; the slot is named in `- gap filled:` and body §2 (F2). Non-blocking under the claim's own binding requirement (entry↔README equality), but the integrator should know the distinction, especially because the cartography charter is a disclaimer (negative naming), unlike the lapidary's positive naming in `symbolism-synthesis-method.md:29`.
- **Landing condition:** re-run §4 against the assembled right-sized entry; keep F3's promise ledger with the landing wire.

---

## 8. Reproduction commands (run from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`)

```
# write-cut snapshot (grows as seats file; no assembled entry body present)
$ find reports/round-48 -type f | sort
reports/round-48/adj/A03-write-surface.md
reports/round-48/claims.json
reports/round-48/cov/C02-header.md
reports/round-48/cov/C04-citations.md
reports/round-48/cov/M01-example.md
reports/round-48/cross/N01-numbers.md
reports/round-48/cross/X00-connector.md
reports/round-48/scribe/S03-shonen.md
reports/round-48/targets.json
reports/round-48/telemetry/dispatch-declared.json
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access ...: No such file or directory
$ grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr|survey map|world map|graticule|theodolite)' corpus/knowledge/ | wc -l
0

# topic extraction and hashes (seed / r47 / r48)
python3 - <<'PY'
import hashlib
seed = open('reports/round-44/scout/K02-gap-scout.md', encoding='utf-8').read().splitlines()[226]
assert seed.startswith('- topic: ')
t = seed[len('- topic:'):].strip()
print(len(t), hashlib.sha256(t.encode()).hexdigest())
print(hashlib.sha256(seed.encode()).hexdigest())        # naked line  a42926b1...
print(hashlib.sha256((seed+'\n').encode()).hexdigest()) # + newline   9424fb81...
for p in ('reports/round-47/cov/C04-entry-header.md', 'reports/round-48/cov/C02-header.md'):
    l = open(p, encoding='utf-8').read().splitlines()[113]
    print(p, l.strip() == seed.strip())
PY
766 bc7274f411cc6977032ab2754ebff19def4a1f5240fe5882624fc76e744f4495
a42926b1d0fe5ac5d608bb4ebd8e16873b3ed2f43a74c34392f0e4d5632496f8
9424fb81c22fe8c9a468d75aa291e1b5943a268b8699320915de52d7bda3459a
reports/round-47/cov/C04-entry-header.md True
reports/round-48/cov/C02-header.md True

# sweep parsers, exercised directly (scratch only)
topic_of(scratch entry) == seed topic                 -> True
README row chars                                      -> 766 (prefix adds 35)
parsed row == topic_of(entry)                         -> True
control (one clause deleted)                          -> mismatch True
```

Live anchors used above, re-read in this seat: `corpus/knowledge/myth-symbol/cosmology-cosmography.md:27` ("how the world is drawn (maps)…"), `:71` ("symbolic, not survey maps"), `:102` ("not cartographic"); `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:29` ("bestiary + lapidary + numerology + heraldic code"); `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:5` (the register-topic precedent); `reports/round-47/cov/C01-entry-a.md:109,163,171-177,184-187,214,234,238-249`; `reports/round-47/cov/C02-entry-b.md:41,149,218,299`; `reports/round-47/cov/C03-entry-c.md:73,84,107,154,189`; `reports/round-28/readme/sweep.py:60-61,74-80,139-146`.

## Owed

- `/none` for the topic field itself. The one open item is **F3**: the r48 assembled body did not exist at my cut, so the §4 promise ledger is `could-not-evaluate` against the final entry and must be re-run at landing. Owner: the integrator / C-claim scribe; command: the §4 ledger plus `python3 -B reports/round-28/readme/sweep.py` on the staged 224 tree.
- `to-verify`: the `9424fb81…` digest convention (line + newline) — state it in the landing wire rather than re-pin the hash.
