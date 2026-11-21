# Executable example: exact Toffoli-to-Clifford+T synthesis

**Definition.** Implement an exact CCX using an explicit seven-T Clifford+T circuit, verify unitary equivalence, and count the non-Clifford operations before comparing alternative syntheses.

Run: `pip install "qiskit>=2,<3"`.

~~~python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator

original = QuantumCircuit(3)
original.ccx(0, 1, 2)

exact = QuantumCircuit(3)
exact.h(2)
exact.cx(1, 2)
exact.tdg(2)
exact.cx(0, 2)
exact.t(2)
exact.cx(1, 2)
exact.tdg(2)
exact.cx(0, 2)
exact.t(1)
exact.t(2)
exact.h(2)
exact.cx(0, 1)
exact.t(0)
exact.tdg(1)
exact.cx(0, 1)

assert Operator(original).equiv(Operator(exact))
assert set(exact.count_ops()) == {"h", "cx", "t", "tdg"}
t_count = exact.count_ops()["t"] + exact.count_ops()["tdg"]
assert t_count == 7
assert exact.count_ops()["cx"] == 6
print("Exact Clifford+T decomposition verified; T-count:", t_count)
~~~

**Primary API:** https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.CCXGate

**Compilation:** This provides a correctness-checked exact baseline; optimize T count or T-depth only against another exactly equivalent candidate with the same ancilla and phase contracts. A cost decrease requires comparing measured counts of both candidates; exact synthesis alone is not an improvement claim.
