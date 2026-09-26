# Toric-code tool references

API/source status checked September 2026.

## PanQEC

Repository: https://github.com/panqec/panqec

Use for current code-capacity studies across:
- `Toric2DCode`;
- `Toric3DCode`;
- `MatchingDecoder`;
- `UnionFindDecoder`;
- `SweepMatchDecoder`;
- Pauli error models;
- XZZX/XY toric deformations.

The implementation/examples were checked against repository commit `13886d8f598579f6971707bccdf1f4e2be4607a3`.

## PyMatching

Repository: https://github.com/oscarhiggott/PyMatching
Documentation: https://pymatching.readthedocs.io/

The upstream toric-code notebook constructs the square toric CSS parity-check matrix from two cyclic repetition-code matrices and uses `Matching(H)` for code capacity and `Matching(H, repetitions=T)` for repeated syndrome data. The repository example was checked at commit `6f63b2b9474ba0fa7e511fe52bffdce858a06984`.

## qecsim

Repository: https://github.com/qecsim/qecsim
Documentation: https://qecsim.github.io/

qecsim 1.0b9 includes:
- `ToricCode(rows, columns)`;
- `ToricMWPMDecoder`;
- `RotatedToricCode`;
- `RotatedToricSMWPMDecoder`;
- biased/depolarizing Pauli models;
- `app.run` and `app.run_ftp`.

Use it for transparent toric geometry, Pauli paths, homology/logical-success demonstrations, and its rotated-toric phenomenological workflow. Treat it as a reference/teaching simulator rather than assuming it is the preferred current production stack.

## Stim

Repository: https://github.com/quantumlib/Stim

Use Stim for explicit stabilizer measurement circuits, detector annotations, repeated syndrome extraction, circuit-level Pauli noise, and high-throughput sampling when the desired toric circuit is provided explicitly. Stim's generated-code catalog is surface/repetition oriented; construct the periodic toric circuit rather than relabeling a generated planar surface-code circuit.

## Cirq toric-code tutorial

https://quantumai.google/cirq/experiments/toric_code

Use as an experimental/state-preparation reference for toric ground-state construction, topological entanglement and anyon operations. It accompanies the 2021 Google Quantum AI toric-code experiment.

## IBM/Qiskit learning reference

https://qiskit.qotlabs.org/learning/courses/foundations-of-quantum-error-correction/quantum-code-constructions/toric-code

Use for a current independent derivation of toric stabilizers, logical loops, syndromes and shortest-path recovery. It is conceptual documentation, not the production simulator selected by this workflow.
