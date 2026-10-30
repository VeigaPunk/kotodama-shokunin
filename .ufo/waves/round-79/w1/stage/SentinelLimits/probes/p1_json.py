# Probe P1: hostile JSON shapes against the round-76 load path semantics
# (json.loads on bytes/str, catching only ValueError) and against strict variants.
import json, time, sys, collections
print("python", sys.version.split()[0])
def attempt(label, data, **kw):
    t = time.perf_counter()
    try:
        v = json.loads(data, **kw)
        out = "OK type=%s" % type(v).__name__
    except ValueError as e:
        out = "ValueError(%s): %s" % (type(e).__name__, str(e)[:70])
    except BaseException as e:  # what the round-76 handler does NOT catch
        out = "UNCAUGHT %s: %s" % (type(e).__name__, str(e)[:70])
    print("%-28s %-62s %.3fs" % (label, out, time.perf_counter() - t))
attempt("deep-nest-200k", b"[" * 200000 + b"]" * 200000)
attempt("deep-nest-500", b"[" * 500 + b"]" * 500)
attempt("NaN", b'{"observed_at_base": NaN}')
attempt("Infinity", b'{"x": Infinity}')
attempt("dup-keys-silent", b'{"observed_at_base":"present","observed_at_base":"absent"}')
attempt("lone-surrogate", b'{"t":"\\ud800"}')
print("  lone surrogate encode ->", end=" ")
try:
    json.loads(b'{"t":"\\ud800"}')["t"].encode("utf-8"); print("encoded")
except UnicodeEncodeError as e: print("UnicodeEncodeError", str(e)[:60])
attempt("int-5000-digits", b'{"n": ' + b"9" * 5000 + b"}")
attempt("int-100-digits", b'{"n": ' + b"9" * 100 + b"}")
attempt("float-1e999999", b'{"n": 1e999999}')
attempt("bom-prefixed", b"\xef\xbb\xbf{}")
attempt("invalid-utf8-bytes", b'{"t":"\xff"}')
attempt("raw-control-char", b'{"t":"a\x01b"}')
attempt("nul-in-string", b'{"t":"a\\u0000b"}')
big = b'{"s":"' + b"x" * (64 * 1024 * 1024) + b'"}'
attempt("64MiB-string", big)
del big
attempt("100k-element-array", b"[" + b",".join([b"0"] * 100000) + b"]")
