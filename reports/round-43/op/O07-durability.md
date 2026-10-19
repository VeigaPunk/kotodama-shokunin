# O07 — Durability leg: canonical path, CLI contract, instrument relations

- **Seat:** O07 (`reports/round-43/targets.json:23`), claim **O** (operability),
  round 43, loop 1.
- **Baseline:** `7ceff59` (`git log --oneline -3`, 2026-10-19). Tree state:
  clean except untracked `reports/round-43/` (`git status --porcelain`).
- **Scope:** name the canonical durable path, the shebang/CLI contract
  (`--selftest` / `--census` / `[paths]`), the relation to — and non-edit of —
  the filed r19 instrument and the r42 `couples-reference-extractor.py`, and
  prove no `.scratch` dependency remains. Read-only survey; no bytes outside
  this out path were written.

## 0. Verdict for the integrator

1. **Canonical path — conditional on a path ruling (§1.1).** Recommended:
   `tools/harness/basename-couples-resolver.py`; free (`ls` → "No such file or
   directory"), durable, and the literal name the claim sanctions
   (`reports/round-43/claims.json:28`). **Contested:** scout K01 §7 recommends
   the opposite — patch the tracked r42 extractor in place, because a second
   live resolver re-creates the divergence problem
   (`reports/round-43/scout/K01-resolver-scout.md:313-315`). Applying both would
   leave two live resolvers. The integrator must rule before O01's body is
   applied; the contract below applies to whichever host wins.
2. **Do not edit the filed r19 instrument** (`reports/round-19/audit/entry-audit.py`,
   sha256 `e7992c32…`). Its bytes are evidence; the successor cites `:75` and
   copies the Tier-1 semantics without importing it (§3). Under the recommended
   new-file route the r42 extractor also stays byte-identical
   (`d8d23a26…`, tracked at `7ceff59`); under K01's route it is patched by an
   explicit integrator ruling and its digest must be re-pinned (§1.1, §4.3).
3. **The r43 claim's `before` is stale on one half.** A durable instrument that
   reads the wrapped field whole already exists and is committed: the r42
   extractor. Live proof: `--selftest` → 8/8 PASS; `--census` → 223 entries /
   2730 refs, `wrapped fields: 1`; per-entry on
   `corpus/knowledge/linguistics/phonetics-phonology.md` → `tokens=4`. So defect
   **D1 (block extraction) is already fixed in a landed instrument**; the r43
   increment is **D2 (disposition leg), four-class reporting with every fallback
   mapping listed, a synthetic ambiguous negative, and a filed census**. The
   round must not re-claim D1 as "missing" (see §7 finding F1).
4. **No `.scratch` dependency is achievable and should be mandatory.** The r42
   extractor itself has no runtime `.scratch` dependency, but its `--selftest`
   calls `tempfile.mkdtemp()` and therefore writes one temp dir under `$TMPDIR`
   per run; 68 such residue dirs exist in `.scratch` today (strace evidence,
   §5.2). The r43 successor's selftest must build its phantom/ambiguous fixtures
   **in memory**, so its write surface is exactly zero.
5. **`reports/round-43/run-validation.py` does not exist yet** (`ls` → no such
   file), so the runner-side digest pin is `to-verify`; §6 names the exact
   command the integrator should add once the runner lands.

## 1. Canonical path

### 1.1 Decision gate (read first)

Two mutually exclusive routes; applying both leaves two live resolvers.

| | **A. New successor file** (this seat's contract) | **B. Patch r42 in place** (K01 §7) |
|---|---|---|
| Path | `tools/harness/basename-couples-resolver.py` | `tools/harness/couples-reference-extractor.py` |
| Claim fit | literal name at `claims.json:28` | "wave-named equivalent" at `claims.json:28` |
| r42 bytes | unchanged (`d8d23a26…`) | move; re-pin digest + successor note |
| Live resolvers | two — drift risk, contained by §4.4–§4.5 | one — no drift |
| O07 mission | matches the non-edit relation (`targets.json:23`) | contradicts it; needs an explicit integrator ruling |
| Cost | new file + SKILL row + equivalence receipt | K01's line table (`scout/K01-resolver-scout.md:298-315`) + re-run census + digest re-pin |
| Precedent | r42 minted a successor rather than editing the filed r19 report | `tools/harness/packet_links.py` has 2 commits (in-place amendment is established) |

**Recommendation: A** — the claim and this seat's contract name it, it keeps the
r42 instrument as a stable N6 witness, and its drift risk is testable (same
wrapped field, same four token names; authority rule §4.5). **If the integrator
rules B**, §1.2–§1.4 and §4.3 are superseded: apply the §2 contract and K01's
patch table (`scout/K01-resolver-scout.md:298-315`) to the r42 path, record the
new digest in the census header and LOG, and keep the authority rule.

### 1.2 Option A path and rationale

```
tools/harness/basename-couples-resolver.py
```

- Parent directory exists and holds seven tracked peers
  (`git ls-files tools/harness/`; `stat -c '%A'` all `-rw-r--r--`).
- Name: the policy is the "basename-couples policy"
  (`reports/round-39/calib/basename-couples-policy.md:1`; full successor
  `reports/round-42/calib/basename-couples-policy-full.md:1`), and the claim
  explicitly allows this path "or wave-named equivalent"
  (`reports/round-43/claims.json:28`). Using the literal claim name keeps every
  future citation and digest stable.
- Scope of the name: the tool resolves **both** tiers, not only the basename
  fallback. Its docstring must say so (contract fragment in §2.6) so the name is
  not read as "fallback-only".

### 1.3 Other paths rejected under either route

| Path | Why not |
|---|---|
| `reports/round-43/op/...` or any round path | Round reports are filed evidence; a tool there is frozen by the never-edit rule and cannot be fixed next round. Precedent: the r39 I-C05 resolver lives in `.scratch` and is now cited only by digest (`reports/round-39/cov/C05-audit.md:30`) — the exact durability failure this claim exists to end. |
| `corpus/...` | Instruments never live under the corpus; corpus admission is governed separately (`corpus/QUALITY.md:13-20`). |
| Shared helper module extracted from the r42 tool | Adds a second new path and a third file to keep in sync; under A the successor is standalone and equivalence is a filed one-off receipt (§4.4), not a runtime import. |

### 1.4 Collision / precondition checks (observed)

```
$ ls -la tools/harness/basename-couples-resolver.py
ls: cannot access 'tools/harness/basename-couples-resolver.py': No such file or directory
$ ls -la reports/round-43/run-validation.py
ls: cannot access 'reports/round-43/run-validation.py': No such file or directory
$ git status --porcelain tools/harness/ reports/round-19/
(no output)
```

`.gitignore` contains `.scratch/` and `__pycache__/` but no rule that would hide
`tools/harness/*.py`. The new file is therefore visible to `git add` and to the
r43 runner.

## 2. Shebang and CLI contract

### 2.1 Normative header

| Item | Contract | Precedent / evidence |
|---|---|---|
| Shebang | `#!/usr/bin/env python3` | all seven `tools/harness/*.py` start with it (`head -1`) |
| Encoding / endings | UTF-8, LF | repo convention |
| Mode | `0644`, no exec bit required | `stat -c '%A' tools/harness/*.py` → all `-rw-r--r--`; invocation is `python3 <path>` |
| Python | stdlib only; 3.7+ (`from __future__ import annotations` permitted) | 6/7 harness tools use it; host `python3 --version` → `Python 3.14.7` |
| Bytecode | `sys.dont_write_bytecode = True` at module top; invoke with `-B` in round commands | r42 tool `:25`; `.gitignore` has `__pycache__/` |
| Network / subprocess / git | none | read-only instrument; r42 tool imports only `argparse, glob, os, re, sys` (+ `tempfile` inside selftest — the r43 tool must not, §5.2) |
| Writes | **none**; stdout only | aligns with r42 tool; the filed artifact is produced by shell redirection (§2.5) |

### 2.2 Modes

The claim's counting commands are `--selftest` and `--census` exactly
(`reports/round-43/claims.json:30-31`). The third leg, positional paths, is the
per-entry disposition surface O06 owns.

| Invocation | Reads | Emits | Exit |
|---|---|---|---|
| `python3 tools/harness/basename-couples-resolver.py --selftest` | in-memory fixtures + the live wrapped field (`corpus/knowledge/linguistics/phonetics-phonology.md:72-77`, read-only) | one `PASS`/`FAIL` line per control + summary | `0` green, `1` red |
| `... --census` | every `corpus/knowledge/*/*.md` | four-class totals per entry + corpus totals; every fallback mapping listed | `0` completed (findings are data, not failure) |
| `... --census --json` | same | machine artifact on **stdout** (schema owned by O06/O10) | `0` |
| `... PATH [PATH ...]` | the named entries + the corpus index | per-token disposition: class, mapping or reason, group label, alignment | `0` completed |
| `... PATH --json` | same | JSON records on stdout | `0` |
| no arguments / `--help` | — | usage | `2` |
| both `--selftest` and `--census` | — | error (mutually exclusive) | `2` |
| corpus root not found | — | error naming the searched start path | `2` |
| named entry missing/unreadable | — | error naming the path | `2` |

Exit `2` for a missing input is an instrument failure, not a couples finding:
an unresolved/ambiguous token is reported **inside** a successful run, never by
exit code. This keeps the runner able to distinguish "census ran and found N
unresolved" from "census could not run".

### 2.3 Root discovery (cwd- and symlink-independent)

Copy the r42 pattern (`tools/harness/couples-reference-extractor.py:27-32`) with
one hardening — resolve symlinks:

```python
HERE = os.path.dirname(os.path.realpath(__file__))
LANE = HERE
for _ in range(8):
    if os.path.isdir(os.path.join(LANE, "corpus", "knowledge")):
        break
    LANE = os.path.dirname(LANE)
else:
    sys.exit("lane root not found upward from " + HERE)
KNOW = os.path.join(LANE, "corpus", "knowledge")
```

Evidence that this pattern is cwd-independent: the r42 tool was run from `/tmp`
with an absolute path and returned the identical census
(`entries=223 refs=2730 …`, §6 log). `abspath(__file__)` does not resolve a
symlink; `realpath` closes that hole. No `LANE`/`TMPDIR` environment override is
read.

### 2.4 Output stability

- Token iteration and entry iteration are sorted; the JSON artifact is written
  with a fixed key order and `sort_keys=True` so two runs produce byte-identical
  digests.
- The human summary's first line must keep the policy's four class names exactly
  (`direct`, `fallback`, `ambiguous`, `unresolved`) and print the identity
  `refs == direct + fallback + ambiguous + unresolved`. Non-policy artifacts
  (the §5.6 glob fragment, declared-prospective seeds) are reported in a
  **separate labelled section**, never folded into `unresolved` or `direct`
  (`reports/round-42/calib/basename-couples-policy-full.md:97-102`).
- Every fallback row carries `token -> corpus-relative path`; every
  unresolved/ambiguous row carries a named reason (policy §3.3, §2). The exact
  row schema is O06's (`op/O06-disposition-leg.md`), not redefined here.

### 2.5 The filing act

The tool never chooses a `reports/` path and has no `--out` switch. The census
artifact is filed by the integrator as a shell redirection, e.g.:

```
python3 tools/harness/basename-couples-resolver.py --census --json \
  > reports/round-43/calib/<artifact-name>.json
```

This keeps the instrument's write surface at zero (O12 negative-proof) and keeps
"what is filed" an explicit integrator act. Artifact name and schema: O06/O10.

### 2.6 Fenced contract fragment (O01 owns the implementation body)

```python
#!/usr/bin/env python3
"""Durable resolver for the basename-couples policy (r43 claim O).

Policy: reports/round-42/calib/basename-couples-policy-full.md (the full
successor of the truncated r39 filing).
Defect provenance: reports/round-19/audit/entry-audit.py:75 (single-line
capture); reports/round-39/calib/Ca04-verify.md:78-93 (D1/D2).
Predecessor (NOT edited, NOT imported): tools/harness/couples-reference-extractor.py
(sha256 d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1).

Read-only: opens corpus entries, writes nothing. Stdlib only.
Modes: --selftest | --census [--json] | [PATH ...] [--json]
Exit: 0 green/completed, 1 selftest red, 2 usage/IO/root error.
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.realpath(__file__))
LANE = HERE
for _ in range(8):
    if os.path.isdir(os.path.join(LANE, "corpus", "knowledge")):
        break
    LANE = os.path.dirname(LANE)
else:
    sys.exit("lane root not found upward from " + HERE)
KNOW = os.path.join(LANE, "corpus", "knowledge")

# ... O01's extraction / classification / disposition body ...

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="basename-couples resolver (Tier 1 direct + Tier 2 fallback)")
    parser.add_argument("paths", nargs="*")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--selftest", action="store_true")
    modes.add_argument("--census", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    # dispatch: selftest -> 0/1; census -> 0; paths -> 0; none -> help, 2
```

The integrator applies O01's full body; this fragment fixes only the durability
surface (shebang, root discovery, mode exclusivity, exit-code policy).

## 3. Relation to the filed r19 instrument — read-only reference, never edited

| Fact | Evidence |
|---|---|
| Path | `reports/round-19/audit/entry-audit.py` |
| sha256 | `e7992c325a479aa7415c42722a034a95a9ea342a58367ead9cd2636a5a62830c` |
| History | single commit `caf1bea`; no working-tree change (`git status --porcelain reports/round-19/` → empty) |
| Defect host | `def couples_targets` at `:74`; single-line capture `re.search(r"^- couples:\s*(.*)$", text, re.M)` at `:75`; Tier-1 candidates `:87-91`; `os.path.isfile` gate `:92`; return `:96` |
| Policy's citation of it | `basename-couples-policy-full.md:16-17,29,261` |

**What the successor copies (semantics, not code):** the Tier-1 candidate order
**entry directory → lane root → `corpus/knowledge`**, each normalized with
`os.path.normpath`, resolved by `os.path.isfile` (`entry-audit.py:87-95`). This
order is why same-partition basenames are `direct`, not `fallback`
(policy §5.4). Token regex and one-level brace expansion likewise match
`entry-audit.py:31,34-42`.

**What it does not do:** import the r19 module. Importing would bind the
successor to a filed round path and to that module's import-time `LANE`
computation, and would mix an entry-admission audit surface into a
couples-specific instrument. The defect line is cited in the docstring for
provenance; the code is independent.

**Why no edit:** filed bytes `reports/round-19/**` are immutable
(`reports/round-43/targets.json:6`), and the r19 file is the evidence that the
defect existed. The fix lives only in the successor; the r19 digest above is the
check that its bytes did not move.

## 4. Relation to the r42 `couples-reference-extractor.py` — read-only reference, never edited

### 4.1 What r42 already landed

| Fact | Evidence |
|---|---|
| Path | `tools/harness/couples-reference-extractor.py` (332 lines) |
| sha256 | `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1` |
| Tracked | `git ls-files tools/harness/` lists it; introduced by `7ceff59` |
| Claim status | r42 O **passed** (`reports/round-42/validation.json`, `claims.O.passed=true`); r42 was rejected only on C (`acceptance_checks_passed=false`) |
| Block extraction | `couples_block()` `:50-73`; hyphen soft-wrap heal `join_parts()` `:76-92` |
| Live wrapped field | selftest `:288-289` and my run: 4 tokens `sound-change.md`, `sound-symbolism.md`, `tone-prosody.md`, `writing-systems.md` |
| Selftest | 8/8 PASS (my run, §6) |
| Census | `entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1`; `wrapped fields: 1` |
| Standalone | no `.scratch` runtime reference; cwd-independent (run from `/tmp`, identical output) |

### 4.2 Gaps the r43 successor must close (measured, not assumed)

1. **No fallback mappings in census mode.** `--census` prints totals, wrapped
   fields, unresolved, misaligned — but no `token -> path` lines:
   `--census | grep -c "fallback.*->"` → `0`. Policy §3.3 requires every
   fallback mapping listed.
2. **Six classes, not the policy's four.** It adds `prospective` and
   `glob-fragment`. The policy permits separately classing glob fragments
   (`basename-couples-policy-full.md:97-102`) and r42 introduced `prospective`
   for declared seeds; but the r43 claim's threshold is a **four-class** census.
   The successor reports the four policy classes as the headline and the two
   non-policy buckets in a separate labelled section.
3. **No synthetic ambiguous negative.** Its selftest has wrapped positive,
   unwrapped regression, over-capture trap, phantom/prospective negative, N6
   regression, glob fragment — but no two-index-hit `ambiguous` control
   (`selftest()` `:242-295`). The r43 claim requires one
   (`reports/round-43/claims.json:34`).
4. **No disposition leg (D2).** Nothing maps an `unresolved` token to
   blocker vs documented/non-blocker per C12 row 2
   (`reports/round-39/calib/Ca04-verify.md:94-99`). Its records carry
   `documented` (`:159-160,180`) but no disposition decision.
5. **Selftest temp write.** `tempfile.mkdtemp()` at `:269-271` creates a dir
   under `$TMPDIR` and leaves it; 68 residue dirs in `.scratch` (§5.2).
6. **Blank-line over-capture (latent; zero live instances).** `couples_block()`
   skips blank lines (`:64-65` `if not following.strip(): continue`), so an
   indented line *after* a blank is still captured. Synthetic proof (importlib,
   `-B`, no writes):

   ```
   text = "- couples: `a.md`\n\n  prose paragraph with `b.md`\n- next: x\n"
   couples_block(text) -> ['`a.md`', 'prose paragraph with `b.md`']
   field_refs(text)    -> ['a.md', 'b.md']
   ```

   Live impact is **zero** at HEAD: the corpus census reports exactly one
   wrapped field (`phonetics-phonology.md`, legitimate), so no second entry
   exhibits the pattern. Fix is `break` on a blank line, as K01 §7 and O02
   control 4 require (`scout/K01-resolver-scout.md:302`); a successor must not
   reproduce the `continue`.

### 4.3 Why the successor does not edit it (Option A; superseded under Option B)

- Its digest is the r42 O evidence anchor; r42's census artifact and validation
  cite the instrument. An in-place edit would make the filed r42 result
  unreproducible from its own instrument.
- The claim asks for a **successor** instrument with the disposition leg; the
  seat mission explicitly says "does not edit … the r42 couples-reference-extractor"
  (`reports/round-43/targets.json:23`).
- Editing a landed instrument also violates the round's drafting rule: changes
  are drafted for the integrator, and an edit to a tracked instrument is a
  different, larger change than a new file (it needs its own audit + digest
  update). A new path keeps the r42 witness intact.
- **If the integrator rules Option B**, this section is void: the r42 tool is
  patched by ruling, its digest moves, and the new digest must be re-pinned in
  the census header, the LOG entry and any runner assertion.

### 4.4 Cross-check obligation (filed receipt, not runtime coupling)

At landing, file both lines in the census artifact/LOG:

```
tools/harness/couples-reference-extractor.py --census
  -> entries=223 refs=2730 ... wrapped fields: 1
tools/harness/basename-couples-resolver.py --census
  -> entries=<N> refs=<N> direct/four-class totals; wrapped fields: 1
```

The two must agree that **exactly one** wrapped field exists and that it yields
**the same four token names**. Four-class totals may differ from r42's six-class
totals only by the documented separation of `prospective`/`glob-fragment`; any
other difference is a finding, not a preference. Record the r42 digest
`d8d23a26…` beside the comparison so the witness is pinned.

### 4.5 Authority after landing

**Option A:** `tools/harness/basename-couples-resolver.py` becomes the **single
census authority** for `couples:` references from r43 onward. The r42 extractor
remains the N6 regression witness and the historical 223/2730 recorder; it is not
extended and not re-run as an authority. This avoids two instruments drifting
while both are cited.

**Option B:** the patched r42 path is the single authority *and* the witness; no
successor authority line is needed, but the r42 digest changes and the r42
census number becomes historical-only (the new census supersedes it). In both
routes, exactly one path is cited as authority in the census header and the
SKILL.md inventory.

## 5. No `.scratch` dependency

### 5.1 What the claim's "before" refers to — and what it actually is

- The r43 claim says "the only resolver that ever ran (r39 I-C05) lives in
  ephemeral `.scratch`" (`reports/round-43/claims.json:27`).
- Filed r39 record: `I-C05` is `.scratch/c05/c05-audit.py`, sha256
  `4326bb856e13e34a3334e4769140e4ee20a1a1d1266a91d8616eb557da75cbd6`, and it is a
  **citation/path resolver**, not a couples resolver
  (`reports/round-39/cov/C05-audit.md:30`; its checks are fence extraction and
  path/line citation binding, `:31,61`). The identification in the claim is
  therefore inaccurate — flag, do not repeat it in filed prose.
- The r39 policy document's only `.scratch` mention is the TMPDIR export in its
  verification recipe, not a read/write dependency:
  `reports/round-39/calib/basename-couples-policy.md:106-107`.
- The landed r39 policy is truncated at 107 lines / 5832 bytes and its §6
  heading is followed only by "Run from the lane root; no writes…" — the recipe
  body is absent (`wc -l -c`; `sed -n '104,107p'`). The full policy is the r42
  successor doc. The new tool cites the **full** doc.

### 5.2 The r42 selftest's transient `.scratch` write (must not be copied)

Strace of `--selftest` with `TMPDIR=$PWD/.scratch`:

```
openat(AT_FDCWD, ".../.scratch/bbmayv7b", O_RDWR|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC, 0600) = 3
unlink(".../.scratch/bbmayv7b") = 0
mkdir(".../.scratch/tmpovougwue", 0700) = 0
mkdir(".../.scratch/tmpovougwue/linguistics", 0777) = 0
openat(AT_FDCWD, ".../.scratch/tmpovougwue/e.md", O_WRONLY|O_CREAT|O_TRUNC|O_CLOEXEC, 0666) = 3
```

`ls -d .scratch/tmp* | wc -l` → **68**. These are disposable fixture dirs, not a
read dependency — the tool never reads a pre-existing `.scratch` artifact — but
they are a write residue and would trip O12's "writes outside out path" check if
copied. The r43 contract is stricter: **in-memory fixtures only**.

### 5.3 Contract for the new tool

- No string `scratch`, no `TMPDIR`, no `tempfile`, no `os.environ`, no
  `subprocess`, no `shutil`. Phantom/ambiguous fixtures are dicts passed to an
  index-injectable `classify(ref, entry_dir, index=...)`; no files are created.
- The wrapped-field positive control reads the live
  `corpus/knowledge/linguistics/phonetics-phonology.md` (read-only), as the r42
  selftest already does (`:281-289`).
- Post-landing proof (run by the integrator/verifier; expected results shown):

```
$ grep -nE '\.scratch|TMPDIR|tempfile|subprocess|os\.environ' \
    tools/harness/basename-couples-resolver.py
(no output; grep exit 1)
$ cd /tmp && env -u TMPDIR python3 -B <lane>/tools/harness/basename-couples-resolver.py --selftest
... all PASS; exit 0
$ env -u TMPDIR python3 -B <lane>/tools/harness/basename-couples-resolver.py --census | sha256sum
$ (cd <lane> && python3 -B tools/harness/basename-couples-resolver.py --census | sha256sum)
(identical digests)
$ strace -f -e trace=openat,mkdir,unlink ... --selftest 2>&1 | grep -c '\.scratch'
0
```

Symlink hardening check (optional, disposable under `.scratch`):

```
ln -s ../../tools/harness/basename-couples-resolver.py .scratch/o07-link.py
cd /tmp && env -u TMPDIR python3 -B <lane>/.scratch/o07-link.py --selftest   # realpath discovery
rm .scratch/o07-link.py
```

## 6. Durability lifecycle and verification

1. **Draft** — O01's fenced block in `op/O01-tool-draft.md`; this document fixes
   the durability surface it must carry.
2. **Apply** — integrator writes
   `tools/harness/basename-couples-resolver.py` (mode 0644; no chmod needed).
3. **Selftest before filing** —
   `python3 -B tools/harness/basename-couples-resolver.py --selftest` → exit 0.
4. **Census + artifact** —
   `python3 -B tools/harness/basename-couples-resolver.py --census --json > reports/round-43/calib/<name>.json`.
5. **Pin** — `sha256sum tools/harness/basename-couples-resolver.py` recorded in
   the census artifact header and the r43 LOG entry, beside the r19/r42 digests
   (`e7992c32…`, `d8d23a26…`).
6. **Commit** — integrator only. Proof of durability:
   `git ls-files --error-unmatch tools/harness/basename-couples-resolver.py` →
   prints the path. Before commit it is untracked and not durable.
7. **Scratch-cleanup replay** — after `.scratch` is cleared, re-run steps 3–4
   from `/tmp` with `TMPDIR` unset; outputs must be byte-identical (same
   `sha256sum`). This is the operational meaning of "no `.scratch` dependency".
8. **Runner pin (to-verify)** — when `reports/round-43/run-validation.py` lands,
   it should (a) invoke `--selftest`, (b) check the resolver's sha256 against the
   pinned value, (c) parse the four-class totals and assert the arithmetic.
   The runner does not exist at the time of writing (`ls` → no such file).

## 7. Discrepancies, collisions, and handoff notes

| ID | Finding | Evidence | Owner / route |
|---|---|---|---|
| F1 | The r43 claim's `before` ("no durable instrument implements the policy"; "the only resolver … is r39 I-C05 in `.scratch`") is contradicted by the tracked r42 extractor and misidentifies I-C05. The durable gap is D2 + four-class census + ambiguous control, not D1. | §0.3, §4.1, §5.1; `7ceff59`; `reports/round-42/validation.json` O passed; `reports/round-39/cov/C05-audit.md:30` | Scribes (`O09`, `S01`) and reviewers (`R01`, `R02`, `X02`) must state the corrected `before`; do not file the stale wording. |
| F2 | Two instruments will cover the same field. Without an authority rule they can drift. | §4.5 | Resolver is census authority; r42 extractor is N6 witness. Record in census header + LOG. |
| F3 | `SKILL.md`'s durable-surface inventory (`:444-454`) lists neither the r42 extractor nor the new resolver; discovery is currently `ls tools/harness/`. | `grep -n couples SKILL.md` → only an unrelated `:531` | Integrator: add two rows to the table (fenced draft below), or record why not. |
| F4 | The landed r39 policy is truncated (107 lines; no §6 body), so a tool that cites "the policy's §6 recipe" cites a non-existent block. | `wc -l -c` → `107 5832`; `sed -n '104,107p'` | Resolver docstring cites the r42 full doc; policy-doc readers cite `reports/round-42/calib/basename-couples-policy-full.md`. |
| F5 | r42 selftest leaves temp dirs (68 in `.scratch`). | §5.2 strace; `ls -d .scratch/tmp* | wc -l` → 68 | New tool: in-memory fixtures. Existing residue is disposable (`.gitignore`), no filed-byte issue. |
| F6 | r43 runner absent, so no digest pin exists yet. | `ls reports/round-43/run-validation.py` → absent | Integrator, step 8; mark `to-verify` until filed. |

Optional `SKILL.md` inventory rows (fenced for the integrator; not applied by
this seat):

```markdown
| `tools/harness/couples-reference-extractor.py` | N6 witness: `couples:` block extraction + hyphen rejoin; `--selftest` / `--census`; historical 223/2730 census recorder; not the r43 census authority | module docstring; `reports/round-42/op/couples-extractor-census.json` |
| `tools/harness/basename-couples-resolver.py` | basename-couples policy authority (r43): Tier-1 direct + Tier-2 fallback, four classes, every fallback mapping, disposition leg; `--selftest` / `--census [--json]` / `[paths]`; read-only | module docstring; `reports/round-43/calib/` census |
```

## 8. Evidence log (commands run for this document)

All read-only; `TMPDIR=$PWD/.scratch`, `PYTHONDONTWRITEBYTECODE=1`, lane root
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

```
$ git log --oneline -3
7ceff59 round-42: NOT ADMITTED on C (O verified) — N6 successor extractor, ...
ac47c78 round-41: admit O/Ca — ...
456674d round-40: final receipt refresh ...

$ git ls-files tools/harness/
tools/harness/couples-reference-extractor.py
tools/harness/packet_links.py
tools/harness/packet_uncertainty.py
tools/harness/r8_checks.py
tools/harness/receipt_guard.py
tools/harness/receipt_guard_adoption.py
tools/harness/round_runner_conformance.py

$ sha256sum tools/harness/couples-reference-extractor.py reports/round-19/audit/entry-audit.py
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1  tools/harness/couples-reference-extractor.py
e7992c325a479aa7415c42722a034a95a9ea342a58367ead9cd2636a5a62830c  reports/round-19/audit/entry-audit.py

$ python3 tools/harness/couples-reference-extractor.py --selftest
PASS wrapped positive 4/4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS wrapped positive heals soft wrap
PASS unwrapped regression
PASS over-capture trap (prose excluded) ['sound-symbolism.md']
PASS phantom negative: absent wrapped targets are visible, not zeroed {'sound-change.md': 'prospective', 'sound-symbolism.md': 'fallback', 'tone-prosody.md': 'prospective', 'writing-systems.md': 'fallback'}
PASS N6 regression guard: single-line capture still yields 0 tokens
PASS N6 regression guard: block read yields 4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS glob fragment classified
exit=0

$ python3 tools/harness/couples-reference-extractor.py --census
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)
  misaligned: none

$ python3 tools/harness/couples-reference-extractor.py corpus/knowledge/linguistics/phonetics-phonology.md
corpus/knowledge/linguistics/phonetics-phonology.md wrapped=True tokens=4
    sound-change.md                  prospective
    sound-symbolism.md               direct
    tone-prosody.md                  prospective
    writing-systems.md               direct

$ (cd /tmp && python3 <lane>/tools/harness/couples-reference-extractor.py --census)
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)
  misaligned: none

$ python3 tools/harness/couples-reference-extractor.py --census | grep -c "fallback.*->"
0

$ grep -n "def couples_targets\|^- couples\|candidates = \|os.path.isfile" reports/round-19/audit/entry-audit.py
74:def couples_targets(text, path):
75:    m = re.search(r"^- couples:\s*(.*)$", text, re.M)
87:        candidates = [
92:        if any(os.path.isfile(c) for c in candidates):

$ wc -l -c reports/round-39/calib/basename-couples-policy.md
107 5832 reports/round-39/calib/basename-couples-policy.md

$ ls -d .scratch/tmp* | wc -l
68

$ python3 --version
Python 3.14.7
```

## 9. Handoff checklist (what the parent can apply without re-deriving)

- [ ] Apply O01's tool body to `tools/harness/basename-couples-resolver.py`
      under the §2 contract (realpath root walk, mutually exclusive modes,
      exit 0/1/2, stdout-only, no `tempfile`).
- [ ] Run `--selftest` (exit 0) and `--census` (four classes + every fallback
      mapping); file the JSON census under `reports/round-43/calib/`.
- [ ] File the r19/r42/new digests in the census header and LOG entry.
- [ ] Add the resolver to the round-43 commit; verify with `git ls-files`.
- [ ] Publish the corrected claim `before` (D1 already fixed by r42; increment
      is D2 + four-class census + ambiguous control + filed artifact).
- [ ] Mark F6 (`to-verify`) until `reports/round-43/run-validation.py` pins the
      resolver digest.
