# CritNoopO — cheapest O no-work/stub-print-selftest attack and its kill fixture

Round 79 W1, seat CritNoopO. Lane `kotodama-shokunin`, base `44f76d456c1b326a71ffdb381590af825cbf11be`.
Scope: O claim only (CLAIMS-DRAFT.md "O / operability"). No shared files edited; all
artifacts under `.ufo/waves/round-79/w1/stage/CritNoopO/`.

## 1. What the O guard must do (from the committed draft)

`.ufo/waves/round-79/CLAIMS-DRAFT.md` (O / operability): a bounded ledger-token guard
that "re-runs approved read-only observations against immutable committed bytes; refuses
mutable revisions/constant printers; rejects an observed_at_base differing from the
actual observation and rejects stated_token equal to the actual observation. Success:
committed red/green fixtures, mutation controls, selftest and independent acceptance
counter all pass at lands."

Concrete record the guard exists for: `reports/round-78/telemetry/census-end.txt:33`
records S884 `used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md`
while registry row S884 at `corpus/SOURCES.md:839` carries a different used-by token —
the opened R77 mismatch evidence the draft says own-work source S897 will cite.

## 2. The cheapest attack (two variants, both ~10 lines)

**A1 — canned `--selftest`.** The guard ships a `--selftest` that prints the receipt
shape QUALITY 23/23-addendum greps for (`selftest: clean -> exit=0 OBS=PASS …`,
`SELFTEST: n/n`) and exits 0 without constructing a single fixture. This is precisely
the class QUALITY 28 names: "a landing that replaces the checker with a four-line stub
printing the expected line satisfies a wording that names only the output." QUALITY 25
J4 already rules the general shape ("a receipt typed without the run does not count"),
but the ruling is only enforceable if the acceptance layer re-derives something the
printer cannot know.

**A2 — echo/lookup observe leg.** The guard "re-runs" observations by echoing the
ledger's `stated_token` (or by looking up a verdict keyed by the committed fixture's
hash), never reading a committed byte. On an honest green record
(`observed_at_base == actual != stated`) an echo of *stated* dies on the
`observed_at_base` check — but a guard that hardcodes the committed fixtures' expected
verdicts (fixture sha256 → PASS table) passes without any observation machinery,
because the fixtures are static committed bytes. QUALITY 25 J4b is the same lesson on
the grammar side: any channel that can produce the token without reading clone bytes
(`import os;print(str(…))`) is a constant printer.

Cost: A1 is a literal `print()` block; A2 is `json.load` + one dict lookup. Both are
cheaper than implementing the grammar, and both pass any acceptance that greps static
output or static fixtures.

## 3. The kill — run-time salted driver-side oracle

Principle: the acceptance driver generates a **fresh nonce token per run**, commits it
into an isolated fixture repository it built itself, and re-derives the actual
observation **independently** (its own `git show <base>:probe.txt` + parse). The
guard's output must echo the observed token per pair; the driver asserts equality with
its own oracle. A stub written before the run cannot know a nonce that did not exist
when it was written; a lookup table cannot cover a fixture hash it has never seen.

Two mechanical requirements on the guard contract (smallest safe correction to the O
acceptance wording):

1. **Batch mode echoes derived values.** `<guard> --ledger L --base B --work W --repo R`
   must print one `pair <id> observed <token>` line per pair, with exit 0 green /
   1 mismatch-rejection / 2 refusal. The acceptance counter compares every echoed token
   to its own re-derivation from committed bytes — never to a value copied from the
   ledger, because `observed_at_base` and `stated_token` are both attacker-controlled
   record fields.
2. **Selftest leaves its fixtures behind.** `<guard> --selftest --work W` must exit 0
   and leave under W the fixture repo(s) it built (with commits) plus a
   `selftest-manifest.json` naming each scenario, its `fixture_commit`, `repo_dir`,
   `pair_id`, `expect_exit` and `observed_token`. The acceptance counter re-derives
   every `observed_token` from the left-behind committed bytes with its own oracle.
   A canned printer leaves nothing; an echo-stub leaves tokens that fail re-derivation.
   This extends QUALITY 25(b)'s "the fixture commit travels in the receipt" to "the
   fixture bytes remain inspectable".

Additionally (QUALITY 23 addendum): the green fixture must pass in the same run before
any mutant redness counts; the battery enforces this by running `green` first and by
checking the guard's echoed token against the oracle only in that green leg.

## 4. The executable fixture

`stage/CritNoopO/noop-killer.py` (stdlib only; runs anywhere; fixture repos are
explicitly initialized isolated repos with `git rev-parse --show-toplevel` verified
against the scratch dir). Usage:

```
python3 -B noop-killer.py \
  --guard-cmd '<guard> --ledger {ledger} --base {base} --work {work} --repo {repo}' \
  --selftest-cmd '<guard> --selftest --work {work}' --work <scratch>
python3 -B noop-killer.py --demo   # runs both simulated attacks; every leg must CAUGHT
```

Battery legs (fresh nonce per run; `oracle` = driver-side committed-bytes re-derivation):

| leg | fixture | real guard must | stub fate |
|---|---|---|---|
| `batch:green` | honest record: stated≠actual, observed_at_base=actual | exit 0, echo token == oracle | echo prints stated ≠ oracle → CAUGHT |
| `batch:m1-stated-eq-actual` | stated_token = actual nonce | exit 1 (no-op lie rejected) | stub prints PASS → CAUGHT |
| `batch:m2-observed-tampered` | observed_at_base = wrong value | exit 1 (record mismatch) | stub prints PASS → CAUGHT |
| `batch:m3-constant-printer` | observe grammar = `python3 -c …` (evasive J4b form) | exit 2 (refused) | stub prints PASS → CAUGHT |
| `batch:m4-mutable-revision` | observe target = `main:probe.txt` (branch, not 40-hex) | exit 2 (refused) | stub prints PASS → CAUGHT |
| `batch:worktree-poison` | worktree file appended with decoy token after commit; oracle reads committed bytes | echo token == committed oracle | worktree-reading or echo guard leaks → CAUGHT |
| `selftest:manifest-left-behind` | (A1) | manifest + fixtures under --work | no manifest → CAUGHT |
| `selftest:every-observed-token-rederived` | (A2) manifest tokens | every token re-derives from its fixture_commit | echoed constants ≠ oracle → CAUGHT |

`stage/CritNoopO/stub-guards.py` implements A1 (`canned-selftest`) and A2 (`echo-lookup`)
as honest simulations of the cheapest attacks. `stage/CritNoopO/ref-guard.py` is a
minimal *honest* guard implementing the claimed semantics against the battery's ledger
grammar — it exists to prove the battery is not vacuous and doubles as a behavioural
spec for `tools/ledger-token-guard.py` (read-only 5-element `git show <rev>:<path>`
grammar with 40-hex revision enforcement; stated==actual → exit 1; observed mismatch
→ exit 1; anything else → exit 2).

## 5. Observed evidence (probes run this seat; raw output preserved)

- `receipts/noop-killer-demo.txt` — battery against both simulated attacks.
  **Every leg CAUGHT on both attacks** (`DEMO VERDICT: ALL SIMULATED ATTACKS CAUGHT ON
  EVERY LEG`, driver exit 0). The A1 stub's own words are preserved in
  `receipts/raw-stub-canned/raw-batch-green.txt`: it printed
  `pair G observed S884-stated-decoy` / `GUARD: PASS pairs=1 (simulated canned-selftest
  stub)` while the oracle was `n-5f0ff20e9e669bc2` — the guard echoed the ledger's
  stated token and never observed a byte.
- `receipts/noop-killer-refguard.txt` — battery against the honest reference guard:
  **every leg GUARD-OK** (`KILL VERDICT: GUARD SURVIVES BATTERY`, exit 0). Mutant
  redness in the demo runs is therefore measured against a baseline this same battery
  shows green (QUALITY 23 addendum).
- Nonce freshness across three runs: `n-82ba87a58b85a61a` (refguard),
  `n-c30000faf989f11d`, `n-f8ddc18131ef48a1`, `n-5f0ff20e9e669bc2` (demos) — a lookup
  or canned-output guard cannot carry values across runs.
- `receipts/raw-stub-echo/selftest-manifest.json` shows the A2 manifest whose
  `observed_token` is the literal `echoed-not-derived` — caught by re-derivation, not
  by shape.

Honesty bound: the real `tools/ledger-token-guard.py` is being drafted in a parallel
W1 seat and is **not yet integrated**; no check of it is claimed or implied. The
battery is contract-level (guard command is a `--guard-cmd` template), so it binds
whatever CLI names the draft lands as long as the two behavioural requirements of §3
hold. If the draft's grammar differs from the battery's
`["git","show","<rev>:<path>","|parse",<regex>]` form, L1 must either extend
`noop-killer.py`'s oracle to the landed grammar or have the guard accept the battery's
ledger form — that reconciliation is the one open integration point, and it is named
here rather than silently assumed.

## 6. Impact if unaddressed

Without §3's two requirements, the O claim's success criterion ("selftest and
independent acceptance counter all pass at lands") is satisfiable by A1/A2 at ~10 lines
each — the guard would be a second constant-printer channel of exactly the kind
QUALITY 25 J4/J4b and 28 were written to kill, and the claim would certify
observation machinery that does not exist.

## 7. Housekeeping

- No tools installed or updated; nothing written outside the stage dir, its report,
  and `/fast/scratch/hyaku/kotodama-r79/CritNoopO/` (all scratch removed after
  receipts were copied; verified empty).
- Fixture repositories were isolated scratch repos only; no lane/fleet git or jj
  mutation. Lane and fleet trees untouched except the two files named above.
- No lane build/lint/test run (not required by this seat); the only executions are
  the battery probes quoted above.
