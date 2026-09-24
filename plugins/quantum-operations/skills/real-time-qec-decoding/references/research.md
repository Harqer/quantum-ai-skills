# Real-time QEC decoding research notes

These references are examples and design evidence, not universal architecture prescriptions.

## Primary references

- Ye, Maksymov, Delfosse, **Real-time decoder for a MegaQuOp quantum computer using a single CPU** (2026), arXiv:2608.25027.
  - End-to-end streaming decoding for a trapped-ion Walking Cat Architecture.
  - Separates continuous error decoding from lower-latency logical-measurement outcome decoding.
  - Measures execution stretch caused by decoder backlog and delayed outcomes.
  - Uses on-the-fly DEM prior updates with a static Tanner graph because of a WCA-specific detector-signature property.
  - Do not generalize the static-graph result to unrelated QEC protocols.

- Ye, Wecker, Delfosse, **Beam search decoder for quantum low-density parity-check codes** (2025/2026), arXiv:2512.07057.
  - Demonstrates explicit speed/accuracy tradeoffs and reports p99.9 latency.
  - Beam width/configuration is a tunable implementation choice, not a default decoder mandate.

- Bombín et al., **Modular decoding: parallelizable real-time decoding for quantum computers** (2023), arXiv:2303.04846.
  - Decomposes global FT decoding into communicating subtasks.
  - Establishes a buffering condition so committed corrections retain fault distance.

- Liyanage et al., **Network-Integrated Decoding System for Real-Time Quantum Error Correction with Lattice Surgery** (2025), arXiv:2504.11805.
  - Shows multi-logical-qubit/lattice-surgery decoding is a systems problem involving communication topology, throughput, and backlog.

- Barber et al., **A real-time, scalable, fast and highly resource efficient decoder for a quantum computer** (Nature Electronics 2025; arXiv:2309.05558).
  - Shows the opposite timing regime: superconducting-style microsecond/MHz requirements can motivate FPGA/ASIC implementations.
  - Do not infer commodity-CPU adequacy across modalities.

## Tool semantics

### Stim detector error models

Stim DEMs encode independent error mechanisms using:
- a probability;
- detector symptoms;
- logical-observable frame changes;
- optional suggested decompositions.

Reference:
https://github.com/quantumlib/Stim/blob/main/doc/file_format_dem_detector_error_model.md

A DEM is an error-model interface, not proof that a chosen decoder handles every correlation faithfully.

### PyMatching

PyMatching consumes graphlike mechanisms (one or two detection events per edge, including suitable decompositions) and performs MWPM.

Reference:
https://pymatching.readthedocs.io/en/stable/

When converting a general DEM to matching:
- document decomposition assumptions;
- record ignored/non-graphlike mechanisms if the interface cannot represent them;
- compare correlated and uncorrelated decoding experiments separately.

### MQT QECC

MQT QECC includes QEC representations, decoding, synthesis, state preparation, and logical compilation:
https://mqt.readthedocs.io/projects/qecc/en/latest/

Use current documentation before writing tool-specific calls.


## Worked examples

Implementation-oriented examples live under [examples/](examples/README.md):

- [DEM to Tanner graph](examples/dem-to-tanner.md) — explicit `H e = d (mod 2)` construction from a minimal Stim-style detector error model.
- [Walking Cat sliding window](examples/walking-cat-sliding-window.md) — exact six-SEC `(w,c)=(3,1)` block-matrix example, duplicate-column merge rule, commit semantics, and detector offset updates from Sec. XVII.C of arXiv:2604.19481.
- [BeamSearchDecoder code path](examples/beam-search-code-path.md) — published Stim DEM → check matrix/priors → C++ beam-search decoder → logical-observable prediction flow.

Use these files when implementing or auditing a decoder. Keep architecture-specific details in the examples/references layer rather than promoting them to universal skill rules.
