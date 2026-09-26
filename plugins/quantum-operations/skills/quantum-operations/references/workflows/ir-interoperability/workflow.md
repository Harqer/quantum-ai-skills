---
name: ir-interoperability
description: Keep FTQC workflows portable across circuit frameworks and intermediate representations. Use for OpenQASM 3, QIR, Qiskit, Cirq, pytket, Stim, or resource-estimator interchange while preserving measurements, control flow, and logical metadata.
---

# IR and Framework Interoperability

Treat every conversion as a semantic translation. Inventory qubit ordering, initialization, gates and parameters, measurement destinations, reset, classical conditions and control flow, timing semantics, physical identifiers, phase requirements, detector annotations, logical observables, and custom QEC operations before conversion. Map every required semantic either into a native target construct or into an explicit sidecar/extension whose reconstruction path is defined.

For multilevel candidates, first establish whether the target IR and provider expose d-level operations. Standard qubit OpenQASM/QIR programs do not by themselves represent native qutrit transitions or pulse-level multilevel control; preserve those operations in a provider-specific extension or sidecar with an explicit lowering path. Choose OpenQASM 3 or QIR when the next tool can represent the required semantics, and select the QIR target profile that matches the program's dynamic-control requirements. Preserve detector and logical-observable metadata through a QEC-aware sidecar whenever the target IR lacks native equivalents. After conversion, compare resource counts, register mappings, measurement/reset placement, branch predicates, parameter units, phase semantics, and QEC metadata so hidden decomposition or normalization remains visible.

## Implementation gate

Load `references/implementation.md` before coding a conversion. It defines the semantic checklist, OpenQASM 3.1 dynamic and reset semantics, QIR profile boundaries, an adaptive-control example, the Stim detector-sidecar rule, round-trip tests, and explicit unsupported-feature reporting. Apply `../quantum-operations/references/implementation-contract.md` so successful interchange means semantic preservation rather than parser acceptance alone.
