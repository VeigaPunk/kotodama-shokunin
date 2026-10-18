# R29-O13 — family-G hold-set pin filter

- Date: 2026-10-18.
- Status: **bounded sweep fix landed and currently detects the hold-set surface.**

## Defect and correction

The R27 claim sweep's family-G filter searched for literal D4 path/name tokens. `expected-holds.json` identified the D4 packet through its digest-valued `packet_sha256` field, so the hold-set self-pins were omitted. The independent R27 adjudication reproduced the defect: `python3 -B reports/round-27/audit/o38-sweep-inventory-adjudication.py` on 2026-10-18 reported the family-G defect true and the sweep selftest control `hold-walker-finds-the-committed-hold-set` failed. R28's `reports/round-28/sweep/sweep.py` switched the family-G decision to compare the pin against the recorded D4 packet digest, not a filename substring.

## Independent current control

At **2026-10-18 17:59:27−03:00**, with `TMPDIR=$PWD/.scratch`, I loaded the R28 sweep module read-only and called its `walk_holds()` function, printing the row whose path is `culture-d4/expected-holds.json`. It returned family **G**, path `examples/culture-d4/expected-holds.json`, reading `pinned`, with an empty drift list. This checks the specific missed surface against the current sweep logic; it is not the full sweep or a round validator.

The R28 sweep's own selftest also contains `hold-walker-finds-the-committed-hold-set` (`reports/round-28/sweep/sweep.py:686–687`). I did not run its frozen replay path: its temporary replay root must be outside the repository, while this round's scratch rule requires `TMPDIR=$PWD/.scratch` and the replay tool refuses an in-repo mirror. No result is inferred from that unrun control.

## Disposition

Retain digest-identity detection. Do not treat the earlier R27 zero-row family-G result as current evidence. Historical receipt/evidence files that pin old bytes remain historical by design; they are not live hold-set pins.