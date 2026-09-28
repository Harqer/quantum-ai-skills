# Example: transversal CNOT with correlated decoding

Assume the selected CSS code has a documented transversal logical CNOT from block C to block T.

## Physical layer

~~~text
for i in physical_carriers:
    CNOT C[i] -> T[i]
~~~

Apply this only after verifying the induced logical map for the selected code.

## Fault propagation

~~~text
X on control: X_c -> X_c X_t
Z on target:  Z_t -> Z_c Z_t
~~~

Therefore decoding the two blocks independently can discard useful correlation information.

## Decoder-window record

~~~text
window:
  blocks = [C, T]
  operations = [transversal_CNOT]
  detectors_before = ...
  detectors_after = ...
  propagated_correlations = [X_control_to_target, Z_target_to_control]
  deadline = first dependent logical event
~~~

Build the decoding graph over the selected window and propagate the decoded logical frame into subsequent operations.

## Verification

Inject every single-fault location in a small instance or simulator-supported code model and verify detector propagation, decoded logical frame, and feed-forward timing.

Do not generalize a reduced QEC-round cadence from one code/distance/noise model to another without evidence.