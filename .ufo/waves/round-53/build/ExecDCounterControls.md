# ExecDCounterControls — claim D counter controls and separability probe (round 53)

- Seat: `KotodamaR53.ExecDCounterControls` (executor, leaf; no delegation, no background job, no labrat spawned)
- Date: 2026-10-22
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (branch main, jj-colocated). **No lane file was edited except this report.** No jj command was run anywhere; no git write command (`add`, `commit`, `stash`, `checkout`, `switch`, `reset`, `pull`, `push`) was run in the lane. The lane's `git status --porcelain` shows only untracked artefacts other seats created (`corpus/lessons/round-53.md`, `tools/check-draft-ids.py`, `reports/round-53/clauses.py`, `reports/round-53/final-measures.py`, `.ufo/waves/round-53/`); `git diff --stat` is empty, so no tracked lane file was modified by any seat at the time I checked.
- Sandbox: `/fast/scratch/hyaku/kotodama-r53/ExecDCounterControls`, a private `git clone --shared` checked out at the declaration `60f1d2a3d832b926e37f82b11c67496d131a1431`. All controls ran inside it.
- Judged axis: depth.
- Assigned item: instrument controls (red-before receipts) for claim D's counting/acceptance command `python3 -B reports/round-53/d-count.py`, plus the separability checker `python3 -B tools/check-claim-separability.py reports/round-53/separability-manifest.json` over a repaired copy plus a synthetic C landing.

---

## 1. Axes named

| axis | state | evidence |
|---|---|---|
| depth | the counter's own semantics were mapped to its source strings, not just to its counts: eleven defects probed (one per routed instance class), plus eleven adversarial probes on the regexes' boundaries, plus four on the separability checker's dynamic leg | §3–§7 |
| calibration | every routed instance was re-checked against the re-opened page, not against the closure's wording; two of the closure's premises did not survive the re-open | §8 |
| operability | the counter is a substring instrument with six distinct lexical forms and a case-sensitive, pipe-aware, table-blind set of boundaries; each is named with the exact failing form | §5, §6 |
| coverage | the repair's own groundings were verified from the opened pages (7 external sources re-opened this session) | §8 |

No axis was harmed: no lane file was touched, no gate was weakened, no control was deleted.

---

## 2. Sandbox and the baseline

```
git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin \
    /fast/scratch/hyaku/kotodama-r53/ExecDCounterControls
git -C /fast/scratch/hyaku/kotodama-r53/ExecDCounterControls checkout -q \
    60f1d2a3d832b926e37f82b11c67496d131a1431
```

The entry file is byte-identical at the claim base and at the declaration commit, so the declaration tree is a valid stand-in for base:

```
$ git diff --stat a9cf95fe47a82b516f6c2487cb76b89c3a71c493 \
      60f1d2a3d832b926e37f82b11c67496d131a1431 \
      -- corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md
(empty)
$ git show a9cf95fe...:corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md | md5sum
65fb68dccb6f6968caaaeebe62c28326
$ md5sum corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md
65fb68dccb6f6968caaaeebe62c28326
```

**Base measurement** — argv `python3 -B reports/round-53/d-count.py`, cwd = sandbox root:

```
OPEN 18
  OVER1 corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:54
  OVER2 corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:54
  OVER3 corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:76
  OVER4 corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:79
  FRAG corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:106 ', -6'
  FRAG corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:107 ', -6'
  FRAG corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:113 ', -4'
  OVER5 corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:121
  FRAG corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:174 ', -5'
  OVER6 corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:176
  FRAG corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:177 ', -5'
  FRAG corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:177 ', -6'
  FRAG corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:177 ', -7'
  FRAG corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:179 ', -12'
  FRAG corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:181 ', -2'
  FRAG corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:181 ', -12'
  WROW1 corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:[106] 'working their farms' not cited to S162
  WROW2 corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:[113] mobile-phone decline not cited to S159 alone
SID_BAD 0 [] cited 50
exit 1
```

**OPEN 18, SID_BAD 0, exit 1 — exactly as the assignment expects.** The 18 decompose as 10 FRAG + 6 OVER + 2 WROW, and the 10 FRAG sit on 7 distinct lines (106, 107, 113, 174, 177×3, 179, 181×2). Re-running the same argv against a base-commit tree (`--root /tmp/baseroot`, built from `git show a9cf95f:…`) reproduces OPEN 18 / SID_BAD 0 / exit 1 identically.

The declaration dry-run receipt at `reports/round-53/telemetry/declaration-dry-run.txt` carries the same OPEN 18 / SID_BAD 0 / exit 1 for the same argv, and `python3 -B reports/round-53/dry-run.py check reports/round-53/telemetry/declaration-dry-run.txt` prints `MISSING_FROM_RECEIPT []` / `UNDECLARED_IN_RECEIPT []`, exit 0 — the red-before receipt is two-way consistent with the declarations.

---

## 3. The required controls (a)–(g)

Each control is a copy of the entry inside the sandbox, run through the counter's own `--root` argument. The repaired copy (a) is built by `controls/build_controls.py`; the drivers are `controls/run_controls.py`, `controls/run_g_controls.py`, `controls/run_extra_probes.py`, `controls/run_coverage_probes.py`, `controls/run_gap_probes.py`, `controls/run_form_probes.py`, `controls/run_s187_probes.py`, `controls/run_sep_s187.py`, `controls/run_export_gap.py`, `controls/run_s300_probe.py`, `controls/run_repair_options.py`, `controls/run_s163_rehome.py`. All stdout is saved beside them (`controls/*-output.txt`).

### (a) The hand-made repaired copy

Repairs applied, each traced to a re-opened page (§8) and each mapping a draft-id to the registered row the round-52 seat's own draft table assigns to it:

| line | base | repaired | ground |
|---|---|---|---|
| 54 | `two tones (Suruí) force fixed formulas (S135)` | `two tones (Suruí) make whistled sentences more formulaic and therefore more predictable (S135)` | S135 p. 7 |
| 54 | `Hmong (Laos, Thailand, United States) (S135)` | `Hmong (S135)` | S135 p. 4, p. 7 |
| 76 | `lip-locked /p/, /b/ merging with /k/ in the whistle (S147)` | `lip-locked /p/ similar to /k/ in the whistle (S147)` | S147 p. 837 |
| 79 | `the archive deposit was made with children of the village, so the register is learned young (S151)` | `the archive deposit was made with children of the village (S151)` | MPI deposit description |
| 106 | `(S159, -6)` | `(S159, S162)` | S162 p. 151 |
| 107 | `(S160, -6)` | `(S160, S162)` | S162 p. 148 |
| 113 | `(S163, -4)` | `(S159)` | S159 `teaches` |
| 121 | `in Akan (Ghana) practice a master drummer is` | `in one Akan (Ghana) case a master drummer is` | S165 `teaches` |
| 174 | `(S179, -5)` | `(S179, S174)` | S174 `teaches` |
| 176 | `senses frame non-Western people as "natives of a jungle"/"primitive peoples", S181)` | `its senses frame non-Western people with the idiom's own colonial wording, S181)` | S181 `teaches` |
| 177 | `(S179, -5, -6, -7)` | `(S179, S174, S176, S175)` | S174, S176, S175 `teaches` |
| 179 | `S183, -12)` | `S183, S180)` | S180 `teaches` |
| 181 | `(S173, -2)` | `(S173, S157)` | S157 `teaches` |
| 181 | `(S173, -12)` | `(S173, S180)` | S180 `teaches` |

The ten draft-id → S-id mappings are not guesses: each is read off the round-52 seat's own draft-id table, which lists the source of every `NEW-<Seat>-<n>` placeholder. `ScribeSec08Ecology.md` gives `NEW-ScribeSec08Ecology-4` = UNESCO nomination form 00658 (→ S159) and `-6` = Cloarec-Heiss 1999 (→ S162); `ScribeSec14Calibration.md` gives `-4` = Akinbo (→ S179), `-5` = McPherson (→ S174), `-6` = Gleick (→ S176), `-7` = TIME 1942/Good (→ S175), `-2` = UNESCO element 00172 (→ S157), `-12` = Meyer CNRS 2017 (→ S180). The round-52 closure independently lists the same target set at `corpus/lessons/round-52-verifier-spotcheck.md:73`: "All but the line-104 one map to registered rows (S162, S159, S174, S175, S176, S157, S180)".

```
$ python3 -B reports/round-53/d-count.py --root controls/a
OPEN 0
SID_BAD 0 [] cited 49
exit 0
```

**OPEN 0, SID_BAD 0, exit 0 — as expected.** Cited set falls from 50 to 49 because S163 is dropped from line 113; no S-id is added that was not already in the registry.

### (b) One fragment restored

```
$ python3 -B reports/round-53/d-count.py --root controls/b
OPEN 1
  FRAG corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:107 ', -6'
SID_BAD 0 [] cited 49
exit 1
```

**OPEN 1, exit 1 — as expected.** The counter counts the fragment on the line, once per token.

### (c) Line 113 citing S163 again

```
$ python3 -B reports/round-53/d-count.py --root controls/c
OPEN 1
  WROW2 corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:[113] mobile-phone decline not cited to S159 alone
SID_BAD 0 [] cited 50
exit 1
```

**OPEN 1 (WROW2), exit 1 — as expected.** WROW2 fires even though S159 is still present on the line: the leg reads "cites S159 **or** still cites S163", so adding S163 back while keeping S159 is caught.

### (d) Line 106 deleted

```
$ python3 -B reports/round-53/d-count.py --root controls/d
OPEN 1
  WROW1 corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:absent 'working their farms' not cited to S162
SID_BAD 0 [] cited 49
exit 1
```

**OPEN 1 (WROW1, `absent`), exit 1 — as expected.** Note the WROW1 leg is *absence*-sensitive, not just mis-citation-sensitive: deleting the row trips it. The repair cannot silence WROW1 by deleting the sentence it guards.

### (e) Citing S187

```
$ python3 -B reports/round-53/d-count.py --root controls/e
OPEN 0
SID_BAD 1 ['S187'] cited 50
exit 1
```

**SID_BAD 1, exit 1 — as expected.** Note OPEN is 0: the S187 citation is not one of the routed instances, so it is invisible to the OPEN figure and visible only to the SID_BAD figure.

### (f) `'force fixed formulas'` restored inside a code span

```
$ python3 -B reports/round-53/d-count.py --root controls/f
OPEN 1
  OVER1 corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:54
SID_BAD 0 [] cited 49
exit 1
```

**Result: OVER1 still fires — the counter is formatting-blind.** The regex `re.compile(r"force fixed formulas")` is a plain substring match; backticks do not shield it. A repair that quotes the banned phrase in order to *explain* the over-read (e.g. "the phrase `force fixed formulas` is not what the source says") is counted as still-open. This is the fail-closed direction, and it is the correct direction for a gate, but the landing seat must know it: the routed phrase must be **gone**, not merely quoted.

### (g) The separability checker, with a repaired D plus a minimal synthetic C landing

The g-lane is a copy of the sandbox at the declaration commit, carrying: the repaired entry (a), a minimal synthetic `corpus/knowledge/linguistics/gesture-co-speech-pointing.md` citing one S-id, a README index row for it with the counts footer moved to 229, an S187 registry row (`status` `mined`, `used-by` naming the gesture entry), and the two REC land paths the manifest declares but the checkout does not contain (`corpus/lessons/round-53.md`, `tools/check-draft-ids.py`).

```
$ python3 -B tools/check-claim-separability.py reports/round-53/separability-manifest.json
SEPARABILITY: 0 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=2
exit 0
```

**0 findings, exit 0.** The two acceptance runs are D's `d-count.py` and C's `accept-c.py`, each executed on a counterfactual tree built from base plus that unit's own lands; each passed alone, so neither claim's acceptance depends on the other's lands. Supporting measurements in the same lane:

```
$ python3 -B reports/round-53/accept-c.py
COUNT PASS knowledge_files=229 required=229
ENTRY PASS corpus/knowledge/linguistics/gesture-co-speech-pointing.md
SWEEP PASS exit=0 rows 229 files 229 missing_from_index 0 []
SIDS PASS cited=1 bad=[]
exit 0

$ python3 -B reports/round-28/readme/sweep.py
rows 229 files 229
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 229 totals_ok True
footer_findings [] footer_ok True
exit 0

$ python3 -B reports/round-53/d-count.py
OPEN 0
SID_BAD 0 [] cited 49
exit 0
```

The sweep exits 0 **on its own** with the README row present, which is what routed defect 2 of the round-52 closure asked for ("Gate on the sweep's own exit status … not on a piped `grep`"). The lane's own source-access gate stays clean in the same tree (`python3 -B tools/check-source-access.py` → `ACCESS: 2 flagged rows, 0 findings`, exit 0).

---

## 4. Controls showing the checker can fail (red-before receipts for the instrument itself)

A checker that cannot fail proves nothing. Four controls in the g-lane:

| control | mutation | checker output | exit |
|---|---|---|---|
| g-neg | D's repair reverted to the base entry | `SEPARABILITY_DEPENDENCY D-><base> via acceptance ['python3', '-B', 'reports/round-53/d-count.py'] fails on base+D.lands (rc=1) and no declared unit's lands repairs it` — 1 finding | 1 |
| g-pos | D's entry names C's new land path | `SEPARABILITY_DEPENDENCY D->C via land path 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md' named at corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:9` — 1 finding | 1 |
| g-partial | C's lands present but the two REC lands absent | `SEPARABILITY_INPUT_ERROR unit REC lands 'corpus/lessons/round-53.md', which is absent from the worktree` | 2 |

The g-neg control is the important one: with D unrepaired, the checker names D's own acceptance as the thing that fails and reports that no other unit's lands repair it. The instrument is live in both directions.

---

## 5. What the counter actually measures (adversarial probes)

The counter is a **string instrument**, not a semantic one. Eleven probes, each a one-token change to the repaired copy, with the counter's whole output recorded. Every one of these reads **OPEN 0 / exit 0** on a copy that still carries the routed defect in a different spelling:

| probe | defect still present, but spelled | counter |
|---|---|---|
| r1 | `, -6` — the base fragment form | OPEN 1 (FRAG), exit 1 |
| r2 | `(S160,-6)` — no space after the comma | **OPEN 0, exit 0** |
| r3 | `(S160 -6)` — no comma | **OPEN 0, exit 0** |
| r4 | `(S160, - 6)` — space after the hyphen | **OPEN 0, exit 0** |
| r5 | `(S160 (-6))` — bare parenthesised draft-id | **OPEN 0, exit 0** |
| q1 | `the register is transmitted young` (OVER4's inference, in S151's own registry wording) | **OPEN 0, exit 0** |
| q2 | `Force fixed formulas` — capitalised | **OPEN 0, exit 0** |
| q3 | `(S179, -06)` — zero-padded draft-id | OPEN 1 (FRAG), exit 1 |
| q4 | `Hmong (Laos, Thailand, United States) (S135; S140)` — the country list still attributed to S135, but with a second id after it | **OPEN 0, exit 0** |
| w1 | the country list **kept and re-cited** to the rows that carry it: `Hmong (Laos, Thailand, United States) (S135; S140; S141)` | OPEN 0, exit 0 |
| w2 | `/b/ | merging with /k/` — the OVER3 phrase split across a table-cell boundary | **OPEN 0, exit 0** |

And the two legs that are *not* substring matches:

- **WROW1 / WROW2 are row-presence checks, not citation checks.** They test whether a specific S-id appears *anywhere on the line* that carries the guarded phrase. Control (c) proved WROW2 fires on an *additional* wrong id on the line; control (d) proved WROW1 fires on the row's *deletion*. A repair that keeps "working their farms" and adds S162 anywhere on that line passes, whether or not the sentence is still attributed to S162.
- **SID_BAD is a registry-consistency check, not a range check.** It reads `corpus/SOURCES.md`, takes each `S###` the entry cites, and flags any id whose row's `used-by` cell does not name the entry. It has no notion of "S187 and above". Probe s1 (an S187 row naming **both** the gesture entry and the speech entry) and s2 (an S199 row naming the speech entry) both read **SID_BAD 0 / exit 0**; probe v1 (an S300 row naming the speech entry) also reads **SID_BAD 0 / exit 0**. So the counter alone does **not** enforce claim D's `must_not_cite: any S-id from S187 upward`.

That clause is enforced elsewhere — by the separability manifest's static export leg, which carries the regex `\bS(18[7-9]|19[0-9]|2[0-9][0-9])\b` on claim C. Probes t1/t2 (D citing S187 and S199) and u1/u2 (S187 and S299) each produce `SEPARABILITY_DEPENDENCY D->C via export '\bS(18[7-9]|19[0-9]|2[0-9][0-9])\b' matched …:113` and exit 1. **But u3 (S300) and u4 (S999) produce no export finding**: the regex tops out at S299. Probe v2 shows D citing S300 is caught only incidentally, because the S300 row then makes D's *acceptance* depend on C's lands (`D->C via acceptance … fails on base+D.lands and passes on base+D.lands+C.lands`) — the dependency is reported for the wrong reason, and it disappears the moment the registry row lands on D's side. **The export regex has a gap at S300 and above.** I flag it; the fix belongs to whoever writes the manifest, not to me.

### The counter's blind spots, stated plainly

1. **The FRAG regex is form-bound.** `, -[0-9]+\b` needs comma, space, hyphen, digits. Any other spelling of a draft-id — `(S160,-6)`, `(S160 -6)`, `(S160, - 6)`, `(-6)` — is invisible (r2–r5). The routed defect says "replace all 11 `, -N` draft-id fragments"; a repairer who reformats a citation while re-citing it can leave a live draft-id behind and the counter will read 0. **This is the most likely way the landed D could read 0 while still carrying a fragment.** The round-52 closure's own grep used the same regex, so its count of 11 has the same blind spot.
2. **The OVER legs are exact-phrase and case-sensitive.** OVER1 needs the literal `force fixed formulas`; `Force fixed formulas` passes (q2). OVER3 needs `/b/` and `merg…with /k/` on one line segment without a `|` between them; the same claim split across a table cell passes (w2). OVER4 needs the literal `learned young`; `transmitted young` — which is S151's **own registry wording** — passes (q1).
3. **The counter measures removal, not re-grounding.** A repaired line passes when the routed wording is gone. Whether the replacement is *supported* is not checked by any leg, and cannot be: the counter never opens a source. Probes q1 and q4 are the demonstration — both pass while the entry still makes the routed claim in a synonym and still attributes the country list to a row that does not carry it.

---

## 6. Registry bookkeeping the repair creates

Two facts the landing seat needs, both measured:

1. **Dropping S163 from line 113 leaves S163's `used-by` cell pointing at an entry that no longer cites it.** Control x1: after the repair the entry cites S163 **0 times** (`cited 49`), while `corpus/SOURCES.md`'s S163 row still reads `used-by = corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`. **No lane gate catches this**: the counter only checks the forward direction (cited → row names the entry), and the two tools that read `used-by` (`tools/check-claim-separability.py`, `tools/check-source-access.py`) do not check the reverse direction either. Control x2 shows the clean alternative: re-home S163 onto the living-practice flag line (`inscribed 2017 on the Urgent Safeguarding List, S183, S163, S180`), where S163's own `teaches` cell ("Inscribed in 2017 (12.COM) … decline in the number of practitioners and in the area where the practice is used") actually supports the claim — the counter reads **OPEN 0 / SID_BAD 0 / cited 50 / exit 0**, and the registry stays consistent. **Recommend x2 over the plain drop.**
2. **The entry's cited set after the repair is 49 ids, all of them rows whose `used-by` names the entry.** I checked each of S157, S159, S160, S162, S163, S173, S174, S175, S176, S179, S180, S181, S183 in `corpus/SOURCES.md`: every one is `status = mined` and `used-by = corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`. The repair introduces no new registry row and no new id.

---

## 7. Sources re-opened this session (2026-10-22), for the six over-reads

Every source below was fetched by ordinary means — plain `curl` with a browser User-Agent, plus `pdftotext`. No headless browser, no captcha solved, no paywall or login bypass, no access control routed around. Where a live page served a bot challenge I used a public archive capture and say so.

| id | URL | route | quote (≤25 words) and location | what it settles |
|---|---|---|---|---|
| S135 | `http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf` | live, plain request, HTTP 200, 1 439 365 B, 10 PDF pages | "in tonal languages with low informational load on spoken pitch, whistled sentences are more formulaic and therefore more predictable" — PDF p. 7 (printed p. 7), §"Body Text" | OVER1's wording; the closure's correction is exact |
| S135 | same | live | "Hmong, Akha" — PDF p. 4 (printed p. 4), the tonal-language table; "this informational load is much higher in Hmong (seven to eight contour tones, depending on the dialect) than in Suruí (two level tones)" — PDF p. 7 | OVER2: S135 names Hmong but **never lists** Laos, Thailand, United States |
| S147 | `http://www.icphs2007.de/conference/Papers/1286/1286.pdf` | live, plain request, HTTP 200, 337 860 B | "labial articulation of [m], [p] and [b] which all use in compensation a glottal occlusion to produce a stop" and "The occlusive [p] is expressed mainly with this process and is therefore very similar to [k] in whistles" — PDF p. 3 (printed p. 837), §3 "CONSONANTS" | OVER3: the [p]/[k] similarity is stated for **[p]**; [b] is named among "intermediate positions between two of these categories, like [n], [b], [v] and [f]" |
| S151 | `https://archive.mpi.nl/tla/islandora/object/lat:1839_00_0000_0000_0016_B509_0` | live, plain request, HTTP 200 | "David Yetman and Mark Sicoli elicit spoken and whistled Chinantec from children in San Pedro Sochiápam" — Description block | OVER4: the deposit records *that* children produced the material, not a transmission claim |
| S162 | `https://regroupement-rcms.org/wp-content/uploads/2016/08/Article-F.Cloarec-Heiss.pdf` | live, plain request, HTTP 200, 4 410 976 B | "indicate messages sent by the village chief to all people who are somewhere outside the village (working their farms, hunting, or gathering)" — printed p. 151; "accidents (e.g., on hunting expeditions or when someone gets lost in the bush)" — printed p. 148 | WROW1: "working their farms" is in S162; line 107's fragment is also S162 |
| S159 | `corpus/SOURCES.md` row S159 (UNESCO nomination form 00658) | already registered | `teaches`: "mobile phones named as the main threat" | WROW2: the mobile-phone decline is S159's, not S163's |
| S165 | `corpus/SOURCES.md` row S165 (Brown University) | already registered | `teaches`: "the page supports the appointment and the course, not the wider Akan institution" | OVER5: one drummer's biography is not "Akan practice" |
| S181 | `https://www.dictionary.com/browse/bush-telegraph` | live, plain request, HTTP 200, 72 425 B | "any system of communication in which the natives of a jungle or bush region transmit news rapidly, as by runners, drum codes, or smoke signals" (Random House Unabridged sense); "a means of communication between primitive peoples over large areas, as by drum beats" (Collins sense); "First recorded in 1875–80" | OVER6: **see §8** |
| S180 | `corpus/SOURCES.md` row S180 (Meyer CNRS 2017) | already registered | `teaches`: "2017 figure >70 languages" | the `-12` fragments on lines 179 and 181 |

---

## 8. Two closure premises that did not survive the re-open

This is the part I most want the L1 to see, because it changes what the repair should say.

**Premise 1 — OVER6.** `corpus/lessons/round-52-verifier-spotcheck.md:81` reads: "line 176: the sub-quote "primitive peoples" is not on S181's page." **It is on the page.** I fetched the live Dictionary.com entry on 2026-10-22 and the Collins sense reads, verbatim: "a means of communication between primitive peoples over large areas, as by drum beats". The public archive capture of the same URL carries the identical string in its preloaded state ("…\"text\":\"a means of communication between primitive peoples over large areas, as by drum beats\"…"), and the registry's own S181 `anchor` cell already quotes that Collins sense word for word. So the sub-quote is on the page, in the registry, and in the archive.

What *is* wrong on line 176 is the **presentation**: the entry fuses two different senses into one slash-joined pseudo-quotation, `"natives of a jungle"/"primitive peoples"`, inside one pair of quote marks, as though a single source said both. The Random House sense says "the natives of a jungle **or bush region** transmit news rapidly" — a clause about *transmitting news*, not about framing people; the Collins sense says "between primitive peoples". Splicing them produces a sentence the page does not carry, which is a real defect, but it is a **quotation-fusion** defect, not a "the phrase is not on the page" defect. My repaired copy (a) therefore paraphrases the sense ("its senses frame non-Western people with the idiom's own colonial wording") instead of deleting a phrase the page does carry. Control h confirms the consequence: a copy that quotes the Collins sense **accurately and correctly attributed** — `"natives of a jungle" (Random House sense) and "primitive peoples" (Collins sense)` — still reads **OPEN 1 / OVER6 / exit 1**. The counter bans the string, so a *faithful* quotation cannot pass. The landing seat must choose deliberately between paraphrasing (passes, loses the quotation) and quoting accurately (fails the counter). I recommend paraphrasing and, if the quotation is wanted, also correcting the S181 row's `teaches` cell, which repeats the fused form: `senses carry "natives of a jungle"/"primitive peoples" wording`.

**Premise 2 — OVER2.** The closure's correction at `:77` is "Hmong '(Laos, Thailand, United States)', which S135 does not list", and it is right that S135 does not list the countries. But the closure's routed instruction at `:136` says to "soften or re-source" the over-reads, and the counter's OVER2 regex fires on the exact string `(Laos, Thailand, United States) \(S135\)` — so the cheapest fix is to delete the country list. **The list is not unsupportable; it is supported by another registered row.** S141 (Morrison 1998, *The Hmong Qeej*, opened this session from `https://www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf`, HTTP 200, 17 pages) carries both: "In current times, in Laos and Thailand, interested boys who are eight to ten years old begin to learn the note-fingering of the qeej" (printed p. 7 of 17) and "Hmong men continue to learn the qeej in the United States, no one here is studying to become a qeej master" (printed p. 9 of 17). S140 (McPherson, *Documenting musical surrogate languages*) also treats Hmong communities, though its own `teaches` cell does not name the countries. **Control w1 shows the re-sourcing repair also reads OPEN 0 / exit 0**: `Hmong (Laos, Thailand, United States) (S135; S140; S141)`. Keeping the country list and re-citing it is the better repair — it preserves the entry's information and adds no new registry row, since S140 and S141 are already registered and already name this entry in `used-by`. But note that the counter cannot *require* this: probe q4 shows `Hmong (Laos, Thailand, United States) (S135; S140)` — the same country list still attributed to S135 — also reads OPEN 0. The counter measures the string, not the attribution.

**One more, not a closure premise but a live erratum.** The S135 registry row's `anchor` cell reads `Abstract and "Body Text", PDF pp. 1–2 of 17`. The PDF at the registered URL has **10** pages, not 17, and the OVER1 sentence ("more formulaic and therefore more predictable") is on **PDF p. 7**, well outside the cited pp. 1–2. The `teaches` cell does not mention the formulaic/predictable claim at all. So the row that OVER1 must be re-grounded on is anchored to pages that do not carry the sentence, and its `teaches` cell carries no claim that the re-grounding needs. That is a registry defect the counter cannot see (it checks only that S135's `used-by` names the entry) and that the round-52 closure did not route, because the closure audited the entry's citations, not the rows' own anchors. I flag it as a routed-adjacent erratum for the gate-text wave; it sits in `corpus/SOURCES.md`, which is **not** claim D's land, so I have not touched it.

---

## 9. Evidence index

| fact | where |
|---|---|
| base = OPEN 18, SID_BAD 0, exit 1 | `python3 -B reports/round-53/d-count.py` in the sandbox at `60f1d2a3…`; reproduced at base `a9cf95f…` via `--root /tmp/baseroot` |
| entry identical at base and declaration | `git diff --stat a9cf95f 60f1d2a -- corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` (empty); md5 `65fb68dccb6f6968caaaeebe62c28326` both sides |
| the 10 fragments sit on 7 lines | `grep -n -o -E ', -[0-9]+\b' corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` → lines 106, 107, 113, 174, 177×3, 179, 181×2 |
| routed defect list | `corpus/lessons/round-52-verifier-spotcheck.md:71-83` (defects) and `:130-136` (routed items) |
| draft-id → S-id mapping | `.ufo/waves/round-52/build/ScribeSec08Ecology.md` §4 (registry row drafts) and `.ufo/waves/round-52/build/ScribeSec14Calibration.md` §2; independently corroborated at `corpus/lessons/round-52-verifier-spotcheck.md:73` |
| the closure's own list of the mapped rows | `corpus/lessons/round-52-verifier-spotcheck.md:73` |
| OVER6 premise refuted | live `https://www.dictionary.com/browse/bush-telegraph` HTTP 200, Collins sense; and the Wayback copy of the same URL, `window.__PRELOADED_STATE__` |
| OVER2's country list supported elsewhere | S141 PDF printed p. 7 and p. 9 of 17, `https://www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf` |
| S135's anchor page range is wrong | `corpus/SOURCES.md` S135 `anchor` cell vs. `pdfinfo` on the registered URL: 10 pages, quote on PDF p. 7 |
| separability checker green with a repaired D and a synthetic C | `python3 -B tools/check-claim-separability.py reports/round-53/separability-manifest.json` in `controls/g-lane` → `SEPARABILITY: 0 findings`, exit 0 |
| checker can fail | `controls/g-neg` (D unrepaired → 1 finding), `controls/g-pos` (land-path back-reference → 1 finding), `controls/g-partial` (absent REC land → exit 2) |
| export-regex gap at S300+ | `controls/u3`, `controls/u4` |
| all driver scripts and their saved stdout | `/fast/scratch/hyaku/kotodama-r53/ExecDCounterControls/controls/` |
| red-before receipt consistency | `python3 -B reports/round-53/dry-run.py check reports/round-53/telemetry/declaration-dry-run.txt` → `MISSING_FROM_RECEIPT []`, `UNDECLARED_IN_RECEIPT []`, exit 0 |
| agreement | `python3 -B reports/round-53/claims-agree.py` → `AGREE claims=['C', 'D']`, exit 0 |

---

## 10. Checks I did not run

- **No lane file was edited except this report.** The landing of claim D — the actual repaired entry in `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`, and any `corpus/SOURCES.md` edit that follows from it — is the L1's and the landing seat's work, not mine. Everything I measured ran on copies inside the sandbox.
- I did not run the lane's full gate battery, the source census (`scripts/sources-census.sh`, which this checkout does not contain — `scripts/` is absent here), the round-28 sweep over the real lane tree, or any lint, formatter, build or test suite. The sweep and the source-access gate were run inside the g-lane only, where they exit 0.
- I did not verify the C claim's own entry text, the C claim's sources, or the round-53 lesson file. Those belong to the C seat and the record seat.
- I did not run `tools/check-draft-ids.py` — it is declared as a REC land path in the manifest but does not exist in the checkout; the separability checker exits 2 without it (control g-partial), and I supplied a placeholder in the g-lane only, to let the dynamic leg run.
- I did not run the counter against a *landed* D, because no D has landed.
- **No tool was installed or upgraded for this assignment.** The stock `git`, `curl`, `pdftotext`, `pdfinfo`, `python3` and `grep` on the host were sufficient; the tooling directive was read and no pacman transaction was run (host-wide pacman pause observed).

---

## 11. Result

Measured, no change to any lane file other than this report.

**The required controls all behaved as expected.** Base OPEN 18 / SID_BAD 0 / exit 1; (a) OPEN 0 / SID_BAD 0 / exit 0; (b) OPEN 1 (FRAG) / exit 1; (c) OPEN 1 (WROW2) / exit 1; (d) OPEN 1 (WROW1 `absent`) / exit 1; (e) SID_BAD 1 / exit 1; (f) OVER1 still fires inside a code span / exit 1 — the counter is formatting-blind; (g) the separability checker over a repaired D plus a synthetic C landing reads `SEPARABILITY: 0 findings`, exit 0, and the checker is shown able to fail in three separate ways.

**Ten findings the L1 should carry into the landing.**

1. **The FRAG leg is form-bound.** Only the literal `, -N` spelling is caught. `(S160,-6)`, `(S160 -6)`, `(S160, - 6)` and `(-6)` all read OPEN 0 while the draft-id is still there (r2–r5). **This is the most likely way a landed D reads 0 and still carries a fragment.** The round-52 closure's grep shares the blind spot, so its "11 tokens" count may under-count. The repair must be read as a re-citation task, not a regex sweep.
2. **The OVER legs are exact-phrase and case-sensitive**, so a synonym for the same over-read passes: `transmitted young` (OVER4's inference, in S151's own registry wording) and `Force fixed formulas` both read OPEN 0 (q1, q2).
3. **OVER3 can be evaded across a table-cell boundary** because the regex is `[^|]*`-bounded (w2).
4. **SID_BAD does not enforce claim D's `must_not_cite: any S-id from S187 upward`.** With a registry row naming the entry, S187, S199 and S300 all read SID_BAD 0 / exit 0 (s1, s2, v1). That clause rests entirely on the separability manifest's export regex.
5. **That export regex has a gap at S300 and above.** `\bS(18[7-9]|19[0-9]|2[0-9][0-9])\b` fires on S187, S199, S299 (t1, t2, u1, u2) and not on S300 or S999 (u3, u4). D citing S300 is then caught only as an acceptance dependency, and that finding vanishes once the registry row lands on D's side (v2). The manifest's regex should cover S300+.
6. **The counter measures removal, not re-grounding.** No leg opens a source; probes q1 and q4 pass while the routed claim survives in a synonym and while a country list stays attributed to a row that does not carry it. The claim's falsifier clause "a repaired line now states something its cited row's page does not carry" is a **review** obligation, not a counter obligation.
7. **OVER6's premise is wrong: "primitive peoples" IS on S181's page** (live and archived), and it is already in S181's `anchor` cell. The real defect is that line 176 fuses two senses into one slash-joined quotation. The counter bans the string, so a faithful, correctly attributed quotation cannot pass (control h). My repair paraphrases; the alternative is to also correct the S181 `teaches` cell, which repeats the fused form. **This is a `corpus/SOURCES.md` edit, outside claim D's land.**
8. **OVER2 should be re-sourced, not deleted.** The country list is carried by S141 (printed pp. 7 and 9 of 17). Control w1 shows `Hmong (Laos, Thailand, United States) (S135; S140; S141)` reads OPEN 0 / exit 0 and preserves the information using two rows that already exist and already name this entry. Note the counter cannot *require* this (q4).
9. **Dropping S163 leaves a dangling registry reference.** After the repair the entry cites S163 zero times while S163's `used-by` still names it, and no lane gate checks that direction. Control x2 shows the clean alternative — re-home S163 onto the living-practice flag line, where its `teaches` cell actually supports the claim — reads OPEN 0 / SID_BAD 0 / cited 50 / exit 0. **Recommend x2.**
10. **S135's registry `anchor` cell is wrong**: it reads `PDF pp. 1–2 of 17`; the PDF at the registered URL has 10 pages and the OVER1 sentence is on p. 7. The `teaches` cell carries no formulaic/predictable claim, so the row OVER1 must be re-grounded on is not anchored to the sentence it must carry. This is a `corpus/SOURCES.md` erratum for the gate-text wave, outside claim D's land.

**Risk carried to the L1:** the counter is a necessary, fail-closed-on-removal condition for claim D, and every routed instance class is caught in its canonical spelling. It is not sufficient for the claim's own falsifier, and four of its boundaries (FRAG spelling, OVER case, OVER pipe-boundary, SID_BAD range) admit a false pass on a copy that still carries the routed defect. The landed D must be reviewed line by line against the re-opened pages, and the counter's 0 must be read as "the routed wording is gone", not as "the routed defect is gone".

**Blockers:** none.
