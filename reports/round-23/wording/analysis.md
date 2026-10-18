# R23-O01..O04 — the PLACEHOLDER_RE false positive on D4-CL08: analysis

Date: 2026-10-18. Seat: round-23 wording (4/4 wording claims). NON-CANON
engineering evidence; not a lore receipt. All counts below carry their
commands; run receipts live in `reports/round-23/wording/evidence/`.

## 1. The symptom

The full historical successor acceptance — the frozen round-20 validator
(`reports/round-20/run-validation.py`, sha256
`2b7a252b5449415dddac2e667ed2e192df800a80173849989fa72423961646da`) driven
through the round-22 deterministic selector adapter
(`reports/round-22/fixes/tie-break.py`, sha256
`2856a571da286b62b4eced7da610f5cebd46f3504bdf2f6dd8a53d60272dce0a`) — exits 1
on exactly one failure after the round-22 selector fix landed:

- `reports/round-22/fixes/tie-break.md` ("Integration status"): the successor
  `--check` "exposes a **different** historical check failure: the old
  `PLACEHOLDER_RE` matches the legitimate word `unchanged` in D4-CL08's
  `unchanged-foreign-path control` basis."
- `reports/round-22/routed-resolution.json:16`: "Open tail: PLACEHOLDER_RE
  false positive on D4-CL08's legitimate phrase 'unchanged-foreign-path
  control' blocks the full historical check — routed to round 25 (validator
  wording fix), not weakened here". Round 23 dispositioned it early, here.

## 2. The mechanism

`reports/round-20/run-validation.py:87-89`:

```python
PLACEHOLDER_RE = re.compile(
    r"\b(tbd|tba|todo|placeholder|boilerplate|same[- ]as[- ](?:above|below)|"
    r"as (?:above|below)|see (?:above|below|other)|copy of|unchanged)\b", re.I)
```

`uncertainty_problems()` (same file, :442-469) runs this regex over each
claim's `uncertainty_basis` cell parsed from the selected packet's
`## claim_ledger` table and flags any hit as `placeholder basis` (:459-460).
Python's `\b` is a boundary between a word character and a non-word character;
`-` is a non-word character, so the token `unchanged` in the hyphenated
compound **`unchanged-foreign-path`** is bounded on both sides and matches,
exactly as a standalone `unchanged` would. The rule was written to catch
unfinished-content boilerplate; it has no compound-awareness, so legitimate
evidence vocabulary shaped `noun-noun-noun` collides with it.

D4-CL08's basis names a real control in exactly that shape
(`reports/round-22/handoff/declared-in-r2/packet.md:151`, carried verbatim from
`reports/round-20/handoff/packet.md:149`):

> … and the unchanged-foreign-path control is tools/d2-typed-labels.py
> --selftest exit 0 50/50 plus tools/gates/typed-pipeline-gate.py over
> examples/culture-d2/packet.d2.typed.yml exit 0 13/13 legs with stdout sha256
> 9a69985a… equal to the round-18 pre-generalization baseline

Every word of that phrase is substantive: it names the controls that hold the
foreign (D2) path byte-stable while the D4 leg runs, and pins their output
digest. Nothing in it is boilerplate. The finding is a false positive on the
rule's letter, not a near-miss on its intent.

## 3. Where the phrase lives (all filed; none modifiable this round)

- `reports/round-20/handoff/packet.md:149` (packet 3.0.0, sha256 `e92f5e67…`,
  the round-20 baseline pin), `…/claims-map.md:138`, `…/twin.json:1108`.
- `reports/round-22/handoff/declared-in/packet.md:151` and
  `…/declared-in-r2/packet.md:151` (packet 3.1.1, sha256 `a97a0f0a…`) with the
  same basis; the 3.1.1 renderer note itself states "the claim rows and their
  evidence statuses are unchanged" across the revision.
- The frozen validators carrying the triggering rule:
  `reports/round-15/run-validation.py`, `reports/round-16/run-validation.py`,
  `reports/round-20/run-validation.py` (identical `PLACEHOLDER_RE`).

The uncertainty claim tables of packet 3.0.0 and 3.1.1 are byte-identical
(control `ledger-shape-unchanged` in
`reports/round-23/wording/evidence/selftest-receipt.json`: same 27 row ids,
same status sequence), so the false positive is revision-independent: whichever
packet revision the check binds, D4-CL08 trips the rule.

## 4. Disposition choice: reword + new revision (preferred), not a validator change

The assignment offered two lawful exits:

1. **preferred** — reword D4-CL08's basis inside the uncertainty grammar and
   re-pin the packet as a new revision; the validators stay frozen;
2. alternative — a successor validator accepts the documented phrase class,
   with a regression control.

Route 2 was rejected for three reasons. First, it edits the boilerplate rule's
behavior in a successor: every future "the rule is X" argument then has to
carry the compound exception with it — that is the shape of a weakened rule,
even when documented. Round 22 had already refused exactly that ("not weakened
here", `routed-resolution.json:16`). Second, the regex is triplicated across
rounds 15/16/20; a successor fix would either cover one copy (divergence) or
re-verify three frozen modules (spread). Third, the phrase sits in the lane's
own artifact lineage, where a wording supersession is the established,
additive mechanism (packet 3.1.1 was itself a correcting revision of 3.0.0
"without rewriting it"). Fixing the artifact keeps every validator byte
identical and leaves the rule's strength demonstrable by direct exercise.

The reword chosen is minimal and meaning-preserving:
`the unchanged-foreign-path control` → `the foreign-path-stability control`.
The control's content — which tools run, their 50/50 and 13/13 pass counts,
the pinned stdout digest, the round-18 baseline equality — is quoted with its
values untouched; "stability" states the same property the old compound
asserted (the foreign path produces byte-identical output while the D4 leg
runs). No placeholder rule is weakened: the frozen `PLACEHOLDER_RE` is not
edited, and the controls re-exercise it on real placeholders (it still fires)
and on the old basis (the false positive still reproduces) — see
`controls.md`.

## 5. Why the check can go green without touching filed rounds

The round-20 validator selects the packet it parses by binding candidate
packets to a baseline pin (`packet_sha256` in the selected baseline's
`expected.json`), a mechanism introduced by the round-22 successor adapter
(`tie-break.py:52-77`, `install_round20_selectors`). The pin is data, not
code: `reports/round-23/wording/wording-check.py` rebinds that pin to the new
revision's `expected.json` inside an isolated clone and injects the revision
into the candidate set. The rule "the parsed packet is the pinned packet" is
applied unchanged — the pin simply names the declared-in-r3 row. Everything
else the full check measures (rounds 8-19 evidence, v1/v2/v3 exercise runs,
the v2 frozen replay, the audit verdict, the filed-bytes freeze) is untouched
and must be green in the same run.

## 6. Residual limits

- The renderer (`tools/exercise-handoff-e2e.py`) still renders 3.1.1 and its
  frozen v3 baseline still pins the declared-in-r2 packet; both stay green and
  untouched. Folding the reword into a future renderer revision (3.1.2) and
  re-freezing that baseline is renderer-owner work (round-25 tail, shared with
  the twin supersession).
- The machine twin's D4-CL08 basis (round-20/round-22 twins) is not reworded
  here: the twin is exercised only through the renderer's own baseline, and a
  hand-patched twin would risk a self-inconsistent artifact. The packet
  revision note declares the supersession; the twin follows with the renderer
  revision.
- This file is engineering evidence for the round-23 wording claims; it
  asserts nothing about canon standing (lore-shokunin's alone).
