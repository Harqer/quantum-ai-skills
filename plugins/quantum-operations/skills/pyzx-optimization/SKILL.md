---
name: pyzx-optimization
description: Use PyZX for ZX-calculus, Clifford+T, phase-polynomial, parity-network, T-count, and fault-equivalence-oriented reasoning. Use after semantic optimization and verify extraction regressions.
---

# PyZX Optimization

Use PyZX as a post-semantic optimizer and reasoning tool.

- `full_reduce` can expose global ZX simplifications.
- `basic_optimization` performs gate-level commutation/cancellation.
- `phase_block_optimize` / `full_optimize` are useful for compatible Clifford+T phase-polynomial structure.
- PyZX documentation warns that `phase_block_optimize` is restricted to Clifford+T-style inputs and can be wrong on unsupported smaller rotations or Toffoli-like gates.
- Circuit extraction is not architecture-aware and can increase 2Q count; preserve pre-extraction candidates.
- Use ZX equality verification where applicable, supplemented by independent verification for important rewrites.
- For FTQC, evaluate T/non-Clifford savings, Clifford overhead, logical depth, and compatibility with the chosen QEC compilation path.

See `references/tools.md`.

## Implementation gate

Before writing a PyZX pipeline, load `references/implementation.md`; use `references/tools.md` only as a link/version index. The implementation reference gives current load/reduce/extract/verify pipelines, unsupported phase-block cases, equality semantics, and acceptance tests.

Also apply `../quantum-operations/references/implementation-contract.md`.
