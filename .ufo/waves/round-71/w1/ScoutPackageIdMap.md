# Staged package ID map findings

Read-only source inspection: staged `SOURCES.append.md` contains 132 rows, S859–S990; lane `corpus/SOURCES.md` contains 784 registry rows. The staged IDs S859 and S860 collide with lane-owned S859 and S860 (S860 is the lane's settlement-state classifier). The collisions are not resolved in either repository.

A document-keyed map is at `/tmp/kotodama-package-id-map.json`. It maps all 132 staged rows, groups repeated staged citations to the same document under one lane ID, reuses a lane ID when the URL already appears in the registry, and assigns new IDs starting at S785 while skipping IDs already occupied in the lane registry. This is a scratch adoption map only; it does not append or renumber any source row. No tools were installed.

Evidence: staged source `/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md`; lane registry `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`; frozen claim confirms 784 registry rows, 132 staged IDs, and collisions S859/S860 (`reports/round-71/claims.json`, item10 collision_check).

Caveat: document identity in the JSON is matched by the first URL token in each source cell. Non-URL bibliographic variants for one underlying work may require human equivalence adjudication before adoption.