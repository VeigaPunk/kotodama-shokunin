# Correction — round 78 census-end S884 used-by token (round-79 Ca fixture record)

This correction is APPENDED. The historical receipt
`reports/round-78/telemetry/census-end.txt` is not rewritten (append-only
discipline; QUALITY 17/29 class: a receipt must re-derive from the artifact
and revision the sentence names).

The mismatch: receipt line 33 records the S884 `used-by` token
`corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md`,
which never existed in this lane and does not equal the registry cell at the
receipt's recorded revision. The committed registry at the recorded revision
`4b255745dea45a45d88b17e3c3fea4cdb6700cf7` (and at lane base
`44f76d456c1b326a71ffdb381590af825cbf11be`) carries
`corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md`,
the value since the row's introduction at `d7a38405`.

In this FIXTURE the evidence bytes are copied at fixture base
`b96a9830cec2150a8a83fc0fcbaa3d98ba5ad5a1` (byte-identical: receipt sha256
equals the real lane's), so the fixture counter binds the fixture base as its
measured revision; the real r79 record binds `4b255745…`.

Binding (each field re-derives from committed bytes):

receipt-digest: 05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867
measured-revision: b96a9830cec2150a8a83fc0fcbaa3d98ba5ad5a1
old-token: corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md
actual-token: corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md

Re-derivation commands (counter re-runs these; frozen constants come from
`reports/round-79/claims.json` at the freeze commit, never from the graded
tree):

    git show <lands>:reports/round-78/telemetry/census-end.txt   # receipt bytes; sha256 must equal the digest above
    git show b96a9830cec2150a8a83fc0fcbaa3d98ba5ad5a1:corpus/SOURCES.md | awk -F'|' '$2 ~ / S884 / {print $12}'
    /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file <clone@measured-rev>/corpus/SOURCES.md

Diagnosis (recorded, not repaired-by-rewrite): the receipt was captured
against an uncommitted working-tree state — the registry cell and an
on-disk amend file were renamed to the `amend-2026-10-24-r13.md` convention
(used by `heritage-taxonomy-models`, S874) and reverted before commit; the
capture-time census answered exit 0, so the renamed file existed on disk at
capture. Committed bytes at every revision print the `10-23` token.
