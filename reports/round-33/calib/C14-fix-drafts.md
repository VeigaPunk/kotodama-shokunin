- Seat: C14 | executor | claim C | date 2026-10-19 | baseline 139e3b6

# C14 — bounded-fix drafts for the fixable open items (no source edits by this seat)

**Write scope:** this file only (`reports/round-33/calib/C14-fix-drafts.md`), plus scratch
under `.scratch/c14/`. No source file was edited; every draft is a before/after text block for
the **integrator** to apply. No filed round byte (`reports/round-1..32/**`), no
`corpus/lessons/*.md`, no `tools/gates/frozen/**`, no `.ufo/**` was touched.
`git status --porcelain` at this seat's close: ` M LOG.md` (another writer), `?? REGIMEN.md`,
`?? reports/round-33/` — no filed-round path. The three round-5/6/7 validators this seat ran
for Fix 4's evidence **do** rewrite their own filed `validation.json` (R06-F9,
`reports/round-33/review/R06-calib-review.md:257-264`); the three receipts currently match
their HEAD digests (`sha256sum` vs `git show HEAD:` → `73a66f74…`, `32c621ef…`, `2f4c1e15…`,
2026-10-19), so no repair is owed. Fix 4's errata text now carries the isolation warning.

**Item binding (K03 landed mid-seat; re-bound).** `reports/round-33/calib/K03-open-items.md:75-78`
maps C01↔OI-01 … C12↔OI-12 in table order, and states: "C14's bounded-fix drafts correspond to
OI-04, OI-05, OI-06 (the three box-1 citation pointer fixes) and OI-07's N1 errata; OI-01..OI-03,
OI-08..OI-12 are the carry candidates". Drafts below are keyed to those ids. Owner fragments on
disk at this seat's close: `C04-item-04.md` (OI-04) and `C07-item-07.md` (OI-07); OI-05 and
OI-06 owners (`C05`, `C06`) had not landed — see `## Owed`.

**Reviewer answer key.** `reports/round-33/review/R06-calib-review.md` pre-registered the
judging key for this file (its §2-§3). Three of its findings changed the drafts and are
reconciled inline: R06-F1/F2 (clause coverage — adopted), R06-F3 (no re-point target inside the
contract — scope-qualified, converged target retained), R06-F5 (no target for the retired
anchor tokens — qualified: the *retired* tokens have no target; the *live* vocabulary does).
R06-F7's requirement (a distinct expected verdict per round) is satisfied by Fix 4.

## Fix 1 — OI-04 (box-1 condition 2): the loanword-dating cite cluster (`SKILL.md:486`, `:488`)

**Finding (re-verified live, 2026-10-19).** `corpus/knowledge/synthesis/loanword-material-dating.md`
(sha256 `5b1d75abd29422b100ab47649f2b5be1e40f598cf2d5cdf35d8afd6103db4d58`, 209 lines, last
touched `e1694ba`): `:26` is blank; the four-clock table is `:27-34` (Contact `:29`, Lexical `:30`,
Material `:31`); the sense–referent pairing is `:63`; the prestige/dictionary-bias row is `:59`.
Both SKILL rows still cite stale lines. Corroborated by `C04-item-04.md` §1.1 (same measurement,
same day).

**Root cause (this seat, diff-verified).** The cites were authored *in* commit `e1694ba`, and
that same commit edited the corpus file, inserting 3 lines at the top
(`git diff e1694ba~1 e1694ba -- corpus/knowledge/synthesis/loanword-material-dating.md`
→ hunk `@@ -2,6 +2,9 @@`, the added `- source:` / `- verified-at:` / `- recheck:` lines), which
shifted every later pointer by **+3**. Pre-commit: `:26` = the Contact row, `:60` = the
sense–referent pairing line. So `:26,60` was valid against pre-commit bytes and was invalidated
by the commit's own corpus edit — a drift, not a fabrication. (`:57` was already off by one
pre-commit: the craft-domain row was pre `:56` → HEAD `:59`.)

### Draft 1a — `SKILL.md:486`

before:

```
| A loan's oldest form used to date the referent's arrival | clock conflation; keep word-entry and object-arrival intervals separate (`loanword-material-dating.md:26,60`; executable B4) |
```

after (RECOMMENDED — R06-F1's minimum meaning-preserving set: `:30` covers "word entry ≠
referent arrival" in its own two cells, `:31` is the object clock, `:63` is the "oldest form"
clause):

```
| A loan's oldest form used to date the referent's arrival | clock conflation; keep word-entry and object-arrival intervals separate (`loanword-material-dating.md:30-31,63`; executable B4) |
```

**Withdrawn variant (this seat's first draft).** `:29,63` — drift-faithful (Contact row +3) but
R06-F1 is right that it loses clause (ii): the Contact row is about encounter events, not the
word/object clock separation. A citation's job is to support the row's claim, not to preserve a
stale line choice, so `:29,63` is withdrawn. C04's `:30,63` (`C04-item-04.md` §3.1) is a
verifiable 2-pointer subset of the recommended set if the integrator prefers a smaller edit.

### Draft 1b — `SKILL.md:488`

before:

```
| Imported prestige terminology for locally made goods read as evidence of import | dictionary/selection bias; check local manufacture under imported labels (`loanword-material-dating.md:57`) |
```

after (RECOMMENDED — R06-F2: `:59` carries the diagnosis verbatim, `:63` the remedy
"local manufacture under an imported label"):

```
| Imported prestige terminology for locally made goods read as evidence of import | dictionary/selection bias; check local manufacture under imported labels (`loanword-material-dating.md:59,63`) |
```

C04's `:59`-only variant (`C04-item-04.md` §3.1) resolves and covers the diagnosis; it drops the
remedy clause, which is why `:63` is added here.

**Verification command** (must print `:26` blank, `:30` Lexical, `:31` Material, `:59` craft row,
`:63` pairing):

```
awk 'NR==26||NR==30||NR==31||NR==59||NR==63{printf "%d: %s\n", NR, $0}' corpus/knowledge/synthesis/loanword-material-dating.md
grep -n "prestige terminology\|sense–referent" corpus/knowledge/synthesis/loanword-material-dating.md
git diff e1694ba~1 e1694ba -- corpus/knowledge/synthesis/loanword-material-dating.md | head -12
```

**Not part of this item (recorded so it is not "fixed" twice):** C04 §1.1 measured that
`era-language-staging.md:124→:127` (the other r24 cluster member) is already applied at
`SKILL.md:490`, and that the row's "executable B4" anchor is **not** dangling (`B4` is a live leg
name, `tools/d2-typed-labels.py:711,:751`, enforced `:738-742`). This seat's drafts do not touch
either.

## Fix 2 — OI-05 (box-1 condition 3): `worldbible-integration-contract.md:183` mis-cite (`SKILL.md:128`, `:501`)

**Finding (re-verified live).** `corpus/knowledge/synthesis/worldbible-integration-contract.md`
(209 lines, sha256 `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`): no
basis-hygiene wording exists at all — `grep -n "boilerplate"` → rc=1 (no match);
`grep -n "basis\|Basis"` → rc=1 (no match). `:183` is the delivered-record checklist item
("Every delivered record has scope, stable identity, provenance/invention status, and a
disposition question; unknowns are not blank cells"). Same finding: `reports/round-24/skill-audit.md:75`
R1, `C04-item-04.md` §1.2, R06-F3 (`review/R06-calib-review.md:98-134`).

**Converged target (three independent seats).** The rule is executable:
`tools/harness/packet_uncertainty.py:84-90` (`_is_boilerplate`), findings `:205`
`U-BASIS-BOILERPLATE` ("basis is a boilerplate token, not a reason") and `:209`
`U-BASIS-RESTATES` ("basis only restates the status or evidence_status token");
`python3 -B tools/harness/packet_uncertainty.py --selftest` → exit 0, "19 checks passed"
(2026-10-19). r24 proposed this exact target (`reports/round-24/skill-audit.md:75`:
`tools/harness/packet_uncertainty.py:84,199-212`); C04 §3.2 drafts it the same way. Design
authority: `reports/round-15/handoff/v2-design.md:126,131-139` §2.3 (heading `:126`, the five
builder checks `:130-139`; `:127`/`:129` are blank, so the range is written `:126,131-139` —
the machine-checkable form below).

**R06-F3 reconciliation.** R06 is right that **no target exists inside the contract** ("the word
`basis` occurs zero times"), so a contract-internal re-point is impossible and the honest
disposition is an erratum. This draft is that erratum: it deletes the bad cite and names a
verified executable authority outside the contract. If the integrator prefers R06's stricter
reading (delete the cite, keep only the already-present `v2-design §2.3` / `claims.json:14`),
that variant is meaning-neutral too — see Draft 2 fallback.

### Draft 2a — `SKILL.md:128`

before (span `:126-128`; cited clause on `:128`):

```
rejected (`worldbible-integration-contract.md:183`; v2-design §2.3).
```

after (RECOMMENDED):

```
rejected (`tools/harness/packet_uncertainty.py:205,209`; v2-design §2.3 = `reports/round-15/handoff/v2-design.md:126,131-139`; erratum 2026-10-19: contract `:183` carries the delivered-record checklist item, not basis hygiene).
```

fallback (R06-F3 strict variant, meaning-neutral):

```
rejected (v2-design §2.3 = `reports/round-15/handoff/v2-design.md:126,131-139`; erratum 2026-10-19: the prior `worldbible-integration-contract.md:183` cite carried the delivered-record checklist item, not basis hygiene).
```

### Draft 2b — `SKILL.md:501`

before:

```
| Two claims share one basis sentence, or a basis restates the status word | boilerplate basis: basis is per-claim evidence whose witness resolves (`reports/round-15/claims.json:14`; `worldbible-integration-contract.md:183`) |
```

after (RECOMMENDED):

```
| Two claims share one basis sentence, or a basis restates the status word | boilerplate basis: basis is per-claim evidence whose witness resolves (`reports/round-15/claims.json:14`; `tools/harness/packet_uncertainty.py:205,209`; erratum 2026-10-19: contract `:183` carried the delivered-record checklist item) |
```

fallback (R06-F3 strict): same row with `; `worldbible-integration-contract.md:183`` deleted and
no new pointer (the row keeps `reports/round-15/claims.json:14`, which already carries the
zero-boilerplate declaration).

**Two sites, one defect (R06-F4).** Both `:128` and `:501` carry the wrong pointer; fixing only
one leaves the mis-cite reproducible from its origin,
`reports/round-15/knowledge/skill-draft.md:95-97` (R06's measurement). Fix both or neither.

**Verification commands:**

```
grep -n "boilerplate" corpus/knowledge/synthesis/worldbible-integration-contract.md; echo "rc=$?"   # rc=1
grep -n "basis\|Basis" corpus/knowledge/synthesis/worldbible-integration-contract.md; echo "rc=$?"  # rc=1
awk 'NR==183{print}' corpus/knowledge/synthesis/worldbible-integration-contract.md                   # delivered-record item
awk 'NR==205||NR==209{printf "%d: %s\n", NR, $0}' tools/harness/packet_uncertainty.py
python3 -B tools/harness/packet_uncertainty.py --selftest                                            # exit 0, 19 checks
```

## Fix 3 — OI-06 (box-1 condition 4): dangling tool anchors (`SKILL.md:479`, `:481`, `:483`, `:491`)

**Finding (re-verified live).** `TL-01`, `TL-02`, `FIELD_DEFAULTS`, `fictional-coordinate`,
`descriptive-gloss` each occur **0** times in `tools/d2-typed-labels.py` (3645 lines,
`grep -c` per token = 0, 2026-10-19; C04 §1.3 and R06-F5 measured the same). The live vocabulary
is `FINDING_CLASSES` (`tools/d2-typed-labels.py:419-420`) with `D2L_DATA = "D2L-DATA"` (`:421`)
and `D2L_FORM = "D2L-FORM-UNRESOLVED"` (`:422`); shipped kinds are exactly three,
`KINDS = ("translated-label", "native-form", "borrowed-strata")` (`:410`);
`SOUND_KINDS = ("native-form", "borrowed-strata")` (`:411`).
`python3 -B tools/d2-typed-labels.py --selftest` → exit 0, "163/163 checks passed" (2026-10-19),
including "live packet: the owed form slots stay held, never passed" (`:3193`) and
"live packet: no GAR label is graded on the sound channel" (`:3195`).

**R06-F5 reconciliation.** R06 is right that **the retired tokens have no target anywhere in
`tools/`** — a re-point *of those tokens* would be unverifiable. What is verifiable is naming the
live replacement, which is what `reports/round-10/drift/shard-05.md:54` prescribed
("Fix: update the four citations to the live ids (`D2L-FORM-UNRESOLVED`, `D2L-DATA`) or land the
mapping table") and what C04 §1.3/§3.3 drafts. Each draft below is therefore a **dated erratum
plus a live-id naming**, not a token re-point. If the integrator prefers R06's stricter reading
(pure errata, no new id), the behavior sentence in each after-text stands alone and the id may be
dropped — no draft here depends on a token that does not exist.

**Live behavior per row (probed this seat — the same in-process path the tool's selftest uses;
stable messages, no traceback):**

| probe | exit | finding |
|---|---|---|
| invalid declared kind | 2 | `D2L-DATA` **fail** — `kind 'not-a-kind' is not one of ('translated-label', 'native-form', 'borrowed-strata')` |
| `native-form`, `status: supplied`, empty text | 2 | `D2L-DATA` **fail** ×2 — `status supplied requires text` + `supplied sound form has no text` |
| `translated-label` whose `label_id` has no supplied form | 1 | `D2L-FORM-UNRESOLVED` **hold** — `label_id LEX-GAR-99 has no supplied native/borrowed form` |

**Probe command (re-runnable verbatim):**

```
python3 - <<'PY'
import importlib.util, json
spec = importlib.util.spec_from_file_location("tl", "tools/d2-typed-labels.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
BASE = {"id": "PROBE-01", "owner": "05-lexicon", "label_id": "L-99",
        "kind": "native-form", "text": "kas", "script": "Latn",
        "representation": "editorial-romanization", "scheme": "d2-roman",
        "status": "supplied", "era_ids": [], "issues": []}
def probe(name, **over):
    label = dict(BASE); label.update(over)
    r = m.parse_typed_labels({"eras": ["E0"], "layers": [],
                              "typed_labels": [label]})
    print(name, "-> exit", r["exit_code"],
          json.dumps([{"code": f["code"], "kind": f["kind"], "detail": f["detail"]}
                      for f in r["findings"]]))
probe("kindless  ", kind="not-a-kind")
probe("nobytes   ", text="")
probe("owed-slot ", kind="translated-label", label_id="LEX-GAR-99",
      representation="english-gloss", status="to-verify", text="wrap skirt")
PY
```

### Draft 3a — `SKILL.md:479` (live-id naming; behavior claim survives; C04 §3.3 same target)

before:

```
| A label-only record passes silently | forbidden: label-only → off the sound channel **and** a hold, so the aggregate stays red (`22-label-representation.md:126-128`; executable `TL-01`) |
```

after:

```
| A label-only record passes silently | forbidden: label-only → off the sound channel **and** a hold, so the aggregate stays red (`22-label-representation.md:126-128`; live hold `D2L-FORM-UNRESOLVED`, `tools/d2-typed-labels.py:422,:810-814`; erratum 2026-10-19: retired anchor `TL-01`) |
```

### Draft 3b — `SKILL.md:481` (live-id naming + dated verdict erratum: HOLD is state-dependent)

before:

```
| A sound kind declared with no bytes supplied | HOLD, not clean (`22-label-representation.md:131-132`; executable `TL-01`) |
```

after:

```
| A sound kind declared with no bytes supplied | not clean: a `supplied` sound kind with no text is a `D2L-DATA` FAIL (exit 2, `tools/d2-typed-labels.py:694-695,:774-775`); carried `to-verify` with its owed slot, the `D2L-FORM-UNRESOLVED` hold stands (`:810-814`) (`22-label-representation.md:131-132`; erratum 2026-10-19: retired anchor `TL-01`) |
```

**Rationale (errata, not cosmetics).** The probe shows the `supplied`-with-no-bytes case is a
**fail** (two `D2L-DATA` findings, exit 2), while the carried `to-verify` case is the
`D2L-FORM-UNRESOLVED` **hold** — the row is true only in the second state. The row's punchline
("not clean") survives in both. C04 §3.3's minimal variant (re-point to
`D2L-FORM-UNRESOLVED` at `:810-811`, no verdict correction) is the smaller edit; the version
above is the one the probe supports for both states. This closes the r10 observation that the
class was "silent in the live tool" (`reports/round-10/drift/shard-05.md:35`) — at HEAD it fails
loudly with a stable message. The divergence is the errata's core: the r5 design row
(`reports/supplement-opencode-1/22-label-representation.md:131-132`, "`form_kind: native` with no
`native_form` ⇒ HOLD") states a **HOLD**, while the shipped tool at HEAD refuses a `supplied`
kind with no text as a `D2L-DATA` **fail**; the HOLD survives only on the carried `to-verify`
path. The draft states both so the row is true against either reading.

### Draft 3c — `SKILL.md:483` (live-id naming + dated verdict erratum: hold → fail)

before:

```
| A record with no declared kind at all | hold with a stable reason — the kind is never guessed from the text's language (`tools/d2-typed-labels.py` `TL-02`) |
```

after:

```
| A record with no declared kind at all | refused with a stable reason: `D2L-DATA` FAIL, exit 2 — the kind is never guessed from the text's language; it is assigned by declaration/component or refused (`tools/d2-typed-labels.py:768-769`; projection `:500,:549,:565`; erratum 2026-10-19: retired anchor `TL-02`) |
```

**Rationale.** Live: an invalid/undeclared kind is a `D2L-DATA` **fail** with a stable message
(`:768-769`, exit 2 via `:830`) — never a hold, never a traceback (the r10 crash noted at
`reports/round-10/drift/shard-05.md:37` is gone at HEAD; the probe returns a stable message).
The row's load-bearing claim ("the kind is never guessed from the text's language") is preserved
and now points at how kinds are actually assigned: costume → `translated-label` (`:500`),
lexicon → `native-form` (`:549`) or `borrowed-strata` (`:565`) by declared layer.

### Draft 3d — `SKILL.md:491` (retired name + live mechanism; keeps the design vocabulary)

before:

```
| Era tags or slot glosses graded on the name/sound channel | type them `fictional-coordinate` / `descriptive-gloss`; neither enters the sound channel (tool `FIELD_DEFAULTS`) |
```

after (RECOMMENDED):

```
| Era tags or slot glosses graded on the name/sound channel | type them off the sound channel: costume labels project `translated-label` (`tools/d2-typed-labels.py:500`) and slot glosses ride as `gloss`/`representation`, never as a form (`:520,:529`), so neither enters the sound channel (retired anchor `FIELD_DEFAULTS`; the five-kind superset `fictional-coordinate`/`descriptive-gloss` remains proposed-only, `reports/round-11/depth/shard-gate-adapter.md:120-125`; selftest `no GAR label is graded on the sound channel`, `:3195`; erratum 2026-10-19) |
```

minimal variant (one parenthetical swap, if the integrator prefers the smaller edit):

```
| Era tags or slot glosses graded on the name/sound channel | type them `fictional-coordinate` / `descriptive-gloss`; neither enters the sound channel (retired anchor; live: `translated-label` projection `tools/d2-typed-labels.py:500`, `reconcile_era` `:859`, selftest `:3195`) |
```

**Rationale.** `FIELD_DEFAULTS` and the two kind names exist in no shipped tool (0 hits).
`reports/round-11/depth/shard-gate-adapter.md:120-125` records their exact status: design-spec
§8.1 *proposes* the five-kind superset; the shipped tool ships three and refuses the unknowns
rather than guessing a channel. The row's behavior claim is current (`:3195` selftest check).
C04 §1.3 names the same live mechanics (`:520`, `:529`; era resolution `:1840`).

**Verification commands:**

```
for t in TL-01 TL-02 FIELD_DEFAULTS fictional-coordinate descriptive-gloss; do printf "%s: " "$t"; grep -c -- "$t" tools/d2-typed-labels.py; done   # all 0
awk 'NR==410||NR==411||NR==419||NR==420||NR==421||NR==422{printf "%d: %s\n", NR, $0}' tools/d2-typed-labels.py
python3 -B tools/d2-typed-labels.py --selftest   # exit 0, 163/163
```

## Fix 4 — OI-07 (cold-run N1): dated expected-verdict errata for the round-5/6/7 acceptance re-runs

**Finding (re-measured live, 2026-10-19; all three exit 1, distinct causes).** `SKILL.md:701-704`
(checklist item 5) names only the round-7 command and no expected verdict (D11 box-3: "N1 — NOT
closed by text"). R06-F7 independently reproduced the three distinct causes and fixed the
requirement: an N1 errata is correct only if it states a **distinct expected verdict per round**
(`review/R06-calib-review.md:192-206`).

Captured this seat at HEAD `139e3b6` (tree = HEAD + this round's in-flight edits; `LOG.md`
modified in the working tree by another writer, not this seat):

- `python3 -B reports/round-5/run-validation.py` → **exit 1**; `acceptance_checks_passed: false`;
  `F` = `non-append corpus edit: ('corpus/lessons/supplement-opencode-1/sources/ottoman.json', 'OTT-06')`;
  `O` = `tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` → 7
  `could-not-evaluate reason=gate_digest_mismatch` rows ("on-disk bytes are not the pinned
  revision" for gates repaired after round 3).
- `python3 -B reports/round-6/run-validation.py` → **exit 1**; `error: "historical file changed: .gitignore"`
  (compared against its BASE; `.gitignore` was legitimately edited later — `git log --oneline -- .gitignore` → `94ca098` round-10).
- `python3 -B reports/round-7/run-validation.py` → **exit 1**; failures: preservation
  (`historical file changed vs BASE: .gitignore`), `inventory: historical knowledge totals changed`,
  `claim F: wrong rejection for duplicate-parent-receipt-does-not-inflate`, and
  `previous_acceptance: previous round-6 acceptance failed`; its `O` leg is green
  (`positive 5/5`, `domain 16/16`, `malformed 4/4`, `frozen 5/5`), `O_passed: true`.

**Isolation is load-bearing (R06-F9, `review/R06-calib-review.md:238-264`).** Re-running round 5
and round 7 **rewrites their filed `validation.json` in place** (round 5's diff is substantive:
the `O` error and a `tested_file_sha256` change; round 6 is byte-stable by luck); R06 restored
both via `git checkout --`. This seat's own runs left the receipts at their HEAD digests
(`73a66f74…` / `32c621ef…` / `2f4c1e15…`, verified 2026-10-19), so nothing is owed — but a cold
runner following "re-run every cited command" must clone first. The errata text says so.

### Draft 4 — `SKILL.md:701-704` (append to checklist item 5; item text otherwise unchanged)

before:

```
5. Run `python3 reports/round-7/run-validation.py` for the original F/O
   thresholds, input preservation and old-surface regressions. It writes its
   own receipt, not historical receipts. Fresh source access and invented
   model consistency are causally separate checks.
```

after:

```
5. Run `python3 reports/round-7/run-validation.py` for the original F/O
   thresholds, input preservation and old-surface regressions. It writes its
   own receipt, not historical receipts. Fresh source access and invented
   model consistency are causally separate checks. **Expected verdicts at HEAD
   (dated 2026-10-19; each exits 1 by design — a regression is a different
   output, not this), and run them in a disposable clone: round 5 and round 7
   rewrite their own filed `validation.json` in place (round 6 is byte-stable).**
   round-5 `run-validation.py` → `acceptance_checks_passed: false` with F =
   non-append corpus edit (`supplement-opencode-1/sources/ottoman.json`, OTT-06)
   and O = seven `gate_digest_mismatch` could-not-evaluate rows replaying
   `tools/gates/frozen/round-3/MANIFEST.tsv` against gates repaired after round 3;
   round-6 `run-validation.py` → `historical file changed: .gitignore` vs its
   BASE; round-7 `run-validation.py` → preservation (`.gitignore`), historical
   knowledge-inventory totals, one claim-F rejection, and the round-6 predecessor
   check, while its O leg passes (5/5, 16/16, 4/4, frozen 5/5).
```

**Rationale.** N1 asks for dated errata, not a repair of the historical scripts (their inputs
are historical by design). The block is the smallest text that makes the commands
executable-by-verdict for a cold reader: three commands, three distinct named causes, one shared
expected exit, plus the isolation sentence R06-F9 shows is required rather than advisory.

**Verification commands** (in a clone/worktree, not in place):

```
git clone . /tmp/c14-clone && cd /tmp/c14-clone
for r in 5 6 7; do python3 -B reports/round-$r/run-validation.py >/tmp/rv$r.out 2>&1; echo "round-$r EXIT=$?"; done
head -8 /tmp/rv5.out; head -3 /tmp/rv6.out; head -20 /tmp/rv7.out
```

## Fix 5 — conditional extras (NOT among the canonical twelve; apply only on explicit instruction)

These two r24 residuals are outside K03's twelve (K03 §3 lists the boundary calls; neither R5
nor R7 is in the canonical set). They are drafted only because they sit in the same table and
are pointer-level.

### 5a — r24 R5: `language-contact.md:78-79` → `:80-81` (`SKILL.md:485`)

before:

```
| A borrowed form judged only against the native stratum | misfile: loans pass through the recipient's phonotactic filter and carry donor provenance (`language-contact.md:78-79`) |
```

after:

```
| A borrowed form judged only against the native stratum | misfile: loans pass through the recipient's phonotactic filter and carry donor provenance (`corpus/knowledge/linguistics/language-contact.md:80-81`) |
```

Rationale: `:78` is the intro line ("Two principles worth their weight in canon:"); the two
principles are `:80-81` (verified live). The path prefix also removes the bare-name ambiguity
r24 R5 names (`reports/round-24/skill-audit.md:79`).

### 5b — r24 R7: cause attribution at `SKILL.md:213` (one-line touch-up; `to-verify`)

`SKILL.md:213` reads "cited `:369` before the round-22 `carry_findings` block landed above it".
r24 measured the message still at `:369` at round-18 `e571894` and at `:387` by round-20
`35b6797` (`reports/round-24/skill-audit.md:81`), so the cause is off by up to two rounds.
Draft: replace that clause with "cited `:369` at round-18 `e571894`, `:387` by round-20
`35b6797`". **`to-verify`:** the two hashes are r24's measurement; this seat did not re-run the
cross-revision check.

## Items with no bounded edit draft (named, with the reason — no draft is not a silent drop)

| id (K03) | item | why no edit draft | pointer |
|---|---|---|---|
| OI-01 | 12 D4 garment-form holds + owed slots | design debt by design; clearing it is a design act | `reports/round-24/box2-d4.md:104-108` (K03:62) |
| OI-02 | `head2` empty proper domain | named craft gap (identity, not derivation) | `reports/round-26/register/design.md:228` (K03:63) |
| OI-03 | RL-3 register-lexicon ceiling | recorded as a constraint, not a defect | `corpus/knowledge/linguistics/register-lexicon-ceilings.md:6` (K03:64) |
| OI-08 | lore-owned: bilateral same-revision read outstanding | other lane's province — this lane may not edit or absorb it | K03:69; `corpus/knowledge/synthesis/worldbible-integration-contract.md:15` |
| OI-09 | lore-owned: L0 contract-digest ratification | same; routed, not absorbed | K03:70; `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:45` |
| OI-10 | calibrated numeric rubric undefined | operator/protocol ruling, not a text fix; a seat draft would invent the standard — C07 §Primary reaches the same disposition on two filed grounds (r26 refused to paper it over; the standard is the operator's) | K03:71; `SCORECARD.md:13-14`; `reports/round-33/calib/C07-item-07.md:65-70` |
| OI-11 | devin availability could-not-evaluate | a record class, not an editable artifact; re-observation is telemetry work | K03:72; `reports/round-29/recount/dispositions.md:22` |
| OI-12 | r18 D4-adapter baseline supersession semantics | routed observation about pin semantics; a text edit would prejudge the operator's rule | K03:73; `reports/round-31/final-sweep.md:187-192` |

## Machine-checkable after-set (R06's checker, run 2026-10-19)

R06's pointer checker is filed as source in `review/R06-calib-review.md:287-388` (to be applied
by the integrator at `reports/round-33/review/R06-c14-pointer-check.py`; not on disk at this
seat's close — `ls reports/round-33/review/` → the six review fragments only). This seat
extracted it to `.scratch/c14/r06-pointer-check.py` and ran it:

- `--selftest` → exit 0, "selftest: 2/2 cases correct".
- On the **full draft file** → exit 1, `resolved=493 findings=70`. That count is **expected and
  not a defect signal**: the checker scans every backticked `path:LINE` token, so it flags
  (a) the verbatim before-block quotes of the *known-bad* pointers
  (`loanword-material-dating.md:26`, `:57`, `:60`, `worldbible-integration-contract.md:183` —
  4 of the 70, and exactly the cites these drafts remove), (b) blank lines inside cited
  fragments quoted from other seats' files, and (c) bare relative names such as
  `22-label-representation.md:131-132` as written in `SKILL.md` house style, which the checker
  cannot resolve from the repo root.
- On the **after-set below** (every pointer this file proposes, in full repo-relative form) →
  exit 0, `resolved=46 findings=0`. This is the run that answers R06 §9 step 2's question.

```
`corpus/knowledge/synthesis/loanword-material-dating.md:30-31,63`
`corpus/knowledge/synthesis/loanword-material-dating.md:59,63`
`tools/harness/packet_uncertainty.py:205,209`
`reports/round-15/handoff/v2-design.md:126,131-139`
`tools/d2-typed-labels.py:410`
`tools/d2-typed-labels.py:411`
`tools/d2-typed-labels.py:419-422`
`tools/d2-typed-labels.py:500`
`tools/d2-typed-labels.py:520`
`tools/d2-typed-labels.py:529`
`tools/d2-typed-labels.py:694-695`
`tools/d2-typed-labels.py:768-769`
`tools/d2-typed-labels.py:774-775`
`tools/d2-typed-labels.py:810-814`
`tools/d2-typed-labels.py:859`
`tools/d2-typed-labels.py:3195`
`reports/supplement-opencode-1/22-label-representation.md:126-128`
`reports/supplement-opencode-1/22-label-representation.md:131-132`
`corpus/knowledge/linguistics/language-contact.md:80-81`
```

**Checker-limits note (for R06/integrator).** The checker's §9 step-2 expectation ("exit 0" on
`C14-fix-drafts.md`) cannot hold for any draft that quotes its before-text verbatim, because
`PTR` does not distinguish a quoted bad cite from a proposed one. The after-set block above is
the machine-checkable object; R06 §3's clause-coverage table still has to be applied by hand to
the before/after pairs, which is what R06 §7 already says the checker cannot do.

## Application notes for the integrator

1. Apply Fixes 1-4 to `SKILL.md` only (Fix 5 only on instruction). No corpus file is edited by
   any draft; `corpus/knowledge/synthesis/loanword-material-dating.md` and
   `worldbible-integration-contract.md` keep their bytes.
2. `SKILL.md` sha at this seat's cut: `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d`
   (last commit `17e90b9`); line numbers above are valid at that digest — re-locate by content if
   the integrator's tree differs. Every after-text is a **same-line-count** replacement
   (`SKILL.md` line numbers do not shift), matching C04 §2's house style.
3. Fixes 3b/3c change a verdict word, not just a pointer: they are the only drafts here that
   alter a claim, and both state the behavior measured by the probe. Review them as errata
   (`D2L-DATA` fail vs hold), not as pointer hygiene.
4. Post-application battery: `python3 -B tools/d2-typed-labels.py --selftest` (163/163, exit 0),
   `python3 -B tools/harness/packet_uncertainty.py --selftest` (19 checks, exit 0), the
   Fix 1/2/3 verification commands, and Fix 4's clone loop. `SKILL.md` edits invalidate the
   box-1 survey pin `79fe91d3…` — re-run `python3 -B reports/round-30/craft/box1-survey.py`
   (expect 28/28, exit 0), record the new digest, and check pin-cascade exposure against
   `reports/round-33/adj/A09-pins.md`.
5. No draft touches `reports/round-1..32/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**`.
6. Reviewer route: R06 §3's clause-coverage table is the intended meaning judgment; R06's
   checker is filed as source at `review/R06-calib-review.md:287-388` and this seat's runs are
   reported in the after-set section above (after-set: exit 0, 46 resolved, 0 findings). The
   two divergences (R06-F3 scope, R06-F5 retired-vs-live tokens) are reconciled above rather
   than left silent.

## Owed

- `reports/round-33/calib/C05-item-05.md` (OI-05 owner) — absent at this seat's close; Fix 2's
  disposition class (`fixable-now` vs `carried`) and the ledger row's `evidence` field bind to it.
- `reports/round-33/calib/C06-item-06.md` (OI-06 owner) — absent; Fix 3 binds to it.
- `reports/round-33/calib/C09-item-09.md`, `C10-item-10.md` — absent (OI-09/OI-10 dispositions).
- `reports/round-33/calib/C13-consistency.md`, `C15-ledger-draft.json` — the ledger's `evidence`
  column should cite this file's verification commands for OI-04..OI-07.
- R06's third-pass verdict on this file's actual bytes (its §9 steps 3-5) — the answer key is
  filed; the verdict is owed by the R06/integrator side.
- The only genuinely open draft question: Fix 3d is offered in two sizes (full / minimal
  variant); both are byte-verified. Integrator picks one.

## Citations

Files read (paths relative to repo root; line numbers as of the 2026-10-19 cut):

- `SKILL.md:128,213,479,481,483,485,486,488,490,491,501,701-704` (sha256 `79fe91d3…`, `git log -1` → `17e90b9`)
- `corpus/knowledge/synthesis/loanword-material-dating.md:26,27-34,29,30,31,56,57,59,60,63` (sha256 `5b1d75ab…`, `git log -1` → `e1694ba`)
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:15,179,182-187,183` (sha256 `5f4c02bf…`, 209 lines)
- `corpus/knowledge/linguistics/language-contact.md:78,80,81`
- `tools/d2-typed-labels.py:410,411,419-422,500,520,529,549,565,694-695,711,738-742,751,768-769,774-775,783-788,810-814,830,859,3193,3195`
- `tools/harness/packet_uncertainty.py:84-90,205,209`
- `reports/round-33/calib/K03-open-items.md:55-78,80-90` (canonical ids + boundary calls)
- `reports/round-33/calib/C04-item-04.md` §1.1-§1.4, §2, §3.1-§3.3 (item-owner drafts)
- `reports/round-33/calib/C07-item-07.md:65-70` (rubric carry disposition, corroborating OI-10)
- `reports/round-33/review/R06-calib-review.md:47-168` (answer key, F1-F5), `:192-206` (F7),
  `:238-264` (F9 + filed-receipt digests), `:266-388` (checker)
- `reports/round-24/promotion-review.md:71-88,176-196`
- `reports/round-24/skill-audit.md:75-81`
- `reports/round-10/drift/shard-05.md:32,35,37,46,54`
- `reports/round-11/depth/shard-gate-adapter.md:120-125`
- `reports/round-15/handoff/v2-design.md:126-139`
- `reports/round-31/final-sweep.md:187-192`
- `reports/round-32/dossier-d13-operator-decisions.md:128-138`
- `reports/round-32/dossier-d11-shonen-boxes.md:53-75,145-153,203-208`
- `SCORECARD.md:13-14`

Commands run (2026-10-19, all inside the repo, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `git diff e1694ba~1 e1694ba -- corpus/knowledge/synthesis/loanword-material-dating.md` (hunk `@@ -2,6 +2,9 @@`)
- `git log --oneline -S "loanword-material-dating.md:26,60" -- SKILL.md` → `e1694ba`
- `git show e1694ba~1:corpus/knowledge/synthesis/loanword-material-dating.md` (pre-commit pointers `:26`, `:60`)
- `grep -c` per anchor token over `tools/d2-typed-labels.py` → 0 each
- `python3 -B tools/d2-typed-labels.py --selftest` → exit 0, 163/163
- `python3 -B tools/harness/packet_uncertainty.py --selftest` → exit 0, 19 checks
- in-process probe (Fix 3 block) → kindless exit 2 `D2L-DATA`; no-bytes exit 2 `D2L-DATA`×2; owed-slot exit 1 `D2L-FORM-UNRESOLVED`
- `python3 -B reports/round-{5,6,7}/run-validation.py` → exit 1 each, causes as quoted in Fix 4
- `sha256sum reports/round-{5,6,7}/validation.json` vs `git show HEAD:…` → `73a66f74…`, `32c621ef…`, `2f4c1e15…` (filed digests intact)
- `git status --porcelain` → ` M LOG.md`, `?? REGIMEN.md`, `?? reports/round-33/`
