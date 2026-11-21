# Executable example: CNOT propagation of a logical Pauli frame

**Definition.** Represent logical Pauli corrections by binary `x,z` bits and propagate them through Clifford CNOT without inserting physical correction gates. Verify the update against explicit matrix conjugation.

Run: `pip install numpy`.

~~~python
from itertools import product
import numpy as np

X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
U = np.zeros((4, 4), dtype=complex)  # CNOT q0 -> q1 (q0 is LSB)
for basis in range(4):
    U[basis ^ (2 if basis & 1 else 0), basis] = 1

def pauli(xc, xt, zc, zt):
    pc = np.linalg.matrix_power(X, xc) @ np.linalg.matrix_power(Z, zc)
    pt = np.linalg.matrix_power(X, xt) @ np.linalg.matrix_power(Z, zt)
    return np.kron(pt, pc)

def propagate(xc, xt, zc, zt):
    return xc, xt ^ xc, zc ^ zt, zt

for bits in product((0, 1), repeat=4):
    assert np.allclose(U @ pauli(*bits) @ U.conj().T, pauli(*propagate(*bits)))
assert (1 ^ 1) == 0  # a raw Z measurement bit flips under an X frame
print("all 16 Pauli-frame CNOT cases pass")
~~~

**Primary description:** https://qiskit.qotlabs.org/learning/courses/foundations-of-quantum-error-correction/stabilizer-formalism/stabilizer-codes

**Contract:** Track both Pauli components and, for Clifford frames beyond pure Pauli tracking, the appropriate additional frame metadata. Decode measurement outcomes using the corresponding anticommution rule before dependent feed-forward.
