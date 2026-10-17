# Header Conformance Readings — Measuring the Fleet source/verified-at/recheck Trio Without Reading-Laundering

- topic: The measurement contract for the corpus entry header — the fleet sentence ("each `knowledge/` entry opens with `source:`, `verified-at:` and `recheck:`") versus this lane's gate profile (`topic`/`sources`/`couples`), the three defensible readings of the source leg that make a single corpus report three different conformance counts (64 / 3 / 0 of 179 on 2026-10-17), a count-statement schema so no header count circulates without its reading id, a context table for which reading a given check may cite, the digest-pin constraint that keeps three placement stragglers deliberately unrepaired, repair discipline that forbids boilerplate `verified-at` lines, and the open integrator question this lane reports but does not absorb.
- sources: primary receipts inspected 2026-10-17 — fleet contract sentence read directly at `/home/vgpnk/Projects/shokunin/CORPUS.md:17`; `corpus/QUALITY.md` items 1–3 (the lane admission bar, which the trio is not part of); `tools/gates/provenance-audit.py:75` (`FIELD_NAMES = ("topic", "sources", "couples")`); `reports/round-9/metadata/audit.md` (three-reading table, A 83→64, B 4→3, C 0→0, close 2026-10-17); `reports/round-8/metadata/m11-verification.md` and `reports/round-8/metadata/m07-synth-13-24.md` (the lane's shard protocol: plural `- sources:` is the source leg, no separate singular line added); `reports/supplement-opencode-1/28-corpus-contract.md` §2/§6/§7 (gap statement, bounded correction plan, limits); `tools/gates/frozen/provenance-audit/r9-pre/expected.json` (digest pins, live bytes re-hashed by this entry); `corpus/README.md` revision 1.2 known-gaps paragraph. Live re-measurement commands are quoted with output hashes in §3; no external source is claimed beyond the fleet contract sentence and the in-repo receipts.
- couples: sibling verification entries — `provenance-audit-ledger-format.md` (claim-level ledger schema; this entry is header-level and does not restate it), `citation-format-and-source-registry.md` (in-entry citation syntax and source-version registry, not header conformance), `gate-frozen-run-standard.md` (the freeze/pin standard whose digests constrain §6), `verification-method-overview.md`, `to-verify-triage-protocol.md`; synthesis handoff — `../synthesis/worldbible-integration-contract.md`, `../synthesis/consistency-verification-checklist.md`; lane index — `corpus/README.md` (the known-gaps paragraph this entry answers). The corpus's own counting tool `tools/source-audit-inventory.py` is the parallel count surface for `to-verify` markers; this entry's counts are header counts, not marker counts.
- verified-at: 2026-10-17 — live re-measurement at 21:28–21:30Z on worktree `e3a1ec9435787328ac9f828f96cb6390e4916b8f` (concurrent-shard dirty tree; `corpus/knowledge/` itself unchanged at measurement, verified by mtime sweep): all three readings re-derived with an independent reimplementation and with the round-9 verbatim command (A=64, B=3, C=0, both agreeing); per-partition A-breakdown recomputed; the three B-remainder files' live sha256 re-hashed against the `r9-pre` pin (all match); the lane gate re-run on a B-conformant entry (exit 0). What was NOT checked: no entry's sources were re-inspected, no URL was re-fetched, and the fleet ruling question was not adjudicated.
- recheck: before citing any header-conformance count in a handoff, SCORECARD row, or acceptance claim — re-run the §3 command on the then-current tree and quote its reading id; before repairing any of the §6 pinned files, re-check the pin; recheck this entry if `tools/gates/provenance-audit.py` `FIELD_NAMES` changes, if `CORPUS.md` is amended, or if the integrator rules on the fleet sentence.

## 1. The gap this entry fills

`corpus/README.md` revision 1.2 known-gaps states it: "Most historical entries lack the fleet's complete `source`, `verified-at`, `recheck` header. The existing provenance gate checks the older topic/sources/couples profile, not full corpus conformance." What exists today is: (a) a fleet contract sentence, (b) a lane gate profile that cannot see the trio, (c) two metadata sweep rounds (8 and 9) that repaired part of the corpus under a chosen reading, (d) a three-reading audit whose counts were left explicitly unreconciled, and (e) a contract question filed with the integrator and still open. What does not exist is a reader-facing measurement contract: how to *measure*, *state*, *cite*, and *bound* a header-conformance count so that the same corpus cannot be reported as 64, 3, or 0 conformant depending on who is counting. This entry is that contract. It is a verification instrument for the corpus's own provenance apparatus — it verifies no historical claim and adjudicates no entry's content.

## 2. Vocabulary and the three contracts in play

| term | definition used here |
|---|---|
| **header (opening block)** | the text of an entry before its first `## ` heading |
| **the trio** | the fleet fields `source:`, `verified-at:`, `recheck:` as named by the fleet sentence |
| **the gate profile** | the lane fields `topic`, `sources`, `couples` enforced by `tools/gates/provenance-audit.py` |
| **reading** | a named, written definition of what counts as satisfying the trio's source leg and where it must sit; a reading is not a preference — it is a reproducible rule that changes the number |
| **header count** | `missing / total` entries under one named reading, at one tree revision, on one date |
| **repair** | an in-place edit to a corpus header (lane-authorized); distinct from a **correction** to a filed report (append-only, new bytes) |

Three contract texts govern, and they do not say the same thing:

| contract text | what it requires | what it can see |
|---|---|---|
| fleet `CORPUS.md:17` (inspected 2026-10-17): "Each `knowledge/` entry **opens with** `source:`, `verified-at:` and `recheck:`" | the trio, in the opening block, singular field names | nothing executable — it is prose |
| lane gate `tools/gates/provenance-audit.py:75`: `FIELD_NAMES = ("topic", "sources", "couples")` | the gate profile only | header presence/emptiness of three different fields; **blind to the trio by construction** |
| lane bar `corpus/QUALITY.md` items 1–3 | provenance, calibration, coupling as *content* obligations | nothing about field names |

Demonstration of the gate's blindness (run by this entry, 2026-10-17): `python3 tools/gates/provenance-audit.py corpus/knowledge/verification/to-verify-triage-protocol.md` → exit 0, `INFO scan: files=1 marks=13 mark-lines=13 findings=0 blocked=0`. That entry passes the lane gate while reading A (§3) counts it as missing the trio's source leg. A green gate run is therefore never evidence about the trio, and a red reading-A count is never evidence that the gate is broken. The two instruments measure different contracts.

A header is provenance *apparatus*: a pointer to what was checked, when, and when to re-check. Its presence is not evidence that any claim is true; its absence is not evidence that an entry is unverified. The `verified-at` value is the only field that can carry a claim — it must name the check actually performed (round-8 shard protocol), never a template date.

## 3. The three readings, and today's numbers

Definitions (as established by `reports/round-9/metadata/audit.md`, re-implemented and re-run by this entry):

| reading | source leg | placement | verdict vocabulary |
|---|---|---|---|
| **A — strict/literal** | singular `- source:` | opening block | "does not literally open with the fleet sentence" |
| **B — lane/plural** | `- source:` **or** `- sources:` | opening block | the reading the lane's round-8/9 metadata shards applied (`m07`, `m11`: the existing `- sources:` ledger *is* the source metadata) |
| **C — whole-file** | either | anywhere in the file | weakest reading; satisfies presence, ignores placement |

Reproduction command (the round-9 auditor's, run verbatim 2026-10-17T21:29:14Z; output sha256 `5464c9b08f939f65f4c99316251cd4860f605187d3887a6e503a0b04ba1a1076`):

```sh
python3 -c "import re,pathlib;root=pathlib.Path('corpus/knowledge');pat=re.compile(r'(?:^[-*]\s|;\s)(source|verified-at|recheck)\s*:',re.M);files=sorted(root.rglob('*.md'));miss=[(p.as_posix(),d) for p in files for d in [sorted({'source','verified-at','recheck'}-{m.group(1) for m in pat.finditer(re.split(r'^## ',p.read_text(encoding='utf-8'),maxsplit=1,flags=re.M)[0])})] if d];print('files=%d missing_any=%d'%(len(files),len(miss)))"
# files=179 missing_any=64        (reading A)
```

Results — this entry's independent reimplementation and the round-9 verbatim command agree exactly, and agree with the round-9 audit's close:

| state | A (strict) | B (plural) | C (whole-file) |
|---|---|---|---|
| round-9 baseline HEAD | 83 / 179 | 4 / 179 | 0 / 179 |
| round-9 close (audit.md) | 64 / 179 | 3 / 179 | 0 / 179 |
| **round-10 re-measure, 2026-10-17T21:29Z, tree `e3a1ec9`** | **64 / 179** | **3 / 179** | **0 / 179** |

Reading-A remainder by partition (recomputed this entry, same definitions): civilizations 19/94, culture-material 16/16, linguistics 16/16, verification 13/13, myth-symbol 0/16, synthesis 0/24. The partition shape matches the round-9 audit's close description exactly (positions 39–57 of civilizations, all culture-material, all linguistics, all verification). The reading-B remainder is exactly three files, all in `verification/` (§6).

Interpretation, stated as the count-statement rules require:

- The corpus did **not** move between round-9 close and this re-measure: all three counts identical. The round-10 regimen had not repaired any header at measurement time (verified: no file under `corpus/knowledge/` newer than the round-10 wave start).
- Under reading A the missing leg is almost always the *singular* form only — those entries carry a plural `- sources:` ledger, which reading A by definition does not accept. A/B/C differ on a definitional boundary, not on corpus quality.
- **The readings are not monotone under growth.** A newly authored entry written to the lane's operative profile (plural `- sources:`, no singular line) increases the A-count by one while nothing regressed. Measured after this entry and its sibling round-10 verification entry (`verification-independence-anti-circularity.md`, a different gap) both landed: `files=181 A=66 B=3 C=0` (2026-10-17T21:31:22Z, §3 command) — two B-conformant additions, two more A-missing files, zero regressions. An A-count that rises while B and C hold steady is reading arithmetic, not decay — which is precisely why a count without its reading id is not citable. (This entry's own pre-landing prediction of `65/180` was falsified by the sibling's same-window landing; the measured figure supersedes it, recorded here as an in-entry demonstration that counts are revision- and time-stamped.)

## 4. Count-statement schema

Any header-conformance count — in a report, a SCORECARD row, an acceptance script, a handoff note — must carry all six fields, or it is not citable:

```yaml
reading: A | B | C            # the named definition from §3, or a new reading registered per §5
scope: <path glob, e.g. corpus/knowledge/**/*.md>
total: <n files matched>
missing: <n under this reading>
command: <exact command, one line>
run_at: <date, with UTC time>
revision: <git rev of the tree measured>
```

Rules:

1. A bare `missing/total` figure is not a finding. Two rounds of lane work used three readings of the same corpus; the number is a function of the reading, and the reading is a function of who wrote the check.
2. A count never asserts that a *named file* is conformant — it asserts field presence under a reading. Per-file claims must name the file and the reading.
3. Counts are dated and revision-stamped; a recount returning different numbers means the earlier report is stale or the tree moved, not that the contract changed silently (`28-corpus-contract.md` §6.5).
4. Negative claims ("no entry lacks X", "every entry opens with Y") require the reading id and the sweep — otherwise they are false under at least one defensible reading of this corpus.
5. Never merge readings into a range ("3–64 missing") in a headline. Ranges hide which definition produced which end.

## 5. Reading registry and context table

New readings may be registered, but only in writing and only with a falsification condition — otherwise they are ad-hoc counting. Current registry: A/B/C as defined in §3; no others are registered.

| context | citable reading | why |
|---|---|---|
| Admitting a new entry this lane authors | **B** | it is the lane's operative profile (round-8/9 shard protocol); the entry must still carry a scope-bearing `verified-at` |
| Auditing legacy entries / reporting corpus state | **A, B and C together** | the audit's job is to show the reading-dependence, as round 9 did; a single reading alone over- or under-claims |
| Claiming the lane gate passes | **none of them** | the gate measures `topic/sources/couples`; a gate run says nothing about the trio (§2) |
| A lore handoff or world-bible packet | **B**, plus the entry's own `verified-at`/`recheck` values | the recipient needs what was checked and when to re-check, not a corpus-wide score |
| SCORECARD / acceptance rows | the reading id must appear in the row text | rows survive rounds; an unlabeled count becomes a false history |
| Fleet-level conformance claim | **blocked pending the integrator ruling** (§8) | the fleet sentence is the fleet's to interpret; this lane reports its measurement and does not decide the reading |

## 6. Placement stragglers and the digest-pin constraint

The reading-B remainder is exactly three files, each with a singular `- source:` line and the trio sitting *below* the first `## ` heading, so they satisfy B's field requirement but not the fleet sentence's "opens with" placement:

| file | first `## ` heading | trio lines | live sha256 vs `r9-pre` pin |
|---|---|---|---|
| `verification/citation-format-and-source-registry.md` | 13 | 15–17 | match |
| `verification/myth-consistency-gate.md` | 6 | 9–11 | match |
| `verification/provenance-audit-ledger-format.md` | 6 | 9–11 | match |

The pin check (this entry, 2026-10-17T21:29:01Z): every input digest in `tools/gates/frozen/provenance-audit/r9-pre/expected.json` re-hashed against the live tree — all 20 inputs match, including these three files. Consequence, recorded as decision DR-3: relocating those lines is a corpus edit that would break a committed frozen baseline; the placement question is a *contract* question, and the lane does not buy conformance by silently drifting a pin. The three files stay as-is until either the integrator rules or a new freeze is deliberately authored.

## 7. Repair discipline

- **Only honest repairs.** An entry gains `verified-at`/`recheck` only if it can cite the check it actually performed (locator sweep, header audit, passage recheck — as round-8's shards did per file). A boilerplate date is a fabricated verification and is worse than a missing field: it converts an honest absence into a false presence (`28-corpus-contract.md` §6.3, adopted here).
- **No bulk rewrite.** The 64-entry A-remainder is a normative gap, not a backlog to burn down by template (`28-corpus-contract.md` §6). Bulk header rewrites are exactly the byte-churn the append-only rules exist to prevent.
- **Corpus headers: in-place, logged.** Repairs to `corpus/knowledge/` headers are lane-authorized in-place edits with per-file evidence fragments (the round-8/9 metadata pattern), never silent.
- **Filed reports: append-only.** A correction to a filed round report is new bytes with a superseding note — never a rewrite of the old report, and never a re-pin of a frozen artifact to bless a change (`gate-frozen-run-standard.md` §6; round-9 D09 S1's re-pin warning is the standing lesson).
- **Counting commands change nothing.** Every command in §3 is read-only; a repair round must re-run them and publish before/after counts under the same reading.

## 8. What a count does and does not prove

| a header count CAN show | a header count CANNOT show |
|---|---|
| how many entries carry the trio's fields under one named reading, at one revision, on one date | that any cited source supports any claim |
| the shape and size of a conformance gap, and its movement between rounds | that entries missing a field are unverified (many carry the apparatus elsewhere — e.g. in-body `## Source registry` blocks) |
| that a repair round changed what it claims to have changed (before/after, same reading) | that a green state makes the corpus "verified" — the trio is apparatus, the claims are not inspected by any count |
| that two implementations of the same reading agree (as §3's two did) | that the reading is the right one — that is a contract question (§8 escalation) |

## 9. Decision record

| id | date | decision | evidence | status / reopen |
|---|---|---|---|---|
| DR-1 | 2026-10-17 | The lane-operative reading for entries this lane authors and for handoff claims is **B** (plural `- sources:` in the opening block satisfies the source leg). | `reports/round-8/metadata/m07-synth-13-24.md` §Protocol; `reports/round-8/metadata/m11-verification.md`; `reports/round-9/metadata/audit.md` reading B. | Standing until the integrator rules on the fleet sentence (§10). Reopen on a `CORPUS.md` amendment or a `FIELD_NAMES` change. |
| DR-2 | 2026-10-17 | Header counts are citable only with the six-field schema of §4; the readings A/B/C are the registered set, and no headline may merge them. | The round-9 audit's three defensible answers for one corpus (83/4/0 at baseline; 64/3/0 at close); this entry's re-measure reproducing 64/3/0 independently. | Standing. Reopen if a new reading is registered in writing with a falsification condition. |
| DR-3 | 2026-10-17 | The three §6 placement stragglers stay unrepaired in this regimen; their live bytes match the `r9-pre` frozen pin, so relocation would drift a committed baseline to buy a placement clause. | Live re-hash of all 20 pin inputs, 2026-10-17T21:29:01Z, all match; `gate-frozen-run-standard.md` §6 tamper semantics. | Reopen when a new freeze is deliberately authored, or the integrator rules placement. |
| DR-4 | 2026-10-17 | No boilerplate `verified-at` on the A-remainder; entries gain the trio only with a check they performed and can cite. | `28-corpus-contract.md` §6.3 ("a placeholder date is a fabricated verification"); round-8 shard fix-shape (each `verified-at` states what the pass checked and what it did not). | Standing; a repair round may add per-file honest values but may not template. |
| DR-5 | 2026-10-17 | This entry does not decide the fleet sentence. The lane reports its measurements (this file) and keeps the question with the integrator. | `28-corpus-contract.md` §6.2/§7 (filed question, owner = parent/integrator for fleet-file changes); `PROVINCE.md` (report contested scope, never absorb). | Open escalation, not a lane decision. |

## 10. Escalation state (reported, not absorbed)

The fleet sentence and the lane profile are two different contracts. Three readings are defensible for one corpus. This lane has filed the question with the integrator (`28-corpus-contract.md` §6.2: "The integrator either amends CORPUS.md's sentence to a profile-inherits-its-gate rule or declares the lane non-conformant") and, per lane rules, does not amend fleet files, does not reinterpret the fleet sentence for the fleet, and does not convert its own reading choice (DR-1) into a fleet-level claim. Until the ruling: any fleet-level "conformant/non-conformant" statement about this corpus is `(to-verify)` against the integrator's answer, and lane documents should cite their reading explicitly (as this entry does).

## 11. What a worldbuilder or handoff reader takes from this

1. When a corpus or world-bible packet claims "entries are sourced and dated", ask which reading produced the claim; the honest answer is a reading id, a count, and a date — or `(to-verify)`.
2. Treat headers as apparatus: a `verified-at` value is usable only when it names the check performed; a template date is a fabrication, not a badge.
3. The same discipline transfers to a fictional archive: an in-world register of provenances (who checked what, when, and when to re-check) is only as good as its counting rule — write the rule down next to the count.
4. Do not ask this entry to certify any historical claim or any world-bible fact; it certifies nothing about content, only about how the corpus's own apparatus is measured.

## 12. Limits

- All counts are field-presence measurements under named readings, on one tree revision, at one date. They are reproducible (§3) but they are not quality scores; `tools/source-audit-inventory.py`'s caveat applies in kind: marker (and here, field) absence is not verification.
- The A/B/C definitions were taken from `reports/round-9/metadata/audit.md` and re-implemented independently; agreement of two implementations is evidence of reproducibility, not a ruling on which definition is correct.
- The fleet sentence was read directly in this pass (`CORPUS.md:17`); no other fleet file was inspected, and no fleet file was written.
- The tree measured was dirty from concurrent round-10 shards; `corpus/knowledge/` itself was unchanged at measurement time (mtime sweep), and every number above is reproducible with the §3 command on a clean checkout of `e3a1ec9`.
- This entry was authored inside a live wave; if a sibling shard repairs headers after its landing, §3's numbers become stale by design — the recheck trigger is the §3 command itself, not this paragraph.
