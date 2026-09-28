# Example: high-rate permutation gates and Reed-Muller teleportation

## A. [[16,6,4]] permutation logical operation

The neutral-atom architecture reports logical entangling operations within a high-rate [[16,6,4]] block that can be realized through physical-qubit re-indexing for supported code automorphisms.

~~~text
candidate_permutation = pi on physical indices
logical_map = induced_logical_clifford(pi)

if logical_map == requested_map:
    emit BlockPermute(pi)
else:
    retain explicit logical-gate implementation
~~~

Verification must compute or import the exact induced logical map. Code parameters alone are not enough.

Cost: compiler relabeling can have zero quantum-entangling cost; any required physical movement is hardware-dependent and must be counted separately.

## B. [[15,1,3]] Reed-Muller transversal-teleportation pattern

Bluvstein et al. use 3D [[15,1,3]] Reed-Muller logical resources, logical CZ interactions, X-basis logical measurements, and software feed-forward for transversal-teleportation unitary synthesis.

~~~text
prepare required RM logical resource block(s)
apply documented logical CZ layer(s)
perform documented X-basis logical measurement(s)
decode measurement outcomes
apply/track documented byproduct
logical information continues on destination block
release measured resource/source block
~~~

Resource accounting includes encoded resource-state preparation, physical implementation of logical CZ, all measurements, decoding/feed-forward, reset/reuse, and code-switching/interface costs.

Do not replace this with a generic fixed physical gate count for a logical gate unless the exact paper protocol and logical-basis mapping have been instantiated and verified.