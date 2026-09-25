---
name: pyzx-optimization
description: Use PyZX for ZX-calculus, Clifford+T, phase-polynomial, parity-network, T-count, and fault-equivalence-oriented reasoning after semantic optimization.
---

# PyZX Optimization

Use PyZX after the semantic layer has already exposed algebraic structure. Choose graph-level `full_reduce`, circuit-level `basic_optimization` or `full_optimize`, phase-polynomial optimization, or phase teleportation according to the circuit gate set and the intended extraction path. Preserve the pre-optimization and pre-extraction candidates so the final selection can compare T/non-Clifford savings, Clifford overhead, logical depth, two-qubit count, and compatibility with downstream QEC compilation.

Run a gate-set preflight before phase-block optimization and use the documented Clifford+T domain for that path. After graph extraction, measure the resulting circuit because extraction is architecture-independent and can change two-qubit cost. Establish equality with PyZX where its proof procedure succeeds, supplement important rewrites with an independent checker or small exact tensor/state comparison, and carry explicit wire permutations and phase semantics into the verification record.

## Implementation gate

Load `references/implementation.md` before writing a PyZX pipeline, and use `references/tools.md` as the source/version index. The implementation reference provides current load, reduce, extract, verify, and phase-teleportation flows together with the gate-set preflight and acceptance checks. Apply `../quantum-operations/references/implementation-contract.md` so every optimized circuit is accepted through an explicit semantic proof and resource comparison.
