---
name: quantum-operations
description: Route fault-tolerant quantum computing work across specialized skills. Use for hardware-agnostic FTQC design, optimization, error correction, logical compilation, runtime control, real-time decoding, verification, scheduling, or resource estimation.
---

# Quantum Operations Router

Use this skill as the entry point for fault-tolerant quantum-computing work. Preserve the requested algorithm exactly unless the task explicitly includes approximation, and keep logical algorithm cost, fault-tolerant logical cost, execution/runtime cost, and physical-resource cost as separate layers. Optimize across logical width, non-Clifford demand, logical depth, spacetime volume, decoder load, classical feed-forward, physical qubits, and wall-clock runtime while treating hardware as an explicit capability/error/timing model.

Route high-level semantic work to `semantic-gate-reduction`; reversible cryptographic arithmetic to `reversible-arithmetic`, `boolean-fusion`, and `ancilla-lifetime`; non-Clifford synthesis to `clifford-t-optimization`; ZX reasoning to `pyzx-optimization`; compiler passes and mapping to `pytket-optimization`; code selection to `qec-code-strategy`; offline decoder studies to `qec-simulation-decoding`; streaming decoder engineering to `real-time-qec-decoding`; logical frames and feed-forward to `fault-tolerant-runtime-control`; topological compilation to `lattice-surgery`; magic-state systems to `magic-state-factories`; whole-machine timing to `ftqc-runtime-scheduling`; physical and classical costing to `ftqc-resource-estimation`; verification to `fault-tolerant-verification`; interchange to `ir-interoperability`; and present-day Fire Opal execution to `fire-opal-adjunct`.

The default FTQC flow freezes the exact workload and resource baseline, performs semantic and reversible reduction, optimizes the surviving non-Clifford structure and ancilla lifetimes, selects a QEC/logical ISA from the physical model, compiles logical operations, sizes magic-state production, defines frame and measurement-control semantics, provisions real-time decoding, builds the dependency-aware runtime schedule, estimates logical/classical/physical resources, and verifies the resulting design independently. Keep the Pareto frontier when several candidates trade width, runtime, factories, decoder resources, or error budget differently.

Architecture-specific examples stay attached to the assumptions that make them valid. A fixed Tanner graph with changing priors belongs to architectures whose detector signatures preserve that topology; CPU decoder conclusions inherit the syndrome-cycle timing and workload scale of the benchmark; measurement-assisted cleanup inherits the gadget's measurement and byproduct semantics; and lattice-surgery scheduling rules inherit the selected topological architecture.

## Implementation gate

For every request that produces or modifies production quantum code, load `references/implementation-contract.md` first, then load the routed skill's `references/implementation.md` when present and the smallest relevant worked example under `references/examples/`. Verify current external APIs when the reference marks them as version-sensitive, and complete any missing algorithmic detail from the primary specification or paper before implementation. The production path is ready when the loaded documentation supplies explicit inputs, outputs, preconditions, algorithm/circuit/API steps, examples, verification, and failure boundaries for the requested technique.
