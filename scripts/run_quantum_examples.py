#!/usr/bin/env python3
"""Run self-contained evidence-backed examples under their actual SDK."""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
runtime = sys.argv[1]
items = json.loads((ROOT / "plugins/quantum-operations/EVIDENCE_MANIFEST.json").read_text())
pattern = re.compile(r"(?:~~~|\x60\x60\x60)python\s*\n(.*?)(?:~~~|\x60\x60\x60)", re.S | re.I)
count = 0
for row in items:
    if row["runtime"] != runtime or not row["reference"].endswith("evidence-backed.md"):
        continue
    path = ROOT / row["reference"]
    code = pattern.findall(path.read_text())
    assert len(code) == 1, ("one self-contained Python program expected", path)
    result = subprocess.run([sys.executable, "-c", code[0]], capture_output=True, text=True, timeout=120)
    print(row["workflow"], "exit:", result.returncode, "stdout:", result.stdout.strip())
    if result.returncode:
        print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)
    count += 1
assert count, f"no selected examples for {runtime}"
print("Passed", count, "full runnable", runtime, "reference examples")
