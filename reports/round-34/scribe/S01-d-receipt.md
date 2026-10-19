- Seat: S01 | scribe | claim D | date 2026-10-19 | baseline da68a6d

# S01 — final depth (claim D) receipt, cut 2026-10-19T07:12Z (rev 1)

## 0. Status at this cut — read this first

**Claim D is not verified at this cut, and cannot be until the integrator applies
the drafted shared-file changes and the r7 freeze lands.** Nothing below presents a
green as the after-state: the after-state directory
`reports/round-34/handoff/declared-in-r7/` **does not exist** at this cut
(`ls reports/round-34/handoff` → `No such file or directory`, exit 2, 07:09Z), so all
three of claim D's own counting commands are owed or only partially observable (§7).

What this receipt is: the post-review fold of the reviews that landed. **R02**
(`review/R02-d-review.md`) and **R03** (`review/R03-d-review.md`) are folded in §6 as
accepted findings / integration rules. **R01 has not landed** (`ls reports/round-34/review`
→ `R02-d-review.md`, `R03-d-review.md`, plus the two claim-O reviews, 07:09Z); its slot
is carried as owed per the shared missing-dependency rule
(`reports/round-34/targets.json:10`). The D-block builders landed during this seat's run
(D01–D04, D08, D10–D12, D14, D16, D18, K01, K02, P01); every number this seat quotes
from them is attributed, and every number this seat asserts as measured was re-taken
first-hand (§9 commands).

**Honesty declaration (R02-F3-adjacent, R03 F1/F2 as the decisive reading).** The
current default pair is shape-green and semantically stale, and it is green *because*
the renderer treats the stale prose as a pinned **input** — the packet's D4 rows are
carried verbatim from the filed `reports/round-20/handoff/claims-map.md`
(`tools/exercise-handoff-e2e.py:184,2289-2320,3511`) and `OQ-V3-05` is a compiled-in
literal (`:3524-3531`). A green `--profile v3 --quiet` therefore certifies
reproducibility, not currency, and must never be read as claim D's semantic leg. The
decisive leg is the live-vs-row audit (§3).

| leg at this cut | state | evidence |
|---|---|---|
| L1 gate on the new packet | **not observable** — path absent; the same gate on the current pair is green | §2, §7 |
| L2 e2e `--profile v3 --quiet` | **green, but against the r6 default** — pre-move reading, not the after-state | §2 |
| L3 `reports/round-34/run-validation.py` | **absent by construction** (round's own runner, integrator-owned) | §7 |
| L4 zero-stale-figure audit | **owed** — no r7 bytes exist; the audit recipe is on record | §3, §7 |
| L5 re-pin cascade | **drafted, not applied** (D10, D16, K02, R02) | §5 |
| L6 byte preservation (pre-build) | **verified by two seats** — D11 and R03 §4 reproduce each other | §2.4 |
| R01 / R02 / R03 folded | R02, R03 **folded**; R01 **owed** | §6 |

Scope statement: this seat wrote exactly this file plus two scratch captures
(`.scratch/s01-links.json`, `.scratch/s01-unc.json`). No filed round byte, no
`corpus/lessons/*.md`, no `tools/gates/frozen/**`, no `.ufo/**` and **no shared file**
was written; no `reports/round-*/run-validation.py` was executed in-tree (F-C13-1);
no git command mutated state; no network call was made. `git status --porcelain` at
07:09Z read `?? reports/round-34/` (one row), matching D11 and R03 §4.

## 1. Method and dependency state

Mission (`reports/round-34/targets.json`, seat S01): "Final D receipt post-review
(fold R01-R03 findings as accepted/errata)." Out path: `scribe/S01-d-receipt.md`.

At this seat's first read the round directory held `claims.json`, `targets.json`,
`telemetry/dispatch-declared.json` and one D fragment; the D block and the two reviews
landed while this seat measured. Per the shared missing-dependency rule
(`targets.json:10`) this seat re-ran every claim-D command it could and re-measured
every pin it quotes rather than inheriting numbers, then folded each fragment as it
landed. Exit codes were captured unpiped (`; echo "EXIT=$?"`), never as a pipe's
status. Interpreter: `python3 -V` → **Python 3.14.7** (recorded because counting-command
outputs are interpreter-sensitive); run environment `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`, repo root
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`, HEAD
`da68a6d705e41f369f21e8607bfaab5b54077f84`.

## 2. Claim D's before-state, reproduced first-hand (2026-10-19T07:0x–07:1xZ)

### 2.1 The pin and the pair

| surface | value at HEAD | citation |
|---|---|---|
| renderer baseline default | `"reports/round-30/handoff/declared-in-r6/expected.json"` | `tools/exercise-handoff-e2e.py:1933` |
| renderer frozen-dir default | `"reports/round-30/handoff/declared-in-r6"` | `tools/exercise-handoff-e2e.py:1934` |
| pair digests (live, this seat) | `packet.md` `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb`; `twin.json` `6633443d70ce44ed2bb43ab58aa60a1c98e4bbc79b2f577a63181c89dc16fd4e` | `sha256sum` over the pair |
| pair's freeze record | `freeze.txt:2` `packet_sha256: 6ced88ad…`; `:3` twin `6633443d…`; `:1` `frozen: 2026-10-18` | `reports/round-30/handoff/declared-in-r6/freeze.txt` |
| other pair digests (R02 §0, corroborated) | `expected.json` `ea1e2927…`, `freeze.txt` `6fe70c0c…`, `run.log` `b5ee3351…` | `review/R02-d-review.md:18-24` |

The live `packet.md` digest equals `freeze.txt:2`: the pair is self-consistent and its
defect is semantic, exactly as claim D's `before` states
(`reports/round-34/claims.json:26`).

### 2.2 The claim's two counting commands, as measured now

```
$ python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md
INFO scan: fields=16/16 glossary-entries=20 findings=0                       # exit 0

$ python3 tools/exercise-handoff-e2e.py --profile v3 --quiet                  # exit 0, ~3.3 s
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27
statuses=16/7/4 v2_subset=equal alias_leg=landed
packet_sha256=6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb
```

Two harness legs re-run by this seat for the same window: `python3 -B
tools/harness/packet_links.py --packet …/declared-in-r6/twin.json --json` → exit 0,
`links_checked 105`, `resolved 105`, `findings []`;
`python3 -B tools/harness/packet_uncertainty.py --packet …/declared-in-r6/twin.json
--json` → exit 0, `claims 27`, findings 0. Both match the e2e's own lines and the
filed `run.log`.

The gate is green **by construction, not by luck**: its own docstring states it
"judges the packet document, not the truth of its contents"
(`tools/gates/handoff-packet-check.py:28`). Claim D's before-state therefore reproduces
exactly: shape-green, semantically stale.

### 2.3 The staleness, measured live-vs-file

Live readings (this seat, `examples/culture-d4/typed-labels.d4.yml` `coverage` block
`:29-46`): `conflicts: 0` (`:30`), `findings_hold_or_fail: 12` (`:31`),
`findings_total: 12` (`:32`), `label_findings_fail: 0` (`:33`),
`label_findings_hold: 12` (`:34`), `labels_by_kind {borrowed-strata: 6, native-form: 64,
translated-label: 12}` (`:35-39`), `rank_quarantine_handles: 0` (`:40`),
`rank_rules_unresolved_items: 0` (`:44`), `reconciliation_records: 6` (`:45`),
`typed_labels: 82` (`:46`); `stats` `{fail: 0, hold: 12, labels: 82}` (`:2865-2869`);
`act_rules: []` (`:303`); `examples/culture-d4/expected-holds.json#counts`
`{hold: 12, note: 0, fail: 0}`.

| stale site in the r6 packet | r6 says | live | live citation |
|---|---|---|---|
| `packet.md:148` (D4-CL05 basis) | `typed_labels 74`, `native-form 56`, `findings_total 16`, `findings_hold_or_fail 15` | 82 / 64 / 12 / 12 | `typed-labels.d4.yml:46,37,32,31` |
| `packet.md:149` (D4-CL06 basis) | `(hold 15, note 1, fail 0)` | hold 12, note 0, fail 0 | `expected-holds.json` `counts` |
| `packet.md:150` (D4-CL07 statement) | `conflicts (4), quarantine handles (3)` | 0 / 0 | `typed-labels.d4.yml:30,40` |
| `packet.md:152` (D4-CL09 basis) | `13 unresolved rank items, 3 quarantine handles and 4 conflicts` | 0 / 0 / 0 | `typed-labels.d4.yml:44,40,30` |
| `packet.md:307` (OQ-V3-05 bullet) | `twelve form holds + three rank holds + one note, thirteen unresolved…` | 12 holds, 0 note, 0/0/0 | as above |
| **correct in the same document** `packet.md:68-69` (A-30/A-31) | `82 labels (64 native-form …)`, `12 findings`, `12 holds / 0 note / 0 fail` | agrees with live | `packet.md:68-69` |

The twin mirrors the Markdown: this seat counted the stale tokens in
`reports/round-30/handoff/declared-in-r6/twin.json` (`grep -o -F … | wc -l`) →
`typed_labels 74` ×1, `hold 15, note 1` ×1, `conflicts (4)` ×1,
`quarantine handles (3)` ×1, `thirteen unresolved rank items` ×2. Row locations, read
by this seat: `twin.json:1087` and `:1089` (D4-CL05 statement/basis),
`:1105` (D4-CL06 basis), `:1120` (D4-CL07 statement), `:1157` (D4-CL09 basis),
`:2619` (OQ-V3-05 question). R03's independent token census over both files counts
**15/15** stale tokens present (`review/R03-d-review.md:140-146`).

**The staleness is D4-local, not a document-wide drift.** D2's rows match live D2 bytes
(`examples/culture-d2/typed-labels.d2.yml:29-46` → typed 58, 46/10/2, findings 16/15,
13 unresolved, 3 handles, 4 conflicts, 10 reconciliation records) which is exactly what
`packet.md:129-130`, `:284` and OQ-V2-03 `:301` state — confirmed here and independently
in `depth/D12-receipt.md:164-167` and `depth/D18-verify-ledger.md:86-98`. Also
unchanged-and-correct in the D4 rows: `translated-label 12`, `borrowed-strata 6`,
`label_findings_fail 0`, `reconciliation_records 6` — the trap tokens R03-F9 and
`depth/D14-scribe.md:249-263` warn an audit about.

**The intra-file contradiction claim D names is real**
(`reports/round-34/claims.json:28`): the manifest rows at `packet.md:68-69` already
carry the live values while the claim rows one screen later do not — the document
contradicts itself about the same artifact.

**Provenance of the stale figures** (recorded so the rewrite is understood as a
re-generation, not a typo fix): they are the round-18-generation projection's counts
carried forward — `depth/D18-verify-ledger.md:101-135`, converging with
`corpus/lessons/round-25.md:82-85` ("the stale prose has **two** sources, not one") and
`depth/D04-oq-glossary.md:11-31`. One row is worse than mis-numbered: D4-CL09's
mechanism sentence describes `act_rules` rows the live projection no longer emits
(`act_rules: []`, `typed-labels.d4.yml:303`; `depth/D12-receipt.md:142-148`,
`depth/D18-verify-ledger.md:146-155`).

### 2.4 Byte preservation (pre-build): verified

D11's proof (`depth/D11-preservation.md`) and R03's independent re-run agree
item-for-item (`review/R03-d-review.md:174-196`): `git diff --name-only HEAD` → 0;
`git status --porcelain` → `?? reports/round-34/` only; 1909/1909 filed files
byte-identical, set fingerprint
`1713e725abbd3a73b03ff2e42a8774adcd9b8c294c458f25d4657065b126ce71`; 0 filed files with
post-commit mtimes; the five revision homes are rounds 22/23/25/26/30 (D11's correction
of the mission's `round-{2,4,5,6}/handoff` shorthand). This seat reproduced the HEAD
identity (`git rev-parse HEAD`) and the clean `git status` row; it did not re-run the
1909-file sweep — D11 and R03 own that leg, and R03 §4 is the independent verdict:
**D11 verified, 0 defects**.

## 3. The decisive constraint: the stale prose is a renderer *input*

This is the finding that governs whether claim D can verify at all, and it is the one
the claim's `before` does not name. Four routes measured it independently; this seat
re-derived it from the source bytes before folding the others.

1. **The twelve D4 ledger rows are carried verbatim from a filed file.**
   `CLAIMS_MAP = "reports/round-20/handoff/claims-map.md"`
   (`tools/exercise-handoff-e2e.py:184`), parsed by `v3_parse_claims_map`
   (`:2289-2320`, requiring exactly 12 rows each with statement/basis/links) and used at
   `:3511`; the packet says so itself at `packet.md:3`, `:125` and manifest row **A-57**
   (`packet.md:95`). The stale words live in that filed file:
   `reports/round-20/handoff/claims-map.md:104` (D4-CL05), `:116` (D4-CL06), `:124`
   (D4-CL07), `:138` (D4-CL08), `:158` (D4-CL09). `reports/round-20/**` is filed bytes —
   never edited.
2. **`OQ-V3-05`'s words are a compiled-in literal.** `tools/exercise-handoff-e2e.py:3524-3531`
   appends the row with the string "twelve form holds + three rank holds + one note,
   thirteen unresolved rank items, three quarantine handles and four conflicts"
   (`:3526-3527`, read by this seat). No artifact and no map can correct it.
3. **The exercise refuses any packet it cannot re-assemble.** `v3_exercise` compares the
   freshly assembled `packet_sha256` with the frozen baseline and raises `E2E-DIGEST`
   (`:3932-3941`), and it first requires every read-set input digest to equal the frozen
   one (`:3822-3826`). `--freeze` writes the renderer's own bytes
   (`(target / "packet.md").write_text(assembly.packet, …)`, `:4085`), so a frozen
   revision cannot be a hand-edited packet either.
4. **A fresh render today is byte-identical to the filed r6 packet.** Measured
   independently by D02 (`depth/D02-render.md:39-71`, read-set drift 0) and D12
   (`depth/D12-receipt.md:84-116`, `cmp` → `IDENTICAL`), and implied by this seat's own
   green default run (§2.2) — the render reproduces `6ced88ad…`.

**Consequence (route change, not quality objection):** `after_required`'s "regenerates
the packet from the current D2/D3/D4 artifacts, rewrites the claim-ledger/OQ prose to
live numbers" is **unachievable through the renderer as it stands**. The corrected prose
must enter *through the renderer's inputs* — a new claims-map file plus a re-pointed
`CLAIMS_MAP`, and a rewritten `OQ-V3-05` literal — i.e. shared-file changes the seats
draft and the integrator applies (`targets.json:7`). R03 files this as its two blockers
(`review/R03-d-review.md:39-77`, F1/F2); the drafted before/after blocks are D16's
(`depth/D16-gap-fill.md:160-186`, surfaces A–F, recommended home
`reports/round-34/handoff/claims-map.md`) and D08's
(`depth/D08-links-uncertainty.md:190-254`), with D04 owning the OQ literal text
(`depth/D04-oq-glossary.md:56-121`).

**One consequence of this route that must not be lost** (R03-F6,
`review/R03-d-review.md:107-116`): the e2e selftest's m11 control mutates the exact
sentence "the run evidence is tools/assemble-d4-typed.py --selftest exit 0 with 12/12
checks" inside `CLAIMS_MAP` (`tools/exercise-handoff-e2e.py:4381-4395`; the sentence
lives at `reports/round-20/handoff/claims-map.md:138`). The new map's D4-CL08 row must
keep that sentence verbatim or the selftest's own assertion fails. **This seat's check:
no landed D-block draft contains that sentence** — `grep -rn "12/12 checks"
reports/round-34/` → `depth/D03-ledger-rows.md:56` (an output quote),
`scout/K01-packet-state.md:190,195,358` (quotes/reads), `review/R03-d-review.md:109`
(the finding); the new-map draft at `depth/D16-gap-fill.md:168-174` does not carry it.
**Requirement carried forward** (§7, §8).

## 4. Prior-art note: this class has fired before

Carried because it decides how the round should describe the fix: `declared-in-r4` was
exactly a hand-built prose correction, and the following renderer builds reverted it —
r5's packet reads `hold 15, note 1` again (`review/R03-d-review.md:61-65`, citing
`reports/round-25/v3-supersession/freeze.txt:2` and
`reports/round-26/handoff/declared-in-r5/packet.md:149`; independently measured at
`corpus/lessons/round-25.md:82-85`). The filed r6 freeze record carries the same story
in its own diff line (`reports/round-30/handoff/declared-in-r6/freeze.txt:8`:
`re-frozen packet_sha256: ec30b11f… -> 6ced88ad…`). So an r7 that fixes the prose
without moving the *input* route reproduces the r4→r5 revert at a new address — the
reason R03 calls F1/F2 blockers rather than quality nits.

## 5. The re-pin surface (cascade)

This seat's own census (`git grep -l "declared-in-r6"`, tracked files only) → 15 files:
`LOG.md`, `SCORECARD.md`, `tools/exercise-handoff-e2e.py`, the r6 pair's own
`packet.md`, `reports/round-31/scope.md`, and ten filed `reports/round-33/**`
fragments (A02, A10, A11, A12, A14, A15, K04, P02, R07, S03). R02's independent census (`review/R02-d-review.md:32-67`) classifies the
same tree, adding the *derived* surfaces that a literal grep cannot see:

| class | surfaces | action |
|---|---|---|
| live pins | `tools/exercise-handoff-e2e.py:1933` (`V3_BASELINE_DEFAULT`), `:1934` (`V3_FROZEN_DIR_DEFAULT`) | EDIT by the integrator (drafted: `depth/D10-repin-drafts.md:63-111`) |
| derived (bytes are a function of the pin) | `:3185` (the packet's own gate line interpolates the constant), `:3806`, `:4149`, `:4172`, `:4561`, `:4575` | no edit; **ordering constraint** (R02-F1, R03-F7) |
| append-only state of record | `SCORECARD.md:400`, `LOG.md:3428` | NEW round-34 rows only (drafted: `depth/D10-repin-drafts.md:177-200`) |
| filed narratives | `reports/round-31/scope.md:55`; ten `reports/round-33/**` fragments | never edited; named as superseded readings in this round's record |
| by-reference consumers | 12 filed runners executing `--profile v3` with no explicit baseline (r20–r31; r32 has zero handoff legs, r33's handoff legs are the sample-packet gate only) | cannot be edited; their filed receipts become historical readings after the move (R02-F3) |

K02's landed census (`scout/K02-repin-census.md`) classifies the pins as PM/PC/PR/PS/PN
and proves the A1/A2 must-move-together coupling (`:20-60`). **Diff against R02's
class list, taken by this seat:** K02 covers the mutable pins, the same-file consumers
(B1 = `:3185`), the filed records and the prose rows; its fragment contains no token
for the by-reference runner class (`grep -c "by-reference"` → 0) and none for
`typed-pipelines` (`→ 0`), while `run-validation` appears 6×. R02-F6 asked for exactly
that diff; the result is: **R02's S9/S10 classes and its F4 pre-flight are additions to
K02's census, not duplicates.**

One further pin-surface no literal grep reaches (D16 §4, `depth/D16-gap-fill.md:181-186`):
`CLAIMS_MAP` itself pins **round-20**, not r6, so the cascade that fixes §3's constraint
is invisible to a `declared-in-r6` census and must be carried as its own new rows.

## 6. Fold-in register for R01–R03

| slot | source | state | fold-in result |
|---|---|---|---|
| R01 | `reports/round-34/review/R01-d-review.md` | **NOT LANDED at this cut** (`ls reports/round-34/review` at 07:09Z: R02, R03, R04, R05) | **owed** — §8. Its mission (stale-number hunt, renderer-contract violations, freeze-design holes) overlaps §§3–5; when it lands, its findings must be folded into this register by the integrator or a successor scribe, and any finding that contradicts §§3–5 must be re-measured, not averaged |
| R02 | `review/R02-d-review.md` | landed, folded | seven findings (F1–F7), all accepted; fold table below |
| R03 | `review/R03-d-review.md` | landed, folded | nine findings (F1–F9), all accepted; fold table below; its two blockers are §3's constraint and its preservation verdict confirms D11 |

### R02 findings — accepted / errata

| finding | fold-in result |
|---|---|
| **R02-F1** (material): the r7 packet's bytes are a function of the *constant*, not of `--baseline`; a draft rendered before the re-point carries the superseded path in its gate line and cannot be the landed bytes | **accepted** — §5 derived class; the re-point must precede the freeze. Counting check adopted for the landed revision: `grep -c 'declared-in-r6' reports/round-34/handoff/declared-in-r7/packet.md` must be 0 and its gate line must name the r7 baseline (`review/R02-d-review.md:85-90`) |
| **R02-F2** (material): `v3_freeze` writes five files in-tree (`:4073-4117`), and `expected.json` is integrity-checked on load, so it can never be hand-authored | **accepted** — §7 rule: the r7 directory is produced by one freeze run into a **fresh** directory; never re-frozen after filing. Named as the same write-own-receipt shape claim O audits, aimed at this round's own new directory (`review/R02-d-review.md:92-104`) |
| **R02-F3** (material): 12 filed runners consume the default by reference; after the move their isolated re-runs read r7 | **accepted** — §5; the round record must name this supersession and must not claim those filed receipts reproduce. Post-move exit codes stay `to-verify` — **no file was executed to test it** (F-C13-1) |
| **R02-F4** (informational): cross-check the new `expected.json.inputs` against `tools/gates/typed-pipelines.json`'s first-match generation | **accepted as pre-flight** — the four D4 digests are stable at this cut (`aac91246…`, `d581e0ad…`, `c23b0ab5…`, `e6ae9828…`, §2.3/§9), so the check is cheap and must run before the freeze |
| **R02-F5** (low): `.scratch` mirrors carry the pre-move constant and are not evidence surfaces | **accepted** — this receipt's own two scratch captures are output-only (JSON receipts), not mirrors of the pin |
| **R02-F6** (completeness): the cascade class list in the push brief omits the derived interpolation, the by-reference consumers, the freeze's write set, the future r34 validator and the negative surfaces; row-set precedent is rounds 27/28 | **accepted** — §5 carries the classes; the r27/r28 row-set precedent (`reports/round-28/sweep/repin-rows.json`, `reports/round-27/pinsweep/sweep.md:252-255`) is the shape D10's rows should match. My diff of K02 against §1 (recorded) is the diff R02 asked for |
| **R02-F7**: verdict on D11 | **accepted as confirmation** — D11's set is a superset of R02's; no conflict (`review/R02-d-review.md:156-161`) |

### R03 findings — accepted / errata

| finding | fold-in result |
|---|---|
| **R03-F1** (BLOCKER): the D4 ledger prose is a pinned input, not a render | **accepted** — §3.1/3.3/3.4; route change to a new claims-map file with `CLAIMS_MAP` re-pointed (drafts: D16 §4, D08 §6) |
| **R03-F2** (BLOCKER): `OQ-V3-05` prose is a hard-coded literal (`:3523-3532`), same class as the hardcoded map path at `:2700` and the supersedes statement at `:2711-2712` | **accepted** — §3.2; the literal must be rewritten and the two prose literals re-pointed **before** the freeze, or the frozen packet carries the stale row and the "zero stale figures" threshold fails on r7's own bytes |
| **R03-F3** (MAJOR): no version bump planned; `V3_PACKET_VERSION = "3.1.1"` (`:1932`) is rendered into the packet and the baseline, and §4:55 requires revised bytes to carry a new version | **accepted, with a recorded divergence**: `depth/D10-repin-drafts.md:92` states "`V3_PACKET_VERSION` stays `3.1.1` unless P01/D01 decide otherwise" while R03-F3 requires a bump. **The integrator must resolve this one way and record it** — the two fragments cannot both be followed. This seat does not choose for them |
| **R03-F4** (MAJOR): no supersedes/`derived_from` record inherits — r5's and r6's freeze files contain no `parent|supersed|derived` line; r4's `corrections:` block is the in-repo template | **accepted** — the r7 revision must carry (a) a narrative supersession naming r6 by version + packet digest `6ced88ad…` + expected.json digest `ea1e2927…` and (b) an old→new mapping file per §9:153 |
| **R03-F5** (MAJOR): predecessor accuracy — r6's own narrative supersedes round-20 3.0.0, never r5, and the r5/r6 renderer builds reverted r4's corrections | **accepted** — r7's statement must name **both** that it supersedes the r6 default and that it re-instates r4's corrections at live-measured values; a clean r6→r7 lineage claim would hide the reverted correction (§4) |
| **R03-F6** (DO-NOT-BREAK): the new claims-map must retain the m11 selftest anchor sentence | **accepted; OPEN** — §3, evidenced by this seat's own grep: no landed draft carries the sentence |
| **R03-F7** (ordering): drafts → fresh-directory freeze → `--quiet` verify | **accepted** — §7's ordered checklist; converges with R02-F1 and `depth/D01-layout.md:66-118`'s build script |
| **R03-F8** (auditable adoption): per-surface old path + old digest → new path + new digest, date, reason, and the fact that r6 stays filed and green | **accepted** — §5/§7; "the default moved" alone is not an adopted-revision record |
| **R03-F9** (audit recipe): the stale-token census is partial; a row-level "wrong number" test both over- and under-reports; the audit must be token-level against live sources | **accepted** — §2.3's trap tokens; converges with `depth/D14-scribe.md:249-263` (audit scoping rule) and `depth/D18-verify-ledger.md:167-183` (negative control on the method) |

Neither review falsifies a measurement in D12's before-state, and no review asked for a
filed byte to move. Both reviews' blocker findings reduce to the same single order of
operations (§7).

## 7. What would make claim D verify

Ordered, with the claim's own thresholds (`reports/round-34/claims.json:33-37`) and the
reviews' constraints folded in. Steps 1–3 are integrator-applied shared-file drafts;
nothing here is a seat's to apply.

1. **Apply the input-route drafts** (§3): new claims map
   `reports/round-34/handoff/claims-map.md` (12 D4 rows, live numbers, **m11 anchor
   sentence preserved in the D4-CL08 row**), `CLAIMS_MAP` re-pointed at `:184`, the
   `OQ-V3-05` literal rewritten (`:3524-3531`), the prose literals at `:2700`/`:2711-2712`
   re-pointed, and the version decision (R03-F3 vs D10 §2 divergence) named.
2. **Apply the re-pin drafts** (`depth/D10-repin-drafts.md`): `:1933-1934` →
   `reports/round-34/handoff/declared-in-r7[/expected.json]`, plus NEW append-only rows
   for `SCORECARD.md`, `LOG.md` and the supersession/adoption record (R03-F4/F5/F8).
   The re-point must precede the freeze (R02-F1, R03-F7).
3. **Freeze once into a fresh directory:**
   `python3 tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-34/handoff/declared-in-r7`
   — writes `packet.md`, `twin.json`, `expected.json`, `freeze.txt`, `run.log`
   (`tools/exercise-handoff-e2e.py:4077-4117`). `expected.json` must be produced by this
   run, never authored (R02-F2).
4. **Claim D counting command 1:**
   `python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md`
   → exit 0, `fields=16/16 glossary-entries=20 findings=0` (threshold: gate green on the
   new pair, `claims.json:30`).
5. **Claim D counting command 2:**
   `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0 with
   `packet_sha256` equal to `sha256sum reports/round-34/handoff/declared-in-r7/packet.md`
   and to `freeze.txt`'s `packet_sha256` (the claim's `after_required`).
6. **The decisive semantic leg (L4), which no green above proves:** re-run §2.3's live
   readings and diff them against the new rows; zero stale figures in
   `D4-CL05…CL09` and `OQ-V3-05`; the D4-CL09 narrative must match `act_rules: []`, not
   merely carry corrected digits (`depth/D12-receipt.md:142-148,221-225`; R03-F9).
7. **Cascade completeness:** `grep -c 'declared-in-r6'` in the new packet = 0; the gate
   line names the r7 baseline; every §5 surface either moved or holds a recorded
   superseded row; the r6 pair's five digests are unchanged (R02 §3 items 3–4).
8. **Preservation at close:** §2.4's witness table still holds and no filed byte moved
   (`git status --porcelain` free of `reports/round-*` rows).
9. **Claim D counting command 3:** `python3 reports/round-34/run-validation.py` → exit 0
   (the runner does not exist yet; integrator-owned).

**At this cut, step 1 has drafts but no applied change, steps 2–3 have drafts but no
landed r7 directory, and steps 4–9 are unobservable.** The honest verdict is therefore
**not verified — before-state reproduced, route identified, after-state owed.**

## Owed

- `reports/round-34/review/R01-d-review.md` — the first D review; absent at this seat's
  cut. Its findings (stale-number hunt, renderer-contract violations, freeze-design
  holes) must be folded into §6 by the integrator or a successor scribe, and any
  contradiction with §3 must be re-measured.
- `reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,expected.json,freeze.txt,run.log}`
  — the after-state; step 3's fresh-directory freeze is the only producer.
- `reports/round-34/handoff/claims-map.md` — the new renderer input (D16 draft B / R03
  F1's recommended home), including the **verbatim m11 anchor sentence** in D4-CL08
  (R03-F6 is undischarged: no landed draft carries it).
- The `tools/exercise-handoff-e2e.py` drafts as integrator edits: `:184`, `:1933-1934`,
  `:2700`, `:2711-2712`, `:3524-3531`, `:2290`, `:29-34`, and — if R03-F3 wins the
  divergence — `:1932` (`V3_PACKET_VERSION`). Seats never edit shared files.
- Resolution of **R03-F3 vs `depth/D10-repin-drafts.md:92`** (version bump or not) and
  the consequent `expected.json.packet_version`, naming which fragment was followed.
- R02's `to-verify` item: post-move exit codes of the 12 by-reference filed runners
  (isolated `git archive` copy only; never in-tree) or an explicit "not run" record.
- `reports/round-34/depth/D05-packet-draft.md`, `depth/D07-gate-run.md`,
  `depth/D09-freeze-design.md`, `depth/D13-negatives.md`, `depth/D15-gap-fill.md`,
  `depth/D17-verify-gates.md`, `depth/D19-verify-repin.md`, `depth/D20-verify-preservation.md`,
  `cross/X00-connector.md` — D-block seats whose outputs were absent at this cut; their
  L1/L2/L4/L5 legs are owed for the close-time audit.
- L4's audit instrument: D16 §5's script (`depth/D16-gap-fill.md:186-293`) and D18's
  oracle (`depth/D18-verify-ledger.md:28-58`) must be re-run against the **landed** r7
  bytes, not against a draft.

## Citations

Paths:lines

- `reports/round-34/claims.json:21-37` (claim D before/after/thresholds), `:68-74` (non-goals);
  `reports/round-34/targets.json:5-11` (shared rules; `:7` shared-file integrator rule, `:10` missing-dependency rule)
- `tools/exercise-handoff-e2e.py:184` (`CLAIMS_MAP`), `:1932` (`V3_PACKET_VERSION`), `:1933-1934` (defaults),
  `:2289-2320` (`v3_parse_claims_map`), `:2566` (manifest "carries them verbatim"), `:2699-2700`/`:2711-2712` (hardcoded prose),
  `:3185` (packet gate line interpolates the constant), `:3511` (`self.d4_rows = v3_parse_claims_map(root)`),
  `:3524-3531` (`OQ-V3-05` literal), `:3822-3826` (input-digest drift), `:3932-3941` (`frozen-packet` / `E2E-DIGEST`),
  `:3978-4138` (`v3_freeze`), `:4085` (`packet.md` written from `assembly.packet`), `:4090` (`expected.json` write),
  `:4381-4395` (m11 control on `CLAIMS_MAP`)
- `tools/gates/handoff-packet-check.py:28` ("judges the packet document, not the truth of its contents")
- `reports/round-30/handoff/declared-in-r6/`: `packet.md:3,68,69,95,125,129-130,148,149,150,152,284,301,307`;
  `twin.json:1087,1089,1105,1120,1157,2619`; `freeze.txt:1,2,3,4,8`; `expected.json` (`counts`, `inputs`, `packet_sha256`, `baseline_digest`); `run.log`
- `reports/round-20/handoff/claims-map.md:104,116,124,138,158` — the stale source (filed; digest `4b1b9a35…`)
- `examples/culture-d4/typed-labels.d4.yml:29-46,303,2865-2869`; `examples/culture-d4/expected-holds.json` (`counts`);
  `examples/culture-d2/typed-labels.d2.yml:29-46`
- `reports/round-34/depth/D12-receipt.md` (the draft this receipt finalizes): `:18-31,84-116,118-167,169-193,207-225`;
  `depth/D11-preservation.md`; `depth/D02-render.md:39-71,138-146`; `depth/D04-oq-glossary.md:56-121,211-231`;
  `depth/D03-ledger-rows.md:64-157`; `depth/D08-links-uncertainty.md:173-254`; `depth/D10-repin-drafts.md:20-111,113-200`;
  `depth/D14-scribe.md:249-263`; `depth/D16-gap-fill.md:118-186,307-314`; `depth/D18-verify-ledger.md:28-58,86-98,101-135,146-183`;
  `depth/D01-layout.md:12-118`; `scout/K01-packet-state.md:190,195,358`; `scout/K02-repin-census.md:20-60`; `plan/P01-d-plan.md:17-35`
- `reports/round-34/review/R02-d-review.md:9-24,32-67,70-172`; `review/R03-d-review.md:14-23,25-36,39-152,153-172,174-196,198-224`
- `reports/round-33/adj/A02-handoff.md:94-120` (finding A02-H1 — the filed antecedent of claim D, reproduced here independently)
- `corpus/lessons/round-25.md:82-85`; `reports/round-25/v3-supersession/{freeze.txt,build-revision.py}`;
  `reports/round-26/handoff/declared-in-r5/packet.md:149`; `reports/round-28/sweep/repin-rows.json`; `reports/round-27/pinsweep/sweep.md:252-255`
- `SCORECARD.md:400`, `LOG.md:3428`, `reports/round-31/scope.md:55` (filed surfaces the cascade must not edit)

Commands (this seat, 2026-10-19T07:05–07:12Z, repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; exits unpiped)

- `python3 -V` → `Python 3.14.7`; `git rev-parse HEAD` → `da68a6d705e41f369f21e8607bfaab5b54077f84`
- `git status --porcelain` → `?? reports/round-34/` (single row)
- `python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md` → exit 0, `INFO scan: fields=16/16 glossary-entries=20 findings=0`
- `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0, `packet_sha256=6ced88ad…` (output quoted in §2.2)
- `python3 -B tools/harness/packet_links.py --packet …/declared-in-r6/twin.json --json` → exit 0, `links_checked 105`, `resolved 105`, `findings []`
- `python3 -B tools/harness/packet_uncertainty.py --packet …/declared-in-r6/twin.json --json` → exit 0, `claims 27`, findings 0
- `sha256sum` on the r6 pair + `examples/culture-d4/{typed-labels.d4.yml,expected-holds.json}` + `reports/round-20/handoff/claims-map.md` (`4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8`) + `tools/exercise-handoff-e2e.py` (`a5e4a8c5dda9d63c177a3dce75a8716ba5d285371d0a37a2535f6c323e7619df`)
- `python3 -c` digest comparison of `expected.json#inputs` against live sha256 (5 files checked: `typed-labels.d4.yml`, `expected-holds.json`, `packet.d4.yml`, `packet.d4.typed.yml`, `typed-labels.d2.yml` — all match)
- `grep -n`/`sed -n` reads as cited; `grep -o -F … | wc -l` stale-token counts over `twin.json` (§2.3)
- `git grep -l "declared-in-r6"` → 15 tracked files; `grep -rn "declared-in-r6" --exclude-dir=.git .` → 76 paths including `.scratch` mirrors
- `grep -rn "12/12 checks" reports/round-34/` → 5 hits, none a landed new-map draft (§3)
- `grep -c -F` probes over `scout/K02-repin-census.md` (`by-reference` 0, `typed-pipelines` 0, `run-validation` 6, `3185` 2, `SCORECARD` 5, `LOG.md` 5)
- `ls reports/round-34/handoff` → `No such file or directory` (exit 2); `ls reports/round-34/review` → R02, R03, R04, R05
- Not executed (F-C13-1 prevention): no `reports/round-*/run-validation.py` in-tree — the only such invocation in this seat's window was D12's, over a non-existent round-34 path
