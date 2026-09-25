---
name: clifford-t-optimization
description: Optimize fault-tolerant logical circuits expressed through Clifford+T, Toffoli/CCZ, Pauli rotations, or synthesized arbitrary rotations. Use for T-count, T-depth, factory demand, relative-phase constructions, and non-Clifford scheduling.
---

# Clifford+T and Non-Clifford Optimization

Treat non-Clifford optimization as a multi-objective FTQC problem. Track T count, T depth, CCZ and Toffoli count, arbitrary-rotation count and precision, measurement depth, Clifford two-qubit cost, logical width, and the resulting factory-consumption timeline. Evaluate direct T-state, CCZ-state, catalysis, and other factory interfaces against the actual workload so the logical circuit and the factory system are optimized together.

Use relative-phase Toffoli and temporary-AND constructions when their phase semantics are proven for the surrounding computation, and pair compute and cleanup structures so phase cancellation is explicit. Combine commuting Pauli rotations before primitive T synthesis, assign rotation precision from the declared algorithmic error budget, and carry the resulting non-Clifford demand into factory throughput and spacetime estimation.

## Implementation gate

Load `references/implementation.md` before replacing gates or changing non-Clifford structure. It defines the cost record, relative-phase safety conditions, paired phase cancellation, Pauli-rotation combining, synthesis-error allocation, and factory-aware acceptance checks. Apply `../quantum-operations/references/implementation-contract.md` so each replacement is accepted through an explicit phase/equivalence proof rather than a basis-state truth table alone.
