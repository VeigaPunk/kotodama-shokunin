- Seat: Ca01 | executor | claim O | date 2026-10-19 | baseline ac47c78

# Ca01 — spare gap-fill, claim O (operability)

Assignment: `reports/round-42/targets.json:161` (seat `Ca01`, role `executor`,
claim `O`, out `calib/Ca01-gap-fill.md`), mission "Spare gap-fill across both
blocks." Two items below are unowned. The round's own claim-O text names the
wrapped-field defect (`reports/round-42/claims.json` claim O `before`) and
assigns the *fix* (O01/O02/O04/O05), a *forward-looking* predicted census for
the fixed logic (O03, `targets.json:58`), and the *policy arithmetic* check
(O12) — but no seat owns the r39-owed **retroactive corpus-wide recount that
must reconcile against the filed 2504**, and no seat owns C06's rev-2.4 vector
slot order. Both are discharged here as drafts. This seat's numbers are
offered as O03's reproduction target, not as a substitute for O03's own run.
**No filed byte was edited; no `run-validation.py` was executed; no git,
network, or install action was taken.**

## 1. The r39-owed corpus-wide block-parser recount — CLOSED (to-verify discharged)

`reports/round-39/calib/Ca04-verify.md:114-115` files this as owed: "a full
block-parser couples recount corpus-wide (this seat's partial: exactly 1
wrapped field, 4 tokens, 2 phantom — commands above)." It has not been run
since: no round-40/41/42 seat's `out` claims it. This seat ran it.

**Method.** Read-only script, run from the lane root with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. Two extractors over the
same 220-entry live corpus:
- **single-line** — `re.search(r"^- couples:\s*(.*)$", text, re.M)`, byte-equal
  to `reports/round-19/audit/entry-audit.py:75` and to r39 policy §1.
- **block parser** — `frontmatter_block()` + `fields_of()`, transcribed
  byte-for-byte from `reports/round-35/cov/C14-audit-6-10.md:208-236` (the
  `- key:` continuation walk).
Token regex `[A-Za-z0-9_./{},\-]+\.md` + one-level brace expansion
(`entry-audit.py:31,34-42`), deduplicated per entry; classification per
`entry-audit.py:87-95` (Tier 1 three bases) then the r39 policy §2 Tier 2
(slash-free unique-basename fallback). The script is inlined here rather than
left in `.scratch` so the recount is reproducible after scratch cleanup; paste
it to a file and run `python3 -B <file>` from the lane root.

```python
import glob, os, re
LANE=os.getcwd(); KNOW=os.path.join(LANE,"corpus","knowledge")
MDREF=re.compile(r"[A-Za-z0-9_./{},\-]+\.md"); BRACE=re.compile(r"\{([^{}]*)\}")
FIELD_RE=re.compile(r"^- ([a-z-]+):", re.M)
def expand(s):
    m=BRACE.search(s)
    if not m: return [s]
    out=[]
    for part in m.group(1).split(","): out.extend(expand(s[:m.start()]+part+s[m.end():]))
    return out
IDX={}
for p in glob.glob(os.path.join(KNOW,"*","*.md")):
    IDX.setdefault(os.path.basename(p),[]).append(os.path.relpath(p,LANE))
def frontmatter_block(text):
    lines=text.splitlines(); start=None; end=len(lines)
    for i,line in enumerate(lines):
        if re.match(r"^- [a-z-]+:",line):
            if start is None: start=i
        elif start is not None and line.startswith("## "): end=i; break
    return "" if start is None else "\n".join(lines[start:end])
def fields_of(block):
    out={}; cur=None
    for line in block.splitlines():
        m=FIELD_RE.match(line)
        if m: cur=m.group(1); out[cur]=[line.split(":",1)[1].strip()]
        elif cur and line.strip(): out[cur].append(line.strip())
    return {k:"\n".join(v) for k,v in out.items()}
def sl(text):
    m=re.search(r"^- couples:\s*(.*)$",text,re.M); return m.group(1) if m else ""
def refs(f):
    out=set()
    for raw in MDREF.findall(f):
        for c in expand(raw): out.add(c.strip())
    return out
def cls(r,ed):
    for b in (ed,LANE,KNOW):
        if os.path.isfile(os.path.normpath(os.path.join(b,r))): return "direct",None
    if "/" in r: return "unresolved",None
    h=IDX.get(os.path.basename(r),[])
    if len(h)==1: return "fallback",h[0]
    return ("ambiguous",None) if len(h)>1 else ("unresolved",None)
files=sorted(glob.glob(os.path.join(KNOW,"*","*.md")))
for name,ex in (("single-line",sl),
                ("block",lambda t: fields_of(frontmatter_block(t)).get("couples",""))):
    a=dict(direct=0,fallback=0,ambiguous=0,unresolved=0); tok=0; U=[]
    for p in files:
        t=open(p,encoding="utf-8",errors="replace").read(); f=ex(t); tok+=len(refs(f))
        for r in sorted(refs(f)):
            c,m=cls(r,os.path.dirname(os.path.abspath(p))); a[c]+=1
            if c=="unresolved": U.append((os.path.relpath(p,LANE),r))
    print(f"[{name}] entries={len(files)} tokens={tok} {a}")
    for p,r in U: print(f"   {r}   <- {p}")
```

**Result — the r39 count reproduces exactly, and both instruments agree on the
four classes at the live tree (220 entries, 2026-10-19):**

| extractor | tokens | direct | fallback | ambiguous | unresolved |
|---|---|---|---|---|---|
| single-line (r19/r39 §1) | 2607 | 2435 | 166 | 0 | 6 |
| block parser (C14 `fields_of`) | 2611 | 2437 | 166 | 0 | 8 |

Reconciliation against the filed r39 number: r39 measured 212 entries →
`2504 = 2335 + 163 + 0 + 6`. The 8 entries landed since (4 verification, r39;
4 linguistics, r40 — `corpus/README.md:5-20`) contribute exactly **103**
`couples:` tokens under the single-line extractor (measured per entry: 20/12/
12/16/10/10/11/12), and `2504 + 103 = 2607` — an exact match, so the r39
census is reproduced, not merely consistent.

**The r39 `to-verify` sub-question ("C14's 8/7-distinct count … includes the
mangled token `prosody.md`, split from `tone-prosody.md` by the line break —
to-verify, not re-derived") is now DERIVED, and the mechanism is confirmed as
a real, reproducible extractor hazard:**

- The wrapped field is `corpus/knowledge/linguistics/phonetics-phonology.md:73-77`
  (block parser: 4 tokens; single-line: 0 tokens) — **wrapped-field count = 1**,
  confirming `Ca04-verify.md:82-83` exactly.
- The block parser's 4 tokens are `sound-change.md`, `prosody.md`,
  `sound-symbolism.md`, `writing-systems.md`. The field's *prose intent* is
  `tone-prosody.md` (line 76 ends `… sound-change.md, tone-` and line 77 opens
  `prosody.md, …`). Raw `MDREF.findall` over the block value (newlines intact)
  yields `prosody.md`, **not** `tone-prosody.md`; joining the continuation lines
  with a space yields the same; only re-joining with the hyphen yields
  `tone-prosody.md`. So `Ca04`'s hypothesis is **confirmed by construction**:
  the token is mangled at the line break, and `tone-prosody.md` never appears
  as a token in any current instrument.
- The "2 phantom" count also verifies: of the 4 named targets, `sound-symbolism.md`
  and `writing-systems.md` exist (`corpus/knowledge/linguistics/`), while
  `sound-change.md` and `tone-prosody.md` do not (`find corpus -name` → no such
  files; the nearest is `verification/phonology-sanity-gate.md` for the
  unrelated `phonology-sanity.md`). Confirms `Ca04-verify.md:84`.

**Corrected-baseline caveat that O03/O12 must carry (the claim-O accounting).**
The claim text (`reports/round-42/claims.json`, claim O `after_required`) asks
the recount to re-derive "the r39 policy's 2504 = 2335 + 163 + 0 + 6 … with the
2 phantom attributions dispositioned". This seat's independent reading is that
those two legs do **not** sit on the same extractor, and a corrected census
must say which one it means:

- **Under the policy §1 single-line extractor (the instrument that produced
  2504):** the corpus-wide unresolved set is 6 rows / **5 distinct tokens** —
  `-gate.md` x1 (glob fragment, `verification/gate-frozen-run-standard.md:15`),
  `../linguistics/phonology-sanity.md` **x2** (r19 X26-1 phantom, live at
  `verification/label-channel-routing-verification.md:14` **and** at
  `synthesis/typed-label-routing-workflow.md:16`), and `phonology-basics.md`,
  `naming-and-onomastics.md`, `honorifics-and-register.md` x1 each
  (`linguistics/language-contact.md:7`). All five are attributed; **the
  arithmetic 2607 = 2435 + 166 + 0 + 6 reproduces exactly.**
- **Under the block parser (the instrument the fix lands):** 2611 = 2437 + 166 +
  0 + **8**, i.e. the same 6 rows plus the 2 wrapped-field rows
  (`sound-change.md`, `prosody.md` in `phonetics-phonology.md`). Both extra rows
  are non-phantom-class findings about the *field's own bytes* — `sound-change.md`
  is a genuine never-written prospective sibling, and `prosody.md` is the
  line-break mangling — and neither is a phantom *attribution*.

So: **the "2 phantom attributions" are not a block-parser delta.** They are the
two live carriers of the single phantom token `../linguistics/phonology-sanity.md`
(the path `linguistics/phonology-sanity.md` does not exist; only
`verification/phonology-sanity-gate.md` does). `Ca04`'s D1 conflates the
"2 phantom attributions" (carriers) with the wrapped field's "2 phantom
targets" (nonexistent files). **Both dispositions are now named, which is what
the claim's `after_required` needs:** the second carrier of the X26-1 phantom —
which `R01-review.md:271-274` (R01-7) filed as an *incomplete attribution in
Ca03's Part 2* and required the integrator to "complete the phantom's
second-carrier attribution" — is
`corpus/knowledge/synthesis/typed-label-routing-workflow.md:16`, measured this
seat. The r39 policy's Part 2 attributes the phantom to one file only
(`Ca03-basename-policy.md:270-274` names `label-channel-routing-verification.md:14`).

**Two further discrepancies this recount surfaces (both for O12/O04, both
`to-verify` until the fixed instrument runs):**

1. **Fallback count.** r39 filed 163 fallback at 212 entries; this seat
   measures **166** at 220 under the policy's slash-free Tier 2. The 3-ref
   delta is not attributable from this seat's data alone (the 8 new entries
   contribute 103 tokens; the split direct/fallback among them is
   `to-verify`). O03's predicted census should state 166, and O04 should
   confirm or contest it — the number is load-bearing for the policy's §3.1
   "fallback count beside every zero-unresolved claim".
2. **`ambiguous` is empty corpus-wide (0), and no duplicate basename exists.**
   `IDX` has 220 distinct basenames over 220 files → 0 cross-partition
   duplicates, so policy §2(b)'s "two or more → `ambiguous`" branch and §5.5's
   re-adjudication trigger are currently unexercised. A synthetic fixture (O05's
   adversarial job) is the only way to test that branch; no live instance exists.

**New operability hazard found (not in any round-42 seat's mission): a
`couples:` field that swallows the *whole* remaining header.** A first pass at
this seat used `FIELD_RE = r"^- (topic|sources|couples):"` — the field-name set
from `tools/gates/provenance-audit.py:75-76` — instead of C14's
`r"^- ([a-z-]+):"`. Because the parser then never sees `- source:` /
`- verified-at:` / `- recheck:` as field boundaries, the `couples` value ran to
the end of the file and captured **3396** tokens (vs 2611 correct). The
corpus-wide wrapped-field detector is also sensitive to this: with the C14
semantics exactly **1** entry's single-line and block captures differ
(`phonetics-phonology.md`); the naive variant reported 7 false wrapped fields
(any entry whose header is followed by a `## ` heading at a non-`- ` line).
This is a concrete, reproducible false-green surface for O01/O02: the block
parser's field-name regex **must** stay `[a-z-]+` (C14 `:210`), and any
successor instrument should carry a control that pins it. `to-verify`: whether
`tools/gates/provenance-audit.py:76`'s three-name `FIELD_RE` is used anywhere
for couples extraction; if it is, that call site shares the defect.

## 2. C06's rev-2.4 vector has two slots swapped (coverage, claim C)

`reports/round-42/targets.json:163` (seat C06) requires the rev-2.4 delta to
carry "vector 25/23/27/25/24/94". The live README establishes the slot order
unambiguously, and that target does not match it.

**Order, established three ways this seat:**
- Section headers, in file order: `## linguistics/ (25)` `:168`, `## myth-symbol/
  (23)` `:196`, `## culture-material/ (25)` `:222`, `## synthesis/ (29)` `:249`,
  `## verification/ (24)` `:281`, `## civilizations/ (94)` `:308`.
- Footer (`corpus/README.md:536`): `(total 220 files; directory totals
  25/23/25/29/24/94)`.
- `python3 -B reports/round-28/readme/sweep.py`: `footer_live {"dir_totals":
  [25, 23, 25, 29, 24, 94], "order": ["linguistics","myth-symbol",
  "culture-material","synthesis","verification","civilizations"]}`, `footer_ok
  True`, exit 0.

All three agree: slot 1 `linguistics`, slot 2 `myth-symbol`, slot 3
`culture-material`, slot 4 `synthesis`, slot 5 `verification`, slot 6
`civilizations`. The two filed revision vectors use this same order —
rev-2.3 (`:10-11`) `21/23/25/29/24/94 → 25/23/25/29/24/94` (moves
`linguistics` 21 → 25, slot 1) and rev-2.2 (`:19-20`)
`21/23/25/29/20/94 → 21/23/25/29/24/94` (moves `verification` 20 → 24, slot 5).
Both are arithmetically correct against live counts.

Claim C adds 4 entries to `myth-symbol` (23 → 27) and touches no other
partition. The correct rev-2.4 vector is therefore **`25/27/25/25/24/94`**:
slot 2 = 27 (`myth-symbol`), slot 3 = 25 (`culture-material`, unchanged).
C06's stated `25/23/27/25/24/94` puts **23 in slot 2 and 27 in slot 3** — it
assigns `myth-symbol`'s new value to the `culture-material` slot and leaves
`myth-symbol` at its old 23. That is a two-token fix in C06's draft; it should
be checked in C05/C07's verification, because a wrong vector in the revision
history is exactly the class of defect rev-2.0's repair note
(`corpus/README.md:24-26`) documents having been burned by before.

**Correction to my own first reading, recorded for honesty:** I first suspected
a defect in the *filed* rev-2.3 line and briefly considered a mis-ordering
there. On re-reading, both filed vectors are correct and the sweep reports
`footer_ok True`. **No defect is filed against any filed README byte by this
seat**; the finding is confined to C06's round-42 draft target.

Pre-landing coverage checks this seat ran against the live tree (all green):
`ls corpus/knowledge/myth-symbol/*.md | wc -l` → **23** (so claim C's 23 → 27
starts from a verified base); `ls corpus/knowledge/*/*.md | wc -l` → **220**;
`python3 -B reports/round-28/readme/sweep.py` → `rows 220 files 220`,
`missing_from_index 0 []`, `topic_mismatch 0 []`, `orphan_rows 0 []`,
`totals_ok True`, `footer_ok True`, `readme_sha256
d2eed26b30e8e62189d95446dae7d5503b6c6a398bb8e77348f878c947a5ac4f`, exit 0.

## 3. Cross-check offered to O12 (r39 policy arithmetic)

O12's mission is to verify "the r39 policy document's arithmetic still holds
under the corrected census". This seat's independent reading, stated so O12 can
agree or contest: **the policy's §1 extractor definition and its filed 212-entry
arithmetic both hold** (`2504 = 2335 + 163 + 0 + 6` reproduces; the 220-entry
successor is `2607 = 2435 + 166 + 0 + 6`), and the *only* change a corrected
census forces is the §5.6 glob-fragment class (`-gate.md`) and the X26-1
phantom's **second carrier**. The policy's Part-2 text is not wrong about the
phantom; it is incomplete by one carrier line. The D1 exception the policy
declines to adopt (block extraction) is, per §1 of this fragment, the correct
call for the *policy* (which fixes the reporting population) — the block parser
belongs to the *successor instrument* the claim-O fix lands. Policy and fix do
not conflict; they must simply state which population each reports.

## Owed

- **Integrator/O03/O04**: the fixed instrument's predicted and verified census
  must state the extractor it uses. Under single-line: `2607 = 2435 + 166 + 0 + 6`.
  Under the block parser (the fix): `2611 = 2437 + 166 + 0 + 8`. Both are filed
  above with their row-level attribution; O03 should reproduce one and say which.
- **Integrator/O12**: fold the phantom's **second carrier**
  (`corpus/knowledge/synthesis/typed-label-routing-workflow.md:16`) into the
  successor note that disposition the X26-1 phantom — this discharges
  `R01-review.md:271-274` (R01-7) and `Ca03-basename-policy.md:306-312`'s
  "to-verify: whether the unresolved trio … and the X26-1 phantom get repair
  dispositions". This seat names the carrier; it does not disposition the repair.
- **Integrator/C06**: check the rev-2.4 vector's slot order (§2 above) before
  landing; the target's `25/23/27/25/24/94` and the footer order
  (`linguistics` first) disagree in slots 2–3.
- **to-verify**: (a) the 163 → 166 fallback delta's per-entry split; (b) whether
  `tools/gates/provenance-audit.py:76`'s three-name `FIELD_RE` is used for any
  couples extraction in-tree (the swallowing hazard of §1); (c) the `ambiguous`
  branch has no live instance — needs O05's synthetic fixture.
- **Not done, out of scope**: no corpus byte, no `entry-audit.py`, no policy
  document, and no README byte was edited. The fix itself (O01–O05) is not this
  seat's mission; this fragment supplies the corpus-wide measurement it must
  reproduce.

## Citations

- Assignment: `reports/round-42/targets.json:161` (Ca01 out
  `calib/Ca01-gap-fill.md`); claim O `before`/`after_required`:
  `reports/round-42/claims.json` (claim `O`, `before` "N6 (queue-v2) … 0 tokens
  captured vs 4 named, 2 phantom attributions in the census", `after_required`
  "the corpus-wide recount re-derives the reference census"); seat roster with
  no owning seat for this recount: `reports/round-42/targets.json:1-160`.
- Owed item being closed: `reports/round-39/calib/Ca04-verify.md:114-115`
  (to-verify: full block-parser recount corpus-wide) and `:82-89` (D1: wrapped
  field, 4 named / 0 captured, 2 phantom, `prosody.md` mangling `to-verify`).
- r39 filed census and attribution: `reports/round-39/calib/Ca03-basename-policy.md:258-290`
  (Part 2 `212/2504 → 2335/163/0/6`, 5 distinct, all attributed),
  `:306-320` (Owed/to-verify), `:326-350` (Citations). Landed policy:
  `reports/round-39/calib/basename-couples-policy.md:1-107` (§1 extraction
  `:14-23`, §2 tiers `:24-46`, §3 reporting `:47-58`, §5 limits `:59-...`,
  §6 recipe).
- Extractor code: `reports/round-19/audit/entry-audit.py:31,34-42,74-96`
  (MDREF `:31`; braces `:34-42`; single-line capture `:75`; candidates `:87-95`).
- Block parser transcribed: `reports/round-35/cov/C14-audit-6-10.md:208-236`
  (`frontmatter_block` `:208-220`, `fields_of` `:225-236`), `:249-288`
  (index `:252-260`, classes `:271-288`, slash-bearing basename key `:281`).
- D1 instance bytes: `corpus/knowledge/linguistics/phonetics-phonology.md:73-77`
  (field; line 76 ends `tone-`, line 77 opens `prosody.md`).
- Phantom carriers: `corpus/knowledge/verification/label-channel-routing-verification.md:14`
  and **`corpus/knowledge/synthesis/typed-label-routing-workflow.md:16`** (second
  carrier, this seat). Provenance: `reports/round-19/audit/x26-spotcheck-entries.md`
  §3 as quoted at `reports/round-35/cov/C14-audit-6-10.md:114-119`.
- Unresolved trio: `corpus/knowledge/linguistics/language-contact.md:7`.
- Glob fragment: `corpus/knowledge/verification/gate-frozen-run-standard.md:15`.
- Review requirement: `reports/round-39/review/R01-review.md:271-274` (R01-7
  second-carrier attribution).
- README surfaces: `corpus/README.md:5-13` (rev 2.3), `:15-20` (rev 2.2),
  `:24-26` (rev-2.0 repair note), `:196` (`## myth-symbol/ (23)`), `:532`
  (`Total knowledge entries: 220.`), `:536` (footer `25/23/25/29/24/94`).
  Target vector: `reports/round-42/targets.json:163`.
- Hazard surface: `tools/gates/provenance-audit.py:75-76` (`FIELD_NAMES` /
  three-name `FIELD_RE`).
- Command outputs (this seat, 2026-10-19, lane root, tree at `ac47c78`,
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all read-only):
  (a) `.scratch/ca01/recount3.py` → single-line `2607 = 2435 + 166 + 0 + 6`,
  6 unresolved rows / 5 distinct; block parser `2611 = 2437 + 166 + 0 + 8`,
  8 rows / 7 distinct; both listed with row attribution; `ambiguous = 0`.
  (b) wrapped-field detector (C14 semantics) → **1** entry differs
  (`phonetics-phonology.md`); the naive three-name-`FIELD_RE` variant → 3396
  tokens and 7 false wrapped fields. (c) `MDREF` on the raw field with newlines
  → `prosody.md`; with hyphen-join → `tone-prosody.md`; per-entry new-entry
  token counts 20/12/12/16/10/10/11/12 = **103**; `2504 + 103 = 2607`.
  (d) `ls corpus/knowledge/myth-symbol/*.md | wc -l` → **23**;
  `ls corpus/knowledge/*/*.md | wc -l` → **220**; `find corpus -name
  "phonology-sanity*"` → only `verification/phonology-sanity-gate.md`.
  (e) `python3 -B reports/round-28/readme/sweep.py` → `rows 220 files 220`,
  `missing_from_index 0 []`, `topic_mismatch 0 []`, `orphan_rows 0 []`,
  `totals_ok True`, `footer_ok True`, `readme_sha256 d2eed26b…`, exit 0.
  (f) `IDX` size 220 distinct basenames, 0 duplicates.
