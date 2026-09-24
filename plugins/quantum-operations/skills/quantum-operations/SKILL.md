---
name: quantum-operations
description: Route fault-tolerant quantum computing work across specialized skills. Use for hardware-agnostic FTQC design, optimization, error correction, logical compilation, runtime control, real-time decoding, verification, scheduling, or resource estimation.
---

# Quantum Operations Router

Use this as the entry point for fault-tolerant quantum computing work.

## Core contract

- Preserve the requested algorithm exactly unless approximation is explicitly allowed.
- Separate **logical algorithm cost**, **fault-tolerant logical cost**, **execution/runtime cost**, and **physical-resource cost**. Never mix them.
- Optimize jointly for logical width, non-Clifford cost, logical depth, spacetime volume, decoding load, classical feed-forward, and physical qubits/runtime.
- Treat hardware as a configurable model, not a vendor assumption.
- Treat decoder/controller latency as part of the execution architecture whenever logical progress depends on classical outcomes.
- Prefer exact/offline verification and simulation before any metered hardware execution.
- Keep tool-specific and architecture-specific facts in references and verify rapidly changing APIs when they matter.

## Route by task

- high-level gate/work reduction -> `semantic-gate-reduction`
- reversible arithmetic / cryptographic logic -> `reversible-arithmetic`, `boolean-fusion`, `ancilla-lifetime`
- Clifford+T / Toffoli / rotations -> `clifford-t-optimization`
- ZX calculus -> `pyzx-optimization`
- compiler passes / mapping -> `pytket-optimization`
- QEC family / logical operation strategy -> `qec-code-strategy`
- syndrome simulation / thresholds / offline decoder studies -> `qec-simulation-decoding`
- streaming decoder deadlines / backlog / tail latency -> `real-time-qec-decoding`
- Pauli/Clifford frames / logical measurement feed-forward / reset legality -> `fault-tolerant-runtime-control`
- topological compilation / lattice surgery -> `lattice-surgery`
- magic states / T factories -> `magic-state-factories`
- whole-machine schedule / decoder + factory + routing stalls -> `ftqc-runtime-scheduling`
- physical/logical resource costing -> `ftqc-resource-estimation`
- equivalence / fault-tolerance validation -> `fault-tolerant-verification`
- QASM/QIR/framework interchange -> `ir-interoperability`
- Fire Opal on present-day hardware -> `fire-opal-adjunct`

## Default FTQC flow

1. Freeze the exact logical workload and resource baseline.
2. Reduce semantic/reversible work before primitive decomposition.
3. Optimize Clifford+T/non-Clifford structure and ancilla lifetimes.
4. Select a QEC/logical-operation strategy from the physical error/timing model and logical ISA.
5. Compile logical operations (e.g. lattice surgery, transversal operations, or code switching when appropriate).
6. Size magic-state production from the non-Clifford consumption timeline.
7. Define runtime frame tracking, logical-measurement interpretation, and classical feed-forward dependencies.
8. Choose and provision the real-time decoder against syndrome rate, tail latency, and backlog requirements.
9. Build a dependency-aware FT runtime schedule including QEC cycles, factories, routing, decoding, and stalls.
10. Model logical error budgets, code distance, classical resources, physical qubits, and wall-clock runtime.
11. Validate with independent equivalence/QEC/runtime checks.
12. Keep Pareto-optimal candidates rather than one opaque score.

## Do not over-generalize architecture examples

A paper-specific optimization becomes a general rule only when its assumptions are explicitly satisfied.

Examples:
- a static Tanner graph with changing priors is not valid for every logical-operation protocol;
- a CPU decoder adequate for millisecond trapped-ion cycles does not imply CPU adequacy for microsecond syndrome cycles;
- measurement-assisted ancilla cleanup does not permit arbitrary measurement of coherent workspace;
- lattice-surgery scheduling assumptions do not automatically apply to transversal or code-switching architectures.
