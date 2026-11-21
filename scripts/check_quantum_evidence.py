#!/usr/bin/env python3
"""Structural and pure-Python acceptance gate for Quantum Operations examples."""
import ast
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "plugins/quantum-operations/EVIDENCE_MANIFEST.json"
WORKFLOWS = ROOT / "plugins/quantum-operations/skills/quantum-operations/references/workflows"
PATTERN = re.compile(r"(?:~~~|\x60\x60\x60)(python|qasm)\s*\n(.*?)(?:~~~|\x60\x60\x60)", re.S | re.I)

def main():
    entries = json.loads(MANIFEST.read_text())
    actual = {p.parent.name for p in WORKFLOWS.glob("*/workflow.md")}
    names = [row["workflow"] for row in entries]
    assert len(names) == len(set(names)), "duplicate workflows in evidence manifest"
    assert set(names) == actual, (sorted(set(names) - actual), sorted(actual - set(names)))
    executed = 0
    for row in entries:
        path = ROOT / row["reference"]
        assert path.is_file(), f"missing reference: {path}"
        assert row["primary_source"].startswith("https://"), row["workflow"]
        assert len(row["verification"]) > 10, row["workflow"]
        examples = PATTERN.findall(path.read_text())
        assert examples, f"missing code example for {row['workflow']}"
        python_blocks = [code for lang, code in examples if lang.lower() == "python"]
        for code in python_blocks:
            ast.parse(code, filename=str(path))
        if row["runtime"] == "stdlib":
            assert python_blocks, row["workflow"]
            # Self-contained source: execute, not merely parse.
            result = subprocess.run([sys.executable, "-c", python_blocks[0]],
                                    check=False, capture_output=True, text=True, timeout=15)
            assert result.returncode == 0, (row["workflow"], result.stdout, result.stderr)
            executed += 1
    print(f"{len(entries)} workflows have source + code references; "
          f"{executed} stdlib examples executed; external dependencies require separate execution.")

if __name__ == "__main__":
    main()
