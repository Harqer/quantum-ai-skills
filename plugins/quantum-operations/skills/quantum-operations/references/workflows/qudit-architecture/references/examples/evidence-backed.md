# Executable example: exact two-qubit encoding in a ququart

**Definition.** A native `d=4` carrier can encode the four computational basis states `|00>, |01>, |10>, |11>`. An encoding map and gate compilation must preserve the logical truth table and unitarity.

Run: `pip install numpy`.

~~~python
import numpy as np

I4 = np.eye(4, dtype=complex)
# Two virtual qubits: high bit is control, low bit is target.
native_cnot = I4.copy()
native_cnot[2, 2] = native_cnot[3, 3] = 0
native_cnot[2, 3] = native_cnot[3, 2] = 1

assert np.allclose(native_cnot.conj().T @ native_cnot, I4)
for bits in range(4):
    encoded = np.eye(4, dtype=complex)[:, bits]
    decoded = native_cnot @ encoded
    expected = bits ^ (bits & 2 != 0)
    assert np.allclose(decoded, I4[:, expected])
print("four-level virtual CNOT unitary and basis map verified")
~~~

**Published native multilevel entangler:** https://www.nature.com/articles/s41467-023-37375-2

**Verification boundary:** This is the executable *logical encoding and matrix* reference. The published experiment establishes a native `d<=5` two-qudit entangling primitive; pulse-level lowering must use the specific hardware's native gate basis, calibration and measured leakage/error rates. Count physical carriers separately from pulse depth and physical error.
