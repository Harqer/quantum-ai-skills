---
name: quantum-operations
description: Route FTQC design and implementation across logical optimization, QEC, decoding, scheduling, resource estimation, and verification.
---

# Quantum Operations Router

Use this skill as the single entry point for fault-tolerant quantum-computing work. Preserve the requested algorithm exactly unless the task explicitly includes approximation or replacement by a different problem-solving method. Keep logical algorithm cost, fault-tolerant logical cost, execution/runtime cost, and physical-resource cost as separate layers. Optimize across logical width, non-Clifford demand, logical depth, spacetime volume, decoder load, classical feed-forward, physical qubits, and wall-clock runtime while representing hardware through explicit capabilities, error models, timing, topology, and QEC assumptions.

## Route the work

Select the smallest workflow set that covers the request, then load each selected workflow's `workflow.md` from `references/workflows/<workflow>/`.

| Need | Workflow |
| --- | --- |
| Algebraic simplification, virtual permutations, constant propagation, cross-boundary fusion | `semantic-gate-reduction` |
| Replace an algorithmic realization with a lower-gate method while preserving the stated problem objective | `algorithmic-gate-compression` |
| Exact adders, compressors, modular arithmetic, carry-save forms | `reversible-arithmetic` |
| XOR/AND structure, shared nonlinear products, multiplicative complexity | `boolean-fusion` |
| Peak logical width, temporary lifetime, compute-use-uncompute, pebbling | `ancilla-lifetime` |
| Mid-circuit measurement/reset compilation that reuses physical qubits | `qubit-reuse-compilation` |
| T/Toffoli/CCZ cost, non-Clifford synthesis, factory demand | `clifford-t-optimization` |
| Signature-tensor / AlphaTensor-style exact T-count optimization | `tensor-t-optimization` |
| Native parameterized entanglers, KAK/canonical 2Q synthesis, hardware-aware entangler lowering | `native-entangler-synthesis` |
| ZX-calculus and phase-polynomial rewriting | `pyzx-optimization` |
| Compiler passes, rebasing, placement, routing, mapping | `pytket-optimization` |
| QEC code selection and logical-operation strategy | `qec-code-strategy` |
| Transversal gates, logical teleportation, fresh-block reset/reuse, permutation logical gates, correlated decoding | `transversal-teleportation` |
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
| Q-CTRL Fire Opal QPU layout/routing optimization, hardware-aware compilation, suppression, execution, and managed algorithms | `fire-opal-adjunct` |

For multi-stage production work, freeze the exact workload and baseline first. Perform semantic reduction before primitive decomposition; apply algorithmic replacement only when the requested problem contract permits it. Then optimize reversible arithmetic, Boolean structure, qubit/ancilla lifetime, exact non-Clifford structure, tensor T-count where applicable, and native entanglers. Use qubit-reuse compilation only when measurement/reset is semantically legal and the target exposes MCMR. Select the QEC/logical ISA, compile logical operations, size non-Clifford resources, define runtime control, schedule the whole machine, estimate resources, and verify independently. Preserve the Pareto frontier when candidates trade width, gates, depth, runtime, fidelity, factories, decoder resources, or error budget differently.

Architecture-specific examples inherit the assumptions that make them valid. Carry native-angle reductions only into hardware that exposes the required parameterized entangler and angle range. Carry runtime-squashing observations only as measured backend behavior, not as guaranteed compile-time savings. Carry qubit-reuse savings only across measurement/reset boundaries whose semantics are proven. Carry signature-tensor T-count reductions only into supported Clifford+T regions and preserve exact phase semantics. Carry Floquet-style gate-count claims only to classical target Hamiltonians and only when replacing the original algorithm is allowed; it is not an exact circuit-equivalence pass. Carry qudit width or gate-count reductions only into hardware whose programming interface exposes the demonstrated d-level controls.

## Implementation gate

For every request that produces or modifies production quantum code, load `references/implementation-contract.md` first. Then load:
1. `references/workflows/<workflow>/workflow.md`.
2. `references/workflows/<workflow>/references/implementation.md` when present.
3. The smallest relevant worked example under `references/examples/`.
4. `references/research.md` or `references/tools.md` when the method depends on current APIs, empirical results, or architecture-specific assumptions.

Verify current external APIs when marked version-sensitive. Complete missing algorithmic detail from the primary specification, paper, or current tool documentation before implementation. Production code is ready only when the loaded material gives explicit inputs, outputs, preconditions, exact transformation/API steps, a nontrivial worked example, verification, and failure boundaries.
