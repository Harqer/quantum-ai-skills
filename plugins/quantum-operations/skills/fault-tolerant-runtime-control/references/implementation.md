# Fault-tolerant runtime control: implementation reference

## Pauli-frame representation

For n logical qubits, represent a Pauli correction frame (ignoring global phase) with two n-bit vectors:

~~~text
x[i] = 1 if X component present on logical qubit i
z[i] = 1 if Z component present on logical qubit i
~~~

The current frame is:

~~~text
P = product_i X_i^x[i] Z_i^z[i]
~~~

## Clifford propagation rules

When propagating the current Pauli frame forward through a Clifford gate U, update according to U P U^dagger.

### H on qubit q

~~~python
x[q], z[q] = z[q], x[q]
~~~

because H X H = Z and H Z H = X.

### S on qubit q

~~~python
z[q] ^= x[q]
~~~

because S X S^dagger is XZ up to phase and S Z S^dagger = Z.

### CNOT(control=c, target=t)

~~~python
x[t] ^= x[c]
z[c] ^= z[t]
~~~

because:

~~~text
X_c -> X_c X_t
X_t -> X_t
Z_c -> Z_c
Z_t -> Z_c Z_t
~~~

These rules are exact for Pauli-frame tracking up to global phase.

## Measurement interpretation

Let the physical/raw binary result be m_raw, encoded as 0 for +1 eigenvalue and 1 for -1 eigenvalue.

### Z measurement on q

An X component anticommutes with Z, so:

~~~python
m_logical = m_raw ^ x[q]
~~~

### X measurement on q

A Z component anticommutes with X:

~~~python
m_logical = m_raw ^ z[q]
~~~

### General Pauli measurement

Represent measured Pauli M by binary vectors x_m, z_m.

The frame flips the measurement outcome iff P and M anticommute:

~~~text
flip =
  dot(x, z_m)
  XOR
  dot(z, x_m)
  mod 2

m_logical = m_raw XOR flip
~~~

This symplectic inner product is the implementation rule for arbitrary Pauli-product measurement reinterpretation.

## Example

Start with two-qubit frame:

~~~text
x = [1, 0]
z = [0, 1]
~~~

Propagate through CNOT 0 -> 1:

~~~text
x[1] ^= x[0]  => x = [1, 1]
z[0] ^= z[1]  => z = [1, 1]
~~~

A subsequent raw Z measurement on qubit 0 must be flipped because x[0] = 1.

## Clifford-frame boundary

A Pauli frame is closed under Clifford gates.

A non-Clifford operation such as T can map an existing Pauli correction into a non-Pauli correction. When that occurs, choose one explicit strategy:

1. materialize the required Clifford correction;
2. extend the software frame to a Clifford frame;
3. use a teleportation/injection protocol whose byproduct rules are explicitly tracked.

Do not continue applying Pauli-only update rules through a non-Clifford gate when the frame is no longer Pauli.

## Measurement-assisted cleanup

For temporary logical-AND cleanup, load:
reversible-arithmetic/references/examples/temporary-logical-and.md

The controller must:
- receive the measurement bit;
- derive the required Clifford byproduct;
- apply or track it;
- only then mark the measured ancilla resettable/reusable.

## Feed-forward deadline

For every measurement-dependent event record:

~~~text
measurement_complete_time
decoder_complete_time
frame_update_complete_time
dependent_quantum_event
latest_safe_start
~~~

The available classical-control budget is:

~~~text
deadline =
  dependent_quantum_event.latest_safe_start
  - measurement_complete_time
~~~

The decoder/controller path is feasible only if its required completion time meets that deadline or the runtime scheduler inserts an allowed stall.

## Tests

For frame code:
1. generate random Pauli frames on small n;
2. propagate with the software rules;
3. independently conjugate the Pauli operator by the Clifford circuit;
4. compare resulting Pauli operators up to global phase;
5. test measurement reinterpretation for X, Z, and random Pauli strings;
6. test non-Clifford boundaries explicitly rather than allowing silent Pauli-frame continuation.
