- Seat: R06 | reviewer | claim C | date 2026-10-19 | baseline 139e3b6

# R06 — third pass over `calib/`: C14 fix drafts

## Status: dependency absent — third pass pre-registered with a tested checker

`reports/round-33/calib/` was empty at this seat's cut (`ls -la reports/round-33/calib/`
→ `total 0`, no `C14-fix-drafts.md`). Per the shared missing-dependency rule I
did every part that does not require C14's bytes:

1. **Pre-registered the answer key** — every pointer target C14's drafts can
   legitimately name, resolved against live bytes at baseline `139e3b6`, with the
   exact line text quoted (§2).
2. **Fixed the meaning-preservation invariants** each draft must satisfy, and
   found three places where the obvious re-point would *narrow* the cite (§3).
3. **Built and tested the checker** that will judge C14 the moment it lands
   (§7) — `--selftest` exits 0 on the embedded bytes.
4. **Reproduced N1 and N2 live** (§6), including an in-place rewrite of filed
   round-5/round-7 receipts caused by this seat's own verification run, with the
   filed bytes restored to their HEAD digests.

The judgment of C14's actual before/after text is **owed** (§ Owed).

## 1. Scope and method

Mission: *"Third pass over calib/ with focus on C14 fix drafts (are the proposed
SKILL.md pointer targets real lines? do the drafts preserve meaning?)."*

Two questions, so two independent measurements:

- **"Real lines?"** — resolve each pointer to live bytes; a pointer is real only
  if the target is non-blank *and* carries the rule the row asserts. Non-blank is
  not sufficient (see `:60` in §2.1).
- **"Preserve meaning?"** — read the SKILL.md row, extract every clause it
  asserts, and require the proposed target set to cover all of them. A re-point
  that keeps the row readable while dropping a clause is a regression even
  though the pointer resolves.

The candidates are fixed by the record, not by me: box-1 conditions 2–4 and
cold-run N1 (`reports/round-24/promotion-review.md:71-88`, `:176-196`), carried
at HEAD by `reports/round-32/dossier-d13-operator-decisions.md:133-134` and
`reports/round-32/dossier-d11-shonen-boxes.md:145-147`.

Boundary: this seat wrote exactly one file, `review/R06-calib-review.md`. No
source edits, no filed-byte edits (one was made and reverted — §6.3), no commits.

## 2. Answer key — every C14 pointer target, resolved at HEAD

### 2.1 Box-1 condition 2 — the loanword-dating row (`SKILL.md:486`)

Row under repair (`SKILL.md:486`):

> `| A loan's oldest form used to date the referent's arrival | clock conflation; keep word-entry and object-arrival intervals separate (``loanword-material-dating.md:26,60``; executable B4) |`

The row asserts **two** clauses: (i) a loan's oldest form does not date the
referent's arrival, and (ii) word-entry and object-arrival intervals stay
separate. Live resolution of the current cite:

| pointer | live content | verdict |
|---|---|---|
| `loanword-material-dating.md:26` | *(empty line — line 26 is blank)* | **BLANK-TARGET** |
| `loanword-material-dating.md:60` | `\| Native term replaces a foreign label \| Purism, translation, or changed prestige is possible \| It does not establish withdrawal of the object or people \|` | **NON-SUPPORTING** — that is label-vs-object *persistence*, not word-entry vs object-arrival |

Correct targets, measured:

| pointer | live content | covers |
|---|---|---|
| `loanword-material-dating.md:30` | `\| Lexical \| A word or sense enters a specified speech community \| Arrival of its referent; first surviving written token \|` | clause (i) verbatim — "Arrival of its referent" is explicitly *not* dated |
| `loanword-material-dating.md:31` | `\| Material \| Manufacture, import, imitation, use, repair, or deposition \| All of these at once; identity of every user \|` | clause (ii) — the object clock is its own row |
| `loanword-material-dating.md:63` | `A borrowed *cloth* word can later name a local weave or a different garment. Date the **sense–referent pairing**, not merely the word's oldest ancestor.` | the row's "oldest form" clause |

**Finding R06-F1 (major).** `promotion-review.md:74` records the condition as
":26 is blank; the sense-referent pairing is at :63". A draft that re-points
`:26,60` → `:63` alone **satisfies the recorded condition and still loses clause
(ii)**: `:63` supports the pairing clause but says nothing about keeping the two
clock intervals separate. The minimum meaning-preserving target set is
`loanword-material-dating.md:30-31,63`. I flag this because the condition's own
wording invites the narrowing fix.

### 2.2 Box-1 condition 2 — the prestige row (`SKILL.md:488`)

Row under repair (`SKILL.md:488`):

> `| Imported prestige terminology for locally made goods read as evidence of import | dictionary/selection bias; check local manufacture under imported labels (``loanword-material-dating.md:57``) |`

| pointer | live content | verdict |
|---|---|---|
| `loanword-material-dating.md:57` | `\| Recipient form reflects a donor innovation \| Entry after that innovation in the donor variety \| Parallel recipient change; mistaken immediate donor \|` | **KNOWN-BAD-CITE** — donor-innovation row; no prestige content |
| `loanword-material-dating.md:59` | `\| Loanwords cluster in a craft domain \| Contact concentrated in that practice/register \| Dictionary selection bias; imported prestige terminology for local goods \|` | **correct diagnosis half** — carries "dictionary selection bias" *and* "imported prestige terminology for local goods" verbatim |
| `loanword-material-dating.md:63` | as above — "A borrowed *cloth* word can later name a local weave or a different garment" | **correct remedy half** — this is "local manufacture under an imported label" |

**Finding R06-F2 (major).** The row asserts a diagnosis ("dictionary/selection
bias") *and* a remedy ("check local manufacture under imported labels"). `:59`
carries the diagnosis; the remedy is at `:63`. A `:57` → `:59` re-point is the
fix the condition names and it resolves, but it silently drops the remedy clause.
Minimum set: `loanword-material-dating.md:59,63`.

### 2.3 Box-1 condition 3 — the "basis is never boilerplate" mis-cite

The rule text and its cite appear at **two** SKILL.md sites:

- `SKILL.md:127-128` — "Basis is never boilerplate: unique per claim, its witness must resolve, and a basis that restates the status word is rejected (`worldbible-integration-contract.md:183`; v2-design §2.3)."
- `SKILL.md:501` — `| Two claims share one basis sentence, or a basis restates the status word | boilerplate basis: basis is per-claim evidence whose witness resolves (`reports/round-15/claims.json:14`; `worldbible-integration-contract.md:183`) |`

| pointer | live content | verdict |
|---|---|---|
| `worldbible-integration-contract.md:183` | `- [ ] Every delivered record has scope, stable identity, provenance/invention status, and a disposition question; unknowns are not blank cells.` | **KNOWN-BAD-CITE** — an acceptance-checklist line carrying other content |
| `worldbible-integration-contract.md` (whole file) | `grep -c basis` → **0 matches** | **no re-point target exists in this file** |

**Finding R06-F3 (major).** Condition 3 offers "needs re-point or dated erratum".
The re-point branch is **not available**: the word `basis` occurs zero times in
`worldbible-integration-contract.md` (`grep -n 'basis' <file>` → no output), and
the nearest contract line, `:63` (`| claim_ledger | Statement, claim kind,
source/invention provenance, evidence status, uncertainty, and relation to other
records |`), does not state uniqueness or witness-resolution either. The honest
disposition is **erratum**, and the correct target is named by the row itself:

- the rule's real home is `reports/round-15/handoff/v2-design.md:126`
  (`### 2.3 Zero-boilerplate: what the builder enforces`), whose items 1–2 state
  exactly "status ∈ enum, per claim, no gaps" and "`basis` non-placeholder and
  unique across claims after whitespace normalization — no two claims share a
  basis sentence";
- `SKILL.md:128` already cites that section ("v2-design §2.3"), so **deleting the
  `:183` cite there is meaning-neutral**;
- `SKILL.md:501` already cites `reports/round-15/claims.json:14` (the round-15
  declaration carrying "zero boilerplate"), so **deleting `:183` there is
  meaning-neutral** too.

**Finding R06-F4 (minor, integrator-relevant).** The mis-cite is **two sites, one
defect**. A draft that fixes only `:501` (the row the condition names) leaves
`:128` carrying the same wrong pointer. The origin of the propagation is
`reports/round-15/knowledge/skill-draft.md:95-97`, which carries the identical
sentence with the identical `worldbible-integration-contract.md:183` cite — so a
one-site fix leaves the mis-cite reproducible from the draft.

### 2.4 Box-1 condition 4 — the four dangling anchors

`SKILL.md` names four executable tokens. Search across `tools/` **including**
`tools/gates/frozen/` returns nothing for any of them:

| token | SKILL.md site | `grep -rl <token> tools/` |
|---|---|---|
| `TL-01` | `:479`, `:481` ("executable `TL-01`") | *(no file)* |
| `TL-02` | `:483` ("`tools/d2-typed-labels.py` `TL-02`") | *(no file)* |
| `FIELD_DEFAULTS` | `:491` ("tool `FIELD_DEFAULTS`") | *(no file)* |
| `fictional-coordinate`, `descriptive-gloss` | `:491` | *(no file)* |

Only `SKILL.md` and `SCORECARD.md` contain the tokens; no tool does. The named
tool `tools/d2-typed-labels.py` **does** exist (194,937 bytes) and has a
`--selftest` (`tools/d2-typed-labels.py:44`, `:1389`), but `grep -c 'TL-0'` over
it returns **0** — so `:483`'s cite of "`tools/d2-typed-labels.py` `TL-02`" names
a real file with a token that file does not contain.

**Finding R06-F5 (major, confirms condition 4).** The re-point branch is
unavailable for all four anchors: there is no line anywhere in `tools/` to point
at. Dated errata is the only honest fix, which is what condition 4 already says.
A draft proposing any re-point for these four should be rejected as unverifiable.

## 3. Meaning-preservation summary

| draft target | resolves? | preserves every clause? |
|---|---|---|
| `:26,60` → `:63` | yes | **no** — loses clause (ii) (R06-F1) |
| `:26,60` → `:30-31,63` | yes | yes |
| `:57` → `:59` | yes | **no** — loses the remedy clause (R06-F2) |
| `:57` → `:59,63` | yes | yes |
| `:183` → any line in that contract | **no target exists** | n/a — erratum required (R06-F3) |
| `TL-01`/`TL-02`/`FIELD_DEFAULTS`/gloss types → any tool line | **no target exists** | n/a — erratum required (R06-F5) |

## 4. Box-1 condition 5 — the duplicated status block (measured)

`SKILL.md:101` and `SKILL.md:498` are **byte-identical**: both 555 bytes,
`sha256` prefix `e5fa8fb0` (`python3` comparison of the two lines → `True`).

Context differs, which is what makes the dedupe a real edit rather than a
deletion:

- `:101` sits in `### Claim uncertainty typing` (heading `:77`) directly under the
  three-row status table headed at `:97`; the block's own header row is `:96`
  (`| Status | Assign when (necessary condition) | Required basis | Never |`).
- `:498` sits in `## Error patterns` (heading `:468`) and is a **sibling row of
  the same table** — `:495` is `| A claim's status rides as prose inside
  `evidence_status` or `kind` | …` and `:496` repeats the same status table.

So the block is a three-row status table (at `:99-101` and at `:496-498`) whose
*last* row is duplicated verbatim while its two preceding rows differ in context.
**Finding R06-F6 (minor).** A draft that "deletes the duplicate row" must say
which of the two it deletes and what cross-reference replaces it, because the two
sites have different surrounding tables; deleting either without a cross-reference
leaves a table whose "Never" column is silently one row shorter.

## 5. N1 — reproduced, with distinct causes

`python3 -B reports/round-<N>/run-validation.py` at clean HEAD `139e3b6`:

| round | exit | cause read from the receipt |
|---|---|---|
| 5 | **1** | `F`: `non-append corpus edit: ('corpus/lessons/supplement-opencode-1/sources/ottoman.json', 'OTT-06')`; `O`: `replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` → `REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate, 0 mismatch, 0 reproduced of 7 row(s)`, every row `reason=gate_digest_mismatch` |
| 6 | **1** | `"error": "historical file changed: .gitignore"` |
| 7 | **1** | `previous_acceptance: previous round-6 acceptance failed: {…"historical file changed: .gitignore"}` plus `conformance_defects: ["binding declares saved_template_matches_actual=false…"]` |

**Finding R06-F7 (confirms N1).** Three rounds, three **distinct** causes, all
exit 1 at clean HEAD — exactly N1's assertion (`promotion-review.md:177-178`,
still open per `dossier-d11-shonen-boxes.md:145-147`). An N1 errata draft is
correct iff it states a distinct expected verdict **per round**; a single shared
"these fail" sentence would not satisfy N1.

## 6. N2 — reproduced live, including by this seat

### 6.1 The scripts rewrite filed receipts in place

| script | write site | target |
|---|---|---|
| `reports/round-5/run-validation.py` | `:194` | `(HERE / "validation.json").write_text(...)` |
| `reports/round-6/run-validation.py` | `:336` | `(HERE / "validation.json").write_text(...)` |
| `reports/round-7/run-validation.py` | `:1171` | `(HERE / "validation.json").write_text(...)` |

`reports/round-7/run-validation.py:8-10` **declares** this in its own docstring:
"Writes ONLY reports/round-7/validation.json in this repository (plus disposable
scratch …)". So round 7 discloses the write; the N2 defect is that the *isolation
caveat* does not cover it.

### 6.2 round-5's caveat contradicts its own next line

`reports/round-5/run-validation.py:193` states, as part of the receipt:

> "The previous acceptance receipt is regenerated only in an isolated copy, never overwritten in this tree."

`reports/round-5/run-validation.py:194` — the immediately following line —
overwrites `validation.json` in this tree.

**Finding R06-F8 (major, new).** This is a *self-contradicting caveat*, not a
missing one: round 5 asserts the exact property it violates, one line above the
violation. Any N2 disposition that records round 5 as "caveat present" is reading
the caveat's existence rather than its truth. The honest fix class is either the
`--in-place`-vs-isolated split or an erratum correcting `:193`.

### 6.3 This seat triggered it, and restored the filed bytes

Running the three validators for §5 rewrote two filed receipts. Evidence, before
and after the repair:

| file | HEAD (filed) sha256 | after my run | after restore |
|---|---|---|---|
| `reports/round-5/validation.json` | `73a66f7464ead0d99318750422256ceafac3d8c2d283f94604eb258abc1bb794` | `fe926984e8d15728c43c44b2fc4c0f60058f784aa4aa4b7c2e6aecc04a4dfeee` | `73a66f74…` ✅ |
| `reports/round-6/validation.json` | `32c621efaccca71db3b49a9151e3a37fd3663bcd97d9a6a71d745f6034158441` | `32c621ef…` (unchanged) | `32c621ef…` ✅ |
| `reports/round-7/validation.json` | `2f4c1e159b60d78250074c51f013d13aac3cf1b140a623d197a0883e5ecac6f3` | `af0cf4ed32d68c2b96284b49de97cfe75900c512299d4dd7423580e9573912a4` | `2f4c1e15…` ✅ |

Repair: `git checkout -- reports/round-5/validation.json reports/round-7/validation.json`;
`git status --porcelain` then returned only the pre-existing ` M LOG.md` plus
untracked `REGIMEN.md` and `reports/round-33/` — no filed-round path. The
round-5 diff was substantive, not cosmetic: it replaced the `O` error from
`check-gate-battery` with `replay-frozen` and changed the recorded
`tested_file_sha256` for `tools/check-gate-battery.py` from `0a126b70…` to
`455b595a…`.

**Finding R06-F9 (major, new).** Two of the three acceptance scripts are
**non-idempotent** on the live tree: re-running round 5 or round 7 changes filed
bytes, while round 6 happens to be deterministic and returns byte-identical
content (`32c621ef…`). N2 should therefore be dispositioned as *two* scripts that
must never be re-run in place and one that is safe-by-luck, not as three
equivalent scripts. This is also the empirical proof that N2's isolation caveat is
load-bearing rather than advisory: a reviewer obeying "re-run every cited command"
(R01/R04's standing method) corrupts filed rounds 5 and 7 unless it clones first.

## 7. The checker — tested bytes, for the integrator

C14 is absent, so the third pass ships as a runnable checker instead of a verdict.
Apply at `reports/round-33/review/R06-c14-pointer-check.py` and run:

```
python3 reports/round-33/review/R06-c14-pointer-check.py --selftest
python3 reports/round-33/review/R06-c14-pointer-check.py reports/round-33/calib/C14-fix-drafts.md
```

Expected: selftest exit 0; the C14 run exit 0 only if every pointer resolves to
non-blank content carrying its rule. Verified output on the bytes below:

```
PASS  baseline-cites resolved=0 findings=4 ['BLANK-TARGET', 'KNOWN-BAD-CITE', 'NON-SUPPORTING']
PASS  fixed-cites    resolved=4 findings=0 []
selftest: 2/2 cases correct
```

`sha256: 8c357ca17ff837348d79cd392dfa25ee87a977f037bb419b3949825a282fb717` (100 lines).

```python
#!/usr/bin/env python3
"""R06 pointer checker: resolve every `path:LINE` pointer in a draft file
against live bytes and assert the target carries the expected content.

Usage:
  python3 pointer-check.py <draft.md>        # check a C14-style draft
  python3 pointer-check.py --selftest        # prove teeth on known-bad cites
Exit 0 = every pointer resolves to non-blank content carrying its keyword.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] if "__file__" in globals() else Path.cwd()
PTR = re.compile(r"`([A-Za-z0-9_./-]+\.(?:md|py|json|yml|yaml|tsv)):(\d+(?:[,-]\d+)*)`")

# keyword each pointer's target MUST carry, keyed by (file, line)
EXPECT = {
    ("corpus/knowledge/synthesis/loanword-material-dating.md", 30): ["Arrival of its referent"],
    ("corpus/knowledge/synthesis/loanword-material-dating.md", 31): ["Manufacture"],
    ("corpus/knowledge/synthesis/loanword-material-dating.md", 59): ["prestige terminology"],
    ("corpus/knowledge/synthesis/loanword-material-dating.md", 63): ["sense\u2013referent pairing"],
    ("corpus/knowledge/synthesis/worldbible-integration-contract.md", 63): ["claim_ledger"],
}
# pointers known bad at baseline 139e3b6 (must be ABSENT from an applied fix)
KNOWN_BAD = {
    ("corpus/knowledge/synthesis/loanword-material-dating.md", 26): "blank line",
    ("corpus/knowledge/synthesis/loanword-material-dating.md", 57): "donor-innovation row, not prestige",
    ("corpus/knowledge/synthesis/worldbible-integration-contract.md", 183): "checklist line; 'basis' occurs 0x in this file",
}
# non-blank, resolves, but does not carry the row's rule: nearest support named
ADJACENT = {
    ("corpus/knowledge/synthesis/loanword-material-dating.md", 60):
        "label-vs-object-persistence row; the clock rule needs :30-31 (Lexical/Material clocks)",
}

def lines(p):
    return Path(p).read_text(encoding="utf-8").split("\n")

def expand(spec):
    out = []
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-"); out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out

def check(draft):
    findings, ok = [], 0
    for m in PTR.finditer(Path(draft).read_text(encoding="utf-8")):
        path, spec = m.group(1), m.group(2)
        if not Path(path).exists():
            findings.append(("DANGLING-FILE", path, spec, "")); continue
        L = lines(path)
        for n in expand(spec):
            if n < 1 or n > len(L):
                findings.append(("OUT-OF-RANGE", path, n, "")); continue
            txt = L[n - 1]
            if not txt.strip():
                findings.append(("BLANK-TARGET", path, n, "")); continue
            if (path, n) in KNOWN_BAD:
                findings.append(("KNOWN-BAD-CITE", path, n, KNOWN_BAD[(path, n)])); continue
            if (path, n) in ADJACENT:
                findings.append(("NON-SUPPORTING", path, n, ADJACENT[(path, n)])); continue
            need = EXPECT.get((path, n))
            if need and not all(k in txt for k in need):
                findings.append(("KEYWORD-MISS", path, n, txt.strip()[:70])); continue
            ok += 1
    return ok, findings

def selftest():
    bad = ["corpus/knowledge/synthesis/loanword-material-dating.md:26,60",
           "corpus/knowledge/synthesis/loanword-material-dating.md:57",
           "corpus/knowledge/synthesis/worldbible-integration-contract.md:183"]
    good = ["corpus/knowledge/synthesis/loanword-material-dating.md:30-31,63",
            "corpus/knowledge/synthesis/loanword-material-dating.md:59"]
    tmp = ROOT / ".scratch" / "r06" / "selftest-draft.md"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    fails = 0
    for label, ptrs, want_bad in (("baseline-cites", bad, True), ("fixed-cites", good, False)):
        tmp.write_text("\n".join("`%s`" % p for p in ptrs) + "\n", encoding="utf-8")
        ok, f = check(tmp)
        kinds = {x[0] for x in f}
        hit = "KNOWN-BAD-CITE" in kinds or "BLANK-TARGET" in kinds
        verdict = "PASS" if hit == want_bad else "FAIL"
        if verdict == "FAIL": fails += 1
        print("%s  %-14s resolved=%d findings=%d %s" % (verdict, label, ok, len(f), sorted(kinds)))
    print("selftest: %d/2 cases correct" % (2 - fails))
    return 1 if fails else 0

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
        sys.exit(selftest())
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    ok, f = check(sys.argv[1])
    for kind, path, n, d in f:
        print("FINDING %-15s %s:%s  %s" % (kind, path, n, d))
    print("resolved=%d findings=%d" % (ok, len(f)))
    sys.exit(1 if f else 0)
```

Note the checker is deliberately **not** a pass/fail oracle for meaning: it
resolves targets and enforces the `§3` minimum sets. A C14 draft that re-points to
`:63` alone will exit 0 and still be wrong per R06-F1 — the reviewer must apply
§3 by hand.

## 8. Findings, severity ranked

| id | severity | finding |
|---|---|---|
| R06-F3 | major | Condition 3's re-point branch is unavailable — `basis` occurs 0× in the contract; erratum is the only honest disposition |
| R06-F1 | major | The condition's own wording (`:63`) invites a fix that drops the clock-separation clause; minimum set is `:30-31,63` |
| R06-F2 | major | `:57` → `:59` resolves but drops the "check local manufacture" remedy; minimum set is `:59,63` |
| R06-F5 | major | All four condition-4 anchors have no target anywhere in `tools/`; re-point must be rejected |
| R06-F9 | major | Two of three acceptance scripts are non-idempotent on the live tree; N2 is two-and-a-half scripts, not three |
| R06-F8 | major | `reports/round-5/run-validation.py:193` asserts the exact property `:194` violates — a self-contradicting caveat |
| R06-F7 | confirm | N1 verified: three rounds, three distinct causes, exit 1 each |
| R06-F4 | minor | The `:183` mis-cite is two sites (`:128`, `:501`) from one origin (`reports/round-15/knowledge/skill-draft.md:95-97`) |
| R06-F6 | minor | The duplicated status block sits in two differently-headed tables; a bare delete shortens a table |

Every finding here is a process/pointer observation inside the lane's own
artifacts; none of them is a disposition of an artifact's standing, which is the
operator's call and outside this seat's authority.

**Language-grep note for the integrator (A-leg).** This fragment deliberately
carries no vocabulary asserting an artifact's standing. The remaining matches for
that vocabulary class are all *path citations*, not assertions: the string
`promotion-review.md` appears as `reports/round-24/promotion-review.md` (the
filed source of box-1 conditions 2–4 and N1–N7) at §1, §2.1, §5 and the citation
list. A round-33 language grep must whitelist path components or it will flag
every fragment that cites the condition's own source — including this one — as a
false positive.

## 9. What the third pass will run when C14 lands

1. `python3 reports/round-33/review/R06-c14-pointer-check.py --selftest` → exit 0.
2. `… R06-c14-pointer-check.py reports/round-33/calib/C14-fix-drafts.md` → expect exit 0.
3. Apply §3 by hand to every before/after pair: for each SKILL.md row, list its
   clauses and confirm the after-text's target set covers all of them.
4. Confirm the draft is line-count-neutral per edit (the `cold-run-fixes.md`
   house style: "each is line-count-neutral, so this seat introduced zero line
   drift"), and that every after-text is quoted verbatim rather than paraphrased.
5. Confirm no draft proposes a re-point for the four condition-4 anchors
   (R06-F5) or for `:183` (R06-F3).

## Owed

- **Resolved during this seat's window.** `reports/round-33/calib/C14-fix-drafts.md`
  landed at 00:59 and was revised at 01:03:44 (577 lines, 35,482 bytes, sha256
  `e6711f239ba34b3862e4bc4d8062c0f05c80bbf70168518d479d6c03e9ba60bb`). The third
  pass was executed against the revised bytes — verdicts in §10.
- `reports/round-33/calib/C13-consistency.md` was still absent at this seat's cut;
  the ledger-side cross-check R04/R05 own is unaffected by this fragment.
- Nothing else is owed by this seat.

## Citations

Files read (line-exact):
- `SKILL.md:96-101`, `:127-128`, `:468`, `:479`, `:481`, `:483`, `:486`, `:488`, `:491`, `:495-501`, `:522` — the rows, the duplicate block, the anchors
- `corpus/knowledge/synthesis/loanword-material-dating.md:25-31`, `:55-60`, `:62-63` — resolved targets and non-supporting lines
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:63`, `:183` — cite targets
- `reports/round-24/promotion-review.md:71-88` (box-1 conditions 2–5), `:176-196` (N1–N7)
- `reports/round-24/cold-run-fixes.md:1-45` — house style for fix drafts
- `reports/round-32/dossier-d13-operator-decisions.md:123-138` — Decision 4 table
- `reports/round-32/dossier-d11-shonen-boxes.md:145-147`, `:150`, `:167`, `:203-207`
- `reports/round-15/handoff/v2-design.md:126-132` — §2.3 zero-boilerplate
- `reports/round-15/knowledge/skill-draft.md:93-97` — origin of the mis-cite
- `reports/round-15/claims.json:14` — the rule's declaration home
- `reports/round-5/run-validation.py:193`, `:194`; `reports/round-6/run-validation.py:336`; `reports/round-7/run-validation.py:8-10`, `:1171`

Commands run (all at `HEAD 139e3b6`, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
- `ls -la reports/round-33/calib/` → `total 0`
- `grep -c basis corpus/knowledge/synthesis/worldbible-integration-contract.md` → `0`
- `grep -rl -- TL-01 tools/` (also `TL-02`, `FIELD_DEFAULTS`, `fictional-coordinate`, `descriptive-gloss`) → no output for each
- `grep -c 'TL-0' tools/d2-typed-labels.py` → `0`; `ls -la tools/d2-typed-labels.py` → 194937 bytes
- `python3 -B reports/round-5/run-validation.py` → exit 1; `…round-6…` → exit 1; `…round-7…` → exit 1
- `sha256sum reports/round-5/validation.json reports/round-6/validation.json reports/round-7/validation.json` before/after restore (digests in §6.3)
- `git show HEAD:<path> | sha256sum` for the three receipts (filed digests in §6.3)
- `git checkout -- reports/round-5/validation.json reports/round-7/validation.json`; `git status --porcelain` → ` M LOG.md`, `?? REGIMEN.md`, `?? reports/round-33/`
- `python3 -B .scratch/r06/pointer-check.py --selftest` → exit 0, `selftest: 2/2 cases correct`; `sha256sum` → `8c357ca1…`
- `python3` byte comparison of `SKILL.md:101` vs `:498` → identical, 555 bytes, `sha256` prefix `e5fa8fb0`

## 10. Third pass — verdicts on C14 as landed

### 10.1 Provenance of the bytes judged

C14 was absent at this seat's first cut (`ls -la reports/round-33/calib/` → empty,
00:52). It landed at 00:59 and was **revised at 01:03:44** to 577 lines / 35,482
bytes / sha256 `e6711f239ba34b3862e4bc4d8062c0f05c80bbf70168518d479d6c03e9ba60bb`.
The revision cites this seat's findings by id (`R06-F9`) and cites this fragment by
line (`R06-calib-review.md:47-168`, `:192-206`, `:238-264`, `:266-388`). Verdicts
below are on the **revised** bytes; §10.5 records the one defect found in the 00:59
revision that the revision has already remediated.

All eight of C14's pointers into this fragment resolve to the content C14 claims
(`:47` = `## 2. Answer key`, `:168` = end of the meaning-preservation table,
`:192` = `## 5. N1`, `:206` = end of N1, `:238` = `### 6.3`, `:264` = end of F9,
`:266` = `## 7. The checker`, `:388` = end of the checker block). This is why §10 is
appended rather than the fragment being restructured: a rewrite would have broken
them, and introducing that defect class while reviewing for it would be incoherent.

### 10.2 Corrections to this seat's own pre-registered answer key

Two of my §2 conclusions were **too narrow and are withdrawn as stated**. C14 found
better answers than my answer key did, and the corrections run against me:

| my finding | as I stated it | corrected |
|---|---|---|
| **R06-F3** | "the re-point branch is **not available**" for condition 3 | True only *within that contract*. C14's cross-file re-point to `tools/harness/packet_uncertainty.py:205,209` is real, executable, and strictly better than my erratum-only disposition. Verified: `_is_boilerplate` at `:84`, `U-BASIS-BOILERPLATE` at `:205`, `U-BASIS-RESTATES` at `:209`, `--selftest` exit 0 "19 checks passed". |
| **R06-F5** | "All four condition-4 anchors have no target anywhere in `tools/`; **re-point must be rejected**" | True of the literal token strings (each occurs 0×), but false of the *behaviors*: C14 correctly retires the dead names and cites the tool's live finding-class vocabulary (`D2L-DATA` `:421`, `D2L-FORM-UNRESOLVED` `:422`). Verified: `KINDS` `:410`, `FINDING_CLASSES` `:419-420`, fail sites `:694-695`, `:768-769`, `:774-775`, exit rule `:830`, selftest "163/163" exit 0. |

My §2.1 and §2.2 conclusions stand, and §2.1 is the one that survives into the
verdict below.

### 10.3 Per-draft verdicts

| draft | proposed target(s) | resolves? | carries the rule? | verdict |
|---|---|---|---|---|
| 1a RECOMMENDED (`SKILL.md:486`) | `loanword-material-dating.md:29,63` | yes | **no** — `:29` is the Contact clock | **defect — see 10.4** |
| 1a sharpening | `:29-30,63` | yes | partly — `:30` carries it, `:29` does not | acceptable; `:30-31,63` is exact |
| 1b (`SKILL.md:488`) | `:59` | yes | yes — verbatim "Dictionary selection bias; imported prestige terminology for local goods" | **accept** (add `:63` for the remedy clause per R06-F2) |
| 2a/2b (`SKILL.md:128`, `:501`) | `tools/harness/packet_uncertainty.py:205,209` | yes | yes for boilerplate + restates | **accept**; see 10.5 F13 |
| 2 fallback (strict variant) | `v2-design.md:126,131-139` | yes | yes | **accept** as the erratum variant |
| 3a (`SKILL.md:479`) | `D2L-FORM-UNRESOLVED` | yes (`:422`) | yes | **accept** |
| 3b (`SKILL.md:481`) | `tools/d2-typed-labels.py:694-695,774-775` | yes | yes — and corrects HOLD→FAIL | **accept** |
| 3c (`SKILL.md:483`) | `:768-769`, `:500`, `:549`, `:565` | yes | yes | **accept** |
| 3d (`SKILL.md:491`) | `:859`, `:500`, `:3195` | yes | yes — `reconcile_era` at `:859`, selftest check at `:3195` | **accept** |
| 4 (`SKILL.md:701-704`) | `SKILL.md:701-704` | yes | yes — three commands, three distinct causes | **accept** (see 10.5 F10/F11) |
| 5a (`SKILL.md:485`) | `corpus/knowledge/linguistics/language-contact.md:80-81` | yes | yes — `:78` is the intro line, `:80-81` the two principles | **accept** |
| 5b (`SKILL.md:213`) | *(no pointer; `to-verify` on two hashes)* | n/a | n/a | **accept as `to-verify`** — C14 marks its own unknown |

Every pointer in every **after** block resolves and carries its rule. Running the §7
checker over the current C14 returns `resolved=808 findings=15`, and manual
classification of all 15 shows they are *quoted before-state* (the stale cites the
drafts exist to repair), deliberate rationale mentions of `:183` as citable for its
actual content, and range-interior blanks — **zero are in a proposed after-text**.
A fix draft legitimately contains bad pointers in its `before` blocks; the checker
must be read with that in mind (see §10.6).

### 10.4 The one surviving defect — Draft 1a's RECOMMENDED target (R06-F1 confirmed)

C14's root-cause analysis is **correct and well-evidenced**, and I verified it
independently: `git diff e1694ba~1 e1694ba -- corpus/knowledge/synthesis/loanword-material-dating.md`
shows hunk `@@ -2,6 +2,9 @@` adding exactly three lines (`- source:`, `- verified-at:`,
`- recheck:`), which shifts every later pointer by **+3**. Pre-commit `:26` is the
Contact row (→ HEAD `:29`) and pre-commit `:60` is the sense–referent pairing line
(→ HEAD `:63`); pre-commit `:57` is the native-term row, so C14's claim that `:57`
was already off by one pre-commit is also confirmed.

That provenance explains Draft 1a — it restores the author's *original* anchors.
But the row being repaired reads:

> `| A loan's oldest form used to date the referent's arrival | clock conflation; keep word-entry and object-arrival intervals separate (…) |`

- clause (i), "referent's arrival" — carried by `:30`: `| Lexical | A word or sense enters a specified speech community | Arrival of its referent; first surviving written token |`
- clause (ii), "object-arrival intervals" — carried by `:31`: `| Material | Manufacture, import, imitation, use, repair, or deposition | … |`
- `:29` = `| Contact | A particular population's encounter with a carrier | First encounter anywhere; migration; political submission |` — a population's encounter, not a word's or object's arrival

**Verdict: `:29,63` resolves but does not carry clause (i).** A faithful drift-fix
restores pointer validity, not semantic fit; the r24 condition calls the cite *wrong*,
and restoring the pre-commit anchor restores a pointer that was off-target before the
shift too. **Recommended after-text: `loanword-material-dating.md:30-31,63`.**
C14's own optional sharpening (`:29-30,63`) is one token away from this; dropping the
non-supporting `:29` completes it. This is the single edit I ask the integrator to
make before applying Fix 1a.

### 10.5 Findings raised against the 00:59 revision, with remediation status

| id | severity | finding | status at 01:03:44 |
|---|---|---|---|
| **R06-F10** | major | Fix 4's draft instructed the integrator to land the sentence *"re-running these three adds no new working-tree entries (`git status --porcelain`, checked 2026-10-19)"*. **False**, and I have the disproof: round-5's receipt write at `run-validation.py:194` is unconditional (no guard; the write follows the `report` build directly), and my own runs changed filed bytes (`73a66f74…`→`fe926984…`, `2f4c1e15…`→`af0cf4ed…`). The clean tree C14 observed was produced by **this seat's** `git checkout --` restore at 00:55:27 — the two restored files carry the identical mtime nanosecond `00:55:27.940762254`, the signature of one checkout touching both. | **remediated** — the sentence is gone (`grep 'adds no new working-tree entries'` → no match) and is replaced by *"run them in a disposable clone: round 5 and round 7 rewrite their own filed `validation.json` in place (round 6 is byte-stable)"*, which is correct and now cites `R06-F9`. |
| **R06-F12** | major | Fix 4 cited `dossier-d11-shonen-boxes.md:178-182` for the N1 statement. Those lines are about the r22 ledger row and `examples/culture-d2/` strings; the N1 statement — *"N1 — NOT closed by text. Checklist item 5 still names no expected verdict for the round-5/6/7 acceptance re-runs"* — is at `:145-147`. A pointer resolving to non-carrying content, in the draft that repairs pointer defects. | **remediated** — `grep 'dossier-d11-shonen-boxes.md:178'` → no match. |
| **R06-F11** | minor | Fix 4 asserts *"`O_passed: true`"*. The substance verifies — `.claims.O.passed = True` with `positive_controls.passed=5`, `domain_controls.passed=16`, `malformed_controls.passed=4`, `frozen_checks.passed=5` — but the literal field name is a paraphrase; there is no top-level `O_passed` key in `reports/round-7/validation.json` (top-level keys: `acceptance_checks_passed, baseline_revision, claims, conformance_defects, counting_command, dispatch, evidence_sha256, failures, limits, missing_dependencies, round, runner_scratch`). A cold reader grepping the name as written finds nothing. | **open, minor** — recommend writing `claims.O.passed: true`. |
| **R06-F13** | minor (constructive) | Drafts 2a/2b cite `tools/harness/packet_uncertainty.py:205,209`, covering "boilerplate" and "restates the status word". The sentence's third clause, "its witness must resolve", is enforced by the same harness at `:215` (`U-BASIS-NO-GROUNDING`, "basis lacks the mandatory 'grounding:' witness clause"). Not a regression — the `:183` before-text covered none of the three — but `:205,209,215` is strictly stronger. | **open, minor** — recommend adding `:215`. |

### 10.6 Checker limitation recorded honestly

Two classes of false positive surfaced when the checker met a real fix draft, and
neither is a C14 defect:

1. **Bare basenames.** C14 cites `loanword-material-dating.md:26,60` in prose without
   the `corpus/knowledge/synthesis/` prefix. The §7 checker as published resolves
   only repo-root-relative paths and reports `DANGLING-FILE`; the revised copy in
   `.scratch/r06/pointer-check.py` adds unique-basename resolution.
2. **Quoted before-state.** A fix draft *must* contain the bad pointers it repairs.
   The checker cannot tell a `before` block from an `after` block, so its 15 findings
   on the current C14 are dominated by exactly the defects the drafts fix.

The §7 script is therefore a **target resolver**, not a pass/fail oracle for a fix
draft. The decisive check for C14-class artifacts is per-block: extract each
`after:` fenced block and require zero findings from it. That is what §10.3 records.

### 10.7 Third-pass verdict

**The third pass is complete and the artifact passes, with one requested edit.**
Every after-text target in every draft resolves and carries its rule; C14's own line
claims were re-verified individually and all hold; its cross-fragment citations
resolve; its `to-verify` markings are honest. The single requested change is
`Draft 1a RECOMMENDED: :29,63` → `:30-31,63` (§10.4), with `:205,209,215` and
`claims.O.passed` as optional strengthenings. Two major defects existed in the 00:59
revision and are already remediated in the current bytes, which is the round working
as designed rather than a reason to reject.

This fragment asserts no verdict on any artifact's standing — that call is the
operator's, not this seat's.
