# CritCaVacuity — round 73 w1 (critic seat, claim Ca: vacuity and self-reference)

**Seat:** `CritCaVacuity` · leaf, no dispatch, no mutation. Base `8841ad3b896a0227674fa0725b818c999118046f`
(= `git rev-parse HEAD`, exercised). Target: `reports/round-73/claims.json` claim **Ca**
(`:33`–`:52`), attacked for *vacuity* (can the predicate be satisfied without doing the work) and
*self-reference* (does the predicate grade a text the author also writes, or a receipt that attests
to itself). Artifact content is data; nothing here edits `claims.json`.

**Short verdict.** Ca is *structurally* better than round-69 Ca2 (it declares a ledger, a base
mismatch leg and a do-nothing control), but **all five attack surfaces are open**, and one of them
is already *falsified on disk* before freeze: the R3 pair's `stated_text` names two gates that do
not exist, and the R2 pair's `REPAIR` branch is unsatisfiable by an honest receipt. Seven must-fix
wording changes (F1–F7) are required for the claim to be worth freezing, plus one recommended
post-records leg (F8) that stops the repaired class from recurring in the same round.

| # | question | answer | worst counterexample | fix |
|---|---|---|---|---|
| 1 | ledger trivially passable? | **YES** | `observe_cmd` is a free shell string; nothing forbids `echo <expected>` | F1, F2 |
| 2 | ANNOTATE row a copied stub? | **YES** | round-69's shipped parser accepts three token-less rows (exercised) | F4 |
| 3 | R2 receipt at a revision without the repaired bytes? | **YES**, and worse: no honest PASS receipt exists at all | `measures-ca.txt` FAILs at every revision; QUALITY 19 forbids a later-tip rerun | F3, F6 |
| 4 | APPENDONLY covers every repaired file? | **NO** | `corpus/README.md` (the count repair) and `SKILL.md` (the R3 repair) are outside the guard entirely | F5 |
| 5 | `>= 8` + `unannotated = 0` enough? | **NO** | denominator, pair set, dispositions and observed values are all author-chosen; C's landing moves the README count 245 → 247 | F7, F8 |

---

## 1. Can the ledger be authored to pass trivially? — **Yes, three independent channels**

**(a) `observe_cmd` is an executable string the author supplies.** `claims.json:40` requires the
pair to carry `observe_cmd` and says the counter "recomputes observed from committed bytes at
`<lands>`, never from the ledger's own copy". Those are different things. A command that reads
committed bytes and a command that prints a constant are indistinguishable to a counter that runs
the string; `observe_cmd: "echo 245"` + `expected_after: "245"` satisfies both halves of the
sentence. The leg constrains the *source* of the value but not the *derivation*. This is not
hypothetical: round-72's `REPORTCORR` leg (`reports/round-72/accept-ca.py:125-133`) is a
substring test on a file it reads, and its **do-nothing control at base** printed
`LEG PASS REPORTCORR` (`reports/round-72/telemetry/controls-ca.txt:13`) — a leg green on the
control is a leg whose "observed" is not load-bearing.

**(b) Pairs that already match are not excluded, because `BASEMISMATCH` is not bound to the
ledger.** `claims.json:41` says "the counter finds >= 8 mismatch pairs" — not "at least 8 *of the
ledger's* pairs are red at base". A counter can find eight mismatches anywhere in the repo while
every declared pair is already consistent; the ANNOTATE rows then restate a token that never
differed, and `unannotated = 0` is true by construction. Nothing in `:40`–`:45` requires
`observed_base != stated_text` per pair.

**(c) The before-state contains an unbound symbol.** `claims.json:37` reads "shows **N**
unannotated mismatches". `N` is a literal placeholder character in the frozen text. A predicate
whose before-state is a variable can be satisfied for any value of it, including the value that
happens to be easy.

**Under-scoping is visible at base.** R1's observation is path-scoped
(`git ls-files --others --exclude-standard .ufo/waves/round-72`), which returns exactly the two
files (exercised). But the repo at base has **62** untracked paths
(`git ls-files --others --exclude-standard | wc -l` = 62). The pair is honest about its own two
paths; the *class* it is filed under ("work products untracked") is not closed by tracking two
files, and the next round can re-file the same class. `>= 8 pairs` does not measure that.

**Impacted axes:** calibration (primary — the claim's whole content is the calibration record);
quality (the round's own mined mistake class, "receipt/verdict mismatch", is left re-openable).

---

## 2. Can an ANNOTATE row be a stub naming id + tokens copied from the ledger? — **Yes**

`claims.json:43` requires the row to *name* "pair id + stated token + observed token".
`claims.json:45` (`NOSTUB`) requires "no correction row is shorter than the ledger's minimum
shape (id + old token + new token + re-derivation command)". Both are **shape** tests. Every one of
those four elements is already present in the ledger (`stated_text`, `expected_after`,
`observe_cmd`), so the row is a transcription, not a derivation. No leg says the row's "observed
token" must equal *the counter's* recomputation — it may be a stale value, a fabricated value, or
the ledger's own `expected_after` echoed back.

**Exercised counterexample (the exact class `:43` cites).** I imported the shipped round-69 module
and called its row parser on a synthetic corrections file containing three rows with **no token and
no command**:

```
| LEGCOUNT    | SCORECARD.md  | x |
| DEADPOINTER | fleet-report  | x |
| OVERREACH   | SCORECARD.md  | x |
```

`reports/round-69/accept-ca.py` `correction_pairs()` (lines 179-195) reads `cells[1]`/`cells[2]`
and returned `[('DEADPOINTER','fleet-report'), ('LEGCOUNT','SCORECARD.md'),
('OVERREACH','SCORECARD.md')]` — all three accepted. The round-69 lesson records the consequence
(`corpus/lessons/round-69.md:55`: "stub correction rows also pass"). Ca renames the hole
("minimum shape") without closing it: a shape rule is still satisfiable by transcription.

**Second, sharper channel — the token can be *contained* rather than *equal*.** The R2 pair's
stated token is `ACCEPT-CA-72 PASS legs=12/12`; the receipt reads `ACCEPT-CA-72: FAIL legs=12/12`
(`reports/round-72/telemetry/measures-ca.txt:29`). Both contain `legs=12/12`. A containment test
(or any test that does not compare the verdict word) passes on the *unrepaired* value. Round-72
demonstrates the failure mode live: its `REPORTLAST` leg passed at the **base** control
(`controls-ca.txt:24`, "commits=0 report-names-lands=True") because the base revision string
appears in the report.

**Impacted axes:** calibration.

---

## 3. Does REPAIR for R2 admit a receipt produced at a revision without the repaired bytes? — **Yes; and the honest branch does not exist**

`claims.json:42`: "R2 a committed receipt carrying a PASS stamp at the stamped revision for
REPORTCORR+REPORTLAST, or the pair is re-dispositioned ANNOTATE before freeze if the rerun fails".

**(i) The leg grades a *text stamp*, not the revision.** The modelled precedent is round-72's
`CASTAMP` leg (`accept-ca.py:141-151`): read the receipt at lands, substring-check a few hex
strings, then require `in_range(commit)` — i.e. the adding commit is between base and lands. It
never re-evaluates a leg *at* the stamped revision. Any ancestor commit in `base..lands` qualifies,
including one that predates the corrected bytes. "PASS stamp at the stamped revision" is a
self-description unless the counter re-derives the two named legs against that revision's tree.

**(ii) No PASS receipt for the round-72 Ca counter exists at any revision.** Exercised:
`grep -rn "ACCEPT-CA-72" reports/round-72/` returns the claim text, the counter's print statement,
and two receipts, **both** `FAIL legs=12/12`
(`telemetry/measures-ca.txt:29`, `telemetry/controls-ca.txt:28`). The lands receipt's own body
shows why: `LEG FAIL REPORTCORR / fleet-rev=MISSING` and `LEG FAIL REPORTLAST`. There is no
restamp in `reports/round-72/telemetry/` (directory listed). So the REPAIR branch can only be
satisfied by (a) fabricating a PASS stamp, or (b) re-running an earlier claim's counter at a later
tip — which QUALITY 19 explicitly forbids ("an earlier claim's receipt is never re-run at a later
tip to cover it", `corpus/QUALITY.md:59`). Either way the leg's green state is produced by the
author's text, not by repo state. That is the round-72 R2 defect reproduced inside the round that
repairs it.

**(iii) The escape hatch makes the disposition a post-hoc choice.** "or the pair is
re-dispositioned ANNOTATE before freeze if the rerun fails" tells the author, at freeze time, to
pick the disposition that happens to pass. The ledger is then authored *to* the achievable
after-state — the definition of a claim about a number the author chose. It also contradicts the
claim's own **title** (`claims.json:35`, "the round-72 routed defects R1-R3 **repaired**"): if R2
must be ANNOTATE, the title is false while the predicate is green.

**(iv) The receipt shape cannot be reused even if a PASS existed.** Exercised:
`python3 -B tools/check-receipt-seq.py --root . --lands 21ad3088… reports/round-72/telemetry/measures-ca.txt reports/round-72/accept-ca.py`
→ `SEQ-… FAIL missing_headers=['stamped','evaluated','measured']`, `RECEIPT-SEQ: FAIL`, **exit 1**
(`--selftest` on the same tool prints `SELFTEST: 14/14`, exit 0). The round-72 receipt carries a
combined `# stamped/evaluated/measured revision (lane main):` line; QUALITY 19 requires three
separate headers plus `# tree:` and `# counter sha256 (self):`. Ca's STAMP leg (`:47`) says the
receipt "names the lands revision, its tree hash, the counter sha256, and was produced inside a
materialized clone" — "was produced inside a clone" is unverifiable from receipt text; the shipped
tool is the only thing on disk that can fail it.

**Impacted axes:** calibration; quality (Ca cites QUALITY 17/19 as its guard while implementing
less than the shipped tool does).

---

## 4. Does APPENDONLY cover every file the repairs touch? — **No**

`claims.json:44` guards **five** surfaces: `LOG.md`, `SCORECARD.md`,
`corpus/lessons/round-72.md`, `corpus/lessons/round-71.md`, and the round-72 fleet report. The
repairs named in `:42` touch **three more**:

| repair | file touched | guarded? |
|---|---|---|
| R1 track two files | `.ufo/waves/round-72/w1/{ScoutMergeScan,ScribeLesson}.md` (add) | n/a (additions) — but see below |
| R2 receipt/verdict | `SCORECARD.md` (append) + `reports/round-73/telemetry/*` (new) | SCORECARD yes; telemetry unguarded (fine) |
| R3 registry rows | **`SKILL.md`** (in-place insert) | **NO** |
| README count | **`corpus/README.md`** (the totals line + appended dated line) | **NO** |

The permission clause — "in-place edits permitted only to SKILL.md registry rows and README
footer, each listed in the ledger" — is not an enforcement. A ledger **pair** is a mismatch claim,
not a line-range authorisation; nothing in the leg ties the diff to the registry rows or the
footer. `SKILL.md` §Gates and probes runs from `:619` to the registry table header at `:648` — 28
lines of contract prose (measured); under `:44` an author may delete any of it while inserting the four
registry rows, and the counter cannot see it, because `SKILL.md` carries no zero-removed-lines
constraint at all. The same is true of `corpus/README.md`, which is where the count actually lives.

Two further coverage defects:

- **Path ambiguity.** The token `Total knowledge entries: 243.` is at **`corpus/README.md:732`**,
  not in root `README.md` (exercised: `grep -rn "Total knowledge entries" --include='*.md'` finds
  it only under `corpus/README.md` and in lessons). `:37` says "README" unqualified, so the pair's
  `stated_at` can name a path:line where the token is absent — and no leg checks provenance.
- **The count has two surfaces.** `corpus/README.md:732` states `243`, and `:736` states
  "(total 243 files; directory totals 30/29/36/29/24/95)". One pair cannot cover both; the
  directory totals are separately wrong (measured `95/38/30/29/29/24` = 245).

**R1 content identity.** "both files tracked" is satisfied by `touch` + commit. The two files are
13,412 and 19,765 bytes at base (measured); a zero-byte file with the right name passes the leg as
written. Nothing pins their bytes.

**Impacted axes:** calibration; quality (frozen-byte discipline is the round-69 lesson's core).

---

## 5. Is `>= 8 pairs` + `unannotated = 0` enough? — **No**

The after-state is a statement about the author's ledger, not about the repo's mismatch population.
Four free parameters remain: the denominator (`>= 8`), the pair set, the disposition of each pair
(at freeze, after seeing what passes), and — via `observe_cmd` — the observed value itself.

**The README pair is a moving target, and C moves it.** At base the count is **245** by two
independent instruments: `find corpus/knowledge -type f -name '*.md' | wc -l` = 245, and the
README's *own* declared instrument `python3 tools/source-audit-inventory.py --json --summary
--root corpus/knowledge` prints `"files": 245` (exercised). Claim C admits two new entries
(`claims.json:17`, `conlang-scholarship.md` + `conlang-scholarship.amend-2026-10-23.md`), so at
`<lands>` the same command returns **247** [INFERENCE: two `.md` files added under
`corpus/knowledge/linguistics/`; the command counts every `.md` under the root]. The "corrected"
number is therefore 245 or 247 depending on whether C lands — a number the author can move by
landing entries. `SEPARABLE` (`:46`) forbids citing S-ids and C paths; it says nothing about a
derived count, so the interference passes.

**`SEPARABLE` is unimplementable as worded.** "leg set passes on base + the Ca paths alone" is a
path-subset construction, but Ca's corrections section and C's round row both live in
`SCORECARD.md`. You cannot separate two claims by path when they share a file; the leg will either
be skipped or silently include C's SCORECARD changes. Round-72 has the precedent: its
`AUTHORIZED_PREFIXES` (`accept-ca.py:38-42`) lists `SCORECARD.md` and `corpus/`, so both claims'
bytes were graded together.

**`unannotated = 0` is scoped to the ledger.** No leg asks whether the *population* of mismatches
at `<lands>` is zero. Combined with (1b), that means "0" can be true while the population is
unchanged.

**Already falsified before freeze: R3's own text.** `claims.json:37` says SKILL.md "has no rows for
accept-ca-70..72 / accept-c-70..72 **although those gates exist**". Exercised:
`reports/round-70/` contains `claims.json`, `corrections-r69.md`, `telemetry/` and **no
`accept-*.py`**; only rounds 71 and 72 have `accept-c.py` / `accept-ca.py`. So two of the six named
gates do not exist, and the REPAIR branch ("SKILL.md registry rows exist for each named gate")
would force rows for nonexistent gates — fabrication — or a freeze-time narrowing of the pair. The
registry gap that *is* real is total: `grep -o "accept-[a-z]*-[0-9]*" SKILL.md | sort -u` tops out
at `accept-o-69`; there is no row for any round 70, 71 or 72 gate.

**Impacted axes:** calibration (primary), coverage (C interference via the count), quality.

---

## 6. Proposed predicate wording fixes (8; exact replacement text)

Line numbers refer to `reports/round-73/claims.json`. Each fix is a drop-in replacement for the
named leg (or for the `before`/`after` field where stated). F1–F7 are **must-fix**; F8 is
**nice-to-have** (post-records evidence, cited by no frozen predicate, per QUALITY 19).

### F1 — `LEDGER` (`:40`) — **must-fix**: kill the command channel, bind provenance
> `LEDGER: reports/round-73/ledger.json is added by the first Ca commit after base and that commit is an ancestor of every other Ca commit; it declares a literal pair count n and the pair set, each {id, stated_at(path:line), stated_text(verbatim), observe(kind,args), expected_after, disposition: REPAIR|ANNOTATE}. observe is a closed descriptor over a fixed kind enum (file_count, line_text, verdict_word, path_tracked, blob_sha256, registry_row) carrying only a path and a line/anchor — never a shell command, and the counter executes no string from the ledger. The counter derives every observation itself from committed bytes (git show <rev>:<path>) at the base revision and at <lands>, and prints per pair (stated, observed_base, observed_graded). A pair whose stated_text is not byte-present at stated_at in the base tree fails this leg (provenance).`

### F2 — `BASEMISMATCH` (`:41`) — **must-fix**: bind the mismatches to the ledger, define "mismatch"
> `BASEMISMATCH: at the base revision the counter observes, for at least 8 of the ledger's own pairs, observed_base != stated_text under that pair's kind rule, and the number of such red pairs equals the ledger's literal n (the before-state field names n as a number, never as a placeholder). A difference confined to surrounding whitespace is not a mismatch; a verdict_word pair is red only when the verdict word itself differs (the round-72 case: 'PASS legs=12/12' vs 'FAIL legs=12/12' differs in the verdict, not in the leg count). A do-nothing control FAIL receipt is committed pre-data and the counter reproduces it at base.`

### F3 — `REPAIR` (`:42`) — **must-fix**: red-at-base, per-pair minima, R2 is ANNOTATE-only
> `REPAIR: every REPAIR pair is red at base and green at <lands> under the same kind rule (observed_graded == expected_after and expected_after != stated_text). Per-pair minima: R1 — both named files are tracked at <lands>, non-empty, each file's first line names the seat id it is filed under, and each blob sha256 equals the digest the pre-data ledger records; R2 — ANNOTATE-only: no PASS receipt for reports/round-72/accept-ca.py exists at any revision (measured 2026-10-25: both committed receipts read FAIL), the pair's correction row names the receipt path and its sha256, and the claim title reads 'R1-R3 closed (REPAIR or ANNOTATE)' — a title claiming 'repaired' while the predicate admits ANNOTATE is a false self-report; R3 — for each gate file the counter can git cat-file -e <base>:<path>, SKILL.md carries a registry row whose entry-command cell names that exact path and whose owner cell is kotodama-shokunin, and the pair's stated_text enumerates exactly those gates (round 70 has no accept-*.py; a row for accept-c-70/accept-ca-70 is fabrication); README — the appended dated line names old token, new token and the measurement revision, and new token equals the counter's own recount at that revision.`

### F4 — `ANNOTATE` (`:43`) + `NOSTUB` (`:45`), merged — **must-fix**: derivation, not shape
> `ANNOTATE: every ANNOTATE pair has a row at <lands> in SCORECARD.md under a heading matching ^## Corrections — round 73\b, with four cells: pair id, old token, new token, re-derivation command. DERIVED: for each row the counter (a) requires new token == its own observed_graded for that pair — never the ledger's expected_after; (b) requires new token != old token and old token == the pair's stated_text, compared as exact strings after whitespace normalisation (containment never passes: 'PASS legs=12/12' and 'FAIL legs=12/12' share a substring); (c) runs the row's re-derivation command inside a materialised clone at <lands> under a 60 s cap and requires exit 0 and stdout containing the new token; (d) rejects any command whose argv is a constant printer or shell builtin (echo, printf, true, :, or cat of a literal). Row presence alone never passes.`

### F5 — `APPENDONLY` (`:44`) — **must-fix**: cover every repaired file, region-scope the in-place edits
> `APPENDONLY: over git diff --no-renames --numstat base..<lands> the guarded set {LOG.md, SCORECARD.md, corpus/README.md, corpus/lessons/round-71.md, corpus/lessons/round-72.md, corpus/QUALITY.md} shows zero deleted lines, and git diff --diff-filter=DR --name-only base..<lands> over that set is empty. SKILL.md: every line removed by git diff -U0 base..<lands> -- SKILL.md must be a registry table row (starts '| accept-'), and the number of added '| accept-' rows equals the number of gates the R3 pair names; any removed SKILL.md line outside the table fails the leg. corpus/README.md is append-only: zero removed lines, and the appended dated line's numbers equal the counter's recount at the measurement revision. The fleet round-72 report is read fail-closed: the counter compares its blob at fleet HEAD to the sha256 recorded in the pre-data ledger and fails if the fleet repo is unreadable or the blob differs — it never compares the file to itself.`

### F6 — `STAMP` (`:47`) — **must-fix**: use the shipped tool, re-evaluate at the stamped revision, break the cycle
> `STAMP: python3 -B tools/check-receipt-seq.py --root . --lands <lands> <receipt> <counter> exits 0, i.e. separate '# stamped revision:', '# evaluated revision:', '# measured revision (lane main):', '# tree:' and '# counter sha256 (self):' headers with stamped == evaluated == measured and tree == git rev-parse <stamped>^{tree}; the round-72 receipt shape is inadmissible (measured 2026-10-25: missing_headers=['stamped','evaluated','measured']). The counter re-evaluates every leg the receipt stamps against the stamped revision's own tree — a stamp whose revision does not contain the bytes that leg grades prints FAIL. Cycle guard: a receipt is never admissible as evidence for a leg it stamps; the R2 receipt's stamped leg set must be a proper subset of the leg set and must not include REPAIR or ANNOTATE.`

### F7 — `SEPARABLE` (`:46`) — **must-fix**: land-order separability and pinned count revisions
> `SEPARABLE: the Ca legs pass at a commit Ca1 that is a child of base and an ancestor of <lands>, that contains no C path (corpus/knowledge/**, corpus/SOURCES.md, corpus/lessons/round-73.md) and no C-added line; the counter prints ACCEPT-CA-73: PASS at Ca1 and at <lands>. Path-level separability is not accepted where both claims edit SCORECARD.md. PINNED: every pair whose kind is file_count or a line_text over a counting line records its measurement revision in the ledger, and the counter grades it at that revision, never at <lands> (C's landing moves corpus/knowledge from 245 files to 247, so an unpinned count makes the corrected number a number the author can move by landing entries).`

### F8 — `POPULATION` (new leg, post-records) — **nice-to-have**
> `POPULATION (post-records; cited by no frozen predicate, graded after the records commit): reports/round-73/extract-claims.py --root . --rev <lands> reports zero residual mismatches over the declared statement domain, or every residual is listed with reason and flip; and python3 -B tools/check-receipt-seq.py --root . --topo <round-73 receipts> exits 0, so the round-73 SCORECARD row's own PASS verdict is carried by a commit whose parent is the stamped revision — the round-72 R2 class cannot recur in the round that repairs it.`

---

## 7. Impacted axes and smallest safe correction

- **calibration** (Ca's own axis): vacuous predicate ⇒ the claim verifies while calibration stays
  unprovable — round-69's Ca2 outcome (`SCORECARD.md:1362`, `corpus/lessons/round-69.md:33` R69-M7).
  F1–F4, F6 are the minimum set that makes the after-state a property of the repo.
- **quality**: Ca cites QUALITY 17/19 but implements less than `tools/check-receipt-seq.py`
  already enforces (F6 closes this at zero new tooling). The round's own `mistake_to_mine`
  ("receipt/verdict mismatch with no rerun receipt") is re-committable by the round itself
  unless F8 lands post-records.
- **coverage**: C's landing moves the README count 245 → 247; unpinned counts let one claim's
  landing satisfy another's after-state (F7).
- **freshness**: untouched (paused under the open L0 `kotodama | round-11` ruling); no fix here
  claims a freshness move.
- **No harm:** every fix above is a tightening of a read-only counter leg; none requires rewriting
  frozen bytes, so the kill rule's "never requires rewriting frozen bytes" property survives.

**Smallest safe correction, if only three changes are affordable:** F4 (derivation instead of
shape — kills the stub class), F6 (shipped receipt tool + re-evaluation at the stamped revision —
kills the self-attesting receipt), F5 (guard `corpus/README.md` and region-scope `SKILL.md` — kills
the silent rewrite). Those three close the three channels that survive an honest author trying to
do the work; F1–F3 close the channels that a dishonest or rushed author would find first.

---

## 8. Honesty block — what I exercised and what I did not

**Exercised (all read-only, no writes outside `/tmp/critca/CritCaVacuity/` and this report):**
`git rev-parse HEAD`; `git ls-files --others --exclude-standard` (62 paths) and the scoped variant
(2 paths); `git status --porcelain`; `grep -rn "ACCEPT-CA-72" reports/round-72/`; directory listings
of `reports/round-72/telemetry/`, `reports/round-70/`, `reports/round-73/`; `find
corpus/knowledge -type f -name '*.md' | wc -l` (245) and per-directory counts; `python3
tools/source-audit-inventory.py --json --summary --root corpus/knowledge` (exit 0, `"files": 245`);
`grep -o "accept-[a-z]*-[0-9]*" SKILL.md | sort -u` (registry stops at 69); `ls
reports/round-7{0,1,2}/accept-c*.py`; `python3 -B tools/check-receipt-seq.py --selftest` (exit 0,
`SELFTEST: 14/14`); `python3 -B tools/check-receipt-seq.py --root . --lands 21ad3088… 
reports/round-72/telemetry/measures-ca.txt reports/round-72/accept-ca.py` (exit 1,
`missing_headers=['stamped','evaluated','measured']`); import of `reports/round-69/accept-ca.py`
and a call to its shipped `correction_pairs()` on a synthetic three-row stub table under
`/tmp/critca/CritCaVacuity/root` (all three rows accepted).

**Not exercised / not claimed:** no round-73 counter exists yet (`reports/round-73/accept-ca.py`
absent), so every Q1–Q5 finding is a finding about the *predicate text*, not about an implementation
that has been run; `reports/round-73/ledger.json` does not exist at base, so "pairs that already
match" is a demonstration that the text permits it, not an accusation that a ledger does it. The
245 → 247 post-C figure is [INFERENCE] from C's ENTRIES leg plus the counting command; I did not
land C. No network fetches, so no UA or Wayback question arose. No tool was installed or upgraded.
I did not run `accept-c.py`, any census, or any gate; I did not message other seats.

**Attacked, not judged.** This seat does not admit, edit, freeze or ship Ca. If the author adopts
F1–F7 verbatim the claim is attackable at freeze; if the draft is frozen as written, the honest
prediction is a repeat of round-69 Ca2 — PASS on the frozen predicate, FAILED AS DECLARED.
