# ExecSeparability — wave 3 attack: causal separability (QUALITY 7)

**Verdict: PARTIAL.** Both counters are discriminating and **claim C's verdict is causally
separable** (accept-c.py = 13/13 at freeze+C alone, and still 13/13 after Ca's own bytes are deleted
from the one shared file). What is **not** separable is (a) the *landing* of C's patch — it does not
apply to the freeze at all, it needs the file Ca's commit creates — and (b) **claim Ca's declared
after-state command does not reproduce its declared verdict** (11/12, exit 1 without `--combined`,
and 11/12 even *with* `--combined` if Ca lands second). Exhaustive defects at the end.

## Environment and method

- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (read-only). Scratch:
  `/fast/scratch/hyaku/kotodama-r75/ExecSeparability/` (two shared clones + per-run
  `HYAKU_SCRATCH`), deleted at the end of this wave; every `git` call names `-C`, every clone asserted
  `rev-parse --show-toplevel` == its own dir before any mutation.
- Counter runs use `HYAKU_SCRATCH` inside my seat dir (never `/tmp`), `python3 -B`, and the frozen
  counter blobs at the revision under test.
- Fixture commits (cherry-picks, one dependency-probe mutation) use
  `-c user.name=fixture -c user.email=f@f.invalid`, inside the scratch clones only.

Revisions measured (all scratch; the landed ones also named for identity):

| id | composition | commit | tree |
|---|---|---|---|
| freeze | — | `5d0167464309d8133991b30f7d7a7011a6a0fd14` | (constant source) |
| **A** | freeze + cherry-pick Ca `012e8d3` (**clean**) | `e21bee46cd08…` / `3ffa5264015f…` | `c943f86b4cb24668682c3e46b40629104c5816dd` |
| **B** | freeze + cherry-pick C `4f5e3b2` (**conflict**, see P1) | `95f6e100d04cdb7b88ee16a829fff4d0453beaa7` | `76dfe8f53e5e65e96df11efe4d05401693d9861d` |
| **comb1** | A + cherry-pick C (**clean**) = Ca→C | `d3287389b3939d6afcd1be5612066fb2a29a8b25` | `43a96e737f250fb8e5bed93abc13c6b9ba608bdb` |
| **comb2** | B + cherry-pick Ca (**conflict**, see P1) = C→Ca | `c52ccf33dd3c7b6468c86361c6748140aa954238` | `43a96e737f250fb8e5bed93abc13c6b9ba608bdb` |
| B2 (probe) | B with `corpus/lessons/round-75.md` reduced to C's own 363 lines (all 40 of Ca's lines in that file dropped) | `cfbb11abdcafc15e1a38ab1908a0e8c1de7a20d2` | `9c1599e307d878299900a5800bb46b004af98eb4` |
| landed Ca `012e8d3` | real | tree `c943f86b4cb2…` (**== A**) | |
| landed C `4f5e3b2` | real | tree `43a96e737f25…` (**== comb1 == comb2**) | |

**Convergence:** both landing orders produce the *identical* tree `43a96e737f25…`, which is also the
real landed tree at `4f5e3b2`. There is no content divergence between orders — only patch-application
and grading-order divergence.

## The matrix

`accept-c.py` legs = 13 (ENTRIES…INDEX); `accept-ca.py` legs = 12 (LEDGER…STAMP).

| tree | accept-c.py | accept-ca.py |
|---|---|---|
| freeze alone | not run (outside this ticket's matrix) | not run |
| **B** (C only) | **PASS 13/13** (exit 0) | **FAIL 6/12** (`REPAIR ANNOTATE NOSTUB APPENDONLY RECEIPTS COMBINED`) |
| **A** (Ca only) | **FAIL 4/13** (`ENTRIES ROWS REPOINTED GATE EVIDENCE REJECTS CITEDLINES SCRATCHMIRROR INDEX`; only `GROUND CENSUS COLLCHECK FROZENCFG` green) | **FAIL 11/12 without `--combined`** (only `COMBINED`: *"the explicit --combined revision is required"*); **PASS 12/12 with `--combined`** |
| **comb1** (Ca→C) | **PASS 13/13** | **PASS 12/12** (`--combined comb1`; detail `ca-lands=3ffa5264015f combined=d3287389b393 tree=43a96e737f25 problems=[]`) |
| **comb2** (C→Ca) | **PASS 13/13** | **PASS 12/12** at lands=A + `--combined comb2` (`ca-lands=e21bee46cd08 combined=c52ccf33dd3c tree=43a96e737f25 problems=[]`) |
| **comb2 as `<lands>`** (Ca landing *is* the second commit) | (13/13, same tree) | **FAIL 10/12** without `--combined`; **FAIL 11/12 with `--combined c52ccf3`** — `APPENDONLY` red: `corpus/README.md: changed lines outside REPAIR stated_at lines [376]` |
| **B2** (probe) | **PASS 13/13** | not run |

Answers to the ticket's questions:

1. **Does accept-c.py PASS 13/13 on (B)?** Yes — exit 0, `ACCEPT-C-75: PASS legs=13/13`, all 13 legs
   green, `tree=76dfe8f53e5e…`, `lands==freeze=no first-parent-chain=yes claims@lands=frozen-bytes
   map=…(sha256-match)`. The claim's sentence "Claim C is checked at `<lands>` without claim Ca landed"
   is **true for the verdict**. It is not constructible as a pure patch application (P1).
2. **Does accept-ca.py PASS on (A) without C?** Only with an extra flag that the claim's own
   `counter`/`after` command line does not show. Without `--combined`: `ACCEPT-CA-75: FAIL legs=11/12`,
   exit 1, `LEG FAIL COMBINED — the explicit --combined revision is required`. With
   `--combined <rev>`: `ACCEPT-CA-75: PASS legs=12/12`, exit 0. The committed receipt
   `reports/round-75/telemetry/measures-ca.txt` does carry the `--combined 4f5e3b2…` form, so the
   landing evidence is honest; the claim text's command line is what is incomplete (D1).
3. **Order sensitivity of the counters.** `accept-c.py` is order-free: 13/13 at B (C alone), B2, comb1
   and comb2. `accept-ca.py` is **not**: 12/12 only when Ca's landing revision is the Ca-first tree
   (`c943f86b`); if Ca lands second its landing revision already carries C's bytes and the main
   `APPENDONLY` leg goes red on the C-owned README heading, `--combined` notwithstanding (D2).

## Shared paths that create an order dependence

`git diff 5d01674..012e8d3` ∩ `git diff 012e8d3..4f5e3b2` = exactly two paths.

### P1 `corpus/lessons/round-75.md` — hard, both directions

- **absent at the freeze**; **created by Ca** (`012e8d3`, 40 lines, blob `ac41f8be1bd846c3…`);
  **modified by C** (`+363 lines`, blob `9903ee1f4e06b310…`, hunk `@@ -14,6 +14,369 @@`).
- C onto the freeze → `CONFLICT (modify/delete): corpus/lessons/round-75.md deleted in HEAD and
  modified in 4f5e3b2 … Version 4f5e3b2 … left in tree.` Only resolution available: `git add` the
  left-in-tree C blob (no hand edit; nothing comes from Ca's blob that C's blob does not itself carry —
  but C's blob *does* carry **all 40** of Ca's lines: `git show --stat 4f5e3b2` on that path is
  `363 insertions(+)`, zero deletions, so B's 403-line file = Ca 1–16, C's inserted block 17–379,
  Ca 17–40 at 380–403).
- Ca onto freeze+C → `CONFLICT (add/add): Merge conflict in corpus/lessons/round-75.md`. I resolved it
  with the canonical landed blob (`git checkout 4f5e3b2 -- corpus/lessons/round-75.md`), i.e. exactly
  the file both orders must converge on; `git add` + `cherry-pick --continue`.
- **Revert asymmetry** on comb1: reverting C alone is clean and yields A's tree byte-for-byte
  (`c943f86b4cb2…`); reverting Ca alone → `CONFLICT (modify/delete): corpus/lessons/round-75.md
  deleted in parent of 3ffa526 … and modified in HEAD. Version HEAD … left in tree.`
- **The dependency is only on the file's existence, not on Ca's bytes** (measured): B2 deletes Ca's
  40 lines that live in that file, leaving only C's own 363-line block, and accept-c.py still prints
  `ACCEPT-C-75: PASS legs=13/13` (exit 0). So no C leg reads a Ca-authored byte; the coupling is
  patch-application/commit-history, not graded content. `ENTRIES/ROWS/GATE/EVIDENCE/INDEX` all still
  green with Ca's `## Corrections` section physically gone.

### P2 `corpus/README.md` — soft (auto-merges), but grading-order dependent

- Ca hunks `@@ -341,7 @@`, `@@ -404,7 @@`, `@@ -426,6 @@` (`## linguistics/ (30)→(32)`,
  `## culture-material/ (36)→(40)`, two heritage index rows).
- C hunks `@@ -373,7 @@`, `@@ -403,6 @@`, `@@ -822,3 @@` (`## myth-symbol/ (29)→(32)`, three index
  rows, appended `Total knowledge entries: 252.` + `Counts checked … 32/32/40/29/24/95` block).
- Hunk ranges do not overlap: Ca→C applies clean (**comb1**), C→Ca auto-merges (`M corpus/README.md`,
  zero conflict markers, **comb2**). Content is order-free.
- **Grading is not**: with Ca landing second, its lands tree contains C's `## myth-symbol/ (32)` at
  line 376, which is outside Ca's REPAIR `stated_at` set (`{SHONEN.md:6, corpus/README.md:344, :407,
  SKILL.md:701}`) → `APPENDONLY` red, 11/12 even with `--combined` (D2). Ca's 12/12 requires "Ca
  lands before C", which W2-F2 already declares, but the counter's own leg text does not say it.
- C's counter tolerates the other direction on the same file: `INDEX` green at B (*"6 section(s),
  myth-symbol=32, last footer total=252 vector=32/32/40/29/24/95, 3 adopted row(s), 822 base / 829
  lands line(s), 8 exempt line(s)"*) and at comb1/comb2 (*"… 831 lands line(s), 12 exempt line(s)"*).
  At B the other two partition headings are still the base's stale `(30)`/`(36)` and INDEX does not
  care — consistent with the frozen leg text (it pins only the myth-symbol heading) and with
  "the linguistics/culture-material README headings are Ca-owned and not graded by C".

No other path is shared: knowledge files, `corpus/SOURCES.md`, `reports/round-75/evidence/**`,
`reports/round-75/telemetry/census-end.txt` are C-only; `SHONEN.md`, `SKILL.md`, `SCORECARD.md`,
`corpus/QUALITY.md`, `reports/round-28/readme/sweep.py`, `reports/round-75/telemetry/{controls-*,
sweep-*,selftest-*,accept-ca-74-at-lands}.txt` are Ca-only.

## Exact defect list

**D1 — claim Ca's declared command does not produce its declared verdict (BLOCKING for the
claim text, not for the landing).** `claims.json` `claims[Ca].counter` and `claims[Ca].after` both
give `python3 -B reports/round-75/accept-ca.py --root . --lands <Ca-lands> --freeze <freeze>
--fleet-root …` with no `--combined`, and `after` asserts it "prints ACCEPT-CA-75: PASS legs=12/12
(exit 0)". Measured at the Ca landing A (`3ffa526…`, `012e8d3…`'s twin): `ACCEPT-CA-75: FAIL
legs=11/12`, exit 1, only `COMBINED` red with *"the explicit --combined revision is required"*.
The `COMBINED` leg text does name `--combined <combined-revision>`; the `after`/`counter` strings do
not. `reports/round-75/telemetry/measures-ca.txt` records the correct `--combined 4f5e3b2…` form, so
this is a claim-text/verifiability defect, not a fabricated receipt.

**D2 — claim Ca's verdict is landing-order dependent.** At a Ca lands that already carries C
(comb2 as `<lands>`, `c52ccf3…`, tree `43a96e73…`): 10/12 without `--combined` and **11/12 with
`--combined`** — `APPENDONLY` red: `corpus/README.md: changed lines outside REPAIR stated_at lines
[376]`. Same tree, same counters, different commit order → different verdict. Declared only indirectly
(W2-F2: "Ca lands before C"); the frozen `APPENDONLY` leg text does not state the order premise.

**D3 — claim C's landing is not applicable to the freeze (QUALITY 7's "base commit plus only the
paths it lands itself").** `git cherry-pick 4f5e3b2` on `5d01674` → `CONFLICT (modify/delete)` on
`corpus/lessons/round-75.md`; the reverse order → `CONFLICT (add/add)` on the same path; reverting Ca
alone from the combined tree → `CONFLICT (modify/delete)` (C's 403-line version left in tree, Ca's
40 authored lines cannot be removed without a manual decision). The file is created by the *other*
claim's commit, and the axes_note's "claim C owns … `corpus/lessons/round-75.md` Gate admits" /
"claim Ca owns … correction rows" splits ownership by *section*, which git cannot land
independently. Mitigation measured (B2): deleting Ca's bytes from that file leaves C at 13/13, so the
coupling is inert — the defect is in the landing mechanics and the ownership declaration, not in C's
verdict.

**O1 (minor, secondary) — false assertion in the landed lesson.** `corpus/lessons/round-75.md:3-4`
(at both `012e8d3` and `4f5e3b2`, authored in the Ca commit) states "base … (also HEAD; no freeze
commit exists — `git cat-file -e HEAD:reports/round-75/claims.json` → absent …)". Re-run at its own
landing: the blob is **PRESENT** (`git -C … cat-file -e 012e8d3:reports/round-75/claims.json` →
exists; same at `4f5e3b2`). True of the base `f556d10` only. Neither counter reads the line.

## What survives the attack (measured, not asserted)

- `accept-c.py` is order-free and content-separable: 13/13 at B (C alone), B2 (Ca's bytes in the shared
  file gone), comb1 and comb2; 4/13 at A (Ca alone) proves it is not vacuously green.
- `accept-ca.py` is order-free in the *content* sense: 12/12 at A with either order's combined
  revision (`comb1` and `comb2`), and 6/12 at B proves it is not vacuously green.
- Both orders converge to the real landed tree `43a96e737f25…`; `A`'s tree equals the real Ca tree
  `c943f86b4cb2…`.
- No byte of Ca's ledger, SCORECARD corrections, telemetry receipts or `stated_at` lines cites a
  C-only id or the `narrative-structure-frameworks*` family (`SEPARABLE` green in every Ca run,
  including at B where C's artifacts are present in the tree).

## Reproduce (all inside my scratch clone, `git -C` on every call)

```
D=$(mktemp -d -p /fast/scratch/hyaku/kotodama-r75/ExecSeparability lane.XXXX)
git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane"
git -C "$D/lane" rev-parse --show-toplevel            # must print "$D/lane"
git -C "$D/lane" -c user.name=fixture -c user.email=f@f.invalid checkout -q -B A 5d01674643…
git -C "$D/lane" -c user.name=fixture -c user.email=f@f.invalid cherry-pick 012e8d3c8b…   # clean
git -C "$D/lane" -c user.name=fixture -c user.email=f@f.invalid checkout -q -B B 5d01674643…
git -C "$D/lane" -c user.name=fixture -c user.email=f@f.invalid cherry-pick 4f5e3b2535…   # modify/delete conflict
git -C "$D/lane" add corpus/lessons/round-75.md      # the left-in-tree C blob, unedited
git -C "$D/lane" -c user.name=fixture -c user.email=f@f.invalid -c core.editor=true cherry-pick --continue
HYAKU_SCRATCH=$D/cs python3 -B reports/round-75/accept-c.py --root . --lands <B> --freeze 5d01674643…
```

Every verdict above is the counter's own `LEG PASS/FAIL …` line plus its `ACCEPT-C-75:` /
`ACCEPT-CA-75:` summary; the run logs were kept only inside the (now deleted) seat scratch and their
load-bearing lines are quoted inline above. No tool installs were made in this seat; no file outside
this report, my scratch, and the two scratch clones was written.
