# R28-O39..O40 — adversarial review of the round-28 law replay leg, RL-4 fix and final pin sweep

- **Seat:** O, round-28 claims **R28-O39..O40** (reviewers x2), assignment verbatim:
  "adversarial".
- **Date:** 2026-10-18. Observation window **20:11Z–20:27Z** (all stamps from
  `date -u --iso-8601=seconds`; `python3` 3.14.7). Lane HEAD
  `69cecbc7dcf575a29f29660ecac470e05260fd86` (round-28 declaration, 17:10:20−03:00);
  declared baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`
  (`reports/round-28/claims.json:5`).
- **Write scope:** this file only. Scratch under `.scratch/r28-o39/` (gitignored,
  lane-internal); `export PYTHONDONTWRITEBYTECODE=1` preceded every scratch-writing
  command. **`TMPDIR` was set outside the repo for every `replay-frozen` run** —
  `/tmp/r28o39` until that tmpfs hit its quota at 20:12, then `/var/tmp/r28o39`
  (see §6, which is the reason the trap matters). No git commit or push. No filed
  round-8–27 byte, tool, gate, packet or shared bookkeeping was edited by this seat.
- **Canon:** NON-CANON engineering evidence. This review admits nothing, certifies
  no round, and adjudicates no claim. It measures the three claims against their own
  `after_required` text and reports what it found.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | **A filed round-27 artifact was rewritten in place mid-wave** — `reports/round-27/gate-tests/receipt.json` moved `854ed1a3…` → `fbc1f4b6…` (mtime 20:12:33Z, inside the 20:10Z dispatch window) and its verdict flipped `passed: true, 55/55` → `passed: false, 42/55`. Restored to the baseline blob by 20:14:42Z. Round-28's own runner and two audit seats independently record it. | **measured — protected-surface breach, healed** |
| 2 | **The replay leg grades the LIVE tree, not the pinned snapshot.** Rows 2 and 3 of `tools/gates/frozen/round-26/post-register/MANIFEST.tsv` pin `dd25077b…` / `618a78c9…` and recorded `3eb9042e…` / `67056bb9…`, yet both replay `mismatch` (exit 2 vs recorded 0) with messages that cite the **live** assembly (`543d68a8…`) rather than either pinned digest. Two symptoms, one cause: at 20:12Z both rows emitted **one identical** output digest `484e5b25…` (a collision — different pins, same bytes); after the round-28 profile re-pin the collision is gone and each row emits its own mismatch, still citing the live tree. | **measured — instrument defect, pre-existing** |
| 3 | **RL-1 is closed for `force`, only partly for `speaker`.** The delivered leg fires a named `D4L-LAW-FORCE` on `force: "no-such-force"` (control: silent on the clean packet). But round-27's own RL-1 tamper shape — `speaker: "no-such-speaker"`, a **speaker class with no `(ID)` token** — still emits **byte-identical findings** to the clean packet (4 vs 4). Speaker *classes* are never resolved; only `Name (ID)` tokens are. | **measured — partial closure** |
| 4 | **RL-4 is fixed for the eight named records, and partial beyond them.** `03-orthography.yml` and `09-costumes.yml` now declare `packet_keys`; `records`, `literacy_institutions` and `enforcement` are packet blocks; all eight ids (`OR-01..03`, `LI-01..03`, `EN-01..02`) are present as `id:` rows; records went 175 → 183. `signs` (20 rows) and `orthography_rules` (7) still do not reach the packet. | measured |
| 5 | **The clean packet exits 1, and nothing gates it.** `register-law-gate.py` on the delivered packet emits four `D4L-LAW-DANGLING` HOLDs (`QREG-05..08` name rows that never landed) and exits 1. Disclosed in the gate's own calibration, but the gate appears in **no** regression label — the runner's 35 labels include none naming it — so its exit is never read. The claim's "D4 typed gate + argot gate + assemblers green" is true and does not extend to the new law leg. | measured |
| 6 | **Filed rounds 8–27 are byte-clean at this stamp**: 1 793 protected paths, **0 changed, 0 missing**, by `git hash-object` against the baseline blob. The round-28 runner's own `protected_filed_artifacts` leg agrees (`passed: true`). | measured |
| 7 | **The runner now reads green** (`acceptance_checks_passed: true`, D/O/C all `passed: true`) at 20:23Z — and it was red on all three claims 8 minutes earlier at 20:15Z. Both readings carry their stamp; the movement is the round landing, not a defect. | measured |

**Bottom line for the parent.** The three claims' *shape* is right and, at the closing
stamp, the runner agrees. Three findings cut against the product. **(i)** The new law leg
resolves only `Name (ID)` tokens, so the round-27 defect it exists to close is closed
for `force` and for `consequence` but **not** for the speaker *class* — the delivered
leg cannot tell `speaker: "no-such-speaker"` from a clean row, which is precisely the
RL-1 probe round 27 filed. The claim's wording ("speaker classes resolve against
delivered records") is stronger than the delivered code. **(ii)** A separate,
**pre-existing** defect makes the frozen-replay leg unable to evaluate its own pinned
rows: `tools/replay-frozen.py` copies only the gate script and the pinned snapshot into
its mirror, but `typed-pipeline-gate.py` resolves `ROOT` from its own file location and
loads peers and live `examples/` bytes the mirror cannot hold — so the gate refuses with
a message about the **live** assembly, and an environmental refusal is surfaced as a
content `mismatch` (exit 1) rather than as could-not-evaluate (exit 2). **(iii)** The O
claim's "all replays green" clause is measured against a set that **excludes the
manifest leg**: the runner gates four labels, none of which replays a frozen manifest,
while the sweep's own family-A table records 11 of 12 generations non-zero. The clause
passes without touching the leg that is red. Findings (ii) and (iii) together mean the
lane currently has **no green reading of its frozen-replay surface at all** — not
because the round failed, but because the instrument that would report it is either
unable to evaluate (ii) or not asked (iii).

## 1. The filed-byte breach, measured and healed

At 20:11:13Z the round-28 declaration commit was a clean successor: `git status` was
empty and `git diff --name-status 6c0ac44 HEAD` added only
`reports/round-28/{claims,targets}.json`.

At 20:13:33Z the working tree carried:

```
 M reports/round-27/gate-tests/receipt.json
```

The file's writer is its own re-runner, `reports/round-27/gate-tests/run-gate-tests.py:820`:

```python
receipt_path = HERE / "receipt.json"
receipt_path.write_text(...)
```

so re-running a filed round-27 instrument **overwrites its own filed receipt in place**.
The verdict did not survive: at baseline the receipt read `passed: true`,
`{checks: 55, passed: 55, failed: 0}`; at 20:13:19Z it read `passed: false`,
`{checks: 55, passed: 42, failed: 13}`, because the D4 packet had moved under it
(`FAIL L1-profile: packet: pins 86079a6708a0, live 543d68a82640`). A filed round-27
artifact therefore read as a *failed round-27 receipt* for roughly two minutes.

Independent records of the window (this seat did not create them, and they were written
by seats that also observed it):

| instrument | reading |
|---|---|
| `reports/round-28/validation.json` (20:13:51Z) | `protected_filed_artifacts.measurement.differences` names this path and no other: `baseline_blob 854ed1a3… / observed_blob fbc1f4b6…` |
| `reports/round-28/adjacency.md` §1 | records the window, the writer (line 820) and the restore |
| `reports/round-28/audit/x60-sweep-completeness.md` X60-F5 | "a filed round-27 artifact was rewritten in place during round 28 … then was restored to its baseline bytes" |
| `.scratch/x51/watchlog28.json` | samples at 20:11:22Z / 20:12:22Z clean; 20:13:22Z / 20:14:22Z flag the path |
| this seat's own harness | `git hash-object` ≠ baseline blob at 20:13Z; equal again at 20:16Z |

**Restored at 20:14:42Z** (mtime), blob-identical to the baseline: `git hash-object` →
`854ed1a37805a7f848ca2d17e8f005a34788b592` = `git rev-parse 6c0ac44:reports/round-27/gate-tests/receipt.json`.
At the closing stamp (20:24Z) this seat re-measured all 1 793 protected paths: **0 changed,
0 missing**. The end-of-round tree is clean on this path.

**Why it still matters.** The lane rule is "re-pins are NEW rows"; a re-run that writes
its receipt back to the filed path violates it by construction, and the *only* reason no
filed byte survives the breach is that someone noticed and restored it. `round-27/gate-tests/run-gate-tests.py`
remains a live hazard: any later seat that re-runs it re-breaches the same path. Round 28
fixed this for itself (`reports/round-28/gate-tests/run-gate-tests.py` writes
`reports/round-28/gate-tests/receipt.json`) but did not retire or annotate the round-27
runner. **A one-line guard in the filed runner, or a note in the round-27 receipt, would
close the hazard; neither is present.**

## 2. The load-bearing instrument finding — the replay leg grades the live tree

### 2.1 The reading

Replaying `tools/gates/frozen/round-26/post-register/MANIFEST.tsv` (`TMPDIR=/var/tmp/r28o39`)
at **20:12Z**, before the round-28 profile re-pin:

| row | pinned input | pinned `input_sha256` | recorded output | recorded `output_sha256` | observed output | observed exit |
|---|---|---|---|---|---|---|
| 2 | `examples/culture-d4/packet.d4.yml` | `dd25077bc01681bc…` | `d4-source.out` | `3eb9042e066426fd…` | **`484e5b259f93fa26…`** | 2 |
| 3 | `examples/culture-d4/packet.d4.typed.yml` | `618a78c90fc04c0d…` | `d4-typed.out` | `67056bb9090e437d…` | **`484e5b259f93fa26…`** | 2 |

Two rows with **different pinned inputs and different recorded outputs** observed **one
identical output digest**. That is arithmetically impossible if each row ran against its
own pinned snapshot: the two snapshots are distinct files with distinct digests
(`dd25077b…` and `618a78c9…`, both verified on disk), and the recorded outputs are
distinct (`3eb9042e…` and `67056bb9…`).

**At 20:26Z, after the round-28 profile re-pin, the collision is gone and each row emits
its own digest** (`b261866cf0abea7a…`, `1594cef724937a33…`) — **but both rows still
mismatch**, both still exit 2 against a recorded 0, and the failure message still cites
the live tree. The collision was one *symptom*; the cause survives it.

### 2.2 The cause

`tools/replay-frozen.py:175-196` builds a mirror holding only the pinned gate and the
pinned snapshot, then launches the gate with `cwd=mirror`. `typed-pipeline-gate.py:78`
resolves its root from its **own** location:

```python
ROOT = Path(__file__).resolve().parent.parent.parent
```

and `replay-frozen.py` launches the gate by its **repository** path, so `ROOT` is the
live lane, not the mirror. The gate therefore reads the live `tools/gates/typed-pipelines.json`
profile and the live `examples/culture-d4/` bytes, and refuses. Measured at 20:26Z, running
the **pinned snapshot** with the gate on its repo path (cwd outside the repo):

```
declared pipeline: family d4; profile tools/gates/typed-pipelines.json (sha256 7f5a9c722a5c); …
ok   L3b-argot:
ok   L1-profile:
FAIL L1-assembler: packet bytes dd25077bc016 are not tools/assemble-culture-d4.py's deterministic assembly (543d68a82640)
```

The message names the **pinned** snapshot (`dd25077b…`) and the **live** assembly
(`543d68a8…`) in one line. That is the defect in a sentence: the input is pinned, the
reference it is judged against is live. At 20:12Z the same mechanism produced the
`L1-profile` variant, whose text is a function of the live packet and projection digests
alone — which is why both rows emitted identical bytes then. **Controls, both directions:**

| control | result |
|---|---|
| the two pinned snapshots on disk | distinct digests `dd25077b…` / `618a78c9…` |
| the two recorded outputs on disk | distinct digests `3eb9042e…` / `67056bb9…` |
| the two observed outputs at 20:12Z | **identical** `484e5b25…` |
| the two observed outputs at 20:26Z | distinct (`b261866c…`, `1594cef7…`) — but both still mismatch |
| copy the pinned snapshot outside the repo, run the gate with `cwd` there, gate on its **repo** path | exit 2, same live-assembly message |
| copy the **gate** into the mirror so `ROOT` = mirror | different failure (`L1-assembler: assembler unreadable`), proving the gate's `ROOT` is what changed the reading |
| the D2 rows 4–7 in the same manifest | `reproduced`, distinct digests each — **because the live D2 packet is byte-identical to its pin** (`e0f21509…` at both), so the defect is invisible there and the row passes by coincidence, not by design |

### 2.3 The misclassification

`replay-frozen.py` reports both rows as `reason=replay_mismatch`, `status=mismatch`,
exit 1 (unchanged at 20:26Z):

```
ROW 2 mismatch reason=replay_mismatch … exit=2/0 count=0/12 bytes=differ launched=yes
  detail: exit code 2 != recorded 0; finding count 0 != recorded 12; output bytes differ from the recorded output
```

The gate's exit 2 is its own **input-class refusal** ("could-not-evaluate"), and the
replay tool's contract reserves exit 2 for exactly that class. Surfacing it as a content
`mismatch` tells a reader "the gate now disagrees with its record", when what actually
happened is "the gate could not be evaluated in this mirror". Round 28's own sweep
inherits the reading: `reports/round-28/sweep/_prelanding-census.md` lists these rows
under `MANIFEST-INPUT-MOVED`, and `reports/round-28/audit/x60-sweep-completeness.md`
X60-F6 discloses the resulting ambiguity — "the TMPDIR trap is currently masked by an
upstream red".

### 2.4 Scope, and the clause the runner does not gate

The affected rows are every manifest row whose gate resolves `ROOT` and loads peers —
i.e. all `typed-pipeline-gate.py` rows over a family whose live packet differs from its
pin. Measured across the lane:

| manifest | typed-pipeline rows | reading |
|---|---:|---|
| `round-26/post-register` | 2 | both `mismatch`, exit 2 vs 0 |
| `round-26/gate-input` | 2 | both `mismatch`, exit 2 vs 0 |
| `round-18`, `round-22/d4-repin` | 2 each | both `mismatch` (`e3b0c442…` empty at 20:12Z) |
| `round-25/gate-input` | 6 | all `could-not-evaluate` (a different, honest class) |
| D2 rows (4–7 in round-26) | — | reproduce — live D2 == pin, so by coincidence |

**The runner's `replays` clause does not cover the manifest leg at all.** Round-28's
runner gates four labels —

```python
replay = {label: label_run(regressions, label).get("exit") for label in
          ("replay-selftest", "handoff-v2", "handoff-v3-selftest", "handoff-v3")}
```

— all four of which are handoff-profile and selftest legs, **none of which replays a
frozen manifest**. The `O` measurement's `sweep` block carries `drift`/`green`/row counts
but **no `replays` key**. So the `after_required` clause "all replays green" is measured
against a set that excludes the leg this section shows to be red: the sweep receipt's own
family-A table records **11 of 12 manifests non-zero** (`round-17` exit 0; everything else
1 or 2), and no O failure names it. This is the sharpest form of the finding — not that
the replays are red, but that the claim's replay clause and the lane's replay leg are
**different sets**.

**This defect predates round 28.** `reports/round-27/pinsweep/sweep-receipt.json`
records the same shape on the same rows (`observed_exit: 2`, recorded 0), and the
round-26 generations have been replaying red since the packet moved in round 27. It is
reported here because it is the reason the "all replays green" clause cannot be read at
face value, and because the round-27 adversarial seat named the same class of complaint
about this runner one round earlier.

## 3. RL-1: closed for `force` and `consequence`, open for the speaker class

The delivered leg is `tools/gates/register-law-gate.py`. **It was revised mid-wave**
(`cfbff16bbb67d94d…` → **`bbad35784bfb463d…`** at ~20:27Z); this seat re-ran every tamper
against **both** revisions and the readings below are identical on each — the speaker
finding is not an artifact of one revision. `--selftest` is 33/33 on both. This seat
re-ran every tamper itself against the delivered packet rather than trusting the
selftest's own fixtures.

**What fires (control in both directions — silent on the clean packet, fires on the tamper):**

| tamper | observed |
|---|---|
| `force: "no-such-force"` on RGL-02 | **fires** `D4L-LAW-FORCE` FAIL, names the row and the value; clean packet: `force_failures=0` |
| `consequence` on a binding act (RGL-01) replaced with `"zzz no machinery at all"` | **fires** `D4L-LAW-CONSEQUENCE` FAIL; clean packet: `consequence_failures=0` |
| `(RK-03)` → `(RK-99)`, `(OR-02)` → `(OR-99)` | **fires** `D4L-LAW-SPEAKER` FAIL; clean packet: `speaker_failures=0` |
| `speaker: "nonexistent (ZZ-99)"` | **fires** `D4L-LAW-SPEAKER` FAIL |

**What does not fire — the RL-1 gap.** `AGENT_ID_RE = re.compile(r"\(\s*([A-Z]{2,4}-\d{2,3})\b")`
(`register-law-gate.py:134`) resolves only bracketed `Name (ID)` tokens. A `speaker`
value carrying **no token** is never resolved against anything. Measured, all with the
clean packet's own 4 findings as the control:

| tamper | findings | non-dangling | verdict |
|---|---:|---:|---|
| clean control | 4 | 0 | — |
| **`speaker: "no-such-speaker"`** (round-27's own RL-1 shape) | **4** | **0** | **no teeth** |
| RGL-01 speaker class → `"utter-nonsense-class"` | 4 | 0 | no teeth |
| RGL-02 speaker class → `"utter-nonsense-class"` | 4 | 0 | no teeth |
| RGL-03 speaker class → `"utter-nonsense-class"` | 4 | 0 | no teeth |
| all five speaker values → `"utter-nonsense-RGL-0n"` | 4 | 0 | no teeth |

The claim's `after_required` reads "**speaker classes resolve against delivered
records**". The delivered leg resolves **`Name (ID)` tokens**, not speaker classes. The
speaker vocabulary the law actually uses — `stamp-holder`, `furnace-master`, `broker`,
`market-goer`, `mold-keeper`, `no master, no delegate`, `any speaker admitted by RGL-01
or RGL-03` — is free prose and is unconstrained. A reader of the claim would expect the
round-27 probe (`speaker: "no-such-speaker"`) to be caught; it is not.

**The runner shares the gap, and this is the sharpest way to state it.** Round-28's
runner builds its own speaker tamper (`run-validation.py:648-651`):

```python
if mutation == "speaker":
    pattern = re.compile(r"(?m)^(\s*)speaker:\s*(.+)$")
    return pattern.sub(lambda m: f'{m.group(1)}speaker: "nobody-nowhere (ZZ-99)"', …)
```

`"nobody-nowhere (ZZ-99)"` **keeps an ID token**, so it fires — and the runner's three
tampers therefore all pass. The runner never plants the token-less shape that round 27
filed as RL-1. So the claim closes on the runner's instrument and stays open on the
tamper the round-27 review actually measured. The gate's own `--selftest` does the same:
its `speaker-tamper` fixture is `"nobody-nowhere (ZZ-99)"` (`register-law-gate.py:411`).

**Honest counterweight.** The gate's docstring declares the limit as craft policy: "a
`Name (ID)` token must name an id the packet carries as a record". A leg that resolved
free-prose classes would need a declared class vocabulary the packet does not carry
(round-28's own audit X59-F5 measured `force_vocabulary=0`, and the gate solved the
analogous `force` problem by **declaring a closed set in the tool**). The same move is
available for speakers and was not made. This is a named design limit, not a silent one —
but the claim's wording does not carry the limit.

## 4. RL-4: the eight named records land, the rest still do not

Measured on the delivered bytes at 20:14Z:

| reading | before (round-27 close) | after |
|---|---|---|
| `03-orthography.yml` `packet_keys` | absent (fell back to the allowlist) | `[orthography, records, literacy_institutions]` |
| `09-costumes.yml` `packet_keys` | `[costumes, materials, cloth_sources, rank_rules, form_slots]` | `+ enforcement` |
| packet blocks | — | `records`, `literacy_institutions`, `enforcement` now top-level |
| `OR-01..03`, `LI-01..03`, `EN-01..02` as `id:` rows | 0 of 8 | **8 of 8** |
| argot `records=` | 175 | **183** (+8) |
| `assembly.skipped_keys` | carried `records`, `literacy_institutions`, `enforcement` | those three moved out |

So RL-4 is **closed for the eight records the round-27 review named** — verified by id
presence as records, not by prose cross-reference, which is what the claim requires.

**Partial beyond them**, disclosed by round 28's own `adjacency.md` §4.1 and confirmed
here: `signs` (20 rows, `SG-01..20`) and `orthography_rules` (7 rows, `WR-01..07`) are
still component-only and reach no packet block. That is 27 further rows of the same class
the claim repairs. The claim scopes itself to `OR/LI/EN`, so this is not a claim failure —
it is the ceiling the round leaves, and a later round that wants the orthography
component whole owes those two keys.

## 5. Claim-by-claim reading against `after_required`

| claim | clause | reading |
|---|---|---|
| **D** | law gains a replay/checking leg | **landed** — `tools/gates/register-law-gate.py`, `D4L-LAW-*` ids present, `--selftest` 33/33 |
| **D** | the law leg is a *green* regression | **not landed** — the clean packet exits **1** (4 `D4L-LAW-DANGLING` HOLDs); the gate is in **no** regression label (35 labels, 0 naming it), so the runner never reads its exit |
| **D** | forces against a declared vocabulary | **landed** — `force` fires on `no-such-force`, control silent on clean |
| **D** | consequences against the roll/rank machinery | **landed** — fires on a binding act's stripped consequence, control silent |
| **D** | **speaker classes resolve against delivered records** | **partial** — resolves `Name (ID)` tokens only; a token-less speaker class is unchecked (§3) |
| **D** | a tampered row is a named finding | **partial** — true for force/consequence/token; **false** for the RL-1 token-less speaker probe |
| **D** | RL-4 fixed | **landed for OR/LI/EN**; 27 further rows still component-only (§4) |
| **D** | D4 typed gate + argot gate + assemblers green | **landed** — `typed-pipeline-gate.py` 20/20 and 17/17, `argot-derivation-gate.py` exit 0, both assemblers `--check` byte-identical |
| **D** | RL-3 ceiling recorded as a design constraint | **landed** (claim C) |
| **O** | every frozen/baseline/replay surface re-verified | **partial** — the manifest replay leg cannot evaluate its own D4 rows (§2); the sweep's *other* families do read |
| **O** | drifted rows re-pinned as NEW rows | **landed** — `reports/round-28/sweep/repin-rows.json` carries 22 rows over 17 surfaces, all under `reports/round-28/`; 0 filed bytes touched |
| **O** | battery 9/9 | **landed** — `pass 7 / fail 0 / unevaluable 0`, coverage 9/9, 19 baselines pinned |
| **O** | all replays green | **not met, and not measured by the runner's own clause** — the runner's `replays` set is `{replay-selftest, handoff-v2, handoff-v3-selftest, handoff-v3}`, **none of which replays a frozen manifest**; the manifest leg is red on 11 of 12 generations (§2.4) |
| **C** | ceiling as amendment entry | **landed** — new section in `register-strata-attestation.md`, earlier headers intact |
| **C** | new sourced knowledge entry | **landed** — new file under `corpus/knowledge/linguistics/`, absent from baseline by blob identity |
| **C** | README reconciled | **landed** — revision 1.8, counts footer corrected |

## 6. The TMPDIR trap, and why this seat left the repo for it

The regimen mandates `export TMPDIR=$PWD/.scratch`. `tools/replay-frozen.py:175-177`
refuses a mirror inside the repo:

```python
if real_mirror == root or root in real_mirror.parents:
    raise RowError("mirror_unsafe", …)
```

Measured, same manifest, one variable changed:

| TMPDIR | replay of `round-26/post-register/MANIFEST.tsv` |
|---|---|
| `$PWD/.scratch` (mandated) | `6 could-not-evaluate, 0 reproduced` — every row void |
| `/var/tmp/r28o39` (outside) | `2 mismatch, 4 reproduced` — the real verdict |

A sweep run under the mandated setting reports **0 reproduced across all rows** and looks
like total failure. **This seat therefore ran every replay with `TMPDIR` outside the repo**,
and recorded the in-repo control in §6's table above. Note that `/tmp` is a 16G tmpfs at
80% full on this host and hit its quota during the window (`cp: Disk quota exceeded`);
`/var/tmp` was used after that. Round 27's adversarial seat proposed promoting this trap
to the knowledge corpus; round 28 has not done so.

## 7. What this review does not establish

- It does not certify the round, adjudicate a claim, or admit anything. The runner's
  receipt is the lane's instrument; this seat reports its reading at a stamp, not a verdict.
- **Its counts are snapshots.** The D4 packet moved at least twice during the window
  (`86079a67…` → `543d68a8…`), the runner went red→green across it, and a filed byte was
  breached and healed inside it. Every digest above carries its stamp.
- It does not measure the D4 packet's *content* correctness — whether RGL-01..05 say the
  right things is the D seats' question, not this seat's.
- It created no clones and edited no filed byte, so the "before" controls for §1 and §2
  are the stored receipts and the on-disk snapshots, not re-runs.
- It does not claim the speaker gap is a *wrong* design — §3 states the counterweight:
  the limit is declared in the gate's calibration. The finding is that the **claim's
  wording is stronger than the delivered leg**, and that neither the runner's tamper nor
  the gate's selftest plants the shape round 27 filed.
- §2's defect is **pre-existing**, not introduced by round 28; it is reported because it
  bounds what "all replays green" can mean and because round 28's sweep inherits the
  misclassification.

## 8. Disposition proposed to the parent (not a decision — the parent owns it)

1. **The speaker clause needs either teeth or a narrower claim.** Cheapest honest fix:
   declare a closed speaker-class set in the gate, exactly as `force` was solved, and
   plant the token-less tamper (`speaker: "no-such-speaker"`) in both the gate's
   `--selftest` and the runner's tamper set. Failing that, the claim's wording should
   read "speaker *id tokens* resolve against delivered records", which is what the code does.
2. **Retire or guard `reports/round-27/gate-tests/run-gate-tests.py`.** It writes its own
   filed receipt in place; it re-breached a filed byte once this round and will again.
3. **`replay-frozen.py` should classify a gate that resolves `ROOT` to the live lane as
   `could-not-evaluate` (exit 2), not `mismatch` (exit 1).** The two rows in §2 are
   unevaluable in that mirror, and saying so is a one-line honesty fix; it would also
   un-mask the TMPDIR trap that X60-F6 records as currently hidden.
4. **The O clause "all replays green" is measured against the wrong set.** The runner
   gates four labels and **none of them replays a frozen manifest**; the sweep receipt
   records 11 of 12 generations non-zero and no O failure names it. Either add the
   manifest leg to `REGRESSIONS`/`replays` (and accept it will be red until §3 below is
   fixed), or narrow the claim to name the set it actually measures.
5. **The new law gate should be a gated regression, with its own exit declared.** It is
   in no label, so a future round can move the law surface and never learn that
   `register-law-gate.py` started exiting 2. If the four `D4L-LAW-DANGLING` HOLDs are the
   intended clean reading, the gate should exit 0 on them (HOLD-class, as the docstring's
   level table implies) so that a *new* finding is visible as a change; right now the
   clean packet and a tampered packet both exit 1, which is the same class of
   indistinguishability the round exists to remove.
6. **The TMPDIR trap belongs in `corpus/knowledge/`** — round 27 proposed it, round 28
   did not land it, and it is currently duplicated across four scratch notes.
