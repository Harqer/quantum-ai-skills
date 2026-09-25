---
name: ftqc-runtime-scheduling
description: Schedule a complete fault-tolerant computation across logical operations, QEC cycles, magic-state production, decoding, measurement/feed-forward, routing, and classical stalls. Use when counts alone are insufficient to predict executable runtime or throughput.
---

# FTQC Runtime Scheduling

Build executable runtime from a dependency-aware schedule that contains quantum and classical resources together. Represent logical data blocks, syndrome-extraction cycles, logical measurements and their termination rules, logical gates or surgery/code-switching operations, magic-state factories and buffers, decoder instances and deadlines, feed-forward dependencies, and routing or communication resources. Derive runtime from this event graph so logical depth and T count become inputs rather than substitutes for an execution model.

Convert non-Clifford demand into a time-resolved consumption trace and compare it with factory output rate, acceptance probability, buffer occupancy, and routing capacity. Replay syndrome arrivals through decoder workers using the measured latency distribution, then propagate late logical outcomes into dependent quantum events. A stable design should have service capacity above sustained demand and enough headroom for the burst and tail-latency behavior required by its deadline target.

Use the timing model of the selected physical architecture for gate, measurement, reset, communication, and syndrome-cycle durations. Report baseline cycles, executed cycles after stalls, wall-clock runtime, logical and physical peak qubits, factory utilization and starvation, decoder utilization and deadline misses, classical feed-forward wait, routing utilization, and restart/failure behavior. Optimize these jointly and keep the Pareto-optimal schedules over qubits, runtime, error budget, and classical resources.

## Implementation gate

Load `references/implementation.md` together with `references/research.md` before implementing a scheduler. The implementation reference defines the event/resource schema, list scheduler, decoder queue, factory buffer, stall equations, fixed-point scheduling loop, and invariants. Apply `../quantum-operations/references/implementation-contract.md` so every scheduled delay arises from an explicit dependency, resource, queue, or protocol event.
