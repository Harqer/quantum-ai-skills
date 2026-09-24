# FTQC runtime-scheduling research notes

## Decoder-aware schedules

- Ye, Maksymov, Delfosse, **Real-time decoder for a MegaQuOp quantum computer using a single CPU**, arXiv:2608.25027.
  - Defines computation "stretch" from decoder-induced additional syndrome-extraction cycles.
  - Models decoder backlog and delayed logical-measurement outcomes as distinct ways classical latency extends the quantum schedule.
  - Demonstrates why tail-latency effects must be evaluated on complete workloads.

- Liyanage et al., **Network-Integrated Decoding System for Real-Time Quantum Error Correction with Lattice Surgery**, arXiv:2504.11805.
  - Highlights communication topology and throughput as scaling constraints for multi-logical-qubit decoding.

## Magic-state scheduling

- Hofmeyr et al., **Scheduling Lattice Surgery with Magic State Cultivation**, arXiv:2512.06484.
  - Demonstrates that factory placement, routing resources, and dynamic reuse change schedule efficiency.
  - Treat its "Pure Magic" architecture as one design point, not a general requirement.

- Silva et al., **Optimizing Multi-level Magic State Factories for Fault-Tolerant Quantum Architectures**, arXiv:2411.04270.
  - Treats factory production/consumption as a supply-chain and space-time optimization problem.
  - Supports explicit slowdown/space tradeoffs instead of deriving runtime from T count alone.

## Resource-estimation integration

Microsoft Quantum Resource Estimator uses layered application, hardware, error-correction/factory, and error-budget models and explores a Pareto frontier:
https://learn.microsoft.com/en-us/azure/quantum/overview-resources-estimator

Use such estimators for physical-resource envelopes, but add explicit runtime-control/decoder scheduling when the estimator does not model those queues/deadlines at the required fidelity.

## Topological compilation

TQEC supports representation/construction/compilation of surface-code and lattice-surgery computations:
https://tqec.github.io/tqec/

MQT QECC includes logical-compilation workflows such as code switching and color-code/lattice-surgery routing:
https://mqt.readthedocs.io/projects/qecc/en/latest/tools/compilation.html

Verify current APIs and distinguish schedule models from executable physical-control software.
