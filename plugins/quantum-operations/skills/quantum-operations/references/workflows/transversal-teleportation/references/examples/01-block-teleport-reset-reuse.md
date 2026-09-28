# Example: block teleportation with reset/reuse

Goal: move encoded logical information from active block A to fresh block B and make A physically reusable.

## Protocol template

~~~text
precondition:
  A contains encoded logical state
  B is prepared in the protocol-required fresh encoded state

1. apply the code's documented transversal/logical entangling layer A <-> B
2. measure A in the protocol-required basis
3. decode A's logical measurement result
4. derive the logical Pauli/Clifford byproduct on B
5. update B's software frame, or materialize the correction if required
6. declare A logically dead
7. reset / re-cool / reinitialize A
8. return A to fresh-block pool
~~~

For an n-carrier CSS block, a common transversal entangling pattern is one two-qubit gate between each corresponding carrier. This is a template, not a universal teleportation circuit; instantiate the code's exact source protocol.

## Compiler checks

~~~text
assert logical_state_location_after == B
assert A has no remaining logical consumer
assert byproduct_resolved_before_dependent_nonclifford
assert reset(A) precedes reuse(A)
~~~

## Resource fields

~~~text
fresh_blocks_peak += 1
transversal_2q_layer += 1
measurements += physical_measurements_of_A
reset_events += physical_carriers_of_A
decoder_job += logical_measurement_decode
~~~

The neutral-atom architecture in Bluvstein et al. uses this pattern to propagate logical information onto fresh encoded blocks while physical errors remain on the previous block, enabling reset/reuse and constant-entropy deep computation.