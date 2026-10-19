- Seat: X02 | critic | cross | date 2026-10-19 | baseline 4a7aede

# X02 — conformance critic: append-only discipline, F-C13-1 prevention, entry-shape conformance

- Observation window: **08:07Z–08:18Z, 2026-10-19** (`date -u` = `2026-10-19T08:18:11Z`
  at the last reading). Lane HEAD `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`
  (committed `2026-10-19T05:01:17-03:00` = 08:01:17Z); round-35 declared at 08:05Z
  (`reports/round-35/telemetry/dispatch-declared.json`).
- Axes this seat works, named per Godspeed: (1) **coverage** of the conformance
  check surface — the C-claim's "10/10 audited clean" threshold made runnable
  instead of asserted; (2) **operability** — every leg below is a command with a
  named expected result; (3) **adjacency** — the boundary surfaces (filed rounds,
  `corpus/lessons`, `tools/gates/frozen`, `.ufo`) verified byte-clean.
- Role limits: this seat reads and reports. Its only write is this file. It runs
  no filed round runner (`F-C13-1` prevention), edits no corpus byte, admits no
  claim, and absorbs no sibling fragment's evidence as its own.
- Pinned inputs: `reports/round-35/claims.json` sha256
  `ccfaafc363981d16729c351fa11135e8082b1b0695dc399884d5c91bcc9e26e4`;
  `reports/round-35/targets.json` sha256
  `56ad03927c7063a3616af2ed0e78ab7b1ca1f3ea43fdf67f2ecf60a7f1b63215`.

## 0. Verdict summary

| # | Leg | Verdict at 08:18Z | Evidence |
|---|---|---|---|
| 1 | Append-only discipline (filed rounds 1–34, `corpus/lessons/*.md`, `tools/gates/frozen/**`, `.ufo/**`) | **green** | §1 |
| 2 | F-C13-1 prevention (no in-tree execution of any filed runner) | **green in flight; one close-time check owed to the integrator** | §2 |
| 3 | Entry-shape conformance of the 10 new entries | **7 of 10 read: 5 clean, 2 defects (D1, D2); wave threshold not established** | §3, §6.2, §6.3, `## Owed` |
| 4 | Declaration-language conformance of the round-35 declarations | **green** | §4 |

Finding count: **2** (X02-F1 shape-contract ambiguity, X02-F2 discovery-form
risk), both routed with owners; no defect against a landed artifact — the 10
entry drafts had not landed at this seat's close (§6). `op/O08-validation-legs.md`
landed at 08:19Z and already carries the **static** half of the F-C13-1 fence
(its O6 leg: the validator source must name no filed runner path); §2's
close-time receipt-integrity check is the **dynamic** complement, because a
source-level scan cannot detect a receipt that was written by some other
process. Both are needed; neither substitutes for the other.

## 1. Append-only discipline — green

Commands and observed results (all run in-tree, read-only; no command below
writes):

1. `git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`; the tree is
   still exactly at the declared baseline, so no filed byte can have moved
   relative to the pin.
2. `git status --porcelain=v1` → **1 line**, `?? reports/round-35/`. No tracked
   file is modified or staged; the whole round-35 working set is untracked and
   lives under the one permitted root.
3. `git diff --stat 4a7aede -- reports/round-1..34` → **empty**.
   `git diff --stat HEAD -- corpus/lessons` → **empty**;
   `git diff --stat 4a7aede -- tools/gates/frozen` → **empty**;
   `git diff --stat 4a7aede -- .ufo` → **empty**. All four protected surfaces are
   byte-identical to the baseline.
4. `git diff --stat 4a7aede` (whole tree) → **empty**: the zero-diff result is not
   an artifact of a narrow pathspec.
5. `find reports -maxdepth 2 -type f -newermt "2026-10-19 05:01:17" ! -path
   'reports/round-35/*'` → **no output**. Nothing under any filed round has an
   mtime inside the round-35 window; the newest filed receipt is
   `reports/round-34/validation.json` at `05:00:03` local = 08:00:03Z, i.e.
   round-34's own close, four minutes *before* the round-35 declaration.
6. `corpus/lessons` census: 33 `.md` files + 8 subdirectories + `README.md`
   (`ls corpus/lessons | wc -l` = 42) — the 33-file partition R09 owns is
   unchanged and untouched by this round's declared work.

Note on the limits of mtime evidence: mtimes are not digests. The load-bearing
append-only claim is #2/#3/#4 (Git objects vs the pinned commit); #5 is a
secondary, independently-consistent reading.

## 2. F-C13-1 prevention — green in flight, one close-time check owed

**The hazard class, restated from the filed record.** `LOG.md:3548-3567` records
that during round 33, `reports/round-{5,6,7}/validation.json` were rewritten
in-tree and restored byte-exact; `LOG.md:3556-3558` names the mechanism — those
runners write their own receipt in place (`reports/round-5/run-validation.py:194`,
`reports/round-7/run-validation.py:1171`, `reports/round-6/run-validation.py:336`)
and never adopted the round-14 receipt-guard. `LOG.md:3594-3603` (round-34
errata) corrects the round-33 record: r26 *is* guard-adopted; the unguarded class
is the r5/r6/r7 runners. `reports/round-34/op/adoption-inventory.json` lands the
census: `runner_count` 28, `class_counts` = 17 `guarded-refresh` / 11
`unguarded-in-place`, `hazard_count` 11; the route for the hazard class is
verbatim `isolated-copy-only: never execute in-tree; work from a git archive or
clone under .scratch (F-C13-1 prevention)`.

**Round-35 compliance evidence observed:**

1. **No filed receipt was written during this round.** See §1.5: zero files under
   `reports/round-1..34` carry an mtime inside the 08:05Z+ window.
2. **The three restored receipts are still byte-identical to their committed
   blobs** — the restoration has not been disturbed:
   `git hash-object reports/round-{5,6,7}/validation.json` equals
   `git rev-parse HEAD:reports/round-{5,6,7}/validation.json` for all three
   (`778c3f5e…`, `9f6a0f45…`, `e7a8d449…`).
3. **Seats are using the declared isolated-copy route.** `.scratch/o03-iso/tree/`,
   `.scratch/k03-iso/`, `.scratch/s04-iso/` are extracted copies with **no `.git`
   directory** (`[ -d <d>/.git ]` → `no`), and their `reports/round-6/run-validation.py`
   hashes to `c53f100927b8723bea25eeaa06048ace68fdfa3e763811a64e1104323e535c6e`,
   identical to the in-tree filed runner — i.e. the isolated copies are faithful
   archive extracts, not re-authored stand-ins. Runner output written inside a
   copy (`.scratch/s04-iso/reports/round-*/validation.json`, all 05:01) is
   out-of-tree and therefore outside the hazard.
4. **The guard tool itself is green**: `python3 -B tools/harness/receipt_guard.py
   --selftest` → `selftest_passed: true`, `controls_passed: 45 / controls_total: 45`.

**Residual risk and the owed close-time check.** Items 1–3 establish that no
in-tree write has happened *so far*. The hazard is a write, and writes happen at
the end of a round. The integrator therefore owes one mechanical check at close,
before `reports/round-35/validation.json` is filed:

```
git status --porcelain=v1 -- reports/round-1 reports/round-2 ... reports/round-34
# expected: empty. Any line here is an F-C13-1 recurrence; restore with
#   git checkout -- <path>   (filed bytes) and file an errata entry in LOG.md.
git hash-object reports/round-{5,6,7}/validation.json   # must equal HEAD blobs
```

Also owed to the validator author: `reports/round-35/run-validation.py` **must
not** execute any filed runner as one of its legs. The round-10 runner states the
convention explicitly (`reports/round-10/run-validation.py:39-42`: "It executes no
gate and re-runs none of the ledger's commands"; its self-description at
`:1029-1030` repeats "Cited commands are checked for ledger presence, not
re-executed here"). A round-35 leg that shells out to `reports/round-<N>/run-validation.py`
would reintroduce exactly the F-C13-1 hazard the round is hardening against.

**This leg already has a landed home** — `reports/round-35/op/O08-validation-legs.md:126-134`
(§2 O6) specifies the static scan: the validator source must contain no quoted
`--freeze` argv literal and no filed-runner path, with the refusal
`reports/round-35/op/O08-validation-legs.md:341` (R-f) naming "a validator that
executes any filed round runner in-tree (F-C13-1 class)". Read that as the
source-level half. The commands in the block above are the runtime half and stay
owed: O6 passes on a validator that never *names* a runner while some other seat
still writes a filed receipt in-tree. Neither half detects the other's failure
mode.

## 3. Entry-shape conformance — contract derived from the lane's own instruments

> Status note (added after the sweep): this section was written before any draft
> landed. Seven drafts were read afterwards — see **§6.2** for the per-draft
> results and **§6.3**/**§6.2** for defects D1 and D2. The contract, the census
> calibration and the recipe below are unchanged by that; only the wave verdict
> moved from "no draft on disk" to "5 clean / 2 defective / 3 never landed".

### 3.1 The binding shape, from the lane's own acceptance instruments

The corpus does **not** use YAML frontmatter. All 201 entries open with a
Markdown header line and a bullet-field block; `^---$` frontmatter matches **0**
files (census command §3.3, first leg). "Frontmatter" in this lane means that
opening bullet block. The field set is fixed by the round-10 acceptance runner:

- `reports/round-10/run-validation.py:81-82` —
  `C_FRONTMATTER_FIELDS = ("topic", "sources", "verified-at", "recheck", "couples")`
  (the lane's profile), with the docstring at `:13-14` stating the **claim
  minimum is `sources`/`verified-at`/`recheck`** and `:1018-1020` repeating it.
- `reports/round-10/run-validation.py:349-377` — `entry_checks()`, the four
  per-entry legs: (a) each of the five fields present via
  `^\s*[-*]?\s*<field>\s*:\s*(\S.*)$` (multiline, anywhere in the file — *not*
  header-block-only); (b) **a named gap** — a `gap: …` field/clause
  (`:363-364`) or a body heading naming the gap (`:365-366`); (c) **a
  decision-record section** — `^#{2,4}[^\n]*decision[- ]record[^\n]*` followed by
  a non-empty line (`:368-370`); (d) **≥1 retrievable locator** — an existing
  repo path (`corpus|tools|reports|examples/…`) or a URL (`:371-376`, `:110-112`).
- `reports/round-10/run-validation.py:380-399` — `readme_index()`: partition
  headings must match `^##\s+([a-z][a-z-]*)/\s*\((\d+)\)\s*$`, rows
  `^-\s+`<file>.md``, and the totals line `^Total knowledge entries:\s*(\d+)\.$`.
- `reports/round-19/audit-1.md:63-70` — the same bar applied to the round-19
  wave, with `gap filled:` as the recognized field form and `## 6. Decision
  record` as the recognized heading form; `:69` confirms `follows:` is required
  by neither bar, so its absence is not a defect.

### 3.2 Finding X02-F1 — the claims.json field list does not match the live contract

`reports/round-35/claims.json` (claim C) requires entries "frontmatter-complete
(**source / verified-at / recheck / scope**)" and the threshold "frontmatter
**4/4** or documented 3/4 class". Neither names the live sets:

- `- scope:` occurs in **0 of 201** entries (census §3.3, second leg). No
  acceptance instrument in the lane reads a `scope` header field.
- The live profile is **5** fields, the claim minimum is **3**
  (`reports/round-10/run-validation.py:81-82`, `:1018-1020`). There is no
  live 4-field set, so "4/4" is not checkable as written.
- The claims text also omits `topic` and `couples`. `topic` is load-bearing
  beyond the entry itself: `corpus/README.md` index rows must be **byte-equal**
  to the entry's own `- topic:` text (`corpus/README.md:6-8`, revision 1.9
  note). An author who follows the claims.json field list literally and omits
  `topic:` produces an entry that (i) fails the round-10 field leg, and (ii)
  cannot be reconciled into the index at all.

**Recommended binding for the integrator and the validator author** (this is the
repair, not a defect against any landed byte): treat
`("topic","sources","verified-at","recheck","couples")` as the required profile,
`sources`/`verified-at`/`recheck` as the non-negotiable minimum, and read "4/4"
as superseded text — or record the divergence explicitly in the round-35 receipt
as the round-34 `CO4` deviation was recorded. **Owner:** S04 (validator author) +
integrator. **Severity:** medium — it can only bite through a literal reading,
but the literal reading is the one the authors were handed.

The **documented 3/4 class** named by claims.json does exist and resolves:
`reports/round-8/metadata/m11-verification.md:103` records
`citation-format-and-source-registry.md`, `myth-consistency-gate.md`,
`provenance-audit-ledger-format.md` as "conformant before this pass (both fields
present in §1), **not edited**", and `:171` lists the same three under
`conformant_before`. Those are exactly the three entries whose `verified-at:`/
`recheck:` sit as §1 body bullets rather than in the opening block (my
header-block census, §3.3 leg 2). So the class is real, is pre-existing, and is
**not** available as a cover for a new draft: a round-35 entry that omits either
field from its opening block should be repaired, not excused by this precedent.

### 3.3 Census of the live corpus (the calibration for "audited clean")

Command (read-only, in-tree; no file written):

```
python3 - <<'PY'
import glob,re
FIELDS=("topic","sources","verified-at","recheck","couples")
def blk(t):
    i=t.find('\n## '); return t if i<0 else t[:i]
strict=loose=0
for f in sorted(glob.glob('corpus/knowledge/*/*.md')):
    t=open(f,encoding='utf-8').read()
    s=[x for x in FIELDS if not re.search(r'(?m)^\s*[-*]?\s*'+re.escape(x)+r'\s*:\s*(\S.*)$',blk(t))]
    l=[x for x in FIELDS if not re.search(r'(?m)^\s*[-*]?\s*'+re.escape(x)+r'\s*:\s*(\S.*)$',t)]
    strict+=bool(s); loose+=bool(l)
print("files",len(glob.glob('corpus/knowledge/*/*.md')),"strict_header_fail",strict,"loose_field_fail",loose)
PY
```

Observed: `files 201 strict_header_fail 3 loose_field_fail 0`; the three strict
failures are the documented class above. Additionally:

- YAML-frontmatter census: `^---\n…\n---\n` matches **0** of 201 files.
- `- scope:` present in **0** of 201 files; `- topic:` **201**, `- sources:`
  **201**, `- couples:` **201**, `- verified-at:` **198**, `- recheck:` **198**.
- Decision-record heading: **22 of 201** entries; any `decision` heading:
  **32 of 201**. **This is the calibration that matters** — the gap and
  decision-record legs are *new-entry* requirements, not corpus-wide invariants.
  A round-35 validator that applies them to all 201 files would fail ~180
  incumbent entries and reject a correct round. They apply to the 10 new drafts
  only, exactly as `reports/round-10/run-validation.py:425-442` scopes them (it
  iterates the discovered *new* entry set).
- Live README state: headings sum **201** = totals line **201** = index rows
  **201**; heading vector `linguistics 21 / myth-symbol 19 / culture-material 18 /
  synthesis 29 / verification 20 / civilizations 94`; footer
  `(total 201 files; directory totals 21/19/18/29/20/94)`. Live partition census
  by `ls corpus/knowledge/<p>/*.md | wc -l` matches every one of those numbers.
  Post-landing target: **culture-material 24, myth-symbol 23, total 211**, footer
  `(total 211 files; directory totals 21/23/24/29/20/94)`.

### 3.4 The recipe the integrator runs over the 10 applied drafts

Runnable as-is from the repo root once the drafts are applied to
`corpus/knowledge/**` (adjust the path list if the integrator lands them under
different filenames); it prints one JSON object per entry and a summary. It
replicates the round-10 regexes verbatim and adds the strict header-block leg as
a **reported, non-gating** observation:

```
python3 - <<'PY'
import re, sys, json, pathlib
ROOT = pathlib.Path('.')
FIELDS = ("topic","sources","verified-at","recheck","couples")
MIN    = ("sources","verified-at","recheck")
GAP    = re.compile(r"(?i)(?:^|[\s.;—–|-])gap(?:[\s-]+(?:filled|addressed|served))?\s*:\s*(\S[^\n]{0,300})")
GAP_H  = re.compile(r"(?mi)^#{2,4}[^\n]*\bgap\b[^\n]*\n(?:[^\n]*\n)*?[^\n\s][^\n]*$")
DEC    = re.compile(r"(?mi)^#{2,4}[^\n]*decision[- ]record[^\n]*\n+\s*(\S[^\n]*)")
PATHRE = re.compile(r"\b((?:corpus|tools|reports|examples)/[\w./-]+\.(?:md|json|py|yml|yaml|tsv|txt))\b")
URLRE  = re.compile(r"https?://[^\s`)\]]+")
paths = [pathlib.Path(x) for x in sys.argv[1:]] or sorted(
        pathlib.Path('corpus/knowledge').glob('*/*.md'))
bad = 0
for p in paths:
    t = p.read_text(encoding='utf-8')
    head = t[:t.find('\n## ')] if '\n## ' in t else t
    miss_loose = [f for f in FIELDS if not re.search(r'(?m)^\s*[-*]?\s*'+re.escape(f)+r'\s*:\s*(\S.*)$', t)]
    miss_min   = [f for f in MIN    if not re.search(r'(?m)^\s*[-*]?\s*'+re.escape(f)+r'\s*:\s*(\S.*)$', t)]
    miss_head  = [f for f in FIELDS if not re.search(r'(?m)^\s*[-*]?\s*'+re.escape(f)+r'\s*:\s*(\S.*)$', head)]
    loc = sorted({x for x in PATHRE.findall(t) if (ROOT/x).exists()})
    rec = {"entry": str(p), "missing_profile": miss_loose, "missing_minimum": miss_min,
           "missing_in_header_block": miss_head, "gap_named": bool(GAP.search(t) or GAP_H.search(t)),
           "decision_record": bool(DEC.search(t)),
           "resolving_repo_locators": loc[:6], "has_url": bool(URLRE.search(t)),
           "to_verify_marks": len(re.findall(r'\(to-verify\)|to-verify', t))}
    rec["clean"] = not miss_min and rec["gap_named"] and rec["decision_record"] and (loc or rec["has_url"])
    bad += not rec["clean"]
    print(json.dumps(rec, ensure_ascii=False))
print(json.dumps({"entries": len(paths), "not_clean": bad}))
PY
```

Expected result on the 10 applied drafts: `entries 10, not_clean 0`. Any
`missing_minimum` or `decision_record: false` is a repair, not a judgement call;
`missing_in_header_block` is reported for the integrator to weigh against the
documented 3/4 class. `to_verify_marks` is a count, not a verdict — the honesty
leg is X04's.

### 3.5 Finding X02-F2 — entry discovery must not be `git status`-only

`reports/round-19/run-validation.py:10` discovers new entries with
`git status --short | grep '^?? corpus/knowledge'`. If the integrator commits the
10 new entries before the round-35 validation run, that form returns an empty
set and the validator fails a correct round. The round-10 form is the robust one
and is the form to copy: **untracked ∪ added-vs-baseline**
(`reports/round-10/run-validation.py:420` → `discover_new_entries()`, with the
self-description at `:1016-1018`: "Entry discovery uses git (untracked ∪
added-vs-baseline); a staged-only or renamed-existing file is not counted as
new"). **Owner:** S04 / integrator. **Severity:** low (process), high if hit.

## 4. Declaration-language conformance — green

`grep -rniE "promot|certif|clearance|canon(ical)? (decision|truth)|\bapproved\b"`
over `reports/round-35/claims.json` and `reports/round-35/telemetry/*.json`
returns only: `claims.json:3` (`operator-approved` REGIMEN citation — a citation
of the operator's own approval, not a lane claim), `claims.json:60` and `:69`
(negations: "no promotion/canon/clearance/closure language … outside negations"
and the non-goal "no promotion, canon, clearance, or closure verdicts"), and
`targets.json:257` (A01's mission, itself a negation: "no canon/clearance
assertions"). Zero affirmative lane-owned canon/clearance language in the
declarations. This is the same reading A05/A08 will produce per-surface on the
artifacts; recorded here so the assembled audit has a declaration-level baseline.

## 5. Findings index (routed, not absorbed)

| ID | Finding | Owner | Severity |
|---|---|---|---|
| X02-F1 | `claims.json` C names a 4-field set (`source`/`verified-at`/`recheck`/`scope`) that matches no live contract; live profile is 5 fields, minimum 3; `scope` is 0/201 | S04 (validator author) + integrator | medium |
| X02-F2 | Entry discovery by `git status --untracked` alone (round-19 form) would return zero entries if the drafts are committed before validation | S04 / integrator | low, high if hit |

Carried risk, not a finding: the F-C13-1 close-time check (§2) and the
`no-filed-runner-execution` validator leg are owed by the integrator, not by
this seat.

## 6. Verification of this fragment's own deliverable, and citation scope

1. **The §3.4 recipe was extracted verbatim from this file and executed** — it is
   confirmed runnable, not merely written:

   ```
   python3 - <<'PY'   # extractor: pull the fenced recipe out of this fragment
   import re, pathlib
   t = pathlib.Path('reports/round-35/cross/X02-conformance.md').read_text(encoding='utf-8')
   blocks = re.findall(r'```\n(python3 - <<.PY.\n.*?\nPY\n)```', t, re.S)
   pathlib.Path('.scratch/x02-recipe.sh').write_text(max(blocks, key=len))
   PY
   bash .scratch/x02-recipe.sh     # no args → the recipe's own default: whole-corpus glob
   ```

   Observed summary line: `{"entries": 201, "not_clean": 179}`. That is an
   independent cross-check of §3.3, not a restatement of it: 201 − 22 entries
   carrying a decision-record heading = 179, so every entry failing `clean` fails
   on the decision-record leg, and **no** entry fails on the field or locator
   legs that the §3.3 census read clean. The recipe runs and its two readings
   agree.
2. **How to scope it to the drafts.** The recipe reads paths from Python argv, so
   the invocation form is `python3 - <path> [<path> …] <<'PY'` (alternatively,
   edit its default-glob line). Run against the 10 applied drafts, the expected
   summary is `{"entries": 10, "not_clean": 0}`.
3. **Citation scope — do not over-read the exemplars.** The three entries cited
   in `## Citations` for header-field shape are cited for **that shape only**.
   Two of them (`warrior-material-culture.md`, `trickster.md`) were run through
   the recipe and return `gap_named: false, decision_record: false` — correct for
   incumbent entries, and precisely why §3.3 insists the gap/decision-record legs
   are new-entry-only. Citing them endorses their header shape, not their
   gap/decision-record conformance; the integrator should not "repair" them this
   round.
4. **Limits of this seat's verdicts.** §1's append-only reading is Git-object
   based (load-bearing). §2's F-C13-1 reading is a point-in-time window (08:07Z–
   08:20Z) and expires at close — hence the owed runtime check. §3 is
   `could-not-evaluate`, not a pass: nothing in this fragment asserts that any
   draft is conformant, because none was on disk to read.

### 6.1 Recipe defect log, the extraction requirement, and the first draft verdict

The §3.4 recipe was tested against the first landed draft rather than assumed
correct; **two defects were found and are fixed in §3.4**:

- `paths = sys.argv[1:] or …` left argv entries as `str` and crashed on
  `p.read_text()` — observed `AttributeError: 'str' object has no attribute
  'read_text'`. §3.4 now reads
  `paths = [pathlib.Path(x) for x in sys.argv[1:]] or sorted(pathlib.Path('corpus/knowledge').glob('*/*.md'))`.
- the bash-wrapper form (`bash recipe.sh <path>`) does **not** forward its
  arguments into the heredoc and silently falls back to the whole-corpus glob — a
  fail-open if the integrator reads only the summary line. Do not use it.

**Verified invocation** (extract the recipe body to a file once, then):
`python3 -B .scratch/x02-recipe.py <entry.md> [<entry.md> …]`. Observed with the
fix: `{"entries": 1, "not_clean": 0}` for the known-good control
`corpus/knowledge/verification/verification-independence-anti-circularity.md`
**and** for the first landed draft (below). Against the 10 applied drafts the
expected summary is `{"entries": 10, "not_clean": 0}`.

**The drafts are fenced — extract before checking.** A draft wraps the entry in a
four-backtick fence because the entry itself contains three-backtick blocks
(`reports/round-35/cov/C02-entry-2.md:15` opens, `:203` closes). Running the
recipe on the fragment file would test the fragment's own prose against the entry
bar and report a false failure:

```
python3 - <<'PY'
import re, pathlib
frag = pathlib.Path('reports/round-35/cov/C02-entry-2.md').read_text(encoding='utf-8')
entry = re.search(r'^````markdown\n(.*?)\n````\s*$', frag, re.S | re.M).group(1)
pathlib.Path('.scratch/x02-c02-entry.md').write_text(entry)
PY
```

**First real entry-shape verdict of the round — `cov/C02-entry-2.md`: clean.** The
extracted entry (36 616 bytes, 186 lines) returns `missing_profile: []`,
`missing_minimum: []`, `missing_in_header_block: []`, `gap_named: true` (the
`- gap:` field form), `decision_record: true`, and **10 resolving in-repo
locators**: `corpus/knowledge/civilizations/{austronesia-philippines-taiwan,khmer-angkor,nazca}.md`
and `corpus/knowledge/culture-material/{calendar-festival-systems,cuisine-food-lexicon,material-culture-inference-method,textile-technology,trade-economy-lexicon,transport-mobility-lexicon,vessel-container-lexicon}.md`.
`has_url: false` is **not** a defect — the round-10 locator leg accepts an
existing repo path *or* a URL (`reports/round-10/run-validation.py:110-112`,
`:371-376`) — and the entry states its no-network condition in-file. Its 38
`to-verify` marks are the honest reading of a source-map entry authored without
network access; judging them is X04's honesty leg and C13/C14/C17's, not this
seat's. **Caveat: this is one draft of ten.** The other nine were absent at this
seat's close, so the `10/10 audited clean` threshold is *not* established here —
§3's verdict stays `could-not-evaluate` for the wave, with one entry now read
green.

### 6.2 Seven-draft conformance sweep (the wave as it stood at this seat's close)

`ls reports/round-35/cov/` → **7 of 10 drafts on disk** (C01, C02, C03, C05, C06,
C07, C08; C04, C09, C10 absent). Each draft's entry was extracted from its fence,
then run through the §3.4 recipe:

| draft | fence | profile 5/5 | minimum 3/3 | header block | gap named | decision record | resolving repo locators | `to-verify` marks | verdict |
|---|---|---|---|---|---|---|---|---|---|
| `cov/C01-entry-1.md` | 4-tick | yes | yes | yes | yes | yes | ≥6 | 42 | **clean** |
| `cov/C02-entry-2.md` | 4-tick | yes | yes | yes | yes | yes | 10 | 38 | **clean** |
| `cov/C03-entry-3.md` | 4-tick | yes | yes | yes | yes | yes | ≥6 | 24 | **clean** |
| `cov/C05-entry-5.md` | 4-tick | yes | yes | yes | yes | yes | ≥6 | 31 | **clean** |
| `cov/C06-entry-6.md` | 4-tick | yes | yes | yes | yes | yes | **0** | 39 | **defect D1** (§6.3) |
| `cov/C07-entry-7.md` | **3-tick** | yes | yes | yes | yes | yes | ≥6 | 15 | **clean** |
| `cov/C08-entry-8.md` | 4-tick | yes | yes | yes | yes | **no** | 6 | 61 | **defect D2** (below) |

Six of the seven carry the full five-field profile in the opening block, a named
gap, and a decision-record section. The two failures are both cheap form repairs,
not substance failures.

**Recipe fix 3 (found by this sweep).** The §6.1 extractor handled only a
four-backtick fence; C07 wraps its entry in a **three-backtick** ```markdown fence
(`reports/round-35/cov/C07-entry-7.md:40` opens, `:241` closes) because its entry
body contains no triple-backtick block. The extractor must therefore try the
four-backtick form first and fall back to the three-backtick form — both are
in use in this same wave, so a single-form extractor silently reports
`NO-FENCED-ENTRY` and the integrator would misread a correct draft as malformed.

**Defect D2 — `cov/C08-entry-8.md` has no decision-record section.**
C08's extracted entry has 13 numbered sections (`## 1.` … `## 13.`,
`.scratch/x02-C08-entry-8.md`), and **none is a decision record**: §10 is the
application/build protocol, §11 the calibration shelf, §12 the `(to-verify)`
census, §13 coupling notes. The entry's own `- topic:` line promises one —
"with a build order, **a decision record**, and a calibration shelf" — so the
promise is unfulfilled in the bytes. Inline uses of the word (`Two cross-cutting
decisions:` at `:125`, `Design decision:` at `:158`) do not satisfy the leg:
`reports/round-10/run-validation.py:368-370` requires a `^#{2,4}` heading naming
a decision record followed by a non-empty line, and the failure text it produces
is `:437-438` "no decision-record section". **Repair:** add the section (the
sibling drafts C01/C02/C03/C05/C07 all carry one; C02's and C07's are usable as
the house shape). **Owner:** C08's author or the integrator. **Severity:**
blocking for claim C if unrepaired, and it is the second defect of the same class
as D1 — a mechanical leg the draft's prose satisfies but its structure does not.

**Not established by this sweep, stated rather than omitted:** the wave threshold
`10/10 audited clean` (3 drafts never landed), the substantive quality of any
draft's sources (X04's honesty leg; the `to-verify` counts above are counts, not
verdicts), the audits C13/C14/C17 performed, and C11's synthetic +10 rehearsal
(R03/A07).

### 6.3 Draft defect D1 — `cov/C06-entry-6.md` fails the locator leg on citation form

**Observed.** C06's extracted entry returns `resolving_repo_locators: []` and
`has_url: false` under the recipe's locator leg, which is the round-10 leg
replicated verbatim (`reports/round-10/run-validation.py:110-112` `REPO_PATH_RE` =
`\b((?:corpus|tools|reports|examples)/[\w./-]+\.(?:md|json|py|yml|yaml|tsv|txt))\b`,
used at `:371-376`; the failure text it produces is `:439-442` "no retrievable
locator (existing repo path or URL)").

**Why, precisely.** C06 cites its in-repo sources as **bare basenames** inside
backticks (`` `cuisine-food-lexicon.md` ``, `` `architecture-settlement-lexicon.md:49` ``)
and its couplings as **partition-relative** paths
(`culture-material/architecture-settlement-lexicon.md`,
`myth-symbol/ritual-liminality.md:63,83,88,93`). It contains **no**
repo-root-prefixed file path and **no** URL. Its only `corpus/`-prefixed token is
the directory `corpus/knowledge/culture-material/` inside the `- gap:` grep
command, which the leg's extension-anchored regex cannot match.

**The pointers are substantively sound — measured, not assumed.** All **12** bare
basenames resolve on disk (`re.search(r'`([a-z0-9][a-z0-9-]*\.md)(?::[\d,\-]+)?`', entry)`
then `corpus/knowledge/*/<name>`), and **all 44** partition-relative couples
targets resolve (`corpus/knowledge/<target>`); zero unresolvable on either list.
So this is a **form defect against the binding leg**, not a fabricated or dangling
citation.

**Consequence if unrepaired.** The round-35 validator, if it copies the round-10
leg (the §3.1 precedent and the recommended binding), fails C06 → the
"10/10 new entries audited clean" threshold fails → claim C fails → the round is
rejected. The repair cost is minutes; the discovery cost at validation time is a
whole round.

**Recommended repair (a), owned by the C block.** Rewrite C06's in-repo
references to the repo-root form its four sibling drafts already use —
`corpus/knowledge/culture-material/cuisine-food-lexicon.md:17` rather than
`` `cuisine-food-lexicon.md:17` ``. C01/C02/C03/C05 pass the leg precisely because
they already cite this way, so the repair restores consistency rather than
imposing a new rule.

**Rejected repair (b).** Loosening the validator's locator leg to accept bare
basenames or partition-relative paths would diverge from the round-10 contract
without a recorded rationale, and a basename-only leg cannot detect an ambiguous
or wrong-partition pointer (12 basenames here resolve uniquely today, but
`color-symbolism.md`-class names could collide across partitions). If the
integrator nevertheless chooses (b), it must be recorded as a **declared
deviation with the collision caveat**, in the round-34 `CO4`/`repair.json` style
(`reports/round-34/run-validation.py:124-126` precedent cited by
`reports/round-35/op/O08-validation-legs.md:172-174`).

**Owner:** C06's author or the integrator (repair (a)); C13/C14/C17/R03 (the
defect register). **This is a draft defect row, not one of §5's instrument
findings** — §5's count of 2 (X02-F1, X02-F2) stands unchanged; the integrator
should carry D1 into the C-block defect register.

**Not checked by this seat, stated rather than omitted:** the substantive quality
of any draft's sources (X04's honesty leg), the audits C13/C14/C17 performed, and
C11's synthetic +10 rehearsal (R03/A07). This seat checked shape, field presence,
gap/decision-record presence, locator resolvability, and citation form only.

## Owed

- `reports/round-35/cov/C04-entry-4.md`, `C09-entry-9.md`, `C10-entry-10.md` —
  **3 of the 10 drafts were still absent at this seat's close.** Landed and read
  by this seat: C01, C02, C03, C05, C06, C07, C08 (§6.2 — five clean; C06 defect
  D1 §6.3; C08 defect D2 §6.2). Not on disk: C04, C09, C10
  (`ls reports/round-35/cov/` at 08:29Z → `C01,C02,C03,C05,C06,C11,C12,C14,C15,C16,C17`).
  The entry-shape verdict for those five is **could-not-evaluate**; the integrator
  runs §3.4 over the remaining drafts (extract the four-backtick block first,
  §6.1) and the wave threshold `10/10 audited clean` is established only when all
  ten read clean. Also still owed to the C block: `plan/P01-c-plan.md` (the topic
  and author assignments; absent, and several authors self-selected topics and
  flagged the de-collision risk in their own `## Owed`), and
  `scout/K01-coverage-census.md`.
- ~~`reports/round-35/cov/C11-readme-delta.md`~~ — **landed at 08:22Z and
  cross-checked green by this seat** (recorded here rather than re-filed):
  (a) its pinned README digest `053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`
  equals the live `sha256sum corpus/README.md` at HEAD, byte count 106 218, 493
  lines; (b) its baseline reading `21/19/18/29/20/94 = 201` equals this
  fragment's §3.3 census exactly; (c) its target vector `21/23/24/29/20/94`,
  totals `201 → 211` equals §3.3's target; (d) its cited lesson
  `corpus/lessons/round-19.md:115` resolves and carries the quoted sentence
  verbatim. So the README reconciliation leg is now covered by a landed fragment
  whose numbers agree with this seat's independent census — **no owed path
  remains for it**. The one thing this seat did *not* verify is C11's synthetic
  +10 rehearsal (`--apply` / sweep-synth readings), which is C-block review's
  (R03) and A-block's (A07) ground, not this seat's.
- **The runtime F-C13-1 receipt-integrity check (§2)** — no landed fragment owns
  it. `op/O08-validation-legs.md` (landed 08:19Z) owns the static half only
  (its §2 O6, refusal R-f). This is the one owed item that is *not* completed by
  a dependency landing; it is owed to the integrator at close, after all seats
  stop writing.

## Citations

Paths and lines relied on (all resolve at HEAD `4a7aede` unless stated):

- `REGIMEN.md:25-50` (per-round contract), `:60-69` (scope, provider deviations)
- `reports/round-35/claims.json` (whole file; sha256 `ccfaafc3…`), claim C at
  `:20-36`, non-goals `:67-73`
- `reports/round-35/targets.json` (sha256 `56ad0392…`), `shared_rules` `:5-13`,
  seat X02 `:386-392`, seats C01–C10 `:64-133`, C11 `:134-140`
- `reports/round-35/telemetry/dispatch-declared.json` (declaration stamp 08:05Z;
  `standing_rules_of_note`; `closing_snapshot: open-at-seat-close`)
- `AGENTS.md` (repo root) — append-only LOG rule, telemetry rule, "close what you
  open"
- `PROVINCE.md:9-16` (owns), `:18-22` (refuses), `:24-26` (adjacent contract)
- `LOG.md:3548-3567` (F-C13-1 incident record: window, mechanism, sites
  `reports/round-{5,6,7}/run-validation.py:194/:336/:1171`, prevention)
- `LOG.md:3594-3614` (round-34 errata: r26 guard-adopted; adoption census
  28 runners / 17 guarded / 11 unguarded; `CO4` deviation precedent)
- `reports/round-34/op/adoption-inventory.json` — `runner_count` 28,
  `class_counts`, `hazard_count` 11, `protocols.unguarded-in-place`,
  `declared_hazards[0..3]`, findings `RGA-1-round-26` / `RGA-2`
- `reports/round-10/run-validation.py:11-18` (claim C contract), `:39-44`
  (fail-closed, executes no gate), `:81-82` (`C_FRONTMATTER_FIELDS`),
  `:100-101` (`INVENTORY_COMMAND`), `:110-112` (locator regexes), `:349-377`
  (`entry_checks`), `:363-370` (gap/decision regexes), `:380-399`
  (`readme_index`), `:418-451` (`measure_c`), `:1015-1020` (limits text)
- `reports/round-19/audit-1.md:63-70` (round-19 entry census; `gap filled:` form;
  `## 6. Decision record`; `follows:` not required), `:6-16` (role limits,
  instruments)
- `reports/round-19/run-validation.py:10` (git-status-only discovery — the
  X02-F2 precedent), `:19-21` (writes its own receipt in place)
- `reports/round-8/metadata/m11-verification.md:103`, `:171`, `:187-192`
  (the documented 3/4 class: three entries conformant with the fields in §1)
- `corpus/QUALITY.md:3-21` (admission bar: provenance, calibration, coupling,
  usability, canon hygiene)
- `corpus/README.md:1-11` (revision 1.9: totals 201, footer vector
  `21/19/18/29/20/94`, index rows byte-equal to each entry's `- topic:`),
  `:123-245` (partition headings), `:469-473` (totals + counts footer),
  `:475-493` (dated index-row re-measurements)
- `corpus/knowledge/culture-material/warrior-material-culture.md:1-8`,
  `corpus/knowledge/myth-symbol/trickster.md:1-8`,
  `corpus/knowledge/myth-symbol/flood-traditions.md:1-10` (exemplar shape: header
  line, `- topic:`, `- sources:`, `- couples:`, `- verified-at:`, `- recheck:`)
- `corpus/knowledge/verification/{citation-format-and-source-registry,
  myth-consistency-gate,provenance-audit-ledger-format}.md` §1 (the three
  header-lax entries)
- `tools/harness/receipt_guard.py:1-12` (guard contract; `REFRESH_RECEIPTS=1`
  only override; refusal exit 3)
- `tools/source-audit-inventory.py` (`--help`; `--json --summary --root
  corpus/knowledge` → `totals.files 201`, `read_only: true`)

Commands run (all read-only; none writes, none executes a filed runner):

- `git rev-parse HEAD`; `git status --porcelain=v1`; `git diff --stat 4a7aede`
  (whole tree and each protected path); `git hash-object` vs `git rev-parse
  HEAD:<path>` for `reports/round-{5,6,7}/validation.json`
- `find reports -maxdepth 2 -type f -newermt "2026-10-19 05:01:17" ! -path
  'reports/round-35/*'`; `find reports -maxdepth 2 -name validation.json
  -printf '%TY-%Tm-%Td %TH:%TM:%TS %p\n' | sort -r`
- `for p in linguistics myth-symbol culture-material synthesis verification
  civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done`
- `python3 -B tools/source-audit-inventory.py --json --summary --root
  corpus/knowledge` → `totals.files 201`
- `python3 -B tools/harness/receipt_guard.py --selftest` → 45/45, passed
- the two in-line `python3 - <<'PY'` censuses quoted in §3.3 (field/heading
  census; README heading/row/total parse)
- `ls -d .scratch/{o03-iso/tree,k03-iso,s04-iso,o11/iso}` + `.git` presence test
  + `sha256sum` of the isolated copy's `reports/round-6/run-validation.py`
- `date -u +%FT%TZ`; `git log -1 --format='%cI'`
