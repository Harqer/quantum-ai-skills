# Executable example: share one nonlinear product

**Definition.** Compute a Boolean product once, reuse it for two XOR outputs, then restore the clean temporary. Inputs are basis bits `x,y`; outputs are `o1 ^= x&y`, `o2 ^= x&y`. The ancilla begins and ends in `|0>`.

Run: `pip install "qiskit>=2,<3"`, then execute this Python block.

~~~python
from itertools import product
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

c = QuantumCircuit(5)
c.ccx(0, 1, 2)  # compute shared nonlinear product in clean ancilla
c.cx(2, 3)       # reuse
c.cx(2, 4)
c.ccx(0, 1, 2)  # uncompute

assert c.count_ops()["ccx"] == 2
for x, y, o1, o2 in product(range(2), repeat=4):
    inp = x | (y << 1) | (o1 << 3) | (o2 << 4)
    expected = x | (y << 1) | ((o1 ^ (x & y)) << 3) | ((o2 ^ (x & y)) << 4)
    result = Statevector.from_int(inp, 2**5).evolve(c)
    assert abs(result.data[expected] - 1) < 1e-12
print("all 16 cases pass; scratch qubit restored")
~~~

The unfused implementation computes each product in its own temporary, requiring four CCX calls rather than two. Count the clean-ancilla overhead and actual synthesis costs before selecting the fusion for a hardware target.

**Primary API:** https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit

**Verification:** Exhaustive basis mapping; the circuit's linearity extends the exact mapping to all superpositions with the same clean-ancilla precondition.
