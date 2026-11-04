#!/usr/bin/env python3
"""Call the frozen accept-d84.py helpers on the base revision, no reimplementation."""
import importlib.util
import os
import subprocess
import sys

lane, base = sys.argv[1:3]
sys.path.insert(0, os.path.join(lane, "reports", "round-84"))
spec = importlib.util.spec_from_file_location(
    "accept_d84", os.path.join(lane, "reports", "round-84", "accept-d84.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

files = mod.knowledge_files(lane, base)
names = [os.path.basename(p) for p in files]
print("KNOWLEDGE_FILES_ACCEPT_D84=%d" % len(files))
print("KNOWLEDGE_NONDOTMD=%d" % (len(mod.C.tree_paths(lane, base, "corpus/knowledge")) - len(files)))

text = subprocess.run(["git", "-C", lane, "show", "%s:corpus/SOURCES.md" % base],
                      capture_output=True, check=True).stdout.decode("utf-8")
rows = mod.registry_rows(text)
print("REGISTRY_LINES_MATCHED=%d" % len(rows))
print("REGISTRY_ROWS_11CELL=%d" % sum(1 for _id, cells in rows if cells))
print("REGISTRY_ROWS_MALFORMED=%d" % sum(1 for _id, cells in rows if not cells))
print("ROW_LINE_SOURCE=%r" % mod.ROW_LINE.pattern)

import re
surf = re.compile(r"(?i)\b(witch|witches|witchcraft|sorcer[a-z]*|malefic[a-z]*)\b")
print("OWNED_BASENAMES_CLAIM_RE=%s" % ([n for n in names if surf.search(n)] or "none"))
