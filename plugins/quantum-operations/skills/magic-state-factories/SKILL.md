---
name: magic-state-factories
description: Model and optimize magic-state distillation, cultivation, catalysis, factory throughput, buffering, acceptance, routing, and error budgets for FTQC.
---

# Magic-State Factories

Model each magic-state protocol as a concrete producer with explicit inputs, outputs, acceptance probability, output-error model, cycle cost, footprint, routing ports, retry behavior, and classical-control dependencies. Derive the required output fidelity from the workload error budget, then calculate demand from the time-resolved non-Clifford consumption schedule so peak bursts, sustained rate, buffering, and routing all enter the factory design.

Evaluate T-state, CCZ-state, catalysis, cultivation, and rotation-oriented producers under their own protocol-specific models. Keep distillation, cultivation, and catalysis as separate producer families with their own equations and acceptance semantics, then connect the selected producer to `fault-tolerant-runtime-control` for byproducts and to `ftqc-runtime-scheduling` for starvation, buffering, retries, and transport. Use published factory models or executable protocol implementations to quantify output error, throughput, footprint, and restart cost.

## Implementation gate

Load `references/implementation.md` before implementing or sizing a factory. It defines the common producer interface, 15-to-1 assumptions and equations, a concrete current protocol implementation, rejection-aware rate and buffer models, cultivation separation, and verification. Apply `../quantum-operations/references/implementation-contract.md` so every producer uses the equations and failure semantics that belong to its own protocol family.
