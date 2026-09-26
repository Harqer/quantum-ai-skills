---
name: toric-code-architecture
description: Design, simulate, decode, verify, and cost toric-code quantum memories and toric-derived topological QEC architectures. Use for 2D periodic toric codes, rotated/generalized toric codes, biased-noise deformations, 3D/4D toric variants, single-shot constructions, anyon/homology reasoning, syndrome circuits, and decoder studies.
---

# Toric-Code Architecture

Treat the toric code as both a concrete quantum error-correcting code and the canonical reference model for topological QEC. Use the ordinary 2D square-lattice toric code when periodic topology, two encoded logical qubits, local weight-four checks, homological logical operators, decoder benchmarking, or topological-memory reasoning matches the target. Route planar/open-boundary computation to the surface-code/lattice-surgery workflow when physical periodic boundaries are unavailable and the workload needs patch operations.

Fix the lattice and Pauli convention before doing algebra. In the standard square-lattice convention, place one data qubit on every edge of an L by L periodic square lattice. Define star checks A_v as products of X on the four edges incident to vertex v and plaquette checks B_p as products of Z around face p. The code has n=2L^2 data qubits, k=2 logical qubits, and distance d=L. Some software packages exchange the X/Z assignment through a global Hadamard-equivalent convention; preserve the package convention consistently instead of mixing formulas across tools.

Interpret errors topologically. A Pauli string creates syndrome defects at its boundary. Contractible closed loops are stabilizers and act trivially on encoded information. Noncontractible loops around either cycle of the torus are logical operators. A decoder succeeds only when the product of physical error and recovery has both zero syndrome and trivial homology. Zero syndrome alone is insufficient because an undetected noncontractible loop is a logical failure.

Separate evidence classes. Code-capacity studies assume perfect syndrome measurements. Phenomenological studies include data and measurement errors across time. Circuit-level studies instantiate the actual ancilla preparation, check-interaction ordering, measurement, reset, idle, leakage, crosstalk, and hardware timing. Keep decoder thresholds attached to the corresponding noise layer and decoder.

Route toric variants according to the physical and computational objective. Use rotated or Clifford-deformed/XZZX toric variants for biased noise when their effective distance and decoder exploit that bias. Use generalized/twisted-torus constructions when increased logical dimension or alternative periodic geometry is the point of the candidate. Use 3D toric and subsystem-toric variants for single-shot and higher-dimensional topological mechanisms. Use 4D toric variants only with their four-dimensional connectivity/architecture assumptions and gate constructions; their self-correction or transversal-gate properties do not transfer to ordinary 2D toric code.

Treat the 2D toric code primarily as a memory, decoder, and architecture reference unless a complete logical-operation mechanism is supplied. Record how logical Clifford operations, measurements, initialization, non-Clifford operations, code deformation, defects, teleportation, or conversion to a surface-code architecture are realized. A toric memory result is not automatically a universal-computation result.

## Implementation gate

Load `references/implementation.md`, `references/research.md`, `references/tools.md`, and the smallest relevant worked example under `references/examples/`. Apply the shared implementation contract. A production toric candidate is ready for comparison when the lattice/check convention, logical operators, syndrome circuit, noise model, decoder, homology-success test, logical-operation interface, physical layout, classical latency, and failure budget are explicit.
