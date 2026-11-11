# Bosonic cavity architecture: research basis

This reference records engineering conclusions used by the workflow. Recheck primary literature before attaching current hardware numbers.

## Experimentally grounded mechanisms

- Superconducting circuit-QED experiments have encoded cat-like multiphoton states in microwave cavities and demonstrated repeated parity-based or autonomous correction of photon-loss errors.
- Superconducting oscillator experiments have demonstrated GKP/grid-state stabilization and beyond-break-even protected logical information. Recent qudit work demonstrates GKP qutrit and ququart memories; this supports bosonic logical qudits, not arbitrary high-d packing.
- Number-selective phase control (SNAP) together with oscillator displacements provides powerful control over a truncated oscillator subspace. The implementation requires a nonlinear ancilla and calibrated dispersive control.
- Trapped-ion motional modes are experimentally useful bosonic systems; randomized displacement benchmarking has exposed heating/dephasing behavior that must be represented separately from qubit Pauli noise.

## Primary sources to verify

- Lescanne et al., "Exponential suppression of bit-flips in a qubit encoded in an oscillator", Nature Physics 2020 / arXiv:1907.11729.
- Ofek et al., "Extending the lifetime of a quantum bit with error correction in superconducting circuits", Nature 2016.
- Campagne-Ibarcq et al., repetitive GKP/grid-state error correction in a superconducting oscillator, Nature 2020.
- Heeres et al., universal control of an oscillator using dispersive number-selective operations (SNAP-family control).
- Valahu et al., "Benchmarking Bosonic Modes for Quantum Information with Randomized Displacements", PRX Quantum 5, 040337 (2024).
- Current GKP-qudit experiments cited by the qudit-architecture workflow for demonstrated d=3 and d=4 beyond-break-even memories.

## Interpretation boundary

The research supplied for this workflow emphasizes photon/phonon loss, dephasing/heating, finite useful occupation, analog calibration, leakage, ancilla back-action, QEC overhead, and multi-mode scaling. Those constraints are mandatory in production estimates.

Treat proposed D=16/D=256 cavity packing or word-level SHA packing as research hypotheses until a concrete code, gate set, error-correction path, and hardware interface support the dimension. In particular, no information-capacity calculation alone licenses a fault-tolerant carrier-count reduction.

## SHA-256 consequence

For the exact 440-bit coherent message plus 256-bit arbitrary XOR target, 696 coherent bits remain a semantic requirement. Bosonic hardware can change the physical representation, but a production estimate must derive effective logical capacity from an encoding and its QEC/control resources. A hybrid high-Q bosonic memory plus nonlinear ancilla arithmetic engine is therefore a valid architecture candidate; an "infinite-dimensional cavity" resource estimate is not.
