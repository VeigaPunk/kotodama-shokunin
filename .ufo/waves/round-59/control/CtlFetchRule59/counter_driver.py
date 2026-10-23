#!/usr/bin/env python3
"""Load loopback transport, then execute the otherwise unchanged frozen counter."""
import fixture_transport
import runpy
import sys
sys.argv = ['reports/round-59/accept-c.py']
runpy.run_path(sys.argv[0], run_name='__main__')
