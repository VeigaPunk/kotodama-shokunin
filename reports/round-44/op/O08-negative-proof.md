# O08 — Negative-proof: the O09 body has a zero-write surface and lands as a single authority

- **Seat:** O08 (verifier, claim O)
- **Out:** `reports/round-44/op/O08-negative-proof.md`
- **Observation window:** 2026-10-19T17:20Z–17:22Z (UTC), Python 3.14.7
- **Baseline:** `git rev-parse HEAD` → `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d`
- **Verdict:** **PASS** — the extracted O09 body is a read-only instrument; the landing's durable write set is exactly `tools/harness/basename-couples-resolver.py` (new) plus files under `reports/round-44/`. No filed byte, no corpus byte, and no second durable resolver path is touched. Five binding integration notes (N1–N5) in §6, one of which (N1) is a path in the r43 source doc that must **not** be followed literally.

## 1. Claim under test

`reports/round-44/claims.json:26` (claim O) requires landing the r43 O09 body
(`reports/round-43/op/O09-scribe.md:356-870`, sha256 `43ce341f…`) at
`tools/harness/basename-couples-resolver.py` as the single four-class census
authority, with `couples-reference-extractor.py` demoted to witness-only and its
bytes untouched (`d8d23a26…`). My seat's question is the negative form: **does
the landing write anything it should not?**

Three independent instruments were used:

1. **Static AST scan** of the extracted body (write-call inventory).
2. **Dynamic manifest diff** — 2,921-file sha256 manifest of `corpus/`, `tools/`,
   and every filed round `reports/round-1..43/**`, taken before and after all
   tool modes were exercised; plus `git status --porcelain -uall` before/after.
3. **Floor simulation** — the body placed at
   `<lane>/tools/harness/basename-couples-resolver.py` in a scratch lane with the
   real root files symlinked, to prove the landed *path shape* (not just the
   source location) produces the pinned census and the authority path name.

The extraction is byte-exact:

```
$ sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/o08/resolver-extract.py
$ sha256sum .scratch/o08/resolver-extract.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64  .scratch/o08/resolver-extract.py
$ wc -l .scratch/o08/resolver-extract.py
515
```

The digest matches `reports/round-43/op/O09-scribe.md:977` and
`reports/round-44/claims.json:26` exactly.

## 2. W1 — write set of the tool body: empty

Static scan (AST, all calls to write-capable names):

```
$ python3 -B - <<'PY'   # walk ast.Call for open/write/remove/rename/...
(164, 'open', ['path', "'rb'"])
(322, 'open', ['LIVE_PATH'])
(463, 'open', ['__file__', "'rb'"])
PY
```

- `resolver-extract.py:164` — `open(path, "rb")` (entry read).
- `resolver-extract.py:322` — `open(LIVE_PATH)` (default read mode; live wrapped
  field `corpus/knowledge/linguistics/phonetics-phonology.md`).
- `resolver-extract.py:463` — `open(__file__, "rb")` (self-digest for the JSON).

No `write`, `writelines`, `os.remove/rename/unlink/mkdir/makedirs`, `shutil.*`,
`subprocess.*`, or pathlib write methods anywhere in the body. Imports are stdlib
only (`__future__, argparse, glob, hashlib, json, os, re, sys`;
`resolver-extract.py:15-23`). `sys.dont_write_bytecode = True`
(`resolver-extract.py:25`). All file output is `print()` to stdout; the JSON
artifact is produced by the integrator's shell redirection, not by the tool.

Cross-instrument: the r43 O12 gate (extracted verbatim from
`reports/round-43/op/O12-negative-proof.md:283-411` to
`.scratch/o08/o12-gate.py`, sha256 `dbaa07e5…`) agrees:

```
$ python3 -B .scratch/o08/o12-gate.py .scratch/o08/resolver-extract.py --dynamic
FILE .scratch/o08/resolver-extract.py
  sha256      43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64
  dont_write_bytecode True
  imports     ['__future__', 'argparse', 'glob', 'hashlib', 'json', 'os', 're', 'sys']
  non-stdlib  none
  write-calls none
  VERDICT PASS-static
DYNAMIC
  run ['--selftest'] rc=0            | SELFTEST OK: 27/27 controls
  run ['--census'] rc=0              | misaligned: none
  run ['corpus/knowledge/linguistics/phonetics-phonology.md'] rc=0
                                     | wrapped=True tokens=4
  tree-diff NO-DIFF
  git-status-diff SAME
gate_rc=0
```

## 3. W2 — filed bytes unchanged (r42 witness digest stays)

`couples-reference-extractor.py` before and after the dynamic runs:

```
$ sha256sum tools/harness/couples-reference-extractor.py
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1
$ git hash-object tools/harness/couples-reference-extractor.py
1ded489bbb2bb90b3ad883ec0cd052822d870225
$ stat -c '%s %y' tools/harness/couples-reference-extractor.py
12223 2026-10-19 13:33:32.620681363 -0300
```

The digest equals the value pinned in `reports/round-44/claims.json:34` and the
O09 body's own docstring (`reports/round-43/op/O09-scribe.md:362-364`), and the
mtime predates this round's seat activity. The body does not import the witness
(it copies parse semantics by citation, per its docstring); no shadow aliasing.

Whole-tree filing check:

```
$ git diff --stat HEAD          # (no output; rc=0)
$ git status --porcelain -- corpus tools reports/round-1* reports/round-2* \
      reports/round-3* reports/round-4[0-3]
                                # (no output)
$ git status --porcelain -uall | grep -v '^?? .scratch/'
?? reports/round-44/claims.json
?? reports/round-44/targets.json
?? reports/round-44/telemetry/dispatch-declared.json
```

The only untracked non-scratch paths are r44 round metadata — expected and
inside the allowlist. Every tracked file under `corpus/`, `tools/`, and
`reports/round-1..43/**` is clean.

## 4. W3 — no corpus write

Static: no write call exists (§2). Dynamic: the 2,921-file manifest covers all
of `corpus/` (including `corpus/lessons/`), all of `tools/`, and every filed
round, and is byte-identical before/after:

```
$ wc -l .scratch/o08/manifest-before.sha256 .scratch/o08/manifest-after.sha256
2921 ... manifest-before.sha256
2921 ... manifest-after.sha256
$ sha256sum .scratch/o08/manifest-before.sha256 .scratch/o08/manifest-after.sha256
3006cd77a57ec77eda1d52022fb2dd7d3b4d9f42c1f1a5143e323014fce4911c  ...-before...
3006cd77a57ec77eda1d52022fb2dd7d3b4d9f42c1f1a5143e323014fce4911c  ...-after...
$ diff ...-before ...-after && echo TREE NO-DIFF
TREE NO-DIFF
```

All four modes were exercised in that window: `--selftest` (rc=0),
`--census` (rc=0), `--census --json` (rc=0), and one entry path (rc=0).
`git status --porcelain -uall` is identical before and after
(`5ef42ce6…` for both snapshot files). Corpus entry count remains 223
(`find corpus/knowledge -name '*.md' | wc -l` → `223`).

## 5. W4 — no second competing resolver path

**Durable tree at HEAD has no resolver at all, only the witness:**

```
$ ls -l tools/harness/basename-couples-resolver.py
ls: cannot access '...': No such file or directory
$ git ls-files | grep -E 'basename-couples-resolver|couples-resolver'
                                # (no output — none tracked)
$ git ls-files tools/harness | grep -i couples
tools/harness/couples-reference-extractor.py
```

**Floor simulation proves the landed path shape.** Copy of the extracted body at
`<scratch-lane>/tools/harness/basename-couples-resolver.py`, with the real
`corpus/`, `reports/`, and root `.md` files symlinked at the lane root:

```
$ python3 -B .../sim/tools/harness/basename-couples-resolver.py --census --json
tool        tools/harness/basename-couples-resolver.py
round       43
sha256      43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64
entries SAME | refs SAME | four_class_totals SAME | artifact_totals SAME
conservation SAME | wrapped_fields SAME | misaligned SAME
fallback_mappings SAME | disposition SAME | entries_detail SAME
```

Field-for-field equality with the source-location run (all ten compared keys
`SAME`). The tool names itself `tools/harness/basename-couples-resolver.py`, i.e.
exactly the claim path, and carries the pinned digest. (An earlier simulation
without the lane-root `.md` files and `reports/` produced 2,538/25 because those
tokens are Tier-1 lane-root references such as `AGENTS.md` and
`reports/round-20/…`; adding them restored the exact census. That is expected
policy behavior — Tier 1 includes the lane root — not a tool defect.)

**Scratch duplicates are non-durable.** `find .scratch -name
'basename-couples-resolver.py' | wc -l` → `19`; all are under `.scratch/`, which
`.gitignore:6` ignores (`git check-ignore -v` confirms), and none is tracked. They
are prior seats' simulation copies, not authorities.

**The contract mentions exactly one couples-resolver path:**

```
$ grep -oE 'tools/harness/[A-Za-z0-9._-]+' reports/round-44/claims.json reports/round-44/targets.json | sort | uniq -c
   4 claims.json:tools/harness/basename-couples-resolver.py
   2 targets.json:tools/harness/basename-couples-resolver.py
   1 targets.json:tools/harness/claims-freshness.py        # Ca's gate, not a resolver
   1 targets.json:tools/harness/couples-reference-extractor.py
```

The claim's non-goal `reports/round-44/claims.json:68` also forbids landing the
body at a second competing path. The body cannot alias the witness: stdlib-only
imports, no `import couples_reference_extractor`, and the witness is
demoted-by-record, not re-exported.

## 6. Integration notes — conditions the PASS depends on

**N1 (binding, path hazard).** The r43 integration sequence at
`reports/round-43/op/O09-scribe.md:882` says
`--census --json > reports/round-43/calib/couples-census-r43.json`. **Do not
follow that line in r44.** The r44 contract binds the artifact under
`reports/round-44/calib/` (`reports/round-44/claims.json:28`) and the shared rule
forbids writing `reports/round-1..43/**` (`reports/round-44/targets.json:6`).
Retarget to `reports/round-44/calib/<name>`; O06 fixes the name.

**N2 (metadata, do not edit bytes).** The body hardcodes
`payload["round"] = 43` (`resolver-extract.py:461`; source
`reports/round-43/op/O09-scribe.md:816`) and schema
`kotodama-couples-census-v3` (`:460`). The r44 artifact will therefore carry
`"round": 43` unless the wrapper records provenance. The body bytes are pinned
at `43ce341f…`, so **do not modify them**; record the r43 schema value as
provenance in the artifact header/LOG, or accept it explicitly. `to-verify` with
O06/integrator.

**N3 (denominator ordering).** The measured census is `entries=223 refs=2730`
and the four-class `2556+166+0+7=2729` + `glob-fragment=1`. Claim C takes the
corpus to 224 (`reports/round-44/claims.json:39-41`). If C lands before the O
census artifact is taken, the claim-O numbers will not reproduce. Sequence the O
census artifact from the pre-C tree at `c9f4eaa` (or record both denominators and
the delta). Cross-ref X00's ordering analysis; this seat does not resolve it.

**N4 (gate reuse).** The r43 O12 gate's allowlist is
`ALLOWED_PREFIXES = ("reports/round-43/", "tools/harness/")`
(`reports/round-43/op/O12-negative-proof.md:292`). If reused as an r44 check,
re-scope the report prefix to `reports/round-44/`. No present effect: the body
has zero write calls, so nothing is allowlisted or denied at runtime.

**N5 (queue record).** `reports/round-43/op/O09-scribe.md:898-900` closes
`r39-ic05-resolver-durability` as a successor record. File that record under
`reports/round-44/`; never edit
`reports/round-40/op/defect-queue-v2.json` (tracked; currently clean per
`git status --porcelain -- reports/round-40`).

## 7. Limits / not verified

- I did not apply the landing (seats draft; the integrator applies). This proof
  covers the extracted bytes and their write surface, not the post-landing tree.
- I did not run `reports/round-44/run-validation.py` (in-tree execution is
  forbidden by the round rules; the file may not exist yet).
- Semantic parity between the successor and the r42 witness is O07's receipt,
  not mine; I verified only that the witness bytes/digest are unchanged.
- This is a point-in-time snapshot (17:20–17:22Z). Concurrent seats write only
  under `reports/round-44/**`, outside the durable surfaces measured here.
- I did not verify C's landing or Ca's gate (other claims).

## 8. Reproduction

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/o08/resolver-extract.py
sha256sum .scratch/o08/resolver-extract.py                 # 43ce341f…
git rev-parse HEAD                                          # c9f4eaa
sha256sum tools/harness/couples-reference-extractor.py      # d8d23a26…
python3 -B .scratch/o08/resolver-extract.py --selftest      # 27/27, rc=0
python3 -B .scratch/o08/resolver-extract.py --census        # 223/2730, 2556/166/0/7 +1
python3 -B .scratch/o08/resolver-extract.py --census --json # one JSON stream to stdout
git diff --stat HEAD                                        # empty
git status --porcelain -- corpus tools reports/round-1* reports/round-2* \
  reports/round-3* reports/round-4[0-3]                     # empty
```

Scratch evidence left in `.scratch/o08/` (ignored, non-durable): `resolver-extract.py`
(`43ce341f…`), `manifest-before/after.sha256` (`3006cd77…`), `selftest.out`
(`17f47462…`), `census.out` (`87ef57d5…`), `census.json` (`30a41200…`,
586,834 bytes, 223 `entries_detail` rows, 50 mappings / 166 occurrences, 7
unresolved rows, 1 glob row, 0 ambiguous), `sim-census3.json` (`583377d0…`),
`o12-gate.py` (`dbaa07e5…`), git-status snapshots (`5ef42ce6…` both).

## 9. Evidence pointers

- Claim text: `reports/round-44/claims.json:24-34`; non-goals `:60-69`.
- Shared rules: `reports/round-44/targets.json:4-11`; seat mission `:25`.
- Source body: `reports/round-43/op/O09-scribe.md:346-371` (header/contract),
  `:356-870` (fenced body), `:873-902` (integration sequence), `:977` (digest).
- r42 witness: `tools/harness/couples-reference-extractor.py` (sha256
  `d8d23a26…`, blob `1ded489b…`, 12,223 bytes).
- r43 gate source: `reports/round-43/op/O12-negative-proof.md:281-411`.
- Live wrapped field: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
  (two direct + two `declared-prospective-seed` unresolved; identity set
  `{sound-change.md, sound-symbolism.md, tone-prosody.md, writing-systems.md}`).
