# Example 10: qutrit toric code on qubit hardware is not carrier compression

The 2025 Z3 toric-code experiment used Quantinuum H2 and prepared up to 24 qutrits.

Critical representation:

~~~text
one logical qutrit = two physical qubits
three used binary states = qutrit basis
fourth binary state = leakage/heralding subspace
~~~

Therefore:

~~~text
24 qutrits -> 48 physical qubits
~~~

for the encoding used in that experiment.

The unused fourth state provides leakage detection: preparation events that leave the qutrit subspace can be heralded.

Use this experiment for:
- generalized Pauli and Z3 toric-code semantics.
- qutrit defect and parafermion protocols.
- encoded-qudit algorithm validation.

Do not use it as evidence that native qutrit hardware halves physical carrier count, because the experiment deliberately encoded every qutrit into two qubits.
