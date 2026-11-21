# Executable example: peephole cancellation and unitary equality

**Definition.** Apply a documented pytket compilation pass to a unitary circuit, compare the before/after unitary and count two-qubit operations. Preserve logical output permutations when exporting.

Run: `pip install pytket numpy`.

~~~python
import numpy as np
from pytket.circuit import Circuit
from pytket.passes import FullPeepholeOptimise

c = Circuit(2)
c.CX(0, 1)
c.CX(0, 1)
baseline = c.get_unitary()
before = c.n_gates

FullPeepholeOptimise().apply(c)
assert np.allclose(baseline, c.get_unitary())
assert c.n_gates < before
print("pytket verified gate reduction:", before, "->", c.n_gates)
~~~

**Primary official documentation:** https://docs.quantinuum.com/tket/user-guide/examples/circuit_compilation/compilation_example.html

**Verification:** Evaluate after applying the selected pass. For general circuits, also inspect and restore any implicit qubit permutation before exchanging IR with software that cannot represent it.
