- Seat: A01 | executor | claim A | date 2026-10-19 | baseline 57c8409

# A01 — r7 freeze re-render and 13-component adjudication

**Verdict.** In an isolated archive of baseline `57c8409ba16d9f9e692297198d95e8f2ce5a1937`, the r7 `packet.md` and `twin.json` re-render byte-identically. The `13-register-law.yml` asymmetry is **not a documented skip**: it is omitted from `V3_READ_SET`/the frozen input map even though it is in the packet's 13-component source manifest. Treat it as a read-set roster/completeness defect, not as a demonstrated integrity bypass: the separate component-digest check still measures it and detects changed bytes.

## Re-render evidence

The tracked tree was archived to `.scratch`, and only the isolated copy was rendered; the target was `.scratch/render`, never `reports/round-34/handoff/declared-in-r7`.

```text
command: python3 -B tools/exercise-handoff-e2e.py --profile v3 --freeze .scratch/render
frozen: 2026-10-19 by tools/exercise-handoff-e2e.py --profile v3
packet_sha256: 45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
twin_sha256: 0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599
gate: exit 0, fields=16/16, glossary-entries=20, findings=0
semantics: uncertainty exit 0, links 105/105 resolved
claims: 27 statuses 16/7/4; v2-subset ad35c860acf3b452…; alias leg landed
read set: 58 files; component digests 26/26; d4 pins 8/8
```

`cmp` result against the filed r7 pair: `packet.md: byte-identical`; `twin.json: byte-identical`. The isolated output and filed r7 pair each measure to packet SHA-256 `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` and twin SHA-256 `0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599`. `expected.json` was also byte-identical. No in-tree `run-validation.py` or r7 freeze was run.

## 13-component finding

- `tools/exercise-handoff-e2e.py:157-170` defines `D4_COMPONENTS` with 12 paths; `:1939-1953` expands that tuple into `V3_READ_SET`. The filed r7 `expected.json:124-183` has 58 `inputs` and omits `examples/culture-d4/components/13-register-law.yml` (rechecked in the isolated archive).
- Conversely, `examples/culture-d4/packet.d4.yml:2788` contains `register_law`, and `:2875-2888` records all 13 component source digests, including `13-register-law.yml` (digest `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7`). The isolated renderer reports 26/26 component digests matched; 13 are from this packet's D4 manifest.
- This is not a documented exclusion rationale. The renderer's v3 inventory comment at `tools/exercise-handoff-e2e.py:51-59` says “the twelve D4 components”; `examples/culture-d4/ASSEMBLY.md:12-24` likewise describes 12 inputs; neither explains why the 13th manifest member is excluded. `reports/round-34/handoff/repin.json:32-38` separately records the scope text correction to “thirteen authored components,” confirming the 13 count was known, not that the read-set exclusion was intentional.
- The check is nevertheless effective for the current bytes: `v3_mine_d4` extracts the component manifest (`tools/exercise-handoff-e2e.py:2045-2056`), and `v3_verify_component_digests` measures each listed path (`:2208-2222`). As an isolated control, I appended a comment to the 13th component in a second archive only, then ran `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet`: exit 1, `E2E-DIGEST: D4 component examples/culture-d4/components/13-register-law.yml: the assembler recorded c0d77181ac56… but the bytes measure d075d6dc90ca…`. This confirms detection is transitive through the packet's pinned manifest even though the file is absent from the frozen `inputs` map.

**Adjudication:** The packet/twin render pair is faithful. The manifest asymmetry is a roster/completeness defect, not a documented skip, while the current component-digest control prevents a silent component-byte change. No edits or re-freeze were made. A future integrator-owned baseline revision should either add this source to the direct read set or explicitly narrow/document what the read-set contract means; the filed r7 bytes remain untouched.

## Owed

- Integrator: route the read-set roster/documentation correction to a future baseline revision; do not rewrite or re-freeze the filed r7 pair. No dependency blocked this seat.

## Citations

- `tools/exercise-handoff-e2e.py:51-59,157-170,1939-1953,2045-2056,2208-2222`
- `examples/culture-d4/packet.d4.yml:2788,2875-2888`
- `examples/culture-d4/ASSEMBLY.md:12-24`
- `reports/round-34/handoff/declared-in-r7/expected.json:124-183`
- `reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,expected.json,freeze.txt}`
- `reports/round-34/handoff/repin.json:32-38`
- Command/output evidence above: archive commit `57c8409ba16d9f9e692297198d95e8f2ce5a1937`; isolated v3 `--freeze .scratch/render`; `cmp` packet/twin; isolated 13th-component mutation control. `git rev-parse HEAD` → `57c8409ba16d9f9e692297198d95e8f2ce5a1937`; `git status --short` → only `?? reports/round-37/` before this fragment.
