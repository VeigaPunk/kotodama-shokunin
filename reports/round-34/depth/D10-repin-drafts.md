- Seat: D10 | executor | claim D | date 2026-10-19 | baseline da68a6d | revision 2 (supersedes this file's first draft after K02's census landed mid-run)

# D10 — Re-pin cascade: the exact edit set, per surface, with a measured simulation

Writes: this file only. No shared file was edited, no filed round byte written, no
`reports/round-*/run-validation.py` executed in-tree (shared rule, F-C13-1).
Every command ran with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`
from `/home/vgpnk/Projects/shokunin/kotodama-shokunin` at HEAD
`da68a6d705e41f369f21e8607bfaab5b54077f84` (`git rev-parse HEAD`;
`git status --porcelain` → `?? reports/round-34/`).

**Dependency note.** K02's census (`reports/round-34/scout/K02-repin-census.md`)
did not exist at my first measuring stamp; I ran an independent census, then K02
landed mid-run and I reconciled against it (§1). Everything below is either
measured by me on the live bytes or cited to K02's row where K02 is the
authority; K02 and I agree on the headline and differ only in coverage (§1.3).

## 1. Census — the surfaces that pin the r6 pair, reconciled

### 1.1 Agreement

Both censuses agree: in the durable tree the pair is pinned **only** by
`tools/exercise-handoff-e2e.py:1933-1934`; every other occurrence of
`declared-in-r6` is a filed row, a ledger row, this round's own declaration, or
scratch (K02 §A/§C/§D/§F; my §1.2 rows 1-2, 8-21). K02's four measured negatives
match mine: `corpus/**`, `examples/**`, `tools/gates/**` (incl.
`tools/gates/expected/` → five gate dirs, no handoff row) and
`tools/check-gate-battery.py` carry no pin of the pair (K02 §E3-E7, E9-E10; my
`grep -rn "declared-in" tools/` → lines 38, 39, 1933, 1934 only).

### 1.2 Surfaces K02 found that my first census missed (now folded in)

| # | surface | path:line | pin kind | action |
|---|---|---|---|---|
| K1 | `v3_exercise` signature default | `tools/exercise-handoff-e2e.py:3806` | consumer of A1 (default arg) | no edit; follows the constant |
| K2 | `--baseline` override flag | `tools/exercise-handoff-e2e.py:4488` | **not a pin** — the documented escape hatch to bind a superseded row explicitly | no edit; used by control C2 below |
| K3 | selftest subprocess runs the CLI with `--root <fixture>` and **no** `--baseline` | `tools/exercise-handoff-e2e.py:4183-4189` | coupling proof | **A1 and A2 must move together** or the isolation leg goes red (K02 §B-coupling) |
| K4 | filed runners read the default **live** from the tool source by regex | `reports/round-27/run-validation.py:1388-1389`, `reports/round-28/run-validation.py:1348-1349` | filed readers of a live constant | never edited; after the move an *isolated* re-run records `v3_baseline_default.path` = r7 while the filed receipt shows the old path. **"verdict-stable, reading-changed"** — the round-34 record must state which reading it produced (K02 §C14-C16) |
| K5 | filed receipts that pin the *default chain's* recorded field | `reports/round-27/validation.json`, `reports/round-28/validation.json` (`/claims/O/measurement/v3_baseline_default.path`, `v3_replay.default_baseline`) | filed record | never edited; historical readings |
| K6 | fleet-root prose + manifest | `../.ufo/reports/round-30/kotodama.md:14-18`; `../MANIFEST.json` (`grep -c "declared-in-r6\|6ced88ad"` → **0**) | outside the lane repo, read-only | a new fleet report for round 34; the round-34 `MANIFEST.json` bookkeeping entry is not a pin (K02 §E11 resolves my earlier `to-verify`) |

### 1.3 Surfaces I found that the pin-census does **not** answer (the cascade's real depth)

K02's census enumerates surfaces that pin the **r6 pair**. It does not enumerate
surfaces that pin the **r6 packet's stale prose** — and those are the cascade
steps that decide whether claim D's `after_required` ("every claim-ledger/OQ
number equal to a measured live value") can be met. Measured (§3, §5):

| # | stale-prose source | path:line | live-file edit required? |
|---|---|---|---|
| S1 | the two v3 default constants | `tools/exercise-handoff-e2e.py:1933-1934` | **yes** — Draft A |
| S2 | `CLAIMS_MAP` (the D4 ledger source) | `tools/exercise-handoff-e2e.py:184` | **yes** — Draft B1, plus a successor map file (§4) |
| S3 | scope cell, "twelve authored components" | `tools/exercise-handoff-e2e.py:2779` | **yes** — Draft B2 (live count 13: `ls examples/culture-d4/components/*.yml \| wc -l` → `13`) |
| S4 | `OQ-V3-05` question text, hard-coded | `tools/exercise-handoff-e2e.py:3526-3527` | **yes** — Draft B3 |
| S5 | D4 row statements **and** bases (CL01 "twelve authored inputs/components", CL05 74/56/16/15, CL06 hold 15 note 1 / three D2L-RANK rows / +9 hold, CL07 conflicts 4, CL08 "50/50", CL09 13/3/4) | contents of `reports/round-20/handoff/claims-map.md` (filed, in the read set as `CLAIMS_MAP`) | **yes, but not by editing that file** — a successor map (§4); D03 measured the same rows (`reports/round-34/depth/D03-ledger-rows.md:66-75,88,94,110`) |

Measured negative that matters: the packet's *other* numbers are already live —
`A-11` / `:284` / `OQ-V2-03` carry the **D2** channel's numbers (`58` labels,
`16` findings, `13` unresolved rank items, `3` quarantine handles, `4` conflicts,
`46/10/2` by kind), and those are exactly the live
`examples/culture-d2/typed-labels.d2.yml` coverage values I re-read
(`conflicts 4`, `findings_total 16`, `native-form 46`, `translated-label 10`,
`borrowed-strata 2`, `rank_quarantine_handles 3`). **They must not be "fixed".**
A naive tree-wide stale-token sweep flags them; the sweep has to be scoped to the
D4 region (my §5 probe initially mis-flagged them, and the scope is recorded
here so the integrator does not repeat it).

## 2. Draft A — the renderer defaults (integrator applies; DRAFT ONLY)

Shared file: `tools/exercise-handoff-e2e.py` (4612 lines,
`sha256 a5e4a8c5dda9d63c177a3dce75a8716ba5d285371d0a37a2535f6c323e7619df`).

**Before** (byte-exact, `sed -n '1933,1934p'`; one space before `=`):

```
V3_BASELINE_DEFAULT = "reports/round-30/handoff/declared-in-r6/expected.json"
V3_FROZEN_DIR_DEFAULT = "reports/round-30/handoff/declared-in-r6"
```

**After:**

```
V3_BASELINE_DEFAULT = "reports/round-34/handoff/declared-in-r7/expected.json"
V3_FROZEN_DIR_DEFAULT = "reports/round-34/handoff/declared-in-r7"
```

Binding notes:

- **Move both lines or neither** (K02 §B-coupling: the selftest re-runs the CLI
  against the temp fixture with no `--baseline`, so a one-sided move reddens the
  isolation leg).
- Nothing else in `tools/` needs this path (`grep -rn
  "declared-in-r6\|round-30/handoff" --include=*.py .` → only these two lines).
- `V3_PACKET_VERSION` stays `3.1.1`: every revision r2…r6 carries `3.1.1`
  (`reports/round-30/handoff/declared-in-r6/expected.json` → `"packet_version":
  "3.1.1"`), the constant is shared by all revisions, and a bump would change the
  provenance cell of every future packet. A bump is a separate decision —
  `to-verify` with P01/D01.

## 3. Draft B — the three further tool edits (the stale-prose fixes)

### B1 — the ledger source constant (`:184`)

**Before** (`grep -n "^CLAIMS_MAP" tools/exercise-handoff-e2e.py` → `184`):

```
CLAIMS_MAP = "reports/round-20/handoff/claims-map.md"
```

**After** (successor path; bytes owed to D03/D05, §4):

```
CLAIMS_MAP = "reports/round-34/handoff/claims-map-r34.md"
```

Why a successor and not an edit: `reports/round-20/**` is a filed round; the file
is also a read-set member, so its digest is pinned by the new baseline row's
`inputs{}` and named in the packet's own manifest (`A-57`) and intro
(`tools/exercise-handoff-e2e.py:2934` renders `{CLAIMS_MAP}` — the intro follows
the constant automatically). Both `A-57` and the intro line change with this one
edit; measured in §5.

### B2 — the scope cell's hard-coded word (`:2779`)

**Before** (`sed -n '2779p'`):

```
        f"{counts['contact']} contact layers, twelve authored components); all native spellings are "
```

**After:**

```
        f"{counts['contact']} contact layers, thirteen authored components); all native spellings are "
```

Live count: `ls examples/culture-d4/components/*.yml | wc -l` → `13`; D03
independently measured 13 registry rows / 13 component files / 13 assembly pins
(`reports/round-34/depth/D03-ledger-rows.md:70` rows 9-10).

### B3 — the `OQ-V3-05` question text (`:3526-3527`)

**Before** (byte text of the two source lines):

```
                    "D4's inherited and own holds stay open: twelve form holds + three rank holds + one "
                    "note, thirteen unresolved rank items, three quarantine handles and four conflicts — "
```

**After** (live numbers; wording to be reconciled with D03's drafted row
`reports/round-34/depth/D03-ledger-rows.md:116` — treat the text below as the
draft, not the delivered bytes):

```
                    "D4's holds stay open on the six garment terms: twelve form holds and zero rank holds, "
                    "with zero notes, zero unresolved rank items, zero quarantine handles and zero conflicts — "
```

Live basis: `examples/culture-d4/expected-holds.json` → `counts {hold 12, note 0,
fail 0}`, all 12 rows `D2L-FORM-UNRESOLVED`; `examples/culture-d4/typed-labels.d4.yml`
coverage → `rank_rules_unresolved_items 0`, `rank_quarantine_handles 0`,
`conflicts 0`.

Not to be touched: `OQ-V3-04` and `OQ-V3-06` carry no numbers; the v2 OQ rows are
parsed from the filed v2 twin (`v3_load_v2_rows`, `tools/exercise-handoff-e2e.py:2261`)
and their D2 numbers are live (§1.3).

## 4. Draft C — the successor claims-map (new row; bytes owned by D03/D05)

Shape contract, read from the parser (`v3_parse_claims_map`,
`tools/exercise-handoff-e2e.py:2289-2320`): the file must carry exactly **12**
rows matching `D4_ROW_RE = re.compile(r"^### (D4-CL\d\d) — (.+?) — (.+?) — `([a-z]+)`\s*$", re.M)`
(`:2286`), each row body carrying `- **statement:**`, `- **u.basis:**` and
`- **links:**` bullets (links as backticked specs); a 13th or missing row raises
`ArtifactError`. Otherwise the packet seat re-declares the ledger source and the
render refuses — the successor is not a free-form rewrite.

**Stale-token target list (measured, D4 region only — the D2 tokens in §1.3 are
live and must survive):**

| token | where in the filed map | live value / source |
|---|---|---|
| `typed_labels 74`, `native-form 56`, `findings_total 16, findings_hold_or_fail 15`, `labels 74` | D4-CL05 basis+statement (map `:104`; packet `:148`) | `82`, `64`, `12, 12`, `82` — `examples/culture-d4/typed-labels.d4.yml` coverage `:31-46` and stats `{fail 0, hold 12, labels 82}` |
| `hold 15, note 1, fail 0`, "three D2L-RANK rows, plus one D2L-RANK note", `+9 hold delta` | D4-CL06 basis+statement (map `:116`; packet `:149`) | `hold 12, note 0, fail 0`; zero rank rows, zero notes; `+6 hold / +0 note` — `examples/culture-d4/expected-holds.json` `counts` + `holds` (12 rows, all `D2L-FORM-UNRESOLVED`) |
| `conflicts 4`, `quarantine handles 3` | D4-CL07 row (map ~`:124`; packet `:150`) | `0`, `0` — live coverage block |
| `exit 0 50/50` | D4-CL08 basis (map ~`:138`; packet `:151`) | `163/163` — `tools/d2-typed-labels.py --selftest` (D03 §2 row 8) |
| `rank_rules_unresolved_items 13`, `rank_quarantine_handles 3`, `conflicts 4` | D4-CL09 basis+statement (map `:158`; packet `:152`) | `0`, `0`, `0` |
| `twelve authored inputs` / `twelve authored components` | D4-CL01 statement (map `:57`) **and** basis (wrapped text, map `:62` region) | `thirteen` — 13 component files, measured |
| `OQ-V3-05`'s `12 + 3 + 1 / 13 / 3 / 4` | **not** in the map — tool hard-code (§3 B3) | `12 + 0 + 0 / 0 / 0 / 0` |

**Sweep instruction (from the measured probe, §5):** the stale tokens sit in row
**statements as well as bases** — my probe rewrote three bases and still left
`+9 hold`, `four conflicts` and `twelve authored` because those live in
statements/wrapped lines. The successor must be swept token-by-token across both
bullets of all 12 rows, then re-swept on the *rendered* packet (§5 method).

## 5. Measured simulation — what each edit stage actually produces

Method: the tool source was patched **in memory** (`exec` of the modified text,
`__name__="e2e_sim"`), never written; the map successor lived in
`.scratch/d10/claims-map-r34.md` (scratch, out of the durable tree). Assemblies
ran in-process via `V3Assembly(ROOT)`; the gate ran on its own isolated copy.

| state | edits applied | assembled packet sha256 | residual D4-region stale tokens |
|---|---|---|---|
| **S1** filed r6 | none | `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb` (= `freeze.txt:2`) | the full stale set (`:20`, `:144`, `:148-152`, `:307`) |
| **S1′** live default, no edits | none | **byte-identical to S1** (`live_render_equals_filed_r6: true`) — the current tree reproduces the r6 packet exactly | same |
| **S2** Draft A + B2 + B3 (filed map kept) | 3 of 4 tool sites | `d453c107b18faf3c8ef1d8be8e2abd959343049bfcb6c05c68a083c6133a0bd6` | **16** map-sourced tokens remain (`typed_labels 74`, `hold 15`, `50/50`, …) — **the successor map is required; the tool edits alone do not close claim D** |
| **S3** S2 + Draft B1 + a probe successor map (D03's drafted CL05/CL06/CL09 rows + token substitutions) | 4 of 4 tool sites + successor map | `fd8330dfc37a4e28f7e70199bb85cbeb892345dc7d89ddec07e04385b74ca9e2` (twin `9f017c43370173c534a47b45077b65265cb604d2052c9e1695260a08b7e2d9a1`) — **provisional**: my probe wording is not D05's final map | `+9 hold`, `four conflicts`, `twelve authored` — exactly the statement/wrapped-line residue §4 warns about |

S3's changed-line map versus the filed r6 packet (unified diff, `n=0`), i.e. the
cascade's full blast radius when the successor map is done:

```
@@ -20 +20 @@      scope cell                     twelve -> thirteen authored components
@@ -95 +95 @@      manifest row A-57              claims-map path + digest
@@ -113 +113 @@    read-set bullet                claims-map path + digest
@@ -125 +125 @@    intro sentence                 "carried from {CLAIMS_MAP}"
@@ -144 +144 @@    D4-CL01 row
@@ -148,5 +148,5 @@ D4-CL05..CL09 rows
@@ -295 +295 @@    baseline provenance line       r6 -> r7 path (§6)
@@ -307 +307 @@    OQ-V3-05
```

Consequences for the freeze: the new row's `packet_sha256` is whatever the final
map bytes produce — `fd8330df…` is a *probe*, not a prediction to be trusted; the
freeze measures it. The **line map above is stable** (any successor map wording
changes the digest, not the changed-line set, as long as the same cells are
rewritten).

**Two independent cross-checks that the D4-prose staleness is real and is the
same class claim D names:**

1. The filed r6 row's own counts already disagree with its own prose:
   `reports/round-30/handoff/declared-in-r6/expected.json` `counts` →
   `d4_typed_labels 82`, `d4_holds 12`, while `packet.md:148` says `typed_labels 74`
   and `:149` says `hold 15, note 1`. Same file, two readings.
2. S1′ shows the live render reproduces the filed packet **byte for byte**, so
   nothing in the read set drifted; the stale prose is carried, not computed. A
   "re-render" is not a fix — only the four tool sites plus the successor map are.

## 6. Freeze order — the self-referential constraint (measured)

The renderer writes the live default path into the packet body
(`tools/exercise-handoff-e2e.py:3185`; in the filed packet at
`reports/round-30/handoff/declared-in-r6/packet.md:295`). Measured effect of the
re-point alone, with every other byte held fixed:

```
diff (filed r6 packet vs constant re-pointed to r7): one hunk, @@ -295 +295 @@, one changed line
  - … compared against the frozen baseline in `reports/round-30/handoff/declared-in-r6/expected.json` …
  + … compared against the frozen baseline in `reports/round-34/handoff/declared-in-r7/expected.json` …
packet_sha256 6ced88ad… -> 548940b14b8413edfe293d0cc72f32a3e76d14c12cf7787f09c5cf6553400a58
```

Required order:

1. land Draft A (+ B1/B2/B3 as decided) with the successor map bytes in place;
2. `python3 tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-34/handoff/declared-in-r7`;
3. verify the frozen pair: `freeze.txt:2-3` equal to the on-disk `packet.md` /
   `twin.json`, and the packet's `:295` line naming the **r7** path;
4. `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0;
5. `python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md` → exit 0.

Why this order: round-27's filed narrative
(`reports/round-27/pinsweep/sweep.md:258-266`) records that freezing before the
re-point forced a second freeze ("The first freeze (`a2b2a5fc…`) was taken before
the re-point and therefore no longer matches what the tool assembles"); round-26's
SCORECARD row states the same rule. Round 30 hit the trap too — its
`freeze.txt:8` carries `re-frozen packet_sha256: ec30b11f12accfa4c43e24a36e53fca858eddb07… -> 6ced88ad009f1cfc94f7fc9e5656555f7da6682c…`.
Expected r7 signature: one `froze …` line whose digests equal the bytes on disk.

`v3_freeze` refuses to write a row whose own gate/semantics are red
(`tools/exercise-handoff-e2e.py:3988-4005`: `E2E-GATE`, `E2E-SCAN`, `E2E-UNC`,
`E2E-LINK`) — so a frozen row is green by construction, and the independent replay
in step 4 is still owed.

## 7. Controls — measured, and what remains `to-verify`

| # | control | command | result | status |
|---|---|---|---|---|
| C1 | pre-state: the default chain is green and the r6 row replays green *before* the move | `v3_exercise(root=ROOT, baseline_rel=<live default>)` and `baseline_rel=<r6 row>` (in-process) | both **exit 0**, `frozen-packet` = `packet sha256 6ced88ad…` | **measured** (§5 S1′) |
| C2 | the superseded row refuses its own replayer *after* the move | same call with the constant patched to r7, `baseline_rel` = the r6 row | **exit 1**, code **`E2E-DIGEST`**, leg `frozen-packet`: `assembled 548940b14b84… vs frozen 6ced88ad009f…` | **measured (simulated)** — the simulation is in-memory; the final confirmation runs against the real applied edit |
| C3 | the successor row replays green | `--profile v3 --quiet --baseline reports/round-34/handoff/declared-in-r7/expected.json` | exit 0, `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4` | `to-verify` (dir does not exist yet) |
| C4 | the default chain is green at the new row | `--profile v3 --quiet` | exit 0, `packet_sha256` == r7 `freeze.txt:2` | `to-verify` |
| C5 | filed bytes untouched | D11's git/`hash-object` evidence | 0 changed rows | D11 landed: `reports/round-34/depth/D11-preservation.md` |
| C6 | tamper control on the new row | D09's mutated-byte probe | red | `to-verify` — D09's design file was not present at my stamp |

C2's red is the **designed** signature, per the claim threshold
(`reports/round-34/claims.json:34`): "old rows replay red or are named superseded,
new rows green". Note the precise mechanism, because it is not the read-set leg:
the renderer is **not** in its own read set (`expected.json.inputs` = 58 files,
`'tools/exercise-handoff-e2e.py' in inputs` → `False`), so the red comes from the
packet digest, not from `input-digest`.

## 8. Supersession record (new row; DRAFT)

Proposed path `reports/round-34/handoff/repin.json` (precedent shapes:
`reports/round-26/remainders/pins.json`, `reports/round-27/pinsweep/d4-pins.json`,
`default-pointer` row in `reports/round-27/pinsweep/repin.py:305-334`). `‹…›`
cells are filled from measured values at landing time.

```json
{
 "schema": "kotodama-pin-repoint-v1", "round": 34, "date": "2026-10-19",
 "axis": "depth", "baseline_commit": "da68a6d",
 "kind": "re-point as a NEW row; the filed r2..r6 rows and the r28 row stay byte-identical",
 "canon": "NON-CANON engineering evidence; a pin is integrity, never truth and never clearance",
 "rows": [
  {"id": "R34-D-default-pointer",
   "surface": "tools/exercise-handoff-e2e.py:1933-1934",
   "was": "reports/round-30/handoff/declared-in-r6/{expected.json,}",
   "now": "reports/round-34/handoff/declared-in-r7/{expected.json,}",
   "surface_sha256_before": "a5e4a8c5dda9d63c177a3dce75a8716ba5d285371d0a37a2535f6c323e7619df",
   "surface_sha256_after": "‹measured after the edit›",
   "control": {"command": "python3 tools/exercise-handoff-e2e.py --profile v3 --quiet", "exit": 0}},
  {"id": "R34-D-stale-row",
   "surface": "reports/round-30/handoff/declared-in-r6/expected.json",
   "surface_sha256": "ea1e29276478477aa9e0605172723c63cd9d0b8e63e7d478896951895abda8a0",
   "stale_pin": {"packet_sha256": "6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb"},
   "control": {"command": "… --baseline reports/round-30/handoff/declared-in-r6/expected.json",
               "exit": 1, "code": "E2E-DIGEST",
               "leg": "frozen-packet: assembled <new> vs frozen 6ced88ad009f…"},
   "note": "the refusal is the control; the r6 bytes stay untouched (D11)"},
  {"id": "R34-D-new-row",
   "surface": "reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,expected.json,freeze.txt,run.log}",
   "frozen_by": "python3 tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-34/handoff/declared-in-r7",
   "digests": {"packet.md": "‹›", "twin.json": "‹›", "expected.json": "‹›", "freeze.txt": "‹›"},
   "control": {"exit": 0, "reading": "‹fields=16/16 glossary=20/20 findings=0 links=105/105 …›"}},
  {"id": "R34-D-edit-set",
   "surface": "tools/exercise-handoff-e2e.py",
   "edits": ["184 CLAIMS_MAP -> successor map", "1933-1934 default pair -> declared-in-r7",
             "2779 twelve -> thirteen authored components", "3526-3527 OQ-V3-05 -> live numbers"],
   "successor_row": "reports/round-34/handoff/claims-map-r34.md (‹digest›)",
   "limit": "a reader must not mistake the claim-map successor for a lore disposition"},
  {"id": "R34-D-history",
   "rows": ["reports/round-22/handoff/declared-in/", "reports/round-22/handoff/declared-in-r2/",
            "reports/round-25/v3-supersession/declared-in-r4/", "reports/round-26/handoff/declared-in-r5/",
            "reports/round-28/pinsweep/v3-baseline-r28/", "reports/round-30/handoff/declared-in-r6/"],
   "reading_changed_not_verdict": ["reports/round-27/run-validation.py:1388-1389",
                                   "reports/round-28/run-validation.py:1348-1349"],
   "precedent": "reports/round-29/defects/regression.md:52 — earlier baselines are named superseded, never rewritten"}
 ],
 "limits": "pins the cascade surfaces only; not canon, not lore acceptance, not round admission"
}
```

## 9. Ledger rows (append-only; integrator/parent)

`SCORECARD.md` — append a round-34 row in the existing table shape; do **not**
touch `SCORECARD.md:400` (the round-30 row). `LOG.md` — append a new section;
`LOG.md:3428` stays as filed. Drafts with the same wording pattern as their
round-30 counterparts:

```
| depth | improved (claim D) | A02-H1 closed: handoff packet declared-in-r7 built from live bytes; every D4 claim-ledger and OQ figure equals a measured live value (typed-labels 82/64/12/12, holds 12+0+0, rank residuals 0/0/0, 13 authored components); four wiring edits + a successor claims-map landed as new rows; gate 16/16 + 20/20 + findings 0; e2e --quiet exit 0 with packet_sha256 == freeze.txt; the r6 default re-pointed with the supersession record (filed r2..r6 bytes untouched) | `python3 reports/round-34/run-validation.py` | `reports/round-34/handoff/declared-in-r7/`, `reports/round-34/handoff/repin.json` |
```

```
## 2026-10-19 — Round 34 admitted (loop 1 build 2 of 3)

- **Trigger:** regimen; claims D/O/C in `reports/round-34/claims.json`; baseline
  `da68a6d`; ‹N›/64 completed; integrator dispositions post-wave.
- **D (…):** packet `declared-in-r7` built from live bytes; the r6 default
  re-pointed as a new row (`tools/exercise-handoff-e2e.py:1933-1934`) together
  with the ledger-source, scope and OQ edits; supersession record
  `reports/round-34/handoff/repin.json`; filed r2/r4/r5/r6 bytes untouched.
- **O (…):** …
- **C (…):** …
- **Evidence:** `reports/round-34/validation.json` acceptance ‹true|false›.
```

Number cells are to be replaced with the values actually observed at close time.

## 10. What I measured, and what I did not do

Measured by me at this stamp: the census (§1); the live D4/D2 values (§1.3, §3,
§4); the in-memory simulations S1′/S2/S3 with the changed-line map (§5); the
one-line re-point diff and the resulting `548940b1…` digest (§6); C1 and C2 (§7);
the r6 pair's five digests; `tools/exercise-handoff-e2e.py` = `a5e4a8c5…`, 4612
lines; `expected.json` internals (58 inputs, renderer absent, `baseline_digest
714b41fc…`); `13` D4 component files; `../MANIFEST.json` → 0 hits (via K02 §E11).

Not done: no shared file edited (the four tool edits are drafts, applied by the
integrator); no durable artifact written under `reports/round-34/handoff/`; no
freeze; no independent replay of a landed row; every "expected" cell above is
labelled `to-verify`. The S3 digest is a probe over my own substitute map wording
and must not be quoted as the r7 digest.

## Owed

- **K02's census** — landed mid-run; reconciled in §1. Remaining integrator action:
  confirm §1.3's stale-prose surfaces against D03/D05's final map, and run R02's
  second independent pass over §2-§4 (R02's mission asks for exactly this diff).
- `reports/round-34/handoff/claims-map-r34.md` — the successor map bytes (D03
  drafted the rows; D05/assembler owns the file). Until it lands, Draft B1 must
  not be applied alone: S2 shows the packet would still carry 16 stale tokens.
- `reports/round-34/depth/D09-freeze-design.md` — needed for C6's tamper probe and
  the expected `freeze.txt` line set (§6).
- `reports/round-34/plan/P01-d-plan.md` — owns the ordering decision and the
  `V3_PACKET_VERSION` question (§2).
- Applied values: the four tool sites, the final map digest, the frozen r7
  digests, and the C3/C4/C6 measurements — all integrator-side; this seat writes
  none of them.

## Citations

- `REGIMEN.md`; `reports/round-34/claims.json:24-34`; `reports/round-34/targets.json:14-15,32,66`.
- `reports/round-34/scout/K02-repin-census.md` §A (A1/A2), §B (B1-B6, coupling
  proof), §C (C1-C16), §D (D1-D4), §E (E1-E12), §F, §G, §H (H1-H5).
- `tools/exercise-handoff-e2e.py:184` (`CLAIMS_MAP`), `:25` (docstring 50/50),
  `:1925-1940` (v3 block, `V3_READ_SET`), `:2286-2320` (`D4_ROW_RE`,
  `v3_parse_claims_map`), `:2261-2285` (`v3_load_v2_rows`), `:2476-2584`
  (`v3_manifest_rows`, read-set-derived `A-nn`), `:2775-2781` (scope f-string),
  `:2934` (intro f-string), `:3185` (provenance render), `:3526-3527` (OQ-V3-05
  hard-code), `:3806` (`v3_exercise` default), `:3929-3940` (v3 `frozen-packet`
  leg, `E2E-DIGEST`), `:3978-4005` (`v3_freeze` + refusals), `:4073-4083`
  (`baseline_digest`, dir create, previous-row read), `:4146-4189` (fixture
  freeze / selftest subprocess), `:4488`, `:4561`, `:4577`.
- `reports/round-30/handoff/declared-in-r6/{packet.md:20,95,113,125,144,148-152,295,307,
  expected.json (counts 82/12, inputs 58, baseline_digest 714b41fc…), freeze.txt:2,3,8, run.log}`.
- `reports/round-20/handoff/claims-map.md:57,62,104,116,124,138,155,158` (filed; read-only).
- `examples/culture-d4/{typed-labels.d4.yml (coverage :31-46, stats), expected-holds.json (counts, 12 holds, revision_note), components/01-brief.yml}`;
  `examples/culture-d2/typed-labels.d2.yml` coverage (D2 live values).
- `reports/round-34/depth/{D03-ledger-rows.md:66-75,88,94,110,116, D11-preservation.md}`;
  `reports/round-27/pinsweep/{sweep.md:20-32,258-266, repin.py:305-334}`;
  `reports/round-26/remainders/{pins.json, pins.md:1-60}`; `reports/round-29/defects/regression.md:52`;
  `SCORECARD.md:330,400`; `LOG.md:3428`; `reports/round-31/scope.md:55`.

Commands (all 2026-10-19, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `git rev-parse HEAD`; `git status --porcelain`.
- `grep -rn "declared-in-r6\|declared-in-r7" --exclude-dir=.git --exclude-dir=.scratch --exclude-dir=out .`;
  `grep -rn "declared-in" tools/ | grep -v tools/gates/frozen`;
  `grep -rn "reports/round-30/handoff/declared-in-r6" --include=*.py --include=*.md … .`;
  `grep -rln "handoff" tools/gates/`; `ls tools/gates/expected/ tools/gates/frozen/handoff-packet-check/`.
- `grep -n "typed_labels 74\|hold 15\|…" reports/round-20/handoff/claims-map.md` plus a
  multiline Python `re.finditer` scan (line-based grep missed wrapped hits).
- `sed -n '1933,1934p' tools/exercise-handoff-e2e.py | cat -A`; `:3185`, `:3526-3527`, `:2779`, `:184`.
- `sha256sum tools/exercise-handoff-e2e.py tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/*`.
- `python3 -c "…json.load(expected.json)…"` → `58 False 714b41fc…`.
- `python3 .scratch/d10/measure.py` → `{"live_default":{"exit":0,…},"r6_row_pre_edit":{"exit":0},"patched_render_provenance_line":"… declared-in-r7/expected.json …","patched_packet_sha256":"548940b14b84…","r6_row_post_edit_simulated":{"exit":1,"code":"E2E-DIGEST","failing_legs":[{"check":"frozen-packet","detail":"assembled 548940b14b84… vs frozen 6ced88ad009f…"}]}}`.
- `python3 .scratch/d10/measure2.py` → `live_render_equals_filed_r6: true`, one-hunk diff at `@@ -295 +295 @@`.
- `python3 .scratch/d10/sim.py` and `sim2.py` → S2 sha `d453c107…` (16 residual stale tokens), S3 sha `fd8330df…`, twin `9f017c43…`, changed lines `20, 95, 113, 125, 144, 148-152, 295, 307`, residual `+9 hold / four conflicts / twelve authored`.
- `ls examples/culture-d4/components/*.yml | wc -l` → `13`.
- `ls -la reports/round-34/scout/` → exit 2 at my first stamp.
