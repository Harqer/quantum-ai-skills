---
name: magic-state-factories
description: Model and optimize magic-state distillation/factory demand for FTQC. Use when T, CCZ, arbitrary rotations, factory footprint, throughput, buffering, distillation levels, or error budgets dominate the computation.
---

# Magic-State Factories

- Derive required magic-state fidelity from the total logical failure/error budget, not an arbitrary fixed target.
- Compute demand from non-Clifford schedule and peak consumption rate, not only total T count.
- Compare factory protocols on output error, acceptance probability, footprint, latency, throughput, and routing/interface cost.
- Include buffering and factory-to-data transport/scheduling overhead.
- Evaluate T-state, CCZ-state, catalysis, and rotation-oriented approaches where relevant.
- Allow different code distances inside factories when the error model/resource estimator supports it.
- Keep distillation assumptions explicit and reproducible.
- Use resource estimators or published factory models instead of hand-waving that magic states “dominate” or “do not dominate”.
