# Example 1: native 40Ca+ ququart as two virtual qubits

Use d=4 so one ion has four computational basis states:

~~~text
|0>_4 <-> |00>
|1>_4 <-> |01>
|2>_4 <-> |10>
|3>_4 <-> |11>
~~~

The mapping reduces two binary carriers to one physical ion only because the 40Ca+ experiments demonstrated both local qudit control and a native multiqudit entangling interaction.

Local basis rotations are synthesized from resonant 729 nm transitions. The native two-qudit light-shift gate is:

~~~text
G(theta)|jj> = |jj>
G(theta)|jk> = exp(i theta)|jk>, j != k
~~~

For a compiler, represent a logical operation on the two packed virtual qubits as a 4x4 unitary U. Compile U into the experimentally available single-qudit rotations. Inter-ion interactions are lowered into G(theta) plus local qudit rotations.

Resource record:

~~~text
binary baseline:
  carriers: 2 ions per two virtual qubits

ququart:
  carriers: 1 ion per two virtual qubits
  local dimension: 4
  local-control cost: qudit pulse sequence
  inter-carrier primitive: native G(theta)
  measured G(theta) fidelity at d=4: about 97.0% in the 2023 experiment
~~~

Use this as a fully demonstrated carrier-level width reduction mechanism, then compare total pulse depth and error against the qubit encoding.
