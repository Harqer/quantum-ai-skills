# Transversal teleportation: research basis

Primary sources used by this workflow:

1. D. Bluvstein et al., A fault-tolerant neutral-atom architecture for universal quantum computation, Nature 649 (2026), published online 2025. DOI: https://doi.org/10.1038/s41586-025-09848-5
   - transversal logical gates and logical teleportation;
   - logical information propagated to fresh encoded blocks while physical errors remain on old blocks;
   - mid-circuit reset/re-cooling/reinitialization and reuse;
   - high-rate [[16,6,4]] experiments and permutation CNOTs by physical-qubit re-indexing;
   - [[15,1,3]] Reed-Muller resources and transversal-teleportation unitary synthesis;
   - software feed-forward / frame handling.

2. N. Cain et al., Fast correlated decoding of transversal logical algorithms, arXiv:2505.13587.
   - correlated decoder windows that follow propagated logical products through transversal circuits;
   - reduced decoding problem size and fault-tolerant correlated decoding;
   - source-specific assumptions are required before transferring reduced-QEC-cadence claims.

3. H. Zhou et al., Resource Analysis of Low-Overhead Transversal Architectures for Reconfigurable Atom Arrays, arXiv:2505.15907.
   - system-level resource models for transversal architectures;
   - magic-state factories, arithmetic units, and lookup tables;
   - interaction-distance, atom-movement, and correlated-decoding-volume optimization.

4. Logical qubits with erasure conversion using metastable neutral atoms, Nature Physics (2026). DOI: https://doi.org/10.1038/s41567-026-03309-0
   - mid-circuit erasure information;
   - conditional logical teleportation between code blocks;
   - leakage/erasure-aware block selection.

## Transfer rules

- The [[16,6,4]] permutation-CNOT observation does not imply arbitrary logical CNOTs are free.
- A transversal gate for one code does not imply the same gate is transversal for another code.
- Fresh-block teleportation removes accumulated physical entropy only under the complete measurement/decoding/reset protocol.
- Reduced syndrome-round claims require the cited correlated-decoding method and matching code/noise assumptions.
- Reed-Muller teleportation examples do not eliminate resource-state preparation, measurement, decoding, feed-forward, or code-switching costs.
- Report physical two-qubit gates separately from logical gate counts.