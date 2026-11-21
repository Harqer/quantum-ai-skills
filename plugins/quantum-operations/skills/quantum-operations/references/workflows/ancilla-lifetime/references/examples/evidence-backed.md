# Executable example: compute, consume, uncompute

**Definition.** Reuse a clean ancilla only after the original input-dependent temporary has been uncomputed. Inputs: control bits `a,b`, output `o`, scratch initialized to zero. Outputs: `o ^= a&b`; `a,b` unchanged and scratch returned to zero.

Run: `pip install "qiskit>=2,<3"`, then execute:

~~~python
from itertools import product
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

q = QuantumCircuit(4)
q.ccx(0, 1, 2)  # allocate and compute scratch
q.cx(2, 3)       # consume scratch into output
q.ccx(0, 1, 2)  # uncompute before release

for a, b, o in product(range(2), repeat=3):
    initial = a | (b << 1) | (o << 3)  # scratch qubit 2 = 0
    final = a | (b << 1) | ((o ^ (a & b)) << 3)
    result = Statevector.from_int(initial, 16).evolve(q)
    assert abs(result.data[final] - 1) < 1e-12
print("scratch restored for every valid input")
~~~

**Primary API:** https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit

**Verification boundary:** The contract requires a **clean** scratch qubit. Equivalence is checked over the valid clean-ancilla input subspace, rather than incorrectly asserting equality for arbitrary dirty ancillas. At allocation, record first use; at release, require a restoration proof.
