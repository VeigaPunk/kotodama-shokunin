# apparatus-draft — how L1 assembles the production freeze/lands

Everything under this directory was dumped byte-identical from the counter's
isolated selftest fixture (env `DUMP_FIXTURES`). It is a DRAFT of the claim-O
freeze apparatus; assembly notes:

1. `tools/ledger-token-guard.py` here is the **reference fixture guard**
   embedded in `accept-o.py` (marked as such in its docstring). Substitute
   ExecGuard's production guard before freezing. Its docstring/comment may
   differ; only behaviour is graded. Fixture ledgers carry exactly the
   contract's example fields (top-level `round/claim/base/pairs`; per-pair
   `id/disposition/stated_at/stated_text/stated_parse/observe_cmd/parse/
   expected_after/observed_at_base/rederive`) — the production guard's
   strict key set accepts them as-is; do not add keys.
2. Regenerate `reports/round-79/telemetry/selftest-guard.txt` after the
   substitution: run the production guard with `--selftest` under explicit
   scratch and commit the output under the same `# guard sha256:` header
   (sha of the production guard bytes at the lands tree).
3. Regenerate `reports/round-79/telemetry/junk-o.txt` and
   `controls-o.txt` by running `accept-o.py` against the junk/control trees
   (mutations named in the receipt lines, applied to the freeze bytes) with
   the production guard in place — the receipt lines carry each fixture's
   commit, the command, the counter's own `LEG FAIL <leg>` line and its exit
   code (QUALITY 25(b) shape).
4. Regenerate `reports/round-79/claims.json` with the production base
   `44f76d456c1b326a71ffdb381590af825cbf11be` (the dumped copy carries the
   synthetic fixture-base hash). Keep `legs`, `fixture_manifest`,
   `junk_expect`, `controls_expect`, `receipts` exactly as dumped — the
   counter refuses (LEGCOUNT / config error, exit 2) on any drift.
5. `reports/round-79/accept-o.py` is the byte-identical counter copy the
   frozen manifest requires (sha pinned by the STAMP leg).
6. `reports/round-79/telemetry/selftest-o.txt` here is the FIXTURE copy; the
   production O-lands commits the real W1 receipt from
   `stage/ExecOCounter/selftest-o.txt` (same shape: do-nothing line, clean
   line, `SELFTEST:` summary).
7. Freeze shape: claims.json + counter + guard + fixtures + the three
   receipts above. O-lands shape: freeze + `selftest-guard.txt` +
   `selftest-o.txt` + a `LOG.md` row containing `round-79` and `claim O`.
   Grading: `python3 -B reports/round-79/accept-o.py --root <lane> --lands
   <O-lands> --freeze <freeze> --work $HYAKU_SCRATCH`.
