# D02 — the RL-8 era leg: design, fenced patch, and measured controls

- Seat: D02 | executor | claim D | date 2026-10-19 | baseline 9bccc9b
- Round 38, loop 1 position 6; single 32-seat batch on devin/deepseek-v4-1-flash-high
  (the NAMED live-lane deviation after grok returned 403 out-of-credits —
  `reports/round-38/telemetry/availability-attempt-1.json`).
- Write scope: **this file only**. No tool, gate, packet, component, pin, fixture or
  filed byte written; the patch below was prototyped and measured **only** inside
  `git archive` copies under `.scratch/r38-d02/`. No commit, no push, no install,
  no network.
- Measurement stamp **2026-10-19** (`date -u +%FT%TZ`); cwd = lane root;
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` before every python call.
- Canon: NON-CANON engineering evidence. A digest is integrity, never truth, never
  clearance.

**Verdict in one line.** The RL-8 residue is closed in design and measured: the
`D4L-LAW-ERA` leg grades RGL-05's dating constraint against the packet's own declared
window, is green over a non-vacuous 8-form domain, fires on an E0-dated stamp form,
and HOLDs (never silently passes) every ungradable case. The patch is a
`tools/gates/register-law-gate.py` revision: **one** gate file, no packet or
component byte moved.

## 1. The residue, and who named it

RL-8 is a three-times-named gap, not a new finding:

| where | what it says |
|---|---|
| `reports/round-26/register/rules.md:128` | §5 specifies `REGISTER-ERA-01` ("a record with register == stamp must carry stage >= E1; a `stamp` record with stage E0 -> D4L-ERA (FAIL)") and states it is **specified here and unimplemented**; "the mechanism's owner is whoever grows the leg" |
| `reports/round-26/register/review.md:187,226` | names the same gap `RL-8` (row `RD-5b`, medium) |
| `reports/round-27/law/impl-8.md:68` | `RL-8` — "the **era leg** (`RGL-05`'s substance) is unimplemented: the argot gate has no era concept, so an E0-dated stamp form produces no finding"; owner "whoever grows the leg" |
| `reports/round-27/law/rules.md:29` | `RLAW-04` (era) is **not** replayable; the site that would replay it is named `argot-derivation-gate.py` (unowned) |
| `reports/round-27/law/impl-5.md:128-129` | the battery "does not exercise the era leg"; "the gate has no era concept, and the sibling design measured the same gap as `RL-8`" |
| `reports/round-36/scout/K01-register-scout.md:130-139,215-216` | re-measures it at `ce103bf`: "RL-8 era leg. Specified, unimplemented; owner recorded in `reports/round-27/law/impl-8.md:68`" |
| `reports/round-37/op/O01-queue-draft.md:153,164` | the r37 defect queue carries it (`R36-D-RL8` label) with `next_touch`: "scope the era leg in a corrected claim; if retained, assign the implementation to round 45 and **require a negative control for a form dated before its availability**" |
| `examples/culture-d4/components/13-register-law.yml` `law_binding.enforcement` | the component's own honest self-description: "no gate executes these rows. The era leg (RGL-05) is specified and unimplemented" |

The delivered gate declares the vocabulary but grades nothing: `DECLARED_KINDS`
includes `era` (`tools/gates/register-law-gate.py:121`), so RGL-05 is *shaped*
correctly and then skipped. That is exactly the "row with no teeth" shape RL-1 was
for `force`, one clause over.

## 2. The design

Three decisions, each pinned to delivered bytes.

### 2.1 Host: the law gate, not the argot gate

`rules.md:29` names `argot-derivation-gate.py` as the era leg's site. This design
deliberately hosts in `register-law-gate.py` instead, and says why:

- RGL-05 is a **register-law row** (`kind: era`); its window is declared in the
  `registers` block (`QREG-04`), both of which the law gate already reads and
  resolves. The argot gate reads neither — it is scoped to *derivation* replay.
- The argot gate is reachable through `typed-pipeline-gate.py` as leg `L3b-argot`
  (`tools/gates/typed-pipeline-gate.py:84,517-541`). Adding an era leg there would
  move a pipeline leg the O seat's sweep has already frozen.
- The law gate is the gate whose own docstring already promises to replay "every
  clause of the law"; the era clause is the one clause it did not.

This is a **deviation from the site `rules.md` named**, and it is recorded here as
such rather than silently. The residue is closed either way; only the address
differs.

### 2.2 The window is read from the packet, never hard-coded

RGL-05's substance is stated twice in the delivered tree, both as **free prose**:

```
examples/culture-d4/packet.d4.yml:1358  (registers QREG-04)
    era_rule: "a stamp form is available_from E1"
examples/culture-d4/packet.d4.yml  (register_law RGL-05)
    consequence: "every stamp form is available_from E1, the era 03-orthography
                  dates the stamp-house to; an E0 stamp claim is a defect and E3
                  is reserved and unoccupied"
```

and once as a **bare tag** on the act rows (`era_rule: "E1"`, `QREG-05..08`). The
leg reads the bound by pattern (`available_from\s+(E\d+)`, falling back to a bare
`^E\d+$`) off the `registers` identity rows — the block that *owns* the register's
dating rule. First readable row per register wins, so the delivered prose rule is
read before the bare-tag act rows.

The **tag order** is the packet's own `contract.era_tags.space`:

```
examples/culture-d4/packet.d4.yml:8-12
    era_tags:
      space: ["E0", "E1", "E2", "E3"]
```

"Before the window" is an *order* claim, so the leg ranks against the packet's
declared order and falls back to a gate-declared `ERA_TAG_ORDER = ("E0","E1","E2","E3")`
only when the block is absent. The leg prints which it read (`era_tag_order=4`).

### 2.3 The domain is *forms*, not law rows — and the driver is the law row

Two separate scoping decisions, both measured against false-red risk:

- **A graded record is one carrying both `register` and `term`.** The `registers`
  and `register_law` rows also carry a `register`, but they *declare* the law. The
  delivered packet has **20** rows carrying `register: "stamp"` (8 forms + 7
  `registers` rows + 5 `register_law` rows) and only the 8 forms are dated forms.
  Grading the other 12 would read the law's own vocabulary as a dating claim —
  exactly the false red the reviewer R02 is asked to hunt. Control
  `era-grades-forms-not-law-rows` asserts this.
- **The `era`-kind law row drives the leg.** `grade_era` looks for a
  `register_law` row with `kind == "era"` and HOLDs when none exists, so the leg
  cannot be green over a window no law row states. RGL-05 is the delivered driver
  (`era_law_rows=1`).

### 2.4 Ungradable is a HOLD, never a silent pass

Five distinct ungradable cases each emit `D4L-LAW-ERA` at HOLD level rather than
counting as clean: a missing `stage`; a tag outside the declared order; a register
with no readable window; a block with no `era`-kind law row; and a form scoped to a
register the block declares no window for. This is the anti-vacuous-pass
discipline the r37 queue's `next_touch` demanded.

## 3. Measured outputs

All commands run in `git archive` copies under `.scratch/r38-d02/`; never in-tree
(F-C13-1).

### 3.1 The live packet is green over a non-vacuous domain

```
$ python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 era_forms=8 era_windows=1 era_law_rows=1 era_checked=8 era_failures=0 era_holds=0 findings=0
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
exit 0
```

`era_forms=8 era_checked=8` — the domain is non-empty and every member was graded.
The 8 are `lexicon` `L-55..L-62`, all `register: "stamp"`, all `stage: "E1"`.

### 3.2 The negative control fires, naming the row and both dates

Flipping the first stamp form's stage (`L-56`, `examples/culture-d4/packet.d4.yml:1015`):

```
$ python3 -B tools/gates/register-law-gate.py <tampered packet>
FINDING D4L-LAW-ERA: FAIL — L-56 'kit' (register 'stamp') is dated E0, before the window's bound E1: RGL-05 makes a form claimed before the register's era a defect (reports/round-26/register/rules.md section 5, REGISTER-ERA-01)
exit 1
```

`era_failures=1`, exactly one added finding line, `era_holds=0`. This is the control
the r37 queue required: "a negative control for a form dated before its
availability" (`O01-queue-draft.md:164`).

### 3.3 The selftest grows 45 -> 67 and all pass

```
$ python3 -B tools/gates/register-law-gate.py --selftest
selftest: 67/67 checks passed
exit 0
```

22 new controls, listed in §5. The pre-existing 45 are unchanged and still pass.

### 3.4 No sibling leg is harmed

In the patched isolated copy:

| leg | command | result |
|---|---|---|
| argot derivation | `tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `derived_pairs=8 violations=0`, exit 0 |
| argot selftest | `… --selftest` | `27/27` |
| typed pipeline | `tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed`, exit 0 |
| assembler check | `tools/assemble-culture-d4.py --check` | `byte-identical deterministic assembly`, exit 0 |
| assembler selftest | `… --selftest` | `81/81` |
| typed labels | `tools/d2-typed-labels.py --selftest` | `163/163` |
| handoff v3 (r7 default chain) | `tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0, `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` |

The r7 packet digest is **unchanged** (`45f57132…`), so claim D's `thresholds` and
claim O's `45f57132…` requirement both hold.

### 3.5 The pin surface: exactly one reading moves

```
$ python3 -B tools/check-gate-battery.py      # in the patched isolated copy
summary: {"battery_exit": 2, "fail": 0, "pass": 7, "unevaluable": 0}
baselines: {"baseline_exit": 2, "pinned": 19, "readings": {"gate_revised": 1, "pinned": 19}}
   baseline: expected/register-law-gate/r30-post/expected.json
   gate_sha256: {declared: 15f8b232…, actual: 9adb0bcb…, reading: gate_revised}
```

One `gate_revised` reading on the r30-post law baseline, zero findings. The
unpatched control copy exits 0 with `pinned: 19`. Exit 2 here is the battery's
**fail-closed** response to a revised pinned gate — the expected new-generation
requirement, not a defect.

## 4. The fenced patch (integrator applies; this seat wrote no tool byte)

Apply by replacing `tools/gates/register-law-gate.py` with the patched revision, or
by applying the diff below. Patched file: 647 -> 1014 lines,
sha256 `9adb0bcbaafd2e3472f3434ad78411136bac2ccc2b66bc88b70638c6c6ebd84f`
(from `15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169`).

The patch applier used for the measurements is reproduced verbatim at
`.scratch/r38-d02/apply-d02-patch.py` (scratch, not promoted); it asserts each
anchor matches exactly once, so a moved anchor fails loudly rather than patching
the wrong site.

```diff
--- tools/gates/register-law-gate.py	2026-10-18 19:10:17.117771862 -0300
+++ tools/gates/register-law-gate.py	2026-10-19 08:08:47.366787992 -0300
@@ -49,6 +49,7 @@
     D4L-LAW-KIND         a kind is outside the declared rule-kind set     [HOLD]
     D4L-LAW-DANGLING     a design_row token names no delivered record     [HOLD]
     D4L-LAW-COVERAGE     the packet declares no law block to replay       [HOLD]
+    D4L-LAW-ERA          a dated form falls before its register's window  [FAIL/HOLD]
 
 Output:  one finding per line, `FINDING <id>: <LEVEL> — <message>`, then one
          `coverage:` line and one `dependency:` line. Exit 0 clean / 1 findings
@@ -126,6 +127,28 @@
 SPINE_AXES = ("mark", "fire", "cloth", "wind", "word", "knot", "water", "both",
               "neutral")
 
+# The era vocabulary and the register's dating window: RGL-05's substance, the
+# residue `reports/round-26/register/rules.md` section 5 named `RL-8` and
+# `reports/round-27/law/impl-8.md` left to "whoever grows the leg".
+#
+# The tag *order* is the packet's own `contract.era_tags.space` order when that
+# block is readable, because "before the window" is an order claim and a
+# reordered tag list would silently re-read it. This tuple is the declared
+# fallback, used only when the block is absent; the leg prints which it read.
+ERA_TAG_ORDER = ("E0", "E1", "E2", "E3")
+
+# The window's lower bound is declared as free prose in two places — `registers`
+# QREG-04's `era_rule: "a stamp form is available_from E1"` and RGL-05's own
+# `consequence` — so it is read by pattern. The bare-tag form (`era_rule: "E1"`,
+# which QREG-05..08 carry) is accepted by the second pattern.
+AVAILABLE_FROM_RE = re.compile(r"available_from\s+(E\d+)")
+ERA_TAG_RE = re.compile(r"^E\d+$")
+
+# The register-law row kind that drives the dating leg. RGL-05 is the delivered
+# driver; a block that drops it is already a `D4L-LAW-ROW` finding, and the era
+# leg names the same absence in its own coverage rather than passing silently.
+ERA_DRIVER_KIND = "era"
+
 # The delivered roll/rank machinery a binding act's consequence must name. Stems,
 # not exact strings, because `consequence` is free prose (RU-L3).
 CONSEQUENCE_STEMS = ("roll", "rk-", "rank", "tally", "rite", "rit-", "entry",
@@ -243,6 +266,168 @@
     return names
 
 
+def era_order(packet):
+    """The ordered era tags the packet declares, and where the order came from.
+
+    `contract.era_tags.space` is the packet's own statement of the tag order; the
+    fallback is used only when that block is absent or empty, and the leg reports
+    which one it read so a reader can tell a packet-declared order from the gate's.
+    """
+    contract = packet.get("contract") if isinstance(packet, dict) else None
+    tags = contract.get("era_tags") if isinstance(contract, dict) else None
+    space = tags.get("space") if isinstance(tags, dict) else None
+    if isinstance(space, list):
+        ordered = [text_of(token).strip() for token in space
+                   if text_of(token).strip()]
+        if ordered:
+            return ordered, "packet"
+    return list(ERA_TAG_ORDER), "declared-fallback"
+
+
+def era_windows(packet):
+    """The `available_from` bound each register declares, keyed by register name.
+
+    The bound is read off the `registers` identity rows — the block that owns the
+    register's own dating rule (`QREG-04` for `stamp`) — because the law rows carry
+    the *consequence* of the rule, not its window. The first readable row per
+    register wins, so the delivered QREG-04 prose rule is read before the bare-tag
+    act rows (QREG-05..08). A register whose rows declare no readable bound is
+    absent from the map, and the leg then holds rather than passing it.
+    """
+    windows = {}
+    regs = packet.get("registers") if isinstance(packet, dict) else None
+    for row in (regs or []):
+        if not isinstance(row, dict):
+            continue
+        register = text_of(row.get("register")).strip()
+        if not register or register in windows:
+            continue
+        rule = text_of(row.get("era_rule")).strip()
+        if not rule:
+            continue
+        match = AVAILABLE_FROM_RE.search(rule)
+        bound = match.group(1) if match else (rule if ERA_TAG_RE.match(rule) else None)
+        if bound:
+            windows[register] = bound
+    return windows
+
+
+def era_form_records(packet):
+    """Every form record that carries a `register`: this leg's domain.
+
+    A *form* is a row carrying both `register` and `term`. The `registers` and
+    `register_law` rows also carry a `register`, but they declare the law rather
+    than a dated form, and grading them would read the law's own vocabulary as a
+    dating claim — a false red on the delivered tree.
+    """
+    forms = []
+    if not isinstance(packet, dict):
+        return forms
+    for block, value in packet.items():
+        if not isinstance(value, list):
+            continue
+        for row in value:
+            if not isinstance(row, dict):
+                continue
+            if text_of(row.get("register")).strip() and text_of(row.get("term")).strip():
+                forms.append((block, row))
+    return forms
+
+
+def grade_era(packet, counters):
+    """RGL-05's substance: a form dated before its register's window is a defect.
+
+    Specified at `reports/round-26/register/rules.md` section 5
+    (`REGISTER-ERA-01`: "a record with register == stamp must carry stage >= E1; a
+    `stamp` record with stage E0 -> D4L-ERA (FAIL)") and named unimplemented as
+    `RL-8` in `reports/round-27/law/impl-8.md` section 4. The window is read from
+    the packet's own `registers` block, so this leg grades the delivered law rather
+    than a bound hard-coded here.
+
+    An ungradable form is a HOLD, never a silent pass: an unknown tag, a missing
+    `stage`, a register with no declared window, or a window with no `era`-kind law
+    row driving it.
+    """
+    findings = []
+    order, order_source = era_order(packet)
+    rank = {tag: index for index, tag in enumerate(order)}
+    counters["era_tag_order"] = len(order)
+    windows = era_windows(packet)
+    counters["era_windows"] = len(windows)
+
+    drivers = [row for row in (packet.get("register_law") or [])
+               if isinstance(row, dict)
+               and text_of(row.get("kind")).strip() == ERA_DRIVER_KIND]
+    counters["era_law_rows"] = len(drivers)
+
+    forms = era_form_records(packet)
+    counters["era_forms"] = len(forms)
+    if not forms:
+        return findings
+
+    if not drivers:
+        findings.append(finding(
+            "D4L-LAW-ERA", "HOLD",
+            "%d dated form(s) carry a register but no law row declares kind %r: the "
+            "window has no driver, so the leg would be green over an unstated law"
+            % (len(forms), ERA_DRIVER_KIND)))
+    if not windows:
+        findings.append(finding(
+            "D4L-LAW-ERA", "HOLD",
+            "%d dated form(s) carry a register but the `registers` block declares no "
+            "readable `available_from` window: there is nothing to grade them against"
+            % len(forms)))
+        return findings
+
+    for block, row in forms:
+        rid = text_of(row.get("id")).strip() or "?"
+        register = text_of(row.get("register")).strip()
+        stage = text_of(row.get("stage")).strip()
+        bound = windows.get(register)
+        counters["era_checked"] += 1
+        if bound is None:
+            counters["era_holds"] += 1
+            findings.append(finding(
+                "D4L-LAW-ERA", "HOLD",
+                "%s (%s) carries register %r, which declares no `available_from` "
+                "window in the `registers` block: the form's dating is ungraded, "
+                "not clean" % (rid, block, register)))
+            continue
+        if bound not in rank:
+            counters["era_holds"] += 1
+            findings.append(finding(
+                "D4L-LAW-ERA", "HOLD",
+                "%s: the window bound %r is outside the era tag order %s (%s), so "
+                "\"before the window\" cannot be ranked"
+                % (rid, bound, "/".join(order), order_source)))
+            continue
+        if not stage:
+            counters["era_holds"] += 1
+            findings.append(finding(
+                "D4L-LAW-ERA", "HOLD",
+                "%s (%s, register %r) declares no `stage`: the register's window is "
+                "%s and the form states no dating, so the claim cannot be graded"
+                % (rid, block, register, bound)))
+            continue
+        if stage not in rank:
+            counters["era_holds"] += 1
+            findings.append(finding(
+                "D4L-LAW-ERA", "HOLD",
+                "%s (%s) stage %r is outside the era tag order %s (%s): an unknown "
+                "tag cannot be ranked against the window %s"
+                % (rid, block, stage, "/".join(order), order_source, bound)))
+            continue
+        if rank[stage] < rank[bound]:
+            counters["era_failures"] += 1
+            findings.append(finding(
+                "D4L-LAW-ERA", "FAIL",
+                "%s %r (register %r) is dated %s, before the window's bound %s: "
+                "RGL-05 makes a form claimed before the register's era a defect "
+                "(reports/round-26/register/rules.md section 5, REGISTER-ERA-01)"
+                % (rid, text_of(row.get("term")).strip(), register, stage, bound)))
+    return findings
+
+
 def evaluate_packet(packet):
     """Replay every clause of the law against the packet's other blocks."""
     findings = []
@@ -255,6 +440,10 @@
     counters["identity_rows"] = len(identity)
     counters["law_rows"] = len(speech)
 
+    # RGL-05's substance, run before the coverage short-circuit so a packet with
+    # no law block cannot silently skip the dating leg.
+    findings.extend(grade_era(packet, counters))
+
     if not speech:
         findings.append(finding(
             "D4L-LAW-COVERAGE", "HOLD",
@@ -417,6 +606,73 @@
     return "\n".join(lines) + "\n"
 
 
+def _era_packet(stage="E1", form_register="stamp", window_register="stamp",
+                bound="E1", tag_space="[E0, E1, E2, E3]", era_kind="era",
+                form_rows=1, include_window=True):
+    """A minimal packet whose era leg can be moved clause by clause.
+
+    The shape mirrors the delivered tree: a `registers` identity row carrying the
+    `available_from` prose rule, the five declared law rows with one of kind `era`
+    as the driver, and dated *form* records (a row with both `register` and
+    `term`). `form_register` and `window_register` are separable so a form can be
+    scoped to a register the block declares no window for.
+    """
+    lines = ["contract:", "  era_tags:", "    space: %s" % tag_space, "registers:"]
+    if include_window:
+        lines.append('  - {id: QREG-04, register: %s, era_rule: "a form is '
+                     'available_from %s"}' % (window_register, bound))
+    else:
+        lines.append('  - {id: QREG-04, register: %s, era_rule: "a dating rule with '
+                     'no readable bound"}' % window_register)
+    lines += ["rank_rules:", "  - {id: RK-03}", "register_law:",
+              '  - {id: RGL-01, register: stamp, axis: mark, kind: admissibility, '
+              'force: "directive-binding", speaker: "stamp-holder (RK-03)", '
+              'consequence: "entered on the stamp-roll", design_row: [RK-03]}']
+    for rid, kind in (("RGL-02", "exclusion"), ("RGL-03", "asymmetry"),
+                      ("RGL-04", "no-segment")):
+        lines.append('  - {id: %s, register: stamp, axis: mark, kind: %s, '
+                     'force: "none — a constraint, not a speech act", '
+                     'speaker: "any speaker admitted by RGL-01 or RGL-03", '
+                     'consequence: "a constraint statement", design_row: []}'
+                     % (rid, kind))
+    if era_kind is not None:
+        lines.append('  - {id: RGL-05, register: stamp, axis: mark, kind: %s, '
+                     'force: "none — a dating constraint", '
+                     'speaker: "any speaker admitted by RGL-01 or RGL-03", '
+                     'consequence: "a constraint statement", design_row: []}'
+                     % era_kind)
+    lines.append("lexicon:")
+    for index in range(form_rows):
+        lines.append('  - {id: L-5%d, term: taa%d, register: %s, stage: "%s"}'
+                     % (index, index, form_register, stage))
+    return "\n".join(lines) + "\n"
+
+
+def _first_stamp_stage_flip(text):
+    """Flip the `stage` of the first lexicon record scoped to `register: "stamp"`.
+
+    A record-block scan, not a global regex: the packet carries 15 `stage: "E1"`
+    lines and only 8 belong to stamp forms, and `stage` is written *before*
+    `register` inside a record, so neither a count=1 regex nor a single forward
+    pass can find the right line. The block boundary is a line that opens a list
+    item (`-` alone or `- ...` at the record indent).
+    """
+    lines = text.split("\n")
+    starts = [index for index, line in enumerate(lines)
+              if re.match(r"^  -\s*$", line) or re.match(r"^  - \S", line)]
+    bounds = starts + [len(lines)]
+    for position, begin in enumerate(starts):
+        end = bounds[position + 1]
+        block = lines[begin:end]
+        if not any('register: "stamp"' in line for line in block):
+            continue
+        for offset, line in enumerate(block):
+            if line.strip() == 'stage: "E1"':
+                lines[begin + offset] = line.replace('"E1"', '"E0"')
+                return "\n".join(lines), 1
+    return text, 0
+
+
 def _classes(findings, name):
     return [item for item in findings if item["id"] == name]
 
@@ -548,6 +804,88 @@
     checks.append(("unevaluated-names-the-data-class",
                    bool(_classes(run("\t- [unbalanced\n")[1], "D4L-LAW-DATA"))))
 
+    # ---- the era leg (RGL-05's substance; RL-8)
+    code, clean_era, era_counters = run(_era_packet())
+    checks.append(("era-clean-form-is-green",
+                   code == EXIT_CLEAN and not _classes(clean_era, "D4L-LAW-ERA")))
+    checks.append(("era-leg-has-a-non-vacuous-domain",
+                   era_counters["era_forms"] == 1 and era_counters["era_checked"] == 1
+                   and era_counters["era_failures"] == 0))
+    checks.append(("era-window-is-read-from-the-packet",
+                   era_counters["era_windows"] == 1 and era_counters["era_law_rows"] == 1))
+    # ---- the negative control: a form dated BEFORE the window is a FAIL
+    code, early, early_counters = run(_era_packet(stage="E0", bound="E1"))
+    fired = _classes(early, "D4L-LAW-ERA")
+    checks.append(("era-pre-window-form-fires",
+                   code == EXIT_FINDINGS and len(fired) == 1
+                   and early_counters["era_failures"] == 1))
+    checks.append(("era-finding-is-a-fail-not-a-hold",
+                   bool(fired) and fired[0]["level"] == "FAIL"))
+    checks.append(("era-finding-names-the-form-and-both-dates",
+                   bool(fired) and "L-50" in fired[0]["message"]
+                   and "E0" in fired[0]["message"] and "E1" in fired[0]["message"]))
+    checks.append(("era-resolution-is-discriminating",
+                   bool(_classes(run(_era_packet(stage="E0"))[1], "D4L-LAW-ERA"))
+                   and not _classes(run(_era_packet(stage="E1"))[1], "D4L-LAW-ERA")))
+
+    # ---- the boundary: the window's own bound is in-window, not before it
+    checks.append(("era-bound-is-inclusive",
+                   not _classes(run(_era_packet(stage="E1", bound="E1"))[1],
+                                "D4L-LAW-ERA")))
+    checks.append(("era-later-than-window-is-green",
+                   not _classes(run(_era_packet(stage="E2", bound="E1"))[1],
+                                "D4L-LAW-ERA")))
+
+    # ---- the tag ORDER is the packet's, so a reordered space re-reads 'before'
+    _, reordered, _ = run(_era_packet(stage="E0", bound="E1",
+                                      tag_space="[E3, E2, E1, E0]"))
+    checks.append(("era-order-comes-from-the-packet",
+                   not _classes(reordered, "D4L-LAW-ERA")
+                   and bool(_classes(run(_era_packet(stage="E0", bound="E1"))[1],
+                                     "D4L-LAW-ERA"))))
+
+    # ---- ungradable, never silently clean: each gap is a HOLD
+    _, no_stage, _ = run(_era_packet(stage=""))
+    fired = _classes(no_stage, "D4L-LAW-ERA")
+    checks.append(("era-missing-stage-is-a-hold",
+                   len(fired) == 1 and fired[0]["level"] == "HOLD"
+                   and "no `stage`" in fired[0]["message"]))
+    _, unknown_tag, _ = run(_era_packet(stage="E9"))
+    fired = _classes(unknown_tag, "D4L-LAW-ERA")
+    checks.append(("era-unknown-tag-is-a-hold",
+                   len(fired) == 1 and fired[0]["level"] == "HOLD"
+                   and "outside the era tag order" in fired[0]["message"]))
+    _, no_window, _ = run(_era_packet(include_window=False))
+    fired = _classes(no_window, "D4L-LAW-ERA")
+    checks.append(("era-unreadable-window-is-a-hold",
+                   len(fired) == 1 and fired[0]["level"] == "HOLD"
+                   and "nothing to grade" in fired[0]["message"]))
+    _, no_driver, _ = run(_era_packet(era_kind=None))
+    fired = _classes(no_driver, "D4L-LAW-ERA")
+    checks.append(("era-with-no-era-law-row-is-a-hold",
+                   len(fired) == 1 and fired[0]["level"] == "HOLD"
+                   and "no law row declares kind" in fired[0]["message"]))
+    _, other_register, _ = run(_era_packet(form_register="trade"))
+    fired = _classes(other_register, "D4L-LAW-ERA")
+    checks.append(("era-form-in-a-windowless-register-is-a-hold",
+                   len(fired) == 1 and fired[0]["level"] == "HOLD"
+                   and "ungraded, not clean" in fired[0]["message"]))
+
+    # ---- the law-vocabulary rows are NOT graded as dated forms (no false red)
+    _, vocabulary, era_counters = run(_era_packet(form_rows=1))
+    checks.append(("era-grades-forms-not-law-rows",
+                   era_counters["era_forms"] == 1
+                   and not _classes(vocabulary, "D4L-LAW-ERA")))
+
+    # ---- the era leg runs even when the packet carries no law block at all
+    _, no_law, era_counters = run(
+        'contract:\n  era_tags:\n    space: [E0, E1]\n'
+        'registers:\n  - {id: QREG-04, register: stamp, era_rule: "available_from E1"}\n'
+        'lexicon:\n  - {id: L-50, term: taa, register: stamp, stage: E0}\n')
+    checks.append(("era-leg-does-not-short-circuit-on-empty-law",
+                   bool(_classes(no_law, "D4L-LAW-ERA"))
+                   and era_counters["era_forms"] == 1))
+
     # ---- the teeth control: the DELIVERED packet, tampered the way round 27 did
     live = ROOT / "examples/culture-d4/packet.d4.yml"
     if live.is_file():
@@ -558,6 +896,31 @@
         checks.append(("delivered-packet-replays",
                        base_code in (EXIT_CLEAN, EXIT_FINDINGS)
                        and base_counters["law_rows"] == len(LAW_DECLARED_ROWS)))
+        # the delivered packet's own era domain: every stamp form is E1, so the
+        # live leg must be green over a non-empty domain, and one E0 rewrite of a
+        # stamp form must add exactly one era line.
+        _, _, live_era = run(text)
+        checks.append(("delivered-era-domain-is-non-empty",
+                       live_era["era_forms"] == 8 and live_era["era_checked"] == 8))
+        checks.append(("delivered-era-leg-is-green-over-it",
+                       live_era["era_failures"] == 0 and live_era["era_holds"] == 0
+                       and live_era["era_windows"] >= 1
+                       and live_era["era_law_rows"] >= 1))
+        early_text, early_count = _first_stamp_stage_flip(text)
+        early_code, early_findings, early_counters = run(early_text)
+        added_era = {format_finding(item) for item in early_findings
+                     if item["id"] == "D4L-LAW-ERA"} - base
+        checks.append(("delivered-era-tamper-rewrites-one-stamp-form",
+                       early_count == 1))
+        checks.append(("delivered-era-tamper-adds-one-era-fail",
+                       early_code == EXIT_FINDINGS and len(added_era) == 1
+                       and all(line.startswith("FINDING D4L-LAW-ERA: FAIL")
+                               for line in added_era)
+                       and early_counters["era_failures"] == 1
+                       and early_counters["era_holds"] == 0))
+        checks.append(("delivered-unchanged-era-control-identical-lines",
+                       {format_finding(item) for item in run(text)[1]} == base))
+
         for name, field, value, fid in (
             ("force", "force", "no-such-force", "D4L-LAW-FORCE"),
             ("speaker", "speaker", "no-such-speaker", "D4L-LAW-SPEAKER"),
@@ -634,11 +997,15 @@
         shown = str(path)
     print("coverage: %s law_rows=%d identity_rows=%d record_ids=%d registers=%d "
           "speaker_tokens=%d force_failures=%d consequence_failures=%d dangling=%d "
-          "findings=%d"
+          "era_forms=%d era_windows=%d era_law_rows=%d era_checked=%d "
+          "era_failures=%d era_holds=%d findings=%d"
           % (shown, counters["law_rows"], counters["identity_rows"],
              counters["record_ids"], counters["registers"],
              counters["speaker_tokens"], counters["force_failures"],
-             counters["consequence_failures"], counters["dangling"], len(findings)))
+             counters["consequence_failures"], counters["dangling"],
+             counters["era_forms"], counters["era_windows"],
+             counters["era_law_rows"], counters["era_checked"],
+             counters["era_failures"], counters["era_holds"], len(findings)))
     print("dependency: %s sha256 %s" % (NAMING.relative_to(ROOT), sha256_file(NAMING)))
     return code
 
```

## 5. The 22 new selftest controls

| # | control | asserts |
|---|---|---|
| 1 | `era-clean-form-is-green` | an in-window form emits no era finding |
| 2 | `era-leg-has-a-non-vacuous-domain` | `era_forms=1 era_checked=1 era_failures=0` |
| 3 | `era-window-is-read-from-the-packet` | `era_windows=1 era_law_rows=1` |
| 4 | `era-pre-window-form-fires` | E0 vs bound E1 -> exit 1, one FAIL |
| 5 | `era-finding-is-a-fail-not-a-hold` | the pre-window case is FAIL, not HOLD |
| 6 | `era-finding-names-the-form-and-both-dates` | message carries `L-50`, `E0`, `E1` |
| 7 | `era-resolution-is-discriminating` | fires on E0, silent on E1 |
| 8 | `era-bound-is-inclusive` | `stage == bound` is in-window |
| 9 | `era-later-than-window-is-green` | E2 vs bound E1 is clean |
| 10 | `era-order-comes-from-the-packet` | reordering `space` re-reads "before" |
| 11 | `era-missing-stage-is-a-hold` | no `stage` -> HOLD |
| 12 | `era-unknown-tag-is-a-hold` | `E9` -> HOLD |
| 13 | `era-unreadable-window-is-a-hold` | unreadable `era_rule` -> HOLD |
| 14 | `era-with-no-era-law-row-is-a-hold` | no `kind: era` row -> HOLD |
| 15 | `era-form-in-a-windowless-register-is-a-hold` | register without a window -> HOLD |
| 16 | `era-grades-forms-not-law-rows` | the 20 `register: stamp` rows do not become 20 reds |
| 17 | `era-leg-does-not-short-circuit-on-empty-law` | the leg runs with no `register_law` block |
| 18 | `delivered-era-domain-is-non-empty` | live packet: `era_forms=8 era_checked=8` |
| 19 | `delivered-era-leg-is-green-over-it` | live packet: 0 fails, 0 holds |
| 20 | `delivered-era-tamper-rewrites-one-stamp-form` | the flip rewrites exactly one form |
| 21 | `delivered-era-tamper-adds-one-era-fail` | exactly one added FAIL line, exit 1 |
| 22 | `delivered-unchanged-era-control-identical-lines` | the untampered control is unchanged |

Controls 1-3, 5-6, 8-9, 11-15, 17 are new; 4 and 7 are the required negative
control and its discrimination pair; 16 and 18-22 are the false-red and
delivered-teeth controls.

## 6. The pin cascade (new rows; no filed byte moved)

The patch revises **one** gate. The cascade the integrator owes:

| artifact | current | action |
|---|---|---|
| `tools/gates/expected/register-law-gate/r30-post/expected.json` | pins gate `15f8b232…`, `stdout_sha256 be9e054d…`, `expected {exit:0, class:clean, findings:[]}` | **new generation dir** (e.g. `r38-post/`) with gate `9adb0bcb…`, a fresh `run.log`, and a recomputed `stdout_sha256` (`5e0a7c92…` measured from the patched revision's coverage line). Never rewritten in place — the r30-post dir is append-only per `gate-frozen-run-standard.md` §3 |
| `tools/check-gate-battery.py` registry | reads `GATES_DIR/expected` and requires 10/10 coverage | no code change; the new generation satisfies `BASELINE-GATE-REVISED` by superseding the old pin |
| `examples/culture-d4/expected-holds.json` | `pin_generations` current row pins packet/projection/assembler digests | **no change** — the packet, projection, assembler and hold set are all byte-identical; this patch moves no example byte |
| `tools/gates/typed-pipelines.json` `d4` profile | pins packet/typed-labels/assembler/expected-holds | **no change** — none of those digests move |
| `tools/gates/frozen/**` | contains no `register-law-gate` entry (`grep -rl` → no match) | **no change**; nothing to re-freeze |
| `reports/round-34/handoff/declared-in-r7/**` | packet `45f57132…` | **untouched** — the r7 packet digest is unchanged, verified by `--profile v3` exit 0 |

Precise digest movement:

```
tools/gates/register-law-gate.py    15f8b232… -> 9adb0bcb…   (revised)
tools/gates/expected/register-law-gate/r30-post/expected.json   pins 15f8b232…
  declared stdout_sha256          be9e054d7b4e8dd78ddbf3390c78eec056825e8036faa12187a49dedaa6d0a1a
  patched stdout_sha256           5e0a7c92002336e5f8b89ac2c4c1003560a85bc3758f01aaf0786756746c80f0
examples/culture-d4/packet.d4.yml    aac91246… (UNCHANGED)
tools/gates/naming-collision-gate.py d9e4e8f4… (UNCHANGED, the gate's dependency)
```

Because the packet, projection and assembler do not move, the D4 hold set stays
12/0/0 and the O claim's roster guard is unaffected — the two claims do not
collide on any artifact (reported for X00 and R03).

## 7. Limits, declared rather than silently skipped

- **A prose window read by pattern.** The bound is free prose (`RU-L3`-class), so
  the leg reads `available_from <TAG>` or a bare tag. A register that states its
  window in a phrasing neither pattern matches is HOLDed, not mis-read — but a
  *rewritten* phrasing would silently drop the register out of the window map and
  turn its forms into HOLDs. That is the conservative direction, and it is
  disclosed here rather than left implicit.
- **The window is a lower bound only.** RGL-05 states `available_from E1` and
  "E3 is reserved and unoccupied". The leg grades the lower bound; it does not
  grade the reserved-E3 clause, which has no delivered form to test. Recorded as a
  carried limit, not claimed as covered.
- **RLAW-01/02/03/05 remain unowned.** This leg closes `RLAW-04` only. The
  admissibility-slot, speaker-permission, void-consequence, and inventory legs
  named at `reports/round-27/law/rules.md:22-27` are untouched and remain
  declarations. The round must not read this as closing the law.
- **The host is a deviation** from the site `rules.md:29` named (see §2.1).
- **Not measured by this seat:** the round-38 `run-validation.py` does not exist
  (`ls reports/round-38/run-validation.py` → No such file), so claim D's declared
  counting command `python3 reports/round-38/run-validation.py` is `to-verify`
  until the integrator lands it. Per F-C13-1 it must not be run in-tree regardless.
- **The three verifier seats (D03/D05/D10b) still owe independent confirmation.**
  This seat's measurements are one seat's; §3.2's control and §3.5's pin reading
  are what they should reproduce.

## Owed

- **The patch is not landed.** `tools/gates/register-law-gate.py` is a live tool
  and this seat writes only its `out` path; the integrator applies §4.
- **The r30-post successor generation.** A new `expected/register-law-gate/<new>/`
  dir with the revised gate sha and a recomputed `stdout_sha256`; owner the
  integrator (D04's pins plan is the sibling draft).
- **`reports/round-38/run-validation.py`** — does not exist; the claim's declared
  counting command is `to-verify` until landed. Owner: round-38 integrator.
- **Independent verification.** D03/D05/D10b/D06 still owe the isolated re-run;
  the R02 reviewer owes the false-red hunt on the 20 `register: stamp` rows.
- **RLAW-01/02/03/05** remain unowned (see §7); `head2`'s empty domain remains
  operator-owned (`OI-02`). Neither is this seat's.

## Citations

Files (sha256 measured 2026-10-19, cwd = lane root, `TMPDIR=$PWD/.scratch`):

```
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/register-law-gate.py          (baseline)
9adb0bcbaafd2e3472f3434ad78411136bac2ccc2b66bc88b70638c6c6ebd84f  tools/gates/register-law-gate.py          (patched, in isolated copy)
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85  tools/gates/typed-pipeline-gate.py
455b595ad6d5b1be7844fc9b53a259a5b8a0efbd788b129dbfd2cc0d0ad173ce  tools/check-gate-battery.py
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7  examples/culture-d4/components/13-register-law.yml
be9e054d7b4e8dd78ddbf3390c78eec056825e8036faa12187a49dedaa6d0a1a  stdout pin, tools/gates/expected/register-law-gate/r30-post/expected.json (declared)
5e0a7c92002336e5f8b89ac2c4c1003560a85bc3758f01aaf0786756746c80f0  patched revision's coverage-line stdout
```

Commands run (all from lane root or an isolated `git archive` copy under
`.scratch/r38-d02/`, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

```
git archive HEAD | tar -x -C .scratch/r38-d02/tree
python3 -B .scratch/r38-d02/apply-d02-patch.py .scratch/r38-d02/tree   # 647 -> 1014 lines
python3 -B tools/gates/register-law-gate.py --selftest                 # 67/67 checks passed, exit 0
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
    # era_forms=8 era_windows=1 era_law_rows=1 era_checked=8 era_failures=0 era_holds=0 findings=0, exit 0
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml     # exit 0
python3 -B tools/gates/argot-derivation-gate.py --selftest                            # 27/27
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml       # 20/20, exit 0
python3 -B tools/assemble-culture-d4.py --check                                       # byte-identical, exit 0
python3 -B tools/assemble-culture-d4.py --selftest                                    # 81/81
python3 -B tools/d2-typed-labels.py --selftest                                        # 163/163
python3 -B tools/check-gate-battery.py                        # unpatched control: exit 0, pinned 19
python3 -B tools/check-gate-battery.py                        # patched: exit 2, gate_revised 1, findings 0
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet # exit 0, packet 45f57132… (unchanged)
grep -rl "15f8b232…" . --include=*.json --include=*.txt       # 5 files pin the baseline gate sha
grep -rl "register-law" tools/gates/frozen/                   # no match: nothing frozen to re-freeze
```

Source lines cited: `tools/gates/register-law-gate.py:121,150,647`;
`examples/culture-d4/packet.d4.yml:8-12,1015,1358,2788-2835`;
`examples/culture-d4/components/13-register-law.yml` (`law_binding.enforcement`);
`reports/round-26/register/rules.md:128`; `reports/round-26/register/review.md:187,226`;
`reports/round-27/law/impl-8.md:68`; `reports/round-27/law/rules.md:22-29`;
`reports/round-27/law/impl-5.md:128-129`; `reports/round-36/scout/K01-register-scout.md:130-139,215-216`;
`reports/round-37/op/O01-queue-draft.md:153,164`;
`reports/round-37/scout/K02-defect-census.md:114`;
`tools/gates/expected/register-law-gate/r30-post/expected.json`;
`tools/check-gate-battery.py:130,1183-1213`; `tools/exercise-handoff-e2e.py:157-169,1939`.
