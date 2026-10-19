# O02 — resolver-edge review: was the O-claim drop correct?

- Seat: `O02` | role: verifier | claim: **cross** (feeds the O drop / next-O premise) | round 48, loop 2, position 2
- Baseline: `a01405d` (`git rev-parse HEAD` → `a01405dd36367292255c2652ac0a601f4cd6a0af`, 2026-10-19); equal to `reports/round-48/claims.json:7`
- Out path: `reports/round-48/op/O02-resolver-edge.md` (this file)
- Non-author statement: I wrote no other round-48 fragment and edited no `corpus/**`, `tools/**`, `reports/round-1..47/**` byte. The resolver and extractor were imported read-only; fixtures were written under `.scratch/o02/`.

**One-line verdict.** The drop is **correct as a dispatch decision** — the premise is a carried, already-filed latent edge with 0/223 live incidence, so O resting costs nothing — but the **stated ground is wrong**: on the declared fixture the pinned resolver really does drop the soft-wrap continuation (`wrapped=False`, `tokens=1`). `reports/round-48/claims.json:19` calls that measurement a refutation ("premise was false as framed"); it is the defect's signature. What the gate actually proved is that its own probe cannot observe the premise: the probe replaces a live selftest input, so the selftest exits 1 for any non-identical fixture, and `measured=False` follows from the exit code, not from resolver behavior.

---

## 1. The declared premise and the declared probe

**Premise** (`.scratch/r48-claims-skel.json:13`, the candidate O `before`):

```
resolver drops blank-separated hyphen soft-wrap tokens (latent edge)
```

**Probe** (`.scratch/r48-freshness-check.json:38-59`):

| Field | Value |
|---|---|
| `clause` | `resolver blank-hyphen edge` |
| `probe_kind` | `capability_present` |
| `globs` | `tools/harness/basename-couples-resolver.py` |
| `argv` | `["--selftest"]` |
| `fixture` | replaces `corpus/knowledge/linguistics/phonetics-phonology.md` |
| fixture bytes | `- couples: a — `x.md`; prospective sibling files: tone-\n\n  prosody.md\n` (verified by loading the JSON, `repr` exact) |
| `success_regex` | `drops\|0 tokens\|prosody` |
| `expect` | `true` |

**Replayed gate output** (`.scratch/o02/gate.json`, command in §8):

```
[C] FRESH   2/2 clauses hold
[O] STALE   1/1 clauses contradict
    clause 0 (capability_present): measured=False expected=True -- resolver blank-hyphen edge
    reason: 0/1 candidate(s) pass the declared behavior
[Ca] FRESH  1/1 clauses hold
REFUSE: claim(s) O have a `before` already false at a01405d; do not dispatch.
exit 1
```

The round record's reading of that verdict is `reports/round-48/claims.json:19` ("its 'resolver drops hyphen soft-wrap' premise was false as framed — the resolver yields wrapped=False tokens=1, a different edge") and `reports/round-48/telemetry/dispatch-declared.json:18-20` ("O STALE (candidate premise false …)"). Both treat the probe result as a fact about the premise. §2 measures the premise directly.

---

## 2. Direct measurement of the premise

### 2.1 The exact declared fixture, through the pinned resolver

Imported `tools/harness/basename-couples-resolver.py` (sha256 `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64`, identical to the r47 pin) and called its public functions on the fixture bytes above:

```
parts      = ['a — `x.md`; prospective sibling files: tone-']
wrapped    = False
joined     = 'a — `x.md`; prospective sibling files: tone-'
field_refs = ['x.md']
```

`x.md` survives; the continuation `prosody.md` — which `join_parts` should heal to `tone-prosody.md` (`:83-99`) — is **dropped**, and the field is reported as not wrapped. That is the declared premise, reproduced exactly. `wrapped=False tokens=1` is not a counter-example; it is the drop seen from the field level: the block terminated at the blank line, so the resolver believes it read a complete one-token field.

The code reason is unchanged from the r47 record (`reports/round-47/calib/queue-successor-r47.json:93`): at `tools/harness/basename-couples-resolver.py:73`,

```python
soft_wrap = parts[-1].endswith("-") and not saw_blank
```

so the guard at `:74` (`not saw_blank or soft_wrap`) is equivalent to `not saw_blank`; after a blank line the hyphen exception is unreachable. The docstring at `:55-59` still promises the exception.

### 2.2 The same fixture, through the census extractor — the control

```
$ python3 -B tools/harness/couples-reference-extractor.py .scratch/o02/hyphen_blank.md
.scratch/o02/hyphen_blank.md wrapped=True tokens=2
    tone-prosody.md                  prospective
    x.md                             prospective
```

`tools/harness/couples-reference-extractor.py:50-73` skips blank lines instead of terminating on them, so the operative census tool **heals the soft wrap** and loses nothing. The two tools named "resolver" are not interchangeable:

| Tool | sha256 | fixture result | baseline census |
|---|---|---|---|
| `basename-couples-resolver.py` | `43ce341f…` | `wrapped=False tokens=1` (drop) | `refs=2730 direct=2556 fallback=166 ambiguous=0 unresolved=7 glob=1` |
| `couples-reference-extractor.py` | `d8d23a26…` | `wrapped=True tokens=2` (no drop) | `refs=2730 direct=2556 fallback=166 unresolved=2 prospective=5 glob=1` |

The census totals agree (2730) but the class vocabulary does not (`unresolved=7` vs `unresolved=2 + prospective=5`), which is the second place the word "resolver" is ambiguous. A premise written "the resolver drops …" without naming the tool is under-specified even when its behavior clause is true.

### 2.3 Continuity with the r47 measurement

r47's fixture had no leading complete token (`language — `tone-` + blank + `  prosody.md``). Re-run at this baseline:

```
parts  = ['language — `tone-']
tokens = set()
```

`tokens=0`, matching `reports/round-47/calib/queue-successor-r47.json:96` ("field_refs returns []"). The r48 fixture adds `x.md`, so the same defect reads `tokens=1`. Same branch, same drop; only the fixture's leading token changes the count.

### 2.4 Live incidence at a01405d

Scan of all 223 entries for the trap shape (a `- couples:` block, then a blank line, then an indented continuation whose preceding part ends in `-`):

```
blank-separated hyphen continuation hits: 0
```

0/223, reproducing r47's scope. The edge is latent, not live.

---

## 3. Why the gate returned `measured=False`

`_probe_capability_present` requires **both** a zero exit and a regex hit (`tools/harness/claims-freshness.py:1180`):

```python
matched = proc.returncode == 0 and success.search(output) is not None
```

The declared probe materializes its fixture *over a live selftest input* (`corpus/knowledge/linguistics/phonetics-phonology.md`), then runs `--selftest`. The resolver's selftest asserts that the live file equals an embedded constant (`tools/harness/basename-couples-resolver.py:272-273,302,325`). Replaying the probe tree manually:

```
$ python3 -I -B tools/harness/basename-couples-resolver.py --selftest
rc=1
FAIL S1a embedded fixture == live bytes at :1  [live_line=1]
FAIL S1f live field resolves 2 direct + 2 unresolved (four-class policy)
FAIL S4a Tier-1 direct wins over a same-basename hit elsewhere (5.4)
FAIL S4b direct carries no fallback mapping
FAIL S4c corpus-relative path token -> direct (Tier-1 base 3)
FAIL S10 live wrapped entry reads 4 tokens (2 direct + 2 unresolved)
SELFTEST FAIL: 21/27 controls
```

So the fixture forces 6 control failures **before any blank-line behavior is exercised**. Any fixture content short of the original 6-line field fails `S1a`; the only fixture that passes is byte-identical to the live file, which cannot exercise the shape. The probe is self-defeating: it is guaranteed to return `measured=False` whether the defect exists or not.

There is a second, independent flaw. The success regex `drops|0 tokens|prosody` asks a *passing* (exit-0) run to print the words "drops" or "0 tokens". A resolver that drops tokens cannot both succeed and announce it; the resolver has no control for this shape at all (`S2b` at `:359` is a non-blank hyphen wrap; `S7c` at `:411-415` is a blank line without a hyphen). The regex would only match a run that documents the defect while exiting 0 — a control the tool does not contain.

Therefore the gate's `CONTRADICTED` means "the declared probe could not pass", not "the premise is false at the baseline". The gate did what its contract says; the probe specification is what failed.

---

## 4. Verdict on the O drop

| Question | Measurement | Verdict |
|---|---|---|
| Does the declared premise reproduce on the pinned resolver? | `wrapped=False tokens=1`, continuation dropped (§2.1) | **YES — premise true for `basename-couples-resolver.py`** |
| Does it reproduce on the operative census extractor? | `wrapped=True tokens=2` (§2.2) | **NO — the census path does not drop** |
| Is the defect live? | 0/223 trap shapes (§2.4) | **latent; 0 incidence** |
| Is it already filed? | `r44-resolver-hyphen-after-blank`, class `recorded`, `v2_class_equivalent: carried-with-owner`, owner "next resolver touch — tools/harness maintainer", explicit `next_touch` options (a) docstring correction + control or (b) drop `and not saw_blank` + control (`reports/round-47/calib/queue-successor-r47.json:88-96`) | **yes — carried with an owner** |
| Was the gate's `STALE` mechanically reproduced? | `measured=False expected=True`, REFUSE, exit 1 (§1) | **yes, reproduces** |
| Does `measured=False` prove the premise false? | the probe is self-defeating (§3) | **NO** |
| Is dropping O correct? | it duplicates a carried row; no round move is lost; O is not in `axes_in_play` (`reports/round-48/claims.json:15-18`) | **YES as a dispatch decision — but not for the reason recorded** |

So: **O resting this round is right; the sentence explaining it is wrong.** The correct explanation is: *the premise as framed does not name which resolver, the gate’s probe could not measure it, and the defect is already dispositioned with an owner and a next touch — so O rests rather than re-litigate a carried row.* The record must not say the resolver does not drop, because it does.

This matters because `claims.json:19` and the telemetry note are upstream of `LOG.md`, and `AGENTS.md` requires that unverifiable or wrong claims not be recorded as facts. `wrapped=False tokens=1` should never be cited as evidence *against* a drop; it is the drop's field-level signature.

### 4.1 What "different edge" could have meant, and why it is still not falsity

The only defensible reading of "a different edge" is: the r47 record described `field_refs -> []` (2 tokens dropped), while the r48 fixture yields `tokens=1`. That is a difference in the fixture's leading token, not in the branch (§2.3). It does not make the premise false, and it does not justify the word "false". If the intent was "the census tool does not drop", the premise needed to say so explicitly.

### 4.2 Cross-seat check (filed concurrently)

- `reports/round-48/op/O01-gate-live.md:188` reaches the same distinction independently: "The **drop** half is true: one reference is silently lost and the record says `wrapped=False`. A premise worded literally as 'the resolver drops blank-separated hyphen soft-wrap tokens' would therefore measure TRUE and pass." O01 also flags that the original candidate bytes are not durably filed, so *which* framing was dispatched is `to-verify`; I confirm I could only measure `.scratch/r48-claims-skel.json:13` plus the declared overlay, both scratch-resident.
- `reports/round-48/op/O04-gate-replay.md:116` states "The premise 'the resolver drops hyphen soft-wrap' is false". That is the same overstatement I am correcting: O04's own measurement one line earlier is `wrapped=false`, one token — the drop. O04-F3 (`O04:217`) correctly identifies the probe as unable to confirm the edge; its wording should not be carried forward as "premise false".
- All three seats agree on the mechanism (dead branch at `:73`; probe cannot measure it). Only the *classification sentence* differs; §5 is the wording I recommend so the record does not enter `LOG.md` with three versions.

---

## 5. Draft correction for the round record (fenced; integrator applies)

`reports/round-48/claims.json:19` currently reads (excerpt):

```
the candidate O claim STALE (its 'resolver drops hyphen soft-wrap' premise was false as framed — the resolver yields wrapped=False tokens=1, a different edge), so O rests this round rather than dispatch a stale claim
```

Draft replacement for that parenthetical:

```text
the candidate O claim was refused at declaration: the defect premise reproduces on the pinned
`basename-couples-resolver.py` (wrapped=False, tokens=1, continuation dropped) but not on the
operative `couples-reference-extractor.py` (wrapped=True, tokens=2); the declared probe could not
measure either (`--selftest` fails 6/27 controls when its live input is replaced, so measured=False
follows from the exit code). The edge is already filed as `r44-resolver-hyphen-after-blank`
(recorded, carried-with-owner, 0/223 live incidence) with a named next touch, so O rests rather
than re-litigate a carried row. See `reports/round-48/op/O02-resolver-edge.md`.
```

Draft replacement for `reports/round-48/telemetry/dispatch-declared.json:18-20` `result`:

```text
O STALE as declared (probe could not measure the premise; see op/O02-resolver-edge.md §3);
C FRESH; Ca FRESH. O rests because the edge is carried with an owner, not because the premise
is false — the pinned resolver does drop the continuation.
```

Both are successor-style corrections to this round's own uncommitted declaration, not edits to filed bytes. I did not apply them.

---

## 6. Tested probe shape for the next O round (for O03 / O04 / gate maintainer)

The defect **is** measurable with the gate's existing `capability_present` vocabulary if the fixture is given a fresh path instead of replacing a live selftest input. Verified in a temp tree:

```
fixture: corpus/knowledge/_probe/fixture.md   (same bytes)
argv:    ["corpus/knowledge/_probe/fixture.md"]
output:  corpus/knowledge/_probe/fixture.md wrapped=False tokens=1
         x.md  unresolved  dangling-reference
exit:    0
```

A `success_regex` of `wrapped=False tokens=1` matches, and the extractor on the identical file prints `wrapped=True tokens=2` — a clean discriminating control. This yields the premise as a measured fact:

```text
before: "basename-couples-resolver.py reads a blank-separated hyphen continuation as an
unwrapped single-token field (wrapped=False, tokens=1), dropping the continuation"
```

Recommended next-O shape (premise only, not a claim this round): name the tool, state the observed
`wrapped`/`tokens`, and scope incidence to 0/223. A proposed successor row for the gate itself —
class `recorded`, owner the freshness-gate maintainer, evidence `tools/harness/claims-freshness.py:1129-1196` plus this file — belongs to the Ca02/Ca06 disposition seats, not to me; I flag it rather than file a competing row.

---

## 7. What I did not verify

- Whether an O round on this edge would be *accepted* as a move; my verdict is only that the premise is verifiable and the drop's recorded reason is wrong.
- The `S1a`-under-fixture behavior for any tool other than the two measured. The general claim ("a live-input selftest fixture is self-defeating") is supported by this one tool's 6 failures, not exhaustively across the harness.
- The census class-vocabulary divergence (`unresolved=7` vs `2+5`) beyond reporting it; it is not part of the O premise.
- The r44 originals (`reports/round-44/cross/X01-trades.md`, `op/O03-defects-verify.md`) were not re-read this round; I relied on the r47 row's quotations and my own measurements.

---

## 8. Commands and write surface

All commands from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

```text
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ sha256sum tools/harness/basename-couples-resolver.py tools/harness/couples-reference-extractor.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64  basename-couples-resolver.py
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1  couples-reference-extractor.py

# §2.1 resolver on the declared fixture (import + call)
parts = ['a — `x.md`; prospective sibling files: tone-'] ; wrapped = False ; field_refs = ['x.md']

# §2.2 extractor control
$ python3 -B tools/harness/couples-reference-extractor.py .scratch/o02/hyphen_blank.md
.scratch/o02/hyphen_blank.md wrapped=True tokens=2   (tone-prosody.md, x.md)

# §2.3 r47 shape
parts = ['language — `tone-'] ; tokens = set()

# §2.4 live incidence
blank-separated hyphen continuation hits: 0        (223 files scanned)

# §3 probe replay (fixture replacing the live input)
$ python3 -I -B tools/harness/basename-couples-resolver.py --selftest
rc=1 ; SELFTEST FAIL: 21/27 controls ; FAIL S1a, S1f, S4a, S4b, S4c, S10

# §1 gate replay
$ python3 -B tools/harness/claims-freshness.py --claims .scratch/r48-claims-skel.json \
      --checks .scratch/r48-freshness-check.json
[O] STALE 1/1 clauses contradict ; REFUSE ; exit 1

# §6 corrected probe shape
$ python3 -I -B tools/harness/basename-couples-resolver.py corpus/knowledge/_probe/fixture.md
corpus/knowledge/_probe/fixture.md wrapped=False tokens=1 ; exit 0

# control selftests at baseline
$ python3 -B tools/harness/basename-couples-resolver.py --selftest   -> SELFTEST OK: 27/27, exit 0
$ python3 -B tools/harness/basename-couples-resolver.py --census     -> entries=223 refs=2730
$ python3 -B tools/harness/couples-reference-extractor.py --census   -> entries=223 refs=2730
```

**Write surface:** this file only — `reports/round-48/op/O02-resolver-edge.md`, plus disposable fixtures and the gate JSON under `.scratch/o02/`. No `corpus/**`, `tools/**`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged; no git commit/push, no install, no network; no `reports/round-*/run-validation.py` executed. `git status --porcelain` at my write cut shows only the pre-existing `?? reports/round-46/review/` and `?? reports/round-48/`.

**No axis is harmed.** Calibration is improved by correcting the record's reason; coverage and operability are untouched by anything on disk.
