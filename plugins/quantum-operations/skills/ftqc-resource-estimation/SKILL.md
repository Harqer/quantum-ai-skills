---
name: ftqc-resource-estimation
description: Estimate logical and physical resources for fault-tolerant quantum algorithms using hardware-agnostic models. Use for physical qubits, logical qubits, code distance, runtime, factory count, spacetime volume, error budgets, or Pareto studies.
---

# FTQC Resource Estimation

Always state the model assumptions with the estimate.

## Required layers

1. **Application/logical model**: logical qubits, Clifford/non-Clifford operations, measurements, depth/dependencies, rotation precision.
2. **QEC/logical ISA model**: code family, distance, logical operation cycles, logical error model.
3. **Factory model**: magic-state type, output error, throughput, footprint.
4. **Physical architecture model**: operation times/error rates, connectivity/locality, measurement/reset, classical-feedforward assumptions.
5. **Error budget**: algorithmic approximation + synthesis + logical failures + distillation/factory errors.

## Tools

- Qualtran: compositional representations (“bloqs”) and costing for FT algorithms; use it to inspect/compose algorithmic resource models.
- Microsoft Quantum Resource Estimator (`qdk[qre]`): open-source layered application/architecture/QEC/factory estimation and Pareto exploration; it accepts Q#, Cirq, OpenQASM, QIR, logical counts, and custom applications.

Run sensitivity analysis over error rates, code distance/factory options, and physical operation times. Prefer Pareto frontiers over a single headline number.

See `references/tools.md`.
