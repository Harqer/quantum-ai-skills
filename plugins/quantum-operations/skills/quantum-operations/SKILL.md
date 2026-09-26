---
name: quantum-operations
description: Route FTQC design and implementation across logical optimization, QEC, decoding, scheduling, resource estimation, and verification.
---

# Quantum Operations Router

Use this skill as the single entry point for fault-tolerant quantum-computing work. Preserve the requested algorithm exactly unless the task explicitly includes approximation. Keep logical algorithm cost, fault-tolerant logical cost, execution/runtime cost, and physical-resource cost as separate layers. Optimize across logical width, non-Clifford demand, logical depth, spacetime volume, decoder load, classical feed-forward, physical qubits, and wall-clock runtime while representing hardware through explicit capabilities, error models, timing, topology, and QEC assumptions.

## Route the work

Select the smallest workflow set that covers the request, then load each selected workflow's `workflow.md` from `references/workflows/<workflow>/`.

| Need | Workflow |
| --- | --- |
| Algebraic simplification, virtual permutations, constant propagation, cross-boundary fusion | `semantic-gate-reduction` |
| Exact adders, compressors, modular arithmetic, carry-save forms | `reversible-arithmetic` |
| XOR/AND structure, shared nonlinear products, multiplicative complexity | `boolean-fusion` |
| Peak logical width, temporary lifetime, compute-use-uncompute, pebbling | `ancilla-lifetime` |
| T/Toffoli/CCZ cost, non-Clifford synthesis, factory demand | `clifford-t-optimization` |
| ZX-calculus and phase-polynomial rewriting | `pyzx-optimization` |
| Compiler passes, rebasing, placement, routing, mapping | `pytket-optimization` |
| QEC code selection and logical-operation strategy | `qec-code-strategy` |
| qLDPC construction, syndrome circuits, decoding, nonlocal routing, and logical gates | `qldpc-architecture` |
| Toric-code topology, homological logicals, periodic layouts, biased noise, 2D/3D/4D variants, and toric decoders | `toric-code-architecture` |
| Proven qutrit/qudit carrier packing, native multilevel gates, transient higher levels, and bosonic logical qudits | `qudit-architecture` |
| Offline detector simulation and decoder benchmarking | `qec-simulation-decoding` |
| Streaming decoder deadlines, backlog, tail latency | `real-time-qec-decoding` |
| Pauli/Clifford frames, decoded measurements, feed-forward | `fault-tolerant-runtime-control` |
| Lattice surgery, patches, routing, topological schedules | `lattice-surgery` |
| Distillation, cultivation, catalysis, factory throughput | `magic-state-factories` |
| Whole-machine event/dependency scheduling | `ftqc-runtime-scheduling` |
| Logical, classical, and physical resource estimation | `ftqc-resource-estimation` |
| Equivalence, detector/logical validation, regression tests | `fault-tolerant-verification` |
| OpenQASM/QIR/framework interchange | `ir-interoperability` |
| Q-CTRL Fire Opal hardware execution, suppression, batches, expectations, QAOA, dynamics, Monte Carlo | `fire-opal-adjunct` |

For multi-stage production work, use the default flow: freeze the exact workload and baseline; perform semantic and reversible reduction; optimize surviving non-Clifford structure and ancilla lifetimes; select the QEC/logical ISA, routing qLDPC candidates through `qldpc-architecture`, toric/topological candidates through `toric-code-architecture`, and experimentally supported qutrit/qudit candidates through `qudit-architecture`; compile logical operations; size magic-state production; define frame and measurement-control semantics; provision real-time decoding; build the dependency-aware runtime schedule; estimate resources; then verify the candidate independently. Preserve the Pareto frontier when candidates trade width, runtime, factory demand, decoder resources, or error budget differently.

Architecture-specific examples inherit the assumptions that make them valid. Carry fixed topology assumptions only into workloads that preserve that topology. Carry decoder throughput conclusions only into comparable syndrome-cycle timing and workload scale. Carry measurement-assisted cleanup only into gadgets with matching measurement and byproduct semantics. Carry qudit width or gate-count reductions only into hardware whose programming interface exposes the demonstrated d-level controls, and cost multilevel pulse depth, leakage, SPAM, and serialization explicitly. Carry lattice-surgery rules only into the selected topological architecture.

## Implementation gate

For every request that produces or modifies production quantum code, load `references/implementation-contract.md` first. Then load:

1. `references/workflows/<workflow>/workflow.md` for each routed workflow.
2. `references/workflows/<workflow>/references/implementation.md` when present.
3. The smallest relevant worked example under that workflow's `references/examples/`.
4. The workflow's tool or research reference when the implementation depends on version-sensitive APIs, empirical results, or architecture-specific assumptions.

Verify current external APIs when a reference marks them as version-sensitive. Complete missing algorithmic detail from the primary specification, paper, or current tool documentation before implementation. The production path is ready when the loaded material supplies explicit inputs, outputs, preconditions, algorithm/circuit/API steps, examples for nontrivial mechanics, verification, and failure boundaries.
