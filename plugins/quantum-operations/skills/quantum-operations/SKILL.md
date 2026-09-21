---
name: quantum-operations
description: Route fault-tolerant quantum computing work across specialized skills. Use for hardware-agnostic FTQC design, optimization, error correction, logical compilation, verification, or resource estimation.
---

# Quantum Operations Router

Use this as the entry point for fault-tolerant quantum computing work.

## Core contract

- Preserve the requested algorithm exactly unless approximation is explicitly allowed.
- Separate **logical algorithm cost**, **fault-tolerant logical cost**, and **physical-resource cost**. Never mix them.
- Optimize jointly for logical width, non-Clifford cost, logical depth, spacetime volume, decoding load, and physical qubits/runtime.
- Treat hardware as a configurable model, not a vendor assumption.
- Prefer exact/offline verification and simulation before any metered hardware execution.
- Keep tool-specific facts in references and verify rapidly changing APIs when they matter.

## Route by task

- high-level gate/work reduction -> `semantic-gate-reduction`
- reversible arithmetic / cryptographic logic -> `reversible-arithmetic`, `boolean-fusion`, `ancilla-lifetime`
- Clifford+T / Toffoli / rotations -> `clifford-t-optimization`
- ZX calculus -> `pyzx-optimization`
- compiler passes / mapping -> `pytket-optimization`
- QEC family / logical operation strategy -> `qec-code-strategy`
- syndrome simulation / thresholds / decoder studies -> `qec-simulation-decoding`
- topological compilation / lattice surgery -> `lattice-surgery`
- magic states / T factories -> `magic-state-factories`
- physical/logical resource costing -> `ftqc-resource-estimation`
- equivalence / fault-tolerance validation -> `fault-tolerant-verification`
- QASM/QIR/framework interchange -> `ir-interoperability`
- Fire Opal on present-day hardware -> `fire-opal-adjunct`

## Default FTQC flow

1. Freeze the exact logical workload and resource baseline.
2. Reduce semantic/reversible work before primitive decomposition.
3. Optimize Clifford+T/non-Clifford structure and ancilla lifetimes.
4. Select a QEC/logical-operation strategy based on assumptions, not vendor branding.
5. Compile/schedule logical operations (e.g. lattice surgery when appropriate).
6. Size magic-state production and non-Clifford throughput.
7. Model logical error budgets, code distance, physical qubits, and runtime.
8. Validate with independent equivalence/QEC simulation tools.
9. Keep Pareto-optimal candidates rather than one opaque score.
