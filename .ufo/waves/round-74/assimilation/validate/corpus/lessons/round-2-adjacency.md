# Round 2 adjacency — handoff-format confirmation filed to lore (2026-10-17)

## Move

- Handed off: the world-bible intake format check for the non-canon sample
  envelope at `kotodama-shokunin/examples/handoff-packet.sample.yml`
  (kotodama → lore). The sample is a sibling round-2 deliverable; this
  lesson worker neither created nor edited it.
- Recipient: lore-shokunin, the canon owner. Channel: one appended line in
  the fleet's append-only `.ufo/l0-questions.md` (permitted lane surface,
  `PROVINCE.md`). The question was filed at 14:03Z before the packet
  existed; the path resolved at 14:07:28Z. No world-bible or sibling file
  was touched; no canon claim is made.
- Ask: confirm the sample's format is consumable for world-bible intake,
  plus (a) §4 field gaps, (b) whether a §1 same-revision read record is
  needed before a real packet, (c) where lore stages its receipt.

## Contract anchors (worldbible-integration-contract.md, rev 1.0.0)

- §4 — required envelope fields and frozen digest manifest; UTF-8 Markdown
  with explicit tables is the default "unless both lanes agree another
  serialization" (the open serialization question below).
- §6 — claim kind, evidence status and canon standing stay separate;
  `not canonized` is the required standing; §11 forbids producer-issued
  canon certification.
- §8 steps 1–4 — submission, delivery and silence are never acceptance; a
  lore receipt precedes any canonized import. §9 — released bytes freeze;
  revised bytes need a new version.
- §1 — both lanes pin revision/digest before transfer; the contract digest
  below is what such a read record must name.

## Packet status (digest-scoped)

- The packet was under active revision while this round closed — five
  digests observed between 14:07:28Z and 14:13Z. Pinned observation:
  `5db077625a704acdc4cd6a9dad4c779bde01df2156608efb9571bc4841b54eaa`
  (593 lines, mtime 14:11:23Z, unchanged for ≥60 s, re-checked 14:14Z).
  Any digest here is snapshot-bound: §4's freeze rule means the bytes that
  matter are the ones frozen at submission, and a later edit invalidates
  the delivery digest.
- The writer had not stopped at round close: `bf87ea6f`… (619 lines,
  14:13Z), still no `validation` section. Treat all packet facts here as
  observations of one revision, not as a frozen delivery.
- On the pinned revision, 15 of the 16 §4 envelope keys are present at
  top level; `validation` is absent even though the file
  forward-references `/validation` gate runs (lines 26, 97, 258).
- The sample self-labels non-canon: "NON-CANON sample" header,
  `packet_status`, `canon_status: "not canonized (contract §6…)"`, and a
  "WHAT THIS IS NOT" note (no bible entry, no acceptance, §§1/3/6/8/13).
  Its SERIALIZATION note declares the YAML file a non-default
  serialization and that no §4 agreement exists for it — the live question
  this round files.
- Checker (`tools/gates/handoff-packet-check.py`, sibling deliverable,
  bytes stable since 14:07:14Z): cites §1/§4/§5/§6/§8.7/§11; read-only;
  `--selftest` green (exit 0, 9 finding IDs) on current bytes. Its fixture
  pair landed 14:04–14:05Z, so a 14:03Z run caught the pre-fixture state
  and aborted — verified race-tight, not assumed.
- Checker on the pinned packet: exit 1, `fields=9/16`, 7 × HO-EMPTY (FAIL)
  plus HO-MANIFEST-DIGEST (REVIEW — `released_bytes_digest_sha256` is
  declared `pending-freeze`, matching §4's freeze-before-review rule). The
  seven flagged keys carry non-blank top-level values; the checker
  recognizes fields only as `## field` headings, `- field: value` items or
  Markdown table rows (its "Field recognition" note), while the sample
  uses top-level YAML `field: value`. The FAILs are therefore
  serialization artifacts, not empty fields. Recorded, not repaired
  (sibling-owned; this round touches this lesson and the L0 line only).

## Open questions

1. Serialization: §4 defaults to Markdown; the packet is YAML with an
   explicit no-agreement note; the checker cannot read its field forms.
   Lore's answer should state the accepted intake serialization.
2. §4 completeness: `validation` absent from the pinned revision while
   `/validation` is cited three times — packet-side to close; relevant to
   lore's answer (a).
3. §1 read gate: no kotodama-side read record (`lane, contract_id,
   revision, file_sha256, reader, read_at, evidence_pointer`) exists in
   this repo; the packet itself records `bilateral_read: "pending"`.
4. Packet digest is not stabilizable at close; re-check the L0 record
   against the frozen submission rather than these snapshots.

## Verification

- `wc -l .ufo/l0-questions.md` 43 → 44; `head -43 | sha256sum` =
  `238c089efe4217e19580e1a518296a392e56d08d7f4b8b1f291a0bdcddc61cf0`
  — all pre-existing lines byte-identical.
- Contract digest (what a §1 record must name):
  `50c4c2f25a728e69260b76d42f0d838a398cc4683a6149f74cceeec8fb7268c1` —
  matches the packet's `contract_ref.digest_sha256`.
- Packet digests observed: `4e0b66a2`… (14:07:28Z), `dd2893c4`…,
  `1317d003`… (14:09:21Z), `2ec9bdea`…, then the pinned `5db077625a70`…
  (593 lines, mtime 14:11:23Z; stable ≥60 s).
- Checker: `--selftest` exit 0; on the pinned packet exit 1 with the
  findings above; probes (`/tmp/kotodama-adj/probe*.yml`): pure YAML →
  exit 2 HO-DATA, YAML with a `#` heading → exit 1.
- Key presence loop over the 16 §4 names: 15 present, `validation` absent
  (pinned revision, checked 14:12:50Z); checker's reported lines for the
  flagged keys: 30, 37, 130, 153, 168, 279, 307.
