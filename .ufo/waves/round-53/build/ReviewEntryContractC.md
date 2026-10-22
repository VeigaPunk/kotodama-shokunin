# ReviewEntryContractC — round 53, claim C: gesture-co-speech-pointing.md entry contract

- Seat: KotodamaR53.ReviewEntryContractC (leaf; no delegation, no background jobs).
- Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin, HEAD `60f1d2a3` (the declaration commit); read-only except this report.
- Contract source: `.ufo/waves/round-50/build/ReviewEntryContract.md` §2, applied to the round-53 models. Models re-read this session: `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` (195 lines) and `corpus/knowledge/linguistics/sign-languages-manual-modality.md` (224 lines).
- Not covered here (per assignment): README index-row mechanics (sweep row insertion, counts footer, revisions) — the README seat owns those; the sweep leg of `accept-c.py` is referenced only as an external dependency C's acceptance reads.

## 0. Result

The contract is fully derivable and every gate is runnable at the current tree. The two models carry the exact eight-field head in the same key order, numbered H2s ending Recheck→Scope, zero H3, and gate-clean provenance (`provenance-audit.py` on the speech-surrogates model: `findings=0`, exit 0). `DR-GES` has 0 hits in `corpus` and `reports` (grep this session), so the prefix is free. Pre-entry state verified: 228 knowledge files, linguistics 27, `gesture-co-speech-pointing.md` ABSENT, filename probes `*gestur*|*pointing*|*kinesic*` → 0. No blocker to drafting the entry.

## 1. Axes

| axis | state | evidence |
|---|---|---|
| coverage | checklist covers all seven assigned contract dimensions; each rule pinned to a model line or tool | §2 below |
| operability | every gate run live this session on a model entry; outputs quoted; two traps found (§2.10 S-id whole-file scan, §3 absent tool) | §2.7, §2.10, §3 |
| calibration | code vocabulary confirmed at `calibration-registry.md:35-39`; gate's `missing-calibration` shape satisfied by the planned `## 12. Calibration bank` heading | §2.5, §2.7 |

## 2. The checklist — what the L1 must pass for `corpus/knowledge/linguistics/gesture-co-speech-pointing.md`

### 2.1 Path and length

- Path exactly `corpus/knowledge/linguistics/gesture-co-speech-pointing.md`. Run `test ! -e <path>` before writing (never overwrite an existing entry; round-42 incident per the r50 contract §2.1). Verified ABSENT this session.
- `wc -l` ≤ **230** (the claim's hard cap; tighter than the r50 default of 250). Reference: the tightest model, sign-languages, is 224 lines with 15 H2s; the planned 14 sections must stay table-dense. `accept-c.py` has **no length leg** — this gate exists only as a manual `wc -l`, so it must not be skipped.

### 2.2 Head: eight fields, this exact key order, then blank line, then first H2

Required key sequence (both models comply, verified line-by-line): `topic, gap filled, sources, couples, source, verified-at, recheck, scope`. Note the singular `- source:` between `couples` and `verified-at` — the provenance gate ignores it, but the 8-field head requires it (r50 contract §2.3; conflict DR-1 in `header-conformance-readings.md` names a plural-only profile for new entries — the claim's 8-field head wins; escalation stays with the integrator).

1. `- topic: <one line>` — the register words for future freshness probes as whole words: gesture, co-speech, pointing, quotable, emblem, kinesic. Sweep's extractor is `TOPIC_RE = ^- topic:(.*?)(?=\n- \w)` with continuations space-joined (`reports/round-28/readme/sweep.py:61-70`), so a continuation line must never begin with `- ` + word character; keep it one line like both models. (Byte-equality with the README row is the README seat's check.)
2. `- gap filled:` — the two routed probes re-run **at landing**, at the pre-entry sha, each with its measured `→ **0**`: filename sweep `find corpus/knowledge -iname '*gestur*' -o -iname '*pointing*' -o -iname '*kinesic*'` and topic-line sweep `grep -rliE '^- topic:.*(gestur|pointing|kinesic)' corpus/knowledge`. State the sha they ran at explicitly (pre-entry), because the filename sweep matches the entry itself once it exists — the models do exactly this ("both run 2026-10-22 at `dea5ece`" / "on corpus bytes equal to base `bff83ba`"). Then the boundary sentences naming the routed partial owners with `path:line`, cited one-way: `culture-material/adornment-body-codes.md:77-93` (emblem taxonomy, Morris geography, proxemics, bow/wai, nod/shake, finger counting), `sign-languages-manual-modality.md:64,:161` (co-speech gesture as the manual modality's boundary row), `numerals-and-measures.md:107` (finger counting), `../myth-symbol/direction-symbolism.md:6,:36` (Guugu Yimithirr absolute directions, Haviland 1993 pointing). One-way: these entries are never restated, only cited.
3. `- sources:` — plural key, nested two-space block in house style. First bullet: in-corpus anchors as `` `path:line` `` re-read at the landing sha with date. Second bullet: external shelf opened this round (2026-10-22), registered as `corpus/SOURCES.md` rows **S187 upward** (ids as assigned at integration), each carrying URL, access date, tier scope and anchor in the registry; works not opened by ordinary means are cited only through opened rows that report them (the S186 pattern records "challenge met, not passed" for captcha pages). Placeholder-value trap: a `sources:` value that is only `none`/`tbd`/`(to-verify)` etc. counts as empty → gate finding (see §2.7).
4. `- couples:` — exactly one line, ends with a period. Each `;`-group starts with a partition label + em dash (labels: linguistics, myth-symbol, culture-material, civilizations, verification, synthesis). Cross-partition targets as `` `../<partition>/<file>.md` ``, same-directory as bare basename. Every `.md` token must resolve — verify with `python3 -B tools/harness/basename-couples-resolver.py <entry>`: every token `direct` or `fallback` with a path, zero unresolved/ambiguous (observed on the speech-surrogates model: 8 tokens, all resolved, exit 0). Expected shape for this entry: linguistics — sign-languages, numerals-and-measures, politeness/conlang-methodology as owned; culture-material — `../adornment-body-codes.md`; myth-symbol — `../direction-symbolism.md`; verification — `../calibration-registry.md`; lore-shokunin handoff.
5. `- source: lane-side authority is …` — singular line naming the in-corpus anchors and the S187+ rows, ending with one design-method sentence (model: sign-languages' "fix the community first, then the manual parameters, then the grammar in space").
6. `- verified-at: 2026-10-22 — …` — the sha actually measured (do not template a date; r50 DR-4), the measured counts: pre-entry `find corpus/knowledge -name '*.md' | wc -l` → **228**, `ls corpus/knowledge/linguistics/*.md | wc -l` → **27**; post-entry **229** and **28**; plus each command actually run → its value, and a `not claimed:` list.
7. `- recheck: before <trigger> — …` — trigger first, then the re-open list: re-run both gap sweeps before extending gesture material elsewhere; re-open each S-row before quoting a figure or a count; re-read `sign-languages-manual-modality.md:64` and `adornment-body-codes.md:77-93` before assigning a form to emblem, illustrator, or point.
8. `- scope: reference method and lane policy for the linguistics partition. This entry owns … It does not own … It decides nothing about any world …` — with the handoff sentence.

### 2.3 Headings

- Line 1: exactly one H1, `# <Title> — <subtitle>` with U+2014 em dash, one space each side (verified in the model by hexdump: `20 e2 80 94 20`). Line 2 blank.
- H2s: `## 1. …` through `## 14. …`, consecutive from 1, every H2 numbered, matching the planned section list (1 register property, 2 one-owner boundary, 3 gesture types, 4 pointing, 5 gesture in space and time, 6 language shapes gesture, 7 quotable gestures and emblem repertoires, 8 social control, 9 acquisition and learning, 10 decision table and build order, 11 NON-CANON worked example, 12 calibration bank, 13 recheck, 14 scope).
- Last H2 is `Scope` (title containing "Scope"); `Recheck` immediately precedes it (models: `## 11. Recheck`/`## 12. Scope` and `## 14. Recheck`/`## 15. Scope`).
- Zero `###` and zero `####` lines anywhere (both models: 0; verified by grep). Fold all sub-structure into tables and bold lead-ins.
- Every `§N` reference in the text must satisfy N ≤ 14.

### 2.4 Body shape and tables

- §1 register property: bold **Master claim.** paragraph, the load-bearing choices in order, and a three-column test table `| Test | Pass when | Fails as (owner) |` whose failures name owning neighbours with `path:line`.
- §2 one-owner boundary: one sentence, then `| Neighbour (anchor) | What it owns | This entry's boundary |` — at least the four routed partial owners plus the linguistics neighbours (politeness-taboo for hand/status etiquette, conlang-methodology for the pipeline, sociolinguistics-registers if etiquette registers are cited).
- Every domain section (§3–§9) carries at least one pipe table with a `|---|` separator row and a blank line before and after the table. Every factual claim cites `path:line`, an S-id, or carries `(to-verify)` inline at the dependency.
- §10: decision table `| If your culture… | then the gesture system needs… | and check |`, numbered build order with each step ending `*Artifact: …*`, and the decision-record table inside the same section (both models fold the DR table into their decision/build section).
- §11 begins `**NON-CANON.**` and states that culture, place and numbers are invented and canon belongs to lore-shokunin.
- §12 calibration bank (see §2.5) followed by bold **Living-practice flag** and **Precision traps** paragraphs (both models carry them immediately after the bank table).
- §14 Scope body must contain `Handoff: lore-shokunin owns …`.
- Forbidden anywhere, case-insensitive: TODO, TBD, placeholder, scaffold, MVP. No emoji. Plain English.

### 2.5 Calibration codes

- Status vocabulary is exactly the five codes of `corpus/knowledge/verification/calibration-registry.md:35-39`: **R** rejected/discredited as the specified general inference (never evidence; may portray as dated ideology or explicit fictional premise); **C** contested interpretation (preserve alternatives, never report one reading as settled); **B** bounded, usable within a named domain (carry population/genre/period/exceptions, no extrapolation by resemblance); **H** heuristic/designer framework (label the designer's choices, never present as discovery); **T** unresolved provenance — mark `(to-verify)` inline at the exact dependency and never make it load-bearing.
- The bank table is `| Claim | Status | What to say instead |`; each status verdict carries its reason and, where one exists, its registry row (models cite `../verification/calibration-registry.md:35-39` at the bank head and sprinkle CAL ids where apt).
- The gate only demands the word `calibrat*` somewhere; the planned `## 12. Calibration bank` H2 satisfies the strongest apparatus shape (`CALIB_HEADING_RE`), avoiding the softer `INFO calibration-prose-only` reading.

### 2.6 Decision record prefix

- IDs `DR-GES-01` upward in `| ID | Decision | Trigger | Failure if skipped |`. **`DR-GES` confirmed unused: grep for `DR-GES` over `corpus` and `reports` returned 0 matches this session.** Nearest existing prefixes are `DR-SRG-01..05` (speech-surrogates §8) and `DR-SGN-01..04` (sign-languages §11) — no collision. Use `DR-GES`, not `DR-GES-` variants of other registers, and reference the range in the Scope handoff like the models do ("DR-SRG-01 to DR-SRG-05").

### 2.7 Provenance gate expectations (`tools/gates/provenance-audit.py`)

Run: `python3 -B tools/gates/provenance-audit.py corpus/knowledge/linguistics/gesture-co-speech-pointing.md`. How to read it (semantics from the script docstring and constants, lines 1-96):

- **Expected result: exit 0, `findings=0`.** Observed on the speech-surrogates model this session: `INFO to-verify-count: …14 mark(s) on 13 line(s)` then `INFO scan: files=1 marks=14 mark-lines=13 findings=0 blocked=0`, exit 0. That is the pass shape: marks are inventory, never findings.
- Findings (each prints `FINDING <id>: <path>: <message>`, any one ⇒ exit 1), in gate order: `missing-topic`, `missing-sources`, `empty-sources`, `missing-couples`, `empty-couples`, `missing-calibration`. The gate checks **only** `- topic:`, `- sources:`, `- couples:` (FIELD_NAMES) and the calibration vocabulary; the other five head fields are enforced by §2.2/§2.9 of this checklist, not by this gate — passing the gate is necessary, not sufficient.
- Empty-value rule: a field value that is blank or only a placeholder (`none`, `n/a`, `tbd`, `todo`, `unknown`, `-`, `—`, `(to-verify)`, …) counts as empty → `empty-sources`/`empty-couples`. Field content includes indented continuation lines, so the house-style nested `sources:` block is read correctly.
- `missing-calibration` fires only when `calibrat*` is absent from the whole file; naming calibration only in running prose passes with `INFO calibration-prose-only` — acceptable but weaker than the §12 heading.
- `CANNOT-EVALUATE: <path>: <reason>` ⇒ exit 2 (unreadable, not UTF-8, or not an entry document). A finding list of zero and exit 0 is the landing condition; record the `INFO scan:` line verbatim in the round record.

### 2.8 Mechanical checker (run before landing; adapted from r50 §2.9-A)

```python
import re, pathlib
CANON = ['topic','gap filled','sources','couples','source','verified-at','recheck','scope']
REL = 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md'
text = pathlib.Path(REL).read_text(encoding='utf-8'); f = []
lines = text.rstrip('\n').split('\n')
if len(lines) > 230: f.append(f'length {len(lines)} > 230')
h1 = [l for l in lines if l.startswith('# ')]
if not (len(h1) == 1 and lines[0].startswith('# ') and ' \u2014 ' in lines[0]): f.append('H1')
if any(re.match(r'^#{3,} ', l) for l in lines): f.append('H3+ present')
h2 = [l for l in lines if l.startswith('## ')]
nums = [re.match(r'^## (\d+)\. ', l) for l in h2]
if any(m is None for m in nums) or [int(m.group(1)) for m in nums] != list(range(1, len(h2)+1)): f.append('H2 numbering')
if 'Scope' not in h2[-1]: f.append('last H2 not Scope')
if not any('Recheck' in l for l in h2): f.append('no Recheck H2')
first_h2 = next(i for i, l in enumerate(lines) if l.startswith('## '))
keys = [m.group(1) for l in lines[:first_h2] for m in [re.match(r'^- ([a-z][a-z \-]*?):', l)] if m]
if keys != CANON: f.append(f'head keys {keys}')
if not any(l.startswith('**NON-CANON') for l in lines): f.append('no NON-CANON')
if not re.search(r'^\|[\s:\-|]+\|\s*$', text, re.M): f.append('no pipe-table separator')
secs = [int(x) for x in re.findall(r'\u00a7(\d+)', text)]
if secs and max(secs) > len(h2): f.append(f'section ref {max(secs)} > {len(h2)} H2s')
if re.search(r'\b(TODO|TBD|placeholder|scaffold|MVP)\b', text, re.I): f.append('placeholder word')
print(f or 'PASS')
```

Validated shape only (the models pass every clause; this checker was not executed against a gesture draft — none exists yet).

### 2.9 Acceptance (`reports/round-53/accept-c.py`, read from source this session)

Four legs, exit 0 only when all pass: **COUNT** 229 knowledge files exactly; **ENTRY** the file exists; **SWEEP** the bare sweep (`python3 -B reports/round-28/readme/sweep.py`, run as a subprocess, exit code read directly) exits 0 printing `rows 229 files 229` and `missing_from_index 0 []` — so the README index row is a hard dependency of C's acceptance even though another seat drafts it; **SIDS** the entry cites ≥1 S-id and every cited S-id is ≥ S187, is a `corpus/SOURCES.md` row with status `mined`, and its `used-by` cell contains `corpus/knowledge/linguistics/gesture-co-speech-pointing.md`. Baseline now: sweep prints `rows 228 files 228`, exit 0 (verified this session).

### 2.10 S-id discipline (a trap worth its own line)

`accept-c.py` scans the **whole entry file** with `\bS\d{3}\b`. Any S-id token below S187 anywhere — head, boundary table, calibration bank, even a comparison like "unlike S134" — fails the SIDS leg. Cite neighbours by `path:line`, never by their round's S-ids. The head's `sources:` bullet names the S187+ range; that is the only place low-numbered context may be described in words (say "rows S134–S183 of the speech-surrogates round" only if written without the `S\d{3}` tokens — or simply avoid it).

### 2.11 Draft-id shape (frontier rows feeding this entry)

SOURCES rows drafted this round use ids written exactly `NEW-<SeatName>-<n>`; never a bare `-N` or `, -N` fragment (round-52's integration left 11 bare fragments — the mined mistake). At integration the L1 assigns real ids S187 upward and the landed entry cites only those. Note: `tools/check-draft-ids.py` appears in `claims.json` `records_not_claims` but **does not exist in the worktree at HEAD `60f1d2a3`** — if the L1 plans to run it, it must land it as a record first; otherwise enforce the shape with a direct grep for `-N` fragments.

## 3. Evidence (all run this session, lane root, read-only)

| check | command | result |
|---|---|---|
| gate on model | `python3 -B tools/gates/provenance-audit.py corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` | exit 0; `files=1 marks=14 mark-lines=13 findings=0 blocked=0` |
| couples resolver on model | `python3 -B tools/harness/basename-couples-resolver.py <speech-surrogates>` | exit 0; 8 tokens, `direct` or `fallback`, all resolved |
| DR-GES uniqueness | grep `DR-GES` over `corpus` and `reports` | 0 matches |
| DR prefix neighbours | grep `DR-(GES\|[A-Z]{2,4})-` | DR-SRG (speech-surrogates), DR-SGN (sign-languages), plus unrelated registers |
| pre-entry counts | `find corpus/knowledge -name '*.md' \| wc -l`; `ls corpus/knowledge/linguistics/*.md \| wc -l` | 228; 27 |
| gap freshness | `test -e` gesture file; filename probe gestur/pointing/kinesic | ABSENT; 0 hits |
| sweep baseline | `python3 -B reports/round-28/readme/sweep.py` | exit 0; `rows 228 files 228`; `missing_from_index 0 []`; `footer_ok True` |
| model lengths / headings | `wc -l`; `grep -c '###'`; H1 hexdump | 195 and 224 lines; 0 H3 each; U+2014 with spaces in H1 |
| worktree state | `git rev-parse HEAD`; `git status --porcelain` | `60f1d2a3`; dirty: `.ufo/waves/round-53/`, `corpus/lessons/round-53.md`, `reports/round-53/final-measures.py` — no knowledge-file edits in flight at check time |

## 4. Conflicts and notes

- **Singular `- source:` line** — required by the 8-field head this claim declares; the round-8 protocol's plural-only profile (r50 contract §3, DR-1) conflicts. Follow the claim; both models carry all eight fields, so the models are precedent. Gate-neutral either way.
- **Length is the binding constraint.** 14 planned sections in ≤230 lines (sign-languages needed 224 for 15). No acceptance leg enforces length — it dies only if someone runs `wc -l`. Keep the checklist's §2.1 probe in the landing sequence.
- **`accept-c.py` SIDS leg is stronger than the r50 §2.9-B check** (it adds ≥S187, `mined` status, and `used-by` containment) — run `accept-c.py`, not the r50 snippet, for S-ids.
- The gate's `- topic:` finding is `missing-topic` only; it does not check the register words — the freshness-word requirement in §2.2(1) is contract, not gate.

## 5. Unrun checks and limits

- No draft of the entry exists; the §2.8 checker is shape-validated on the models, not executed against a gesture draft.
- No external source opened; no SOURCES row drafted; README untouched (another seat's scope).
- `accept-c.py`, `d-count.py`, and the sweep were run only at the current pre-landing tree; post-landing values (229/229, S187+) are requirements read from the scripts, not yet observed.
- Tooling record: no installs, no updates; system `python3` and existing lane tools only, all read-only.
