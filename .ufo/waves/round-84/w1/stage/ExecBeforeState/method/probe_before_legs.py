#!/usr/bin/env python3
"""Recompute the frozen BEFORE legs of accept-d84.py and accept-o84.py at BASE.

D before() (accept-d84.py:106-127): entry absent at base, knowledge .md count
== base_knowledge_files, 11-cell registry rows == base_registry_rows, no owning
basename under surface_re.
O before() (accept-o84.py:104-109): tool absent, no example file, no committed
blob in tools/ or examples/ carrying SOUNDLAWS.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

lane, base = sys.argv[1:3]
sys.path.insert(0, os.path.join(lane, "reports", "round-84"))
spec = importlib.util.spec_from_file_location(
    "accept_d84", os.path.join(lane, "reports", "round-84", "accept-d84.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
C = mod.C

cfg = json.loads(C.show(lane, "3ca2cf288fb593618e0559ea86a36e2dd3110eb8",
                        "reports/round-84/claims.json").decode("utf-8"))
d = [c for c in cfg["claims"] if c["id"] == "D"][0]["entry84"]
o = [c for c in cfg["claims"] if c["id"] == "O"][0]["tool84"]

# ---- claim D before() ----
bfiles = mod.knowledge_files(lane, base)
names = [os.path.basename(p) for p in bfiles]
surf = re.compile(d["surface_re"])
owned = [n for n in names if surf.search(n)]
entry_at_base = C.show(lane, base, d["entry_path"]) is not None
base_rows = mod.registry_rows(
    C.show(lane, base, "corpus/SOURCES.md").decode("utf-8"))
base_ids = [i for i, cells in base_rows if cells]
d_ok = (not entry_at_base and len(bfiles) == d["base_knowledge_files"]
        and len(base_ids) == d["base_registry_rows"] and not owned)
print("D_BEFORE_OK=%s" % d_ok)
print("D_entry_at_base=%s" % entry_at_base)
print("D_knowledge_files=%d frozen=%d" % (len(bfiles), d["base_knowledge_files"]))
print("D_registry_rows_11cell=%d frozen=%d" % (len(base_ids), d["base_registry_rows"]))
print("D_owned_basenames=%s" % (owned or "none"))
print("D_surface_re=%r" % d["surface_re"])

# ---- claim O before() ----
tool_at_base = C.show(lane, base, o["tool_path"]) is not None
example_at_base = C.tree_paths(lane, base, o["example_dir"])
marker = 0
marker_files = []
for p in C.tree_paths(lane, base, "tools") + C.tree_paths(lane, base, "examples"):
    b = C.show(lane, base, p)
    if b and b"SOUNDLAWS" in b:
        marker += 1
        marker_files.append(p)
o_ok = (not tool_at_base and not example_at_base and marker == 0)
print("O_BEFORE_OK=%s" % o_ok)
print("O_tool_at_base=%s" % tool_at_base)
print("O_example_files=%d" % len(example_at_base))
print("O_marker_files=%d %s" % (marker, marker_files or ""))
print("O_shape_markers=%s" % o["shape_markers"])
