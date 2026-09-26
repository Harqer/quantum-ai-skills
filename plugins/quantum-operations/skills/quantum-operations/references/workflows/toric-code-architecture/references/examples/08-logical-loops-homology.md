# Example 8: noncontractible loops and hidden logical failure

This example demonstrates the central toric-code invariant: a noncontractible Pauli loop has zero syndrome but acts logically.

~~~python
import numpy as np
from qecsim import paulitools as pt
from qecsim.models.toric import ToricCode

code = ToricCode(5, 5)

# qecsim supplies canonical noncontractible logical strings.
logical_loop = code.new_pauli().logical_x1().to_bsf()

# A logical loop commutes with every stabilizer.
syndrome = pt.bsp(logical_loop, code.stabilizers.T)
assert not syndrome.any()

# But it has nontrivial logical commutation.
logical_signature = pt.bsp(logical_loop, code.logicals.T)
assert logical_signature.any()

print("syndrome:", syndrome)
print("logical signature:", logical_signature)
~~~

Interpretation:

~~~text
open error string
    -> two endpoint defects
decoder joins defects
    -> error * recovery becomes a closed loop
contractible closed loop
    -> stabilizer, success
noncontractible closed loop
    -> logical operator, failure
~~~

This is why every toric decoder test must check the logical class of the residual, not only its syndrome.

Source:
https://github.com/qecsim/qecsim/blob/24d6b8a320b292461b66b68fe4fba40c9ddc2257/src/qecsim/models/toric/_toriccode.py
