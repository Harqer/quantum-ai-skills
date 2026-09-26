---
name: qldpc-architecture
description: Design executable quantum-LDPC architectures, including bivariate/generalized bicycle, hypergraph-product, lifted-product, Tanner, balanced-product, and related high-rate codes. Use for qLDPC construction, syndrome extraction, decoding, hardware routing, logical gates, and low-overhead comparisons.
---

# Quantum LDPC Architecture

Treat qLDPC as an executable architecture family rather than a synonym for low qubit overhead. Start from the workload, target logical failure budget, physical noise and timing model, connectivity or transport capabilities, and classical decoder resources. Classify the target as protected memory, Clifford computation, or universal fault-tolerant computation because each level requires a different logical-operation record.

Represent every candidate with explicit CSS or stabilizer matrices, code parameters and provenance, check and variable degrees, a concrete syndrome-extraction circuit, circuit-level noise behavior, decoder configuration and latency distribution, physical layout/routing cost, state-preparation and readout protocols, and a complete logical-operation interface. Keep asymptotic code-family results separate from finite block-length candidates that have concrete matrices, circuits, decoders, and hardware mappings.

For finite-length engineering, evaluate bivariate/generalized bicycle and hypergraph-product constructions when their parameters and syndrome circuits match the target. Use lifted-product, Tanner, balanced-product, fiber-bundle, expander, or other asymptotically strong constructions when a finite instance and executable protocol are available for the requested machine. Preserve each construction's assumptions rather than transferring distance, threshold, decoder, or gate claims across families.

Derive the Tanner graph from the actual parity-check matrices and map every Tanner edge to a native interaction, movement, teleportation, photonic link, or routed path. Include ancilla count, communication distance, routing layers, transport time, crosstalk/leakage exposure, and cycle stretch in the resource model. A qLDPC candidate earns a low-overhead result only after those costs and the decoder/control plane are included under the same logical-failure target used for the comparison baseline.

Benchmark decoding under the same noise layer as the claim. Use code-capacity experiments for algebraic decoder studies, phenomenological experiments for repeated noisy syndromes, and circuit-level experiments for execution claims. BP+OSD is a strong generic finite-length baseline; BP+LSD, ambiguity clustering, correlated-error graph augmentation/min-sum, union-find-like methods, small-set-flip, Tanner-specific decoders, and hardware accelerators are candidate alternatives when their assumptions match the code. Pass measured throughput and p99/p99.9 latency into `real-time-qec-decoding`.

Treat memory performance and computation as separate milestones. For Clifford and universal computation, record the exact mechanism for each required logical operation: transversal gates, automorphisms, dynamic syndrome circuits, code switching, generalized surgery/Pauli-product measurement, teleportation, magic-state injection, or a heterogeneous qLDPC/surface-code interface. Route non-Clifford production into `magic-state-factories` when the architecture requires it.

## Implementation gate

Load `references/implementation.md`, `references/research.md`, and the smallest relevant file under `references/examples/`. Apply the shared implementation contract. A production qLDPC candidate is ready for resource comparison when its algebraic construction, syndrome circuit, decoder, routing model, logical ISA, state preparation/readout, circuit-level error evidence, and physical/classical resource record are all concrete.
