# CriticClaimD — round 82 report (r82-v1)

Verdict: claim D's ground stands (census re-run clean) and the landed artifact passes its pins, but
three counter legs are weaker than they look — findings below; full dossier with commands and raw
output: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/CriticClaimD/falsify.md`.

1. Census at base c285b2afb19d4b64320e18df1f55e426bf2d0b0c: 255 knowledge files, 0 with a `guest`
   filename; "guest-right" appears only as subsections (cuisine-food-lexicon.md:95,138,170 salt-covenant;
   ritual-liminality.md:21 safe-conduct). No owner — claim D ground is free; the new entry must couple to
   those two adjacent owners, not restate them. (255/0 — `git ls-tree … | wc -l` / `| grep -c guest`.)
2. accept-d82.py leg attacks: (a) ENTRY is sha-pinned (landed entry 29020 B, sha256 == pinned
   c7fb9bc4…) — a stub cannot pass post-freeze; marker/size checks are redundant under the pin and
   freeze-time honesty is unauditable. (b) ROWS binds anchor quotes by shape only (「…」, ≤25 words,
   capture record contains "row: S904") — a fabricated quote passes; strongest observed form: S905's
   source identity changed mid-round (planned Bellows Hovamol → landed Tacitus *Germania*, Church &
   Brodribb) with zero counter effect. Evidentially documented in the registry/capture record, invisible
   to the instrument. (c) ROWCOUNT passes on count alone (827→832 measured, floor 831) and LINT passes
   vacuously on a zero-citation file (measured: `CITED-LINES: 0 finding(s)`, rc=0 on a synthetic
   0-citation entry; tool sha matches pin a9b0fbd5…) — rows-appended-but-entry-cites-none is green.
   (d) SEPARABLE's `reports/round-82/` directory prefix admits claim O's counter (accept-o82.py) and O
   telemetry; neither counter's bytes are pinned anywhere (receipt stamps its own sha, nothing compares).
3. Source tiers: landed A(Butler)/A(Germania)/B(Riley)/C(EB11) match honest scopes — translations cited
   for their own wording (teaches cells encode this); no R81-V1-class tier inflation found. Planned
   Bellows row never landed (superseded). S907 reject-candidate was REFUTED at lands (Parsoid-template
   decode artifact; prose present, mined, tier C) and the actual reject moved to S908 (Frazer,
   reject-golden-bough.txt) — consistent across frozen config, claim prose and registry; the seat
   assignment text ("S907 is a recorded reject") is stale relative to the freeze. No fetches this round;
   S907/S908 fetch claims rest on the round's recorded receipts and were not independently re-verified
   (unrun, per no-probes directive).
4. Strongest one-pass entry: the breach-ladder (degrees of guest → owed package → markers/seals → breach
   → sacral sanction → guest's half) with the guest/host~hostis lexicon interface. Reference-not-craft
   failure mode: §2 written as attestation survey instead of six decisions-with-defaults, and the worked
   example collapsing into a Baucis-and-Philemon retelling — the counter is stance-blind; only
   review_only scoping catches it (landed entry pre-commits to that scoping).
5. Smallest safe corrections (judge's call, nothing implemented by this seat): pin anchor quotes + source
   fingerprint in frozen config; require each mined row id to occur in the entry (kills the vacuous
   LINT pass); narrow SEPARABLE to `evidence/`/`telemetry/` + exact paths and pin both counters' bytes.

Files written: the report above and
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/CriticClaimD/falsify.md`.
Scratch `/fast/scratch/hyaku/kotodama-r82/CriticClaimD/` removed. No installs. Blockers: none.
