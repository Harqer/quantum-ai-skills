# Toric-code architecture: implementation reference

This reference turns a toric-code label into a reproducible QEC candidate.

## 1. Fundamental 2D code

For a square L by L torus with one qubit on each edge:

~~~text
data qubits: n = 2 L^2
encoded logical qubits: k = 2
distance: d = L
vertex checks: L^2, with one global dependency
plaquette checks: L^2, with one global dependency
independent stabilizers: 2 L^2 - 2
~~~

Use the standard convention

~~~text
A_v = product of X_e over edges e incident to vertex v
B_p = product of Z_e over edges e in boundary of plaquette p
~~~

so every A_v and B_p overlap on zero or two edges and commute.

A CSS representation stores binary matrices Hx and Hz with:

~~~text
Hx @ Hz.T == 0 mod 2
rank_GF2(Hx) = L^2 - 1
rank_GF2(Hz) = L^2 - 1
k = 2 L^2 - rank(Hx) - rank(Hz) = 2
~~~

The direct construction is worked in `examples/01-square-lattice-css.md`.

## 2. Homology and logical failure

Represent X- and Z-type Pauli errors as edge chains. The syndrome is the boundary/coboundary of those chains. A recovery R for error E is valid when:

~~~text
syndrome(E * R) = 0
~~~

but it is successful only when:

~~~text
homology(E * R) = trivial
~~~

Equivalently, the residual operator must commute with all logical Pauli representatives. For the two torus cycles, keep an explicit canonical basis:

~~~text
X1, Z1
X2, Z2
~~~

with each Xi anticommuting only with Zi and commuting with the other logical pair.

This distinction is mandatory in every decoder example and regression test.

## 3. Noise layers

### Code-capacity

Perfect check measurements and Pauli data noise. Use this layer for:
- decoder mechanics;
- homology tests;
- ideal thresholds;
- biased-noise comparisons.

### Phenomenological

At every round:
- data errors occur;
- reported syndrome bits can flip;
- decoding is performed on a space-time graph.

Use enough rounds to match the benchmark protocol and state the terminal/boundary treatment.

### Circuit-level

Instantiate:
- check ancilla preparation;
- ordered entangling gates;
- measurement;
- reset;
- data/ancilla idle locations;
- leakage/correlated noise when relevant;
- cycle time and decoder deadline.

The check ordering is part of the protocol because ancilla faults can propagate through the four-body measurement circuit.

## 4. Decoder selection

Keep a decoder record:

~~~text
decoder:
  algorithm
  noise layer
  edge/prior weights
  X/Z correlation handling
  degeneracy handling
  measurement-error handling
  complexity
  mean_latency
  p99_latency
  p99_9_latency
  throughput
  logical_error_curve
  confidence_intervals
~~~

Candidate families include:
- MWPM / weighted MWPM;
- union-find / weighted union-find;
- symmetry-aware matching for biased noise;
- tensor-network / maximum-likelihood approximations;
- renormalization decoders;
- belief propagation plus matching;
- local cellular automata;
- neural/high-level decoders.

A larger threshold is one metric. Runtime, memory, tail latency, parallelizability, model mismatch, and subthreshold scaling remain separate.

## 5. Syndrome measurement primitive

For a Z-type check measured by an ancilla initialized in |0>, apply CNOT(data -> ancilla) from every supported data qubit and measure the ancilla in Z. For an X-type check, initialize the ancilla in |+>, apply CNOT(ancilla -> data), and measure in X. A production round schedules all checks conflict-free and validates fault propagation.

The exact Stim primitive is in `examples/11-syndrome-measurement-circuit.md`.

## 6. Biased-noise toric variants

When pZ, pX, and pY are strongly asymmetric, compare:
- ordinary toric code with weighted decoding;
- XZZX or Clifford-deformed toric code;
- generalized toric constructions tailored to the bias.

Record the bias convention, deformation, effective distance, decoder, and noise layer. PanQEC exposes XZZX/XY deformations on Toric2DCode and is used in `examples/06-biased-noise-xzzx.md`.

## 7. Higher dimensions

### 3D toric code

A periodic cubic implementation may place qubits on edges, with point-like and loop-like syndrome structures for the two Pauli sectors. Decoder asymmetry is therefore expected. PanQEC's Toric3DCode uses weight-six vertex and weight-four face checks and exposes SweepMatchDecoder for the corresponding X/Z decoder split.

Use 3D subsystem toric code as a distinct candidate when single-shot QEC with noisy measurements is required. Its low-weight gauge checks and single-shot decoder are a different architecture from ordinary periodic 3D toric code.

### 4D toric code

Use only with explicit four-dimensional or effectively emulated connectivity. Carry self-correction and transversal-gate claims together with their lattice assumptions. A 4D result is not evidence for 2D hardware.

## 8. Periodic-boundary hardware cost

The toric code's logical model is geometrically local on a torus. A planar chip must realize the periodic seams through one of:
- native wrap-around couplers;
- multilayer routing;
- qubit movement;
- teleportation/modular links;
- long-range gates;
- an embedding with explicit additional routing.

Record seam-edge count, added error, extra ancillas, interaction distance, routing layers, and cycle stretch. If the target hardware cannot realize periodic seams efficiently, compare against an open-boundary surface-code candidate instead of silently assuming a torus.

## 9. Resource comparison

For every candidate report:

~~~text
logical:
  k
  distance
  logical operation interface

physical:
  data qubits
  check ancillas
  routing/communication ancillas
  total peak qubits

qec:
  check weights
  syndrome layers
  cycle time
  rounds
  decoder

runtime:
  detector rate
  decoder latency distribution
  stalls/deadlines
  wall clock

reliability:
  noise model
  p_L per round/location
  confidence interval
  total failure budget
~~~

The ordinary 2D toric code has n=2L^2 data qubits for k=2, but a full hardware result additionally includes check ancillas and whatever implements periodic connectivity.

## 10. Verification

Minimum checks:
- Hx Hz^T = 0 mod 2;
- rank gives k=2 for the square torus;
- all stabilizers commute;
- logical pairs have the expected symplectic commutation;
- a single-edge Pauli creates the expected pair of defects;
- every local correction clears the expected syndrome;
- a noncontractible residual loop is detected as a logical error;
- Monte Carlo results include shots, failures, confidence interval and seed/version metadata;
- phenomenological/circuit-level experiments preserve their time-boundary assumptions;
- resource estimates include seam/routing cost.

## 11. Tool API policy

Examples are tied to the API/source version stated in `references/tools.md`. Re-check current upstream APIs before production use. PanQEC and PyMatching examples are preferred for active decoder work; qecsim examples are retained because they expose toric geometry and homology mechanics very clearly, but qecsim 1.0b9 is an older reference implementation.
