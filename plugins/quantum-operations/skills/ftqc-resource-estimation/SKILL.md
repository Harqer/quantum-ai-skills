---
name: ftqc-resource-estimation
description: Estimate logical, classical, and physical resources for fault-tolerant quantum algorithms using hardware-agnostic models. Use for physical/logical qubits, code distance, runtime, factory count, decoder/control resources, spacetime volume, error budgets, or Pareto studies.
---

# FTQC Resource Estimation

Always state the model assumptions with the estimate.

Do not report wall-clock runtime from logical gate counts alone when decoding, measurement feed-forward, routing, or factory availability can stall execution.

## Required layers

1. **Application/logical model**: logical qubits, Clifford/non-Clifford operations, measurements, depth/dependencies, rotation precision.
2. **QEC/logical ISA model**: code family, distance, syndrome cycle, logical operation protocols/cycles, logical error model.
3. **Factory model**: magic-state type, output error, acceptance probability, throughput, buffering, footprint, transport.
4. **Physical architecture model**: operation/error rates, connectivity/locality, measurement/reset, communication, cycle times.
5. **Classical runtime model**: decoder algorithm, concurrent code blocks, latency distribution, throughput, memory/communication cost, frame tracking, and feed-forward deadlines.
6. **Execution schedule model**: dependencies, routing/factory contention, decoder backlog, stalls/retries, baseline and executed cycle count.
7. **Error budget**: algorithmic approximation + synthesis + logical failures + distillation/factory errors + any decoder/protocol failure contributions.

## Report separate resource classes

At minimum separate:
- logical qubits and logical operation counts;
- physical data/QEC qubits;
- factory qubits and factory throughput;
- decoder/controller compute and memory;
- baseline schedule depth;
- stall/extension sources;
- final wall-clock runtime;
- total failure/error budget.

Do not hide classical compute inside an unexplained "runtime overhead" factor when it is material.

## Sensitivity and Pareto analysis

Sweep the assumptions that can change the architecture:
- physical error rates and operation times;
- code distances/code families;
- factory protocols/counts;
- decoder configurations and allocated compute;
- feed-forward latency;
- routing/layout choices;
- allowed slowdown/runtime targets.

Prefer Pareto frontiers over a single headline number.

## Tools

- Qualtran: compositional algorithm/resource representations; use for logical and FT building-block costing where its abstractions match the workload.
- Microsoft Quantum Resource Estimator (`qdk[qre]`): layered application/architecture/QEC/factory estimation and Pareto exploration.
- TQEC / MQT QECC: useful for logical/topological compilation details that can supply a more realistic schedule or operation inventory.

A resource estimator may not model real-time decoder queues or controller deadlines at the required fidelity. Couple it to `ftqc-runtime-scheduling` and `real-time-qec-decoding` instead of inventing a constant correction factor.

See `references/tools.md`.
