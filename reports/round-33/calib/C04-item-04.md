- Seat: C04 | executor (claim C / calibration, open item 4) | box-1 citation conditions 2-4 | date 2026-10-19 | baseline 139e3b6

# C04 — disposition of open item 4 (box-1 citation conditions 2-4)

Write scope: this file only. No source edits by this seat (the SKILL.md fixes
below are **drafts** for integrator application). No git commit/push. No filed
round-1..32 bytes touched. Scratch: `TMPDIR=$PWD/.scratch`.
Non-author declaration: I authored none of the artifacts cited here.

## 0. Item identification and the mapping I used

K03's canonical table (`reports/round-33/calib/K03-open-items.md`) was **not on
disk** at my evidence cut (`ls reports/round-33/calib/` → empty, 2026-10-19), so
item 4 is pinned to the only ordering on record at declaration: the round-32
Decision-4 table row order (`reports/round-32/dossier-d13-operator-decisions.md`,
"Decision 4 — the open-debt inventory", rows 1-9).

- **Row 4 = "box-1 citation conditions 2-4 | r24 (re-confirmed r32) |
  `promotion-review.md:71-88`; D11".** That is my item.
- **Split-mapping coverage.** If K03 instead splits the three conditions into
  three rows (row 4 = condition 2, row 5 = condition 3, row 6 = condition 4),
  then item 4 = the loanword-dating cite cluster — dispositioned in full in
  §1.1/§3.1. Conditions 3 and 4 are dispositioned here too (§1.2/§1.3, §3.2/§3.3),
  so **either mapping is satisfied by this fragment**.
- **C13 instruction:** treat §1.1-§1.3 as ONE item's three sub-parts under the
  cluster mapping; under the split mapping they are items 4, 5, 6. Do not
  disposition them a second time from another fragment.
- The item is a cluster of **three citation-level defects**, and all three are
  **STILL OPEN at HEAD** (re-verified below, dated).

## 1. Status quo re-verification at HEAD (dated)

HEAD = `139e3b662900557afe54f632b468619593dc9fcb` (`git rev-parse HEAD`,
2026-10-19); `SKILL.md` sha256 `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d`,
715 lines. Both corpus sources are byte-stable since round 8 (`git log -1`:
`e1694ba` for `loanword-material-dating.md` and for
`worldbible-integration-contract.md`), so the r24 measurements cannot have
self-healed.

### 1.1 Condition 2 — loanword-dating cite cluster: STILL OPEN

`reports/round-24/promotion-review.md:71-76` names two rows. Measured now:

| row | current cite | measured state of the cited line | rule actually lives at |
|---|---|---|---|
| `SKILL.md:486` | `loanword-material-dating.md:26,60` | `:26` is a **blank line**; `:60` is the "Native term replaces a foreign label / purism" row | `:30` ("A word or sense enters a specified speech community \| Arrival of its referent…") + `:63` ("Date the **sense–referent pairing**…") |
| `SKILL.md:488` | `loanword-material-dating.md:57` | `:57` is "Recipient form reflects a donor innovation" | `:59` ("… \| Dictionary selection bias; imported prestige terminology for local goods") |

Commands: `sed -n '26p' …` → empty; `awk 'NR==30||NR==59||NR==60||NR==63' …`
(reproduced in the control, §4). The r24 cluster also proposed
`era-language-staging.md:124→:127`; **that one is already applied** —
`SKILL.md:490` now cites `era-language-staging.md:127` and
`corpus/knowledge/synthesis/era-language-staging.md:127` carries the
inherited-spoken-label rule. So the open remainder is exactly the two rows above
(2 cite defects, 3 wrong line numbers).

Third measurement, worth recording: `SKILL.md:486`'s second anchor,
"executable B4", is **not** a dangling anchor — `B4` is a leg name in the tool's
own docstring (`tools/d2-typed-labels.py:711` "B1-B6 for a supplied
borrowed-strata label", `:751` "L1-L5, R1-R6, B1-B6"), enforced at `:738-742`
(`entry_stage` earlier than `referent_available_from` ⇒ `D2L-BORROW` FAIL), and
`SKILL.md:59-62` already spells the same anchor out in its live form. Only the
**corpus** half of that row is wrong.

### 1.2 Condition 3 — `worldbible-integration-contract.md:183` mis-cite: STILL OPEN

- Citing sites at HEAD: `SKILL.md:128` and `SKILL.md:501` (both
  `grep -n "worldbible-integration-contract.md:183" SKILL.md`).
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:183` =
  "`- [ ] Every delivered record has scope, stable identity, provenance/invention
  status, and a disposition question; unknowns are not blank cells.`" — the
  delivered-record checklist item, **not** basis hygiene.
- The contract contains **no** basis/boilerplate text at all:
  `grep -ci 'basis\|boilerplate' corpus/knowledge/synthesis/worldbible-integration-contract.md` → **0**.
- Resolving authorities for the rule, verified at HEAD:
  - executable: `tools/harness/packet_uncertainty.py:84` (`_is_boilerplate`) and
    `:199-212` (`U-BASIS-SHORT`, `U-BASIS-BOILERPLATE`, `U-BASIS-RESTATES`);
  - design: `reports/round-15/handoff/v2-design.md:126` ("### 2.3
    Zero-boilerplate: what the builder enforces").
- Same defect class as the r24 record (`reports/round-24/audit-typed.md:84`,
  `reports/round-24/skill-audit.md:75`); the r24 seats proposed the erratum and
  it was **never landed** — this re-measurement confirms both sites still carry
  the wrong pointer.

### 1.3 Condition 4 — dangling tool anchors: STILL OPEN

`grep -c` over `tools/d2-typed-labels.py` at HEAD: `TL-01` → **0**, `TL-02` →
**0**, `FIELD_DEFAULTS` → **0**, `fictional-coordinate` → **0**,
`descriptive-gloss` → **0**. Four rows carry them: `SKILL.md:479`, `:481`
(`TL-01`), `:483` (`TL-02`), `:491` (`fictional-coordinate` / `descriptive-gloss`
/ `FIELD_DEFAULTS`). Live replacements, all verified:

- `D2L-FORM-UNRESOLVED` = `tools/d2-typed-labels.py:422`, emitted as a **hold**
  at `:810-811` ("label_id … has no supplied native/borrowed form") and `:812-814`
  ("translated label with no supplied sound form and no label_id"); selftest
  asserts the 12-row `D2L-FORM-UNRESOLVED` hold set (`:2998`).
- declared kind set: `KINDS` = 3 kinds at `:410`; sound-channel gate:
  `SOUND_KINDS` = (`native-form`, `borrowed-strata`) at `:411`.
- slot gloss is carried as `gloss` + `representation`, **never** as a form:
  `:520` ("the slot carries a gloss, not a form"), `:529`.
- era labels: `D2L-ERA` = `:425`, era resolution `resolve_era` at `:1840`.
- The row's **behaviors** are real and selftest-enforced —
  `python3 tools/d2-typed-labels.py --selftest` → **163/163 checks passed,
  exit 0** (2026-10-19). Only the named tokens are stale.
- The cited `22-label-representation.md` lines in rows 479-482 are **accurate**
  (verified: `reports/supplement-opencode-1/22-label-representation.md:126-128`,
  `:131-132`, `:133-134` carry exactly the claimed classes), so condition 4
  reduces to the **tool** tokens only.

### 1.4 Condition 5 (adjacent, re-measured): reads closed

`grep -c "supported / partial / unresolved" SKILL.md` → **1** (`SKILL.md:77`);
no verbatim duplicate status block found. Consistent with D11's r32
re-measurement. This is a re-measurement, not a disposition — condition 5 is not
part of item 4's cluster.

## 2. Classification

**fixable-now** — every defect is a citation/token re-point inside `SKILL.md`,
bounded to 6 lines (`128`, `479`, `481`, `483`, `486`, `488`, `501` → 7 lines),
**same-line-count replacements** (no line added or removed ⇒ no line-pin shift
for any other artifact citing `SKILL.md` line numbers). No behavior, gate, pin,
or corpus byte changes. Rationale for not carrying: the three conditions have
been open since r24 (re-confirmed r32) and are pointer-level; r24's own seats
proposed the same re-points, so the fix is already reviewed in substance.

## 3. Bounded fix drafts (before/after; integrator applies — no seat edits SKILL.md)

### 3.1 Condition 2

`SKILL.md:486` — before:

```
| A loan's oldest form used to date the referent's arrival | clock conflation; keep word-entry and object-arrival intervals separate (`loanword-material-dating.md:26,60`; executable B4) |
```

after:

```
| A loan's oldest form used to date the referent's arrival | clock conflation; keep word-entry and object-arrival intervals separate (`loanword-material-dating.md:30,63`; executable B4 = `tools/d2-typed-labels.py:738-742` ⇒ `D2L-BORROW` FAIL; erratum 2026-10-19: prior cite `:26` was a blank line and `:60` the purism row) |
```

`SKILL.md:488` — before:

```
| Imported prestige terminology for locally made goods read as evidence of import | dictionary/selection bias; check local manufacture under imported labels (`loanword-material-dating.md:57`) |
```

after:

```
| Imported prestige terminology for locally made goods read as evidence of import | dictionary/selection bias; check local manufacture under imported labels (`loanword-material-dating.md:59`; erratum 2026-10-19: `:57` is the donor-innovation row) |
```

Alternative on record: r24 `reports/round-24/box1-craft.md:68` proposed
`:60→:36-39/:63`. I use `:30,63` because `:36-39` is the TPQ/TAQ **dating-bound**
material, a different rule from this row's clock **separation** rule (`:30` is the
Lexical clock row that states word-entry ≠ referent arrival). If C14 prefers the
r24 wording, the `:63` half is common to both.

### 3.2 Condition 3

`SKILL.md:128` — before:

```
rejected (`worldbible-integration-contract.md:183`; v2-design §2.3).
```

after:

```
rejected (`tools/harness/packet_uncertainty.py:84,199-212`; v2-design §2.3 = `reports/round-15/handoff/v2-design.md:126`; erratum 2026-10-19: `worldbible-integration-contract.md:183` carries the delivered-record checklist item, not basis hygiene).
```

`SKILL.md:501` — before (row tail):

```
(`reports/round-15/claims.json:14`; `worldbible-integration-contract.md:183`) |
```

after (row tail):

```
(`reports/round-15/claims.json:14`; `tools/harness/packet_uncertainty.py:203-211` `U-BASIS-BOILERPLATE`/`U-BASIS-RESTATES`; erratum 2026-10-19: contract `:183` carries the delivered-record checklist item, not basis hygiene) |
```

Both edits keep the existing "v2-design §2.3" reference and add the resolving
path/line so the §-only reference stops being the sole pointer. Erratum-only
variant (acceptable if the integrator prefers not to drop the contract cite):
keep `worldbible-integration-contract.md:183` and append
"erratum 2026-10-19: this line carries the delivered-record checklist item, not
basis hygiene; rule authority `tools/harness/packet_uncertainty.py:84,199-212`".
Under that variant, §4's C3 assertions must be relaxed to "erratum present +
authority present".

### 3.3 Condition 4

`SKILL.md:479` — `; executable `TL-01`)` → `; executable `D2L-FORM-UNRESOLVED` (`tools/d2-typed-labels.py:422`, hold at `:810-811`))`

`SKILL.md:481` — same re-point: `` (`22-label-representation.md:131-132`; executable `TL-01`) `` → `` (`22-label-representation.md:131-132`; executable `D2L-FORM-UNRESOLVED` at `tools/d2-typed-labels.py:810-811`) ``

`SKILL.md:483` — before:

```
| A record with no declared kind at all | hold with a stable reason — the kind is never guessed from the text's language (`tools/d2-typed-labels.py` `TL-02`) |
```

after:

```
| A record with no declared kind at all | hold with a stable reason — the kind is never guessed from the text's language (`tools/d2-typed-labels.py:410` `KINDS` are declared; hold `D2L-FORM-UNRESOLVED` at `:812-814`) |
```

`SKILL.md:491` — before:

```
| Era tags or slot glosses graded on the name/sound channel | type them `fictional-coordinate` / `descriptive-gloss`; neither enters the sound channel (tool `FIELD_DEFAULTS`) |
```

after:

```
| Era tags or slot glosses graded on the name/sound channel | keep them off the sound channel: only `native-form`/`borrowed-strata` enter it (`tools/d2-typed-labels.py:411` `SOUND_KINDS`); a slot gloss rides as `gloss` + `representation: english-gloss`, never as a form (`:520,529`); era labels resolve through era records and are checked as `D2L-ERA` (`:425`); erratum 2026-10-19: the five-kind vocabulary (`fictional-coordinate`/`descriptive-gloss`, tool `FIELD_DEFAULTS`) is not shipped — live `KINDS` is three (`:410`) |
```

Minimal variant for :491 if the cell must stay short: replace
"`fictional-coordinate` / `descriptive-gloss` … (tool `FIELD_DEFAULTS`)" with
"off the sound channel (`tools/d2-typed-labels.py:411` `SOUND_KINDS`; gloss as
`representation`, `:520,529`; era via `D2L-ERA`)" and drop the five-kind
vocabulary. Note the vocabulary change is substantive, not cosmetic: the live
tool ships **three** kinds (`:410`), a resolution on record since round 8
(`reports/round-8/depth/findings.md:112`).

## 4. Controls (RED now; GREEN after application)

Run from the repo root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:

```bash
python3 - <<'PY'
import re, sys, pathlib
R = pathlib.Path(".")
rd = lambda p: p.read_text(encoding="utf-8").splitlines()
skill = rd(R/"SKILL.md"); lw = rd(R/"corpus/knowledge/synthesis/loanword-material-dating.md")
ct = rd(R/"corpus/knowledge/synthesis/worldbible-integration-contract.md")
tool = rd(R/"tools/d2-typed-labels.py"); pu = rd(R/"tools/harness/packet_uncertainty.py")
L = lambda p, n: p[n-1] if n-1 < len(p) else ""
fails = []
r486 = L(skill,486)
for part in re.findall(r"loanword-material-dating\.md:([0-9,\-]+)", r486):
    for x in part.split(","):
        if x.isdigit() and not L(lw,int(x)).strip():
            fails.append("C2-a SKILL.md:486 cites blank loanword-material-dating.md:%s" % x)
if not re.search(r"loanword-material-dating\.md:30,63", r486): fails.append("C2-a SKILL.md:486 does not cite :30,63")
if "Arrival of its referent" not in L(lw,30): fails.append("C2-a target :30 lost the rule")
if "referent pairing" not in L(lw,63): fails.append("C2-a target :63 lost the rule")
r488 = L(skill,488)
if not re.search(r"loanword-material-dating\.md:59", r488): fails.append("C2-b SKILL.md:488 does not cite :59")
if "Dictionary selection bias" not in L(lw,59): fails.append("C2-b target :59 lost the rule")
for n in (128,501):
    t = L(skill,n)
    if "worldbible-integration-contract.md:183" in t: fails.append("C3 SKILL.md:%d still cites mis-cited contract :183" % n)
    if "packet_uncertainty.py" not in t: fails.append("C3 SKILL.md:%d lacks the executable basis authority" % n)
if "_is_boilerplate" not in L(pu,84): fails.append("C3 authority moved: packet_uncertainty.py:84")
if "U-BASIS-BOILERPLATE" not in "\n".join(pu[198:212]): fails.append("C3 authority moved: packet_uncertainty.py:199-212")
if "basis" in "\n".join(ct).casefold(): fails.append("C3 note: contract now carries basis text - re-read erratum")
for n in (479,481,483,491):
    t = L(skill,n)
    for tok in ("TL-01","TL-02","FIELD_DEFAULTS","fictional-coordinate","descriptive-gloss"):
        if tok in t: fails.append("C4 SKILL.md:%d still names dangling token %s" % (n,tok))
if "D2L-FORM-UNRESOLVED" not in L(tool,422): fails.append("C4 live id missing at tools/d2-typed-labels.py:422")
if "SOUND_KINDS" not in L(tool,411): fails.append("C4 live SOUND_KINDS missing at :411")
if "D2L-BORROW" not in L(tool,423): fails.append("C4 live id missing at :423")
print("C04-item04-control: %s (%d failing assertions)" % ("GREEN" if not fails else "RED", len(fails)))
for f in fails: print("   ", f)
sys.exit(1 if fails else 0)
PY
```

**Measured now (pre-application), 2026-10-19 at `139e3b6`:**

```
C04-item04-control: RED (13 failing assertions)
    C2-a SKILL.md:486 cites blank loanword-material-dating.md:26
    C2-a SKILL.md:486 does not cite :30,63
    C2-b SKILL.md:488 does not cite :59
    C3 SKILL.md:128 still cites mis-cited contract :183
    C3 SKILL.md:128 lacks the executable basis authority
    C3 SKILL.md:501 still cites mis-cited contract :183
    C3 SKILL.md:501 lacks the executable basis authority
    C4 SKILL.md:479 still names dangling token TL-01
    C4 SKILL.md:481 still names dangling token TL-01
    C4 SKILL.md:483 still names dangling token TL-02
    C4 SKILL.md:491 still names dangling token FIELD_DEFAULTS
    C4 SKILL.md:491 still names dangling token fictional-coordinate
    C4 SKILL.md:491 still names dangling token descriptive-gloss
```

The 13 assertions map 1:1 onto §1.1 (3), §1.2 (4), §1.3 (6) — no assertion is
unexplained. The control is a **counting command**: it exits **1** while any
assertion fails and **0** when GREEN (measured: exit 1 now, 13 failures).
Expected after the integrator applies §3.1-§3.3:
`C04-item04-control: GREEN (0 failing assertions)`, exit 0. The control is
**prescriptive** (it tests the prescribed re-points, not merely "a fix of some
kind"); under the erratum-only variants named in §3.2 the C3 pair must be
relaxed as stated there.

Regression controls for the same edit (must stay green after application):

```bash
python3 tools/d2-typed-labels.py --selftest                     # 163/163, exit 0
python3 -B reports/round-30/craft/box1-survey.py                # named 28 / resolvable 28, exit 0
python3 tools/harness/packet_uncertainty.py --selftest           # exit 0 (authority still live)
```

All three measured **green at HEAD before the edit** (2026-10-19); box1-survey
exit 0 with `named: 28, resolvable: 28` and the current `skill_sha256`
`79fe91d3…`.

## 5. Pin-cascade exposure for this item (X00 owns the global map)

- **No tool asserts `SKILL.md`'s digest.** `tools/gates/argot-derivation-gate.py:4`
  only cites SKILL.md in a docstring (selftest 27/27, exit 0);
  `reports/round-30/craft/box1-survey.py:10` **reports** the digest, does not
  assert it. So the edit cannot break a gate or a frozen pin.
- **Filed receipts will show a new digest.** `reports/round-31/validation.json:1026`
  and `reports/round-32/validation.json:1000` record `SKILL.md:
  79fe91d3…` — filed bytes, never edited; the round-33 receipt must record the
  **new** digest (r31-sweep §5 supersession semantics: pins green, content ages).
- **No line-pin shift:** every draft is a same-line-count replacement, so all
  other `SKILL.md:<n>` citations stay valid.

## 6. Ledger row for C15 (item 4, cluster mapping)

```json
{
  "id": "item-04",
  "item": "box-1 citation conditions 2-4 (loanword-dating cite cluster; worldbible-integration-contract.md:183 mis-cite; dangling tool anchors TL-01/TL-02/FIELD_DEFAULTS/fictional-coordinate/descriptive-gloss)",
  "origin": "r24 (re-confirmed r32)",
  "pointer": "reports/round-24/promotion-review.md:71-88; reports/round-32/dossier-d11-shonen-boxes.md (box 1, conditions 2-4); reports/round-32/dossier-d13-operator-decisions.md (Decision 4, row 4)",
  "status_quo_check": "RE-VERIFIED OPEN at HEAD 139e3b6, 2026-10-19: SKILL.md:486 cites a blank line (:26); SKILL.md:488 cites :57 not :59; SKILL.md:128+:501 cite contract :183 which carries the delivered-record checklist item (grep -ci 'basis|boilerplate' contract = 0); TL-01/TL-02/FIELD_DEFAULTS/fictional-coordinate/descriptive-gloss = 0 hits in tools/d2-typed-labels.py; control RED with 13 failing assertions",
  "disposition_class": "fixed-with-evidence",
  "applies_via": "calib/C04-item-04.md §3.1-3.3 -> calib/C14-fix-drafts.md -> integrator SKILL.md edit (no seat edits SKILL.md)",
  "evidence": "reports/round-33/calib/C04-item-04.md §1.1-§1.3, §3.1-§3.3, §4 (control RED 13/13 now, GREEN 0 after application); tools/d2-typed-labels.py:410,411,422,423,425,520,529,738-742,810-814; tools/harness/packet_uncertainty.py:84,199-212; reports/round-15/handoff/v2-design.md:126; corpus/knowledge/synthesis/loanword-material-dating.md:30,59,63",
  "fix_draft": "reports/round-33/calib/C04-item-04.md §3 (7 SKILL.md lines, same-line-count replacements)",
  "fix_verification": "the §4 control must print GREEN (0 failing assertions) and exit 0 (exit 1 while any assertion fails; measured exit 1 with 13 failures pre-application); regression controls: tools/d2-typed-labels.py --selftest 163/163, box1-survey 28/28, packet_uncertainty.py --selftest 19/19",
  "owner": "integrator (applies) / operator (owns box-1 promotion reading)",
  "reason": "if the drafts are NOT applied in round 33, re-classify this row carried-with-owner+reason+next-touch (owner: integrator; reason: no seat may edit SKILL.md, draft ready and controlled; next_touch: round-34 integrator application)",
  "next_touch": "round-33 integrator application, else round-34"
}
```

## 7. Adjacent same-class findings (NOT part of item 4 — do not double-disposition)

Recorded for C13/C14 awareness with pointers only; I make no disposition claim
on them:

- **Other corpus citation drift** in the same error-pattern table:
  `SKILL.md:485` cites `language-contact.md:78-79` bare (file lives at
  `corpus/knowledge/linguistics/language-contact.md`); `SKILL.md:487` cites
  `garment-lexicon-crosslinguistic.md:28,30` (bare; the r24 audit measured `:26`
  blank); `SKILL.md:489` cites `costume-language-coupling-table.md:43`,
  `SKILL.md:492` cites `naming-collision-gate.md:72` bare. Source:
  `reports/round-24/audit-typed.md:105,§5.2 item 4`. Not in promotion-review's
  conditions 2-4, so not mine.
- **`reports/round-18/d4/holds.md` §4.2** non-existent section
  (`reports/round-24/audit-typed.md:105`). Separate pointer class.
- **`SKILL.md:479-482`'s `22-label-representation.md` cites are accurate**
  (verified `:126-128`, `:129-130`, `:131-132`, `:133-134`) — no fix owed there.

## Owed

- `reports/round-33/calib/K03-open-items.md` — K03's canonical table was absent
  at my cut, so my item↔row mapping (§0) is inferred from the on-record
  Decision-4 row order. The integrator/C13 must confirm item 4 against K03's
  table and, if K03 numbered differently, re-map §1.1-§1.3 accordingly (the
  content is complete for all three conditions, so only the numbering changes).
- Integrator application of §3.1-§3.3 (no seat may edit `SKILL.md`), then the §4
  control re-run to GREEN — this is what converts `fixed-with-evidence` from
  draft-ready to landed.

## Citations

Paths (all read at HEAD `139e3b6`, 2026-10-19):

- `reports/round-33/targets.json` (seat C04 mission; shared_rules)
- `reports/round-33/claims.json` (claim C, after_required, thresholds)
- `reports/round-32/dossier-d13-operator-decisions.md` (Decision 4 table, row 4)
- `reports/round-32/dossier-d11-shonen-boxes.md` (box-1 conditions 2-4, condition 5 re-measurement)
- `reports/round-24/promotion-review.md:71-88`
- `reports/round-24/audit-typed.md:84,105,169,178,§5.2`
- `reports/round-24/skill-audit.md:75`
- `reports/round-24/box1-craft.md:68`
- `SKILL.md:59-62,128,479-492,501`
- `corpus/knowledge/synthesis/loanword-material-dating.md:26,30,57,59,60,63`
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:183`
- `corpus/knowledge/synthesis/era-language-staging.md:127`
- `reports/supplement-opencode-1/22-label-representation.md:124-134`
- `tools/d2-typed-labels.py:410,411,419-427,520,529,711,738-742,751,810-814,2998`
- `tools/harness/packet_uncertainty.py:84,199-212`
- `reports/round-15/handoff/v2-design.md:126`
- `reports/round-8/depth/findings.md:112`
- `reports/round-10/drift/ledger.json` (TL-01/TL-02 id-drift note)
- `reports/round-30/craft/box1-survey.py:10`; `tools/gates/argot-derivation-gate.py:4`
- `reports/round-31/validation.json:1026`; `reports/round-32/validation.json:1000` (SKILL.md digest receipts)

Commands (all run 2026-10-19 in the repo root):

- `git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb`
- `sha256sum SKILL.md` → `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d`
- `grep -c "TL-01\|TL-02\|FIELD_DEFAULTS\|fictional-coordinate\|descriptive-gloss" tools/d2-typed-labels.py` → 0
- `grep -ci 'basis\|boilerplate' corpus/knowledge/synthesis/worldbible-integration-contract.md` → 0
- `sed -n '26p' corpus/knowledge/synthesis/loanword-material-dating.md` → empty
- `python3 tools/d2-typed-labels.py --selftest` → 163/163 passed, exit 0
- `python3 -B reports/round-30/craft/box1-survey.py` → named 28 / resolvable 28, exit 0
- `python3 tools/harness/packet_uncertainty.py --selftest` → 19/19 passed, exit 0
- `python3 tools/gates/argot-derivation-gate.py --selftest` → 27/27, exit 0
- §4 control (extracted verbatim from this file and run) → `RED (13 failing assertions)`, **exit 1** (output quoted verbatim in §4)
- `ls reports/round-33/calib/` → empty at my cut (K03 absent)
