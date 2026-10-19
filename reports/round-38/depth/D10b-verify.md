- Seat: D10b | verifier | D | date 2026-10-19 | baseline 9bccc9b

# D10b — third independent verifier: is the F-6 emitter's output *consumed*, or only present?

Mission (verbatim, `reports/round-38/targets.json` seat `D10b`): *"Third independent
verifier: the F-6 emitter's output consumed by the argot leg (not just present) — a
vacuous-pass guard."*

Verdict: **the D claim's `after_required` has a live vacuous-pass hole.** Emitting the
F-6 keys is not the same as the legs counting them, and at `9bccc9b` **no consumer reads
the counters on either available route**. A key-only emitter would satisfy the letter of
the claim and fail its substance. Both routes are measured below with mutation controls.

---

## 1. The before-state, re-measured independently

F-6 is `design-brief.md:306-307`: *"the coverage block reports `derived_forms` and
`derived_ok` counts that agree"* (row F-6 of the forecast table,
`reports/round-25/argot/forecast.md:37`).

```
$ for t in derived_forms derived_ok; do
    printf "%-14s examples=%s tools=%s\n" "$t" \
      "$(grep -rl "$t" examples | wc -l)" "$(grep -rl "$t" tools --include=*.py | wc -l)"; done
derived_forms  examples=0 tools=0
derived_ok     examples=0 tools=0
```

Confirms `reports/round-36/scout/K01-register-scout.md:115` ("NOT DELIVERED — and no
producer exists") at the current baseline. The numbers the forecast wants exist under
different names: the argot gate prints

```
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml | tail -2
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
exit=0
```

`derived_pairs=8 violations=0` is non-vacuous (`derived_pairs` has members), so the
existing pass is real — the F-6 gap is a **key-set** gap, as K01 said, not a capability gap.

## 2. Route A — the argot gate's `coverage:` line is printed and never parsed

The gate builds the line at `tools/gates/argot-derivation-gate.py:917` and returns
(`:920`); nothing downstream reads it.

```
$ grep -rn "derived_pairs\|register_scoped\|claimed_chains\|borrow_pairs\|rule_holds" \
      tools/ --include=*.py | grep -v "argot-derivation-gate.py"
(no output)
```

The consumer the mission names is the argot leg `L3b-argot`
(`tools/gates/typed-pipeline-gate.py:517-541`). It reads **only** `FINDING D4L-ARGOT-*`
lines and the exit code:

- `typed-pipeline-gate.py:530-531` — `argot_lines = [line for line in proc.stdout.splitlines() if line.startswith("FINDING D4L-ARGOT-")]`
- `typed-pipeline-gate.py:533-534` — fails are lines containing `"FAIL"`
- `typed-pipeline-gate.py:539` — `check("L3b-argot", not argot_fails and proc.returncode in (0, 1), ...)`

`result["argot"]` (`:528-529`) records the exit code and the **sha256 of the whole
stdout**, but that digest is reported, never compared against an expected value — it is
not a pin. The `coverage:` line reaches no comparison anywhere.

### Control C1 — pristine baseline, keys absent

```
$ python3 -B .scratch-d10b-probe.py examples/culture-d4/packet.d4.yml
recount: derived_forms=8 derived_ok=8
emitted: derived_forms=None derived_ok=None
REFUSE: the coverage line omits the F-6 keys
probe exit=1
```

### Control C2 — key-only emitter, honest values: the leg stays green

`derived_forms`/`derived_ok` appended to the coverage print with correct values:

```
coverage: ... violations=0 rule_holds=0 derived_forms=8 derived_ok=8

$ python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
ok   L3b-argot
summary: 20/20 legs passed
typed-pipeline exit=0
```

The keys landed and **nothing noticed**. This is the vacuous pass the mission asks me to
find: an emitter that only writes the keys is green everywhere.

### Control C3 — a lying line is equally invisible

`derived_pairs=0`, `violations=99`, `derived_forms=0`, with the gate's own findings clean
(`grep -c FINDING` → `0`):

```
coverage: ... derived_pairs=0 ... violations=99 rule_holds=0 derived_forms=0 derived_ok=8

$ python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
ok   L3b-argot
summary: 20/20 legs passed
typed-pipeline exit=0
```

The leg's verdict is **independent of the counters**, in both directions.

### Control C4 — the leg *is* discriminating (the gap is specific, not general)

So the finding is not "the leg is always green". Planting a real violation by mutating
`derived_from: "tik"` → `"tikX"` (`packet.d4.yml:1020`; the gate reads `derived_from` as
the base, `argot-derivation-gate.py:394`):

```
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form L-56 'kit' (register 'stamp'): declared chain 'reverse' applied to 'tikX' yields 'Xkit'; the stated inputs and rules do not yield the candidate
argot exit=1

$ python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
FAIL L3b-argot: argot leg exit 1: FINDING D4L-ARGOT-DERIV: FAIL — ...
tp exit=2
```

The leg catches findings. It does not catch **counter** defects — exactly the F-6 surface.

### The gate's own selftest does not close this either

`--selftest` is 27/27 green under the pristine gate, under C2 (keys added) and under C3
(lying values) alike:

```
$ python3 -B tools/gates/argot-derivation-gate.py --selftest | tail -1
selftest: 27/27 checks passed        # pristine, C2 and C3 all identical
```

No selftest check asserts the coverage line's content (`grep -n coverage` over the file
finds only the docstring `:22`, a scope note `:78-79`, the builder `:543`, the
`COVERAGE_CONTROL` fixture `:755`, the `coverage-hold-fires` check `:856` and the print
`:917`). So a D executor adding an emitter cannot rely on the selftest to tell a
consumed counter from a decorative one.

## 3. Route B — the projection block is byte-consumed but *value-unguarded*

The alternative placement is the projection's own `coverage` block
(`examples/culture-d4/typed-labels.d4.yml:29-47`), built at
`tools/d2-typed-labels.py:2880-2895` and printed at `:2971-2976`. That block **is**
byte-consumed:

```
$ # add derived_forms/derived_ok to the delivered projection, then check
$ python3 -B tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml
examples/culture-d4/typed-labels.d4.yml differs from the deterministic projection
check-gate exit=1
```

But byte-identity guards **bytes, not values**. Patching the projector to emit
`"derived_forms": 999` (`tools/d2-typed-labels.py:2895`), re-emitting, and checking:

```
$ python3 -B tools/d2-typed-labels.py --packet ... --emit examples/culture-d4/typed-labels.d4.yml
$ grep -n '"derived_forms"' examples/culture-d4/typed-labels.d4.yml
31:    "derived_forms": 999,

$ python3 -B tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml
examples/culture-d4/typed-labels.d4.yml: byte-identical deterministic projection
check-gate exit=0
```

The projection says `derived_forms=999` while the packet holds 8 derived rows and the
check leg says *byte-identical*. Nothing asserts the value:

```
$ grep -rn "derived_forms" tools/ --include=*.py
tools/d2-typed-labels.py:2895:        "derived_forms": 999,      # (the planted line, isolated copy)
```

So **both routes are holey today**: Route A is never read; Route B is read only for
byte-equality with a projector that is free to lie. An emitter landing on either route
can pass vacuously, which is precisely what the mission's guard is for.

## 4. The guard (draft — fenced, integrator-applied)

Minimal form, closing Route A. It parses the gate's own `coverage:` line and re-derives
the two counters from the packet bytes, refusing on absence, disagreement, or an empty
set. Deliberately line-oriented so it shares no code path with the gate's `Counter`.

```python
#!/usr/bin/env python3
"""D10b probe — is the F-6 coverage output CONSUMED, or only printed?

Parses the argot gate's `coverage:` line and re-derives derived_forms /
derived_ok independently from the packet bytes. Refuses (exit 1) when the keys
are absent, disagree with the recount, or the set is empty (anti-vacuous).
"""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GATE = ROOT / "tools/gates/argot-derivation-gate.py"
COVERAGE_RE = re.compile(r"^coverage:\s+\S+\s+(?P<rest>.*)$")


def parse_line(text):
    for line in text.splitlines():
        m = COVERAGE_RE.match(line)
        if m:
            return {k: int(v) for k, v in re.findall(r"(\w+)=(\d+)", m.group("rest"))}
    return None


def recount(packet_text):
    forms = ok = 0
    lines = packet_text.splitlines()
    for i, line in enumerate(lines):
        if not re.match(r"^\s{2,}derived_from:\s*\S", line):
            continue
        indent = len(line) - len(line.lstrip())
        forms += 1
        has = False
        for follow in lines[i + 1:]:
            if not follow.strip():
                continue
            if len(follow) - len(follow.lstrip()) < indent:
                break
            if re.match(r"^\s{%d}derivation:" % indent, follow):
                has = True
            elif re.match(r"^\s{%d}\w" % indent, follow) and has:
                break
        if has:
            ok += 1
    return forms, ok


def main(argv):
    packet = Path(argv[1])
    proc = subprocess.run([sys.executable, "-B", str(GATE), str(packet)],
                          capture_output=True, text=True, cwd=str(ROOT), check=False)
    counters = parse_line(proc.stdout)
    if counters is None:
        print("REFUSE: no coverage: line printed")
        return 1
    forms, ok = recount(packet.read_text(encoding="utf-8"))
    ef, eo = counters.get("derived_forms"), counters.get("derived_ok")
    print("recount: derived_forms=%d derived_ok=%d" % (forms, ok))
    print("emitted: derived_forms=%s derived_ok=%s" % (ef, eo))
    if ef is None or eo is None:
        print("REFUSE: the coverage line omits the F-6 keys")
        return 1
    if ef != forms or eo != ok:
        print("REFUSE: emitted counters disagree with the recount")
        return 1
    if forms == 0:
        print("REFUSE: zero derived forms — a pass would be vacuous")
        return 1
    print("OK: counters agree and the set is non-empty")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

Guard behaviour, all four states measured (isolated copy, `git archive` of `9bccc9b`):

| state | gate | probe | leg `L3b-argot` |
|---|---|---|---|
| C1 pristine, keys absent | exit 0 | **REFUSE** (1) | ok |
| C2 key-only emitter, honest | exit 0 | **OK** (0) | ok |
| C3 lying line | exit 0 | **REFUSE** (1) | ok |
| C4 planted `D4L-ARGOT-DERIV` | exit 1 | (findings path) | **FAIL** |

C2 is the anti-always-red control: the probe accepts a correct emitter, so it is a
guard, not a wall. C1/C3 are the discriminating controls.

**Where it should land (integrator's call, not this seat's):** as a new `check(...)` in
`tools/gates/argot-derivation-gate.py --selftest` (Route A, self-contained, no new
file), and/or as an `L3b-argot` sub-assertion in
`tools/gates/typed-pipeline-gate.py:539` that consumes the counters rather than only the
findings. For Route B the guard must recount from the packet and compare against the
projection's `coverage` values, since byte-identity provably cannot (§3).

## 5. Consequences for the D claim's acceptance

The claim's `after_required` is *"the counters emit from the packet/components (or a
documented equivalent the legs can count)"*. Read literally, "the legs can count" is
satisfied by nothing at this baseline: no leg counts them (§2, §3). The claim's own
threshold is *"the new coverage named (no vacuous-pass)"* — which is exactly the hole
C2/C3 demonstrate. So this seat's independent verdict is:

- **A key-only emitter must not be accepted** as D's after-state, on this evidence.
- Acceptance needs the consumer half: the guard above (or an equivalent that reads the
  counters and refuses on disagreement), plus its own selftest controls.
- The claim's "two independent verifiers" threshold is **not** met by this fragment
  alone — I am one of three verifier seats (D05, D06, D10b); the count is the
  integrator's to take, and D05/D06's evidence was not on disk when I ran (`ls
  reports/round-38/depth/` → empty at 08:05–08:06).

`reports/round-36/validation.json` records D as failed-as-declared with the residue
*"F-6 counters, head2 domain, RL-8 era leg, the 13-vs-12 component read-set asymmetry"*
routed forward. This fragment narrows that first residue: F-6 needs **an emitter and a
consumer**, and the consumer is the load-bearing half.

## 5b. Division of labour with the sibling verifier seats

`reports/round-38/depth/D05-verify.md` landed while I ran and names a related hazard:
*"if D03 lands the two keys by emitting `derived_forms`/`derived_ok` as constants, the
coverage block would 'report counts that agree' with nothing behind them"*
(`D05-verify.md:60-66`). That is the **constant-value** hazard, and D05's control is
"`0/0` emission is a vacuous pass".

This fragment's hazard is different and, on the evidence above, stronger: even a
**correct, non-constant** emitter is unguarded, because *no consumer reads the counters at
all* (§2 Route A: the leg filters `FINDING D4L-ARGOT-` lines only; §3 Route B: byte-
identity accepts a lying value). D05's `0/0` control would not catch C3's
`derived_forms=0`-with-`derived_ok=8` on Route A — nothing on Route A would, because the
line reaches no comparison. The two controls compose: D05's guards the *value's
plausibility*, mine guards the *presence of a reader*. Both are needed; neither subsumes
the other.

`D07-receipt.md:177` records the placement fork — *"(a) add `derived_forms`/`derived_ok`
to the argot gate's own `coverage:` line (minimal, …)"* — as the integrator's choice. If
that fork lands on Route A, §4's guard is what makes the addition non-decorative; that is
the one thing this seat asks the integrator to carry.

## 6. Scope and hygiene

- All mutation work ran in `git archive` copies under `.scratch/` (`.scratch/d10b-iso`),
  re-created from `9bccc9b` between runs; the in-tree copy was never mutated and no
  `reports/round-*/run-validation.py` was executed anywhere (F-C13-1).
- In-tree bytes unchanged: `git status --porcelain` → only `?? reports/round-38/`;
  `argot-derivation-gate.py` `b5406bcd…`, `d2-typed-labels.py` `2819f687…`,
  `typed-labels.d4.yml` `c23b0ab5…`, `packet.d4.yml` `aac91246…` — all equal to the
  `9bccc9b` values.
- No filed byte touched; `reports/round-34/handoff/declared-in-r7` was read only.

## Owed

- **`reports/round-38/run-validation.py`** — does not exist yet (`ls` → No such file),
  so the D claim's third counting command is `to-verify` until the integrator lands it.
  Per F-C13-1 it must not be run in-tree regardless; owed to the integrator.
- **D05 / D06 evidence** — `reports/round-38/depth/` was empty when I ran; this fragment
  cannot confirm or contradict their isolated results, and does not claim the claim's
  two-verifier threshold.
- **Route-B guard** — the recount-vs-projection-value check is specified here (§3, §4)
  but not implemented; owner is whoever lands the F-6 emitter.
- **The emitter itself** — this seat is a verifier; the `derived_forms`/`derived_ok`
  emitter is D01's design. My C2/C3 patches are controls, not a proposed implementation.

## Citations

Files (sha256 measured 2026-10-19, cwd = lane root, `TMPDIR=$PWD/.scratch`):

```
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85  tools/gates/typed-pipeline-gate.py
2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3  tools/d2-typed-labels.py
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3  examples/culture-d4/expected-holds.json
```

Source lines cited: `tools/gates/argot-derivation-gate.py:392-411` (`declared_derivation`,
`derived_from` is the base), `:543-567` (the counter builder), `:917` (the coverage
print); `tools/gates/typed-pipeline-gate.py:517-541` (leg `L3b-argot`), `:530-531` (the
`FINDING D4L-ARGOT-` filter), `:539` (the check); `tools/d2-typed-labels.py:2880-2895`
(the projection `coverage` dict), `:2971-2976` (its printer);
`examples/culture-d4/typed-labels.d4.yml:29-47` (the delivered coverage block);
`examples/culture-d4/packet.d4.yml:1020-1023` (the L-56 stamp row);
`reports/round-17/d4/design-brief.md:306-307`; `reports/round-25/argot/forecast.md:37`;
`reports/round-36/scout/K01-register-scout.md:115,208-212`;
`reports/round-36/validation.json` (claim D, failed as declared).

Commands run (isolated copy `.scratch/d10b-iso`, `TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`; in-tree where read-only):

```
git archive HEAD | tar -x -C .scratch/d10b-iso
grep -rl "derived_forms\|derived_ok" examples | wc -l                                   # 0
grep -rl "derived_forms\|derived_ok" tools --include=*.py | wc -l                       # 0
grep -rn "derived_pairs\|register_scoped\|claimed_chains\|borrow_pairs\|rule_holds" \
    tools/ --include=*.py | grep -v "argot-derivation-gate.py"                          # no output
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml        # exit 0
python3 -B tools/gates/argot-derivation-gate.py --selftest                              # 27/27
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml         # 20/20, ok L3b-argot
python3 -B .scratch-d10b-probe.py examples/culture-d4/packet.d4.yml                     # C1 refuse / C2 ok / C3 refuse
python3 -B tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml
git status --porcelain                                                                  # ?? reports/round-38/
git rev-parse --short=7 HEAD                                                            # 9bccc9b
```

Controls applied in the isolated copy only (each from a fresh `git archive` of `9bccc9b`):
C2/C3 patch the coverage print at `argot-derivation-gate.py:917-921`; C4 patches
`packet.d4.yml:1020`; Route-B patches `d2-typed-labels.py:2895` and re-emits. All
restored or discarded; the in-tree digests above re-verified after.
