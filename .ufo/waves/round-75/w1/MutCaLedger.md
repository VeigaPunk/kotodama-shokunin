# MutCaLedger — round 75 draft ledger mutation probe

## Scope and detector

Read the draft `reports/round-75/claims.json` and `reports/round-75/ledger.json` first. The round-75 counter was absent at initial inspection; it appeared during this probe. The landed draft file `.ufo/waves/round-75/counters/accept-ca.py` currently ends at `# @@PART2@@` and contains no `leg_ledger` / `leg_basemismatch` implementations. I therefore ran its present `observe_problem`, `observed_token`, and `stated_token` functions on a scratch base clone, and evaluated the missing leg decisions against the claims' draft LEDGER/BASEMISMATCH text. For line-anchor and REPAIR details I used the round-74 counter as an implementation proxy, clearly distinguished below. No campaign command or write touched the source tree.

Scratch was `/fast/scratch/hyaku/kotodama-r75/MutCaLedger`; the base clone was asserted toplevel `/fast/scratch/hyaku/kotodama-r75/MutCaLedger/base-clone`, checked out at `f556d1049fe651d3d63975600b13acd9fb686f15`. The evil fixture was a separate scratch git repo with 999 planted SOURCES rows.

## Baseline actual outputs

Current round-75 counter token/guard results on all 11 draft pairs (the counter's `observed_token` result is the operative parse result):

| Pair | stated | observed | result |
|---|---:|---:|---|
| L75-01 | `412` | `808` | red |
| L75-02 | `30` | `32` | red |
| L75-03 | `36` | `40` | red |
| L75-04 | `adds that leg.` | `1` | red |
| L75-05 | `was absent from the page it was bound to` | `1` | red |
| L75-06 | `was the Sowers-Wills clause, absent from this page` | `1` | red |
| L75-07 | `the QUALITY 23 addendum` | unobservable: `parse-miss(exit=1 (zero matches))` | not red/BASEMISMATCH fails |
| L75-08 | `see the closing line below` | unobservable: dead pin `3a7401609325341eb3fe0efd42d0eec29d06be3c` is not in lane clone | not red/BASEMISMATCH fails |
| L75-09 | `FAIL` | `FAI` | red, but stated-text anchor is false |
| L75-10 | `43` | `.md` | red, but not a count token |
| L75-11 | `10/11` | unobservable: `parse-miss(exit=1 (zero matches))` | not red/BASEMISMATCH fails |

Raw base observations: L75-01 `...corpus/SOURCES.md:808`; L75-02 `32 files changed`; L75-03 `40 files changed`; L75-04 `...sweep.py:1`; L75-05 and L75-06 each `...round-74.md:1`; L75-07 and L75-11 return no stdout and exit 1; L75-08 fails in the lane clone with `fatal: unable to parse object: 3a740160...`; L75-09's parse yields `FAI`; L75-10 lists 44 `.md` filenames in the base clone.

Additional literal anchor failures in the draft: L75-07 says `the QUALITY 23 addendum` at `corpus/lessons/round-74.md:208`, but the line contains `the **QUALITY 23 addendum**` (stated_text not found verbatim). L75-09 says `min-pairs gate FAIL` at `reports/round-73/telemetry/selftest-r3.txt:6`, but the committed line ends `min-pairs gate FAI`; stated_text is not found. L75-10's parse `\\.md$` has no capture group, contrary to the draft LEDGER requirement. These are pre-existing draft defects, not mutations.

## Mutations and outcomes

`SURVIVES` means the mutated pair still yields a red/acceptable observation under the exercised guard; `KILLED` means the exercised guard rejects it or it becomes unobservable. Where the round-75 detector is incomplete, the missing whole-leg verdict is explicitly not claimed.

| Class / mutant | Actual output and verdict | Hardening implicated |
|---|---|---|
| (a) L75-01 `observe_cmd` → `git log --oneline -1 <base>`; loosen parse to `([0-9]+)` | Current R75 guard accepts (`None`); parsed token `556` comes from the revision hash, not the registry. `412 != 556`, so BASEMISMATCH-only check **SURVIVES** with false evidence. With the original `:([0-9]+)$` parse, it is unobservable/parse-miss and is killed. | Bind allowed git subcommands/output fields to the stated subject; require parse semantics/anchoring that cannot take digits from a revision or unrelated output. `git log` is in the read-only subcommand allowlist. |
| (a) L75-02 pathspec swapped from `linguistics/*.md` to `culture-material/*.md` | Current guard accepts; observed `40`, stated `30`; remains red: **SURVIVES** while measuring the wrong directory. Symmetric L75-03 swap to linguistics yields `32` vs `36`, also survives. | Bind observe path/revision to the pair's stated path/claimed subject, not merely to a valid in-clone operand. |
| (a) L75-01 `git -C <evil scratch repo> grep ...` | Unguarded command actually printed `HEAD:corpus/SOURCES.md:999`. Current R75 guard rejects non-canonical `-C`: `git -C '/fast/scratch/.../evil' is refused ... only the --fleet-root may be named`. **KILLED** by the current guard. A `-C` to the canonical fleet root is the only admitted form, subject to checking operands in that repo. | Preserve the current explicit fleet-root-only `-C` rule and repository-specific operand validation. |
| (a) L75-08 as drafted | Current R75 guard rejects the pinned fleet commit as a dead lane-clone object; `stated_at` is an absolute fleet path and cannot be read from the lane clone. Raw run in lane exits 128; the same grep succeeds only when explicitly run with `-C /home/vgpnk/Projects/shokunin`. **KILLED/unobservable as drafted.** | Carry the explicit fleet-site grammar/resolve `stated_at` at the fleet pin and make `observe_cmd` use the permitted fleet-root channel; do not silently treat a fleet pin as a lane object. |
| (b) L75-01 parse changed to `([0-9]+)` | Current guard accepts; parsed token is `556` from the hash; red survives BASEMISMATCH (**SURVIVES**). The R74 REPAIR proxy would reject the resulting wrong truth at lands (statement `808` vs loose-parsed `556`), so a complete repair leg can catch it later, but BASEMISMATCH alone does not. | Keep capture-group check, plus bind/anchor the captured field to the intended count; capture group alone is insufficient. |
| (b) L75-05 widened path to `corpus/lessons/` | Output still has one matching line and token `1`; in this particular tree the token coincides with the correct value, so this probe does not expose a changed count. It demonstrates that operand widening is not itself rejected; the path-swap probes above show the surviving evidentiary drift. | Same subject/path binding as (a). |
| (c) L75-02 `stated_at` 344→345; L75-06 38→37 | In both cases stated_text remains somewhere in the file but is not on the declared line. R74 line-exact anchor check reports `in file but NOT on line`; **KILLED**. L75-02 line 99999 is also killed as beyond EOF. | Preserve the line-exact `stated_text` check (not merely whole-file containment). |
| (d) L75-01 `expected_after := observed_at_base` (`808`) | This is already the draft value; no byte/behavior change, so it **SURVIVES as an identity mutation**. The R74 REPAIR proxy makes this non-vacuous only with the complete chain: observed truth at lands, statement changes from base, old stated_text absent, and `expected_after == re-read statement`. The current R75 part-1 functions do not consume `expected_after`; the R75 leg text's REPAIR sentence also does not explicitly state the expected_after equality. | Keep an explicit expected-after equality in REPAIR and the unchanged-statement / old-text-absence checks. The copied-base mutation is harmless only if those checks are actually implemented. |
| (d) L75-11 `expected_after := stated token` (`10/11`) | Under draft leg text alone this field change has no defined effect; no full R75 leg implementation is present to run. Under R74 REPAIR proxy it is **KILLED** unless the statement is unchanged, in which case unchanged/base-text checks reject it; a changed statement still must equal truth and expected_after. | Make the frozen REPAIR contract consume expected_after and reject no-op repair, rather than relying on a non-empty field. |

## Other detector-sensitive findings

- L75-07 and L75-11 use `git grep -c` for zero matches. R75's runner normalizes grep exit-1/empty output to token `0`, but the pair parse `:([0-9]+)$` then misses that normalized bare `0`; thus each is unobservable in the actual token function. L75-07's stated anchor independently fails because of Markdown bold markers. The no-absence rule does not reject L75-07 by expected_after because its expected_after is `0`, not a positive count.
- L75-09's rederive is a shell string with `|`; the current parser splits it into argv and the H2 guard rejects `|`. Its `tail -c 4` also reads the *end of the whole receipt* (`'son\\n'`), not the truncated line-6 token `FAI`. A pipe-free, correctly scoped rederive is needed. Its stated anchor already fails (`FAIL` vs actual `FAI`).
- L75-10's `ls` + `\\.md$` parse yields the constant suffix `.md`, not a numeric file count. The R74 proxy rejects this parse for lacking a capture group. Its rederive also contains a rejected pipe, and its numeric ANNOTATE count has no frozen-base operand.
- R74 proxy grammar requires the REPAIR statement reread; the current R75 draft counter documents a fallback to stated_at/stated_parse when statement_after is absent. All six REPAIR draft pairs omit statement_after; the current draft's fallback is a deliberate behavior, but it still must satisfy the full REPAIR invariants. R75 explicitly permits base-pinned REPAIR observations executed in the lands clone, so R74's prior blanket rejection of pinned REPAIR observations is not applicable to this draft.

## Hash / restoration evidence

No ledger bytes were edited: mutations were deep-copied in-memory pairs plus scratch fixture repositories. `reports/round-75/ledger.json` SHA-256 before = after = `48a8bc443fa8a90be7fba0bb497b16279616720f9427b462535a735d29f7d61c`. `claims.json` changed during the concurrent wave (before observed `0f4fd1b040f75af9af055926058eb28e9b3b5ab7826ce3366ffa5f1d82e16a42`; final observed `a5e9fb2f396be1da1d8507c84522e942383053da3ceabb389cdf746369f201bc`); I did not edit it. Scratch artifacts were copied into this report; scratch was removed before yielding. No tools installed.
