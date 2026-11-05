# CriticC96 — Report (round 96, w1, r96-v1)

Scope: falsify coverage claim C. I edited nothing in the lane; outputs are this report and
`stage/CriticC96/critic.md` (full detail, every command with rc). Tools installed: none.

## Verdict: claim C survives.

Legs attacked and results (all numbers with commands/rc in critic.md):

1. **Zero-owner at base** — filename sweep at `0539276...` rc 1 (zero oath/blessing/curse
   owners); 63 base files mention "oath", max = `myth-symbol/binding-speech-complex.md` (59).
   That file's topic line names "the four channels (oath, curse, blessing, name-power)" with
   dedicated §4 oath (41 lines) / §5 curse (28) / §6 blessing (12): the surface has a
   content-level near-twin at base. "Zero owned knowledge file" holds only under the
   filename sweep the frozen claim itself cites as verification. The landed entry defers the
   machinery by name in §1 and ConnectorOverlap96 routed the seam to L0 (§6.3) — flagged,
   not falsified (round-92 precedent: expansion on the dedicated-entry surface).
2. **Overlap (8-word n-grams, case-folded, ConnectorOverlap96's 20 owners)** —
   binding-speech-complex.md 14 shared grams of 4891 (0.29%), top spans all inside the entry's
   deferral/citation prose; ordeal 2, witchcraft 1 (pointer lines); **the other 17 owners: 0**.
3. **Quotes/ids/census** — recount S975–S984: **10/10 count=1, ≤25 words, rc 0** (tool
   dry-run-validated on r95 rows: 5/5). Entry cited ids == rows.md ids == SOURCES qualifying
   ids (10); used-by byte-exact; registry 898 → 908, highest S984; append-only removed=0
   added=10; census rc 0 (2 pre-existing W04); entry shape 30143 B / 11 h2 / 19×5 / 6/6
   phrases / topic byte-equal; captures 10/10.
4. **Unsourced claims** — none found; 45 `design, not sourced` markers; one garbled sentence
   (entry line 122, "the one it "a ritual…" (S980)") — cosmetic, still attributed.
5. **Provenance spot-checks** — S982/S984 capture heads and quote contexts match their rows.

## Landing dependency (for the L1)

Index on the tree as it stands: `CORPUS-INDEX: FINDINGS files=268 rows=267 findings=5` rc 1 —
corpus/README.md bytes are not landed. `stage/ScribeEntry96/README.diff` applies clean with
`git apply --check -p0` rc 0, and the simulated landed mirror gives `CORPUS-INDEX: OK files=268
rows=268 findings=0` rc 0. **Leg C5 passes at lands iff the L1 lands that README diff** (no seat
in w1-spec.json owns corpus/README.md — ScoutSurface96's routing-gap finding, confirmed against
ExecRegistry96's prompt: 0 README mentions).

## Hazards recorded (non-fatal)

- Round-95 staged unlanded S975–S981 (lament-topic) vs round-96 landed S975–S981 (oath-topic,
  different documents): registry append-only unbroken, but the lament widening's staged ids are
  burned — for the L1 ledger.
- ScribeEntry96's DONE was re-stamped once mid-run (9039cf79… → 4a604334…); final DONE matches
  the landed entry bytes (verified). ExecRegistry96 DONE = rows.md sha (verified).
- My read-only run of the frozen counter was killed at my own 280 s cap during the O legs
  (C legs print last); `counter_rc=1` is my timeout, not a C measurement. Lands measurement
  belongs to the scoring seats.
