# Tool references

Use [implementation.md](implementation.md) for current load → graph → simplify → extract → verify pipelines and hard preconditions.

- PyZX docs: https://pyzx.readthedocs.io/en/latest/
- Optimization/API reference: https://pyzx.readthedocs.io/en/latest/api.html

Key implementation constraints:
- gate-set check before `phase_block_optimize`;
- treat an unproved equality result as not verified;
- extraction is not architecture-aware, so retain/checkpoint pre-extraction candidates and remeasure 2Q cost.
