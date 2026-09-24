# Clifford+T optimization: implementation reference

## Cost record

For every candidate maintain:

~~~text
logical_qubits
T_count
T_depth
Toffoli_count
CCZ_count
arbitrary_rotation_count + precision
measurement_depth
Clifford_2q_count
factory_consumption_timeline
~~~

Do not optimize only T_count.

## Exact Toffoli versus phase-relaxed constructions

A standard exact Clifford+T Toffoli decomposition is commonly costed at 7 T gates.

A relative-phase Toffoli can use fewer T gates, commonly 4 T, while implementing the same classical permutation with additional basis-state-dependent phases.

Therefore a relative-phase replacement is legal only when one of these is proved:

1. the phase is globally irrelevant;
2. the relative phase cancels with a paired inverse/compute-uncompute structure;
3. a surrounding phase-polynomial proof shows exact cancellation;
4. the target semantic specification explicitly permits the phase relation.

A computational-basis truth table is **not** sufficient proof.

## Safe paired-compute pattern

Suppose R implements a Boolean compute map with phase:

~~~text
R |x,0> = exp(i*phi(x)) |x,f(x)>
~~~

If the middle operation V does not disturb the information required by the inverse and the exact inverse R^dagger is applied:

~~~text
R
V
R^dagger
~~~

the phase introduced by R cancels through the exact inverse.

Do not substitute a different approximate/phase-relaxed inverse without proving cancellation.

## Temporary logical AND

For AND-like temporaries, load:
reversible-arithmetic/references/examples/temporary-logical-and.md

That pattern uses 4 T forward and a measurement-assisted 0-T erase, but only under its measurement/feed-forward preconditions.

## Pauli-rotation representation

Before synthesizing each rotation independently, represent a commuting region as:

~~~text
exp(-i theta_j P_j / 2)
~~~

for Pauli strings P_j.

Operations with commuting Pauli strings may be reordered. Equal Pauli strings combine:

~~~text
R_P(alpha) R_P(beta) = R_P(alpha+beta)
~~~

Normalize angles modulo the representation exact periodicity before synthesis.

## Rotation error allocation

Given algorithmic synthesis error budget epsilon_synth and m independently synthesized rotations, a conservative equal allocation is:

~~~text
epsilon_i <= epsilon_synth / m
~~~

under a triangle-inequality-style bound.

If a tighter composition theorem/tool is used, state it explicitly. Never silently select a synthesis precision.

## Factory-aware scheduling

Convert each non-Clifford operation into the magic-state interface actually selected by magic-state-factories:

~~~text
T layer -> T-state requests
CCZ gadget -> CCZ-state request
catalyzed rotation -> catalyst + input-state requirements
~~~

Produce a timestamped consumption trace. T-depth reduction that creates a larger burst may require more factories/buffer.

## Verification

For each rewrite:
- exact QCEC/PyZX equivalence when supported;
- explicit phase-polynomial proof for phase-relaxed replacements;
- statevector comparison on small circuits including superpositions;
- resource counts before/after;
- factory timeline comparison;
- reject a candidate if exact semantics are not proved.
