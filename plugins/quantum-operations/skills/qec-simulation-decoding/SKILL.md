---
name: qec-simulation-decoding
description: Design and benchmark QEC simulations and offline decoder experiments using Stim/Sinter, PyMatching, Fusion Blossom, MQT QECC, or compatible tools. Use for syndrome circuits, detector error models, thresholds, logical error rates, and decoder accuracy/latency characterization; use real-time-qec-decoding for sustained execution deadlines and backlog.
---

# QEC Simulation and Decoding

Use high-throughput stabilizer simulation for QEC studies whenever the circuit/noise model permits it.

This skill establishes decoder correctness and statistical performance. It does **not** by itself prove that a decoder can keep pace with a full fault-tolerant workload.

## Workflow

1. Define the QEC circuit, detectors/observables, logical operations under test, and explicit noise model.
2. Generate detector error models when supported.
3. Sweep physical error rates, code distances, rounds, and decoder settings.
4. Estimate logical error rates with confidence intervals; do not compare tiny Monte Carlo samples as definitive.
5. Benchmark decoder accuracy **and latency/throughput**, including tail latency when runtime matters.
6. Separate phenomenological, code-capacity, and circuit-level noise results.
7. Record correlation assumptions; an MWPM decoder that ignores or decomposes correlations is a different experiment from a correlated decoder.
8. Test logical-operation traces in addition to memory experiments when the intended workload contains surgery, transversal gates, measurements, factories, or other non-memory behavior.

## Detector-error-model discipline

A DEM captures error mechanisms, detector symptoms, and logical-observable frame changes.

- Verify detector and observable definitions before trusting a logical-error estimate.
- Record any approximation used to produce a graphlike model.
- Do not silently discard non-graphlike/correlated mechanisms.
- Do not assume a DEM is static across logical operations unless the architecture guarantees it.

## Tools

- Stim: high-performance stabilizer/QEC simulation and detector-error-model generation; Sinter automates sampling/decoding studies.
- PyMatching: sparse MWPM decoder for graphlike detector models.
- Fusion Blossom: MWPM solver with parallel/partition-oriented decoding work.
- MQT QECC: QEC code, synthesis, state-preparation, decoding, and logical-compilation workflows.

See `references/tools.md`.

## Handoff to real-time engineering

Use `real-time-qec-decoding` when the question becomes:
- can decoding keep up with the syndrome stream;
- what buffer/window/commit scheme is safe;
- how much p99/p99.9 latency fits the hardware cycle;
- will backlog remain bounded;
- how many decoder processes/cores/accelerators are required;
- how decoder delays change the executed FT schedule.
