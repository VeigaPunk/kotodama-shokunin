- Seat: S01 | scribe | cross | date 2026-10-19 | baseline 7ceff59

# S01 — round-43 integration draft: three claims, two stale premises, one blocking collision

**Mission (`reports/round-43/targets.json`, seat S01):** *"Integration scribe: assemble the
whole round — all three claims' evidence chains, the per-axis verdict candidates, the SHONEN
section — into the integration draft the parent uses to land + judge."* Out path: this file only.

**Status: DRAFT, written mid-wave.** This seat wrote **zero bytes** outside this file (the only
other writes are disposable `.scratch/s01/` probes). No `reports/round-*/run-validation.py` was
executed anywhere, in-tree or in a copy. Every number below was measured read-only by this seat at
HEAD `7ceff59a0216a8ea21ee43262d9fc72abf770cee` under
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, or is attributed to the sibling fragment
named beside it. Nothing here asserts promotion, canon, clearance or closure; those words appear
only as negations, quoted scanner patterns, or routed references.

**Wave census, two cuts (this seat's `find reports/round-43 -type f | sort`):**

- **16:50Z cut — 3 files:** `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`.
  No peer fragment had landed; O04, O12 and C07 each independently recorded the same empty-tree
  observation in their own fragments.
- **17:00Z cut — 16 files:** the three above plus `scout/K01-resolver-scout.md`,
  `scout/K02-landing-scout.md`, `op/O02-controls.md`, `op/O04-verify.md`, `op/O07-durability.md`,
  `op/O12-negative-proof.md`, `cov/C01-prepare.md`, `cov/C02-readme-draft.md`, `cov/C03-audit.md`,
  `cov/C05-delta-receipt.md`, `cov/C06-collision.md`, `cov/C07-scribe.md`.

The integrator must recompute the census at close; never trust either count. §8 lists the seats
whose fragments were still absent at the final cut.

---

## §0 — The headline the integrator must read first

1. **Claim C is blocked by a live topic collision, not by a landing defect.** The r42 C01 spare
   targets `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`, which **already exists** at
   HEAD — a 192-line, 61,884-byte entry landed by r42's C04 in commit `7ceff59` (sha256
   `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f`). The live partition is
   **26/223**, and the README indexes the owner at `corpus/README.md:219`. The spare is a *second
   draft of the same lithic register*, not a missing slot: r42's own receipt says "C01 and C04
   authored the same lithic register mid-wave; C04 lands, C01 routes as the named spare"
   (`reports/round-42/validation.json`, claim-C ruling). Landing it at its declared path
   overwrites; landing it under a new slug creates duplicate ownership. **Neither is a lawful
   224.** Four sibling seats (C01, C02, C06, C07) independently reached the same verdict.
2. **Claim O's `before` is half stale, but the remaining delta is real.** A durable instrument
   already exists and is committed: `tools/harness/couples-reference-extractor.py` (r42; sha256
   `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`). Its `--selftest` is
   **8/8 PASS** and it reads the wrapped field **4/4 by identity**; live census is
   **223 entries / 2730 refs**. The r43 increment is narrower and genuine: the **disposition leg**
   (every fallback mapping listed, every unresolved/ambiguous row reasoned), a **synthetic
   ambiguous** control, a **blank-line field-boundary** fix, and a filed census artifact. Do not
   re-mint D1 as "missing"; do not ship a duplicate resolver that ignores the landed one.
3. **The four-class arithmetic has two defensible folds and the peers used both.** The r42 tool
   prints six buckets: `2556 direct + 166 fallback + 2 unresolved + 5 prospective + 1
   glob-fragment = 2730`. O04/K01 fold the glob fragment into `unresolved` and get
   **`2730 = 2556 + 166 + 0 + 8`** (`op/O04-verify.md:121-156`; K01 §6); O03/O10 apply policy
   §5.6's "skip or separately class" and get **`2556 + 166 + 0 + 7 = 2729`, plus 1 quarantined
   glob = 2730** (`op/O03-predicted.md` §0; `op/O10-census-artifact.md` §0.2). Both reconcile and
   neither drops a token. The artifact must print **which fold it used** and the one-token
   exclusion; a reader must not have to guess why 2729 and 2730 both appear. A tool that prints
   four classes without sub-reasons loses the distinction; a tool that prints six buckets without
   the four-class total fails the claim.
4. **The r42 extractor has a confirmed over-capture edge the r43 tool must fix.** Its
   `couples_block()` does `if not following.strip(): continue`, so an **indented prose paragraph
   after a blank line** is captured as couples tokens. This seat reproduced it in memory: a
   fixture with `- couples: myth — \`sound-symbolism.md\``, a blank line, then indented prose
   naming `prose-token.md` classifies **both** tokens (`prose-token.md` → `unresolved`). K01 §5
   (F5) found the same edge independently. The fix is `break` at the blank line, not `continue`;
   the filed r42 instrument must not be edited.
5. **Claim Ca is executable, and two of the queue's three O02 sub-findings do not reproduce.**
   `r38-O07-empty-fragment` reproduces (`wc -c` → **0**). `r38-O08-fragment-defect` reproduces
   (O01 declares `e5812751…`, O08 declares `ae22013b…` and calls it identical). But
   `r38-O02-fragment-defects` D-1 and D-2 are **not reproducible against the filed O02 bytes**:
   O02 says "plus 45 controls" at `:20`, `:62` and `:203` (also at `dfb0719`), and its in-sync row
   at `:63` names the carried manifest — the "44 controls" and "names nothing" quotations live in
   **O03-verify.md:259-260** and **O02-isolated.md:99** (a different, rejected control),
   respectively. A disposition pass that copies the queue row forward would launder a
   misquotation. §4 tables all 20 rows.
6. **The round runner is absent at this cut.** `reports/round-43/run-validation.py` does not
   exist. It is close-time and integrator-only; §6 is the leg spec it should implement. One leg
   must not be copied blindly from r42: r43's `telemetry/dispatch-declared.json` uses
   `declared_artifacts` (not `durable_sources`), and the **live `claims.json` no longer matches
   its declared digest** (declared `beda7644…` / 6,353 B; live `9662e2bd…` / 6,546 B). `targets.json`
   matches (`44d1f7ce…` / 12,285 B).
7. **Admission candidate: NOT ADMITTED on C** under the regimen rule ("admit only when every
   claim verifies"), unless the integrator re-scopes C before close. O and Ca can be admitted on
   their own evidence if their artifacts land and verify; a re-scoped C would be a *new* claim,
   not this spare. The r42 precedent (rejected on C, O verified) is the honest template.

---

## §1 — Window, state pins, and what "first-hand" means here

| pin | value | command |
|---|---|---|
| lane HEAD / declared baseline | `7ceff59a0216a8ea21ee43262d9fc72abf770cee` / `7ceff59` | `git rev-parse HEAD`; `git rev-parse --short HEAD` |
| working tree | only `?? reports/round-43/` untracked; no tracked modification | `git status --porcelain` |
| corpus total | **223** (`linguistics 25`, `myth-symbol 26`, `culture-material 25`, `synthesis 29`, `verification 24`, `civilizations 94`) | `for d in corpus/knowledge/*/; do ls "$d"*.md \| wc -l; done` |
| corpus README | revision **2.4**, totals line 223, footer vector `25/26/25/29/24/94` | `grep -n '^revision:' corpus/README.md`; `:544`; `:548` |
| README sha256 | `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` | `sha256sum corpus/README.md` |
| sweep baseline | exit 0, `rows 223 files 223`, `missing_from_index 0`, `topic_mismatch 0`, `footer_ok True` | `python3 -B reports/round-28/readme/sweep.py` |
| r43 declared digests | `targets.json` matches; `claims.json` **mismatches** | `sha256sum` vs `telemetry/dispatch-declared.json` |
| r42 extractor | sha256 `d8d23a26…`; selftest 8/8; census 223/2730 | `sha256sum tools/harness/couples-reference-extractor.py`; `--selftest`; `--census` |
| r19 filed instrument | sha256 `e7992c325a479aa7415c42722a034a95a9ea342a58367ead9cd2636a5a62830c`; still zeroes the wrapped field | `python3 -B reports/round-19/audit/entry-audit.py corpus/knowledge/linguistics/phonetics-phonology.md` |
| r39 policy, filed | 107 lines / 5,832 B, sha256 `105dfff6…`, truncated mid-§6 | `wc -l`; `tail` |
| r42 full policy | 263 lines, sha256 `8c3d7c35…` | `wc -l`; `sha256sum` |
| defect queue v2 | sha256 `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`; 38 rows | `sha256sum`; `python3 -c` row census |

"First-hand" means opened or executed by this seat in the window above. Sibling figures are
attributed in the paragraph where they appear and were not re-derived; where a sibling figure and
this seat's measurement disagree, both are printed.

---

## §2 — Claim O (operability): what is actually left to build

### 2.1 The policy's four classes and the wrapped field

The policy (full successor doc, `reports/round-42/calib/basename-couples-policy-full.md`):

| class | rule | carried evidence |
|---|---|---|
| `direct` | Tier 1: `<entry dir>/<token>`, `<lane root>/<token>` or `corpus/knowledge/<token>` exists | token only |
| `fallback` | Tier 1 failed, token slash-free, exactly one `corpus/knowledge/*/*.md` basename hit | **explicit `token -> path` mapping** (§3.3) |
| `ambiguous` | Tier 1 failed, slash-free, ≥2 basename hits | candidate paths, never guessed |
| `unresolved` | Tier 1 failed, slash-free, 0 hits | named reason, never dropped |

The corpus's **only** wrapped `couples:` field is `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
(sha256 `b4f9b003…`; 325 lines, 20,405 B). Its six physical parts join to four tokens, and the
line break falls inside the filename `tone-prosody.md`:

```
sound-change.md      unresolved (declared-prospective)
sound-symbolism.md   direct
tone-prosody.md      unresolved (declared-prospective)
writing-systems.md   direct
```

The r19 filed instrument still reads **0** tokens there:
`python3 -B reports/round-19/audit/entry-audit.py corpus/knowledge/linguistics/phonetics-phonology.md`
→ `FAIL … src=15/15 couples=0 unresolved=[] gap=False`, `TOTAL 0/1`, exit 2. Its defect is
`reports/round-19/audit/entry-audit.py:75` (`re.search(r"^- couples:\s*(.*)$", text, re.M)`).
**A 4/4 couples read does not flip this gate green** — the failing threshold is `gap=False`; no
leg may claim otherwise.

### 2.2 What exists at HEAD (do not re-mint it)

`tools/harness/couples-reference-extractor.py` (r42) already implements block extraction,
hyphen-soft-wrap healing, brace expansion, the two tiers, group alignment, a fifth
`prospective` class and a `glob-fragment` class. Executed:

```
$ python3 -B tools/harness/couples-reference-extractor.py --selftest
PASS wrapped positive 4/4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS wrapped positive heals soft wrap
PASS unwrapped regression
PASS over-capture trap (prose excluded) ['sound-symbolism.md']
PASS phantom negative: absent wrapped targets are visible, not zeroed {...}
PASS N6 regression guard: single-line capture still yields 0 tokens
PASS N6 regression guard: block read yields 4 tokens [...]
PASS glob fragment classified
exit=0

$ python3 -B tools/harness/couples-reference-extractor.py --census
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)
  misaligned: none
```

Its remaining defects, all confirmed:

- **D2 disposition leg absent from the census.** `--census` prints totals and the unresolved
  distinct list, but **not** the 166 fallback mappings, not per-entry detail, and not a reason per
  unresolved/ambiguous row. This is the genuine r43 increment.
- **No synthetic ambiguous control.** The corpus has 223 entries with 223 distinct basenames and
  **0 duplicates**, so the ambiguous branch cannot be exercised without an injected index
  (O02 §0, measured `reports/round-43/op/O02-controls.md:29-37`).
- **Blank-line over-capture (K01 F5; this seat reproduced).** A blank line does not terminate the
  field (`couples-reference-extractor.py:64-65` → `continue`), so an indented prose paragraph after
  the field is captured. Confirmed with an in-memory fixture: tokens
  `['prose-token.md', 'sound-symbolism.md']`, classes `unresolved` / `fallback`.
- **A fifth/sixth class is not the policy's four.** `prospective` (5) and `glob-fragment` (1) must
  become named sub-reasons of `unresolved`, not separate policy classes (K01 §6; O04 §2).

### 2.3 Measured census and the reconciliation

Live at HEAD, from the r42 extractor and independently from O04's oracle
(`reports/round-43/op/O04-verify.md:121-156`):

```
six buckets (r42 tool):      2730 = 2556 direct + 166 fallback + 2 unresolved + 5 prospective + 1 glob-fragment
fold A (O04/K01, glob in):   2730 = 2556 direct + 166 fallback + 0 ambiguous + 8 unresolved
                             where the 8 = 2 true + 5 declared-prospective + 1 glob-fragment
fold B (O03/O10, §5.6):      2730 = 2556 direct + 166 fallback + 0 ambiguous + 7 unresolved + 1 quarantined glob
                             (2729 in the four classes + 1 separately classed exclusion)
```

O03's prediction and O10's artifact use fold B (`op/O03-predicted.md` §0: `2556+166+7+1=2730`;
`op/O10-census-artifact.md` §0.2: `2556+166+0+7=2729`, `2729+1=2730`); O04's independent oracle
and K01 §6 use fold A. **Both are correct under the policy; the census artifact must state its
fold and the excluded token.** The distinction is not cosmetic: under fold B, "unresolved=7" is
the finding count and the glob fragment is a named exclusion; under fold A, "unresolved=8" is the
arithmetic closure. A runner that asserts one number without the convention will red a correct
artifact or green a dropped token.

Baseline cross-check against the r42 filed census (`reports/round-42/op/couples-census-corrected.json`):
the 220-entry era read `2611 = 2437 + 166 + 0 + 8`. The three entries r42 landed contribute
**119 refs, all direct** (mineral 44 + purity 36 + sacred-topography 39), and
`2611 + 119 = 2730`, `2437 + 119 = 2556`. The census is monotone and attributable. O10 also
measured a population digest over the 223 entries (sorted `path:sha256` lines):
`444ff801727604b614e1eca302ff77314ebbd0f5f064a82d1c167e7f02125e35` — the artifact should pin it
so a later census can prove the population, not only the totals.

Fallback spread (this seat, per-entry token classification): **166 occurrences over 50 distinct
tokens in 21 carrier entries**; target partitions `linguistics 67, culture-material 53,
myth-symbol 30, synthesis 8, verification 5, civilizations 3`; **0 misaligned**. Appendix A lists
every distinct mapping (the policy requires the mapping, not only the count; one mapping covers
every occurrence of that token).

### 2.4 What a conformant r43 tool must output

Shape (folded from K01 §6 and claim O's `after_required`):

```json
{
  "schema": "kotodama-basename-couples-census-v1",
  "tool": {"path": "tools/harness/basename-couples-resolver.py", "sha256": "<pin>"},
  "population": {"entries": 223,
                  "digest": "444ff801727604b614e1eca302ff77314ebbd0f5f064a82d1c167e7f02125e35"},
  "entries": 223, "refs": 2730,
  "fold": "policy-5.6-quarantine | glob-into-unresolved",
  "totals": {"direct": 2556, "fallback": 166, "ambiguous": 0, "unresolved": 7},
  "subclasses": {"unresolved_true": 2, "unresolved_declared_prospective": 5,
                  "unresolved_glob_fragment": 1},
  "excluded": {"glob_fragment": 1, "reason": "policy §5.6; not a couples finding"},
  "wrapped_fields": [{"path": "corpus/knowledge/linguistics/phonetics-phonology.md",
                       "parts": 6,
                       "tokens": ["sound-change.md", "tone-prosody.md",
                                  "sound-symbolism.md", "writing-systems.md"]}],
  "entries_detail": [{"path": "...", "wrapped": false,
                       "tokens": [{"token": "...", "class": "direct|fallback|ambiguous|unresolved",
                                    "mapping": "corpus/.../x.md|null", "reason": "...",
                                    "carrier_line": 37, "group": "linguistics|null",
                                    "alignment": "ok|MISALIGNED|null"}]}],
  "fallback_mappings": [{"token": "...", "path": "corpus/.../x.md", "occurrences": 14,
                          "carriers": ["..."], "group": "...", "alignment": "ok"}],
  "unresolved": [{"token": "...", "count": 2, "carriers": ["...:14", "...:16"], "reason": "..."}],
  "ambiguous": []
}
```

Non-negotiable properties: the four-class arithmetic closes **under the stated fold** (fold B:
`2556 + 166 + 0 + 7 = 2729`, `+1 excluded = 2730`; fold A: `2556 + 166 + 0 + 8 = 2730`); every
fallback mapping listed; every unresolved/ambiguous row carries a named reason and carrier; glob
fragments reported separately and excluded from the finding count (§5.6); brace expansion one
level, `:NN` anchors stripped, per-entry dedup; **blank line OR next header field terminates the
field**. The artifact also names its producing tool and sha256 — if it is a new
`basename-couples-resolver.py`, it must **wrap or explicitly supersede** the r42 extractor, not
silently diverge from it (O06 §1; O10 §0.1).

Selftest minimum: wrapped positive **by identity** (not merely four tokens — space-join and
hyphen-delete both produce four wrong tokens), hyphen-heal (`tone-prosody.md` present,
`prosody.md` absent), phantom negative (0 hits → `unresolved`), synthetic ambiguous (two injected
hits → `ambiguous`, both candidates listed, not guessed), direct positive (Tier 1 never relaxed),
unwrapped regression, glob-fragment check, and the blank-line boundary negative. O02's fenced
battery already specifies S1a–S4c and executes red/green against a stub host
(`reports/round-43/op/O02-controls.md`); it is the strongest available selftest spec.

### 2.5 Routing

O01's tool draft was **absent at every cut of O04's seat** (`reports/round-43/op/O04-verify.md:1-20`
→ `could-not-evaluate`, not a pass) and remains absent at this cut. O12's negative proof is
likewise **conditional**: live tree PASS, wrapped field PASS, **r43 draft could-not-evaluate —
draft absent** (`reports/round-43/op/O12-negative-proof.md:0-25`). O07 fixes the canonical path as
`tools/harness/basename-couples-resolver.py` and requires in-memory fixtures (zero `.scratch`
dependency; the r42 selftest leaves temp dirs). O03's prediction supplies the exact numbers and
the fold-B convention; O06 specifies the per-row disposition shape and the artifact contract;
O10 supplies the fill-ready census artifact plus the population digest. The integrator must apply
O01's tool with O02's battery and O06/O10's output contract, then re-run the O04 matrix (R1–R10)
and the O05 traps before claiming O. **A second tool that neither wraps nor supersedes the r42
extractor is a divergence, not a fix** (O06 §1, O10 §0.1).

### 2.6 Verdict candidate

- **If the tool lands and the selftest/census legs pass:** operability **improved** — the
  disposition leg and census artifact are new durable capability; D1 is *not* re-claimed.
- **If only the r42 extractor is cited:** operability **unchanged** (the claim's `after_required`
  is not met; no census artifact, no ambiguous control, no disposition leg).
- **If a duplicate resolver ships without reconciling to the r42 extractor:** **harmed**
  (two diverging instruments; the r42 census pin `d8d23a26…` no longer identifies the policy
  implementation).

---

## §3 — Claim C (coverage): blocked by a live topic collision

### 3.1 The collision, measured four ways

1. **The path exists and is tracked:**
   `git ls-files corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` → the file;
   `wc -lc` → **192 lines, 61,884 bytes**; sha256 `c99f44ca…`; clean at HEAD.
2. **It is r42's C04 landing, byte-exact:** the fenced body of
   `reports/round-42/cov/C04-entry-4.md` hashes to the same `c99f44ca…` (C01 §2, C07 §3.1).
3. **The r42 record says the two drafts are the same topic:** `reports/round-42/validation.json`
   ruling quoted in §0.1; the spare's own header at `reports/round-42/cov/C01-mineral-spare.md:1`
   repeats it.
4. **The README indexes the owner:** `corpus/README.md:205` (`## myth-symbol/ (26)`) and
   `:219` (the lithic row); revision 2.4 at `:5-12` already documents the landing and the spare
   routing.

### 3.2 The live partition (26 names, observed)

```
animal-symbolism.md            binding-speech-complex.md      celestial-symbolism-calendars.md
color-symbolism.md             comparative-frameworks.md      cosmology-cosmography.md
creation-myths-taxonomy.md     death-afterlife-eschatology.md direction-symbolism.md
divination-omen-systems.md     eschatology-world-end-systems.md flood-traditions.md
hero-journey-variants.md       mineral-stone-symbolism.md      motif-index-usage.md
myth-folktale-genres.md        myth-ritual-theories.md         number-symbolism.md
pantheon-archetypes.md         plant-symbolism.md              purity-pollution-boundary-systems.md
ritual-liminality.md           sacred-kingship-mythic-charter.md sacred-topography-pilgrimage.md
symbolism-synthesis-method.md  trickster.md
```

### 3.3 The spare

`reports/round-42/cov/C01-mineral-spare.md`: 219 lines / 55,433 B, sha256 `2b9326e3…`; fenced
body lines 4–218, byte range **[328, 55,429)**, 55,101 B, sha256 `6999a912…` (C01 §5). Its only
pre-fence text is the integrator ruling; **it names no target path itself**. The declared path is
in the r42 fragments: `reports/round-42/cov/C01-entry-1.md:3` and `:28` →
`corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` — **OCCUPIED**.

The spare's head block is also **stale as a landed entry**: its `- gap filled:` asserts
"the lithic slot is named but never built", "no entry owns stone", 220 files and a 0-hit sweep;
HEAD is 223 files with a true owner (C01 §3). Applying it unmodified would import false measured
claims, which `corpus/QUALITY.md:5-8` bars.

### 3.4 Why there is no lawful route to 224

| route | outcome | verdict |
|---|---|---|
| land at the declared path | `M` not `A`; overwrites a tracked entry | forbidden by claim's own "no existing entry overwritten" (`claims.json:41`) and shared rule (`targets.json:9`) |
| land under a free slug (e.g. `stone-symbolism.md`) | 27/224 mechanically, but two entries own one register; the spare's gap line becomes false; README would list two lithic rows | duplicate-topic collision; the exact condition r42 routed the spare *away* from |
| replace/retire the C04 entry | count stays 26; overwrite of filed corpus bytes | outside claim authority; needs its own operator ruling and provenance record |
| no landing | 26/223, claim C fails as declared | the honest outcome; matches r42's rejection precedent |

The sweep is **not** a collision detector: it checks row↔file correspondence and topic equality
(`reports/round-28/readme/sweep.py:74-84,136-146`), so a duplicate-topic 224 would sweep green.
C02 demonstrated exactly this with a simulated 224 tree (`reports/round-43/cov/C02-readme-draft.md`
§3, §6 Variant A) — **do not let that green become the verdict.**

### 3.5 Peer agreement

C01 (blocked; contract-complete but topical defect), C02 (blocked; conditional rev-2.5 diff and an
honest no-bump variant), C06 (FAIL collision; full listing), C07 (cannot be admitted; do not
apply), K02 (COLLISION; target occupied). No sibling proposed a workaround, per the shared rule.

### 3.6 Verdict candidate

Coverage **unchanged** (223/26, no corpus delta). Claim C **failed as declared / blocked-by-
collision**; round **NOT ADMITTED on C** unless re-scoped. File the collision as a successor
queue row with owner `integrator` and next touch `operator re-scope or retirement`; keep the spare
routed. Do **not** edit `reports/round-42/**` or `corpus/**`.

---

## §4 — Claim Ca (calibration): per-finding disposition pass

### 4.1 The four carried rows at HEAD

| queue row | origin | re-measurement at HEAD |
|---|---|---|
| `r39-review-findings-disposition` | R01-2..R01-14 unrecorded | `grep -c 'R01-' reports/round-39/validation.json` → **0**; LOG r39 names R01-1 only; R01-1's ruling is in `reports/round-39/calib/recount-ledger-successor.json` note |
| `r38-O02-fragment-defects` | O03 §4.1–4.3 | D-3 reproduces as a substantive leg mis-attribution; **D-1 and D-2 do not reproduce against the filed O02 bytes** (§4.3) |
| `r38-O08-fragment-defect` | O03 §4.4 | **reproduces**: O01 `e5812751…` (`O01-guard-design.md:144,:309`) vs O08 `ae22013b…` (`O08-regression.md:18,:80,:83`), identity assertion false |
| `r38-O07-empty-fragment` | LOG.md:3741 | **reproduces**: `wc -c reports/round-38/op/O07-scribe.md` → **0** |

### 4.2 Per-finding disposition table (integration candidate)

Class definitions used: **fixed-with-evidence** = a durable successor artifact exists and a
re-run command reproduces the fix; **recorded** = a successor record (queue row/correction note)
carries the finding and the filed bytes stay immutable; **routed-with-owner** = a future action
with a named owner; **could-not-recover** = the claimed condition is not reproducible at HEAD,
with owner and reason. This table is the integration-side candidate; Ca01 owns the filed artifact.

| # | finding (source) | class | owner | evidence (re-run) |
|---|---|---|---|---|
| 1 | R01-1 replay mechanism ruling (`R01-review.md:226-247`) | recorded | integrator | `recount-ledger-successor.json:4` note folds the ruling; `LOG.md:3745-3761` |
| 2 | R01-2 protocol names 3 absolute runners, measured 5 (`:182-190`) | routed-with-owner | integrator / next protocol revision | `R01-review.md:182-190`; protocol text at `reports/round-39/calib/isolation-replay-protocol.md` |
| 3 | R01-3 Tier B has no wrong-tree discriminator (`:191-202`) | routed-with-owner | integrator / next protocol revision | `R01-review.md:191-202`; Ca02's O2 contrast is the practice precedent |
| 4 | R01-4 C05 audit absent at review (`:147-152`) | fixed-with-evidence | C05 / integrator | `reports/round-39/cov/C05-audit.md` exists (28,221 B); `grep -c '4/4'` → 1 (`:46` "4/4 PASS") |
| 5 | R01-5 Tier A uses a shared clone (`:203-207`) | recorded | Ca01 | `reports/round-39/calib/Ca01-protocol.md:111-125,283` documents the shared-clone decision |
| 6 | R01-6 vacuous `or True` + off-by-one line cites (`:208-212`) | recorded | integrator | `R01-review.md:208-212`; filed protocol bytes immutable |
| 7 | R01-7 adopt D1+D2 at landing (`:262-270`) | fixed-with-evidence | r42 O | full policy 263 lines, sha `8c3d7c35…`, §1/§2 carry block extraction + disposition; `--selftest` 8/8 PASS; `--census` wrapped field 1 |
| 7b | R01-7 residual: phantom `../linguistics/phonology-sanity.md` has two hosts (`:271-277`) | routed-with-owner | integrator / r43 O census | second host `corpus/knowledge/synthesis/typed-label-routing-workflow.md:16` verified; the successor policy's Part 2 names only `label-channel-routing-verification.md:14` |
| 8 | R01-8 C02 provenance label (`:75-77`) | recorded | C02 / integrator | `R01-review.md:75-77`; filed fragment immutable |
| 9 | R01-9 C04 staged-size pin pre-reword (`:128-130`) | recorded | C04 / integrator | `R01-review.md:128-130`; filed fragment immutable |
| 10 | R01-10 fence-shape heterogeneity (`:140-146`) | recorded | r40+ extractors | `reports/round-40/cov/C05-audit.md:40` implements 4-backtick fence extraction (successor evidence) |
| 11 | R01-11 C01 counting-unit (occurrences vs distinct) (`:144-146`) | recorded | C01 / integrator | `R01-review.md:144-146` |
| 12 | R01-12 K01 taboo count 9 vs measured 10 (`:278-287`) | recorded | K01 | R01 itself re-measured `taboo = 10`; conclusion unchanged |
| 13 | R01-13 G2/G3/G4 unallocated (`:288-291`) | fixed-with-evidence | r40 C | r40 landed `taboo-strata-lifecycle.md`, `dialect-register-consistency.md`, `translation-protocol-fidelity.md`; README rev 2.3 |
| 14 | R01-14 unreproduced reviewer-side +2 anomaly (`:292-298`) | could-not-recover | R01 / integrator | no durable artifact; `R01-review.md:292-298` and `:335` say so |
| 15 | O02 D-1 "O02 says 44 controls" (`O03-verify.md:259-261`) | could-not-recover (claimed defect not reproducible) | Ca01 / integrator | `O02-isolated.md:20,:62,:203` all read **45 controls**, byte-identical at `dfb0719`; the 44 quote is O03's, not O02's |
| 15b | **new:** O03 D-1 quotation error | recorded | O03 / integrator | correction note cites `O03-verify.md:259-260` vs `O02-isolated.md:62`; no filed-byte edit |
| 16 | O02 D-2 "m15b says names nothing" (`O03-verify.md:262-276`) | could-not-recover (claimed text not found) | Ca01 / integrator | `O02-isolated.md:63` reads "OK manifest-roster: … carried by the live read set"; "names nothing" at `:99` describes a **different, rejected** rendered-text control |
| 16b | **new:** O03 D-2 quotation error | recorded | O03 / integrator | correction note; O02's §1 `:19` and §2 `:63` agree with O01's landed assertion |
| 17 | O02 D-3 tamper leg mis-attribution (`O03-verify.md:277-306`) | recorded | O02 / integrator | `O02-isolated.md:160-165` says the tampered component "surfaces through the assembled-vs-frozen packet compare (`:3951-3957`)"; O03 measured the per-component leg `:2208-2222` firing |
| 18 | O08 D-4 digest provenance (`O03-verify.md:308-341`) | recorded | O08 / integrator | O01 `e5812751…` (`O01-guard-design.md:144,:309`) ≠ O08 `ae22013b…` (`O08-regression.md:18,:80,:83`); O08's readings stand, provenance claim false |
| 19 | O07 0-byte fragment (`LOG.md:3741`) | recorded | integrator | `wc -c` → **0** at HEAD |
| 19b | **new:** O07 prevention (min-bytes check) | routed-with-owner | integrator / future runner | spec exists at `reports/round-40/scribe/S01-integration-draft.md` CO4; no durable checker at HEAD (`grep` finds only the queue's next_touch) |

No filed byte is proposed for edit anywhere in the table. Every "fixed" row carries a command
above; every "could-not-recover" names the owner and the reason.

### 4.3 The notable calibration corrections

- **D-1 is a misquotation.** The queue row quotes O02 as saying "plus 44 controls". The filed O02
  says **45** in all three occurrences, and that is correct arithmetic (43-control suite + two new
  controls = 45). O03 §4.1's quote is the source of the error. The successor record should correct
  the *row's* description, not O02.
- **D-2 is a category error.** O02's "names nothing" (`:99`) describes the **rejected rendered-text
  guard** (a vacuous 12-row read), not the in-sync `m15b` control. The in-sync row at `:63`
  explicitly names the carried manifest and the 59-member read set. The queue row conflates them.
- **D-3 stands.** O02's last §7 bullet attributes the tamper surface to the assembled-vs-frozen
  compare; O03's measurement (per-component digest leg) is the correct mechanism. This is a real
  filed-fragment defect and must stay `recorded`, not be dropped with D-1/D-2.
- **D-4 stands.** The two digests are both in filed bytes; the identity assertion is false. No
  re-run can reconstruct O08's scratch tree (gone), so the *cause* is could-not-recover, but the
  *finding* is recorded — do not inflate it to "fixed".
- **R01-14 is the only true could-not-recover** in the R01 family; do not let it launder the
  other rows into "unknown".

### 4.4 Successor queue shape (draft, Ca03 owns the file)

New file under `reports/round-43/calib/` (e.g. `defect-queue-successor-r43.json`), **not** an edit
to `reports/round-40/op/defect-queue-v2.json` (sha `dfc9265d…` must stay). Minimum shape:

```json
{
  "schema": "kotodama-defect-queue-successor-v1",
  "round": 43, "parent": "reports/round-40/op/defect-queue-v2.json",
  "parent_sha256": "dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907",
  "rows": [
    {"id": "r39-review-findings-disposition", "successor": "per-finding disposition list",
     "dispositions": [{"finding": "R01-2", "class": "routed-with-owner", "owner": "...",
                        "evidence": "..."}]},
    {"id": "r38-O02-fragment-defects",
     "dispositions": [{"finding": "D-1", "class": "could-not-recover",
                        "reason": "filed O02 reads 45 controls; the 44 quote is O03 §4.1"},
                       {"finding": "D-3", "class": "recorded", "evidence": "O03 §4.3"}]},
    {"id": "r38-O08-fragment-defect", "dispositions": [{"finding": "D-4", "class": "recorded"}]},
    {"id": "r38-O07-empty-fragment", "dispositions": [{"finding": "fragment", "class": "recorded"},
                                                       {"finding": "prevention", "class": "routed-with-owner"}]}
  ],
  "untouched": ["reports/round-40/op/defect-queue-v2.json"]
}
```

### 4.5 Verdict candidate

Calibration **improved** if the disposition artifact and successor queue land with the rows above
(every one of the four named rows reaches a class + owner + citation; zero dropped). If the
successor merely copies the queue rows forward, calibration is **unchanged** — the point of the
claim is per-finding resolution, and D-1/D-2 prove copying is not enough.

---

## §5 — Per-axis verdict candidates

| axis | candidate | before → after | evidence |
|---|---|---|---|
| operability | **improved** only if the resolver + disposition leg + census land and verify; else unchanged | "durable policy implementation exists but census drops mappings" → "four-class census with every fallback mapping + ambiguous control + blank-line fix" | §2; O04 oracle; O02 controls; O07 path; O12 conditional gate |
| coverage | **unchanged** (claim failed/blocked) | 26/223 → 26/223; no corpus delta | §3; C01/C02/C06/C07/K02 |
| calibration | **improved** only if the per-finding disposition artifact lands | 4 carried rows with no per-finding pass → 20 classed rows + successor queue | §4 |
| depth | unchanged | not claimed | — |
| adjacency | unchanged | no packet/canon/lore surface touched | A01 pending |
| freshness | unchanged (paused) | not claimed | `claims.json:13` |

**Admission candidate: NOT ADMITTED on C** (regimen rule; r42 precedent), with O and Ca
admissible on their own evidence. If the operator re-scopes C, that is a new claim and must be
declared, not silently substituted. No axis is *harmed* by the round as it stands; the failure is
a failed claim, not a regression.

---

## §6 — Landing checklist and runner leg spec

### 6.1 Files the integrator may commit (only if their claims verify)

| path | source | condition |
|---|---|---|
| `tools/harness/basename-couples-resolver.py` | O01/O02/O07 drafts | selftest + census pass; no `.scratch`, stdlib only; does not edit r42/r19 |
| `reports/round-43/calib/census-basename-couples.json` | O06/O10 | four-class totals close; 166 mappings listed |
| `reports/round-43/calib/dispositions-r38-r39.json` | Ca01 | every named finding classed with owner + evidence |
| `reports/round-43/calib/defect-queue-successor-r43.json` | Ca03 | parent sha pinned; r40 file untouched |
| `reports/round-43/run-validation.py` | integrator | §6.2 legs; never executed in-tree by seats |
| `reports/round-43/validation.json` | runner (isolated copy at close) | receipt, `acceptance_checks_passed` honest |
| `reports/round-43/telemetry/observed-dispatch.json` | S02/integrator | observed launches/completions/routes |
| `reports/round-43/telemetry/availability-close-43.json` | integrator | closes the declared snapshot; digest-pinned |

**Do not commit:** any `corpus/**` change (C blocked), any README rev 2.5 (there is no 224),
any edit to `reports/round-1..42/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**` or `.ufo/**`
(the fleet report is the orchestrator's external path), or `declared-in-r7` re-freeze.

### 6.2 Runner legs (spec — do not copy r42's digest leg blindly)

- **CO (identity):** `round == 43`, `baseline_commit == "7ceff59"`, `seat_count == 32 == len(seats)`,
  `dispatch.model == "deepseek-v4.1-flash"`, `batched_calls == 1`; record the named provider
  deviation (operator redirect) with both declared and observed route.
- **O1 (durability):** the resolver exists, has a shebang, imports stdlib only, has no `.scratch`
  path, and does **not** import/patch `reports/round-19/audit/entry-audit.py` or
  `tools/harness/couples-reference-extractor.py`.
- **O2 (selftest):** exit 0; output contains the wrapped positive **by identity**
  (`tone-prosody.md` present, `prosody.md` absent), phantom→`unresolved`, synthetic
  two-hit→`ambiguous` (both candidates listed), direct positive, blank-line boundary negative.
- **O3 (census):** parse the artifact, not stdout prose. Assert
  `direct+fallback+ambiguous+unresolved == refs == 2730`, `entries == 223`,
  `direct == 2556`, `fallback == 166`, `ambiguous == 0`, `unresolved == 8` with sub-reasons
  `2/5/1`, `wrapped_fields == 1`, and `len(fallback_mappings) == 50` distinct tokens covering
  `166` occurrences. Fail if any mapping is missing.
- **O4 (filed-byte guard):** r19 sha `e7992c32…`, r27 `fb589b28…`, r28 `9b2ccac0…`, r42 extractor
  `d8d23a26…`, policy full doc `8c3d7c35…`; any drift fails.
- **C1 (honest coverage):** if C stays blocked, assert **223/26** and require the collision record
  (`cov/C06-collision.md`, `scout/K02-landing-scout.md`) in `named_findings`; the leg must **not**
  pass a 224 claim and must **not** be a no-op. If C is re-scoped, assert the new target and
  224/27, and assert the spare bytes were not applied.
- **Ca1 (dispositions):** parse the disposition artifact; every finding id in
  `{R01-2..R01-14, O02-D1..D3, O08-D4, O07}` present exactly once with a class in
  `{fixed-with-evidence, routed-with-owner, recorded, could-not-recover}`, a non-empty owner, and
  a citation; every `fixed-with-evidence` row carries a command; the r40 queue sha is unchanged.
- **P1 (filed bytes):** compare `corpus/knowledge/**` and `reports/round-1..42/**` to baseline;
  any change fails. This is the leg that would have caught r42's overwrite incident earlier.
- **X1–X4 (governance):** L1 bleed scan as in r42 (negation/quote allowlist); no seat out is
  0 bytes (min-bytes, the O07 lesson); telemetry digests read `declared_artifacts` (r43 shape) and
  record the `claims.json` amendment (declared `beda7644…` vs live `9662e2bd…`) as a named
  finding, not a silent pass; receipt idempotence (two builds equal).

### 6.3 One-command re-checks the integrator can paste

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git rev-parse HEAD; git status --porcelain
ls corpus/knowledge/myth-symbol/*.md | wc -l          # 26
find corpus/knowledge -name '*.md' | wc -l            # 223
python3 -B reports/round-28/readme/sweep.py           # 223==223, exit 0
python3 -B tools/harness/couples-reference-extractor.py --selftest
python3 -B tools/harness/couples-reference-extractor.py --census
python3 -B reports/round-19/audit/entry-audit.py corpus/knowledge/linguistics/phonetics-phonology.md
wc -c reports/round-38/op/O07-scribe.md               # 0
```

---

## §7 — SHONEN section (draft for the fleet report)

**What this round actually taught.**

1. **A claim's `before` is a measurement, not a memory.** Both C ("lithic slot unbuilt") and O
   ("no durable instrument") were false at the declared baseline. The wave caught both because
   seats re-measured instead of copying the premise. The contract should make a premise-check
   (one command per `before` clause at dispatch time) a required seat artifact.
2. **Extend the durable predecessor; do not re-mint it.** The r42 extractor already read the
   wrapped field 4/4. The r43 value is the disposition leg, the ambiguous control and the
   blank-line boundary — a delta that a second resolver would have hidden. Naming a new tool is
   not itself an improvement.
3. **A filename check is not a topic check.** The partition was "free" only if one looked at the
   path; the register was already owned. Collision detection needs a topic-ownership probe
   (the gap line's claim vs the partition's topic lines), not just `test -e`.
4. **Disposition is a measurement, not a filing exercise.** Two of the three O02 sub-findings
   dissolved when re-read against the filed bytes; D-3 and D-4 survived. A pass that copies queue
   text forward would have preserved two errors and missed the chance to correct the record.
5. **Four classes need a fold rule.** Six buckets and four classes are both true only when the
   sub-reasons are printed; an arithmetic-only assertion is a false green (space-join and
   hyphen-delete both yield four wrong tokens).
6. **Byte-range evidence makes a 55 KB spare auditable.** C01's `[328, 55429)` / `6999a912…` pin
   let four seats confirm the collision without re-reading the entry. Keep that convention.

**Honest stop:** the round cannot be admitted on C as declared. O and Ca are admissible on their
own evidence; the collision is reported, not routed around.

---

## §8 — Owed / to-verify

- **O01 tool draft** absent at this cut; O03/O05/O06/O08/O09/O10 absent. O02/O04/O07/O12 are
  conditional and must be re-run against O01 once it lands.
- **Ca01/Ca02/Ca03** absent; §4 is an integration-side candidate, not the filed disposition
  artifact. Ca02 must independently re-measure D-1/D-2 (this seat predicts disagreement with the
  queue row) and D-3/D-4 (agreement).
- **R01/R02/X01/X02/A01** absent; no non-author review or trades/honesty critique at this cut.
- **`reports/round-43/run-validation.py`** absent; §6.2 is a spec. Absolute rule stands: never
  execute a round runner in-tree; the close-time run happens in an isolated copy.
- **Telemetry:** `claims.json` digest mismatch must be refiled or recorded as an amendment
  (declared `beda7644…` / 6,353 B vs live `9662e2bd…` / 6,546 B); `observed-dispatch.json` and
  `availability-close-43.json` are owed at close.
- **Filed r39 policy** is truncated at 107 lines; the r42 successor corrects it but the filed byte
  must not be edited. Cite the successor, note the truncation.
- **r42 extractor blank-line over-capture** (K01 F5; reproduced here) must be fixed in the r43
  tool, not in the r42 file.
- **C spare** remains routed; retirement/re-scope is an operator/integrator decision. Do not
  stage under `corpus/`.
- **`MANIFEST.json rounds[]`** and the fleet `.ufo/reports/round-43/kotodama.md` are external to
  this repo tree; the integrator/orchestrator files them.

---

## §9 — Citations

- `reports/round-43/claims.json` (claims O/C/Ca; `:24-42`, `:50-56`); `reports/round-43/targets.json:9`
  (shared rule), `:1-33` (seat contract); `reports/round-43/telemetry/dispatch-declared.json`.
- Policy: `reports/round-42/calib/basename-couples-policy-full.md` (263 lines); filed r39 original
  `reports/round-39/calib/basename-couples-policy.md` (107 lines, truncated).
- Instruments: `reports/round-19/audit/entry-audit.py:75,87-95`;
  `tools/harness/couples-reference-extractor.py` (sha `d8d23a26…`, `:64-65`, `:134`);
  `reports/round-28/readme/sweep.py` (sha `9b2ccac0…`).
- Wrapped field: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77` (sha `b4f9b003…`).
- Census: `reports/round-42/op/couples-census-corrected.json` (220-era `2611 = 2437+166+0+8`);
  live `--census` 223/2730; O04 oracle `reports/round-43/op/O04-verify.md:121-156`.
- Collision: `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` (sha `c99f44ca…`);
  `reports/round-42/cov/C01-mineral-spare.md` (sha `2b9326e3…`, body `6999a912…`);
  `reports/round-42/cov/C01-entry-1.md:3,28`; `reports/round-42/validation.json` claim-C ruling;
  `corpus/README.md:5-12,205,219,544,548`; peers `cov/C01-prepare.md`, `cov/C02-readme-draft.md`,
  `cov/C06-collision.md`, `cov/C07-scribe.md`, `scout/K02-landing-scout.md`.
- Dispositions: `reports/round-40/op/defect-queue-v2.json` (sha `dfc9265d…`); queue rows at ids
  `r39-review-findings-disposition`, `r38-O02-fragment-defects`, `r38-O08-fragment-defect`,
  `r38-O07-empty-fragment`; `reports/round-39/review/R01-review.md:25-34,75,93,128,140-147,182-212,226-298,321-335`;
  `reports/round-38/op/O02-isolated.md:19-20,60-63,99,152-170,203`;
  `reports/round-38/op/O03-verify.md:255-341`; `reports/round-38/op/O01-guard-design.md:144,309`;
  `reports/round-38/op/O08-regression.md:18,80,83`; `reports/round-39/calib/recount-ledger-successor.json:4`;
  `reports/round-39/cov/C05-audit.md:46`; `LOG.md:3741,3745-3761`.
- Peers folded: `reports/round-43/scout/K01-resolver-scout.md` (four classes, F5 over-capture,
  conformant output); `op/O02-controls.md` (selftest battery); `op/O04-verify.md` (oracle,
  conditional); `op/O07-durability.md` (canonical path, in-memory fixtures); `op/O12-negative-proof.md`
  (live-tree PASS, draft could-not-evaluate).

---

## Appendix A — Distinct fallback mappings at HEAD (50 tokens / 166 occurrences)

Every row is a `token -> corpus-relative path` mapping; `n` is the occurrence count. This is the
list the O census artifact must carry (policy §3.3).

| token | n | mapping |
|---|---:|---|
| naming-systems.md | 14 | corpus/knowledge/linguistics/naming-systems.md |
| writing-systems.md | 13 | corpus/knowledge/linguistics/writing-systems.md |
| language-contact.md | 10 | corpus/knowledge/linguistics/language-contact.md |
| material-culture-inference-method.md | 10 | corpus/knowledge/culture-material/material-culture-inference-method.md |
| symbolism-synthesis-method.md | 10 | corpus/knowledge/myth-symbol/symbolism-synthesis-method.md |
| historical-linguistics.md | 9 | corpus/knowledge/linguistics/historical-linguistics.md |
| costume-semiotics.md | 8 | corpus/knowledge/culture-material/costume-semiotics.md |
| sociolinguistics-registers.md | 7 | corpus/knowledge/linguistics/sociolinguistics-registers.md |
| ritual-garments.md | 6 | corpus/knowledge/culture-material/ritual-garments.md |
| dress-through-eras.md | 5 | corpus/knowledge/culture-material/dress-through-eras.md |
| pantheon-archetypes.md | 5 | corpus/knowledge/myth-symbol/pantheon-archetypes.md |
| architecture-settlement-lexicon.md | 4 | corpus/knowledge/culture-material/architecture-settlement-lexicon.md |
| comparative-frameworks.md | 4 | corpus/knowledge/myth-symbol/comparative-frameworks.md |
| orality-formulaic-language.md | 4 | corpus/knowledge/linguistics/orality-formulaic-language.md |
| textile-technology.md | 4 | corpus/knowledge/culture-material/textile-technology.md |
| color-symbolism.md | 3 | corpus/knowledge/myth-symbol/color-symbolism.md |
| garment-lexicon-crosslinguistic.md | 3 | corpus/knowledge/culture-material/garment-lexicon-crosslinguistic.md |
| semantics-pragmatics.md | 3 | corpus/knowledge/linguistics/semantics-pragmatics.md |
| sumptuary-law-rank-display.md | 3 | corpus/knowledge/culture-material/sumptuary-law-rank-display.md |
| trade-economy-lexicon.md | 3 | corpus/knowledge/culture-material/trade-economy-lexicon.md |
| adornment-body-codes.md | 2 | corpus/knowledge/culture-material/adornment-body-codes.md |
| calendar-festival-systems.md | 2 | corpus/knowledge/culture-material/calendar-festival-systems.md |
| calibration-registry.md | 2 | corpus/knowledge/verification/calibration-registry.md |
| cosmology-cosmography.md | 2 | corpus/knowledge/myth-symbol/cosmology-cosmography.md |
| morphological-typology.md | 2 | corpus/knowledge/linguistics/morphological-typology.md |
| politeness-taboo-euphemism.md | 2 | corpus/knowledge/linguistics/politeness-taboo-euphemism.md |
| real-world-inspiration-boundaries.md | 2 | corpus/knowledge/verification/real-world-inspiration-boundaries.md |
| ritual-liminality.md | 2 | corpus/knowledge/myth-symbol/ritual-liminality.md |
| animal-symbolism.md | 1 | corpus/knowledge/myth-symbol/animal-symbolism.md |
| consistency-verification-checklist.md | 1 | corpus/knowledge/synthesis/consistency-verification-checklist.md |
| coupling-model.md | 1 | corpus/knowledge/synthesis/coupling-model.md |
| creation-myths-taxonomy.md | 1 | corpus/knowledge/myth-symbol/creation-myths-taxonomy.md |
| era-language-staging.md | 1 | corpus/knowledge/synthesis/era-language-staging.md |
| era-periodization-models.md | 1 | corpus/knowledge/culture-material/era-periodization-models.md |
| inca.md | 1 | corpus/knowledge/civilizations/inca.md |
| kinship-terminology.md | 1 | corpus/knowledge/linguistics/kinship-terminology.md |
| lexicon-coverage-audit.md | 1 | corpus/knowledge/verification/lexicon-coverage-audit.md |
| loanword-material-dating.md | 1 | corpus/knowledge/synthesis/loanword-material-dating.md |
| maya-classic.md | 1 | corpus/knowledge/civilizations/maya-classic.md |
| mesopotamia-sumer-akkad.md | 1 | corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md |
| music-instrument-lexicon.md | 1 | corpus/knowledge/culture-material/music-instrument-lexicon.md |
| myth-ritual-theories.md | 1 | corpus/knowledge/myth-symbol/myth-ritual-theories.md |
| myth-to-language-derivation.md | 1 | corpus/knowledge/synthesis/myth-to-language-derivation.md |
| number-symbolism.md | 1 | corpus/knowledge/myth-symbol/number-symbolism.md |
| phonetics-phonology.md | 1 | corpus/knowledge/linguistics/phonetics-phonology.md |
| register-strata-attestation.md | 1 | corpus/knowledge/linguistics/register-strata-attestation.md |
| religion-language-co-evolution.md | 1 | corpus/knowledge/synthesis/religion-language-co-evolution.md |
| source-discipline-calibration.md | 1 | corpus/knowledge/synthesis/source-discipline-calibration.md |
| taboo-euphemism-lifecycle.md | 1 | corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md |
| warrior-material-culture.md | 1 | corpus/knowledge/culture-material/warrior-material-culture.md |

**Totals: 50 distinct tokens, 166 occurrences, 21 carrier entries, 0 misaligned.**
