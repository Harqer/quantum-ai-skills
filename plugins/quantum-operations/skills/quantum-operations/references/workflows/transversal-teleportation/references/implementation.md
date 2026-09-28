# Transversal teleportation: implementation reference

## IR

~~~text
Block:
  id
  code
  code_parameters
  physical_qubits[]
  logical_qubits[]
  status: active | fresh | measured | resettable | resetting
  frame
  error_budget

LogicalOp:
  id
  logical_map
  blocks[]
  transversal_protocol?
  permutation_protocol?
  teleportable
  fresh_blocks_required
  measurements[]
  decoder_window?
  byproduct_rule?
  reset_release[]
  physical_resources
~~~

## Transversal legality

A physical transversal layer is legal only when all are known: the selected code/logical basis, the physical gate on corresponding carriers, the induced logical operator, propagated fault support, and the decoder/noise model for that layer.

Record physical_layer -> logical_map and verify it from stabilizers/logical operators or an authoritative code construction.

## Teleportation boundary

~~~text
prepare fresh destination block
apply documented logical entangling layer
measure source block in documented basis
decode logical measurement
derive logical byproduct
update software frame or materialize correction
mark source resettable
reset/re-cool/reinitialize source
return source to fresh-block pool
~~~

The old block is released only after the logical result no longer depends on its coherent state.

## Constant-entropy scheduling

Maintain a block-local error/entropy budget derived from the selected physical model. Insert syndrome extraction or logical teleportation according to a validated code/hardware policy. If only a relative score exists, label it heuristic and preserve a fixed-cadence baseline.

## Correlated decoding window

For transversal CNOT, model X_control -> X_control X_target and Z_target -> Z_control Z_target. Decoder windows must span the detector events needed to infer these correlations. Claims of O(1)-style QEC cadence require the specific decoder/protocol and matching code/noise regime.

## Frame tracking

Keep decoded Pauli byproducts in software while subsequent operations remain inside the supported frame group. At non-Clifford boundaries, materialize the correction, extend to a Clifford frame, or consume it through an explicit teleportation/injection protocol.

## Permutation logical gates

For code automorphism pi, compute the induced logical Clifford map L(pi). Replace a gate network by re-indexing only when L(pi) equals the requested logical map. Pure compiler relabeling has zero quantum-gate cost; physical motion is costed separately when required by hardware.

## Fresh-block pool

Track fresh_available(t), active_blocks(t), measuring_blocks(t), and resetting_blocks(t). A teleport consumes a fresh destination, releases the measured source after byproduct resolution, then returns the reset/re-cooled/reinitialized source to the fresh pool.

A one-fresh-block rolling schedule minimizes width but can serialize execution. Retain wider schedules when extra fresh blocks reduce runtime or idle exposure.

## Measurement-assisted temporary disposal

For a temporary t=f(x) used only through a protocol permitting X-basis disposal: complete the desired data operation, X-measure t, derive the phase/byproduct on source data, prove the byproduct lies in the tracked frame or materialize it, then reset/reuse t.

Classical truth-table equality is insufficient if disposal changes relative phase. Verify the quantum map by stabilizer, phase-polynomial, exact equivalence, or small-statevector proof.

## Resource record

~~~text
persistent_data_blocks
peak_fresh_blocks
peak_physical_qubits_or_atoms
transversal_2q_layers
physical_2q_count
permutation_logical_ops
measurement_count
reset_count
qec_rounds
decoder_windows
decoder_work
feedforward_stall
movement_time
T_count / CCZ_count / injected_resources
logical_failure_budget
wall_clock_runtime
~~~

## Verification

- logical map before/after optimization is identical;
- logical operators/stabilizers transform as expected;
- every measured block is dead after its protocol boundary;
- every released block is reset before reuse;
- frame updates reproduce explicit corrections;
- decoder windows include modeled propagated correlations;
- resource accounting includes preparation, measurement, reset, movement, and classical stalls;
- empirical claims stay inside the source code, distance, error model, and timing regime.