---
name: ftqc-runtime-scheduling
description: Schedule a complete fault-tolerant computation across logical operations, QEC cycles, magic-state production, decoding, measurement/feed-forward, routing, and classical stalls. Use when counts alone are insufficient to predict executable runtime or throughput.
---

# FTQC Runtime Scheduling

Do not infer executable runtime from logical depth or T count alone.

Build a dependency-aware schedule containing both quantum and classical resources.

## Required schedule resources

Represent at least:
- logical data/code blocks;
- syndrome-extraction cycles;
- logical measurements and their repetition/termination rules;
- logical gates or surgery/code-switching operations;
- magic-state factories, buffers, and transport/injection interfaces;
- decoder instances and decoder deadlines;
- controller/feed-forward dependencies;
- routing or communication resources where the architecture requires them.

## Distinguish counts from throughput

A total T/CCZ count does not determine factory demand. Compute:
- consumption timeline;
- peak and sustained non-Clifford rate;
- factory output rate and acceptance probability;
- buffer occupancy;
- stalls caused by factory starvation;
- data/factory routing contention.

Likewise, a decoder's isolated latency does not determine whether the schedule is feasible. Model incoming syndrome rate and queue/backlog dynamics.

## Critical-path semantics

For every event, mark dependencies that block future quantum progress.

Examples:
- decoded logical measurement required before a conditional operation;
- magic state required before injection;
- decoder frame must be caught up before a measurement begins;
- routing lane/ancilla patch required before lattice-surgery operation.

Only critical-path latency contributes directly to a stall, but non-critical work can accumulate into later contention.

## Stalls and backlog

Track separately:
- decoder backlog;
- delayed logical-measurement decisions;
- factory starvation;
- routing congestion;
- rejected/retried factory or measurement procedures;
- intentionally inserted idle/QEC cycles.

A stable system must be able to drain transient backlog. Do not accept a schedule whose average service rate is lower than its production/demand rate.

## Architecture-specific timing

Use the target architecture's real cycle/gate/measurement/reset/communication times.

Do not transfer:
- trapped-ion millisecond decoder budgets to superconducting hardware;
- superconducting microsecond assumptions to ion/neutral-atom systems;
- lattice-surgery routing assumptions to transversal/code-switching architectures.

## Runtime metrics

Report:
- baseline logical/QEC schedule depth;
- total executed cycles after stalls;
- wall-clock runtime;
- physical/logical qubit peak;
- factory utilization and starvation time;
- decoder utilization, deadline misses, and backlog;
- classical feed-forward wait time;
- routing/communication utilization where relevant;
- failure/restart probability under the stated model.

A "stretch" ratio (additional cycles divided by zero-decoder-latency baseline cycles) is useful when appropriate, but it is only one possible stall metric.

## Optimization

Optimize the joint system, not one layer independently.

Examples:
- reducing T-depth can increase peak factory demand;
- fewer logical qubits can lengthen a schedule and increase accumulated logical failure;
- a more accurate decoder may create more deadline stalls;
- extra decoder cores/factories may reduce runtime without changing the logical circuit;
- measurement-assisted uncomputation can reduce non-Clifford demand while increasing feed-forward dependence.

Return Pareto-optimal designs over qubits, runtime, error/failure budget, and classical resources.

See `references/research.md`.
