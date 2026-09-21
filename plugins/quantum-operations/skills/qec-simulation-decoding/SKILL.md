---
name: qec-simulation-decoding
description: Design and benchmark QEC simulations and decoders using Stim/Sinter, PyMatching, Fusion Blossom, MQT QECC, or compatible tools. Use for syndrome circuits, detector error models, thresholds, logical error rates, and decoder latency.
---

# QEC Simulation and Decoding

Use high-throughput stabilizer simulation for QEC studies whenever the circuit/noise model permits it.

## Workflow

1. Define the QEC circuit, detectors/observables, and explicit noise model.
2. Generate detector error models when supported.
3. Sweep physical error rates, code distances, rounds, and decoder settings.
4. Estimate logical error rates with confidence intervals; do not compare tiny Monte Carlo samples as definitive.
5. Benchmark decoder accuracy **and latency/throughput**.
6. Separate phenomenological, code-capacity, and circuit-level noise results.
7. Record correlation assumptions; an MWPM decoder that ignores correlations is a different experiment from a correlated decoder.

## Tools

- Stim: high-performance stabilizer/QEC simulation; Sinter automates sampling/decoding studies.
- PyMatching: sparse MWPM decoder with Stim detector-error-model support and correlated matching options.
- Fusion Blossom: exact MWPM solver with parallel/partitioned decoding support.
- MQT QECC: additional QEC code, synthesis, decoding, and logical-compilation workflows.

See `references/tools.md`.
