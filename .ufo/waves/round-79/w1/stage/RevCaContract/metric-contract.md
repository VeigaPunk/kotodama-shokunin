# RevCaContract — Ca mismatch metric contract (round-79 W1 pre-data)

Seat item: *Ca mismatch metric: original discrepancy remains historical; annotation
must not assert mismatch erased.* All constants below were re-derived read-only from
committed bytes (see `probe-r79-ca-mismatch.txt` for the verbatim run).

## 1. Measured facts (constants the freeze must carry)

| field | value | evidence |
|---|---|---|
| stated (old) token | `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md` | `44f76d45:reports/round-78/telemetry/census-end.txt:33` |
| actual token | `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md` | `4b255745:corpus/SOURCES.md` S884 used-by cell; identical at `44f76d45` |
| original receipt path | `reports/round-78/telemetry/census-end.txt` | — |
| original receipt blob | `62eb55b77f44bf47c283c98c5645dd7141e98495` | `git rev-parse 44f76d45:<path>` |
| original receipt sha256 | `05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867` | `git show 44f76d45:<path> \| sha256sum` |
| measured revision (receipt) | `4b255745dea45a45d88b17e3c3fea4cdb6700cf7` | first commit carrying the blob (round-78 honest-stop lands); also the recorded round-78 revision in `corpus/lessons/round-78-verifier-spotcheck.md:4` |
| base | `44f76d456c1b326a71ffdb381590af825cbf11be` | dispatch |
| registry row | `corpus/SOURCES.md:839` (S884) | stable since `d7a38405` (round-74) |
| start-receipt control | `census-start.txt` S884 line shows `…amend-2026-10-23.md` | matches registry; the end receipt is the anomaly |
| stated token history | `git log --all -S 'worldbuilding-setting-practice.amend-2026-10-24-r13' -- corpus/SOURCES.md` → empty | token never present in registry at ANY revision |
| stated file history | `git log --all -- corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md` → empty | file never committed; on disk only `…10-23.md` and base `….md` exist |
| `r13` suffix at base | exists only as `heritage-taxonomy-models.amend-2026-10-24-r13.md` (different family, S874/S875) | the receipt token is a chimera: worldbuilding stem + heritage r13 suffix |

Routed precedent: `corpus/lessons/round-78-verifier-spotcheck.md:67` (routed defect 2) —
"the lane should diagnose and append a correcting entry in the next round (append-only)".

## 2. Metric semantics — the core finding of this seat

The claim needs **two distinct counters**, and conflating them is the erase-the-history bug:

1. **`mismatch` (historical, time-invariant).** Derived once, at base, by comparing the
   frozen receipt's stated token against the registry at the recorded round-78 revision:
   `mismatch = 1`. Both operands are immutable (append-only receipt; pinned revision), so
   this count can never change. **After the correction lands it must still read 1.**
   A counter, report or SCORECARD row that prints `mismatch=0` post-correction — without
   the `unresolved` qualifier — is asserting the discrepancy was erased and is a *lying
   correction* under the draft's failure modes.
2. **`unresolved` (live, lands-derived).** At base no correction binds the four fields →
   `unresolved = 1`. After the append-only correction lands → `unresolved = 0`.

Draft's own words support this split: "A frozen counter re-derives mismatch=1 at base
and unresolved mismatch=0 after the new correction." Two readings are only consistent
with the split: the base re-derivation pins the historical 1; the after-value names the
unresolved tail. Resolution ≠ erasure: the correction *closes* the mismatch (binds truth
to the record) — it does not delete the mismatch from history.

## 3. Correction-row contract (what the annotation must bind)

One appended row (SCORECARD `## Corrections — round 79` or a corrections file — L1's
choice), carrying all four bindings, each mechanically re-derivable at `<lands>`:

1. **original receipt digest** — path + blob `62eb55b7…` + sha256 `05b5011a…`;
2. **measured revision** — `4b255745dea45a45d88b17e3c3fea4cdb6700cf7` (receipt commit;
   registry bytes identical at base `44f76d45` for the S884 row);
3. **old token** — `…worldbuilding-setting-practice.amend-2026-10-24-r13.md`;
4. **actual token** — `…worldbuilding-setting-practice.amend-2026-10-23.md`.

Plus the re-derivation command(s) a reviewer can re-run (QUALITY 12/27 shape), e.g.:

```
git show 4b255745dea45a45d88b17e3c3fea4cdb6700cf7:corpus/SOURCES.md | grep -E '^\| S884 ' | grep -oE 'corpus/knowledge/[^ |]*worldbuilding[^ |]*'
git rev-parse 44f76d456c1b326a71ffdb381590af825cbf11be:reports/round-78/telemetry/census-end.txt
```

## 4. Failure-mode → leg mapping (for ExecCaCounter / L1)

Draft names four failures; each needs its own leg, none collapsible into "row present":

| draft failure | mechanical check (constants read at `--freeze`, graded at `--lands`, per QUALITY 25/26) |
|---|---|
| do-nothing | no correction row at `<lands>` binding the four fields → `unresolved` stays 1 → FAIL |
| lying correction | row's old/actual/digest/measured-revision values ≠ the frozen constants (re-derive each with `git show` at the named revisions) → FAIL |
| wrong revision | row names a measured revision whose registry actually carried the stated token — provably none exists (`git log --all -S` empty over `corpus/SOURCES.md`); a row naming any other revision for these bytes → FAIL |
| changed receipt | `git rev-parse <lands>:reports/round-78/telemetry/census-end.txt` ≠ `62eb55b7…` → APPENDONLY FAIL (J6 precedent: in-place receipt edit fails the leg) |

Vacuity hazard (J5 precedent — "a correction row naming only its id" fails ANNOTATE): a
row binding only id + actual token, omitting receipt digest and measured revision,
under-specifies which receipt was wrong. That is the *partial-erasure* shape: the lane
could later forget the receipt was ever wrong while the file count looks clean. The
four-field binding above is the minimum that keeps the discrepancy historical. The
counter must reject 1-field, 2-field and 3-field rows.

## 5. Annotation wording — review-only checklist (QUALITY 11)

Whether prose *asserts erasure* is a wording judgment; named review-only with this
checklist:

- FORBIDDEN post-correction framings: "mismatch erased", "mismatch corrected to 0",
  "no mismatch (S884)", any count reset of the historical 1, "receipt was correct".
- REQUIRED framing: recorded mismatch = 1 (historical, append-only); unresolved = 0
  after the correction; the receipt's stated token was wrong at capture time and the
  correction binds the truth without rewriting the receipt.
- The row may note the chimera diagnosis (worldbuilding stem + heritage `r13` suffix
  that exists only under `heritage-taxonomy-models.*`, S874/S875) — observed evidence,
  useful for the lesson's `## Corrections` — but diagnosis is not a binding field.

## 6. Disposition observation (supports L1; not my bounded item)

The CLAIMS-DRAFT sizing rule requires mismatches in *SCORECARD/SHONEN self-assessment*.
Observed: no SCORECARD line and no `SHONEN.md` line states the r13 token for S884 or the
worldbuilding used-by (grep evidence in the report). The mismatch lives only in the
census receipt. Under the draft's pre-freeze disposition this Ca candidate is therefore
rejected before freeze and the correction lands as **unclaimed conformance repair** —
consistent with QUALITY 20 (records repair → both trends `unchanged`).

## 7. Out-of-scope observation (flag, do not fix here)

The round-78 census receipts carry no `# stamped revision` header (only `Command:`/`Exit:`)
— a criterion-17 gap: the receipt cannot self-prove its measurement revision, which is
why the correction must bind `4b255745` externally. Census-tool header repair belongs to
a different seat/round; this seat only flags it so the correction's measured-revision
binding is understood as externally pinned, not receipt-proven.
