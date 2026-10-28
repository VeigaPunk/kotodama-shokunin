# gen_legs.py — print a counter's frozen legs[] names from its own leg table (AST, read-only).
# Usage: python3 -B gen_legs.py <path/to/accept-c.py|accept-ca.py>
# Refuses (exit 2) a table with a duplicate name: round-76 accept-c.py listed INDEX twice.
import ast
import json
import sys

path = sys.argv[1]
tree = ast.parse(open(path, encoding="utf-8").read())
names = None
for node in tree.body:
    if not isinstance(node, ast.Assign):
        continue
    if not any(isinstance(t, ast.Name) and t.id in ("LEGS", "REQUIRED_LEGS") for t in node.targets):
        continue
    if not isinstance(node.value, ast.Tuple):
        continue
    out = []
    for el in node.value.elts:
        if isinstance(el, ast.Tuple) and isinstance(el.elts[0], ast.Constant):
            out.append(el.elts[0].value)
        elif isinstance(el, ast.Constant):
            out.append(el.value)
    names = out
if names is None:
    print("NO LEG TABLE FOUND")
    sys.exit(2)
dups = sorted({x for x in names if names.count(x) > 1})
if dups:
    print("REFUSED duplicate legs in table: %s" % ",".join(dups))
    print(json.dumps(names))
    sys.exit(2)
print(json.dumps(names))
print("n=%d distinct=%d" % (len(names), len(set(names))))
