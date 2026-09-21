---
name: ir-interoperability
description: Keep FTQC workflows portable across circuit frameworks and intermediate representations. Use for OpenQASM 3, QIR, Qiskit, Cirq, pytket, Stim, or resource-estimator interchange while preserving measurements, control flow, and logical metadata.
---

# IR and Framework Interoperability

- Prefer explicit, documented interchange formats over lossy ad-hoc conversion.
- Preserve measurement, reset, classical control, qubit ordering, global/relative phase requirements, and custom logical/QEC metadata.
- Use OpenQASM 3 or QIR when they preserve the semantics required by the next tool.
- Do not round-trip through an IR that cannot represent detector annotations, logical observables, dynamic control, or custom operations required by the workflow.
- Compare resource counts before and after conversion; conversion itself can decompose or normalize operations.
- Treat tool-specific extensions as versioned boundaries and verify current support.
