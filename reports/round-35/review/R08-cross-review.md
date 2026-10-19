- Seat: R08 | reviewer | cross | date 2026-10-19 | baseline 4a7aede

# R08 — cross-claim review: claim C vs the r7 freeze read set; claim O vs the C/A landings

Method: every live run below was made in an isolated `git archive HEAD` copy under
`.scratch/` (`r08-iso`, `r08-iso2`), never in-tree; no `reports/round-*/run-validation.py`
was executed; no `--freeze` was pointed at `reports/round-34/handoff/declared-in-r7`
(probe freezes went to `.scratch/r08-iso/.probe/refreeze`, inside the copy).

## 1. X00's question, answered: a re-freeze would see ZERO drift from claim C

**Verdict: no drift.** Two independent lines — structural and empirical.

Structural (the read set cannot absorb the new entries by construction):

- `V3_READ_SET` is a hard-coded 58-member tuple (`tools/exercise-handoff-e2e.py:1935-1959`).
  The whole set of `corpus/` literals in the renderer is five paths: the contract (`:118`)
  and four round-6 source ledgers (`:132-135`); `grep -n "corpus/" tools/exercise-handoff-e2e.py`
  returns exactly those five lines. `corpus/README.md` is not among them.
- The renderer performs **no directory enumeration at all**:
  `grep -n "iterdir\|glob\|listdir" tools/exercise-handoff-e2e.py` → no match. A new file
  under `corpus/knowledge/**` therefore cannot enter the read set, and the packet is
  assembled from those pinned bytes only (`v3_build_packet`, called at `:3578-3596`).
- The r7 baseline's own `inputs` census confirms it: 58 rows
  (`reports/round-34/handoff/declared-in-r7/expected.json`), whose corpus members are
  exactly `corpus/knowledge/synthesis/worldbible-integration-contract.md` and
  `corpus/lessons/round-6-sources/{03,05,09,13}.json`.

Empirical (isolated copy at 4a7aede):

- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --freeze .probe/refreeze` → exit 0,
  `packet_sha256: 45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` — equal to
  the pinned r7 packet digest; `freeze.txt` line: `no tracked value changed since the previous freeze`.
- Then, in that copy only, I added **synthetic probes** shaped like claim C's landing —
  6 files under `corpus/knowledge/culture-material/` and 4 under `corpus/knowledge/myth-symbol/`
  (live census after the probe: `myth-symbol 23`, `culture-material 24`, i.e. C's declared
  after-state) plus one appended `corpus/README.md` revision line — and re-froze into the
  same dir: exit 0, diff line again `no tracked value changed since the previous freeze`.
- Comparing the re-frozen `expected.json` with the pinned r7 baseline: `inputs` equal (58/58),
  `packet_sha256` equal, `twin_sha256` equal, `baseline_digest` equal, **0 differing
  top-level keys**.
- The re-freeze also re-runs its refusal legs against the mutated tree and stays green:
  gate exit 0 / fields 16/16 / glossary 20 / findings 0; uncertainty exit 0; links 105/105.
- Caveat, stated rather than glossed: the probe files are synthetic (I did not have C01-C10's
  drafts). The structural argument above makes the result independent of entry content, so
  the real entries behave identically as long as they land under `corpus/knowledge/**` and the
  README delta stays in `corpus/README.md`.

## 2. The renderer edit (claim O) is read-set-neutral for the r7 baseline

- The tool is **not in its own read set**: the 58 `inputs` rows name no
  `tools/exercise-handoff-e2e.py`; `TOOLS` is the five assembler/gate tools (`:139-145`) and the
  harness pair (`:180`). The baseline records no digest of the tool itself (`frozen_by` is a
  string, `:4014`; `frozen_at` at `:4013`).
- Combined probe (C and O together): with the probe corpus files already in place, I appended a
  byte-change to the isolated copy's renderer and re-ran the r7 default chain →
  `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4
  v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`.
- So claim O's regression threshold ("the r7 default chain still exits 0") and claim C's landing
  are not in tension, and the A block's r7-packet/PROVINCE surfaces (audit-only, writes confined to
  `reports/round-35/**`) touch no read-set byte either. **No claim in this round can move a member
  of the frozen read set.**

## 3. R34-N1 reproduced live — plus an acceptance-surface defect in the claim's own control

Reproduced in the isolated copy with the claim's exact command
(`--profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json`):

- exit **1**, **stdout 0 bytes**, stderr a Python traceback, `KeyError:
  'reports/round-20/handoff/claims-map.md'` at `tools/exercise-handoff-e2e.py:3822`.
- Mechanism, exactly: `drifted = [rel for rel, digest in baseline["inputs"].items() if
  assembly.digests.get(rel) != digest]` (`:3820`) — the r6-only member yields `None`, so `drifted`
  is non-empty; the *reporting* line `:3822` then indexes `assembly.digests[rel]`, which the current
  read set does not hold, so the KeyError fires **before** the designed `Failed("E2E-DIGEST", …)`
  at `:3823`. The refusal is correct; the mechanism is not, and it violates the tool's own
  documented contract — *"Exit codes (stable messages, no traceback)"* (`:90-94`).
- The r6↔r7 read-set delta is exactly one member each way (import probe of the module):
  `r6 inputs − V3_READ_SET = ['reports/round-20/handoff/claims-map.md']`;
  `V3_READ_SET − r6 inputs = ['reports/round-34/handoff/declared-in-r7/claims-map.md']`.

**Finding R08-F1 (owner: O block / O08 / S04 — acceptance leg).** The exit code cannot
discriminate the defect from the fix: the KeyError path already exits 1, and `EXIT_FAIL = 1`
(`:113`) is the fixed path's code. And under the claim's own `--quiet` command the named
diagnostic is **not printable**: `main` prints the detail line only under `if err and not
args.quiet` (`:4603`), and the unconditional summary line (`:4595`) carries exit/fields/glossary/
findings/links/claims/statuses/v2_subset/alias/packet_sha256 — no path. A validation leg keyed on
"stdout contains the diagnostic naming the member" will therefore **fail on the fixed tool** if it
uses `--quiet`. Recommended surfaces: `--json` (records are emitted unconditionally, `:4605-4608`,
and the failed `input-digest` record's `detail` names the member) or the non-quiet run
(`:4603`). Precedent for reading the summary line as the machine surface: r34's runner leg
`D5-quiet` parses `packet_sha256=` out of it (`reports/round-34/run-validation.py:180-182`).

*Refined after `reports/round-35/op/O08-validation-legs.md` landed (§2 O1):* that leg keeps the
`--quiet` command and requires the token `E2E-READSET` **and** the literal member path on one line
of `stdout + stderr` combined. That is satisfiable only if the patch prints the diagnostic on a
surface that survives `--quiet` — the current code prints the records loop only under
`if not args.quiet` (`:4579-4581`) and the detail line only at `:4603`, so a patch that merely
stops the crash and mirrors the existing gated reporting will **fail O08's O1 leg** while passing
claim O's letter. O01's patch must therefore emit the diagnostic unconditionally (or the leg must
move to `--json`); the two artifacts must agree on this surface, and O02's control for the
superseded-row refusal should assert it under `--quiet` for the same reason.

**Finding R08-F2 (owner: O01 scope decision / integrator).** The identical shape exists in the v1
path at `tools/exercise-handoff-e2e.py:1440` (`v1_exercise`'s drifted loop). Today it is *latent*
only: the v1 baseline's `inputs` equal `V1_READ_SET` exactly (empty set-diff both ways, import
probe), so no v1 replay can reach it. The patch should either mirror the fix there or route the v1
twin explicitly as a named finding — otherwise the class is half-closed.

## 4. C × A sequencing: the README delta and the round-33 census readings

- Round-33's filed adjacency audit recorded `corpus/README.md` at
  `readme_sha256 053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c` with the
  census 201 and footer `201 / 21-19-18-29-20-94`
  (`reports/round-33/adj/A05-corpus.md:15,202`; re-run identical at
  `reports/round-33/adj/A12-verify-a04-a06.md:43`). I measured the same digest at HEAD
  (`sha256sum corpus/README.md` → `053966a2…d57c`), so that reading is still live at the baseline.
- Claim C's landing moves rows/totals/footer, so `053966a2…` stops being the live digest and the
  live census reads 211.

**Finding R08-F3 (owner: A06/A07 + integrator).** A-block readings that cite 201 or
`053966a2…` must be stamped with the revision they measured (or re-measured to 211 / a new digest
after C lands). Comparing the post-C tree against round-33's digest *as if live* would manufacture a
false finding. The README's own convention supports this: superseded readings are preserved as
dated readings, not rewritten (`corpus/README.md:20-28`).

*Refined after the A block landed:* the risk is largely already handled and can be downgraded —
`reports/round-35/adj/A06-province.md:43` reads the live census 201 and explicitly stamps it "==
the claim-C before-state, `reports/round-35/claims.json:26-27`", and
`reports/round-35/adj/A07-verify.md:47` does the same in its PROVINCE row. No A-block artifact pins
`053966a2…` at all (`grep -rn "053966a2\|201 files\|readme_sha256" reports/round-35/adj/*.md
reports/round-35/scribe/S03-a-receipt.md` → no match). Residual, for the receipts: A09/S03 and the
round receipt must not restate 201 as a *post-landing* reading, and any A-block re-run after C lands
must expect 211 / a new README digest.

- Delta completeness for C11/the integrator — the existing instrument checks four surfaces
  together (`reports/round-28/readme/sweep.py:161-193`: rows vs files, missing/ghosts, topic
  byte-equality, header drift, totals line, footer total **and** footer dir vector). So the C
  landing must move all four: the 10 rows; the section headers `## culture-material/ (18)` →
  `(24)` and `## myth-symbol/ (19)` → `(23)` (`corpus/README.md:147,169`); the totals line
  (201 → 211); and the counts footer block `(total 211 files; directory totals 21/23/24/29/20/94)`
  (`corpus/README.md:471-473`, vector order linguistics/myth-symbol/culture-material/synthesis/
  verification/civilizations). New rows must carry the entry's own `- topic:` text byte-equal
  (the sweep's `topic_mismatch` leg).

## 5. Pre-existing observation (NOT a round-35 harm): the v1 default chain is red at baseline

- Isolated run of the v1 default chain (`python3 -B tools/exercise-handoff-e2e.py`):
  exit 1, `FAIL input-digest: tools/d2-typed-labels.py: frozen 0da0015f7003… live 2819f68769df…`.
- This is filed and old, not caused by C/O/A: `reports/round-20/handoff/v3.md:146-152` records the
  v1 default run as "the one remaining claim-D failure at this stamp" and `:153` names rev 1's
  baseline superseded; `git log -- tools/d2-typed-labels.py` shows its last move in `0e81d9d`
  (round 22). C adds only corpus files outside `V1_READ_SET`; O patches a tool that is outside it
  too (v1 set-diff empty both ways).

**Finding R08-F4 (owner: validation-leg spec — S04/O08).** Do not add a `--profile v1` default leg
to `reports/round-35/run-validation.py`: it is red before any round-35 landing, so it would fail the
round for a pre-existing, filed-superseded condition. r34's runner used only the v3 quiet leg
(`reports/round-34/run-validation.py:180`).

## Findings summary

| id | finding | severity | owner |
|---|---|---|---|
| R08-F1 | claim O's own control surface (`--quiet`) cannot display the named diagnostic; exit code cannot discriminate defect from fix | medium (acceptance-leg design) | O block / O08 / S04 |
| R08-F2 | twin KeyError shape at `:1440` (v1 path), latent today | low | O01 / integrator (route or mirror) |
| R08-F3 | A-block census/digest readings vs C's README landing must be revision-stamped — **downgraded: A06/A07 already stamp 201 as the before-state; residual is the receipts** | low (was medium) | A09/S03 + integrator |
| R08-F4 | v1 default chain red at baseline (filed supersession, r20) | low | validation-leg spec (S04/O08) |
| R08-F5 | `repin.json:12` pins the live renderer sha `34c85f57…`; the O patch makes that pin stale | medium (filed-byte discipline) | A01/A05/A09/A11 + integrator |

No claim in this round is blocked by these; R08-F1/F2/F5 change how the acceptance leg is written
and where the post-patch digest is filed, not whether the claims can verify.

**R08-F5 detail (cross-claim, C/O/A).** `sha256sum tools/exercise-handoff-e2e.py` at HEAD →
`34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9`, byte-equal to
`reports/round-34/handoff/repin.json:12` (`surface_sha256_after`). The moment claim O's patch lands,
that pinned value describes a superseded surface. The correct move is the repin's own precedent —
a **new row** in a round-35 record (`repin.json:41-47`, "earlier baselines are named superseded,
never rewritten") — never an edit of the filed `reports/round-34/**` bytes. The A block's audit of
that row (A01, and A05/A09/A11 as re-readers) must read the pin as pre-patch, and the O receipt must
carry the post-patch digest. This is the one place where the round's three claims genuinely
interlock: C's landing is freeze-neutral (§1), O's patch is freeze-neutral but *not* pin-neutral
(here), and A owns the surface where that shows up.

## 6. Limits and fences

- Probe corpus files and the renderer byte-change are synthetic stand-ins, never presented as the C
  block's entries or O01's patch.
- At the time §1-§5 were measured, the C01-C10 drafts, O01's patch bytes and X00's collision matrix
  did not exist; §7 records what changed once peers landed. The structural argument in §1-§2 does not
  depend on any of them.
- Live commands ran in `.scratch/r08-iso`, `.scratch/r08-iso2` (git-archive copies at 4a7aede). Both
  copies were deleted after the run; the two probe artifacts that carry the §1 result are kept at
  `.scratch/r08-probe-evidence/{refreeze-after-probe.freeze.txt,refreeze-after-probe.expected.json}`
  together with the r6 replay's split streams (`r6-replay.stdout.txt` = 0 bytes,
  `r6-replay.stderr.txt` = the traceback). Nothing under `reports/round-1..34/**` was modified; the
  probe freeze wrote only inside the copy.

## 7. Reconciliation with the fragments that landed after §1-§6

- **X00 (`cross/X00-connector.md`)** — same membership conclusion reached independently (§1: one
  `corpus/knowledge` member, the read set is a literal tuple, no glob), and the same O-1 verdict (the
  renderer is not a read-set member). X00 states explicitly it ran **no `--freeze` anywhere**; my §1
  is the direct re-freeze experiment for the same question, and it agrees. Two X00 rows extend my
  §2/§3 and should be read with them: **O-2** (the `repin.json:12` stale pin — my R08-F5 confirms it
  against live bytes) and **O-5** (bare `--selftest` defaults to `--profile v1`, so claim O's
  counting command as written measures the v1 suite: `:4485`, `:4525-4527`). X00 §3's census — five
  filed superseded rows carry the R34-N1 class, r7 the only clean row — is the class-level extent of
  the instance I reproduce in §3.
- **O08 (`op/O08-validation-legs.md`)** — O1 keeps the `--quiet` command and demands the token +
  member path on one combined-output line; see the refinement under R08-F1. O08 §1 O2 already
  switches the selftest leg to `--profile v3` (40 result lines pre-patch), which matches my measured
  count and closes X00's O-5 trap on the leg side.
- **K03 (`scout/K03-keyerror-path.md`)** — independently locates the same defect line `:3822`, the
  same mechanism, and the same v1 mirror (`:1436-1441`), confirming R08-F2 without coordination.
- **A06/A07** — both read the census as 201 and stamp it as the claim-C before-state
  (`adj/A06-province.md:43`, `adj/A07-verify.md:47`); see the downgrade under R08-F3.

## Owed

- `reports/round-35/op/O01-patch-draft.md` — absent at this stamp. R08-F1/F2 are stated as
  constraints on that patch (the `--quiet`-surviving diagnostic surface; the v1 twin at `:1440`),
  and the integrator should re-check them against the landed patch bytes.
- Reconciliation of R08-F5 against whatever row A01/A09/A11 files for the post-patch renderer digest.
- `reports/round-35/cov/C01,C04,C07,C08,C09,C10-entry-*.md` — six of the ten entry drafts were absent
  at this stamp; §1's structural argument makes the freeze verdict independent of their content, so
  this is a completeness note, not a blocker.

## Citations

- `tools/exercise-handoff-e2e.py:118,132-135` (the five `corpus/` literals), `:139-145` (`TOOLS`),
  `:180` (`HARNESS`), `:184` (`CLAIMS_MAP`), `:1935-1959` (`V3_READ_SET`), `:1933-1934`
  (v3 default pair), `:3479-3483` (digests built only from `V3_READ_SET`), `:3579-3596`
  (`v3_build_packet`), `:3820-3823` (drifted detection + KeyError site), `:1440` (v1 twin),
  `:90-94` (documented exit-code/no-traceback contract), `:112-114` (`EXIT_*`), `:4485,4525-4527`
  (profile/selftest dispatch), `:4579-4581` (records loop gated by `--quiet`), `:4594-4600` (summary
  line), `:4603` (gated diagnostic), `:4605-4608` (`--json` records).
- `reports/round-34/handoff/declared-in-r7/expected.json` (58 `inputs`; `packet_sha256`,
  `twin_sha256`, `baseline_digest`), `reports/round-30/handoff/declared-in-r6/expected.json`
  (r6 `inputs`, incl. `reports/round-20/handoff/claims-map.md`).
- Commands (isolated copies): `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` →
  exit 0, packet sha `45f57132…`; `… --profile v3 --quiet --baseline
  reports/round-30/handoff/declared-in-r6/expected.json` → exit 1, stdout 0 bytes, KeyError at
  `:3822`; `… --profile v3 --freeze .probe/refreeze` before and after the synthetic corpus probes →
  exit 0 both times, `no tracked value changed since the previous freeze`; `… --profile v3 --selftest`
  → exit 0, 40 control lines; `python3 -B tools/exercise-handoff-e2e.py` (v1 default) → exit 1,
  `tools/d2-typed-labels.py` drifted; import probe printing `r6 inputs − V3_READ_SET`,
  `V3_READ_SET − r6 inputs`, and `V1` set-diffs.
- `sha256sum corpus/README.md` → `053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`
  (equal to `reports/round-33/adj/A05-corpus.md:15,202`); `corpus/README.md:20-28,147,169,471-473`;
  `reports/round-28/readme/sweep.py:161-193`.
- `reports/round-20/handoff/v3.md:146-153` (filed v1-supersession record);
  `git log --oneline -5 -- tools/d2-typed-labels.py` (`0e81d9d` round-22);
  `reports/round-34/run-validation.py:180-182` (D5-quiet leg); `reports/round-34/handoff/repin.json`
  (`:11-12` the before/after renderer shas, `:41-47` the supersede-never-rewrite precedent,
  `R34-D-stale-row` control naming the same KeyError; `R34-N1` routed).
- `sha256sum tools/exercise-handoff-e2e.py` → `34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9`
  == `reports/round-34/handoff/repin.json:12` (R08-F5).
- Peer fragments read for §6: `reports/round-35/cross/X00-connector.md` (§1, O-1, O-2, O-5, §3),
  `reports/round-35/op/O08-validation-legs.md` (§1 O1/O2, §3), `reports/round-35/scout/K03-keyerror-path.md`
  (`:48-53`), `reports/round-35/adj/A06-province.md:43`, `reports/round-35/adj/A07-verify.md:47`;
  `grep -rn "053966a2\|201 files\|readme_sha256" reports/round-35/adj/*.md reports/round-35/scribe/S03-a-receipt.md`
  → no match.
