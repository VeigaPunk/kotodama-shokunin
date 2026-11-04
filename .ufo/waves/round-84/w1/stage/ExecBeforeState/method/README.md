# Method

Normalised copies of the executables used for this seat. Substitutions applied
to the driver scripts:

- the scratch root became `${STAGE:?}`;
- the lane repository root became `${LANE:?}`;
- the tip materialisation revision is pinned to
  `7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2` (the lane tip at measurement) instead
  of live `HEAD`, so a later replay reads the same bytes;
- nothing else changed.

Files:

- `run.sh` — provenance, claim D census (knowledge files, registry rows), the four
  absence sweeps, the entry-path absence, claim O name/marker/example absence, and the
  gate-registry reading at the materialised tip.
- `run2.sh` — exact frozen `BEFORE` legs with the counters' own helpers, content-level
  sound-law context, the gate reading at base, and the regex-instrument probes.
- `run3.sh` — contract-versus-counter evidence and the pre-dispatch freeze revisions.
- `probe_counter.py` — calls `accept-d84.py`'s `knowledge_files` and `registry_rows`
  helpers; no reimplementation.
- `probe_before_legs.py` — replays `accept-d84.py:106-127` and `accept-o84.py:104-109`
  against the base tree.
- `materialize.py` — writes the `SKILL.md`, `tools/**.py` and `reports/**.py` blobs at a
  revision into a sink tree, so the gate registry is graded from committed bytes.

Replay instructions and the reproduction result are in
`../receipts/repro-check.txt`.
