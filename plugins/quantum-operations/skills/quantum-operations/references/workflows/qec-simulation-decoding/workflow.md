---
name: qec-simulation-decoding
description: Design and benchmark QEC simulations and offline decoder experiments using Stim/Sinter, PyMatching, Fusion Blossom, MQT QECC, or compatible tools.
---

# QEC Simulation and Decoding

Use high-throughput stabilizer and detector simulation whenever the circuit and noise model support it. Define the actual syndrome circuit, detector and observable annotations, logical operations under test, and explicit noise model, then generate the corresponding detector error model and sweep physical error rate, code parameters, rounds, and decoder settings. Report logical error estimates together with confidence intervals, sample counts, decoder latency/throughput, and the exact DEM/correlation assumptions used for each point.

Keep code-capacity, phenomenological, and circuit-level experiments as distinct datasets, and preserve correlation/decomposition choices as part of the experiment record. For qLDPC experiments, use the exact finite parity-check matrices and syndrome circuit from `qldpc-architecture`; benchmark BP+OSD as a generic finite-length baseline where applicable, and compare BP+LSD/localized statistics, ambiguity clustering, correlated-error methods, Tanner/expander-specific decoders, or other validated alternatives under the same circuit/noise samples. Verify detector and logical-observable definitions before interpreting a decoder result, exercise logical-operation traces in addition to memory experiments, and compare graphlike, correlated, or alternative decoders under the same circuit and sampling conditions when that distinction matters.

When the engineering question becomes sustained syndrome throughput, buffering, deadline misses, or decoder backlog, pass the measured latency distribution, detector rate, concurrency, and logical-operation trace into `real-time-qec-decoding`. That skill turns the offline statistical decoder result into a live execution constraint.

## Implementation gate

Load `references/implementation.md` before coding a QEC experiment, and use `references/tools.md` as the source/version index. The implementation reference contains an executable Stim and PyMatching workflow, a qLDPC BP+OSD/BP+LSD branch, the correlated-decoding branch, Wilson confidence interval, sweep record, and detector/observable sanity checks. Apply `../quantum-operations/references/implementation-contract.md` so every reported result remains tied to an explicit circuit, noise model, decoder configuration, and statistical method.
