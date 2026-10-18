# R25-D16 — adversarial review 2: over-matching patterns and join-key integrity

- **Seat:** R25-D16 (reviewer 2 of 3), round 25, loop 3 build 1 of 4, claim **D**
  `argot-derivation-check` (`reports/round-25/claims.json:20-27`).
- **Date:** 2026-10-18. Baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`;
  worktree HEAD at measurement `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- **Write scope:** this file only. Scratch under `.scratch/r25-d15/`
  (`TMPDIR=$PWD/.scratch`). No tool, gate, packet, component, or rounds 8–24
  byte touched; no commit, no push.
- **Canon:** NON-CANON engineering evidence.

**Assignment.** Reviewer 2 of 3, adversarial: *a pattern that over-matches?*
Where `review-1.md` asked whether a replay that should fail passes, this file
asks whether the **rule** itself is too permissive — whether a pattern accepts
inputs its own construction text forbids. It reviews the three delivered rules
(`morphology.derivation_rules`, `examples/culture-d4/packet.d4.yml:205-226`),
the `constructions` registry (`:995-1040`), and the two engines that consume
them (`tools/gates/naming-collision-gate.py` gate C,
`tools/gates/lexicon-coverage-audit.py` leg D).

**Verdict in one line.** The three rules are **correct for the forms they
grade** — every one of the 12 delivered derivations replays under exactly one
rule — but their patterns are *unrestricted*, and the restrictions the packet
itself declares (`base_eligibility: native-only`, the seam-legality clause,
`base_classes`) are read by **no engine on the D4 path**. So the rules
over-match: they accept any base, of any layer, of any class, with any seam.

## 1. The three patterns, and what each one actually accepts

| rule | pattern | output | accepts (measured) |
|---|---|---|---|
| `CX-01` STACK-COMPOUND | `^(?P<a>.+)\+(?P<b>.+)$` | `{a}{b}` | any non-empty `a`, any non-empty `b` |
| `CX-02` CRAFT-AGENT | `^(?P<stem>.+)$` | `{stem}ar` | **any** non-empty string |
| `CX-03` ATTRIBUTIVE | `^(?P<stem>.+)$` | `{stem}en` | **any** non-empty string |

`CX-02`/`CX-03` are the over-match core: `.+` is the whole input alphabet. The
rule asserts nothing about the stem's class, layer, or shape. Measured: a stem
of digits, punctuation, or another language's inventory satisfies both.

```
python3 .scratch/r25-d15/adv.py       # A3: name "ZZ9ar", stem "ZZ9", rule CX-02
→ the replay leg reports nothing for the derivation; the only finding is
  PHON-INVENTORY ×7 (the inventory leg caught the digits, not the derivation leg)
```

That is the precise shape of the over-match: **the derivation leg cannot fail on
CX-02/CX-03**, because for any candidate ending in `-ar`/`-en` there exists a
stem the pattern accepts and the output reproduces. The leg's only reachable
verdict on the suffix class is "ok".

### 1.1 The declared restrictions, and which engine reads them

The packet declares three restrictions that would narrow the over-match:

| declaration | where | read by |
|---|---|---|
| `base_eligibility: native-only` | `constructions` `:995-1040` (all three rules) | `lexicon-coverage-audit.py:963` — **dead on D4**, see §2 |
| `base_classes: [noun]` | same | `lexicon-coverage-audit.py:807-813` — fires only when a base carries `class`; D4 lexicon records carry none |
| seam legality ("the compound is legal only if its seam creates no consonant cluster") | `constructions[].description` (`:1005`) | **no engine** — it is prose in a `description` field |

Measured: `grep -n "base_eligibility\|base_classes" tools/gates/naming-collision-gate.py` → **0**.
Gate C reads `pattern` and `output` only (`:1470-1480`); the construction text,
the class list, and the eligibility rule never reach it.

## 2. The `native-only` rule is dead on D4 (measured)

`lexicon-coverage-audit.py:963-976` implements the eligibility check, but
compares a base's `layer` against the literals `("loan", "borrowed")`:

```python
borrowed_base = [base for base in bases
                 if _compact(term_index.get(_compact(base), {}).get("layer"))
                 in ("loan", "borrowed")]
```

D4 stores layer **names**, not those tokens (`L-50 layer: "Salt-road trade
layer"`). So the branch cannot fire. Measured with a compound that reproduces
from a borrowed base and is therefore clean under the form check:

```
# L-45 tikmes -> karmes, bases kal? no: bases ["kar","mes"], construction STACK-COMPOUND (native-only)
python3 tools/gates/lexicon-coverage-audit.py .scratch/r25-d15/v3-borrowed-base.yml
→ exit 0, no finding                     ← should be L-integration-mismatch
# control: same shape with a native base (["mes","mes"])
python3 tools/gates/lexicon-coverage-audit.py .scratch/r25-d15/v3-native-control.yml
→ exit 0
```

The control proves the leg is not merely quiet on this packet: it cannot
distinguish a native base from a borrowed one, so it cannot enforce the
`native-only` declaration it holds in its hands. This is the cleanest
over-match in the review: **a rule declared native-only accepts a loan base, and
the one engine that means to check it is comparing against the wrong vocabulary.**

Note this is a *latent* defect in a delivered tool, not something the D-argot
leg introduced — but it is exactly the discipline the argot leg's `derived_from`
pointer would need, so it belongs in this review's scope.

### 2.1 The delivered argot gate closes the over-match on its own surface

`tools/gates/argot-derivation-gate.py` (landed during this review; sha256
`07db6e9b…`) does **not** read `base_eligibility`, so O-2 is unchanged for it —
but it closes the *rule* over-match that §1 describes, because it does not rely
on `pattern`/`output` alone. It carries the two operations as code
(`op_head2`, `op_reverse`, `:162-170`) and dispatches on the declared
`derivation` name (`head2` / `reverse` / a licensed rule id). Measured on its
own fixture:

```
{term: saalum, derived_from: saalumi, derivation: head2}  → FAIL
   "declared chain 'head2' applied to 'saalumi' yields 'saalu'"
```

So the maximal-coda reading of `head2` — the design's own named trap — is
rejected, and a packet cannot widen the operation by editing a regex. The
over-match in §1 is a property of the *`pattern`/`output` encoding*, and the
delivered gate routes around it for the built-in ops. The residual over-match is
the one this review still reports, and it is **measured**: a packet that declares
a **third** operation as a `pattern`/`output` pair inherits the unrestricted
pattern and the concat-only replay. Declaring `ZZ-01` as
`^(?P<stem>.+)$ → {stem}ar` and grading `{term: ZZ9ar, derived_from: "ZZ9",
derivation: ZZ-01}`:

```
exit 1 — no line names Q-02; the digit stem and the fabricated base replay clean
```

The gate names this limit in its docstring ("a family declaring a third argot
operation must declare it as a `morphology.derivation_rules` entry, or the record
reads `D4L-ARGOT-RULE`") — but the declared-entry path is the permissive one, so
the limit is the over-match, not a guard against it.

## 3. Join-key integrity: the name→id map is keyed on prose

`argot-replay.py:20-24` resolves a lexicon record's `construction` (a **name**)
to a rule **id** by:

```python
if str(r.get("note","")).startswith(str(c.get("name",""))):
    cname2rid[str(c.get("name"))] = rid
```

Three defects in one line:

1. **Prose as a key.** `note` is documentation. Measured: mutating `CX-02`'s
   note to begin `"STACK-COMPOUND …"` moves **3** rows' verdicts
   (`violations 3`, exit 0) with no change to any rule's semantics.
2. **Prefix, not equality.** `startswith` accepts `"STACK-COMPOUND is not this
   rule"` for the name `"STACK-COMPOUND"`. Any note that opens with another
   rule's name steals that mapping.
3. **Last-writer-wins.** The loop does not break and does not detect a
   collision; the final matching rule in iteration order wins silently.

The delivered gate avoids all three: it joins on the typed `formation.rule`
field, which holds a rule **id** (`naming-collision-gate.py:1385`, `rule_id =
_s(formation.get("rule") or formation.get("rule_id")).strip()`), and an
unlicensed id is `DERIV-AFFIX` FAIL (`:1409`). The correct fix is to use the
`constructions` **id**, which the packet already carries and which the CX ids
already share with the rules.

## 4. The over-match's second face: no ReDoS bound on a packet-authored regex

`SKILL.md:203` states the rule: "A packet-authored regex is matched under a
wall-clock budget — `re.error` is not enough against catastrophic
backtracking." The delivered naming gate honours it (`MATCH_BUDGET_SECONDS = 0.5`,
`:1223`; `_catastrophic_pattern`, `:1303`), and the delivered argot gate inherits
both by path (`argot-derivation-gate.py:406-410`). The D11 harness does not:

```
pattern ^(?P<a>(a+)+)$, stem 'a'*28 + 'b'
harness re.match → HUNG (>3 s, deadline-killed)
naming gate      → _catastrophic_pattern True → DERIV-HOLD ×8, 0.03 s
argot gate       → the same guard, via the loaded dependency
```

An over-matching pattern and an unbounded pattern are the same defect seen from
two sides: both are "the rule accepts more work than it was written to do". Both
delivered gates have the two guards already written; only the scratch harness
does not.

## 5. Attacks run (receipts)

`cwd = /home/vgpnk/Projects/shokunin/kotodama-shokunin`, `TMPDIR=$PWD/.scratch`,
2026-10-18T17:29–17:36Z.

| id | attack | result |
|---|---|---|
| O-1 | suffix rule with a digit/punct stem (`ZZ9` → `ZZ9ar`, CX-02) | derivation leg silent; `PHON-INVENTORY ×7` from the *other* leg |
| O-2 | borrowed base under `native-only` (L-45 `karmes`, bases `kar`+`mes`) | lexicon audit exit 0 (should be `L-integration-mismatch`); control with native base also exit 0 |
| O-3 | note-prefix join collision (CX-02's note opens with `STACK-COMPOUND`) | harness `violations 3`, exit 0 — a prose edit moved three grades |
| O-4 | catastrophic pattern under the harness | HUNG >3 s; naming gate `DERIV-HOLD` ×8 in 0.03 s |
| O-5 | `base_classes` enforcement | fires only if a base record carries `class`; D4 lexicon records carry none (`grep -c '^    class:'` → 0) |
| O-6 | seam-legality clause | prose in `description`; 0 engines read it |
| O-7 | third op declared as `pattern`/`output` (`ZZ-01`, stem `ZZ9`) | argot gate exit 1, **no line names Q-02** — the third-op path inherits the over-match |
| O-8 | delivered argot gate on its fixture | `head2` maximal-coda row rejected: "yields 'saalu'"; 4 `D4L-ARGOT-DERIV` + 1 `D4L-ARGOT-RULE`, matching the committed `.expected` |
| O-9 | `sha256sum tools/gates/argot-derivation-gate.py`; `--selftest` | `07db6e9b…`; `selftest: 18/18 checks passed` |

## 6. What this review does **not** claim

- It does **not** claim the delivered rules are wrong. All 12 delivered
  derivations replay under exactly one rule each (V-0 in `review-1.md`), and the
  rules are byte-frozen in the packet's own digest.
- It does **not** claim the over-match has produced a wrong byte. The
  over-match is a *reachability* finding: the suffix class has no reachable
  failing verdict, so a future packet could smuggle a bad derivation through it.
- It does **not** ask for the rules to be tightened in this round. Tightening
  `CX-02`'s `.+` would be a packet edit with its own re-pin; the honest
  sequencing is to record the reachability limit and let the round that builds
  the `derived_from` relation decide the restriction.
- It does **not** dispute `execution-1.md` §4, which already declares the
  replay's bound. O-1/O-2 measure the *width* of that bound.

## 7. What this seat did not do

- Wrote only this file. Fixtures and receipts under `.scratch/r25-d15/`.
- Did not edit any tool, gate, packet, component, or rounds 8–24 artifact; did
  not commit or push.
- Did not adjudicate promotion or the culture fork.
