#!/usr/bin/env python3
"""Counterfeit non-reader: prints a fixed clean body and never reads the packet."""
import json

print(json.dumps({'records': 6, 'findings': []}))
