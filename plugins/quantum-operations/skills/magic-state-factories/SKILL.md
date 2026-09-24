---
name: magic-state-factories
description: Model and optimize magic-state distillation/factory demand for FTQC. Use when T, CCZ, arbitrary rotations, factory footprint, throughput, buffering, acceptance, routing, or distillation error budgets dominate the computation.
---

# Magic-State Factories

- Derive required magic-state fidelity from the total logical failure/error budget, not an arbitrary fixed target.
- Compute demand from the **time-resolved non-Clifford consumption schedule**, not only total T/CCZ count.
- Record peak and sustained demand separately.
- Compare factory protocols on output error, acceptance probability, footprint, latency, throughput, and routing/interface cost.
- Include stochastic acceptance/rejection, retries/postselection, buffering, and factory-to-data transport.
- Evaluate T-state, CCZ-state, catalysis, cultivation, and rotation-oriented approaches where relevant.
- Allow different code distances inside factories when the error model/resource estimator supports it.
- Model measurement outcomes and Pauli/Clifford byproducts at the injection interface through `fault-tolerant-runtime-control`.
- Couple factory supply to `ftqc-runtime-scheduling` so starvation and routing contention appear as explicit stalls.
- Keep distillation assumptions explicit and reproducible.
- Use resource estimators or published factory models instead of hand-waving that magic states "dominate" or "do not dominate".

A lower total T count does not automatically imply a smaller FT machine: transformations that concentrate T gates can increase peak factory demand and required parallel factory capacity.

## Implementation gate

Before implementing or sizing a factory, load `references/implementation.md`. It defines a common producer interface, 15-to-1 assumptions/equations, a concrete current protocol implementation, rejection-aware rate/buffer models, cultivation separation, and verification.

Also apply `../quantum-operations/references/implementation-contract.md`. Never reuse one protocol's error law for a different protocol family.
