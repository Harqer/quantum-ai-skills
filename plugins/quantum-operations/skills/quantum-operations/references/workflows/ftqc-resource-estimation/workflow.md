---
name: ftqc-resource-estimation
description: Estimate logical, classical, and physical resources for fault-tolerant quantum algorithms using hardware-agnostic models. Use for physical/logical qubits, code distance, runtime, factory count, decoder/control resources, spacetime volume, error budgets, or Pareto studies.
---

# FTQC Resource Estimation

Build each estimate from explicit layers. Start with the application model—logical qubits, Clifford and non-Clifford operations, measurements, dependencies, and rotation precision—then add the QEC/logical ISA, magic-state producer, physical architecture, classical decoder/control plane, execution schedule, and error budget. Keep these layers distinct in the data model so the final report can attribute qubits, runtime, failure probability, and classical cost to their actual sources.

Report logical resources, physical data/QEC qubits, factory footprint and throughput, decoder/controller compute and memory, baseline schedule depth, stall sources, wall-clock runtime, and the composed error budget as separate fields. Sweep physical error rates and timings, code parameters, factory choices, decoder configurations, feed-forward latency, routing/layout, and slowdown targets, then preserve the Pareto frontier instead of collapsing the design space into one opaque score.

Use Qualtran for compositional logical and FT building-block costing where its abstractions match the workload, Microsoft QDK QRE for layered physical estimation and Pareto exploration, and TQEC or MQT QECC when a more concrete logical/topological compilation supplies the operation inventory. Couple estimator outputs to `ftqc-runtime-scheduling` and `real-time-qec-decoding` so decoder queues and controller deadlines are represented explicitly.

## Implementation gate

Load `references/implementation.md` before producing a physical-resource result, and use `references/tools.md` as the source/version index. The implementation reference defines current QDK QRE and Qualtran usage, their modeling boundaries, the canonical resource record, error-budget composition, and reproducibility requirements. Apply `../quantum-operations/references/implementation-contract.md` so every estimate remains reproducible from its workload, architecture, QEC, factory, decoder, runtime, and tool-version inputs.
