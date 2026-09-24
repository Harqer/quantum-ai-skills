---
name: real-time-qec-decoding
description: Engineer streaming QEC decoders that must keep pace with a fault-tolerant computation. Use for online syndrome streams, sliding/modular windows, decoder deadlines, tail latency, backlog, convergence failures, dynamic detector error models, and classical decoder provisioning.
---

# Real-Time QEC Decoding

Treat a real-time decoder as part of the execution system, not merely an offline logical-error-rate experiment.

## Capture the execution contract first

Record:
- QEC code and logical-operation protocol;
- syndrome-extraction cycle (SEC) duration and detector production rate;
- whether logical measurements or gates change the decoding graph/model;
- which decoded outputs are on the quantum execution critical path;
- permitted decoder latency and buffering/look-ahead;
- target logical failure contribution from decoding;
- number of simultaneously live code blocks and decoder instances;
- classical CPU/GPU/FPGA/ASIC constraints, memory budget, and communication topology.

Do not claim "real time" from average decode time alone.

## Benchmark both correctness and deadlines

Measure at minimum:
- logical error rate or decoder-induced logical failure contribution;
- mean and high-percentile latency, including p99/p99.9 when enough samples exist;
- throughput relative to incoming syndrome rate;
- deadline-miss fraction;
- backlog growth/drain behavior under sustained streams;
- convergence/failure/restart rate separately from ordinary latency;
- memory footprint and bandwidth/communication pressure under concurrent decoding.

A decoder can have low mean latency yet be unusable if its tail latency causes unbounded backlog or delays logical feed-forward.

## Streaming and windowed decoding

For sliding-window, modular, or partitioned decoding:
- distinguish **window size**, **commit region**, and **look-ahead/buffer region**;
- never commit a correction using insufficient future context unless the selected decoder/protocol justifies it;
- preserve code distance/fault-distance requirements when partitioning;
- model boundary handoff state explicitly;
- benchmark the complete streaming pipeline, not independent windows sampled in isolation.

Modular decoding research identifies buffering as a correctness condition, not only a performance knob.

## Decoder specialization is allowed

Different runtime outputs may justify different decoder configurations. A low-latency logical-measurement decoder can use a different accuracy/latency point from the decoder maintaining the long-lived Pauli frame, provided the resulting total logical error is explicitly bounded.

Do not copy a dual-decoder architecture unless the target logical protocol actually has separable accuracy/latency requirements.

## Detector error models

A detector error model (DEM) describes error mechanisms through probabilities, detector symptoms, and logical frame changes.

- Reuse static graph structure when the architecture mathematically permits it.
- If logical operations alter detector connectivity, boundaries, checks, or correlations, regenerate or update the appropriate model rather than assuming priors alone are sufficient.
- Treat "fixed Tanner graph + dynamic priors" as an architecture-specific optimization, not a universal rule.
- Track correlated mechanisms deliberately; graphlike decomposition changes the decoding experiment.

## Provisioning

Provision decoding compute from the worst relevant combination of:
- live code blocks;
- syndrome rate per block;
- decoder tail latency;
- communication overhead;
- logical-operation bursts;
- memory bandwidth/cache pressure;
- target backlog margin.

Scale classical resources before accepting a schedule whose decoder backlog is unstable.

## Verification

Before declaring a decoder production-capable:
1. validate detector/observable definitions;
2. reproduce logical-error results with statistically meaningful sampling;
3. stress high-percentile runtime under concurrent load;
4. replay full logical-operation traces, not memory-only traces;
5. inject deadline overruns and verify schedule/backlog behavior;
6. distinguish recoverable latency from decoder convergence failure;
7. cross-check at least one independent decoder or small exact reference where practical.

See `references/research.md` for primary-source patterns and tool notes. For concrete Tanner/DEM and sliding-window constructions, load `references/examples/README.md` and only the example required for the current implementation.
