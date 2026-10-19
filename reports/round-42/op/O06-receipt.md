- Seat: O06 | executor | O | date 2026-10-19 | baseline ac47c78

# O06 — operability receipt draft (claim O, the N6 couples-extractor fix)

**Status: DRAFT receipt, in-flight snapshot; claim O is not certified here.**
This seat landed nothing but this file. At its cut
(`2026-10-19T15:58:51Z`, `find reports/round-42 -type f | sort`) the round
contained four files — `claims.json`, `targets.json`,
`telemetry/dispatch-declared.json`, `op/O09-scribe.md` — so every sibling the
claim depends on (`K01` scout, `O01` fix draft, `O02` controls, `O03` predicted
census, `O04`/`O05` verifications, `O08` queue update, `O12` policy check) is
**absent at this stamp** and filed under `## Owed`, never assumed. What this
receipt does now, from primary records and its own read-only commands, is
(a) pin the before-state of claim O precisely, (b) reconcile the counting units
so a corrected census cannot be mis-stated, (c) establish the corrected-census
prediction and its delta decomposition, and (d) file four findings that bear on
the claim's own wording and on the fix host.

## 1. State pins

| pin | value | source |
|---|---|---|
| HEAD | `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4` | `git rev-parse HEAD`, this seat |
| working tree | `?? reports/round-42/` only | `git status --porcelain` |
| r39 policy under correction | `reports/round-39/calib/basename-couples-policy.md`, sha256 `105dfff6c667ad5b77c28be8d6070ec243b5e19029fb60ae83d6028aa2e941cf`, 107 lines | `sha256sum` + `wc -l` |
| claim under receipt | `reports/round-42/claims.json:13-17` (claim O, axis operability) | read |
| env | `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` for every command below | set |

No filed byte was edited; no `run-validation.py` was executed; no git, network
or install action beyond read-only `git show`/`ls-tree`/`rev-parse`.

## 2. Before-state (measured, not asserted)

**2.1 The wrapped field is real and singular.** Corpus-wide `- couples:` scan
over the 220 entries: `total couples fields: 220`, `wrapped (continuation
lines): 1`. The one field is
`corpus/knowledge/linguistics/phonetics-phonology.md:72-77`; `:76` ends `tone-`
and `:77` begins `prosody.md`. This reproduces r39 Ca04 D1
(`reports/round-39/calib/Ca04-verify.md`, D1) and O09's item 1.

**2.2 Both located hosts are single-line, and the capture truncates.** The two
filed resolver instruments capture the field with `re.M` single-line semantics:
`reports/round-19/audit/entry-audit.py:75` and
`reports/round-27/audit/entry-audit.py:275`, each
`re.search(r"^- couples:\s*(.*)$", text, re.M)`. Applied to the live field the
r19 shape returns the string
`'language (this file, core method); myth (divine/true names, taboo'` — **zero
`.md` tokens**. `tools/` carries no couples resolver, so the only located hosts
are filed bytes (see §5.1).

**2.3 The r39 policy's 2504 is a per-entry-deduplicated, brace-expanded token
unit — reproduced exactly.** Re-running the r39-shape (single-line) extractor
read-only against the tree at r39's own baseline `dfb0719` (212 entries,
`git ls-tree` + `git show`, no checkout) yields:

```
entries=212 refs=2504 = direct 2335 + fallback 163 + ambiguous 0 + unresolved 6
```

byte-for-byte the arithmetic of `reports/round-39/calib/Ca03-basename-policy.md:35-36`
and Ca04 §1. **The unit is therefore pinned: refs = sum over entries of
`len({brace-expanded tokens})`** (per-entry dedup, brace expansion applied).
Three nearby-but-different counts exist and must never be substituted:

| unit | single-line | block+de-hyphen |
|---|---|---|
| raw regex matches summed, no dedup, no brace expansion | 1851 | 1855 |
| per-entry dedup, no brace expansion | 1848 | 1852 |
| global distinct strings across the corpus | 400 | 403 |
| **refs = per-entry dedup, brace-expanded (the r39 unit)** | **2607** | **2611** |

The 2504 → 2607 gap is **not** the defect; it is the entry denominator moving
212 → 220 across r39–r40 landings. The defect's own contribution is exactly
**+4 refs** (§2.4).

**2.4 The wrapped field contributes exactly 4 refs; only 2 resolve.** Read-only
block extraction (continuations to the next `- ` header field, soft-hyphen wrap
undone) over `:72-77` yields tokens `sound-change.md`, `tone-prosody.md`,
`sound-symbolism.md`, `writing-systems.md`. Existence against
`corpus/knowledge/linguistics/`: `sound-symbolism.md` ✓ and `writing-systems.md`
✓ exist; `sound-change.md` and `tone-prosody.md` are **absent** (and have zero
index hits anywhere in `corpus/knowledge`). Corpus-wide, single-line vs
block+de-hyphen differs in **exactly one file** —
`corpus/knowledge/linguistics/phonetics-phonology.md`, block-only tokens
`['sound-change.md', 'tone-prosody.md', 'sound-symbolism.md', 'writing-systems.md']`,
single-only `[]`. Totals 2607 → 2611.

**2.5 The de-hyphenation distinction is load-bearing (finding F-O06-2).** A block
parser that joins continuation lines *verbatim* — the shape r39 C14 used
(`reports/round-35/cov/C14-audit-6-10.md:227-236`) — emits the **mangled** token
`prosody.md`, not `tone-prosody.md`: the field writes `tone-` at the end of
`:76` and `prosody.md` at the start of `:77`. Block-without-de-hyphenation yields
global distinct 403 but with `prosody.md`; block-with-de-hyphenation yields 403
with `tone-prosody.md`. Both give the same 2611 refs and the same 8 unresolved,
so **the census totals cannot distinguish a correct fix from a mangling one**;
only the token *identity* can. A control that checks counts alone will pass a
mangling parser (finding filed for O02/O04/O05).

## 3. The corrected census (prediction, this seat's independent read-only run)

At the current tree (`ac47c78`, 220 entries), same unit, same two-tier
resolution as the policy:

```
single-line (r19/r27 shape) : entries=220 refs=2607 = direct 2435 + fallback 166 + ambiguous 0 + unresolved 6
block+de-hyphen (fixed)     : entries=220 refs=2611 = direct 2437 + fallback 166 + ambiguous 0 + unresolved 8
```

**Delta decomposition (finding F-O06-1).** The +4 refs are **+2 direct and +2
unresolved** — *not* "+4 named targets read". The claim's `after_required`
wording ("the wrapped field read whole on the live corpus … zero phantom
attributions remaining or each dispositioned") is directionally right but
loose: under the fixed extractor the field's 4 tokens resolve 2 direct / 2
unresolved, so the phantom count **rises** from 0 to 2 rather than falling. The
before-state is *zero phantom attributions from this field*, because the
single-line extractor captures none of them (§2.2); the phantoms are a
consequence of the fix, which is precisely why the fix must ship with their
disposition.

**Unresolved-set ledger under the fixed logic (8 rows, every one attributed).**

| # | token | entry | family | disposition route |
|---|---|---|---|---|
| 1-3 | `honorifics-and-register.md`, `naming-and-onomastics.md`, `phonology-basics.md` | `corpus/knowledge/linguistics/language-contact.md:7` | 3 never-written seeds | corpus leg (integrator); pre-existing, unchanged by the fix |
| 4-5 | `../linguistics/phonology-sanity.md` ×2 | `corpus/knowledge/verification/label-channel-routing-verification.md:14`, `corpus/knowledge/synthesis/typed-label-routing-workflow.md` | X26-1 phantom (resolves nowhere) | corpus leg; pre-existing, unchanged |
| 6 | `-gate.md` | `corpus/knowledge/verification/gate-frozen-run-standard.md:15` | **glob fragment**, not a couples ref | policy §5.6: a successor instrument must skip or separately class it; must not be counted as a couples finding |
| 7-8 | `sound-change.md`, `tone-prosody.md` | `corpus/knowledge/linguistics/phonetics-phonology.md:76-77` | **the 2 new phantoms** the fix surfaces (prospective sibling files named in the field's own prose, never written) | corpus leg or documented as prospective |

Rows 1-6 are the six r39 unresolved tokens exactly — five distinct strings, of
which `../linguistics/phonology-sanity.md` now appears under two entries (hence
six rows); rows 7-8 are the two new phantoms the fix surfaces. So the honest statement of the fix's effect
on unresolved counts is **6 → 8, of which 2 are new and 1 of the 8 is a glob
fragment the policy already says not to count**.

## 4. What the claim still owes (unestablished here)

The claim's `after_required` names four deliverables; at this cut **none exists
in the tree**: (i) the fixed extractor durable at a named host — see §5.1;
(ii) the wrapped field read whole on the live corpus — §3 is a *prediction* from
this seat's synthetic re-parse, not a run of a landed tool; (iii) the corrected
census filed; (iv) selftest green (controls at `op/O02-controls.md`, absent).
The claim's `counting_commands` are `python3 reports/round-42/run-validation.py`,
which this seat is forbidden to run in-tree (`targets.json:8`). Its thresholds —
"the wrapped field reads 4/4 targets; the corrected census reproduces the r39
policy's arithmetic minus the phantoms; two independent verifiers" — cannot be
graded until O01-O05 land and the parent runs the validator in an isolated copy.

## 5. Findings filed

**5.1 F-O06-4 — the fix host is not yet identified, and every located host is a
filed byte.** K01's mission (`targets.json:16`) is exactly this identification;
at this stamp it has not landed. The two extractors that actually implement the
defect (`reports/round-19/audit/entry-audit.py:75`,
`reports/round-27/audit/entry-audit.py:275`) are under `reports/round-19|27/`,
which the round's non-goal "no filed byte rewrites" (`claims.json` non_goals;
`targets.json:8`) bars editing in place. A `tools/harness/` couples checker is
the only durable route consistent with the non-goals, and `tools/harness/` today
contains no couples resolver (`packet_links.py`, `packet_uncertainty.py`,
`r8_checks.py`, `receipt_guard.py`, `receipt_guard_adoption.py`,
`round_runner_conformance.py`). **This choice is the integrator's, not this
seat's**; the receipt records it as owed.

**5.2 F-O06-3 — the landed r39 policy is verbatim, so its §1 still states the
defective single-line rule.** Grep of the landed
`reports/round-39/calib/basename-couples-policy.md` (sha `105dfff6…`) finds **no**
occurrence of `wrapped`, `block`, `blocker` or `continuation`; Ca04's Owed
required the integrator to "either apply D1+D2 (one sentence each) or land
verbatim and queue both to the successor instrument". It landed verbatim, so the
successor note (O12's assignment, `targets.json`) is the carrier of the
correction and the policy document itself must stay filed unchanged.

**5.3 F-O06-1 / F-O06-2** — the delta wording and the de-hyphenation trap, §3
and §2.5 above.

**5.4 F-O06-5 — cross-seat convergence, and a classification correction to
O03.** Sibling fragments landed after this receipt's first cut
(`op/O03-predicted.md`, `op/O04-verify.md`, `scout/K01-n6-scout.md`). This seat
re-ran its census independently at both revisions and **agrees with O03's
totals exactly**: `dfb0719` 212 entries `2504 = 2335 + 163 + 0 + 6` (single-line)
→ `2508 = 2337 + 163 + 0 + 8` (block+de-hyphen); `ac47c78` 220 entries
`2607 = 2435 + 166 + 0 + 6` → `2611 = 2437 + 166 + 0 + 8`. Three seats
(O03, O04, O06) now reproduce the r39 arithmetic from primary `git show` reads.

One correction: O03 §4-§6 states the wrapped field's two live tokens
(`sound-symbolism.md`, `writing-systems.md`) are `fallback`, not `direct`, at
`dfb0719`. **That is wrong** — this seat's direct check returns
`sound-symbolism.md at r39? ['corpus/knowledge/linguistics/sound-symbolism.md']`
and the same for `writing-systems.md`, so Tier 1 resolves both as `direct`; the
`+2 direct` delta in O03's own table is the correct reading, and its prose
contradicts its table. O03's substantive point survives intact — the field's
**absent** tokens are `sound-change.md` and `tone-prosody.md` (0 index hits),
which is what the 2 new phantoms are — and its §7 ledger classifies
`prosody.md`/`tone-prosody.md` correctly as `unresolved` (mangled artifact).
The correction affects only the `direct`/`fallback` attribution of two tokens,
not any total.

O04's §4 negative result is independently confirmed here: a space-join block
parser yields `prosody.md` (3/4 of the field's named targets), so the claim's own
"4/4" threshold is **not** met by a bare block parser — a hyphen-aware join is a
required second repair (F-O06-2).

## Owed

- **Integrator:** identify and land the durable fix host (§5.1) and rule on the
  filed-byte boundary; apply or queue Ca04 D1/D2 to the successor instrument
  (§5.2); after O01-O05 land, run `python3 reports/round-42/run-validation.py`
  in an isolated copy and grade claim O's thresholds on the delivered revision.
- **O01/K01:** the fix host and the fenced patch; a block parser must undo the
  soft-hyphen wrap or it emits `prosody.md` (§2.5).
- **O02/O04/O05:** the wrapped-field positive control must assert **token
  identity** (`tone-prosody.md`), not only the 4/4 count, or it will pass a
  mangling parser (§2.5); the synthetic phantom negative must cover the
  `-gate.md` glob-fragment class (§3 row 6).
- **O03/O12:** the corrected census must state its **unit** and its **entry
  denominator** (refs, per-entry dedup + brace expansion, at 220) — a "2504
  minus the phantoms" statement is a denominator error (§2.3).
- **This seat:** `op/O01-fix-draft.md`, `op/O02-controls.md`,
  `op/O03-predicted.md`, `op/O04-verify.md`, `op/O05-traps.md`,
  `op/O08-queue-update.md`, `op/O12-policy-check.md`, `scout/K01-n6-scout.md`
  were all absent at `2026-10-19T15:58:51Z`; the claim's after-state cannot be
  described as landed until they arrive.

## Citations

- Assignment and write boundary: `reports/round-42/targets.json:9` (seat O06,
  out `op/O06-receipt.md`), `:4-9` (shared rules), `:8` (no in-tree
  `run-validation.py`), `:16` (K01), `:41-73` (O01-O05), `:92-94` (O08),
  `:105-107` (O12).
- Claim O and thresholds: `reports/round-42/claims.json:13-17`; non-goals
  (`no filed byte rewrites`) `:19-21`.
- r39 policy and its arithmetic: `reports/round-39/calib/basename-couples-policy.md:35-36,54-65,100-107,104` (sha `105dfff6c667ad5b77c28be8d6070ec243b5e19029fb60ae83d6028aa2e941cf`);
  `reports/round-39/calib/Ca03-basename-policy.md:35-36`.
- D1 and the mangling note: `reports/round-39/calib/Ca04-verify.md` (D1;
  `to-verify` on C14's `prosody.md`); C14's block parser
  `reports/round-35/cov/C14-audit-6-10.md:227-236`.
- Extractor hosts: `reports/round-19/audit/entry-audit.py:75` (+`:74-96`),
  `reports/round-27/audit/entry-audit.py:275` (+`:270-288`).
- Wrapped-field bytes: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`.
- Queue row: `reports/round-40/op/defect-queue-v2.json:362-369`
  (`N6-couples-extractor-wrapped-field`, `carried-with-owner`).
- Prior in-flight snapshot: `reports/round-42/op/O09-scribe.md` (items 1-5).
- Command outputs (this seat, 2026-10-19, lane root, all read-only; no
  `run-validation.py`, no git mutation, no network/install):
  (a) `git rev-parse HEAD` → `ac47c78…`; `git status --porcelain` → `?? reports/round-42/`;
  `find reports/round-42 -type f | sort` → 4 files; `date -u` → `2026-10-19T15:58:51Z`.
  (b) corpus `- couples:` scan → 220 fields, 1 wrapped
  (`phonetics-phonology.md:72`).
  (c) r19-shape capture on the live field → `'language (this file, core method);
  myth (divine/true names, taboo'` (0 `.md` tokens).
  (d) r39-shape reproduction at `dfb0719` via `git ls-tree`/`git show` (212
  entries) → `2504 = 2335 + 163 + 0 + 6`, matching the filed policy exactly.
  (e) census at `ac47c78` (220 entries) → single-line `2607 = 2435 + 166 + 0 + 6`;
  block+de-hyphen `2611 = 2437 + 166 + 0 + 8`; unresolved sets as §3.
  (f) unit cross-check → raw matches 1851/1855; per-entry dedup 1848/1852;
  global distinct 400/403.
  (g) block-only token set at `phonetics-phonology.md` →
  `[prosody.md | tone-prosody.md, sound-change.md, sound-symbolism.md, writing-systems.md]`;
  existence `sound-symbolism.md` ✓, `writing-systems.md` ✓, `sound-change.md` ✗,
  `tone-prosody.md` ✗; index hits 0 for both absent tokens.
  (h) `grep -in "wrapped|de-hyphen|block parser|block extraction|disposition"`
  in the landed policy → no matches; `sha256sum` → `105dfff6…`; `wc -l` → 107.
  (i) `ls tools/harness/` → no couples resolver; `glob corpus/knowledge/verification/*-gate.md`
  → 5 files (the `-gate.md` token is a glob fragment, policy §5.6).
  (j) block+de-hyphen census at `dfb0719` (212 entries) →
  `2508 = 2337 + 163 + 0 + 8`, unresolved = the six pre-existing tokens plus
  `sound-change.md` and `tone-prosody.md` (§5.4).
  (k) `git ls-tree` at `dfb0719` → 212 entries, 21 under `linguistics/`;
  `sound-symbolism.md` and `writing-systems.md` both present under
  `corpus/knowledge/linguistics/`, so the field's two live tokens are `direct`
  at r39 (§5.4 correction to O03 §4).
- Cross-seat: `reports/round-42/op/O03-predicted.md:19-23,33-38,140-157` (totals
  agreeing with §3; the `fallback`-at-r39 prose corrected in §5.4),
  `reports/round-42/op/O04-verify.md:63-95` (the space-join 3/4 negative result),
  `reports/round-42/scout/K01-n6-scout.md:100-110,251-272` (host set and the
  filed-byte constraint).
