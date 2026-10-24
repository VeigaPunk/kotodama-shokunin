# mut-reg — ACCEPT-C-66 registry-diff mutation probes

Fixture, not corpus data. 24 synthetic registry rows S777-S800 (hosts
`fixtureNN.example.org`), one synthetic entry and one README index row, all
generated on top of base `94209e8f80969dbac48d56c5d0e2e623635b8616`
(lane main == base). `FIXTURE.md` carries the same warning inside the tree.

Files:

- `SOURCES.pristine.md`, `ENTRY.pristine.md`, `README.pristine.md` — the exact
  fixture bytes; on this fixture all 11 ACCEPT-C-66 legs PASS (baseline
  transcript `restored-baseline.txt`).
- `mut*.SOURCES.md` — one mutation each, diffed against the pristine registry:
  - `mut1-status-queued` S790 status `mined` -> `queued`
  - `mut2-dup-url-query` S791 live URL -> S790's page + `?mirror=1`
  - `mut2b-dup-url-identical` S791 live URL -> S790's page, identical
  - `mut2c-dup-url-fragment` S791 live URL -> S790's page + `#anchor`
  - `mut3-teaches-nearcopy` S792 teaches cell -> verbatim copy of its anchor quote
  - `mut3b-teaches-padded` S792 teaches cell -> quote copy + 2 extra content words
  - `mut3c-purecopy-both` / `mut3d-padded-both` — same two registry mutations with
    an extra `*.entry.md` where the S792 bullet copies the quote verbatim
- `*.txt` — captured counter output per probe (`restored-baseline.txt` is the
  restored-bytes run).
- `run.sh` — rebuilds the tree (`git clone --shared` of the lane, ~0.4 s) and
  replays baseline + all probes. `.git`/`control/` are pruned from this directory;
  run.sh recreates them.

Result: ROWS kills mut1; LINK kills mut2b/mut2c but not mut2 (query is part of
`norm_url`); RESTATE kills mut3c only — mut3 and mut3d survive.
