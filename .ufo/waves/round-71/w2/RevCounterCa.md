# RevCounterCa — falsify seat, round 71 wave 2 (claim Ca counter + landings)

Seat: `L1Kotodama71.RevCounterCa` (reviewer, leaf, read-only on the lane).
Revision of this report: re-measured at lane HEAD **`99e3d63a`**. An earlier pass at `14c88d9b` is summarised in the history section at the end.
Fresh clone: `git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/revca2.ai6V/k` (HEAD = 99e3d63).
Scratch: `/tmp/revca2.ai6V/` (clone and mutants) and `/tmp/revca.pKYQ/` (first pass). No lane bytes written except this file.
Tools: no installs or updates.
Cross-checked with RevReceipts (`.ufo/waves/round-71/w2/RevReceipts.md`). Every point it raised was re-derived here before adoption.

## Verdict summary at 99e3d63

| check | result |
|---|---|
| `python3 -B reports/round-71/accept-ca.py --root .` in fresh clone | **PASS** (exit 0, 6/6 legs; counter sha `1ce25fb9…`) |
| Six receipt restamps: 6 header lines, marker, original bytes below | **PASS**. Each header prefix appears once, the marker is at line 8, and the below-marker bytes are byte-identical to the pre-restamp blobs. Header values now verify (F1 is resolved), but `--topo` fails and line 1 no longer names its digest object (F1′). |
| S860 verify-at = acc2d614 | **PASS** |
| Round-70 quote words <= 25 | **PASS** (25) |
| Scorecard row | **PASS (weak)**: F6 |
| Lesson reject sweep | **PASS on literal predicate**; the "each carries reason + flip" statement is still false: F4 |
| 21-row quarantine id bijection | **PASS**: table ids equal the register slice; tally now PRESENT 10 · REFUSED 7 · UNVERIFIABLE 4 |
| Claim's declared `counting_command` | **FAIL on the quarantine leg**: prints 0, target 21 (F3, unchanged) |
| Counter falsifiability | **Improved, still weak**: 8 of 12 mutants pass (F2) |
| Round-71 Ca receipt (`reports/round-71/telemetry/measures-ca.txt`) | **New defect**: the top header pairs counter sha `1ce25fb9` with stamp `64da9e1`, where that counter did not exist (F7) |

## Findings by severity

### F7 — HIGH (new) — the round-71 Ca receipt's top header stamps a revision where its counter did not exist

Lines 1-6 of `reports/round-71/telemetry/measures-ca.txt` read:
- `# counter sha256 (self): 1ce25fb9…`
- `# stamped/evaluated/measured revision: 64da9e14…`
- `# tree: ff803f43…`

The counter's history does not support that pairing:

| revision | `sha256` of `accept-ca.py` | has `class_ok` |
|---|---|---|
| `75d1675` | `f706aacd…` | 0 |
| `64da9e1` | `f706aacd…` | 0 |
| `57e0a72` | `1ce25fb9…` | 3 |
| HEAD | `1ce25fb9…` | 3 |

`git merge-base --is-ancestor 64da9e1 57e0a72` succeeds, so the counter named in line 1 was first committed after the stamped revision.

The run that actually used `1ce25fb9` is the appended block at lines 24-37, headed only `# re-run at 27db4ce (class-ok leg, append-only)`. That block has no 17/19 header of its own. The top header therefore claims an evaluation at `64da9e1` that the counter it names could not have performed.

**The file contradicts itself.** Its own preserved previous header (lines 9-10) records counter `f706aacd…` at the same stamp `64da9e14`. The `57e0a72` append-only re-stamp updated the counter sha without moving the stamp. RevReceipts found this independently and records it as V9.

**The lane checker grades the wrong object.** `check_counter_sha` in `tools/check-receipt-seq.py` (lines 160-175) hashes `read_worktree(counter)`, falling back to `read_rev("main", counter)`. It never reads the counter at the stamped revision. The results:
- Default mode, paired: `SHA-… PASS recorded=1ce25fb9 actual=1ce25fb9`. Both sides are read from the current tree.
- `--lands 1d1b432`, paired: `SHA-… FAIL recorded=3f3f63fc actual=1ce25fb9`. It fails for the wrong reason: the receipt is read at lands, the counter from the worktree.

**A one-line fix, tested in scratch** (`/tmp/revca2.ai6V/fix.py`; no lane bytes changed). The change resolves the counter as `read_rev(root, h["stamped"], cpath)`:

| receipt | recorded | counter at stamp | result |
|---|---|---|---|
| `measures-ca.txt` | `1ce25fb9` | `f706aacd` | **FAIL** |
| `measures-c.txt` | `80b4ca09` | `80b4ca09` (`accept-c.py` at `64da9e14`) | PASS |
| `measures-d.txt` | `459cfa9d` | `459cfa9d` (`accept-d.py` at `1d1b4325`) | PASS |

`--selftest` stays `SELFTEST: 14/14` both before and after, so the selftest has no fixture for a counter sha taken from a later revision. A fixture for that case should be added alongside the fix. Lands mode would resolve the counter at `<lands>`. RevReceipts reproduced these three results independently (V9).

**The fix must not fall back to the worktree.** RevReceipts' scratch variant reads the stamp first, then falls back to the worktree, then `main`. That fallback reopens the hole whenever the counter is absent at the stamp. Scratch fixture `/tmp/revca2.ai6V/fx-receipt.txt` stamps `8c203bd`, where `accept-ca.py` does not exist, with a correct tree and today's counter sha `1ce25fb9`:

| checker | result on the fixture |
|---|---|
| current tool | `SHA … PASS recorded=1ce25fb9 actual=1ce25fb9` |
| fallback variant (`/tmp/revca2.ai6V/fix-fallback.py`) | `SHA … PASS recorded=1ce25fb9 actual=1ce25fb9` |
| strict stamp-only (`/tmp/revca2.ai6V/fix.py`) | `SHA … FAIL counter_absent:reports/round-71/accept-ca.py` |

The counter must resolve at the stamp (or at `<lands>` in lands mode). If it is absent there, the result must be FAIL, never a worktree or `main` read.

**Fixtures to route with the fix:**
- **(a) counter edited later.** Counter committed at L, receipt stamped at L, counter edited in a later commit. Default mode must print SHA FAIL against the blob at L. This is RevReceipts' spec.
- **(b) counter absent at the stamp.** Receipt stamped at a revision without the counter, carrying the current counter's sha. The checker must print SHA FAIL `counter_absent_at_stamp`, not PASS via fallback. My scratch run printed the tool's existing `counter_absent` label; RevReceipts' strict variant names it `counter_absent_at_stamp`, which says what failed and is the label to adopt.

RevReceipts reproduced both fixtures in a fresh clone at `99e3d63` and adopted the stamp-only route. Its earlier fallback proposal is marked wrong in `.ufo/waves/round-71/w2/RevReceipts.md` (V9, lines 290-317).

`--topo` also fails for this receipt now: carrier `99e3d63a`, parent `27db4ce8`, stamped `64da9e14`. It passed at `27db4ce` (carrier `7179d6d`, parent `64da9e1`) until `99e3d63` touched the file. RevReceipts reports the same instability.

### F1′ — MEDIUM — the round-70 restamps now verify, but were rewritten in place twice and line 1 no longer names its object

Status of the six headers:
- **The original F1 points 1-2 are resolved at `f5c845b`.** Line 1 is now sha256 of the matching claim's `counting_command` in `reports/round-70/claims.json`:

  | claim | digest | receipts |
  |---|---|---|
  | O | `b0555dcb…` | measures-o, controls-o |
  | Ca | `e391f886…` | measures-ca, controls-ca |
  | D | `2d157c19…` | measures-d, controls-d |

  I re-derived these with `hashlib.sha256(cmd.encode())`, with no trailing newline.
- **The controls now stamp the base.** They stamp `21e6a7f3…` with tree `ece8c7cd` = `21e6a7f^{tree}`, which is where their bodies reproduce. The measures stamp `453676a2`, tree `7153d0d1`, where their bodies reproduce. Header-equality mode passes 6/6.
- **The digest's object is no longer stated in-file.** `27db4ce`, whose message is about the id map and says nothing of receipts, removed the line-1 parenthetical. A reader now cannot tell that line 1 hashes a command string, not a counter file. Criterion 17 says "the counter's sha256", and round 70 has no `accept-*.py` counter to hash. RevReceipts tracks this as F-A.
- **The restamps were rewritten in place.** `f5c845b` and `27db4ce` rewrote lines 1-6 of the round-70 restamps. The round-71 re-stamps, by contrast, are append-only (previous header kept below the marker). The header form that wave 1 scored survives only in git at `1d1b432`, and `corrections-r70.md` records neither rewrite.
- **The routed stamp change is still undisclosed.** V70-1 routed the restamp "at `acc2d614`"; the measures stamp `453676a2`. The bodies do reproduce there, but no record states the change.
- **`worktree dirty (tracked): False` still sits above bodies that say "6cb51a4+landed edits".**
- **`--topo` fails 6/6.** Carrier `27db4ce8`, parent `e1d0d44d`; stamps `453676a2` and `21e6a7f3`. Lane census: 18 PASS / 10 FAIL of 28. The leg is satisfiable, so this counts against the receipts.
- **`--lands` is not counted against the restamps.** It cannot attest any receipt's current bytes. `git show <stamped>:<file> | cmp -s - <file>` mismatches for **28 of 28** header-carrying receipts. RevReceipts' earlier "2 present at stamp" were older re-stamps stamped `1d1b432`, not the bytes on disk; we now agree on 0 of 28. Only `--topo` can attest current bytes.
- **Criterion 19's sentence that "no header is ever written onto [a pre-protocol receipt's] original bytes" still conflicts with the restamp.** Nothing records the conflict.

### F2 — HIGH — `accept-ca.py` was hardened but still passes most fabrications; not frozen before data

**What changed.** `75d1675` and `57e0a72` changed the counter:
- "Original below" must now start with `# after-state receipt` or `# pre-data control`.
- QUARANTINE now requires the id set to equal a hard-coded 21-id `SLICE`.
- A class-admissibility check was added: S807, S812 and S835 must be UNVERIFIABLE.

**Mutation results at HEAD.** Each mutant ran in a fresh copy (`/tmp/revca2.ai6V/mut.sh`).

| mutant | mutation | at 14c88d9 | at 99e3d63 |
|---|---|---|---|
| A | header values set to `NOT-A-REVISION` / `x` | PASS | **PASS** |
| B | header block moved directly below the marker | PASS | FAIL V70-1 (fixed) |
| B2 | header block moved below the first two original lines | — | **PASS** |
| C | original bytes replaced with `# after-state receipt fabricated` | PASS* | **PASS** |
| D | S860 anchor reverted to `6cb51a4`; `acc2d614` moved to the used-by cell | PASS | **PASS** |
| E | reject sweep replaced with `rejected this round: none.`; a stray `flip` added | PASS | **PASS** |
| F | quarantine ids renumbered S001..S021 | PASS | FAIL QUARANTINE (fixed) |
| F2 | every non-unreachable row relabelled PRESENT | — | **PASS** |
| G | 27-word quote restored, line inserted at top | PASS | **PASS** |
| H | scorecard sentence negated | PASS | **PASS** |
| I | header block deleted | FAIL | FAIL |
| K | S807 (unreachable class) set to PRESENT | — | FAIL QUARANTINE (new leg works) |

\*At `14c88d9`, mutant C used `# fabricated body`.

**Remaining gaps:**
- V70-1 checks substring presence only: no values, no ordering above the marker, no comparison with prior bytes.
- V70-2 is line-level, not cell-level.
- V70-3 is positional (`r70[12]`).
- V70-4 and V70-5 are bare substrings.

**Freeze and predicate gaps (unchanged).**
- `accept-ca.py` is absent at `8c203bd` and first appears at `1d1b432`, the Ca data commit. It was not frozen pre-data.
- `--lands` is parsed at line 64 and never read.
- The counter never runs `tools/check-gate-quotes.py`, which the frozen predicate names. I ran it by hand on `corpus/lessons/round-71.md`: 0 findings, exit 0. The tool is also blind to 27 words.

RevReceipts confirmed both points independently.

### F3 — HIGH — the claim's declared `counting_command` gives 0 for the quarantine leg, target 21 (unchanged)

`claims.json` was last touched at `65ff151`. The awk segment `'$1 ~ /S[0-9]+/ && $2 ~ /^(PRESENT|REFUSED|UNVERIFIABLE)$/'` still prints **0** on the 21-row table: `$1` is empty and `$2` holds the id padded with spaces. A trimmed variant prints 21. Read literally, the kill rule fires on the declared measurement; the PASS rests on the counter's own parser. RevReceipts confirmed this independently.

### F4 — MEDIUM — the reject sweep says each item has reason + flip; one does not (unchanged)

- `corpus/lessons/round-71.md:38`: `EFDSS Morris pages (soft-404)` has no flip.
- The CAPTCHA-wall item is an access route the round used, not a refused candidate.
- All 13 Gate table rows are `admitted`. The refusals are scout pre-filters, not Gate or frontier decisions, so the shape V70-5 named persists in form.

### F5 — LOW — the round-70 Gate row grounds still pair the hardened selftest with `6cb51a4` (unchanged)

- `corpus/lessons/round-70.md:13`, grounds cell: "SELFTEST 10/10 … at `6cb51a4`".
- `6cb51a4:tools/check-supersession-settlement.py` (blob `1ef2e965`) prints `SELFTEST: 7/7` and contains none of the named cases.

### F6 — LOW — the V70-4 "row" is a prose subsection matched by a bare substring (unchanged)

`SCORECARD.md:1393` is the only case-sensitive match. Mutant H (a negated sentence) passes.

## PASS evidence at 99e3d63

**Receipt bytes.** For all six, `tail -n +9 <f>` equals `git show <prev>:<f>` (`cmp`), where prev is `acc2d61` for measures and `6cb51a4` for controls. RevReceipts verifies the same bytes against `453676a2`.

**Header values.**
- Each of the six header prefixes appears once in each file.
- `git rev-parse <stamp>^{tree}` equals the recorded tree for all six.
- `check-receipt-seq.py` in header-equality mode: RECEIPT-SEQ PASS.

**S860.** `grep -c acc2d614 corpus/SOURCES.md` = 1, in the anchor cell. `acc2d614` is the first commit carrying blob `6a314e9c`.

**Round-70 quote.** `awk -F'|' 'NR==13 {print $4}' corpus/lessons/round-70.md | wc -w` = 25. It is a verbatim contiguous prefix of blob `6a314e9c`.

**Quarantine bijection.** `comm -3` between the register slice ids and the table ids is empty; both have 21 unique ids. The register is `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`, sha `5afe1810…`.

**Quarantine tally.** The table gives PRESENT 10 · REFUSED 7 · UNVERIFIABLE 4, matching its tally line. Changes since `14c88d9`:
- S778 moved UNVERIFIABLE → PRESENT (EUC-JP decode).
- S816 moved PRESENT → REFUSED (capture byte-identical to a live re-fetch; quote absent).

Line 22 of the round-71 Ca receipt still says 10/6/5. That is historical preserved output from the earlier run, not a current claim.

## Residual risk / verification gaps

- **Verdict correctness.** I did not re-fetch the 21 quarantine URLs, so the S778 and S816 re-verdicts are taken on the table's notes and RevQuarantine's re-derivation.
- **Moving tree.** The lane moved 18 commits during this seat, so every result here is pinned to `99e3d63a`. A later commit touching any receipt changes `--topo` again.

## History (first pass at 14c88d9b, superseded where noted)

- **F1 (resolved by `f5c845b`).** Line-1 digests matched no blob in 7172 reachable blobs. The controls stamped `453676a2` while their bodies reproduced only at `21e6a7f`; this held for all three, and `controls-d` was confirmed per-command, matching RevReceipts.
- **`--lands` (withdrawn as evidence).** The `--lands 453676a2` failure is structural lane-wide. I counted 27 header-carrying receipts at `14c88d9`; RevReceipts counts 28 at HEAD. The difference is the later commit of round-71 `measures-c.txt`, which was untracked at `14c88d9`.
- **Counter mutants.** 8 of 12 mutants passed the counter at `1d1b432` (sha `3f3f63fc`). The QUARANTINE leg then checked the count only.
