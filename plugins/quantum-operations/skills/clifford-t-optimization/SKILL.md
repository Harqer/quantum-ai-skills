---
name: clifford-t-optimization
description: Optimize fault-tolerant logical circuits expressed through Clifford+T, Toffoli/CCZ, Pauli rotations, or synthesized arbitrary rotations. Use for T-count, T-depth, factory demand, relative-phase constructions, and non-Clifford scheduling.
---

# Clifford+T and Non-Clifford Optimization

Non-Clifford operations usually drive FTQC cost, but do not optimize T-count in isolation.

- Track T count, T depth, CCZ/Toffoli count, rotation count/precision, measurement depth, and logical-qubit footprint.
- Use relative-phase Toffoli/temporary-AND constructions only when phase semantics prove them safe.
- Prefer paired compute/uncompute structures that cancel phase artifacts by construction.
- Optimize Pauli rotations and commuting non-Clifford layers before lowering to individual T gates.
- For arbitrary rotations, explicitly budget synthesis precision against the algorithm error budget.
- Compare direct T-state, CCZ-state, catalysis, and other factory interfaces when relevant; do not assume a single magic-state primitive.
- Translate non-Clifford structure into **factory throughput and spacetime demand**, not just abstract gate counts.
