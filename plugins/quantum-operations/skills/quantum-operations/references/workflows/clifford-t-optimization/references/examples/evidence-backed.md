# Executable example: exact Toffoli-to-Clifford+T synthesis

**Definition.** Expand an exact CCX into its documented Clifford+T decomposition, verify unitary equivalence, and count the non-Clifford operations before comparing alternative syntheses.

Run: `pip install "qiskit>=2,<3"`.

~~~python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator

original = QuantumCircuit(3)
original.ccx(0, 1, 2)
synthesized = original.decompose(reps=2)
allowed = {"h", "s", "sdg", "t", "tdg", "cx", "id"}
assert set(synthesized.count_ops()).issubset(allowed), synthesized.count_ops()
assert Operator(original).equiv(Operator(synthesized))
t_count = synthesized.count_ops().get("t", 0) + synthesized.count_ops().get("tdg", 0)
assert t_count > 0
print("T-count:", t_count, "two-qubit gates:", synthesized.count_ops().get("cx", 0))
~~~

**Primary API:** https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.CCXGate

**Compilation:** This provides a correctness-checked exact baseline; optimize T count or T-depth only against another exactly equivalent candidate with the same ancilla and phase contracts. A cost decrease requires comparing measured counts of both candidates; exact synthesis alone is not an improvement claim.
