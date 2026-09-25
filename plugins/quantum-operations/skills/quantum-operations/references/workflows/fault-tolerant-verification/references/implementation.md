# Fault-tolerant verification: implementation reference

## 1. Circuit equivalence with MQT QCEC

API checked against MQT QCEC 3.10.0.

~~~python
from mqt.qcec import verify

result = verify(circuit_before, circuit_after)
print(result.equivalence)
~~~

Expected result for an exact verified rewrite is equivalent.

Treat not_equivalent as failure. Treat any inconclusive/unsupported result as **not proven**.

## 2. Approximate equivalence

Only use approximate checking when the algorithm specification explicitly permits approximation.

~~~python
from mqt.qcec import verify
from mqt.qcec.pyqcec import Configuration

config = Configuration()
config.functionality.check_approximate_equivalence = True
config.functionality.approximate_checking_threshold = epsilon

result = verify(
    circuit_before,
    circuit_after,
    configuration=config,
)
~~~

MQT QCEC uses projective Hilbert-Schmidt distance for this mode.

Current limitation: approximate mode is intended for fixed full-unitary circuits and is not interchangeable with parameterized/partial-equivalence workflows.

## 3. Dynamic circuits

QCEC 3.10.0 tightened dynamic-circuit preprocessing assumptions. When transform_dynamic_circuit is enabled:
- measurements after reset elimination require one-to-one qubit/classical-bit mapping;
- reset a measured qubit before reusing it as a gate target;
- supported classical conditions have restrictions.

For dynamic circuits with measurement, reset, or feed-forward, verify the classical branches and measurement maps with a checker mode that supports those semantics, and use unitary equivalence only for the unitary subregions.

## 4. Ancilla contract testing

### Clean ancilla

For small circuits, test all basis inputs and selected superpositions and verify:

~~~text
data output correct
ancilla final state = |0>
ancilla unentangled
~~~

### Dirty ancilla

Initialize the borrowed qubit in multiple basis states and random superpositions, including entanglement with a reference qubit for small tests.

After the candidate circuit:
- borrowed qubit/reference joint state must be restored;
- data result must be correct.

## 5. Detector/observable verification

For Stim/QEC circuits:
- detector annotations must be deterministic in the no-noise reference execution where expected;
- logical observables must match the intended encoded operator;
- explain unexpected DEM mechanisms using Stim error explanation tools;
- compare sampled logical outcomes to decoder predictions.

## 6. Single-fault gadget test

For an FT gadget claiming t-fault tolerance:
1. enumerate fault locations for tractable small gadgets;
2. inject all fault sets up to the claimed order;
3. propagate through syndrome/decoder;
4. verify no accepted case produces an uncorrectable logical error beyond the stated model.

For larger gadgets use structured sampling/enumeration tools, but state coverage limits.

Establish fault tolerance with the stated fault model and injected-fault tests in addition to functional circuit equivalence.

## 7. Resource regression

Persist baseline maxima/bounds:

~~~text
logical width
T/CCZ/Toffoli count
non-Clifford depth
measurement depth
QEC cycles
physical-qubit estimate
decoder memory/runtime
~~~

A rewrite that is functionally correct but violates an agreed resource ceiling fails the production regression.

Sources:
- https://mqt.readthedocs.io/projects/qcec/en/v3.10.0/
- https://github.com/quantumlib/Stim
