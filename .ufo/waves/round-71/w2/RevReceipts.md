# RevReceipts — round-70 telemetry re-stamps: byte preservation and header honesty

Seat: `L1Kotodama71.RevReceipts` (reviewer, leaf; no delegation, lane read-only).
Scope (assigned): verify the six round-70 telemetry receipts preserve their original bytes below the
marker, by diffing the below-marker region against `git show 453676a2:reports/round-70/telemetry/<file>`.
Scope (reviewer duty, same artefacts): the header block wave 1 wrote onto those six files
(`# counter sha256 (self)`, `# stamped/evaluated/measured revision`, `# tree`, `# worktree dirty`).

Revision of record: the six receipts are frozen since their re-stamp commit — `git log 1d1b432..HEAD --
<file>` is empty for all six (checked at HEAD `2eb0183f1b8aae1e721a7ed0e582a2f6eb480e2b`; earlier runs
during this review at `edd7895…` and `baf3b6a6…` gave the same empty result and the same tool verdicts).
Verdicts below were re-confirmed at `2eb0183f`.
Base the receipts name: `453676a2363c97e158cb112c9588906564d95a21` (round-70 records; tree
`7153d0d12f457edc5ee358b9e7b59adc0da1d104`). Re-stamp carrier: `1d1b432` (round-71 records).
Tooling: none installed (git + python3 sufficed; pacman paused per operator directive).

## Verdict summary

| # | check | verdict | evidence |
|---|---|---|---|
| V1 | below-marker bytes == original bytes at `453676a2` (the assigned question) | **PASS 6/6** | byte-identical, `diff` exit 0, sha256 equal, strict composition check |
| V2 | `# counter sha256 (self)` matches the object its own parenthetical names | **FAIL 6/6** | declared value ≠ sha256 of preserved bytes; matches no file in the repo |
| V3 | `# evaluated/measured revision` == where the recorded legs actually run | **FAIL 3/6** (all three controls) | re-run at `453676a2` prints the after-state, not the control values; the bodies reproduce at `21e6a7f` |
| V4 | criterion-19 carrier parentage (`--topo`) | **FAIL 6/6** | carrier `1d1b432` parent `8c203bd` ≠ stamped `453676a2` |
| V5 | criterion-19 `--lands` leg | **not attributable** | fails for all 28 header-carrying receipts in the lane, by the tool's own design |
| V6 | the landed counter (`accept-ca.py` V70-1 leg) can detect V2–V4 | **FAIL** | leg only greps prefixes and tests `first.startswith("#")` |
| V7 | marker-set completeness (exactly six files, one marker each, nothing else re-stamped) | **PASS** | `grep -c` per file; `census-{start,end}.txt` carry no marker/header |

## V1 — byte preservation: PASS 6/6 (exact commands)

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
for f in controls-ca controls-d controls-o measures-ca measures-d measures-o; do
  p=reports/round-70/telemetry/$f.txt
  git show 453676a2:$p > /tmp/orig-$f.txt
  tail -n +9 $p > /tmp/below-$f.txt        # marker is line 8 in every file
  diff -q /tmp/orig-$f.txt /tmp/below-$f.txt; echo "diff_exit=$?"
  sha256sum /tmp/orig-$f.txt /tmp/below-$f.txt
done
```

`diff_exit=0` for all six; the two sha256 lines agree per file:

| receipt | original bytes | sha256 (original == below-marker) |
|---|---|---|
| controls-ca | 342 | `ab73517ed465329a98f4c7ba1708e9536fbac13e60c53b484b04d8f10490eaf1` |
| controls-d | 1284 | `be192e81c7a7d1ca6e37e9e6fbed5b803c6f3183136ef9d317cbd8c57567bd14` |
| controls-o | 407 | `60772272fce24e139bf5851fa871beafece8e4bf1ff6afe24c11fc6f73bf32eb` |
| measures-ca | 132 | `6f40598b2ab66794bd2efc554c5a29319bac02e0eb6d55374ed3e3e226b3a57d` |
| measures-d | 1536 | `e19c6158098adbe027abcfbd86b22bccfaaccaf792f8af0eae54bd4acee8af71` |
| measures-o | 207 | `b7790bec03e5585bfdb0746b7b5ae8758d977495de31117ba1cdf7d0c8f03b8a` |

Strict composition (nothing inserted or dropped at the boundary): for each file,
`sha256(header_block_through_marker_line + original) == sha256(current_file)` → `True`; header block is
exactly 556 bytes in all six; `added_bytes == 556`; originals end with a newline. The marker line
`# original bytes preserved below` occurs exactly once per file and at line 8 in all six.
`census-start.txt` (last touched `6cb51a4`) and `census-end.txt` (`acc2d61`) carry neither header nor
marker — correct, since V70-1 names exactly the six `measures-*`/`controls-*` files.

**V1 is the assigned question and it passes.** The defects below are in the header the re-stamp added,
not in the preserved bytes.

## V2 — HIGH — `# counter sha256 (self)` is unverifiable and contradicts its own parenthetical (6/6)

Line 1 of every receipt reads `# counter sha256 (self): <64hex>  (digest of the preserved original
bytes below the marker)`. The computed digest of that region is **not** the declared value, in all six
(compare V1 table against the declared values):

| receipt | declared line-1 digest | sha256 of the named object |
|---|---|---|
| controls-ca | `a368cc05cdf1841ec66c9b43ca45f95ddd0b7c36e5a5779d4601f755af16d77c` | `ab73517e…` |
| controls-d | `8fefc70f767e190a874fa2bca2351740916322168c3e6bf1504dc58fdf4bfee6` | `be192e81…` |
| controls-o | `fb1fa64f917791015b3759efcd8cfd8891dd711982d2f1ac41d5b85227f0e03f` | `60772272…` |
| measures-ca | `3722a4a68548af55e550ae136d3ff7b30b483d4470b9d188713d3eec86dd4724` | `6f40598b…` |
| measures-d | `03cda056679bdd775e55d1db4b03a84d37e6fea99d803aafab8776aca4aaddc1` | `e19c6158…` |
| measures-o | `eff10b1b66299f75d3560da3dbbf5f8f41fe4cf66b7a2be607a55fccc7d00902` | `b7790bec…` |

I could not derive the declared values from any plausible object. Tested and rejected (29 constructions,
script kept inline in this review, run at HEAD): the below-marker region raw/rstrip/strip/CRLF/with-marker
line/comments-only/non-comments/lines-stripped/duplicated; the whole file; the file minus line 1; the
header block; the original at `453676a2`/`6cb51a4`/`acc2d61`/`1d1b432` (raw and stripped); git blob
header framing; path+content; sha-of-sha; sha256("") / sha256("\n"); and every sha1 blob id of the file.
Cross-file mixups were also excluded (no declared value equals any other receipt's digest).

The declared values are also not any committed file's content:

```
# scan every committed file body at HEAD (6917 files), 453676a2 and acc2d614 (6828 each)
git cat-file --batch over `git ls-tree -r --name-only <rev>`
→ "declared digests matching a committed file body: NONE"
```

Field semantics in this lane are unambiguous, so the field is not merely undefined — it is wrong:

* `corpus/QUALITY.md:59` (criterion 19): receipts carry `# counter sha256 (self)` with
  stamped == evaluated == measured and tree == `git rev-parse <stamped>^{tree}`; `tools/check-receipt-seq.py:28`
  pairs that line with the counter path and grades `recorded sha256 == sha256(counter)`.
* Precedent: `reports/round-65/telemetry/final-measures-ca.txt` records `counter sha256:
  550c89a4…` = sha256 of `reports/round-65/accept-ca.py` (re-derived here: match).
* Wave 1's own model header (`/.ufo/waves/round-71/w1/MutReceiptHeader.md:64`) uses
  `091074c5c054e1ed214204efee8ac25d12c7697414f2e8ea16aac9ec483b405e` = sha256 of
  `reports/round-69/accept-ca.py` (re-derived: match).
* Round-71 receipts in the same lane, stamped at the same commit, use the true counter sha:
  `reports/round-71/telemetry/measures-ca.txt:1` = `3f3f63fc…` = sha256(`reports/round-71/accept-ca.py`);
  `measures-d.txt:1` = `459cfa9d…` = sha256(`reports/round-71/accept-d.py`).

Round 70 has no counter file to hash — `git ls-tree -r --name-only 453676a2 -- reports/round-70 | grep accept-`
is empty; round-70's counting commands were inline shell (see `reports/round-70/claims.json`). So the honest
options were (a) omit the line (criterion 19: the counter-sha leg is *skipped, not failed*, when the line is
absent) or (b) write a digest whose definition a re-opener can execute. The landed re-stamp did neither: it
invented six values that no command in the lane reproduces. Any re-opener running the parenthetical's own
instruction gets a mismatch on 6/6.

Severity HIGH because these files are the evidence of record: a receipt field that cannot be re-derived is
an unfalsifiable claim inside the artefact whose job is falsifiability, and `tools/check-receipt-seq.py`
silently accepts it (no counter paired → sha leg skipped; `--selftest` 14/14 still green).

## V3 — HIGH — `# evaluated revision` / `# measured revision` are false for the three control receipts

All six stamp `stamped == evaluated == measured == 453676a2` (tree `7153d0d1`). For the three
`controls-*` receipts the recorded legs were run at the declaration base `21e6a7f` — their own preserved
first line says so (`# pre-data control … measured at base 21e6a7f on 2026-10-25`) — and at `453676a2`
those legs provably print the after-state instead. Method: fresh clone (a `git archive` extraction is *not*
usable for the `accept-d --selftest` leg — its fixture needs git and prints a misleading `1/2` outside a repo):

```
git clone -q --no-hardlinks /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/klane
cd /tmp/klane && git checkout -q 453676a2
```

Re-running each receipt's own legs (commands copied verbatim from the preserved bodies):

| receipt | recorded (preserved body) | same legs at stamped `453676a2` | same legs at base `21e6a7f` | reproduces at stamp? |
|---|---|---|---|---|
| controls-ca | `0` / `exists=1` / `0` | `10` / `exists=0` / `1` | `0` / `exists=1` / `0` | **NO** (reproduces at base) |
| controls-d | `SELFTEST: 7/7` | `SELFTEST: 10/10` | `SELFTEST: 7/7` | **NO** (reproduces at base) |
| controls-o | `0` / `36` / `SELFTEST: 1/2 exit=1` | `36` / `36` / `SELFTEST: 2/2 exit=0` | `0` / `36` / `SELFTEST: 1/2 exit=1` | **NO** (reproduces at base) |
| measures-ca | `10` / `0` / `1` | `10` / `0` / `1` | — | YES |
| measures-d | `SELFTEST: 10/10` + `ACCEPT-O-69: PASS legs=7/7` | identical (all 7 LEG lines byte-equal) | — | YES |
| measures-o | `36` / `36` / `SELFTEST: 2/2 exit=0` | `36` / `36` / `SELFTEST: 2/2 exit=0` | — | YES |

Exact commands used at `453676a2` (all inside `/tmp/klane`): the `awk|sort -u|wc -l`,
`test -f …; echo exists=$?` and `grep -c 'round-69 calibration' SCORECARD.md` trio; the registry
`grep -cE` + `find reports -name 'accept-*.py' | sort | wc -l` + `python3 -B reports/round-69/accept-d.py --selftest`;
`python3 -B tools/check-supersession-settlement.py --selftest`; `python3 -B reports/round-69/accept-o.py --root .`.
At base `21e6a7f` (tree `ece8c7cd25b64bb8cbbc590cd750ecc07790c40e`) the same commands print the control
bodies exactly.

So the control *contents* are valid do-nothing controls; the header is the false part. Each of the three
files now contradicts itself: lines 3–4 say evaluated/measured at `453676a2`, line 9 says measured at base
`21e6a7f`, and the legs split the two ways. The lane's own bar makes this a graded defect:
`corpus/QUALITY.md:57` (criterion 17) — "A receipt … stamping a revision whose bytes fail the receipt's own
legs, is a calibration defect"; `QUALITY.md:59` (criterion 19) — "the evaluation runs at that revision …
the receipt proves stamp and evaluation agree". `# tree:` is wrong in the same way for the controls
(`7153d0d1` is `453676a2`'s tree; the run happened on `ece8c7cd`), and `# worktree dirty (tracked): False`
describes the `453676a2` clone rather than the base-tree run.

Note the three after-state receipts (`measures-*`) are honest on this axis: their numbers reproduce at the
stamped revision, and at the true lands commit `acc2d614` too (`SELFTEST: 10/10`, `ACCEPT-O-69: PASS
legs=7/7`, `SELFTEST: 2/2`, registry rows `36`).

## V4 — MEDIUM — criterion-19 carrier parentage fails 6/6 (`--topo` exit 1)

```
python3 -B tools/check-receipt-seq.py --root . --topo \
  reports/round-70/telemetry/{controls,measures}-{o,ca,d}.txt
→ TOPO-… FAIL carrier=1d1b4325 parent=8c203bd9 stamped=453676a2   (×6)
→ RECEIPT-SEQ: FAIL   exit=1
```

The chain is `453676a2 → b94a543 → 825b78a → b694afd → 65ff151 → 498db73 → 8c203bd → 1d1b432`, so the
re-stamp carrier sits five commits past the revision it stamps. This is not an unsatisfiable leg: the same
command over all 28 header-carrying receipts in the lane gives 19 PASS / 9 FAIL, and the round-71 receipts
carried by `3764c2d` (parent `1d1b432`) PASS. Criterion 19 requires `--topo` to exit 0 post-records; it does
not. A re-stamp committed as the direct child of `453676a2` (or stamping the actual lands commit and
committing the re-stamp immediately after it) would satisfy it.

## V5 — MEDIUM — `--lands` mode cannot grade this re-stamp (instrument defect, not a seat defect)

```
python3 -B tools/check-receipt-seq.py --root . --lands 453676a2363c97e158cb112c9588906564d95a21 <six>
→ SEQ-… FAIL missing_headers=['stamped','evaluated','measured','tree']  (×6) → exit=1
```

I do **not** charge this to the re-stamp: the header only exists in the carrier commit, and `--lands`
reads committed bytes at the stamped revision, so it fails by construction. Measured lane-wide: of the 28
receipts that carry a `# stamped revision:` header, **0** have that header present at their stamped
revision. The tool's own selftest asserts this behaviour is intended (`lands-absent-is-fail` — "receipt not
in lands tree must FAIL not skip"; `lands-read-committed` — "receipt lands in the NEXT commit; at lands it
is absent"). Criterion 19 nevertheless states the check as "`--lands <40hex> <receipt> [<counter>]` exits 0".
That criterion clause is unsatisfiable for any receipt and should be restated (grade the *counter* at lands,
the *receipt* by header equality + `--topo`). Route: criterion text / instrument, not the six files.

## V6 — MEDIUM — the landed Ca counter cannot see V2, V3 or V4

`reports/round-71/accept-ca.py:76-84` (V70-1 leg):

```
has_all     = all(line in data for line in HDR_LINES)     # substring presence only
marker_ok   = MARKER in data
below       = data.split(MARKER, 1)[1]
first       = below.strip().splitlines()[0].strip()
original_ok = first.startswith("#") and len(first) > 3     # ANY comment counts as "original bytes"
```

Consequences, all exercised by the six landed files: a fabricated `# counter sha256 (self)` passes
(V2); a header asserting evaluation at a revision that contradicts the body passes (V3); `--topo` is never
invoked (V4); and the "original bytes preserved" clause is satisfied by any line beginning with `#`, so the
leg cannot distinguish the real body from a stub. This is exactly the hole wave 1's own critic predicted
(`.ufo/waves/round-71/w1/CritClaimSizing.md` §2.4: "A claim could overwrite the six files with header-only
content and pass every counted leg"). The mutation seat's leg design (`MutReceiptHeader.md` §2, L1–L4)
was stronger than what landed: it at least counted six *distinct* prefixes and required non-empty preserved
bytes. Recommended minimum for the leg: per-file `sha256(below_marker) == recorded` against
`git show <stamped>:<path>` and `evaluated == measured == stamped`, plus a `--topo` call.

## V7 — PASS — marker-set completeness

`grep -c '^# original bytes preserved below$' reports/round-70/telemetry/*.txt` → 1 for the six, 0 for
`census-start.txt`/`census-end.txt`; `grep -l '^# stamped revision' reports/round-70/telemetry/*.txt` →
exactly the same six. No seventh receipt was silently re-stamped, and no receipt outside round 70 carries
this marker (`grep -rl '^# original bytes preserved below' reports/` → the six only).

## Cross-check that does pass

`python3 -B tools/check-receipt-seq.py --root . <six>` (default header-equality mode) → `RECEIPT-SEQ: PASS`,
exit 0: the six prefixes are present, stamped == evaluated == measured, and the recorded tree equals
`git rev-parse 453676a2^{tree}`. So the wave-1 landing is green on the two legs that check *internal*
consistency and red on the legs that check *correspondence to reality* (V2 declared digest, V3 evaluation
site, V4 parentage).

## Residual risk and verification gaps

* Provenance of the six declared digests is unknown. The only construction consistent with all the
  evidence is that they were computed over a worktree state that was never committed (round 70 measured
  "at lane `6cb51a4`+landed edits", i.e. an uncommitted tree). If so, the re-stamp's line 1 attests to a
  state no re-opener can reconstruct — which is itself the defect, not a gap.
* I did not attempt to prove *when* the re-stamp was written relative to `1d1b432` (single commit, no
  in-commit timestamps); the carrier-parentage failure (V4) is the objective form of that question.
* The controls' `# worktree dirty (tracked): False` is unverifiable as a historical fact (no recorded
  dirty-file list); I only show it does not describe the run the body records.
* V3 rests on leg re-execution in a clean clone; `accept-d --selftest` is git-sensitive, so a re-opener
  must use a clone, not an extracted tarball (documented above to prevent a false `1/2`).
* No lane source was modified by this seat; only this report was written.
